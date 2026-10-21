from __future__ import annotations

import asyncio
import json
import time
from dataclasses import dataclass
from hashlib import sha256
from typing import Mapping
from urllib.parse import urlparse

import httpx

from .config import settings
from .scope import ScopePolicy, ScopeViolation
from .safe_network import ScopePinnedNetworkBackend


_AUTH_HEADER_NAMES = {
    "authorization", "proxy-authorization", "cookie", "set-cookie",
    "x-api-key", "api-key", "x-auth-token", "x-access-token",
    "x-session-token", "authentication",
}
_SAFE_GRAPHQL_INTROSPECTION_QUERY = (
    "query IntrospectionQuery { __schema { queryType { name } mutationType { name } "
    "types { name kind fields { name } } } }"
)
_SAFE_HTTP_METHODS = {"GET", "HEAD", "OPTIONS"}

_ALWAYS_BLOCKED_HEADERS = {
    "proxy-authorization", "proxy-connection", "host", "content-length",
    "transfer-encoding", "connection", "upgrade", "te", "trailer",
}



def credentials_allowed_for_root_origin(root_url: str, target_url: str, allow_private_targets: bool = False) -> bool:
    """Return whether configured authentication may be sent to the target origin.

    Origin matching includes scheme, normalized hostname, and effective port.
    Authentication is not sent over public cleartext HTTP.
    """
    try:
        root = urlparse(str(root_url))
        target = urlparse(str(target_url))
        if root.username is not None or root.password is not None or target.username is not None or target.password is not None:
            return False
        root_scheme = root.scheme.lower()
        target_scheme = target.scheme.lower()
        root_host = (root.hostname or "").lower().rstrip(".")
        target_host = (target.hostname or "").lower().rstrip(".")
        root_port = root.port or (443 if root_scheme == "https" else 80)
        target_port = target.port or (443 if target_scheme == "https" else 80)
        valid_scheme = target_scheme in {"http", "https"} and target_scheme == root_scheme
        secure_channel = target_scheme == "https" or allow_private_targets
        return bool(root_host and target_host and root_host == target_host and valid_scheme
                    and root_port == target_port and secure_channel)
    except (TypeError, ValueError):
        return False

def _is_credential_header(name: str) -> bool:
    low = name.strip().lower()
    return (
        low in _AUTH_HEADER_NAMES
        or low.startswith("x-auth-")
        or low.endswith("-token")
        or "api-key" in low
        or "client-secret" in low
        or "session-id" in low
    )


@dataclass
class HTTPObservation:
    requested_url: str
    final_url: str
    status_code: int
    headers: dict[str, str]
    body: str
    elapsed_ms: float
    content_type: str
    body_sha256: str
    error: str | None = None
    set_cookies: list[str] | None = None
    body_truncated: bool = False
    body_encoding_unsupported: bool = False


class SafeHTTPClient:
    """Scoped HTTP client with conservative pacing and root-host credential isolation.

    Authentication material is sent only to the exact hostname in the root URL.
    Additional in-scope hosts can still be discovered, but credentials are not
    forwarded to them. Redirects are never followed automatically.
    """

    def __init__(self, scope: ScopePolicy, timeout: float | None = None,
                 delay_ms: int | None = None, headers: Mapping[str, str] | None = None,
                 max_response_bytes: int | None = None,
                 transport: httpx.AsyncBaseTransport | None = None):
        self.scope = scope
        self.timeout = timeout or settings.request_timeout_seconds
        self.delay_ms = settings.request_delay_ms if delay_ms is None else delay_ms
        if max_response_bytes is None:
            max_response_bytes = getattr(settings, "max_response_body_bytes", 2_000_000)
        if not isinstance(max_response_bytes, int) or isinstance(max_response_bytes, bool) or not 1024 <= max_response_bytes <= 25_000_000:
            raise ValueError("max_response_bytes must be within 1024..25000000")
        self.max_response_bytes = max_response_bytes
        self.transport = transport
        self.headers = dict(headers or {})
        root = urlparse(scope.root_url)
        self.root_host = (root.hostname or "").lower().rstrip(".")
        self.root_scheme = root.scheme.lower()
        self.root_port = root.port or (443 if self.root_scheme == "https" else 80)
        self.client: httpx.AsyncClient | None = None
        self._last_request_at = 0.0
        self._lock = asyncio.Lock()

    async def __aenter__(self):
        base = {
            "User-Agent": settings.user_agent,
            "Accept": "text/html,application/json,text/plain,application/xml,*/*",
            # Ask for identity so parser code never needs to decompress an
            # attacker-controlled compressed response. If the server ignores it,
            # content inspection is skipped rather than buffering/decompressing.
            "Accept-Encoding": "identity",
        }
        client_kwargs = dict(
            timeout=self.timeout,
            follow_redirects=False,
            headers=base,
            verify=True,
            trust_env=False,
            limits=httpx.Limits(max_connections=20, max_keepalive_connections=10),
        )
        if self.transport is not None:
            # Injectable transports are reserved for deterministic local tests.
            # Normal application traffic always uses the scope-pinned transport.
            client_kwargs["transport"] = self.transport
        else:
            transport = httpx.AsyncHTTPTransport(
                verify=True, trust_env=False,
                limits=httpx.Limits(max_connections=20, max_keepalive_connections=10),
            )
            pool = getattr(transport, "_pool", None)
            if pool is None or not hasattr(pool, "_network_backend"):
                # Fail closed if an upstream httpx/httpcore update changes the
                # transport contract needed to enforce DNS pinning.
                raise RuntimeError("Installed HTTP transport cannot enforce scoped DNS pinning")
            pool._network_backend = ScopePinnedNetworkBackend(self.scope)
            client_kwargs["transport"] = transport
        self.client = httpx.AsyncClient(**client_kwargs)
        return self

    async def __aexit__(self, *_):
        if self.client:
            await self.client.aclose()

    async def _throttle(self):
        requested = max(0, self.delay_ms)
        effective = requested if self.scope.allow_private_targets else max(50, requested)
        gap = effective / 1000.0
        async with self._lock:
            elapsed = time.monotonic() - self._last_request_at
            if elapsed < gap:
                await asyncio.sleep(gap - elapsed)
            self._last_request_at = time.monotonic()

    def _headers_for(self, url: str, extra: Mapping[str, str] | None = None) -> dict[str, str]:
        merged: dict[str, tuple[str, str]] = {}
        for source in (self.headers, extra or {}):
            for key, value in source.items():
                low = str(key).strip().lower()
                if not low or low in _ALWAYS_BLOCKED_HEADERS:
                    continue
                merged[low] = (str(key), str(value))
        # Authentication material is bound to the exact root origin (scheme, host, port),
        # not merely the host. Different services on the same host may have different trust.
        credentials_allowed = credentials_allowed_for_root_origin(
            self.scope.root_url, url, self.scope.allow_private_targets
        )
        result = {}
        for low, (original, value) in merged.items():
            if _is_credential_header(low) and not credentials_allowed:
                continue
            result[original] = value
        return result

    @staticmethod
    def _is_safe_graphql_introspection(url: str, content: str | bytes | None) -> bool:
        """Allow only the one bounded GraphQL schema query used by discovery.

        POST is otherwise denied to prevent future probes from accidentally
        mutating target state. The request must target a conventional GraphQL
        endpoint and contain exactly the reviewed, static introspection query.
        """
        if content is None:
            return False
        try:
            raw = content.encode("utf-8") if isinstance(content, str) else bytes(content)
            if len(raw) > 16_384:
                return False
            path = urlparse(url).path.rstrip("/").lower()
            if not path or path.split("/")[-1] != "graphql":
                return False
            payload = json.loads(raw.decode("utf-8"))
            return (isinstance(payload, dict) and set(payload) == {"query"}
                    and payload.get("query") == _SAFE_GRAPHQL_INTROSPECTION_QUERY)
        except (UnicodeDecodeError, TypeError, ValueError, json.JSONDecodeError):
            return False

    async def request(self, method: str, url: str,
                      headers: Mapping[str, str] | None = None,
                      content: str | bytes | None = None) -> HTTPObservation:
        if not self.client:
            raise RuntimeError("SafeHTTPClient must be used as an async context manager")
        clean = self.scope.validate_url(url)
        normalized_method = str(method).upper()
        if normalized_method in _SAFE_HTTP_METHODS:
            if content not in (None, "", b""):
                raise ScopeViolation("Request bodies are not allowed for GET, HEAD, or OPTIONS")
        elif normalized_method == "POST" and self._is_safe_graphql_introspection(clean, content):
            effective_headers = self._headers_for(clean, headers)
            content_type = next((v for k, v in effective_headers.items() if k.lower() == "content-type"), "")
            if content_type.split(";", 1)[0].strip().lower() != "application/json":
                raise ScopeViolation("GraphQL introspection POST requires application/json")
        else:
            raise ScopeViolation("Only GET, HEAD, OPTIONS, and the exact read-only GraphQL introspection POST are permitted")
        await self._throttle()
        start = time.perf_counter()
        try:
            async with self.client.stream(
                normalized_method, clean,
                headers=self._headers_for(clean, headers),
                content=content,
            ) as resp:
                raw = bytearray()
                truncated = False
                if resp.is_stream_consumed:
                    # Custom/test transports may return an already-buffered
                    # Response object. Enforce the parser cap even though that
                    # transport itself supplied the buffered bytes.
                    buffered = resp.content
                    raw.extend(buffered[:self.max_response_bytes])
                    truncated = len(buffered) > self.max_response_bytes
                else:
                    async for chunk in resp.aiter_raw():
                        remaining = self.max_response_bytes - len(raw)
                        if len(chunk) > remaining:
                            if remaining > 0:
                                raw.extend(chunk[:remaining])
                            truncated = True
                            break
                        raw.extend(chunk)
                cookies = resp.headers.get_list("set-cookie")
                normalized = {k.lower(): v for k, v in resp.headers.items()}
                if cookies:
                    normalized["set-cookie"] = "\n".join(cookies)
                content_encoding = (resp.headers.get("content-encoding") or "identity").strip().lower()
                encoding_unsupported = content_encoding not in {"", "identity"}
                if encoding_unsupported:
                    # The response bytes stay bounded, but do not feed compressed
                    # data to text parsers or trigger automatic decompression.
                    body = ""
                else:
                    content_type_header = resp.headers.get("content-type", "")
                    charset = "utf-8"
                    for part in content_type_header.split(";")[1:]:
                        key, sep, value = part.strip().partition("=")
                        if sep and key.strip().lower() == "charset":
                            candidate = value.strip().strip('"\'')
                            if candidate and len(candidate) <= 40:
                                charset = candidate
                            break
                    try:
                        body = bytes(raw).decode(charset, errors="replace")
                    except LookupError:
                        body = bytes(raw).decode("utf-8", errors="replace")
                elapsed = (time.perf_counter() - start) * 1000
                return HTTPObservation(
                    clean, str(resp.url), resp.status_code, normalized, body,
                    round(elapsed, 2), resp.headers.get("content-type", ""),
                    sha256(bytes(raw)).hexdigest(), None, cookies, truncated, encoding_unsupported,
                )
        except Exception as exc:
            elapsed = (time.perf_counter() - start) * 1000
            # Exception strings can include URLs/query values; do not persist them verbatim.
            return HTTPObservation(
                clean, clean, 0, {}, "", round(elapsed, 2), "",
                sha256(b"").hexdigest(), type(exc).__name__, None, False, False,
            )
