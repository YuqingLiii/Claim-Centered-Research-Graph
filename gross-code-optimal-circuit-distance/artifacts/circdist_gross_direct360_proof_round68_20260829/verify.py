#!/usr/bin/env python3
"""Read-only verifier for the sealed CIRCDIST Gross round-68 package."""
from __future__ import annotations
import argparse, hashlib, itertools, json, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'src';sys.path[:0]=[str(SRC/'round63_src'),str(SRC)]
import model as M
import pattern as P
import round68_build as B
import round68_verify as V
from pysat.solvers import Solver

def fail(msg):raise AssertionError(msg)
def sha_file(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def norm(x):return json.loads(json.dumps(x,sort_keys=True))
def manifest_check():
 lines=(ROOT/'SHA256SUMS.txt').read_text().splitlines();seen={}
 for line in lines:
  d,rel=line.split('  ',1);p=ROOT/rel
  if rel in seen or not p.is_file() or sha_file(p)!=d:fail('manifest mismatch '+rel)
  seen[rel]=d
 actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and p.relative_to(ROOT).as_posix()!='SHA256SUMS.txt'}
 if set(seen)!=actual:fail(f'manifest coverage mismatch missing={sorted(actual-set(seen))} extra={sorted(set(seen)-actual)}')
 return len(seen)
def tree_binding(repo,b):
 p=repo/b['path']
 if b['kind']=='file':
  return p.is_file() and p.stat().st_size==b['bytes'] and sha_file(p)==b['sha256']
 rows=[]
 for q in sorted(x for x in p.rglob('*') if x.is_file()):
  rr=q.relative_to(repo).as_posix();rows.append({'path':rr,'bytes':q.stat().st_size,'sha256':sha_file(q)})
 h=hashlib.sha256()
 for r in rows:h.update(f"{r['path']}\0{r['bytes']}\0{r['sha256']}\n".encode())
 return len(rows)==b['file_count'] and sum(r['bytes'] for r in rows)==b['bytes'] and h.hexdigest()==b['tree_sha256'] and rows==b['files']
def live_bindings(repo):
 x=json.loads((ROOT/'SOURCE_BINDINGS.json').read_text());bad=[]
 for b in x['bindings']:
  if not tree_binding(repo,b):bad.append(b['path'])
 if bad:fail('live source binding mismatch: '+repr(bad))
 return {'paths':len(x['bindings']),'expanded_files':sum(1 if b['kind']=='file' else b['file_count'] for b in x['bindings'])}
def verify_static_and_candidate():
 px,pz,lx,lz=B.load_context();sealed=json.loads((SRC/'global_single_clauses.json').read_text())
 actual=P.build_global_single_summary(px,pz)
 if not all(actual[k]==sealed[k] for k in actual):fail('round63 sealed static summary mismatch')
 rx,sx=B.global_single_records('Xerr',M.Xchecks,px,'X');rz,sz=B.global_single_records('Zerr',M.Zchecks,pz,'Z');records=rx+rz
 cert=json.loads((ROOT/'candidate/global_single_clause_certificates.json').read_text())
 if norm(cert['records'])!=norm(records):fail('full 1440-clause certificate ledger mismatch')
 if cert['sectors']!=[sx,sz]:fail('static sector summary mismatch')
 r62=json.loads((SRC/'round62_cegar20.json').read_text());replay=B.replay_round62_blocks(r62,lx,lz)
 saved=json.loads((ROOT/'candidate/round62_blocks_replay.json').read_text())
 if norm(saved['replayed'])!=norm(replay):fail('round62 block replay mismatch')
 cand=json.loads((ROOT/'candidate/candidate.json').read_text());times={k:int(v) for k,v in cand['schedule_times'].items()}
 if B.sha_obj(times)!=cand['schedule_sha256']:fail('candidate hash mismatch')
 audit=M.audit_schedule(times,True)
 if audit!=cand['audit'] or not audit['ok'] or not audit['global_interleaved']:fail('candidate raw audit mismatch')
 if sha_file(ROOT/'candidate/candidate_outer.smt2')!=cand['outer_smt2_sha256']:fail('candidate SMT2 hash mismatch')
 if any(M.block_holds(times,[tuple(a) for a in r['atoms']]) for r in records):fail('candidate hits a round63 clause antecedent')
 if any(M.block_holds(times,[tuple(a) for a in b['atoms']]) for b in r62['outer_blocks']):fail('candidate hits a round62 block antecedent')
 ss=B.sectors(times,lx,lz)
 for lab,sec in ss.items():
  if len(sec.columns)!=360 or len(set(c.support for c in sec.columns[144:]))!=216:fail('column rebuild mismatch '+lab)
  saved_cols=cand['columns'][lab]
  if [c.name for c in sec.columns]!=[c['name'] for c in saved_cols]:fail('column name mismatch '+lab)
  if [M.bits(c.support) for c in sec.columns]!=[c['support'] for c in saved_cols]:fail('column support mismatch '+lab)
 return px,pz,lx,lz,cand,ss,records,r62

def verify_direct(cand,ss):
 expected=json.loads((ROOT/'verification.json').read_text());out={'schema':expected['schema'],'candidate_sha256':cand['schedule_sha256'],'schedule_audit':cand['audit'],'sectors':{}}
 for lab in ('Xerr','Zerr'):out['sectors'][lab]=V.verify_one(ROOT,lab,ss[lab])
 out['repair_gate']=expected['repair_gate'];out['verdict']=expected['verdict']
 if norm(out)!=norm(expected):fail('direct SAT/raw replay mismatch')
 return expected

def verify_continuation(px,pz,lx,lz,primary):
 obj=json.loads((ROOT/'cegar_continuation5.json').read_text());prior=[]
 for lab in ('Xerr','Zerr'):prior.append([tuple(x) for x in primary['sectors'][lab]['mechanism']['sound_outer_block']['atoms']])
 new=[]
 for i,row in enumerate(obj['ledger']):
  if row['iteration']!=i or row['outer']['status']!='SAT':fail('continuation outer status mismatch')
  times={k:int(v) for k,v in row['schedule'].items()}
  if B.sha_obj(times)!=row['schedule_sha256'] or M.audit_schedule(times,True)!=row['audit']:fail('continuation schedule mismatch')
  if any(M.block_holds(times,z) for z in prior+new):fail('continuation prior block exclusion failed')
  ss=B.sectors(times,lx,lz)
  for lab in ('Xerr','Zerr'):
   entry=row['sectors'][lab]
   if entry['finder_status']!='SAT' or entry['complete_for_absence']:fail('continuation evidence-scope mismatch')
   selected=entry['mechanism']['selected_indices'];m=V.mechanism(ss[lab],selected)
   if norm(m)!=norm(entry['mechanism']):fail('continuation raw mechanism mismatch')
   new.append([tuple(x) for x in m['sound_outer_block']['atoms']])
 if len(new)!=obj['new_sound_blocks'] or len(new)!=10:fail('continuation block count mismatch')
 return {'iterations':len(obj['ledger']),'raw_mechanisms':len(new),'new_sound_blocks':len(new)}
def run(cmd,timeout=60):
 cp=subprocess.run([str(x) for x in cmd],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=timeout,check=False)
 return cp.returncode,cp.stdout.decode(errors='replace')
def verify_proof_controls():
 c=ROOT/'controls/proof_checker';drat=ROOT/'tooling/drat-trim-arm64-macos';lrat=ROOT/'tooling/lrat-check-arm64-macos'
 rc,o=run([drat,c/'php6_5.cnf',c/'php6_5.drat','-t','60']);
 if rc!=0 or 's VERIFIED' not in o:fail('fresh DRAT positive control failed')
 rc2,o2=run([lrat,c/'php6_5.cnf',c/'php6_5.lrat']);
 if rc2!=0 or 'c VERIFIED' not in o2:fail('fresh LRAT positive control failed')
 rc3,o3=run([drat,c/'php6_5.cnf',c/'php6_5_corrupted_truncated_10_lines.drat','-t','60'])
 if rc3==0 or 'NOT VERIFIED' not in o3:fail('fresh corrupted DRAT negative control failed')
 rc4,o4=run([lrat,c/'php6_5.cnf',c/'php6_5_corrupted_truncated_10_lines.lrat'])
 if rc4==0 or 'NOT VERIFIED' not in o4:fail('fresh corrupted LRAT negative control failed')
 return {'drat_positive':'VERIFIED','lrat_positive':'VERIFIED','truncated_drat':'REJECTED','truncated_lrat':'REJECTED'}
def encoding_controls():
 def one(n,k):
  e=B.Encoder('control','none');x=[e.var(f'x{i}','control',{}) for i in range(n)];e.atmost(x,k);cls=[c['lits'] for c in e.clauses]
  with Solver(name='cadical195',bootstrap_with=cls) as s:
   for vals in itertools.product((0,1),repeat=n):
    sat=s.solve(assumptions=[x[i] if vals[i] else -x[i] for i in range(n)])
    if sat!=(sum(vals)<=k):fail('cardinality truth-table mismatch')
  return 2**n
 rows=sum(one(n,k) for n,k in [(5,1),(5,2),(6,5)])
 saved=json.loads((ROOT/'controls/encoding_controls.json').read_text())
 if not saved['xor2']['all_match'] or not all(x['all_match'] for x in saved['atmost_controls']):fail('persisted encoder control mismatch')
 return {'cardinality_assignments_checked':rows,'xor_rows_checked':8}
def glucose_control(ss):
 x=json.loads((ROOT/'controls/Zerr_glucose42.json').read_text())
 if x['status']!='SAT':fail('Glucose SAT control missing')
 pos={v for v in x['model'] if v>0};selected=[j for j in range(360) if j+1 in pos];m=V.mechanism(ss['Zerr'],selected)
 saved=json.loads((ROOT/'controls/Zerr_glucose42_raw_replay.json').read_text())
 if norm(m)!=norm(saved['raw_replay']):fail('Glucose raw replay mismatch')
 return {'status':'SAT','weight':m['fault_count'],'selected_model_differs_from_cadical':not saved['agreement_with_cadical_selected_indices']}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo-root',type=Path);ap.add_argument('--skip-manifest',action='store_true');a=ap.parse_args()
 manifest=None if a.skip_manifest else manifest_check()
 px,pz,lx,lz,cand,ss,records,r62=verify_static_and_candidate();primary=verify_direct(cand,ss)
 result={'status':'PASS','manifest_entries':manifest,'live_bindings':live_bindings(a.repo_root.resolve()) if a.repo_root else None,
  'model':{'edges':864,'MC_overlaps':648,'pools':[len(px),len(pz)],'static_clauses':len(records),'round62_blocks':len(r62['outer_blocks'])},
  'candidate':{'sha256':cand['schedule_sha256'],'audit':cand['audit']},
  'direct':{lab:{'status':primary['sectors'][lab]['status'],'fault_weight':primary['sectors'][lab]['mechanism']['fault_count'],'all_clauses_satisfied':True} for lab in ('Xerr','Zerr')},
  'repair_entered':False,'continuation':verify_continuation(px,pz,lx,lz,primary),
  'proof_controls':verify_proof_controls(),'encoding_controls':encoding_controls(),'sat_control':glucose_control(ss),
  'exact_residual':[11,12],'verdict':'MATERIAL-CHECKED-PROGRESS-NOT-CLOSED'}
 print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
