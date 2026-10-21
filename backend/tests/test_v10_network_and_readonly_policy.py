"""Regression tests for socket-level scope enforcement and read-only HTTP policy."""
from __future__ import annotations

import asyncio
import ipaddress
import json
from dataclasses import replace

import httpcore
import httpx
import pytest

from app.http_client import SafeHTTPClient, _SAFE_GRAPHQL_INTROSPECTION_QUERY
from app.safe_network import ScopePinnedNetworkBackend
from app.scope import ScopePolicy, ScopeViolation


class FakeNetworkBackend:
    def __init__(self):
        self.connected = []

    async def connect_tcp(self, host, port, timeout=None, local_address=None, socket_options=None):
        self.connected.append((host, port))
        return object()

    async def connect_unix_socket(self, path, timeout=None, socket_options=None):
        raise AssertionError("Unix sockets must not be used")

    async def sleep(self, seconds):
        return None


def private_disabled_scope():
    scope = ScopePolicy.from_root("https://target.example.test/", allow_private_targets=True)
    return replace(scope, allow_private_targets=False)


def test_network_backend_connects_to_the_validated_ip_literal_not_hostname():
    async def resolver(_host, _port):
        return [ipaddress.ip_address("93.184.216.34")]

    async def run():
        fallback = FakeNetworkBackend()
        backend = ScopePinnedNetworkBackend(private_disabled_scope(), fallback=fallback, resolver=resolver)
        await backend.connect_tcp("target.example.test", 443, timeout=1.5)
        assert fallback.connected == [("93.184.216.34", 443)]

    asyncio.run(run())


def test_network_backend_rejects_mixed_public_and_private_dns_answers_before_connecting():
    async def resolver(_host, _port):
        return [ipaddress.ip_address("93.184.216.34"), ipaddress.ip_address("127.0.0.1")]

    async def run():
        fallback = FakeNetworkBackend()
        backend = ScopePinnedNetworkBackend(private_disabled_scope(), fallback=fallback, resolver=resolver)
        with pytest.raises(httpcore.ConnectError, match="non-public"):
            await backend.connect_tcp("target.example.test", 443)
        assert fallback.connected == []

    asyncio.run(run())


def test_network_backend_fails_closed_for_empty_dns_answers():
    async def resolver(_host, _port):
        return []

    async def run():
        fallback = FakeNetworkBackend()
        backend = ScopePinnedNetworkBackend(private_disabled_scope(), fallback=fallback, resolver=resolver)
        with pytest.raises(httpcore.ConnectError, match="did not resolve"):
            await backend.connect_tcp("target.example.test", 443)
        assert fallback.connected == []

    asyncio.run(run())


@pytest.mark.parametrize("method", ["PUT", "PATCH", "DELETE", "TRACE", "CONNECT", "PROPFIND"])
def test_non_read_only_methods_are_rejected_before_transport(method):
    async def run():
        seen = []

        async def handler(request):
            seen.append(request.method)
            return httpx.Response(200, text="unexpected")

        scope = ScopePolicy.from_root("https://app.example.test/", allow_private_targets=True)
        async with SafeHTTPClient(scope, delay_ms=0, transport=httpx.MockTransport(handler)) as client:
            with pytest.raises(ScopeViolation, match="Only GET, HEAD, OPTIONS"):
                await client.request(method, scope.root_url)
        assert seen == []

    asyncio.run(run())


def test_safe_graphql_introspection_post_is_allowed_but_mutation_is_not():
    async def run():
        seen = []

        async def handler(request):
            seen.append((request.method, json.loads(request.content.decode("utf-8"))))
            return httpx.Response(200, json={"data": {"__schema": {"queryType": {"name": "Query"}}}})

        scope = ScopePolicy.from_root("https://app.example.test/", allow_private_targets=True)
        async with SafeHTTPClient(
            scope,
            delay_ms=0,
            headers={"Content-Type": "application/json"},
            transport=httpx.MockTransport(handler),
        ) as client:
            observation = await client.request(
                "POST", "https://app.example.test/graphql",
                content=json.dumps({"query": _SAFE_GRAPHQL_INTROSPECTION_QUERY}),
            )
            assert observation.status_code == 200
            with pytest.raises(ScopeViolation, match="Only GET, HEAD, OPTIONS"):
                await client.request(
                    "POST", "https://app.example.test/graphql",
                    content=json.dumps({"query": "mutation { deleteAllUsers }"}),
                )
        assert len(seen) == 1
        assert seen[0][0] == "POST"
        assert seen[0][1] == {"query": _SAFE_GRAPHQL_INTROSPECTION_QUERY}

    asyncio.run(run())


@pytest.mark.parametrize(
    "url,content",
    [
        ("https://app.example.test/graphql", json.dumps({"query": _SAFE_GRAPHQL_INTROSPECTION_QUERY, "variables": {}})),
        ("https://app.example.test/api/execute", json.dumps({"query": _SAFE_GRAPHQL_INTROSPECTION_QUERY})),
        ("https://app.example.test/graphql", "x" * 16_385),
        ("https://app.example.test/graphql", "not-json"),
    ],
)
def test_graphql_post_guard_rejects_noncanonical_or_oversized_payloads(url, content):
    async def run():
        seen = []

        async def handler(request):
            seen.append(request)
            return httpx.Response(200)

        scope = ScopePolicy.from_root("https://app.example.test/", allow_private_targets=True)
        async with SafeHTTPClient(
            scope, delay_ms=0, headers={"Content-Type": "application/json"},
            transport=httpx.MockTransport(handler),
        ) as client:
            with pytest.raises(ScopeViolation):
                await client.request("POST", url, content=content)
        assert seen == []

    asyncio.run(run())


def test_default_http_transport_installs_scope_pinned_backend():
    async def run():
        scope = ScopePolicy.from_root("https://app.example.test/", allow_private_targets=True)
        async with SafeHTTPClient(scope, delay_ms=0) as client:
            transport = client.client._transport
            assert isinstance(transport, httpx.AsyncHTTPTransport)
            assert isinstance(transport._pool._network_backend, ScopePinnedNetworkBackend)

    asyncio.run(run())


def test_safe_read_methods_reject_request_bodies():
    async def run():
        scope = ScopePolicy.from_root("https://app.example.test/", allow_private_targets=True)
        async with SafeHTTPClient(scope, delay_ms=0, transport=httpx.MockTransport(lambda request: httpx.Response(200))) as client:
            with pytest.raises(ScopeViolation, match="Request bodies are not allowed"):
                await client.request("GET", scope.root_url, content="unexpected")

    asyncio.run(run())
