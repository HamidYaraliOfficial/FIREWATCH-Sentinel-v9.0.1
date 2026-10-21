# FIREWATCH Sentinel v9.0.1 — Hardening and Verification Record

## Summary

This maintenance release makes two security boundaries explicit in code and adds tests for them:

1. **Per-connection DNS pinning for normal HTTP traffic.** The default HTTP transport resolves the assessed host before the TCP connection and connects to the validated IP literal. HTTPS still uses the original URL hostname for Host/SNI/certificate verification. When `ALLOW_PRIVATE_TARGETS=false`, any DNS answer that is not globally routable causes the connection to fail closed, including mixed public/private answer sets.
2. **Read-only request enforcement.** The default `SafeHTTPClient` permits GET, HEAD and OPTIONS without bodies. The only permitted POST is the exact bounded GraphQL schema introspection query sent as JSON to a URL whose final path segment is `/graphql`. Other HTTP methods and arbitrary POST bodies are refused before the transport is called.

Inline and external worker paths use the same lease implementation. The orchestrator refuses to resurrect a terminal scan if its lease expires between claim and execution. The default HTTP transport fails closed if the installed HTTPX/HTTPCore connection-pool contract required for pinning changes. `httpcore` is directly version-constrained for reproducibility. Injected transports are used by tests; application/API configuration does not accept an injected transport.

## Verification performed in this workspace

- Existing plus new pytest suite with Python statement coverage gate.
- JavaScript syntax check (`node --check frontend/static/app.js`).
- Python bytecode compilation of app, tests, demo target and scripts.
- Bash syntax check for the publishing script.
- Docker Compose YAML parsing and generated inventory checks.
- Release-bundle integrity verification.

The exact totals are recorded in `VERIFICATION.md`. This workspace does not provide Docker, so Docker image build and container-runtime hardening are not claimed as verified. Bandit, `pip-audit`, hosted GitHub Actions and hosted CodeQL results must be recorded only if the respective tools/services actually run successfully.

## Important residual production gates

- Playwright does not use the pinned HTTPX transport. Enforce outbound egress filtering for the API, worker, browser and optional tools, denying loopback, private, link-local, metadata-service and other special-use addresses except explicit authorized exceptions.
- The common API-key gate is not multi-tenant identity and does not authorize per-project/per-resource access. Do not use a shared instance for mutually untrusted customers without identity integration and independent RBAC/ABAC testing.
- The database still uses `create_all()` without Alembic migrations. Existing production schemas require a planned, rehearsed migration and rollback process.
- Worker heartbeat leases and stale `RUNNING` scan detection are implemented: an expired lease is marked `FAILED` with an audit event, and the scan is not automatically replayed. Automatic retry ceilings, exactly-once report publication and PostgreSQL crash-recovery drills remain open.
- The optional ZAP integration writes a passive plan and checks reachability; it does not run a complete ZAP assessment or import ZAP alerts.
- A report SHA-256 manifest detects inconsistency but is not a digital signature or publisher identity proof.
- Full independent penetration testing, disaster-recovery drills, key rotation, TLS ingress, monitoring/alerting and incident-response exercises remain release gates.

## Interpretation

Passing tests demonstrates behavior exercised by those tests, not absence of all defects. FIREWATCH is a bounded, evidence-driven assessment tool and checklist—not a certification authority and not proof that a target is vulnerability-free.
