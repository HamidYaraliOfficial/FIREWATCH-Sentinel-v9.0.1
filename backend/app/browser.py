from __future__ import annotations

from dataclasses import dataclass, field
import asyncio
import importlib.util
import time
from urllib.parse import urlparse

from .config import settings
from .http_client import _is_credential_header, credentials_allowed_for_root_origin
from .scope import ScopePolicy


@dataclass
class BrowserResult:
    url: str
    links: list[str]
    resources: list[str]
    title: str | None
    technologies: list[str]
    requests: list[str] = field(default_factory=list)
    cookies: list[dict] = field(default_factory=list)
    storage_keys: list[str] = field(default_factory=list)
    forms: list[dict] = field(default_factory=list)


class BrowserDiscovery:
    """Read-only browser discovery with per-request scope and credential guards."""

    def __init__(self, scope: ScopePolicy, headers: dict[str, str] | None = None,
                 delay_ms: int | None = None):
        self.scope = scope
        self.headers = dict(headers or {})
        root = urlparse(scope.root_url)
        self.root_host = (root.hostname or "").lower().rstrip(".")
        self.root_scheme = root.scheme.lower()
        self.root_port = root.port or (443 if self.root_scheme == "https" else 80)
        self.delay_ms = settings.request_delay_ms if delay_ms is None else max(0, int(delay_ms))
        self._last_request = 0.0
        self._throttle_lock = asyncio.Lock()

    async def _throttle(self):
        delay = self.delay_ms / 1000.0
        if not self.scope.allow_private_targets:
            delay = max(delay, 0.05)
        async with self._throttle_lock:
            elapsed = time.monotonic() - self._last_request
            if elapsed < delay:
                await asyncio.sleep(delay - elapsed)
            self._last_request = time.monotonic()

    async def discover(self) -> BrowserResult:
        if importlib.util.find_spec("playwright") is None:
            raise RuntimeError("Playwright is not installed")
        from playwright.async_api import async_playwright

        requests: list[str] = []
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=True)
            context = None
            try:
                # Do not put credentials in context-wide extra_http_headers: those are
                # sent with every navigation/resource request, including other origins.
                context = await browser.new_context(
                    ignore_https_errors=False,
                    user_agent=settings.user_agent,
                    accept_downloads=False,
                    service_workers="block",
                )
                context.set_default_timeout(int(settings.browser_timeout_seconds * 1000))
                page = await context.new_page()

                def record(req):
                    try:
                        if self.scope.is_allowed(req.url):
                            requests.append(req.url)
                    except Exception:
                        pass

                page.on("request", record)

                async def guard(route):
                    url = route.request.url
                    scheme = urlparse(url).scheme.lower()
                    if scheme in {"data", "blob", "about"}:
                        await route.continue_()
                        return
                    try:
                        self.scope.validate_url(url)
                    except Exception:
                        await route.abort()
                        return
                    await self._throttle()
                    # Restrict credentials to the exact root origin (scheme, host, port).
                    credentials_allowed = credentials_allowed_for_root_origin(
                        self.scope.root_url, url, self.scope.allow_private_targets
                    )
                    headers = dict(route.request.headers)
                    if credentials_allowed:
                        for key, value in self.headers.items():
                            low = key.lower()
                            if low not in {"host", "content-length", "transfer-encoding", "connection", "proxy-authorization"}:
                                headers[low] = str(value)
                    else:
                        # Remove configured credentials and browser cookies when crossing
                        # an origin or when the request would downgrade the root scheme.
                        headers = {k: v for k, v in headers.items() if not _is_credential_header(k)}
                    await route.continue_(headers=headers)

                await page.route("**/*", guard)
                await page.goto(
                    self.scope.root_url,
                    wait_until="domcontentloaded",
                    timeout=int(settings.browser_timeout_seconds * 1000),
                )
                await page.wait_for_timeout(400)
                links = await page.locator("a[href]").evaluate_all("els => els.map(e => e.href)")
                resources = await page.locator("script[src],img[src],link[href],iframe[src]").evaluate_all(
                    "els => els.map(e => e.src || e.href)"
                )
                forms = await page.locator("form").evaluate_all(
                    "forms => forms.map(f => ({action:f.action,method:(f.method||'GET').toUpperCase(),inputs:[...f.querySelectorAll('input,textarea,select,button')].map(i=>({name:i.name,type:i.type}))}))"
                )
                safe_links = [x for x in (self.scope.join(self.scope.root_url, u) for u in links) if x]
                safe_resources = [x for x in (self.scope.join(self.scope.root_url, u) for u in resources) if x]
                safe_requests = [x for x in requests if self.scope.is_allowed(x)]
                storage = await page.evaluate("() => [...Object.keys(localStorage), ...Object.keys(sessionStorage)]")
                cookies = await context.cookies()
                scripts = " ".join(safe_resources + safe_requests)
                tech = []
                if "/_next/" in scripts:
                    tech.append("Next.js")
                if "react" in scripts.lower():
                    tech.append("React")
                if "vue" in scripts.lower():
                    tech.append("Vue")
                return BrowserResult(
                    self.scope.root_url,
                    list(dict.fromkeys(safe_links))[:1000],
                    list(dict.fromkeys(safe_resources))[:1000],
                    await page.title(), sorted(set(tech)),
                    list(dict.fromkeys(safe_requests))[:2000], cookies[:200],
                    sorted(set(storage))[:500], forms[:200],
                )
            finally:
                if context is not None:
                    await context.close()
                await browser.close()
