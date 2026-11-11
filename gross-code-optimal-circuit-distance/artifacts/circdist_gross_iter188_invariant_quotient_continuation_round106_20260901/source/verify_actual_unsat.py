#!/usr/bin/env python3
"""Check a real DRAT, generate/check LRAT, and run proof-specific rejection controls."""
from pathlib import Path
import argparse, hashlib, json, subprocess, time

ap=argparse.ArgumentParser(); ap.add_argument('--formula',type=Path,required=True); ap.add_argument('--proof',type=Path,required=True); ap.add_argument('--tooling',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
a.output.mkdir(parents=True,exist_ok=True); drat=a.tooling/'drat-trim-arm64-macos'; lcheck=a.tooling/'lrat-check-arm64-macos'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
rows=[]
def run(name,cmd,expected):
 t=time.time(); cp=subprocess.run([str(x) for x in cmd],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=1800)
 row={'name':name,'command':[str(x) for x in cmd],'returncode':cp.returncode,'expected_returncode':expected,'stdout':cp.stdout,'stderr':cp.stderr,'wall_seconds':round(time.time()-t,6),'reaped':True,'detached':False}; rows.append(row); assert cp.returncode==expected,(name,cp.returncode,cp.stdout[-2000:],cp.stderr[-2000:]); return row
assert a.formula.is_file() and a.proof.is_file() and a.proof.stat().st_size>0
lrat=a.output/'accepted.lrat'
run('valid_drat_generate_lrat',[drat,a.formula,a.proof,'-t','1700','-L',lrat],0); assert lrat.stat().st_size>0
run('valid_lrat',[lcheck,a.formula,lrat],0)
raw=a.proof.read_bytes(); lr=lrat.read_bytes()
trunc=a.output/'truncated.drat'; corrupt=a.output/'corrupt.drat'; trunc.write_bytes(raw[:max(1,len(raw)//2)]); corrupt.write_bytes(b'not-a-valid-proof\n')
ltrunc=a.output/'truncated.lrat'; lcorrupt=a.output/'corrupt.lrat'; ltrunc.write_bytes(lr[:max(1,len(lr)//2)]); lcorrupt.write_bytes(b'not-a-valid-lrat\n')
run('truncated_drat_rejected',[drat,a.formula,trunc,'-t','1700'],1); run('corrupt_drat_rejected',[drat,a.formula,corrupt,'-t','1700'],1)
run('truncated_lrat_rejected',[lcheck,a.formula,ltrunc],1); run('corrupt_lrat_rejected',[lcheck,a.formula,lcorrupt],1)
out={'schema':'circdist-round96-actual-unsat-certificate-v1','status':'PASS','formula_sha256':sha(a.formula),'drat_sha256':sha(a.proof),'lrat_sha256':sha(lrat),'drat_bytes':a.proof.stat().st_size,'lrat_bytes':lrat.stat().st_size,'valid_drat_accepted':True,'generated_lrat_accepted':True,'corrupt_drat_rejected':True,'truncated_drat_rejected':True,'corrupt_lrat_rejected':True,'truncated_lrat_rejected':True,'processes':rows,'all_children_reaped':True,'detached_processes':0}
(a.output/'certificate.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({k:out[k] for k in ('status','formula_sha256','drat_sha256','lrat_sha256')},sort_keys=True))
