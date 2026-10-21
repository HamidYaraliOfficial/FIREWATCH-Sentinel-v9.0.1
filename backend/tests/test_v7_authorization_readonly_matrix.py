"""Read-only authorization review contract; fake transport prevents outbound traffic."""
import asyncio
from dataclasses import dataclass
import pytest
from app.authz import AuthProfile, review_authorization
from app.http_client import HTTPObservation
from app.scope import ScopePolicy

@dataclass
class DummyObs:
    url: str
    status_code: int = 200
    body: str = '{"email":"test@example.invalid","role":"user"}'
    body_sha256: str = "same-hash"
    error: str | None = None

class FakeClient:
    seen = []
    statuses = {}
    def __init__(self, scope, delay_ms=150): self.scope=scope
    async def __aenter__(self): return self
    async def __aexit__(self, *args): return None
    async def request(self, method, url, headers=None, content=None):
        if method.upper() != "GET": raise AssertionError(f"non-read method used: {method}")
        if content is not None: raise AssertionError("authorization review must not send request bodies")
        if not self.scope.is_allowed(url): raise AssertionError("out-of-scope request")
        self.seen.append((method.upper(),url,dict(headers or {}),content))
        status = self.statuses.get((url, (headers or {}).get("Authorization")), 200)
        body = '{"email":"demo@example.invalid","role":"user"}'
        return HTTPObservation(url,url,status,{"content-type":"application/json"},body,1.0,"application/json","same-hash",None,[])

@pytest.fixture
def policy():
    return ScopePolicy.from_root("https://app.example.test/", exclusions=["/logout"], allow_private_targets=True)

def test_v7_authz_review_requires_two_profiles_without_network(monkeypatch, policy):
    from app import authz
    monkeypatch.setattr(authz, "SafeHTTPClient", FakeClient)
    FakeClient.seen=[]
    result=asyncio.run(review_authorization(policy,["https://app.example.test/admin/users"],[AuthProfile("admin",{} )]))
    assert result == []
    assert FakeClient.seen == []

@pytest.mark.parametrize("path", ["/admin", "/admin/users", "/management/jobs", "/internal/status", "/users/1", "/orders/42", "/billing/invoices", "/accounts/current", "/profile", "/settings"])
def test_v7_authorization_review_uses_only_get_and_reports_candidates(monkeypatch, policy, path):
    from app import authz
    monkeypatch.setattr(authz, "SafeHTTPClient", FakeClient)
    FakeClient.seen=[]; FakeClient.statuses={}
    url="https://app.example.test"+path
    profiles=[AuthProfile("admin",{"Authorization":"admin-test"}), AuthProfile("user",{"Authorization":"user-test"})]
    findings=asyncio.run(review_authorization(policy,[url],profiles,delay_ms=0))
    assert [call[0] for call in FakeClient.seen] == ["GET","GET"]
    assert all(call[3] is None for call in FakeClient.seen)
    assert all(call[1] == url for call in FakeClient.seen)
    assert all(call[2].get("Authorization") in {"admin-test","user-test"} for call in FakeClient.seen)
    assert findings and findings[0].rule_id == "FW-AUTHZ-001"
    assert "not proof" in findings[0].description.lower()
    assert findings[0].evidence["methods_used"] == ["GET"]

def test_v7_authorization_review_ignores_out_of_scope_and_non_sensitive_paths(monkeypatch, policy):
    from app import authz
    monkeypatch.setattr(authz, "SafeHTTPClient", FakeClient)
    FakeClient.seen=[]
    urls=["https://evil.example/admin/users", "https://app.example.test/logout", "https://app.example.test/about"]
    result=asyncio.run(review_authorization(policy,urls,[AuthProfile("admin",{}),AuthProfile("user",{})]))
    assert result == []
    assert FakeClient.seen == []

def test_v7_authorization_review_caps_unique_candidate_urls_at_100(monkeypatch, policy):
    from app import authz
    monkeypatch.setattr(authz, "SafeHTTPClient", FakeClient)
    FakeClient.seen=[]
    urls=[f"https://app.example.test/admin/users/{i}" for i in range(125)]
    asyncio.run(review_authorization(policy,urls,[AuthProfile("admin",{}),AuthProfile("user",{})]))
    assert len(FakeClient.seen) == 200
    assert len({call[1] for call in FakeClient.seen}) == 100

def test_v7_authorization_review_skips_candidates_when_either_request_fails(monkeypatch, policy):
    from app import authz
    monkeypatch.setattr(authz, "SafeHTTPClient", FakeClient)
    url="https://app.example.test/admin/users"
    FakeClient.seen=[]; FakeClient.statuses={(url,"user-test"):403}
    result=asyncio.run(review_authorization(policy,[url],[AuthProfile("admin",{"Authorization":"admin-test"}),AuthProfile("user",{"Authorization":"user-test"})]))
    assert result == []
