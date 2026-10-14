#!/usr/bin/env python3
import sys,hashlib,json,datetime
from pathlib import Path
root=Path(sys.argv[2] if len(sys.argv)>2 else '.'); manifest=root/'project-manifest.json'
def files():
 return {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob('*')) if p.is_file() and p.name!='project-manifest.json' and '__pycache__' not in p.parts and p.relative_to(root).parts[0] not in ('.git','exports')}
cmd=sys.argv[1] if len(sys.argv)>1 else 'verify'
if cmd=='init':
 if manifest.exists():raise SystemExit('manifest finns redan')
 obj={'schema_version':1,'project_slug':'digital-omstallning-i-en-foranderlig-omvarld','revision':1,'parent_revision':None,'tracked_files':files(),'last_operation':'init'}
 manifest.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
elif cmd=='revise':
 obj=json.loads(manifest.read_text());obj['parent_revision']=obj['revision'];obj['revision']+=1;obj['tracked_files']=files();obj['last_operation']='revise';manifest.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
elif cmd=='verify':
 obj=json.loads(manifest.read_text());current=files();expected={k:v for k,v in obj['tracked_files'].items() if k.split('/')[0] not in ('.git','exports')};added=set(current)-set(expected);removed=set(expected)-set(current);changed={x for x in current.keys()&expected.keys() if current[x]!=expected[x]}
 if added or removed or changed:raise SystemExit(f'FAIL: added={added}, removed={removed}, changed={changed}')
 print(f'PASS: manifest SHA256, revision {obj["revision"]}, {len(current)} filer')
else:raise SystemExit('Använd init, revise eller verify')
