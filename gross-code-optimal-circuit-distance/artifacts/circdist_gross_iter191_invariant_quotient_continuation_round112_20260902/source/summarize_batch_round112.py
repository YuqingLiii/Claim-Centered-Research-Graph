#!/usr/bin/env python3
from pathlib import Path
import gzip,hashlib,json

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''):h.update(b)
 return h.hexdigest()
def kt(x):return (str(x[0]),tuple(map(int,x[1])),tuple((int(c),tuple(map(int,ks))) for c,ks in x[2]))
plan=Path('batch/BATCH_PLAN.json');assert sha(plan)=='1b476ae4bc79aa5f257f0b00d5d2649ece935fd0decdd45db04c872f02e112eb'
rows=[];keys=set();parents=[]
for sector in ('Xerr','Zerr'):
 for attempt in range(1,5):
  p=Path(f'batch/{sector}/attempt{attempt:02}/audit.json');o=json.loads(p.read_text())
  assert o['status']=='PASS' and o['sector']==sector and o['attempt']==attempt
  assert o['accepted_collision_free'] and o['collision_count']==0 and o['orbit_size']==72
  assert o['all_variables_assigned_exactly_once'] and o['all_clauses_satisfied']
  assert o['all_translated_schedules_legal'] and o['all_translated_mechanisms_weight_at_most_10_zero_syndrome_nonstabilizer']
  for r in o['orbit_rows']:
   k=kt(r['selector_key']);assert k not in keys;keys.add(k)
  if attempt==1:
   assignment=Path(f'solver/iter191/direct/solver/{sector}.assignment.dimacs')
   proc=Path(f'logs/process/solve_iter191_{sector}.json')
   expected_clauses=23012 if sector=='Xerr' else 22928
  else:
   assignment=Path(f'batch/{sector}/attempt{attempt:02}/assignment.dimacs')
   proc=Path(f'logs/process/batch_{sector}_attempt{attempt:02}_solver.json')
   expected_clauses=(23012 if sector=='Xerr' else 22928)+attempt-1
   q=json.loads(Path(f'batch/{sector}/attempt{attempt:02}/query.json').read_text())
   assert q['blocking_clause_count']==attempt-1 and q['clauses']==expected_clauses and q['exact_primary_blocking']
  pr=json.loads(proc.read_text());assert pr['returncode']==10 and pr['reaped'] and not pr['timed_out'] and not pr['detached']
  assert pr['argv'][-1].endswith('.drat')
  assert o['assignment_sha256']==sha(assignment) and o['clauses']==expected_clauses
  parent={'sector':sector,'attempt':attempt,'audit':str(p),'audit_sha256':sha(p),'assignment':str(assignment),'assignment_sha256':sha(assignment),'cnf_sha256':o['cnf_sha256'],'variables':o['variables'],'clauses':o['clauses'],'selected_names':o['selected_names'],'parent_selector_semantic_sha256':o['parent_selector_semantic_sha256'],'orbit_size':72,'collision_count':0,'solver_process':str(proc),'solver_wall_seconds':pr['wall_seconds'],'solver_pid':pr['child_pid']}
  parents.append(parent)
  rows.append({'sector':sector,'attempt':attempt,'accepted':True,'collision_count':0,'orbit_size':72})
assert len(parents)==8 and len(keys)==576
assert not Path('batch/Xerr/attempt05').exists() and not Path('batch/Zerr/attempt05').exists()
with gzip.open('input/iter191_full_invariant/source.json.gz','rt') as f:source=json.load(f)
installed=set()
for s in source['selectors']:
 k=(s['sector'],tuple(sorted(map(int,s['data_support']))),tuple(sorted((int(c),tuple(sorted(map(int,ks)))) for c,ks in s['group_kinds'].items())))
 assert k not in installed;installed.add(k)
assert not (keys&installed)
out={'schema':'circdist-gross-round112-direct-selector-batch-result-v1','status':'PASS','plan_sha256':sha(plan),'sectors':{'Xerr':{'attempts':4,'accepted':4,'collisions':0,'stopped_at_target':True},'Zerr':{'attempts':4,'accepted':4,'collisions':0,'stopped_at_target':True}},'parents':parents,'accepted_parent_count':8,'accepted_parent_orbits':8,'new_selector_count':576,'union_orbit_key_count':len(keys),'installed_selector_count':len(installed),'installed_collisions':0,'cross_batch_collisions':0,'all_assignments_complete_and_all_clauses_satisfied':True,'all_576_translated_schedules_and_physical_mechanisms_replayed':True,'attempt05_absent':True,'hard_cap_respected':True,'conclusion':'A four-parent-per-sector finite batch supplies 576 complete free selector-orbit members; it excludes mechanisms/order regions but is not a root theorem.'}
Path('batch/BATCH_RESULT.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:out[k] for k in ['status','accepted_parent_count','new_selector_count','installed_collisions','cross_batch_collisions','hard_cap_respected']},sort_keys=True))
