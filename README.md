# FIREWATCH Sentinel v9.0.1

**An evidence-driven, scope-controlled platform for authorized web application security assessment.**

[![CI](https://github.com/HamidYaraliOfficial/FIREWATCH-WebSec-Agent/actions/workflows/ci.yml/badge.svg)](https://github.com/HamidYaraliOfficial/FIREWATCH-WebSec-Agent/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![API](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)
![Security](https://img.shields.io/badge/Mode-Scope--controlled-15803d)
![Version](https://img.shields.io/badge/version-9.0.1-2563eb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

FIREWATCH Sentinel combines bounded reconnaissance, HTTP/browser inventory, API discovery, low-impact security checks, evidence handling, role-comparison review candidates, risk ranking, and multi-format reporting. It is designed to support repeatable assessments—not to claim that automation can prove an application is vulnerability-free. Maintained by [Hamid Yarali](https://github.com/HamidYaraliOfficial).

**v9.0.1 security hardening:** the default HTTP transport pins each TCP connection to a validated IP address and refuses non-read-only methods except the exact, bounded GraphQL introspection query. The browser process still requires egress firewall/proxy restrictions. See [`docs/RELEASE_HARDENING_V9_0_1.md`](docs/RELEASE_HARDENING_V9_0_1.md) for verification results and remaining production gates.

> **Authorized use only.** Test only systems you own or are explicitly authorized to assess. Review the target, allowed hosts/ports, exclusions, rate, and test window before every scan. Production mode requires an API key.

## What's new in v9.0.1

- **Startup configuration gate:** invalid resource limits and malformed CORS/ZAP configuration fail closed; production requires a strong API key, a non-SQLite database, restricted private-target setting, and external worker topology.
- **Verifiable report bundles:** every ZIP bundle now includes `manifest.json` and `manifest.txt` with each report's byte size and SHA-256. The manifest is not digitally signed; use an external signing system when authenticity across trust boundaries is required.
- **Declared dependency inventory:** generated JSON/Markdown lists declared requirements and version constraints without misrepresenting ranges as resolved package versions.
- **Independent report-bundle verifier:** `python scripts/verify_report_bundle.py <bundle.zip>` verifies archive paths, manifest/file list agreement, byte lengths and SHA-256 digests.
- **Staged combined coverage:** module-balanced coverage shards can be run in stages; the runner fingerprints the collected test inventory and refuses to finalize coverage until every shard has passed against the same inventory.
- **Fail-closed production gate:** validates timeout/page/depth/endpoint/probe/concurrency ceilings; CORS and optional ZAP origins; strong API key; Postgres; private target prohibition; external worker topology; stable secret-key configuration.
- **Release readiness docs:** threat model, production checklist, GitHub release checklist and declared dependency inventory.

- **Expanded regression suite:** adversarial URL/scope, recursive redaction, OpenAPI security semantics, report sink safety, transport/origin isolation, crawler parser behavior, schema validation, authorization-review boundaries and safe parameter-probe matrices. The collected inventory is generated in `docs/TEST_MATRIX_V9.md` and `docs/TEST_MANIFEST_V9.json`.
- **Security fixes driven by tests:** correct wildcard exclusion boundaries; recognition and redaction of multiply encoded nested URLs; Markdown output escaping; exact-segment GraphQL classification; additional URL-like OpenAPI input discovery; whitespace-normalized prohibited-header rejection; and zero-port rejection for the optional ZAP endpoint.
- **Crawler correctness:** case-insensitive PHP and Next.js indicators; synthetic tests for links, forms, JavaScript routes, common technology markers and exclusion behavior.
- **Release verification:** Python 3.11/3.12/3.13 CI matrix, 80% Python statement coverage gate, generated assessment/test inventories, JS and shell syntax, YAML parse, repository hygiene, CodeQL, Bandit and dependency audit.
- **Transparent limitations:** software test counts/coverage are not vulnerability-detection rates. The independent assessment catalog labels items requiring manual workflows, dedicated test accounts, or specialist tools.
- **Bounded response handling:** HTTP bodies are captured with a streaming byte cap (`MAX_RESPONSE_BODY_BYTES`, default 2,000,000 bytes); unexpectedly compressed responses are not decompressed and are marked as incomplete content analysis.
- **Report path and size hardening:** individual report downloads are constrained to `REPORT_DIR/<scan-id>/`, symlink/path escapes are rejected, individual reports are capped at 32 MiB, and report bundles at 64 MiB.
- **Atomic scan finalization:** reports are rendered first and the completed status plus report records are committed together with a conditional transition; a concurrent cancellation wins.
- **Production API docs:** Swagger, ReDoc and OpenAPI JSON are disabled in production by default.
- **Final release verification:** **5,948 pytest cases across 62 modules**, with **84.53% Python statement coverage** in one full-suite run (80% minimum gate).

## Capabilities

### Discovery and inventory

- Bounded HTTP crawler with deduplication, configurable maximum pages/depth/endpoints, concurrency ceilings, and request pacing.
- Robots.txt and recursive sitemap discovery, with robots treated as crawler guidance—not as permission to test.
- HTML links, forms, resources, mixed-content references, JavaScript route heuristics, and technology indicators.
- Optional Playwright Chromium observation of in-scope requests, resources, forms, cookie names, and storage **keys**; values are not exported by the browser inventory.
- OpenAPI/Swagger JSON/YAML discovery, operation inventory, basic security-declaration review, GraphQL discovery, and optional read-only introspection.

### Low-impact security assessment

- HTTP security headers, CSP policy indicators, HSTS, transport redirects, TLS/certificate posture, cookie flags, form/password transport indicators, CORS observations, caching indicators, information disclosure signatures, third-party script SRI review, and client-visible secret-pattern checks.
- A bounded, harmless alphanumeric GET canary for selected query parameters. Reflection is reported as a review candidate, not as proof of XSS.
- Optional read-only GET comparisons across tester-supplied authorization profiles. These are **review candidates**, not automatic proof of IDOR/BOLA.
- OWASP category/rule-family mapping in a coverage matrix. A category with no recorded finding may be untested, not applicable, or simply not detected.

### Evidence and reporting

- Finding deduplication, confidence and risk score, evidence redaction, scan events and status history.
- Report formats: **HTML, JSON, CSV, Markdown, SARIF 2.1.0**.
- REST endpoints for scan comparison, evidence, coverage, and ZIP report bundles.
- API-key gate, encrypted-at-rest scan authentication configuration, and response-header hardening.


## Standards & Assurance Checklist (Pro module)

This edition adds a project-scoped standards register and control-tracking module. The curated catalogue currently contains **67 selected standards/framework references, 32 control domains and 469 paraphrased checklist controls**. Its scope includes web/API application security; test methodology; identity, sessions and protocols; secure SDLC; risk and incident management; supply-chain security; cloud/container; privacy and conditional sector laws; AI/LLM; and accessibility. Every registry row records an edition/status, applicability relationship, official source URL and a limitation note.

- Human-readable checklist: [`standards/STANDARDS_CHECKLIST.md`](standards/STANDARDS_CHECKLIST.md)
- Editable offline Excel tracker: [`standards/FIREWATCH_Standards_Checklist_v9_Pro.xlsx`](standards/FIREWATCH_Standards_Checklist_v9_Pro.xlsx)
- Machine-readable register: [`standards/standards_registry.json`](standards/standards_registry.json)
- Canonical 469-control catalogue: [`standards/standards_checklist.json`](standards/standards_checklist.json)
- API guide: [`docs/STANDARDS_API.md`](docs/STANDARDS_API.md)
- Governance and evidence process: [`docs/STANDARDS_GOVERNANCE_V9_PRO.md`](docs/STANDARDS_GOVERNANCE_V9_PRO.md)

The dashboard has a **Standards & Assurance Checklist** panel to filter controls by framework, domain, priority, applicability, status, verification mode and relationship type (direct/supporting/conditional/adjacent); view acceptance criteria and source mappings; record owner/due date/evidence/reviewer/exception; inspect audit history; and export CSV/Excel. API endpoints include `GET /api/v1/standards/registry`, `GET /api/v1/standards/summary`, `GET /api/v1/standards/checklist`, `PATCH /api/v1/standards/checklist/{control_id}`, `GET /api/v1/standards/checklist/{control_id}/history`, `GET /api/v1/standards/checklist/export.csv`, and `GET /api/v1/standards/workbook`. The workbook is an offline snapshot and does not automatically synchronize with the database-backed dashboard; use the API/UI for the live project state.

**Conformance limitation:** this is a curated subject/family crosswalk and original, paraphrased control list—not a verbatim reproduction of licensed standards or a certification. Verify exact clauses against official editions. “No finding” does not imply “compliant”; manual, identity/role-dependent, legal, cloud, mobile, AI and sector-specific controls require their indicated evidence and specialist review.

## Architecture

```text
Dashboard / REST API
        │
        ├── API-key gate + authorization acknowledgement
        ├── Strict target/scope policy
        ├── Encrypted auth configuration
        └── Database-backed job queue
                    │
                    ▼
             Scan Orchestrator
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
  HTTP Crawler   API Discovery  Playwright
       │            │            │
       └────────────┼────────────┘
                    ▼
    Passive + bounded read-only checks
                    ▼
    Evidence redaction + finding correlation
                    ▼
      Coverage, risk ranking, scan diff
                    ▼
     HTML / JSON / CSV / Markdown / SARIF
```

## Repository map

```text
backend/app/
  main.py              FastAPI API, readiness, evidence/coverage/report routes
  orchestrator.py      Assessment pipeline, cancellation checkpoints, persistence
  scope.py             Host/port/path policy and URL validation
  http_client.py       Read-only HTTP policy, body limits, pacing and credential isolation
  safe_network.py      Per-connection DNS resolution and IP pinning for default HTTP traffic
  crawler.py           Sitemap + page/endpoint discovery
  browser.py           Same-scope Playwright browser observation
  api_discovery.py     OpenAPI/Swagger + GraphQL discovery
  authz.py             Read-only role comparison review candidates
  checks/              Deterministic security rule modules
  report.py            HTML and JSON report rendering
  report_extras.py     CSV, Markdown, SARIF exports
  secret_store.py      Credential encryption at rest
  redaction.py         Secret-like URL/field/evidence redaction
  worker.py            Inline/external worker leases, heartbeats and stale-job handling
  tests/               v4–v11 regression, fuzz-matrix, API and local end-to-end tests (count in generated manifest)
frontend/              Self-hosted dashboard (no frontend build step)
demo_target/           Deliberately vulnerable local lab application
examples/demo_scan/    Demonstration reports generated from the local lab
docs/                  API, operations, testing, coverage and extension guides
.github/               CI, CodeQL, Dependabot and issue templates
```

## Quick start: local Python

Python 3.11 or newer is recommended. Run commands from the repository root.

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r backend/requirements.txt
# Optional: enable real browser discovery
python -m playwright install chromium
export PYTHONPATH=backend
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

### Windows PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r backend/requirements.txt
# Optional: enable real browser discovery
python -m playwright install chromium
$env:PYTHONPATH = "backend"
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open <http://127.0.0.1:8000/>. API documentation is at <http://127.0.0.1:8000/docs>; health and readiness checks are `/health` and `/ready`.

By default, the dashboard/API binds to loopback in the documented local commands. In development mode, the API key is optional; **do not expose a development-mode instance to an untrusted network**.

## Recommended first run: local demo target

Use the deliberately vulnerable target included with this project, not an arbitrary internet host.

Terminal A — start the lab application:

```bash
PYTHONPATH=. python -m uvicorn demo_target.main:app --host 127.0.0.1 --port 8765
```

Terminal B — allow loopback targets only for this isolated lab run:

```bash
# Linux / macOS
PYTHONPATH=backend ALLOW_PRIVATE_TARGETS=true python -m app.cli http://127.0.0.1:8765/ --pages 50 --depth 4 --endpoints 300 --delay 0 --no-browser
```

```powershell
# Windows PowerShell
$env:PYTHONPATH = "backend"
$env:ALLOW_PRIVATE_TARGETS = "true"
python -m app.cli http://127.0.0.1:8765/ --pages 50 --depth 4 --endpoints 300 --delay 0 --no-browser
```

The command prints the HTML/JSON report paths. Reports are written beneath `reports/<scan-id>/` by default; generated reports and databases are ignored by `.gitignore`.

> Keep `ALLOW_PRIVATE_TARGETS=false` for normal use. Do not set it on a publicly reachable deployment: it removes the private/loopback IP guard and can expose internal services to scanning.

## Docker Compose

```bash
cp .env.example .env
# Set POSTGRES_PASSWORD to a strong random value; set FIREWATCH_API_KEY for API access.
# Example key generation: python -c "import secrets; print(secrets.token_urlsafe(32))"
docker compose up --build
```

Dashboard: <http://127.0.0.1:8000/>. The database port is not published to the host and the web port binds to loopback by default. Compose requires a non-empty `POSTGRES_PASSWORD`; there is no baked-in database password fallback. Keep `.env` local and never commit it.

### Inline worker vs external worker

For a local/single-process install, keep `ENABLE_INLINE_WORKER=true` (the default). For an API deployment with a separate worker process:

1. Set `ENABLE_INLINE_WORKER=false` in `.env`.
2. Run `docker compose --profile external-worker up --build`.
3. Scale the worker only after confirming PostgreSQL is used and that queue claims are behaving as expected.

Do not run multiple Uvicorn processes with the inline worker enabled. The in-process queue is intended for local/single-process use; use the external worker topology for multi-process deployment.

## Authentication and secret handling

Use dedicated, least-privileged test identities. Example API request:

```http
POST /api/v1/scans
Content-Type: application/json
X-API-Key: <configured-api-key>

{
  "target_url": "https://your-authorized-domain.example/",
  "scope_acknowledged": true,
  "profile": "standard",
  "request_headers": {"Authorization": "Bearer <test-token>"},
  "authorization_profiles": [
    {"name": "admin", "headers": {"Authorization": "Bearer <admin-test-token>"}},
    {"name": "user", "headers": {"Authorization": "Bearer <least-privilege-test-token>"}}
  ]
}
```

The credentials are encrypted at rest using Fernet and are never returned by scan-detail responses. **Configured credentials are sent only to the exact origin (scheme, hostname and effective port) in the root target URL; they are not forwarded to additional in-scope hosts or ports.** For public targets they are sent only over HTTPS on the root scheme. To assess another host with authentication, create a separate scan rooted at that host. Public HTTP targets are not sent configured auth material.

URLs with query parameters commonly used for secrets (`token`, `session`, `access_token`, and similar) are refused by automatic discovery. Test reset links or signed URLs separately under a specific plan rather than letting them circulate through a crawler.

## Assessment profiles

| Profile | Defaults | Suggested use |
|---|---|---|
| `baseline` | Passive/low-impact inventory, lower page/depth ceiling, no browser or active probes | Initial production-safe review |
| `standard` | Bounded crawling, browser discovery, API discovery, safe GET canaries, optional read-only GraphQL introspection | Routine authorized assessment |
| `comprehensive` | Higher bounded page/endpoint ceilings; concurrency remains capped | Pre-release or larger authorized application |

A profile is a preset, not a promise of complete OWASP verification. Review the submitted `ScanCreate` fields and server-side ceilings before each engagement.

## Key API routes

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/health`, `/ready` | Liveness and database readiness |
| `GET` | `/api/v1/coverage` | Rule-family catalogue |
| `GET` | `/api/v1/assessment-plan` | Full 79-case assessment plan with execution-mode boundaries |
| `POST` | `/api/v1/scans` | Validate scope and queue an assessment |
| `GET` | `/api/v1/scans?limit=50&offset=0` | Paginated scan list |
| `GET` | `/api/v1/scans/{id}` | Scan summary and counts |
| `GET` | `/api/v1/scans/{id}/findings` | Filterable/paginated findings |
| `GET` | `/api/v1/scans/{id}/assets` | Paginated discovered assets |
| `GET` | `/api/v1/scans/{id}/events` | Scan lifecycle and progress events |
| `GET` | `/api/v1/scans/{id}/evidence` | Redacted evidence records |
| `GET` | `/api/v1/scans/{id}/coverage` | Coverage matrix for one scan |
| `GET` | `/api/v1/scans/{id}/diff` | Compare with the previous completed scan |
| `GET` | `/api/v1/scans/{id}/report?format=html` | Download one report format |
| `GET` | `/api/v1/scans/{id}/bundle` | Download all generated reports as ZIP |
| `POST` | `/api/v1/scans/{id}/cancel` | Request cooperative cancellation |

Set `FIREWATCH_API_KEY` to require the `X-API-Key` header. Production mode returns an error rather than enabling assessment APIs without a configured key.

## Bundle integrity and dependency inventory

The report bundle endpoint includes `manifest.json`; independently verify each `sha256` against the file at the matching relative path and compare `size_bytes`. This detects accidental corruption but is not a signature:

```bash
python scripts/verify_report_bundle.py path/to/firewatch-scan.zip
```

`docs/DEPENDENCY_INVENTORY_V9.json` describes declared requirements and version constraints. It is an inventory, not a resolved SBOM and not a vulnerability audit. Run `pip-audit` in an environment with package-index access before deployment. `RELEASE_CHECKLIST.md` records the final pre-release steps.

## Testing and development

The v9 Sentinel suite contains **5,948 pytest cases across 62 modules**. The full local regression suite passed; Python statement coverage was **84.53%** in one full-suite run, exceeding the 80% minimum gate. See `docs/TEST_MATRIX_V9.md`, `docs/TEST_MANIFEST_V9.json` and `VERIFICATION.md`. These are software regression tests, not a percentage of vulnerabilities detected.

```bash
python -m pip install -r backend/requirements-dev.txt
python scripts/build_test_manifest.py
python scripts/run_coverage_shards.py --shards 8 --min-coverage 80
```

From the repository root:

```bash
python -m compileall -q backend/app
node --check frontend/static/app.js
python scripts/repo_hygiene.py
bash -n scripts/publish_to_github.sh
```

The local integration test starts the local demo target and exercises a complete CLI scan/report pipeline. Browser discovery requires Playwright's Chromium browser; install it with `python -m playwright install chromium` if your Python environment does not use the supplied Playwright Docker base image.

## Assessment coverage: what “all tests” means

The assessment catalog tracks 79 test cases. It is deliberately honest about execution mode: **22** passive automated observations, **13** automated review candidates that require validation, **38** manual/test-account/workflow cases, and **6** specialist-tool-required checks. These are coverage-plan entries, not 79 guaranteed automated exploit tests. See [the generated plan](docs/ASSESSMENT_CATALOG.md), the machine-readable [JSON catalog](docs/assessment-plan-v9.json), [CSV catalog](docs/assessment-plan-v9.csv), [v9 test matrix](docs/TEST_MATRIX_V9.md), and [test manifest](docs/TEST_MANIFEST_V9.json).

## Production configuration gate

At startup FIREWATCH Sentinel validates configured resource ceilings, CORS origins, user-agent syntax, optional ZAP origin, and an explicit Fernet key. Production additionally requires an API key of at least 32 printable ASCII characters, a non-SQLite database, `ALLOW_PRIVATE_TARGETS=false`, and `ENABLE_INLINE_WORKER=false`. Configure a separate worker process and a persistent secret-key mount before a production deployment. See `docs/PRODUCTION_READINESS.md` and `docs/THREAT_MODEL.md`.

## Security boundaries and limitations

FIREWATCH does **not** automate password guessing, credential stuffing, account lockout testing, arbitrary write/delete requests, destructive business flows, executable XSS payloads, SQL injection exploit payloads, shell injection, or weaponized SSRF. It does not claim to fully automate every OWASP Top 10, WSTG, ASVS, or API Security control.

IDOR/BOLA, authorization policy, business logic, and exploitable injection issues usually require test fixtures, a precise authorization matrix, application-specific workflows, and human validation. The current authorization and reflection checks are review candidates. The optional ZAP adapter safely creates a passive Automation Framework plan and checks reachability; it does not claim to run a full ZAP scan automatically. Automated rules provide evidence for triage, not proof of exploitability or absence. The current API key is shared and the standards `project_key` is not tenant-level authorization. Do not use this build to host mutually untrusted customers until per-tenant identity and resource-level authorization are implemented and independently tested. The default HTTP transport now pins each TCP connection to a per-connection validated IP address; Playwright still uses a separate resolver, so enforce an egress firewall/proxy for the browser and optional tools to mitigate DNS-rebinding risks. Database migrations, tenant-level authorization, production KMS/rotation, resolved SBOM, signed provenance, full ZAP execution, and independent penetration testing remain industrial-release gates. Worker heartbeat leases now detect and fail stale RUNNING scans, but automatic retries and exactly-once artifact publication are not implemented.

The default HTTP transport resolves and pins each TCP connection to validated IP literals and rejects mixed public/private DNS answers when private targets are disabled. Playwright and optional external tools do not share that HTTP transport, so enforce outbound firewall/proxy allow-lists and do not rely on application checks as the only network isolation boundary.

Read [SECURITY.md](SECURITY.md), [docs/OPERATIONS.md](docs/OPERATIONS.md), [docs/SECURITY_COVERAGE.md](docs/SECURITY_COVERAGE.md), and [docs/GITHUB_PUBLISHING.md](docs/GITHUB_PUBLISHING.md) before deployment or public release.

## Publish to your GitHub account

The repository ships with an interactive publishing helper that runs pre-publish checks, displays the staged files, requires explicit confirmation, offers public/private repository creation, and never force-pushes. See [the publishing guide](docs/GITHUB_PUBLISHING.md).

```bash
# Linux / macOS / Git Bash
python -m pip install -r backend/requirements-dev.txt
bash scripts/publish_to_github.sh
```

```powershell
# Windows PowerShell
py -m pip install -r backend/requirements-dev.txt
.\scripts\publish_to_github.ps1
```

The publisher requires Git, Python, Node.js, the GitHub CLI (`gh`), and an authenticated GitHub CLI session. Review the staged file list carefully; never publish real target reports, credentials, or customer data.

## Maintainer

**Hamid Yarali** · [GitHub profile](https://github.com/HamidYaraliOfficial)

Issues and pull requests are welcome. Please do not publish sensitive target information, tokens, logs, or vulnerability details from third-party systems in public issues.
