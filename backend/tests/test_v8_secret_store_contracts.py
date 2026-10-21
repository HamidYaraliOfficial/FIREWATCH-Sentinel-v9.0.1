"""Secret storage regression tests: encrypted at rest, redacted publicly, fail closed on wrong key."""
import json, os, stat
import pytest
from cryptography.fernet import Fernet
from app.secret_store import protect_config, reveal_config, public_config

SECRET="FWV8-STORAGE-CANARY-NOT-PLAINTEXT"

@pytest.fixture
def isolated_key(tmp_path, monkeypatch):
    monkeypatch.delenv("FIREWATCH_SECRET_KEY", raising=False)
    keyfile=tmp_path/"private"/"secret.key"
    monkeypatch.setenv("FIREWATCH_SECRET_KEY_FILE",str(keyfile))
    return keyfile

@pytest.mark.parametrize("field,value", [
    ("request_headers",{"Authorization":f"Bearer {SECRET}","X-API-Key":SECRET}),
    ("auth_cookies",f"session={SECRET}; HttpOnly"),
    ("authorization_profiles",[{"name":"admin-test","headers":{"Authorization":f"Bearer {SECRET}"}}]),
])
def test_v8_protected_config_never_contains_secret_in_plaintext(isolated_key,field,value):
    protected=protect_config({"profile":"standard",field:value})
    encoded=json.dumps(protected)
    assert SECRET not in encoded
    assert "_secret_blob" in protected
    assert field not in protected
    assert SECRET not in json.dumps(public_config(protected))

@pytest.mark.parametrize("field,value", [
    ("request_headers",{"Authorization":f"Bearer {SECRET}"}),
    ("auth_cookies",f"session={SECRET}"),
    ("authorization_profiles",[{"name":"user","headers":{"Cookie":SECRET}}]),
])
def test_v8_protected_config_roundtrips_only_with_correct_key(isolated_key,field,value):
    protected=protect_config({"profile":"baseline",field:value})
    assert reveal_config(protected)[field]==value

@pytest.mark.parametrize("config", [{}, {"profile":"baseline"}, {"max_pages":10}, {"request_headers":{}}, {"auth_cookies":""}, {"authorization_profiles":[]}])
def test_v8_empty_or_nonsecret_configuration_does_not_create_ciphertext(isolated_key,config):
    result=protect_config(config)
    assert "_secret_blob" not in result
    expected={k:v for k,v in config.items() if k not in {"request_headers","auth_cookies","authorization_profiles"}}
    assert reveal_config(result)==expected

@pytest.mark.parametrize("name,value", [("Authorization",SECRET),("Cookie",SECRET),("X-API-Key",SECRET),("X-Trace-Id","ordinary")])
def test_v8_public_config_masks_each_auth_header_value(isolated_key,name,value):
    cfg=protect_config({"request_headers":{name:value},"profile":"standard"})
    public=public_config(cfg)
    serialized=json.dumps(public)
    assert SECRET not in serialized
    if name != "X-Trace-Id": assert public.get("authentication_configured") is True or public.get("request_headers",{}).get(name)=="[REDACTED]"

@pytest.mark.parametrize("raw_key", ["invalid", "short", "not-a-fernet-key-123456"])
def test_v8_invalid_fernet_environment_key_fails_closed(raw_key,isolated_key,monkeypatch):
    monkeypatch.setenv("FIREWATCH_SECRET_KEY",raw_key)
    from app.secret_store import _get_cipher
    with pytest.raises(RuntimeError): _get_cipher()

def test_v8_generated_key_file_has_restrictive_posix_permissions(isolated_key):
    protect_config({"request_headers":{"Authorization":"Bearer test"}})
    assert isolated_key.exists()
    if os.name != "nt":
        assert stat.S_IMODE(isolated_key.stat().st_mode) == 0o600

def test_v8_wrong_key_cannot_decrypt_stored_credentials(isolated_key,monkeypatch):
    monkeypatch.delenv("FIREWATCH_SECRET_KEY",raising=False)
    protected=protect_config({"auth_cookies":SECRET})
    wrong=Fernet.generate_key().decode("ascii")
    monkeypatch.setenv("FIREWATCH_SECRET_KEY",wrong)
    with pytest.raises(RuntimeError): reveal_config(protected)
