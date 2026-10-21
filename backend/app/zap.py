from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit
import json
import urllib.request
import yaml


@dataclass(frozen=True)
class ZAPPlan:
    target_url: str
    plan_path: str


class ZAPAdapter:
    """Bounded adapter for ZAP's passive Automation Framework plan.

    The adapter generates a YAML data document rather than interpolating the URL
    into YAML source. It does not execute arbitrary commands from target content.
    Active ZAP jobs are intentionally not enabled by this adapter.
    """

    def __init__(self, base_url: str, workdir: str = "./reports/zap"):
        parsed = urlsplit(str(base_url).strip())
        if parsed.scheme.lower() not in {"http", "https"} or not parsed.hostname:
            raise ValueError("ZAP base URL must be an absolute HTTP(S) URL")
        if parsed.username is not None or parsed.password is not None:
            raise ValueError("Credentials embedded in ZAP base URL are forbidden")
        if parsed.query or parsed.fragment:
            raise ValueError("ZAP base URL must not include a query or fragment")
        try:
            port = parsed.port
        except ValueError as exc:
            raise ValueError("ZAP base URL has an invalid port") from exc
        if port == 0:
            raise ValueError("ZAP base URL port must be between 1 and 65535")
        self.base_url = str(base_url).rstrip("/")
        self.workdir = Path(workdir)
        self.workdir.mkdir(parents=True, exist_ok=True)

    def write_plan(self, target_url: str) -> ZAPPlan:
        # Never construct YAML by string interpolation: a URL can contain syntax
        # that is meaningful in YAML even when it is a valid URL.
        payload = {
            "env": {"contexts": [{
                "name": "FIREWATCH",
                "urls": [target_url],
                "includePaths": [target_url + ".*"],
                "excludePaths": [],
            }]},
            "jobs": [{"type": "passiveScan-wait", "parameters": {"maxDuration": 10}}],
        }
        path = self.workdir / "automation.yaml"
        path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")
        return ZAPPlan(target_url, str(path))

    def health(self) -> bool:
        try:
            with urllib.request.urlopen(self.base_url + "/JSON/core/view/version/", timeout=3) as resp:
                payload = json.load(resp)
                return bool(payload.get("version"))
        except Exception:
            return False
