# Contributing to FIREWATCH

Thanks for helping improve FIREWATCH. Contributions should improve reproducibility, evidence quality, scope safety, documentation, or maintainability.

## Before opening a pull request

1. Read `SECURITY.md` and respect the authorized-testing boundary.
2. Keep automatic checks low-impact by default. Do not add credential guessing, destructive requests, executable exploit chains, or unbounded crawling to the default profile.
3. Add regression tests for scope enforcement, redirects, credential handling, redaction, or rule behavior where relevant.
4. Do not include customer URLs, live credentials, production evidence, local databases, `.env`, or generated reports from real targets.
5. Run the following from the repository root:

   ```bash
   python scripts/repo_hygiene.py
   python -m compileall -q backend/app
   node --check frontend/static/app.js
   cd backend && PYTHONPATH=. python -m pytest -q -rA
   ```

## Rule authoring guidance

A rule should have a stable ID, explicit preconditions, bounded requests, reproducible evidence, a severity rationale, confidence, practical remediation, and references. Distinguish a confirmed observation from a candidate that needs application-specific validation. Avoid saving response bodies or secret values when a short signature/hash is sufficient.

## Pull requests

Use focused changes, explain the security impact, list tests performed, and note any platform/database limitations. Breaking API or schema changes should include migration/backward-compatibility notes.
