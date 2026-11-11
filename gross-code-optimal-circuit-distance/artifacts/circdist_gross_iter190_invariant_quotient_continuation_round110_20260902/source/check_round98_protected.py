#!/usr/bin/env python3
"""Verify the exact Round98 commissioned inputs and their package snapshots."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()

p=argparse.ArgumentParser();p.add_argument('--package',type=Path,required=True);p.add_argument('--repository',type=Path);a=p.parse_args()
P=a.package.resolve();B=json.loads((P/'INPUT_BINDINGS.json').read_text())
for rel,want in B['package_snapshot_sha256'].items(): assert sha(P/rel)==want,(rel,sha(P/rel),want)
if a.repository:
    R=a.repository.resolve()
    for rel,want in B['expected_protected_sha256'].items(): assert sha(R/rel)==want,(rel,sha(R/rel),want)
    dep=B['reviewed_dependency'];D=R/dep['repository_relative_path']
    for name,key in [('SHA256SUMS.txt','root_manifest_file_sha256'),('PAYLOAD_SHA256SUMS.txt','payload_manifest_file_sha256')]:
        assert sha(D/name)==dep[key]
        snap=P/'bindings'/('circdist__artifacts__circdist_gross_proof_outer_round96_20260831__'+name)
        assert snap.read_bytes()==(D/name).read_bytes()
    for name in ('SHA256SUMS.txt','PAYLOAD_SHA256SUMS.txt'):
        rows=[]
        for line in (D/name).read_text().splitlines():
            digest,sep,rel=line.partition('  ');q=PurePosixPath(rel)
            assert sep and len(digest)==64 and not q.is_absolute() and '..' not in q.parts and rel==q.as_posix()
            rows.append((rel,digest))
        assert rows==sorted(rows) and len(rows)==len({x for x,_ in rows})
        for rel,digest in rows: assert (D/rel).is_file() and sha(D/rel)==digest,(name,rel)
print('ROUND98_PROTECTED_BINDINGS_PASS',len(B['package_snapshot_sha256']),len(B['expected_protected_sha256']) if a.repository else 0)
