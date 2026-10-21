import json
from pathlib import Path
from app.redaction import redact_data
from app.evidence import redact_headers, normalize_candidate
from app.checks.base import FindingCandidate
from app.models import Severity
from app.check_catalog import CATALOG, coverage_matrix
from app.assessment_catalog import TEST_PLAN


def test_coverage_catalog_entries_have_required_fields():
    assert len(CATALOG) >= 10
    for item in CATALOG:
        assert item.get('id') and item.get('domain') and item.get('mode') and item.get('mapping')

def test_coverage_matrix_marks_findings_without_claiming_absence():
    result=coverage_matrix([])
    assert len(result)==len(CATALOG)
    assert all('status' in x and 'finding_count' in x for x in result)
    assert all(x['finding_count']==0 for x in result)

def test_redact_headers_case_insensitive():
    output=redact_headers({'Authorization':'Bearer xx','COOKIE':'sid=xx','X-Test':'ok'})
    assert output['Authorization']=='[REDACTED]'
    assert output['COOKIE']=='[REDACTED]'
    assert output['X-Test']=='ok'

def test_finding_normalization_is_repeatable():
    def candidate(endpoint):
        return FindingCandidate('FW-X','cat','title',Severity.LOW,.8,endpoint,'desc','impact','fix','proof')
    a=normalize_candidate(candidate('https://example.test/path#frag')).dedupe_key
    b=normalize_candidate(candidate('https://example.test/path')).dedupe_key
    assert a==b

def test_finding_normalization_separates_different_rules():
    a=FindingCandidate('FW-A','cat','title',Severity.LOW,.8,'https://example.test/','desc','impact','fix','proof')
    b=FindingCandidate('FW-B','cat','title',Severity.LOW,.8,'https://example.test/','desc','impact','fix','proof')
    assert normalize_candidate(a).dedupe_key != normalize_candidate(b).dedupe_key

def test_test_plan_contains_common_high_risk_manual_domains():
    titles=' '.join((x['title']+' '+x['category']).lower() for x in TEST_PLAN)
    for expected in ['idor','bola','sql','cross-site scripting','ssrf','mfa','business logic','file upload']:
        assert expected in titles

def test_test_plan_labels_automation_truthfully():
    for item in TEST_PLAN:
        if item['execution_mode'] != 'automated_passive':
            assert item['status_semantics'] != 'implemented'
