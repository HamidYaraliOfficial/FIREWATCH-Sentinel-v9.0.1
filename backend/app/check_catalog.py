"""Machine-readable test coverage catalog for reports and CI consumers."""
import re
CATALOG = [
 {"id":"FW-WEB-001..011","domain":"HTTP security headers, transport, disclosure, caching, source maps, mixed content","mode":"passive","mapping":["OWASP Top 10:2025 A02","OWASP WSTG stable: Configuration / Information Gathering"]},
 {"id":"FW-CSP-001..006","domain":"CSP policy weaknesses","mode":"passive","mapping":["OWASP Top 10:2025 A02","OWASP WSTG stable: Client-side Testing"]},
 {"id":"FW-HSTS-002","domain":"HSTS lifetime review","mode":"passive","mapping":["OWASP Top 10:2025 A02/A04"]},
 {"id":"FW-COOKIE-001..006","domain":"Cookie flags and session indicators","mode":"passive","mapping":["OWASP Top 10:2025 A07","OWASP WSTG stable: Session Management"]},
 {"id":"FW-FORM-001..002","domain":"Password transport and CSRF review candidates","mode":"passive","mapping":["OWASP Top 10:2025 A01/A07","OWASP WSTG stable: Authentication / CSRF"]},
 {"id":"FW-CORS-001..005","domain":"CORS policy, origin reflection and preflight","mode":"read-only active + passive","mapping":["OWASP API Security Top 10:2023 API8","OWASP WSTG stable: Configuration"]},
 {"id":"FW-API-001..003","domain":"OpenAPI security declarations, operation inventory, URL-like parameters","mode":"passive","mapping":["OWASP API Security Top 10:2023 API9/API8/API7"]},
 {"id":"FW-GQL-001..002","domain":"GraphQL discovery and read-only introspection","mode":"read-only active","mapping":["OWASP API Security Top 10:2023 API8/API9"]},
 {"id":"FW-AUTHZ-001","domain":"Cross-role read-only authorization review candidate","mode":"read-only active; requires supplied profiles","mapping":["OWASP Top 10:2025 A01","OWASP API Security Top 10:2023 API1/API5"]},
 {"id":"FW-TLS-001..005","domain":"TLS protocol, cipher, certificate and connection posture","mode":"network observation","mapping":["OWASP Top 10:2025 A04","OWASP WSTG stable: Transport Layer Protection"]},
 {"id":"FW-SUPPLY-001","domain":"Third-party script integrity review","mode":"passive","mapping":["OWASP Top 10:2025 A03/A08"]},
 {"id":"FW-CONTENT-001..002","domain":"Backup indicators and client-visible secret patterns","mode":"passive","mapping":["OWASP Top 10:2025 A02/A04"]},
 {"id":"FW-ISOLATION-001..002","domain":"Cross-origin opener/resource policy observations","mode":"passive review candidate","mapping":["OWASP ASVS 5.0.0: Browser security"]},
 {"id":"FW-HEADER-001..002","domain":"Unexpected security-header values","mode":"passive","mapping":["OWASP Top 10:2025 A02","OWASP ASVS 5.0.0"]},
 {"id":"FW-DISCLOSE-001","domain":"Versioned server/framework banner exposure","mode":"passive","mapping":["OWASP Top 10:2025 A02"]},
 {"id":"FW-EXPOSE-001","domain":"Read-only diagnostic/config/repository exposure signatures","mode":"bounded GET probes","mapping":["OWASP Top 10:2025 A02/A09","OWASP API Security Top 10:2023 API8/API9"]},
 {"id":"FW-INPUT-001","domain":"Harmless GET parameter reflection canary; not an XSS proof","mode":"bounded read-only GET probe","mapping":["OWASP Top 10:2025 A05","OWASP WSTG stable: Input Validation Testing"]},
]

def _matches(rule_id: str, family: str) -> bool:
    if '..' not in family: return rule_id == family
    prefix, end_text = family.split('..',1)
    match=re.match(r'^(.*?)(\d+)$',prefix)
    if not match:return rule_id.startswith(prefix)
    stem,start=match.group(1),int(match.group(2))
    try:end=int(end_text)
    except ValueError:return rule_id.startswith(stem)
    found=re.match(r'^'+re.escape(stem)+r'(\d+)$',rule_id)
    return bool(found and start<=int(found.group(1))<=end)

def coverage_matrix(findings):
    result=[]
    for item in CATALOG:
        base=dict(item)
        matched=[f for f in findings if _matches(getattr(f,'rule_id','') or '',item['id'])]
        base['finding_count']=len(matched)
        base['status']='finding_observed' if matched else 'no_finding_recorded_or_not_applicable'
        result.append(base)
    return result
