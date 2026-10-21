import pytest
from app.redaction import contains_sensitive_query, redact_data, redact_text, redact_url

@pytest.mark.parametrize('name', [
    'token','jwt','access_token','refresh_token','id_token','api_key','apikey','secret','secret_key',
    'private_key','password','passwd','passphrase','session','sessionid','session_id','sid','authorization',
    'auth','code','signature','sig','key','client_secret','clientsecret','credential','credentials',
    'aws_secret_access_key','samlresponse','assertion','bearer','auth_token','x_api_key','csrf_token',
    'Access-Token','client.secret','Session Id','PRIVATE-KEY'
])
def test_sensitive_query_name_matrix(name):
    assert contains_sensitive_query(f'https://example.test/path?{name}=super-secret-value')

@pytest.mark.parametrize('url', [
    'https://example.test/a?token=abc',
    'https://example.test/a?access_token=abc&keep=yes',
    'http://user:password@example.test/a?key=abc',
    'https://alice:s3cr3t@example.test/a?signature=abc',
    'https://example.test/a?Session-Id=abc',
    'https://example.test/a?client.secret=abc',
])
def test_url_redaction_never_keeps_common_credentials(url):
    output = redact_url(url)
    low = output.lower()
    for secret in ('password', 's3cr3t', 'super-secret', '=abc'):
        if secret in url.lower() and ('token' in url.lower() or 'key=' in url.lower() or '@' in url):
            assert secret not in low
    assert 'user:' not in low and 'alice:' not in low

@pytest.mark.parametrize('data', [
    {'Authorization':'Bearer secret-token-123'}, {'Cookie':'sid=secret-123'},
    {'Set-Cookie':'sessionid=secret-123; HttpOnly'}, {'x-api-key':'secret-123'},
    {'nested': {'password':'pw-123456'}}, {'list':[{'client_secret':'secret-123'}]},
    {'AWS_SECRET_ACCESS_KEY':'very-secret'}, {'database_url':'postgres://u:p@db/db'},
    {'Session-Id':'abc123'}, {'refresh-token':'rt-123456'}, {'private key':'key-123'},
])
def test_sensitive_fields_redacted_recursively(data):
    rendered = str(redact_data(data))
    for marker in ('secret-123','pw-123456','very-secret','abc123','rt-123456','key-123','u:p@db'):
        if marker in str(data):
            assert marker not in rendered

@pytest.mark.parametrize('text,secret', [
    ('Authorization: Bearer abcdefghijklmnop','abcdefghijklmnop'),
    ('authorization=Bearer abcdefghijklmnop','abcdefghijklmnop'),
    ('password=' + 'my-secret-password','my-secret-password'),
    ('client_secret="my long client secret"','my long client secret'),
    ('Cookie: sid=my-session-token; theme=dark','my-session-token'),
    ('Set-Cookie: auth=super-secret; Path=/; HttpOnly','super-secret'),
    ('private_key="-----BEGIN ' + 'PRIVATE KEY-----xx"','BEGIN PRIVATE KEY'),
    ('https://example.test/?access_token=secretvalue','secretvalue'),
    ('token: secretvalue','secretvalue'),
    ('AWS_SECRET_ACCESS_KEY=ABCDEF123456','ABCDEF123456'),
])
def test_text_redaction_matrix(text, secret):
    assert secret not in redact_text(text)

@pytest.mark.parametrize('benign', [
    'https://example.test/path?lang=en', 'application/json', 'hello world',
    'Cache-Control: no-store', 'cookie attributes should be reviewed',
])
def test_benign_strings_are_stable(benign):
    assert redact_text(benign) == benign
