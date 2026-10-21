"""Regression tests for credential isolation across origin boundaries."""
import asyncio
import httpx
import pytest
from app.http_client import SafeHTTPClient, credentials_allowed_for_root_origin
from app.scope import ScopePolicy

@pytest.mark.parametrize("root,target,allow_private,expected", [
    ("https://app.example.test/", "https://app.example.test/", False, True),
    ("https://app.example.test/", "https://app.example.test:443/a", False, True),
    ("https://app.example.test:8443/", "https://app.example.test:8443/a", False, True),
    ("https://app.example.test:8443/", "https://app.example.test/a", False, False),
    ("https://app.example.test/", "https://app.example.test:8443/a", False, False),
    ("https://app.example.test/", "http://app.example.test/a", False, False),
    ("http://app.example.test/", "http://app.example.test/a", False, False),
    ("http://app.example.test/", "http://app.example.test/a", True, True),
    ("https://app.example.test/", "https://api.example.test/a", False, False),
    ("https://app.example.test/", "https://app.example.test.evil.test/a", False, False),
    ("https://app.example.test/", "https://user@app.example.test/a", False, False),
    ("https://app.example.test/", "ftp://app.example.test/a", False, False),
    ("not a url", "https://app.example.test/a", True, False),
    ("https://app.example.test:bad/", "https://app.example.test/a", True, False),
])
def test_v6_credentials_require_exact_root_origin(root, target, allow_private, expected):
    assert credentials_allowed_for_root_origin(root, target, allow_private) is expected

@pytest.mark.parametrize("port,expected", [(443, True), (8443, False), (9443, False)])
def test_v6_same_host_other_port_never_receives_configured_credentials(port, expected):
    policy = ScopePolicy.from_root(
        "https://app.example.test/", allowed_hosts=[f"https://app.example.test:{port}"], allow_private_targets=True
    )
    # Build a policy whose scope explicitly allows the alternate port, to isolate credential behavior from scope.
    assert policy.is_allowed(f"https://app.example.test:{port}/")
    client = SafeHTTPClient(policy, delay_ms=0, headers={"Authorization": "Bearer private-token-123", "Cookie": "sid=secret-session"})
    headers = {k.lower(): v for k, v in client._headers_for(f"https://app.example.test:{port}/").items()}
    if expected:
        assert headers.get("authorization") == "Bearer private-token-123"
        assert headers.get("cookie") == "sid=secret-session"
    else:
        assert "authorization" not in headers
        assert "cookie" not in headers


def test_v6_mock_transport_never_sends_auth_to_other_port():
    async def run():
        policy = ScopePolicy.from_root("https://app.example.test/", allowed_hosts=["https://app.example.test:8443"], allow_private_targets=True)
        seen = []
        async def handler(request):
            seen.append((request.url.port or (443 if request.url.scheme == "https" else 80), request.headers.get("authorization"), request.headers.get("cookie")))
            return httpx.Response(200, text="ok")
        client = SafeHTTPClient(policy, delay_ms=0, headers={"Authorization": "Bearer top-secret-test", "Cookie": "sid=top-secret-test"})
        await client.__aenter__()
        await client.client.aclose()
        client.client = httpx.AsyncClient(transport=httpx.MockTransport(handler), follow_redirects=False)
        try:
            await client.request("GET", "https://app.example.test/")
            await client.request("GET", "https://app.example.test:8443/")
        finally:
            await client.__aexit__(None, None, None)
        assert seen[0] == (443, "Bearer top-secret-test", "sid=top-secret-test")
        assert seen[1] == (8443, None, None)
    asyncio.run(run())
