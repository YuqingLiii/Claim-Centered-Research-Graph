#!/usr/bin/env python3
from pathlib import Path
import gzip,hashlib,json,sys
repo=Path('<repo>')
pred=repo/'circdist/artifacts/circdist_gross_iter190_invariant_quotient_continuation_round110_20260902'
work=Path('.')

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''): h.update(b)
 return h.hexdigest()
def canon_sha(o):
 h=hashlib.sha256(); enc=json.JSONEncoder(sort_keys=True,separators=(',',':'))
 for x in enc.iterencode(o): h.update(x.encode())
 return h.hexdigest()
def cnf_stats(p):
 hdr=None; clauses=0
 with Path(p).open('rb') as f:
  for line in f:
   if line.startswith(b'p cnf '):
    a=line.split(); hdr=(int(a[2]),int(a[3]))
   elif line and not line.startswith(b'c') and line.strip(): clauses += 1
 assert hdr and clauses==hdr[1], (p,hdr,clauses)
 return {'variables':hdr[0],'clauses_header':hdr[1],'clauses_streamed':clauses}
expected={
 repo/'operations/circdist/SCHEDULER.yaml':'e5b55acfbbc21380b28aa6758c6e9cf180491a51af0b1bf93bd597fd930be196',
 repo/'circdist/proof-dag/nodes/CIRCDIST.gross.yaml':'7cc45da6ae90deb2f44aee40fa28a17c5f0a74a36970f4cef795d6ae317883d4',
 repo/'circdist/reviews/circdist_gross_iter190_invariant_quotient_continuation_round110_exact_review_round111_20260902.md':'36f2fdac0c74a0bfa3f67013590e21fd24c445295c488edc95c2114edef72e9e',
 pred/'SHA256SUMS.txt':'8ce014a0bc1b4273cec02e2af7d9da54691290dd35a82d7c3bfe6c522a031bc5'}
for p,e in expected.items(): assert sha(p)==e,(p,sha(p),e)
src=work/'input/iter191_full_invariant/source.json.gz'; statep=work/'input/iter191_full_invariant/state.json'
assert sha(src)=='0b0ac7e6daa69d8d3ab1b98b7228c43690a5406c52defe57e46027b185984a47'
assert sha(statep)=='6059554d307e7c503bd1792dd77718a205346f5dce243e719ae057f402cf6c9f'
with gzip.open(src,'rt') as f: source=json.load(f)
claim=source.pop('semantic_payload_sha256'); sem=canon_sha(source); source['semantic_payload_sha256']=claim
assert claim==sem=='02da1bcb87a45637afa8434a8dfa4e4c8092489ace7f5a7fd1ba3266f9615532'
assert len(source['edges'])==864 and len(set(source['edges']))==864
assert len(source['blocks'])==517140 and len(source['selectors'])==24588
state=json.loads(statep.read_text()); assert state['next_iteration']==191 and state['started'] is False and state['stop'] is None
assert state['block_count']==517140 and state['selector_count']==24588
sel_view=[{k:s.get(k) for k in ('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256')} for s in source['selectors']]
selsha=canon_sha(sel_view); assert selsha==state['selector_state_sha256']=='41bb458a1b9a31aba7d70f063165221a9ae9c989421682320826dbc5d166f9e6'
pairs=[]
for sub,files in [
 ('iter191_full_invariant/formula',['outer.cnf','metadata.json','assertion_map.jsonl','definitions.json.gz']),
 ('iter191_full_invariant_quotient',['outer.cnf','metadata.json','translation_roots.jsonl','translation_trace.json.gz'])]:
 for name in files:
  a=work/'reconstructed'/sub/name; b=pred/'frontier'/sub/name
  ha,hb=sha(a),sha(b)
  if name == 'metadata.json':
   ja,jb=json.loads(a.read_text()),json.loads(b.read_text())
   timing={}
   for key in sorted(set(ja)|set(jb)):
    if key.endswith('_seconds'):
     timing[key]={'reconstructed':ja.pop(key,None),'sealed':jb.pop(key,None)}
   assert ja==jb,(sub,name,'non-timing metadata differs')
   pairs.append({'path':sub+'/'+name,'reconstructed_sha256':ha,'sealed_sha256':hb,'semantic_non_timing_identical':True,'timing_fields':timing})
  else:
   assert ha==hb,(sub,name,ha,hb)
   assert a.stat().st_size==b.stat().st_size
   pairs.append({'path':sub+'/'+name,'sha256':ha,'bytes':a.stat().st_size,'byte_identical':True})
base=cnf_stats(work/'reconstructed/iter191_full_invariant/formula/outer.cnf')
quot=cnf_stats(work/'reconstructed/iter191_full_invariant_quotient/outer.cnf')
assert base=={'variables':1853886,'clauses_header':6929888,'clauses_streamed':6929888}
assert quot=={'variables':2467326,'clauses_header':11837479,'clauses_streamed':11837479}
assert sha(work/'reconstructed/iter191_full_invariant/formula/outer.cnf')=='d1e68e88eb4c22ffda58d3a1c73cb7dbf6082690c594e8c538f8cc70c432e223'
assert sha(work/'reconstructed/iter191_full_invariant_quotient/outer.cnf')=='30ce7d14d96349e61d7105255cddc8899b8927ce728dfd147b641c75c97fe10f'
roots=[json.loads(x) for x in (work/'reconstructed/iter191_full_invariant_quotient/translation_roots.jsonl').read_text().splitlines()]
assert len(roots)==71
forbidden=[]
for p in (pred/'frontier/iter191_full_invariant').rglob('*'):
 if p.is_file() and any(x in p.name.lower() for x in ('solver','assignment','model','drat','lrat')): forbidden.append(str(p))
for p in (pred/'frontier/iter191_full_invariant_quotient').rglob('*'):
 if p.is_file() and any(x in p.name.lower() for x in ('solver','assignment','model','drat','lrat')): forbidden.append(str(p))
assert not forbidden,forbidden
out={'schema':'circdist-gross-round112-iter191-reconstruction-binding-v1','status':'PASS','governance':{str(p.relative_to(repo)):e for p,e in expected.items()},'source':{'sha256':sha(src),'semantic_sha256':sem,'state_sha256':sha(statep),'selector_state_sha256':selsha,'blocks':517140,'selectors':24588,'edges':864,'started':False,'stop':None},'generated_files':pairs,'base':base,'quotient':quot,'lex_roots':len(roots),'forbidden_solver_artifacts':forbidden,'conclusion':'Fresh reconstruction reproduces every load-bearing byte; only measured runtime fields in metadata vary. Solver may start only on the exact quotient hash.'}
Path('verification/iter191_reconstruction_binding.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','base':base,'quotient':quot,'roots':len(roots),'semantic':sem,'selector_state':selsha},sort_keys=True))
