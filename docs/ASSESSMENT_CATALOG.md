# FIREWATCH v9 Assessment Catalog

Version: `9.0.1` · Cases: **79**

This is a coverage plan, not a claim that each entry is automatically executed. Read the execution mode for every item.

## Standards baseline

- `owasp_top_10`: 2025
- `owasp_asvs`: 5.0.0
- `owasp_wstg_stable`: 4.2 (stable; WSTG 5.0 is under development)
- `owasp_api_security_top_10`: 2023

## Execution mode totals

- **Manual workflow or dedicated test account required:** 38
- **Automated passive/low-impact observation:** 22
- **Automated signal; validation required:** 13
- **Specialist tool or dedicated testing required:** 6

## Full assessment plan

| ID | Category | Test | Execution mode | Standard mapping |
|---|---|---|---|---|
| `WSTG-INFO-01` | Information Gathering | Search-engine / public metadata review | `manual_or_test-account_required` | WSTG-INFO |
| `WSTG-INFO-02` | Information Gathering | Fingerprint web server and technologies | `automated_passive` | WSTG-INFO |
| `WSTG-INFO-03` | Information Gathering | Review metadata and comments in HTML | `automated_passive` | WSTG-INFO |
| `WSTG-INFO-04` | Information Gathering | Enumerate application entry points | `automated_passive` | WSTG-INFO |
| `WSTG-INFO-05` | Information Gathering | Review web page content for information leakage | `automated_passive` | WSTG-INFO |
| `WSTG-INFO-06` | Information Gathering | Identify application frameworks | `automated_passive` | WSTG-INFO |
| `WSTG-INFO-07` | Information Gathering | Map execution paths and discovered routes | `automated_passive` | WSTG-INFO |
| `WSTG-CONF-01` | Configuration | Check security headers and browser policy | `automated_passive` | WSTG-CONF |
| `WSTG-CONF-02` | Configuration | Review exposed backup/configuration artifacts | `automated_review_candidate` | WSTG-CONF |
| `WSTG-CONF-03` | Configuration | Review HTTP methods and OPTIONS observations | `automated_passive` | WSTG-CONF |
| `WSTG-CONF-04` | Configuration | Review TLS/certificate posture | `automated_passive` | WSTG-CONF |
| `WSTG-CONF-05` | Configuration | Check subdomain takeover conditions | `manual_or_test-account_required` | WSTG-CONF |
| `WSTG-CONF-06` | Configuration | Review application/platform error handling | `automated_passive` | WSTG-CONF |
| `WSTG-CONF-07` | Configuration | Review HSTS, redirect and cleartext transport | `automated_passive` | WSTG-CONF |
| `WSTG-CONF-08` | Configuration | Review CSP directives and enforcement | `automated_passive` | WSTG-CONF |
| `WSTG-CONF-09` | Configuration | Review source-map and public asset indicators | `automated_review_candidate` | WSTG-CONF |
| `WSTG-CONF-10` | Configuration | Review cross-origin isolation policy | `automated_review_candidate` | WSTG-CONF |
| `WSTG-IDNT-01` | Identity | Role/tenant model and identity lifecycle | `manual_or_test-account_required` | WSTG-IDNT |
| `WSTG-IDNT-02` | Identity | Account enumeration on registration/recovery | `manual_or_test-account_required` | WSTG-IDNT |
| `WSTG-ATHN-01` | Authentication | Credentials transported only over HTTPS | `automated_passive` | WSTG-ATHN |
| `WSTG-ATHN-02` | Authentication | Default/weak credential assessment | `manual_or_test-account_required` | WSTG-ATHN |
| `WSTG-ATHN-03` | Authentication | Password policy and breached-password checks | `manual_or_test-account_required` | WSTG-ATHN |
| `WSTG-ATHN-04` | Authentication | Authentication bypass and alternate channels | `manual_or_test-account_required` | WSTG-ATHN |
| `WSTG-ATHN-05` | Authentication | MFA enforcement and recovery controls | `manual_or_test-account_required` | WSTG-ATHN |
| `WSTG-ATHN-06` | Authentication | Password reset and account recovery workflows | `manual_or_test-account_required` | WSTG-ATHN |
| `WSTG-ATHN-07` | Authentication | Rate limiting and lockout behavior | `manual_or_test-account_required` | WSTG-ATHN |
| `WSTG-ATHN-08` | Authentication | Authentication response differences | `manual_or_test-account_required` | WSTG-ATHN |
| `WSTG-ATHN-09` | Authentication | Logout and session invalidation | `manual_or_test-account_required` | WSTG-ATHN |
| `WSTG-ATHZ-01` | Authorization | Read-only comparison of supplied role profiles | `automated_review_candidate` | WSTG-ATHZ |
| `WSTG-ATHZ-02` | Authorization | Vertical privilege escalation / function authorization | `manual_or_test-account_required` | WSTG-ATHZ |
| `WSTG-ATHZ-03` | Authorization | Horizontal access / IDOR / BOLA | `manual_or_test-account_required` | WSTG-ATHZ |
| `WSTG-ATHZ-04` | Authorization | Tenant isolation and object ownership | `manual_or_test-account_required` | WSTG-ATHZ |
| `WSTG-ATHZ-05` | Authorization | Path traversal and forced browsing | `manual_or_test-account_required` | WSTG-ATHZ |
| `WSTG-SESS-01` | Session Management | Cookie Secure/HttpOnly/SameSite flags | `automated_passive` | WSTG-SESS |
| `WSTG-SESS-02` | Session Management | Cookie prefixes and SameSite=None constraints | `automated_passive` | WSTG-SESS |
| `WSTG-SESS-03` | Session Management | Session fixation and rotation | `manual_or_test-account_required` | WSTG-SESS |
| `WSTG-SESS-04` | Session Management | Session timeout and renewal | `manual_or_test-account_required` | WSTG-SESS |
| `WSTG-SESS-05` | Session Management | CSRF tokens and origin validation | `automated_review_candidate` | WSTG-SESS |
| `WSTG-SESS-06` | Session Management | Concurrent sessions and logout invalidation | `manual_or_test-account_required` | WSTG-SESS |
| `WSTG-SESS-07` | Session Management | Cache-control behavior for personalized content | `automated_review_candidate` | WSTG-SESS |
| `WSTG-INPV-01` | Input Validation | Reflected input canary (not an XSS proof) | `automated_review_candidate` | WSTG-INPV |
| `WSTG-INPV-02` | Input Validation | Stored and DOM-based cross-site scripting (XSS) assessment | `optional_specialist_tool_required` | WSTG-INPV |
| `WSTG-INPV-03` | Input Validation | SQL/NoSQL injection confirmation | `optional_specialist_tool_required` | WSTG-INPV |
| `WSTG-INPV-04` | Input Validation | OS command injection | `manual_or_test-account_required` | WSTG-INPV |
| `WSTG-INPV-05` | Input Validation | Server-side template injection | `optional_specialist_tool_required` | WSTG-INPV |
| `WSTG-INPV-06` | Input Validation | LDAP/XPath/other interpreter injection | `manual_or_test-account_required` | WSTG-INPV |
| `WSTG-INPV-07` | Input Validation | XML external entity processing (XXE) | `manual_or_test-account_required` | WSTG-INPV |
| `WSTG-INPV-08` | Input Validation | SSRF and URL-fetch input review | `automated_review_candidate` | WSTG-INPV |
| `WSTG-INPV-09` | Input Validation | Path traversal and file inclusion | `manual_or_test-account_required` | WSTG-INPV |
| `WSTG-INPV-10` | Input Validation | HTTP parameter pollution and mass assignment | `manual_or_test-account_required` | WSTG-INPV |
| `WSTG-ERRH-01` | Error Handling | Verbose framework / stack-trace disclosure | `automated_passive` | WSTG-ERRH |
| `WSTG-CRYP-01` | Cryptography | TLS certificate, protocol and cipher posture | `automated_passive` | WSTG-CRYP |
| `WSTG-CRYP-02` | Cryptography | Sensitive data over cleartext transport | `automated_review_candidate` | WSTG-CRYP |
| `WSTG-BUSL-01` | Business Logic | Workflow/state-machine validation | `manual_or_test-account_required` | WSTG-BUSL |
| `WSTG-BUSL-02` | Business Logic | Price/quantity/coupon/limit manipulation | `manual_or_test-account_required` | WSTG-BUSL |
| `WSTG-BUSL-03` | Business Logic | Replay, idempotency and duplicate submission | `manual_or_test-account_required` | WSTG-BUSL |
| `WSTG-BUSL-04` | Business Logic | Abuse of application workflows | `manual_or_test-account_required` | WSTG-BUSL |
| `WSTG-CLNT-01` | Client-side | DOM sinks and client-side data flow | `optional_specialist_tool_required` | WSTG-CLNT |
| `WSTG-CLNT-02` | Client-side | Third-party script SRI and supply chain | `automated_passive` | WSTG-CLNT |
| `WSTG-CLNT-03` | Client-side | CORS and cross-origin policy observations | `automated_passive` | WSTG-CLNT |
| `WSTG-CLNT-04` | Client-side | Clickjacking defense | `automated_passive` | WSTG-CLNT |
| `API-01` | API Security | API inventory and deprecated/versioned routes | `automated_passive` | OWASP API Top 10 |
| `API-02` | API Security | OpenAPI/Swagger authentication declaration review | `automated_review_candidate` | OWASP API Top 10 |
| `API-03` | API Security | GraphQL discovery and read-only introspection | `automated_review_candidate` | OWASP API Top 10 |
| `API-04` | API Security | BOLA / object-level authorization | `manual_or_test-account_required` | OWASP API Top 10 |
| `API-05` | API Security | Broken function-level authorization | `manual_or_test-account_required` | OWASP API Top 10 |
| `API-06` | API Security | Property-level authorization and mass assignment | `manual_or_test-account_required` | OWASP API Top 10 |
| `API-07` | API Security | Authentication and token lifecycle | `manual_or_test-account_required` | OWASP API Top 10 |
| `API-08` | API Security | Resource-consumption/rate-limit policy | `manual_or_test-account_required` | OWASP API Top 10 |
| `API-09` | API Security | SSRF-like URL parameters in API specs | `automated_review_candidate` | OWASP API Top 10 |
| `API-10` | API Security | API misconfiguration and sensitive data exposure | `automated_review_candidate` | OWASP API Top 10 |
| `SUPPLY-01` | Software Supply Chain | Third-party script integrity indicators | `automated_passive` | OWASP Top 10:2025 |
| `SUPPLY-02` | Software Supply Chain | Dependency/SBOM vulnerability review | `optional_specialist_tool_required` | OWASP ASVS 5.0 |
| `CLOUD-01` | Cloud/Deployment | Cloud IAM and storage policy review | `manual_or_test-account_required` | OWASP ASVS 5.0 |
| `CLOUD-02` | Cloud/Deployment | Container image and IaC scanning | `optional_specialist_tool_required` | OWASP ASVS 5.0 |
| `PRIV-01` | Privacy/Data Exposure | PII exposure in authenticated response bodies | `manual_or_test-account_required` | OWASP ASVS 5.0 |
| `LOG-01` | Logging/Monitoring | Security event logging and alerting validation | `manual_or_test-account_required` | OWASP ASVS 5.0 |
| `UPLOAD-01` | File Upload | Upload type, storage, execution and size controls | `manual_or_test-account_required` | OWASP WSTG |
| `UPLOAD-02` | File Upload | Download disposition and path handling | `manual_or_test-account_required` | OWASP WSTG |

## Important interpretation

This is a coverage plan. Manual/tool-required entries are not executed by the built-in safe scanner. No-finding does not prove absence.
