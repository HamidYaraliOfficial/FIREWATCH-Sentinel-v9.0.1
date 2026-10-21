# Standards Checklist API — FIREWATCH Sentinel v9

All `/api/v1/standards/*` endpoints are protected by the same `X-API-Key` gate as the rest of the API whenever `FIREWATCH_API_KEY` is configured. Use HTTPS in deployed environments. The request label `updated_by` is audit metadata, not identity proof unless backed by a trusted identity provider/reverse proxy.

## Read endpoints

- `GET /api/v1/standards/registry`: curated standards/framework registry, official URLs, version/status, relationship and usage limitation.
- `GET /api/v1/standards/summary?project_key=default`: status counts, assessed progress, compliance arithmetic (excludes N/A from denominator), mapped reference/domain counts and interpretation notice.
- `GET /api/v1/standards/checklist?project_key=default&page=1&page_size=100`: filters include `framework_id`, `domain_id`, `priority`, `applicability`, `status`, `verification_mode`, `relationship` (`direct`, `supporting`, `conditional`, `adjacent`) and `search`; page size max is 250.
- `GET /api/v1/standards/checklist/{control_id}/history?project_key=default&limit=50`: state transition history.
- `GET /api/v1/standards/checklist/export.csv?project_key=default`: Excel-safe CSV (UTF-8 BOM; formula-leading cells neutralized).
- `GET /api/v1/standards/workbook`: download offline Excel tracker; requires API key if configured.
- `GET /standards/STANDARDS_CHECKLIST.md`: human-readable checklist.

## Update a control

`PATCH /api/v1/standards/checklist/{control_id}`

```json
{
  "project_key": "default",
  "status": "evidence_pending",
  "expected_revision": 0,
  "owner": "AppSec owner",
  "reviewer": "Independent reviewer",
  "due_date": "2026-12-01",
  "evidence_url": "https://evidence.example.test/ticket/APPSEC-123",
  "evidence_note": "Sanitized evidence, build hash, test date, result and reproduction steps.",
  "justification": null,
  "updated_by": "dashboard-editor-label"
}
```

The first saved state uses `expected_revision: 0`; on subsequent updates use the latest returned revision. A stale revision returns `409` to prevent lost updates. Statuses: `not_assessed`, `evidence_pending`, `blocked`, `compliant`, `partially_compliant`, `non_compliant`, `not_applicable`.

For `compliant`, `partially_compliant` and `non_compliant`, at least an evidence URL or a sufficiently detailed evidence note, an owner, and reviewer are required. `not_applicable` needs a documented rationale and reviewer. Evidence URLs with user-info or token/password/signature-like query strings are rejected. Treat notes as sensitive and do not place secrets or raw customer data in them.

## Semantics and limitations

The compliance percentage is a checklist-management metric, not a certification score. It excludes `not_applicable` from its denominator and should be interpreted with scope, applicability, and evidence quality. Framework mappings are subject/family crosswalks; they are not guaranteed clause-level equivalence. Confirm exact current editions and clauses against the official documents.
