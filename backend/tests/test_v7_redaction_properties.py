"""Credential redaction corpus spanning key normalizations and nested values."""
from urllib.parse import quote
import pytest
from app.redaction import SENSITIVE_QUERY_NAMES, SENSITIVE_FIELD_NAMES, contains_sensitive_query, redact_data, redact_text, redact_url

@pytest.mark.parametrize("name", sorted(SENSITIVE_QUERY_NAMES))
@pytest.mark.parametrize("separator", ["_", "-", ".", " "])
def test_v7_sensitive_query_names_survive_common_separator_variants(name, separator):
    variant = name.replace("_", separator)
    secret = "FWV7-DO-NOT-LEAK-5e8b1f"
    assert contains_sensitive_query(f"https://app.example.test/?{quote(variant)}={secret}")
    rendered = redact_url(f"https://app.example.test/?{quote(variant)}={secret}")
    assert secret not in rendered

@pytest.mark.parametrize("name", sorted(SENSITIVE_FIELD_NAMES))
def test_v7_sensitive_structured_field_names_are_redacted(name):
    sentinel = "FWV7-STRUCTURED-SECRET-9127"
    output = str(redact_data({"level1": [{"level2": {name: sentinel}}]}))
    assert sentinel not in output

@pytest.mark.parametrize("depth", range(1, 5))
@pytest.mark.parametrize("secret_name", ["token", "access_token", "client_secret", "session", "api_key", "password"])
def test_v7_nested_url_credentials_are_redacted_within_supported_depth(depth, secret_name):
    secret = "FWV7-NESTED-SECRET-7319"
    nested = f"https://inner.example.test/path?{secret_name}={secret}"
    for idx in range(depth):
        nested = "https://outer.example.test/return?next=" + quote(nested, safe="")
    output = redact_url(nested)
    assert secret not in output

@pytest.mark.parametrize("name", ["authorization", "cookie", "set-cookie", "x-api-key", "private_key", "database_url", "credential", "refresh_token"])
@pytest.mark.parametrize("container", ["dict", "list", "tuple"])
def test_v7_nested_redaction_handles_container_shapes(name, container):
    secret = "FWV7-CONTAINER-SECRET-3900"
    leaf = {name: secret}
    value = {"items": [leaf]} if container == "dict" else ([leaf] if container == "list" else (leaf,))
    output = str(redact_data(value))
    assert secret not in output

@pytest.mark.parametrize("credential", [
    "Bearer abcdefghijklmnop", "Basic YWJjZGVmZ2hpamts", "password='long secret value'",
    ("client_" + "secret" + "=" + "verylongsecretvalue"), "Cookie: sid=very-secret; theme=light",
    "Set-Cookie: sessionid=very-secret; HttpOnly", "token: very-secret-value",
    ("-----BEGIN " + "PRIVATE KEY-----\nMIIEvSECRET\n-----END " + "PRIVATE KEY-----"),
])
def test_v7_redact_text_removes_credential_patterns(credential):
    result = redact_text(credential)
    assert "very-secret" not in result
    assert "abcdefghijklmnop" not in result
    assert "YWJjZGVmZ2hpamts" not in result
    assert "MIIEvSECRET" not in result

@pytest.mark.parametrize("value", [None, True, False, 0, 1, 3.1415, [], {}, {"safe": "hello"}, ["one", "two"]])
def test_v7_redact_data_preserves_benign_non_secret_values(value):
    assert redact_data(value) == value

@pytest.mark.parametrize("url", [
    "https://example.test/path?lang=en", "https://example.test/a?x=1&y=two", "http://localhost:8000/health",
    "https://example.test/#safe-fragment", "https://example.test/?empty=",
])
def test_v7_benign_urls_do_not_trigger_credential_filter(url):
    assert not contains_sensitive_query(url)
