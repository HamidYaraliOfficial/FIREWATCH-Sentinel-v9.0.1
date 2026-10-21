"""Transparent security assessment plan for v9.

This is a coverage plan, not a claim that every test is automated. Each entry
states the execution mode so reports can distinguish an automated observation
from a human or specialist-tool requirement.
"""
from __future__ import annotations

_AUTOMATED = "automated_passive"
_CANDIDATE = "automated_review_candidate"
_MANUAL = "manual_or_test-account_required"
_TOOL = "optional_specialist_tool_required"

_ROWS = [
# Information gathering and attack-surface inventory
("WSTG-INFO-01","Information Gathering","Search-engine / public metadata review",_MANUAL,"WSTG-INFO"),
("WSTG-INFO-02","Information Gathering","Fingerprint web server and technologies",_AUTOMATED,"WSTG-INFO"),
("WSTG-INFO-03","Information Gathering","Review metadata and comments in HTML",_AUTOMATED,"WSTG-INFO"),
("WSTG-INFO-04","Information Gathering","Enumerate application entry points",_AUTOMATED,"WSTG-INFO"),
("WSTG-INFO-05","Information Gathering","Review web page content for information leakage",_AUTOMATED,"WSTG-INFO"),
("WSTG-INFO-06","Information Gathering","Identify application frameworks",_AUTOMATED,"WSTG-INFO"),
("WSTG-INFO-07","Information Gathering","Map execution paths and discovered routes",_AUTOMATED,"WSTG-INFO"),
("WSTG-CONF-01","Configuration","Check security headers and browser policy",_AUTOMATED,"WSTG-CONF"),
("WSTG-CONF-02","Configuration","Review exposed backup/configuration artifacts",_CANDIDATE,"WSTG-CONF"),
("WSTG-CONF-03","Configuration","Review HTTP methods and OPTIONS observations",_AUTOMATED,"WSTG-CONF"),
("WSTG-CONF-04","Configuration","Review TLS/certificate posture",_AUTOMATED,"WSTG-CONF"),
("WSTG-CONF-05","Configuration","Check subdomain takeover conditions",_MANUAL,"WSTG-CONF"),
("WSTG-CONF-06","Configuration","Review application/platform error handling",_AUTOMATED,"WSTG-CONF"),
("WSTG-CONF-07","Configuration","Review HSTS, redirect and cleartext transport",_AUTOMATED,"WSTG-CONF"),
("WSTG-CONF-08","Configuration","Review CSP directives and enforcement",_AUTOMATED,"WSTG-CONF"),
("WSTG-CONF-09","Configuration","Review source-map and public asset indicators",_CANDIDATE,"WSTG-CONF"),
("WSTG-CONF-10","Configuration","Review cross-origin isolation policy",_CANDIDATE,"WSTG-CONF"),
("WSTG-IDNT-01","Identity","Role/tenant model and identity lifecycle",_MANUAL,"WSTG-IDNT"),
("WSTG-IDNT-02","Identity","Account enumeration on registration/recovery",_MANUAL,"WSTG-IDNT"),
("WSTG-ATHN-01","Authentication","Credentials transported only over HTTPS",_AUTOMATED,"WSTG-ATHN"),
("WSTG-ATHN-02","Authentication","Default/weak credential assessment",_MANUAL,"WSTG-ATHN"),
("WSTG-ATHN-03","Authentication","Password policy and breached-password checks",_MANUAL,"WSTG-ATHN"),
("WSTG-ATHN-04","Authentication","Authentication bypass and alternate channels",_MANUAL,"WSTG-ATHN"),
("WSTG-ATHN-05","Authentication","MFA enforcement and recovery controls",_MANUAL,"WSTG-ATHN"),
("WSTG-ATHN-06","Authentication","Password reset and account recovery workflows",_MANUAL,"WSTG-ATHN"),
("WSTG-ATHN-07","Authentication","Rate limiting and lockout behavior",_MANUAL,"WSTG-ATHN"),
("WSTG-ATHN-08","Authentication","Authentication response differences",_MANUAL,"WSTG-ATHN"),
("WSTG-ATHN-09","Authentication","Logout and session invalidation",_MANUAL,"WSTG-ATHN"),
("WSTG-ATHZ-01","Authorization","Read-only comparison of supplied role profiles",_CANDIDATE,"WSTG-ATHZ"),
("WSTG-ATHZ-02","Authorization","Vertical privilege escalation / function authorization",_MANUAL,"WSTG-ATHZ"),
("WSTG-ATHZ-03","Authorization","Horizontal access / IDOR / BOLA",_MANUAL,"WSTG-ATHZ"),
("WSTG-ATHZ-04","Authorization","Tenant isolation and object ownership",_MANUAL,"WSTG-ATHZ"),
("WSTG-ATHZ-05","Authorization","Path traversal and forced browsing",_MANUAL,"WSTG-ATHZ"),
("WSTG-SESS-01","Session Management","Cookie Secure/HttpOnly/SameSite flags",_AUTOMATED,"WSTG-SESS"),
("WSTG-SESS-02","Session Management","Cookie prefixes and SameSite=None constraints",_AUTOMATED,"WSTG-SESS"),
("WSTG-SESS-03","Session Management","Session fixation and rotation",_MANUAL,"WSTG-SESS"),
("WSTG-SESS-04","Session Management","Session timeout and renewal",_MANUAL,"WSTG-SESS"),
("WSTG-SESS-05","Session Management","CSRF tokens and origin validation",_CANDIDATE,"WSTG-SESS"),
("WSTG-SESS-06","Session Management","Concurrent sessions and logout invalidation",_MANUAL,"WSTG-SESS"),
("WSTG-SESS-07","Session Management","Cache-control behavior for personalized content",_CANDIDATE,"WSTG-SESS"),
("WSTG-INPV-01","Input Validation","Reflected input canary (not an XSS proof)",_CANDIDATE,"WSTG-INPV"),
("WSTG-INPV-02","Input Validation","Stored and DOM-based cross-site scripting (XSS) assessment",_TOOL,"WSTG-INPV"),
("WSTG-INPV-03","Input Validation","SQL/NoSQL injection confirmation",_TOOL,"WSTG-INPV"),
("WSTG-INPV-04","Input Validation","OS command injection",_MANUAL,"WSTG-INPV"),
("WSTG-INPV-05","Input Validation","Server-side template injection",_TOOL,"WSTG-INPV"),
("WSTG-INPV-06","Input Validation","LDAP/XPath/other interpreter injection",_MANUAL,"WSTG-INPV"),
("WSTG-INPV-07","Input Validation","XML external entity processing (XXE)",_MANUAL,"WSTG-INPV"),
("WSTG-INPV-08","Input Validation","SSRF and URL-fetch input review",_CANDIDATE,"WSTG-INPV"),
("WSTG-INPV-09","Input Validation","Path traversal and file inclusion",_MANUAL,"WSTG-INPV"),
("WSTG-INPV-10","Input Validation","HTTP parameter pollution and mass assignment",_MANUAL,"WSTG-INPV"),
("WSTG-ERRH-01","Error Handling","Verbose framework / stack-trace disclosure",_AUTOMATED,"WSTG-ERRH"),
("WSTG-CRYP-01","Cryptography","TLS certificate, protocol and cipher posture",_AUTOMATED,"WSTG-CRYP"),
("WSTG-CRYP-02","Cryptography","Sensitive data over cleartext transport",_CANDIDATE,"WSTG-CRYP"),
("WSTG-BUSL-01","Business Logic","Workflow/state-machine validation",_MANUAL,"WSTG-BUSL"),
("WSTG-BUSL-02","Business Logic","Price/quantity/coupon/limit manipulation",_MANUAL,"WSTG-BUSL"),
("WSTG-BUSL-03","Business Logic","Replay, idempotency and duplicate submission",_MANUAL,"WSTG-BUSL"),
("WSTG-BUSL-04","Business Logic","Abuse of application workflows",_MANUAL,"WSTG-BUSL"),
("WSTG-CLNT-01","Client-side","DOM sinks and client-side data flow",_TOOL,"WSTG-CLNT"),
("WSTG-CLNT-02","Client-side","Third-party script SRI and supply chain",_AUTOMATED,"WSTG-CLNT"),
("WSTG-CLNT-03","Client-side","CORS and cross-origin policy observations",_AUTOMATED,"WSTG-CLNT"),
("WSTG-CLNT-04","Client-side","Clickjacking defense",_AUTOMATED,"WSTG-CLNT"),
("API-01","API Security","API inventory and deprecated/versioned routes",_AUTOMATED,"OWASP API Top 10"),
("API-02","API Security","OpenAPI/Swagger authentication declaration review",_CANDIDATE,"OWASP API Top 10"),
("API-03","API Security","GraphQL discovery and read-only introspection",_CANDIDATE,"OWASP API Top 10"),
("API-04","API Security","BOLA / object-level authorization",_MANUAL,"OWASP API Top 10"),
("API-05","API Security","Broken function-level authorization",_MANUAL,"OWASP API Top 10"),
("API-06","API Security","Property-level authorization and mass assignment",_MANUAL,"OWASP API Top 10"),
("API-07","API Security","Authentication and token lifecycle",_MANUAL,"OWASP API Top 10"),
("API-08","API Security","Resource-consumption/rate-limit policy",_MANUAL,"OWASP API Top 10"),
("API-09","API Security","SSRF-like URL parameters in API specs",_CANDIDATE,"OWASP API Top 10"),
("API-10","API Security","API misconfiguration and sensitive data exposure",_CANDIDATE,"OWASP API Top 10"),
("SUPPLY-01","Software Supply Chain","Third-party script integrity indicators",_AUTOMATED,"OWASP Top 10:2025"),
("SUPPLY-02","Software Supply Chain","Dependency/SBOM vulnerability review",_TOOL,"OWASP ASVS 5.0"),
("CLOUD-01","Cloud/Deployment","Cloud IAM and storage policy review",_MANUAL,"OWASP ASVS 5.0"),
("CLOUD-02","Cloud/Deployment","Container image and IaC scanning",_TOOL,"OWASP ASVS 5.0"),
("PRIV-01","Privacy/Data Exposure","PII exposure in authenticated response bodies",_MANUAL,"OWASP ASVS 5.0"),
("LOG-01","Logging/Monitoring","Security event logging and alerting validation",_MANUAL,"OWASP ASVS 5.0"),
("UPLOAD-01","File Upload","Upload type, storage, execution and size controls",_MANUAL,"OWASP WSTG"),
("UPLOAD-02","File Upload","Download disposition and path handling",_MANUAL,"OWASP WSTG"),
]

TEST_PLAN = [
    {"id": rid, "category": category, "title": title, "execution_mode": mode,
     "standard_mapping": mapping, "safe_by_default": True,
     "status_semantics": ("implemented" if mode == _AUTOMATED else "candidate_or_additional_validation_required")}
    for rid, category, title, mode, mapping in _ROWS
]

STANDARDS = {
    "owasp_top_10": "2025",
    "owasp_asvs": "5.0.0",
    "owasp_wstg_stable": "4.2 (stable; WSTG 5.0 is under development)",
    "owasp_api_security_top_10": "2023",
}

def get_assessment_plan():
    counts = {}
    for item in TEST_PLAN:
        counts[item["execution_mode"]] = counts.get(item["execution_mode"], 0) + 1
    return {
        "version": "9.0.1",
        "standards": STANDARDS,
        "total_cases": len(TEST_PLAN),
        "execution_mode_counts": counts,
        "test_cases": TEST_PLAN,
        "disclaimer": "This is a coverage plan. Manual/tool-required entries are not executed by the built-in safe scanner. No-finding does not prove absence.",
    }
