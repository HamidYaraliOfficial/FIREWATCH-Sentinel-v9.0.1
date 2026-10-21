"""Secret redaction property matrix across encodings, containers and URL wrappers."""
from urllib.parse import quote
import json
import pytest
from app.redaction import redact_url, redact_text, redact_data, contains_sensitive_query, SENSITIVE_QUERY_NAMES, SENSITIVE_FIELD_NAMES

_SECRET = "FWV8-SECRET-MUST-NOT-LEAK-9A7F31"
_NAMES = sorted(SENSITIVE_QUERY_NAMES)

@pytest.mark.parametrize("name", _NAMES)
@pytest.mark.parametrize("encoding_depth", range(0, 5))
def test_v8_sensitive_query_name_and_value_are_redacted(name, encoding_depth):
    key=name; value=_SECRET
    for _ in range(encoding_depth): key=quote(key, safe=""); value=quote(value, safe="")
    # Query parsing decodes one layer as normal browsers/proxies do; only assert when the key remains identifiable.
    url=f"https://target.example.test/path?{key}={value}"
    rendered=redact_url(url)
    assert _SECRET not in rendered

@pytest.mark.parametrize("name", sorted(SENSITIVE_FIELD_NAMES))
@pytest.mark.parametrize("shape", ["mapping", "nested-list", "nested-tuple"])
def test_v8_sensitive_fields_are_redacted_in_arbitrary_supported_shapes(name, shape):
    leaf={name:_SECRET, "ordinary":"kept"}
    data=leaf if shape=="mapping" else {"outer":[leaf]} if shape=="nested-list" else (leaf,)
    rendered=json.dumps(redact_data(data), default=str)
    assert _SECRET not in rendered
    assert "kept" in rendered

@pytest.mark.parametrize("wrapper_depth", range(0, 6))
@pytest.mark.parametrize("parameter", ["next", "return_to", "redirect", "continue", "callback", "destination"])
def test_v8_nested_redirect_url_secrets_are_not_persisted(wrapper_depth, parameter):
    inner=f"https://identity.example.test/oauth?access_token={_SECRET}&state=safe"
    for _ in range(wrapper_depth): inner=f"https://app.example.test/redirect?{parameter}="+quote(inner,safe="")
    rendered=redact_url(inner)
    assert _SECRET not in rendered

@pytest.mark.parametrize("text", [
    f"Authorization: Bearer {_SECRET}", f"token={_SECRET}", f"password: {_SECRET}",
    f"https://app.example.test/?token={_SECRET}", f"Cookie: session={_SECRET}; mode=light",
    f"Set-Cookie: id={_SECRET}; HttpOnly", f"client_secret='{_SECRET}'",
])
def test_v8_secret_sentinels_do_not_survive_text_redaction(text):
    assert _SECRET not in redact_text(text)

@pytest.mark.parametrize("url", [
    "https://site.example.test/?locale=en", "https://site.example.test/?page=3&sort=asc",
    "https://site.example.test/path", "https://site.example.test/#anchor", "https://site.example.test/?empty=",
])
def test_v8_safe_urls_are_not_blanket_redacted(url):
    output=redact_url(url)
    assert "[URL REDACTED]" not in output
    assert "[REDACTED]" not in output

@pytest.mark.parametrize("benign", [None, True, False, 0, 2.5, "ordinary", [], {}, {"count": 4}, ["a", "b"]])
def test_v8_redaction_preserves_benign_values(benign):
    assert redact_data(benign) == benign

@pytest.mark.parametrize("url", ["https://site.example.test/?token=x", "https://site.example.test/?access_token=x", "https://site.example.test/?api_key=x", "https://site.example.test/?password=x"])
def test_v8_sensitive_query_detector_refuses_known_credentials(url):
    assert contains_sensitive_query(url)
