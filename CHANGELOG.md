## FIREWATCH Sentinel v9.0.1 — hardening patch (2026-10-19)

- Pin every default HTTP TCP connection to the IP addresses resolved for that connection, preserving original-host TLS/SNI and failing closed on non-public DNS answers when private targets are disabled. This closes the scanner HTTP client's DNS-rebinding time-of-check/time-of-use gap; network egress controls remain required for browser traffic and defense in depth.
- Enforce a read-only HTTP method policy in `SafeHTTPClient`: GET, HEAD and OPTIONS are allowed; POST is limited to the exact bounded GraphQL schema introspection query; other methods and request bodies are refused before network I/O.
- Add regression tests for IP pinning, mixed public/private DNS answers, DNS failures, safe GraphQL introspection and rejected mutation methods.
- Lock the tested `httpcore` version because socket pinning uses the underlying HTTP connection-pool network-backend contract and fails closed if that contract changes.
- Add heartbeat leases and stale `RUNNING` scan recovery for inline, external-worker and CLI execution. Stale scans are failed with an audit event rather than automatically replayed; retry/idempotency design remains open.
- Update deployment guidance to call out browser DNS/egress policy, tenant authorization, database migrations, retry semantics and other still-open production gates.

## FIREWATCH Sentinel v9.0.0 finalization (2026-10-19)

- Adopted the final product display name **FIREWATCH Sentinel** while retaining the established GitHub repository URL.
- Added stream-based HTTP response byte limits; unexpected content encodings are not decompressed/parsed and produce an explicit incomplete-analysis event.
- Constrained report paths to `REPORT_DIR/<scan-id>/`, rejecting path traversal and symlink escapes; added per-report and report-bundle size ceilings.
- Moved scan completion after report rendering and made the terminal scan state/report rows a single conditional persistence step so cancellation can win the race.
- Disabled Swagger, ReDoc and OpenAPI schema routes in production by default.
- Added 19 final-release regression cases for body streaming/encoding, report path confinement and production docs behavior.
- Local final verification: 5,931 pytest cases across 60 modules; 85.81% combined Python statement coverage across eight deterministic shards.
- Explicitly documented remaining blockers: shared-key/no tenant RBAC, DNS not pinned to the socket, ZAP plan-only adapter, no Alembic migrations, no worker leases, and independent deployment security reviews still required.

# Changelog

## v9 Pro — Standards & Assurance expansion (2026-10-15)

- Added a curated 67-reference standards/framework register and 469 paraphrased control objectives across 32 domains, including direct, supporting, conditional and adjacent sources.
- Added source-traceable Markdown, JSON, CSV and Excel checklist artefacts; the workbook includes Dashboard, Master Checklist, Standards Register, Domain Summary and Methodology sheets, status/priority validation and project-progress formulas.
- Added project-scoped standards APIs for registry, summary, filtering/pagination, state updates with revision conflict detection, audit history, CSV export and protected Excel download.
- Added checklist UI to the dashboard with filters, control detail, evidence, owner, due date, reviewer, N/A rationale, audit history and CSV/Excel exports.
- Added validation for project keys and evidence links; blocks user-info and token-like query strings, rejects invalid status transitions when required evidence/reviewer/owner is missing, and sanitizes exported filenames/CSV formula starts.
- Added standalone standards governance and API documentation plus an integration test module for catalogue consistency, endpoint contracts, evidence validation, status workflow, audit and export behavior.
- Clarified that mapped controls are a curated crosswalk, not certification or a clause-complete reproduction; legal/sector standards remain conditional and require expert applicability review.


## 9.0.0 — 2026-10-14

- Validate effective runtime configuration before startup; production mode fails closed on weak/missing API keys, SQLite, private-target override, inline worker mode, malformed resource limits, CORS origins and ZAP URL configuration.
- Report ZIP bundles now include a JSON integrity manifest with per-file SHA-256 and byte lengths; the text manifest carries the same digests and clearly states that it is not digitally signed.
- Add regression matrices for production settings and bundle-manifest integrity.
- Add declared dependency inventory generation for JSON/Markdown without claiming dependency resolution or SBOM completeness.
- Add threat-model and production-readiness documentation; update version branding, test catalogs, CI checks and publish scripts to v9.0.0.
- Build from a cleaned source tree, excluding Python bytecode, caches and local database artifacts.


All notable release changes are recorded here.

## 8.0.0 — 2026-10-13

### Security and scope hardening
- Enforce RFC-style header-token syntax, reject case-insensitive duplicate custom headers, and reject forbidden control characters before requests are queued.
- Reject embedded URL user-info and credential-like query parameters directly in the scan request schema.
- Bind configured additional-host scope declarations to their configured scheme as well as allowed port.
- Make path exclusions conservative across case variants and explicitly block multicast/reserved address classes; reject unescaped URL whitespace.
- Extend bounded recursive redaction to handle more layers of nested encoded return/redirect URLs.

### Expanded verification
- Added 11 v8 test modules for header protocol rules, adversarial URL/scope matrices, risk/status invariants, redaction properties, output sinks, schema limits, crawler parser robustness, API discovery, encrypted credential storage, origin isolation and transport boundaries.
- Updated release version metadata, test inventory generation and CI freshness checks to v8.0.0.
- The automated test total and coverage are published only after a full run; optional tools unavailable in the local build environment are explicitly listed as unverified.

### Safety boundary
- The default assessment remains bounded and non-destructive. A clean software test suite does not imply that every target vulnerability will be detected or that an assessed target is secure.

## 7.0.0 — 2026-10-13

### Security and correctness
- Tightened wildcard exclusion semantics: `/internal/*` covers the intended path and descendants without matching siblings such as `/internal-public`.
- Improved redaction of nested redirect/return URLs that are percent-encoded multiple times.
- Escaped target-derived content in Markdown reports to reduce raw HTML and Markdown-link injection; retained spreadsheet formula neutralization in CSV reports.
- API classification now matches `graphql` as a path segment, reducing substring false positives. Expanded inventory review for URL-like OpenAPI parameters.
- Reject whitespace-padded prohibited request header names and zero as an optional ZAP service port.
- Improved case-insensitive fingerprinting of PHP and Next.js markers.

### Test and release quality
- Added deterministic adversarial matrices for scope paths/ports, sensitive-field and nested-URL redaction, OpenAPI effective authentication, report sinks, origin credential isolation, crawling, schema boundaries, ZAP serialization, role-comparison boundaries, and safe GET canary behavior.
- Version metadata now uses a single application constant and v7 release manifests/catalog exports are generated from the live test collection.
- Raised the release coverage gate to 80%; local measurements are recorded only after the full suite completes.

### Safety boundary
- Default assessment remains bounded and non-destructive. Review candidates/manual cases are explicitly distinguished from validated vulnerabilities; the assessment catalog is not a count of tests automatically performed against arbitrary targets.

## 6.0.0 — 2026-10-12

### Origin and scope security
- Bind HTTP and browser authentication headers to the exact root origin (scheme, hostname, and effective port), preventing credentials from being sent to a different service on the same hostname.
- Reject URL user-information in the shared credential-origin guard.
- Normalize encoded path traversal multiple times for exclusion-policy comparison without mutating the actual request URL.
- Recursively redact credentials nested in redirect/return/next URL query values, with a recursion cap.
- Align the scan schema's restricted transport-header list with the HTTP client (`TE` and `Trailer` included).

### Test and release quality
- Added broad deterministic matrices for adversarial URL scope, nested redaction, Pydantic scan/header bounds, risk scoring, HTTP methods/redirect behavior, catalog/report contracts and API routes.
- Added an executable release verification script plus machine-generated test inventory and JUnit/coverage output options.
- CI coverage floor raised to 78% and release metadata/docs/dashboard updated to v6.0.0.
- Maintained a clear boundary between software-regression test counts and the separate security-assessment catalog.

### Safety boundary
- The scanner remains scope-controlled and non-destructive by default. Test-account, business-logic and specialist-tool cases are explicitly identified rather than reported as fully automated.

## 5.0.0 — 2026-10-09

### Assessment coverage and transparency
- Added a 79-case assessment plan mapped to OWASP Top 10:2025, OWASP ASVS 5.0.0, WSTG v4.2 stable and OWASP API Security Top 10:2023.
- Added `/api/v1/assessment-plan` and export formats JSON, CSV, and Markdown.
- Clearly separated built-in passive observations, automated review candidates, manual/test-account workflows, and specialist-tool-only tests.

### Security and correctness
- Expanded secret redaction for URLs, structured evidence, Authorization, cookies and credential-like values.
- Corrected URL rejection for control characters/backslashes and invalid port values.
- Corrected OpenAPI operation-level `security: []` review behavior.
- Added precise cookie attribute, SameSite=None/Secure, `__Host-` and `__Secure-` policy checks.
- Added CSP `object-src`/`base-uri`, cross-origin isolation and header-value review checks.
- Enabled Jinja HTML autoescaping for generated findings reports.
- Neutralized spreadsheet formula injection in CSV findings exports.
- Safely serialized optional ZAP automation YAML and validated ZAP base URLs.
- Fixed same-transaction asset de-duplication with SQLAlchemy sessions configured with `autoflush=False`.
- Hardened risk score handling for NaN, infinity and malformed confidence values.

### Test quality and GitHub automation
- Expanded the automated suite to 400 unit, matrix, regression and local end-to-end tests.
- Measured 80.39% statement coverage in the local build environment and added a 65% CI coverage threshold.
- Added Python 3.11/3.12/3.13 CI matrix, high-severity/high-confidence Bandit checks and `pip-audit` dependency review.
- Added test inventory, generated assessment catalog, v5 verification record and release notes.
- Updated publishing helpers and package metadata to v6.0.0.

### Boundaries
- Manual and specialist tests are not represented as automatically executed. FIREWATCH does not perform brute-force login attempts, destructive workflows, exploit chains, or arbitrary write/delete operations by default.

## 4.0.0 — 2026-10-09
- Isolated credentials to the root hostname and scheme; refused credential-like query strings.
- Added cancellation checkpoints, strict scope behavior, report bundle APIs and GitHub publishing helpers.

## 3.0.0
- Improved scope validation, credential encryption/redaction, API discovery, coverage catalog, multiple report outputs, and security tests.

## 2.0.0
- Added browser/API discovery and a broader low-impact rule catalog.

## 1.0.0
- Initial working assessment pipeline, queue, dashboard, findings, and HTML/JSON reports.
