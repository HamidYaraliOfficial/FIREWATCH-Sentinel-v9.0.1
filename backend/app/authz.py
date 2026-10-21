from __future__ import annotations
from dataclasses import dataclass
from urllib.parse import urlparse
from .http_client import SafeHTTPClient
from .scope import ScopePolicy
from .checks.base import FindingCandidate
from .models import Severity

@dataclass
class AuthProfile:
    name:str
    headers:dict[str,str]

SUCCESS={200,206,304}
SENSITIVE_PATH_HINTS=('/admin','/users/','/accounts/','/orders/','/profile','/settings','/management','/internal','/billing','/invoices')
SENSITIVE_BODY_HINTS=('"email"','"role"','"isadmin"','"owner_id"','"userid"','"accountnumber"','"billing"','"private"','"permissions"','"ssn"')

async def review_authorization(scope:ScopePolicy,urls:list[str],profiles:list[AuthProfile],delay_ms:int=150):
    """Read-only role comparison. Reports candidates only, never calls write methods."""
    if len(profiles)<2:return []
    low=next((p for p in profiles if p.name.lower() in {'low','user','member','anonymous','least-privilege'}),profiles[-1])
    high=next((p for p in profiles if p.name.lower() in {'high','admin','privileged','administrator'}),profiles[0])
    candidates=[u for u in dict.fromkeys(urls) if scope.is_allowed(u) and any(x in urlparse(u).path.lower() for x in SENSITIVE_PATH_HINTS)][:100]
    out=[]
    async with SafeHTTPClient(scope,delay_ms=max(200,delay_ms)) as client:
        for url in candidates:
            # Only GET requests are used. Profile header values are provided by the authorized tester.
            h=await client.request('GET',url,headers=high.headers)
            l=await client.request('GET',url,headers=low.headers)
            if h.error or l.error or h.status_code not in SUCCESS or l.status_code not in SUCCESS: continue
            body=l.body.lower()[:500_000]
            privileged_path=any(x in urlparse(url).path.lower() for x in ('/admin','/management','/internal'))
            sensitive_data=any(token in body for token in SENSITIVE_BODY_HINTS)
            same_body=h.body_sha256==l.body_sha256
            if not (privileged_path or sensitive_data): continue
            # A successful response alone is not considered proof. Make the evidence explicit.
            out.append(FindingCandidate(
                'FW-AUTHZ-001','access-control','Authorization review candidate: lower-privilege profile can read a sensitive endpoint',
                Severity.MEDIUM,.70,url,
                'A supplied lower-privilege profile received a successful GET response from a sensitive-looking endpoint; response indicators warranted review. This is not proof of an authorization flaw.',
                'If the resource should be restricted to higher privileges, an authorization defect could expose privileged functions or sensitive records.',
                'Verify access decisions with designated least-privilege test accounts. Confirm the expected role policy and review the returned resource without exposing production user data.',
                f'High profile status {h.status_code}; lower-privilege profile status {l.status_code}; privileged-path hint={privileged_path}; sensitive-data marker={sensitive_data}; bodies-identical={same_body}.',
                references=['OWASP Top 10:2025 A01 Broken Access Control','OWASP API Security Top 10:2023 API1/API5'],
                evidence={'high_status':h.status_code,'low_status':l.status_code,'privileged_path_hint':privileged_path,'sensitive_data_marker':sensitive_data,'body_hashes_equal':same_body,'methods_used':['GET']}))
    return out
