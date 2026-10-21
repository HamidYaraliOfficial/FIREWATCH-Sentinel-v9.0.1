# FIREWATCH v7 — Automated Test Matrix

Release: `7.0.0`  
Collected tests: **2763** across **41** test modules.

> This manifest is generated from pytest collection. Software test count and statement coverage are not the percentage of vulnerabilities found and do not prove that any target is secure.

## Suite inventory

| Test module | Collected cases | Focus |
|---|---:|---|
| `test_api.py` | 6 | API health/readiness, security headers, evidence and report bundles |
| `test_checks.py` | 1 | Unit, matrix, integration, and regression tests |
| `test_integration.py` | 1 | Local-only end-to-end demo scan and report generation |
| `test_scope.py` | 2 | Unit, matrix, integration, and regression tests |
| `test_security_regressions.py` | 14 | Unit, matrix, integration, and regression tests |
| `test_v4_security.py` | 6 | Unit, matrix, integration, and regression tests |
| `test_v5_api_extended.py` | 8 | Unit, matrix, integration, and regression tests |
| `test_v5_authz_matrix.py` | 14 | Unit, matrix, integration, and regression tests |
| `test_v5_authz_policy.py` | 17 | Unit, matrix, integration, and regression tests |
| `test_v5_browser_mock.py` | 3 | Unit, matrix, integration, and regression tests |
| `test_v5_cli.py` | 7 | Unit, matrix, integration, and regression tests |
| `test_v5_discovery_components.py` | 18 | Unit, matrix, integration, and regression tests |
| `test_v5_misc_invariants.py` | 7 | Unit, matrix, integration, and regression tests |
| `test_v5_redaction_matrix.py` | 70 | Unit, matrix, integration, and regression tests |
| `test_v5_risk_catalog.py` | 35 | Unit, matrix, integration, and regression tests |
| `test_v5_schema_matrix.py` | 39 | Unit, matrix, integration, and regression tests |
| `test_v5_scope_matrix.py` | 44 | Unit, matrix, integration, and regression tests |
| `test_v5_security_checks.py` | 44 | Unit, matrix, integration, and regression tests |
| `test_v5_tls_matrix.py` | 9 | Unit, matrix, integration, and regression tests |
| `test_v5_transport_report.py` | 34 | Unit, matrix, integration, and regression tests |
| `test_v5_worker_planner_zap.py` | 21 | Unit, matrix, integration, and regression tests |
| `test_v6_api_route_contract_matrix.py` | 17 | Unit, matrix, integration, and regression tests |
| `test_v6_catalog_report_contract.py` | 109 | Assessment/check catalog contracts and all report formats |
| `test_v6_config_parser_matrix.py` | 26 | Environment configuration parser boundary and malformed-value handling |
| `test_v6_http_method_and_redirect_matrix.py` | 13 | HTTP method, no-follow redirect and pre-network scope enforcement |
| `test_v6_origin_credential_isolation.py` | 18 | Exact-origin credential isolation and same-host different-port regressions |
| `test_v6_redaction_fuzz_matrix.py` | 149 | Inherited registered sensitive field/query names and recursive redaction matrix |
| `test_v6_risk_math_matrix.py` | 532 | Fine-grained severity/confidence risk scoring invariants |
| `test_v6_rule_behavior_matrix.py` | 75 | Parameterized behavior checks for registered passive and low-impact rules |
| `test_v6_schema_hardening_matrix.py` | 51 | Boundary values, header injection and authorization profile schema checks |
| `test_v6_scope_fuzz_matrix.py` | 93 | Inherited adversarial URL, nested encoding, ports, scope joins and exclusions |
| `test_v7_authorization_readonly_matrix.py` | 14 | Read-only role comparisons, authorization candidates, scope enforcement and request-body invariants |
| `test_v7_crawler_inventory_matrix.py` | 48 | Synthetic HTML, links, forms, JS routes, scope limits and technology fingerprints |
| `test_v7_openapi_contract_matrix.py` | 125 | OpenAPI effective auth declarations, URL-like parameters, API classification and GraphQL inventory |
| `test_v7_parameter_probe_policy_matrix.py` | 36 | Non-sensitive parameter selection, request limits, and benign GET canary policy |
| `test_v7_redaction_properties.py` | 251 | Sensitive field/query normalization, recursive URL decoding and benign-value invariants |
| `test_v7_report_sink_matrix.py` | 71 | HTML/Markdown injection resistance, CSV formula safety, JSON/SARIF schema contracts |
| `test_v7_schema_boundary_fuzz.py` | 146 | Input bounds, header injection variants, profiles and configuration limits |
| `test_v7_scope_adversarial_properties.py` | 470 | Encoded path exclusions, exact ports, hostile URL forms and scope joins |
| `test_v7_transport_boundary_matrix.py` | 98 | Exact-origin credential isolation, forbidden transport headers and redirect non-following |
| `test_v7_zap_plan_serialization.py` | 21 | YAML serialization without injection and malformed ZAP endpoint rejection |

| **Total** | **2763** | All collected unit, matrix, regression, API and local demo tests |

## Reproduce collection and run the suite

```bash
python -m pip install -r backend/requirements-dev.txt
python scripts/build_test_manifest.py
cd backend
PYTHONPATH=. python -m pytest tests -q --cov=app --cov-report=term-missing --cov-fail-under=80
```

## Separate target assessment catalog

The 79-item assessment plan is separate from software regression tests. It labels cases requiring manual workflows, test accounts or specialist tools; those are not represented as automatically executed.
See `ASSESSMENT_CATALOG.md`, `assessment-plan-v7.json`, and `assessment-plan-v7.csv`.
