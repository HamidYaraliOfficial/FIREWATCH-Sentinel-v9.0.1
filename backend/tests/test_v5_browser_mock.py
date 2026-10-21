import asyncio
import sys
import types
from app.browser import BrowserDiscovery
from app.scope import ScopePolicy

class FakeRequest:
    def __init__(self, url, headers=None):
        self.url = url
        self.headers = dict(headers or {})

class FakeRoute:
    def __init__(self, url, headers=None):
        self.request = FakeRequest(url, headers or {'accept': 'text/html', 'cookie': 'browser=old'})
        self.action = None
        self.headers_after = None
    async def continue_(self, headers=None):
        self.action = 'continue'
        self.headers_after = dict(headers or {})
    async def abort(self):
        self.action = 'abort'

class FakeLocator:
    def __init__(self, selector): self.selector = selector
    async def evaluate_all(self, _script):
        if self.selector == 'a[href]':
            return ['/login', 'https://outside.invalid/should-not-appear']
        if self.selector == 'script[src],img[src],link[href],iframe[src]':
            return ['/static/react.js', 'https://api.example.test/schema.js']
        if self.selector == 'form':
            return [{'action':'https://app.example.test/submit','method':'POST','inputs':[{'name':'email','type':'email'}]}]
        return []

class FakePage:
    def __init__(self, raise_on_goto=False):
        self.handlers = {}
        self.route_handler = None
        self.routes = []
        self.raise_on_goto = raise_on_goto
    def on(self, event, callback): self.handlers[event] = callback
    async def route(self, _pattern, handler): self.route_handler = handler
    async def goto(self, url, **_kwargs):
        if self.raise_on_goto: raise RuntimeError('navigation failed')
        request_cb = self.handlers['request']
        for target in [url, 'https://api.example.test/data', 'https://outside.invalid/data']:
            request_cb(FakeRequest(target))
            route = FakeRoute(target)
            self.routes.append(route)
            await self.route_handler(route)
    async def wait_for_timeout(self, _ms): pass
    def locator(self, selector): return FakeLocator(selector)
    async def evaluate(self, _script): return ['accessKey', 'theme']
    async def title(self): return 'Demo'

class FakeContext:
    def __init__(self, page): self.page = page; self.closed = False; self.timeout = None
    async def new_page(self): return self.page
    def set_default_timeout(self, value): self.timeout = value
    async def cookies(self): return [{'name':'session','value':'test-only','httpOnly':True}]
    async def close(self): self.closed = True

class FakeBrowser:
    def __init__(self, context): self.context=context; self.closed=False; self.options=None
    async def new_context(self, **kwargs): self.options=kwargs; return self.context
    async def close(self): self.closed=True

class FakeChromium:
    def __init__(self, browser): self.browser=browser
    async def launch(self, **kwargs): return self.browser

class FakePlaywrightManager:
    def __init__(self, browser): self.browser=browser
    async def __aenter__(self):
        return types.SimpleNamespace(chromium=FakeChromium(self.browser))
    async def __aexit__(self, *_): pass

def install_fake_playwright(monkeypatch, page):
    context=FakeContext(page); browser=FakeBrowser(context)
    package=types.ModuleType('playwright'); package.__path__=[]
    api=types.ModuleType('playwright.async_api')
    api.async_playwright=lambda: FakePlaywrightManager(browser)
    monkeypatch.setitem(sys.modules,'playwright',package)
    monkeypatch.setitem(sys.modules,'playwright.async_api',api)
    monkeypatch.setattr('app.browser.importlib.util.find_spec',lambda name: object() if name=='playwright' else None)
    return browser,context

def test_browser_discovery_filters_links_and_isolates_auth_headers(monkeypatch):
    page=FakePage(); browser,context=install_fake_playwright(monkeypatch,page)
    scope=ScopePolicy.from_root('https://app.example.test/',allow_private_targets=True,allowed_hosts=['api.example.test'])
    result=asyncio.run(BrowserDiscovery(scope,headers={'Authorization':'Bearer top-secret','X-API-Key':'private-key'},delay_ms=0).discover())
    assert result.title=='Demo'
    assert result.links==['https://app.example.test/login']
    assert all('outside.invalid' not in u for u in result.requests+result.resources)
    assert result.storage_keys==['accessKey','theme']
    assert result.forms and result.forms[0]['method']=='POST'
    assert 'React' in result.technologies
    root_route=next(x for x in page.routes if x.request.url=='https://app.example.test/')
    api_route=next(x for x in page.routes if x.request.url=='https://api.example.test/data')
    outside_route=next(x for x in page.routes if x.request.url=='https://outside.invalid/data')
    assert root_route.action=='continue'
    assert root_route.headers_after['authorization']=='Bearer top-secret'
    assert root_route.headers_after['x-api-key']=='private-key'
    assert api_route.action=='continue'
    assert not any(k.lower() in {'authorization','x-api-key','cookie'} for k in api_route.headers_after)
    assert outside_route.action=='abort'
    assert context.closed and browser.closed
    assert context.timeout is not None and browser.options['accept_downloads'] is False

def test_browser_cleanup_runs_when_navigation_errors(monkeypatch):
    page=FakePage(raise_on_goto=True); browser,context=install_fake_playwright(monkeypatch,page)
    scope=ScopePolicy.from_root('https://app.example.test/',allow_private_targets=True)
    try:
        asyncio.run(BrowserDiscovery(scope,delay_ms=0).discover())
    except RuntimeError as exc:
        assert 'navigation failed' in str(exc)
    else:
        raise AssertionError('navigation exception should propagate')
    assert context.closed and browser.closed

def test_browser_module_reports_missing_playwright(monkeypatch):
    monkeypatch.setattr('app.browser.importlib.util.find_spec',lambda _name: None)
    scope=ScopePolicy.from_root('https://app.example.test/',allow_private_targets=True)
    try:
        asyncio.run(BrowserDiscovery(scope).discover())
    except RuntimeError as exc:
        assert 'not installed' in str(exc)
    else:
        raise AssertionError('missing optional dependency should be explicit')
