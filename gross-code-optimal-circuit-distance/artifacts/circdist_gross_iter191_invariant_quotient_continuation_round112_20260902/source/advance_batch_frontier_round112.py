#!/usr/bin/env python3
from pathlib import Path
import argparse,gzip,hashlib,json
L,M,G=12,6,72

def canonical(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def semsha(o):return hashlib.sha256(canonical(o)).hexdigest()
def filesha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''):h.update(b)
 return h.hexdigest()
def key(s):return (str(s['sector']),tuple(sorted(map(int,s['data_support']))),tuple(sorted((int(c),tuple(sorted(map(int,ks)))) for c,ks in s['group_kinds'].items())))
def key_from_json(x):return (str(x[0]),tuple(map(int,x[1])),tuple((int(c),tuple(map(int,ks))) for c,ks in x[2]))
def semantics(k):
 sector,data,groups=k;names=[f'D:{q}' for q in data];gd={str(c):list(ks) for c,ks in groups}
 for c,ks in groups:names += [f'R:{c}:{x}' for x in ks]
 return semsha({'sector':sector,'selected_names':names,'data_support':list(data),'group_kinds':gd}),names,gd
ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);ap.add_argument('--state',type=Path,required=True);ap.add_argument('--plan',type=Path,required=True);ap.add_argument('--batch-result',type=Path,required=True);ap.add_argument('--audit',type=Path,action='append',required=True);ap.add_argument('--output-source',type=Path,required=True);ap.add_argument('--output-state',type=Path,required=True);ap.add_argument('--output-audit',type=Path,required=True);a=ap.parse_args()
with gzip.open(a.source,'rt') as f:source=json.load(f)
state=json.loads(a.state.read_text());plan=json.loads(a.plan.read_text());batch=json.loads(a.batch_result.read_text())
assert state['next_iteration']==191 and state['started'] is False and state['stop'] is None
assert state['source_file_sha256']==filesha(a.source);assert state['block_count']==517140 and state['selector_count']==24588
assert len(source['blocks'])==517140 and len(source['selectors'])==24588
assert plan['target_collision_free_parents_per_sector']==4 and plan['maximum_total_attempts_per_sector_including_mandatory']==12
assert batch['status']=='PASS' and batch['accepted_parent_count']==8 and batch['new_selector_count']==576 and batch['hard_cap_respected']
audits=[json.loads(p.read_text()) for p in a.audit]
assert [(o['sector'],o['attempt']) for o in audits]==[(s,i) for s in ('Xerr','Zerr') for i in range(1,5)]
existing=list(source['selectors']);by_key={key(s):s for s in existing};assert len(by_key)==len(existing)
by_hash={s['selector_semantic_sha256']:key(s) for s in existing};assert len(by_hash)==len(existing)
plan_sha=filesha(a.plan);batch_sha=filesha(a.batch_result);parent_rows=[];new_rows=[]
for o,p in zip(audits,a.audit):
 assert o['status']=='PASS' and o['accepted_collision_free'] and o['collision_count']==0 and o['orbit_size']==72
 sector=o['sector'];attempt=o['attempt'];parent_id=f'r112-i191-{sector}-a{attempt:02}-parent'
 parent_rows.append({'sector':sector,'attempt':attempt,'parent_mechanism_id':parent_id,'selector_semantic_sha256':o['parent_selector_semantic_sha256'],'selected_names':o['selected_names'],'assignment_sha256':o['assignment_sha256'],'audit_path':str(p),'audit_sha256':filesha(p),'orbit_size':72})
 seen_delta=set()
 for r in o['orbit_rows']:
  d=tuple(map(int,r['delta']));assert d not in seen_delta;seen_delta.add(d)
  k=key_from_json(r['selector_key']);digest,names,gd=semantics(k)
  assert digest==r['selector_semantic_sha256'] and names==r['selected_names'];assert k[0]==sector
  assert r['fault_count']==len(names)<=10 and r['syndrome']==[] and r['canonical_nonstabilizer'] and r['physical_nonstabilizer']
  assert k not in by_key and digest not in by_hash
  s={'mechanism_id':f'r112-i191-batch-{sector}-a{attempt:02}-d{d[0]}_{d[1]}','source_iteration':191,'sector':sector,'fault_count':len(names),'selected_names':names,'data_support':list(k[1]),'group_kinds':gd,'selector_semantic_sha256':digest,'origin':'round112_iter191_predeclared_four_parent_per_sector_batch','source_schedule_parent_sha256':r['translated_schedule_sha256'],'translation_parent_mechanism_id':parent_id,'translation_parent_selector_semantic_sha256':o['parent_selector_semantic_sha256'],'translation_delta':list(d),'soundness_provenance':'complete cumulative-CNF SAT assignment plus exact physical replay on translated legal source schedule','batch_plan_sha256':plan_sha,'batch_result_sha256':batch_sha,'attempt_audit_sha256':filesha(p)}
  by_key[k]=s;by_hash[digest]=k;existing.append(s);new_rows.append({'mechanism_id':s['mechanism_id'],'sector':sector,'attempt':attempt,'delta':list(d),'selector_semantic_sha256':digest,'selected_names':names,'translated_schedule_sha256':r['translated_schedule_sha256'],'canonical_support':r['canonical_support'],'physical_support':r['physical_support'],'logical_parities':r['logical_parities']})
 assert len(seen_delta)==72
assert len(existing)==24588+576==25164 and len(new_rows)==576
source.pop('semantic_payload_sha256');source['schema']='circdist-gross-iteration192-full-translation-closure-finite-source-v1';source['selectors']=existing;source['expected']['selectors']=len(existing);source['expected']['assertions']=4398+len(source['blocks'])+len(existing)
source['bindings']['round112_iter191_batch_plan_sha256']=plan_sha;source['bindings']['round112_iter191_batch_result_sha256']=batch_sha;source['bindings']['round112_iter191_batch_parent_selector_semantic_sha256']=[r['selector_semantic_sha256'] for r in parent_rows]
respos=[set(x) for x in source['residual_positions']]
def positions(kinds):
 out=set()
 for k in kinds:out.symmetric_difference_update(respos[int(k)])
 return tuple(sorted(out))
members=set();ranks=set()
for s in existing:
 d=source['sector_definitions'][s['sector']]
 for cs,kinds in s['group_kinds'].items():
  c=int(cs);pos=positions(kinds)
  for q in d['checks'][c]:
   members.add((s['sector'],c,pos,q))
   if pos and pos!=tuple(range(6)):ranks.add((s['sector'],c,q))
source['expected']['membership_expressions']=len(members);source['expected']['rank_expressions']=len(ranks);source['semantic_payload_sha256']=semsha(source)
a.output_source.parent.mkdir(parents=True,exist_ok=True);a.output_source.write_bytes(gzip.compress((json.dumps(source,indent=2,sort_keys=True)+'\n').encode(),compresslevel=9,mtime=0))
selector_state=semsha([{k:s.get(k) for k in ('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256')} for s in existing])
state_out={'schema':'circdist-gross-round112-iteration192-full-translation-frontier-state-v1','status':'PASS','next_iteration':192,'started':False,'stop':None,'block_count':517140,'selector_count':25164,'selector_state_sha256':selector_state,'source_semantic_payload_sha256':source['semantic_payload_sha256'],'source_file_sha256':filesha(a.output_source),'translation_group':'Z_12 x Z_6','translation_group_order':72,'scope':'fresh unstarted four-parent-per-sector batch orbit-closed outer frontier','batch_plan_sha256':plan_sha,'batch_result_sha256':batch_sha}
a.output_state.parent.mkdir(parents=True,exist_ok=True);a.output_state.write_text(json.dumps(state_out,indent=2,sort_keys=True)+'\n')
aud={'schema':'circdist-gross-round112-iteration192-batch-orbit-frontier-audit-v1','status':'PASS','group':{'name':'Z_12 x Z_6','order':72},'plan_sha256':plan_sha,'batch_result_sha256':batch_sha,'base_selectors':24588,'fresh_selectors':25164,'new_unique_selectors':576,'parent_count':8,'parent_orbit_sizes':{f"{r['sector']}:a{r['attempt']:02}":72 for r in parent_rows},'parent_rows':parent_rows,'translated_selector_replays':new_rows,'translated_schedule_mechanism_pairs':576,'collision_count':0,'collisions':[],'all_source_schedules_legal':True,'all_selectors_named_weight_at_most_10_zero_syndrome_nontrivial':True,'source_file_sha256':filesha(a.output_source),'source_semantic_payload_sha256':source['semantic_payload_sha256'],'state_file_sha256':filesha(a.output_state),'selector_state_sha256':selector_state,'membership_expressions':len(members),'rank_expressions':len(ranks)}
a.output_audit.parent.mkdir(parents=True,exist_ok=True);a.output_audit.write_text(json.dumps(aud,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':'PASS','base_selectors':24588,'fresh_selectors':25164,'added':576,'parent_count':8,'collision_count':0,'source_sha256':filesha(a.output_source),'semantic_sha256':source['semantic_payload_sha256'],'state_sha256':filesha(a.output_state),'selector_state_sha256':selector_state,'assertions':source['expected']['assertions'],'membership_expressions':len(members),'rank_expressions':len(ranks)},sort_keys=True))
