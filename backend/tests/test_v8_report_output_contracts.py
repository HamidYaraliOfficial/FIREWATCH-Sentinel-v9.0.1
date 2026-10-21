"""Cross-format output security and schema contract matrix for v8."""
import csv, json
from types import SimpleNamespace
import pytest
from app.models import FindingStatus, ScanStatus, Severity
from app.report import render, render_json
from app.report_extras import render_csv, render_markdown, render_sarif
from app.version import VERSION

BASE_PAYLOADS = [
    "<script>alert(1)</script>", "</title><img src=x onerror=alert(1)>", "<svg/onload=alert(1)>",
    "javascript:alert(1)", "\"><iframe srcdoc='<script>x</script>'>", "&lt;script&gt;", "[click](javascript:alert(1))",
    "`<script>`", "<details open ontoggle=x>", "=HYPERLINK(\"https://evil.example\")", "+SUM(1,1)", "-1+1", "@SUM(1,1)",
    "\t=1+1", "\r=1+1", "\n=1+1", " \ufeff=1+1", "\x00=1+1", "正常な日本語", "فارسی امن", "emoji 🔐",
    "\u2028separator", "\u2029separator", "null\x00byte", "'leading quote", "-not-a-formula", "@username", "safe/path/1",
]

@pytest.fixture
def sample():
    scan=SimpleNamespace(id="scan-v8", target_url="https://app.example.test/", status=ScanStatus.COMPLETED)
    def finding(**overrides):
        data=dict(id="finding-v8",rule_id="FW-V8-TEST",category="regression",title="Finding",severity=Severity.MEDIUM,
            confidence=.8,risk_score=4.0,status=FindingStatus.OPEN,endpoint="https://app.example.test/item",description="desc",
            impact="impact",remediation="remediate",references=["https://owasp.org/"],evidence_summary="safe evidence")
        data.update(overrides); return SimpleNamespace(**data)
    return scan, finding

@pytest.mark.parametrize("field", ["title", "endpoint", "description", "impact", "remediation", "evidence_summary"])
@pytest.mark.parametrize("payload", BASE_PAYLOADS)
def test_v8_html_sink_never_interprets_untrusted_field_as_active_markup(tmp_path, sample, field, payload):
    scan, factory=sample; out=tmp_path/"report.html"
    render(scan,[factory(**{field:payload})],[],out,[],[])
    text=out.read_text(encoding="utf-8").lower()
    assert "<script>alert(1)</script>" not in text
    assert "<iframe" not in text
    assert "<img src=x" not in text

@pytest.mark.parametrize("field", ["title", "endpoint", "description", "impact", "remediation", "evidence_summary"])
@pytest.mark.parametrize("payload", BASE_PAYLOADS)
def test_v8_markdown_sink_escapes_html_and_links(tmp_path, sample, field, payload):
    scan, factory=sample; out=tmp_path/"report.md"
    render_markdown(scan,[factory(**{field:payload})],[],out)
    text=out.read_text(encoding="utf-8").lower()
    assert "<script>alert(1)</script>" not in text
    assert "<iframe" not in text
    assert "<img src=x" not in text

@pytest.mark.parametrize("payload", BASE_PAYLOADS)
def test_v8_csv_formula_neutralization_handles_untrusted_title(tmp_path, sample, payload):
    scan, factory=sample; out=tmp_path/"findings.csv"
    render_csv(scan,[factory(title=payload)],out)
    with out.open(encoding="utf-8-sig",newline="") as file:
        row=next(csv.DictReader(file))
    normalized=payload.lstrip("\ufeff\x00\t\r\n ")
    if normalized.startswith(("=", "+", "-", "@")):
        assert row["title"].startswith("'")

@pytest.mark.parametrize("severity", list(Severity))
def test_v8_sarif_contract_has_version_and_rule_metadata(tmp_path, sample, severity):
    scan, factory=sample; out=tmp_path/"out.sarif"; finding=factory(severity=severity)
    render_sarif(scan,[finding],out)
    payload=json.loads(out.read_text(encoding="utf-8")); run=payload["runs"][0]
    assert payload["version"] == "2.1.0"
    assert run["tool"]["driver"]["version"] == VERSION
    assert run["results"][0]["ruleId"] == finding.rule_id

@pytest.mark.parametrize("target", ["https://app.example.test/", "https://unicode.example.test/", "http://127.0.0.1:8765/", "https://app.example.test/app?q=safe"])
def test_v8_json_report_roundtrips_core_metadata(tmp_path, sample, target):
    scan,factory=sample; scan.target_url=target; out=tmp_path/"out.json"
    render_json(scan,[factory()],[],out,[],[])
    payload=json.loads(out.read_text(encoding="utf-8"))
    assert payload["meta"]["version"] == VERSION
    assert payload["meta"]["target"] == target

@pytest.mark.parametrize("n", range(0, 16))
def test_v8_empty_and_multi_finding_reports_remain_valid_json(tmp_path, sample, n):
    scan,factory=sample; out=tmp_path/f"out-{n}.json"
    findings=[factory(id=f"finding-{i}", title=f"Finding {i}") for i in range(n)]
    render_json(scan,findings,[],out,[],[])
    payload=json.loads(out.read_text(encoding="utf-8"))
    assert len(payload["findings"]) == n
