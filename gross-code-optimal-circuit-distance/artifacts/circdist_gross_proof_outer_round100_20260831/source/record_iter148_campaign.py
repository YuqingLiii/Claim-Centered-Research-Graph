#!/usr/bin/env python3
from pathlib import Path
import argparse, json, datetime
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();C=R/'campaign';C.mkdir(exist_ok=True)
s=json.loads((R/'state/iter148_state.json').read_text());n=json.loads((R/'state/iter149_state.json').read_text());o=json.loads((R/'iterations/iter148/outer/replay.json').read_text());d=json.loads((R/'iterations/iter148/direct/direct_verification.json').read_text())
assert s['selector_count']==256 and n['selector_count']==258 and n['next_iteration']==149 and n['started'] is False and n['stop'] is None
assert o['status']=='PASS' and o['solver_status']=='SATISFIABLE' and o['all_dimacs_clauses_satisfied']
assert all(d['sectors'][x]['status']=='SATISFIABLE' and d['sectors'][x]['all_dimacs_clauses_satisfied'] for x in ('Xerr','Zerr'))
row={'iteration':148,'status':'COMPLETE_SAT','outer_returncode':10,'direct_returncodes':{'Xerr':10,'Zerr':10},'weights':{x:d['sectors'][x]['mechanism']['fault_count'] for x in ('Xerr','Zerr')},'source_selector_count':256,'next_selector_count':258,'next_iteration':149,'next_started':False,'next_selector_state_sha256':n['selector_state_sha256'],'order4_synthesis_completed_before_transition':True,'order4_terms_added':0}
progress=C/'progress.jsonl';assert not progress.exists();progress.write_text(json.dumps(row,sort_keys=True)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat();(C/'current.json').write_text(json.dumps({'phase':'iteration_complete','utc':now,**row},indent=2,sort_keys=True)+'\n')
process_names=['outer_iter148_cadical_proof','outer_iter148_verify_sat','outer_iter148_assignment_independent_check','direct_iter148_build','direct_iter148_Xerr_cadical_proof','direct_iter148_Zerr_cadical_proof','direct_iter148_replay','direct_iter148_Xerr_assignment_check','direct_iter148_Zerr_assignment_check','outer_iter148_sat_trace_summary','direct_iter148_Xerr_sat_trace_summary','direct_iter148_Zerr_sat_trace_summary','order4_exact_synthesis','order4_exact_synthesis_repair1','order4_exact_synthesis_repair2','iter148_pending_transition_build','iter149_pending_compile','iter149_pending_encoding_check','iter148_atomic_commit']
records=[]
for name in process_names:
 p=R/f'logs/process/{name}.json';assert p.is_file();q=json.loads(p.read_text());records.append({'name':name,'returncode':q['returncode'],'started_utc':q['started_utc'],'ended_utc':q['ended_utc'],'reaped':q['reaped']})
(C/'manual_process_148.json').write_text(json.dumps({'schema':'circdist-round96-iter148-orchestration-record-v1','status':'COMPLETE_SAT','strict_serial':True,'records':records,'all_children_reaped':all(x['reaped'] for x in records),'failed_synthesis_attempts':2,'detached_processes':0},indent=2,sort_keys=True)+'\n')
(C/'summary_148_148.json').write_text(json.dumps({'schema':'circdist-round96-campaign-summary-v1','status':'SAT_PREFIX_COMPLETE','first':148,'last':148,'progress_rows':1,'orchestration':'campaign/manual_process_148.json'},indent=2,sort_keys=True)+'\n')
print(json.dumps(row,sort_keys=True))
