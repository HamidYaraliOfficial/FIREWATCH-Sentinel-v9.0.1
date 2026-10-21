from __future__ import annotations

import argparse
import asyncio
import os
import uuid
from pathlib import Path

from .config import settings
from .db import SessionLocal, init_db
from .models import Scan, ScanStatus, WorkerLease, now_utc
from .scope import ScopePolicy
from .orchestrator import ScanOrchestrator
from .worker import process as process_claimed_scan


async def run(args):
    init_db()
    policy = ScopePolicy.from_root(args.url, allow_private_targets=settings.allow_private_targets)
    # Enforce the same secret-query and URL policy as the API before persisting a CLI scan.
    safe_url = policy.validate_url(args.url)
    db = SessionLocal()
    scan = Scan(
        target_url=safe_url,
        config={
            "max_pages": args.pages,
            "max_depth": args.depth,
            "max_endpoints": args.endpoints,
            "request_delay_ms": args.delay,
            "enable_browser": not args.no_browser,
            "enable_api_introspection": not args.no_graphql,
            "passive_only": args.passive,
            "respect_robots": not args.ignore_robots,
            "exclusions": [],
            "allowed_hosts": [],
            "request_headers": {},
            "auth_cookies": None,
        },
    )
    db.add(scan)
    db.commit()
    db.refresh(scan)
    scan_id = scan.id
    # One-shot CLI scans also use a lease so a concurrent recovery pass cannot
    # mistake a long-running command for a dead worker.
    worker_id = f"cli:{os.getpid()}:{uuid.uuid4().hex[:12]}"[:160]
    scan.status = ScanStatus.RUNNING
    scan.started_at = now_utc()
    db.add(WorkerLease(scan_id=scan_id, worker_id=worker_id, heartbeat_at=now_utc()))
    db.commit()
    await process_claimed_scan(scan_id, worker_id, orchestrator_cls=ScanOrchestrator, session_factory=SessionLocal)
    db.expire_all()
    scan = db.get(Scan, scan_id)
    report_dir = Path(settings.report_dir) / scan_id
    print(f"[{scan.status.value}] {scan_id}\nHTML: {report_dir / 'report.html'}\nJSON: {report_dir / 'report.json'}")
    db.close()


def main():
    parser = argparse.ArgumentParser(description="FIREWATCH authorized web security scanner")
    parser.add_argument("url")
    parser.add_argument("--pages", type=int, default=300)
    parser.add_argument("--depth", type=int, default=8)
    parser.add_argument("--endpoints", type=int, default=2000)
    parser.add_argument("--delay", type=int, default=150)
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument("--no-graphql", action="store_true")
    parser.add_argument("--passive", action="store_true")
    parser.add_argument("--ignore-robots", action="store_true")
    args = parser.parse_args()
    asyncio.run(run(args))


if __name__ == "__main__":
    main()
