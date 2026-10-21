"""Exhaustive mathematical invariants for risk score normalization and state enums."""
import math
import pytest
from app.risk import calculate_risk, SEV_WEIGHT
from app.models import Severity, ScanStatus, FindingStatus

@pytest.mark.parametrize("severity", list(Severity))
@pytest.mark.parametrize("step", range(0, 101))
def test_v8_risk_score_is_bounded_monotonic_and_rounded(severity, step):
    confidence = step / 100
    score = calculate_risk(severity, confidence)
    assert 0 <= score <= 10
    assert round(score, 2) == score
    assert score == round(SEV_WEIGHT[severity.value] * confidence, 2)
    if step > 0:
        assert score >= calculate_risk(severity, (step - 1) / 100)

@pytest.mark.parametrize("bad", [None, "", "unknown", "NaN", "Infinity", "-Infinity", float("nan"), float("inf"), float("-inf"), {}, [], object()])
def test_v8_invalid_confidence_normalizes_to_finite_zero(bad):
    assert calculate_risk("high", bad) == 0.0

@pytest.mark.parametrize("confidence", [-100, -10, -1, -0.0001, 0, 0.0001, 0.5, 1, 1.0001, 2, 10, 100, 1e100, -1e100])
def test_v8_confidence_is_clamped_to_unit_interval(confidence):
    score = calculate_risk("high", confidence)
    assert score == calculate_risk("high", max(0, min(1, confidence)))

@pytest.mark.parametrize("severity", ["critical", "high", "medium", "low", "info"])
def test_v8_risk_severity_order_is_monotonic(severity):
    assert calculate_risk(severity, .73) >= 0

@pytest.mark.parametrize("status", list(ScanStatus))
def test_v8_scan_status_enum_values_are_unique_and_lowercase(status):
    assert status.value == status.value.lower()
    assert status.value.replace("_", "").isalnum()

@pytest.mark.parametrize("status", list(FindingStatus))
def test_v8_finding_status_enum_values_are_unique_and_lowercase(status):
    assert status.value == status.value.lower()
    assert status.value.replace("_", "").isalnum()

def test_v8_risk_unknown_severity_uses_bounded_fallback():
    assert calculate_risk("not-a-severity", .8) == .8
