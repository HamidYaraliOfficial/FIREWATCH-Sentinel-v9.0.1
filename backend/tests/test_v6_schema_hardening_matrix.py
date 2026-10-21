"""Schema-boundary tests for scan settings and user-controlled headers."""
import pytest
from pydantic import ValidationError
from app.schemas import ScanCreate

@pytest.mark.parametrize("field,value", [
    ("max_pages", 1), ("max_pages", 5000), ("max_depth", 0), ("max_depth", 20),
    ("max_endpoints", 10), ("max_endpoints", 10000), ("request_delay_ms", 0),
    ("request_delay_ms", 10000), ("max_concurrency", 1), ("max_concurrency", 20),
])
def test_v6_numeric_schema_boundaries_accept(field, value):
    model = ScanCreate(target_url="https://example.test/", **{field: value})
    assert getattr(model, field) == value

@pytest.mark.parametrize("field,value", [
    ("max_pages", -1), ("max_pages", 5001), ("max_depth", -1), ("max_depth", 21),
    ("max_endpoints", 9), ("max_endpoints", 10001), ("request_delay_ms", -1),
    ("request_delay_ms", 10001), ("max_concurrency", 0), ("max_concurrency", 21),
])
def test_v6_numeric_schema_boundaries_reject(field, value):
    with pytest.raises(ValidationError):
        ScanCreate(target_url="https://example.test/", **{field: value})

@pytest.mark.parametrize("header", [
    "Host", "Content-Length", "Transfer-Encoding", "Connection", "Proxy-Authorization",
    "Proxy-Connection", "Upgrade", "TE", "Trailer",
])
def test_v6_request_headers_cannot_override_transport_headers(header):
    with pytest.raises(ValidationError):
        ScanCreate(target_url="https://example.test/", request_headers={header: "test"})

@pytest.mark.parametrize("value", ["a\nb", "a\rb", "\r\nInjected: yes"])
def test_v6_header_value_newline_injection_is_rejected(value):
    with pytest.raises(ValidationError):
        ScanCreate(target_url="https://example.test/", request_headers={"X-Test": value})

@pytest.mark.parametrize("name", ["X-Test\nHost", "X-Test\rHost", "\n", "a" * 101])
def test_v6_header_name_malformed_values_are_rejected(name):
    with pytest.raises(ValidationError):
        ScanCreate(target_url="https://example.test/", request_headers={name: "v"})

@pytest.mark.parametrize("profile", ["baseline", "standard", "comprehensive"])
def test_v6_profiles_stay_within_server_bounds(profile):
    model = ScanCreate(target_url="https://example.test/", profile=profile)
    assert 1 <= model.max_pages <= 5000
    assert 0 <= model.max_depth <= 20
    assert 10 <= model.max_endpoints <= 10000
    assert 1 <= model.max_concurrency <= 20

@pytest.mark.parametrize("profile", ["default", "passive", "active", "full", "../../scope", "STANDARD", ""])
def test_v6_unknown_profiles_are_rejected(profile):
    with pytest.raises(ValidationError):
        ScanCreate(target_url="https://example.test/", profile=profile)

@pytest.mark.parametrize("headers", [
    {"Authorization": "Bearer x\nX-Evil: y"},
    {"Cookie": "sid=x\r\nX-Evil: y"},
    {"Host": "example.test"},
    {"Content-Length": "1"},
    {"Proxy-Authorization": "Basic c2VjcmV0"},
])
def test_v6_profile_headers_enforce_transport_and_newline_limits(headers):
    with pytest.raises(ValidationError):
        ScanCreate(target_url="https://example.test/", authorization_profiles=[{"name": "tester", "headers": headers}])
