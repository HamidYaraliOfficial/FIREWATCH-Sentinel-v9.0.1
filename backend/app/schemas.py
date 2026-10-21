from __future__ import annotations
from datetime import datetime
from typing import Any
import re
from pydantic import BaseModel,Field,HttpUrl,ConfigDict,field_validator,model_validator
from .models import ScanStatus,Severity,FindingStatus
from .redaction import contains_sensitive_query

_FORBIDDEN_CUSTOM_HEADERS = {
    "host", "content-length", "transfer-encoding", "connection",
    "proxy-authorization", "proxy-connection", "upgrade", "te", "trailer",
}
_HEADER_NAME_RE = re.compile(r"^[!#$%&'*+.^_`|~0-9A-Za-z-]+$")

def _validate_header_map(headers: dict[str, str], *, context: str) -> dict[str, str]:
    """Validate user-supplied header maps before any HTTP client sees them.

    Header names must use the RFC token alphabet, case-insensitive duplicates are
    rejected to avoid ambiguous Authorization/Cookie interpretation, and control
    characters in values are refused (HTAB is the only accepted control).
    """
    if len(headers) > 50:
        raise ValueError(f"At most 50 {context} headers are allowed")
    normalized: set[str] = set()
    for raw_key, raw_value in headers.items():
        key = str(raw_key)
        value = str(raw_value)
        if (not key or key != key.strip() or len(key) > 100
                or not _HEADER_NAME_RE.fullmatch(key)
                or key.lower() in _FORBIDDEN_CUSTOM_HEADERS):
            raise ValueError(f"Forbidden or invalid {context} header: {key}")
        lowered = key.casefold()
        if lowered in normalized:
            raise ValueError(f"Duplicate case-insensitive {context} header: {key}")
        normalized.add(lowered)
        if len(value) > 8192:
            raise ValueError(f"{context.title()} header values must be at most 8192 characters")
        if any((ord(ch) < 32 and ch != "\t") or ord(ch) == 127 for ch in value):
            raise ValueError(f"Control characters are forbidden in {context} header values")
    return headers

class ScanCreate(BaseModel):
    target_url:HttpUrl; scope_acknowledged:bool=False; project_id:str|None=None

    @field_validator('target_url')
    @classmethod
    def validate_target_url(cls, value):
        # Reject user-info and credential-like query parameters at the API boundary,
        # before a scan request can be persisted or queued.
        if getattr(value, 'username', None) is not None or getattr(value, 'password', None) is not None:
            raise ValueError('Credentials embedded in target URLs are forbidden; use a scoped authentication profile')
        if contains_sensitive_query(str(value)):
            raise ValueError('Credential-like query parameters are refused; test signed/reset URLs under a separate reviewed plan')
        return value
    profile:str=Field('standard',pattern='^(baseline|standard|comprehensive)$')
    max_pages:int=Field(300,ge=1,le=5000); max_depth:int=Field(8,ge=0,le=20); max_endpoints:int=Field(2000,ge=10,le=10000)
    request_delay_ms:int=Field(150,ge=0,le=10000); max_concurrency:int=Field(6,ge=1,le=20)
    enable_browser:bool=True; enable_api_introspection:bool=True; enable_zap:bool=False; enable_safe_parameter_probes:bool=True; passive_only:bool=False; respect_robots:bool=True
    exclusions:list[str]=Field(default_factory=list,max_length=200); allowed_hosts:list[str]=Field(default_factory=list,max_length=20)
    request_headers:dict[str,str]=Field(default_factory=dict); auth_cookies:str|None=None; authorization_profiles:list[dict[str,Any]]=Field(default_factory=list,max_length=10); notes:str|None=None

    @model_validator(mode='before')
    @classmethod
    def defaults_for_profile(cls, values):
        if not isinstance(values,dict): return values
        values=dict(values); profile=values.get('profile','standard')
        presets={
            'baseline': {'max_pages':100,'max_depth':4,'max_endpoints':500,'request_delay_ms':300,'max_concurrency':2,'enable_browser':False,'enable_api_introspection':False,'enable_safe_parameter_probes':False,'passive_only':True},
            'standard': {'max_pages':300,'max_depth':8,'max_endpoints':2000,'request_delay_ms':150,'max_concurrency':4,'enable_browser':True,'enable_api_introspection':True,'enable_safe_parameter_probes':True,'passive_only':False},
            'comprehensive': {'max_pages':1500,'max_depth':12,'max_endpoints':7000,'request_delay_ms':200,'max_concurrency':4,'enable_browser':True,'enable_api_introspection':True,'enable_safe_parameter_probes':True,'passive_only':False},
        }
        for key,value in presets.get(profile,presets['standard']).items(): values.setdefault(key,value)
        return values

    @field_validator('request_headers')
    @classmethod
    def validate_request_headers(cls, value):
        return _validate_header_map(value, context="custom request")

    @field_validator('authorization_profiles')
    @classmethod
    def validate_profiles(cls, value):
        if len(value)>10: raise ValueError('At most 10 authorization profiles are allowed')
        seen_names=set()
        for item in value:
            if not isinstance(item,dict): raise ValueError('Authorization profile must be an object')
            name=str(item.get('name','profile')).strip()
            if not name or len(name)>100: raise ValueError('Authorization profile name must contain 1..100 characters')
            lowered_name=name.casefold()
            if lowered_name in seen_names: raise ValueError('Authorization profile names must be unique (case-insensitive)')
            seen_names.add(lowered_name)
            headers=item.get('headers') or {}
            if not isinstance(headers,dict): raise ValueError('Authorization profile headers are invalid')
            _validate_header_map(headers, context='authorization profile')
        return value
class ScanSummary(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id:str;target_url:str;status:ScanStatus;created_at:datetime;started_at:datetime|None=None;finished_at:datetime|None=None;error:str|None=None
class ScanDetail(ScanSummary): config:dict[str,Any];pages_count:int=0;assets_count:int=0;findings_count:int=0;events_count:int=0
class FindingOut(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id:str;rule_id:str;category:str;title:str;severity:Severity;confidence:float;risk_score:float;status:FindingStatus;endpoint:str;description:str;impact:str;remediation:str;references:list[Any];evidence_summary:str
class EventOut(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id:str;phase:str;message:str;progress:float;created_at:datetime
class AssetOut(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id:str;url:str;kind:str;method:str;status_code:int|None;content_type:str|None;source:str;authenticated:bool;metadata_json:dict[str,Any]
