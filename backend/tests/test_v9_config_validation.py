"""Startup configuration fail-closed behavior and production deployment guardrails."""
from types import SimpleNamespace
import math
import pytest

from app.config import settings, validate_settings


def candidate(**changes):
    return SimpleNamespace(**({**vars(settings), **changes}))


def test_v9_default_configuration_is_valid():
    assert validate_settings(candidate()) == []


@pytest.mark.parametrize("field,low,high", [
    ("max_pages", 1, 5000),
    ("max_depth", 0, 20),
    ("max_endpoints", 10, 10000),
    ("request_timeout_seconds", 0.5, 120.0),
    ("max_response_body_bytes", 1024, 25_000_000),
    ("browser_timeout_seconds", 1.0, 180.0),
    ("request_delay_ms", 0, 10000),
    ("max_concurrency", 1, 20),
    ("max_parameter_probes", 0, 1000),
])
@pytest.mark.parametrize("edge", ["below", "above"])
def test_v9_resource_limits_reject_values_outside_documented_range(field, low, high, edge):
    value = low - 1 if edge == "below" else high + 1
    errors = validate_settings(candidate(**{field: value}))
    assert any(field in error for error in errors)


@pytest.mark.parametrize("field,value", [
    ("max_pages", float("nan")), ("max_pages", float("inf")),
    ("max_depth", True), ("max_endpoints", -100),
    ("request_timeout_seconds", float("nan")),
    ("max_response_body_bytes", -1),
    ("browser_timeout_seconds", 0), ("request_delay_ms", -1),
    ("max_concurrency", 0), ("max_parameter_probes", -1),
])
def test_v9_non_finite_boolean_or_negative_config_values_are_rejected(field, value):
    assert any(field in error for error in validate_settings(candidate(**{field: value})))


@pytest.mark.parametrize("level", ["", "TRACE", "WARN", "INFO;DROP", "debug\nERROR", "verbose"])
def test_v9_unknown_log_levels_are_rejected(level):
    assert any("log_level" in error for error in validate_settings(candidate(log_level=level)))


@pytest.mark.parametrize("origin", [
    "*", "ftp://example.test", "https://user:pass@example.test",
    "https://example.test/admin", "https://example.test/?secret=x",
    "https://example.test/#fragment", "https://example.test:bad",
    "", "null", "//example.test",
])
def test_v9_invalid_cors_origin_is_rejected(origin):
    cfg = candidate(cors_origins=origin)
    assert any("cors_origins" in error for error in validate_settings(cfg))


@pytest.mark.parametrize("origin", [
    "https://security.example", "https://portal.example,https://admin.example",
    "http://localhost:8000", "http://127.0.0.1:8000", "http://[::1]:8000",
])
def test_v9_development_cors_explicit_origins_are_accepted(origin):
    assert not any("cors_origins" in error for error in validate_settings(candidate(cors_origins=origin)))


def production_candidate(**changes):
    base = {
        "environment": "production", "api_key": "k" * 48,
        "database_url": "postgresql+psycopg://fw:placeholder@db:5432/firewatch",
        "allow_private_targets": False, "enable_inline_worker": False,
        "cors_origins": "https://security.example",
    }
    return candidate(**(base | changes))


def test_v9_valid_production_config_passes_gate(monkeypatch):
    monkeypatch.delenv("FIREWATCH_SECRET_KEY", raising=False)
    monkeypatch.setenv("FIREWATCH_SECRET_KEY_FILE", "/data/secret.key")
    assert validate_settings(production_candidate()) == []


@pytest.mark.parametrize("changes,expected", [
    ({"api_key": "short"}, "FIREWATCH_API_KEY"),
    ({"api_key": ""}, "FIREWATCH_API_KEY"),
    ({"api_key": "é" * 40}, "FIREWATCH_API_KEY"),
    ({"allow_private_targets": True}, "ALLOW_PRIVATE_TARGETS"),
    ({"database_url": "sqlite:///./firewatch.db"}, "DATABASE_URL"),
    ({"enable_inline_worker": True}, "ENABLE_INLINE_WORKER"),
    ({"cors_origins": "*"}, "cors_origins"),
    ({"cors_origins": "http://remote.example"}, "HTTPS"),
])
def test_v9_production_guardrails_fail_closed(changes, expected, monkeypatch):
    monkeypatch.delenv("FIREWATCH_SECRET_KEY", raising=False)
    monkeypatch.setenv("FIREWATCH_SECRET_KEY_FILE", "/data/secret.key")
    errors = validate_settings(production_candidate(**changes))
    assert any(expected in error for error in errors)


@pytest.mark.parametrize("zap_url", [
    "ftp://zap.example", "http://user:pass@zap.example", "http://zap.example/path", "http://zap.example:0",
    "http://zap.example/?api_key=secret", "http://zap.example/#frag", "http://zap.example:bad",
])
def test_v9_invalid_zap_origin_is_rejected(zap_url):
    assert any("ZAP_BASE_URL" in error for error in validate_settings(candidate(enable_zap=True, zap_base_url=zap_url)))


@pytest.mark.parametrize("user_agent", ["", "x" * 257, "Agent\r\nX: injected", "Agent\x7f"])
def test_v9_user_agent_rejects_control_or_out_of_range_values(user_agent):
    assert any("user_agent" in error for error in validate_settings(candidate(user_agent=user_agent)))


def test_v9_invalid_explicit_fernet_key_fails_without_echoing_value(monkeypatch):
    secret = "not-a-real-fernet-key-secret-value"
    monkeypatch.setenv("FIREWATCH_SECRET_KEY", secret)
    errors = validate_settings(candidate())
    assert any("FIREWATCH_SECRET_KEY" in error for error in errors)
    assert secret not in " ".join(errors)


def test_v9_production_rejects_non_loopback_http_cors_origin(monkeypatch):
    monkeypatch.delenv("FIREWATCH_SECRET_KEY", raising=False)
    monkeypatch.setenv("FIREWATCH_SECRET_KEY_FILE", "/data/secret.key")
    errors = validate_settings(production_candidate(cors_origins="http://security.example"))
    assert any("HTTPS" in error for error in errors)
