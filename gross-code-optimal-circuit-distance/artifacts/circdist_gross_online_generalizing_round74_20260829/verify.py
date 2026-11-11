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
def jround(o):return json.loads(json.dumps(o))
def path_for(p):
 p=Path(p)
 if p.exists():return p
 q=Path(str(p)+'.gz')
 if q.exists():return q
 raise FileNotFoundError(p)
def data(p):
 q=path_for(p);b=q.read_bytes();return gzip.decompress(b) if q.suffix=='.gz' else b
def load(p):return json.loads(data(p))
def materialize(src,dst):dst=Path(dst);dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(data(src));return dst

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
 actual=sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.gz'));assert actual==sorted(r['path'] for r in inv['files']),(len(actual),len(inv['files']))
 for r in inv['files']:
  p=ROOT/r['path'];raw=p.read_bytes();assert not (ROOT/r['original_path']).exists(),r['original_path'];assert len(raw)==r['compressed_bytes'] and sha_bytes(raw)==r['compressed_sha256'] and int.from_bytes(raw[4:8],'little')==0
  z=gzip.decompress(raw);assert len(z)==r['uncompressed_bytes'] and sha_bytes(z)==r['uncompressed_sha256'];tot+=len(z);comp+=len(raw)
 assert (tot,comp)==(inv['uncompressed_bytes'],inv['compressed_bytes']);return {'files':len(actual),'uncompressed_bytes':tot,'compressed_bytes':comp}

def verify_nested_manifest(pkg,seal):
 p=pkg/'SHA256SUMS.txt';assert sha_bytes(p.read_bytes())==seal;rows=[]
 for line in p.read_text().splitlines():
  if not line.strip():continue
  h,rel=line.split('  ',1);q=pkg/rel;assert q.is_file() and sha_bytes(q.read_bytes())==h,(pkg.name,rel);rows.append(rel)
 expected=sorted(q.relative_to(pkg).as_posix() for q in pkg.rglob('*') if q.is_file() and q.relative_to(pkg).as_posix()!='SHA256SUMS.txt');assert sorted(rows)==expected,(len(rows),len(expected));return len(rows)

def verify_bindings(repo_root=None):
 s=load(ROOT/'SOURCE_BINDINGS.json');assert s['round72_root_seal_sha256']=='bc2bf8bdc2da199e348b0471ef4f0367e52e1a7e5eefe1294adb51ab25a4f7f6' and s['round73_review_sha256']=='92e2b6306f7181b2c61fa02b3eba0624a74864f19045e6e72b208754115224d3'
 live=0
 for r in s['frozen_inputs']:
  b=(ROOT/r['snapshot']).read_bytes();assert len(b)==r['bytes'] and sha_bytes(b)==r['sha256'],r['snapshot']
  if repo_root is not None:assert (repo_root/r['path']).read_bytes()==b,r['path'];live+=1
 p=ROOT/s['self_contained_source_packages'][0]['path'];n=verify_nested_manifest(p,s['self_contained_source_packages'][0]['seal_sha256'])
 pre=load(ROOT/'preflight/round72_clean_full_verifier.run.json');assert pre['exit_code']==0 and not pre['timed_out'] and abs(pre['wall_seconds']-1326.432404875)<1e-6
 assert '"status": "PASS"' in (ROOT/'preflight/round72_clean_full_verifier.log').read_text()
 read=load(ROOT/'preflight/all_required_inputs_read.json');assert read['status']=='PASS' and not read['errors'] and read['round72_seal_sha256']==s['round72_root_seal_sha256'] and read['round73_review_sha256']==s['round73_review_sha256']
 assert [(x['physical_files'],x['gzip_files'],x['tar_regular_members']) for x in read['packages']]==[(250,112,472),(794,414,472),(1492,742,944)]
 return {'frozen_bindings':len(s['frozen_inputs']),'live_files_checked':live,'nested_round72_manifest_entries':n,'round72_clean_full_replay_seconds':pre['wall_seconds']}

def run_control(cmd,want,marker,timeout=180):
 p=subprocess.run([str(x) for x in cmd],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=timeout);assert p.returncode==want and marker in p.stdout,(p.returncode,p.stdout[-1000:]);return {'exit_code':p.returncode,'marker':marker}
def verify_proof_controls():
 c=ROOT/'controls/round74_proof_checker';t=ROOT/'tooling'
 with tempfile.TemporaryDirectory(prefix='circdist_r74_proof_') as td:
  lrat=Path(td)/'valid.lrat'
  return {'drat_valid':run_control([t/'drat-trim-arm64-macos',c/'php6_5.cnf',c/'php6_5.drat','-t','170','-L',lrat],0,'VERIFIED'),'lrat_valid':run_control([t/'lrat-check-arm64-macos',c/'php6_5.cnf',lrat],0,'VERIFIED'),'drat_corrupt':run_control([t/'drat-trim-arm64-macos',c/'php6_5.cnf',c/'php6_5_corrupted_truncated_10_lines.drat','-t','170'],1,'NOT VERIFIED'),'lrat_corrupt':run_control([t/'lrat-check-arm64-macos',c/'php6_5.cnf',c/'php6_5_corrupted_truncated_10_lines.lrat'],1,'NOT VERIFIED')}

def pc(z):return bin(z).count('1')
def mask(xs):return sum(1<<int(x) for x in xs)
def signature(lab,x,lx,lz):
 det=M.HZ if lab=='Xerr' else M.HX;duals=lz if lab=='Xerr' else lx;syn=sum(((pc(x&r)&1)<<j) for j,r in enumerate(det));logical=sum(((pc(x&r)&1)<<j) for j,r in enumerate(duals));return syn|(logical<<72)
def verify_generalization_quick():
 want={'source_mechanisms':24,'formula_assignment_raw_replays':24,'participating_catalogs':111,'local_order_records':79920,'structural_pair_relations':249,'structural_pair_cells_represented':129081600,'positive_pair_relations':65,'unary_only_pair_relations':184,'positive_pair_configurations':70,'positive_pair_cells':30576,'multi_check_exact_relations':24,'multi_check_terms_generated':48,'pair_terms_generated':140,'raw_term_candidates':188,'retained_increment':134,'merged_installed_generalized_terms':5440,'literal_retained_tuple_replays':1137096,'factorized_symbolically_proved_tuples':2985984,'pair_domain_library_relative_new_tuples':1098444,'retained_deletion_controls':1372}
 s=load(ROOT/'classification/summary.json');assert s['status']=='PASS' and s['factorized_multi_validation_is_symbolic_universal_not_sampling'] and s['retained_relation_kinds']=={'multi_check_exact_selected_mechanism':1,'positive_pair_rectangle':133}
 for k,v in want.items():assert s[k]==v,(k,s[k],v)
 d=load(ROOT/'classification/dedup_ledger.json');assert {k:d[k] for k in ['raw_term_candidates','multi_check_candidates','pair_candidates','duplicate_old','duplicate_new','dominated_old','dominated_new','retained_increment']}=={'raw_term_candidates':188,'multi_check_candidates':48,'pair_candidates':140,'duplicate_old':0,'duplicate_new':31,'dominated_old':0,'dominated_new':23,'retained_increment':134}
 terms=load(ROOT/'classification/round74_retained_terms.json')['terms'];assert len(terms)==134 and len({t['term_id'] for t in terms})==134 and sum(len(t['deletion_controls']) for t in terms)==1372
 for t in terms:
  atoms=[tuple(x) for x in t['atoms']];assert len(atoms)==t['atom_count'] and all(tuple(c['removed_atom']) in atoms for c in t['deletion_controls']) and t['covered_tuple_count']>0
 state=load(ROOT/'classification/installed_generalized_terms.json');reg=load(ROOT/'classification/online_mechanism_registry.json');assert state['term_count']==5440 and state['round74_retained_terms']==134 and reg['mechanism_count']==24
 byid={t['term_id']:t for t in terms};assert set(byid)=={t['term_id'] for t in state['terms'] if t.get('source_round')==74}
 px,pz,lx,lz=B.load_context();assert len(px)==len(pz)==1884
 totals={'catalogs':0,'relations':0,'literal':0,'factorized':0,'raw':0,'retained':0};prev_dyn=84;prev_gen=5306;prev_reg=0
 for i in range(42,54):
  q=ROOT/'cegar'/f'iter{i}';o=load(q/'iteration_outcome.json');cand=load(q/'candidate.json');orep=load(q/'outer_independent_replay.json');dv=load(q/'direct_verification.json');gs=load(q/'generalization/summary.json');dl=load(q/'generalization/dedup_ledger.json');cat=load(q/'generalization/local_order_catalog.json');mr=load(q/'generalization/multi_check_relations.json');pr=load(q/'generalization/pair_relations.json');tr=load(q/'generalization/retained_terms.json')['terms'];tu=load(q/'generalization/tuple_raw_replay.json');fb=load(q/'generalization/formula_raw_replay_bindings.json')['records'];wb=load(q/'generalization/w14_positive_pool.json')
  before=load(q/'dynamic_before.json');after=load(q/'dynamic_after.json');gb=load(q/'generalized_before.json');ga=load(q/'generalized_after.json');rb=load(q/'mechanism_registry_before.json');ra=load(q/'mechanism_registry_after.json')
  assert len(before)==prev_dyn and len(after)==prev_dyn+2 and gb['term_count']==prev_gen and ga['term_count']==prev_gen+gs['retained_increment'] and rb['mechanism_count']==prev_reg and ra['mechanism_count']==prev_reg+2
  assert o['outer_status']=='SAT' and o['raw_replay_passed'] and not o['repair_entered'] and not o['branch_closed'] and o['installed_blocks_before']==1440+20+prev_gen+prev_dyn and o['installed_blocks_after']==1440+20+ga['term_count']+len(after)
  assert cand['asserted_blocks']['total']==o['installed_blocks_before'] and cand['audit']['ok'] and cand['audit']['global_interleaved'] and cand['audit']['edge_count']==864 and cand['audit']['overlaps']==648
  assert orep['status']=='PASS' and orep['parsed_ordered_assertions_equal'] and orep['serialized_formula_fixed_model_status']=='SAT' and orep['all_installed_antecedents_excluded']
  assert len(fb)==2 and all(x['complete_assignment'] and x['all_dimacs_clauses_satisfied_independently'] and x['raw_canonical_and_physical_replay_passed'] for x in fb)
  for off,lab in enumerate(('Xerr','Zerr')):
   sec=dv['sectors'][lab];fs=sec['formula_summary'];assert sec['status']=='SATISFIABLE' and sec['all_dimacs_clauses_satisfied'] and fs['complete_query'] and fs['primary_selection_variables']==360 and fs['W']==10 and fs['excluded_restrictions']==['no pool restriction','no residual-pattern restriction','no check-count restriction','no within-check order family restriction'] and sec['mechanism']['canonical_replay']['ok'] and sec['mechanism']['physical_syndrome']==[] and sec['mechanism']['physical_nontrivial'] and sec['mechanism']['fault_count']<=10
   assert after[-2+off]['source_iteration']==i and after[-2+off]['sector']==lab and after[-2+off]['atoms']==sec['mechanism']['sound_outer_block']['atoms']
  assert gs['status']=='PASS' and dl['installed_generalized_before']==prev_gen and dl['installed_generalized_after']==ga['term_count'] and len(tr)==gs['retained_increment'] and tu['all_passed'] and len(tu['terms'])==len(tr)
  wbc={x['sector']:x['count'] for x in wb['sectors']};assert wbc==gs['weight14_positive_pool_counts'] and wbc['Xerr']==9438 and wbc['Zerr'] in (9435,9436)
  assert len(cat['entries'])==gs['participating_catalogs'] and len(mr['relations'])==2 and len(pr['relations'])==gs['structural_pair_relations']
  for e in cat['entries']:
   assert len(e['orders'])==720 and [x['order_id'] for x in e['orders']]==list(range(720)) and all(sorted(x['qubits'])==sorted(e['row']) for x in e['orders'])
   for order in e['orders']:
    for op in order['options']:
     assert signature(e['sector'],mask(op['canonical_support']),lx,lz)==signature(e['sector'],mask(op['physical_support']),lx,lz)==int(op['signature_hex'],16)
  for rel in mr['relations']:
   assert rel['joint_not_pair_independent'] and len(rel['minimized_terms'])==2 and all(t['relation_kind']=='multi_check_exact_selected_mechanism' and t['reachable_signature_count']>0 for t in rel['minimized_terms'])
   for c,x in rel['local_order_contributions'].items():
    assert x['allowed_count']==pc(int(x['allowed_mask_hex'],16))
    for rec in x['per_order']:assert signature(rel['sector'],mask(rec['canonical_support']),lx,lz)==signature(rel['sector'],mask(rec['physical_support']),lx,lz)==int(rec['signature_hex'],16)
  truth_cells=explicit_cells=configurations=positive_relations=0
  for rel in pr['relations']:
   assert len(rel['truth_rows_hex'])==len(rel['explicit_good_good_rows_hex'])==720
   truth=[int(x,16) for x in rel['truth_rows_hex']];explicit=[int(x,16) for x in rel['explicit_good_good_rows_hex']]
   assert all(0<=x<(1<<720) for x in truth+explicit) and all((e&~t)==0 for t,e in zip(truth,explicit))
   assert sum(pc(x) for x in truth)==rel['truth_cell_count'] and sum(pc(x) for x in explicit)==rel['explicit_good_good_cell_count']
   assert len(rel['positive_configurations'])==rel['positive_configuration_count'] and len(rel['generated_terms'])==2*rel['positive_configuration_count']
   truth_cells+=rel['truth_cell_count'];explicit_cells+=rel['explicit_good_good_cell_count'];configurations+=rel['positive_configuration_count'];positive_relations+=bool(rel['positive_configuration_count'])
  assert len(pr['relations'])*720*720==gs['structural_pair_cells_represented'] and explicit_cells==gs['positive_pair_cells'] and configurations==gs['positive_pair_configurations'] and positive_relations==gs['positive_pair_relations']
  for x in tu['terms']:
   assert x['all_raw_replays_passed'] and x['tuples_instantiated']==x['expected_covered_tuples']
   if x['relation_kind']=='positive_pair_rectangle':assert x['validation_mode']=='literal_every_tuple' and x['selector_stream_scope']=='every covered tuple'
   else:assert x['validation_mode']=='factorized_symbolic_universal' and x['factorized_universal_basis'] and 'without sampling' in x['factorized_universal_basis']
  totals['catalogs']+=len(cat['entries']);totals['relations']+=len(pr['relations']);totals['literal']+=gs['literal_retained_tuple_replays'];totals['factorized']+=gs['factorized_symbolically_proved_tuples'];totals['raw']+=gs['raw_term_candidates'];totals['retained']+=gs['retained_increment'];prev_dyn=len(after);prev_gen=ga['term_count'];prev_reg=ra['mechanism_count']
 assert (prev_dyn,prev_gen,prev_reg)==(108,5440,24) and totals=={'catalogs':111,'relations':249,'literal':1137096,'factorized':2985984,'raw':188,'retained':134}
 return {'status':'PASS',**want,'retained_relation_kinds':s['retained_relation_kinds'],'totals':totals}

def verify_cegar_quick():
 s=load(ROOT/'cegar/summary.json');assert s['iteration_range']==[42,53] and s['completed_dual_sector_candidates']==12 and s['outer_verdicts']=={'SAT':12,'TIMEOUT':0,'UNKNOWN':0,'UNSAT':0} and s['direct_sector_verdicts']=={'SATISFIABLE':24,'UNKNOWN_OR_TIMEOUT':0,'UNSAT_PROOFS_ACCEPTED':0}
 assert s['restart']=={'next_iteration':54,'round63_unary_blocks':1440,'round62_blocks':20,'round69_generalized_blocks':4740,'round72_generalized_blocks':566,'round74_generalized_blocks':134,'merged_generalized_blocks':5440,'dynamic_blocks_total':108,'dynamic_blocks_inherited_round72':84,'dynamic_blocks_new_round74':24,'exploratory_round63_pair_clauses_installed':0,'next_outer_total_blocks':7008,'dynamic_state':'cegar/dynamic_blocks.json','generalized_state':'classification/installed_generalized_terms.json','registry_state':'classification/online_mechanism_registry.json'}
 rs=load(ROOT/'restart/restart_state.json');assert rs['next_iteration']==54 and rs['total_installed_blocks']==7008 and load(ROOT/rs['states']['dynamic'])==load(ROOT/'cegar/dynamic_blocks.json') and load(ROOT/rs['states']['generalized'])==load(ROOT/'classification/installed_generalized_terms.json') and load(ROOT/rs['states']['mechanism_registry'])==load(ROOT/'classification/online_mechanism_registry.json')
 return {'completed_candidates':12,'outer_sat':12,'direct_sat_raw_replayed':24,'new_exact_blocks':24,'new_generalized_terms':134,'dynamic_blocks':108,'generalized_terms':5440,'next_iteration':54,'next_total_blocks':7008,'absence_proofs':0,'repair_entered':False,'root_closed':False}

def verify_process_ledger():
 p=load(ROOT/'PROCESS_LEDGER.json');rows=p['candidate_process_records'];assert len(rows)==84 and p['strict_foreground_serial'] and p['detached_processes']==0 and p['candidate_exit_10_sat']==24 and p['candidate_exit_0']==60 and p['candidate_timeouts']==p['candidate_signals']==0 and len(p['correction_records'])==3
 assert sorted(set(r['iteration'] for r in rows))==list(range(42,54)) and all(not r['timed_out'] and not r['sigterm_sent'] and not r['sigkill_sent'] for r in rows)
 for a,b in zip(rows,rows[1:]):assert a['ended_utc']<=b['started_utc']
 assert [r['exit_code'] for r in p['correction_records']]==[1,-15,-15]
 return {'records':84,'exit_0':60,'exit_10_sat':24,'timeouts':0,'signals':0,'correction_records':3,'detached':0}

def verify_negative_controls():
 n=load(ROOT/'controls/negative_controls.json');assert n['status']=='PASS' and n['counts']=={'assignment_flip_rejected':24,'fault_removal_rejected':24,'proof_checker_corrupt_truncated_rejects':2,'proof_checker_valid_accepts':2,'retained_term_deletion_controls':1372,'schedule_collision_rejected':12,'truncated_assignment_rejected':1} and len(n['direct_controls'])==24 and len(n['schedule_mutation_controls'])==12
 for r in n['direct_controls']:assert r['flip_assignment_control']['failed_clause_count']>0 and not r['remove_fault_control']['ok']
 for r in n['schedule_mutation_controls']:
  times={k:int(v) for k,v in load(ROOT/'cegar'/f"iter{r['iteration']}"/'candidate.json')['schedule_times'].items()};m=r['mutation'];bad=dict(times);bad[m['edge']]=m['corrupted_time'];assert jround(M.audit_schedule(bad,True))==r['audit'] and not r['accepted']
 raw=data(ROOT/n['truncated_assignment']['path']);lits=[]
 for line in raw.decode(errors='replace').splitlines():
  if line.startswith('v '):lits.extend(int(x) for x in line[2:].split() if int(x))
 assert len({abs(x) for x in lits})==n['truncated_assignment']['expected_variables']-1 and not n['truncated_assignment']['accepted']
 return n['counts']

def load_outer_context():
 px,pz,lx,lz=B.load_context();rx,_=B.global_single_records('Xerr',M.Xchecks,px,'X');rz,_=B.global_single_records('Zerr',M.Zchecks,pz,'Z');unary=rx+rz;assert len(unary)==1440
 r62=load(ROOT/'src/round62_cegar20.json');B.replay_round62_blocks(r62,lx,lz);assert len(r62['outer_blocks'])==20;return px,pz,lx,lz,unary,r62

def verify_outer_fresh(i):
 px,pz,lx,lz,unary,r62=load_outer_context();d=ROOT/'cegar'/f'iter{i}';cand=load(d/'candidate.json');before=load(d/'dynamic_before.json');gens=load(d/'generalized_before.json');outer=OuterScheduler(True)
 for j,r in enumerate(unary):outer.add_block([tuple(x) for x in r['atoms']],f'r63-{j}')
 for b in r62['outer_blocks']:outer.add_block([tuple(x) for x in b['atoms']],'r62-'+b['tag'],b['trace_sha256'])
 for t in gens['terms']:outer.add_block([tuple(x) for x in t['atoms']],t['term_id'],t.get('source_term_sha256'))
 for j,b in enumerate(before):outer.add_block([tuple(x) for x in b['atoms']],f"dynamic-{j}-{b['sector']}",b.get('mechanism_sha256'))
 assert len(outer.blocks)==cand['asserted_blocks']['total']==1440+20+gens['term_count']+len(before)
 rebuilt=outer.s.to_smt2().encode();stored=data(d/'outer.smt2');assert rebuilt==stored,(i,sha_bytes(rebuilt),sha_bytes(stored));times={k:int(v) for k,v in cand['schedule_times'].items()};audit=M.audit_schedule(times,True);assert audit==cand['audit'] and audit['ok'] and audit['global_interleaved'] and set(times)==set(M.ALL_EDGES) and len(times)==864
 fixed=z3.Solver();fixed.add(z3.parse_smt2_string(stored.decode()))
 for e in M.ALL_EDGES:fixed.add(z3.Int('t_'+e.replace(':','_'))==times[e])
 assert fixed.check()==z3.sat and all(not M.block_holds(times,[tuple(x) for x in t['atoms']]) for t in gens['terms']) and all(not M.block_holds(times,[tuple(x) for x in b['atoms']]) for b in before)
 return {'schema':'round74-fresh-outer-full-replay-v1','status':'PASS','iteration':i,'blocks':len(outer.blocks),'smt2_sha256':sha_bytes(stored),'schedule_sha256':sha_obj(times),'fixed_model_status':'SAT','named_edges':864,'mc_constraints':648}

def verify_direct_full():
 px,pz,lx,lz,unary,r62=load_outer_context();rows=[]
 with tempfile.TemporaryDirectory(prefix='circdist_r74_direct_full_') as td:
  tmp=Path(td)
  for i in range(42,54):
   d=ROOT/'cegar'/f'iter{i}';cand=load(d/'candidate.json');saved=load(d/'direct_verification.json');times={k:int(v) for k,v in cand['schedule_times'].items()};ss=B.sectors(times,lx,lz);vr=tmp/f'iter{i}';(vr/'direct360').mkdir(parents=True);(vr/'solver').mkdir()
   for lab in ('Xerr','Zerr'):
    gen=tmp/f'generated-{i}'/lab;B.build_direct_cnf(ss[lab],gen,cand['schedule_sha256'],10)
    for suffix in ('clauses.jsonl','cnf','columns.json','summary.json','variables.json'):
     got=data(d/'direct360'/f'{lab}.{suffix}');want=gen.with_suffix('.'+suffix).read_bytes();assert got==want,(i,lab,suffix,sha_bytes(got),sha_bytes(want));(vr/'direct360'/f'{lab}.{suffix}').write_bytes(got)
    (vr/'solver'/f'{lab}.solver.log').write_bytes(data(d/'solver'/f'{lab}.solver.log'));got=jround(V.verify_one(vr,lab,ss[lab]));assert got==saved['sectors'][lab]
    rows.append({'iteration':i,'sector':lab,'cnf_sha256':sha_bytes(data(d/'direct360'/f'{lab}.cnf')),'assignment_variables':got['assignment_variables'],'fault_weight':got['mechanism']['fault_count'],'raw_replay':'PASS'})
 return {'status':'PASS','formulae_rebuilt':24,'assignments_replayed':24,'rows':rows}

def verify_generalization_full():
 names=['formula_raw_replay_bindings.json','mechanisms.json','local_order_catalog.json','w14_positive_pool.json','multi_check_relations.json','pair_relations.json','raw_term_candidates.json','retained_terms.json','tuple_raw_replay.json','dedup_ledger.json','summary.json','generalized_after.json','mechanism_registry_after.json','install_result.json']
 rows=[]
 with tempfile.TemporaryDirectory(prefix='circdist_r74_generalization_full_') as td:
  tmp=Path(td);state=materialize(ROOT/'restart/installed_generalized_terms_iteration42.json',tmp/'state.json');registry=materialize(ROOT/'restart/online_mechanism_registry_iteration42.json',tmp/'registry.json')
  for i in range(42,54):
   src=ROOT/'cegar'/f'iter{i}';it=tmp/f'iter{i}';(it/'direct360').mkdir(parents=True);(it/'solver').mkdir()
   for n in ['candidate.json','direct_verification.json']:materialize(src/n,it/n)
   for lab in ('Xerr','Zerr'):
    for suffix in ('clauses.jsonl','cnf','columns.json','summary.json','variables.json'):materialize(src/'direct360'/f'{lab}.{suffix}',it/'direct360'/f'{lab}.{suffix}')
    materialize(src/'solver'/f'{lab}.solver.log',it/'solver'/f'{lab}.solver.log')
   out=it/'generalization';cmd=[sys.executable,str(ROOT/'src/generalize_online.py'),'--root',str(ROOT),'--iteration-root',str(it),'--generalized-state',str(state),'--registry-state',str(registry),'--output-root',str(out)];p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=900);assert p.returncode==0,(i,p.returncode,p.stdout[-4000:])
   fs=[]
   for n in names:
    got=(out/n).read_bytes();want=data(src/'generalization'/n);assert got==want,(i,n,len(got),len(want),sha_bytes(got),sha_bytes(want));fs.append({'path':n,'bytes':len(got),'sha256':sha_bytes(got)})
   rows.append({'iteration':i,'recomputed_outputs':fs,'stdout_sha256':sha_bytes(p.stdout.encode())})
  assert state.read_bytes()==data(ROOT/'classification/installed_generalized_terms.json') and registry.read_bytes()==data(ROOT/'classification/online_mechanism_registry.json')
 return {'status':'PASS','iterations':12,'output_files_recomputed':12*len(names),'final_state_equal':True,'rows':rows}

def verify_full():
 outer=[]
 for i in range(42,54):
  p=subprocess.run([sys.executable,str(ROOT/'verify.py'),'--outer-only',str(i)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=300);assert p.returncode==0 and '"status": "PASS"' in p.stdout,(i,p.returncode,p.stdout[-2000:]);outer.append(json.loads(p.stdout))
 return {'fresh_process_outer_replays':outer,'direct':verify_direct_full(),'online_generalization':verify_generalization_full()}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo-root',type=Path);ap.add_argument('--quick',action='store_true');ap.add_argument('--full',action='store_true');ap.add_argument('--allow-unsealed',action='store_true');ap.add_argument('--outer-only',type=int);a=ap.parse_args();t=time.monotonic()
 if a.outer_only is not None:print(json.dumps(verify_outer_fresh(a.outer_only),indent=2,sort_keys=True));return
 result={'schema':'round74-self-contained-verification-v1','manifest':verify_manifest(a.allow_unsealed),'compression':verify_compression(),'bindings':verify_bindings(a.repo_root.resolve() if a.repo_root else None),'cegar_quick':verify_cegar_quick(),'generalization_quick':verify_generalization_quick(),'processes':verify_process_ledger(),'negative_controls':verify_negative_controls(),'proof_checker_controls':verify_proof_controls()}
 if a.full or not a.quick:result['full']=verify_full()
 assert (ROOT/'VERDICT.txt').read_text().strip()=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED' and load(ROOT/'RESULT.json')['verdict']=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED';result['verdict']='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED';result['fresh_independent_review_required']=True;result['status']='PASS';result['wall_seconds']=time.monotonic()-t;print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
