"""Scan schema bounds, profile defaults and malformed input rejection matrix."""
import pytest
from pydantic import ValidationError
from app.schemas import ScanCreate

BASE={"target_url":"https://app.example.test/","scope_acknowledged":True}
NUMERIC={"max_pages":(1,5000),"max_depth":(0,20),"max_endpoints":(10,10000),"request_delay_ms":(0,10000),"max_concurrency":(1,20)}

@pytest.mark.parametrize("field,bounds", list(NUMERIC.items()))
@pytest.mark.parametrize("value", [0, 1, 2, 9, 10, 19, 20, 99, 100, 499, 500, 999, 1000, 1999, 2000, 4999, 5000, 7000, 9999, 10000])
def test_v8_numeric_schema_acceptance_is_exactly_within_declared_bounds(field,bounds,value):
    low,high=bounds
    if low <= value <= high:
        assert getattr(ScanCreate(**BASE,**{field:value}),field)==value
    else:
        with pytest.raises(ValidationError): ScanCreate(**BASE,**{field:value})

@pytest.mark.parametrize("profile", ["baseline","standard","comprehensive"])
def test_v8_profiles_keep_bounded_defaults(profile):
    item=ScanCreate(**BASE,profile=profile)
    assert 1 <= item.max_pages <= 5000
    assert 0 <= item.max_depth <= 20
    assert 10 <= item.max_endpoints <= 10000
    assert 1 <= item.max_concurrency <= 20

@pytest.mark.parametrize("profile", ["", "admin", "fast", "active", "STANDARD", "comprehensive;drop", "../standard", "none", "all", "full", "passive-only", "baseline ", " standard"])
def test_v8_unrecognized_profiles_rejected(profile):
    with pytest.raises(ValidationError): ScanCreate(**BASE,profile=profile)

@pytest.mark.parametrize("target", ["", "relative/path", "//example.test/path", "ftp://example.test/", "javascript:alert(1)", "data:text/html,x", "http://", "https://user:pass@example.test/", "https://example.test:bad/", "https://example.test:99999/"])
def test_v8_invalid_target_url_shapes_rejected(target):
    with pytest.raises(ValidationError): ScanCreate(**(BASE | {"target_url": target}))

@pytest.mark.parametrize("count", [201, 250, 500])
def test_v8_exclusion_count_over_cap_rejected(count):
    with pytest.raises(ValidationError): ScanCreate(**BASE,exclusions=[f"/private-{i}" for i in range(count)])

@pytest.mark.parametrize("count", [0, 1, 10, 20])
def test_v8_allowed_host_count_at_schema_cap(count):
    items=[f"https://api-{i}.example.test" for i in range(count)]
    assert len(ScanCreate(**BASE,allowed_hosts=items).allowed_hosts)==count

@pytest.mark.parametrize("count", [21, 25, 100])
def test_v8_allowed_host_count_over_cap_rejected(count):
    with pytest.raises(ValidationError): ScanCreate(**BASE,allowed_hosts=[f"https://api-{i}.example.test" for i in range(count)])

@pytest.mark.parametrize("notes", [None,"","safe note","x"*1000,"فارسی: آزمایش","line\twith tab"])
def test_v8_scan_notes_allow_benign_text(notes):
    assert ScanCreate(**BASE,notes=notes).notes==notes

@pytest.mark.parametrize("target", [
    "https://app.example.test/?token=secret",
    "https://app.example.test/?access_token=secret",
    "https://app.example.test/?api_key=secret",
    "https://app.example.test/?client_secret=secret",
    "https://app.example.test/?sessionid=secret",
    "https://app.example.test/?password=secret",
])
def test_v8_scan_schema_rejects_credential_like_target_query(target):
    with pytest.raises(ValidationError):
        ScanCreate(**(BASE | {"target_url": target}))

@pytest.mark.parametrize("headers", [
    {"Authorization": "Bearer a", "authorization": "Bearer b"},
    {"Cookie": "sid=a", "cookie": "sid=b"},
    {"X-API-Key": "a", "x-api-key": "b"},
])
def test_v8_scan_schema_rejects_case_insensitive_duplicate_auth_headers(headers):
    with pytest.raises(ValidationError):
        ScanCreate(**BASE, request_headers=headers)
