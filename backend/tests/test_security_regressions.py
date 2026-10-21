from __future__ import annotations
import json
from types import SimpleNamespace
from pathlib import Path

import pytest
from app.scope import ScopePolicy, ScopeViolation
from app.secret_store import protect_config, reveal_config, public_config
from app.checks.api_checks import run_openapi_checks
from app.checks.advanced_checks import run_advanced_checks
from app.check_catalog import coverage_matrix
from app.checks.base import FindingCandidate
from app.models import Severity
from app.schemas import ScanCreate
from app.redaction import contains_sensitive_query, redact_url, redact_data
from app.report_extras import render_csv, render_markdown, render_sarif


def test_scope_rejects_non_scoped_ports_and_embedded_credentials():
    scope=ScopePolicy.from_root('http://example.com:8080/',allow_private_targets=True)
    assert scope.is_allowed('http://example.com:8080/a')
    assert not scope.is_allowed('http://example.com:8081/a')
    with pytest.raises(ScopeViolation): scope.validate_url('http://user:pass@example.com:8080/')


def test_target_url_secret_query_rejected_and_inventory_redacted():
    assert contains_sensitive_query('https://example.com/?access_token=super-secret')
    assert '%5BREDACTED%5D' in redact_url('https://example.com/?access_token=super-secret&tab=users')
    data=redact_data({'Authorization':'Bearer never-store-me','url':'https://example.com/?token=abc123'})
    assert data['Authorization']=='[REDACTED]'
    assert 'abc123' not in data['url']


def test_scan_credentials_are_encrypted_at_rest(tmp_path, monkeypatch):
    monkeypatch.setenv('FIREWATCH_SECRET_KEY_FILE',str(tmp_path/'secret.key'))
    config={'profile':'standard','request_headers':{'Authorization':'Bearer highly-sensitive'},'auth_cookies':'sid=secret-cookie','authorization_profiles':[{'name':'admin','headers':{'Cookie':'sid=privileged'}}]}
    protected=protect_config(config)
    assert '_secret_blob' in protected
    assert 'highly-sensitive' not in json.dumps(protected)
    assert 'secret-cookie' not in json.dumps(protected)
    assert reveal_config(protected)==config
    public=public_config(protected)
    assert 'authentication_configured' in public
    assert '_secret_blob' not in public


def test_openapi_yaml_parses_security_and_url_parameter_candidates():
    spec='''openapi: 3.0.3
info: {title: Demo, version: '1'}
paths:
  /fetch:
    get:
      parameters:
        - name: url
          in: query
          schema: {type: string, format: uri}
'''
    findings=run_openapi_checks('https://example.com/openapi.yaml',spec,'application/yaml')
    ids={f.rule_id for f in findings}
    assert 'FW-API-002' in ids
    assert 'FW-API-003' in ids


def test_advanced_checks_report_weak_csp_and_shared_cache():
    url='https://example.com/account'
    obs=SimpleNamespace(headers={'content-security-policy':"default-src *; script-src 'unsafe-inline' 'unsafe-eval' *",'cache-control':'public, s-maxage=600'},body='<html><script src="https://cdn.example.net/app.js"></script></html>')
    page=SimpleNamespace(url=url,observation=obs,mixed_content=[])
    ids={x.rule_id for x in run_advanced_checks(page,{})}
    assert {'FW-CSP-001','FW-CSP-002','FW-CSP-003','FW-CACHE-002','FW-SUPPLY-001'} <= ids


def test_profile_presets_apply_expected_safety_defaults():
    baseline=ScanCreate(target_url='https://example.com/',scope_acknowledged=True,profile='baseline')
    comprehensive=ScanCreate(target_url='https://example.com/',scope_acknowledged=True,profile='comprehensive')
    assert baseline.max_pages==100 and baseline.passive_only is True and baseline.enable_browser is False
    assert comprehensive.max_pages==1500 and comprehensive.max_depth==12 and comprehensive.max_concurrency==4


def test_rule_coverage_counts_findings_in_numeric_ranges():
    f1=SimpleNamespace(rule_id='FW-WEB-001'); f2=SimpleNamespace(rule_id='FW-WEB-010'); f3=SimpleNamespace(rule_id='FW-WEB-011')
    row=next(x for x in coverage_matrix([f1,f2,f3]) if x['id']=='FW-WEB-001..011')
    assert row['finding_count']==3


def test_report_exports_csv_markdown_and_sarif(tmp_path):
    scan=SimpleNamespace(id='scan-1',target_url='https://example.com/',status=SimpleNamespace(value='completed'))
    finding=SimpleNamespace(id='f-1',rule_id='FW-WEB-001',category='headers',title='CSP missing',severity=Severity.MEDIUM,confidence=.97,risk_score=4.85,status=SimpleNamespace(value='open'),endpoint='https://example.com/',description='Description',impact='Impact',remediation='Fix',evidence_summary='Header absent',references=['OWASP'])
    csvp=tmp_path/'f.csv'; mdp=tmp_path/'r.md'; sarifp=tmp_path/'r.sarif.json'
    render_csv(scan,[finding],csvp); render_markdown(scan,[finding],[],mdp); render_sarif(scan,[finding],sarifp)
    assert 'FW-WEB-001' in csvp.read_text(encoding='utf-8-sig')
    assert 'CSP missing' in mdp.read_text()
    sarif=json.loads(sarifp.read_text()); assert sarif['version']=='2.1.0' and sarif['runs'][0]['results'][0]['ruleId']=='FW-WEB-001'


def test_authorization_profile_headers_are_bounded():
    with pytest.raises(Exception):
        ScanCreate(target_url='https://example.com/', scope_acknowledged=True,
                   authorization_profiles=[{'name':'user','headers':{'Authorization':'x'*9000}}])


def test_root_custom_port_does_not_expand_when_host_is_repeated():
    policy=ScopePolicy.from_root('https://example.com:8443/',allow_private_targets=True,allowed_hosts=['example.com'])
    assert policy.is_allowed('https://example.com:8443/path')
    assert not policy.is_allowed('https://example.com/path')
    with pytest.raises(ScopeViolation):
        ScopePolicy.from_root('https://example.com/',allow_private_targets=True,allowed_hosts=['ftp://other.example'])


def test_secret_field_name_variants_are_redacted():
    url='https://example.com/?session-id=secret123&search=flowers'
    assert contains_sensitive_query(url)
    safe=redact_url(url)
    assert 'secret123' not in safe and 'flowers' in safe
    assert redact_data({'session_id':'session-secret'})['session_id']=='[REDACTED]'

def test_wrong_secret_key_fails_closed(tmp_path, monkeypatch):
    from cryptography.fernet import Fernet
    monkeypatch.setenv('FIREWATCH_SECRET_KEY_FILE', str(tmp_path / 'key-a'))
    config={'request_headers': {'Authorization': 'Bearer unique-test-secret'}}
    protected=protect_config(config)
    monkeypatch.setenv('FIREWATCH_SECRET_KEY', Fernet.generate_key().decode('ascii'))
    with pytest.raises(RuntimeError):
        reveal_config(protected)
    monkeypatch.delenv('FIREWATCH_SECRET_KEY',raising=False)

def test_secret_key_file_permissions_are_private_on_posix(tmp_path, monkeypatch):
    import os, stat
    monkeypatch.setenv('FIREWATCH_SECRET_KEY_FILE', str(tmp_path/'key'))
    protect_config({'auth_cookies':'sid=example'})
    if os.name != 'nt':
        assert stat.S_IMODE((tmp_path/'key').stat().st_mode) == 0o600

def test_redaction_does_not_leak_url_userinfo():
    from app.redaction import redact_url
    value=redact_url('https://user:do-not-store@example.test/path?ok=yes')
    assert 'user:' not in value and 'do-not-store' not in value and 'ok=yes' in value
