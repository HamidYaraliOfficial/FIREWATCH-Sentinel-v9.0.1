from datetime import timedelta
from types import SimpleNamespace

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from app.db import Base
from app.models import Scan, ScanEvent, ScanStatus, WorkerLease, now_utc


def _db(tmp_path):
    engine = create_engine(f"sqlite:///{tmp_path / 'worker-leases.db'}", connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
    return engine, session_factory


def test_claim_creates_owner_lease_and_fresh_lease_heartbeat_is_accepted(tmp_path, monkeypatch):
    import app.worker as worker

    engine, factory = _db(tmp_path)
    db = factory()
    monkeypatch.setattr(worker, "SessionLocal", lambda: db)
    monkeypatch.setattr(worker, "settings", SimpleNamespace(worker_lease_timeout_seconds=60, worker_heartbeat_seconds=10))
    scan = Scan(target_url="https://target.example.test/", status=ScanStatus.QUEUED, config={})
    db.add(scan)
    db.commit()

    scan_id = worker.claim_one("worker-a")
    assert scan_id == scan.id
    lease = db.get(WorkerLease, scan_id)
    assert lease is not None and lease.worker_id == "worker-a"
    assert worker.heartbeat_once(scan_id, "worker-a") is True
    assert worker.heartbeat_once(scan_id, "worker-b") is False
    db.refresh(db.get(Scan, scan_id))
    assert db.get(Scan, scan_id).status == ScanStatus.RUNNING
    db.close()
    engine.dispose()


def test_stale_worker_lease_is_failed_with_audit_event_and_next_scan_can_be_claimed(tmp_path, monkeypatch):
    import app.worker as worker

    engine, factory = _db(tmp_path)
    db = factory()
    monkeypatch.setattr(worker, "SessionLocal", lambda: db)
    monkeypatch.setattr(worker, "settings", SimpleNamespace(worker_lease_timeout_seconds=60, worker_heartbeat_seconds=10))
    stale_time = now_utc() - timedelta(minutes=10)
    abandoned = Scan(
        target_url="https://abandoned.example.test/", status=ScanStatus.RUNNING,
        started_at=stale_time, created_at=stale_time, config={},
    )
    queued = Scan(target_url="https://queued.example.test/", status=ScanStatus.QUEUED, config={})
    db.add_all([abandoned, queued])
    db.commit()
    db.add(WorkerLease(scan_id=abandoned.id, worker_id="dead-worker", heartbeat_at=stale_time))
    db.commit()

    claimed_id = worker.claim_one("replacement-worker")
    db.refresh(db.get(Scan, abandoned.id))
    assert db.get(Scan, abandoned.id).status == ScanStatus.FAILED
    assert "lease expired" in db.get(Scan, abandoned.id).error.lower()
    assert db.get(WorkerLease, abandoned.id) is None
    assert claimed_id == queued.id
    events = list(db.scalars(select(ScanEvent).where(ScanEvent.scan_id == abandoned.id)))
    assert any(event.phase == "worker-recovery" for event in events)
    db.close()
    engine.dispose()


def test_running_legacy_scan_without_lease_is_recovered_after_timeout(tmp_path, monkeypatch):
    import app.worker as worker

    engine, factory = _db(tmp_path)
    db = factory()
    monkeypatch.setattr(worker, "SessionLocal", lambda: db)
    monkeypatch.setattr(worker, "settings", SimpleNamespace(worker_lease_timeout_seconds=60, worker_heartbeat_seconds=10))
    stale_time = now_utc() - timedelta(minutes=10)
    scan = Scan(
        target_url="https://legacy.example.test/", status=ScanStatus.RUNNING,
        started_at=stale_time, created_at=stale_time, config={},
    )
    db.add(scan)
    db.commit()

    assert worker.claim_one("worker-a") is None
    db.refresh(db.get(Scan, scan.id))
    assert db.get(Scan, scan.id).status == ScanStatus.FAILED
    db.close()
    engine.dispose()


def test_stale_orchestrator_checkpoint_does_not_overwrite_worker_recovery_failure(tmp_path):
    from app.orchestrator import ScanOrchestrator

    engine, factory = _db(tmp_path)
    with factory() as db:
        scan = Scan(
            target_url="https://recovered.example.test/", status=ScanStatus.FAILED,
            started_at=now_utc() - timedelta(minutes=10), config={},
        )
        db.add(scan)
        db.commit()
        runner = ScanOrchestrator(db)
        assert runner._cancel_checkpoint(scan) is True
        db.refresh(scan)
        assert scan.status == ScanStatus.FAILED
    engine.dispose()


def test_orchestrator_does_not_resurrect_failed_scan(tmp_path):
    import asyncio
    from app.orchestrator import ScanOrchestrator

    engine, factory = _db(tmp_path)
    with factory() as db:
        scan = Scan(target_url="https://terminal.example.test/", status=ScanStatus.FAILED, config={})
        db.add(scan)
        db.commit()
        asyncio.run(ScanOrchestrator(db).run(scan))
        db.refresh(scan)
        assert scan.status == ScanStatus.FAILED
    engine.dispose()
