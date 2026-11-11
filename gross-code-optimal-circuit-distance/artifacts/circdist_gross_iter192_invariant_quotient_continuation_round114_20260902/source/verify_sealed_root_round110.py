#!/usr/bin/env python3
"""Independently verify exact manifests, inventory, modes, and canonical identity."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json
CHUNK=8<<20
def scan(p):
 h=hashlib.sha256(); size=lf=0
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(CHUNK),b''): h.update(b); size+=len(b); lf+=b.count(b'\n')
 return h.hexdigest(),size,lf
def manifest(root,name):
 rows=[]
 for n,line in enumerate((root/name).read_text().splitlines(),1):
  digest,sep,rel=line.partition('  '); assert sep and len(digest)==64
  pos=PurePosixPath(rel); assert rel==pos.as_posix() and not pos.is_absolute() and '..' not in pos.parts
  p=root/rel; assert p.is_file() and not p.is_symlink() and scan(p)[0]==digest,(name,n,rel); rows.append(rel)
 assert rows==sorted(rows) and len(rows)==len(set(rows)); return rows
ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args(); r=a.root.resolve()
assert not [p for p in r.rglob('*') if p.is_symlink()]
payload=manifest(r,'PAYLOAD_SHA256SUMS.txt'); rootrows=manifest(r,'SHA256SUMS.txt'); actual=sorted(p.relative_to(r).as_posix() for p in r.rglob('*') if p.is_file())
assert set(rootrows)==set(actual)-{'SHA256SUMS.txt'} and len(rootrows)==len(actual)-1
inventory=[]
for n,line in enumerate((r/'FILE_INVENTORY.jsonl').read_text().splitlines(),1):
 x=json.loads(line); digest,size,lf=scan(r/x['path']); assert (digest,size,lf)==(x['sha256'],x['bytes'],x['lines']),(n,x['path']); inventory.append(x)
assert [x['path'] for x in inventory]==sorted(x['path'] for x in inventory) and len(inventory)==len({x['path'] for x in inventory})
assert set(x['path'] for x in inventory)==set(actual)-{'FILE_INVENTORY.jsonl','SHA256SUMS.txt'}
files=[r/x for x in actual]; dirs=[r,*[p for p in r.rglob('*') if p.is_dir()]]; assert all(not(p.stat().st_mode&0o222) for p in files+dirs)
assert scan(r/'PROPOSED_CIRCDIST.gross.yaml')[0]==scan(r/'bindings/CIRCDIST.gross.yaml')[0]=='7302da9e4726bd2c62a9e335d75d6a9098780888ed91a87a66d503b5938f607b'
out={'schema':'circdist-gross-round110-independent-sealed-root-verification-v1','status':'PASS',
 'root_manifest_sha256':scan(r/'SHA256SUMS.txt')[0],'root_manifest_bytes':scan(r/'SHA256SUMS.txt')[1],
 'root_manifest_lf':scan(r/'SHA256SUMS.txt')[2],'root_rows':len(rootrows),
 'payload_manifest_sha256':scan(r/'PAYLOAD_SHA256SUMS.txt')[0],'payload_manifest_bytes':scan(r/'PAYLOAD_SHA256SUMS.txt')[1],
 'payload_manifest_lf':scan(r/'PAYLOAD_SHA256SUMS.txt')[2],'payload_rows':len(payload),'inventory_rows':len(inventory),
 'physical_files':len(actual),'substantive_bytes':sum(x['bytes'] for x in inventory),'substantive_lf':sum(x['lines'] for x in inventory),
 'symlinks':0,'writable_files':0,'writable_directories':0,'canonical_yaml_unchanged':True}
a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
