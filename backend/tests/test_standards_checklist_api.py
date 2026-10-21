"""Integration tests for the project-scoped standards checklist API."""
from __future__ import annotations
import csv
import io
import json
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
import app.main as main_module
from dataclasses import replace
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree
from app.db import Base, get_db
from app.config import settings
from app.standards_catalog import checklist_document, get_registry

@pytest.fixture
def standards_api_store(tmp_path):
    engine = create_engine(f"sqlite:///{tmp_path/'standards-api.db'}", connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)
    def override_db():
        db = Session()
        try:
            yield db
        finally:
            db.close()
    app.dependency_overrides[get_db] = override_db
    yield Session
    app.dependency_overrides.pop(get_db, None)
    engine.dispose()


def test_standards_registry_and_catalog_counts_are_consistent():
    registry = get_registry()
    catalog = checklist_document()
    assert len(registry["frameworks"]) == 67
    assert len(catalog["controls"]) == 469
    assert catalog["framework_count"] == len(registry["frameworks"])
    assert len({row["id"] for row in catalog["controls"]}) == 469
    known = {row["id"] for row in registry["frameworks"]}
    assert all(set(row["framework_ids"]).issubset(known) for row in catalog["controls"])


def test_registry_endpoint_has_official_sources_and_notice(standards_api_store):
    with TestClient(app) as client:
        response = client.get("/api/v1/standards/registry")
    assert response.status_code == 200
    body = response.json()
    assert len(body["frameworks"]) == 67
    assert all(item["official_url"].startswith("https://") for item in body["frameworks"])


def test_checklist_default_page_contract_and_required_fields(standards_api_store):
    with TestClient(app) as client:
        response = client.get("/api/v1/standards/checklist?page=1&page_size=10")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 469
    assert len(data["controls"]) == 10
    control = data["controls"][0]
    for key in ("id", "requirement", "acceptance_criteria", "expected_evidence", "verification_mode", "priority", "applicability", "relationship", "relationship_types", "framework_ids", "source_urls", "status", "revision"):
        assert key in control
    assert control["status"] == "not_assessed" and control["revision"] == 0


@pytest.mark.parametrize("query", [
    "priority=P0", "priority=P1", "priority=P2", "priority=P3",
    "applicability=core", "applicability=conditional", "applicability=adjacent",
    "status=not_assessed", "verification_mode=manual_review",
    "framework_id=OWASP_ASVS", "domain_id=GOV", "search=authorization", "relationship=direct",
])
def test_checklist_filter_contracts_are_nonempty_or_well_formed(standards_api_store, query):
    with TestClient(app) as client:
        response = client.get("/api/v1/standards/checklist?" + query)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["total"] >= 0
    assert len(data["controls"]) <= data["page_size"]
    assert all(isinstance(item.get("framework_ids"), list) for item in data["controls"])


@pytest.mark.parametrize("query", [
    "framework_id=DOES_NOT_EXIST", "priority=CRITICAL", "applicability=unknown",
    "status=passed", "relationship=unknown", "project_key=../invalid", "project_key=bad%0Akey", "page=0", "page_size=251",
])
def test_checklist_rejects_invalid_filters_and_project_keys(standards_api_store, query):
    with TestClient(app) as client:
        response = client.get("/api/v1/standards/checklist?" + query)
    assert response.status_code in (400, 422), response.text


def test_summary_has_status_progress_and_non_certification_interpretation(standards_api_store):
    with TestClient(app) as client:
        response = client.get("/api/v1/standards/summary?project_key=default")
    assert response.status_code == 200
    data = response.json()
    assert data["total_controls"] == 469
    assert data["framework_count"] == 67
    assert data["domain_count"] == 32
    assert data["assessment_progress_pct"] == 0
    assert data["compliance_rate_pct"] is None
    assert "not legal certification" in data["interpretation"] or "legal certification" in data["interpretation"]


def test_compliant_status_requires_evidence_owner_and_reviewer(standards_api_store):
    control_id = checklist_document()["controls"][0]["id"]
    with TestClient(app) as client:
        response = client.patch(f"/api/v1/standards/checklist/{control_id}", json={
            "status": "compliant", "expected_revision": 0, "project_key": "default"
        })
    assert response.status_code == 422


def test_checklist_update_persists_revision_and_audit_history(standards_api_store):
    control_id = checklist_document()["controls"][0]["id"]
    payload = {
        "project_key": "project-alpha", "status": "compliant", "expected_revision": 0,
        "owner": "AppSec owner", "reviewer": "Independent reviewer",
        "evidence_note": "Reviewed signed evidence package EVT-1042 and verified current production-equivalent build.",
        "due_date": "2026-12-01", "last_reviewed": "2026-10-15", "updated_by": "test-actor",
    }
    with TestClient(app) as client:
        response = client.patch(f"/api/v1/standards/checklist/{control_id}", json=payload)
        assert response.status_code == 200, response.text
        state = response.json()["state"]
        assert state["status"] == "compliant" and state["revision"] == 1
        stale = client.patch(f"/api/v1/standards/checklist/{control_id}", json=payload)
        assert stale.status_code == 409
        listed = client.get("/api/v1/standards/checklist?project_key=project-alpha&status=compliant&page_size=5")
        assert listed.status_code == 200 and listed.json()["total"] == 1
        history = client.get(f"/api/v1/standards/checklist/{control_id}/history?project_key=project-alpha")
        assert history.status_code == 200 and len(history.json()) == 1
        assert history.json()[0]["previous_state"] is None
        assert history.json()[0]["new_state"]["revision"] == 1


def test_not_applicable_requires_reason_and_reviewer(standards_api_store):
    control_id = checklist_document()["controls"][0]["id"]
    with TestClient(app) as client:
        short = client.patch(f"/api/v1/standards/checklist/{control_id}", json={
            "status": "not_applicable", "expected_revision": 0, "project_key": "default",
            "justification": "not used", "reviewer": "reviewer"
        })
        assert short.status_code == 422
        valid = client.patch(f"/api/v1/standards/checklist/{control_id}", json={
            "status": "not_applicable", "expected_revision": 0, "project_key": "default",
            "justification": "This requirement does not apply because the product has no mobile client; confirmed in scope review.",
            "reviewer": "reviewer"
        })
        assert valid.status_code == 200, valid.text
        assert valid.json()["state"]["status"] == "not_applicable"


@pytest.mark.parametrize("url", [
    "https://user:pass@example.com/evidence", "https://evidence.example/?access_token=secret",
    "https://evidence.example/?signature=secret", "file:///etc/passwd", "javascript:alert(1)",
    "https://evidence.example:0/path", "not-a-url",
])
def test_evidence_url_rejects_userinfo_tokens_and_unsafe_urls(standards_api_store, url):
    control_id = checklist_document()["controls"][0]["id"]
    with TestClient(app) as client:
        response = client.patch(f"/api/v1/standards/checklist/{control_id}", json={
            "status": "evidence_pending", "expected_revision": 0, "project_key": "default", "evidence_url": url
        })
    assert response.status_code == 422, (url, response.status_code, response.text)


def test_csv_export_has_utf8_bom_correct_rows_and_safe_filename(standards_api_store):
    with TestClient(app) as client:
        response = client.get("/api/v1/standards/checklist/export.csv?project_key=team:blue")
    assert response.status_code == 200
    assert response.content.startswith(b"\xef\xbb\xbf")
    assert "firewatch-standards-checklist-team_blue.csv" in response.headers["content-disposition"]
    rows = list(csv.reader(io.StringIO(response.content.decode("utf-8-sig"))))
    assert len(rows) == 470
    assert rows[0][0] == "control_id" and rows[1][0].startswith("FWPRO-")


def test_api_key_gate_protects_standards_endpoints(standards_api_store, monkeypatch):
    monkeypatch.setattr(main_module, "settings", replace(settings, api_key="replace-this-test-key-for-api-gate"))
    with TestClient(app) as client:
        assert client.get("/api/v1/standards/registry").status_code == 401
        response = client.get("/api/v1/standards/registry", headers={"X-API-Key": "replace-this-test-key-for-api-gate"})
    assert response.status_code == 200


def test_markdown_checklist_and_excel_workbook_downloads(standards_api_store):
    with TestClient(app) as client:
        markdown = client.get("/standards/STANDARDS_CHECKLIST.md")
        workbook = client.get("/api/v1/standards/workbook")
    assert markdown.status_code == 200 and "469" in markdown.text
    assert "حدود ادعا" in markdown.text and "469" in markdown.text
    assert workbook.status_code == 200
    assert workbook.headers["content-type"].startswith("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    assert workbook.content[:2] == b"PK" and len(workbook.content) > 10_000


def test_project_key_validation_applies_to_summary_history_and_export(standards_api_store):
    control_id = checklist_document()["controls"][0]["id"]
    with TestClient(app) as client:
        assert client.get("/api/v1/standards/summary?project_key=../unsafe").status_code == 422
        assert client.get(f"/api/v1/standards/checklist/{control_id}/history?project_key=../unsafe").status_code == 422
        assert client.get("/api/v1/standards/checklist/export.csv?project_key=../unsafe").status_code == 422


def test_excel_workbook_is_valid_xlsx_with_expected_tabs_and_data_validation():
    root = Path(__file__).resolve().parents[2]
    workbook = root / "standards" / "FIREWATCH_Standards_Checklist_v9_Pro.xlsx"
    assert workbook.is_file() and workbook.stat().st_size > 10_000
    with ZipFile(workbook) as archive:
        assert archive.testzip() is None
        names = set(archive.namelist())
        assert "xl/workbook.xml" in names
        assert any(name.startswith("xl/tables/table") and name.endswith(".xml") for name in names)
        xml = ElementTree.fromstring(archive.read("xl/workbook.xml"))
        ns = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
        tabs = {node.attrib["name"] for node in xml.findall(".//x:sheets/x:sheet", ns)}
        assert {"Dashboard", "Master Checklist", "Standards Register", "Domain Summary", "Methodology"}.issubset(tabs)
        assert any("worksheets/sheet1.xml" in name for name in names)


def test_registry_mapping_names_versions_are_traceable():
    registry = {item["id"]: item for item in get_registry()["frameworks"]}
    for control in checklist_document()["controls"]:
        mapping_ids = {mapping["framework_id"] for mapping in control["framework_mappings"]}
        assert mapping_ids.issubset(registry)
        assert set(control["framework_ids"]) == mapping_ids
        for mapping in control["framework_mappings"]:
            assert mapping["framework_name"] == registry[mapping["framework_id"]]["name"]
            assert mapping["version"] in registry[mapping["framework_id"]]["version_or_status"]


def test_standards_registry_classifies_direct_conditional_and_supporting_sources():
    relationships = {item["relationship"] for item in get_registry()["frameworks"]}
    assert {"direct", "supporting", "conditional", "adjacent"}.issubset(relationships)
    conditional = [item for item in get_registry()["frameworks"] if item["relationship"] == "conditional"]
    assert conditional and all(item["use_and_limitations"] for item in conditional)
    assert all(item["mapped_control_count"] > 0 for item in get_registry()["frameworks"])
