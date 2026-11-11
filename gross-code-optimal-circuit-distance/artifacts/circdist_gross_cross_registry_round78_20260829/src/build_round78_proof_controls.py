#!/usr/bin/env python3
from pathlib import Path
import argparse, datetime, hashlib, json, subprocess, time

ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); a=ap.parse_args()
R=a.root.resolve(); C=R/'controls/round78_proof_checker'; T=R/'tooling'; C.mkdir(parents=True,exist_ok=False)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,o): Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def run(name,cmd,want,markers):
    t=time.monotonic(); started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    cp=subprocess.run([str(x) for x in cmd],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=30)
    ended=datetime.datetime.now(datetime.timezone.utc).isoformat(); (C/f'{name}.log').write_bytes(cp.stdout)
    rec={'schema':'round78-proof-control-run-v1','name':name,'argv':[str(x).replace(str(R),'PACKAGE') for x in cmd],
         'started_utc':started,'ended_utc':ended,'wall_seconds':time.monotonic()-t,'exit_code':cp.returncode,
         'expected_exit':want,'required_marker_any':markers,'log':f'controls/round78_proof_checker/{name}.log','log_sha256':hashlib.sha256(cp.stdout).hexdigest()}
    dump(C/f'{name}.run.json',rec)
    assert cp.returncode==want and any(x.encode() in cp.stdout for x in markers),(name,cp.returncode,cp.stdout[-2000:])
    return rec

# Deterministic PHP(6,5): every pigeon has exactly one hole and no hole has two pigeons.
def v(p,h): return p*5+h+1
clauses=[]
for p in range(6):
    clauses.append([v(p,h) for h in range(5)])
    for h in range(5):
        for k in range(h+1,5): clauses.append([-v(p,h),-v(p,k)])
for h in range(5):
    for p in range(6):
        for q in range(p+1,6): clauses.append([-v(p,h),-v(q,h)])
assert len(clauses)==141
cnf=C/'php6_5.cnf'; cnf.write_text('c fresh round78 pigeonhole PHP(6,5) proof-control fixture\n'+'p cnf 30 141\n'+''.join(' '.join(map(str,c))+' 0\n' for c in clauses))
drat=C/'php6_5.fresh.drat'; lrat=C/'php6_5.fresh.lrat'
records=[]
records.append(run('proof_generate',[T/'cadical-1.9.5-arm64-macos','--no-binary',cnf,drat],20,['UNSATISFIABLE']))
records.append(run('drat_valid_generate_lrat',[T/'drat-trim-arm64-macos',cnf,drat,'-t','170','-L',lrat],0,['VERIFIED']))
records.append(run('lrat_valid',[T/'lrat-check-arm64-macos',cnf,lrat],0,['VERIFIED']))
dl=drat.read_bytes().splitlines(keepends=True); ll=lrat.read_bytes().splitlines(keepends=True); assert len(dl)>20 and len(ll)>20
dc=C/'php6_5.corrupt.drat'; dt=C/'php6_5.truncated.drat'; lc=C/'php6_5.corrupt.lrat'; lt=C/'php6_5.truncated.lrat'
dc.write_bytes(b'x syntactically-corrupt-drat-control\n'+drat.read_bytes()); dt.write_bytes(b''.join(dl[:10]))
lc.write_bytes(b'x syntactically-corrupt-lrat-control\n'+lrat.read_bytes()); lt.write_bytes(b''.join(ll[:10]))
records.append(run('drat_corrupt',[T/'drat-trim-arm64-macos',cnf,dc,'-t','170'],1,['NOT VERIFIED','ERROR']))
records.append(run('drat_truncated',[T/'drat-trim-arm64-macos',cnf,dt,'-t','170'],1,['NOT VERIFIED','ERROR']))
records.append(run('lrat_corrupt',[T/'lrat-check-arm64-macos',cnf,lc],1,['NOT VERIFIED','ERROR']))
records.append(run('lrat_truncated',[T/'lrat-check-arm64-macos',cnf,lt],1,['NOT VERIFIED','ERROR']))
fixtures=[cnf,drat,lrat,dc,dt,lc,lt]
summary={'schema':'round78-proof-checker-controls-v1','status':'PASS','fresh_generation':True,
 'scope':'fresh toolchain valid/corrupt/truncated controls only; no candidate or outer returned UNSAT, so these are not Gross absence or closure proofs',
 'fixtures':{p.name:{'bytes':p.stat().st_size,'sha256':sha(p)} for p in fixtures},'records':records,
 'counts':{'proof_generation_unsat':1,'valid_accepts':2,'corrupt_rejects':2,'truncated_rejects':2,'candidate_specific_gross_proofs':0}}
dump(C/'summary.json',summary); print(json.dumps(summary,sort_keys=True))
