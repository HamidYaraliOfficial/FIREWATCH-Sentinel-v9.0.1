# Security policy and safe operation

FIREWATCH is intended for authorized web application security assessment. Only assess domains, paths, APIs and accounts for which written authorization and clear scope exist.

## Reporting a vulnerability in FIREWATCH

Please do not publish exploit details, active credentials, private target names or scan output in public Issues. Contact the maintainer privately through the contact options shown on the [GitHub profile](https://github.com/HamidYaraliOfficial) and provide a minimal reproducible description. Allow time for triage before public disclosure.

## Built-in guardrails

- HTTP response bodies are streamed into a bounded capture buffer (`MAX_RESPONSE_BODY_BYTES`); unexpected non-identity content encodings are not decompressed or parsed. Check scan events for incomplete-content-analysis notices.
- Report downloads are restricted to the resolved report directory for the requested scan and capped in size; report bundle manifests are integrity checks, not signatures.

- HTTP(S)-only targets; no embedded URL credentials and no credential-like query parameters in the root target or automatic discovery requests.
- Exact hostname allow-list and port-aware scope; extra hosts must be explicitly listed.
- Private, loopback, link-local, reserved and other non-global IP addresses are blocked by default.
- Redirect following is disabled in the HTTP client; requested URLs are revalidated before each request.
- Path exclusions are evaluated against a normalized path decoded through a bounded number of layers and compared case-insensitively to reduce common path-boundary bypasses.
- Configured auth headers/cookies are scoped to the exact root origin (scheme, hostname and effective port); for public targets they are only sent over HTTPS. They are not forwarded to other allowed hosts.
- Browser routes use per-request credential handling rather than context-wide auth headers, block out-of-scope network requests, and do not submit forms or accept downloads.
- Depth/page/endpoint limits, bounded concurrency, conservative public request spacing, and browser throttling.
- robots.txt is respected by default but is crawl guidance rather than authorization.
- No credential guessing, brute force, destructive forms, arbitrary writes/deletes, executable XSS probes, SQLi exploit payloads, shell injection or weaponized SSRF.
- The only input probe is a harmless alphanumeric canary through bounded GET query parameters.
- Role comparison uses tester-supplied profiles and GET requests only; results are review candidates.
- Authentication headers/cookies/profile headers are encrypted at rest and redacted from API responses; evidence is redacted again when served from the API.
- Optional API-key gate; production mode refuses assessment API access unless `FIREWATCH_API_KEY` is configured.
- Docker's web port binds to loopback by default; PostgreSQL is not published to the host.

## Production checklist

1. Set `ENVIRONMENT=production` and a long random `FIREWATCH_API_KEY`.
2. Set and protect a stable `FIREWATCH_SECRET_KEY`, or securely persist `FIREWATCH_SECRET_KEY_FILE`; never commit either key.
3. Replace `POSTGRES_PASSWORD` and use a secret manager in deployments.
4. Bind the API to a private interface; place it behind TLS and an authenticated reverse proxy for remote access.
5. Keep `ALLOW_PRIVATE_TARGETS=false` unless a separately isolated lab explicitly needs private targets.
6. Use `ENABLE_INLINE_WORKER=false` when running the separate worker process or multiple API processes.
7. Restrict access to the database, report directory and backups; reports can include sensitive endpoint/security metadata.
8. Use dedicated, least-privileged test accounts and synthetic data.
9. Review target scope, exclusions, rate, maintenance window and authorization before each run.
10. Validate findings manually before treating them as confirmed vulnerabilities.
11. Review dependencies and GitHub Actions permissions as part of release maintenance.

## Known limitations

The platform does not implement complete multi-tenant access control, DNS address pinning to the final connection, all WSTG/ASVS tests, destructive business-flow tests, every API authorization permutation, authenticated browser login workflow automation, complete exploit confirmation, or full CI/CD policy enforcement. It is an assessment aid, not a substitute for professional penetration testing or code review.

DNS is resolved and checked during scope validation, but a target could theoretically change resolution between validation and the eventual network connection. Deploy in an egress-restricted environment and enforce an outbound firewall/proxy allow-list for sensitive engagements. The private-target option is a lab convenience, not a security boundary.
