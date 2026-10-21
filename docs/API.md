# REST API Reference — FIREWATCH v9.0.1

The API is served by FastAPI. Interactive docs are available at `/docs` unless disabled by deployment policy. When `FIREWATCH_API_KEY` is set, assessment endpoints require `X-API-Key: <key>`.

## Create a scan

`POST /api/v1/scans` (201)

```json
{
  "target_url": "https://authorized.example/",
  "scope_acknowledged": true,
  "profile": "standard",
  "max_pages": 300,
  "max_depth": 8,
  "request_delay_ms": 200,
  "allowed_hosts": [],
  "exclusions": ["/logout", "/delete-account"],
  "request_headers": {"Authorization": "Bearer <test-token>"}
}
```

The `scope_acknowledged` field must be true by default. URLs with credential-like query values are rejected; pass authentication in the encrypted credential fields. Configured authentication material is sent only to the exact hostname and scheme of the root target; on public targets it is sent only over HTTPS. The agent does not forward configured credentials to extra allowed hosts.

## Endpoints

| Method | Path | Notes |
|---|---|---|
| GET | `/health` | Liveness metadata |
| GET | `/ready` | Checks database reachability |
| GET | `/api/v1/coverage` | Rule-family catalogue and mapping |
| POST | `/api/v1/scans` | Queue an assessment |
| GET | `/api/v1/scans?limit=50&offset=0` | Paginated scan list |
| GET | `/api/v1/scans/{id}` | Scan summary/config-safe view/counts |
| GET | `/api/v1/scans/{id}/findings?severity=high&status=open&limit=200&offset=0` | Filtered, paginated findings |
| GET | `/api/v1/scans/{id}/assets?kind=page&limit=500&offset=0` | Paginated assets |
| GET | `/api/v1/scans/{id}/events?limit=500&offset=0` | Scan event timeline |
| GET | `/api/v1/scans/{id}/evidence?finding_id={finding-id}` | Redacted evidence for findings in this scan |
| GET | `/api/v1/scans/{id}/coverage` | Per-scan rule-family coverage matrix |
| GET | `/api/v1/scans/{id}/diff` | Compare against prior completed scan with same root URL |
| GET | `/api/v1/scans/{id}/report?format=html` | `html`, `json`, `csv`, `markdown`, `sarif` |
| GET | `/api/v1/scans/{id}/bundle` | ZIP of all available reports |
| POST | `/api/v1/scans/{id}/cancel` | Cooperative cancellation request |

## Status model

`queued → running → completed|failed|canceled`. Cancellation is cooperative: an in-flight network request can finish before the next crawler/orchestrator checkpoint. Atomic finalization prevents a cancelled job from being overwritten as completed if cancellation won the state transition.

## Evidence and coverage semantics

Evidence is redacted before it is returned. Nonetheless, reports can disclose application structure and should be access-controlled. `finding_observed` means at least one rule in a catalog family produced a finding; `no_finding_recorded_or_not_applicable` is intentionally not equivalent to “secure.”

## Errors

- `400`: invalid scope, unsupported URL, sensitive query string, or missing scope acknowledgement.
- `401`: missing/incorrect API key when configured.
- `404`: unknown scan or report not ready.
- `409`: operation conflicts with scan state (for example diff before completion).
- `503`: production mode without API key or unavailable service dependency.


## Standards and Assurance API

See [`STANDARDS_API.md`](STANDARDS_API.md) for the request/response contract. The main routes are:

- `GET /api/v1/standards/registry`
- `GET /api/v1/standards/summary?project_key=default`
- `GET /api/v1/standards/checklist`
- `PATCH /api/v1/standards/checklist/{control_id}`
- `GET /api/v1/standards/checklist/{control_id}/history`
- `GET /api/v1/standards/checklist/export.csv`
- `GET /api/v1/standards/workbook`
- `GET /standards/STANDARDS_CHECKLIST.md`

The tracker uses optimistic concurrency through `expected_revision`, evidence/reviewer validation for assessed statuses, and a per-project status history. Project state is persisted in `standards_checklist_states` and `standards_checklist_audit`.
