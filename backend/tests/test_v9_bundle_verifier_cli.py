"""ZIP bundle verifier integration and adversarial archive tests."""
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path
import zipfile
import pytest
from app.bundle_manifest import build_report_manifest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("firewatch_bundle_verifier", ROOT / "scripts/verify_report_bundle.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)
SCAN = "123e4567-e89b-12d3-a456-426614174000"
STAMP = datetime(2026, 10, 14, tzinfo=timezone.utc)


def make_bundle(path: Path, *, alter=None):
    payloads = [("json", ".json", b'{"status":"completed"}'), ("html", ".html", b"<html>ok</html>")]
    manifest = build_report_manifest(SCAN, payloads, generated_at=STAMP)
    if alter:
        alter(manifest)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        for fmt, suffix, body in payloads:
            zf.writestr(f"{SCAN}/report{suffix}", body)
        zf.writestr(f"{SCAN}/manifest.json", json.dumps(manifest))
        zf.writestr(f"{SCAN}/manifest.txt", "test bundle\n")
    return path


def test_v9_bundle_verifier_accepts_valid_export(tmp_path):
    path = make_bundle(tmp_path / "bundle.zip")
    assert module.verify_bundle(path) == []

@pytest.mark.parametrize("tamper", ["digest", "size", "path", "wrong_scan", "missing_manifest", "extra_report"])
def test_v9_bundle_verifier_rejects_modified_bundle(tmp_path, tamper):
    path = tmp_path / "bundle.zip"
    if tamper == "missing_manifest":
        with zipfile.ZipFile(path, "w") as zf:
            zf.writestr(f"{SCAN}/report.json", b"{}")
    elif tamper == "extra_report":
        make_bundle(path)
        with zipfile.ZipFile(path, "a") as zf:
            zf.writestr(f"{SCAN}/report.csv", b"unexpected")
    else:
        def mutate(m):
            if tamper == "digest": m["reports"][0]["sha256"] = "0" * 64
            elif tamper == "size": m["reports"][0]["size_bytes"] += 1
            elif tamper == "path": m["reports"][0]["path"] = "../escaped.json"
            elif tamper == "wrong_scan": m["scan_id"] = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
        make_bundle(path, alter=mutate)
    assert module.verify_bundle(path)


def test_v9_bundle_verifier_rejects_duplicate_zip_member_names(tmp_path):
    path = make_bundle(tmp_path / "dup.zip")
    with pytest.warns(UserWarning, match="Duplicate name"):
        with zipfile.ZipFile(path, "a") as zf:
            zf.writestr(f"{SCAN}/report.json", b"replacement")
    assert any("duplicate" in error.lower() for error in module.verify_bundle(path))

@pytest.mark.parametrize("bad_name", ["../evil.txt", "/absolute.txt", "folder\\evil.txt"])
def test_v9_bundle_verifier_rejects_unsafe_zip_paths(tmp_path, bad_name):
    path = tmp_path / "bad-path.zip"
    make_bundle(path)
    with zipfile.ZipFile(path, "a") as zf:
        zf.writestr(bad_name, b"oops")
    assert module.verify_bundle(path)

@pytest.mark.parametrize("value", [b"", b"not a zip", b"PK fake zip"])
def test_v9_bundle_verifier_handles_non_zip_input(tmp_path, value):
    path = tmp_path / "bad.zip"; path.write_bytes(value)
    assert module.verify_bundle(path)
