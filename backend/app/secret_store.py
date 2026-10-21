"""Encryption-at-rest helpers for target credentials.

The local key file is generated with restrictive permissions on first use. For
multi-container/production deployments set FIREWATCH_SECRET_KEY consistently or
mount FIREWATCH_SECRET_KEY_FILE on persistent, access-controlled storage.
"""
from __future__ import annotations
import json, os
from pathlib import Path
from threading import Lock
from typing import Any
from cryptography.fernet import Fernet, InvalidToken

_LOCK = Lock()
_SENSITIVE_CONFIG_KEYS = ("request_headers", "auth_cookies", "authorization_profiles")

def _get_cipher() -> Fernet:
    env_key = os.getenv("FIREWATCH_SECRET_KEY")
    if env_key:
        try:
            return Fernet(env_key.encode("ascii"))
        except Exception as exc:
            raise RuntimeError("FIREWATCH_SECRET_KEY must be a valid Fernet key") from exc
    key_path = Path(os.getenv("FIREWATCH_SECRET_KEY_FILE", ".firewatch/secret.key"))
    with _LOCK:
        if not key_path.exists():
            key_path.parent.mkdir(parents=True, exist_ok=True)
            key = Fernet.generate_key()
            try:
                fd = os.open(key_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
                with os.fdopen(fd, "wb") as fh:
                    fh.write(key)
            except FileExistsError:
                pass
        try:
            if os.name != "nt":
                os.chmod(key_path, 0o600)
            return Fernet(key_path.read_bytes().strip())
        except Exception as exc:
            raise RuntimeError(f"Cannot load FIREWATCH secret key from {key_path}") from exc

def protect_config(config: dict[str, Any]) -> dict[str, Any]:
    """Move credentials out of the scan config JSON and encrypt them."""
    result = dict(config)
    secret_payload = {}
    for key in _SENSITIVE_CONFIG_KEYS:
        value = result.pop(key, None)
        if value not in (None, {}, [], ""):
            secret_payload[key] = value
    if secret_payload:
        raw = json.dumps(secret_payload, ensure_ascii=False, separators=(",", ":")).encode()
        result["_secret_blob"] = _get_cipher().encrypt(raw).decode("ascii")
    return result

def reveal_config(config: dict[str, Any] | None) -> dict[str, Any]:
    result = dict(config or {})
    blob = result.pop("_secret_blob", None)
    if not blob:
        return result
    try:
        payload = json.loads(_get_cipher().decrypt(blob.encode("ascii")).decode("utf-8"))
    except (InvalidToken, ValueError, UnicodeDecodeError) as exc:
        raise RuntimeError("Cannot decrypt scan credentials; check FIREWATCH_SECRET_KEY or FIREWATCH_SECRET_KEY_FILE") from exc
    result.update(payload)
    return result

def public_config(config: dict[str, Any] | None) -> dict[str, Any]:
    """Return a safe summary; never return ciphertext or raw credentials."""
    raw=dict(config or {})
    result = {k: v for k, v in raw.items() if not k.startswith("_")}
    if raw.get('_secret_blob'): result['authentication_configured']=True
    for key in _SENSITIVE_CONFIG_KEYS:
        if key in result:
            value = result[key]
            if key == "authorization_profiles" and isinstance(value, list):
                result[key] = [{"name": p.get("name", "profile"), "headers": {k: "[REDACTED]" for k in (p.get("headers") or {})}} for p in value if isinstance(p, dict)]
            elif key == "request_headers" and isinstance(value, dict):
                result[key] = {k: "[REDACTED]" for k in value}
            elif value:
                result[key] = "[REDACTED]"
    return result
