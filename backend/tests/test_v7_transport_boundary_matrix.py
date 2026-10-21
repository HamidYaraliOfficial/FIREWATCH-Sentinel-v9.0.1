"""Cross-origin authentication, transport header and redirect safety invariants."""
import asyncio
import httpx
import pytest
from app.http_client import SafeHTTPClient, credentials_allowed_for_root_origin
from app.scope import ScopePolicy, ScopeViolation

_ROOTS = ["https://app.example.test/", "https://APP.EXAMPLE.TEST./", "https://app.example.test:443/", "http://app.example.test/"]
_TARGETS = [
    ("https://app.example.test/", True), ("https://APP.EXAMPLE.TEST./path", True),
    ("https://app.example.test:443/path", True), ("https://app.example.test:444/path", False),
    ("http://app.example.test/path", False), ("https://api.example.test/path", False),
    ("https://app.example.test.evil/path", False), ("https://app.example.test@evil.test/", False),
    ("https://user:pass@app.example.test/", False), ("javascript:alert(1)", False),
]

@pytest.mark.parametrize("root", _ROOTS)
@pytest.mark.parametrize("target,https_expected", _TARGETS)
@pytest.mark.parametrize("allow_private", [False, True])
def test_v7_credentials_are_origin_and_scheme_bound(root, target, https_expected, allow_private):
    parsed_root = httpx.URL(root)
    parsed_target = httpx.URL(target)
    same_origin = (parsed_root.scheme, parsed_root.host.rstrip("."), parsed_root.port) == (parsed_target.scheme, parsed_target.host.rstrip("."), parsed_target.port)
    expected = same_origin and (parsed_target.scheme == "https" or allow_private) and target.startswith(("https://", "http://")) and "@" not in target.split("//",1)[-1].split("/",1)[0]
    assert credentials_allowed_for_root_origin(root, target, allow_private) == expected

@pytest.mark.parametrize("header", ["Host", "host", "Content-Length", "Transfer-Encoding", "Connection", "Upgrade", "TE", "Trailer", "Proxy-Authorization", "Proxy-Connection"])
def test_v7_transport_and_hop_by_hop_headers_are_always_blocked(header):
    scope = ScopePolicy.from_root("https://app.example.test/", allow_private_targets=True)
    client = SafeHTTPClient(scope, delay_ms=0, headers={header: "unsafe-value"})
    assert all(key.lower() != header.lower() for key in client._headers_for("https://app.example.test/").keys())

@pytest.mark.parametrize("url", ["https://app.example.test:8443/", "https://evil.example.test/", "javascript:alert(1)"])
def test_v7_out_of_scope_request_fails_before_transport(url):
    async def run():
        policy = ScopePolicy.from_root("https://app.example.test/", allow_private_targets=True)
        client = SafeHTTPClient(policy, delay_ms=0)
        calls = []
        async def handler(request):
            calls.append(str(request.url))
            return httpx.Response(200, text="must not happen")
        client.client = httpx.AsyncClient(transport=httpx.MockTransport(handler), follow_redirects=False)
        try:
            try:
                await client.request("GET", url)
            except (ScopeViolation, ValueError):
                pass
        finally:
            await client.client.aclose()
        assert calls == []
    asyncio.run(run())

@pytest.mark.parametrize("status", [301, 302, 303, 307, 308])
def test_v7_http_client_does_not_follow_redirects_automatically(status):
    async def run():
        policy = ScopePolicy.from_root("https://app.example.test/", allow_private_targets=True)
        seen = []
        async def handler(request):
            seen.append(str(request.url))
            return httpx.Response(status, headers={"Location": "https://evil.example.test/collect"}, text="redirect")
        client = SafeHTTPClient(policy, delay_ms=0)
        client.client = httpx.AsyncClient(transport=httpx.MockTransport(handler), follow_redirects=False)
        try:
            result = await client.request("GET", "https://app.example.test/")
        finally:
            await client.client.aclose()
        assert result.status_code == status
        assert seen == ["https://app.example.test/"]
    asyncio.run(run())
