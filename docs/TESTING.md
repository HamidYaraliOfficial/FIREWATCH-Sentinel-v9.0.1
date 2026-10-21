# Testing Guide — FIREWATCH v9.0.1

The v9 regression suite size is generated from pytest collection and recorded in `TEST_MATRIX_V9.md` and `TEST_MANIFEST_V9.json`. The release run executes the complete suite and combined statement-coverage gate. The test count and statement coverage measure software regression coverage, not vulnerability-detection rate.

The complete local regression run passed all 5,948 collected cases across 62 modules; Python statement coverage was 84.53% in a full-suite coverage run. These numbers measure tests and coverage of FIREWATCH's own code. They are not a vulnerability-detection rate and do not prove that a target application is secure.

## Install and run

From the repository root:

```bash
python -m pip install -r backend/requirements-dev.txt
python scripts/build_test_manifest.py
python scripts/run_coverage_shards.py --shards 8 --min-coverage 80
```

To run all tests without coverage instrumentation (typically faster):

```bash
cd backend
PYTHONPATH=. python -m pytest tests -q -rA
```

To inspect a specific module:

```bash
cd backend
PYTHONPATH=. python -m pytest tests/test_v9_config_validation.py tests/test_v9_report_bundle_manifest.py tests/test_v9_dependency_inventory.py tests/test_v9_bundle_verifier_cli.py -q
```

## What is covered

The v9 manifest currently covers **5,948 pytest cases across 62 modules**, including legacy unit and API checks; a local-only end-to-end demo scan; worker lifecycle, leases, stale-worker recovery and cancellation; scope/URL normalization; DNS and IP policy; transport and exact-origin credential isolation; recursive secret redaction; schema and header protocol boundaries; OpenAPI/GraphQL discovery; crawler and JavaScript route heuristics; authorization review candidates; safe, low-impact probe policy; report output sinks (HTML, Markdown, CSV, JSON and SARIF); risk arithmetic; encrypted credential storage; ZAP plan serialization; and API response contracts.

The generated module list and collected counts are in [`TEST_MATRIX_V9.md`](TEST_MATRIX_V9.md) and [`TEST_MANIFEST_V9.json`](TEST_MANIFEST_V9.json). The coverage script balances modules by collected test count and appends coverage data from each shard before enforcing the combined threshold. If the local execution environment has a strict command timeout, split the run into stages; it records collection fingerprints and completed shard IDs:

```bash
python scripts/run_coverage_shards.py --shards 8 --shard-range 1-4 --keep-coverage-data
python scripts/run_coverage_shards.py --shards 8 --shard-range 5-8 --append-coverage --coverage-json /tmp/firewatch-coverage.json
```

The final stage refuses to report complete coverage unless every shard for the same test inventory passed.

## Report-bundle integrity

```bash
python scripts/verify_report_bundle.py path/to/firewatch-scan.zip
```

The verifier checks archive path safety, duplicate ZIP members, the JSON manifest, each report size and digest, and mismatches between archived reports and manifest entries. It does not verify publisher identity because the manifest is intentionally not signed.

## Release verification

```bash
python scripts/verify_release.py
```

This runs compilation and available frontend/shell/YAML/repository checks, regenerates catalogs, then runs the full test/coverage gate. Bandit, `pip-audit`, Docker Engine, Playwright's browser binary, ZAP, hosted GitHub Actions and CodeQL may require installation, network access or an external environment. The verifier marks unavailable optional tools as unverified; it does not call them successful.

## Software tests vs. target assessment

The separate assessment catalog tracks **79 planned target-assessment cases**: 22 passive automated observations, 13 automated review candidates requiring validation, 38 manual/test-account/workflow cases, and 6 specialist-tool-required checks. These are not 79 guaranteed automated exploits. Business logic, BOLA/IDOR, exploitable injection, role-specific behavior and production deployment risks may require a dedicated test application/account and human review.
