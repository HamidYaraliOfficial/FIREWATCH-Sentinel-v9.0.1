#!/usr/bin/env python3
"""Verify integrity manifests in FIREWATCH report ZIP bundles."""
from __future__ import annotations
import json
import sys
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
from app.bundle_manifest import verify_report_manifest  # noqa: E402


def verify_bundle(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        archive = zipfile.ZipFile(path, "r")
    except (OSError, zipfile.BadZipFile) as exc:
        return [f"Not a readable ZIP bundle: {type(exc).__name__}"]
    with archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            errors.append("Archive contains duplicate member names")
        for name in names:
            parsed = PurePosixPath(name)
            if parsed.is_absolute() or ".." in parsed.parts or "\\" in name or name.startswith("/"):
                errors.append(f"Unsafe archive path: {name}")
        if errors:
            return errors
        manifests = [name for name in names if name.endswith("/manifest.json")]
        if len(manifests) != 1:
            return ["Bundle must contain exactly one <scan-id>/manifest.json"]
        manifest_path = manifests[0]
        prefix = manifest_path.split("/", 1)[0]
        try:
            manifest = json.loads(archive.read(manifest_path))
        except (KeyError, json.JSONDecodeError, UnicodeDecodeError):
            return ["Bundle manifest.json is missing or invalid JSON"]
        if not isinstance(manifest, dict):
            return ["Manifest must be a JSON object"]
        if manifest.get("scan_id") != prefix:
            errors.append("Manifest scan_id does not match the archive directory")
        report_entries = manifest.get("reports")
        if not isinstance(report_entries, list):
            return errors + ["Manifest reports member must be a list"]
        file_bytes = {}
        expected_archive_names = set()
        for item in report_entries:
            if not isinstance(item, dict) or not isinstance(item.get("path"), str):
                errors.append("Malformed report entry in manifest")
                continue
            rel_path = item["path"]
            parsed = PurePosixPath(rel_path)
            if parsed.is_absolute() or len(parsed.parts) != 1 or ".." in parsed.parts or "\\" in rel_path:
                errors.append(f"Unsafe manifest report path: {rel_path}")
                continue
            arc_name = f"{prefix}/{rel_path}"
            expected_archive_names.add(arc_name)
            if arc_name in names:
                file_bytes[rel_path] = archive.read(arc_name)
        actual_reports = {name for name in names if name.startswith(prefix + "/report")}
        if actual_reports != expected_archive_names:
            errors.append("Archive report files do not match the manifest file list")
        errors.extend(verify_report_manifest(manifest, file_bytes))
    return errors


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 1:
        print("Usage: python scripts/verify_report_bundle.py <bundle.zip>", file=sys.stderr)
        return 2
    errors = verify_bundle(Path(args[0]))
    if errors:
        print("Report bundle verification FAILED:")
        for error in errors:
            print(f" - {error}")
        return 1
    print("Report bundle manifest verified: file paths, byte sizes and SHA-256 digests match.")
    print("Note: this verifies integrity against the included manifest, not publisher authenticity.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
