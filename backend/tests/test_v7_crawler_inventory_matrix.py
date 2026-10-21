"""HTML/JavaScript crawler parser invariants using only synthetic responses."""
from types import SimpleNamespace
import pytest
from app.crawler import Crawler
from app.http_client import HTTPObservation
from app.scope import ScopePolicy

@pytest.fixture
def crawler():
    policy = ScopePolicy.from_root("https://app.example.test/", exclusions=["/logout", "/admin/*"], allow_private_targets=True)
    return Crawler(policy, max_pages=40, max_depth=4, delay_ms=0, respect_robots=False, max_endpoints=200, max_concurrency=4)

def observation(url, body, content_type="text/html", headers=None, status=200):
    body = body or ""
    return HTTPObservation(url, url, status, {k.lower(): v for k, v in (headers or {}).items()}, body, 1.0, content_type, "a" * 64)

@pytest.mark.parametrize("body,expected", [
    ("<html><title>One</title><a href='/api/users'>API</a></html>", "One"),
    ("<html><title>  Mixed  </title></html>", "Mixed"),
    ("<html><body>none</body></html>", None),
    ("<title>" + "x" * 600 + "</title>", "x" * 500),
])
def test_v7_html_title_parser_is_bounded(crawler, body, expected):
    snap = crawler._snapshot("https://app.example.test/", 0, observation("https://app.example.test/", body))
    assert snap.title == expected

@pytest.mark.parametrize("href", [
    "/about", "https://app.example.test/help", "../guide", "?lang=en", "#section", "/api/v1/users",
    "/search?q=safe", "/products?id=42", "/docs/openapi.json", "/graphql",
])
def test_v7_crawler_discovers_only_valid_same_scope_links(crawler, href):
    body = f"<html><body><a href='{href}'>link</a></body></html>"
    snap = crawler._snapshot("https://app.example.test/page", 0, observation("https://app.example.test/page", body))
    assert all(crawler.scope.is_allowed(link) for link in snap.links)

@pytest.mark.parametrize("href", [
    "https://evil.example/collect", "//evil.example/path", "javascript:alert(1)", "data:text/html,hi",
    "https://app.example.test/logout", "https://app.example.test/admin/users", "https://app.example.test/?token=secret",
])
def test_v7_crawler_does_not_inventory_out_of_scope_or_sensitive_links(crawler, href):
    body = f"<html><body><a href='{href}'>link</a></body></html>"
    snap = crawler._snapshot("https://app.example.test/page", 0, observation("https://app.example.test/page", body))
    assert href not in snap.links

@pytest.mark.parametrize("method", ["get", "GET", "post", "PUT", "delete", "trace", "connect", ""])
def test_v7_form_method_is_normalized_without_submitting(crawler, method):
    body = f"<form action='/submit' method='{method}'><input name='email' value='a@b.test'></form>"
    snap = crawler._snapshot("https://app.example.test/", 0, observation("https://app.example.test/", body))
    assert len(snap.forms) == 1
    assert snap.forms[0]["method"] == (method.upper() or "GET")
    assert snap.forms[0]["action"] == "https://app.example.test/submit"
    assert snap.forms[0]["inputs"][0]["name"] == "email"

@pytest.mark.parametrize("script,should_find", [
    ("fetch('/api/users')", True), ("axios.get('/v1/items')", True), ("'/graphql'", True),
    ("'/auth/callback'", True), ("'/admin/settings'", False), ("'/about'", False),
    ("fetch('https://evil.example/api/key')", False), ("fetch('/logout')", False),
    ("fetch('/api/users?token=secret')", False), ("const x = 'not a route';", False),
])
def test_v7_javascript_route_extraction_is_scoped(script, should_find, crawler):
    found = crawler._extract_js_endpoints(script)
    assert bool(found) is should_find
    assert all(crawler.scope.is_allowed(url) for url in found)

@pytest.mark.parametrize("headers,body,expected", [
    ({"Server":"nginx/1"}, "", {"Nginx"}), ({"Server":"Apache"}, "", {"Apache"}),
    ({"Server":"Microsoft-IIS/10"}, "", {"IIS"}), ({"X-Powered-By":"Express"}, "", {"Express"}),
    ({}, "<?php echo 1; ?>", {"PHP"}), ({}, "<script id='__NEXT_DATA__'>x</script>", {"Next.js"}),
    ({}, "<link href='/wp-content/a.css'>", {"WordPress"}), ({"Server":"uvicorn"}, "", {"FastAPI/Starlette"}),
])
def test_v7_technology_fingerprint_known_indicators(crawler, headers, body, expected):
    assert expected.issubset(set(crawler._fingerprint(headers, body)))

def test_v7_crawler_snapshot_caps_and_deduplicates_links(crawler):
    links = "".join("<a href='/same'>x</a>" for _ in range(1600))
    snap = crawler._snapshot("https://app.example.test/", 0, observation("https://app.example.test/", "<html>"+links+"</html>"))
    assert snap.links == ["https://app.example.test/same"]
    assert len(snap.links) <= 1000
