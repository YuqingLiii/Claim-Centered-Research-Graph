#!/usr/bin/env python3
from pathlib import Path
import collections,gzip,hashlib,json,os,statistics
ROOT=Path(__file__).resolve().parent.parent
REPO=Path('<repo>')
def rb(p):
 p=Path(p)
 if p.suffix=='.gz':
  with gzip.open(p,'rb') as f:return f.read()
 return p.read_bytes()
def load(p):return json.loads(rb(p))
def sha(b):return hashlib.sha256(b).hexdigest()
def sha_obj(o):return sha(json.dumps(o,sort_keys=True,separators=(',',':')).encode())
its=[]; runs=[]
for i in range(6,30):
 d=ROOT/'cegar'/f'iter{i}';o=load(d/'iteration_outcome.json');c=load(d/'candidate.json.gz');ov=load(d/'outer_independent_replay.json');dv=load(d/'direct_verification.json.gz')
 assert o['iteration']==i and ov['status']=='PASS'
 row={'iteration':i,'candidate_sha256':o['candidate_sha256'],'outer_status':o['outer_status'],'outer_seconds':o['outer_seconds'],'outer_smt2_sha256':c['outer_smt2_sha256'],'installed_blocks_before':o['installed_blocks_before'],'dynamic_blocks_after':o['dynamic_blocks_after'],'used_layers':c['audit']['used_layers'],'max_time':c['audit']['max_time'],'global_interleaved':c['audit']['global_interleaved'],'overlap_interleaved_pairs':c['audit']['overlap_interleaved_pairs'],'whole_check_interleaved_pairs':c['audit']['whole_check_interleaved_pairs'],'sectors':{}}
 for s in ('Xerr','Zerr'):
  v=dv['sectors'][s];summ=v['formula_summary'];sr=load(d/f'{s}_solver.run.json')
  row['sectors'][s]={'status':v['status'],'solver_exit_code':sr['exit_code'],'solver_wall_seconds':sr['wall_seconds'],'timed_out':sr['timed_out'],'variables':summ['variables'],'clauses':summ['clauses'],'primary_selection_variables':summ['primary_selection_variables'],'logical_output_variables':summ['logical_output_variables'],'complete_query':summ['complete_query'],'dimacs_sha256':summ['dimacs_sha256'],'fault_count':v['mechanism']['fault_count'],'atom_count':v['mechanism']['sound_outer_block']['atom_count'],'selected_names':v['mechanism']['selected_names'],'canonical_net_weight':len(v['mechanism']['canonical_replay']['net_support']),'physical_net_weight':v['mechanism']['physical_net_weight'],'all_dimacs_clauses_satisfied':v['all_dimacs_clauses_satisfied'],'physical_syndrome':v['mechanism']['physical_syndrome'],'physical_nontrivial':v['mechanism']['physical_nontrivial'],'mechanism_sha256':sha_obj(v['mechanism'])}
 its.append(row)
 for p in sorted(d.glob('*.run.json')):
  x=load(p);runs.append({'iteration':i,'kind':p.name[:-9],'record_path':p.relative_to(ROOT).as_posix(),**x})
assert len(its)==24 and len(runs)==144
final_dyn=load(ROOT/'cegar/dynamic_blocks.json');initial=load(ROOT/'cegar/inherited_dynamic_blocks_round69.json');assert len(initial)==12 and len(final_dyn)==60 and final_dyn[:12]==initial
for idx,b in enumerate(final_dyn[12:]):
 i=6+idx//2;s=('Xerr','Zerr')[idx%2];r=its[i-6];assert b['source_iteration']==i and b['sector']==s and b['candidate_sha256']==r['candidate_sha256'] and b['mechanism_sha256']==r['sectors'][s]['mechanism_sha256']
weight_hist={s:dict(sorted(collections.Counter(r['sectors'][s]['fault_count'] for r in its).items())) for s in ('Xerr','Zerr')}
atom_hist={s:dict(sorted(collections.Counter(r['sectors'][s]['atom_count'] for r in its).items())) for s in ('Xerr','Zerr')}
solver_rows=[(r['sectors'][s]['solver_wall_seconds'],r['iteration'],s) for r in its for s in ('Xerr','Zerr')]
summary={'schema':'round71-gross-exact-cegar-summary-v1','verdict':'MATERIAL-CHECKED-PROGRESS-NOT-CLOSED','iteration_range':[6,29],'completed_dual_sector_candidates':24,'outer_status_counts':{'SAT':24,'UNSAT':0,'UNKNOWN':0,'TIMEOUT':0},'sector_status_counts':{'Xerr':{'SAT':24,'UNSAT':0,'UNKNOWN':0,'TIMEOUT':0},'Zerr':{'SAT':24,'UNSAT':0,'UNKNOWN':0,'TIMEOUT':0}},'restart':{'next_iteration':30,'round63_unary_blocks':1440,'round62_blocks':20,'round69_generalized_blocks':4740,'dynamic_blocks_total':60,'dynamic_blocks_inherited_round69':12,'dynamic_blocks_new_round71':48,'exploratory_round63_pair_clauses_installed':0,'next_outer_total_blocks':6260,'state':'cegar/dynamic_blocks.json'},'mechanisms':{'new_raw_replayed_exact_blocks':48,'weight_histogram':weight_hist,'atom_histogram':atom_hist,'atom_minmax':{s:[min(r['sectors'][s]['atom_count'] for r in its),max(r['sectors'][s]['atom_count'] for r in its)] for s in ('Xerr','Zerr')},'all_formula_assignments_clause_checked':True,'all_raw_physical_replays_passed':True},'direct_formula':{'columns_per_sector':360,'primary_selection_variables':360,'logical_pool_members_per_sector':1884,'weight_bound':10,'restriction_free':True,'variable_ranges':{s:[min(r['sectors'][s]['variables'] for r in its),max(r['sectors'][s]['variables'] for r in its)] for s in ('Xerr','Zerr')},'clause_ranges':{s:[min(r['sectors'][s]['clauses'] for r in its),max(r['sectors'][s]['clauses'] for r in its)] for s in ('Xerr','Zerr')}},'outer':{'named_edges':864,'x_checks':72,'z_checks':72,'mc_constraints':648,'all_independent_replays_passed':True,'outer_solver_seconds_total':sum(r['outer_seconds'] for r in its),'outer_solver_seconds_min':min(r['outer_seconds'] for r in its),'outer_solver_seconds_max':max(r['outer_seconds'] for r in its),'used_layers_range':[min(r['used_layers'] for r in its),max(r['used_layers'] for r in its)]},'processes':{'strict_foreground_serial':True,'recorded_candidate_processes':144,'timeout_count':sum(bool(x['timed_out']) for x in runs),'interruption_count':0,'unexpected_exit_count':sum(x['exit_code'] not in (0,10) for x in runs),'solver_wall_seconds_total':sum(x[0] for x in solver_rows),'slowest_solver_queries':[{'iteration':i,'sector':s,'wall_seconds':w} for w,i,s in sorted(solver_rows,reverse=True)[:10]]},'absence':{'accepted_sector_absence_proofs':0,'double_sector_absence_candidates':0,'repair_entered':False,'outer_exhaustion_certificate':False,'root_closed':False},'iterations':its}
(ROOT/'cegar/summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
ledger={'schema':'round71-process-ledger-v1','strict_foreground_serial':True,'detached_processes':0,'candidate_process_records':runs,'summary':summary['processes'],'preflight':[{'name':'round69_root_seal','command':['shasum','-a','256','-c','SHA256SUMS.txt'],'exit_code':0,'checked_entries':249,'log':'preflight/round69_sha256_check.log'},{'name':'round69_clean_full_verifier','command':['python','verify.py'],'exit_code':0,'wall_seconds':120.11,'reported_math_wall_seconds':119.745757458,'log':'preflight/round69_full_verifier.log'},{'name':'round70_review_binding','command':['shasum','-a','256','circdist_gross_block_minimization_exact_review_20260829.md'],'exit_code':0,'sha256':'b2fe38fd6adb1ef974624a49b84b7a61620a5c97a531155aac01fc39dbfbaabe'},{'name':'round69_all_file_read','exit_code':0,'file_count':250,'gzip_streams':112,'tar_members':472,'record':'preflight/round69_all_file_read.json'}],'development_diagnostics':[{'description':'Initial slowest-query summary used the wrong run-record glob and returned an empty diagnostic list; a corrected glob immediately produced the sealed statistics. Both commands exited 0, changed no candidate state, and supplied no mathematical verdict.'}]}
(ROOT/'PROCESS_LEDGER.json').write_text(json.dumps(ledger,indent=2,sort_keys=True)+'\n')
# Source bindings and offline snapshots.
binding_specs=[
 ('DAG_PROTOCOL.md','bindings/snapshots/DAG_PROTOCOL.md'),('FILE_PROTOCOL.md','bindings/snapshots/FILE_PROTOCOL.md'),('operations/circdist/SCHEDULER.yaml','bindings/snapshots/SCHEDULER.yaml'),('circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md','bindings/snapshots/CIRCDIST_PROBLEMS.md'),('circdist/proof-dag/nodes/CIRCDIST.gross.yaml','bindings/snapshots/CIRCDIST.gross.yaml'),('circdist/artifacts/circdist_gross_block_minimization_round69_20260829/SHA256SUMS.txt','bindings/snapshots/round69_SHA256SUMS.txt'),('circdist/reviews/circdist_gross_block_minimization_exact_review_20260829.md','bindings/snapshots/round70_review.md')]
bind=[]
for live,snap in binding_specs:
 b=(REPO/live).read_bytes();sb=(ROOT/snap).read_bytes();assert b==sb
 bind.append({'path':live,'snapshot':snap,'bytes':len(b),'sha256':sha(b)})
engine=[]
orig=REPO/'circdist/artifacts/circdist_gross_block_minimization_round69_20260829'
for rel in ['requirements.txt','src/build_cegar_candidate.py','src/replay_direct_candidate.py','src/append_dynamic_blocks.py','src/round68_build.py','src/round68_verify.py','src/global_single_clauses.json','src/round62_cegar20.json','src/inputs/w12X.txt','src/inputs/w12Z.txt','src/round63_src/model.py','src/round63_src/outer.py','src/round63_src/pattern.py','classification/pair_classification.json.gz','tooling/cadical-1.9.5-arm64-macos','tooling/drat-trim-arm64-macos','tooling/lrat-check-arm64-macos','tooling/cadical-rel-1.9.5-source.tar.gz','tooling/drat-trim-source.tar.gz']:
 b=(orig/rel).read_bytes();local=(ROOT/rel).read_bytes();assert b==local
 engine.append({'round69_path':f'circdist/artifacts/circdist_gross_block_minimization_round69_20260829/{rel}','local_path':rel,'bytes':len(b),'sha256':sha(b)})
src={'schema':'round71-source-bindings-v1','repo_root_at_execution':str(REPO),'frozen_inputs':bind,'copied_round69_engine':engine,'round69_root_seal_sha256':'aad4434050b1b64d3907b990e8279a2b25b2b4e29abcebf585fb885f3dbab647','round70_review_sha256':'b2fe38fd6adb1ef974624a49b84b7a61620a5c97a531155aac01fc39dbfbaabe','round69_full_verifier_status':'PASS'}
(ROOT/'SOURCE_BINDINGS.json').write_text(json.dumps(src,indent=2,sort_keys=True)+'\n')
print(json.dumps({'iterations':len(its),'runs':len(runs),'dynamic':len(final_dyn),'slowest':summary['processes']['slowest_solver_queries'][0],'weight_hist':weight_hist,'used_layers_range':summary['outer']['used_layers_range']},indent=2))
