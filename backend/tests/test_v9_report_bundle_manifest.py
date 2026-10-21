"""Integrity manifest contract tests for report bundle exports."""
from datetime import datetime, timezone
from hashlib import sha256
import pytest

from app.bundle_manifest import build_report_manifest, verify_report_manifest
from app.version import VERSION

SCAN = "123e4567-e89b-12d3-a456-426614174000"
STAMP = datetime(2026, 10, 14, 9, 30, tzinfo=timezone.utc)

@pytest.mark.parametrize("size", list(range(0, 128)))
def test_v9_manifest_records_exact_size_and_sha256_for_arbitrary_bytes(size):
    body = bytes((n * 29) % 256 for n in range(size))
    manifest = build_report_manifest(SCAN, [("json", ".json", body)], generated_at=STAMP)
    entry = manifest["reports"][0]
    assert entry["size_bytes"] == len(body)
    assert entry["sha256"] == sha256(body).hexdigest()
    assert len(entry["sha256"]) == 64

@pytest.mark.parametrize("scan_id", [
    "", "../etc/passwd", ".." * 18, "x" * 36, "123e4567-e89b-12d3-a456-42661417400g",
    "/123e4567-e89b-12d3-a456-426614174000", "123e4567-e89b-12d3-a456-426614174000/../x",
])
def test_v9_manifest_rejects_unsafe_scan_identifiers(scan_id):
    with pytest.raises(ValueError):
        build_report_manifest(scan_id, [("json", ".json", b"{}")], generated_at=STAMP)

@pytest.mark.parametrize("fmt,suffix", [
    ("json", ".html"), ("html", ".json"), ("csv", ".md"),
    ("sarif", ".json"), ("markdown", ".html"), ("unknown", ".txt"),
])
def test_v9_manifest_rejects_invalid_format_suffix_pairs(fmt, suffix):
    with pytest.raises(ValueError):
        build_report_manifest(SCAN, [(fmt, suffix, b"payload")], generated_at=STAMP)

@pytest.mark.parametrize("reports", [
    [("json", ".json", b"a"), ("json", ".json", b"b")],
    [("html", ".html", b"a"), ("html", ".html", b"b")],
])
def test_v9_manifest_rejects_duplicate_formats(reports):
    with pytest.raises(ValueError):
        build_report_manifest(SCAN, reports, generated_at=STAMP)

@pytest.mark.parametrize("fmt,suffix", [
    ("html", ".html"), ("json", ".json"), ("csv", ".csv"),
    ("markdown", ".md"), ("sarif", ".sarif.json"),
])
def test_v9_manifest_has_stable_safe_filenames(fmt, suffix):
    manifest = build_report_manifest(SCAN, [(fmt, suffix, b"x")], generated_at=STAMP)
    assert manifest["reports"][0]["path"] == "report" + suffix
    assert "/" not in manifest["reports"][0]["path"]


def test_v9_manifest_output_is_stable_for_fixed_time_and_sorted_by_format():
    reports_a = [("html", ".html", b"H"), ("json", ".json", b"J"), ("csv", ".csv", b"C")]
    reports_b = list(reversed(reports_a))
    a = build_report_manifest(SCAN, reports_a, generated_at=STAMP)
    b = build_report_manifest(SCAN, reports_b, generated_at=STAMP)
    assert a == b
    assert a["application_version"] == VERSION == "9.0.1"
    assert a["signed"] is False


def test_v9_manifest_requires_timezone_aware_timestamp():
    with pytest.raises(ValueError):
        build_report_manifest(SCAN, [("json", ".json", b"{}")], generated_at=datetime(2026, 10, 14))


def test_v9_verifier_accepts_correct_manifest_and_bytes():
    payloads = [("html", ".html", b"<h1>test</h1>"), ("json", ".json", b'{"findings":[]}')]
    manifest = build_report_manifest(SCAN, payloads, generated_at=STAMP)
    files = {f"report{suffix}": content for _, suffix, content in payloads}
    assert verify_report_manifest(manifest, files) == []

@pytest.mark.parametrize("tamper", ["modify", "truncate", "missing", "extra"])
def test_v9_verifier_detects_tampered_missing_or_unlisted_report(tamper):
    body = b"original report"
    manifest = build_report_manifest(SCAN, [("json", ".json", body)], generated_at=STAMP)
    files = {"report.json": body}
    if tamper == "modify": files["report.json"] = b"modified report"
    elif tamper == "truncate": files["report.json"] = b"orig"
    elif tamper == "missing": files = {}
    elif tamper == "extra": files["surprise.txt"] = b"unexpected"
    assert verify_report_manifest(manifest, files)

@pytest.mark.parametrize("mutator", ["unsafe_path", "invalid_digest", "wrong_size", "bad_pair", "duplicate"])
def test_v9_verifier_rejects_malformed_manifest_entries(mutator):
    manifest = build_report_manifest(SCAN, [("json", ".json", b"{}")], generated_at=STAMP)
    if mutator == "unsafe_path": manifest["reports"][0]["path"] = "../report.json"
    elif mutator == "invalid_digest": manifest["reports"][0]["sha256"] = "not-a-digest"
    elif mutator == "wrong_size": manifest["reports"][0]["size_bytes"] = 99
    elif mutator == "bad_pair": manifest["reports"][0]["path"] = "report.html"
    elif mutator == "duplicate": manifest["reports"].append(dict(manifest["reports"][0]))
    assert verify_report_manifest(manifest, {"report.json": b"{}"})


def test_v9_manifest_refuses_empty_report_bundle():
    with pytest.raises(ValueError, match="At least one report"):
        build_report_manifest(SCAN, [], generated_at=STAMP)
