"""Central secret redaction helpers used by logs, findings and report APIs.

Redaction is intentionally conservative: false-redacting a diagnostic is preferable
 to persisting credential material in a security report. This is not a replacement
for a proper secret manager or a policy against putting secrets in URLs.
"""
from __future__ import annotations

import re
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode, unquote

SENSITIVE_QUERY_NAMES = {
    "token", "jwt", "access_token", "refresh_token", "id_token", "api_key", "apikey",
    "secret", "secret_key", "private_key", "password", "passwd", "passphrase", "session",
    "sessionid", "session_id", "sid", "authorization", "auth", "code", "signature", "sig",
    "key", "client_secret", "clientsecret", "credential", "credentials", "aws_secret_access_key",
    "samlresponse", "assertion", "bearer", "auth_token", "x_api_key", "csrf_token",
}
SENSITIVE_FIELD_NAMES = SENSITIVE_QUERY_NAMES | {
    "cookie", "set_cookie", "proxy_authorization", "x_auth_token", "x_access_token",
    "privatekey", "secretaccesskey", "database_url", "dsn", "connection_string",
}
_ASSIGNMENT_RE = re.compile(
    r"(?i)(\b(?:access[_-]?token|refresh[_-]?token|id[_-]?token|jwt|api[_-]?key|"
    r"client[_-]?secret|password|passwd|passphrase|secret(?:[_-]?key)?|private[_-]?key|"
    r"authorization|session[_-]?id|credential|aws_secret_access_key|token|session|sid|auth|signature|sig|client[_-]?id)\b\s*[:=]\s*)"
    r"(\"[^\"]*\"|'[^']*'|[^\s,;]+(?:\s+[^\s,;]+)?)"
)
_BEARER_RE = re.compile(r"(?i)\b(Bearer|Basic)\s+[A-Za-z0-9._~+/=-]{6,}")
_PRIVATE_KEY_RE = re.compile(
    r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----.*?-----END (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----",
    re.S,
)
_COOKIE_LINE_RE = re.compile(r"(?im)(\b(?:cookie|set-cookie)\s*:\s*)[^\r\n]+")


def _normalized_name(name: str) -> str:
    return re.sub(r"[-.\s]+", "_", str(name).strip().lower())


def _is_sensitive_name(name: str) -> bool:
    normalized = _normalized_name(name)
    return normalized in SENSITIVE_QUERY_NAMES or normalized in SENSITIVE_FIELD_NAMES


def contains_sensitive_query(url: str) -> bool:
    try:
        return any(_is_sensitive_name(k) and bool(v) for k, v in parse_qsl(urlsplit(url).query, keep_blank_values=True))
    except Exception:
        return False


def redact_url(url: str) -> str:
    """Redact query secrets, including secrets inside nested URL parameters.

    Redirect/return/next parameters often contain a URL whose own query can carry
    OAuth codes or session tokens. Redacting only the outer query misses those values.
    Recursion is deliberately bounded to keep malformed deeply nested inputs cheap.
    """
    return _redact_url(str(url), depth=0)


def _redact_url(url: str, depth: int) -> str:
    try:
        p = urlsplit(url)
        pairs = []
        for key, value in parse_qsl(p.query, keep_blank_values=True):
            if _is_sensitive_name(key):
                safe_value = "[REDACTED]"
            elif depth < 8:
                # Redirect/return URL parameters are frequently URL-encoded several
                # times. Decode only to recognize a nested absolute URL, redact it,
                # then let urlencode re-encode it in the containing URL.
                nested = value
                recognized = False
                for _ in range(8):
                    try:
                        candidate = urlsplit(nested)
                    except Exception:
                        break
                    if candidate.scheme.lower() in {"http", "https"} and candidate.hostname:
                        recognized = True
                        break
                    decoded = unquote(nested)
                    if decoded == nested:
                        break
                    nested = decoded
                safe_value = _redact_url(nested, depth + 1) if recognized else value
            else:
                safe_value = value
            pairs.append((key, safe_value))
        # Never preserve username/password in a URL's authority.
        hostname = p.hostname or ""
        if ":" in hostname and not hostname.startswith("["):
            hostname = f"[{hostname}]"
        try:
            port = p.port
        except ValueError:
            return "[URL REDACTED]"
        netloc = f"{hostname}:{port}" if port is not None else hostname
        return urlunsplit((p.scheme, netloc, p.path, urlencode(pairs, doseq=True), ""))
    except Exception:
        return "[URL REDACTED]"


def redact_text(value: str) -> str:
    """Redact common credential forms in free text and log/evidence snippets."""
    try:
        text = str(value)
        text = _PRIVATE_KEY_RE.sub("[PRIVATE KEY REDACTED]", text)
        text = _COOKIE_LINE_RE.sub(lambda m: m.group(1) + "[REDACTED]", text)
        text = _BEARER_RE.sub(lambda m: m.group(1) + " [REDACTED]", text)
        text = _ASSIGNMENT_RE.sub(lambda m: m.group(1) + "[REDACTED]", text)
        # Inline URLs often appear inside browser/errors rather than as whole values.
        def replace_url(match):
            return redact_url(match.group(0))
        text = re.sub(r"https?://[^\s\"'<>]+", replace_url, text, flags=re.I)
        return text
    except Exception:
        return "[REDACTED]"


def redact_data(value):
    if isinstance(value, dict):
        return {k: ("[REDACTED]" if _is_sensitive_name(str(k)) else redact_data(v)) for k, v in value.items()}
    if isinstance(value, list):
        return [redact_data(x) for x in value]
    if isinstance(value, tuple):
        return [redact_data(x) for x in value]
    if isinstance(value, str):
        if value.startswith(("http://", "https://")):
            return redact_url(value)
        return redact_text(value)
    return value
