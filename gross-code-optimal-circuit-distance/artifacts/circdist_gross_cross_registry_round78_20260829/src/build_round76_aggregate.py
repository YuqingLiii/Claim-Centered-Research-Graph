#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json,shutil
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();C=R/'cegar'
FIRST,LAST=54,77

def load(p):return json.loads(Path(p).read_text())
def dump(p,o):p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def canon(o):return json.dumps(o,sort_keys=True,separators=(',',':')).encode()
def sha_obj(o):return hashlib.sha256(canon(o)).hexdigest()
def sha_file(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def norm(v):
 s=str(v);base=str(R.parent);s=s.replace(base,'SCRATCH').replace(str(R),'PACKAGE').replace('/private/tmp/','/tmp/')
 return s
aggkeys=['source_mechanisms','formula_assignment_raw_replays','participating_catalogs','local_order_records','structural_pair_relations','structural_pair_cells_represented','positive_pair_relations','unary_only_pair_relations','positive_pair_configurations','positive_pair_cells','positive_finder_misses','multi_check_exact_relations','multi_check_terms_generated','pair_terms_generated','raw_term_candidates','retained_increment','retained_tuples_covered_by_exact_validation','literal_retained_tuple_replays','factorized_symbolically_proved_tuples','pair_domain_library_relative_new_tuples','candidate_exact_blocks_preserved','mechanisms_with_installed_generalized_cover','mechanisms_exact_only']
dedkeys=['raw_term_candidates','multi_check_candidates','pair_candidates','duplicate_old','duplicate_new','dominated_old','dominated_new','retained_increment']
agg={k:0 for k in aggkeys};ded={k:0 for k in dedkeys};rows=[];retained=[];mechanisms=[];bindings=[];covers=[];raw_index=[];process=[];state_chain=[]
prev_dyn=load(R/'restart/dynamic_blocks_iteration54.json.gz') if False else None
# Exact source start is materialized in each iteration-54 before file.
prior_dyn=load(C/'iter54/dynamic_before.json');prior_gen=load(C/'iter54/generalized_before.json');prior_reg=load(C/'iter54/mechanism_registry_before.json')
assert len(prior_dyn)==108 and prior_gen['term_count']==5440 and prior_gen['round74_retained_terms']==134 and prior_reg['mechanism_count']==24
initial={'dynamic_sha256':sha_obj(prior_dyn),'generalized_sha256':sha_obj(prior_gen),'registry_sha256':sha_obj(prior_reg),'dynamic_count':108,'generalized_count':5440,'registry_count':24,'total_blocks':7008}
for i in range(FIRST,LAST+1):
 d=C/f'iter{i}';o=load(d/'iteration_outcome.json');s=load(d/'generalization/summary.json');dl=load(d/'generalization/dedup_ledger.json');tr=load(d/'generalization/retained_terms.json')['terms'];ms=load(d/'generalization/mechanisms.json')['mechanisms'];fb=load(d/'generalization/formula_raw_replay_bindings.json')['records'];raw=load(d/'generalization/raw_term_candidates.json')['terms']
 db=load(d/'dynamic_before.json');da=load(d/'dynamic_after.json');gb=load(d/'generalized_before.json');ga=load(d/'generalized_after.json');rb=load(d/'mechanism_registry_before.json');ra=load(d/'mechanism_registry_after.json')
 assert db==prior_dyn and gb==prior_gen and rb==prior_reg
 assert o['iteration']==i and o['outer_status']=='SAT' and o['raw_replay_passed'] and not o['repair_entered'] and not o['branch_closed'] and o['accepted_absence_proofs']==0
 assert o['sector_statuses']=={'Xerr':'SATISFIABLE','Zerr':'SATISFIABLE'} and all(o['all_dimacs_clauses_satisfied'].values())
 assert len(da)==len(db)+2 and ga['term_count']==gb['term_count']+s['retained_increment'] and ra['mechanism_count']==rb['mechanism_count']+2
 assert o['installed_blocks_before']==1440+20+len(db)+gb['term_count'] and o['installed_blocks_after']==1440+20+len(da)+ga['term_count']
 assert len(tr)==s['retained_increment'] and len(ms)==len(fb)==2
 for k in aggkeys:agg[k]+=s[k]
 for k in dedkeys:ded[k]+=dl[k]
 retained.extend(tr);mechanisms.extend(ms);bindings.extend(fb)
 raw_index.append({'iteration':i,'path':f'cegar/iter{i}/generalization/raw_term_candidates.json','terms':len(raw),'semantic_sha256':sha_obj(raw),'file_sha256':sha_file(d/'generalization/raw_term_candidates.json')})
 for m in ms:
  covers.append({'iteration':i,'mechanism_id':m['mechanism_id'],'sector':m['sector'],'fault_count':m['fault_count'],'covering_installed_term_ids':m['installed_generalized_cover_ids'],'covering_new_term_ids':m['new_retained_cover_ids'],'exact_only':m['generalization_disposition']=='exact_only_no_safe_generalized_term'})
 for rec in o['process_records']:
  z=dict(rec);z['argv']=[norm(x) for x in z['argv']];z['log']=norm(z['log']);process.append(z)
 rows.append({'iteration':i,'outer_status':'SAT','outer_seconds':o['outer_seconds'],'candidate_sha256':o['candidate_sha256'],'installed_blocks_before':o['installed_blocks_before'],'installed_blocks_after':o['installed_blocks_after'],'dynamic_before':len(db),'dynamic_after':len(da),'generalized_before':gb['term_count'],'generalized_after':ga['term_count'],'retained_increment':s['retained_increment'],'Xerr_status':'SATISFIABLE','Zerr_status':'SATISFIABLE','Xerr_weight':o['sector_fault_weights']['Xerr'],'Zerr_weight':o['sector_fault_weights']['Zerr'],'raw_candidates':s['raw_term_candidates'],'literal_tuple_replays':s['literal_retained_tuple_replays'],'factorized_symbolic_tuples':s['factorized_symbolically_proved_tuples'],'pair_library_relative_new_tuples':s['pair_domain_library_relative_new_tuples']})
 state_chain.append({'iteration':i,'dynamic_before_sha256':sha_obj(db),'dynamic_after_sha256':sha_obj(da),'generalized_before_sha256':sha_obj(gb),'generalized_after_sha256':sha_obj(ga),'registry_before_sha256':sha_obj(rb),'registry_after_sha256':sha_obj(ra),'before_counts':{'dynamic':len(db),'generalized':gb['term_count'],'registry':rb['mechanism_count'],'blocks':o['installed_blocks_before']},'after_counts':{'dynamic':len(da),'generalized':ga['term_count'],'registry':ra['mechanism_count'],'blocks':o['installed_blocks_after']}})
 prior_dyn,prior_gen,prior_reg=da,ga,ra
final_dyn=load(C/'dynamic_blocks.json');final_gen=load(R/'classification/installed_generalized_terms.json');final_reg=load(R/'classification/online_mechanism_registry.json')
assert (final_dyn,final_gen,final_reg)==(prior_dyn,prior_gen,prior_reg)
assert len(process)==24*7 and sum(x['exit_code']==10 for x in process)==48 and sum(x['exit_code']==0 for x in process)==120
assert all(not x['timed_out'] and not x['sigterm_sent'] and not x['sigkill_sent'] for x in process)
for x,y in zip(process,process[1:]):assert x['ended_utc']<=y['started_utc']
assert final_gen['round74_retained_terms']==134 and final_gen['round76_retained_terms']==len(retained)==303 and final_gen['term_count']==5743
assert len(final_dyn)==156 and final_reg['mechanism_count']==72
restart={'next_iteration':78,'round63_unary_blocks':1440,'round62_blocks':20,'round69_generalized_blocks':4740,'round72_generalized_blocks':566,'round74_generalized_blocks':134,'round76_generalized_blocks':len(retained),'merged_generalized_blocks':final_gen['term_count'],'dynamic_blocks_total':len(final_dyn),'dynamic_blocks_inherited_round74':108,'dynamic_blocks_new_round76':48,'exploratory_round63_pair_clauses_installed':0,'next_outer_total_blocks':1440+20+final_gen['term_count']+len(final_dyn),'dynamic_state':'cegar/dynamic_blocks.json','generalized_state':'classification/installed_generalized_terms.json','registry_state':'classification/online_mechanism_registry.json'}
cegar={'schema':'round76-online-cegar-summary-v1','status':'PASS','iteration_range':[FIRST,LAST],'completed_dual_sector_candidates':24,'outer_verdicts':{'SAT':24,'UNSAT':0,'UNKNOWN':0,'TIMEOUT':0},'direct_sector_verdicts':{'SATISFIABLE':48,'UNSAT_PROOFS_ACCEPTED':0,'UNKNOWN_OR_TIMEOUT':0},'assignment_clause_replays':48,'raw_canonical_physical_replays':48,'candidate_exact_blocks_added':48,'accepted_absence_proofs':0,'repair_entered':False,'branch_closed':False,'root_closed':False,'iterations':rows,'restart':restart}
dump(C/'summary.json',cegar)
class_summary={'schema':'round76-online-generalization-aggregate-summary-v1','status':'PASS','iteration_range':[FIRST,LAST],'inherited_reviewed_generalized_terms':5440,'round76_retained_terms':len(retained),'merged_installed_generalized_terms':final_gen['term_count'],'weight14_positive_pool_counts_last':load(C/f'iter{LAST}/generalization/summary.json')['weight14_positive_pool_counts'],'weight14_negative_results_used':0,'zero_truth_cells_used_as_absence':0,'positive_finder_misses_used_as_absence':0,'deletion_countertuples_used_as_absence':0,'joint_multi_check_dp':True,'factorized_multi_validation_is_symbolic_universal_not_sampling':True,**agg,'retained_deletion_controls':sum(len(t['deletion_controls']) for t in retained),'retained_relation_kinds':{k:sum(t['relation_kind']==k for t in retained) for k in ['positive_pair_rectangle','multi_check_exact_selected_mechanism']},'claim_scope':'positive sound online generalization and exact candidate progress only; no absence, exhaustion, or root closure'}
dump(R/'classification/summary.json',class_summary)
dump(R/'classification/dedup_ledger.json',{'schema':'round76-online-dedup-aggregate-v1','iteration_range':[FIRST,LAST],'inherited_terms':5440,'installed_generalized_after':final_gen['term_count'],**ded,'per_iteration':[{'iteration':i,**{k:load(C/f'iter{i}/generalization/dedup_ledger.json')[k] for k in dedkeys}} for i in range(FIRST,LAST+1)],'semantic_definition':'finite products of exact 720-order masks; U dominates V iff region(V) is a subset of region(U); installed predecessors and earlier current-round terms are never removed','raw_candidate_file_index':raw_index})
dump(R/'classification/round76_retained_terms.json',{'schema':'round76-retained-generalized-terms-aggregate-v1','terms':retained})
dump(R/'classification/round76_mechanisms.json',{'schema':'round76-source-mechanisms-aggregate-v1','mechanisms':mechanisms})
dump(R/'classification/round76_formula_raw_replay_bindings.json',{'schema':'round76-formula-assignment-raw-replay-bindings-aggregate-v1','records':bindings})
dump(R/'classification/source_mechanism_cover.json',{'schema':'round76-source-mechanism-cover-v1','records':covers,'all_covered_by_current_installed_library':all(x['covering_installed_term_ids'] for x in covers)})
dump(R/'classification/iteration_state_chain.json',{'schema':'round76-exact-online-state-chain-v1','initial_iteration':54,'initial':initial,'transitions':state_chain,'final_unstarted_iteration':78,'final':{'dynamic_sha256':sha_obj(final_dyn),'generalized_sha256':sha_obj(final_gen),'registry_sha256':sha_obj(final_reg),'dynamic_count':len(final_dyn),'generalized_count':final_gen['term_count'],'registry_count':final_reg['mechanism_count'],'total_blocks':restart['next_outer_total_blocks']}})
# The sole nonzero construction attempt was a read-only source quick verifier with live bindings; scheduler drift was expected and the offline sealed quick check then passed.
corrections=[{'stage':'round74_source_quick_with_live_repo','record':'preflight/round74_quick_verify.run.json','log':'preflight/round74_quick_verify.log','exit_code':1,'timed_out':False,'state_mutation':False,'reason':'expected live scheduler drift beyond the source package frozen binding; rerun without live comparison passed and exact reviewed start was separately rebound'}]
dump(R/'PROCESS_LEDGER.json',{'schema':'round76-process-ledger-v1','strict_foreground_serial':True,'detached_processes':0,'candidate_process_records':process,'candidate_records':len(process),'candidate_exit_10_sat':48,'candidate_exit_0':120,'candidate_timeouts':0,'candidate_signals':0,'correction_records':corrections,'outer_process_fresh_per_iteration':True})
# Freeze exact iteration-78 restart alongside immutable reviewed iteration-54 start snapshots.
for src,name in [(C/'dynamic_blocks.json','dynamic_blocks_iteration78.json'),(R/'classification/installed_generalized_terms.json','installed_generalized_terms_iteration78.json'),(R/'classification/online_mechanism_registry.json','online_mechanism_registry_iteration78.json')]:shutil.copy2(src,R/'restart'/name)
dump(R/'restart/restart_state.json',{'schema':'round76-exact-restart-state-v1','next_iteration':78,'unstarted':True,'total_installed_blocks':restart['next_outer_total_blocks'],'counts':restart,'state_semantic_sha256':{'dynamic':sha_obj(final_dyn),'generalized':sha_obj(final_gen),'mechanism_registry':sha_obj(final_reg)},'states':{'dynamic':'restart/dynamic_blocks_iteration78.json','generalized':'restart/installed_generalized_terms_iteration78.json','mechanism_registry':'restart/online_mechanism_registry_iteration78.json'},'reviewed_start_states':{'dynamic':'restart/dynamic_blocks_iteration54.json.gz','generalized':'restart/installed_generalized_terms_iteration54.json.gz','mechanism_registry':'restart/online_mechanism_registry_iteration54.json.gz'},'license':'restart only after a fresh independent exact review accepts this proposer package; this package does not close the root'})
print(json.dumps({'restart':restart,'aggregate':class_summary,'process_records':len(process)},sort_keys=True))
