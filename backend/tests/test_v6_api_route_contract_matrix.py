from app.version import VERSION
"""API contract tests using an isolated SQLite DB and synthetic non-sensitive data."""
import json
from datetime import timedelta
from pathlib import Path
from types import SimpleNamespace
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db import Base, get_db
from app.models import (
    Asset, Evidence, Finding, FindingStatus, Page, Report, Scan, ScanEvent,
    ScanStatus, Severity, now_utc,
)

@pytest.fixture
def api_store(tmp_path, monkeypatch):
    engine = create_engine(f"sqlite:///{tmp_path/'v6-api.db'}", connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)
    def override_db():
        db=Session()
        try: yield db
        finally: db.close()
    import app.main as main_module
    from app.config import Settings
    report_root = tmp_path / "reports"
    monkeypatch.setattr(main_module, "settings", Settings(report_dir=str(report_root), enable_inline_worker=False))
    app.dependency_overrides[get_db] = override_db
    try:
        with Session() as db:
            earlier = Scan(target_url="https://api.example.test/", status=ScanStatus.COMPLETED, config={}, created_at=now_utc()-timedelta(minutes=10))
            current = Scan(target_url="https://api.example.test/", status=ScanStatus.COMPLETED, config={}, created_at=now_utc())
            queued = Scan(target_url="https://queued.example.test/", status=ScanStatus.QUEUED, config={})
            running = Scan(target_url="https://running.example.test/", status=ScanStatus.RUNNING, config={})
            failed = Scan(target_url="https://failed.example.test/", status=ScanStatus.FAILED, config={})
            canceled = Scan(target_url="https://canceled.example.test/", status=ScanStatus.CANCELED, config={})
            db.add_all([earlier,current,queued,running,failed,canceled]); db.flush()
            old = Finding(scan_id=earlier.id, rule_id="FW-OLD-001", category="headers", title="Old issue", severity=Severity.LOW,
                confidence=.7, risk_score=1.75, status=FindingStatus.OPEN, endpoint="https://api.example.test/old?q=1", description="old", impact="old", remediation="fix", references=[], evidence_summary="old evidence", dedupe_key="old")
            current_finding = Finding(scan_id=current.id, rule_id="FW-NEW-001", category="headers", title="Current issue", severity=Severity.HIGH,
                confidence=.9, risk_score=7.2, status=FindingStatus.VERIFIED, endpoint="https://api.example.test/new", description="current", impact="impact", remediation="fix", references=[], evidence_summary="safe evidence", dedupe_key="new")
            shared = Finding(scan_id=current.id, rule_id="FW-SHARED-001", category="session", title="Shared issue", severity=Severity.MEDIUM,
                confidence=.8, risk_score=4, status=FindingStatus.OPEN, endpoint="https://api.example.test/shared", description="shared", impact="impact", remediation="fix", references=[], evidence_summary="safe evidence", dedupe_key="shared")
            db.add_all([old,current_finding,shared]); db.flush()
            db.add(Evidence(finding_id=current_finding.id, kind="headers", data={"Authorization":"Bearer this-must-not-leak", "url":"https://api.example.test/?token=must-not-leak"}))
            db.add(Page(scan_id=current.id, url="https://api.example.test/", title="Demo", headers={}, links=[], resources=[], technologies=[]))
            db.add(Asset(scan_id=current.id, url="https://api.example.test/", kind="page", method="GET", source="v6-test", metadata_json={}))
            db.add(Asset(scan_id=current.id, url="https://api.example.test/openapi.json", kind="api_spec", method="GET", source="v6-test", metadata_json={}))
            db.add(ScanEvent(scan_id=current.id, phase="crawl", message="demo event", progress=50))
            report_dir = report_root / current.id
            report_dir.mkdir(parents=True, exist_ok=True)
            report_path=report_dir/"report.json"; report_path.write_text(json.dumps({"meta":{"version":VERSION},"findings":[]}),encoding="utf-8")
            db.add(Report(scan_id=current.id, format="json", path=str(report_path)))
            db.commit()
            state={"earlier":earlier.id,"current":current.id,"queued":queued.id,"running":running.id,
                   "failed":failed.id,"canceled":canceled.id,"report_path":str(report_path)}
    except Exception:
        app.dependency_overrides.pop(get_db, None); engine.dispose(); raise
    yield Session, state
    app.dependency_overrides.pop(get_db, None)
    engine.dispose()


def test_v6_list_detail_and_pagination_contract(api_store):
    _, s=api_store
    with TestClient(app) as client:
        assert client.get("/api/v1/scans?limit=2&offset=0").status_code == 200
        assert client.get("/api/v1/scans?limit=0").status_code == 422
        detail=client.get(f"/api/v1/scans/{s['current']}")
        assert detail.status_code == 200
        data=detail.json()
        assert data["pages_count"] == 1 and data["assets_count"] == 2
        assert data["findings_count"] == 2 and data["events_count"] == 1
        assert "Bearer" not in json.dumps(data)
        assert client.get("/api/v1/scans/missing-scan-id").status_code == 404

@pytest.mark.parametrize("query,expected", [
    ("severity=high", 1), ("severity=medium", 1), ("status=verified", 1),
    ("status=false_positive", 0), ("category=session", 1), ("category=not-present", 0),
    ("limit=1&offset=0", 1), ("limit=1&offset=2", 0),
])
def test_v6_findings_filters_pagination_and_validation(api_store, query, expected):
    _, s=api_store
    with TestClient(app) as client:
        response=client.get(f"/api/v1/scans/{s['current']}/findings?{query}")
        assert response.status_code == 200
        assert len(response.json()) == expected
        assert client.get(f"/api/v1/scans/{s['current']}/findings?limit=0").status_code == 422


def test_v6_events_assets_evidence_and_coverage_routes(api_store):
    _,s=api_store
    with TestClient(app) as client:
        assert len(client.get(f"/api/v1/scans/{s['current']}/events").json()) == 1
        assert len(client.get(f"/api/v1/scans/{s['current']}/assets?kind=page").json()) == 1
        assert len(client.get(f"/api/v1/scans/{s['current']}/assets?kind=missing").json()) == 0
        evidence=client.get(f"/api/v1/scans/{s['current']}/evidence").json()
        body=json.dumps(evidence)
        assert "this-must-not-leak" not in body and "must-not-leak" not in body
        assert evidence[0]["data"]["Authorization"] == "[REDACTED]"
        coverage=client.get(f"/api/v1/scans/{s['current']}/coverage").json()
        assert coverage["pages_discovered"] == 1
        assert coverage["assets_discovered"] == 2
        assert coverage["findings_recorded"] == 2
        assert "not a clean bill of health" in coverage["interpretation"]


def test_v6_diff_identifies_added_resolved_and_unchanged_findings(api_store):
    _,s=api_store
    # Add a same-path shared issue to the earlier scan so one item is unchanged.
    from app.models import Finding
    with TestClient(app) as client:
        # No mutation required for status and first-scan branches.
        no_base=client.get(f"/api/v1/scans/{s['current']}/diff")
        assert no_base.status_code == 200
        result=no_base.json()
        assert result["baseline_scan_id"] == s["earlier"]
        assert {x["rule_id"] for x in result["added"]} == {"FW-NEW-001", "FW-SHARED-001"}
        assert {x["rule_id"] for x in result["resolved"]} == {"FW-OLD-001"}
        assert client.get(f"/api/v1/scans/{s['queued']}/diff").status_code == 409
        assert client.get("/api/v1/scans/unknown/diff").status_code == 404


def test_v6_report_format_errors_missing_files_and_download(api_store):
    _,s=api_store
    with TestClient(app) as client:
        assert client.get(f"/api/v1/scans/{s['current']}/report?format=exe").status_code == 400
        assert client.get(f"/api/v1/scans/{s['current']}/report?format=csv").status_code == 404
        report=client.get(f"/api/v1/scans/{s['current']}/report?format=json")
        assert report.status_code == 200 and report.json()["meta"]["version"] == VERSION
        bundle=client.get(f"/api/v1/scans/{s['current']}/bundle")
        assert bundle.status_code == 200 and bundle.headers["content-type"] == "application/zip"
        assert client.get("/api/v1/scans/missing/bundle").status_code == 404

@pytest.mark.parametrize("status,expected", [
    ("queued", "canceled"), ("running", "canceled"), ("completed", "completed"),
    ("failed", "failed"), ("canceled", "canceled"),
])
def test_v6_cancel_route_is_idempotent_for_terminal_states(api_store, status, expected):
    _,s=api_store
    with TestClient(app) as client:
        scan_id=s["current"] if status == "completed" else s[status]
        result=client.post(f"/api/v1/scans/{scan_id}/cancel")
        assert result.status_code == 200
        assert result.json()["status"] == expected
        assert "cooperative" in result.json()["note"]
