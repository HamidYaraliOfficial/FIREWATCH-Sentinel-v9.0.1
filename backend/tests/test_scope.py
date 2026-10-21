from app.scope import ScopePolicy, ScopeViolation
import pytest

def test_scope_same_host():
    s=ScopePolicy.from_root('http://example.com/',allow_private_targets=True)
    assert s.is_allowed('http://example.com/a')
    assert not s.is_allowed('http://evil.example/a')

def test_exclusion():
    s=ScopePolicy.from_root('http://example.com/',exclusions=['/admin'],allow_private_targets=True)
    with pytest.raises(ScopeViolation): s.validate_url('http://example.com/admin/users')
