"""Deterministic adversarial URL/scope matrices; no external network is used."""
import pytest
from app.scope import ScopePolicy, ScopeViolation

@pytest.fixture
def scope():
    # Name deliberately plain so tests exercise the policy without DNS dependency.
    return ScopePolicy.from_root("https://app.example.test/", exclusions=["/admin", "/private/data"], allow_private_targets=True,
                                 allowed_hosts=["https://api.example.test:8443"])

SAFE_URLS = [
    "https://app.example.test/", "https://app.example.test/index.html",
    "https://app.example.test/a/b?lang=en", "https://app.example.test/search?q=hello",
    "https://app.example.test/assets/app.js", "https://app.example.test/api/v1/items?page=2",
    "https://app.example.test/about#team", "https://app.example.test/products/item-1",
    "https://app.example.test/a%20b", "https://app.example.test/a?utm_source=qa",
    "https://api.example.test:8443/", "https://api.example.test:8443/v1/health",
]
@pytest.mark.parametrize("url", SAFE_URLS)
def test_v6_safe_in_scope_url_matrix(scope, url):
    assert scope.is_allowed(url)
    assert scope.validate_url(url).startswith(("http://", "https://"))

BLOCKED_URLS = [
    "https://evil.example.test/", "https://app.example.test.evil.test/",
    "https://sub.app.example.test/", "https://api.example.test/",
    "https://api.example.test:9443/", "https://app.example.test:8443/",
    "ftp://app.example.test/", "file:///etc/passwd", "javascript:alert(1)",
    "data:text/html,hello", "//evil.example.test/path", "https://user@app.example.test/",
    "https://user:pass@app.example.test/", "https://app.example.test:0/",
    "https://app.example.test:65536/", "https://app.example.test:abc/",
    "https://app.example.test/a\\..\\admin", "https://app.example.test/a\nInjected: yes",
    "https://app.example.test/a\rInjected: yes", "https://app.example.test/\x00x",
    "https://app.example.test/x?token=secret", "https://app.example.test/x?access_token=secret",
    "https://app.example.test/x?session_id=secret", "https://app.example.test/x?client.secret=secret",
    "https://app.example.test/x?signature=signed-value", "https://app.example.test/x?password=pw",
    "https://app.example.test/admin", "https://app.example.test/admin/users",
    "https://app.example.test/public/%2e%2e/admin", "https://app.example.test/public/%252e%252e%252fadmin",
    "https://app.example.test/private/data/a", "https://app.example.test/private%2fdata/a",
    "https://app.example.test/private%252fdata/a", "http://evil.example.test/",
]
@pytest.mark.parametrize("url", BLOCKED_URLS)
def test_v6_blocked_scope_matrix(scope, url):
    assert not scope.is_allowed(url), url

@pytest.mark.parametrize("path", [
    "/admin", "/admin/", "/admin/x", "/a/../admin", "/a/%2e%2e/admin",
    "/a/%252e%252e%252fadmin", "/private/data", "/private%2fdata/x",
    "/private%252fdata/x", "/private/data/../../admin",
])
def test_v6_encoded_or_normalized_exclusions_are_enforced(scope, path):
    assert not scope.is_allowed("https://app.example.test" + path)

@pytest.mark.parametrize("path", ["/administrator", "/admin2", "/private/database", "/private/data-old", "/user/admin"])
def test_v6_exclusions_do_not_overmatch_neighbors(scope, path):
    assert scope.is_allowed("https://app.example.test" + path)

@pytest.mark.parametrize("value", [
    "https://app.example.test/a", "/inside", "../inside", "?page=2", "./child", "#fragment",
])
def test_v6_join_handles_relative_references(scope, value):
    joined = scope.join("https://app.example.test/base/", value)
    assert joined is None or scope.is_allowed(joined)

@pytest.mark.parametrize("value", [
    "https://evil.example.test/x", "//evil.example.test/x", "javascript:alert(1)",
    "https://app.example.test/admin/x", "https://app.example.test/x?token=secret",
])
def test_v6_join_rejects_external_or_disallowed_references(scope, value):
    assert scope.join("https://app.example.test/", value) is None

@pytest.mark.parametrize("root", [
    "", "app.example.test", "ftp://app.example.test/", "file:///etc/passwd", "javascript:alert(1)",
    "https:///missing", "https://user:secret@app.example.test/", "https://app.example.test:bad/",
    "https://app.example.test:0/", "https://app.example.test:65536/", "https://app.example.test\\admin",
    "https://app.example.test/\nHeader: x",
])
def test_v6_invalid_root_cases_fail_closed(root):
    with pytest.raises((ScopeViolation, ValueError)):
        ScopePolicy.from_root(root, allow_private_targets=True)

def test_v6_sensitive_query_in_root_is_rejected_before_request():
    target = "https://app.example.test/?token=secret"
    # v8 rejects the credential-bearing root during policy construction, before a scan can queue it.
    with pytest.raises(ScopeViolation):
        ScopePolicy.from_root(target, allow_private_targets=True)

@pytest.mark.parametrize("depth", range(1, 9))
def test_v6_exclusions_catch_deeply_encoded_dot_segments(depth):
    encoded = "../admin"
    for _ in range(depth):
        encoded = encoded.replace("%", "%25").replace(".", "%2e")
    policy = ScopePolicy.from_root("https://app.example.test/", exclusions=["/admin"], allow_private_targets=True)
    assert not policy.is_allowed("https://app.example.test/public/" + encoded)
