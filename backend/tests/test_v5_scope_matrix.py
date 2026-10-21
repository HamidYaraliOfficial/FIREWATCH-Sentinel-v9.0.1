import pytest
from app.scope import ScopePolicy, ScopeViolation

@pytest.fixture
def scope():
    return ScopePolicy.from_root('https://app.example.test/', allowed_hosts=['api.example.test'], exclusions=['/admin','/private/data'], allow_private_targets=True)

@pytest.mark.parametrize('url', [
 'https://app.example.test/','https://app.example.test/home','https://app.example.test/a?lang=en',
 'https://api.example.test/v1/users','https://app.example.test/administrator','https://APP.EXAMPLE.TEST/UPPER',
 'http://app.example.test/','https://api.example.test/health','https://app.example.test/public/%2e%2e/profile',
 'https://app.example.test/a?utm_source=newsletter','https://app.example.test/a?gclid=abc',
])
def test_allowed_scope_urls(scope,url):
    assert scope.is_allowed(url)

@pytest.mark.parametrize('url', [
 'https://evil.example.test/','https://app.example.test:8443/','ftp://app.example.test/',
 'javascript:alert(1)','//evil.example.test/a','https://user:pass@app.example.test/',
 'https://app.example.test/admin','https://app.example.test/admin/users',
 'https://app.example.test/private/data/a','https://app.example.test/x?token=abc',
 'https://app.example.test/x?session-id=abc','https://app.example.test/a\\..\\admin',
 'https://app.example.test/a\nX-Injected: yes','https://app.example.test:99999/',
])
def test_scope_rejects_invalid_or_out_of_scope_urls(scope,url):
    assert not scope.is_allowed(url)
    with pytest.raises(ScopeViolation):
        scope.validate_url(url)

@pytest.mark.parametrize('root', [
 'ftp://app.example.test/','https:///missing-host','https://user:password@app.example.test/',
 'https://app.example.test:notaport/','file:///etc/passwd','javascript:alert(1)',
])
def test_invalid_roots_rejected(root):
    with pytest.raises((ScopeViolation, ValueError)):
        ScopePolicy.from_root(root, allow_private_targets=True)

@pytest.mark.parametrize('path', ['/admin','/admin/','/admin/users','/private/data','/private/data/1'])
def test_exclusions_are_prefix_boundary_aware(path,scope):
    assert not scope.is_allowed('https://app.example.test'+path)

@pytest.mark.parametrize('path', ['/administrator','/admin2','/private/database','/private/data-old'])
def test_exclusions_do_not_match_neighboring_names(path,scope):
    assert scope.is_allowed('https://app.example.test'+path)

@pytest.mark.parametrize('port', [0,65536,-1,65535])
def test_explicit_ports_have_bounds(port):
    if 1 <= port <= 65535:
        p=ScopePolicy.from_root(f'https://app.example.test:{port}/', allow_private_targets=True)
        assert p.is_allowed(f'https://app.example.test:{port}/')
    else:
        with pytest.raises((ScopeViolation, ValueError)):
            ScopePolicy.from_root(f'https://app.example.test:{port}/', allow_private_targets=True)
