#!/usr/bin/env python3
from pathlib import Path
import argparse,gzip,hashlib,json,os,shutil
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--iteration',type=int,required=True);a=p.parse_args();root=a.root.resolve();i=a.iteration;n=i+1;pend=root/f'pending/iter{i}_to{n}'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
prev=json.loads((root/f'state/iter{i}_state.json').read_text());state=json.loads((pend/'state.json').read_text());record=json.loads((pend/'record.json').read_text());source=json.loads(gzip.decompress((pend/'source.json.gz').read_bytes()));meta=json.loads((pend/'formula/metadata.json').read_text());enc=json.loads((pend/'formula/encoding_check.json').read_text())
assert prev['next_iteration']==i and prev['started'] is False and prev['stop'] is None
assert state['next_iteration']==n and state['started'] is False and state['stop'] is None
assert state['parent_selector_count']==prev['selector_count'] and state['parent_selector_state_sha256']==prev['selector_state_sha256']
assert state['selector_count']==prev['selector_count']+2==len(state['selectors'])==len(source['selectors'])
assert record['iteration']==i and record['source_selector_count']==prev['selector_count'] and record['state_after_sha256']==state['selector_state_sha256']
assert record['outer_status']=='SATISFIABLE' and record['repair_entered'] is False and all(record['direct'][x]['status']=='SATISFIABLE' for x in ('Xerr','Zerr'))
ids=[x['mechanism_id'] for x in state['selectors'][-2:]];assert ids==[f'r96-i{i}-Xerr',f'r96-i{i}-Zerr']==record['new_selectors']
given=source.pop('semantic_payload_sha256');assert hashlib.sha256(canon(source)).hexdigest()==given;source['semantic_payload_sha256']=given
assert source['expected']['selectors']==state['selector_count'] and source['expected']['assertions']==18882+state['selector_count']
assert meta['source_semantic_payload_sha256']==given and meta['selector_count']==state['selector_count'] and meta['cnf_sha256']==sha(pend/'formula/outer.cnf')
assert enc['status']=='PASS' and enc['cnf_sha256']==meta['cnf_sha256'] and enc['efssc_selectors']==state['selector_count']
target_formula=root/f'formulas/iter{n}';target_state=root/f'state/iter{n}_state.json';target_record=root/f'iterations/iter{i}/record.json';transition=root/f'transitions/iter{i}_to{n}';
for q in [target_formula,target_state,target_record,transition]:assert not q.exists(),q
payload={'state_file_sha256':sha(pend/'state.json'),'record_file_sha256':sha(pend/'record.json'),'source_file_sha256':sha(pend/'source.json.gz'),'source_semantic_sha256':given,'cnf_sha256':meta['cnf_sha256'],'selector_state_sha256':state['selector_state_sha256'],'selector_count':state['selector_count'],'new_selector_ids':ids}
intent={'schema':'circdist-round96-atomic-pending-commit-v1','status':'PENDING','iteration_closed':i,'next_iteration':n,'state_promoted_last':True,'payload':payload}
(pend/'commit_intent.json').write_text(json.dumps(intent,indent=2,sort_keys=True)+'\n')
# Formula directory rename is atomic; state visibility changes last.
os.replace(pend/'source.json.gz',pend/'formula/source.json.gz')
target_formula.parent.mkdir(parents=True,exist_ok=True);os.replace(pend/'formula',target_formula)
target_record.parent.mkdir(parents=True,exist_ok=True);os.replace(pend/'record.json',target_record)
os.replace(pend/'state.json',target_state)
transition.mkdir(parents=True,exist_ok=False);intent['status']='COMMITTED';intent['state_target']=str(target_state.relative_to(root));intent['formula_target']=str(target_formula.relative_to(root));intent['record_target']=str(target_record.relative_to(root));intent['all_outputs_present']=all(q.exists() for q in [target_formula,target_state,target_record]);assert intent['all_outputs_present']
(transition/'atomic_commit.json').write_text(json.dumps(intent,indent=2,sort_keys=True)+'\n');shutil.copyfile(pend/'commit_intent.json',transition/'pending_intent.json');shutil.rmtree(pend)
print(json.dumps(intent,sort_keys=True))
