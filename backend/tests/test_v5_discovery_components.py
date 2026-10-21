import asyncio, json
from urllib.parse import parse_qs, urlparse
import pytest
from app.scope import ScopePolicy
from app.http_client import HTTPObservation
from app.crawler import Crawler
from app.api_discovery import APIDiscovery
from app.parameter_probes import probe_reflected_query_inputs
from app.checks.network_checks import inspect_tls


def obs(url, body='', status=200, headers=None, content_type='text/html'):
    from hashlib import sha256
    body=str(body)
    return HTTPObservation(url,url,status,{k.lower():v for k,v in (headers or {}).items()},body,1.0,content_type,sha256(body.encode()).hexdigest())

class FakeHTTPClient:
    responder = None
    def __init__(self, scope, delay_ms=0, headers=None): self.scope=scope; self.headers=headers or {}
    async def __aenter__(self): return self
    async def __aexit__(self,*args): return None
    async def request(self, method, url, headers=None, content=None):
        if not self.scope.is_allowed(url): raise AssertionError('out-of-scope request attempted')
        return type(self).responder(method,url,headers or {},content) if type(self).responder else obs(url,status=404,content_type='text/plain')

@pytest.fixture
def scope():
    return ScopePolicy.from_root('https://app.example.test/', exclusions=['/admin'], allow_private_targets=True)

def test_crawler_js_endpoint_extraction_is_scope_limited(scope):
    crawler=Crawler(scope,10,3,0,respect_robots=False)
    body='''fetch("/api/users"); axios.get("/v1/items"); const outside="https://evil.example.test/api/token"; const gql="/graphql";'''
    result=crawler._extract_js_endpoints(body)
    assert 'https://app.example.test/api/users' in result
    assert 'https://app.example.test/v1/items' in result
    assert all('evil.example.test' not in item for item in result)

def test_crawler_fingerprints_common_server_and_frameworks(scope):
    crawler=Crawler(scope,10,3,0,respect_robots=False)
    technologies=crawler._fingerprint({'server':'nginx/1.24','x-powered-by':'Express'},'/_next/static/app.js')
    assert 'Nginx' in technologies and 'Express' in technologies and 'Next.js' in technologies

@pytest.mark.parametrize('content_type,expected_html', [
 ('text/html',True),('application/xhtml+xml',True),('application/json',False),('application/javascript',False),('text/plain',False),
])
def test_crawler_content_type_classification(scope,content_type,expected_html):
    assert Crawler._is_html(content_type) is expected_html

def test_snapshot_parses_links_forms_resources_and_mixed_content(scope):
    crawler=Crawler(scope,10,3,0,respect_robots=False)
    html='''<html><head><title>Demo title</title><script src="/app.js"></script></head>
    <body><a href="/account">Account</a><a href="https://outside.example.test/private">outside</a>
    <img src="http://app.example.test/pixel.png"><form action="/submit" method="post"><input type="password" name="password"></form></body></html>'''
    snap=crawler._snapshot('https://app.example.test/',0,obs('https://app.example.test/',html,headers={'server':'nginx'},content_type='text/html'))
    assert snap.title=='Demo title'
    assert 'https://app.example.test/account' in snap.links
    assert all('outside.example.test' not in x for x in snap.links)
    assert snap.forms and snap.forms[0]['method']=='POST'
    assert 'https://app.example.test/app.js' in snap.resources
    assert any(x.startswith('http://') for x in snap.mixed_content)

def test_crawler_respects_max_pages_and_discovery_scope(monkeypatch,scope):
    def responder(method,url,headers,content):
        if url.endswith('/'): return obs(url,'<a href="/account">Account</a><a href="/admin">Admin</a><a href="https://outside.example.test/">outside</a>')
        if url.endswith('/account'): return obs(url,'<html><title>Account</title></html>')
        return obs(url,status=404)
    monkeypatch.setattr('app.crawler.SafeHTTPClient',FakeHTTPClient)
    FakeHTTPClient.responder=responder
    pages=asyncio.run(Crawler(scope, max_pages=10,max_depth=3,delay_ms=0,respect_robots=False).crawl())
    assert {p.url for p in pages}=={'https://app.example.test/','https://app.example.test/account'}

def test_crawler_cancellation_stops_before_request(monkeypatch,scope):
    called=[]
    def responder(method,url,headers,content):
        called.append(url); return obs(url,'<html/>')
    monkeypatch.setattr('app.crawler.SafeHTTPClient',FakeHTTPClient)
    FakeHTTPClient.responder=responder
    pages=asyncio.run(Crawler(scope,10,3,0,respect_robots=False,cancel_check=lambda:True).crawl())
    assert pages==[] and called==[]

def test_crawler_sitemap_discovery_is_bounded_and_scoped(monkeypatch,scope):
    def responder(method,url,headers,content):
        if url.endswith('/robots.txt'):
            return obs(url,'Sitemap: https://app.example.test/sitemap.xml',content_type='text/plain')
        if url.endswith('/sitemap.xml'):
            return obs(url,'<urlset><url><loc>https://app.example.test/account</loc></url><url><loc>https://outside.example.test/steal</loc></url></urlset>',headers={'content-type':'application/xml'},content_type='application/xml')
        return obs(url,status=404)
    monkeypatch.setattr('app.crawler.SafeHTTPClient',FakeHTTPClient)
    FakeHTTPClient.responder=responder
    result=asyncio.run(Crawler(scope,10,3,0,respect_robots=False,max_endpoints=50).discover_sitemaps())
    assert result==['https://app.example.test/account']

def test_api_discovery_builds_inventory_from_openapi(monkeypatch,scope):
    spec={'openapi':'3.0.0','info':{'title':'Demo','version':'1'},'paths':{'/api/users':{'get':{'summary':'List users','operationId':'listUsers','responses':{'200':{'description':'ok'}}}}}}
    def responder(method,url,headers,content):
        if url.endswith('/openapi.json'): return obs(url,json.dumps(spec),headers={'content-type':'application/json'},content_type='application/json')
        if method=='OPTIONS': return obs(url,'',headers={'allow':'GET, OPTIONS'},content_type='text/plain')
        return obs(url,'',status=404,content_type='text/plain')
    monkeypatch.setattr('app.api_discovery.SafeHTTPClient',FakeHTTPClient)
    FakeHTTPClient.responder=responder
    assets,findings,specs=asyncio.run(APIDiscovery(scope,delay_ms=0).run())
    assert 'https://app.example.test/openapi.json' in specs
    assert any(x[1]=='api-operation-template' and x[0]=='https://app.example.test/api/users' for x in assets)
    assert 'FW-API-002' in {x.rule_id for x in findings}
    assert any(x[1]=='options' for x in assets)

def test_api_discovery_passive_mode_skips_options(monkeypatch,scope):
    def responder(method,url,headers,content):
        if method=='OPTIONS': raise AssertionError('passive-only mode must skip OPTIONS')
        return obs(url,'',status=404,content_type='text/plain')
    monkeypatch.setattr('app.api_discovery.SafeHTTPClient',FakeHTTPClient)
    FakeHTTPClient.responder=responder
    assets,findings,specs=asyncio.run(APIDiscovery(scope,delay_ms=0).run(passive_only=True))
    assert assets==[] and findings==[] and specs==[]

def test_graphql_readonly_introspection_parses_json(monkeypatch,scope):
    payload={'data':{'__schema':{'types':[{'name':'Query','fields':[]}]}}}
    def responder(method,url,headers,content):
        assert method=='POST' and 'query' in json.loads(content)
        return obs(url,json.dumps(payload),headers={'content-type':'application/json'},content_type='application/json')
    monkeypatch.setattr('app.api_discovery.SafeHTTPClient',FakeHTTPClient)
    FakeHTTPClient.responder=responder
    result=asyncio.run(APIDiscovery(scope,delay_ms=0).graphql_introspection('https://app.example.test/graphql'))
    assert result[1]['data']['__schema']['types'][0]['name']=='Query'

def test_parameter_probe_uses_only_inert_canaries_and_records_reflection(monkeypatch,scope):
    def responder(method,url,headers,content):
        assert method=='GET'
        q=parse_qs(urlparse(url).query)
        marker=q.get('q',[''])[0]
        return obs(url,f'<html><body>{marker}</body></html>')
    monkeypatch.setattr('app.parameter_probes.SafeHTTPClient',FakeHTTPClient)
    FakeHTTPClient.responder=responder
    results=asyncio.run(probe_reflected_query_inputs(scope,['https://app.example.test/search?q=old'],delay_ms=0,max_probes=5))
    assert results and results[0].rule_id=='FW-INPUT-001'
    assert results[0].evidence['probe_type']=='alphanumeric-canary'
    assert 'does not prove XSS' in results[0].description

def test_parameter_probe_skips_sensitive_names(monkeypatch,scope):
    calls=[]
    def responder(method,url,headers,content):
        calls.append(url); return obs(url,'')
    monkeypatch.setattr('app.parameter_probes.SafeHTTPClient',FakeHTTPClient)
    FakeHTTPClient.responder=responder
    result=asyncio.run(probe_reflected_query_inputs(scope,['https://app.example.test/search?token=secret&password=secret'],delay_ms=0,max_probes=10))
    assert result==[] and calls==[]

def test_tls_inspection_skips_plain_http():
    assert inspect_tls('http://app.example.test/')==[]

def test_tls_inspection_failure_is_a_bounded_observation(monkeypatch):
    def fail(*args,**kwargs): raise OSError('simulated offline socket')
    monkeypatch.setattr('app.checks.network_checks.socket.create_connection',fail)
    findings=inspect_tls('https://app.example.test/')
    assert findings and findings[0].rule_id=='FW-TLS-005'
    assert 'OSError' in findings[0].evidence_summary
