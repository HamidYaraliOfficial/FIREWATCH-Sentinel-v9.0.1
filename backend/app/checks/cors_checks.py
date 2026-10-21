from ..models import Severity
from .base import FindingCandidate

def run_cors_checks(page,context):
    h=page.observation.headers; out=[]; acao=h.get('access-control-allow-origin'); acac=h.get('access-control-allow-credentials','').lower()
    if acao=='*': out.append(FindingCandidate('FW-CORS-001','api','Wildcard CORS policy',Severity.LOW,.97,page.url,'Access-Control-Allow-Origin is wildcard.','Cross-origin read access can be broader than intended for public or sensitive APIs.','Use explicit trusted origins for sensitive endpoints.','ACAO: *'))
    if acao=='*' and acac=='true': out.append(FindingCandidate('FW-CORS-002','api','Inconsistent wildcard credentialed CORS',Severity.MEDIUM,.94,page.url,'Wildcard CORS is advertised together with credential support.','The configuration is inconsistent and should be tightened.','Use an explicit allow-list for credentialed cross-origin requests.','ACAO=* and ACAC=true.'))
    expose=h.get('access-control-expose-headers','')
    if expose=='*': out.append(FindingCandidate('FW-CORS-003','api','Wildcard CORS exposed headers',Severity.LOW,.9,page.url,'The response exposes all response headers to cross-origin clients.','Sensitive headers may become readable cross-origin where CORS permits it.','Expose only the minimal required response headers.','Access-Control-Expose-Headers: *'))
    return out
