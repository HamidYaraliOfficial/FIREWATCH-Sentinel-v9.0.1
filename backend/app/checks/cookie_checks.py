from __future__ import annotations
from .base import FindingCandidate,CheckContext
from ..models import Severity

def _cookies(raw):
    if not raw:return []
    # HTTP client normalizes each Set-Cookie value to a newline-separated list.
    # Fall back to a single cookie instead of splitting on commas, because Expires contains commas.
    return [x.strip() for x in raw.splitlines() if x.strip()]
def run_cookie_checks(page,context):
    out=[]; raw=page.observation.headers.get('set-cookie')
    for cookie in _cookies(raw):
        name=cookie.split('=',1)[0].strip(); parts=[x.strip().lower() for x in cookie.split(';')[1:]]; attrs={x.split('=',1)[0].strip() for x in parts}; session=any(x in name.lower() for x in ('session','sess','auth','token','jwt','sid'))
        if page.url.startswith('https://') and 'secure' not in attrs: out.append(FindingCandidate('FW-COOKIE-001','session','Cookie missing Secure attribute',Severity.MEDIUM if session else Severity.LOW,.96,page.url,f'Cookie `{name}` lacks Secure.','Browser may transmit it over non-HTTPS contexts.','Add Secure to cookies that are intended for HTTPS-only transport.',f'{name}: Secure absent.',evidence={'cookie':name}))
        if session and 'httponly' not in attrs: out.append(FindingCandidate('FW-COOKIE-002','session','Session-like cookie missing HttpOnly',Severity.MEDIUM,.95,page.url,f'Cookie `{name}` appears session/auth related but lacks HttpOnly.','Client-side script access can increase credential exposure in case of XSS.','Add HttpOnly when JavaScript access is not required.',f'{name}: HttpOnly absent.',evidence={'cookie':name}))
        if not any(x.startswith('samesite=') for x in parts): out.append(FindingCandidate('FW-COOKIE-003','session','Cookie missing SameSite attribute',Severity.LOW,.9,page.url,f'Cookie `{name}` does not explicitly declare SameSite.','Cross-site cookie behavior is less explicit.','Set SameSite=Lax/Strict as appropriate, using None only when required and with Secure.',f'{name}: SameSite absent.',evidence={'cookie':name}))
        if any(x == 'samesite=none' for x in parts) and 'secure' not in attrs:
            out.append(FindingCandidate('FW-COOKIE-004','session','SameSite=None cookie lacks Secure',Severity.MEDIUM,.97,page.url,f'Cookie `{name}` declares SameSite=None without Secure.','Modern browsers may reject the cookie or the cookie may be exposed to insecure transport contexts.','Add Secure to SameSite=None cookies and serve the application only over HTTPS.',f'{name}: SameSite=None and Secure absent.',evidence={'cookie':name}))
        if name.startswith('__Host-') and ('secure' not in attrs or 'path=/' not in parts or any(x.startswith('domain=') for x in parts)):
            out.append(FindingCandidate('FW-COOKIE-005','session','__Host- cookie prefix constraints not satisfied',Severity.MEDIUM,.98,page.url,f'Cookie `{name}` uses the __Host- prefix but does not satisfy its Secure, Path=/, and no-Domain requirements.','The browser may reject the cookie or its intended host-only guarantees may not hold.','Set Secure, Path=/, and omit Domain for __Host- cookies.',f'{name}: __Host- prefix attributes are inconsistent.',evidence={'cookie':name,'attributes':parts}))
        if name.startswith('__Secure-') and 'secure' not in attrs:
            out.append(FindingCandidate('FW-COOKIE-006','session','__Secure- cookie lacks Secure attribute',Severity.MEDIUM,.98,page.url,f'Cookie `{name}` uses the __Secure- prefix without Secure.','The cookie may be rejected or fail its intended transport guarantee.','Set Secure on __Secure- cookies and deliver them over HTTPS.',f'{name}: __Secure- prefix without Secure.',evidence={'cookie':name}))
    return out
