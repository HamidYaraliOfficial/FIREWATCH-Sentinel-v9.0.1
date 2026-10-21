from __future__ import annotations

import asyncio
import logging
import os
import socket
import threading
import time
import uuid
from datetime import datetime, timedelta, timezone

from sqlalchemy import select

from .config import settings, validate_settings
from .db import SessionLocal, init_db
from .models import Scan, ScanEvent, ScanStatus, WorkerLease, now_utc
from .orchestrator import ScanOrchestrator

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("firewatch.worker")


def _aware_utc(value: datetime) -> datetime:
    """Normalize SQLite's naive datetimes and DB-aware timestamps for comparison."""
    return value.replace(tzinfo=timezone.utc) if value.tzinfo is None else value.astimezone(timezone.utc)


def _recover_stale_scans(db, now: datetime) -> int:
    """Fail abandoned RUNNING scans; do not silently re-run potentially active work."""
    cutoff = now - timedelta(seconds=settings.worker_lease_timeout_seconds)
    recovered = 0
    running = list(db.scalars(
        select(Scan).where(Scan.status == ScanStatus.RUNNING).with_for_update(skip_locked=True)
    ))
    for scan in running:
        lease = db.get(WorkerLease, scan.id)
        last_seen = lease.heartbeat_at if lease is not None else (scan.started_at or scan.created_at)
        if last_seen is None or _aware_utc(last_seen) >= cutoff:
            continue
        scan.status = ScanStatus.FAILED
        scan.finished_at = now
        scan.error = "Worker lease expired; scan stopped without automatic replay. Review the scan and retry if appropriate."
        db.add(ScanEvent(
            scan_id=scan.id,
            phase="worker-recovery",
            message="Worker heartbeat lease expired; scan marked failed to prevent indefinite RUNNING status.",
            progress=0.0,
        ))
        if lease is not None:
            db.delete(lease)
        recovered += 1
    return recovered


def claim_one(worker_id: str | None = None) -> str | None:
    """Atomically recover stale work and claim the oldest queued scan."""
    owner = (worker_id or "local-worker")[:160]
    db = SessionLocal()
    try:
        now = now_utc()
        recovered = _recover_stale_scans(db, now)
        scan = db.scalar(
            select(Scan)
            .where(Scan.status == ScanStatus.QUEUED)
            .order_by(Scan.created_at.asc())
            .with_for_update(skip_locked=True)
            .limit(1)
        )
        claimed_id = None
        if scan is not None:
            scan.status = ScanStatus.RUNNING
            scan.started_at = now
            scan.finished_at = None
            scan.error = None
            db.add(WorkerLease(scan_id=scan.id, worker_id=owner, heartbeat_at=now))
            claimed_id = scan.id
        db.commit()
        if recovered:
            log.warning("recovered %d stale RUNNING scan(s)", recovered)
        return claimed_id
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def heartbeat_once(scan_id: str, worker_id: str, session_factory=None) -> bool:
    """Refresh a lease only while this worker still owns a RUNNING scan."""
    factory = session_factory or SessionLocal
    db = factory()
    try:
        lease = db.get(WorkerLease, scan_id)
        scan = db.get(Scan, scan_id)
        if lease is None or lease.worker_id != worker_id or scan is None or scan.status != ScanStatus.RUNNING:
            return False
        lease.heartbeat_at = now_utc()
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def _heartbeat_loop(scan_id: str, worker_id: str, stop: threading.Event, session_factory=None) -> None:
    interval = max(1, int(settings.worker_heartbeat_seconds))
    while not stop.wait(interval):
        try:
            if not heartbeat_once(scan_id, worker_id, session_factory=session_factory):
                log.warning("lease ownership lost for scan %s; heartbeat stopped", scan_id)
                return
        except Exception:
            # A transient database error is logged. If connectivity does not return,
            # the lease times out and the recovery pass fails the stale scan safely.
            log.exception("heartbeat update failed for scan %s", scan_id)


async def process(scan_id: str, worker_id: str = "local-worker", orchestrator_cls=None, session_factory=None) -> None:
    factory = session_factory or SessionLocal
    stop = threading.Event()
    heartbeat = threading.Thread(
        target=_heartbeat_loop,
        args=(scan_id, worker_id, stop, factory),
        name=f"firewatch-heartbeat-{scan_id[:8]}",
        daemon=True,
    )
    heartbeat.start()
    db = None
    try:
        db = factory()
        scan = db.get(Scan, scan_id)
        lease = db.get(WorkerLease, scan_id)
        if scan is None or scan.status != ScanStatus.RUNNING or lease is None or lease.worker_id != worker_id:
            log.warning("worker %s does not own RUNNING scan %s; refusing to process", worker_id, scan_id)
            return
        runner_cls = orchestrator_cls or ScanOrchestrator
        await runner_cls(db).run(scan)
    except Exception as exc:
        if db is not None:
            db.rollback()
            scan = db.get(Scan, scan_id)
            if scan is not None and scan.status == ScanStatus.RUNNING:
                scan.status = ScanStatus.FAILED
                scan.finished_at = now_utc()
                scan.error = f"Worker failed unexpectedly ({type(exc).__name__}); inspect worker logs and retry if appropriate."
                db.add(ScanEvent(scan_id=scan_id, phase="worker-error", message="Worker exited after an unexpected scan-processing error.", progress=0.0))
                db.commit()
        raise
    finally:
        stop.set()
        heartbeat.join(timeout=max(2, int(settings.worker_heartbeat_seconds) + 1))
        if db is not None:
            try:
                # Release only our own lease. A worker must never remove another worker's lease.
                lease = db.get(WorkerLease, scan_id)
                if lease is not None and lease.worker_id == worker_id:
                    db.delete(lease)
                    db.commit()
            except Exception:
                db.rollback()
                log.exception("could not release worker lease for scan %s", scan_id)
            finally:
                db.close()


def main() -> None:
    errors = validate_settings(settings)
    if errors:
        raise RuntimeError("Invalid FIREWATCH configuration: " + "; ".join(errors))
    init_db()
    worker_id = f"{socket.gethostname()}:{os.getpid()}:{uuid.uuid4().hex[:12]}"[:160]
    log.info("FIREWATCH worker started as %s", worker_id)
    while True:
        scan_id = claim_one(worker_id)
        if scan_id:
            try:
                asyncio.run(process(scan_id, worker_id))
            except Exception:
                log.exception("scan failed: %s", scan_id)
        else:
            time.sleep(1)


if __name__ == "__main__":
    main()
