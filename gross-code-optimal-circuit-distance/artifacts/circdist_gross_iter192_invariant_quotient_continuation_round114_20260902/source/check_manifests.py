#!/usr/bin/env python3
from pathlib import Path,PurePosixPath
import argparse,hashlib
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve()
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def parse(name):
 rows=[]
 for n,line in enumerate((R/name).read_text().splitlines(),1):
  h,sep,path=line.partition('  ');assert sep and len(h)==64 and all(c in '0123456789abcdef' for c in h),(name,n)
  q=PurePosixPath(path);assert not q.is_absolute() and path==q.as_posix() and '..' not in q.parts and '.' not in q.parts,(name,n,path)
  rows.append((path,h))
 assert rows==sorted(rows) and len(rows)==len({p for p,h in rows}),name
 for path,h in rows:assert (R/path).is_file() and sha(R/path)==h,(name,path)
 return {p for p,h in rows}
root=parse('SHA256SUMS.txt');payload=parse('PAYLOAD_SHA256SUMS.txt')
actual={p.relative_to(R).as_posix() for p in R.rglob('*') if p.is_file()}
assert root==actual-{'SHA256SUMS.txt'}
assert payload==actual-{'SHA256SUMS.txt','PAYLOAD_SHA256SUMS.txt'}
assert root==payload|{'PAYLOAD_SHA256SUMS.txt'}
print('MANIFESTS_PASS',len(actual),sha(R/'SHA256SUMS.txt'),sha(R/'PAYLOAD_SHA256SUMS.txt'))
