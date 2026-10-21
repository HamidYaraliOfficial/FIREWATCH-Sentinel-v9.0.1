"""Risk-scoring invariants over a wide confidence/severity matrix."""
import math
import pytest
from app.risk import calculate_risk, SEV_WEIGHT
from app.models import Severity

@pytest.mark.parametrize("severity,weight", [
    ("critical", 10.0), ("high", 8.0), ("medium", 5.0), ("low", 2.5), ("info", 0.5),
    (Severity.CRITICAL, 10.0), (Severity.HIGH, 8.0), (Severity.MEDIUM, 5.0),
    (Severity.LOW, 2.5), (Severity.INFO, 0.5),
])
def test_v6_severity_weights_are_stable(severity, weight):
    assert calculate_risk(severity, 1.0) == weight

@pytest.mark.parametrize("severity", ["critical", "high", "medium", "low", "info"])
@pytest.mark.parametrize("confidence", [i / 100 for i in range(0, 101)])
def test_v6_risk_score_is_bounded_and_exactly_weighted(severity, confidence):
    score = calculate_risk(severity, confidence)
    assert 0 <= score <= SEV_WEIGHT[severity]
    assert score == round(SEV_WEIGHT[severity] * confidence, 2)

@pytest.mark.parametrize("severity", ["critical", "high", "medium", "low", "info"])
def test_v6_risk_score_is_monotonic_at_fine_grained_steps(severity):
    scores = [calculate_risk(severity, i / 100) for i in range(101)]
    assert scores == sorted(scores)

@pytest.mark.parametrize("confidence", [None, "", "abc", float("nan"), float("inf"), float("-inf"), -1e300, 1e300])
def test_v6_risk_score_is_robust_to_invalid_and_extreme_confidence(confidence):
    result = calculate_risk("high", confidence)
    assert math.isfinite(result)
    assert 0 <= result <= 8.0

@pytest.mark.parametrize("severity", ["unknown", "", None, object()])
def test_v6_unknown_severity_has_safe_fallback(severity):
    result = calculate_risk(severity, 1.0)
    assert 0 <= result <= 10.0
