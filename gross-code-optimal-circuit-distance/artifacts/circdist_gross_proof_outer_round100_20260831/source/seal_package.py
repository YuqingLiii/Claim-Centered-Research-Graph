#!/usr/bin/env python3
"""Create deterministic inventory and two-level SHA-256 seals."""
from pathlib import Path
import argparse,hashlib,json
parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,required=True);args=parser.parse_args()
root=args.root.resolve(); excluded={'FILE_INVENTORY.jsonl','SHA256SUMS.txt','PAYLOAD_SHA256SUMS.txt'}
for name in excluded:
 p=root/name
 if p.exists(): p.unlink()
def digest(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def files():return sorted((p.relative_to(root).as_posix(),p) for p in root.rglob('*') if p.is_file())
rows=[]
for rel,path in files():
 if rel in excluded:continue
 data=path.read_bytes();rows.append({'bytes':len(data),'lines':data.count(b'\n'),'path':rel,'sha256':hashlib.sha256(data).hexdigest()})
(root/'FILE_INVENTORY.jsonl').write_text(''.join(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n' for x in rows))
payload=[(rel,path) for rel,path in files() if rel not in {'SHA256SUMS.txt','PAYLOAD_SHA256SUMS.txt'}]
(root/'PAYLOAD_SHA256SUMS.txt').write_text(''.join(f'{digest(path)}  {rel}\n' for rel,path in payload))
root_rows=[(rel,path) for rel,path in files() if rel!='SHA256SUMS.txt']
(root/'SHA256SUMS.txt').write_text(''.join(f'{digest(path)}  {rel}\n' for rel,path in root_rows))
print(json.dumps({'status':'PASS','inventory_rows':len(rows),'payload_rows':len(payload),'root_rows':len(root_rows),'root_seal_sha256':digest(root/'SHA256SUMS.txt'),'payload_seal_sha256':digest(root/'PAYLOAD_SHA256SUMS.txt')},sort_keys=True))
