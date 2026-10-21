# FIREWATCH Sentinel v9.0.1 — Production Readiness

This is a deployment checklist, not a certification. Do not publish an internet-facing instance until each item has an owner and completion evidence.

## Required configuration

- [ ] Set `ENVIRONMENT=production`.
- [ ] Set `FIREWATCH_API_KEY` to a randomly generated secret of at least 32 characters; store it in a secret manager, not source control.
- [ ] Use PostgreSQL or another explicitly supported production database; SQLite is rejected in production mode.
- [ ] Set `ALLOW_PRIVATE_TARGETS=false`; enforce outbound egress allow-lists at the host/network layer for both the HTTP transport and Playwright browser process. Application-level HTTP DNS pinning does not replace firewall isolation.
- [ ] Set `ENABLE_INLINE_WORKER=false` and run the external worker topology.
- [ ] Use explicit CORS origins; public origins must use HTTPS.
- [ ] Set a stable `FIREWATCH_SECRET_KEY` from a secret manager or mount a persistent, access-controlled `FIREWATCH_SECRET_KEY_FILE`. Back it up securely; losing it makes saved encrypted credentials unrecoverable.
- [ ] Keep API and database ports private. Bind public ingress through a TLS reverse proxy/WAF.
- [ ] Configure CPU, memory, PID, temporary-storage and browser shared-memory limits for backend, worker and browser processes.
- [ ] Set a suitable request timeout, concurrency ceiling and rate delay for each engagement.

## Before each assessment

- [ ] Confirm written authorization, exact hosts/ports, allowed paths, testing window and emergency contact.
- [ ] Confirm the target is not a third-party shared system outside the authorization.
- [ ] Confirm credentials belong to dedicated least-privileged test accounts and are not embedded in URLs.
- [ ] Set exclusions for destructive or irreversible paths and avoid mutating workflows.
- [ ] Agree request-rate limits with the service owner.
- [ ] Use a staging environment for browser-authenticated, role-comparison and canary testing when possible.

## Before each release

- [ ] Run `python scripts/verify_release.py` to completion in CI and retain the console output (the local sharded invocation timed out).
- [ ] Run `bandit -q -r backend/app -lll -iii`.
- [ ] Run `pip-audit -r backend/requirements.txt` with package-index access.
- [ ] Build and inspect the Docker images; run a local Demo Target end-to-end scan.
- [ ] Review the generated test and dependency inventories; commit no runtime reports, databases, credentials, coverage artifacts or local key files.
- [ ] Confirm CI and CodeQL completed in GitHub; resolve failures rather than relying only on local checks.
- [ ] Verify any distributed report ZIP with `python scripts/verify_report_bundle.py <bundle.zip>`.
- [ ] For multi-customer hosting, add an authenticated identity provider and project/resource-level RBAC/ABAC before deployment; the single shared API key is not a tenant boundary.
- [ ] Create and rehearse versioned database migrations, backups and rollback before upgrading a persistent production database.
- [x] Implement and unit-test worker heartbeat leases and stale `RUNNING` scan failure/audit events.
- [ ] Test crash recovery and alerting against PostgreSQL; define safe manual retry and idempotent artifact-publication procedures.
- [ ] Sign release artifacts through a trusted CI signing workflow if publisher authenticity is required; the report manifest hashes alone are not a signature.

## Incident / cleanup checklist

- [ ] Stop workers and revoke assessment credentials.
- [ ] Rotate exposed API/encryption keys if compromise is suspected.
- [ ] Preserve required evidence securely, then delete target data according to the engagement's retention policy.
- [ ] Record the affected release, target scope, time window and response steps without publishing secrets in public issues.
