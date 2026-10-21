from types import SimpleNamespace
import pytest
from app.models import Severity
from app.checks.cookie_checks import run_cookie_checks
from app.checks.advanced_checks import run_advanced_checks
from app.checks.web_checks import run_page_checks, run_form_checks, run_content_checks
from app.checks.api_checks import run_openapi_checks, run_graphql_observation


def page(url='https://app.example.test/', headers=None, body='', content_type='text/html'):
    observation=SimpleNamespace(headers={k.lower():v for k,v in (headers or {}).items()},body=body,content_type=content_type)
    return SimpleNamespace(url=url, observation=observation, forms=[], links=[], mixed_content=[])

@pytest.mark.parametrize('header,expected', [
 ('X-Content-Type-Options','FW-WEB-002'), ('Referrer-Policy','FW-WEB-003'),
 ('Permissions-Policy','FW-WEB-004'), ('Content-Security-Policy','FW-WEB-001'),
 ('Strict-Transport-Security','FW-WEB-006'),
])
def test_missing_header_rule_emits_expected_finding(header,expected):
    findings=run_page_checks(page(),None)
    assert expected in {f.rule_id for f in findings}

@pytest.mark.parametrize('cookie,expected', [
 ('session=abc','FW-COOKIE-001'), ('session=abc; Secure','FW-COOKIE-002'),
 ('session=abc; Secure; HttpOnly','FW-COOKIE-003'),
 ('auth=abc; SameSite=None','FW-COOKIE-004'),
 ('__Host-session=abc; HttpOnly; Path=/; SameSite=Lax','FW-COOKIE-005'),
 ('__Secure-token=abc; HttpOnly; SameSite=Lax','FW-COOKIE-006'),
])
def test_cookie_rule_cases(cookie,expected):
    findings=run_cookie_checks(page(headers={'Set-Cookie':cookie}),None)
    assert expected in {f.rule_id for f in findings}

@pytest.mark.parametrize('cookie', [
 'session=abc; Secure; HttpOnly; SameSite=Lax',
 'pref=abc; Secure; SameSite=Strict',
 '__Host-session=abc; Secure; HttpOnly; Path=/; SameSite=Lax',
 '__Secure-token=abc; Secure; SameSite=Lax',
])
def test_well_formed_cookies_avoid_specific_flag_findings(cookie):
    ids={f.rule_id for f in run_cookie_checks(page(headers={'Set-Cookie':cookie}),None)}
    assert 'FW-COOKIE-004' not in ids
    assert 'FW-COOKIE-005' not in ids
    assert 'FW-COOKIE-006' not in ids

@pytest.mark.parametrize('csp,expected', [
 ("default-src 'self'; script-src 'self' 'unsafe-eval'",'FW-CSP-001'),
 ("default-src 'self'; script-src 'self' 'unsafe-inline'",'FW-CSP-002'),
 ("script-src *",'FW-CSP-003'),
 ("Content-Security-Policy-Report-Only",'FW-CSP-004'),
 ("default-src 'self'; script-src 'self'",'FW-CSP-005'),
 ("default-src 'self'; object-src 'none'",'FW-CSP-006'),
])
def test_csp_rule_catalog(csp,expected):
    headers={'Content-Security-Policy':csp} if not csp.startswith('Content-Security-Policy-Report-Only') else {'Content-Security-Policy-Report-Only':"default-src 'self'"}
    findings=run_advanced_checks(page(headers=headers,content_type='text/html'),None)
    assert expected in {f.rule_id for f in findings}

@pytest.mark.parametrize('hsts', ['max-age=10','max-age=15552000','max-age=0'])
def test_hsts_observation(hsts):
    findings=run_advanced_checks(page(url='https://app.example.test/',headers={'Strict-Transport-Security':hsts}),None)
    low=[f for f in findings if f.rule_id=='FW-HSTS-002']
    if hsts in {'max-age=10','max-age=0'}: assert low
    else: assert not low

@pytest.mark.parametrize('header,value,rule', [
 ('X-Content-Type-Options','sniff','FW-HEADER-001'),
 ('X-Frame-Options','allow-all','FW-HEADER-002'),
 ('Server','nginx/1.23.4','FW-DISCLOSE-001'),
])
def test_header_quality_and_banner_detection(header,value,rule):
    findings=run_advanced_checks(page(headers={header:value}),None)
    assert rule in {f.rule_id for f in findings}

def test_good_csp_avoids_unsafe_directive_findings():
    findings=run_advanced_checks(page(headers={'Content-Security-Policy':"default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'"}),None)
    ids={f.rule_id for f in findings}
    assert not ({'FW-CSP-001','FW-CSP-002','FW-CSP-003','FW-CSP-005','FW-CSP-006'} & ids)

def test_external_script_without_sri_is_reviewed():
    findings=run_advanced_checks(page(body='<script src="https://cdn.example.test/app.js"></script>'),None)
    assert 'FW-SUPPLY-001' in {f.rule_id for f in findings}

def test_external_script_with_sri_not_reported_by_sri_check():
    findings=run_advanced_checks(page(body='<script src="https://cdn.example.test/app.js" integrity="sha384-abc" crossorigin="anonymous"></script>'),None)
    assert 'FW-SUPPLY-001' not in {f.rule_id for f in findings}

def test_verbose_runtime_error_markers():
    findings=run_advanced_checks(page(body='Traceback (most recent call last): django.core.exceptions.Error'),None)
    assert 'FW-ERROR-002' in {f.rule_id for f in findings}

def test_password_form_over_http_is_high_severity():
    p=page(url='https://app.example.test/login')
    p.forms=[{'action':'http://app.example.test/login','method':'POST','inputs':[{'name':'password','type':'password'}]}]
    findings=run_form_checks(p,None)
    item=next(f for f in findings if f.rule_id=='FW-FORM-001')
    assert item.severity == Severity.HIGH

def test_csrf_form_signal_is_explicitly_a_candidate():
    p=page(url='https://app.example.test/transfer')
    p.forms=[{'action':'https://app.example.test/transfer','method':'POST','inputs':[{'name':'amount','type':'number'}]}]
    item=next(f for f in run_form_checks(p,None) if f.rule_id=='FW-FORM-002')
    assert 'review candidate' in item.description

def test_openapi_unsecured_operation_candidate():
    body='{"openapi":"3.0.0","info":{"title":"Test","version":"1"},"paths":{"/users":{"get":{"responses":{"200":{"description":"ok"}}}}}}'
    findings=run_openapi_checks('https://app.example.test/openapi.json',body,'application/json')
    assert 'FW-API-002' in {f.rule_id for f in findings}

def test_openapi_global_security_inherited():
    body='{"openapi":"3.0.0","security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"type":"http","scheme":"bearer"}}},"paths":{"/users":{"get":{"responses":{"200":{"description":"ok"}}}}}}'
    findings=run_openapi_checks('https://app.example.test/openapi.json',body,'application/json')
    assert 'FW-API-002' not in {f.rule_id for f in findings}

def test_openapi_operation_explicitly_disables_global_security():
    body='{"openapi":"3.0.0","security":[{"bearerAuth":[]}],"components":{"securitySchemes":{"bearerAuth":{"type":"http","scheme":"bearer"}}},"paths":{"/admin":{"get":{"security":[],"responses":{"200":{"description":"ok"}}}}}}'
    findings=run_openapi_checks('https://app.example.test/openapi.json',body,'application/json')
    assert 'FW-API-002' in {f.rule_id for f in findings}

def test_openapi_ssrf_like_parameter_review_candidate():
    body='{"openapi":"3.0.0","paths":{"/fetch":{"get":{"parameters":[{"name":"url","in":"query","schema":{"type":"string","format":"uri"}}],"responses":{"200":{"description":"ok"}}}}}}'
    findings=run_openapi_checks('https://app.example.test/openapi.json',body,'application/json')
    assert 'FW-API-003' in {f.rule_id for f in findings}

@pytest.mark.parametrize('body', ['not json or yaml', '[]', 'null', '{"paths":{}}', '{"swagger":"2.0","paths":[]}'])
def test_invalid_openapi_documents_do_not_crash(body):
    assert isinstance(run_openapi_checks('https://app.example.test/openapi.json',body,'application/json'),list)

def test_graphql_endpoint_classification():
    findings=run_graphql_observation('https://app.example.test/graphql','{}')
    assert findings and findings[0].rule_id=='FW-GQL-001'

def test_non_graphql_url_is_not_flagged_by_graphql_observer():
    assert run_graphql_observation('https://app.example.test/api/users','{}') == []
