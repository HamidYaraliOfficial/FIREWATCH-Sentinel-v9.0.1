from __future__ import annotations
from hashlib import sha256
from urllib.parse import urlsplit,urlunsplit
from .checks.base import FindingCandidate

def normalize_candidate(c:FindingCandidate):
    endpoint=urlunsplit(urlsplit(c.endpoint)._replace(fragment=''))
    key=sha256(f'{c.rule_id}|{endpoint}|{c.evidence_summary[:300]}'.encode()).hexdigest()
    return type('Normalized',(),{'dedupe_key':key})

def redact_headers(headers:dict[str,str]):
    sensitive=('authorization','cookie','set-cookie','x-api-key','proxy-authorization')
    return {k:('[REDACTED]' if k.lower() in sensitive else v) for k,v in headers.items()}
