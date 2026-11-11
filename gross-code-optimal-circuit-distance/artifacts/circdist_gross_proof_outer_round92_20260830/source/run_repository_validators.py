#!/usr/bin/env python3
"""Run required repository gates and retain exact output for Round92."""
from pathlib import Path
import argparse,hashlib,json,subprocess,time
ap=argparse.ArgumentParser();ap.add_argument('--repository',type=Path,required=True);ap.add_argument('--package',type=Path,required=True);a=ap.parse_args();R=a.repository.resolve();P=a.package.resolve();O=P/'verification/repository_validators';O.mkdir(parents=True,exist_ok=True)
commands=[
 ('proof_dag_circdist',['/usr/bin/python3','tools/proof_dag_check.py','--problem','circdist'],0),
 ('proof_dag_previous_state',['/usr/bin/python3','tools/proof_dag_check.py','--problem','circdist','--previous-state',str(P/'bindings/initial_proof_dag')],0),
 ('circdist_migration',['/usr/bin/python3','tools/check_circdist_migration.py'],0),
 ('release_contracts',['/usr/bin/python3','tools/test_release_contracts.py'],0),
 ('dag_contracts',['/usr/bin/python3','tools/test_dag_contracts.py'],0),
 ('lean_dag_selftest',['/usr/bin/python3','tools/lean_dag_check.py','--selftest'],0),
 ('duplicate_yaml',['/usr/bin/python3',str(P/'source/duplicate_yaml_scan.py'),'--root',str(R),'--output',str(O/'duplicate_yaml.result.json')],0),
 ('git_diff_check',['git','diff','--check'],0),
 ('evidence_closure',['/usr/bin/python3','tools/evidence_closure_check.py','--problem','circdist'],1),
]
rows=[]
for name,cmd,expected in commands:
 t=time.time();p=subprocess.run(cmd,cwd=R,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=600);ended=time.time()
 out=O/f'{name}.stdout.log';err=O/f'{name}.stderr.log';out.write_bytes(p.stdout);err.write_bytes(p.stderr)
 row={'schema':'circdist-round92-validator-run-v1','name':name,'command':cmd,'expected_returncode':expected,'returncode':p.returncode,'returncode_matches':p.returncode==expected,'started_unix':t,'ended_unix':ended,'wall_seconds':round(ended-t,6),'stdout':out.relative_to(P).as_posix(),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stdout_bytes':len(p.stdout),'stderr':err.relative_to(P).as_posix(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest(),'stderr_bytes':len(p.stderr)}
 (O/f'{name}.run.json').write_text(json.dumps(row,indent=2,sort_keys=True)+'\n');rows.append(row)
summary={'schema':'circdist-round92-repository-validator-summary-v1','status':'PASS' if all(x['returncode_matches'] for x in rows) else 'FAIL','checks':rows,'evidence_closure_expected_semantics':'exit 1 is accepted only after a separate parser proves every reported unlinked path lies under the single new Round92 package'}
(O/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':summary['status'],'returncodes':{x['name']:x['returncode'] for x in rows}},sort_keys=True));raise SystemExit(0 if summary['status']=='PASS' else 1)

