#!/usr/bin/env python3
"""Lightweight pre-publish checks for accidental secrets and missing release files."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md", "CITATION.cff",
    "backend/app/main.py", "backend/app/scope.py", "backend/app/http_client.py",
    "frontend/index.html", "frontend/static/app.js", ".github/workflows/ci.yml",
]
PRIVATE_KEY = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")
SECRET_VALUE = re.compile(
    r"(?i)(?:api[_-]?key|client[_-]?secret|password)\s*[=:]\s*['\"]?(?!replace-this|change-me|your-|<|\$\{|\s*$)[A-Za-z0-9_./+=-]{16,}"
)
ALLOWED_SUFFIXES = {".py", ".md", ".yml", ".yaml", ".toml", ".json", ".js", ".css", ".html", ".txt", ".cff", ".ini", ".sh", ".bat", ".ps1", ".gitignore", ".gitattributes"}
SKIP_PARTS = {".git", ".pytest_cache", "__pycache__", ".venv", "node_modules", "reports"}


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required release file: {rel}")

    for candidate in ROOT.rglob("*"):
        if not candidate.is_file():
            continue
        rel = candidate.relative_to(ROOT)
        if any(part in SKIP_PARTS for part in rel.parts):
            continue
        if rel.name == ".env" or (rel.name.startswith(".env.") and not rel.name.endswith(".example")):
            errors.append(f"Local environment file must not be committed: {rel}")
            continue
        if rel.suffix.lower() not in ALLOWED_SUFFIXES and rel.name not in {".env.example", ".dockerignore", ".gitignore", ".gitattributes"}:
            continue
        try:
            text = candidate.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if PRIVATE_KEY.search(text):
            errors.append(f"Private-key marker found in: {rel}")
        if rel.name != ".env.example" and SECRET_VALUE.search(text):
            errors.append(f"Potential hard-coded secret assignment found in: {rel}")

    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    if "*.html" in gitignore:
        errors.append(".gitignore must not globally ignore source HTML files")
    if errors:
        print("Repository hygiene FAILED:")
        for error in errors:
            print(f" - {error}")
        return 1
    print("Repository hygiene passed: required files present; no obvious local secrets/private keys found.")
    print("Note: this lightweight check is not a replacement for a dedicated secret scanner.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
