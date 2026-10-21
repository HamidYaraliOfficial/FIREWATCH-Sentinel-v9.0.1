"""Protocol and scope edge behavior for the HTTP client and scan policy."""
import asyncio
import httpx
import pytest
from app.http_client import SafeHTTPClient
from app.scope import ScopePolicy, ScopeViolation

@pytest.mark.parametrize("method", ["GET","HEAD","OPTIONS","get","head","options"])
def test_v8_safe_client_normalizes_read_only_method_case(method):
    async def run():
        scope=ScopePolicy.from_root("https://app.example.test/",allow_private_targets=True)
        seen=[]
        async def handler(request):
            seen.append(request.method)
            return httpx.Response(200,text="ok")
        client=SafeHTTPClient(scope,delay_ms=0)
        await client.__aenter__(); await client.client.aclose()
        client.client=httpx.AsyncClient(transport=httpx.MockTransport(handler),follow_redirects=False)
        try: await client.request(method,scope.root_url)
        finally: await client.__aexit__(None,None,None)
        assert seen==[method.upper()]
    asyncio.run(run())

@pytest.mark.parametrize("target", ["http://app.example.test:8443/","https://api.example.test:80/","https://api.example.test:443/","http://api.example.test:8443/","https://evil.example.test/"])
def test_v8_scheme_port_and_host_mismatches_fail_before_transport(target):
    async def run():
        scope=ScopePolicy.from_root("https://app.example.test/",allow_private_targets=True,allowed_hosts=["https://api.example.test:8443"])
        seen=[]
        async def handler(request): seen.append(str(request.url)); return httpx.Response(200,text="not expected")
        client=SafeHTTPClient(scope,delay_ms=0)
        await client.__aenter__(); await client.client.aclose()
        client.client=httpx.AsyncClient(transport=httpx.MockTransport(handler),follow_redirects=False)
        try:
            with pytest.raises(ScopeViolation):
                await client.request("GET",target)
        finally: await client.__aexit__(None,None,None)
        assert seen==[]
    asyncio.run(run())

@pytest.mark.parametrize("status", [301,302,303,307,308])
def test_v8_redirect_response_is_returned_without_automatic_follow(status):
    async def run():
        scope=ScopePolicy.from_root("https://app.example.test/",allow_private_targets=True)
        seen=[]
        async def handler(request):
            seen.append(str(request.url))
            return httpx.Response(status,headers={"Location":"https://evil.example.test/receive"},text="redirect")
        client=SafeHTTPClient(scope,delay_ms=0)
        await client.__aenter__(); await client.client.aclose()
        client.client=httpx.AsyncClient(transport=httpx.MockTransport(handler),follow_redirects=False)
        try: obs=await client.request("GET",scope.root_url)
        finally: await client.__aexit__(None,None,None)
        assert obs.status_code==status
        assert len(seen)==1 and "evil.example" not in seen[0]
    asyncio.run(run())

@pytest.mark.parametrize("url", ["https://app.example.test/ path","https://app.example.test/?q=has space","https://app.example.test/\tpath","https://app.example.test/\u00a0path"])
def test_v8_raw_whitespace_is_refused_before_network(url):
    policy=ScopePolicy.from_root("https://app.example.test/",allow_private_targets=True)
    assert not policy.is_allowed(url)
    with pytest.raises(ScopeViolation): policy.validate_url(url)
