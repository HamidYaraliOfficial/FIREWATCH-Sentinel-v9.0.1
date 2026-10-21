# FIREWATCH v9.0.1 Security Coverage and Boundaries

FIREWATCH maps rule families conceptually to OWASP Top 10:2025, OWASP WSTG stable and OWASP API Security Top 10:2023. The mapping is not certification, a compliance attestation, or full conformance.

## Automated observations

- HTTP headers, redirects, TLS/certificate posture, mixed content, CSP/HSTS hints, cache controls, server/runtime disclosure, third-party script integrity signals, common exposed diagnostics, and client-visible secret patterns.
- Cookie attribute observations and form/password transport indicators.
- CORS GET/OPTIONS observations and GraphQL/OpenAPI discovery.
- Basic API spec checks including declared security schemes and suspicious URL-like parameter metadata.
- Safe GET query reflection canaries (reflection is not proof of XSS).
- Read-only role-profile response comparisons for sensitive-looking endpoints (success is not proof of BOLA/IDOR).

## Not automatically proven

- Business-logic defects, race conditions, authorization policy correctness, IDOR/BOLA impact, account takeover, mass assignment exploitability, SQL/NoSQL injection, stored/reflected/DOM XSS exploitability, SSRF reachability, file-upload compromise, deserialization, and complex OAuth/OIDC flaws.
- Absence of vulnerabilities when no finding is recorded.
- Complete coverage of every OWASP WSTG test case, ASVS requirement, Top 10 category or API Security risk.

## Reporting language

Each finding should be read with its evidence, confidence and remediation. Review candidates are hypotheses intended for manual confirmation. A scanner response, HTTP 200, an exposed schema, or reflected text alone is not universal proof of exploitability or impact.

## Extending the catalog

Every new rule should define its ID/category, safe request preconditions, bounded request count, precise evidence fields, false-positive considerations, severity rationale, confidence, remediation and authoritative references. Prefer signatures/hashes and short redacted observations over raw body retention.
