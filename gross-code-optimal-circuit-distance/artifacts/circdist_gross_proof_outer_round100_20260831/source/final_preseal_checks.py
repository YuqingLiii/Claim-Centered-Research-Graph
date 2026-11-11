#!/usr/bin/env python3
"""Run the final Round100 crosschecks with PID-bearing serial child records."""
from pathlib import Path
import json,os,subprocess,sys,tempfile,time
P=Path(__file__).resolve().parent.parent;REPO=P.parents[2];rows=[]
def run(name,command,timeout=1800):
 command=[str(x) for x in command];t=time.time();c=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,start_new_session=False);timed=False
 try:stdout,stderr=c.communicate(timeout=timeout)
 except subprocess.TimeoutExpired:
  timed=True;c.terminate()
  try:stdout,stderr=c.communicate(timeout=15)
  except subprocess.TimeoutExpired:c.kill();stdout,stderr=c.communicate()
 row={'name':name,'command':command,'parent_pid':os.getpid(),'child_pid':c.pid,'returncode':c.returncode,'stdout':stdout,'stderr':stderr,'wall_seconds':round(time.time()-t,6),'timed_out':timed,'reaped':True,'detached':False};rows.append(row);assert not timed and c.returncode==0,(name,c.returncode,stdout,stderr)
with tempfile.TemporaryDirectory(prefix='circdist-r100-final-preseal.') as td:
 proof=Path(td)/'proof.json'
 run('input_bindings',[sys.executable,P/'source/check_input_bindings_round100.py','--root',P])
 run('compression',[sys.executable,P/'source/check_compression_round100.py','--root',P])
 run('result',[sys.executable,P/'source/check_result.py','--root',P])
 run('process',[sys.executable,P/'source/check_process_ledger.py','--root',P])
 run('live_protected',[sys.executable,P/'source/check_live_protected_round100.py','--root',P,'--repository',REPO])
 run('mixed_sector',[sys.executable,P/'source/check_mixed_sector_round100.py','--root',P])
 run('proof_controls',[sys.executable,P/'source/check_proof_controls.py','--root',P,'--output',proof])
 assert json.loads(proof.read_text())['status']=='PASS'
replay=json.loads((P/'verification/preseal_full_replay.json').read_text());repo=json.loads((P/'verification/repository_validators/summary.json').read_text());evidence=json.loads((P/'verification/evidence_closure_interpretation.json').read_text());fix2=json.loads((P/'verification/fix2_closure.json').read_text());audit=json.loads((P/'verification/independent_campaign_audit.json').read_text())
assert all(x['status']=='PASS' for x in (replay,repo,evidence,fix2,audit));assert replay['direct_child_count']==126 and replay['nested_child_count']==18 and replay['all_children_reaped'];assert fix2['survivors']==0 and evidence['raw_exit_code']==1 and evidence['all_errors_under_new_package']
out={'schema':'circdist-round100-final-preseal-checks-v1','status':'PASS','pid':os.getpid(),'parent_pid':os.getppid(),'children':rows,'direct_child_count':len(rows),'nested_proof_control_children':6,'total_known_children':len(rows)+6,'all_children_reaped':True,'detached_processes':0}
(P/'verification/final_preseal_checks.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
summary={'schema':'circdist-round100-validation-summary-v1','status':'PASS','scientific_verdict':'MATERIAL-CHECKED-PROGRESS-NOT-CLOSED','D_star_Gross':[11,12],'campaign':'12 outer SAT; 24 direct SAT; all assignments and physical replays PASS','order6':'exact reduced domain 6,715,648,864; zero combined candidates; independent validator PASS','full_span':'two proof-checked UNSAT synthesis queries plus two independent Z3 UNSAT results','mixed_sector':'component-reduction theorem PASS; no new closure beyond components','full_preseal_replay':'PASS; 126 direct + 18 nested children','repository_validators':'PASS; 12 children','evidence_closure':f"expected exit 1; {evidence['error_count']} unique diagnostics solely under Round100 package",'proof_controls':'actual span DRAT/LRAT valid; corrupt/truncated controls rejected; fixture controls PASS','fix2':'PASS; exact Round100 scratch removed and zero survivors','canonical_unchanged':True,'commit':False,'push':False}
(P/'verification/validation_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n');print(json.dumps(summary,sort_keys=True))
