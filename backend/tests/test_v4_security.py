from __future__ import annotations

import asyncio
import httpx
import pytest

from app.http_client import SafeHTTPClient
from app.scope import ScopePolicy, ScopeViolation


def test_exclusions_are_segment_aware_and_handle_encoded_dot_segments():
    policy = ScopePolicy.from_root(
        "https://app.example.com/", exclusions=["/admin"], allow_private_targets=True
    )
    assert policy.is_allowed("https://app.example.com/administrator")
    assert not policy.is_allowed("https://app.example.com/admin/users")
    with pytest.raises(ScopeViolation):
        policy.validate_url("https://app.example.com/public/%2e%2e/admin/users")


def test_sensitive_query_urls_are_not_requested_or_crawled():
    policy = ScopePolicy.from_root("https://app.example.com/", allow_private_targets=True)
    with pytest.raises(ScopeViolation):
        policy.validate_url("https://app.example.com/reset?token=do-not-store")
    assert not policy.is_allowed("https://app.example.com/reset?session-id=do-not-store")


def test_malformed_url_ports_are_scope_errors():
    with pytest.raises(ScopeViolation):
        ScopePolicy.from_root("https://app.example.com:not-a-port/", allow_private_targets=True)


def test_sensitive_headers_only_go_to_exact_root_hostname():
    policy = ScopePolicy.from_root(
        "https://app.example.com/",
        allowed_hosts=["https://api.example.com"],
        allow_private_targets=True,
    )
    client = SafeHTTPClient(
        policy,
        delay_ms=0,
        headers={
            "Authorization": "Bearer do-not-leak",
            "Cookie": "session=do-not-leak",
            "X-Tenant": "testing",
            "Proxy-Authorization": "never-send",
        },
    )
    root_headers = {k.lower(): v for k, v in client._headers_for("https://app.example.com/account").items()}
    api_headers = {k.lower(): v for k, v in client._headers_for("https://api.example.com/users").items()}
    assert root_headers["authorization"] == "Bearer do-not-leak"
    assert root_headers["cookie"] == "session=do-not-leak"
    assert root_headers["x-tenant"] == "testing"
    assert "proxy-authorization" not in root_headers
    assert "authorization" not in api_headers
    assert "cookie" not in api_headers
    assert api_headers["x-tenant"] == "testing"


def test_http_transport_confirms_credentials_are_not_forwarded():
    async def run():
        policy = ScopePolicy.from_root(
            "https://app.example.com/",
            allowed_hosts=["https://api.example.com"],
            allow_private_targets=True,
        )
        seen = []

        async def handler(request: httpx.Request) -> httpx.Response:
            seen.append((request.url.host, request.headers.get("authorization"), request.headers.get("cookie")))
            return httpx.Response(200, text="ok")

        async with SafeHTTPClient(
            policy, delay_ms=0,
            headers={"Authorization": "Bearer private-test", "Cookie": "sid=private-test"},
        ) as client:
            await client.client.aclose()
            client.client = httpx.AsyncClient(
                transport=httpx.MockTransport(handler),
                headers={"User-Agent": "FIREWATCH-test"},
                follow_redirects=False,
            )
            await client.request("GET", "https://app.example.com/")
            await client.request("GET", "https://api.example.com/users")
        assert seen[0][1:] == ("Bearer private-test", "sid=private-test")
        assert seen[1][1:] == (None, None)

    asyncio.run(run())


def test_authentication_material_is_not_sent_over_public_plain_http():
    # Construct a public-target policy directly to avoid any DNS dependency in tests.
    from app.scope import ScopePolicy
    policy = ScopePolicy(
        root_url="http://app.example.com/",
        allowed_hosts=frozenset({"app.example.com"}),
        excluded_prefixes=(),
        allow_private_targets=False,
        allowed_ports={"app.example.com": frozenset({80, 443})},
    )
    client = SafeHTTPClient(policy, headers={"Authorization": "Bearer do-not-send-over-http", "X-Tenant": "test"})
    headers = {k.lower(): v for k, v in client._headers_for("http://app.example.com/account").items()}
    assert "authorization" not in headers
    assert headers["x-tenant"] == "test"
