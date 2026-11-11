#!/usr/bin/env python3
"""Package-only validation of every Round100 immutable-input binding."""
from pathlib import Path
import argparse,gzip,hashlib,json
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();B=json.loads((R/'INPUT_BINDINGS.json').read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def tree(rows):
 h=hashlib.sha256()
 for x in sorted(rows,key=lambda z:z['path']):h.update(x['path'].encode()+b'\0'+x['stored_sha256'].encode()+b'\0'+str(x['stored_bytes']).encode()+b'\n')
 return h.hexdigest()
for x in B['all_immutable_input_rows']:
 p=R/x['path'];assert p.is_file(),p;stored=p.read_bytes();content=gzip.decompress(stored) if x['gzip'] else stored
 assert (sha(stored),len(stored),stored.count(b'\n'))==(x['stored_sha256'],x['stored_bytes'],x['stored_lf']),x['path']
 assert (sha(content),len(content),content.count(b'\n'))==(x['content_sha256'],x['content_bytes'],x['content_lf']),x['path']
assert tree(B['all_immutable_input_rows'])==B['immutable_input_tree_sha256']
assert tree(B['initial_proof_dag_snapshot']['rows'])==B['initial_proof_dag_snapshot']['tree_sha256']
f=B['licensed_initial_frontier'];assert hashlib.sha256((R/'state/iter172_state.json').read_bytes()).hexdigest()==f['state_file_sha256'];assert hashlib.sha256((R/'formulas/iter172/source.json.gz').read_bytes()).hexdigest()==f['source_file_sha256'];assert hashlib.sha256(gzip.decompress((R/'formulas/iter172/outer.cnf.gz').read_bytes())).hexdigest()==f['cnf_sha256']
print(json.dumps({'status':'PASS','files_checked':len(B['all_immutable_input_rows']),'tree_sha256':B['immutable_input_tree_sha256']},sort_keys=True))
