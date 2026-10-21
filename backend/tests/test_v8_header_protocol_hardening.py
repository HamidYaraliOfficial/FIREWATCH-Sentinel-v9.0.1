"""v8 tests for HTTP field syntax, duplicate headers and control-character rejection."""
import pytest
from pydantic import ValidationError
from app.schemas import ScanCreate, _validate_header_map

BASE = {"target_url": "https://example.test/", "scope_acknowledged": True}
FORBIDDEN = ["Host", "Content-Length", "Transfer-Encoding", "Connection", "Proxy-Authorization", "Proxy-Connection", "Upgrade", "TE", "Trailer"]

@pytest.mark.parametrize("name", ["X-Test", "Accept", "Accept-Language", "Authorization", "Cookie", "X-API-Key", "If-None-Match", "X_Trace", "X+Trace", "X.Trace", "X^Trace", "X|Trace", "X~Trace", "X'Trace", "X#Trace", "X$Trace", "X%Trace", "X&Trace", "X*Trace", "X!Trace", "X-Trace", "X_Trace", "X.Trace"])
def test_v8_supported_rfc_token_header_names(name):
    model = ScanCreate(**BASE, request_headers={name: "safe-value"})
    assert model.request_headers[name] == "safe-value"

@pytest.mark.parametrize("bad", ["", " leading", "trailing ", "X Test", "X:Value", "X/Value", "X\\Value", "X(Value)", "X[Value]", "X{Value}", "X\x00Value", "X\x01Value", "X\x1fValue", "X\x7fValue", "éX", "X\u200b", "\rX", "\nX", "X\tY", "X\u2028Y", "X\u2029Y", "A"*101])
def test_v8_invalid_header_name_characters_fail_closed(bad):
    with pytest.raises(ValidationError):
        ScanCreate(**BASE, request_headers={bad: "x"})

@pytest.mark.parametrize("char_code", [*range(0, 9), *range(10, 32), 127])
def test_v8_header_values_reject_control_characters_except_tab(char_code):
    ch = chr(char_code)
    with pytest.raises(ValidationError):
        ScanCreate(**BASE, request_headers={"X-Test": "before" + ch + "after"})

@pytest.mark.parametrize("value", ["", "ok", "simple text", "unicode فارسی", "line\tseparated", "a"*8191, "b"*8192])
def test_v8_valid_header_values_preserve_allowed_text(value):
    parsed = ScanCreate(**BASE, request_headers={"X-Test": value})
    assert parsed.request_headers["X-Test"] == value

@pytest.mark.parametrize("value", ["a"*8193, "bad\rvalue", "bad\nvalue", "nul\x00value", "del\x7fvalue", "escape\x1bvalue"])
def test_v8_invalid_header_values_are_rejected(value):
    with pytest.raises(ValidationError):
        ScanCreate(**BASE, request_headers={"X-Test": value})

@pytest.mark.parametrize("name", FORBIDDEN)
@pytest.mark.parametrize("variant", [str.lower, str.upper, str.title])
def test_v8_forbidden_transport_headers_rejected_case_insensitively(name, variant):
    with pytest.raises(ValidationError):
        ScanCreate(**BASE, request_headers={variant(name): "unsafe"})

@pytest.mark.parametrize("keys", [
    {"Authorization": "Bearer one", "authorization": "Bearer two"},
    {"Cookie": "sid=one", "COOKIE": "sid=two"},
    {"X-API-Key": "one", "x-api-key": "two"},
    {"ACCEPT": "a", "accept": "b"},
])
def test_v8_case_insensitive_duplicate_header_names_are_rejected(keys):
    with pytest.raises(ValidationError):
        ScanCreate(**BASE, request_headers=keys)

@pytest.mark.parametrize("header_key", ["X-Test", "Authorization", "Cookie", "X-API-Key", "X-Trace-Id"])
@pytest.mark.parametrize("control", ["\r", "\n", "\x00", "\x01", "\x1b", "\x7f"])
def test_v8_authorization_profile_values_cannot_smuggle_controls(header_key, control):
    with pytest.raises(ValidationError):
        ScanCreate(**BASE, authorization_profiles=[{"name": "reviewer", "headers": {header_key: "ok" + control + "bad"}}])

@pytest.mark.parametrize("headers", [
    {"Authorization": "Bearer test", "X-Request-ID": "123"},
    {"Cookie": "session=synthetic", "Accept": "application/json"},
    {"X-Trace": "tab\tallowed"},
])
def test_v8_authorization_profiles_accept_valid_header_maps(headers):
    model = ScanCreate(**BASE, authorization_profiles=[{"name": "reviewer", "headers": headers}])
    assert model.authorization_profiles[0]["headers"] == headers

@pytest.mark.parametrize("names", [["admin", "ADMIN"], ["User", "user"], ["reviewer", " reviewer "]])
def test_v8_duplicate_authorization_profile_names_are_rejected(names):
    with pytest.raises(ValidationError):
        ScanCreate(**BASE, authorization_profiles=[{"name": names[0]}, {"name": names[1]}])

@pytest.mark.parametrize("count", [0, 1, 2, 10])
def test_v8_authorization_profile_count_within_cap_is_accepted(count):
    model = ScanCreate(**BASE, authorization_profiles=[{"name": f"role-{i}", "headers": {}} for i in range(count)])
    assert len(model.authorization_profiles) == count

@pytest.mark.parametrize("count", [11, 12, 20])
def test_v8_authorization_profile_count_over_cap_is_rejected(count):
    with pytest.raises(ValidationError):
        ScanCreate(**BASE, authorization_profiles=[{"name": f"role-{i}", "headers": {}} for i in range(count)])
