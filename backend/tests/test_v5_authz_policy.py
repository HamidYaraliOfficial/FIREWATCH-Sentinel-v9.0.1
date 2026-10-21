import pytest
from app.authz import AuthProfile, review_authorization, SENSITIVE_PATH_HINTS
from app.scope import ScopePolicy

def test_authorization_review_needs_two_profiles():
    import asyncio
    scope=ScopePolicy.from_root('https://app.example.test/',allow_private_targets=True)
    result=asyncio.run(review_authorization(scope,['https://app.example.test/admin/users'],[AuthProfile('user',{})]))
    assert result==[]

def test_authorization_path_hints_are_nonempty_and_unique():
    assert len(SENSITIVE_PATH_HINTS)>=8
    assert len(SENSITIVE_PATH_HINTS)==len(set(SENSITIVE_PATH_HINTS))
    assert all(x.startswith('/') for x in SENSITIVE_PATH_HINTS)

@pytest.mark.parametrize('path', ['/admin','/management','/internal','/users/1','/orders/1','/billing','/invoices'])
def test_sensitive_path_hints_include_common_sensitive_paths(path):
    assert any(hint in path for hint in SENSITIVE_PATH_HINTS)

@pytest.mark.parametrize('name', ['user','member','anonymous','least-privilege','low','admin','privileged','administrator'])
def test_profile_name_handling_does_not_throw(name):
    profile=AuthProfile(name,{'Authorization':'Bearer test-not-real'})
    assert profile.name==name and isinstance(profile.headers,dict)
