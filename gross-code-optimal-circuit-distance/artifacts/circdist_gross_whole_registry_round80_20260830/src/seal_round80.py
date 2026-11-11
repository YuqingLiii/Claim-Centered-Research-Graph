#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();seal=R/'SHA256SUMS.txt';pay=R/'PAYLOAD_SHA256SUMS.txt'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while True:
   b=f.read(8<<20)
   if not b:break
   h.update(b)
 return h.hexdigest()
for p in (seal,pay):
 if p.exists():p.unlink()
# Exact package-root-relative exclusions; a same basename below a subdirectory is payload.
prels=sorted(p.relative_to(R).as_posix() for p in R.rglob('*') if p.is_file() and p.relative_to(R).as_posix() not in {'SHA256SUMS.txt','PAYLOAD_SHA256SUMS.txt'})
pay.write_text(''.join(f'{sha(R/rel)}  {rel}\n' for rel in prels))
srels=sorted(p.relative_to(R).as_posix() for p in R.rglob('*') if p.is_file() and p.relative_to(R).as_posix()!='SHA256SUMS.txt')
seal.write_text(''.join(f'{sha(R/rel)}  {rel}\n' for rel in srels))
print(json.dumps({'status':'PASS','payload_entries':len(prels),'root_entries':len(srels),'payload_manifest_sha256':sha(pay),'external_root_seal_sha256':sha(seal)},sort_keys=True))
