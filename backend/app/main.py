from __future__ import annotations

import asyncio
import csv
import hmac
import io
import json
import logging
import os
import re
import uuid
import zipfile
from datetime import date
from contextlib import asynccontextmanager
from pathlib import Path
from urllib.parse import urlsplit

from fastapi import Depends, FastAPI, Header, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, Response
from sqlalchemy import func, select, update
from sqlalchemy.orm import Session

from .check_catalog import CATALOG, coverage_matrix
from .assessment_catalog import get_assessment_plan
from .config import settings, validate_settings
from .db import get_db, init_db
from .models import (
    Asset, Evidence, Finding, FindingStatus, Page, Report, Scan, ScanEvent,
    ScanStatus, Severity, StandardsChecklistState, StandardsChecklistAudit,
)
from .worker import claim_one as claim_scan, process as process_claimed_scan
from .redaction import contains_sensitive_query, redact_data
from .schemas import AssetOut, EventOut, FindingOut, ScanCreate, ScanDetail, ScanSummary
from .scope import ScopePolicy, ScopeViolation
from .secret_store import protect_config, public_config
from .version import VERSION
from .bundle_manifest import build_report_manifest
from .standards_catalog import get_registry, checklist_document, get_control, list_controls, build_summary, state_to_dict
from .standards_schemas import ChecklistUpdate
from .redaction import redact_text

logging.basicConfig(level=getattr(logging, settings.log_level.upper(), logging.INFO))
logger = logging.getLogger("firewatch.api")
HERE = Path(__file__).resolve()
ROOT = HERE.parents[2] if (HERE.parents[2] / "frontend").exists() else HERE.parents[1]
FRONTEND = ROOT / "frontend"
REPORT_FORMATS = {
    "html": ("text/html", ".html"),
    "json": ("application/json", ".json"),
    "csv": ("text/csv; charset=utf-8", ".csv"),
    "markdown": ("text/markdown; charset=utf-8", ".md"),
    "sarif": ("application/sarif+json", ".sarif.json"),
}


async def queue_loop(stop_event: asyncio.Event):
    """Single-process development queue using the same lease policy as external workers."""
    worker_id = f"inline:{os.getpid()}:{uuid.uuid4().hex[:12]}"[:160]
    while not stop_event.is_set():
        scan_id = await asyncio.to_thread(claim_scan, worker_id)
        if scan_id:
            try:
                await process_claimed_scan(scan_id, worker_id)
            except Exception:
                logger.exception("queued scan failed: %s", scan_id)
        else:
            try:
                await asyncio.wait_for(stop_event.wait(), timeout=0.75)
            except asyncio.TimeoutError:
                pass


@asynccontextmanager
async def lifespan(_app):
    config_errors = validate_settings(settings)
    if config_errors:
        # Only setting names/ranges are reported; never echo key or credential values.
        raise RuntimeError("Invalid FIREWATCH configuration: " + "; ".join(config_errors))
    init_db()
    stop = asyncio.Event()
    # One in-process worker is appropriate for local/dev use only.
    # Disable it when running the separate `app.worker` process in production.
    task = asyncio.create_task(queue_loop(stop)) if getattr(settings, "enable_inline_worker", True) else None
    try:
        yield
    finally:
        stop.set()
        if task is not None:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass


def api_docs_options(environment: str) -> dict[str, str | None]:
    """Return documentation endpoints for a deployment environment.

    Production API schemas are disabled by default. If operators need interactive
    docs, expose them via a separately authenticated/internal documentation service.
    """
    if str(environment).strip().lower() in {"production", "prod"}:
        return {"docs_url": None, "redoc_url": None, "openapi_url": None}
    return {"docs_url": "/docs", "redoc_url": "/redoc", "openapi_url": "/openapi.json"}


app = FastAPI(
    title=settings.app_name,
    version=VERSION,
    lifespan=lifespan,
    **api_docs_options(settings.environment),
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[x.strip() for x in settings.cors_origins.split(",") if x.strip()],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PATCH", "OPTIONS", "DELETE"],
    allow_headers=["Content-Type", "Authorization", "X-API-Key"],
)


@app.middleware("http")
async def baseline_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "DENY")
    response.headers.setdefault("Referrer-Policy", "no-referrer")
    response.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
    if request.url.scheme == "https":
        response.headers.setdefault("Strict-Transport-Security", "max-age=31536000; includeSubDomains")
    if request.url.path == "/":
        response.headers.setdefault(
            "Content-Security-Policy",
            "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'",
        )
    return response


def require_api_key(x_api_key: str | None = Header(default=None)):
    configured = settings.api_key
    if not configured and settings.environment.lower() in {"production", "prod"}:
        raise HTTPException(503, "FIREWATCH_API_KEY must be configured in production")
    if configured and (not x_api_key or not hmac.compare_digest(x_api_key, configured)):
        raise HTTPException(401, "Valid X-API-Key header required")



_PROJECT_KEY_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,119}$")

def _validate_project_key(value: str) -> str:
    value = value.strip()
    if not _PROJECT_KEY_PATTERN.fullmatch(value):
        raise HTTPException(422, "project_key may contain only letters, digits, dot, underscore, colon and hyphen")
    return value

def _get_scan_or_404(scan_id: str, db: Session) -> Scan:
    scan = db.get(Scan, scan_id)
    if scan is None:
        raise HTTPException(404, "Scan not found")
    return scan


@app.get("/health")
def health():
    return {
        "status": "ok", "service": "firewatch-api", "version": VERSION,
        "scanner": "scope-controlled",
        "api_key_protection": bool(settings.api_key or settings.environment.lower() in {"production", "prod"}),
    }


@app.get("/ready")
def ready(db: Session = Depends(get_db)):
    try:
        db.execute(select(1)).scalar_one()
    except Exception as exc:
        logger.warning("readiness check failed: %s", type(exc).__name__)
        raise HTTPException(503, "Database is not ready") from exc
    return {"status": "ready", "database": "reachable"}


@app.get("/api/v1/coverage", dependencies=[Depends(require_api_key)])
def coverage():
    return {
        "baseline": ["OWASP Top 10:2025", "OWASP WSTG stable (v4.2)", "OWASP ASVS 5.0.0", "OWASP API Security Top 10:2023"],
        "catalog": CATALOG,
        "note": "Coverage is mapped at category/rule-family level. No finding is not proof of absence.",
    }


@app.get("/api/v1/assessment-plan", dependencies=[Depends(require_api_key)])
def assessment_plan():
    """Return the full test plan, explicitly separating automated checks from manual work."""
    return get_assessment_plan()



@app.get("/standards/STANDARDS_CHECKLIST.md")
def standards_checklist_markdown():
    """Serve the curated human-readable standards checklist."""
    path = ROOT / "standards" / "STANDARDS_CHECKLIST.md"
    if not path.is_file():
        raise HTTPException(404, "Standards checklist document not found")
    return FileResponse(path, media_type="text/markdown; charset=utf-8",
                        headers={"X-Content-Type-Options": "nosniff", "Content-Disposition": 'inline; filename="STANDARDS_CHECKLIST.md"'})


@app.get("/api/v1/standards/workbook", dependencies=[Depends(require_api_key)])
def standards_checklist_workbook():
    """Download the offline Excel checklist template, protected by the API key gate."""
    path = ROOT / "standards" / "FIREWATCH_Standards_Checklist_v9_Pro.xlsx"
    if not path.is_file():
        raise HTTPException(404, "Standards checklist workbook not found")
    return FileResponse(path, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        filename=path.name, headers={"X-Content-Type-Options": "nosniff"})


@app.get("/api/v1/standards/registry", dependencies=[Depends(require_api_key)])
def standards_registry():
    """Return the curated registry plus filter dimensions for the checklist UI."""
    registry = dict(get_registry())
    controls = checklist_document().get("controls", [])
    domains = {}
    for item in controls:
        domains[item["domain_id"]] = item["domain"]
    registry["domains"] = [{"id": key, "name": value} for key, value in sorted(domains.items())]
    registry["verification_modes"] = sorted({item["verification_mode"] for item in controls})
    registry["applicability_options"] = sorted({item["applicability"] for item in controls})
    registry["relationship_options"] = sorted({relationship for item in controls for relationship in item.get("relationship_types", [])})
    return registry


@app.get("/api/v1/standards/summary", dependencies=[Depends(require_api_key)])
def standards_summary(project_key: str = Query("default", min_length=1, max_length=120), db: Session = Depends(get_db)):
    project_key = _validate_project_key(project_key)
    rows = list_controls(db, project_key=project_key)
    summary = build_summary(rows)
    summary["framework_count"] = len(get_registry().get("frameworks", []))
    summary["domain_count"] = checklist_document().get("domain_count", 0)
    summary["catalog_control_count"] = checklist_document().get("total_controls", 0)
    summary["notice"] = checklist_document().get("important_notice", "")
    return summary


@app.get("/api/v1/standards/checklist", dependencies=[Depends(require_api_key)])
def standards_checklist(
    project_key: str = Query("default", min_length=1, max_length=120),
    framework_id: str | None = Query(default=None, max_length=80),
    domain_id: str | None = Query(default=None, max_length=40),
    priority: str | None = Query(default=None, pattern="^(P0|P1|P2|P3)$"),
    applicability: str | None = Query(default=None, pattern="^(core|conditional|adjacent)$"),
    status: str | None = Query(default=None, pattern="^(not_assessed|compliant|partially_compliant|non_compliant|not_applicable|blocked|evidence_pending)$"),
    verification_mode: str | None = Query(default=None, max_length=50),
    relationship: str | None = Query(default=None, pattern="^(direct|supporting|conditional|adjacent)$"),
    search: str | None = Query(default=None, max_length=250),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=100, ge=1, le=250),
    db: Session = Depends(get_db),
):
    project_key = _validate_project_key(project_key)
    known_frameworks = {item["id"] for item in get_registry().get("frameworks", [])}
    known_domains = {item["domain_id"] for item in checklist_document().get("controls", [])}
    known_modes = {item["verification_mode"] for item in checklist_document().get("controls", [])}
    if framework_id and framework_id not in known_frameworks:
        raise HTTPException(400, "Unknown framework_id")
    if domain_id and domain_id not in known_domains:
        raise HTTPException(400, "Unknown domain_id")
    if verification_mode and verification_mode not in known_modes:
        raise HTTPException(400, "Unknown verification_mode")
    rows = list_controls(db, project_key=project_key, framework_id=framework_id, domain_id=domain_id,
                         priority=priority, applicability=applicability, status=status,
                         verification_mode=verification_mode, relationship=relationship, search=search)
    total = len(rows)
    start = (page - 1) * page_size
    return {
        "project_key": project_key, "page": page, "page_size": page_size, "total": total,
        "pages": (total + page_size - 1) // page_size, "controls": rows[start:start + page_size],
        "notice": "A checklist state is a project tracking decision. It is not proof of certification; compliant requires evidence and reviewer metadata.",
    }


@app.get("/api/v1/standards/checklist/export.csv", dependencies=[Depends(require_api_key)])
def standards_checklist_csv(project_key: str = Query("default", min_length=1, max_length=120), db: Session = Depends(get_db)):
    project_key = _validate_project_key(project_key)
    rows = list_controls(db, project_key=project_key)
    out = io.StringIO(newline="")
    writer = csv.writer(out, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["control_id", "domain_id", "domain", "requirement", "acceptance_criteria", "expected_evidence",
                     "verification_mode", "priority", "applicability", "relationship", "relationship_types", "framework_ids", "status", "owner", "due_date",
                     "evidence_url", "evidence_note", "reviewer", "last_reviewed", "justification", "revision", "source_urls"])
    for row in rows:
        # Prefix strings that spreadsheet applications may interpret as formulas.
        def safe_cell(value):
            value = "" if value is None else str(value)
            return "'" + value if value.startswith(("=", "+", "-", "@", "\t", "\r")) else value
        writer.writerow([safe_cell(row.get(key, "")) for key in [
            "id", "domain_id", "domain", "requirement", "acceptance_criteria", "expected_evidence", "verification_mode",
            "priority", "applicability", "relationship"]] + [safe_cell(";".join(row.get("relationship_types", []))), safe_cell(";".join(row.get("framework_ids", [])))] + [safe_cell(row.get(key, "")) for key in [
            "status", "owner", "due_date", "evidence_url", "evidence_note", "reviewer", "last_reviewed", "justification", "revision"]] +
            [safe_cell(";".join(row.get("source_urls", [])))])
    safe_project_name = re.sub(r"[^A-Za-z0-9._-]", "_", project_key)
    filename = f"firewatch-standards-checklist-{safe_project_name}.csv"
    return Response(content="\ufeff" + out.getvalue(), media_type="text/csv; charset=utf-8",
                    headers={"Content-Disposition": f'attachment; filename="{filename}"', "X-Content-Type-Options": "nosniff"})


@app.patch("/api/v1/standards/checklist/{control_id}", dependencies=[Depends(require_api_key)])
def update_standards_control(control_id: str, payload: ChecklistUpdate, db: Session = Depends(get_db)):
    """Update a single project checklist control using optimistic concurrency and audit history."""
    definition = get_control(control_id)
    if definition is None:
        raise HTTPException(404, "Standards checklist control not found")
    current = db.scalar(select(StandardsChecklistState).where(
        StandardsChecklistState.project_key == payload.project_key,
        StandardsChecklistState.control_id == control_id,
    ))
    current_revision = current.revision if current else 0
    if payload.expected_revision != current_revision:
        raise HTTPException(409, f"Checklist revision conflict; current revision is {current_revision}")
    previous = state_to_dict(current) if current else None
    tracked_fields = ("owner", "due_date", "evidence_url", "evidence_note", "reviewer", "last_reviewed", "justification")
    merged = dict(previous or {})
    merged["status"] = payload.status
    for field in tracked_fields:
        if field in payload.model_fields_set:
            value = getattr(payload, field)
            if field in {"evidence_note", "justification", "owner", "reviewer"} and value:
                value = redact_text(value)
            merged[field] = value or ""
        else:
            merged.setdefault(field, "")
    if payload.status in {"compliant", "partially_compliant", "non_compliant"}:
        if not (merged.get("evidence_url") or len(str(merged.get("evidence_note") or "").strip()) >= 10):
            raise HTTPException(422, "This status requires an evidence URL or at least 10 characters of evidence_note")
        if not str(merged.get("reviewer") or "").strip():
            raise HTTPException(422, "This status requires a reviewer")
        if not str(merged.get("owner") or "").strip():
            raise HTTPException(422, "This status requires an owner")
    if payload.status == "not_applicable":
        if len(str(merged.get("justification") or "").strip()) < 20:
            raise HTTPException(422, "not_applicable requires a justification of at least 20 characters")
        if not str(merged.get("reviewer") or "").strip():
            raise HTTPException(422, "not_applicable requires a reviewer")
    if payload.status in {"compliant", "partially_compliant", "non_compliant", "not_applicable"} and not merged.get("last_reviewed"):
        merged["last_reviewed"] = date.today().isoformat()
    merged["revision"] = current_revision + 1
    if current is None:
        current = StandardsChecklistState(project_key=payload.project_key, control_id=control_id)
        db.add(current)
    for field in ("status", *tracked_fields, "revision"):
        value = merged.get(field)
        if value == "": value = None if field != "status" else "not_assessed"
        setattr(current, field, value)
    # Datetime is assigned server-side; client-supplied timestamps are never trusted.
    from .models import now_utc
    current.updated_at = now_utc()
    db.flush()
    new_state = state_to_dict(current)
    audit = StandardsChecklistAudit(
        project_key=payload.project_key, control_id=control_id,
        actor=redact_text(payload.updated_by)[:160] or "api-user", action="update",
        previous_state=previous, new_state=new_state,
    )
    db.add(audit)
    db.commit()
    return {"control_id": control_id, "project_key": payload.project_key, "definition": definition,
            "state": new_state, "audit_event_id": audit.id,
            "notice": "Checklist state is not independent certification. Evidence and reviewer fields are user supplied and must be verified."}


@app.get("/api/v1/standards/checklist/{control_id}/history", dependencies=[Depends(require_api_key)])
def standards_control_history(control_id: str, project_key: str = Query("default", min_length=1, max_length=120),
                             limit: int = Query(50, ge=1, le=200), db: Session = Depends(get_db)):
    project_key = _validate_project_key(project_key)
    if get_control(control_id) is None:
        raise HTTPException(404, "Standards checklist control not found")
    events = db.scalars(select(StandardsChecklistAudit).where(
        StandardsChecklistAudit.project_key == project_key,
        StandardsChecklistAudit.control_id == control_id,
    ).order_by(StandardsChecklistAudit.created_at.desc()).limit(limit)).all()
    return [{"id": item.id, "project_key": item.project_key, "control_id": item.control_id, "actor": item.actor,
             "action": item.action, "previous_state": item.previous_state, "new_state": item.new_state,
             "created_at": item.created_at.isoformat() if item.created_at else None} for item in events]


@app.post("/api/v1/scans", response_model=ScanSummary, status_code=201, dependencies=[Depends(require_api_key)])
def create_scan(payload: ScanCreate, db: Session = Depends(get_db)):
    if settings.require_scope_ack and not payload.scope_acknowledged:
        raise HTTPException(400, "scope_acknowledged must be true for an active security assessment")
    target = str(payload.target_url)
    if contains_sensitive_query(target):
        raise HTTPException(400, "Do not place credentials/tokens in the target URL; use encrypted authentication fields")
    try:
        # from_root performs URL validation, port-aware scope creation and private-IP checks.
        policy = ScopePolicy.from_root(
            target, exclusions=payload.exclusions,
            allow_private_targets=settings.allow_private_targets,
            allowed_hosts=payload.allowed_hosts,
        )
        target = policy.validate_url(target)
    except ScopeViolation as exc:
        raise HTTPException(400, str(exc)) from exc
    cfg = payload.model_dump(exclude={"target_url", "project_id", "scope_acknowledged"})
    try:
        cfg = protect_config(cfg)
    except Exception as exc:
        logger.exception("could not protect scan credentials")
        raise HTTPException(500, f"Could not safely encrypt scan credentials: {type(exc).__name__}") from exc
    scan = Scan(project_id=payload.project_id, target_url=target, config=cfg)
    db.add(scan)
    db.commit()
    db.refresh(scan)
    return scan


@app.get("/api/v1/scans", response_model=list[ScanSummary], dependencies=[Depends(require_api_key)])
def list_scans(limit: int = Query(50, ge=1, le=200), offset: int = Query(0, ge=0), db: Session = Depends(get_db)):
    return list(db.scalars(select(Scan).order_by(Scan.created_at.desc()).offset(offset).limit(limit)))


@app.get("/api/v1/scans/{scan_id}", response_model=ScanDetail, dependencies=[Depends(require_api_key)])
def get_scan(scan_id: str, db: Session = Depends(get_db)):
    scan = _get_scan_or_404(scan_id, db)
    counts = {
        "pages_count": db.scalar(select(func.count()).select_from(Page).where(Page.scan_id == scan.id)) or 0,
        "assets_count": db.scalar(select(func.count()).select_from(Asset).where(Asset.scan_id == scan.id)) or 0,
        "findings_count": db.scalar(select(func.count()).select_from(Finding).where(Finding.scan_id == scan.id)) or 0,
        "events_count": db.scalar(select(func.count()).select_from(ScanEvent).where(ScanEvent.scan_id == scan.id)) or 0,
    }
    data = {column.name: getattr(scan, column.name) for column in Scan.__table__.columns}
    data["config"] = public_config(scan.config)
    data.update(counts)
    return ScanDetail.model_validate(data)


@app.get("/api/v1/scans/{scan_id}/findings", response_model=list[FindingOut], dependencies=[Depends(require_api_key)])
def list_findings(
    scan_id: str,
    severity: Severity | None = None,
    status: FindingStatus | None = None,
    category: str | None = Query(default=None, max_length=100),
    limit: int = Query(200, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    _get_scan_or_404(scan_id, db)
    query = select(Finding).where(Finding.scan_id == scan_id)
    if severity is not None:
        query = query.where(Finding.severity == severity)
    if status is not None:
        query = query.where(Finding.status == status)
    if category:
        query = query.where(Finding.category == category)
    return list(db.scalars(query.order_by(Finding.risk_score.desc()).offset(offset).limit(limit)))


@app.get("/api/v1/scans/{scan_id}/events", response_model=list[EventOut], dependencies=[Depends(require_api_key)])
def list_events(scan_id: str, limit: int = Query(500, ge=1, le=2000), offset: int = Query(0, ge=0), db: Session = Depends(get_db)):
    _get_scan_or_404(scan_id, db)
    return list(db.scalars(
        select(ScanEvent).where(ScanEvent.scan_id == scan_id)
        .order_by(ScanEvent.created_at.asc()).offset(offset).limit(limit)
    ))


@app.get("/api/v1/scans/{scan_id}/assets", response_model=list[AssetOut], dependencies=[Depends(require_api_key)])
def list_assets(
    scan_id: str,
    kind: str | None = Query(default=None, max_length=60),
    limit: int = Query(500, ge=1, le=2000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    _get_scan_or_404(scan_id, db)
    query = select(Asset).where(Asset.scan_id == scan_id)
    if kind:
        query = query.where(Asset.kind == kind)
    return list(db.scalars(query.order_by(Asset.id).offset(offset).limit(limit)))


@app.get("/api/v1/scans/{scan_id}/evidence", dependencies=[Depends(require_api_key)])
def list_evidence(
    scan_id: str,
    finding_id: str | None = None,
    limit: int = Query(500, ge=1, le=2000),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    _get_scan_or_404(scan_id, db)
    query = select(Evidence).join(Finding, Evidence.finding_id == Finding.id).where(Finding.scan_id == scan_id)
    if finding_id:
        query = query.where(Evidence.finding_id == finding_id)
    items = list(db.scalars(query.order_by(Evidence.created_at.asc()).offset(offset).limit(limit)))
    return [{
        "id": item.id,
        "finding_id": item.finding_id,
        "kind": item.kind,
        "data": redact_data(item.data or {}),
        "created_at": item.created_at,
    } for item in items]


@app.get("/api/v1/scans/{scan_id}/coverage", dependencies=[Depends(require_api_key)])
def scan_coverage(scan_id: str, db: Session = Depends(get_db)):
    scan = _get_scan_or_404(scan_id, db)
    findings = list(db.scalars(select(Finding).where(Finding.scan_id == scan_id)))
    assets = db.scalar(select(func.count()).select_from(Asset).where(Asset.scan_id == scan_id)) or 0
    pages = db.scalar(select(func.count()).select_from(Page).where(Page.scan_id == scan_id)) or 0
    return {
        "scan_id": scan.id,
        "status": scan.status.value,
        "pages_discovered": pages,
        "assets_discovered": assets,
        "findings_recorded": len(findings),
        "catalog": coverage_matrix(findings),
        "interpretation": "finding_observed means at least one mapped rule produced a finding; no_finding_recorded_or_not_applicable is not a clean bill of health.",
    }


@app.post("/api/v1/scans/{scan_id}/cancel", dependencies=[Depends(require_api_key)])
def cancel_scan(scan_id: str, db: Session = Depends(get_db)):
    scan = _get_scan_or_404(scan_id, db)
    if scan.status in {ScanStatus.QUEUED, ScanStatus.RUNNING}:
        # Atomic transition so a concurrent completion cannot be overwritten.
        db.execute(update(Scan).where(
            Scan.id == scan_id,
            Scan.status.in_([ScanStatus.QUEUED, ScanStatus.RUNNING]),
        ).values(status=ScanStatus.CANCELED))
        db.commit()
        db.refresh(scan)
    return {"id": scan.id, "status": scan.status.value, "note": "Cancellation is cooperative; an in-flight request may finish before the worker stops."}


@app.get("/api/v1/scans/{scan_id}/diff", dependencies=[Depends(require_api_key)])
def scan_diff(scan_id: str, db: Session = Depends(get_db)):
    current = _get_scan_or_404(scan_id, db)
    if current.status != ScanStatus.COMPLETED:
        raise HTTPException(409, "Current scan must be completed before diffing")
    previous = db.scalar(
        select(Scan).where(Scan.target_url == current.target_url, Scan.status == ScanStatus.COMPLETED,
                           Scan.created_at < current.created_at)
        .order_by(Scan.created_at.desc()).limit(1)
    )
    if not previous:
        return {"scan_id": current.id, "baseline_scan_id": None, "added": [], "resolved": [], "unchanged": [],
                "message": "No previous completed scan for this exact target URL."}

    def keyed(scan_identifier: str):
        found = list(db.scalars(select(Finding).where(Finding.scan_id == scan_identifier)))
        data = {}
        for finding in found:
            parsed = urlsplit(finding.endpoint)
            key = f"{finding.rule_id}|{parsed.scheme.lower()}://{parsed.netloc.lower()}{parsed.path}"
            data.setdefault(key, {
                "rule_id": finding.rule_id, "title": finding.title, "severity": finding.severity.value,
                "endpoint": finding.endpoint, "status": finding.status.value, "risk_score": finding.risk_score,
            })
        return data

    old = keyed(previous.id)
    new = keyed(current.id)
    return {
        "scan_id": current.id, "baseline_scan_id": previous.id,
        "added": [new[key] for key in sorted(new.keys() - old.keys())],
        "resolved": [old[key] for key in sorted(old.keys() - new.keys())],
        "unchanged": [new[key] for key in sorted(new.keys() & old.keys())],
        "message": "Diff keys use rule ID + endpoint path (query values ignored). Manual review is recommended.",
    }


# Report paths come from the database, so never trust them as arbitrary filesystem
# paths. Resolve symlinks and require each file to stay beneath reports/<scan-id>/.
MAX_REPORT_FILE_BYTES = 32 * 1024 * 1024
MAX_REPORT_BUNDLE_BYTES = 64 * 1024 * 1024


def _resolve_scan_report_path(scan_id: str, stored_path: str) -> Path | None:
    try:
        reports_root = Path(settings.report_dir).expanduser().resolve()
        scan_root = (reports_root / scan_id).resolve()
        # A scan id must be one direct child of REPORT_DIR; this also rejects
        # malicious IDs and a scan-directory symlink pointing outside REPORT_DIR.
        if scan_root.parent != reports_root or scan_root.name != scan_id:
            return None
        candidate = Path(stored_path).expanduser().resolve(strict=True)
        candidate.relative_to(scan_root)
        if not candidate.is_file():
            return None
        return candidate
    except (OSError, RuntimeError, ValueError, TypeError):
        return None


def _log_report_access(scan_id: str, access_type: str, report_format: str = "bundle") -> None:
    # Never log target URLs, filenames from untrusted input, or API key material.
    logger.info("report_access scan_id=%s access_type=%s format=%s", scan_id, access_type, report_format)


@app.get("/api/v1/scans/{scan_id}/report", dependencies=[Depends(require_api_key)])
def report(scan_id: str, format: str = "html", db: Session = Depends(get_db)):
    if format not in REPORT_FORMATS:
        raise HTTPException(400, "Supported formats: html, json, csv, markdown, sarif")
    scan = _get_scan_or_404(scan_id, db)
    if scan.status != ScanStatus.COMPLETED:
        raise HTTPException(409, "Reports are available only after a scan completes")
    item = db.scalar(select(Report).where(Report.scan_id == scan.id, Report.format == format))
    path = _resolve_scan_report_path(scan.id, item.path) if item else None
    if path is None:
        raise HTTPException(404, "Report not available")
    try:
        size = path.stat().st_size
    except OSError as exc:
        raise HTTPException(404, "Report not available") from exc
    if size > MAX_REPORT_FILE_BYTES:
        raise HTTPException(413, "Report exceeds the configured download size limit")
    media_type, _ = REPORT_FORMATS[format]
    _log_report_access(scan.id, "single", format)
    return FileResponse(str(path), media_type=media_type, filename=path.name,
                        headers={"X-Content-Type-Options": "nosniff", "Cache-Control": "no-store"})


@app.get("/api/v1/scans/{scan_id}/bundle", dependencies=[Depends(require_api_key)])
def report_bundle(scan_id: str, db: Session = Depends(get_db)):
    scan = _get_scan_or_404(scan_id, db)
    if scan.status != ScanStatus.COMPLETED:
        raise HTTPException(409, "Report bundles are available only after a scan completes")
    rows = list(db.scalars(select(Report).where(Report.scan_id == scan.id).order_by(Report.format)))
    available: list[tuple[Report, Path]] = []
    total_size = 0
    for row in rows:
        if row.format not in REPORT_FORMATS:
            continue
        path = _resolve_scan_report_path(scan.id, row.path)
        if path is None:
            # Ignore invalid database paths; never bundle a path outside this scan.
            logger.warning("Skipping invalid report path for scan_id=%s format=%s", scan.id, row.format)
            continue
        try:
            size = path.stat().st_size
        except OSError:
            continue
        if size > MAX_REPORT_FILE_BYTES:
            raise HTTPException(413, "One report exceeds the configured download size limit")
        total_size += size
        if total_size > MAX_REPORT_BUNDLE_BYTES:
            raise HTTPException(413, "Report bundle exceeds the configured uncompressed size limit")
        available.append((row, path))
    if not available:
        raise HTTPException(404, "No reports are available for this scan yet")
    buffer = io.BytesIO()
    report_payloads = []
    for row, path in available:
        _, suffix = REPORT_FORMATS[row.format]
        report_payloads.append((row.format, suffix, path.read_bytes()))
    manifest = build_report_manifest(scan.id, report_payloads)
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for report_format, suffix, content in report_payloads:
            archive.writestr(f"{scan.id}/report{suffix}", content)
        archive.writestr(f"{scan.id}/manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        text_lines = ["FIREWATCH Sentinel report bundle", f"Application version: {VERSION}", "Hash algorithm: SHA-256"]
        for item in manifest["reports"]:
            text_lines.append(f"{item['format']}: {item['path']} | {item['size_bytes']} bytes | sha256={item['sha256']}")
        text_lines.append("NOTE: The manifest is not digitally signed.")
        archive.writestr(f"{scan.id}/manifest.txt", "\n".join(text_lines) + "\n")
    if len(buffer.getbuffer()) > MAX_REPORT_BUNDLE_BYTES:
        raise HTTPException(413, "Compressed report bundle exceeds the configured download size limit")
    _log_report_access(scan.id, "bundle")
    return Response(
        content=buffer.getvalue(),
        media_type="application/zip",
        headers={"Content-Disposition": f'attachment; filename="firewatch-sentinel-{scan.id}.zip"',
                 "X-Content-Type-Options": "nosniff", "Cache-Control": "no-store"},
    )


@app.get("/", response_class=HTMLResponse)
def ui():
    path = FRONTEND / "index.html"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return '<h1>FIREWATCH Sentinel v9.0.1</h1><p>Security assessment console.</p>'


@app.get("/static/{file_path:path}")
def static(file_path: str):
    path = (FRONTEND / "static" / file_path).resolve()
    try:
        path.relative_to((FRONTEND / "static").resolve())
    except ValueError as exc:
        raise HTTPException(404, "Not found") from exc
    if not path.is_file():
        raise HTTPException(404, "Not found")
    return FileResponse(path, headers={"X-Content-Type-Options": "nosniff"})
