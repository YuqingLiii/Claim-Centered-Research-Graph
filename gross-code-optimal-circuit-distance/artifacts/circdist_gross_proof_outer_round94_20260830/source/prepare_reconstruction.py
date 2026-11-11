#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import gzip,hashlib,json,shutil,sys
repo=Path(sys.argv[1]).resolve(); out=Path(sys.argv[2]).resolve(); out.mkdir(parents=True,exist_ok=True); (out/'reconstruction').mkdir(parents=True,exist_ok=True); (out/'state').mkdir(parents=True,exist_ok=True)
p92=repo/'circdist/artifacts/circdist_gross_proof_outer_round92_20260830'
f=p92/'formulas/iter136'; b=out/'bindings'; b.mkdir(parents=True,exist_ok=True)
def fsha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as x:
  for z in iter(lambda:x.read(1<<20),b''):h.update(z)
 return h.hexdigest()
def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def copy(src,dst):dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
expected={
 'operations/circdist/SCHEDULER.yaml':'4da1d0f15ddcdb7542cc69507661231807dad97edf684d578d5010c13b9b2383',
 'circdist/proof-dag/nodes/CIRCDIST.gross.yaml':'c3b03597c496ace59bb84f5d4e4cfb1540b98e193dcba9f67adb0abd657bc3f3',
 'circdist/reviews/circdist_gross_proof_outer_weight9_exact_review_round93_20260830.md':'76a07f9d73fda5ced83818361eed24cd83b4ed7fc5a11c13b0fc027df4feb65d',
 'circdist/artifacts/circdist_gross_proof_outer_round92_20260830/SHA256SUMS.txt':'4e255084bdab13ad0b9c295a9fe7cf2aea8231c4a56db656964f0695ddc6c982',
 'circdist/artifacts/circdist_gross_proof_outer_round92_20260830/PAYLOAD_SHA256SUMS.txt':'fbc881f0dc54744cb3cfd0c4497571592f8597326ce98362eb42a032ed289090',
}
rows=[]
for rel,want in expected.items():
 p=repo/rel; got=fsha(p); assert got==want,(rel,got,want)
 dst=b/rel.replace('/','__');copy(p,dst)
 rows.append({'path':rel,'expected_sha256':want,'observed_sha256':got,'snapshot':str(dst.relative_to(out))})
# Protocol snapshots are informative but bound exactly here.
for rel in ['DAG_PROTOCOL.md','FILE_PROTOCOL.md','circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md']:
 p=repo/rel;dst=b/rel.replace('/','__');copy(p,dst);rows.append({'path':rel,'observed_sha256':fsha(p),'snapshot':str(dst.relative_to(out))})
# Frontier and all six unstarted files.
front=p92/'continuation/final_state.json'; assert fsha(front)=='58781b46cc177df046ec334420046e1ccc8a23517f21fe4491e6412741ced57c'
copy(front,out/'state/iter136_state.json')
for name in ['source.json.gz','outer.cnf.gz','metadata.json','assertion_map.jsonl.gz','circuit_trace.json.gz','encoding_check.json']:
 copy(f/name,out/'formulas/iter136'/name)
S=json.loads(gzip.decompress((f/'source.json.gz').read_bytes()))
given=S.pop('semantic_payload_sha256');assert hashlib.sha256(canon(S)).hexdigest()==given=='a561515801904b458d34ebccea5aa364420f9a0a012e36e721f48fcbe9be4ebe';S['semantic_payload_sha256']=given
assert fsha(f/'source.json.gz')=='a71fb5e708eeebf365dda0661b79652b264bc0eb87308626383a5ca389cfc5d8'
state=json.loads(front.read_text());assert state['selector_count']==len(state['selectors'])==len(S['selectors'])==232
assert state['selector_state_sha256']=='1692d905120d2dcf51b949ce4a70ed4b8f1b270c2d07a1ddbf5813d20d80fa81'
assert state['next_iteration']==136 and state['started'] is False and state['stop'] is None
bc=Counter(x['family'] for x in S['blocks']);assert bc==Counter({'generalized':12820,'unary':1440,'dynamic':204,'round62':20})
assert len(S['blocks'])==14484
raw=gzip.decompress((f/'outer.cnf.gz').read_bytes()); assert hashlib.sha256(raw).hexdigest()=='289acad6be1068d63369511e9c95b0b1df146471bf05a1e4128758508612b64e'
(out/'formulas/iter136/outer.cnf').write_bytes(raw)
mapraw=gzip.decompress((f/'assertion_map.jsonl.gz').read_bytes());(out/'formulas/iter136/assertion_map.jsonl').write_bytes(mapraw)
M=json.loads((f/'metadata.json').read_text());assert (M['assertions'],M['variables'],M['clauses'])==(19114,406656,1372232);assert M['cnf_sha256']==fsha(out/'formulas/iter136/outer.cnf')
assert len(mapraw.splitlines())==19114
# Negative inherited-disposition scan from independently reviewed package.
paths=sorted(str(x.relative_to(p92)) for x in p92.rglob('*') if x.is_file() and 'iter136' in str(x.relative_to(p92)))
assert paths==['formulas/iter136/assertion_map.jsonl.gz','formulas/iter136/circuit_trace.json.gz','formulas/iter136/encoding_check.json','formulas/iter136/metadata.json','formulas/iter136/outer.cnf.gz','formulas/iter136/source.json.gz']
outj={'schema':'circdist-round94-input-reconstruction-v1','status':'PASS','bindings':rows,'round92_manifest_verified_separately':True,'frontier':{'state_file_sha256':fsha(front),'selector_count':232,'selector_state_sha256':state['selector_state_sha256'],'next_iteration':136,'started':False,'stop':None},'source':{'file_sha256':fsha(f/'source.json.gz'),'semantic_sha256':given,'assertions':M['assertions'],'variables':M['variables'],'clauses':M['clauses'],'cnf_sha256':M['cnf_sha256'],'block_family_counts':dict(sorted(bc.items()))},'unstarted_iter136_paths':paths,'inherited_disposition_absent':True}
(out/'reconstruction/input_bindings.json').write_text(json.dumps(outj,indent=2,sort_keys=True)+'\n')
print(json.dumps(outj,sort_keys=True))
