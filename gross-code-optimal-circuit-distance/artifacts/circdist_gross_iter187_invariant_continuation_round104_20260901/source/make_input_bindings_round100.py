#!/usr/bin/env python3
"""Write the exact Round100 immutable-input binding inventory."""
from pathlib import Path
import argparse, gzip, hashlib, json

ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve()

def sha(b): return hashlib.sha256(b).hexdigest()
def row(path):
    p=R/path; stored=p.read_bytes(); content=gzip.decompress(stored) if p.suffix=='.gz' else stored
    return {'path':path,'stored_sha256':sha(stored),'stored_bytes':len(stored),'stored_lf':stored.count(b'\n'),
            'content_sha256':sha(content),'content_bytes':len(content),'content_lf':content.count(b'\n'),
            'gzip':p.suffix=='.gz'}
def tree_digest(rows):
    h=hashlib.sha256()
    for x in sorted(rows,key=lambda z:z['path']):
        h.update(x['path'].encode()+b'\0'+x['stored_sha256'].encode()+b'\0'+str(x['stored_bytes']).encode()+b'\n')
    return h.hexdigest()

paths=[]
for base in ('bindings','vendor','tooling','synthesis/inputs','synthesis/order5_input'):
    paths += [p.relative_to(R).as_posix() for p in (R/base).rglob('*') if p.is_file()]
paths += ['state/iter172_state.json','formulas/iter172/source.json.gz','formulas/iter172/metadata.json',
          'formulas/iter172/outer.cnf.gz','formulas/iter172/assertion_map.jsonl.gz',
          'formulas/iter172/circuit_trace.json.gz','formulas/iter172/encoding_check.json']
paths=sorted(set(paths)); rows=[row(p) for p in paths]
by={x['path']:x for x in rows}
dispatched={
 'DAG_PROTOCOL.md':('bindings/DAG_PROTOCOL.md','d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095',15377,283),
 'FILE_PROTOCOL.md':('bindings/FILE_PROTOCOL.md','d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595',8523,166),
 'operations/circdist/SCHEDULER.yaml':('bindings/operations__circdist__SCHEDULER.yaml','a4ecdb895bb62b1537cf012f3dd4385d3e45f63380e95896f3bece409c43abe4',265091,3167),
 'circdist/proof-dag/nodes/CIRCDIST.gross.yaml':('bindings/circdist__proof-dag__nodes__CIRCDIST.gross.yaml','43abf1f383f44a4aee98c71da17af6fddca8b526d76cf135cd16c89a9aaae14c',85062,938),
 'circdist/reviews/circdist_gross_proof_outer_round98_exact_review_round99_20260831.md':('bindings/circdist__reviews__circdist_gross_proof_outer_round98_exact_review_round99_20260831.md','28ed0201da7cfc87aba7ce2ec2ad53afbb3d363b7bc66ab802f9feea6bc1d060',583650,5810),
}
dispatch_rows=[]
for original,(path,expected_sha,expected_bytes,expected_lf) in dispatched.items():
    x=by[path];assert (x['content_sha256'],x['content_bytes'],x['content_lf'])==(expected_sha,expected_bytes,expected_lf),(original,x)
    dispatch_rows.append({'original_path':original,'package_path':path,'sha256':expected_sha,'bytes':expected_bytes,'lf':expected_lf})
frontier={
 'next_iteration':172,'started':False,'stop':None,'selector_count':304,
 'selector_state_sha256':'a5c64ae41f474844ecd3ac41829331f54d419a81573e4f0e11528db0b49e25d1',
 'state_file_sha256':'9fd675be9712a28dd625fba7cce95f75a8a3b9bdf7edc3f398bfa8b13844d2be',
 'source_file_sha256':'99faca59521b675844d0c10eb12afcfe925f474d3eac9d5cac56e11537397b08',
 'source_semantic_sha256':'cfa261df8b148622c80248d398df20f1ff5a4cf3f04eb76a31b2795185cc6412',
 'assertions':19186,'variables':413646,'clauses':1406245,
 'cnf_sha256':'f86b8db36af1df3877ca1d9dbafb171b6173ddc8b6c2f045a808dd6c71f98342'}
assert by['state/iter172_state.json']['stored_sha256']==frontier['state_file_sha256']
assert by['formulas/iter172/source.json.gz']['stored_sha256']==frontier['source_file_sha256']
assert by['formulas/iter172/outer.cnf.gz']['content_sha256']==frontier['cnf_sha256']
prior={'root_sha256':'f64feb1b424b4aff938a1b5a0c1f9a799179e41f4ec99295c5c67376fad9142f',
       'payload_sha256':'2df276eb26dc569f830d0c95ac76aa5ed322bc9fcb525637a96196d66394e6ec',
       'inventory_sha256':'35f77eacac06bb114f897b16e61b2a03b00f961cc8448e258d2210e65273f45c',
       'physical_files':1617,'sealed_replay_children':56,'sealed_replay_status':'PASS'}
initial=[x for x in rows if x['path'].startswith('bindings/initial_proof_dag/')]
out={'schema':'circdist-round100-input-bindings-v1','status':'PASS','dispatch_files':dispatch_rows,
     'licensed_initial_frontier':frontier,'prior_round98_seal':prior,
     'initial_proof_dag_snapshot':{'files':len(initial),'tree_sha256':tree_digest(initial),'rows':initial},
     'all_immutable_input_rows':rows,'immutable_input_file_count':len(rows),'immutable_input_tree_sha256':tree_digest(rows),
     'binding_policy':'All hashes bind copied package inputs. Gzip rows record both physical stored bytes and the exact uncompressed content stream.',
     'canonical_and_protocol_files_read_only':True}
(R/'INPUT_BINDINGS.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','files':len(rows),'tree_sha256':out['immutable_input_tree_sha256'],'proof_dag_tree_sha256':out['initial_proof_dag_snapshot']['tree_sha256']},sort_keys=True))
