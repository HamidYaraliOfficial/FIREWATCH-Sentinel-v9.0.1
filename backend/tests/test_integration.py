import json, os, subprocess, sys, time
from pathlib import Path

def test_cli_end_to_end_local_demo(tmp_path):
    root=Path(__file__).resolve().parents[2]
    env=dict(os.environ)
    env.update({'ALLOW_PRIVATE_TARGETS':'true','DATABASE_URL':f"sqlite:///{tmp_path/'firewatch.db'}",'REPORT_DIR':str(tmp_path/'reports'),'PYTHONPATH':'backend'})
    demo=subprocess.Popen([sys.executable,'-m','uvicorn','demo_target.main:app','--host','127.0.0.1','--port','8766'],cwd=root,env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    try:
        time.sleep(1)
        r=subprocess.run([sys.executable,'-m','app.cli','http://127.0.0.1:8766/','--pages','25','--depth','3','--endpoints','100','--delay','0','--no-browser'],cwd=root,env=env,capture_output=True,text=True,timeout=60)
        assert r.returncode==0, r.stdout+'\n'+r.stderr
        reports=list((tmp_path/'reports').rglob('report.json')); assert reports
        payload=json.loads(reports[0].read_text())
        assert payload['meta']['status']=='completed'
        assert len(payload['findings'])>=10
        assert 'coverage_catalog' in payload
        report_dir=reports[0].parent
        assert (report_dir/'report.html').is_file()
        assert (report_dir/'findings.csv').is_file()
        assert (report_dir/'report.md').is_file()
        sarif=json.loads((report_dir/'report.sarif.json').read_text())
        assert sarif['version']=='2.1.0' and sarif['runs'][0]['results']
    finally:
        demo.terminate(); demo.wait(timeout=5)
