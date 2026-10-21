from app.crawler import PageSnapshot
from app.http_client import HTTPObservation
from app.checks.registry import run_page_rules

def test_security_checks_find_weak_response():
    url='https://example.com/'
    obs=HTTPObservation(url,url,200,{'server':'Demo/1.0','set-cookie':'session=abc'},'<html><form method="post"><input type="password" name="password"></form><script src="http://cdn.invalid/x.js"></script></html>',3,'text/html','x')
    snap=PageSnapshot(url,0,obs,None,[],[{'action':url,'method':'POST','inputs':[{'name':'password','type':'password'}]}],[],[],['http://cdn.invalid/x.js'])
    ids={f.rule_id for f in run_page_rules(snap,{})}
    assert 'FW-WEB-001' in ids
    assert 'FW-COOKIE-001' in ids
    assert 'FW-FORM-002' in ids
    assert 'FW-WEB-010' in ids
