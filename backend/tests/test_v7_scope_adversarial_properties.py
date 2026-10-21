"""Large deterministic adversarial matrix for URL and scope policy invariants."""
from urllib.parse import quote
import pytest
from app.scope import ScopePolicy, ScopeViolation, _policy_path

@pytest.fixture

def scope():
    return ScopePolicy.from_root(
        "https://app.example.test/", exclusions=["/admin", "/logout", "/internal/*"],
        allow_private_targets=True,
        allowed_hosts=["https://api.example.test:8443"],
    )

_EXCLUDED_BASES = ["/admin", "/admin/", "/admin/users", "/logout", "/internal/a", "/internal/nested/delete"]

def _encode_layers(value: str, layers: int) -> str:
    for _ in range(layers):
        value = quote(value, safe="")
    return value

@pytest.mark.parametrize("base", _EXCLUDED_BASES)
@pytest.mark.parametrize("layers", range(0, 9))
def test_v7_multi_layer_encoded_exclusions_fail_closed(scope, base, layers):
    # 7 x 9 = 63 independently collected policy regression cases.
    path = _encode_layers(base, layers)
    assert not scope.is_allowed("https://app.example.test" + path)

@pytest.mark.parametrize("suffix", ["", "/", "/users", "/users/42", "/settings", "/reports", "/health"])
@pytest.mark.parametrize("prefix", ["/admin", "/logout", "/internal"])
def test_v7_exclusion_prefix_does_not_overmatch_neighbor_paths(scope, suffix, prefix):
    path = prefix + "-public" + suffix
    assert scope.is_allowed("https://app.example.test" + path)

@pytest.mark.parametrize("depth", range(1, 31))
def test_v7_path_policy_normalization_is_idempotent(depth):
    raw = "/a/" + ("x/../" * depth) + "safe"
    once = _policy_path(raw)
    twice = _policy_path(once)
    assert once == twice
    assert once.startswith("/")
    assert ".." not in once.split("/")

@pytest.mark.parametrize("port", range(1, 65536, 257))
def test_v7_explicit_port_policy_is_exact(port):
    pol = ScopePolicy.from_root(f"https://app.example.test:{port}/", allow_private_targets=True)
    assert pol.is_allowed(f"https://app.example.test:{port}/")
    other = 1 if port != 1 else 2
    assert not pol.is_allowed(f"https://app.example.test:{other}/")

@pytest.mark.parametrize("raw", [
    "javascript:alert(1)", "data:text/html,hi", "file:///etc/passwd", "//evil.example/path",
    "https://user:pass@app.example.test/", "https://app.example.test:0/", "https://app.example.test:99999/",
    "https://app.example.test/\nX-Injected: yes", "https://app.example.test/\\admin",
    "https://app.example.test/?access_token=secret", "https://evil.example.test/", "https://api.example.test/",
    "https://api.example.test:8443/", "https://app.example.test/%00", "https://app.example.test/#fragment",
])
def test_v7_edge_urls_match_the_documented_scope_contract(scope, raw):
    if "#fragment" in raw:
        # Fragments are never sent to servers and normalize away.
        assert scope.validate_url(raw).endswith("/")
    elif raw == "https://api.example.test:8443/":
        assert scope.is_allowed(raw)
    elif raw == "https://api.example.test/":
        assert not scope.is_allowed(raw)
    elif raw == "https://app.example.test/%00":
        assert scope.is_allowed(raw)
    else:
        assert not scope.is_allowed(raw)

@pytest.mark.parametrize("name,value", [(f"utm_{x}", f"campaign-{x}") for x in range(80)])
def test_v7_tracking_parameter_removal_is_stable(scope, name, value):
    normalized = scope.validate_url(f"https://app.example.test/products?{name}={value}&keep=1")
    assert name not in normalized
    assert "keep=1" in normalized

@pytest.mark.parametrize("suffix", ["/", "/api", "/api/v1/users", "/health", "/search?q=abc", "/docs?lang=en"])
def test_v7_safe_relative_join_stays_in_scope(scope, suffix):
    assert scope.join(scope.root_url, suffix) is not None
    assert "evil.example" not in scope.join(scope.root_url, suffix)

@pytest.mark.parametrize("external", [
    "https://evil.example/", "http://evil.example/", "//evil.example/", "\\\\evil.example\\x",
    "https://app.example.test.evil.example/", "https://app.example.test@evil.example/",
    "javascript:alert(1)", "data:text/html,hello", "file:///etc/passwd",
])
def test_v7_external_join_attempts_are_rejected(scope, external):
    assert scope.join(scope.root_url, external) is None
