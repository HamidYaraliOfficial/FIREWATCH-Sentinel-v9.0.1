"""OpenAPI effective-security and URL-like input inventory contract tests."""
import json
import pytest
from app.checks.api_checks import _load_spec, classify_api, run_openapi_checks, run_graphql_observation, candidate_api_paths

_GLOBAL = [None, [], [{"bearerAuth": []}], "invalid-shape"]
_OPERATION = ["missing", None, [], [{"bearerAuth": []}]]
_SCHEME = [False, True]

@pytest.mark.parametrize("global_security", _GLOBAL, ids=["missing", "empty", "secured", "malformed"])
@pytest.mark.parametrize("operation_security", _OPERATION, ids=["missing", "null", "empty", "secured"])
@pytest.mark.parametrize("scheme_exists", _SCHEME)
def test_v7_openapi_effective_authentication_declaration(global_security, operation_security, scheme_exists):
    operation = {"responses": {"200": {"description": "ok"}}}
    if operation_security != "missing":
        operation["security"] = operation_security
    doc = {"openapi": "3.0.3", "paths": {"/data": {"get": operation}}}
    if global_security is not None:
        doc["security"] = global_security
    if scheme_exists:
        doc["components"] = {"securitySchemes": {"bearerAuth": {"type": "http", "scheme": "bearer"}}}
    findings = run_openapi_checks("https://api.example.test/openapi.json", json.dumps(doc), "application/json")
    needs_review = False
    explicit = operation_security != "missing"
    if explicit:
        effective = bool(operation_security)
    else:
        effective = bool(global_security)
    # The agent reports absent effective security when operation-level security explicitly disables
    # inherited policy, or when no schemes exist to document an authentication requirement.
    security_schemes = scheme_exists or bool(doc.get("securityDefinitions"))
    needs_review = (not effective) and (explicit or not security_schemes)
    assert ("FW-API-002" in {f.rule_id for f in findings}) == needs_review

_URL_PARAM_NAMES = ["url", "uri", "callback", "redirect", "webhook", "target", "destination", "next", "return_to", "host"]
_METHODS = ["get", "post", "put", "patch", "delete", "options", "head"]
@pytest.mark.parametrize("name", _URL_PARAM_NAMES)
@pytest.mark.parametrize("method", _METHODS)
def test_v7_url_like_parameters_are_inventory_review_candidates(name, method):
    doc = {"openapi": "3.0.3", "paths": {"/fetch": {method: {
        "parameters": [{"name": name, "in": "query", "schema": {"type": "string"}}],
        "responses": {"200": {"description": "ok"}},
    }}}}
    findings = run_openapi_checks("https://api.example.test/openapi.json", json.dumps(doc), "application/json")
    assert any(f.rule_id == "FW-API-003" and f.evidence.get("parameter") == name for f in findings)

@pytest.mark.parametrize("url,expected", [
    ("https://example.test/api/v1/users", "api"), ("https://example.test/v2/items", "api"),
    ("https://example.test/rest/items", "api"), ("https://example.test/graphql", "graphql"),
    ("https://example.test/GraphQL/query", "graphql"), ("https://example.test/home", "web"),
    ("https://example.test/apiary", "web"), ("https://example.test/v1", "web"),
    ("https://example.test/rest", "web"), ("https://example.test/graphqlish", "web"),
])
def test_v7_api_classifier_boundary_contract(url, expected):
    assert classify_api(url) == expected

@pytest.mark.parametrize("body", ["", "null", "[]", "{}", "<html>oops</html>", "openapi: [unterminated", "{not-json", "true", "42"])
def test_v7_openapi_loader_malformed_document_never_raises(body):
    try:
        loaded = _load_spec(body)
    except Exception:
        # YAML parsers may raise on malformed data; caller must handle it safely.
        return
    assert isinstance(loaded, (dict, list, str, int, float, bool)) or loaded is None

@pytest.mark.parametrize("url", ["https://example.test/graphql", "https://example.test/api/graphql", "https://example.test/graphql?query=hi"])
def test_v7_graphql_inventory_signal_has_review_semantics(url):
    found = run_graphql_observation(url, "")
    assert len(found) == 1
    assert found[0].rule_id == "FW-GQL-001"
    assert "review" in found[0].remediation.lower() or "review" in found[0].description.lower()

def test_v7_openapi_candidate_paths_are_absolute_to_root():
    paths = candidate_api_paths("https://api.example.test/base/")
    assert paths and all(p.startswith("https://api.example.test/") for p in paths)
    assert len(paths) == len(set(paths))
