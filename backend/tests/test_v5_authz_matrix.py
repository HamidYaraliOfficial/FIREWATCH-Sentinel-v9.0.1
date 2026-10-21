import asyncio
from types import SimpleNamespace
from unittest.mock import patch
import pytest
from app.authz import AuthProfile, review_authorization

class FakeScopedClient:
    responder = None
    calls = []
    def __init__(self, scope, delay_ms=0):
        self.scope=scope; self.delay_ms=delay_ms
    async def __aenter__(self): return self
    async def __aexit__(self,*_): return None
    async def request(self,method,url,headers=None):
        type(self).calls.append((method,url,dict(headers or {})))
        if type(self).responder: return type(self).responder(method,url,dict(headers or {}))
        return SimpleNamespace(error=False,status_code=200,body='{"email":"a@example.test","role":"user"}',body_sha256='same')

def scope_allowing(urls):
    allowed=set(urls)
    return SimpleNamespace(is_allowed=lambda u: u in allowed)

def profiles():
    return [AuthProfile('admin',{'Authorization':'admin-test'}),AuthProfile('user',{'Authorization':'user-test'})]

def test_authz_reviews_only_sensitive_in_scope_paths_and_uses_get_only():
    urls=['https://app.example.test/admin/users/9','https://app.example.test/products/2','https://outside.invalid/admin/users/1']
    scope=scope_allowing(urls[:2])
    FakeScopedClient.calls=[]; FakeScopedClient.responder=None
    with patch('app.authz.SafeHTTPClient',FakeScopedClient):
        findings=asyncio.run(review_authorization(scope,urls,profiles(),delay_ms=0))
    assert len(findings)==1
    assert findings[0].rule_id=='FW-AUTHZ-001'
    assert findings[0].endpoint==urls[0]
    assert findings[0].evidence['methods_used']==['GET']
    assert len(FakeScopedClient.calls)==2
    assert {call[0] for call in FakeScopedClient.calls}=={'GET'}
    assert {call[2]['Authorization'] for call in FakeScopedClient.calls}=={'admin-test','user-test'}

def test_authz_does_not_run_with_fewer_than_two_profiles():
    FakeScopedClient.calls=[]
    with patch('app.authz.SafeHTTPClient',FakeScopedClient):
        findings=asyncio.run(review_authorization(scope_allowing(['https://app.example.test/admin']),['https://app.example.test/admin'],profiles()[:1]))
    assert findings==[] and FakeScopedClient.calls==[]

@pytest.mark.parametrize('status,error',[(401,False),(403,False),(404,False),(200,True),(302,False)])
def test_authz_candidate_requires_success_from_both_profiles(status,error):
    url='https://app.example.test/admin/users/9'
    def responder(_method,_url,headers):
        is_user=headers.get('Authorization')=='user-test'
        return SimpleNamespace(error=error if is_user else False,status_code=status if is_user else 200,
                               body='{"role":"user"}',body_sha256='hash')
    FakeScopedClient.calls=[]; FakeScopedClient.responder=responder
    with patch('app.authz.SafeHTTPClient',FakeScopedClient):
        findings=asyncio.run(review_authorization(scope_allowing([url]),[url],profiles()))
    assert findings==[]

@pytest.mark.parametrize('url',[
 'https://app.example.test/admin','https://app.example.test/management/keys',
 'https://app.example.test/internal/status','https://app.example.test/users/2',
 'https://app.example.test/orders/3','https://app.example.test/billing/invoices/8',
])
def test_authz_sensitive_path_hints_are_reviewed_read_only(url):
    def responder(_method,_url,headers):
        status=200 if headers.get('Authorization') in {'admin-test','user-test'} else 401
        return SimpleNamespace(error=False,status_code=status,body='{"role":"user"}',body_sha256='hash')
    FakeScopedClient.calls=[]; FakeScopedClient.responder=responder
    with patch('app.authz.SafeHTTPClient',FakeScopedClient):
        findings=asyncio.run(review_authorization(scope_allowing([url]),[url],profiles()))
    assert len(findings)==1
    assert all(method=='GET' for method,_,_ in FakeScopedClient.calls)

def test_authz_filters_uninteresting_url_and_limits_to_unique_urls():
    url='https://app.example.test/admin/users/9'
    FakeScopedClient.calls=[]; FakeScopedClient.responder=None
    urls=[url,url,'https://app.example.test/home','https://outside.invalid/admin/users/1']
    with patch('app.authz.SafeHTTPClient',FakeScopedClient):
        findings=asyncio.run(review_authorization(scope_allowing([url,'https://app.example.test/home']),urls,profiles()))
    assert len(findings)==1
    assert len(FakeScopedClient.calls)==2
