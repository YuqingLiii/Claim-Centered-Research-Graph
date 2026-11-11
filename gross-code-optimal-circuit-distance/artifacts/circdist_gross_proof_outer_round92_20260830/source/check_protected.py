#!/usr/bin/env python3
"""Verify protected inputs and the complete reviewed Round90 dependency closure."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()

ap=argparse.ArgumentParser();ap.add_argument('--package',type=Path,required=True);ap.add_argument('--repository',type=Path);a=ap.parse_args()
P=a.package.resolve(); B=json.loads((P/'INPUT_BINDINGS.json').read_text())
for rel,expected in B['package_snapshot_sha256'].items():assert sha(P/rel)==expected,(rel,sha(P/rel),expected)
if a.repository:
    R=a.repository.resolve()
    for rel,expected in B['expected_protected_sha256'].items():assert sha(R/rel)==expected,(rel,sha(R/rel),expected)
    dep=B['reviewed_dependency']; D=R/dep['repository_relative_path']
    assert sha(D/'SHA256SUMS.txt')==dep['root_manifest_file_sha256']
    assert sha(D/'PAYLOAD_SHA256SUMS.txt')==dep['payload_manifest_file_sha256']
    assert (P/'bindings/round90/SHA256SUMS.txt').read_bytes()==(D/'SHA256SUMS.txt').read_bytes()
    assert (P/'bindings/round90/PAYLOAD_SHA256SUMS.txt').read_bytes()==(D/'PAYLOAD_SHA256SUMS.txt').read_bytes()
    def check_manifest(name):
        rows=[]
        for line in (D/name).read_text().splitlines():
            h,sep,rel=line.partition('  ');assert sep and len(h)==64
            q=PurePosixPath(rel);assert not q.is_absolute() and '..' not in q.parts and rel==q.as_posix()
            rows.append((rel,h))
        assert rows==sorted(rows) and len(rows)==len({x[0] for x in rows})
        for rel,h in rows:assert (D/rel).is_file() and sha(D/rel)==h,(name,rel)
        return {x[0] for x in rows}
    root=check_manifest('SHA256SUMS.txt');payload=check_manifest('PAYLOAD_SHA256SUMS.txt')
    actual={p.relative_to(D).as_posix() for p in D.rglob('*') if p.is_file()}
    assert root==actual-{'SHA256SUMS.txt'}
    assert payload==actual-{'SHA256SUMS.txt','PAYLOAD_SHA256SUMS.txt'}
    assert root==payload|{'PAYLOAD_SHA256SUMS.txt'}
print('PROTECTED_AND_DEPENDENCY_PASS',len(B['package_snapshot_sha256']),len(B['expected_protected_sha256']) if a.repository else 0)

