import ssl
import socket
import time
from datetime import datetime, timezone, timedelta
from unittest.mock import patch
import pytest
from app.checks.network_checks import inspect_tls

def cert_time(delta_seconds):
    return time.strftime('%b %d %H:%M:%S %Y GMT', time.gmtime(time.time()+delta_seconds))

class FakeSSLSocket:
    def __init__(self, version='TLSv1.3', cipher='TLS_AES_256_GCM_SHA384', cert=None, der=b'invalid'):
        self._version=version; self._cipher=cipher; self._cert=cert or {}; self._der=der
    def __enter__(self): return self
    def __exit__(self,*_): return None
    def version(self): return self._version
    def cipher(self): return (self._cipher,'TLSv1.2',256)
    def getpeercert(self,binary_form=False): return self._der if binary_form else self._cert

class FakeRawSocket:
    def __enter__(self): return self
    def __exit__(self,*_): return None

class FakeContext:
    def __init__(self,wrapped): self.check_hostname=False; self._wrapped=wrapped
    def wrap_socket(self,raw,server_hostname=None): return self._wrapped

def run_with_fake_tls(monkeypatch,wrapped,url='https://example.test/'):
    monkeypatch.setattr('app.checks.network_checks.ssl.create_default_context',lambda:FakeContext(wrapped))
    monkeypatch.setattr('app.checks.network_checks.socket.create_connection',lambda *a,**kw:FakeRawSocket())
    return inspect_tls(url)

def test_tls_skips_plain_http_without_network_calls(monkeypatch):
    def fail(*_a,**_k): raise AssertionError('plain HTTP must not invoke TLS socket')
    monkeypatch.setattr('app.checks.network_checks.socket.create_connection',fail)
    assert inspect_tls('http://example.test/')==[]

@pytest.mark.parametrize('exception,expected_rule',[
 (ssl.SSLCertVerificationError('untrusted'),'FW-TLS-004'),
 (OSError('offline'),'FW-TLS-005'),
 (TimeoutError('timeout'),'FW-TLS-005'),
 (socket.gaierror('dns'),'FW-TLS-005'),
])
def test_tls_errors_become_bounded_observations(monkeypatch,exception,expected_rule):
    monkeypatch.setattr('app.checks.network_checks.ssl.create_default_context',lambda:(_ for _ in ()).throw(exception))
    findings=inspect_tls('https://example.test/')
    assert any(f.rule_id==expected_rule for f in findings)

@pytest.mark.parametrize('version,cipher',[
 ('TLSv1','TLS_RSA_WITH_3DES_EDE_CBC_SHA'),
 ('SSLv3','TLS_RSA_WITH_NULL_SHA'),
])
def test_tls_flags_legacy_protocol_and_weak_cipher(monkeypatch,version,cipher):
    fake=FakeSSLSocket(version=version,cipher=cipher,cert={'notAfter':cert_time(365*24*3600)})
    findings=run_with_fake_tls(monkeypatch,fake)
    rule_ids={f.rule_id for f in findings}
    assert 'FW-TLS-001' in rule_ids
    assert 'FW-TLS-002' in rule_ids

def test_tls_flags_expired_certificate(monkeypatch):
    fake=FakeSSLSocket(cert={'notAfter':cert_time(-2*24*3600)})
    findings=run_with_fake_tls(monkeypatch,fake)
    assert any(f.rule_id=='FW-TLS-003' and 'expired' in f.title.lower() for f in findings)

def test_tls_flags_certificate_expiring_soon(monkeypatch):
    fake=FakeSSLSocket(cert={'notAfter':cert_time(5*24*3600)})
    findings=run_with_fake_tls(monkeypatch,fake)
    assert any(f.rule_id=='FW-TLS-003' and 'expires soon' in f.title.lower() for f in findings)
