"""DNS-pinned network backend for FIREWATCH's default HTTP transport.

The HTTP layer validates the URL against the scan scope, but validating DNS only
at scan creation leaves a DNS-rebinding window. This backend resolves a hostname
immediately before each TCP connection and connects to the resolved IP literal,
so the HTTP stack cannot perform a second hostname lookup for that socket.
HTTPS TLS still receives the original URL hostname as its server name through
httpcore, preserving certificate validation and SNI.
"""
from __future__ import annotations

import asyncio
import ipaddress
import socket
from collections.abc import Awaitable, Callable, Iterable

import httpcore

from .scope import ScopePolicy

IPAddress = ipaddress.IPv4Address | ipaddress.IPv6Address
Resolver = Callable[[str, int], Awaitable[Iterable[IPAddress]]]


def _publicly_routable(address: IPAddress) -> bool:
    """Conservative global-unicast test; rejects special-use address ranges."""
    return bool(
        address.is_global
        and not address.is_private
        and not address.is_loopback
        and not address.is_link_local
        and not address.is_multicast
        and not address.is_reserved
        and not address.is_unspecified
    )


async def _resolve_addresses(host: str, port: int) -> list[IPAddress]:
    try:
        literal = ipaddress.ip_address(host)
    except ValueError:
        # asyncio's asynchronous resolver avoids blocking the event loop while
        # keeping the selected address and the subsequent connect operation tied.
        loop = asyncio.get_running_loop()
        records = await loop.getaddrinfo(
            host,
            port,
            type=socket.SOCK_STREAM,
            proto=socket.IPPROTO_TCP,
        )
        addresses: list[IPAddress] = []
        seen: set[str] = set()
        for record in records:
            try:
                raw = record[4][0]
                address = ipaddress.ip_address(raw.split("%", 1)[0])
            except (ValueError, IndexError, TypeError):
                continue
            key = str(address)
            if key not in seen:
                seen.add(key)
                addresses.append(address)
        return addresses
    else:
        # Reject IPv6 zone identifiers rather than silently changing their
        # interface-specific meaning while normalizing the connect address.
        if getattr(literal, "scope_id", None):
            raise httpcore.ConnectError("Scoped IPv6 literals are not supported by the safe transport")
        return [literal]


class ScopePinnedNetworkBackend(httpcore.AsyncNetworkBackend):
    """Resolve once per connection and connect directly to a policy-checked IP."""

    def __init__(
        self,
        scope: ScopePolicy,
        *,
        fallback: httpcore.AsyncNetworkBackend | None = None,
        resolver: Resolver | None = None,
    ) -> None:
        self.scope = scope
        self.fallback = fallback or httpcore.AnyIOBackend()
        self.resolver = resolver or _resolve_addresses

    async def connect_tcp(
        self,
        host: str,
        port: int,
        timeout: float | None = None,
        local_address: str | None = None,
        socket_options=None,
    ) -> httpcore.AsyncNetworkStream:
        try:
            addresses = list(await self.resolver(host, port))
        except httpcore.ConnectError:
            raise
        except Exception as exc:
            raise httpcore.ConnectError("Target hostname could not be resolved safely") from exc

        # No socket is opened until every answer has passed policy. In particular,
        # a mixed public/private answer set is rejected rather than selecting only
        # the apparently public member of a potentially rebinding DNS response.
        if not addresses:
            raise httpcore.ConnectError("Target hostname did not resolve to a usable IP address")
        if not self.scope.allow_private_targets and any(not _publicly_routable(ip) for ip in addresses):
            raise httpcore.ConnectError("DNS resolution included a non-public address; refusing connection")

        last_error: Exception | None = None
        for address in addresses:
            try:
                return await self.fallback.connect_tcp(
                    str(address),
                    port,
                    timeout=timeout,
                    local_address=local_address,
                    socket_options=socket_options,
                )
            except Exception as exc:  # Try another validated A/AAAA record if reachable.
                last_error = exc
        raise httpcore.ConnectError("Could not connect to any policy-validated target address") from last_error

    async def connect_unix_socket(self, path: str, timeout: float | None = None, socket_options=None):
        # HTTP(S) target requests do not use Unix sockets. Delegate for interface
        # completeness; Unix-socket URLs remain rejected by ScopePolicy.
        return await self.fallback.connect_unix_socket(path, timeout=timeout, socket_options=socket_options)

    async def sleep(self, seconds: float) -> None:
        await self.fallback.sleep(seconds)
