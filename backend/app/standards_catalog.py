"""Versioned standards register and project-scoped checklist state helpers."""
from __future__ import annotations
import json
from functools import lru_cache
from pathlib import Path
from collections import Counter
from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import StandardsChecklistState

ROOT = Path(__file__).resolve().parents[2]
STANDARDS_DIR = ROOT / "standards"
REGISTRY_PATH = STANDARDS_DIR / "standards_registry.json"
CHECKLIST_PATH = STANDARDS_DIR / "standards_checklist.json"

@lru_cache(maxsize=1)
def registry_document() -> dict:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))

@lru_cache(maxsize=1)
def checklist_document() -> dict:
    data = json.loads(CHECKLIST_PATH.read_text(encoding="utf-8"))
    ids = [item.get("id") for item in data.get("controls", [])]
    if len(ids) != len(set(ids)):
        raise RuntimeError("Duplicate control IDs in standards checklist catalog")
    known = {item["id"] for item in registry_document().get("frameworks", [])}
    unknown = sorted({fid for item in data.get("controls", []) for fid in item.get("framework_ids", []) if fid not in known})
    if unknown:
        raise RuntimeError("Unknown framework IDs in standards checklist: " + ", ".join(unknown))
    return data

def get_registry() -> dict:
    return registry_document()

def get_control(control_id: str) -> dict | None:
    for item in checklist_document()["controls"]:
        if item["id"] == control_id:
            return dict(item)
    return None

def _state_dict(state: StandardsChecklistState) -> dict:
    return {
        "status": state.status, "owner": state.owner or "", "due_date": state.due_date or "",
        "evidence_url": state.evidence_url or "", "evidence_note": state.evidence_note or "",
        "reviewer": state.reviewer or "", "last_reviewed": state.last_reviewed or "",
        "justification": state.justification or "", "revision": state.revision,
        "updated_at": state.updated_at.isoformat() if state.updated_at else None,
    }

def list_controls(db: Session, *, project_key: str = "default", framework_id: str | None = None,
                  domain_id: str | None = None, priority: str | None = None,
                  applicability: str | None = None, status: str | None = None,
                  verification_mode: str | None = None, relationship: str | None = None,
                  search: str | None = None) -> list[dict]:
    states = db.scalars(select(StandardsChecklistState).where(StandardsChecklistState.project_key == project_key)).all()
    state_map = {state.control_id: state for state in states}
    query = (search or "").strip().casefold()
    rows = []
    for original in checklist_document()["controls"]:
        if framework_id and framework_id not in original["framework_ids"]: continue
        if domain_id and original["domain_id"] != domain_id: continue
        if priority and original["priority"] != priority: continue
        if applicability and original["applicability"] != applicability: continue
        if verification_mode and original["verification_mode"] != verification_mode: continue
        if relationship and relationship not in original.get("relationship_types", []): continue
        haystack = " ".join([original["id"], original["domain"], original["requirement"], *original["framework_ids"]]).casefold()
        if query and query not in haystack: continue
        row = dict(original)
        row["framework_mappings"] = list(original["framework_mappings"])
        state = state_map.get(original["id"])
        row["project_key"] = project_key
        row.update(_state_dict(state) if state else {"revision": 0, "updated_at": None})
        if status and row["status"] != status: continue
        rows.append(row)
    return rows

def build_summary(rows: list[dict]) -> dict:
    by_status = Counter(row["status"] for row in rows)
    by_priority = Counter(row["priority"] for row in rows)
    by_mode = Counter(row["verification_mode"] for row in rows)
    by_applicability = Counter(row["applicability"] for row in rows)
    assessed = sum(by_status[s] for s in ("compliant", "partially_compliant", "non_compliant", "not_applicable"))
    denominator = by_status["compliant"] + by_status["partially_compliant"] + by_status["non_compliant"]
    return {
        "project_key": rows[0]["project_key"] if rows else "default", "total_controls": len(rows),
        "by_status": dict(by_status), "by_priority": dict(by_priority),
        "by_verification_mode": dict(by_mode), "by_applicability": dict(by_applicability),
        "assessed_controls": assessed, "assessment_progress_pct": round(assessed / len(rows) * 100, 2) if rows else 0.0,
        "compliance_rate_pct": round(by_status["compliant"] / denominator * 100, 2) if denominator else None,
        "compliance_denominator": denominator,
        "interpretation": "Progress/compliance values describe checklist states only. They are not legal certification or standards conformance. N/A requires a documented justification; blocked/evidence-pending/not-assessed are not passes.",
    }

def state_to_dict(state: StandardsChecklistState) -> dict:
    return _state_dict(state)
