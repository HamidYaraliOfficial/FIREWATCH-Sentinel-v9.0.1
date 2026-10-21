# FIREWATCH v9 Architecture

## Design goals

- Only send requests to URLs allowed by an explicit host/port/path policy.
- Keep the default assessment non-destructive and bounded.
- Keep credential handling separate from endpoint discovery and report output.
- Persist reproducible evidence without storing response bodies or auth material unnecessarily.
- Make scan behavior and rule coverage inspectable and repeatable.

## Request flow

```text
REST API / Dashboard / CLI
        │
        ├── URL validation + target authorization acknowledgment
        ├── API-key gate (for API endpoints when configured)
        ├── Encrypted auth profile persistence
        └── Scan record / queue
                    │
                    ▼
             Scan Orchestrator
                    │
       ┌────────────┼──────────────┐
       ▼            ▼              ▼
  HTTP Crawler   API Discovery  Playwright
       │            │              │
       └────────────┼──────────────┘
                    ▼
    Passive checks + bounded read-only checks
                    ▼
      Redaction → dedupe → risk/confidence
                    ▼
     DB findings/events/assets/evidence
                    ▼
    HTML / JSON / CSV / Markdown / SARIF
```

## Trust boundaries

### Target policy

`ScopePolicy` defines allowed hostnames, ports and exclusions. URLs are checked before each HTTP request; automatic redirect following is disabled. Path exclusions are evaluated against a normalized, once-decoded representation to catch common dot-segment and encoded traversal cases. Query strings with credential-like field names are excluded from automatic requests.

DNS answers are checked for non-global addresses unless explicitly disabled for a lab. The connector does not pin resolved addresses to the final socket connection; deploy with outbound firewall/proxy controls to protect against DNS rebinding and internal-network reachability.

### Credential boundary

`SafeHTTPClient` captures response bytes with a configurable upper limit (`MAX_RESPONSE_BODY_BYTES`, default 2,000,000). If a server ignores `Accept-Encoding: identity` and returns compressed content, the client does not decompress or parse it; the scan timeline records incomplete body analysis. Reports remain under `REPORT_DIR/<scan-id>/`; download routes verify resolved path containment and apply size caps. `SafeHTTPClient` merges default headers with per-request headers case-insensitively and strips transport-controlled headers. Credential-like headers are sent only when the request hostname and scheme exactly match the target root; public targets additionally require HTTPS. Browser discovery avoids context-wide authentication headers and applies the same logic for each route, including redirects and subresources. Authentication for another host requires a separate scan rooted at that host.

### Persistence and reports

Configured request headers, cookies and authorization profiles are stored in an encrypted blob. Query-secret URLs and evidence fields are redacted before persistence; evidence is redacted again when returned via API. Reports are stored under `REPORT_DIR/<scan-id>` and should be treated as sensitive output.

### Job state

Scan states are `queued`, `running`, `completed`, `failed`, and `canceled`. The worker checks cancellation between bounded units of work. Reports are rendered before the terminal transition; report records and the completed state are committed together using a conditional update, so a cancellation that wins while reports are rendered is not overwritten. The inline worker is for a single API process; production multi-process deployment should use PostgreSQL and the external worker with `ENABLE_INLINE_WORKER=false`.

## Data model

- `Scan`: target, status, configuration-safe metadata and lifecycle timestamps.
- `Page`: fetched page inventory, status, content type, response header summary, links/resources and body hash.
- `Asset`: discovered route/resource/API/browser/tool inventory.
- `Finding`: rule ID, category, severity, confidence, risk score, endpoint, evidence summary and remediation.
- `Evidence`: structured and redacted observation records related to a finding.
- `ScanEvent`: stage/progress event timeline.
- `Report`: generated report format and internal path.

## Rule semantics

Rules produce `FindingCandidate` objects. Candidates are normalized/redacted and deduplicated before persistence. Rule catalog mapping is family-level. A rule firing is an observation; a review candidate requires human validation; absence of a finding is not proof of security.

## Extension points

- `backend/app/checks/`: deterministic rule functions.
- `backend/app/check_catalog.py`: rule family and OWASP mapping.
- `backend/app/api_discovery.py`: API specification/GraphQL detection.
- `backend/app/report_extras.py`: new report formats.
- `backend/app/zap.py`: optional external tool adapter. Current implementation writes a plan and checks reachability, not full ZAP orchestration.
