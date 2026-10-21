"""Harmless GET canary policy: sensitive params excluded, limits honored, no forms submitted."""
import asyncio
from urllib.parse import parse_qs, urlparse
import pytest
from app.http_client import HTTPObservation
from app.parameter_probes import probe_reflected_query_inputs
from app.scope import ScopePolicy

class ProbeClient:
    seen=[]
    def __init__(self, scope, delay_ms=0, headers=None): self.scope=scope
    async def __aenter__(self): return self
    async def __aexit__(self,*args): return None
    async def request(self, method, url, headers=None, content=None):
        assert method.upper()=="GET"
        assert content is None
        assert self.scope.is_allowed(url)
        self.seen.append(url)
        q=parse_qs(urlparse(url).query)
        marker=next(iter(q.values()))[0] if q else ""
        body=f"<html><body>{marker}</body></html>"
        from hashlib import sha256
        return HTTPObservation(url,url,200,{"content-type":"text/html"},body,0.1,"text/html",sha256(body.encode()).hexdigest())

@pytest.fixture
def scope(): return ScopePolicy.from_root("https://app.example.test/", allow_private_targets=True)

@pytest.mark.parametrize("name", ["authorization","auth","token","jwt","access_token","refresh_token","id_token","password","passwd","passphrase","secret","secret_key","private_key","api_key","apikey","session","sessionid","session_id","sid","code","otp","csrf","xsrf","credential","credentials"])
def test_v7_probe_never_mutates_sensitive_query_parameter(monkeypatch, scope, name):
    from app import parameter_probes
    monkeypatch.setattr(parameter_probes,"SafeHTTPClient",ProbeClient)
    ProbeClient.seen=[]
    output=asyncio.run(probe_reflected_query_inputs(scope,[f"https://app.example.test/search?{name}=private-value"],delay_ms=0,max_probes=5))
    assert output==[]
    assert ProbeClient.seen==[]

@pytest.mark.parametrize("limit", [0,1,2,3,5,10,25])
def test_v7_probe_respects_global_probe_limit(monkeypatch, scope, limit):
    from app import parameter_probes
    monkeypatch.setattr(parameter_probes,"SafeHTTPClient",ProbeClient)
    ProbeClient.seen=[]
    urls=[f"https://app.example.test/search?param{i}=value" for i in range(40)]
    output=asyncio.run(probe_reflected_query_inputs(scope,urls,delay_ms=0,max_probes=limit))
    assert len(ProbeClient.seen) <= limit
    assert all("token=" not in url for url in ProbeClient.seen)
    assert all(item.evidence["probe_type"]=="alphanumeric-canary" for item in output)

@pytest.mark.parametrize("query", ["?q=one", "?q=one&category=two", "?a=1&b=2&c=3", "?lang=en&theme=dark&sort=asc&view=list"])
def test_v7_probe_canaries_are_non_executable_alphanumeric(monkeypatch, scope, query):
    from app import parameter_probes
    monkeypatch.setattr(parameter_probes,"SafeHTTPClient",ProbeClient)
    ProbeClient.seen=[]
    asyncio.run(probe_reflected_query_inputs(scope,["https://app.example.test/search"+query],delay_ms=0,max_probes=20))
    assert ProbeClient.seen
    for url in ProbeClient.seen:
        values=[v for group in parse_qs(urlparse(url).query).values() for v in group]
        assert all(value.startswith("FWCANARY") and value.isalnum() for value in values if value.startswith("FWCANARY"))
        assert all("<" not in value and ">" not in value and "'" not in value for value in values)
