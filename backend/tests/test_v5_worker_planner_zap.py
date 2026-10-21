import asyncio, json
from pathlib import Path
from unittest.mock import patch
import pytest, yaml
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.db import Base
from app.models import Scan, ScanStatus, Asset, Finding, Evidence, Severity
from app.planner import PlannerProtocol
from app.zap import ZAPAdapter

@pytest.mark.parametrize('browser,zap,passive,expected_browser,expected_zap',[
 (True,True,False,True,True),(True,True,True,False,False),(True,False,False,True,False),
 (False,True,False,False,True),(False,False,False,False,False),(True,False,True,False,False),
])
def test_planner_never_enables_optional_actions_in_passive_mode(browser,zap,passive,expected_browser,expected_zap):
    plan=PlannerProtocol().plan(enable_browser=browser,enable_zap=zap,passive_only=passive)
    assert plan.rule_engine is True
    assert plan.browser_discovery is expected_browser
    assert plan.zap is expected_zap

@pytest.mark.parametrize('base', ['file:///etc/passwd','ftp://zap:8080','https:///missing','http://user:pass@zap:8080','http://zap:99999','http://zap:8080/?x=1'])
def test_zap_rejects_invalid_base_urls(base,tmp_path):
    with pytest.raises(ValueError): ZAPAdapter(base, str(tmp_path))

def test_zap_plan_is_valid_yaml_and_target_is_data_not_injected(tmp_path):
    target='https://app.example.test/a?x=one:two#section'
    adapter=ZAPAdapter('http://zap:8080',str(tmp_path))
    plan=adapter.write_plan(target)
    parsed=yaml.safe_load(Path(plan.plan_path).read_text())
    context=parsed['env']['contexts'][0]
    assert context['urls']==[target]
    assert context['name']=='FIREWATCH'
    assert parsed['jobs'][0]['type']=='passiveScan-wait'

def test_zap_health_returns_false_on_connection_error(tmp_path):
    adapter=ZAPAdapter('http://zap:8080',str(tmp_path))
    with patch('app.zap.urllib.request.urlopen',side_effect=OSError('offline')):
        assert adapter.health() is False

def test_zap_health_accepts_valid_version_payload(tmp_path):
    adapter=ZAPAdapter('http://zap:8080',str(tmp_path))
    class Response:
        def __enter__(self): return self
        def __exit__(self,*args): return None
    response=Response()
    with patch('app.zap.urllib.request.urlopen',return_value=response), patch('app.zap.json.load',return_value={'version':'2.16.0'}):
        assert adapter.health() is True

@pytest.fixture
def db_session(tmp_path,monkeypatch):
    engine=create_engine(f"sqlite:///{tmp_path/'unit.db'}",connect_args={'check_same_thread':False})
    Base.metadata.create_all(engine)
    Session=sessionmaker(bind=engine,autoflush=False,expire_on_commit=False)
    with Session() as db:
        yield db
    engine.dispose()

def test_orchestrator_credential_headers_are_normalized():
    from app.orchestrator import ScanOrchestrator
    scanner=ScanOrchestrator(None)
    assert scanner._headers({'request_headers':{'X-Env':'test'},'auth_cookies':'sid=abc'})=={'X-Env':'test','Cookie':'sid=abc'}
    assert scanner._headers({'request_headers':{'Cookie':'sid=custom'},'auth_cookies':'sid=other'})=={'Cookie':'sid=custom'}

def test_orchestrator_safe_headers_redacts_credentials():
    from app.orchestrator import ScanOrchestrator
    output=ScanOrchestrator(None)._safe_headers({'Authorization':'Bearer secret','set-cookie':'sid=secret','content-type':'application/json'})
    assert output['Authorization']=='[REDACTED]' and output['set-cookie']=='[REDACTED]'
    assert output['content-type']=='application/json'

def test_orchestrator_asset_deduplicates_and_redacts_query_secrets(db_session):
    from app.orchestrator import ScanOrchestrator
    from app.redaction import redact_url
    scan=Scan(target_url='https://app.example.test/',status=ScanStatus.RUNNING,config={})
    db_session.add(scan); db_session.commit()
    runner=ScanOrchestrator(db_session)
    runner._asset(scan,'https://app.example.test/static.js?token=secret','resource',200,'text/javascript','unit',{})
    safe=redact_url('https://app.example.test/static.js?token=secret')
    runner._asset(scan,safe,'resource',200,'text/javascript','unit',{})
    db_session.commit()
    rows=list(db_session.scalars(select(Asset).where(Asset.scan_id==scan.id)))
    assert len(rows)==1 and 'secret' not in rows[0].url

def test_orchestrator_finding_deduplicates_and_records_evidence(db_session):
    from app.orchestrator import ScanOrchestrator
    from app.checks.base import FindingCandidate
    scan=Scan(target_url='https://app.example.test/',status=ScanStatus.RUNNING,config={})
    db_session.add(scan); db_session.commit()
    runner=ScanOrchestrator(db_session)
    candidate=FindingCandidate('FW-UNIT-001','unit','test finding',Severity.LOW,.8,'https://app.example.test/?tab=one','description','impact','fix','observed',evidence={'Authorization':'Bearer secret'})
    runner._store_finding(scan,candidate); runner._store_finding(scan,candidate); db_session.commit()
    findings=list(db_session.scalars(select(Finding).where(Finding.scan_id==scan.id)))
    evidence=list(db_session.scalars(select(Evidence).where(Evidence.finding_id==findings[0].id)))
    assert len(findings)==1 and len(evidence)==1
    assert evidence[0].data['Authorization']=='[REDACTED]'

def test_orchestrator_cancel_checkpoint_is_terminal(db_session):
    from app.orchestrator import ScanOrchestrator
    scan=Scan(target_url='https://app.example.test/',status=ScanStatus.CANCELED,config={})
    db_session.add(scan); db_session.commit()
    runner=ScanOrchestrator(db_session)
    assert runner._cancel_checkpoint(scan) is True
    db_session.refresh(scan)
    assert scan.status==ScanStatus.CANCELED and scan.finished_at is not None

def test_worker_claims_oldest_queued_scan_then_leaves_queue_empty(monkeypatch,db_session):
    import app.worker as worker
    monkeypatch.setattr(worker,'SessionLocal',lambda:db_session)
    first=Scan(target_url='https://one.example.test/',status=ScanStatus.QUEUED,config={})
    second=Scan(target_url='https://two.example.test/',status=ScanStatus.QUEUED,config={})
    db_session.add_all([first,second]); db_session.commit()
    first_id=first.id
    claimed=worker.claim_one()
    assert claimed in {first_id,second.id}
    db_session.refresh(db_session.get(Scan,claimed))
    assert db_session.get(Scan,claimed).status==ScanStatus.RUNNING
    # The single claimed row is no longer QUEUED, so the next claim returns the other row.
    assert worker.claim_one() in {first_id,second.id} - {claimed}
    assert worker.claim_one() is None
