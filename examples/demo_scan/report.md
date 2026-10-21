# FIREWATCH Security Assessment Report

- **Target:** `http://127.0.0.1:8789/`
- **Scan ID:** `7ed5df79-747c-4068-9ef8-58f94a702f64`
- **Status:** `completed`
- **Generated (UTC):** `2026-10-14T09:47:06.888203+00:00`

## Summary

Critical: 0 | High: 1 | Medium: 15 | Low: 15 | Info: 10

## Findings

### [HIGH] Password form submits over HTTP

- **Rule:** `FW-FORM-001`
- **Confidence:** 100%
- **Risk score:** 7.96
- **Endpoint:** `http://127.0.0.1:8789/`
- **Status:** `open`

A password\-bearing form submits to cleartext HTTP.

**Impact:** Credentials may be exposed to interception.

**Evidence:** Password input with HTTP action.

**Remediation:** Use HTTPS\-only authentication endpoints and redirect/block cleartext access.

**References:** OWASP WSTG v4.2

### [MEDIUM] CSP header missing

- **Rule:** `FW-WEB-001`
- **Confidence:** 97%
- **Risk score:** 4.85
- **Endpoint:** `http://127.0.0.1:8789/`
- **Status:** `open`

The response does not advertise content\-security\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** content\-security\-policy was absent.

**Remediation:** Deploy a restrictive Content\-Security\-Policy.

**References:** OWASP WSTG v4.2

### [MEDIUM] CSP header missing

- **Rule:** `FW-WEB-001`
- **Confidence:** 97%
- **Risk score:** 4.85
- **Endpoint:** `http://127.0.0.1:8789/set-cookie`
- **Status:** `open`

The response does not advertise content\-security\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** content\-security\-policy was absent.

**Remediation:** Deploy a restrictive Content\-Security\-Policy.

**References:** OWASP WSTG v4.2

### [MEDIUM] CSP header missing

- **Rule:** `FW-WEB-001`
- **Confidence:** 97%
- **Risk score:** 4.85
- **Endpoint:** `http://127.0.0.1:8789/admin/panel`
- **Status:** `open`

The response does not advertise content\-security\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** content\-security\-policy was absent.

**Remediation:** Deploy a restrictive Content\-Security\-Policy.

**References:** OWASP WSTG v4.2

### [MEDIUM] CSP header missing

- **Rule:** `FW-WEB-001`
- **Confidence:** 97%
- **Risk score:** 4.85
- **Endpoint:** `http://127.0.0.1:8789/api/users/1`
- **Status:** `open`

The response does not advertise content\-security\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** content\-security\-policy was absent.

**Remediation:** Deploy a restrictive Content\-Security\-Policy.

**References:** OWASP WSTG v4.2

### [MEDIUM] CSP header missing

- **Rule:** `FW-WEB-001`
- **Confidence:** 97%
- **Risk score:** 4.85
- **Endpoint:** `http://127.0.0.1:8789/login`
- **Status:** `open`

The response does not advertise content\-security\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** content\-security\-policy was absent.

**Remediation:** Deploy a restrictive Content\-Security\-Policy.

**References:** OWASP WSTG v4.2

### [MEDIUM] Clickjacking protection not detected

- **Rule:** `FW-WEB-005`
- **Confidence:** 95%
- **Risk score:** 4.75
- **Endpoint:** `http://127.0.0.1:8789/`
- **Status:** `open`

Neither X\-Frame\-Options nor CSP frame\-ancestors was observed.

**Impact:** Sensitive UI may be embeddable by another origin.

**Evidence:** No frame restriction detected.

**Remediation:** Set CSP frame\-ancestors and/or X\-Frame\-Options as appropriate.

**References:** OWASP WSTG v4.2

### [MEDIUM] Clickjacking protection not detected

- **Rule:** `FW-WEB-005`
- **Confidence:** 95%
- **Risk score:** 4.75
- **Endpoint:** `http://127.0.0.1:8789/set-cookie`
- **Status:** `open`

Neither X\-Frame\-Options nor CSP frame\-ancestors was observed.

**Impact:** Sensitive UI may be embeddable by another origin.

**Evidence:** No frame restriction detected.

**Remediation:** Set CSP frame\-ancestors and/or X\-Frame\-Options as appropriate.

**References:** OWASP WSTG v4.2

### [MEDIUM] Session\-like cookie missing HttpOnly

- **Rule:** `FW-COOKIE-002`
- **Confidence:** 95%
- **Risk score:** 4.75
- **Endpoint:** `http://127.0.0.1:8789/set-cookie`
- **Status:** `open`

Cookie \`session\_id\` appears session/auth related but lacks HttpOnly.

**Impact:** Client\-side script access can increase credential exposure in case of XSS.

**Evidence:** session\_id: \[REDACTED\]

**Remediation:** Add HttpOnly when JavaScript access is not required.

**References:** 

### [MEDIUM] Clickjacking protection not detected

- **Rule:** `FW-WEB-005`
- **Confidence:** 95%
- **Risk score:** 4.75
- **Endpoint:** `http://127.0.0.1:8789/admin/panel`
- **Status:** `open`

Neither X\-Frame\-Options nor CSP frame\-ancestors was observed.

**Impact:** Sensitive UI may be embeddable by another origin.

**Evidence:** No frame restriction detected.

**Remediation:** Set CSP frame\-ancestors and/or X\-Frame\-Options as appropriate.

**References:** OWASP WSTG v4.2

### [MEDIUM] Clickjacking protection not detected

- **Rule:** `FW-WEB-005`
- **Confidence:** 95%
- **Risk score:** 4.75
- **Endpoint:** `http://127.0.0.1:8789/api/users/1`
- **Status:** `open`

Neither X\-Frame\-Options nor CSP frame\-ancestors was observed.

**Impact:** Sensitive UI may be embeddable by another origin.

**Evidence:** No frame restriction detected.

**Remediation:** Set CSP frame\-ancestors and/or X\-Frame\-Options as appropriate.

**References:** OWASP WSTG v4.2

### [MEDIUM] Clickjacking protection not detected

- **Rule:** `FW-WEB-005`
- **Confidence:** 95%
- **Risk score:** 4.75
- **Endpoint:** `http://127.0.0.1:8789/login`
- **Status:** `open`

Neither X\-Frame\-Options nor CSP frame\-ancestors was observed.

**Impact:** Sensitive UI may be embeddable by another origin.

**Evidence:** No frame restriction detected.

**Remediation:** Set CSP frame\-ancestors and/or X\-Frame\-Options as appropriate.

**References:** OWASP WSTG v4.2

### [MEDIUM] Preflight reflects untrusted origin with credentials enabled

- **Rule:** `FW-CORS-005`
- **Confidence:** 92%
- **Risk score:** 4.6
- **Endpoint:** `http://127.0.0.1:8789/`
- **Status:** `open`

An OPTIONS preflight response reflected the synthetic untrusted Origin and enabled credentials.

**Impact:** If sensitive endpoints share this policy, untrusted browser origins may be able to read responses in a credentialed context.

**Evidence:** Preflight Origin was reflected while Access\-Control\-Allow\-Credentials was true.

**Remediation:** Return only explicitly allow\-listed origins; review credential policy and allowed methods/headers.

**References:** 

### [MEDIUM] CORS origin reflection detected

- **Rule:** `FW-CORS-004`
- **Confidence:** 90%
- **Risk score:** 4.5
- **Endpoint:** `http://127.0.0.1:8789/`
- **Status:** `open`

The response reflected an arbitrary test Origin value in Access\-Control\-Allow\-Origin.

**Impact:** Origin reflection can enable unintended cross\-origin access when combined with sensitive resources or credentials.

**Evidence:** Injected test Origin was reflected.

**Remediation:** Use a strict allow\-list and validate origins server\-side rather than reflecting arbitrary Origin values.

**References:** 

### [MEDIUM] Sensitive\-looking page lacks Cache\-Control evidence

- **Rule:** `FW-WEB-008`
- **Confidence:** 72%
- **Risk score:** 3.6
- **Endpoint:** `http://127.0.0.1:8789/admin/panel`
- **Status:** `open`

A sensitive\-looking URL does not expose a restrictive Cache\-Control policy.

**Impact:** Shared/private caching could retain sensitive material depending on framework/proxy behavior.

**Evidence:** No Cache\-Control header on sensitive\-looking path.

**Remediation:** Review caching policy and explicitly control storage for authenticated/sensitive responses.

**References:** OWASP WSTG v4.2

### [MEDIUM] Sensitive\-looking page lacks Cache\-Control evidence

- **Rule:** `FW-WEB-008`
- **Confidence:** 72%
- **Risk score:** 3.6
- **Endpoint:** `http://127.0.0.1:8789/login`
- **Status:** `open`

A sensitive\-looking URL does not expose a restrictive Cache\-Control policy.

**Impact:** Shared/private caching could retain sensitive material depending on framework/proxy behavior.

**Evidence:** No Cache\-Control header on sensitive\-looking path.

**Remediation:** Review caching policy and explicitly control storage for authenticated/sensitive responses.

**References:** OWASP WSTG v4.2

### [LOW] X\-Content\-Type\-Options missing

- **Rule:** `FW-WEB-002`
- **Confidence:** 98%
- **Risk score:** 2.45
- **Endpoint:** `http://127.0.0.1:8789/`
- **Status:** `open`

The response does not advertise x\-content\-type\-options.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** x\-content\-type\-options was absent.

**Remediation:** Set X\-Content\-Type\-Options: nosniff.

**References:** OWASP WSTG v4.2

### [LOW] X\-Content\-Type\-Options missing

- **Rule:** `FW-WEB-002`
- **Confidence:** 98%
- **Risk score:** 2.45
- **Endpoint:** `http://127.0.0.1:8789/set-cookie`
- **Status:** `open`

The response does not advertise x\-content\-type\-options.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** x\-content\-type\-options was absent.

**Remediation:** Set X\-Content\-Type\-Options: nosniff.

**References:** OWASP WSTG v4.2

### [LOW] X\-Content\-Type\-Options missing

- **Rule:** `FW-WEB-002`
- **Confidence:** 98%
- **Risk score:** 2.45
- **Endpoint:** `http://127.0.0.1:8789/admin/panel`
- **Status:** `open`

The response does not advertise x\-content\-type\-options.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** x\-content\-type\-options was absent.

**Remediation:** Set X\-Content\-Type\-Options: nosniff.

**References:** OWASP WSTG v4.2

### [LOW] X\-Content\-Type\-Options missing

- **Rule:** `FW-WEB-002`
- **Confidence:** 98%
- **Risk score:** 2.45
- **Endpoint:** `http://127.0.0.1:8789/api/users/1`
- **Status:** `open`

The response does not advertise x\-content\-type\-options.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** x\-content\-type\-options was absent.

**Remediation:** Set X\-Content\-Type\-Options: nosniff.

**References:** OWASP WSTG v4.2

### [LOW] X\-Content\-Type\-Options missing

- **Rule:** `FW-WEB-002`
- **Confidence:** 98%
- **Risk score:** 2.45
- **Endpoint:** `http://127.0.0.1:8789/login`
- **Status:** `open`

The response does not advertise x\-content\-type\-options.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** x\-content\-type\-options was absent.

**Remediation:** Set X\-Content\-Type\-Options: nosniff.

**References:** OWASP WSTG v4.2

### [LOW] Referrer\-Policy missing

- **Rule:** `FW-WEB-003`
- **Confidence:** 96%
- **Risk score:** 2.4
- **Endpoint:** `http://127.0.0.1:8789/`
- **Status:** `open`

The response does not advertise referrer\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** referrer\-policy was absent.

**Remediation:** Set an explicit Referrer\-Policy.

**References:** OWASP WSTG v4.2

### [LOW] Referrer\-Policy missing

- **Rule:** `FW-WEB-003`
- **Confidence:** 96%
- **Risk score:** 2.4
- **Endpoint:** `http://127.0.0.1:8789/set-cookie`
- **Status:** `open`

The response does not advertise referrer\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** referrer\-policy was absent.

**Remediation:** Set an explicit Referrer\-Policy.

**References:** OWASP WSTG v4.2

### [LOW] Referrer\-Policy missing

- **Rule:** `FW-WEB-003`
- **Confidence:** 96%
- **Risk score:** 2.4
- **Endpoint:** `http://127.0.0.1:8789/admin/panel`
- **Status:** `open`

The response does not advertise referrer\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** referrer\-policy was absent.

**Remediation:** Set an explicit Referrer\-Policy.

**References:** OWASP WSTG v4.2

### [LOW] Referrer\-Policy missing

- **Rule:** `FW-WEB-003`
- **Confidence:** 96%
- **Risk score:** 2.4
- **Endpoint:** `http://127.0.0.1:8789/api/users/1`
- **Status:** `open`

The response does not advertise referrer\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** referrer\-policy was absent.

**Remediation:** Set an explicit Referrer\-Policy.

**References:** OWASP WSTG v4.2

### [LOW] Referrer\-Policy missing

- **Rule:** `FW-WEB-003`
- **Confidence:** 96%
- **Risk score:** 2.4
- **Endpoint:** `http://127.0.0.1:8789/login`
- **Status:** `open`

The response does not advertise referrer\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** referrer\-policy was absent.

**Remediation:** Set an explicit Referrer\-Policy.

**References:** OWASP WSTG v4.2

### [LOW] Permissions\-Policy missing

- **Rule:** `FW-WEB-004`
- **Confidence:** 93%
- **Risk score:** 2.33
- **Endpoint:** `http://127.0.0.1:8789/`
- **Status:** `open`

The response does not advertise permissions\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** permissions\-policy was absent.

**Remediation:** Define an explicit Permissions\-Policy for used browser capabilities.

**References:** OWASP WSTG v4.2

### [LOW] Permissions\-Policy missing

- **Rule:** `FW-WEB-004`
- **Confidence:** 93%
- **Risk score:** 2.33
- **Endpoint:** `http://127.0.0.1:8789/set-cookie`
- **Status:** `open`

The response does not advertise permissions\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** permissions\-policy was absent.

**Remediation:** Define an explicit Permissions\-Policy for used browser capabilities.

**References:** OWASP WSTG v4.2

### [LOW] Permissions\-Policy missing

- **Rule:** `FW-WEB-004`
- **Confidence:** 93%
- **Risk score:** 2.33
- **Endpoint:** `http://127.0.0.1:8789/admin/panel`
- **Status:** `open`

The response does not advertise permissions\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** permissions\-policy was absent.

**Remediation:** Define an explicit Permissions\-Policy for used browser capabilities.

**References:** OWASP WSTG v4.2

### [LOW] Permissions\-Policy missing

- **Rule:** `FW-WEB-004`
- **Confidence:** 93%
- **Risk score:** 2.33
- **Endpoint:** `http://127.0.0.1:8789/api/users/1`
- **Status:** `open`

The response does not advertise permissions\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** permissions\-policy was absent.

**Remediation:** Define an explicit Permissions\-Policy for used browser capabilities.

**References:** OWASP WSTG v4.2

### [LOW] Permissions\-Policy missing

- **Rule:** `FW-WEB-004`
- **Confidence:** 93%
- **Risk score:** 2.33
- **Endpoint:** `http://127.0.0.1:8789/login`
- **Status:** `open`

The response does not advertise permissions\-policy.

**Impact:** Browser\-side defense\-in\-depth is weaker than necessary.

**Evidence:** permissions\-policy was absent.

**Remediation:** Define an explicit Permissions\-Policy for used browser capabilities.

**References:** OWASP WSTG v4.2

### [INFO] GraphQL endpoint discovered

- **Rule:** `FW-GQL-001`
- **Confidence:** 98%
- **Risk score:** 0.49
- **Endpoint:** `http://127.0.0.1:8789/graphql`
- **Status:** `open`

A GraphQL endpoint appears to be exposed.

**Impact:** GraphQL deserves dedicated authorization, query\-depth/complexity, and introspection review.

**Evidence:** GraphQL\-like URL discovered: http://127.0.0.1:8789/graphql

**Remediation:** Review resolver\-level authorization, query complexity limits, rate controls, and introspection policy.

**References:** 

### [INFO] Technology banner disclosure

- **Rule:** `FW-WEB-007`
- **Confidence:** 92%
- **Risk score:** 0.46
- **Endpoint:** `http://127.0.0.1:8789/`
- **Status:** `open`

Response headers reveal server/framework details.

**Impact:** Fingerprinting becomes easier.

**Evidence:** Disclosed: {'server': 'uvicorn'}

**Remediation:** Reduce unnecessary banner disclosure.

**References:** OWASP WSTG v4.2

### [INFO] Technology banner disclosure

- **Rule:** `FW-WEB-007`
- **Confidence:** 92%
- **Risk score:** 0.46
- **Endpoint:** `http://127.0.0.1:8789/set-cookie`
- **Status:** `open`

Response headers reveal server/framework details.

**Impact:** Fingerprinting becomes easier.

**Evidence:** Disclosed: {'server': 'uvicorn'}

**Remediation:** Reduce unnecessary banner disclosure.

**References:** OWASP WSTG v4.2

### [INFO] Technology banner disclosure

- **Rule:** `FW-WEB-007`
- **Confidence:** 92%
- **Risk score:** 0.46
- **Endpoint:** `http://127.0.0.1:8789/admin/panel`
- **Status:** `open`

Response headers reveal server/framework details.

**Impact:** Fingerprinting becomes easier.

**Evidence:** Disclosed: {'server': 'uvicorn'}

**Remediation:** Reduce unnecessary banner disclosure.

**References:** OWASP WSTG v4.2

### [INFO] Technology banner disclosure

- **Rule:** `FW-WEB-007`
- **Confidence:** 92%
- **Risk score:** 0.46
- **Endpoint:** `http://127.0.0.1:8789/api/users/1`
- **Status:** `open`

Response headers reveal server/framework details.

**Impact:** Fingerprinting becomes easier.

**Evidence:** Disclosed: {'server': 'uvicorn'}

**Remediation:** Reduce unnecessary banner disclosure.

**References:** OWASP WSTG v4.2

### [INFO] Technology banner disclosure

- **Rule:** `FW-WEB-007`
- **Confidence:** 92%
- **Risk score:** 0.46
- **Endpoint:** `http://127.0.0.1:8789/login`
- **Status:** `open`

Response headers reveal server/framework details.

**Impact:** Fingerprinting becomes easier.

**Evidence:** Disclosed: {'server': 'uvicorn'}

**Remediation:** Reduce unnecessary banner disclosure.

**References:** OWASP WSTG v4.2

### [INFO] Third\-party script without Subresource Integrity

- **Rule:** `FW-SUPPLY-001`
- **Confidence:** 80%
- **Risk score:** 0.4
- **Endpoint:** `http://127.0.0.1:8789/`
- **Status:** `open`

One or more third\-party scripts lack an integrity attribute in the observed markup.

**Impact:** If the third\-party source is compromised or changes unexpectedly, script content may change without an SRI check.

**Evidence:** 1 external script\(s\) without SRI observed.

**Remediation:** For stable third\-party assets, consider SRI plus crossorigin; use CSP and dependency governance as defense in depth.

**References:** OWASP WSTG stable

### [INFO] CSRF protection not obvious in state\-changing form

- **Rule:** `FW-FORM-002`
- **Confidence:** 62%
- **Risk score:** 0.31
- **Endpoint:** `http://127.0.0.1:8789/`
- **Status:** `open`

No commonly named CSRF token field was observed. This is a review candidate, not proof of a CSRF flaw.

**Impact:** State\-changing requests may require server\-side CSRF defenses.

**Evidence:** No common CSRF token field name detected.

**Remediation:** Verify framework/token/header\-based CSRF controls for state\-changing operations.

**References:** OWASP WSTG v4.2

### [INFO] Cross\-Origin\-Opener\-Policy not observed

- **Rule:** `FW-ISOLATION-001`
- **Confidence:** 58%
- **Risk score:** 0.29
- **Endpoint:** `http://127.0.0.1:8789/`
- **Status:** `open`

No Cross\-Origin\-Opener\-Policy response header was observed on HTML.

**Impact:** Cross\-origin window relationships may be less isolated than a highly isolated application expects.

**Evidence:** Cross\-Origin\-Opener\-Policy absent; applicability depends on app behavior.

**Remediation:** Review whether same\-origin or same\-origin\-allow\-popups isolation is appropriate for this application.

**References:** OWASP WSTG stable

### [INFO] Cross\-Origin\-Resource\-Policy not observed

- **Rule:** `FW-ISOLATION-002`
- **Confidence:** 55%
- **Risk score:** 0.28
- **Endpoint:** `http://127.0.0.1:8789/`
- **Status:** `open`

No Cross\-Origin\-Resource\-Policy response header was observed on HTML.

**Impact:** Cross\-origin resource embedding policy is implicit rather than explicitly declared.

**Evidence:** Cross\-Origin\-Resource\-Policy absent; no exploit inferred.

**Remediation:** Assess whether same\-origin, same\-site, or cross\-origin resource policy fits the product.

**References:** OWASP WSTG stable

## Test coverage events

| Phase | Progress | Details |
|---|---:|---|
| scope | 2.0% | Validating scope and scan policy |
| recon | 8.0% | Crawling target and building attack\-surface inventory |
| sitemap | 7.0% | Discovered 0 same\-scope sitemap URL candidates |
| recon | 28.0% | Discovered 5 web pages/resources |
| input\-probes | 34.0% | Checking a bounded set of GET query parameters with harmless alphanumeric canaries only |
| api | 40.0% | Discovering API specifications, GraphQL endpoints and OPTIONS/CORS posture |
| transport | 58.0% | Inspecting TLS and redirect posture |
| metadata | 66.0% | Checking standard metadata and operational security endpoints |
| finalize | 90.0% | Deduplicating findings and rendering reports |
