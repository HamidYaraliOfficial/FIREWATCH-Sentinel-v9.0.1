# FIREWATCH Sentinel v9.0.1 — Verification Record

Verification date: 2026-10-19

## Local test results

- Collected and executed **5,948 pytest cases across 62 test modules**. The full suite completed without test failures.
- Full-suite Python statement coverage: **84.53%**, above the configured **80%** minimum gate.
- Targeted network/read-only-policy and worker lease/recovery tests passed.
- Python compilation (`compileall`), dashboard JavaScript syntax (`node --check`), publisher shell syntax (`bash -n`), Docker Compose YAML parsing, repository hygiene, assessment-plan export, test-manifest generation, and declared dependency inventory export passed.
- `examples/demo_scan/report-bundle.zip` passed `scripts/verify_report_bundle.py`, including manifest path, size and SHA-256 checks.
- The assessment plan contains 79 cases (22 passive automated observations, 13 automated review candidates, 38 manual/test-account cases and 6 specialist-tool cases). These are planned target-assessment activities, not all executed automated checks.

## Release-gate caveat

A separate `python scripts/verify_release.py --coverage-shards 4` run exceeded the environment's execution timeout after completing two of four coverage shards. This sharded gate is **not** reported as passed. The complete one-process pytest suite and full-suite coverage-instrumented run both completed successfully.

## Not run or not independently verified

- Bandit and `pip-audit` were not installed. An installation attempt failed because package-index/DNS access was unavailable.
- Docker CLI was absent, so a container image build and Compose runtime test were not possible.
- Hosted GitHub Actions, hosted CodeQL, production PostgreSQL behavior, and real-target browser execution were not run.
- The installed environment used Python 3.13.5 and packages that do not exactly match all repository-pinned versions (including older installed FastAPI and SQLAlchemy versions). Exact dependency-set verification remains a CI requirement.
- The generated dependency inventory is based on declared requirements. It is not a resolved SBOM or vulnerability audit. The report manifest is an integrity aid, not a digital signature or proof of publisher identity.

## Remaining production risks and gates

- The shared API key is not multi-tenant identity or resource-level RBAC/ABAC; `project_key` is a partitioning value, not a security boundary.
- The default HTTP transport now pins each TCP connection to validated IP addresses. Playwright and optional external tools have separate network stacks; enforce outbound firewall/proxy allow-lists and isolated scanning networks.
- The database uses `create_all()` and has no versioned Alembic migration framework. Existing installations need an explicit, rehearsed migration/rollback procedure, including the new `worker_leases` table.
- Worker heartbeats and stale-job recovery are implemented: an expired lease or legacy stale `RUNNING` record is failed with an audit event rather than automatically replayed. Automatic retry ceilings and exactly-once report publication remain incomplete.
- The ZAP adapter writes a passive Automation Framework plan and checks reachability; it does not automatically run a complete ZAP scan or import ZAP alerts.
- Production secret-manager/KMS integration and rotation, resolved SBOM, supply-chain signing/provenance, observability/alerting, backup/restore drills and independent penetration testing remain open deployment gates.

This package is a hardened, scope-controlled assessment tool, not defect-free or certified software. A lack of findings is not proof that a target is secure or compliant.
