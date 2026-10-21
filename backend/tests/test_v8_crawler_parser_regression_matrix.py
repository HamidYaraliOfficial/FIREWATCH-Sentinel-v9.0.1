"""Crawler parsing and inventory robustness over varied synthetic inputs."""
import pytest
from app.crawler import Crawler
from app.http_client import HTTPObservation
from app.scope import ScopePolicy

@pytest.fixture
def crawler():
    p=ScopePolicy.from_root("https://app.example.test/", exclusions=["/logout","/admin/*"],allow_private_targets=True)
    return Crawler(p,max_pages=30,max_depth=4,delay_ms=0,respect_robots=False,max_endpoints=120,max_concurrency=3)

def obs(url,body,content_type="text/html",headers=None,status=200):
    return HTTPObservation(url,url,status,{str(k).lower():str(v) for k,v in (headers or {}).items()},body,0.01,content_type,"a"*64)

@pytest.mark.parametrize("body", ["", "<html></html>", "plain text", "<!doctype html><title>x</title>", "<div><a href='/api/v1'>x</a></div>", "<script>fetch('/api/users')</script>", "<form><input name='x'></form>", "<img src='/asset.png'>", "<iframe src='//evil.test/frame'></iframe>", "<a href='/logout'>logout</a>", "<a href='/admin/private'>admin</a>", "<a href='javascript:alert(1)'>bad</a>", "<a href='data:text/html,x'>bad</a>", "<a href='https://evil.test'>external</a>"])
def test_v8_parser_never_raises_on_common_or_hostile_html(crawler,body):
    snap=crawler._snapshot("https://app.example.test/",0,obs("https://app.example.test/",body))
    assert snap.url=="https://app.example.test/"
    assert len(snap.links)<=1000 and len(snap.resources)<=1000
    assert all(crawler.scope.is_allowed(link) for link in snap.links)
    assert all(crawler.scope.is_allowed(resource) for resource in snap.resources)

@pytest.mark.parametrize("marker,expected", [("nginx", "Nginx"),("apache", "Apache"),("iis", "IIS"),("uvicorn", "FastAPI/Starlette"),("express", "Express")])
def test_v8_fingerprint_header_markers_are_case_insensitive(crawler,marker,expected):
    headers={"Server":marker,"X-Powered-By":marker}
    found=crawler._fingerprint(headers,"")
    assert expected in found

@pytest.mark.parametrize("route", ["/api/users", "/api/v1/items", "/graphql", "/auth/callback", "/login", "/users/123", "/v1/orders", "/v2/search"])
def test_v8_js_endpoint_discovery_finds_supported_route_families(crawler,route):
    found=crawler._extract_js_endpoints(f"const endpoint = '{route}';")
    assert found and all(crawler.scope.is_allowed(value) for value in found)

@pytest.mark.parametrize("route", ["https://evil.test/api/users", "https://app.example.test/logout", "https://app.example.test/admin/private", "https://app.example.test/?token=abc", "javascript:alert(1)", "data:text/html,x", "file:///etc/passwd"])
def test_v8_js_endpoint_discovery_rejects_out_of_scope_routes(crawler,route):
    found=crawler._extract_js_endpoints(f"fetch('{route}')")
    assert all(crawler.scope.is_allowed(value) for value in found)

@pytest.mark.parametrize("content_type", ["text/html", "application/xhtml+xml", "TEXT/HTML; charset=utf-8", "application/json", "text/plain", "application/javascript", "text/javascript; charset=utf-8"])
def test_v8_content_type_classification_is_stable(crawler,content_type):
    if "html" in content_type.lower(): assert crawler._is_html(content_type)
    elif "javascript" in content_type.lower(): assert not crawler._is_html(content_type)
    else: assert not crawler._is_html(content_type)
