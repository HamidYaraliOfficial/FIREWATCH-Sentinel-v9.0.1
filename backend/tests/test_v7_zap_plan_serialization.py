"""YAML serialization safety and strict adapter configuration tests; never launches ZAP."""
from pathlib import Path
import yaml
import pytest
from app.zap import ZAPAdapter

@pytest.mark.parametrize("target", [
    "https://example.test/", "https://example.test/path?x=1", "https://example.test/?q=%0Ajobs%3A%20[]",
    "https://example.test/?q=%23%20YAML-comment", "https://example.test/?q=%7Bfoo%3Abar%7D",
    "https://example.test/path?next=https%3A%2F%2Fevil.test%2F", "https://example.test/a%3A%20value",
    "https://example.test/?query=%22%0Aenv%3A%20evil", "https://example.test/שלום?q=שלום",
])
def test_v7_zap_plan_treats_target_as_yaml_data(tmp_path, target):
    adapter = ZAPAdapter("http://127.0.0.1:8080", str(tmp_path))
    plan = adapter.write_plan(target)
    payload = yaml.safe_load(Path(plan.plan_path).read_text(encoding="utf-8"))
    context = payload["env"]["contexts"][0]
    assert context["urls"] == [target]
    assert context["includePaths"] == [target + ".*"]
    assert len(payload["jobs"]) == 1
    assert payload["jobs"][0]["type"] == "passiveScan-wait"

@pytest.mark.parametrize("base", [
    "", "relative", "ftp://zap.example", "javascript:alert(1)", "http://user:pass@127.0.0.1:8080",
    "http://127.0.0.1:99999", "http://127.0.0.1:0", "http://127.0.0.1:8080/?x=1",
    "http://127.0.0.1:8080/#frag", "//127.0.0.1:8080", "data:text/plain,x",
])
def test_v7_zap_adapter_rejects_invalid_base_urls(tmp_path, base):
    with pytest.raises(ValueError):
        ZAPAdapter(base, str(tmp_path))

def test_v7_zap_plan_contains_only_passive_wait_job(tmp_path):
    adapter = ZAPAdapter("http://127.0.0.1:8080", str(tmp_path))
    plan = adapter.write_plan("https://example.test/")
    payload = yaml.safe_load(Path(plan.plan_path).read_text())
    assert all(job["type"] == "passiveScan-wait" for job in payload["jobs"])
    assert "activeScan" not in Path(plan.plan_path).read_text()
