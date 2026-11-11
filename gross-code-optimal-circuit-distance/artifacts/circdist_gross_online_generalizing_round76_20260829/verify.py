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

def verify_compression(allow_unsealed=False):
 p=ROOT/'COMPRESSED_INVENTORY.json'
 if not p.exists():
  assert allow_unsealed,'missing COMPRESSED_INVENTORY.json';return {'present':False,'files':0}
 inv=load(p);assert inv['file_count']==len(inv['files']);tot=comp=0
 actual=sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.gz'));assert actual==sorted(r['path'] for r in inv['files']),(len(actual),len(inv['files']))
 for r in inv['files']:
  p=ROOT/r['path'];raw=p.read_bytes();assert not (ROOT/r['original_path']).exists(),r['original_path'];assert len(raw)==r['compressed_bytes'] and sha_bytes(raw)==r['compressed_sha256'] and int.from_bytes(raw[4:8],'little')==0
  z=gzip.decompress(raw);assert len(z)==r['uncompressed_bytes'] and sha_bytes(z)==r['uncompressed_sha256'];tot+=len(z);comp+=len(raw)
 assert (tot,comp)==(inv['uncompressed_bytes'],inv['compressed_bytes']);return {'present':True,'files':len(actual),'uncompressed_bytes':tot,'compressed_bytes':comp}

def verify_nested_manifest(pkg,seal):
 p=pkg/'SHA256SUMS.txt';assert sha_bytes(p.read_bytes())==seal;rows=[]
 for line in p.read_text().splitlines():
  if not line.strip():continue
  h,rel=line.split('  ',1);q=pkg/rel;assert q.is_file() and sha_bytes(q.read_bytes())==h,(pkg.name,rel);rows.append(rel)
 expected=sorted(q.relative_to(pkg).as_posix() for q in pkg.rglob('*') if q.is_file() and q.relative_to(pkg).as_posix()!='SHA256SUMS.txt');assert sorted(rows)==expected,(len(rows),len(expected));return len(rows)

def verify_bindings(repo_root=None):
 s=load(ROOT/'SOURCE_BINDINGS.json')
 assert s['round74_source']['seal_file_sha256']=='321eb6ccaae3795e866b0cad409571b35dff7b7b17a84c614c8ab1a23b8e498c'
 assert s['round75_review']['sha256']=='a6ee9d2c18291f3474672fb13682e6720a0f2d313da138da26397e67ccd48cc8'
 assert s['actual_direct_primary_domain']=={'per_sector':360,'data_singletons':144,'residual_elementary_fault_columns':216,'weight12_pool_role':'quotient basis and positive completions only'}
 for r in s['embedded_source_copies']:
  b=(ROOT/r['path']).read_bytes();assert len(b)==r['bytes'] and sha_bytes(b)==r['sha256'],r['path']
 for r in s['engine_files']:
  b=data(ROOT/r['path']);assert len(b)==r['bytes'] and sha_bytes(b)==r['sha256'],r['path']
 assert sha_bytes((ROOT/s['round74_source']['embedded_seal_file']).read_bytes())==s['round74_source']['seal_file_sha256']
 assert len((ROOT/s['round74_source']['embedded_seal_file']).read_text().splitlines())==s['round74_source']['source_manifest_entries']==2258
 start=s['reviewed_unstarted_iteration54'];assert start['installed_blocks']==7008 and start['counts']=={'unary':1440,'round62':20,'round69_generalized':4740,'round72_generalized':566,'round74_generalized':134,'dynamic_exact':108,'registry':24}
 vals={}
 for k,r in start['states'].items():
  raw=(ROOT/r['path']).read_bytes();assert len(raw)==r['compressed_bytes'] and sha_bytes(raw)==r['compressed_sha256'];z=gzip.decompress(raw);assert len(z)==r['uncompressed_bytes'] and sha_bytes(z)==r['uncompressed_sha256'];obj=json.loads(z);assert sha_obj(obj)==r['semantic_sha256'];vals[k]=obj
 assert len(vals['dynamic'])==108 and vals['generalized']['term_count']==5440 and vals['registry']['mechanism_count']==24
 env=s['environment_freeze'];b=(ROOT/env['path']).read_bytes();assert sha_bytes(b)==env['sha256']=='e5ace88d19150ff07d84704ca6e9f4a4a070c2f588a6502e4ca0bfe99ebf6ee6' and b.decode().splitlines()==env['text']
 live=0
 if repo_root is not None:
  for r in s['repository_start_snapshots']:
   b=(ROOT/r['snapshot']).read_bytes();assert len(b)==r['bytes'] and sha_bytes(b)==r['sha256'] and (repo_root/r['live_path']).read_bytes()==b,r['live_path'];live+=1
  sp=repo_root/s['round74_source']['live_repo_path'];assert sha_bytes((sp/'SHA256SUMS.txt').read_bytes())==s['round74_source']['seal_file_sha256'];verify_nested_manifest(sp,s['round74_source']['seal_file_sha256'])
  rp=repo_root/s['round75_review']['live_repo_path'];assert sha_bytes(rp.read_bytes())==s['round75_review']['sha256'];live+=2
 return {'embedded_files':len(s['embedded_source_copies']),'live_bindings_checked':live,'source_manifest_entries':2258,'reviewed_start_blocks':7008,'reviewed_start':{'dynamic':108,'generalized':5440,'registry':24}}

def run_control(cmd,want,marker,timeout=180):
 p=subprocess.run([str(x) for x in cmd],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=timeout);assert p.returncode==want and marker in p.stdout,(p.returncode,p.stdout[-1000:]);return {'exit_code':p.returncode,'marker':marker}
def verify_proof_controls():
 c=ROOT/'controls/round76_proof_checker';t=ROOT/'tooling';summary=load(c/'summary.json');assert summary['status']=='PASS'
 for n,r in summary['fixtures'].items():b=(c/n).read_bytes();assert len(b)==r['bytes'] and sha_bytes(b)==r['sha256']
 with tempfile.TemporaryDirectory(prefix='circdist_r76_proof_') as td:
  lrat=Path(td)/'valid.lrat'
  out={'drat_valid':run_control([t/'drat-trim-arm64-macos',c/'php6_5.cnf',c/'php6_5.drat','-t','170','-L',lrat],0,'VERIFIED'),'lrat_valid':run_control([t/'lrat-check-arm64-macos',c/'php6_5.cnf',lrat],0,'VERIFIED'),'drat_corrupt':run_control([t/'drat-trim-arm64-macos',c/'php6_5.cnf',c/'php6_5_corrupted_truncated_10_lines.drat','-t','170'],1,'NOT VERIFIED'),'lrat_corrupt':run_control([t/'lrat-check-arm64-macos',c/'php6_5.cnf',c/'php6_5_corrupted_truncated_10_lines.lrat'],1,'NOT VERIFIED')}
  assert sha_bytes(lrat.read_bytes())==summary['fixtures']['php6_5.generated.lrat']['sha256'];return out

def pc(z):return bin(z).count('1')
def mask(xs):return sum(1<<int(x) for x in xs)
def signature(lab,x,lx,lz):
 det=M.HZ if lab=='Xerr' else M.HX;duals=lz if lab=='Xerr' else lx;syn=sum(((pc(x&r)&1)<<j) for j,r in enumerate(det));logical=sum(((pc(x&r)&1)<<j) for j,r in enumerate(duals));return syn|(logical<<72)
def verify_generalization_quick():
 want={'source_mechanisms':48,'formula_assignment_raw_replays':48,'participating_catalogs':271,'local_order_records':195120,'structural_pair_relations':755,'structural_pair_cells_represented':391392000,'positive_pair_relations':156,'unary_only_pair_relations':599,'positive_pair_configurations':162,'positive_pair_cells':68352,'positive_finder_misses':793,'multi_check_exact_relations':48,'multi_check_terms_generated':96,'pair_terms_generated':324,'raw_term_candidates':420,'retained_increment':303,'merged_installed_generalized_terms':5743,'literal_retained_tuple_replays':2637648,'factorized_symbolically_proved_tuples':55037740032,'pair_domain_library_relative_new_tuples':2584752,'retained_deletion_controls':3085}
 s=load(ROOT/'classification/summary.json');assert s['status']=='PASS' and s['factorized_multi_validation_is_symbolic_universal_not_sampling'] and s['retained_relation_kinds']=={'multi_check_exact_selected_mechanism':2,'positive_pair_rectangle':301}
 for k,v in want.items():assert s[k]==v,(k,s[k],v)
 d=load(ROOT/'classification/dedup_ledger.json');assert {k:d[k] for k in ['raw_term_candidates','multi_check_candidates','pair_candidates','duplicate_old','duplicate_new','dominated_old','dominated_new','retained_increment']}=={'raw_term_candidates':420,'multi_check_candidates':96,'pair_candidates':324,'duplicate_old':0,'duplicate_new':71,'dominated_old':0,'dominated_new':46,'retained_increment':303}
 terms=load(ROOT/'classification/round76_retained_terms.json')['terms'];assert len(terms)==303 and len({t['term_id'] for t in terms})==303 and sum(len(t['deletion_controls']) for t in terms)==3085
 for t in terms:
  atoms=[tuple(x) for x in t['atoms']];assert len(atoms)==t['atom_count'] and all(tuple(c['removed_atom']) in atoms and ('exposed_tuple' in c or ('exposed_a_order' in c and 'exposed_b_order' in c)) for c in t['deletion_controls']) and t['covered_tuple_count']>0
 state=load(ROOT/'classification/installed_generalized_terms.json');reg=load(ROOT/'classification/online_mechanism_registry.json');assert state['term_count']==5743 and state['round74_retained_terms']==134 and state['round76_retained_terms']==303 and reg['mechanism_count']==72
 byid={t['term_id']:t for t in terms};assert set(byid)=={t['term_id'] for t in state['terms'] if t.get('source_round')==76 or t.get('source_iteration',-1)>=54}
 px,pz,lx,lz=B.load_context();assert len(px)==len(pz)==1884
 totals={'catalogs':0,'relations':0,'literal':0,'factorized':0,'raw':0,'retained':0,'dp_terms':0};prev_dyn=108;prev_gen=5440;prev_reg=24
 for i in range(54,78):
  q=ROOT/'cegar'/f'iter{i}';o=load(q/'iteration_outcome.json');cand=load(q/'candidate.json');orep=load(q/'outer_independent_replay.json');dv=load(q/'direct_verification.json');gs=load(q/'generalization/summary.json');dl=load(q/'generalization/dedup_ledger.json');cat=load(q/'generalization/local_order_catalog.json');mr=load(q/'generalization/multi_check_relations.json');pr=load(q/'generalization/pair_relations.json');tr=load(q/'generalization/retained_terms.json')['terms'];tu=load(q/'generalization/tuple_raw_replay.json');fb=load(q/'generalization/formula_raw_replay_bindings.json')['records'];wb=load(q/'generalization/w14_positive_pool.json')
  before=load(q/'dynamic_before.json');after=load(q/'dynamic_after.json');gb=load(q/'generalized_before.json');ga=load(q/'generalized_after.json');rb=load(q/'mechanism_registry_before.json');ra=load(q/'mechanism_registry_after.json')
  assert len(before)==prev_dyn and len(after)==prev_dyn+2 and gb['term_count']==prev_gen and ga['term_count']==prev_gen+gs['retained_increment'] and rb['mechanism_count']==prev_reg and ra['mechanism_count']==prev_reg+2
  assert o['outer_status']=='SAT' and o['raw_replay_passed'] and not o['repair_entered'] and not o['branch_closed'] and o['installed_blocks_before']==1440+20+prev_gen+prev_dyn and o['installed_blocks_after']==1440+20+ga['term_count']+len(after)
  assert cand['asserted_blocks']['total']==o['installed_blocks_before'] and cand['audit']['ok'] and cand['audit']['global_interleaved'] and cand['audit']['edge_count']==864 and cand['audit']['overlaps']==648
  assert cand['actual_primary_domain']=={'checks':72,'data_singletons':144,'per_sector_total':360,'residual_elementary_fault_columns':216,'residuals_per_check':3,'weight12_pool_is_not_primary_domain':True}
  assert orep['status']=='PASS' and orep['parsed_ordered_assertions_equal'] and orep['serialized_formula_fixed_model_status']=='SAT' and orep['all_installed_antecedents_excluded']
  assert len(fb)==2 and all(x['complete_assignment'] and x['all_dimacs_clauses_satisfied_independently'] and x['raw_canonical_and_physical_replay_passed'] for x in fb)
  for off,lab in enumerate(('Xerr','Zerr')):
   sec=dv['sectors'][lab];fs=sec['formula_summary'];assert sec['status']=='SATISFIABLE' and sec['all_dimacs_clauses_satisfied'] and fs['complete_query'] and fs['primary_selection_variables']==360 and fs['W']==10 and fs['excluded_restrictions']==['no pool restriction','no residual-pattern restriction','no check-count restriction','no within-check order family restriction'] and sec['mechanism']['canonical_replay']['ok'] and sec['mechanism']['physical_syndrome']==[] and sec['mechanism']['physical_nontrivial'] and sec['mechanism']['fault_count']<=10
   assert after[-2+off]['source_iteration']==i and after[-2+off]['sector']==lab and after[-2+off]['atoms']==sec['mechanism']['sound_outer_block']['atoms']
  assert gs['status']=='PASS' and dl['installed_generalized_before']==prev_gen and dl['installed_generalized_after']==ga['term_count'] and len(tr)==gs['retained_increment'] and tu['all_passed'] and len(tu['terms'])==len(tr)
  assert len(cat['entries'])==gs['participating_catalogs'] and len(mr['relations'])==2 and len(pr['relations'])==gs['structural_pair_relations']
  cats={(e['sector'],e['check']):e for e in cat['entries']}
  for e in cat['entries']:
   assert len(e['orders'])==720 and [x['order_id'] for x in e['orders']]==list(range(720)) and all(sorted(x['qubits'])==sorted(e['row']) for x in e['orders'])
   for order in e['orders']:
    for op in order['options']:assert signature(e['sector'],mask(op['canonical_support']),lx,lz)==signature(e['sector'],mask(op['physical_support']),lx,lz)==int(op['signature_hex'],16)
  truth_cells=explicit_cells=configurations=positive_relations=0
  for rel in pr['relations']:
   assert len(rel['truth_rows_hex'])==len(rel['explicit_good_good_rows_hex'])==720
   truth=[int(x,16) for x in rel['truth_rows_hex']];explicit=[int(x,16) for x in rel['explicit_good_good_rows_hex']];assert all(0<=x<(1<<720) for x in truth+explicit) and all((e&~t)==0 for t,e in zip(truth,explicit))
   assert sum(pc(x) for x in truth)==rel['truth_cell_count'] and sum(pc(x) for x in explicit)==rel['explicit_good_good_cell_count'] and len(rel['positive_configurations'])==rel['positive_configuration_count'] and len(rel['generated_terms'])==2*rel['positive_configuration_count']
   truth_cells+=rel['truth_cell_count'];explicit_cells+=rel['explicit_good_good_cell_count'];configurations+=rel['positive_configuration_count'];positive_relations+=bool(rel['positive_configuration_count'])
  assert len(pr['relations'])*720*720==gs['structural_pair_cells_represented'] and explicit_cells==gs['positive_pair_cells'] and configurations==gs['positive_pair_configurations'] and positive_relations==gs['positive_pair_relations']
  relmap={(r['mechanism_id'],r['sector']):r for r in mr['relations']}
  for x in tu['terms']:
   assert x['all_raw_replays_passed'] and x['tuples_instantiated']==x['expected_covered_tuples']
   t=next(z for z in tr if z['term_id']==x['term_id'])
   if x['relation_kind']=='positive_pair_rectangle':assert x['validation_mode']=='literal_every_tuple' and x['selector_stream_scope']=='every covered tuple'
   else:
    assert x['validation_mode']=='factorized_symbolic_universal' and x['factorized_universal_basis'] and 'without sampling' in x['factorized_universal_basis'];rel=relmap[(t['mechanism_id'],t['sector'])];dp={int(t['constant_signature_hex'],16)};product=1;layers=[]
    for c in t['checks']:
     m=int(t['allowed_order_masks_hex'][str(c)],16);ids=[j for j in range(720) if (m>>j)&1];assert len(ids)==t['allowed_order_counts'][str(c)];product*=len(ids);records=rel['local_order_contributions'][str(c)]['per_order'];assert len(records)==720
     sigs=set()
     for j in ids:
      rec=records[j];assert rec['order_id']==j;sg=signature(t['sector'],mask(rec['canonical_support']),lx,lz);assert sg==signature(t['sector'],mask(rec['physical_support']),lx,lz)==int(rec['signature_hex'],16);sigs.add(sg)
     dp={a^b for a in dp for b in sigs};layers.append({'check':c,'reachable_signature_count':len(dp),'reachable_signatures_sha256':sha_obj([hex(z) for z in sorted(dp)])})
    assert product==t['covered_tuple_count']==x['expected_covered_tuples'] and layers==t['dp_layers'] and len(dp)==t['reachable_signature_count'] and all((z&((1<<72)-1))==0 and (z>>72)!=0 for z in dp);totals['dp_terms']+=1
  totals['catalogs']+=len(cat['entries']);totals['relations']+=len(pr['relations']);totals['literal']+=gs['literal_retained_tuple_replays'];totals['factorized']+=gs['factorized_symbolically_proved_tuples'];totals['raw']+=gs['raw_term_candidates'];totals['retained']+=gs['retained_increment'];prev_dyn=len(after);prev_gen=ga['term_count'];prev_reg=ra['mechanism_count']
 assert (prev_dyn,prev_gen,prev_reg)==(156,5743,72) and totals=={'catalogs':271,'relations':755,'literal':2637648,'factorized':55037740032,'raw':420,'retained':303,'dp_terms':2}
 return {'status':'PASS',**want,'retained_relation_kinds':s['retained_relation_kinds'],'totals':totals}

def verify_cegar_quick():
 s=load(ROOT/'cegar/summary.json');assert s['iteration_range']==[54,77] and s['completed_dual_sector_candidates']==24 and s['outer_verdicts']=={'SAT':24,'TIMEOUT':0,'UNKNOWN':0,'UNSAT':0} and s['direct_sector_verdicts']=={'SATISFIABLE':48,'UNKNOWN_OR_TIMEOUT':0,'UNSAT_PROOFS_ACCEPTED':0} and not s['branch_closed'] and s['accepted_absence_proofs']==0
 rs=load(ROOT/'restart/restart_state.json');want={'round63_unary_blocks':1440,'round62_blocks':20,'round69_generalized_blocks':4740,'round72_generalized_blocks':566,'round74_generalized_blocks':134,'round76_generalized_blocks':303,'merged_generalized_blocks':5743,'dynamic_blocks_total':156,'dynamic_blocks_inherited_round74':108,'dynamic_blocks_new_round76':48,'exploratory_round63_pair_clauses_installed':0,'next_outer_total_blocks':7359,'next_iteration':78,'dynamic_state':'cegar/dynamic_blocks.json','generalized_state':'classification/installed_generalized_terms.json','registry_state':'classification/online_mechanism_registry.json'};assert rs['counts']==want and rs['next_iteration']==78 and rs['total_installed_blocks']==7359 and rs['unstarted']
 objs={k:load(ROOT/v) for k,v in rs['states'].items()};assert objs['dynamic']==load(ROOT/'cegar/dynamic_blocks.json') and objs['generalized']==load(ROOT/'classification/installed_generalized_terms.json') and objs['mechanism_registry']==load(ROOT/'classification/online_mechanism_registry.json')
 assert sha_obj(objs['dynamic'])==rs['state_semantic_sha256']['dynamic'] and sha_obj(objs['generalized'])==rs['state_semantic_sha256']['generalized'] and sha_obj(objs['mechanism_registry'])==rs['state_semantic_sha256']['mechanism_registry']
 return {'completed_candidates':24,'outer_sat':24,'direct_sat_raw_replayed':48,'new_exact_blocks':48,'new_generalized_terms':303,'dynamic_blocks':156,'generalized_terms':5743,'registry':72,'next_iteration':78,'next_total_blocks':7359,'absence_proofs':0,'repair_entered':False,'root_closed':False}

def verify_process_ledger():
 p=load(ROOT/'PROCESS_LEDGER.json');rows=p['candidate_process_records'];assert len(rows)==168 and p['strict_foreground_serial'] and p['outer_process_fresh_per_iteration'] and p['detached_processes']==0 and p['candidate_exit_10_sat']==48 and p['candidate_exit_0']==120 and p['candidate_timeouts']==p['candidate_signals']==0 and len(p['correction_records'])==1
 assert sorted(set(r['iteration'] for r in rows))==list(range(54,78)) and all(not r['timed_out'] and not r['sigterm_sent'] and not r['sigkill_sent'] for r in rows)
 for a,b in zip(rows,rows[1:]):assert a['ended_utc']<=b['started_utc']
 assert p['correction_records'][0]['exit_code']==1 and not p['correction_records'][0]['state_mutation']
 return {'records':168,'exit_0':120,'exit_10_sat':48,'timeouts':0,'signals':0,'correction_records':1,'detached':0}

def verify_negative_controls():
 n=load(ROOT/'controls/negative_controls.json');want={'assignment_flip_rejected':48,'fault_removal_rejected':48,'proof_checker_corrupt_truncated_rejects':2,'proof_checker_valid_accepts':2,'retained_term_deletion_controls':3085,'schedule_collision_rejected':24,'truncated_assignment_rejected':1};assert n['status']=='PASS' and n['counts']==want and len(n['direct_controls'])==48 and len(n['schedule_mutation_controls'])==24
 for r in n['direct_controls']:assert r['flip_assignment_control']['failed_clause_count']>0 and not r['remove_fault_control']['ok']
 for r in n['schedule_mutation_controls']:
  times={k:int(v) for k,v in load(ROOT/'cegar'/f"iter{r['iteration']}"/'candidate.json')['schedule_times'].items()};m=r['mutation'];bad=dict(times);bad[m['edge']]=m['corrupted_time'];assert jround(M.audit_schedule(bad,True))==r['audit'] and not r['accepted']
 raw=data(ROOT/n['truncated_assignment']['path']);lits=[]
 for line in raw.decode(errors='replace').splitlines():
  if line.startswith('v '):lits.extend(int(x) for x in line[2:].split() if int(x))
 assert len({abs(x) for x in lits})==n['truncated_assignment']['expected_variables']-1 and not n['truncated_assignment']['accepted'];return want

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
 return {'schema':'round76-fresh-outer-full-replay-v1','status':'PASS','iteration':i,'blocks':len(outer.blocks),'smt2_sha256':sha_bytes(stored),'schedule_sha256':sha_obj(times),'fixed_model_status':'SAT','named_edges':864,'mc_constraints':648}

def verify_direct_full():
 px,pz,lx,lz,unary,r62=load_outer_context();rows=[]
 with tempfile.TemporaryDirectory(prefix='circdist_r76_direct_full_') as td:
  tmp=Path(td)
  for i in range(54,78):
   d=ROOT/'cegar'/f'iter{i}';cand=load(d/'candidate.json');saved=load(d/'direct_verification.json');times={k:int(v) for k,v in cand['schedule_times'].items()};ss=B.sectors(times,lx,lz);vr=tmp/f'iter{i}';(vr/'direct360').mkdir(parents=True);(vr/'solver').mkdir()
   for lab in ('Xerr','Zerr'):
    gen=tmp/f'generated-{i}'/lab;B.build_direct_cnf(ss[lab],gen,cand['schedule_sha256'],10)
    for suffix in ('clauses.jsonl','cnf','columns.json','summary.json','variables.json'):
     got=data(d/'direct360'/f'{lab}.{suffix}');want=gen.with_suffix('.'+suffix).read_bytes();assert got==want,(i,lab,suffix,sha_bytes(got),sha_bytes(want));(vr/'direct360'/f'{lab}.{suffix}').write_bytes(got)
    (vr/'solver'/f'{lab}.solver.log').write_bytes(data(d/'solver'/f'{lab}.solver.log'));got=jround(V.verify_one(vr,lab,ss[lab]));assert got==saved['sectors'][lab]
    rows.append({'iteration':i,'sector':lab,'cnf_sha256':sha_bytes(data(d/'direct360'/f'{lab}.cnf')),'assignment_variables':got['assignment_variables'],'fault_weight':got['mechanism']['fault_count'],'raw_replay':'PASS'})
 return {'status':'PASS','formulae_rebuilt':48,'assignments_replayed':48,'rows':rows}

def verify_generalization_full():
 names=['formula_raw_replay_bindings.json','mechanisms.json','local_order_catalog.json','w14_positive_pool.json','multi_check_relations.json','pair_relations.json','raw_term_candidates.json','retained_terms.json','tuple_raw_replay.json','dedup_ledger.json','summary.json','generalized_after.json','mechanism_registry_after.json','install_result.json']
 rows=[]
 with tempfile.TemporaryDirectory(prefix='circdist_r76_generalization_full_') as td:
  tmp=Path(td);state=materialize(ROOT/'restart/installed_generalized_terms_iteration54.json',tmp/'state.json');registry=materialize(ROOT/'restart/online_mechanism_registry_iteration54.json',tmp/'registry.json')
  for i in range(54,78):
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
 return {'status':'PASS','iterations':24,'output_files_recomputed':24*len(names),'final_state_equal':True,'rows':rows}

def verify_full():
 outer=[]
 for i in range(54,78):
  p=subprocess.run([sys.executable,str(ROOT/'verify.py'),'--outer-only',str(i)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=300);assert p.returncode==0 and '"status": "PASS"' in p.stdout,(i,p.returncode,p.stdout[-2000:]);outer.append(json.loads(p.stdout))
 return {'fresh_process_outer_replays':outer,'direct':verify_direct_full(),'online_generalization':verify_generalization_full()}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo-root',type=Path);ap.add_argument('--quick',action='store_true');ap.add_argument('--full',action='store_true');ap.add_argument('--allow-unsealed',action='store_true');ap.add_argument('--outer-only',type=int);a=ap.parse_args();t=time.monotonic()
 if a.outer_only is not None:print(json.dumps(verify_outer_fresh(a.outer_only),indent=2,sort_keys=True));return
 result={'schema':'round76-self-contained-verification-v1','manifest':verify_manifest(a.allow_unsealed),'compression':verify_compression(a.allow_unsealed),'bindings':verify_bindings(a.repo_root.resolve() if a.repo_root else None),'cegar_quick':verify_cegar_quick(),'generalization_quick':verify_generalization_quick(),'processes':verify_process_ledger(),'negative_controls':verify_negative_controls(),'proof_checker_controls':verify_proof_controls()}
 if a.full or not a.quick:result['full']=verify_full()
 assert (ROOT/'VERDICT.txt').read_text().strip()=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED' and load(ROOT/'RESULT.json')['verdict']=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED';result['verdict']='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED';result['fresh_independent_review_required']=True;result['status']='PASS';result['wall_seconds']=time.monotonic()-t;print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
