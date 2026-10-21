from __future__ import annotations
from dataclasses import dataclass,field
from typing import Any
from ..models import Severity
@dataclass
class FindingCandidate:
    rule_id:str; category:str; title:str; severity:Severity; confidence:float; endpoint:str; description:str; impact:str; remediation:str; evidence_summary:str; references:list[str]=field(default_factory=list); evidence:dict[str,Any]=field(default_factory=dict)
@dataclass
class CheckContext:
    target_url:str; observations:dict[str,Any]=field(default_factory=dict)
