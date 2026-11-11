from pathlib import Path
import argparse,gzip,hashlib,json,sys
def canon(o):return json.dumps(o,sort_keys=True,separators=(",",":")).encode()
def sha(o):return hashlib.sha256(canon(o)).hexdigest()
def load(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix==".gz" else b)
ap=argparse.ArgumentParser();ap.add_argument('--round86',type=Path,required=True);ap.add_argument('--candidate',type=Path,required=True)
ap.add_argument('--direct',type=Path,required=True);ap.add_argument('--source109',type=Path,required=True)
ap.add_argument('--state',type=Path,required=True);ap.add_argument('--iteration',type=Path,required=True);ap.add_argument('--source110',type=Path,required=True)
a=ap.parse_args();R=a.round86.resolve();old=json.loads((R/'continuation/final_state.json').read_text());cand=json.loads(a.candidate.read_text());dv=json.loads(a.direct.read_text());times=cand['compressed_times']
assert old['next_iteration']==109 and old['started'] is False and len(old['selectors'])==134
assert old['selector_state_sha256']=='9be75eba643ac167d5c51497ca8e5cd23eb1656f803a49cbd8e7f1285b004113'
assert dv['candidate_sha256']==cand['compressed_schedule_sha256']==sha(times)
P=R/'vendor'/'round80';sys.path[:0]=[str(P/'src'/'round63_src'),str(P/'src')]
import model as M,round68_build as B
px,pz,lx,lz=B.load_context();ss=B.sectors(times,lx,lz)
assert M.audit_schedule(times,True)['ok']
def make(label):
 m=dv['sectors'][label]['mechanism'];data=[];groups={}
 for name in m['selected_names']:
  p=name.split(':')
  if p[0]=='D':data.append(int(p[1]))
  elif p[0]=='R':groups.setdefault(p[1],[]).append(int(p[2]))
  else:raise AssertionError(name)
 s={'mechanism_id':f'r88-i109-{label}','source_iteration':109,'sector':label,
    'fault_count':m['fault_count'],'selected_names':m['selected_names'],'data_support':sorted(data),
    'group_kinds':{k:sorted(v) for k,v in sorted(groups.items(),key=lambda kv:int(kv[0]))},
    'source_schedule_sha256':cand['compressed_schedule_sha256'],'source_times':times,
    'canonical_support':m['canonical_replay']['net_support'],'physical_support':m['physical_net_support'],
    'source_atoms':m['sound_outer_block']['atoms'],'source_atom_count':m['sound_outer_block']['atom_count'],
    'origin':'round88_proof_outer_iteration109_direct360','source_symbolic_validity':'True'}
 s['selector_semantic_sha256']=sha({k:s[k] for k in ('sector','selected_names','data_support','group_kinds')})
 assert s['fault_count']==len(s['data_support'])+sum(len(v) for v in s['group_kinds'].values())==10
 assert M.verify_named_selection(ss[label],s['selected_names'],10)['ok']
 return s
new=[make('Xerr'),make('Zerr')]
assert len({s['selector_semantic_sha256'] for s in old['selectors']+new})==136
# All old cuts false and both new cut domains true on the source candidate.
assert not any(M.verify_named_selection(ss[s['sector']],s['selected_names'],10)['ok'] for s in old['selectors'])
assert all(M.verify_named_selection(ss[s['sector']],s['selected_names'],10)['ok'] for s in new)
selectors=old['selectors']+new
keys=('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256')
state_hash=sha([{k:s.get(k) for k in keys} for s in selectors])
iteration={
 'schema':'round88-proof-outer-iteration-record-v1','iteration':109,'source_selector_count':134,
 'source_selector_state_sha256':old['selector_state_sha256'],'outer_encoding':'finite 10-bit CNF',
 'outer_cnf_sha256':cand['cnf_sha256'],'outer_status':'SATISFIABLE',
 'candidate_schedule_sha256':cand['compressed_schedule_sha256'],'candidate_audit':cand['frozen_audit'],
 'complete_outer_assignment':True,'reviewed_block_hits':0,'prior_selector_survivors':0,
 'direct':{lab:{'status':dv['sectors'][lab]['status'],'complete_query':dv['sectors'][lab]['formula_summary']['complete_query'],
   'variables':dv['sectors'][lab]['formula_summary']['variables'],'clauses':dv['sectors'][lab]['formula_summary']['clauses'],
   'dimacs_sha256':dv['sectors'][lab]['formula_summary']['dimacs_sha256'],
   'all_dimacs_clauses_satisfied':dv['sectors'][lab]['all_dimacs_clauses_satisfied'],
   'fault_count':dv['sectors'][lab]['mechanism']['fault_count'],
   'mechanism_sha256':sha(dv['sectors'][lab]['mechanism'])} for lab in ('Xerr','Zerr')},
 'repair_entered':False,'repair_gate_reason':'both unrestricted direct-360 sectors are SAT',
 'new_selectors':[s['mechanism_id'] for s in new],'new_cuts_installed':2,
 'state_mutated_atomically':True,'state_after_sha256':state_hash,'next_iteration':110,'started':False,
}
state={
 'schema':'round88-proof-outer-continuation-state-v1','status':'PASS',
 'parent_round86_root_manifest_sha256':'94322390a648262e8cc035f8e843617f134fe2d29ff36191720b646c021c89ff',
 'parent_selector_count':134,'parent_selector_state_sha256':old['selector_state_sha256'],
 'reviewed_base_semantic_sha256':old['reviewed_base_semantic_sha256'],'reviewed_base_blocks':14484,
 'initial_reviewed_selectors':134,'round88_completed_candidates':1,'selector_count':136,
 'selector_state_sha256':state_hash,'next_iteration':110,'started':False,'stop':None,
 'completed_iterations':[109],'iterations':[iteration],'selectors':selectors,
 'atomicity':{'candidate_solved_against_selector_prefix':134,'both_direct_replays_before_commit':True,
              'commit_selector_indices':[134,135],'later_cuts_retroactive':False},
}
a.state.write_text(json.dumps(state,indent=2,sort_keys=True)+'\n');a.iteration.write_text(json.dumps(iteration,indent=2,sort_keys=True)+'\n')
# Produce the complete unstarted iteration-110 semantic source for deterministic compilation.
s=load(a.source109);old_sem=s.pop('semantic_payload_sha256');assert sha(s)==old_sem
s['schema']='circdist-gross-iteration110-finite-source-v1'
for x in new:
 keep=('mechanism_id','source_iteration','sector','fault_count','selected_names','data_support','group_kinds',
       'source_schedule_sha256','origin','selector_semantic_sha256')
 s['selectors'].append({k:x[k] for k in keep})
s['bindings']['round88_iteration109_cnf_sha256']=cand['cnf_sha256']
s['bindings']['round88_continuation_selector_state_sha256']=state_hash
s['expected']['selectors']=136;s['expected']['assertions']=19018
res=[set(x) for x in s['residual_positions']]
def pos(kinds):
 z=set()
 for k in kinds:z.symmetric_difference_update(res[int(k)])
 return tuple(sorted(z))
members=set();ranks=set()
for x in s['selectors']:
 sd=s['sector_definitions'][x['sector']]
 for cs,kinds in x['group_kinds'].items():
  c=int(cs);p=pos(kinds)
  for q in sd['checks'][c]:
   members.add((x['sector'],c,p,q))
   if p and p!=tuple(range(6)):ranks.add((x['sector'],c,q))
s['expected']['membership_expressions']=len(members);s['expected']['rank_expressions']=len(ranks)
s['semantic_payload_sha256']=sha(s)
a.source110.write_bytes(gzip.compress((json.dumps(s,indent=2,sort_keys=True)+'\n').encode(),compresslevel=9,mtime=0))
print(json.dumps({'status':'PASS','selector_count':136,'selector_state_sha256':state_hash,'next_iteration':110,
 'source110_semantic_payload_sha256':s['semantic_payload_sha256'],'rank_expressions':len(ranks),
 'membership_expressions':len(members)},sort_keys=True))
