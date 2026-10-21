# FIREWATCH v6 — Automated Test Matrix

Release: `6.0.0`  
Collected tests: **1483** across **31** test modules.

> This manifest is generated from pytest collection. Software test count and statement coverage are not the percentage of vulnerabilities found and do not prove that any target is secure.

## Suite inventory

| Test module | Collected cases | Focus |
|---|---:|---|
| `test_api.py` | 6 | API health/readiness, security headers, evidence and report bundles |
| `test_checks.py` | 1 | Rule registry smoke test |
| `test_integration.py` | 1 | Local-only end-to-end demo scan and report generation |
| `test_scope.py` | 2 | Basic scope rules |
| `test_security_regressions.py` | 14 | Credential encryption, secret redaction and earlier security fixes |
| `test_v4_security.py` | 6 | Origin credential isolation and transport guard regressions |
| `test_v5_api_extended.py` | 8 | API versioning, auth gate and assessment-plan contract |
| `test_v5_authz_matrix.py` | 14 | Read-only authorization comparison matrix |
| `test_v5_authz_policy.py` | 17 | Authorization policy and profile input matrix |
| `test_v5_browser_mock.py` | 3 | Browser discovery under mocked browser objects |
| `test_v5_cli.py` | 7 | CLI invocation, invalid target and report behavior |
| `test_v5_discovery_components.py` | 18 | Crawler, API discovery and bounded parameter-probe behavior |
| `test_v5_misc_invariants.py` | 7 | Cross-module safety invariants |
| `test_v5_redaction_matrix.py` | 70 | Original secret redaction regression matrix |
| `test_v5_risk_catalog.py` | 35 | Risk score and assessment catalog invariants |
| `test_v5_schema_matrix.py` | 39 | Input schema and malformed values |
| `test_v5_scope_matrix.py` | 44 | Unit and regression tests |
| `test_v5_security_checks.py` | 44 | Cookie, header, CSP and API security checks |
| `test_v5_tls_matrix.py` | 9 | TLS parsing and connection error behavior |
| `test_v5_transport_report.py` | 34 | HTTP transport, redirect and report escaping |
| `test_v5_worker_planner_zap.py` | 21 | Worker queue, planner modes and ZAP plan safety |
| `test_v6_api_route_contract_matrix.py` | 17 | Unit and regression tests |
| `test_v6_catalog_report_contract.py` | 109 | Assessment/check catalog contracts and all report formats |
| `test_v6_config_parser_matrix.py` | 26 | Environment configuration parser boundary and malformed-value handling |
| `test_v6_http_method_and_redirect_matrix.py` | 13 | HTTP method, no-follow redirect and pre-network scope enforcement |
| `test_v6_origin_credential_isolation.py` | 18 | Exact-origin credential guards including same-host different-port regression |
| `test_v6_redaction_fuzz_matrix.py` | 149 | Every registered sensitive field/query name plus recursive redaction matrix |
| `test_v6_risk_math_matrix.py` | 532 | Fine-grained severity/confidence risk scoring invariants |
| `test_v6_rule_behavior_matrix.py` | 75 | Parameterized behavior checks for the registered passive and low-impact security rules |
| `test_v6_schema_hardening_matrix.py` | 51 | Boundary-value, header-injection and authorization profile schema checks |
| `test_v6_scope_fuzz_matrix.py` | 93 | Adversarial URL, nested encoding, ports, scope joins and exclusion boundaries |

| **Total** | **1483** | All collected unit, matrix, regression, API and local demo tests |

## Reproduce collection and run the suite

```bash
python -m pip install -r backend/requirements-dev.txt
python scripts/build_test_manifest.py
cd backend
PYTHONPATH=. python -m pytest tests -q --cov=app --cov-report=term-missing --cov-fail-under=78
```

## Separate target assessment catalog

The 79-item assessment plan is separate from software-regression tests. It labels checks requiring manual workflows, test accounts or specialist tools; those are not represented as automatically executed.
See `ASSESSMENT_CATALOG.md`, `assessment-plan-v6.json`, and `assessment-plan-v6.csv`.
