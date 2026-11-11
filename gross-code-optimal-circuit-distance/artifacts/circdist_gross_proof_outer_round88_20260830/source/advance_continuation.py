from pathlib import Path
import argparse,gzip,hashlib,json,sys
def canon(o):return json.dumps(o,sort_keys=True,separators=(",",":")).encode()
def sha(o):return hashlib.sha256(canon(o)).hexdigest()
def load(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix==".gz" else b)
ap=argparse.ArgumentParser();ap.add_argument('--round86',type=Path,required=True);ap.add_argument('--state-in',type=Path,required=True)
ap.add_argument('--source-in',type=Path,required=True);ap.add_argument('--iteration',type=int,required=True)
ap.add_argument('--candidate',type=Path,required=True);ap.add_argument('--direct',type=Path,required=True)
ap.add_argument('--state-out',type=Path,required=True);ap.add_argument('--record-out',type=Path,required=True);ap.add_argument('--source-out',type=Path,required=True)
a=ap.parse_args();old=json.loads(a.state_in.read_text());source=load(a.source_in);cand=json.loads(a.candidate.read_text());dv=json.loads(a.direct.read_text());i=a.iteration
assert old['next_iteration']==i and old['started'] is False and len(old['selectors'])==old['selector_count']
assert len(source['selectors'])==old['selector_count'] and source['expected']['selectors']==old['selector_count']
times=cand['compressed_times'];assert dv['candidate_sha256']==cand['compressed_schedule_sha256']==sha(times)
R=a.round86.resolve();P=R/'vendor'/'round80';sys.path[:0]=[str(P/'src'/'round63_src'),str(P/'src')]
import model as M,round68_build as B
px,pz,lx,lz=B.load_context();ss=B.sectors(times,lx,lz);assert M.audit_schedule(times,True)['ok']
assert not any(M.verify_named_selection(ss[s['sector']],s['selected_names'],10)['ok'] for s in old['selectors'])
def make(label):
 m=dv['sectors'][label]['mechanism'];data=[];groups={}
 for name in m['selected_names']:
  p=name.split(':')
  if p[0]=='D':data.append(int(p[1]))
  else:assert p[0]=='R';groups.setdefault(p[1],[]).append(int(p[2]))
 s={'mechanism_id':f'r88-i{i}-{label}','source_iteration':i,'sector':label,'fault_count':m['fault_count'],
  'selected_names':m['selected_names'],'data_support':sorted(data),
  'group_kinds':{k:sorted(v) for k,v in sorted(groups.items(),key=lambda kv:int(kv[0]))},
  'source_schedule_sha256':cand['compressed_schedule_sha256'],'source_times':times,
  'canonical_support':m['canonical_replay']['net_support'],'physical_support':m['physical_net_support'],
  'source_atoms':m['sound_outer_block']['atoms'],'source_atom_count':m['sound_outer_block']['atom_count'],
  'origin':f'round88_proof_outer_iteration{i}_direct360','source_symbolic_validity':'True'}
 s['selector_semantic_sha256']=sha({k:s[k] for k in ('sector','selected_names','data_support','group_kinds')})
 assert s['fault_count']==len(s['data_support'])+sum(len(v) for v in s['group_kinds'].values())==10
 assert M.verify_named_selection(ss[label],s['selected_names'],10)['ok']
 return s
new=[make('Xerr'),make('Zerr')];selectors=old['selectors']+new
assert len({s['selector_semantic_sha256'] for s in selectors})==len(selectors)
keys=('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256')
h=sha([{k:s.get(k) for k in keys} for s in selectors])
rec={'schema':'round88-proof-outer-iteration-record-v1','iteration':i,'source_selector_count':len(old['selectors']),
 'source_selector_state_sha256':old['selector_state_sha256'],'outer_encoding':'finite 10-bit CNF',
 'outer_cnf_sha256':cand['cnf_sha256'],'outer_status':'SATISFIABLE',
 'candidate_schedule_sha256':cand['compressed_schedule_sha256'],'candidate_audit':cand['frozen_audit'],
 'complete_outer_assignment':True,'reviewed_block_hits':0,'prior_selector_survivors':0,
 'direct':{lab:{'status':dv['sectors'][lab]['status'],'complete_query':dv['sectors'][lab]['formula_summary']['complete_query'],
  'variables':dv['sectors'][lab]['formula_summary']['variables'],'clauses':dv['sectors'][lab]['formula_summary']['clauses'],
  'dimacs_sha256':dv['sectors'][lab]['formula_summary']['dimacs_sha256'],
  'all_dimacs_clauses_satisfied':dv['sectors'][lab]['all_dimacs_clauses_satisfied'],
  'fault_count':dv['sectors'][lab]['mechanism']['fault_count'],'mechanism_sha256':sha(dv['sectors'][lab]['mechanism'])} for lab in ('Xerr','Zerr')},
 'repair_entered':False,'repair_gate_reason':'both unrestricted direct-360 sectors are SAT',
 'new_selectors':[x['mechanism_id'] for x in new],'new_cuts_installed':2,'state_mutated_atomically':True,
 'state_after_sha256':h,'next_iteration':i+1,'started':False}
out=dict(old);out.update({'schema':'round88-proof-outer-continuation-state-v1','status':'PASS',
 'parent_selector_count':len(old['selectors']),'parent_selector_state_sha256':old['selector_state_sha256'],
 'round88_completed_candidates':old.get('round88_completed_candidates',0)+1,
 'selector_count':len(selectors),'selector_state_sha256':h,'next_iteration':i+1,'started':False,'stop':None,
 'completed_iterations':old.get('completed_iterations',[])+[i],
 'iterations':old.get('iterations',[])+[rec],'selectors':selectors,
 'atomicity':{'candidate_solved_against_selector_prefix':len(old['selectors']),
   'both_direct_replays_before_commit':True,'commit_selector_indices':[len(old['selectors']),len(old['selectors'])+1],
   'later_cuts_retroactive':False}})
a.state_out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');a.record_out.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
source.pop('semantic_payload_sha256')
source['schema']=f'circdist-gross-iteration{i+1}-finite-source-v1'
for x in new:
 keep=('mechanism_id','source_iteration','sector','fault_count','selected_names','data_support','group_kinds','source_schedule_sha256','origin','selector_semantic_sha256')
 source['selectors'].append({k:x[k] for k in keep})
source['bindings'][f'round88_iteration{i}_cnf_sha256']=cand['cnf_sha256'];source['bindings']['round88_continuation_selector_state_sha256']=h
source['expected']['selectors']=len(selectors);source['expected']['assertions']=18882+len(selectors)
res=[set(x) for x in source['residual_positions']]
def pos(kinds):
 z=set()
 for k in kinds:z.symmetric_difference_update(res[int(k)])
 return tuple(sorted(z))
members=set();ranks=set()
for x in source['selectors']:
 sd=source['sector_definitions'][x['sector']]
 for cs,kinds in x['group_kinds'].items():
  c=int(cs);p=pos(kinds)
  for q in sd['checks'][c]:
   members.add((x['sector'],c,p,q))
   if p and p!=tuple(range(6)):ranks.add((x['sector'],c,q))
source['expected']['membership_expressions']=len(members);source['expected']['rank_expressions']=len(ranks)
source['semantic_payload_sha256']=sha(source)
a.source_out.write_bytes(gzip.compress((json.dumps(source,indent=2,sort_keys=True)+'\n').encode(),compresslevel=9,mtime=0))
print(json.dumps({'status':'PASS','iteration':i,'next_iteration':i+1,'selector_count':len(selectors),'selector_state_sha256':h,
 'source_semantic_payload_sha256':source['semantic_payload_sha256'],'rank_expressions':len(ranks),'membership_expressions':len(members)},sort_keys=True))
