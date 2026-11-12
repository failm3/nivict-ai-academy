"""Read-only pattern scan of deliverables; writes redacted findings in QA only.

This detects candidate secrets/PII; it is not a guarantee that none exist.
Never prints matched values. Rerun after final artifacts are assembled.
"""
import collections
import hashlib
import json
import re
from pathlib import Path

OUT=Path(__file__).resolve().parents[1]
QA=Path(__file__).resolve().parent
REPORT=QA/'PUBLICATION-SCAN.json'
PATTERNS={
 'PRIVATE_KEY_MARKER':re.compile(r'-----BEGIN (?:RSA |EC |DSA |OPENSSH |ENCRYPTED )?PRIVATE KEY-----'),
 'GITHUB_TOKEN':re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})\b'),
 'OPENAI_STYLE_TOKEN':re.compile(r'\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{30,}\b'),
 'AWS_ACCESS_KEY_ID':re.compile(r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'),
 'GOOGLE_API_KEY':re.compile(r'\bAIza[A-Za-z0-9_-]{35}\b'),
 'SLACK_TOKEN':re.compile(r'\bxox[baprs]-[A-Za-z0-9-]{20,}\b'),
 'EMAIL_ADDRESS':re.compile(r'(?i)(?<![A-Z0-9._%+-])[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}(?![A-Z0-9.-])'),
 'PHONE_URI':re.compile(r'(?i)\btel:\+?[0-9][0-9() .-]{6,18}'),
 'INTERNATIONAL_PHONE_CANDIDATE':re.compile(r'(?<!\w)\+[1-9](?:[ ()-]*\d){9,14}(?!\d)'),
 'GENERIC_CREDENTIAL_ASSIGNMENT':re.compile(r'''(?i)["']?(?:api[_-]?key|client[_-]?secret|access[_-]?token|auth[_-]?token|password|secret[_-]?key)["']?\s*[:=]\s*["']([A-Za-z0-9/+_=-]{16,})["']'''),
 'URL_USERINFO':re.compile(r'(?i)https?://[^\s/"<>]+:[^\s/@"<>]+@[^\s/"<>]+'),
 'SENSITIVE_QUERY_PARAM':re.compile(r'(?i)(?:[?&]|&amp;)(?:api[_-]?key|client[_-]?secret|access[_-]?token|auth[_-]?token|password)=([^&#\s"<>]{12,})'),
}

def classify(kind,value):
    low=value.lower()
    if kind=='EMAIL_ADDRESS':
        if any(x in low for x in ('example.com','example.org','your-email','your_email','email@','user@','test@','username@','name@')):
            return 'DOCUMENTATION_PLACEHOLDER'
        return 'CONTACT_ADDRESS_REVIEW_SOURCE_CONTEXT'
    if any(x in low for x in ('your_key','your-key','your_token','your-token','placeholder','example','insert','redacted')):
        return 'DOCUMENTATION_PLACEHOLDER'
    if kind=='URL_USERINFO' and ('$' in value or '{' in value or '<' in value):
        return 'DOCUMENTATION_PLACEHOLDER'
    return 'REVIEW_REQUIRED'

def main():
    results=[]; files=[]
    suffixes={'.md','.json','.jsonl','.csv','.py','.txt','.ps1','.mjs','.yaml','.yml'}
    for p in sorted(OUT.rglob('*')):
        if not p.is_file() or p==REPORT or p.suffix.lower() not in suffixes: continue
        b=p.read_bytes()
        try: text=b.decode('utf-8-sig')
        except UnicodeDecodeError: continue
        rel=p.relative_to(OUT).as_posix()
        files.append({'path':rel,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
        for number,line in enumerate(text.splitlines(),1):
            sid=None
            if p.suffix.lower()=='.jsonl':
                try:
                    row=json.loads(line); sid=row.get('source_id',row.get('manus_id',row.get('id')))
                except json.JSONDecodeError: pass
            for kind,pattern in PATTERNS.items():
                for m in pattern.finditer(line):
                    value=m.group(0)
                    results.append({'path':rel,'line':number,'record_id':sid,'kind':kind,'classification':classify(kind,value),'value_sha256_prefix':hashlib.sha256(value.encode()).hexdigest()[:16],'matched_value':'REDACTED'})
    report={'status':'PATTERN_SCAN_COMPLETED_REVIEW_REQUIRED_IF_FINDINGS','checked_at':'2026-11-12','scope':'All UTF-8 text artifacts currently under outputs; excludes this report and binary archives. Does not scan private credential stores or live services. Snapshot only; rerun after final PR staging.','files_scanned':len(files),'bytes_scanned':sum(x['bytes'] for x in files),'rules':list(PATTERNS),'findings_by_kind':dict(collections.Counter(r['kind'] for r in results)),'findings_by_classification':dict(collections.Counter(r['classification'] for r in results)),'findings':results,'snapshot_files':files,'limitations':['Pattern scan cannot establish absence of all secrets or PII.','Public source contact addresses still require publication-scope review; source preservation must not be silently altered.','No matched values are included in this report or terminal output.','No values are validated against live providers.']}
    REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('files_scanned','bytes_scanned','findings_by_kind','findings_by_classification')},ensure_ascii=False))

if __name__=='__main__': main()
