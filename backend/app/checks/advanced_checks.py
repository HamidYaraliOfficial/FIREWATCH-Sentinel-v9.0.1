from __future__ import annotations
import re
from urllib.parse import urlparse
from .base import FindingCandidate
from ..models import Severity

REF_WSTG = "OWASP WSTG stable"

def _f(rule, category, title, severity, confidence, endpoint, description, impact, remediation, evidence, refs=None, data=None):
    return FindingCandidate(rule, category, title, severity, confidence, endpoint, description, impact, remediation, evidence, refs or [REF_WSTG], data or {})

def run_advanced_checks(page, context):
    """Conservative passive checks: observations are reviewable, not exploit claims."""
    out=[]; h={str(k).lower():str(v) for k,v in (page.observation.headers or {}).items()}; url=page.url; body=page.observation.body or ""; low=body.lower()
    csp=h.get('content-security-policy','').lower()
    if csp:
        directives={}
        for chunk in csp.split(';'):
            bits=chunk.strip().split()
            if bits: directives[bits[0]]=bits[1:]
        script=directives.get('script-src',directives.get('default-src',[]))
        if "'unsafe-eval'" in script:
            out.append(_f('FW-CSP-001','security-headers','CSP permits unsafe-eval',Severity.MEDIUM,.94,url,"The Content-Security-Policy permits 'unsafe-eval' for script execution.","This weakens CSP's ability to limit script injection impact.","Remove unsafe-eval where practical; prefer nonce/hash-based policies.","script-src/default-src includes 'unsafe-eval'.",data={'directive':script}))
        if "'unsafe-inline'" in script and not any(x.startswith("'nonce-") or x.startswith("'sha256-") or x.startswith("'sha384-") or x.startswith("'sha512-") for x in script):
            out.append(_f('FW-CSP-002','security-headers','CSP allows inline scripts without nonce/hash restriction',Severity.MEDIUM,.9,url,"The effective script policy allows unsafe inline scripts without a nonce/hash source observed in that directive.","A successful markup/script injection may be harder to contain.","Use strict-dynamic with nonce/hash-based script policies where compatible.","script-src/default-src contains 'unsafe-inline'.",data={'directive':script}))
        if '*' in script:
            out.append(_f('FW-CSP-003','security-headers','CSP uses wildcard script source',Severity.MEDIUM,.86,url,"The effective script policy includes a wildcard source.","Broad source trust reduces script loading restrictions.","Use explicit trusted origins and nonce/hash controls.","script-src/default-src contains wildcard source.",data={'directive':script}))
    elif 'content-security-policy-report-only' in h:
        out.append(_f('FW-CSP-004','security-headers','CSP is report-only rather than enforced',Severity.LOW,.97,url,"Only Content-Security-Policy-Report-Only was found; that policy reports violations but does not block them.","The policy is not an enforcement boundary.","When validated, deploy an enforcing Content-Security-Policy alongside report-only testing.","Report-only header is present without an enforcing CSP."))

    # Additional hardening observations. These are configuration indicators, not exploit proofs.
    if csp:
        directives = {}
        for chunk in csp.split(';'):
            bits = chunk.strip().split()
            if bits: directives[bits[0]] = bits[1:]
        if directives.get('object-src', []) != ["'none'"] and "'none'" not in directives.get('object-src', []):
            out.append(_f('FW-CSP-005','security-headers','CSP does not clearly restrict object-src',Severity.LOW,.82,url,
                "The enforced CSP does not clearly set object-src 'none'.",
                'Legacy plugin/object embedding can remain less restricted than intended.',
                "Set object-src 'none' unless the application explicitly requires object/embed resources.",
                'No object-src none directive observed.'))
        if 'base-uri' not in directives:
            out.append(_f('FW-CSP-006','security-headers','CSP does not define base-uri',Severity.LOW,.80,url,
                'The enforced CSP has no base-uri directive.',
                'An injected base element may influence relative URL resolution in some contexts.',
                "Set base-uri 'self' or 'none' where compatible.",
                'base-uri directive absent.'))
    # Isolation headers are application-dependent, so missing values are low-confidence review items.
    if 'cross-origin-opener-policy' not in h and 'text/html' in getattr(page.observation,'content_type','').lower():
        out.append(_f('FW-ISOLATION-001','browser-isolation','Cross-Origin-Opener-Policy not observed',Severity.INFO,.58,url,
            'No Cross-Origin-Opener-Policy response header was observed on HTML.',
            'Cross-origin window relationships may be less isolated than a highly isolated application expects.',
            'Review whether same-origin or same-origin-allow-popups isolation is appropriate for this application.',
            'Cross-Origin-Opener-Policy absent; applicability depends on app behavior.'))
    if 'cross-origin-resource-policy' not in h and 'text/html' in getattr(page.observation,'content_type','').lower():
        out.append(_f('FW-ISOLATION-002','browser-isolation','Cross-Origin-Resource-Policy not observed',Severity.INFO,.55,url,
            'No Cross-Origin-Resource-Policy response header was observed on HTML.',
            'Cross-origin resource embedding policy is implicit rather than explicitly declared.',
            'Assess whether same-origin, same-site, or cross-origin resource policy fits the product.',
            'Cross-Origin-Resource-Policy absent; no exploit inferred.'))
    xcto = h.get('x-content-type-options','').strip().lower()
    if xcto and xcto != 'nosniff':
        out.append(_f('FW-HEADER-001','security-headers','X-Content-Type-Options has unexpected value',Severity.LOW,.92,url,
            'X-Content-Type-Options is present but does not equal nosniff.',
            'MIME sniffing defenses may not be active as intended.',
            'Set X-Content-Type-Options: nosniff.',f'Observed value: {xcto[:100]}'))
    xfo = h.get('x-frame-options','').strip().lower()
    if xfo and xfo not in {'deny','sameorigin'}:
        out.append(_f('FW-HEADER-002','security-headers','X-Frame-Options has a nonstandard value',Severity.LOW,.85,url,
            'X-Frame-Options does not use DENY or SAMEORIGIN.',
            'Legacy frame protection may not be interpreted consistently by browsers.',
            "Use a compatible X-Frame-Options value and/or CSP frame-ancestors.",f'Observed value: {xfo[:100]}'))
    server = h.get('server','')
    powered = h.get('x-powered-by','')
    if re.search(r'\b(?:apache|nginx|iis|php|express|tomcat)[ /-]?[0-9]+(?:\.[0-9]+){1,3}',server+' '+powered,re.I):
        out.append(_f('FW-DISCLOSE-001','information-disclosure','Versioned technology banner exposed',Severity.INFO,.90,url,
            'A response header appears to expose a precise software version.',
            'Version information may help correlate a service with known advisories; it does not prove that the version is vulnerable.',
            'Suppress unnecessary precise version banners where feasible and maintain patch inventory.',
            f'Observed banner: {(server+' '+powered).strip()[:160]}'))

    # HSTS weaknesses are presented as configuration observations, not universal breakage.
    hsts=h.get('strict-transport-security','')
    if hsts:
        m=re.search(r'max-age\s*=\s*(\d+)',hsts,re.I)
        if m and int(m.group(1)) < 15552000:
            out.append(_f('FW-HSTS-002','transport','HSTS max-age is shorter than six months',Severity.LOW,.96,url,"The HSTS max-age is below 15,552,000 seconds.","Protection against downgrade/first-visit risks expires relatively quickly.","After validating all hosts, consider a longer HSTS max-age and includeSubDomains if appropriate.",f"Observed HSTS: {hsts[:300]}"))

    sensitive_path=any(x in urlparse(url).path.lower() for x in ('/login','/account','/profile','/dashboard','/admin','/token','/session','/orders','/billing'))
    cache=h.get('cache-control','').lower()
    if sensitive_path and ('public' in cache or 's-maxage' in cache) and 'no-store' not in cache:
        out.append(_f('FW-CACHE-002','caching','Sensitive-looking endpoint advertises shared-cache directives',Severity.MEDIUM,.76,url,"The path looks sensitive and Cache-Control includes public or s-maxage without no-store.","Shared caches could retain user-specific content if the response is personalized.","Validate caching behavior with authenticated and anonymous sessions; use private/no-store where appropriate.",f"Cache-Control: {cache[:300]}",data={'cache_control':cache}))

    # Cross-origin libraries without SRI are review candidates; same-origin resources are omitted.
    base=urlparse(url)
    external=[]
    for src in re.findall(r'<script\b[^>]*\bsrc=[\"\']([^\"\']+)[\"\'][^>]*>',body,re.I):
        p=urlparse(src)
        if p.scheme in ('http','https') and p.netloc and p.netloc.lower()!=base.netloc.lower():
            tag_match=re.search(r'<script\b(?=[^>]*\bsrc=[\"\']'+re.escape(src)+r'[\"\'])[^>]*>',body,re.I)
            tag=tag_match.group(0) if tag_match else ''
            if not re.search(r'\bintegrity\s*=',tag,re.I): external.append(src)
    if external:
        out.append(_f('FW-SUPPLY-001','software-supply-chain','Third-party script without Subresource Integrity',Severity.INFO,.8,url,"One or more third-party scripts lack an integrity attribute in the observed markup.","If the third-party source is compromised or changes unexpectedly, script content may change without an SRI check.","For stable third-party assets, consider SRI plus crossorigin; use CSP and dependency governance as defense in depth.",f"{len(external)} external script(s) without SRI observed.",data={'scripts':external[:30]}))

    # Exposed framework/source indicators.
    markers=[]
    for name, pats in {
        'Django debug': ['technical 500 debug page','django.core.exceptions','debug=true'],
        'Spring actuator': ['"activeprofiles"','"propertysources"','"beans"'],
        'PHP diagnostics': ['phpinfo()','php version </td>'],
        'Node stack trace': [' at process.','node_modules/'],
    }.items():
        if any(p in low for p in pats): markers.append(name)
    if markers:
        out.append(_f('FW-ERROR-002','error-handling','Framework diagnostic/stack trace indicators',Severity.MEDIUM,.82,url,"The response contains strings commonly associated with runtime diagnostics or stack traces.","Internal paths and implementation details can assist follow-on attacks.","Disable production debug output and return generic errors while retaining server-side diagnostics.","Matched indicators: "+', '.join(markers),data={'markers':markers}))

    return out
