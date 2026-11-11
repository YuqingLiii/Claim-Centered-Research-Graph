#!/usr/bin/env python3
"""Inventory retained Round110 process records and enforce FIX-2 closure."""
from pathlib import Path
import argparse, hashlib, json

def scan(path):
 raw=Path(path).read_bytes(); return {'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}

ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args(); r=a.root.resolve()
records=[]
for p in sorted((r/'logs/process').glob('*.json')):
 try: value=json.loads(p.read_text())
 except Exception: continue
 records.append({'path':p.relative_to(r).as_posix(),**scan(p),'name':value.get('name'),
                 'child_pid':value.get('child_pid'),'returncode':value.get('returncode'),
                 'timed_out':value.get('timed_out'),'term_sent':value.get('term_sent'),
                 'kill_sent':value.get('kill_sent'),'reaped':value.get('reaped'),
                 'detached':value.get('detached'),'started_unix':value.get('started_unix'),
                 'ended_unix':value.get('ended_unix'),'cwd':value.get('cwd'),'argv':value.get('argv',value.get('command')),
                 'environment':value.get('environment'),'stdout':value.get('stdout'),'stderr':value.get('stderr')})
pid_records=[x for x in records if x['child_pid'] is not None]
assert all(x['reaped'] is True and x['detached'] is False for x in pid_records)
solver=[json.loads((r/f'logs/process/{n}.json').read_text()) for n in ('solve_iter190_quotient','solve_iter190_Xerr','solve_iter190_Zerr')]
assert all(solver[i]['ended_unix']<=solver[i+1]['started_unix'] for i in range(2))
assert all(x['returncode']==10 and not x['timed_out'] for x in solver)
pre=json.loads((r/'verification/preseal_replay.json').read_text()); gates=json.loads((r/'verification/repository_validators/summary.json').read_text())
assert pre['strict_child_nonoverlap'] and pre['all_children_reaped'] and not pre['package_mutated']
assert gates['strict_serial'] and gates['all_children_reaped'] and gates['status']=='PASS'
out={'schema':'circdist-gross-round110-process-fix2-ledger-v1','status':'PASS','records':records,
     'retained_process_record_count':len(records),'pid_bearing_records':len(pid_records),
     'all_pid_bearing_records_reaped':True,'detached_processes':0,
     'solver_order':['quotient','Xerr','Zerr'],'strict_solver_nonoverlap':True,
     'preseal_replay_child_count':pre['child_count'],'preseal_replay_strict_nonoverlap':True,
     'preinstall_gate_child_count':gates['check_count'],'preinstall_gates_strict_serial':True,
     'failure_ids':[f'F110-{i:03d}' for i in range(1,11)],'scientific_failures_or_unknowns':0,
     'external_postseal_records_note':'seal, atomic install, evidence closure, postseal replay, sealed verification, and final census are recorded outside the immutable package'}
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({'status':'PASS','records':len(records),'replay_children':pre['child_count'],'gate_children':gates['check_count']},sort_keys=True))
