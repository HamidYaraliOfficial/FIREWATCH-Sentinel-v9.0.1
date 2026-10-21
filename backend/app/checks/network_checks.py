from __future__ import annotations
import ssl, socket
from datetime import datetime, timezone
from urllib.parse import urlparse
from .base import FindingCandidate
from ..models import Severity

def inspect_tls(url):
    out=[]; p=urlparse(url)
    if p.scheme!='https': return out
    try:
        ctx=ssl.create_default_context(); ctx.check_hostname=True
        with socket.create_connection((p.hostname,p.port or 443),timeout=5) as raw:
            with ctx.wrap_socket(raw,server_hostname=p.hostname) as s:
                cert=s.getpeercert(); version=s.version(); cipher=s.cipher()[0] if s.cipher() else None; der=s.getpeercert(binary_form=True)
        if version not in {'TLSv1.3','TLSv1.2'}:
            out.append(FindingCandidate('FW-TLS-001','transport','Unexpected TLS protocol version',Severity.MEDIUM,.98,url,f'TLS connection negotiated {version}.','Legacy protocol versions can provide weaker cryptographic guarantees.','Restrict service-side TLS to modern protocol versions.',f'Negotiated {version}.'))
        if cipher and any(x in cipher.upper() for x in ('RC4','3DES','NULL','EXPORT')):
            out.append(FindingCandidate('FW-TLS-002','transport','Weak TLS cipher negotiated',Severity.HIGH,.98,url,f'The scanner negotiated cipher {cipher}.','Weak cryptographic suites may reduce transport security.','Disable legacy/weak cipher suites at the edge.',f'Negotiated cipher: {cipher}.'))
        if cert.get('notAfter'):
            expiry=datetime.fromtimestamp(ssl.cert_time_to_seconds(cert['notAfter']),timezone.utc)
            days=(expiry-datetime.now(timezone.utc)).total_seconds()/86400
            if days<0:
                out.append(FindingCandidate('FW-TLS-003','transport','TLS certificate appears expired',Severity.HIGH,.99,url,f'The validated certificate expired {abs(int(days))} day(s) ago.','Clients may reject the connection or users may be exposed to trust warnings.','Renew and deploy a valid certificate chain.',f'Certificate notAfter: {cert["notAfter"]}.',evidence={'days_until_expiry':round(days,2)}))
            elif days<30:
                out.append(FindingCandidate('FW-TLS-003','transport','TLS certificate expires soon',Severity.MEDIUM,.97,url,f'The validated certificate expires in approximately {int(days)} day(s).','An expired certificate can break availability and user trust.','Renew the certificate and verify automated renewal/monitoring.',f'Certificate notAfter: {cert["notAfter"]}.',evidence={'days_until_expiry':round(days,2)}))
        try:
            from cryptography import x509
            cert_obj=x509.load_der_x509_certificate(der); pub=cert_obj.public_key(); key_size=getattr(pub,'key_size',None)
            if key_size and key_size<2048:
                out.append(FindingCandidate('FW-TLS-004','transport','TLS certificate uses a small public key',Severity.HIGH,.98,url,f'The certificate public key size is {key_size} bits.','A weak public key can reduce cryptographic security.','Replace with an appropriately sized key (for RSA, typically at least 2048 bits) or a modern supported elliptic-curve key.',f'Certificate public key size: {key_size} bits.',evidence={'key_size':key_size}))
        except Exception: pass
    except ssl.SSLCertVerificationError as exc:
        out.append(FindingCandidate('FW-TLS-004','transport','TLS certificate validation failed',Severity.HIGH,.98,url,'The TLS client could not validate the certificate hostname/trust chain.','Users and clients may reject the connection; disabling verification would create interception risk.','Deploy a certificate valid for the target hostname with a trusted complete chain.',f'Certificate validation exception: {type(exc).__name__}.'))
    except Exception as exc:
        out.append(FindingCandidate('FW-TLS-005','transport','TLS inspection could not be completed',Severity.INFO,.95,url,'The agent could not complete direct TLS inspection from its runtime.','Transport posture could not be fully evaluated.','Run assessment from a network position that can resolve and reach the target.',f'TLS inspection exception type: {type(exc).__name__}.'))
    return out
