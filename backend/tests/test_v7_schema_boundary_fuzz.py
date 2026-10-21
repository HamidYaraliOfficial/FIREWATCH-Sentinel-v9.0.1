"""High-volume but bounded ScanCreate input, profile, and header validation matrix."""
import pytest
from pydantic import ValidationError
from app.schemas import ScanCreate

_BASE = {"target_url": "https://example.test/", "scope_acknowledged": True}

@pytest.mark.parametrize("profile", ["baseline", "standard", "comprehensive"])
def test_v7_profile_defaults_are_consistent(profile):
    model = ScanCreate(**_BASE, profile=profile)
    assert 1 <= model.max_pages <= 5000
    assert 0 <= model.max_depth <= 20
    assert 10 <= model.max_endpoints <= 10000
    assert 1 <= model.max_concurrency <= 20
    assert model.profile == profile

@pytest.mark.parametrize("field,minimum,maximum", [
    ("max_pages",1,5000), ("max_depth",0,20), ("max_endpoints",10,10000),
    ("request_delay_ms",0,10000), ("max_concurrency",1,20),
])
def test_v7_numeric_fields_accept_all_boundary_slices(field, minimum, maximum):
    values = sorted(set([minimum, maximum, (minimum+maximum)//2, minimum+1 if minimum < maximum else minimum, maximum-1 if minimum < maximum else maximum]))
    for value in values:
        assert getattr(ScanCreate(**_BASE, **{field:value}), field) == value

@pytest.mark.parametrize("field,minimum,maximum", [
    ("max_pages",1,5000), ("max_depth",0,20), ("max_endpoints",10,10000),
    ("request_delay_ms",0,10000), ("max_concurrency",1,20),
])
@pytest.mark.parametrize("delta", [-100000, -1, 1, 100000])
def test_v7_numeric_schema_rejects_outside_boundaries(field, minimum, maximum, delta):
    value = (minimum - abs(delta)) if delta < 0 else (maximum + abs(delta))
    with pytest.raises(ValidationError):
        ScanCreate(**_BASE, **{field:value})

@pytest.mark.parametrize("key", ["Host", "Content-Length", "Transfer-Encoding", "Connection", "Upgrade", "TE", "Trailer", "Proxy-Authorization", "Proxy-Connection"])
@pytest.mark.parametrize("variant", [lambda x:x, lambda x:x.lower(), lambda x:x.upper(), lambda x:" "+x+" "])
def test_v7_dangerous_header_variants_are_rejected(key, variant):
    with pytest.raises(ValidationError):
        ScanCreate(**_BASE, request_headers={variant(key): "controlled"})

@pytest.mark.parametrize("name", ["X-Test", "Authorization", "Cookie", "X-API-Key", "X-Trace-Id", "Accept-Language"])
@pytest.mark.parametrize("value", ["", "ok", "a"*255, "b"*2048, "c"*8192])
def test_v7_normal_header_values_fit_schema_limits(name, value):
    model = ScanCreate(**_BASE, request_headers={name:value})
    assert model.request_headers[name] == value

@pytest.mark.parametrize("value", ["line1\nline2", "line1\rline2", "x\r\nInjected: true", "\n", "\r"])
def test_v7_header_newline_injection_is_rejected(value):
    with pytest.raises(ValidationError):
        ScanCreate(**_BASE, request_headers={"X-Test": value})

@pytest.mark.parametrize("profile", ["", "admin", "fast", "active", "standard;drop", "../baseline", "STANDARD", "none", "all", "full", "passive-only"])
def test_v7_unknown_scan_profiles_fail_closed(profile):
    with pytest.raises(ValidationError):
        ScanCreate(**_BASE, profile=profile)


@pytest.mark.parametrize("key", ["Host", "Content-Length", "Transfer-Encoding", "Connection", "Upgrade", "TE", "Trailer", "Proxy-Authorization", "Proxy-Connection"])
@pytest.mark.parametrize("variant", [lambda x:x, lambda x:x.lower(), lambda x:x.upper(), lambda x:" "+x+" "])
def test_v7_authorization_profile_forbidden_header_variants_are_rejected(key, variant):
    with pytest.raises(ValidationError):
        ScanCreate(**_BASE, authorization_profiles=[{"name":"tester", "headers":{variant(key):"unsafe"}}])
