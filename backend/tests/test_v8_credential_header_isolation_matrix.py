"""Authentication and credential-header propagation boundaries across origin combinations."""
import pytest
from app.http_client import SafeHTTPClient, credentials_allowed_for_root_origin
from app.scope import ScopePolicy

CREDENTIAL_HEADERS=["Authorization","Proxy-Authorization","Cookie","Set-Cookie","X-API-Key","API-Key","X-Auth-Token","X-Access-Token","X-Session-Token","Authentication","X-Custom-Token","X-Client-Secret","X-Session-ID"]
ROOT_TARGETS=[
 ("https://app.example.test/","https://app.example.test/",False,True),
 ("https://app.example.test/","https://app.example.test/",True,True),
 ("https://app.example.test/","https://APP.EXAMPLE.TEST:443/path",False,True),
 ("https://app.example.test:8443/","https://app.example.test:8443/path",False,True),
 ("https://app.example.test/","https://app.example.test:8443/path",False,False),
 ("https://app.example.test/","https://api.example.test/path",False,False),
 ("https://app.example.test/","http://app.example.test/path",False,False),
 ("http://app.example.test/","http://app.example.test/path",False,False),
 ("http://app.example.test/","http://app.example.test/path",True,True),
 ("https://app.example.test/","https://app.example.test.evil.test/path",False,False),
 ("https://app.example.test/","https://app.example.test@evil.test/path",False,False),
 ("https://app.example.test/","https://user:pass@app.example.test/path",False,False),
]

@pytest.mark.parametrize("header", CREDENTIAL_HEADERS)
@pytest.mark.parametrize("root,target,private,expected", ROOT_TARGETS)
def test_v8_all_credentialish_headers_follow_exact_origin_policy(header,root,target,private,expected):
    client=SafeHTTPClient(ScopePolicy.from_root(root,allow_private_targets=True),delay_ms=0,headers={header:"FWV8-CREDENTIAL-CANARY"})
    actual={k.lower():v for k,v in client._headers_for(target).items()}
    if header.lower()=="proxy-authorization":
        assert "proxy-authorization" not in actual
    elif credentials_allowed_for_root_origin(root, target, True):
        assert actual.get(header.lower())=="FWV8-CREDENTIAL-CANARY"
    else:
        assert header.lower() not in actual

@pytest.mark.parametrize("header", ["Host","Content-Length","Transfer-Encoding","Connection","Proxy-Authorization","Proxy-Connection","Upgrade","TE","Trailer"])
def test_v8_http_transport_headers_are_dropped_even_when_customized(header):
    policy=ScopePolicy.from_root("https://app.example.test/",allow_private_targets=True)
    client=SafeHTTPClient(policy,delay_ms=0,headers={header:"attacker-controlled"})
    assert header.lower() not in {k.lower() for k in client._headers_for(policy.root_url)}

@pytest.mark.parametrize("root,target,private,expected", ROOT_TARGETS)
def test_v8_origin_comparison_contract_is_explicit(root,target,private,expected):
    assert credentials_allowed_for_root_origin(root,target,private) is expected
