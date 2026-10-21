"""Deterministic unit matrices for the web/API rule families without external HTTP."""
from types import SimpleNamespace
import pytest
from app.checks.web_checks import run_page_checks, run_form_checks, run_content_checks
from app.checks.cookie_checks import run_cookie_checks
from app.checks.cors_checks import run_cors_checks
from app.checks.api_checks import classify_api, candidate_api_paths, run_openapi_checks, run_graphql_observation
from app.checks.base import CheckContext


def page(url="https://app.example.test/", headers=None, body="", content_type="text/html", mixed=None, forms=None, links=None):
    observation=SimpleNamespace(headers=headers or {}, body=body, content_type=content_type)
    return SimpleNamespace(url=url, observation=observation, mixed_content=mixed or [], forms=forms or [], links=links or [])

@pytest.mark.parametrize("header,rule", [
    ("content-security-policy","FW-WEB-001"), ("x-content-type-options","FW-WEB-002"),
    ("referrer-policy","FW-WEB-003"), ("permissions-policy","FW-WEB-004"),
])
def test_v6_missing_header_rule_emits_expected_rule(header, rule):
    found=run_page_checks(page(headers={}),CheckContext(target_url="https://app.example.test/"))
    assert rule in {item.rule_id for item in found}

@pytest.mark.parametrize("headers,rule,expected", [
    ({},"FW-WEB-005",True), ({"x-frame-options":"DENY"},"FW-WEB-005",False),
    ({"content-security-policy":"default-src 'self'; frame-ancestors 'none'"},"FW-WEB-005",False),
    ({"x-frame-options":"SAMEORIGIN"},"FW-WEB-005",False),
    ({},"FW-WEB-006",True), ({"strict-transport-security":"max-age=31536000"},"FW-WEB-006",False),
])
def test_v6_frame_and_https_transport_rule_signals(headers, rule, expected):
    found=run_page_checks(page(headers=headers),CheckContext(target_url="https://app.example.test/"))
    assert (rule in {item.rule_id for item in found}) is expected

@pytest.mark.parametrize("marker", [
    "traceback (most recent call last)", "stack trace", "sql syntax", "sequelize",
    "django.core", "laravel\\vendor", "org.springframework", "exception: internal",
])
def test_v6_runtime_error_markers_are_detected_as_disclosure(marker):
    found=run_page_checks(page(body=f"Application diagnostic: {marker}"),CheckContext(target_url="https://app.example.test/"))
    assert "FW-WEB-011" in {item.rule_id for item in found}

@pytest.mark.parametrize("path", ["login", "account", "profile", "dashboard", "admin", "token", "session"])
def test_v6_sensitive_path_cache_review_activates_when_cache_policy_missing(path):
    found=run_page_checks(page(url=f"https://app.example.test/{path}"),CheckContext(target_url="https://app.example.test/"))
    assert "FW-WEB-008" in {item.rule_id for item in found}

@pytest.mark.parametrize("content", [
    "const sourceURL = 'app.js.map'; //# sourceMappingURL=app.js.map",
    "bundle content sourceMappingURL=private.js.map",
])
def test_v6_source_map_marker_is_reviewed(content):
    found=run_page_checks(page(body=content),CheckContext(target_url="https://app.example.test/"))
    assert "FW-WEB-009" in {item.rule_id for item in found}

def test_v6_mixed_content_is_reported_without_fetching_resource():
    found=run_page_checks(page(mixed=["http://cdn.example.test/app.js"]),CheckContext(target_url="https://app.example.test/"))
    item=next(x for x in found if x.rule_id=="FW-WEB-010")
    assert "1 HTTP" in item.evidence_summary

@pytest.mark.parametrize("method", ["POST", "PUT", "PATCH", "DELETE"])
def test_v6_state_changing_form_without_named_csrf_token_is_only_candidate(method):
    p=page(forms=[{"action":"https://app.example.test/save","method":method,"inputs":[{"name":"value","type":"text"}]}])
    found=run_form_checks(p,CheckContext(target_url=p.url))
    item=next(x for x in found if x.rule_id=="FW-FORM-002")
    assert "not proof" in item.description

@pytest.mark.parametrize("token_name", ["csrf", "csrf_token", "_csrf", "xsrf", "_token"])
def test_v6_named_csrf_field_avoids_weak_signal(token_name):
    p=page(forms=[{"action":"https://app.example.test/save","method":"POST","inputs":[{"name":token_name,"type":"hidden"}]}])
    assert "FW-FORM-002" not in {x.rule_id for x in run_form_checks(p,CheckContext(target_url=p.url))}

def test_v6_password_form_over_http_is_detected():
    p=page(url="https://app.example.test/login",forms=[{"action":"http://app.example.test/login","method":"POST","inputs":[{"name":"password","type":"password"}]}])
    assert "FW-FORM-001" in {x.rule_id for x in run_form_checks(p,CheckContext(target_url=p.url))}

@pytest.mark.parametrize("extension", ["bak", "old", "orig", "backup", "zip", "tar", "gz", "sql"])
def test_v6_backup_artifact_links_are_flagged_as_candidates(extension):
    p=page(links=[f"https://app.example.test/archive.{extension}"])
    assert "FW-CONTENT-001" in {x.rule_id for x in run_content_checks(p,CheckContext(target_url=p.url))}

@pytest.mark.parametrize("cookie,expected_rules", [
    ("sessionid=abc", {"FW-COOKIE-001","FW-COOKIE-002","FW-COOKIE-003"}),
    ("sid=abc; Secure; HttpOnly; SameSite=Lax", set()),
    ("theme=dark; Secure; SameSite=Strict", set()),
    ("auth_token=abc; Secure; SameSite=None", {"FW-COOKIE-002"}),
    ("sid=abc; SameSite=None", {"FW-COOKIE-001","FW-COOKIE-002","FW-COOKIE-004"}),
    ("__Host-session=abc; HttpOnly; SameSite=Lax", {"FW-COOKIE-001","FW-COOKIE-005"}),
    ("__Secure-token=abc; HttpOnly; SameSite=Lax", {"FW-COOKIE-001","FW-COOKIE-006"}),
])
def test_v6_cookie_attribute_matrix(cookie, expected_rules):
    p=page(headers={"set-cookie":cookie})
    actual={x.rule_id for x in run_cookie_checks(p,CheckContext(target_url=p.url))}
    assert expected_rules.issubset(actual)

@pytest.mark.parametrize("headers,expected", [
    ({"access-control-allow-origin":"*"}, {"FW-CORS-001"}),
    ({"access-control-allow-origin":"*","access-control-allow-credentials":"true"}, {"FW-CORS-001","FW-CORS-002"}),
    ({"access-control-expose-headers":"*"}, {"FW-CORS-003"}),
    ({"access-control-allow-origin":"https://trusted.example.test","access-control-allow-credentials":"true"}, set()),
])
def test_v6_cors_rule_matrix(headers, expected):
    p=page(headers=headers)
    actual={x.rule_id for x in run_cors_checks(p,CheckContext(target_url=p.url))}
    assert actual == expected

@pytest.mark.parametrize("url,expected", [
    ("https://app.example.test/graphql","graphql"), ("https://app.example.test/api/users","api"),
    ("https://app.example.test/v1/users","api"), ("https://app.example.test/v2/health","api"),
    ("https://app.example.test/rest/orders","api"), ("https://app.example.test/account","web"),
])
def test_v6_api_classifier_matrix(url,expected):
    assert classify_api(url)==expected

def test_v6_openapi_candidate_paths_are_relative_to_root():
    paths=candidate_api_paths("https://app.example.test/base/")
    assert len(paths)==7
    assert all(x.startswith("https://app.example.test/") for x in paths)
    assert any(x.endswith("/openapi.json") for x in paths)

@pytest.mark.parametrize("body", ["not yaml: [", "[]", "null", "{not-json}", "\x00\x01"])
def test_v6_invalid_api_specs_do_not_crash(body):
    assert run_openapi_checks("https://app.example.test/openapi.json",body,"application/json") == []

@pytest.mark.parametrize("url", ["https://app.example.test/graphql", "https://app.example.test/api/graphql", "https://app.example.test/graphql/v1"])
def test_v6_graphql_signals_are_inventory_observations(url):
    found=run_graphql_observation(url,"")
    assert found and found[0].rule_id=="FW-GQL-001"
    assert "review" in found[0].impact.lower()

@pytest.mark.parametrize("url", ["https://app.example.test/", "https://app.example.test/api", "https://app.example.test/query"])
def test_v6_non_graphql_paths_do_not_get_graphql_finding(url):
    assert run_graphql_observation(url,"") == []
