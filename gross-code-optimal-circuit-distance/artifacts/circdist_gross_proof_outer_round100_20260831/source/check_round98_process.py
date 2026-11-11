#!/usr/bin/env python3
"""Validate retained Round98 foreground-process and orchestration accounting."""
from pathlib import Path
import argparse,json
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);a=p.parse_args();R=a.root.resolve()
L=json.loads((R/'PROCESS_LEDGER.json').read_text());assert L['schema']=='circdist-gross-round98-process-ledger-v1' and L['status']=='PASS'
assert L['science_solver_children']==36 and L['outer_solver_children']==12 and L['direct_solver_children']==24
assert L['strict_serial_solver_intervals_checked'] and L['all_children_reaped'] and L['background_processes']==L['detached_processes']==L['survivors']==L['timeouts']==0
records=L['records'];actual={p.relative_to(R).as_posix() for p in (R/'logs/process').glob('*.json')};assert {x['path'] for x in records}==actual
sol=[];fail=[]
for x in records:
    assert x['final_status']=='exited_and_reaped' and x['reaped'] and not x['detached'] and not x['timed_out']
    assert x['returncode'] in (-6,0,1,10)
    if x['returncode']==10 and 'cadical_proof' in x.get('name',''):sol.append((x['started_unix'],x['ended_unix'],x['path']))
    if x['returncode'] not in (0,10):fail.append([Path(x['path']).name,x['name'],x['returncode']])
sol.sort();assert len(sol)==36 and all(x[1]<=y[0] for x,y in zip(sol,sol[1:]))
assert fail==L['corrected_failure_records']
assert len(L['orchestration_incidents'])==4 and sum(x['kind']=='model-capacity' for x in L['orchestration_incidents'])==3
print('ROUND98_PROCESS_LEDGER_PASS',len(records),len(sol),len(fail),len(L['orchestration_incidents']))
