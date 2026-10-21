import pytest
from app.risk import calculate_risk
from app.models import Severity
from app.assessment_catalog import TEST_PLAN, STANDARDS, get_assessment_plan

@pytest.mark.parametrize('severity,weight', [
 (Severity.CRITICAL,10),(Severity.HIGH,8),(Severity.MEDIUM,5),(Severity.LOW,2.5),(Severity.INFO,.5),
 ('critical',10),('high',8),('medium',5),('low',2.5),('info',.5),
])
def test_risk_at_full_confidence(severity,weight):
    assert calculate_risk(severity,1) == weight

@pytest.mark.parametrize('confidence', [-10,-1,0,.01,.1,.25,.5,.75,.99,1,5,100])
def test_risk_confidence_clamped_to_unit_interval(confidence):
    value=calculate_risk('high',confidence)
    assert 0 <= value <= 8

@pytest.mark.parametrize('severity', ['critical','high','medium','low','info'])
def test_risk_is_monotonic_for_each_severity(severity):
    values=[calculate_risk(severity,c) for c in (0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1)]
    assert values == sorted(values)

def test_catalog_identifiers_are_unique_and_fields_complete():
    ids=[x['id'] for x in TEST_PLAN]
    assert len(ids) >= 70
    assert len(ids) == len(set(ids))
    for row in TEST_PLAN:
        assert row['title'] and row['category'] and row['execution_mode']
        assert 'safe_by_default' in row and 'status_semantics' in row

def test_plan_discloses_manual_and_tool_gaps():
    plan=get_assessment_plan()
    modes=plan['execution_mode_counts']
    assert plan['total_cases'] == len(TEST_PLAN)
    assert modes['manual_or_test-account_required'] > 0
    assert modes['optional_specialist_tool_required'] > 0
    assert 'not executed' in plan['disclaimer']

def test_current_standard_baselines_are_explicit():
    assert STANDARDS['owasp_top_10'] == '2025'
    assert STANDARDS['owasp_asvs'] == '5.0.0'
    assert STANDARDS['owasp_api_security_top_10'] == '2023'

@pytest.mark.parametrize('confidence', [float('nan'), float('inf'), float('-inf'), None, 'not-a-number'])
def test_risk_handles_nonfinite_or_invalid_confidence_without_crashing(confidence):
    value=calculate_risk('critical',confidence)
    assert value == 0.0
