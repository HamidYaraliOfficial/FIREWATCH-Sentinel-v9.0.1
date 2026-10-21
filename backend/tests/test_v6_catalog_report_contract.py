"""Contracts linking the assessment catalog, rule families, and report formats."""
import json
from pathlib import Path
from types import SimpleNamespace
import pytest
from app.assessment_catalog import TEST_PLAN, STANDARDS, get_assessment_plan
from app.check_catalog import CATALOG, coverage_matrix
from app.report_extras import render_csv, render_markdown, render_sarif
from app.models import FindingStatus, ScanStatus, Severity

@pytest.mark.parametrize("row", TEST_PLAN, ids=lambda x: x["id"])
def test_v6_each_assessment_case_is_explicit_and_safe_by_default(row):
    assert row["id"] and row["category"] and row["title"]
    assert row["execution_mode"] in {
        "automated_passive", "automated_review_candidate",
        "manual_or_test-account_required", "optional_specialist_tool_required"
    }
    assert row["safe_by_default"] is True
    assert row["status_semantics"]
    assert row["standard_mapping"]

@pytest.mark.parametrize("item", CATALOG, ids=lambda x: x["id"])
def test_v6_each_check_family_has_domain_mode_and_mapping(item):
    assert item["id"] and item["domain"] and item["mode"]
    assert isinstance(item["mapping"], list) and item["mapping"]

@pytest.mark.parametrize("mode", [
    "automated_passive", "automated_review_candidate",
    "manual_or_test-account_required", "optional_specialist_tool_required"
])
def test_v6_plan_counts_reconcile_to_case_total(mode):
    plan = get_assessment_plan()
    expected = sum(row["execution_mode"] == mode for row in TEST_PLAN)
    assert plan["execution_mode_counts"].get(mode, 0) == expected
    assert sum(plan["execution_mode_counts"].values()) == plan["total_cases"] == len(TEST_PLAN)

def test_v6_standards_are_reported_separately_from_agent_version():
    plan = get_assessment_plan()
    assert plan["standards"] == STANDARDS
    assert STANDARDS["owasp_asvs"] == "5.0.0"  # standard version is not the FIREWATCH release version

@pytest.mark.parametrize("severity", [Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW, Severity.INFO])
def test_v6_csv_markdown_and_sarif_handle_each_severity(tmp_path, severity):
    scan = SimpleNamespace(id="scan-v6", target_url="https://example.test/", status=ScanStatus.COMPLETED)
    finding = SimpleNamespace(
        id="finding-v6", rule_id="FW-V6-TEST", category="regression", title="Test finding",
        severity=severity, confidence=.9, risk_score=severity.value.__len__(),
        status=FindingStatus.OPEN, endpoint="https://example.test/item", description="test description",
        impact="test impact", remediation="test remediation", references=["https://owasp.org/"],
        evidence_summary="safe evidence"
    )
    events=[]; coverage=[{"phase":"complete","progress":100,"details":"done"}]
    csv_path=tmp_path/"report.csv"; md_path=tmp_path/"report.md"; sarif_path=tmp_path/"report.sarif"
    render_csv(scan,[finding],csv_path)
    render_markdown(scan,[finding],coverage,md_path)
    render_sarif(scan,[finding],sarif_path)
    assert "FW-V6-TEST" in csv_path.read_text(encoding="utf-8-sig")
    assert "FW-V6-TEST" in md_path.read_text(encoding="utf-8")
    payload=json.loads(sarif_path.read_text(encoding="utf-8"))
    assert payload["version"] == "2.1.0"
    assert payload["runs"][0]["results"][0]["ruleId"] == "FW-V6-TEST"

@pytest.mark.parametrize("findings", [[], [SimpleNamespace(rule_id="FW-WEB-001")], [SimpleNamespace(rule_id="FW-COOKIE-003"),SimpleNamespace(rule_id="FW-TLS-004")]])
def test_v6_coverage_matrix_counts_findings_without_claiming_completeness(findings):
    rows=coverage_matrix(findings)
    assert len(rows) == len(CATALOG)
    assert all("finding_count" in row and "status" in row for row in rows)
    assert all(row["status"] in {"finding_observed", "no_finding_recorded_or_not_applicable"} for row in rows)
