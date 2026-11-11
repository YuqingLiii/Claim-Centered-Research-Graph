#!/usr/bin/env python3
from pathlib import Path
import argparse,gzip,hashlib,json
ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--package',type=Path,required=True);ap.add_argument('--scratch',type=Path,required=True);ap.add_argument('--rank',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''):h.update(b)
 return h.hexdigest()
def csha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def cnf_stats(p):
 nv=nc=None; seen=0
 with p.open('rb') as f:
  for line in f:
   if line.startswith(b'p cnf '):
    assert nv is None; z=line.split();nv,nc=int(z[2]),int(z[3])
   elif line.strip() and not line.startswith(b'c'):seen+=1
 assert nv is not None and nc==seen
 return {'variables':nv,'clauses':nc}
expected={
 a.repo/'operations/circdist/SCHEDULER.yaml':'9750f170f0c23f96317b08ff158671310364c8439b6bcd7f44e7c3b455dfef6a',
 a.repo/'circdist/proof-dag/nodes/CIRCDIST.gross.yaml':'25d39fbd9add4f5c0d9b7fea76ab2ede1f0c5c3711cd7a152ca98bbde351a834',
 a.repo/'circdist/reviews/circdist_gross_iter191_invariant_quotient_continuation_round112_exact_review_round113_20260902.md':'9737f5c015ace29a5282685b1bf19d82686e593b0e2e6216531cc0bb2a8d27e8',
 a.package/'SHA256SUMS.txt':'404063fcddeb183c670192e3791c44d23d0393beefae1ee4658c1f480c910e4f',
 a.rank:'aa5475949d9abe25c2168d8dcd47cc5e88c453ec12d1cc9fed6cae556f3925c2'}
for p,e in expected.items():assert sha(p)==e,(p,sha(p),e)
rank=json.loads(a.rank.read_text());assert rank['winner']['key']=='CIRCDIST.gross@dstar-residual' and rank['winner']['score']==0.0011127742156472275
src=a.scratch/'input/iter192_full_invariant/source.json.gz';statep=a.scratch/'input/iter192_full_invariant/state.json'
assert sha(src)=='89ed11977cacaed4f46a8c0756fef77a9706a2f3ce65d6ec1b496424fb9533f3';assert sha(statep)=='e4085c5a776561bfc136d67f64988c31c0e26b063afd715d61a836a2f6ff06f1'
with gzip.open(src,'rt') as f:s=json.load(f)
claim=s.pop('semantic_payload_sha256');sem=csha(s);s['semantic_payload_sha256']=claim
assert claim==sem=='957459e254abc70f0c66a631712ee70e856f9ca11153b78f20b06d7fb1ffe67b'
assert len(s['edges'])==864 and len(set(s['edges']))==864 and len(s['blocks'])==517140 and len(s['selectors'])==25164
state=json.loads(statep.read_text());assert state['next_iteration']==192 and state['started'] is False and state['stop'] is None
assert state['block_count']==517140 and state['selector_count']==25164
sel=[{k:x.get(k) for k in ('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256')} for x in s['selectors']]
selsha=csha(sel);assert selsha==state['selector_state_sha256']=='dbaeb3d246eef029ede5bcba760a254a75f5d77816ca9d0cbf92396fdf42ad60'
pairs=[]
for sub,names in [('iter192_full_invariant/formula',['outer.cnf','metadata.json','assertion_map.jsonl','definitions.json.gz']),('iter192_full_invariant_quotient',['outer.cnf','metadata.json','translation_roots.jsonl','translation_trace.json.gz'])]:
 for name in names:
  x=a.scratch/'reconstructed'/sub/name;y=a.package/'frontier'/sub/name;hx,hy=sha(x),sha(y)
  if name=='metadata.json':
   jx,jy=json.loads(x.read_text()),json.loads(y.read_text());timing={}
   for k in sorted(set(jx)|set(jy)):
    if k.endswith('_seconds'):timing[k]={'reconstructed':jx.pop(k,None),'sealed':jy.pop(k,None)}
   assert jx==jy,(sub,name)
   pairs.append({'path':sub+'/'+name,'reconstructed_sha256':hx,'sealed_sha256':hy,'non_timing_identical':True,'timing_fields':timing})
  else:
   assert hx==hy and x.stat().st_size==y.stat().st_size,(sub,name,hx,hy)
   pairs.append({'path':sub+'/'+name,'sha256':hx,'bytes':x.stat().st_size,'byte_identical':True})
base=cnf_stats(a.scratch/'reconstructed/iter192_full_invariant/formula/outer.cnf');quot=cnf_stats(a.scratch/'reconstructed/iter192_full_invariant_quotient/outer.cnf')
assert base=={'variables':1875411,'clauses':6999141};assert quot=={'variables':2488851,'clauses':11906732}
assert sha(a.scratch/'reconstructed/iter192_full_invariant/formula/outer.cnf')=='3388c5f4927fecce693237cf0b1090d8c7e9b965067e70f10f54c85febb9393b'
assert sha(a.scratch/'reconstructed/iter192_full_invariant_quotient/outer.cnf')=='00baea753d8ef3d47bbd1e3ca149d39bd2a36ef6475e957633d00770c0071e71'
roots=[json.loads(x) for x in (a.scratch/'reconstructed/iter192_full_invariant_quotient/translation_roots.jsonl').read_text().splitlines()];assert len(roots)==71
forbidden=[]
for d in (a.package/'frontier/iter192_full_invariant',a.package/'frontier/iter192_full_invariant_quotient'):
 for p in d.rglob('*'):
  if p.is_file() and any(x in p.name.lower() for x in ('solver','assignment','model','drat','lrat')):forbidden.append(str(p))
assert not forbidden
copy_rows=[]
for name in ('source.json.gz','state.json'):
 x=a.package/'frontier/iter192_full_invariant'/name;y=a.scratch/'input/iter192_full_invariant'/name
 copy_rows.append({'name':name,'source_inode':x.stat().st_ino,'scratch_inode':y.stat().st_ino,'source_nlink':x.stat().st_nlink,'scratch_nlink':y.stat().st_nlink,'distinct_inode':x.stat().st_ino!=y.stat().st_ino});assert copy_rows[-1]['distinct_inode'] and y.stat().st_nlink==1
out={'schema':'circdist-gross-round114-iter192-reconstruction-binding-v1','status':'PASS','governance':{str(p):e for p,e in expected.items()},'winner':rank['winner'],'source':{'file_sha256':sha(src),'semantic_sha256':sem,'state_sha256':sha(statep),'selector_state_sha256':selsha,'blocks':517140,'selectors':25164,'assertions':546702,'started':False,'stop':None},'ordinary_copy_controls':copy_rows,'generated_files':pairs,'base':base,'quotient':quot,'lex_roots':71,'forbidden_frontier_solver_artifacts':forbidden,'global_plan_sha256':sha(a.scratch/'plans/GLOBAL_MECHANISM_PLAN.json'),'fallback_plan_sha256':sha(a.scratch/'plans/FALLBACK_BATCH_PLAN.json'),'conclusion':'All reviewed iteration-192 inputs and deterministic formula bytes reconstructed exactly; only declared compile timing fields differ. The exact quotient is authorized to solve proof-first.'}
a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','base':base,'quotient':quot,'source':sha(src),'semantic':sem,'state':sha(statep),'selector_state':selsha,'roots':71},sort_keys=True))
