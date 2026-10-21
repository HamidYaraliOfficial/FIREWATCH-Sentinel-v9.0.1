from app.version import VERSION
from fastapi.testclient import TestClient
from app.main import app

def test_health():
    with TestClient(app) as client:
        r=client.get('/health'); assert r.status_code==200; assert r.json()['version']==VERSION

def test_scope_ack_required():
    with TestClient(app) as client:
        r=client.post('/api/v1/scans',json={'target_url':'https://example.com/','scope_acknowledged':False})
        assert r.status_code==400


def test_api_key_protects_api_when_configured(monkeypatch):
    from types import SimpleNamespace
    import app.main as main_module
    monkeypatch.setattr(main_module, 'settings', SimpleNamespace(api_key='v4-test-api-key', environment='development'))
    with TestClient(app) as client:
        denied=client.get('/api/v1/coverage')
        allowed=client.get('/api/v1/coverage', headers={'X-API-Key':'v4-test-api-key'})
        assert denied.status_code==401
        assert allowed.status_code==200
        assert 'OWASP Top 10:2025' in allowed.json()['baseline']


def test_readiness_and_v4_security_headers():
    with TestClient(app) as client:
        ready = client.get('/ready')
        assert ready.status_code == 200
        assert ready.json()['status'] == 'ready'
        root = client.get('/')
        assert root.headers.get('x-content-type-options') == 'nosniff'
        assert root.headers.get('x-frame-options') == 'DENY'
        assert "frame-ancestors 'none'" in root.headers.get('content-security-policy', '')


def test_unknown_scan_evidence_returns_404():
    with TestClient(app) as client:
        response = client.get('/api/v1/scans/not-a-real-scan/evidence')
        assert response.status_code == 404


def test_v4_evidence_coverage_and_report_bundle_are_scoped_and_redacted(tmp_path, monkeypatch):
    import io
    import json
    import zipfile
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from fastapi.testclient import TestClient
    from app.db import Base, get_db
    from app.models import Evidence, Finding, FindingStatus, Report, Scan, ScanStatus, Severity
    from app.config import Settings
    import app.main as main_module

    report_root = tmp_path / "reports"
    monkeypatch.setattr(main_module, "settings", Settings(report_dir=str(report_root), enable_inline_worker=False))
    database_path = tmp_path / "api-v4.db"
    engine = create_engine(f"sqlite:///{database_path}", connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    TestSession = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)
    def override_db():
        db = TestSession()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_db
    try:
        with TestSession() as db:
            scan = Scan(target_url="https://example.test/", status=ScanStatus.COMPLETED, config={})
            db.add(scan)
            db.flush()
            finding = Finding(
                scan_id=scan.id, rule_id="TEST-REDACTION", category="configuration",
                title="Test evidence redaction", severity=Severity.MEDIUM, confidence=0.95,
                risk_score=42.0, status=FindingStatus.OPEN, endpoint="https://example.test/",
                description="Test-only finding", impact="Test-only impact", remediation="Test-only remediation",
                references=[], evidence_summary="Test evidence", dedupe_key="test-redaction",
            )
            db.add(finding)
            db.flush()
            db.add(Evidence(finding_id=finding.id, kind="request", data={
                "Authorization": "Bearer secret-that-must-not-be-returned",
                "url": "https://example.test/path?access_token=do-not-return",
                "observation": "response received",
            }))
            report_dir = report_root / scan.id
            report_dir.mkdir(parents=True, exist_ok=True)
            report_path = report_dir / "report.json"
            report_payload = {"meta": {"version": "4.0.0", "status": "completed"}, "findings": []}
            report_path.write_text(json.dumps(report_payload), encoding="utf-8")
            db.add(Report(scan_id=scan.id, format="json", path=str(report_path)))
            db.commit()
            scan_id, finding_id = scan.id, finding.id

        with TestClient(app) as client:
            evidence = client.get(f"/api/v1/scans/{scan_id}/evidence")
            assert evidence.status_code == 200
            body = evidence.json()
            assert body[0]["finding_id"] == finding_id
            assert body[0]["data"]["Authorization"] == "[REDACTED]"
            assert "do-not-return" not in json.dumps(body)

            coverage = client.get(f"/api/v1/scans/{scan_id}/coverage")
            assert coverage.status_code == 200
            assert coverage.json()["findings_recorded"] == 1

            report = client.get(f"/api/v1/scans/{scan_id}/report?format=json")
            assert report.status_code == 200
            assert report.json()["meta"]["version"] == "4.0.0"

            bundle = client.get(f"/api/v1/scans/{scan_id}/bundle")
            assert bundle.status_code == 200
            with zipfile.ZipFile(io.BytesIO(bundle.content)) as archive:
                names = archive.namelist()
                assert f"{scan_id}/report.json" in names
                assert f"{scan_id}/manifest.txt" in names
                assert f"{scan_id}/manifest.json" in names
                manifest = json.loads(archive.read(f"{scan_id}/manifest.json"))
                assert manifest["application_version"] == "9.0.1"
                report_entry = next(item for item in manifest["reports"] if item["format"] == "json")
                report_bytes = archive.read(f"{scan_id}/{report_entry['path']}")
                from hashlib import sha256
                assert report_entry["size_bytes"] == len(report_bytes)
                assert report_entry["sha256"] == sha256(report_bytes).hexdigest()
    finally:
        app.dependency_overrides.pop(get_db, None)
        engine.dispose()
