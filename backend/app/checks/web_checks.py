from __future__ import annotations
import re
from urllib.parse import urlparse
from .base import FindingCandidate,CheckContext
from ..models import Severity

def _f(rule,cat,title,sev,conf,url,desc,impact,fix,evidence,refs=('OWASP WSTG v4.2',),data=None):
    return FindingCandidate(rule,cat,title,sev,conf,url,desc,impact,fix,evidence,list(refs),data or {})

def run_page_checks(page,context):
    h=page.observation.headers; out=[]; u=page.url; low=page.observation.body.lower()
    required=[('content-security-policy','FW-WEB-001','CSP header missing',Severity.MEDIUM,.97,'Deploy a restrictive Content-Security-Policy.'),('x-content-type-options','FW-WEB-002','X-Content-Type-Options missing',Severity.LOW,.98,'Set X-Content-Type-Options: nosniff.'),('referrer-policy','FW-WEB-003','Referrer-Policy missing',Severity.LOW,.96,'Set an explicit Referrer-Policy.'),('permissions-policy','FW-WEB-004','Permissions-Policy missing',Severity.LOW,.93,'Define an explicit Permissions-Policy for used browser capabilities.')]
    for header,rule,title,sev,conf,fix in required:
        if header not in h: out.append(_f(rule,'security-headers',title,sev,conf,u,f'The response does not advertise {header}.','Browser-side defense-in-depth is weaker than necessary.',fix,f'{header} was absent.'))
    csp=h.get('content-security-policy','').lower()
    if 'x-frame-options' not in h and 'frame-ancestors' not in csp: out.append(_f('FW-WEB-005','security-headers','Clickjacking protection not detected',Severity.MEDIUM,.95,u,'Neither X-Frame-Options nor CSP frame-ancestors was observed.','Sensitive UI may be embeddable by another origin.','Set CSP frame-ancestors and/or X-Frame-Options as appropriate.','No frame restriction detected.'))
    if u.startswith('https://') and 'strict-transport-security' not in h: out.append(_f('FW-WEB-006','transport','HSTS missing on HTTPS response',Severity.MEDIUM,.99,u,'The HTTPS response does not set Strict-Transport-Security.','Users can remain exposed to downgrade/first-visit transport risks.','Enable HSTS after validating all relevant subdomains.','Strict-Transport-Security absent.'))
    server={k:h[k] for k in ('server','x-powered-by') if k in h}
    if server: out.append(_f('FW-WEB-007','information-disclosure','Technology banner disclosure',Severity.INFO,.92,u,'Response headers reveal server/framework details.','Fingerprinting becomes easier.','Reduce unnecessary banner disclosure.','Disclosed: '+str(server),data={'headers':server}))
    if 'cache-control' not in h and any(x in u.lower() for x in ('login','account','profile','dashboard','admin','token','session')): out.append(_f('FW-WEB-008','caching','Sensitive-looking page lacks Cache-Control evidence',Severity.MEDIUM,.72,u,'A sensitive-looking URL does not expose a restrictive Cache-Control policy.','Shared/private caching could retain sensitive material depending on framework/proxy behavior.','Review caching policy and explicitly control storage for authenticated/sensitive responses.','No Cache-Control header on sensitive-looking path.'))
    if 'sourceMappingURL=' in page.observation.body: out.append(_f('FW-WEB-009','client-side','Public source map reference',Severity.LOW,.9,u,'The document references a JavaScript source map.','Source maps can reveal original sources and internal paths.','Do not publish sensitive production source maps unless intentionally exposed.','sourceMappingURL marker detected.'))
    if page.mixed_content: out.append(_f('FW-WEB-010','transport','Mixed content reference',Severity.MEDIUM,.99,u,'HTTPS page references HTTP resources.','Integrity/confidentiality can be weakened or resources blocked.','Serve all resources over HTTPS.',f'{len(page.mixed_content)} HTTP resource references detected.',data={'resources':page.mixed_content[:50]}))
    error_markers=['traceback (most recent call last)','stack trace','sql syntax','sequelize','django.core','laravel\\','org.springframework','exception:']
    hits=[x for x in error_markers if x in low]
    if hits: out.append(_f('FW-WEB-011','error-handling','Potential verbose error disclosure',Severity.MEDIUM,.83,u,'The response contains markers associated with developer/runtime error details.','Implementation details can expose internals and aid targeted attacks.','Return generic production errors and log diagnostic details server-side.',f'Markers: {hits}',data={'markers':hits}))
    return out

def run_form_checks(page,context):
    out=[]
    for form in page.forms:
        action=form.get('action') or page.url; method=form.get('method','GET').upper(); types={(i.get('type') or '').lower() for i in form.get('inputs',[])}; names={(i.get('name') or '').lower() for i in form.get('inputs',[]) if i.get('name')}
        if 'password' in types and urlparse(action).scheme=='http': out.append(_f('FW-FORM-001','authentication','Password form submits over HTTP',Severity.HIGH,.995,page.url,'A password-bearing form submits to cleartext HTTP.','Credentials may be exposed to interception.','Use HTTPS-only authentication endpoints and redirect/block cleartext access.','Password input with HTTP action.',data={'action':action}))
        if method in {'POST','PUT','PATCH','DELETE'} and not any(k in names for k in ('csrf','csrf_token','_csrf','xsrf','_token')):
            out.append(_f('FW-FORM-002','csrf','CSRF protection not obvious in state-changing form',Severity.INFO,.62,page.url,'No commonly named CSRF token field was observed. This is a review candidate, not proof of a CSRF flaw.','State-changing requests may require server-side CSRF defenses.','Verify framework/token/header-based CSRF controls for state-changing operations.','No common CSRF token field name detected.',data={'action':action,'method':method}))
    return out

def run_content_checks(page,context):
    out=[]; linked=[]
    for x in page.links:
        path=urlparse(x).path.lower()
        if path.endswith(('.bak','.old','.orig','.backup','.zip','.tar','.gz','.sql')): linked.append(x)
    if linked: out.append(_f('FW-CONTENT-001','information-disclosure','Backup/archive artifact linked by page',Severity.MEDIUM,.94,page.url,'The application exposes links ending in common backup/archive extensions.','Backup files may contain source/configuration/data.','Remove unintended artifacts from web-accessible locations.',f'{len(linked)} candidate links found.',data={'links':linked[:30]}))
    if re.search(r'(?i)(api[_-]?key|secret[_-]?key|access[_-]?token|private[_-]?key)\s*[:=]\s*[\"\'][^\"\']{8,}[\"\']',page.observation.body):
        out.append(_f('FW-CONTENT-002','secrets','Possible hard-coded secret in response',Severity.HIGH,.79,page.url,'The response matches patterns associated with embedded secret material.','Leaked secrets may allow unauthorized access to dependent services.','Remove secrets from client-delivered content and rotate any exposed credential.', 'Secret-like pattern matched; manual verification required.'))
    return out
