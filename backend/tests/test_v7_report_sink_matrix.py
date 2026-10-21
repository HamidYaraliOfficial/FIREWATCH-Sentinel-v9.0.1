"""Report-sink security contract for HTML, JSON, CSV, Markdown, and SARIF."""
import csv, json
from pathlib import Path
from types import SimpleNamespace
import pytest
from app.models import FindingStatus, ScanStatus, Severity
from app.report import render, render_json
from app.report_extras import render_csv, render_markdown, render_sarif, _spreadsheet_safe
from app.version import VERSION

@pytest.fixture
def entities():
    scan = SimpleNamespace(id="scan-v7", target_url="https://app.example.test/", status=ScanStatus.COMPLETED)
    def finding(title="Finding", endpoint="https://app.example.test/item", evidence="bounded evidence"):
        return SimpleNamespace(id="finding-v7", rule_id="FW-V7-TEST", category="regression", title=title,
            severity=Severity.HIGH, confidence=.91, risk_score=7.28, status=FindingStatus.OPEN,
            endpoint=endpoint, description=title, impact="controlled impact", remediation="apply a patch",
            references=["https://owasp.org/"], evidence_summary=evidence)
    return scan, finding

_PAYLOADS = [
    "<script>alert(1)</script>", "</p><img src=x onerror=alert(1)>", "<svg/onload=alert(1)>",
    "javascript:alert(1)", "\"><iframe srcdoc='<script>alert(1)</script>'>", "&lt;script&gt;",
    "[click](javascript:alert(1))", "`<script>alert(1)</script>`", "<details open ontoggle=alert(1)>",
    "\r\nSet-Cookie: secret=do-not-leak", "=HYPERLINK(\"https://bad.example\")", "+SUM(1,1)",
    "-1+1", "@SUM(1,1)", "\t=1+1", "  =cmd|'/C calc'!A0",
]

@pytest.mark.parametrize("payload", _PAYLOADS)
def test_v7_html_report_escapes_untrusted_finding_fields(tmp_path, entities, payload):
    scan, finding = entities
    path = tmp_path / "report.html"
    render(scan, [finding(title=payload, evidence=payload)], [], path, [], [])
    output = path.read_text(encoding="utf-8")
    assert "<script" not in output.lower()
    assert "<iframe" not in output.lower()
    assert "<img" not in output.lower()

@pytest.mark.parametrize("payload", _PAYLOADS)
def test_v7_markdown_report_escapes_raw_html_and_markdown_controls(tmp_path, entities, payload):
    scan, finding = entities
    path = tmp_path / "report.md"
    render_markdown(scan, [finding(title=payload, evidence=payload)], [], path)
    output = path.read_text(encoding="utf-8")
    assert "<script" not in output.lower()
    assert "<iframe" not in output.lower()
    assert "<img" not in output.lower()
    if payload.startswith("<") or payload.startswith("</"):
        assert "&lt;" in output
    if payload.startswith("[click]"):
        assert r"\[click\]" in output

@pytest.mark.parametrize("payload", _PAYLOADS)
def test_v7_csv_report_neutralizes_spreadsheet_formula_values(tmp_path, entities, payload):
    scan, finding = entities
    path = tmp_path / "report.csv"
    render_csv(scan, [finding(title=payload, evidence=payload)], path)
    with path.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    assert len(rows) == 1
    if payload.lstrip("\ufeff\x00\t\r\n ").startswith(("=", "+", "-", "@")):
        assert rows[0]["title"].startswith("'")
    assert rows[0]["rule_id"] == "FW-V7-TEST"

@pytest.mark.parametrize("prefix", ["=", "+", "-", "@", "\t=", "\r=", "\n=", " \ufeff=", "\x00="])
def test_v7_spreadsheet_safe_scalar_matrix(prefix):
    value = prefix + "1+1"
    safe = _spreadsheet_safe(value)
    assert safe.startswith("'")
    assert safe[1:] == value

@pytest.mark.parametrize("severity", list(Severity))
def test_v7_sarif_output_contract_matches_severity(tmp_path, entities, severity):
    scan, finding = entities
    item = finding()
    item.severity = severity
    path = tmp_path / "report.sarif"
    render_sarif(scan, [item], path)
    data = json.loads(path.read_text(encoding="utf-8"))
    result = data["runs"][0]["results"][0]
    expected = "error" if severity in (Severity.CRITICAL, Severity.HIGH) else "warning" if severity == Severity.MEDIUM else "note"
    assert result["level"] == expected
    assert result["ruleId"] == item.rule_id

@pytest.mark.parametrize("target", ["https://example.test/", "https://idn.example/", "http://127.0.0.1:8765/"])
def test_v7_json_report_has_current_version_and_valid_contract(tmp_path, entities, target):
    scan, finding = entities
    scan.target_url = target
    path = tmp_path / "report.json"
    render_json(scan, [finding()], [], path, [], [])
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["meta"]["version"] == VERSION
    assert data["meta"]["target"] == target
    assert data["findings"][0]["rule_id"] == "FW-V7-TEST"

@pytest.mark.parametrize("payload", ["<script>", "</style>", "\u2028", "\u2029", "\x00", "<img src=x>"])
def test_v7_json_encoding_roundtrips_untrusted_text(tmp_path, entities, payload):
    scan, finding = entities
    path = tmp_path / "report.json"
    render_json(scan, [finding(title=payload)], [], path, [], [])
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["findings"][0]["title"] == payload
