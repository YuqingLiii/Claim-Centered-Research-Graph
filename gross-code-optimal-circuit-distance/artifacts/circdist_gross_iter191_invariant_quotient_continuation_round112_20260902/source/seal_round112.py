#!/usr/bin/env python3
"""Create exact payload/root manifests and freeze the complete Round112 package."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, os, shutil
CHUNK=8<<20
GENERATED={'FILE_INVENTORY.jsonl','PAYLOAD_SHA256SUMS.txt','SHA256SUMS.txt'}
def scan(path):
 h=hashlib.sha256(); size=lf=0
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(CHUNK),b''): h.update(b); size+=len(b); lf+=b.count(b'\n')
 return h.hexdigest(),size,lf
def files(root): return sorted((p.relative_to(root).as_posix(),p) for p in root.rglob('*') if p.is_file())
def verify(root,name):
 rows=[]
 for number,line in enumerate((root/name).read_text().splitlines(),1):
  digest,sep,rel=line.partition('  '); assert sep and len(digest)==64 and all(c in '0123456789abcdef' for c in digest)
  pos=PurePosixPath(rel); assert rel==pos.as_posix() and not pos.is_absolute() and '..' not in pos.parts
  assert rel not in rows and (root/rel).is_file() and not (root/rel).is_symlink() and scan(root/rel)[0]==digest,(name,number,rel); rows.append(rel)
 assert rows==sorted(rows); return rows
ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); a=ap.parse_args(); root=a.root.resolve()
for cache in sorted(root.rglob('__pycache__'),reverse=True):
 if cache.is_dir(): shutil.rmtree(cache)
assert not [p for p in root.rglob('*') if p.is_symlink()]
assert not [p for p in root.rglob('*') if p.is_file() and p.name.endswith('.tmp')]
assert not [p for base in (root/'solver',root/'batch') for p in base.rglob('*.drat') if p.is_file()]
for name in GENERATED:
 p=root/name
 if p.exists(): p.unlink()
payload=[(rel,p) for rel,p in files(root) if rel not in GENERATED]
(root/'PAYLOAD_SHA256SUMS.txt').write_text(''.join(f'{scan(p)[0]}  {rel}\n' for rel,p in payload))
payload_rows=verify(root,'PAYLOAD_SHA256SUMS.txt')
substantive=[(rel,p) for rel,p in files(root) if rel not in {'FILE_INVENTORY.jsonl','SHA256SUMS.txt'}]
with (root/'FILE_INVENTORY.jsonl').open('w',encoding='utf-8',newline='\n') as out:
 for rel,p in substantive:
  digest,size,lf=scan(p); out.write(json.dumps({'bytes':size,'lines':lf,'path':rel,'sha256':digest},sort_keys=True,separators=(',',':'))+'\n')
rows=[(rel,p) for rel,p in files(root) if rel!='SHA256SUMS.txt']
with (root/'SHA256SUMS.txt').open('w',encoding='utf-8',newline='\n') as out:
 for rel,p in rows: out.write(f'{scan(p)[0]}  {rel}\n')
root_rows=verify(root,'SHA256SUMS.txt'); actual={rel for rel,_ in files(root)}
assert set(root_rows)==actual-{'SHA256SUMS.txt'} and len(root_rows)==len(actual)-1
inventory=[json.loads(line) for line in (root/'FILE_INVENTORY.jsonl').read_text().splitlines()]
assert {x['path'] for x in inventory}==actual-{'FILE_INVENTORY.jsonl','SHA256SUMS.txt'}
result={'schema':'circdist-gross-round112-full-root-seal-v1','status':'PASS','payload_rows':len(payload_rows),
 'payload_manifest_sha256':scan(root/'PAYLOAD_SHA256SUMS.txt')[0],'inventory_rows':len(inventory),
 'root_rows':len(root_rows),'physical_files':len(actual),'root_manifest_sha256':scan(root/'SHA256SUMS.txt')[0],
 'root_manifest_bytes':scan(root/'SHA256SUMS.txt')[1],'substantive_bytes':sum(x['bytes'] for x in inventory),
 'symlinks':0,'raw_drat_files':0,'temporary_files':0,'verified_after_write':True,'memory_safety':'fixed 8 MiB scans'}
package_files=[p for _,p in files(root)]; executable=0
for p in package_files:
 isexec=bool(p.stat().st_mode&0o111); p.chmod(0o555 if isexec else 0o444); executable+=int(isexec)
directories=sorted((p for p in root.rglob('*') if p.is_dir()),key=lambda p:len(p.parts),reverse=True)
for p in directories: p.chmod(0o555)
root.chmod(0o555)
assert all(not(p.stat().st_mode&0o222) for p in package_files+[root,*directories])
result.update({'content_frozen_read_only':True,'read_only_files':len(package_files),'read_only_directories':len(directories)+1,'executable_files_preserved':executable})
print(json.dumps(result,sort_keys=True))
