#!/usr/bin/env python3
"""Independently verify both Round108 manifests, inventory, bytes/LF, and read-only freeze."""
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
 for num,line in enumerate((root/name).read_text().splitlines(),1):
  digest,sep,rel=line.partition('  '); assert sep and len(digest)==64
  pos=PurePosixPath(rel); assert rel==pos.as_posix() and not pos.is_absolute() and '..' not in pos.parts
  p=root/rel; assert p.is_file() and not p.is_symlink() and scan(p)[0]==digest,(name,num,rel); rows.append(rel)
 assert rows==sorted(rows) and len(rows)==len(set(rows)); return rows
ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args(); r=a.root.resolve()
assert not [p for p in r.rglob('*') if p.is_symlink()]
payload=manifest(r,'PAYLOAD_SHA256SUMS.txt'); rootrows=manifest(r,'SHA256SUMS.txt')
actual=sorted(p.relative_to(r).as_posix() for p in r.rglob('*') if p.is_file())
assert set(rootrows)==set(actual)-{'SHA256SUMS.txt'} and len(rootrows)==len(actual)-1
inv=[]
for n,line in enumerate((r/'FILE_INVENTORY.jsonl').read_text().splitlines(),1):
 x=json.loads(line); p=r/x['path']; digest,size,lf=scan(p); assert (digest,size,lf)==(x['sha256'],x['bytes'],x['lines']),(n,x['path']); inv.append(x)
assert [x['path'] for x in inv]==sorted(x['path'] for x in inv) and len(inv)==len({x['path'] for x in inv})
assert set(x['path'] for x in inv)==set(actual)-{'FILE_INVENTORY.jsonl','SHA256SUMS.txt'}
assert set(payload).issubset(set(actual))
files=[r/x for x in actual]; dirs=[r,*[p for p in r.rglob('*') if p.is_dir()]]
assert all(not (p.stat().st_mode & 0o222) for p in files+dirs)
assert scan(r/'PROPOSED_CIRCDIST.gross.yaml')[0]==scan(r/'bindings/CIRCDIST.gross.yaml')[0]=='8b805a806d5b704047f4ccca648c92efe11740d7c5b7825659eb1e6b7b5dc977'
root_sha,root_bytes,root_lf=scan(r/'SHA256SUMS.txt'); pay_sha,pay_bytes,pay_lf=scan(r/'PAYLOAD_SHA256SUMS.txt')
out={'schema':'circdist-gross-round108-independent-sealed-root-verification-v1','status':'PASS','root_manifest_sha256':root_sha,'root_manifest_bytes':root_bytes,'root_manifest_lf':root_lf,'root_rows':len(rootrows),'payload_manifest_sha256':pay_sha,'payload_manifest_bytes':pay_bytes,'payload_manifest_lf':pay_lf,'payload_rows':len(payload),'inventory_rows':len(inv),'physical_files':len(actual),'substantive_bytes':sum(x['bytes'] for x in inv),'substantive_lf':sum(x['lines'] for x in inv),'symlinks':0,'writable_files':0,'writable_directories':0,'canonical_yaml_unchanged':True}
a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
