"""API discovery and rule-family contracts across endpoint and document variants."""
import json
import pytest
from app.checks.api_checks import classify_api, run_graphql_observation, run_openapi_checks, candidate_api_paths
from app.assessment_catalog import TEST_PLAN, get_assessment_plan
from app.check_catalog import CATALOG, coverage_matrix

@pytest.mark.parametrize("method", ["get","post","put","patch","delete","head","options","trace","connect"])
@pytest.mark.parametrize("path", ["/api/users","/api/v1/orders","/v2/items","/rest/search","/graphql","/home","/apiary","/graphqlish"])
def test_v8_api_classifier_is_segment_based(method,path):
    url="https://api.example.test"+path
    actual=classify_api(url)
    if path.startswith(("/api/","/v2/","/rest/")) or path=="/graphql": assert actual in {"api","graphql"}
    if path in {"/home","/apiary","/graphqlish"}: assert actual=="web"

@pytest.mark.parametrize("name", ["url","uri","callback","redirect","webhook","target","destination","next","return_to","return_url","endpoint","domain","host","image_url","avatar_url","logo_url"])
@pytest.mark.parametrize("location", ["query","path"])
def test_v8_openapi_urlish_inputs_create_review_candidates(name,location):
    parameter={"name":name,"in":location,"schema":{"type":"string"}}
    spec={"openapi":"3.0.3","paths":{"/fetch/{host}":{"get":{"parameters":[parameter],"responses":{"200":{"description":"ok"}}}}}}
    findings=run_openapi_checks("https://api.example.test/openapi.json",json.dumps(spec),"application/json")
    assert any(f.rule_id=="FW-API-003" and f.evidence.get("parameter")==name for f in findings)

@pytest.mark.parametrize("url", ["https://api.example.test/graphql","https://api.example.test/api/graphql","https://api.example.test/GraphQL/query"])
def test_v8_graphql_endpoint_inventory_is_informational(url):
    items=run_graphql_observation(url,"")
    assert len(items)==1 and items[0].rule_id=="FW-GQL-001"
    assert items[0].severity.value=="info"

@pytest.mark.parametrize("root", ["https://api.example.test/","https://api.example.test/base/","http://localhost:8080/service/","https://api.example.test/app?lang=en"])
def test_v8_api_candidate_paths_are_unique_and_same_origin(root):
    paths=candidate_api_paths(root)
    assert len(paths)==len(set(paths))
    assert all(p.startswith(root.split("://",1)[0]+"://"+root.split("://",1)[1].split("/",1)[0]) for p in paths)

def test_v8_assessment_catalog_ids_unique_and_modes_reconcile():
    ids=[row["id"] for row in TEST_PLAN]
    assert len(ids)==len(set(ids))
    plan=get_assessment_plan()
    assert plan["total_cases"]==len(TEST_PLAN)
    assert sum(plan["execution_mode_counts"].values())==len(TEST_PLAN)

@pytest.mark.parametrize("row", CATALOG, ids=lambda row: row["id"])
def test_v8_every_check_catalog_item_has_required_fields(row):
    assert row["id"] and row["domain"] and row["mode"]
    assert isinstance(row["mapping"],list) and row["mapping"]

def test_v8_coverage_matrix_preserves_all_catalog_items():
    rows=coverage_matrix([])
    assert {r["id"] for r in rows}=={r["id"] for r in CATALOG}
    assert all(r["finding_count"]==0 for r in rows)
