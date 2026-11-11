#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,hashlib,json,subprocess,time
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();C=R/'controls/round76_proof_checker';T=R/'tooling'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(name,cmd,want,marker):
 t=time.monotonic();started=datetime.datetime.now(datetime.timezone.utc).isoformat();cp=subprocess.run([str(x) for x in cmd],stdout=subprocess.PIPE,stderr=subprocess.STDOUT);ended=datetime.datetime.now(datetime.timezone.utc).isoformat();(C/f'{name}.log').write_bytes(cp.stdout)
 rec={'schema':'round76-proof-control-run-v1','name':name,'argv':[str(x).replace(str(R),'PACKAGE') for x in cmd],'started_utc':started,'ended_utc':ended,'wall_seconds':time.monotonic()-t,'exit_code':cp.returncode,'expected_exit':want,'marker':marker,'log':f'controls/round76_proof_checker/{name}.log','log_sha256':hashlib.sha256(cp.stdout).hexdigest()};(C/f'{name}.run.json').write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n');assert cp.returncode==want and marker.encode() in cp.stdout,(name,cp.returncode,cp.stdout[-1000:]);return rec
cnf=C/'php6_5.cnf';drat=C/'php6_5.drat';lrat=C/'php6_5.generated.lrat';dc=C/'php6_5_corrupted_truncated_10_lines.drat';lc=C/'php6_5_corrupted_truncated_10_lines.lrat'
records=[]
records.append(run('drat_valid',[T/'drat-trim-arm64-macos',cnf,drat,'-t','170','-L',lrat],0,'VERIFIED'))
records.append(run('lrat_valid',[T/'lrat-check-arm64-macos',cnf,lrat],0,'VERIFIED'))
records.append(run('drat_corrupt',[T/'drat-trim-arm64-macos',cnf,dc,'-t','170'],1,'NOT VERIFIED'))
records.append(run('lrat_corrupt',[T/'lrat-check-arm64-macos',cnf,lc],1,'NOT VERIFIED'))
summary={'schema':'round76-proof-checker-controls-v1','status':'PASS','scope':'toolchain valid/corrupt controls only; no candidate returned UNSAT, so these are not Gross absence proofs','fixtures':{p.name:{'bytes':p.stat().st_size,'sha256':sha(p)} for p in [cnf,drat,lrat,dc,lc]},'records':records}
(C/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n');print(json.dumps(summary,sort_keys=True))
