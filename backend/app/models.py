from __future__ import annotations
import enum,uuid
from datetime import datetime,timezone
from typing import Any
from sqlalchemy import DateTime,Enum,Float,ForeignKey,Integer,JSON,String,Text,UniqueConstraint,Boolean
from sqlalchemy.orm import Mapped,mapped_column,relationship
from .db import Base

def now_utc(): return datetime.now(timezone.utc)
def uid(): return str(uuid.uuid4())
class ScanStatus(str,enum.Enum): QUEUED='queued'; RUNNING='running'; COMPLETED='completed'; FAILED='failed'; CANCELED='canceled'
class Severity(str,enum.Enum): CRITICAL='critical'; HIGH='high'; MEDIUM='medium'; LOW='low'; INFO='info'
class FindingStatus(str,enum.Enum): OPEN='open'; VERIFIED='verified'; FALSE_POSITIVE='false_positive'; ACCEPTED='accepted'
class Project(Base):
    __tablename__='projects'
    id:Mapped[str]=mapped_column(String(36),primary_key=True,default=uid); name:Mapped[str]=mapped_column(String(200)); description:Mapped[str|None]=mapped_column(Text,nullable=True); created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=now_utc)
    scans:Mapped[list['Scan']]=relationship(back_populates='project',cascade='all, delete-orphan')
class Scan(Base):
    __tablename__='scans'
    id:Mapped[str]=mapped_column(String(36),primary_key=True,default=uid); project_id:Mapped[str|None]=mapped_column(ForeignKey('projects.id'),nullable=True,index=True); target_url:Mapped[str]=mapped_column(String(2048)); status:Mapped[ScanStatus]=mapped_column(Enum(ScanStatus),default=ScanStatus.QUEUED,index=True); config:Mapped[dict[str,Any]]=mapped_column(JSON,default=dict); error:Mapped[str|None]=mapped_column(Text,nullable=True); started_at:Mapped[datetime|None]=mapped_column(DateTime(timezone=True),nullable=True); finished_at:Mapped[datetime|None]=mapped_column(DateTime(timezone=True),nullable=True); created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=now_utc,index=True)
    project:Mapped[Project|None]=relationship(back_populates='scans'); pages:Mapped[list['Page']]=relationship(back_populates='scan',cascade='all, delete-orphan'); assets:Mapped[list['Asset']]=relationship(back_populates='scan',cascade='all, delete-orphan'); findings:Mapped[list['Finding']]=relationship(back_populates='scan',cascade='all, delete-orphan'); events:Mapped[list['ScanEvent']]=relationship(back_populates='scan',cascade='all, delete-orphan'); reports:Mapped[list['Report']]=relationship(back_populates='scan',cascade='all, delete-orphan'); lease:Mapped['WorkerLease|None']=relationship(back_populates='scan',cascade='all, delete-orphan',uselist=False)
class WorkerLease(Base):
    """Heartbeat lease for a scan claimed by an external worker process."""
    __tablename__ = "worker_leases"
    scan_id: Mapped[str] = mapped_column(ForeignKey("scans.id", ondelete="CASCADE"), primary_key=True)
    worker_id: Mapped[str] = mapped_column(String(160), index=True)
    heartbeat_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now_utc, index=True)
    scan: Mapped[Scan] = relationship(back_populates="lease")


class Page(Base):
    __tablename__='pages'
    id:Mapped[str]=mapped_column(String(36),primary_key=True,default=uid); scan_id:Mapped[str]=mapped_column(ForeignKey('scans.id'),index=True); url:Mapped[str]=mapped_column(String(2048)); method:Mapped[str]=mapped_column(String(16),default='GET'); status_code:Mapped[int|None]=mapped_column(Integer,nullable=True); content_type:Mapped[str|None]=mapped_column(String(200),nullable=True); title:Mapped[str|None]=mapped_column(String(500),nullable=True); depth:Mapped[int]=mapped_column(Integer,default=0); headers:Mapped[dict[str,Any]]=mapped_column(JSON,default=dict); links:Mapped[list[Any]]=mapped_column(JSON,default=list); resources:Mapped[list[Any]]=mapped_column(JSON,default=list); technologies:Mapped[list[Any]]=mapped_column(JSON,default=list); body_sha256:Mapped[str|None]=mapped_column(String(64),nullable=True); fetched_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=now_utc)
    scan:Mapped[Scan]=relationship(back_populates='pages')
class Asset(Base):
    __tablename__='assets'
    id:Mapped[str]=mapped_column(String(36),primary_key=True,default=uid); scan_id:Mapped[str]=mapped_column(ForeignKey('scans.id'),index=True); url:Mapped[str]=mapped_column(String(2048)); kind:Mapped[str]=mapped_column(String(60),index=True); method:Mapped[str]=mapped_column(String(16),default='GET'); status_code:Mapped[int|None]=mapped_column(Integer,nullable=True); content_type:Mapped[str|None]=mapped_column(String(200),nullable=True); source:Mapped[str]=mapped_column(String(120),default='crawler'); authenticated:Mapped[bool]=mapped_column(Boolean,default=False); metadata_json:Mapped[dict[str,Any]]=mapped_column(JSON,default=dict)
    scan:Mapped[Scan]=relationship(back_populates='assets')
class Finding(Base):
    __tablename__='findings'; __table_args__=(UniqueConstraint('scan_id','dedupe_key',name='uq_finding_scan_dedupe'),)
    id:Mapped[str]=mapped_column(String(36),primary_key=True,default=uid); scan_id:Mapped[str]=mapped_column(ForeignKey('scans.id'),index=True); rule_id:Mapped[str]=mapped_column(String(120),index=True); category:Mapped[str]=mapped_column(String(100),index=True); title:Mapped[str]=mapped_column(String(500)); severity:Mapped[Severity]=mapped_column(Enum(Severity),index=True); confidence:Mapped[float]=mapped_column(Float); risk_score:Mapped[float]=mapped_column(Float); status:Mapped[FindingStatus]=mapped_column(Enum(FindingStatus),default=FindingStatus.OPEN); endpoint:Mapped[str]=mapped_column(String(2048)); description:Mapped[str]=mapped_column(Text); impact:Mapped[str]=mapped_column(Text); remediation:Mapped[str]=mapped_column(Text); references:Mapped[list[Any]]=mapped_column(JSON,default=list); evidence_summary:Mapped[str]=mapped_column(Text); dedupe_key:Mapped[str]=mapped_column(String(500),index=True); created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=now_utc)
    evidence:Mapped[list['Evidence']]=relationship(back_populates='finding',cascade='all, delete-orphan'); scan:Mapped[Scan]=relationship(back_populates='findings')
class Evidence(Base):
    __tablename__='evidence'
    id:Mapped[str]=mapped_column(String(36),primary_key=True,default=uid); finding_id:Mapped[str]=mapped_column(ForeignKey('findings.id'),index=True); kind:Mapped[str]=mapped_column(String(80)); data:Mapped[dict[str,Any]]=mapped_column(JSON,default=dict); created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=now_utc); finding:Mapped[Finding]=relationship(back_populates='evidence')
class ScanEvent(Base):
    __tablename__='scan_events'
    id:Mapped[str]=mapped_column(String(36),primary_key=True,default=uid); scan_id:Mapped[str]=mapped_column(ForeignKey('scans.id'),index=True); phase:Mapped[str]=mapped_column(String(80),index=True); message:Mapped[str]=mapped_column(String(1000)); progress:Mapped[float]=mapped_column(Float,default=0); created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=now_utc); scan:Mapped[Scan]=relationship(back_populates='events')
class Report(Base):
    __tablename__='reports'
    id:Mapped[str]=mapped_column(String(36),primary_key=True,default=uid); scan_id:Mapped[str]=mapped_column(ForeignKey('scans.id'),index=True); format:Mapped[str]=mapped_column(String(20)); path:Mapped[str]=mapped_column(String(4096)); created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=now_utc); scan:Mapped[Scan]=relationship(back_populates='reports')

class StandardsChecklistState(Base):
    """Per-project state for the curated standards checklist.

    Control definitions live in the versioned JSON catalog; this table stores only
    reviewer-entered state and never modifies the canonical checklist itself.
    """
    __tablename__ = "standards_checklist_states"
    __table_args__ = (UniqueConstraint("project_key", "control_id", name="uq_standards_project_control"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uid)
    project_key: Mapped[str] = mapped_column(String(120), index=True)
    control_id: Mapped[str] = mapped_column(String(80), index=True)
    status: Mapped[str] = mapped_column(String(32), default="not_assessed")
    owner: Mapped[str | None] = mapped_column(String(160), nullable=True)
    due_date: Mapped[str | None] = mapped_column(String(10), nullable=True)
    evidence_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    evidence_note: Mapped[str | None] = mapped_column(Text, nullable=True)
    reviewer: Mapped[str | None] = mapped_column(String(160), nullable=True)
    last_reviewed: Mapped[str | None] = mapped_column(String(10), nullable=True)
    justification: Mapped[str | None] = mapped_column(Text, nullable=True)
    revision: Mapped[int] = mapped_column(Integer, default=1)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now_utc, index=True)

class StandardsChecklistAudit(Base):
    """Application-level state-transition audit history for standards checklist updates."""
    __tablename__ = "standards_checklist_audit"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=uid)
    project_key: Mapped[str] = mapped_column(String(120), index=True)
    control_id: Mapped[str] = mapped_column(String(80), index=True)
    actor: Mapped[str] = mapped_column(String(160), default="unknown")
    action: Mapped[str] = mapped_column(String(40), default="update")
    previous_state: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    new_state: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now_utc, index=True)
