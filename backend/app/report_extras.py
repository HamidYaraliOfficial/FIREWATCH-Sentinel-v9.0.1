from __future__ import annotations
import csv, io, json, re, html
from datetime import datetime, timezone
from .version import VERSION

def finding_rows(scan, findings):
    rows=[]
    for f in findings:
        rows.append({"scan_id":scan.id,"target":scan.target_url,"finding_id":f.id,"rule_id":f.rule_id,"category":f.category,"title":f.title,"severity":f.severity.value,"confidence":round(float(f.confidence),4),"risk_score":round(float(f.risk_score),2),"status":f.status.value,"endpoint":f.endpoint,"description":f.description,"impact":f.impact,"evidence":f.evidence_summary,"remediation":f.remediation,"references":f.references})
    return rows

def _spreadsheet_safe(value):
    """Prevent spreadsheet formula execution when analysts open CSV exports."""
    if not isinstance(value, str):
        return value
    candidate = value.lstrip('\ufeff\x00\t\r\n ')
    if candidate.startswith(('=', '+', '-', '@')):
        return "'" + value
    return value


def render_csv(scan, findings, output_path):
    rows=finding_rows(scan,findings); fields=list(rows[0].keys()) if rows else ["scan_id","target","finding_id","rule_id","category","title","severity","confidence","risk_score","status","endpoint","description","impact","evidence","remediation","references"]
    with open(output_path,'w',newline='',encoding='utf-8-sig') as fh:
        w=csv.DictWriter(fh,fieldnames=fields); w.writeheader()
        for row in rows:
            row['references']=' | '.join(row['references']) if isinstance(row.get('references'),list) else row.get('references','')
            w.writerow({key: _spreadsheet_safe(value) for key,value in row.items()})

def _markdown_text(value):
    """Escape untrusted prose so raw HTML and Markdown links are not interpreted."""
    text = html.escape(str(value), quote=False)
    for char in ("\\", "`", "*", "_", "[", "]", "(", ")", "#", "+", "-", "!", "|", ">"):
        text = text.replace(char, "\\" + char)
    return text


def _markdown_code(value):
    """Escape HTML and code delimiters while preserving ordinary code identifiers."""
    return html.escape(str(value), quote=False).replace("`", "&#96;")

def render_markdown(scan, findings, coverage, output_path):
    counts={s:sum(1 for f in findings if f.severity.value==s) for s in ('critical','high','medium','low','info')}
    out=["# FIREWATCH Sentinel Security Assessment Report","",f"- **Target:** `{_markdown_code(scan.target_url)}`",f"- **Scan ID:** `{_markdown_code(scan.id)}`",f"- **Status:** `{_markdown_code(scan.status.value)}`",f"- **Generated (UTC):** `{datetime.now(timezone.utc).isoformat()}`","", "## Summary", "", " | ".join(f"{k.title()}: {v}" for k,v in counts.items()), "", "## Findings", ""]
    if not findings: out.append("No findings were recorded. This does not prove the target is vulnerability-free.")
    for f in findings:
        out.extend([f"### [{f.severity.value.upper()}] {_markdown_text(f.title)}","",f"- **Rule:** `{_markdown_code(f.rule_id)}`",f"- **Confidence:** {f.confidence:.0%}",f"- **Risk score:** {f.risk_score}",f"- **Endpoint:** `{_markdown_code(f.endpoint)}`",f"- **Status:** `{_markdown_code(f.status.value)}`","",_markdown_text(f.description),"",f"**Impact:** {_markdown_text(f.impact)}","",f"**Evidence:** {_markdown_text(f.evidence_summary)}","",f"**Remediation:** {_markdown_text(f.remediation)}","",f"**References:** {_markdown_text(', '.join(f.references or []))}",""])
    out.extend(["## Test coverage events","", "| Phase | Progress | Details |", "|---|---:|---|"])
    for item in coverage: out.append(f"| {_markdown_text(item.get('phase',''))} | {item.get('progress',0)}% | {_markdown_text(item.get('details',''))} |")
    with open(output_path,'w',encoding='utf-8') as fh: fh.write('\n'.join(out)+'\n')

def render_sarif(scan, findings, output_path):
    results=[]
    rules={}
    levels={'critical':'error','high':'error','medium':'warning','low':'note','info':'note'}
    for f in findings:
        rules[f.rule_id]={'id':f.rule_id,'name':f.title,'shortDescription':{'text':f.title},'fullDescription':{'text':f.description},'help':{'text':f.remediation},'properties':{'category':f.category,'severity':f.severity.value,'confidence':f.confidence,'references':f.references}}
        results.append({'ruleId':f.rule_id,'level':levels.get(f.severity.value,'note'),'message':{'text':f'{f.description} Evidence: {f.evidence_summary}'},'locations':[{'physicalLocation':{'artifactLocation':{'uri':f.endpoint}}}],'properties':{'findingId':f.id,'riskScore':f.risk_score,'status':f.status.value,'target':scan.target_url}})
    payload={'$schema':'https://json.schemastore.org/sarif-2.1.0.json','version':'2.1.0','runs':[{'tool':{'driver':{'name':'FIREWATCH Sentinel','informationUri':'https://owasp.org/','version':VERSION,'rules':list(rules.values())}},'results':results,'properties':{'scanId':scan.id,'target':scan.target_url}}]}
    with open(output_path,'w',encoding='utf-8') as fh: json.dump(payload,fh,ensure_ascii=False,indent=2)
