from __future__ import annotations
from dataclasses import dataclass
import os

def _bool(name: str, default: bool) -> bool:
    value=os.getenv(name)
    if value is None: return default
    return value.strip().lower() in {'1','true','yes','on'}
def _int(name: str, default: int) -> int:
    try: return int(os.getenv(name,str(default)))
    except ValueError: return default
def _float(name: str, default: float) -> float:
    try: return float(os.getenv(name,str(default)))
    except ValueError: return default
@dataclass(frozen=True)
class Settings:
    app_name:str=os.getenv('APP_NAME','FIREWATCH Sentinel')
    environment:str=os.getenv('ENVIRONMENT','development')
    database_url:str=os.getenv('DATABASE_URL','sqlite:///./firewatch.db')
    allow_private_targets:bool=_bool('ALLOW_PRIVATE_TARGETS',False)
    require_scope_ack:bool=_bool('REQUIRE_SCOPE_ACK',True)
    max_pages:int=_int('MAX_PAGES',300)
    max_depth:int=_int('MAX_DEPTH',8)
    max_endpoints:int=_int('MAX_ENDPOINTS',2000)
    request_timeout_seconds:float=_float('REQUEST_TIMEOUT_SECONDS',15.0)
    max_response_body_bytes:int=_int('MAX_RESPONSE_BODY_BYTES',2_000_000)
    browser_timeout_seconds:float=_float('BROWSER_TIMEOUT_SECONDS',30.0)
    request_delay_ms:int=_int('REQUEST_DELAY_MS',150)
    max_concurrency:int=_int('MAX_CONCURRENCY',6)
    respect_robots:bool=_bool('RESPECT_ROBOTS',True)
    enable_browser:bool=_bool('ENABLE_BROWSER',True)
    enable_api_introspection:bool=_bool('ENABLE_API_INTROSPECTION',True)
    enable_zap:bool=_bool('ENABLE_ZAP',False)
    zap_base_url:str=os.getenv('ZAP_BASE_URL','http://zap:8080')
    report_dir:str=os.getenv('REPORT_DIR','./reports')
    user_agent:str=os.getenv('USER_AGENT','FIREWATCH-Sentinel/9.0.1 (+authorized-security-testing)')
    cors_origins:str=os.getenv('CORS_ORIGINS','http://localhost:8000,http://127.0.0.1:8000')
    log_level:str=os.getenv('LOG_LEVEL','INFO')
    api_key:str=os.getenv('FIREWATCH_API_KEY','')
    enable_inline_worker:bool=_bool('ENABLE_INLINE_WORKER',True)
    worker_heartbeat_seconds:int=_int('WORKER_HEARTBEAT_SECONDS',10)
    worker_lease_timeout_seconds:int=_int('WORKER_LEASE_TIMEOUT_SECONDS',60)
    enable_safe_parameter_probes:bool=_bool('ENABLE_SAFE_PARAMETER_PROBES',True)
    max_parameter_probes:int=_int('MAX_PARAMETER_PROBES',60)
    secret_key_file:str=os.getenv('FIREWATCH_SECRET_KEY_FILE','.firewatch/secret.key')
settings=Settings()


# Startup configuration validation is intentionally separate from environment parsing.
# Parser helpers retain documented fallback semantics; this gate validates the effective
# values and applies stricter invariants when the service is deployed in production.
import math as _math
from urllib.parse import urlsplit as _urlsplit

def validate_settings(config=None) -> list[str]:
    """Return safe, actionable configuration errors without exposing secret values.

    ``config`` is injectable so tests and deployment tooling can validate candidate
    configurations without mutating the process environment.
    """
    cfg = config if config is not None else settings
    errors: list[str] = []
    bounds = {
        "max_pages": (1, 5000),
        "max_depth": (0, 20),
        "max_endpoints": (10, 10000),
        "request_timeout_seconds": (0.5, 120.0),
        "max_response_body_bytes": (1024, 25_000_000),
        "browser_timeout_seconds": (1.0, 180.0),
        "request_delay_ms": (0, 10000),
        "max_concurrency": (1, 20),
        "max_parameter_probes": (0, 1000),
        "worker_heartbeat_seconds": (2, 60),
        "worker_lease_timeout_seconds": (30, 3600),
    }
    for name, (low, high) in bounds.items():
        value = getattr(cfg, name, {
            "max_pages": 300, "max_depth": 8, "max_endpoints": 2000,
            "request_timeout_seconds": 15.0, "max_response_body_bytes": 2_000_000,
            "browser_timeout_seconds": 30.0, "request_delay_ms": 150,
            "max_concurrency": 4, "max_parameter_probes": 60,
            "worker_heartbeat_seconds": 10, "worker_lease_timeout_seconds": 60,
        }[name])
        valid_type = isinstance(value, (int, float)) and not isinstance(value, bool)
        if not valid_type or not _math.isfinite(float(value)) or value < low or value > high:
            errors.append(f"{name} must be within the supported range {low}..{high}")
    heartbeat = getattr(cfg, "worker_heartbeat_seconds", 10)
    lease_timeout = getattr(cfg, "worker_lease_timeout_seconds", 60)
    if (isinstance(heartbeat, (int, float)) and not isinstance(heartbeat, bool)
            and isinstance(lease_timeout, (int, float)) and not isinstance(lease_timeout, bool)
            and heartbeat * 3 >= lease_timeout):
        errors.append("WORKER_LEASE_TIMEOUT_SECONDS must be greater than three heartbeat intervals")

    level = str(getattr(cfg, "log_level", "INFO")).upper()
    if level not in {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}:
        errors.append("log_level must be DEBUG, INFO, WARNING, ERROR, or CRITICAL")
    user_agent = str(getattr(cfg, "user_agent", "FIREWATCH-Sentinel/9.0.1"))
    if not user_agent or len(user_agent) > 256 or any(ord(ch) < 32 or ord(ch) == 127 for ch in user_agent):
        errors.append("user_agent must be 1..256 printable characters")

    cors_raw = str(getattr(cfg, "cors_origins", "http://localhost:8000,http://127.0.0.1:8000"))
    cors_items = [x.strip() for x in cors_raw.split(",") if x.strip()]
    if not cors_items:
        errors.append("cors_origins must contain at least one explicit origin")
    for origin in cors_items:
        try:
            parsed = _urlsplit(origin)
            valid_origin = (parsed.scheme in {"http", "https"} and bool(parsed.hostname)
                            and parsed.username is None and parsed.password is None
                            and parsed.path in {"", "/"} and not parsed.query and not parsed.fragment
                            and origin != "*")
            parsed_port = parsed.port
            if parsed_port == 0:
                valid_origin = False
        except ValueError:
            valid_origin = False
        if not valid_origin:
            errors.append("cors_origins must contain valid explicit HTTP(S) origins without paths, credentials, query, or wildcards")
            break

    env = str(getattr(cfg, "environment", "development")).strip().lower()
    if env in {"production", "prod"}:
        api_key = str(getattr(cfg, "api_key", ""))
        if len(api_key) < 32 or any(ord(ch) < 33 or ord(ch) > 126 for ch in api_key):
            errors.append("FIREWATCH_API_KEY must be at least 32 printable ASCII characters in production")
        if bool(getattr(cfg, "allow_private_targets", False)):
            errors.append("ALLOW_PRIVATE_TARGETS must be false in production")
        database_url = str(getattr(cfg, "database_url", "sqlite:///./firewatch.db")).lower()
        if not database_url.startswith(("postgresql://", "postgresql+psycopg://", "postgres://")):
            errors.append("DATABASE_URL must use PostgreSQL in production")
        if not cors_items or any(origin == "*" for origin in cors_items):
            errors.append("CORS must use an explicit allow-list in production")
        for origin in cors_items:
            try:
                parsed_origin = _urlsplit(origin)
                host = (parsed_origin.hostname or "").lower().strip("[]")
                loopback_http = host in {"localhost", "127.0.0.1", "::1"}
                if parsed_origin.scheme != "https" and not (parsed_origin.scheme == "http" and loopback_http):
                    errors.append("Production CORS origins must use HTTPS except explicit loopback development origins")
                    break
            except ValueError:
                break
        if bool(getattr(cfg, "enable_inline_worker", True)):
            errors.append("ENABLE_INLINE_WORKER must be false in production; run the separate worker process")
        if not os.getenv("FIREWATCH_SECRET_KEY") and not os.getenv("FIREWATCH_SECRET_KEY_FILE"):
            errors.append("Set FIREWATCH_SECRET_KEY or explicitly mount FIREWATCH_SECRET_KEY_FILE in production")

    if bool(getattr(cfg, "enable_zap", False)):
        zap_url = str(getattr(cfg, "zap_base_url", ""))
        try:
            parsed = _urlsplit(zap_url)
            parsed_port = parsed.port
            valid_zap = (parsed_port != 0 and parsed.scheme in {"http", "https"} and bool(parsed.hostname)
                         and parsed.username is None and parsed.password is None
                         and not parsed.query and not parsed.fragment and parsed.path in {"", "/"})
        except ValueError:
            valid_zap = False
        if not valid_zap:
            errors.append("ZAP_BASE_URL must be a valid HTTP(S) origin without credentials, query, or fragment")

    # If an explicit Fernet key is supplied, validate its syntax at startup so a scan
    # cannot be queued before discovering that credentials cannot be protected.
    secret_key = os.getenv("FIREWATCH_SECRET_KEY", "")
    if secret_key:
        try:
            from cryptography.fernet import Fernet
            Fernet(secret_key.encode("ascii"))
        except Exception:
            errors.append("FIREWATCH_SECRET_KEY must be a valid Fernet key")
    return errors
