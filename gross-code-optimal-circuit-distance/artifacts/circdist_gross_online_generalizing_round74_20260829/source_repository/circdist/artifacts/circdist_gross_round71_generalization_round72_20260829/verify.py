#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse,gzip,hashlib,json,os,subprocess,sys,tempfile,time
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
def path_for(p):
 p=Path(p)
 if p.exists():return p
 q=Path(str(p)+'.gz')
 if q.exists():return q
 raise FileNotFoundError(p)
def data(p):
 q=path_for(p);return gzip.decompress(q.read_bytes()) if q.suffix=='.gz' else q.read_bytes()
def load(p):return json.loads(data(p))
def jround(o):return json.loads(json.dumps(o))
def count_files(p):return sum(1 for q in Path(p).rglob('*') if q.is_file())

def verify_manifest(allow_unsealed=False):
 p=ROOT/'SHA256SUMS.txt'
 if not p.exists():
  assert allow_unsealed,'missing SHA256SUMS.txt';return {'present':False,'entries':0}
 rows=[]
 for line in p.read_text().splitlines():
  if not line.strip():continue
  h,rel=line.split('  ',1);q=ROOT/rel;assert q.is_file(),('missing',rel);assert sha_bytes(q.read_bytes())==h,('hash mismatch',rel);rows.append(rel)
 expected=sorted(q.relative_to(ROOT).as_posix() for q in ROOT.rglob('*') if q.is_file() and q.relative_to(ROOT).as_posix()!='SHA256SUMS.txt')
 assert sorted(rows)==expected,(len(rows),len(expected),'manifest coverage')
 pay=ROOT/'PAYLOAD_SHA256SUMS.txt'
 if pay.exists():
  for line in pay.read_text().splitlines():
   if not line.strip():continue
   h,rel=line.split('  ',1);q=ROOT/rel;assert q.is_file() and sha_bytes(q.read_bytes())==h,('payload',rel)
 return {'present':True,'entries':len(rows),'external_root_seal_sha256':sha_bytes(p.read_bytes()),'payload_manifest_present':pay.exists()}

def verify_compression():
 inv=load(ROOT/'COMPRESSED_INVENTORY.json');assert inv['file_count']==len(inv['files']);tot=comp=0
 actual=sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.gz'))
 assert actual==sorted(r['path'] for r in inv['files']),(len(actual),len(inv['files']))
 for r in inv['files']:
  p=ROOT/r['path'];raw=p.read_bytes();assert not (ROOT/r['original_path']).exists();assert len(raw)==r['compressed_bytes'] and sha_bytes(raw)==r['compressed_sha256'] and r['gzip_mtime']==0
  z=gzip.decompress(raw);assert len(z)==r['uncompressed_bytes'] and sha_bytes(z)==r['uncompressed_sha256'];tot+=len(z);comp+=len(raw)
 assert (tot,comp)==(inv['uncompressed_bytes'],inv['compressed_bytes'])
 return {'files':len(actual),'uncompressed_bytes':tot,'compressed_bytes':comp}

def verify_nested_manifest(pkg,seal):
 p=pkg/'SHA256SUMS.txt';assert sha_bytes(p.read_bytes())==seal;rows=[]
 for line in p.read_text().splitlines():
  if not line.strip():continue
  h,rel=line.split('  ',1);q=pkg/rel;assert q.is_file() and sha_bytes(q.read_bytes())==h,(pkg.name,rel);rows.append(rel)
 expected=sorted(q.relative_to(pkg).as_posix() for q in pkg.rglob('*') if q.is_file() and q.relative_to(pkg).as_posix()!='SHA256SUMS.txt')
 assert sorted(rows)==expected,(pkg,len(rows),len(expected));return len(rows)

def verify_bindings(repo_root=None):
 s=load(ROOT/'SOURCE_BINDINGS.json');seals={'round69':'aad4434050b1b64d3907b990e8279a2b25b2b4e29abcebf585fb885f3dbab647','round71':'4b8e33dac3ab823f7efc8ebde9a8271b81314e2b9e0a8e5b27ba828c2068df3a'}
 assert s['round69_root_seal_sha256']==seals['round69'] and s['round70_review_sha256']=='b2fe38fd6adb1ef974624a49b84b7a61620a5c97a531155aac01fc39dbfbaabe' and s['round71_root_seal_sha256']==seals['round71']
 snap={'round69_SHA256SUMS.txt':seals['round69'],'round70_review.md':s['round70_review_sha256'],'round71_SHA256SUMS.txt':seals['round71']}
 for name,h in snap.items():assert sha_bytes((ROOT/'bindings/snapshots'/name).read_bytes())==h
 live=0
 for r in s['frozen_inputs']:
  b=(ROOT/r['snapshot']).read_bytes();assert len(b)==r['bytes'] and sha_bytes(b)==r['sha256']
  if repo_root is not None:assert (repo_root/r['path']).read_bytes()==b,r['path'];live+=1
 mini=ROOT/'source_repository/circdist/artifacts';counts={}
 for r in s['self_contained_source_packages']:
  counts[r['name']]=verify_nested_manifest(ROOT/r['path'],r['seal_sha256'])
 pre=(ROOT/'preflight/round71_clean_full_verifier.log').read_text();assert '"status": "PASS"' in pre and '"completed_dual_sector_candidates": 24' in pre
 reader=load(ROOT/'preflight/all_required_inputs_read.json');rs=reader['summary'];assert rs['files']==1050 and rs['gzip_members']==522 and rs['tar_members']==970 and rs['errors']==0
 return {'nested_manifest_entries':counts,'frozen_bindings':len(s['frozen_inputs']),'live_files_checked':live,'round69_seal':'PASS','round70_review_bound':True,'round71_seal':'PASS','round71_clean_full_replay':'PASS'}

def run_control(cmd,want,marker,timeout=90):
 p=subprocess.run([str(x) for x in cmd],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=timeout);assert p.returncode==want and marker in p.stdout,(cmd,p.returncode,p.stdout[-1000:]);return {'exit_code':p.returncode,'marker':marker}
def verify_proof_controls():
 c=ROOT/'controls/proof_checker';tool=ROOT/'tooling'
 with tempfile.TemporaryDirectory(prefix='circdist_r72_proof_') as td:
  lrat=Path(td)/'valid.lrat';return {
   'drat_valid':run_control([tool/'drat-trim-arm64-macos',c/'php6_5.cnf',c/'php6_5.drat','-t','60','-L',lrat],0,'VERIFIED'),
   'drat_corrupt':run_control([tool/'drat-trim-arm64-macos',c/'php6_5.cnf',c/'php6_5_corrupted_truncated_10_lines.drat','-t','60'],1,'NOT VERIFIED'),
   'lrat_valid':run_control([tool/'lrat-check-arm64-macos',c/'php6_5.cnf',lrat],0,'VERIFIED'),
   'lrat_corrupt':run_control([tool/'lrat-check-arm64-macos',c/'php6_5.cnf',c/'php6_5_corrupted_truncated_10_lines.lrat'],1,'NOT VERIFIED')}

def verify_classification_quick():
 s=load(ROOT/'classification/summary.json');want={'round71_mechanisms':48,'formula_assignment_raw_replays':48,'participating_catalogs':113,'local_orders_per_catalog':720,'local_order_records':81360,'structural_pair_projections':607,'factorized_pair_relations':607,'factorized_pair_order_cells':314668800,'positive_pair_relations':272,'unary_only_pair_relations':335,'positive_pair_configurations':300,'positive_pair_cells':93888,'multi_check_exact_relations':48,'multi_check_terms_generated':96,'pair_terms_generated':600,'mechanisms_with_positive_pair_generalization':45,'mechanisms_without_positive_pair_generalization':3,'mechanisms_with_retained_generalized_cover':48,'candidate_exact_blocks_preserved':48,'mechanisms_term_failure':0,'weight14_pair_configuration_count':1,'weight14_negative_results_used':0}
 for k,v in want.items():assert s[k]==v,(k,s[k],v)
 assert s['weight14_positive_pool_counts']=={'Xerr':9438,'Zerr':9435} and s['positive_pair_library_miss_ids']==['iter11-Xerr','iter17-Xerr','iter19-Xerr'] and s['claim_scope'].startswith('conservative positive')
 d=load(ROOT/'classification/dedup_ledger.json');dc={'old_reviewed_terms':4740,'new_raw_term_candidates':696,'new_pair_candidates':600,'new_multi_check_candidates':96,'duplicate_old':0,'duplicate_new':85,'dominated_old':0,'dominated_new':45,'retained_new_terms':566,'merged_installed_generalized_terms':5306}
 for k,v in dc.items():assert d[k]==v,(k,d[k],v)
 terms=load(ROOT/'classification/retained_terms.json')['terms'];assert len(terms)==566 and sha_bytes(data(ROOT/'classification/retained_terms.json'))=='d505dea682b1ad1d3bebac4f82c4a0c3c3f5ef634f12a0f71dcbd3e9055e8791'
 kinds={k:sum(t['relation_kind']==k for t in terms) for k in ('positive_pair_rectangle','multi_check_exact_selected_mechanism')};assert kinds=={'positive_pair_rectangle':563,'multi_check_exact_selected_mechanism':3}
 assert sum(len(t['deletion_controls']) for t in terms)==5705 and {t.get('mechanism_id') for t in terms if t['relation_kind'].startswith('multi')}=={'iter11-Xerr','iter17-Xerr','iter19-Xerr'}
 mechs=load(ROOT/'classification/mechanisms.json')['mechanisms'];assert len(mechs)==48 and all(m['fault_count']<=10 and m['covering_retained_term_ids'] for m in mechs)
 f=load(ROOT/'classification/formula_raw_replay_bindings.json')['records'];assert len(f)==48 and all(x['all_dimacs_clauses_satisfied_independently'] and x['solver_status']=='SATISFIABLE' and x['solver_assignment_variables']==x['cnf_variables'] for x in f)
 return {'status':'PASS',**want,'dedup':dc,'retained_kinds':kinds,'deletion_controls':5705,'retained_terms_sha256':'d505dea682b1ad1d3bebac4f82c4a0c3c3f5ef634f12a0f71dcbd3e9055e8791'}

def load_outer_context():
 px,pz,lx,lz=B.load_context();assert len(px)==len(pz)==1884
 rx,_=B.global_single_records('Xerr',M.Xchecks,px,'X');rz,_=B.global_single_records('Zerr',M.Zchecks,pz,'Z');records=rx+rz;assert len(records)==1440
 r62=load(ROOT/'src/round62_cegar20.json');B.replay_round62_blocks(r62,lx,lz);assert len(r62['outer_blocks'])==20
 old=load(ROOT/'classification/round69_pair_classification.json.gz');oldgen=[(f"r69-{p['sector']}-{p['a']}-{p['b']}-{j}",[tuple(x) for x in t['atoms']]) for p in old['pairs'] for j,t in enumerate(p['deletion_minimal_terms'])];assert len(oldgen)==4740
 new=load(ROOT/'classification/retained_terms.json')['terms'];newgen=[(t['term_id'],[tuple(x) for x in t['atoms']]) for t in new];assert len(newgen)==566
 return px,pz,lx,lz,records,r62,oldgen,newgen

def verify_outer_fresh(i):
 px,pz,lx,lz,records,r62,oldgen,newgen=load_outer_context();d=ROOT/'cegar'/f'iter{i}';cand=load(d/'candidate.json');ores=load(d/'outer_result.json');before=load(d/'dynamic_before.json');assert len(before)==60+2*(i-30)
 outer=OuterScheduler(True)
 for j,r in enumerate(records):outer.add_block([tuple(x) for x in r['atoms']],f'r63-{j}')
 for b in r62['outer_blocks']:outer.add_block([tuple(x) for x in b['atoms']],'r62-'+b['tag'],b['trace_sha256'])
 for tag,atoms in oldgen+newgen:outer.add_block(atoms,tag)
 for j,b in enumerate(before):outer.add_block([tuple(x) for x in b['atoms']],f"dynamic-{j}-{b['sector']}",b.get('mechanism_sha256'))
 smt=outer.s.to_smt2().encode();stored=data(d/'outer.smt2');assert smt==stored,(i,len(smt),len(stored),sha_bytes(smt),sha_bytes(stored))
 times={k:int(v) for k,v in cand['schedule_times'].items()};assert cand['iteration']==i and ores['status']=='SAT' and ores['compressed_schedule']==times
 audit=M.audit_schedule(times,True);assert audit==cand['audit'] and audit['ok'] and audit['global_interleaved'] and not audit['conflicts'] and not audit['mc_violations'] and audit['edge_count']==864 and audit['overlaps']==648
 fixed=z3.Solver();fixed.add(z3.parse_smt2_string(stored.decode()))
 for e in M.ALL_EDGES:fixed.add(z3.Int('t_'+e.replace(':','_'))==times[e])
 assert fixed.check()==z3.sat and len(outer.blocks)==6766+len(before)
 assert all(not M.block_holds(times,atoms) for _,atoms in oldgen+newgen) and all(not M.block_holds(times,[tuple(x) for x in b['atoms']]) for b in before)
 assert all(not M.block_holds(times,[tuple(x) for x in r['atoms']]) for r in records) and all(not M.block_holds(times,[tuple(x) for x in b['atoms']]) for b in r62['outer_blocks'])
 assert sha_obj(times)==cand['schedule_sha256'] and sha_bytes(stored)==cand['outer_smt2_sha256']==ores['smt2_sha256']
 want={'round63_single':1440,'round62':20,'round69_generalized':4740,'round72_generalized':566,'dynamic_exact':len(before),'total':6766+len(before),'exploratory_round63_pair':0};assert cand['asserted_blocks']==want
 return {'schema':'round72-fresh-outer-replay-v1','status':'PASS','iteration':i,'blocks':len(outer.blocks),'smt2_sha256':sha_bytes(smt),'schedule_sha256':cand['schedule_sha256'],'fixed_model_status':'SAT','named_edges':864,'mc_constraints':648}

def verify_process_ledger():
 p=load(ROOT/'PROCESS_LEDGER.json');rows=p['candidate_process_records'];assert len(rows)==72 and p['strict_foreground_serial'] and p['detached_processes']==0
 assert sum(r['exit_code']==10 for r in rows)==24 and sum(r['exit_code']==0 for r in rows)==48 and not any(r['timed_out'] or r['sigterm_sent'] or r['sigkill_sent'] for r in rows)
 assert sorted(set(r['iteration'] for r in rows))==list(range(30,42))
 for a,b in zip(rows,rows[1:]):assert a['ended_utc']<=b['started_utc']
 return {'records':72,'exit_0':48,'exit_10_sat':24,'timeouts':0,'signals':0,'interruptions':0,'detached':0}

def verify_negative_controls():
 n=load(ROOT/'controls/negative_controls.json');assert n['status']=='PASS' and n['counts']=={'assignment_flip_rejected':24,'fault_removal_rejected':24,'schedule_collision_rejected':12,'truncated_assignment_rejected':1};assert len(n['direct_controls'])==24 and len(n['schedule_mutation_controls'])==12
 for r in n['direct_controls']:assert r['flip_assignment_control']['failed_clause_count']>0 and not r['remove_fault_control']['ok']
 for r in n['schedule_mutation_controls']:
  cand=load(ROOT/'cegar'/f"iter{r['iteration']}"/'candidate.json');times={k:int(v) for k,v in cand['schedule_times'].items()};m=r['mutation'];bad=dict(times);bad[m['edge']]=m['corrupted_time'];assert jround(M.audit_schedule(bad,True))==r['audit'] and not r['accepted']
 raw=data(ROOT/n['truncated_assignment']['path']);lits=[]
 for line in raw.decode(errors='replace').splitlines():
  if line.startswith('v '):lits.extend(int(x) for x in line[2:].split() if int(x))
 assert len({abs(x) for x in lits})==n['truncated_assignment']['expected_variables']-1 and not n['truncated_assignment']['accepted']
 return n['counts']

def verify_cegar_quick():
 summary=load(ROOT/'cegar/summary.json');final=load(ROOT/'cegar/dynamic_blocks.json');assert summary['iteration_range']==[30,41] and summary['completed_dual_sector_candidates']==12 and len(final)==84
 assert summary['restart']=={'next_iteration':42,'round63_unary_blocks':1440,'round62_blocks':20,'round69_generalized_blocks':4740,'round72_generalized_blocks':566,'dynamic_blocks_total':84,'dynamic_blocks_inherited_round71':60,'dynamic_blocks_new_round72':24,'exploratory_round63_pair_clauses_installed':0,'next_outer_total_blocks':6850,'state':'cegar/dynamic_blocks.json'}
 for i in range(30,42):
  d=ROOT/'cegar'/f'iter{i}';before=load(d/'dynamic_before.json');o=load(d/'iteration_outcome.json');cand=load(d/'candidate.json');dv=load(d/'direct_verification.json');assert before==final[:60+2*(i-30)] and o['outer_status']=='SAT' and o['raw_replay_passed'] and not o['branch_closed'] and not o['repair_entered']
  assert cand['asserted_blocks']['total']==6766+len(before) and o['installed_blocks_before']==6766+len(before) and o['dynamic_blocks_after']==len(before)+2
  for off,s in enumerate(('Xerr','Zerr')):
   sec=dv['sectors'][s];summ=sec['formula_summary'];assert sec['status']=='SATISFIABLE' and sec['all_dimacs_clauses_satisfied'] and summ['complete_query'] and summ['primary_selection_variables']==360 and summ['W']==10 and summ['excluded_restrictions']==['no pool restriction','no residual-pattern restriction','no check-count restriction','no within-check order family restriction']
   entry=final[60+2*(i-30)+off];mech=sec['mechanism'];assert entry['source_iteration']==i and entry['sector']==s and entry['candidate_sha256']==cand['schedule_sha256'] and entry['mechanism_sha256']==sha_obj(mech) and entry['atoms']==mech['sound_outer_block']['atoms']
   run=load(d/f'{s}_solver.run.json');assert run['exit_code']==10 and not run['timed_out']
  assert not list(d.rglob('*.drat')) and not list(d.rglob('*.lrat'))
 return {'completed_candidates':12,'outer_sat':12,'direct_sat_raw_replayed':24,'dynamic_blocks':84,'next_iteration':42,'next_total_blocks':6850,'absence_proofs':0,'repair_entered':False,'root_closed':False}

def verify_cegar_full():
 px,pz,lx,lz,records,r62,oldgen,newgen=load_outer_context();final=load(ROOT/'cegar/dynamic_blocks.json');verified=[]
 with tempfile.TemporaryDirectory(prefix='circdist_r72_cegar_full_') as td:
  tmp=Path(td)
  for i in range(30,42):
   d=ROOT/'cegar'/f'iter{i}';cand=load(d/'candidate.json');ores=load(d/'outer_result.json');before=load(d/'dynamic_before.json');saved=load(d/'direct_verification.json');outcome=load(d/'iteration_outcome.json');oreplay=load(d/'outer_independent_replay.json')
   child=subprocess.run([sys.executable,str(ROOT/'verify.py'),'--outer-only',str(i)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=240);assert child.returncode==0 and '"status": "PASS"' in child.stdout,(i,child.returncode,child.stdout[-2000:])
   times={k:int(v) for k,v in cand['schedule_times'].items()};assert set(times)==set(M.ALL_EDGES) and len(times)==864 and ores['compressed_schedule']==times and sha_obj(times)==cand['schedule_sha256']
   audit=M.audit_schedule(times,True);assert audit==cand['audit'] and audit['ok'] and audit['global_interleaved'] and not audit['conflicts'] and not audit['mc_violations']
   assert cand['schedule_times_sorted']==[{'edge':e,'time':times[e]} for e in sorted(times)] and cand['order_bindings']=={'X':B.order_bindings(times,'X',M.Xchecks),'Z':B.order_bindings(times,'Z',M.Zchecks)}
   assert cand['model_metadata']==jround(M.model_metadata(px,pz,lx,lz)) and cand['pool_bindings']['Xerr_pool_count']==cand['pool_bindings']['Zerr_pool_count']==1884
   ss=B.sectors(times,lx,lz);cols={lab:[B.column_public(sec,col) for col in sec.columns] for lab,sec in ss.items()};assert cand['columns']==cols and all(len(v)==360 for v in cols.values())
   assert oreplay['status']=='PASS' and oreplay['iteration']==i and oreplay['outer_smt2_sha256']==cand['outer_smt2_sha256'] and oreplay['named_edge_count']==864 and oreplay['mc_constraint_count']==648 and oreplay['serialized_formula_fixed_model_status']=='SAT'
   vrroot=tmp/f'iter{i}';(vrroot/'direct360').mkdir(parents=True);(vrroot/'solver').mkdir();sector_results={}
   for off,lab in enumerate(('Xerr','Zerr')):
    gen=tmp/f'generated-{i}'/lab;B.build_direct_cnf(ss[lab],gen,cand['schedule_sha256'],10)
    for suffix in ('clauses.jsonl','cnf','columns.json','summary.json','variables.json'):
     got=data(d/'direct360'/f'{lab}.{suffix}');want=gen.with_suffix('.'+suffix).read_bytes();assert got==want,(i,lab,suffix,sha_bytes(got),sha_bytes(want));(vrroot/'direct360'/f'{lab}.{suffix}').write_bytes(got)
    (vrroot/'solver'/f'{lab}.solver.log').write_bytes(data(d/'solver'/f'{lab}.solver.log'))
    got=jround(V.verify_one(vrroot,lab,ss[lab]));assert got==saved['sectors'][lab];sector_results[lab]=got
    entry=final[60+2*(i-30)+off];mech=got['mechanism'];assert entry['source_iteration']==i and entry['sector']==lab and entry['candidate_sha256']==cand['schedule_sha256'] and entry['mechanism_sha256']==sha_obj(mech) and entry['atoms']==mech['sound_outer_block']['atoms']
   assert saved['repair_gate']['entered'] is False and outcome['repair_entered'] is False and outcome['branch_closed'] is False and outcome['dynamic_blocks_after']==60+2*(i-29)
   verified.append({'iteration':i,'schedule_sha256':cand['schedule_sha256'],'outer_blocks':6766+len(before),'Xerr_weight':sector_results['Xerr']['mechanism']['fault_count'],'Zerr_weight':sector_results['Zerr']['mechanism']['fault_count']})
 return {'iterations':verified,'completed_dual_sector_candidates':12,'outer_sat':12,'Xerr_sat_raw_replayed':12,'Zerr_sat_raw_replayed':12,'new_exact_blocks':24,'dynamic_blocks':84,'next_iteration':42,'next_total_blocks':6850,'absence_proofs':0,'repair_entered':False,'root_closed':False}

def verify_classification_full():
 names=['formula_raw_replay_bindings.json','mechanisms.json','local_order_catalog.json','multi_check_relations.json','pair_relations.json','retained_terms.json','dedup_ledger.json','summary.json']
 with tempfile.TemporaryDirectory(prefix='circdist_r72_classification_full_') as td:
  out=Path(td)/'out';cmd=[sys.executable,str(ROOT/'src/generalize_round71.py'),'--repo-root',str(ROOT/'source_repository'),'--output-root',str(out)];p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=1800);assert p.returncode==0,(p.returncode,p.stdout[-4000:])
  rows=[]
  for n in names:
   got=(out/n).read_bytes();want=data(ROOT/'classification'/n);assert got==want,(n,len(got),len(want),sha_bytes(got),sha_bytes(want));rows.append({'path':n,'bytes':len(got),'sha256':sha_bytes(got)})
 return {'status':'PASS','recomputed_outputs':rows,'round71_assignments_replayed':48,'catalogs':113,'orders':81360,'pair_relations':607,'represented_pair_cells':314668800,'multi_check_relations':48,'retained_terms':566}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo-root',type=Path);ap.add_argument('--quick',action='store_true');ap.add_argument('--full',action='store_true');ap.add_argument('--allow-unsealed',action='store_true');ap.add_argument('--outer-only',type=int);a=ap.parse_args();t=time.monotonic()
 if a.outer_only is not None:print(json.dumps(verify_outer_fresh(a.outer_only),indent=2,sort_keys=True));return
 result={'schema':'round72-independent-verification-v1','manifest':verify_manifest(a.allow_unsealed),'compression':verify_compression(),'bindings':verify_bindings(a.repo_root.resolve() if a.repo_root else None),'classification_quick':verify_classification_quick(),'cegar_quick':verify_cegar_quick(),'processes':verify_process_ledger(),'negative_controls':verify_negative_controls(),'proof_checker_controls':verify_proof_controls()}
 do_full=a.full or not a.quick
 if do_full:
  result['classification_full']=verify_classification_full();result['cegar_full']=verify_cegar_full()
 assert (ROOT/'VERDICT.txt').read_text().strip()=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED' and load(ROOT/'RESULT.json')['verdict']=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED';result['verdict']='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED';result['status']='PASS';result['wall_seconds']=time.monotonic()-t
 print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
