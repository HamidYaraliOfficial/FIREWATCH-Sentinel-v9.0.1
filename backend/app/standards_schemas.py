"""Validation schemas for the standards checklist tracking API."""
from __future__ import annotations
import re
from typing import Literal
from urllib.parse import urlsplit
from pydantic import BaseModel, Field, field_validator, model_validator
from .redaction import contains_sensitive_query

ChecklistStatus = Literal[
    "not_assessed", "compliant", "partially_compliant", "non_compliant",
    "not_applicable", "blocked", "evidence_pending",
]
_PROJECT_KEY = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,119}$")
_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

class ChecklistUpdate(BaseModel):
    project_key: str = Field(default="default", min_length=1, max_length=120)
    status: ChecklistStatus
    expected_revision: int = Field(default=0, ge=0)
    owner: str | None = Field(default=None, max_length=160)
    due_date: str | None = Field(default=None, max_length=10)
    evidence_url: str | None = Field(default=None, max_length=2048)
    evidence_note: str | None = Field(default=None, max_length=4000)
    reviewer: str | None = Field(default=None, max_length=160)
    last_reviewed: str | None = Field(default=None, max_length=10)
    justification: str | None = Field(default=None, max_length=2000)
    updated_by: str = Field(default="api-user", min_length=1, max_length=160)

    @field_validator("project_key")
    @classmethod
    def safe_project_key(cls, value: str) -> str:
        value = value.strip()
        if not _PROJECT_KEY.fullmatch(value):
            raise ValueError("project_key may contain only letters, digits, dot, underscore, colon and hyphen")
        return value

    @field_validator("due_date", "last_reviewed")
    @classmethod
    def valid_iso_date(cls, value: str | None) -> str | None:
        if value in (None, ""):
            return None
        if not _DATE.fullmatch(value):
            raise ValueError("Date must use YYYY-MM-DD format")
        from datetime import date
        try:
            date.fromisoformat(value)
        except ValueError as exc:
            raise ValueError("Invalid calendar date") from exc
        return value

    @field_validator("evidence_url")
    @classmethod
    def safe_evidence_url(cls, value: str | None) -> str | None:
        if value in (None, ""):
            return None
        value = value.strip()
        parsed = urlsplit(value)
        if parsed.scheme not in {"https", "http"} or not parsed.hostname:
            raise ValueError("evidence_url must be an absolute HTTP(S) URL")
        if parsed.username is not None or parsed.password is not None:
            raise ValueError("User-info is forbidden in evidence URLs")
        if contains_sensitive_query(value):
            raise ValueError("Evidence URLs must not contain token/password/signature query parameters")
        try:
            if parsed.port is not None and not 1 <= parsed.port <= 65535:
                raise ValueError("Invalid port in evidence URL")
        except ValueError as exc:
            raise ValueError("Invalid port in evidence URL") from exc
        return value

    @model_validator(mode="after")
    def trim_text(self):
        for attr in ("owner", "reviewer", "evidence_note", "justification", "updated_by"):
            value = getattr(self, attr)
            if isinstance(value, str):
                setattr(self, attr, value.strip())
        return self
