"""v8 deterministic adversarial URL and scope normalization matrix."""
from urllib.parse import quote
import pytest
from app.scope import ScopePolicy, ScopeViolation, _policy_path

@pytest.fixture
def policy():
    return ScopePolicy.from_root("https://app.example.test/", exclusions=["/admin", "/logout", "/internal/*", "/billing/*"], allow_private_targets=True,
        allowed_hosts=["https://api.example.test:8443"])

@pytest.mark.parametrize("scheme", ["http", "https", "HTTP", "HTTPS", "ftp", "file", "javascript", "data", "ws", "wss", "gopher", "mailto"])
@pytest.mark.parametrize("host", ["app.example.test", "evil.example.test", "app.example.test.evil.test", "app.example.test@evil.test"])
def test_v8_scheme_host_cross_product_only_accepts_configured_http_origins(policy, scheme, host):
    raw = f"{scheme}://{host}/safe"
    if scheme.lower() in {"http", "https"} and host == "app.example.test":
        assert policy.is_allowed(raw)
    else:
        assert not policy.is_allowed(raw)

@pytest.mark.parametrize("port", [-1, 0, 1, 2, 79, 80, 81, 443, 444, 8443, 65535, 65536, 99999])
def test_v8_port_boundary_fail_closed(policy, port):
    raw = f"https://app.example.test:{port}/safe"
    # The root configured an implicit HTTPS origin, which permits conventional HTTP/HTTPS ports for passive mixed-content inventory.
    assert policy.is_allowed(raw) is (port in {80, 443})

@pytest.mark.parametrize("path", ["/admin", "/admin/", "/admin/users", "/ADMIN", "/logout", "/logout/", "/internal", "/internal/", "/internal/a", "/internal/nested/a", "/billing", "/billing/invoice", "/billing/nested/1"])
def test_v8_exclusions_cover_exact_paths_and_descendants(policy, path):
    assert not policy.is_allowed("https://app.example.test" + path)

@pytest.mark.parametrize("path", ["/administrator", "/admin-public", "/logout-history", "/internal-public/a", "/billing-help", "/public/internal/a", "/safe", "/api/users", "/billing2"])
def test_v8_exclusions_do_not_capture_unrelated_siblings(policy, path):
    assert policy.is_allowed("https://app.example.test" + path)

@pytest.mark.parametrize("target", ["https://api.example.test:8443/", "https://API.EXAMPLE.TEST:8443/v1", "https://api.example.test:443/", "https://api.example.test/", "http://api.example.test:8443/"])
def test_v8_extra_origins_require_exact_scheme_host_port(policy, target):
    assert policy.is_allowed(target) is (target.startswith("https://api.example.test:8443/") or target.startswith("https://API.EXAMPLE.TEST:8443/"))

@pytest.mark.parametrize("raw", [
    "", " /path", "/relative", "//evil.test", "https:/broken", "https://", "http://?q=1",
    "javascript:alert(1)", "data:text/html,x", "file:///etc/passwd", "https://user@app.example.test/",
    "https://:443/", "https://app.example.test:99999/", "https://app.example.test:0/",
    "https://app.example.test/with space", "https://app.example.test/\\admin", "https://app.example.test/\nX: y",
    "https://app.example.test/?token=x", "https://app.example.test/?access_token=x", "https://app.example.test/?session=x",
])
def test_v8_malformed_or_credential_bearing_urls_raise(raw, policy):
    with pytest.raises(ScopeViolation):
        policy.validate_url(raw)

@pytest.mark.parametrize("depth", range(1, 13))
@pytest.mark.parametrize("segment", [".", "..", "%2e", "%2E%2e", "%252e%252e", "%2fadmin", "%252fadmin"])
def test_v8_encoded_traversal_policy_comparison_is_deterministic(depth, segment):
    raw = "/a/" + (segment + "/") * depth + "safe"
    canonical = _policy_path(raw)
    assert canonical.startswith("/")
    assert _policy_path(canonical) == canonical

@pytest.mark.parametrize("query", ["?utm_source=x", "?gclid=x", "?fbclid=x", "?lang=en", "?page=2", "?x=1&y=2", "?empty=", "?utm_campaign=a&lang=en"])
def test_v8_query_cleaning_only_removes_tracking_keys(query, policy):
    value = policy.validate_url("https://app.example.test/path" + query)
    assert "utm_" not in value.lower() and "gclid=" not in value and "fbclid=" not in value
    if "lang=en" in query: assert "lang=en" in value
    if "page=2" in query: assert "page=2" in value

@pytest.mark.parametrize("value", ["/safe", "../safe", "./safe", "?page=2", "#section", "api/users", "https://app.example.test/api", "https://evil.test/", "//evil.test/x", "javascript:alert(1)", "data:text/plain,x"])
def test_v8_join_never_returns_out_of_scope_target(policy, value):
    joined = policy.join(policy.root_url, value)
    if joined is not None:
        assert policy.is_allowed(joined)

@pytest.mark.parametrize("host", ["127.0.0.1", "localhost", "::1", "169.254.169.254", "10.0.0.1", "192.168.1.10", "172.16.0.1", "224.0.0.1"])
def test_v8_private_and_special_ip_literals_are_blocked_by_default(host):
    with pytest.raises(ScopeViolation):
        ScopePolicy.from_root(f"http://{f'[{host}]' if ':' in host else host}/")

@pytest.mark.parametrize("url", [
    "https://app.example.test/?token=secret",
    "https://app.example.test/?access_token=secret",
    "https://app.example.test/?sessionid=secret",
    "https://app.example.test/?client_secret=secret",
    "https://app.example.test/path with space",
    "https://app.example.test/\\path",
])
def test_v8_root_policy_refuses_secret_urls_and_raw_whitespace(url):
    with pytest.raises(ScopeViolation):
        ScopePolicy.from_root(url, allow_private_targets=True)

@pytest.mark.parametrize("target", [
    "https://api.example.test:8443/", "https://API.EXAMPLE.TEST:8443/a",
    "http://api.example.test:8443/", "https://api.example.test:443/",
])
def test_v8_explicit_allowed_host_preserves_configured_scheme_and_port(target):
    p = ScopePolicy.from_root("https://app.example.test/", allow_private_targets=True,
        allowed_hosts=["https://api.example.test:8443"])
    assert p.is_allowed(target) is (target.lower().startswith("https://api.example.test:8443/"))
