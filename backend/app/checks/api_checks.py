from __future__ import annotations
import json, re, yaml
from urllib.parse import urlparse
from .base import FindingCandidate, CheckContext
from ..models import Severity

SPEC_PATHS=('/openapi.json','/openapi.yaml','/swagger.json','/swagger/v1/swagger.json','/api-docs','/v3/api-docs','/docs/openapi.json')
HTTP_METHODS={'get','post','put','patch','delete','options','head'}

def classify_api(url):
    p=urlparse(url).path.lower()
    segments = {part for part in p.split('/') if part}
    if 'graphql' in segments:
        return 'graphql'
    return 'api' if any(x in p for x in ('/api/','/v1/','/v2/','/rest/')) else 'web'

def _load_spec(body):
    try: value=json.loads(body)
    except Exception: value=yaml.safe_load(body)
    return value if isinstance(value,dict) else {}

def run_openapi_checks(spec_url,body,content_type):
    out=[]
    try: data=_load_spec(body)
    except Exception: return out
    if not ('openapi' in data or 'swagger' in data): return out
    paths=data.get('paths',{}) if isinstance(data.get('paths',{}),dict) else {}
    if not paths:
        out.append(FindingCandidate('FW-API-001','api-inventory','API specification has no paths',Severity.INFO,.95,spec_url,'The published API specification contains no paths.','The documentation may be incomplete or stale.','Keep API inventory synchronized with deployed routes.','No paths entry in published specification.'))
    security_schemes=bool(data.get('components',{}).get('securitySchemes') or data.get('securityDefinitions'))
    for path,item in paths.items():
        if not isinstance(item,dict): continue
        for method,op in item.items():
            m=str(method).lower()
            if m not in HTTP_METHODS or not isinstance(op,dict): continue
            # An explicit security: [] on the operation overrides a secured global declaration.
            explicit_operation_security = 'security' in op
            if explicit_operation_security:
                operation_has_security = bool(op.get('security'))
            else:
                operation_has_security = bool(data.get('security'))
            # A per-operation security: [] explicitly disables a global security
            # requirement and merits review even when schemes are defined.
            if not operation_has_security and (explicit_operation_security or not security_schemes):
                out.append(FindingCandidate('FW-API-002','api-authentication','API operation appears undocumented as authenticated',Severity.MEDIUM,.72,spec_url,f'{m.upper()} {path} has no effective security requirement in the published specification.','Sensitive APIs may be unintentionally exposed, although public operations can be intentional.','Confirm that the endpoint is intended to be public; document and enforce authentication where required.',f'Operation {m.upper()} {path} has no effective security requirement.',evidence={'path':path,'method':m}))
            params=op.get('parameters',[])
            for param in params if isinstance(params,list) else []:
                if not isinstance(param,dict): continue
                name=str(param.get('name',''))
                schema=param.get('schema',{}) if isinstance(param.get('schema',{}),dict) else {}
                if (param.get('in') in {'query','path'} and (schema.get('format')=='uri' or name.lower() in {'url','uri','callback','redirect','webhook','target','destination','next','return_to','return_url','endpoint','domain','host','image_url','avatar_url','logo_url'})):
                    out.append(FindingCandidate('FW-API-003','api-input-validation','URL-like API input requires SSRF/redirect validation review',Severity.INFO,.62,spec_url,f'{m.upper()} {path} defines URL-like parameter `{name}`. This is an inventory-based review candidate only.','If the server fetches or redirects to a user-controlled URL without allow-listing, server-side request risks may exist.','Confirm whether the value triggers server-side fetching; validate scheme, hostname, resolved IP, redirects, and egress policy.',f'OpenAPI declares URL-like parameter {name}.',evidence={'path':path,'method':m,'parameter':name}))
    return out

def run_graphql_observation(url,body):
    if 'graphql' not in url.lower(): return []
    return [FindingCandidate('FW-GQL-001','graphql','GraphQL endpoint discovered',Severity.INFO,.98,url,'A GraphQL endpoint appears to be exposed.','GraphQL deserves dedicated authorization, query-depth/complexity, and introspection review.','Review resolver-level authorization, query complexity limits, rate controls, and introspection policy.',f'GraphQL-like URL discovered: {url}')]

def candidate_api_paths(root):
    from urllib.parse import urljoin
    return [urljoin(root,x) for x in SPEC_PATHS]
