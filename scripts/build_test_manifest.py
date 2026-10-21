#!/usr/bin/env python3
"""Collect pytest tests and generate the release-versioned automated test inventory."""
from __future__ import annotations
import json, re, subprocess, sys
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "backend"
DOCS = ROOT / "docs"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
MAJOR = VERSION.split(".")[0]
MANIFEST_PATH = DOCS / f"TEST_MANIFEST_V{MAJOR}.json"
MATRIX_PATH = DOCS / f"TEST_MATRIX_V{MAJOR}.md"
DESCRIPTIONS = {
    "test_standards_checklist_api.py": "Standards registry counts and mapping integrity, project-scoped checklist API, evidence/status validation, audit history, safe CSV export and Excel workbook/API download contracts",
    "test_v9_coverage_runner.py": "Deterministic coverage shard allocation, validation of inclusive shard ranges, stable grouping and staged-run safety contracts",
    "test_v10_network_and_readonly_policy.py": "Socket-level DNS pinning, mixed/private DNS answer rejection, default transport wiring, bounded read-only GraphQL introspection and pre-network rejection of mutating HTTP methods",
    "test_v11_worker_leases.py": "External and inline worker lease heartbeat ownership, stale RUNNING scan recovery, recovery audit events and terminal-state fencing",
    "test_v9_config_validation.py": "Startup configuration safety: production guardrails, resource bounds, CORS origins, ZAP origin, user-agent and explicit secret-key validation",
    "test_v9_report_bundle_manifest.py": "Report bundle manifest size/digest contracts, safe archive paths, deterministic serialization and tamper detection",
    "test_v9_dependency_inventory.py": "Declared dependency inventory parser, package-name normalization, recursive include/cycle/path safety and limitations",
    "test_v9_bundle_verifier_cli.py": "End-to-end ZIP report bundle verification, tampering, duplicate entries and archive path traversal resistance",
    "test_v7_scope_adversarial_properties.py": "Encoded path exclusions, exact ports, hostile URL forms and scope joins",
    "test_v7_redaction_properties.py": "Sensitive field/query normalization, recursive URL decoding and benign-value invariants",
    "test_v7_openapi_contract_matrix.py": "OpenAPI effective auth declarations, URL-like parameters, API classification and GraphQL inventory",
    "test_v7_report_sink_matrix.py": "HTML/Markdown injection resistance, CSV formula safety, JSON/SARIF schema contracts",
    "test_v7_transport_boundary_matrix.py": "Exact-origin credential isolation, forbidden transport headers and redirect non-following",
    "test_v7_crawler_inventory_matrix.py": "Synthetic HTML, links, forms, JS routes, scope limits and technology fingerprints",
    "test_v7_zap_plan_serialization.py": "YAML serialization without injection and malformed ZAP endpoint rejection",
    "test_v7_schema_boundary_fuzz.py": "Input bounds, header injection variants, profiles and configuration limits",
    "test_v7_authorization_readonly_matrix.py": "Read-only role comparisons, authorization candidates, scope enforcement and request-body invariants",
    "test_v7_parameter_probe_policy_matrix.py": "Non-sensitive parameter selection, request limits, and benign GET canary policy",
    "test_v8_header_protocol_hardening.py": "RFC token header names, case-insensitive duplicate rejection, value controls and authorization-profile boundaries",
    "test_v8_scope_fuzz_and_normalization.py": "Scheme/port/host scope cross product, case-folded exclusions, encoded path traversal, secret-bearing root refusal and unsafe IP classes",
    "test_v8_risk_and_status_contracts.py": "Exhaustive confidence/risk arithmetic and enum/status invariants",
    "test_v8_redaction_property_matrix.py": "Encoded credential values, nested return URLs, structured data redaction and benign-value preservation",
    "test_v8_report_output_contracts.py": "Cross-format HTML/Markdown/CSV/JSON/SARIF sink tests and attacker-controlled content handling",
    "test_v8_schema_limits_and_config_matrix.py": "Schema boundary values, profiles, target URL refusal, list limits and notes fields",
    "test_v8_crawler_parser_regression_matrix.py": "Malformed/hostile HTML parser robustness, JavaScript routes and technology fingerprints",
    "test_v8_api_discovery_contract_matrix.py": "API/GraphQL classification, OpenAPI URL-like input inventory and catalog reconciliation",
    "test_v8_secret_store_contracts.py": "Encrypted-at-rest credentials, key-file permissions, wrong-key behavior and public masking",
    "test_v8_credential_header_isolation_matrix.py": "Cross-origin credential header policy and transport-header exclusions",
    "test_v8_http_policy_boundaries.py": "No-network-on-invalid-scope, redirect non-following and read-only method request contracts",
    "test_api.py": "API health/readiness, security headers, evidence and report bundles",
    "test_integration.py": "Local-only end-to-end demo scan and report generation",
    "test_v6_scope_fuzz_matrix.py": "Inherited adversarial URL, nested encoding, ports, scope joins and exclusions",
    "test_v6_redaction_fuzz_matrix.py": "Inherited registered sensitive field/query names and recursive redaction matrix",
    "test_v6_risk_math_matrix.py": "Fine-grained severity/confidence risk scoring invariants",
    "test_v6_schema_hardening_matrix.py": "Boundary values, header injection and authorization profile schema checks",
    "test_v6_origin_credential_isolation.py": "Exact-origin credential isolation and same-host different-port regressions",
    "test_v6_catalog_report_contract.py": "Assessment/check catalog contracts and all report formats",
    "test_v6_http_method_and_redirect_matrix.py": "HTTP method, no-follow redirect and pre-network scope enforcement",
    "test_v6_rule_behavior_matrix.py": "Parameterized behavior checks for registered passive and low-impact rules",
    "test_v6_config_parser_matrix.py": "Environment configuration parser boundary and malformed-value handling",
}
def main() -> int:
    cmd=[sys.executable,"-m","pytest","--collect-only","-q","-o","addopts=","tests"]
    result=subprocess.run(cmd,cwd=BACKEND,capture_output=True,text=True)
    if result.returncode:
        print(result.stdout); print(result.stderr,file=sys.stderr); return result.returncode
    counts: Counter[str]=Counter()
    for line in (result.stdout+"\n"+result.stderr).splitlines():
        match=re.match(r"tests/(test_[^:]+\.py)::",line.strip())
        if match: counts[match.group(1)]+=1
    total=sum(counts.values())
    if total<1:
        print("Could not parse pytest collection output",file=sys.stderr); return 2
    payload={"release_version":VERSION,"test_count":total,"module_count":len(counts),
      "collection_command":"python -m pytest --collect-only -q -o addopts= tests (from backend/)",
      "modules":[{"file":name,"count":count,"focus":DESCRIPTIONS.get(name,"Unit, matrix, integration, and regression tests")} for name,count in sorted(counts.items())],
      "interpretation":"Software regression tests and code coverage are not a percentage of vulnerabilities detected."}
    MANIFEST_PATH.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    lines=[f"# FIREWATCH v{MAJOR} — Automated Test Matrix","",f"Release: `{VERSION}`  ",f"Collected tests: **{total}** across **{len(counts)}** test modules.","",
      "> This manifest is generated from pytest collection. Software test count and statement coverage are not the percentage of vulnerabilities found and do not prove that any target is secure.","",
      "## Suite inventory","","| Test module | Collected cases | Focus |","|---|---:|---|"]
    for item in payload["modules"]:
        focus = item["focus"].replace("|", "\\|")
        lines.append(f"| `{item['file']}` | {item['count']} | {focus} |")
    lines += ["",f"| **Total** | **{total}** | All collected unit, matrix, regression, API and local demo tests |","","## Reproduce collection and run the suite","","```bash",
      "python -m pip install -r backend/requirements-dev.txt","python scripts/build_test_manifest.py","cd backend",
      "python scripts/run_coverage_shards.py --shards 8 --min-coverage 80","```","",
      "## Separate target assessment catalog","",
      "The 79-item assessment plan is separate from software regression tests. It labels cases requiring manual workflows, test accounts or specialist tools; those are not represented as automatically executed.",
      "See `ASSESSMENT_CATALOG.md`, `assessment-plan-v{MAJOR}.json`, and `assessment-plan-v{MAJOR}.csv`.",""]
    MATRIX_PATH.write_text("\n".join(lines),encoding="utf-8")
    print(f"Generated {MANIFEST_PATH.relative_to(ROOT)} and {MATRIX_PATH.relative_to(ROOT)}: {total} tests in {len(counts)} modules.")
    return 0
if __name__=="__main__": raise SystemExit(main())
