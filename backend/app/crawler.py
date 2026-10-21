from __future__ import annotations
import re, asyncio
from collections import deque
from dataclasses import dataclass,field
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
from bs4 import BeautifulSoup
from .config import settings
from .http_client import HTTPObservation,SafeHTTPClient
from .scope import ScopePolicy
@dataclass
class PageSnapshot:
    url:str; depth:int; observation:HTTPObservation; title:str|None; links:list[str]; forms:list[dict]; resources:list[str]; technologies:list[str]; mixed_content:list[str]=field(default_factory=list); js_endpoints:list[str]=field(default_factory=list); meta:dict=field(default_factory=dict)
class Crawler:
    def __init__(self, scope, max_pages, max_depth, delay_ms, respect_robots=True,
                 max_endpoints=2000, headers=None, max_concurrency=None, cancel_check=None):
        self.scope = scope
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.delay_ms = delay_ms
        self.respect_robots = respect_robots
        self.max_endpoints = max_endpoints
        self.headers = headers or {}
        self.max_concurrency = max(1, min(int(max_concurrency or settings.max_concurrency), 20))
        self.cancel_check = cancel_check or (lambda: False)
    async def crawl(self,seed_urls:list[str]|None=None)->list[PageSnapshot]:
        snapshots=[]
        initial=[(self.scope.root_url,0)]+[(u,1) for u in (seed_urls or []) if self.scope.is_allowed(u)]
        queue=deque(); queued=set()
        for url,depth in initial:
            if url not in queued and len(queued)<self.max_endpoints:
                queue.append((url,depth)); queued.add(url)
        visited=set(); robots=await self._load_robots() if self.respect_robots else None
        async with SafeHTTPClient(self.scope,delay_ms=self.delay_ms,headers=self.headers) as client:
            while queue and len(snapshots)<self.max_pages and len(visited)<self.max_endpoints:
                if self.cancel_check():
                    break
                batch=[]
                while queue and len(batch)<self.max_concurrency:
                    url,depth=queue.popleft(); queued.discard(url)
                    if url in visited or depth>self.max_depth: continue
                    if len(visited)>=self.max_endpoints: break
                    if robots is not None and not robots.can_fetch(settings.user_agent,url): continue
                    visited.add(url); batch.append((url,depth))
                if not batch: continue
                results=await asyncio.gather(*(client.request('GET',u) for u,_ in batch))
                if self.cancel_check():
                    break
                for (url,depth),obs in zip(batch,results):
                    if self.cancel_check():
                        break
                    if obs.error: continue
                    snap=self._snapshot(url,depth,obs); snapshots.append(snap)
                    if depth>=self.max_depth or not (self._is_html(obs.content_type) or 'javascript' in obs.content_type.lower() or urlparse(url).path.lower().endswith(('.js','.mjs'))): continue
                    for link in snap.links+snap.resources+snap.js_endpoints:
                        if len(visited)+len(queued)>=self.max_endpoints: break
                        if link not in visited and link not in queued and self.scope.is_allowed(link):
                            queue.append((link,depth+1)); queued.add(link)
                    if len(snapshots)>=self.max_pages: break
        return snapshots
    async def _load_robots(self):
        p=urlparse(self.scope.root_url); robots_url=f'{p.scheme}://{p.netloc}/robots.txt'
        try:
            async with SafeHTTPClient(self.scope,delay_ms=self.delay_ms,headers=self.headers) as client: obs=await client.request('GET',robots_url)
            if obs.error or obs.status_code>=400: return None
            rp=RobotFileParser(); rp.set_url(robots_url); rp.parse(obs.body.splitlines()); return rp
        except Exception: return None
    async def discover_sitemaps(self)->list[str]:
        """Discover bounded sitemap URLs from robots.txt and common sitemap paths."""
        p=urlparse(self.scope.root_url); origin=f'{p.scheme}://{p.netloc}'; sitemap_docs=[f'{origin}/sitemap.xml',f'{origin}/sitemap_index.xml']; discovered=set(); visited=set()
        async with SafeHTTPClient(self.scope,delay_ms=self.delay_ms,headers=self.headers) as client:
            robots=await client.request('GET',f'{origin}/robots.txt')
            if not robots.error and robots.status_code<400:
                for line in robots.body.splitlines():
                    if line.strip().lower().startswith('sitemap:'):
                        item=self.scope.join(self.scope.root_url,line.split(':',1)[1].strip())
                        if item: sitemap_docs.append(item)
            queue=deque(sitemap_docs)
            while queue and len(visited)<20 and len(discovered)<self.max_endpoints:
                if self.cancel_check():
                    break
                u=queue.popleft()
                if u in visited or not self.scope.is_allowed(u): continue
                visited.add(u); obs=await client.request('GET',u)
                if obs.error or obs.status_code>=400 or not ('xml' in obs.content_type.lower() or '<urlset' in obs.body[:2000].lower() or '<sitemapindex' in obs.body[:2000].lower()): continue
                locs=re.findall(r'<loc>\s*([^<]+?)\s*</loc>',obs.body,flags=re.I)
                for value in locs:
                    target=self.scope.join(u,value.strip())
                    if not target: continue
                    parsed=urlparse(target)
                    if parsed.path.lower().endswith('.xml') or 'sitemap' in parsed.path.lower():
                        if target not in visited and len(queue)<20: queue.append(target)
                    else: discovered.add(target)
                    if len(discovered)>=self.max_endpoints: break
        return sorted(discovered)[:self.max_endpoints]
    @staticmethod
    def _is_html(ct): return 'text/html' in ct.lower() or 'application/xhtml+xml' in ct.lower()
    def _snapshot(self,url,depth,obs):
        links=[];resources=[];forms=[];mixed=[];js_endpoints=[];title=None;tech=self._fingerprint(obs.headers,obs.body)
        if self._is_html(obs.content_type):
            soup=BeautifulSoup(obs.body,'html.parser'); title=soup.title.get_text(strip=True)[:500] if soup.title else None
            for tag in soup.find_all(['a','area']):
                v=tag.get('href'); safe=self.scope.join(url,v) if v else None
                if safe: links.append(safe); mixed += [safe] if url.startswith('https://') and safe.startswith('http://') else []
            for tag in soup.find_all(['script','img','link','iframe','source']):
                attr='src' if tag.name in {'script','img','iframe','source'} else 'href'; v=tag.get(attr); safe=self.scope.join(url,v) if v else None
                if safe: resources.append(safe)
                if v and v.startswith('http://') and url.startswith('https://'): mixed.append(v)
            for form in soup.find_all('form'):
                action=self.scope.join(url,form.get('action') or url) or url; method=(form.get('method') or 'GET').upper(); inputs=[]
                for inp in form.find_all(['input','textarea','select','button']): inputs.append({'name':inp.get('name'),'type':inp.get('type'),'value_present':inp.get('value') is not None})
                forms.append({'action':action,'method':method,'inputs':inputs})
            js_endpoints=self._extract_js_endpoints(obs.body)
        elif 'javascript' in obs.content_type.lower() or urlparse(url).path.lower().endswith(('.js','.mjs')):
            js_endpoints=self._extract_js_endpoints(obs.body)
        return PageSnapshot(url,depth,obs,title,list(dict.fromkeys(links))[:1000],forms[:200],list(dict.fromkeys(resources))[:1000],sorted(set(tech)),list(dict.fromkeys(mixed))[:100],list(dict.fromkeys(js_endpoints))[:500],{'cache_control':obs.headers.get('cache-control'),'content_length':len(obs.body),'server':obs.headers.get('server')})
    def _extract_js_endpoints(self,body):
        found=set(); patterns=[r'["\']((?:https?://|/)[^"\']{2,300})["\']',r'fetch\(\s*["\']([^"\']+)["\']',r'axios\.(?:get|post|put|delete|patch)\(\s*["\']([^"\']+)["\']']
        for pattern in patterns:
            for m in re.findall(pattern,body,flags=re.I):
                c=m[0] if isinstance(m,tuple) else m; safe=self.scope.join(self.scope.root_url,c)
                if safe and any(t in c.lower() for t in ('/api','/graphql','/v1/','/v2/','/auth','/login','/users','/admin')): found.add(safe)
        return sorted(found)
    def _fingerprint(self,headers,body):
        h={k.lower():v.lower() for k,v in headers.items()}; out=[]; server=h.get('server',''); powered=h.get('x-powered-by',''); body_low=(body or '').lower()
        for token,name in [('nginx','Nginx'),('apache','Apache'),('iis','IIS')]:
            if token in server: out.append(name)
        if 'uvicorn' in server or 'starlette' in powered: out.append('FastAPI/Starlette')
        if 'express' in powered: out.append('Express')
        if 'php' in powered or '.php' in body_low or '<?php' in body_low: out.append('PHP')
        if '__next_data__' in body_low or '/_next/' in body_low: out.append('Next.js')
        if 'wp-content' in body_low: out.append('WordPress')
        return sorted(set(out))
