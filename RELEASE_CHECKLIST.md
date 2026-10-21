# FIREWATCH Sentinel v9.0.1 Release Checklist

## Verified locally

- [x] `VERSION`, backend version metadata, README, UI and generated inventories are aligned to `9.0.1`.
- [x] Complete pytest suite passed: **5,948 collected cases across 62 modules**.
- [x] Full-suite statement coverage is **84.53%** (configured minimum: 80%).
- [x] Targeted network DNS-pinning, read-only HTTP policy, worker heartbeat and stale-lease recovery tests pass.
- [x] Python compilation (`python -m compileall -q backend/app backend/tests demo_target scripts`) passes.
- [x] Dashboard JavaScript syntax and publisher shell syntax pass.
- [x] Docker Compose YAML parses successfully with PyYAML.
- [x] Repository hygiene, assessment-plan export, test manifest and declared dependency inventory generation pass.
- [x] Demo report bundle verification validates all paths, file sizes and SHA-256 digests.

## Pending CI/deployment verification

- [ ] Re-run `python scripts/verify_release.py --coverage-shards 4` in an environment with sufficient execution budget. The local attempt timed out after two shards; do not treat the sharded gate as passed.
- [ ] Run Bandit and `pip-audit` in a network-enabled environment and resolve/triage all high/critical results.
- [ ] Build and run Docker Compose with Docker installed; exercise health/readiness and external worker recovery on PostgreSQL.
- [ ] Run hosted GitHub Actions/CodeQL and validate exact pinned dependencies.
- [ ] Rehearse schema migration/rollback and backups; configure secret-manager/KMS and rotation.
- [ ] Complete tenant-level identity and resource authorization before hosting mutually untrusted customers.
- [ ] Enforce network egress policy for Playwright/external scanners; validate with DNS-rebinding/SSRF tests in an isolated lab.
- [ ] Complete ZAP execution/integration, observability and independent penetration testing before making enterprise security claims.

The verification results in `VERIFICATION.md` distinguish passed checks from tests that could not be run in this environment.
