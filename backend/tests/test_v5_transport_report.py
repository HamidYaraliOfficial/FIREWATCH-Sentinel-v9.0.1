from app.version import VERSION
import asyncio, json
from pathlib import Path
from types import SimpleNamespace
import httpx
import pytest
from app.scope import ScopePolicy, ScopeViolation
from app.http_client import SafeHTTPClient
from app.models import ScanStatus, Severity, FindingStatus
from app.report_extras import render_csv, render_markdown, render_sarif
from app.report import render, render_json

@pytest.mark.parametrize('method', ['GET','HEAD','OPTIONS'])
def test_http_client_normalizes_read_only_method_and_returns_observation(method):
    async def run():
        policy=ScopePolicy.from_root('https://app.example.test/',allow_private_targets=True)
        seen=[]
        async def handler(req):
            seen.append(req.method)
            return httpx.Response(200,headers={'content-type':'text/plain'},text='ok')
        async with SafeHTTPClient(policy,delay_ms=0) as c:
            await c.client.aclose()
            c.client=httpx.AsyncClient(transport=httpx.MockTransport(handler),follow_redirects=False)
            obs=await c.request(method,'https://app.example.test/')
            assert obs.status_code==200 and obs.error is None
        assert seen==[method]
    asyncio.run(run())

def test_http_client_does_not_follow_redirects():
    async def run():
        policy=ScopePolicy.from_root('https://app.example.test/',allow_private_targets=True)
        seen=[]
        async def handler(req):
            seen.append(str(req.url))
            return httpx.Response(302,headers={'location':'https://outside.example.test/'})
        async with SafeHTTPClient(policy,delay_ms=0) as c:
            await c.client.aclose(); c.client=httpx.AsyncClient(transport=httpx.MockTransport(handler),follow_redirects=False)
            obs=await c.request('GET','https://app.example.test/')
            assert obs.status_code==302
        assert len(seen)==1
    asyncio.run(run())

def test_http_client_refuses_out_of_scope_before_network():
    async def run():
        policy=ScopePolicy.from_root('https://app.example.test/',allow_private_targets=True)
        async with SafeHTTPClient(policy,delay_ms=0) as c:
            await c.client.aclose()
            async def handler(req): raise AssertionError('network must not be called')
            c.client=httpx.AsyncClient(transport=httpx.MockTransport(handler))
            with pytest.raises(ScopeViolation): await c.request('GET','https://outside.example.test/')
    asyncio.run(run())

def sample_objects():
    scan=SimpleNamespace(id='scan-1',target_url='https://app.example.test/',status=ScanStatus.COMPLETED)
    finding=SimpleNamespace(id='f-1',rule_id='FW-TEST-001',category='test',title='Example finding',severity=Severity.MEDIUM,confidence=.8,risk_score=4.0,status=FindingStatus.OPEN,endpoint='https://app.example.test/path',description='Description',impact='Impact',remediation='Fix',references=['https://owasp.org/'],evidence_summary='Safe evidence')
    return scan,[finding]

def test_csv_report_is_parseable(tmp_path):
    import csv
    scan,findings=sample_objects(); path=tmp_path/'report.csv'; render_csv(scan,findings,path)
    rows=list(csv.DictReader(path.open(encoding='utf-8-sig')))
    assert rows[0]['rule_id']=='FW-TEST-001'

def test_markdown_report_has_disclaimer_when_empty(tmp_path):
    scan, _=sample_objects(); path=tmp_path/'report.md'; render_markdown(scan,[],[],path)
    assert 'does not prove' in path.read_text().lower()

def test_sarif_report_schema_basics(tmp_path):
    scan,findings=sample_objects(); path=tmp_path/'report.sarif.json'; render_sarif(scan,findings,path)
    payload=json.loads(path.read_text())
    assert payload['version']=='2.1.0'
    assert payload['runs'][0]['results'][0]['ruleId']=='FW-TEST-001'
    assert payload['runs'][0]['tool']['driver']['version']==VERSION

def test_sarif_empty_findings_is_valid_shape(tmp_path):
    scan,_=sample_objects(); path=tmp_path/'empty.sarif.json'; render_sarif(scan,[],path)
    payload=json.loads(path.read_text())
    assert payload['runs'][0]['results']==[]

def test_csv_empty_findings_writes_headers(tmp_path):
    scan,_=sample_objects(); path=tmp_path/'empty.csv'; render_csv(scan,[],path)
    assert 'scan_id,target,finding_id' in path.read_text(encoding='utf-8-sig')

@pytest.mark.parametrize('status', list(ScanStatus))
def test_scan_status_enum_values_are_serializable(status):
    assert status.value in {'queued','running','completed','failed','canceled'}

def test_html_report_escapes_untrusted_scan_content(tmp_path):
    scan, findings = sample_objects()
    scan.target_url = 'https://app.example.test/<script>alert(1)</script>'
    findings[0].title = '<img src=x onerror=alert(1)>'
    output = tmp_path / 'report.html'
    render(scan, findings, [], output, [], [])
    html = output.read_text()
    assert '<img src=x onerror=alert(1)>' not in html
    assert '&lt;img src=x onerror=alert(1)&gt;' in html
    assert '<script>alert(1)</script>' not in html

def test_html_report_escapes_attribute_like_payloads(tmp_path):
    scan, findings = sample_objects()
    findings[0].evidence_summary = '" onmouseover="alert(1)'
    output = tmp_path / 'report.html'
    render(scan, findings, [], output, [], [])
    html = output.read_text()
    assert 'onmouseover="alert(1)' not in html

def test_json_report_is_valid_json_and_uses_v6_metadata(tmp_path):
    scan, findings = sample_objects()
    output = tmp_path / 'report.json'
    render_json(scan, findings, [], output, [], [])
    payload = json.loads(output.read_text())
    assert payload['meta']['version'] == VERSION
    assert payload['findings'][0]['rule_id'] == 'FW-TEST-001'

def test_csv_export_neutralizes_formula_injection(tmp_path):
    import csv
    scan, findings = sample_objects()
    findings[0].title = '=HYPERLINK("https://evil.test","open")'
    findings[0].description = '   =cmd|/C calc!A0'
    path = tmp_path / 'injection.csv'
    render_csv(scan, findings, path)
    row = next(csv.DictReader(path.open(encoding='utf-8-sig')))
    assert row['title'].startswith("'=")
    assert row['description'].startswith("'   =")

@pytest.mark.parametrize('formula', ['=1+1', '+cmd', '-2+3', '@SUM(A1:A3)', '\t=HYPERLINK("x")', '  =cmd'])
def test_spreadsheet_safe_neutralizes_formula_prefixes(formula):
    from app.report_extras import _spreadsheet_safe
    assert _spreadsheet_safe(formula).startswith("'")

@pytest.mark.parametrize('ordinary', ['hello', 'Critical finding', 'https://example.test/path', '1.23', ''])
def test_spreadsheet_safe_preserves_ordinary_values(ordinary):
    from app.report_extras import _spreadsheet_safe
    assert _spreadsheet_safe(ordinary) == ordinary
