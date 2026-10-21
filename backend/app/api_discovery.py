from __future__ import annotations
import json
from dataclasses import dataclass,field
from urllib.parse import urljoin,urlparse
from .checks.api_checks import SPEC_PATHS,run_openapi_checks,run_graphql_observation
from .http_client import SafeHTTPClient, _SAFE_GRAPHQL_INTROSPECTION_QUERY
from .scope import ScopePolicy
from .models import Severity
from .checks.base import FindingCandidate
@dataclass
class APIDiscovery:
    scope:ScopePolicy; delay_ms:int; headers:dict[str,str]=field(default_factory=dict); max_endpoints:int=2000
    async def run(self, passive_only:bool=False):
        assets=[]; findings=[]; specs=[]
        async with SafeHTTPClient(self.scope,delay_ms=self.delay_ms,headers=self.headers) as client:
            parsed=urlparse(self.scope.root_url)
            candidates=[urljoin(self.scope.root_url,x) for x in SPEC_PATHS]
            candidates += [urljoin(self.scope.root_url,'/graphql'),urljoin(self.scope.root_url,'/api/graphql')]
            seen=set()
            for url in candidates:
                if url in seen: continue
                seen.add(url)
                obs=await client.request('GET',url)
                if obs.error or obs.status_code>=500: continue
                if obs.status_code<400:
                    kind='graphql' if 'graphql' in url.lower() or 'graphql' in obs.body[:10000].lower() else 'api-spec' if any(x in obs.body[:1000].lower() for x in ('"openapi"','"swagger"','openapi:','swagger:')) else 'api-candidate'
                    assets.append((url,kind,obs.status_code,obs.content_type,{'headers':obs.headers}))
                    if kind=='api-spec':
                        specs.append(url); findings.extend(run_openapi_checks(url,obs.body,obs.content_type))
                        try:
                            import json, yaml
                            try: spec_data=json.loads(obs.body)
                            except Exception: spec_data=yaml.safe_load(obs.body)
                            paths=spec_data.get('paths',{}) if isinstance(spec_data,dict) else {}
                            for path, path_item in list(paths.items())[:min(self.max_endpoints,2000)]:
                                if not isinstance(path_item,dict): continue
                                for method, operation in path_item.items():
                                    if str(method).lower() not in {'get','post','put','patch','delete','head','options'}: continue
                                    route=self.scope.join(self.scope.root_url,str(path))
                                    if not route: continue
                                    op_meta=operation if isinstance(operation,dict) else {}
                                    assets.append((route,'api-operation-template',None,'application/json',{'method':str(method).upper(),'operation_id':op_meta.get('operationId'),'summary':str(op_meta.get('summary',''))[:300],'auth_declared':bool(op_meta.get('security',spec_data.get('security'))),'parameters':[x.get('name') for x in op_meta.get('parameters',[]) if isinstance(x,dict)][:100]}))
                        except Exception: pass
                    if kind=='graphql': findings.extend(run_graphql_observation(url,obs.body))
            options_candidates=[] if passive_only else [self.scope.root_url]+[x[0] for x in assets if x[1] in {'api-spec','graphql','api-candidate'}]
            for url in list(dict.fromkeys(options_candidates))[:100]:
                obs=await client.request('OPTIONS',url)
                if not obs.error and obs.status_code and any(k in obs.headers for k in ('allow','access-control-allow-origin','access-control-allow-methods')):
                    assets.append((url,'options',obs.status_code,obs.content_type,{'allow':obs.headers.get('allow'),'acao':obs.headers.get('access-control-allow-origin'),'acma':obs.headers.get('access-control-allow-methods')}))
        return assets,findings,specs
    async def graphql_introspection(self,endpoint:str):
        query = _SAFE_GRAPHQL_INTROSPECTION_QUERY
        body = json.dumps({'query':query})
        # A page mentioning GraphQL is not itself a GraphQL endpoint. Skip it
        # without issuing any POST rather than failing the entire assessment.
        endpoint_path = urlparse(endpoint).path.rstrip("/").lower()
        if not endpoint_path or endpoint_path.split("/")[-1] != "graphql":
            return None
        async with SafeHTTPClient(self.scope,delay_ms=self.delay_ms,headers={**self.headers,'Content-Type':'application/json'}) as client:
            obs=await client.request('POST',endpoint,content=body)
        if obs.error: return None
        try: data=json.loads(obs.body)
        except Exception: return None
        return obs,data
