#!/usr/bin/env python3
"""Export declared requirements and constraints as a deterministic inventory.

This intentionally does not call itself an SBOM: version ranges may not be resolved,
transitive dependencies are not fully expanded, and no vulnerability audit is run.
"""
from __future__ import annotations
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
NAME_RE = re.compile(r"^([A-Za-z0-9][A-Za-z0-9._-]*)(\[[^\]]+\])?\s*(.*?)\s*$")
CONSTRAINT_RE = re.compile(r"^(?:(?:===|==|!=|~=|<=|>=|<|>)\s*[A-Za-z0-9.*_+!-]+)(?:\s*,\s*(?:===|==|!=|~=|<=|>=|<|>)\s*[A-Za-z0-9.*_+!-]+)*$")


def normalize_name(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def parse_requirements(paths: list[Path], root: Path = ROOT) -> list[dict]:
    components: dict[tuple[str, str, str], dict] = {}
    visiting: set[Path] = set()

    def walk(path: Path):
        resolved = path.resolve()
        try:
            resolved.relative_to(root.resolve())
        except ValueError as exc:
            raise ValueError("Requirement includes must remain inside the repository") from exc
        if resolved in visiting:
            raise ValueError("Recursive requirements include cycle detected")
        if not resolved.is_file():
            raise ValueError(f"Requirements file does not exist: {resolved.relative_to(root.resolve())}")
        visiting.add(resolved)
        source = resolved.relative_to(root.resolve()).as_posix()
        for number, original in enumerate(resolved.read_text(encoding="utf-8").splitlines(), 1):
            line = original.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith(("-r ", "--requirement ")):
                include = line.split(None, 1)[1].strip()
                walk(resolved.parent / include)
                continue
            if line.startswith(("-", "git+", "https://", "http://", "file:")):
                raise ValueError(f"Unsupported requirement directive at {source}:{number}")
            # Strip only conventional inline comments, not URL fragments (URL specs are rejected above).
            line = line.split(" #", 1)[0].strip()
            main, marker_sep, marker = line.partition(";")
            match = NAME_RE.fullmatch(main.strip())
            if not match:
                raise ValueError(f"Cannot parse requirement at {source}:{number}")
            name, extras, constraint = match.groups()
            name = name.strip()
            extras_value = (extras or "").strip("[]")
            constraint = constraint.strip()
            if constraint and not CONSTRAINT_RE.fullmatch(constraint):
                raise ValueError(f"Invalid version constraint at {source}:{number}")
            key = (normalize_name(name), constraint, marker.strip() if marker_sep else "")
            entry = components.setdefault(key, {
                "name": name, "normalized_name": normalize_name(name),
                "extras": sorted(x.strip() for x in extras_value.split(",") if x.strip()),
                "version_constraint": constraint or "unspecified",
                "environment_marker": marker.strip() if marker_sep else None,
                "source_files": [], "resolution_status": "declared_constraint_not_resolved",
            })
            if source not in entry["source_files"]:
                entry["source_files"].append(source)
        visiting.remove(resolved)

    for path in paths:
        walk(path)
    result = list(components.values())
    for item in result:
        item["source_files"].sort()
    return sorted(result, key=lambda item: (item["normalized_name"], item["version_constraint"], item["environment_marker"] or ""))


def generate_inventory(root: Path = ROOT) -> dict:
    requirements = [root / "backend/requirements.txt", root / "backend/requirements-dev.txt"]
    components = parse_requirements(requirements, root=root)
    return {
        "inventory_schema": "firewatch.declared-dependency-inventory.v1",
        "application": "FIREWATCH Sentinel",
        "application_version": (root / "VERSION").read_text(encoding="utf-8").strip(),
        "python_requires": ">=3.11",
        "source_files": ["backend/requirements.txt", "backend/requirements-dev.txt"],
        "component_count": len(components),
        "components": components,
        "limitations": [
            "This is a declared-requirements inventory, not a resolved SBOM.",
            "Constraint ranges are not resolved to installed artifact versions.",
            "Transitive dependency closure and vulnerability status are not implied.",
            "Run pip-audit in a trusted environment with package index access before release/deployment.",
        ],
    }


def main() -> int:
    inventory = generate_inventory(ROOT)
    json_path = ROOT / "docs" / f"DEPENDENCY_INVENTORY_V{VERSION.split('.')[0]}.json"
    md_path = ROOT / "docs" / f"DEPENDENCY_INVENTORY_V{VERSION.split('.')[0]}.md"
    json_path.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [f"# FIREWATCH v{VERSION} — Declared Dependency Inventory", "",
             f"Declared entries: **{inventory['component_count']}**", "",
             "> This inventory is not a resolved SBOM and is not a vulnerability audit.", "",
             "| Package | Extras | Declared constraint | Marker | Requirement files |", "|---|---|---|---|---|"]
    for item in inventory["components"]:
        extras = ", ".join(item["extras"]) or "—"
        marker = item["environment_marker"] or "—"
        sources = ", ".join(item["source_files"])
        lines.append(f"| `{item['name']}` | {extras} | `{item['version_constraint']}` | `{marker}` | `{sources}` |")
    lines += ["", "## Limitations", ""] + [f"- {item}" for item in inventory["limitations"]] + [""]
    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated {json_path.relative_to(ROOT)} and {md_path.relative_to(ROOT)} ({inventory['component_count']} declared entries).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
