#!/usr/bin/env python3
"""Check dispatched files and the full initial proof-DAG snapshot against the live repository."""
from pathlib import Path
import argparse,hashlib,json
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);ap.add_argument('--repository',type=Path,required=True);a=ap.parse_args();P=a.root.resolve();R=a.repository.resolve();B=json.loads((P/'INPUT_BINDINGS.json').read_text())
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
for x in B['dispatch_files']:
 q=R/x['original_path'];assert q.is_file() and (sha(q),q.stat().st_size,q.read_bytes().count(b'\n'))==(x['sha256'],x['bytes'],x['lf']),x['original_path']
for x in B['initial_proof_dag_snapshot']['rows']:
 rel=Path(x['path']).relative_to('bindings/initial_proof_dag');q=R/rel;assert q.is_file() and sha(q)==x['stored_sha256'],rel
snapshot={str(Path(x['path']).relative_to('bindings/initial_proof_dag')) for x in B['initial_proof_dag_snapshot']['rows']};live={str(x.relative_to(R)) for x in (R/'circdist/proof-dag').rglob('*') if x.is_file()};assert live==snapshot,(live-snapshot,snapshot-live)
print(json.dumps({'status':'PASS','dispatch_files':len(B['dispatch_files']),'proof_dag_files':len(snapshot),'canonical_and_protocol_unchanged':True},sort_keys=True))
