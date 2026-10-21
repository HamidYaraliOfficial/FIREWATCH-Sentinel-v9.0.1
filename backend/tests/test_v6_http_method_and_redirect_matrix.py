"""HTTP adapter safety matrix using httpx.MockTransport only."""
import asyncio
import httpx
import pytest
from app.http_client import SafeHTTPClient
from app.scope import ScopePolicy, ScopeViolation

@pytest.mark.parametrize("method", ["get", "head", "options"])
def test_v6_read_only_http_methods_are_normalized_and_redirects_stay_disabled(method):
    async def run():
        seen=[]
        async def handler(request):
            seen.append(request.method)
            return httpx.Response(302, headers={"Location":"https://outside.example.test/"}, text="redirect")
        scope=ScopePolicy.from_root("https://app.example.test/",allow_private_targets=True)
        client=SafeHTTPClient(scope,delay_ms=0)
        await client.__aenter__(); await client.client.aclose()
        client.client=httpx.AsyncClient(transport=httpx.MockTransport(handler),follow_redirects=False)
        try:
            response=await client.request(method,"https://app.example.test/")
        finally:
            await client.__aexit__(None,None,None)
        assert response.status_code == 302
        assert seen == [method.upper()]
    asyncio.run(run())

@pytest.mark.parametrize("method", ["post", "put", "patch", "delete"])
def test_v6_mutating_or_unreviewed_http_methods_are_rejected(method):
    async def run():
        scope=ScopePolicy.from_root("https://app.example.test/",allow_private_targets=True)
        client=SafeHTTPClient(scope,delay_ms=0)
        await client.__aenter__()
        try:
            with pytest.raises(ScopeViolation):
                await client.request(method,"https://app.example.test/")
        finally:
            await client.__aexit__(None,None,None)
    asyncio.run(run())

@pytest.mark.parametrize("url", [
    "https://outside.example.test/", "https://app.example.test:8443/",
    "https://app.example.test/path?token=secret", "https://user:pass@app.example.test/",
    "ftp://app.example.test/", "https://app.example.test:bad/",
])
def test_v6_http_adapter_rejects_out_of_scope_before_send(url):
    async def run():
        scope=ScopePolicy.from_root("https://app.example.test/",allow_private_targets=True)
        client=SafeHTTPClient(scope,delay_ms=0)
        await client.__aenter__()
        try:
            with pytest.raises(ScopeViolation):
                await client.request("GET",url)
        finally:
            await client.__aexit__(None,None,None)
    asyncio.run(run())
