#!/usr/bin/env python3
from pathlib import Path
import argparse,json
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();L=json.loads((R/'PROCESS_LEDGER.json').read_text())
paths=sorted((R/'logs/process').glob('*.json'));assert len(paths)==L['retained_pid_record_count']==len(L['retained_pid_bearing_process_records'])
rows=[]
for p in paths:
 x=json.loads(p.read_text());assert x['reaped'] is True and x['detached'] is False and not x['timed_out'];rows.append((p.name,x))
science=[(n,x) for n,x in rows if n!='independent_campaign_audit.json' and not n.startswith('round100_')]
assert len(science)==L['science_process_record_count']==204
assert {str(c):sum(x['returncode']==c for _,x in science) for c in (0,1,10,20)}==L['science_returncodes']=={'0':165,'1':1,'10':36,'20':2}
solver=sorted((x['started_unix'],x['ended_unix'],n,x['returncode']) for n,x in science if 'cadical_proof' in n and x['returncode'] in (10,20));assert len(solver)==L['science_solver_interval_count']==38 and solver==[tuple(x) for x in L['science_solver_intervals']]
assert all(a[1]<=b[0] for a,b in zip(solver,solver[1:])) and L['strict_solver_nonoverlap']
assert L['campaign_driver_count']==2 and L['campaign_wrapper_processes_started_serially']==192 and L['span_certificate_child_count']==12
assert L['prior_round98_sealed_replay_children']==56 and L['retained_timeouts']==0 and L['retained_detached_processes']==0 and L['all_retained_pid_records_reaped']
assert len(L['repository_validator_children'])==12 and all(x['reaped'] and not x['detached'] for x in L['repository_validator_children'])
assert len(L['final_preseal_children'])==7 and L['final_preseal_nested_proof_children']==6
assert all(x['reaped'] and not x['detached'] and not x['timed_out'] for x in L['final_preseal_children'])
for r in L['package_replay_attempt_records']:
 assert r['record']['all_children_reaped'] and r['record']['detached_processes']==0
print(json.dumps({'status':'PASS','pid_records':len(rows),'science_records':len(science),'solver_intervals':len(solver),'campaign_wrappers':192,'span_proof_children':12,'all_reaped':True},sort_keys=True))
