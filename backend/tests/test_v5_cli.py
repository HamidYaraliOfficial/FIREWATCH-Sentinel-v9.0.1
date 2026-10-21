import asyncio
from pathlib import Path
from types import SimpleNamespace
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base
from app.models import Scan, ScanStatus

@pytest.fixture
def cli_db(tmp_path):
    engine=create_engine(f"sqlite:///{tmp_path/'cli.db'}",connect_args={'check_same_thread':False})
    Base.metadata.create_all(engine)
    session=sessionmaker(bind=engine,autoflush=False,expire_on_commit=False)()
    yield session
    session.close(); engine.dispose()

def test_cli_run_persists_scope_validated_scan_and_reports_paths(monkeypatch,tmp_path,cli_db,capsys):
    import app.cli as cli
    class Policy:
        def validate_url(self,url): return url.rstrip('/')+'/'
    class Runner:
        def __init__(self,db): self.db=db
        async def run(self,scan): scan.status=ScanStatus.COMPLETED; self.db.commit()
    monkeypatch.setattr(cli,'init_db',lambda:None)
    monkeypatch.setattr(cli.ScopePolicy,'from_root',lambda *a,**kw:Policy())
    monkeypatch.setattr(cli,'SessionLocal',lambda:cli_db)
    monkeypatch.setattr(cli,'ScanOrchestrator',Runner)
    monkeypatch.setattr(cli,'settings',SimpleNamespace(allow_private_targets=True,report_dir=str(tmp_path/'reports')))
    asyncio.run(cli.run(SimpleNamespace(url='http://lab.example.test',pages=3,depth=1,endpoints=10,delay=0,no_browser=True,no_graphql=True,passive=True,ignore_robots=True)))
    output=capsys.readouterr().out
    scan=cli_db.query(Scan).one()
    assert scan.target_url=='http://lab.example.test/'
    assert scan.status==ScanStatus.COMPLETED
    assert scan.config['max_pages']==3 and scan.config['passive_only'] is True
    assert str(tmp_path/'reports'/scan.id/'report.html') in output

def test_cli_rejects_invalid_scope_before_creating_database_session(monkeypatch):
    import app.cli as cli
    calls=[]
    class Policy:
        def validate_url(self,url): raise ValueError('out of scope')
    monkeypatch.setattr(cli,'init_db',lambda:None)
    monkeypatch.setattr(cli.ScopePolicy,'from_root',lambda *a,**kw:Policy())
    monkeypatch.setattr(cli,'SessionLocal',lambda: calls.append('opened'))
    monkeypatch.setattr(cli,'settings',SimpleNamespace(allow_private_targets=False,report_dir='reports'))
    with pytest.raises(ValueError,match='out of scope'):
        asyncio.run(cli.run(SimpleNamespace(url='https://bad.example.test/',pages=1,depth=1,endpoints=1,delay=0,no_browser=True,no_graphql=True,passive=True,ignore_robots=False)))
    assert calls==[]

@pytest.mark.parametrize('url',[
 'ftp://example.test','https://user:password@example.test/','https://example.test/?token=secret',
 '\nhttps://example.test/','https://example.test:0/',
])
def test_cli_never_bypasses_the_scope_policy(monkeypatch,url):
    import app.cli as cli
    calls=[]
    def reject(*_args,**_kwargs): raise ValueError('blocked by scope')
    monkeypatch.setattr(cli,'init_db',lambda:None)
    monkeypatch.setattr(cli.ScopePolicy,'from_root',reject)
    monkeypatch.setattr(cli,'SessionLocal',lambda: calls.append('opened'))
    monkeypatch.setattr(cli,'settings',SimpleNamespace(allow_private_targets=False,report_dir='reports'))
    with pytest.raises(ValueError,match='blocked by scope'):
        asyncio.run(cli.run(SimpleNamespace(url=url,pages=1,depth=1,endpoints=1,delay=0,no_browser=True,no_graphql=True,passive=True,ignore_robots=False)))
    assert calls==[]
