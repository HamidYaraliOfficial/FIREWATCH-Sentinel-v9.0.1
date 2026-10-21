"""Integrity manifest for report bundles.

This is an integrity aid, not a digital signature: anyone able to replace both a
report and its manifest can recompute the checksums. Sign bundles externally when
non-repudiation or tamper evidence across trust boundaries is required.
"""
from __future__ import annotations

from datetime import datetime, timezone
from hashlib import sha256
import re
from typing import Iterable, Mapping
from uuid import UUID

from .version import VERSION

_FORMAT_SUFFIX = {"html": ".html", "json": ".json", "csv": ".csv", "markdown": ".md", "sarif": ".sarif.json"}
_ALLOWED_SUFFIXES = set(_FORMAT_SUFFIX.values())
_SCAN_ID = re.compile(r"^[a-fA-F0-9-]{36}$")

def build_report_manifest(
    scan_id: str,
    reports: Iterable[tuple[str, str, bytes]],
    *,
    generated_at: datetime | None = None,
) -> dict:
    """Build deterministic report file hashes with strict archive path validation."""
    if not isinstance(scan_id, str) or not _SCAN_ID.fullmatch(scan_id):
        raise ValueError("scan_id must be a UUID-shaped identifier")
    try:
        if str(UUID(scan_id)) != scan_id.lower():
            raise ValueError("scan_id must be a canonical UUID")
    except (ValueError, AttributeError) as exc:
        raise ValueError("scan_id must be a canonical UUID") from exc
    items = []
    seen_formats: set[str] = set()
    for report_format, suffix, content in reports:
        if report_format not in {"html", "json", "csv", "markdown", "sarif"}:
            raise ValueError("Unsupported report format")
        if suffix not in _ALLOWED_SUFFIXES or suffix != _FORMAT_SUFFIX[report_format] or not isinstance(content, bytes):
            raise ValueError("Invalid report suffix or content type")
        if report_format in seen_formats:
            raise ValueError("Duplicate report format")
        seen_formats.add(report_format)
        name = f"report{suffix}"
        items.append({
            "format": report_format,
            "path": name,
            "size_bytes": len(content),
            "sha256": sha256(content).hexdigest(),
        })
    if not items:
        raise ValueError("At least one report is required for a bundle manifest")
    moment = generated_at or datetime.now(timezone.utc)
    if not isinstance(moment, datetime) or moment.tzinfo is None or moment.utcoffset() is None:
        raise ValueError("generated_at must be a timezone-aware datetime")
    items.sort(key=lambda item: (item["format"], item["path"]))
    return {
        "schema_version": "1.0",
        "application": "FIREWATCH Sentinel",
        "application_version": VERSION,
        "scan_id": scan_id.lower(),
        "generated_at": moment.astimezone(timezone.utc).isoformat(),
        "hash_algorithm": "sha256",
        "signed": False,
        "reports": items,
        "note": "Checksums detect accidental changes; this manifest is not a cryptographic signature.",
    }


def verify_report_manifest(manifest: Mapping, files: Mapping[str, bytes]) -> list[str]:
    """Verify a parsed manifest against bytes keyed by manifest-relative path.

    Returns human-readable integrity errors. This does not authenticate who created
    the manifest; use a detached digital signature for that threat model.
    """
    errors: list[str] = []
    if not isinstance(manifest, Mapping):
        return ["Manifest must be a JSON object"]
    if manifest.get("schema_version") != "1.0":
        errors.append("Unsupported manifest schema_version")
    if manifest.get("hash_algorithm") != "sha256":
        errors.append("Unsupported manifest hash algorithm")
    entries = manifest.get("reports")
    if not isinstance(entries, list):
        return errors + ["Manifest reports must be a list"]
    if not entries:
        errors.append("Manifest must list at least one report")
    seen_paths: set[str] = set()
    seen_formats: set[str] = set()
    for index, entry in enumerate(entries):
        if not isinstance(entry, Mapping):
            errors.append(f"reports[{index}] must be an object")
            continue
        path, report_format = entry.get("path"), entry.get("format")
        if not isinstance(path, str) or path.startswith("/") or ".." in path.split("/") or "\\" in path:
            errors.append(f"reports[{index}] has an unsafe path")
            continue
        if report_format not in _FORMAT_SUFFIX or path != f"report{_FORMAT_SUFFIX[report_format]}":
            errors.append(f"reports[{index}] has an invalid format/path pair")
            continue
        if path in seen_paths or report_format in seen_formats:
            errors.append(f"reports[{index}] duplicates a path or format")
            continue
        seen_paths.add(path); seen_formats.add(report_format)
        content = files.get(path)
        if not isinstance(content, bytes):
            errors.append(f"Missing report file: {path}")
            continue
        if entry.get("size_bytes") != len(content):
            errors.append(f"Size mismatch: {path}")
        if entry.get("sha256") != sha256(content).hexdigest():
            errors.append(f"SHA-256 mismatch: {path}")
    extra = set(files) - seen_paths
    if extra:
        errors.append("Unlisted files supplied to verifier: " + ", ".join(sorted(extra)))
    return errors
