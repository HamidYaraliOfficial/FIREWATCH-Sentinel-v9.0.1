"""Broad deterministic regression matrices for secret handling."""
import pytest
from app.redaction import (
    SENSITIVE_QUERY_NAMES, SENSITIVE_FIELD_NAMES, contains_sensitive_query,
    redact_data, redact_text, redact_url,
)

ALL_NAMES = sorted(SENSITIVE_QUERY_NAMES | SENSITIVE_FIELD_NAMES)
@pytest.mark.parametrize("name", ALL_NAMES)
def test_v6_every_registered_sensitive_name_is_redacted_in_url(name):
    marker = "v6-secret-marker-do-not-leak"
    cleaned = redact_url(f"https://example.test/path?{name}={marker}&keep=visible")
    assert marker not in cleaned, name
    assert "keep=visible" in cleaned

@pytest.mark.parametrize("name", ALL_NAMES)
def test_v6_every_registered_sensitive_name_blocks_sensitive_query(name):
    assert contains_sensitive_query(f"https://example.test/?{name}=nonempty")

@pytest.mark.parametrize("name", ALL_NAMES)
def test_v6_structured_sensitive_fields_are_redacted(name):
    marker = "unique-v6-secret-9291"
    value = redact_data({name: marker, "safe": "ordinary-text"})
    assert marker not in str(value), name
    assert value[name] == "[REDACTED]"
    assert value["safe"] == "ordinary-text"

@pytest.mark.parametrize("url", [
    "https://user:password@example.test/path", "https://example.test/path?token=abc",
    "https://example.test/path?client.secret=abc", "https://example.test/path?x_api_key=abc",
    "https://example.test/path?DATABASE_URL=postgres://user:pw@db/one",
    "https://example.test/path?redirect=https%3A%2F%2Fother.test%2F%3Ftoken%3Dabc",
])
def test_v6_url_redaction_does_not_keep_credentials_or_query_secrets(url):
    output = redact_url(url)
    assert "password" not in output or "[REDACTED]" in output
    assert "user:" not in output
    assert "abc" not in output

@pytest.mark.parametrize("text,marker", [
    ("Authorization: Bearer abcdefghijklmnop", "abcdefghijklmnop"),
    ("Cookie: sessionid=private-value", "private-value"),
    ("Set-Cookie: sid=another-private-value; HttpOnly", "another-private-value"),
    ("password='correct horse battery staple'", "correct horse battery staple"),
    ("client_secret=client-demo", "client-demo"),
    ("https://example.test/path?access_token=query-secret-value", "query-secret-value"),
    ("private_key=" + "-----BEGIN " + "PRIVATE KEY-----" + "fake" + "-----END " + "PRIVATE KEY-----", "fake"),
])
def test_v6_redact_text_secret_patterns(text, marker):
    assert marker not in redact_text(text)

@pytest.mark.parametrize("data", [
    {"nested": {"Authorization": "Bearer secret-token-123456", "okay": 7}},
    {"items": [{"cookie": "sid=private", "name": "public"}]},
    {"url": "https://example.test/?token=secret-value", "message": "password=abc123456"},
    {"set-cookie": "session=secret-value", "child": {"client_secret": "hidden"}},
])
def test_v6_nested_redaction_is_recursive_and_preserves_safe_values(data):
    output = str(redact_data(data))
    for marker in ("secret-token-123456", "sid=private", "secret-value", "abc123456", "hidden"):
        assert marker not in output
