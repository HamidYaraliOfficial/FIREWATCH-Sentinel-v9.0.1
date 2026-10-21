# FIREWATCH Sentinel v9.0.1 — Hardening Patch

Release date: 2026-10-19

FIREWATCH Sentinel is an evidence-driven, scope-controlled platform for authorized web application security assessment. Version 9.0.1 is a security and reliability patch on the v9.0.0 codebase; it strengthens HTTP scope enforcement and worker recovery without claiming defect-free or certified security.

## Changes in v9.0.1

- **HTTP DNS pinning:** the default HTTP transport resolves each hostname before opening a TCP connection, validates every returned address, and connects to the selected IP literal. Mixed public/private answers fail closed when private targets are disabled. The original hostname remains in the HTTP request and HTTPS certificate/SNI checks. A pinned `httpcore` contract is used, and startup fails closed if the expected network-backend hook is unavailable.
- **Read-only request policy:** GET, HEAD, and OPTIONS are permitted without bodies. POST is restricted to the single reviewed GraphQL introspection query, a 16 KiB request limit, `application/json`, and a URL whose final path segment is `graphql`. Other methods and bodies are denied before network I/O.
- **Worker lease and recovery:** inline and external worker paths use heartbeat leases. A stale `RUNNING` scan is marked `FAILED`, emits a recovery event, and is not automatically replayed. This prevents indefinitely stuck jobs without risking duplicate execution of work that may not be idempotent. Automatic retry ceilings and exactly-once artifact publication remain future work.
- **Regression coverage:** tests exercise IP pinning, mixed and empty DNS answers, HTTP method/body policy, bounded GraphQL introspection, lease ownership, heartbeats, stale scan recovery, audit events, and stale-worker terminal-state fencing.
- **Release/package consistency:** versioned metadata, test inventory, dependency inventory, assessment plan, demo report bundle, and SHA-256 report manifests are refreshed for v9.0.1.
- **Runtime hardening:** Docker application process runs as an unprivileged numeric user; Compose services have restart and init behavior, and API/worker resource limits are kept aligned.

## Capabilities retained from v9.0.0

- Scope-controlled crawler with request pacing, URL/host/port/path checks, robots/sitemap guidance, JavaScript route heuristics, optional Playwright inventory, OpenAPI/Swagger and GraphQL discovery.
- Passive and low-impact rules for HTTP security headers, TLS, cookies, CORS, caching, information disclosure, and selected query-parameter reflection candidates.
- Credential configuration encryption, root-origin credential isolation, recursive evidence redaction, finding deduplication, confidence/risk scoring, and cancellation checks.
- HTML, JSON, CSV, Markdown, and SARIF reports; confined report downloads; ZIP report bundles with size and SHA-256 manifests and an independent verifier.
- Standards & Assurance workspace and curated control catalog, FastAPI API/dashboard, local demo target, Compose configuration, CI/CodeQL definitions, and publishing scripts.

## Local verification record

- **Collected/executed regression tests:** 5,948 across 62 modules; the complete suite passed in this environment.
- **Python statement coverage:** 84.53% in one full-suite coverage-instrumented run; minimum gate 80%.
- **Targeted worker/network integration checks:** passed, including lease recovery and the HTTP transport policy.
- **Python compileall, Node JavaScript syntax, Bash syntax, Compose YAML parse, repository hygiene, assessment plan export, test manifest generation, dependency inventory export:** passed.
- **Demo report bundle:** independent verifier passed; all archive paths, file sizes, and SHA-256 digests matched the updated manifest.
- A separate four-shard release-gate run exceeded the execution timeout after completing two shards. It is **not** counted as a successful sharded gate; the complete non-sharded suite and coverage run did finish successfully.

## Not verified in this environment

Bandit and `pip-audit` were unavailable, and package-index access was unavailable when an install was attempted. Docker CLI was not installed, so image build and runtime behavior were not verified. Hosted GitHub Actions and CodeQL were not executed. The installed runtime packages differed from some pinned requirements (for example, installed FastAPI/SQLAlchemy were older than the repository's declared pins), so run verification again in CI using the exact lock/requirements set before deployment. Playwright/Chromium against real targets and production PostgreSQL behavior require deployment-environment validation.

## Remaining production gates

- The common API key is not tenant identity, RBAC/ABAC, or resource-level authorization. Do not host mutually untrusted tenants until identity and per-resource authorization are designed and independently tested.
- Playwright and optional external tools use network stacks separate from the default pinned HTTP transport. An egress firewall/proxy allow-list and isolated scanning network remain mandatory defense in depth.
- The database uses `create_all()` and lacks versioned Alembic migrations; existing deployments need a rehearsed migration and rollback plan.
- The ZAP adapter writes a passive Automation Framework plan and checks reachability; it does not run the entire ZAP workflow or ingest alerts into findings.
- Worker stale-lease recovery now fails abandoned scans, but automatic retries, cancellation fencing for every external stage, and exactly-once report publication need more engineering.
- Production secret-manager/KMS integration and rotation, resolved SBOM, vulnerability audit, signed provenance, monitoring/alerting, backup/restore drills, and independent penetration testing remain open.

The assessment plan's manual and specialist-tool entries are a coverage plan, not evidence that those checks were automatically performed. Test counts and code coverage measure this application's regression suite, not vulnerability-detection accuracy. A scan with no findings is not proof of security or compliance.
