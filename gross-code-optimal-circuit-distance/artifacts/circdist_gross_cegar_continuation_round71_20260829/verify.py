#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse,gzip,hashlib,json,os,shutil,subprocess,sys,tempfile,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
sys.path[:0]=[str(ROOT/'src/round63_src'),str(ROOT/'src')]
import z3
import model as M
import round68_build as B
import round68_verify as V
from outer import OuterScheduler

def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def sha_obj(o):return sha_bytes(json.dumps(o,sort_keys=True,separators=(',',':')).encode())
def data(path):
 p=Path(path)
 if p.suffix=='.gz':
  with gzip.open(p,'rb') as f:return f.read()
 return p.read_bytes()
def load(path):return json.loads(data(path))
def jround(o):return json.loads(json.dumps(o))
def fail(msg):raise AssertionError(msg)

def verify_manifest(allow_unsealed=False):
 p=ROOT/'SHA256SUMS.txt'
 if not p.exists():
  assert allow_unsealed,'missing SHA256SUMS.txt'
  return {'present':False,'entries':0}
 rows=[]
 for line in p.read_text().splitlines():
  if not line.strip():continue
  h,rel=line.split('  ',1);q=ROOT/rel
  assert q.is_file(),('missing',rel)
  assert sha_bytes(q.read_bytes())==h,('hash mismatch',rel)
  rows.append(rel)
 expected=sorted(q.relative_to(ROOT).as_posix() for q in ROOT.rglob('*') if q.is_file() and q.relative_to(ROOT).as_posix()!='SHA256SUMS.txt')
 assert sorted(rows)==expected,(len(rows),len(expected),'manifest coverage')
 pay=ROOT/'PAYLOAD_SHA256SUMS.txt'
 if pay.exists():
  for line in pay.read_text().splitlines():
   if not line.strip():continue
   h,rel=line.split('  ',1);q=ROOT/rel;assert q.is_file() and sha_bytes(q.read_bytes())==h,('payload',rel)
 return {'present':True,'entries':len(rows),'external_root_seal_sha256':sha_bytes(p.read_bytes()),'payload_manifest_present':pay.exists()}

def verify_compression():
 inv=load(ROOT/'COMPRESSED_INVENTORY.json');n=tot=comp=0
 assert inv['file_count']==len(inv['files'])==410
 for r in inv['files']:
  p=ROOT/r['path'];raw=p.read_bytes();assert not (ROOT/r['original_path']).exists()
  assert len(raw)==r['compressed_bytes'] and sha_bytes(raw)==r['compressed_sha256'] and r['gzip_mtime']==0
  z=data(p);assert len(z)==r['uncompressed_bytes'] and sha_bytes(z)==r['uncompressed_sha256'];n+=1;tot+=len(z);comp+=len(raw)
 assert (tot,comp)==(inv['uncompressed_bytes'],inv['compressed_bytes'])
 return {'files':n,'uncompressed_bytes':tot,'compressed_bytes':comp}

def verify_bindings(repo_root=None):
 s=load(ROOT/'SOURCE_BINDINGS.json');assert s['round69_root_seal_sha256']=='aad4434050b1b64d3907b990e8279a2b25b2b4e29abcebf585fb885f3dbab647';assert s['round70_review_sha256']=='b2fe38fd6adb1ef974624a49b84b7a61620a5c97a531155aac01fc39dbfbaabe'
 assert sha_bytes((ROOT/'bindings/snapshots/round69_SHA256SUMS.txt').read_bytes())==s['round69_root_seal_sha256']
 assert sha_bytes((ROOT/'bindings/snapshots/round70_review.md').read_bytes())==s['round70_review_sha256']
 live=0
 for r in s['frozen_inputs']:
  b=(ROOT/r['snapshot']).read_bytes();assert len(b)==r['bytes'] and sha_bytes(b)==r['sha256']
  if repo_root is not None:
   q=repo_root/r['path'];assert q.is_file() and q.read_bytes()==b,r['path'];live+=1
 for r in s['copied_round69_engine']:
  b=(ROOT/r['local_path']).read_bytes();assert len(b)==r['bytes'] and sha_bytes(b)==r['sha256']
  if repo_root is not None:
   q=repo_root/r['round69_path'];assert q.is_file() and q.read_bytes()==b,r['round69_path'];live+=1
 pre=(ROOT/'preflight/round69_full_verifier.log').read_text();assert '"status": "PASS"' in pre and '"sound_terms": 4740' in pre and '"physical_replays": 3368' in pre
 audit=load(ROOT/'preflight/round69_all_file_read.json.gz');assert (audit['file_count'],audit['gzip_count'],audit['tar_member_count'])==(250,112,472)
 assert len((ROOT/'preflight/round69_sha256_check.log').read_text().splitlines())==249
 return {'frozen_bindings':len(s['frozen_inputs']),'engine_bindings':len(s['copied_round69_engine']),'live_files_checked':live,'round69_seal':'PASS','round69_full_replay':'PASS','round70_review_bound':True}

def run_control(cmd,want,marker,timeout=70):
 p=subprocess.run([str(x) for x in cmd],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=timeout)
 assert p.returncode==want and marker in p.stdout,(cmd,p.returncode,p.stdout[-1000:])
 return {'exit_code':p.returncode,'marker':marker}

def verify_proof_controls():
 c=ROOT/'controls/proof_checker';tool=ROOT/'tooling'
 with tempfile.TemporaryDirectory(prefix='circdist_r71_proof_control_') as td:
  lrat=Path(td)/'valid.lrat'
  out={}
  out['drat_valid']=run_control([tool/'drat-trim-arm64-macos',c/'php6_5.cnf',c/'php6_5.drat','-t','60','-L',lrat],0,'VERIFIED')
  out['drat_corrupt']=run_control([tool/'drat-trim-arm64-macos',c/'php6_5.cnf',c/'php6_5_corrupted_truncated_10_lines.drat','-t','60'],1,'NOT VERIFIED')
  out['lrat_valid']=run_control([tool/'lrat-check-arm64-macos',c/'php6_5.cnf',lrat],0,'VERIFIED')
  out['lrat_corrupt']=run_control([tool/'lrat-check-arm64-macos',c/'php6_5.cnf',c/'php6_5_corrupted_truncated_10_lines.lrat'],1,'NOT VERIFIED')
 return out

def load_outer_context():
 px,pz,lx,lz=B.load_context();assert len(px)==len(pz)==1884
 rx,_=B.global_single_records('Xerr',M.Xchecks,px,'X');rz,_=B.global_single_records('Zerr',M.Zchecks,pz,'Z');records=rx+rz;assert len(records)==1440
 r62=load(ROOT/'src/round62_cegar20.json');B.replay_round62_blocks(r62,lx,lz);assert len(r62['outer_blocks'])==20
 pair=load(ROOT/'classification/pair_classification.json.gz');general=[(f"r69-{p['sector']}-{p['a']}-{p['b']}-{j}",[tuple(x) for x in t['atoms']]) for p in pair['pairs'] for j,t in enumerate(p['deletion_minimal_terms'])];assert len(general)==4740
 return px,pz,lx,lz,records,r62,general

def verify_outer_fresh(i):
 px,pz,lx,lz,records,r62,general=load_outer_context();d=ROOT/'cegar'/f'iter{i}';cand=load(d/'candidate.json.gz');ores=load(d/'outer_result.json.gz');before=load(d/'dynamic_before.json.gz')
 assert len(before)==2*i
 outer=OuterScheduler(True)
 for j,r in enumerate(records):outer.add_block([tuple(x) for x in r['atoms']],f'r63-{j}')
 for b in r62['outer_blocks']:outer.add_block([tuple(x) for x in b['atoms']],'r62-'+b['tag'],b['trace_sha256'])
 for tag,atoms in general:outer.add_block(atoms,tag)
 for j,b in enumerate(before):outer.add_block([tuple(x) for x in b['atoms']],f"dynamic-{j}-{b['sector']}",b.get('mechanism_sha256'))
 smt=outer.s.to_smt2().encode();stored=data(d/'outer.smt2.gz');assert smt==stored,(i,len(smt),len(stored),sha_bytes(smt),sha_bytes(stored))
 times={k:int(v) for k,v in cand['schedule_times'].items()};assert cand['iteration']==i and ores['status']=='SAT' and ores['compressed_schedule']==times
 audit=M.audit_schedule(times,True);assert audit==cand['audit'] and audit['ok'] and audit['global_interleaved'] and audit['conflicts']==[] and audit['mc_violations']==[] and audit['edge_count']==864 and audit['overlaps']==648 and audit['min_time']==0 and audit['max_time']==audit['used_layers']-1
 fixed=z3.Solver();fixed.add(z3.parse_smt2_string(stored.decode()))
 for e in M.ALL_EDGES:fixed.add(z3.Int('t_'+e.replace(':','_'))==times[e])
 assert fixed.check()==z3.sat and len(outer.blocks)==6200+2*i
 assert all(not M.block_holds(times,atoms) for _,atoms in general)
 assert all(not M.block_holds(times,[tuple(x) for x in b['atoms']]) for b in before)
 assert all(not M.block_holds(times,[tuple(x) for x in r['atoms']]) for r in records)
 assert all(not M.block_holds(times,[tuple(x) for x in b['atoms']]) for b in r62['outer_blocks'])
 assert sha_obj(times)==cand['schedule_sha256'] and sha_bytes(stored)==cand['outer_smt2_sha256']==ores['smt2_sha256']
 assert cand['asserted_blocks']=={'round63_single':1440,'round62':20,'round69_generalized':4740,'round69_dynamic':2*i,'total':6200+2*i,'exploratory_round63_pair':0}
 return {'status':'PASS','iteration':i,'blocks':len(outer.blocks),'smt2_sha256':sha_bytes(smt),'schedule_sha256':cand['schedule_sha256'],'fixed_model_status':'SAT','named_edges':864,'mc_constraints':648}

def verify_cegar():
 px,pz,lx,lz,records,r62,general=load_outer_context();final_dyn=load(ROOT/'cegar/dynamic_blocks.json');initial=load(ROOT/'cegar/inherited_dynamic_blocks_round69.json');assert len(initial)==12 and len(final_dyn)==60 and final_dyn[:12]==initial
 summary=load(ROOT/'cegar/summary.json');result=load(ROOT/'RESULT.json');assert summary['iteration_range']==[6,29] and summary['completed_dual_sector_candidates']==24;assert result['verdict']=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED'
 verified=[]
 with tempfile.TemporaryDirectory(prefix='circdist_r71_full_replay_') as td:
  tmp=Path(td)
  for i in range(6,30):
   d=ROOT/'cegar'/f'iter{i}';cand=load(d/'candidate.json.gz');ores=load(d/'outer_result.json.gz');before=load(d/'dynamic_before.json.gz');saved=load(d/'direct_verification.json.gz');outcome=load(d/'iteration_outcome.json');oreplay=load(d/'outer_independent_replay.json')
   assert before==final_dyn[:2*i] and len(before)==2*i
   child=subprocess.run([sys.executable,str(ROOT/'verify.py'),'--outer-only',str(i)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=180)
   assert child.returncode==0 and '"status": "PASS"' in child.stdout,(i,child.returncode,child.stdout[-2000:])
   stored=data(d/'outer.smt2.gz')
   times={k:int(v) for k,v in cand['schedule_times'].items()};assert cand['iteration']==i and ores['status']=='SAT' and ores['compressed_schedule']==times
   assert set(times)==set(M.ALL_EDGES) and len(times)==864 and len(M.OVERLAPS)==648
   audit=M.audit_schedule(times,True);assert audit==cand['audit'] and audit['ok'] and audit['global_interleaved'] and audit['conflicts']==[] and audit['mc_violations']==[] and audit['edge_count']==864 and audit['overlaps']==648 and audit['min_time']==0 and audit['max_time']==audit['used_layers']-1
   assert cand['asserted_blocks']=={'round63_single':1440,'round62':20,'round69_generalized':4740,'round69_dynamic':2*i,'total':6200+2*i,'exploratory_round63_pair':0}
   assert all(not M.block_holds(times,atoms) for _,atoms in general)
   assert all(not M.block_holds(times,[tuple(x) for x in b['atoms']]) for b in before)
   assert all(not M.block_holds(times,[tuple(x) for x in r['atoms']]) for r in records)
   assert all(not M.block_holds(times,[tuple(x) for x in b['atoms']]) for b in r62['outer_blocks'])
   assert sha_obj(times)==cand['schedule_sha256'] and sha_bytes(stored)==cand['outer_smt2_sha256']==ores['smt2_sha256']
   assert cand['schedule_times_sorted']==[{'edge':e,'time':times[e]} for e in sorted(times)]
   assert cand['order_bindings']=={'X':B.order_bindings(times,'X',M.Xchecks),'Z':B.order_bindings(times,'Z',M.Zchecks)}
   assert cand['model_metadata']==jround(M.model_metadata(px,pz,lx,lz));assert cand['pool_bindings']['Xerr_pool_count']==cand['pool_bindings']['Zerr_pool_count']==1884
   ss=B.sectors(times,lx,lz);cols={lab:[B.column_public(sec,col) for col in sec.columns] for lab,sec in ss.items()};assert cand['columns']==cols and all(len(v)==360 for v in cols.values())
   assert oreplay['status']=='PASS' and oreplay['iteration']==i and oreplay['outer_smt2_sha256']==cand['outer_smt2_sha256'] and oreplay['named_edge_count']==864 and oreplay['mc_constraint_count']==648 and oreplay['serialized_formula_fixed_model_status']=='SAT'
   vr={'schema':'round69-complete-direct360-replay-v1','candidate_sha256':cand['schedule_sha256'],'schedule_audit':audit,'sectors':{}}
   vrroot=tmp/f'iter{i}';(vrroot/'direct360').mkdir(parents=True);(vrroot/'solver').mkdir()
   for lab in ('Xerr','Zerr'):
    gen=tmp/f'generated-{i}'/lab;B.build_direct_cnf(ss[lab],gen,cand['schedule_sha256'],10)
    for suffix in ('clauses.jsonl','cnf','columns.json','summary.json','variables.json'):
     got=data(d/'direct360'/f'{lab}.{suffix}.gz');want=gen.with_suffix('.'+suffix).read_bytes();assert got==want,(i,lab,suffix)
     (vrroot/'direct360'/f'{lab}.{suffix}').write_bytes(got)
    (vrroot/'solver'/f'{lab}.solver.log').write_bytes(data(d/'solver'/f'{lab}.solver.log.gz'))
    run=load(d/f'{lab}_solver.run.json');assert run['exit_code']==10 and not run['timed_out'] and not run['sigterm_sent'] and not run['sigkill_sent']
    vr['sectors'][lab]=jround(V.verify_one(vrroot,lab,ss[lab]));assert vr['sectors'][lab]==saved['sectors'][lab]
    summ=vr['sectors'][lab]['formula_summary'];assert summ['complete_query'] and summ['primary_selection_variables']==360 and summ['W']==10 and summ['excluded_restrictions']==['no pool restriction','no residual-pattern restriction','no check-count restriction','no within-check order family restriction']
    idx=12+2*(i-6)+(0 if lab=='Xerr' else 1);entry=final_dyn[idx];mech=vr['sectors'][lab]['mechanism'];block=mech['sound_outer_block']
    assert entry['source_iteration']==i and entry['sector']==lab and entry['candidate_sha256']==cand['schedule_sha256'] and entry['mechanism_sha256']==sha_obj(mech) and entry['atoms']==block['atoms'] and entry['atom_count']==block['atom_count']
   assert saved['repair_gate']['entered'] is False and outcome['repair_entered'] is False and outcome['branch_closed'] is False
   assert outcome['candidate_sha256']==cand['schedule_sha256'] and outcome['dynamic_blocks_after']==2*(i+1) and outcome['installed_blocks_before']==6200+2*i
   for name,want in [('outer_build',0),('outer_independent_replay',0),('direct_replay',0),('append_dynamic',0)]:
    r=load(d/f'{name}.run.json');assert r['exit_code']==want and not r['timed_out'] and not r['sigterm_sent'] and not r['sigkill_sent']
   assert not list(d.rglob('*.drat')) and not list(d.rglob('*.lrat'))
   verified.append({'iteration':i,'schedule_sha256':cand['schedule_sha256'],'outer_blocks':6200+2*i,'Xerr_weight':vr['sectors']['Xerr']['mechanism']['fault_count'],'Zerr_weight':vr['sectors']['Zerr']['mechanism']['fault_count']})
 assert summary['restart']=={'next_iteration':30,'round63_unary_blocks':1440,'round62_blocks':20,'round69_generalized_blocks':4740,'dynamic_blocks_total':60,'dynamic_blocks_inherited_round69':12,'dynamic_blocks_new_round71':48,'exploratory_round63_pair_clauses_installed':0,'next_outer_total_blocks':6260,'state':'cegar/dynamic_blocks.json'}
 return {'iterations':verified,'completed_dual_sector_candidates':24,'outer_sat':24,'Xerr_sat_raw_replayed':24,'Zerr_sat_raw_replayed':24,'new_exact_blocks':48,'dynamic_blocks':60,'next_iteration':30,'next_total_blocks':6260,'absence_proofs':0,'repair_entered':False,'root_closed':False}

def verify_negative_controls():
 n=load(ROOT/'controls/negative_controls.json');assert n['status']=='PASS' and n['counts']=={'assignment_flip_rejected':48,'fault_removal_rejected':48,'schedule_collision_rejected':24,'truncated_assignment_rejected':1}
 assert len(n['direct_controls'])==48 and len(n['schedule_mutation_controls'])==24
 for r in n['direct_controls']:
  assert r['flip_assignment_control']['failed_clause_count']>0 and not r['remove_fault_control']['ok']
 for r in n['schedule_mutation_controls']:
  cand=load(ROOT/'cegar'/f"iter{r['iteration']}"/'candidate.json.gz');times={k:int(v) for k,v in cand['schedule_times'].items()};m=r['mutation'];bad=dict(times);bad[m['edge']]=m['corrupted_time'];audit=jround(M.audit_schedule(bad,True));assert not audit['ok'] and audit==r['audit'] and not r['accepted']
 raw=data(ROOT/n['truncated_assignment']['path']);lits=[]
 for line in raw.decode(errors='replace').splitlines():
  if line.startswith('v '):lits.extend(int(x) for x in line[2:].split() if int(x))
 assert len({abs(x) for x in lits})==5995<n['truncated_assignment']['expected_variables'] and not n['truncated_assignment']['accepted']
 return n['counts']

def verify_process_ledger():
 p=load(ROOT/'PROCESS_LEDGER.json');rows=p['candidate_process_records'];assert len(rows)==144 and p['strict_foreground_serial'] and p['detached_processes']==0
 assert sum(bool(r['timed_out']) for r in rows)==0 and sum(bool(r['sigterm_sent']) for r in rows)==0 and sum(bool(r['sigkill_sent']) for r in rows)==0
 assert sum(r['exit_code']==10 for r in rows)==48 and sum(r['exit_code']==0 for r in rows)==96
 assert sorted(set(r['iteration'] for r in rows))==list(range(6,30))
 return {'records':144,'exit_0':96,'exit_10_sat':48,'timeouts':0,'signals':0,'interruptions':0,'detached':0}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo-root',type=Path);ap.add_argument('--quick',action='store_true');ap.add_argument('--allow-unsealed',action='store_true');ap.add_argument('--outer-only',type=int);a=ap.parse_args();t=time.monotonic()
 if a.outer_only is not None:
  print(json.dumps(verify_outer_fresh(a.outer_only),indent=2,sort_keys=True));return
 result={'schema':'round71-full-independent-verification-v1','manifest':verify_manifest(a.allow_unsealed),'compression':verify_compression(),'bindings':verify_bindings(a.repo_root.resolve() if a.repo_root else None),'processes':verify_process_ledger(),'negative_controls':verify_negative_controls(),'proof_checker_controls':verify_proof_controls()}
 if not a.quick:result['cegar']=verify_cegar()
 assert (ROOT/'VERDICT.txt').read_text().strip()=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED';result['verdict']='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED';result['status']='PASS';result['wall_seconds']=time.monotonic()-t
 print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
