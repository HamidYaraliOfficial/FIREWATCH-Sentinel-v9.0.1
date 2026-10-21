"""Tests for bounded raw-response handling in FIREWATCH Sentinel."""
import asyncio
import httpx
import pytest

from app.http_client import SafeHTTPClient
from app.scope import ScopePolicy


def _policy():
    # Synthetic transport ensures these tests never contact a real network target.
    return ScopePolicy.from_root("https://unit.example.test/", allow_private_targets=True)


class _AsyncChunks(httpx.AsyncByteStream):
    def __init__(self, body: bytes, chunk_size: int = 127):
        self.body = body
        self.chunk_size = chunk_size

    async def __aiter__(self):
        for offset in range(0, len(self.body), self.chunk_size):
            yield self.body[offset:offset + self.chunk_size]

    async def aclose(self):
        return None


def test_http_response_body_is_bounded_and_marks_truncation():
    payload = b"A" * 4096
    seen = {}

    def handler(request):
        seen["accept_encoding"] = request.headers.get("accept-encoding")
        return httpx.Response(200, headers={"content-type": "text/plain; charset=utf-8"}, stream=_AsyncChunks(payload))

    async def run():
        async with SafeHTTPClient(_policy(), delay_ms=0, max_response_bytes=1024,
                                  transport=httpx.MockTransport(handler)) as client:
            return await client.request("GET", "https://unit.example.test/")

    observation = asyncio.run(run())
    assert len(observation.body.encode("utf-8")) <= 1024
    assert observation.body == "A" * 1024
    assert observation.body_truncated is True
    assert observation.body_encoding_unsupported is False
    assert seen["accept_encoding"] == "identity"


def test_unexpected_compressed_body_is_not_decompressed_or_parsed():
    def handler(request):
        return httpx.Response(200, headers={
            "content-type": "text/html", "content-encoding": "gzip"
        }, stream=_AsyncChunks(b"not-actually-gzip-but-marked-compressed"))

    async def run():
        async with SafeHTTPClient(_policy(), delay_ms=0, max_response_bytes=1024,
                                  transport=httpx.MockTransport(handler)) as client:
            return await client.request("GET", "https://unit.example.test/")

    observation = asyncio.run(run())
    assert observation.status_code == 200
    assert observation.body == ""
    assert observation.body_encoding_unsupported is True
    assert observation.error is None


@pytest.mark.parametrize("limit", [0, -1, 25_000_001, True, 1.5])
def test_response_body_limit_rejects_invalid_configuration(limit):
    with pytest.raises(ValueError):
        SafeHTTPClient(_policy(), max_response_bytes=limit)
