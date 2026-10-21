import pytest
from app.version import VERSION
from fastapi.testclient import TestClient
from app.main import app

def test_api_version_matches_runtime_version():
    with TestClient(app) as c:
        assert c.get('/health').json()['version']==VERSION
        assert c.get('/openapi.json').json()['info']['version']==VERSION

def test_assessment_plan_endpoint_contains_automated_and_manual_cases():
    with TestClient(app) as c:
        result=c.get('/api/v1/assessment-plan')
        assert result.status_code==200
        body=result.json()
        assert body['version']==VERSION
        assert body['total_cases'] >= 70
        assert any(x['execution_mode']=='automated_passive' for x in body['test_cases'])
        assert any(x['execution_mode']=='manual_or_test-account_required' for x in body['test_cases'])
        assert any(x['execution_mode']=='optional_specialist_tool_required' for x in body['test_cases'])

def test_assessment_plan_requires_api_key_when_configured(monkeypatch):
    from types import SimpleNamespace
    import app.main as main_module
    monkeypatch.setattr(main_module,'settings',SimpleNamespace(api_key='test-v5-key',environment='development'))
    with TestClient(app) as c:
        assert c.get('/api/v1/assessment-plan').status_code==401
        assert c.get('/api/v1/assessment-plan',headers={'X-API-Key':'test-v5-key'}).status_code==200

def test_production_without_api_key_fails_closed_at_startup(monkeypatch):
    from types import SimpleNamespace
    import app.main as main_module
    monkeypatch.setattr(main_module,'settings',SimpleNamespace(api_key='',environment='production'))
    with pytest.raises(RuntimeError, match="FIREWATCH_API_KEY"):
        with TestClient(app):
            pass

def test_malformed_payload_does_not_create_scan():
    with TestClient(app) as c:
        response=c.post('/api/v1/scans',json={'target_url':'ftp://example.test','scope_acknowledged':True})
        assert response.status_code==422

def test_secret_in_query_is_rejected_at_api_boundary():
    with TestClient(app) as c:
        response=c.post('/api/v1/scans',json={'target_url':'https://example.test/?access_token=abc123','scope_acknowledged':True})
        assert response.status_code in {400,422}

def test_root_dashboard_is_served():
    with TestClient(app) as c:
        response=c.get('/')
        assert response.status_code==200
        assert 'FIREWATCH' in response.text

def test_dashboard_static_assets_are_served():
    with TestClient(app) as c:
        css=c.get('/static/app.css')
        js=c.get('/static/app.js')
        assert css.status_code==200 and 'text/css' in css.headers['content-type']
        assert js.status_code==200 and 'javascript' in js.headers['content-type']
