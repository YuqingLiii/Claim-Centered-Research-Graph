#!/usr/bin/env python3
"""Build the retained Round108 FIX-2 process ledger."""
from pathlib import Path
import argparse, collections, json

def load(p): return json.loads(Path(p).read_text())
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args(); root=a.root.resolve()
    records=[]
    for folder in ('logs/process','verification/logs/process'):
        for p in sorted((root/folder).glob('*.json')):
            row=load(p)
            if row.get('schema')!='circdist-gross-round108-process-record-v1': continue
            assert row['reaped'] is True and row['detached'] is False and row['timed_out'] is False
            assert row['ended_unix']>=row['started_unix'] and row['child_pid']>0
            records.append({'path':p.relative_to(root).as_posix(),**row})
    top=sorted(records,key=lambda x:x['started_unix'])
    top_overlaps=[]
    for left,right in zip(top,top[1:]):
        if left['ended_unix']>right['started_unix']:
            top_overlaps.append({'left':left['name'],'right':right['name'],'left_end':left['ended_unix'],'right_start':right['started_unix']})
    assert not top_overlaps, top_overlaps
    solvers=[]
    for row in records:
        cmd=row.get('command',[])
        if cmd and 'cadical' in Path(str(cmd[0])).name:
            solvers.append({'name':row['name'],'path':row['path'],'pid':row['child_pid'],'started_unix':row['started_unix'],'ended_unix':row['ended_unix'],'wall_seconds':row['wall_seconds'],'returncode':row['returncode'],'timed_out':row['timed_out'],'reaped':row['reaped'],'detached':row['detached']})
    solvers.sort(key=lambda x:x['started_unix'])
    assert len(solvers)==3 and [x['returncode'] for x in solvers]==[10,10,10]
    assert all(a['ended_unix']<=b['started_unix'] for a,b in zip(solvers,solvers[1:]))
    failures=[{'name':x['name'],'path':x['path'],'pid':x['child_pid'],'returncode':x['returncode'],'timed_out':x['timed_out'],'reaped':x['reaped']} for x in records if x['returncode'] not in (0,10,20)]
    assert len(failures)==1 and failures[0]['name']=='advance_iter190_full_invariant_frontier' and failures[0]['returncode']==1
    pre=load(root/'verification/preseal_replay.json'); validators=load(root/'verification/repository_validators/summary.json'); proof=load(root/'verification/proof_controls.json')
    assert pre['status']==validators['status']==proof['status']=='PASS'
    assert pre['direct_child_count']==18 and pre['all_children_reaped'] and pre['strict_child_nonoverlap']
    assert validators['all_children_reaped'] and validators['detached_processes']==0
    runs=proof['runs']; assert len(runs)==6
    assert [x['returncode'] for x in runs]==[0,0,1,1,1,1]
    assert all(x['reaped'] and not x['timed_out'] and not x['detached'] for x in runs)
    assert all(a['ended_unix']<=b['started_unix'] for a,b in zip(runs,runs[1:]))
    post_path=root/'verification/postseal_replay.json'; post=load(post_path) if post_path.exists() else None
    if post is not None:
        assert post['status']=='PASS' and post['direct_child_count']==18 and post['all_children_reaped'] and post['strict_child_nonoverlap']
    census_path=root/'verification/final_process_census.json'
    census=load(census_path) if census_path.exists() else None
    if census is not None: assert census['status']=='PASS' and census['science_survivor_count']==0 and census['ps_child_reaped']
    pre_census_path=root/'verification/pre_payload_process_census.json'; pre_census=load(pre_census_path) if pre_census_path.exists() else None
    if pre_census is not None: assert pre_census['status']=='PASS' and pre_census['science_survivor_count']==0
    result={'schema':'circdist-gross-round108-process-fix2-ledger-v1','status':'PASS','retained_pid_record_count':len(records),'records':records,
      'returncodes':dict(sorted(collections.Counter(str(x['returncode']) for x in records).items())),
      'strict_top_level_nonoverlap':True,'top_level_overlaps':top_overlaps,
      'solver_intervals':solvers,'solver_interval_count':3,'strict_solver_nonoverlap':True,'solver_overlaps':[],
      'recorded_failed_attempts':failures,
      'preseal_replay_children':pre['children'],'preseal_replay_child_count':18,
      'postpayload_replay_children':post['children'] if post else [],'postpayload_replay_child_count':post['direct_child_count'] if post else 0,'postpayload_replay_status':post['status'] if post else 'PENDING',
      'repository_validator_children':validators['checks'],'repository_validator_child_count':validators['check_count'],
      'proof_control_nested_children':runs,'proof_control_nested_child_count':6,
      'pre_payload_process_census':pre_census,'final_process_census':census,
      'all_pid_bearing_children_reaped':True,'retained_wrapper_timeouts':0,'retained_detached_processes':0,
      'science_survivor_count':census['science_survivor_count'] if census else (pre_census['science_survivor_count'] if pre_census else 0),
      'scope_note':'The ledger builder cannot include its own still-running wrapper record. Read-only inspection and Codex transport calls are disclosed in FAILURE_LEDGER.md; every solver, science checker, replay, gate, proof-control and census child is PID-recorded.'}
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','pid_records':len(records),'solvers':3,'failed_attempts':1,'preseal_children':18,'postpayload':result['postpayload_replay_status'],'science_survivors':result['science_survivor_count']},sort_keys=True))
if __name__=='__main__': main()
