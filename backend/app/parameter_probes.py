from __future__ import annotations
import secrets, string
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode
from bs4 import BeautifulSoup
from .http_client import SafeHTTPClient
from .scope import ScopePolicy
from .checks.base import FindingCandidate
from .models import Severity

SENSITIVE_PARAMETER_NAMES={'authorization','auth','token','jwt','access_token','refresh_token','id_token','password','passwd','passphrase','secret','secret_key','private_key','api_key','apikey','session','sessionid','session_id','sid','code','otp','csrf','xsrf','credential','credentials'}

def _has_attribute_reflection(html: str, marker: str) -> bool:
    try:
        soup=BeautifulSoup(html,'html.parser')
        for tag in soup.find_all(True):
            for value in tag.attrs.values():
                values=value if isinstance(value,list) else [value]
                if any(isinstance(v,str) and marker in v for v in values): return True
    except Exception: pass
    return False

async def probe_reflected_query_inputs(scope: ScopePolicy, urls: list[str], delay_ms: int=200, max_probes: int=60, headers:dict[str,str]|None=None):
    """Harmless alphanumeric canary only. Never submits forms or injects executable payloads."""
    candidates=[]; seen=set(); probes=0
    async with SafeHTTPClient(scope,delay_ms=delay_ms,headers=headers or {}) as client:
        for original in urls:
            if probes>=max_probes: break
            parts=urlsplit(original); pairs=parse_qsl(parts.query,keep_blank_values=True)
            if not pairs: continue
            for idx,(name,value) in enumerate(pairs):
                if probes>=max_probes: break
                if name.lower() in SENSITIVE_PARAMETER_NAMES or len(name)>100: continue
                marker='FWCANARY'+''.join(secrets.choice(string.ascii_uppercase+string.digits) for _ in range(14))
                mutated=list(pairs); mutated[idx]=(name,marker)
                probe_url=urlunsplit((parts.scheme,parts.netloc,parts.path,urlencode(mutated,doseq=True),''))
                safe=scope.join(scope.root_url,probe_url)
                if not safe or safe in seen: continue
                seen.add(safe); probes+=1
                obs=await client.request('GET',safe)
                if obs.error or obs.status_code<200 or obs.status_code>=400 or marker not in obs.body: continue
                in_attribute=_has_attribute_reflection(obs.body,marker)
                sink='HTML attribute context' if in_attribute else 'response body (context not established)'
                candidates.append(FindingCandidate(
                    'FW-INPUT-001','input-validation','Reflected query parameter requires contextual review',Severity.INFO,.64,original,
                    f'An inert alphanumeric canary submitted via GET parameter `{name}` appeared in the response ({sink}). This does not prove XSS or code execution.',
                    'If untrusted data is reflected into an executable HTML/JavaScript/URL context without context-appropriate encoding, client-side injection may be possible.',
                    'Review the exact output context and apply context-aware encoding; use a restrictive CSP as defense-in-depth. Retest with an approved context-specific methodology.',
                    f'Harmless canary reflection observed for parameter `{name}`; no executable payload was used.',
                    references=['OWASP WSTG stable: Input Validation Testing','OWASP Top 10:2025 A05 Injection'],
                    evidence={'parameter':name,'status_code':obs.status_code,'context_hint':sink,'probe_type':'alphanumeric-canary'}))
    return candidates
