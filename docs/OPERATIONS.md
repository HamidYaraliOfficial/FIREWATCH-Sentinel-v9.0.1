# Operations Guide — FIREWATCH v9.0.1

## Runtime profiles

### Local/single-process

Use SQLite for quick development or PostgreSQL for a more representative environment. Set `ENABLE_INLINE_WORKER=true`, bind to loopback, and keep `ALLOW_PRIVATE_TARGETS=false` except when running the deliberately vulnerable local demo target.

### API + external worker

For a multi-process deployment, set `ENABLE_INLINE_WORKER=false` on the API process and run `python -m app.worker` as a separate worker. Use PostgreSQL so multiple worker processes can rely on database row locking. The inline and external workers both use heartbeat leases; a lease timeout marks a stale scan `FAILED` with an audit event rather than silently replaying potentially non-idempotent work. Coordinate upgrades and do not run old worker versions against the upgraded schema concurrently.

## Key environment variables

| Variable | Purpose | Safe guidance |
|---|---|---|
| `ENVIRONMENT` | Runtime mode | `production` requires an API key |
| `FIREWATCH_API_KEY` | REST API gate | Long, random, secret value |
| `FIREWATCH_SECRET_KEY` | Fernet key | Keep stable and outside source control |
| `FIREWATCH_SECRET_KEY_FILE` | Key-file fallback | Persist and restrict file permissions |
| `DATABASE_URL` | SQLAlchemy connection | PostgreSQL for multi-process work |
| `ALLOW_PRIVATE_TARGETS` | Permit private/loopback IPs | `false` except isolated lab use |
| `ENABLE_INLINE_WORKER` | Run queue inside API lifespan | `false` with external worker or multiple API processes |
| `REQUEST_TIMEOUT_SECONDS` | HTTP timeout | Keep bounded |
| `REQUEST_DELAY_MS` | Start-to-start request interval | Choose a low rate for production |
| `MAX_CONCURRENCY` | HTTP concurrency ceiling | Keep conservative |
| `WORKER_HEARTBEAT_SECONDS` | Worker lease heartbeat interval | Default 10 seconds; must be under one third of lease timeout |
| `WORKER_LEASE_TIMEOUT_SECONDS` | Mark stale `RUNNING` jobs failed | Default 60 seconds; does not automatically replay scans |
| `REPORT_DIR` | Report output location | Restrict filesystem permissions |
| `CORS_ORIGINS` | Dashboard/API browser origins | Exact origins; avoid wildcards |

## Key rotation and backups

Authentication fields are encrypted in the database. If the Fernet key is lost, previously encrypted fields cannot be decrypted. Back up the key separately from the database and use an explicit decrypt/re-encrypt migration when rotating a key. Do not copy production keys into a `.env.example` or issue attachment.

## Outbound network controls

The default HTTP transport resolves and pins each TCP connection to validated IP literals; it rejects mixed public/private answers when private targets are disabled. Playwright uses its own resolver and does not inherit this pinning. Use network-level egress filtering and a dedicated scanning network for high-assurance engagements. Do not treat `ALLOW_PRIVATE_TARGETS` as an isolation control.

## Observability and retention

Use `/health` for liveness and `/ready` for the database dependency. Scan events are retrievable through `/api/v1/scans/{id}/events`. Store reports and database backups in access-controlled storage and define a retention policy appropriate to your engagement. Delete generated local reports manually according to that retention policy; the project ignores report outputs by default.

## Troubleshooting

- **Playwright missing:** install Chromium with `python -m playwright install chromium`, or run the supplied Playwright base image.
- **API gives 401:** provide the configured `X-API-Key` from the dashboard or request header.
- **API gives 503 in production:** configure `FIREWATCH_API_KEY` and confirm the database is reachable.
- **Target rejected:** confirm scheme is HTTP(S), hostname/port is in scope, query parameters do not contain token-like values, and private IP access is not being blocked.
- **No scan progress in external-worker mode:** confirm `ENABLE_INLINE_WORKER=false`, the external worker service is running, all processes share the same database and key configuration, and PostgreSQL is healthy.
- **Credentials not sent:** authentication is deliberately restricted to the exact root hostname and root scheme. Public HTTP will not receive configured credentials; start the scan at the HTTPS root or create a separate root scan for the other authorized host.
