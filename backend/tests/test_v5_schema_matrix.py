import pytest
from pydantic import ValidationError
from app.schemas import ScanCreate

@pytest.mark.parametrize('profile', ['baseline','standard','comprehensive'])
def test_valid_profiles(profile):
    item=ScanCreate(target_url='https://example.test/', scope_acknowledged=True, profile=profile)
    assert item.profile == profile
    assert item.max_pages >= 1 and item.max_depth >= 0 and item.max_endpoints >= 10

@pytest.mark.parametrize('profile', ['fast','full','aggressive','','STANDARD','../../x',None])
def test_invalid_profiles_rejected(profile):
    with pytest.raises(ValidationError):
        ScanCreate(target_url='https://example.test/', profile=profile)

@pytest.mark.parametrize('field,value', [
 ('max_pages',0),('max_pages',5001),('max_depth',-1),('max_depth',21),
 ('max_endpoints',9),('max_endpoints',10001),('request_delay_ms',-1),
 ('request_delay_ms',10001),('max_concurrency',0),('max_concurrency',21),
])
def test_numeric_limits_enforced(field,value):
    with pytest.raises(ValidationError):
        ScanCreate(target_url='https://example.test/', **{field:value})

@pytest.mark.parametrize('headers', [
 {'Host':'evil.test'}, {'Content-Length':'0'}, {'Transfer-Encoding':'chunked'},
 {'Connection':'close'}, {'Proxy-Authorization':'Basic xx'}, {'Upgrade':'websocket'},
 {'Authorization':'Bearer x\r\nX-Injected: y'}, {'X-Test':'ok\nsecond'},
])
def test_unsafe_custom_headers_rejected(headers):
    with pytest.raises(ValidationError):
        ScanCreate(target_url='https://example.test/',request_headers=headers)

def test_too_many_headers_rejected():
    with pytest.raises(ValidationError):
        ScanCreate(target_url='https://example.test/',request_headers={f'X-{i}':'v' for i in range(51)})

@pytest.mark.parametrize('profiles', [
 [None], ['admin'], [{'name':'x','headers':'not-a-dict'}],
 [{'name':'x','headers':{'Host':'evil.test'}}],
 [{'name':'x','headers':{'Authorization':'Bearer x\r\nHost: evil.test'}}],
 [{'name':'a'*101,'headers':{}}],
])
def test_invalid_authorization_profiles_rejected(profiles):
    with pytest.raises(ValidationError):
        ScanCreate(target_url='https://example.test/',authorization_profiles=profiles)

def test_explicit_values_override_profile_defaults():
    scan=ScanCreate(target_url='https://example.test/',profile='baseline',max_pages=42)
    assert scan.max_pages == 42

@pytest.mark.parametrize('target', [
 'https://example.test/','https://example.test/a?lang=en','http://example.test/',
])
def test_schema_accepts_http_urls(target):
    assert str(ScanCreate(target_url=target).target_url).startswith(('http://','https://'))
