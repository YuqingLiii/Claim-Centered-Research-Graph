#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse, collections, gzip, hashlib, json, shutil

ap = argparse.ArgumentParser()
ap.add_argument('--root', type=Path, required=True)
ap.add_argument('--scratch', type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve(); S = a.scratch.resolve()

def canon(o): return json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
def sem(o): return hashlib.sha256(canon(o)).hexdigest()
def fsha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
    p = Path(p)
    if not p.exists() and Path(str(p)+'.gz').exists(): p = Path(str(p)+'.gz')
    b = p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix == '.gz' else b)
def dump(rel, o):
    p = R/rel; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(o, indent=2, sort_keys=True)+'\n')

# Retain the exact reviewed iteration-78 raw state, plus the final iteration-90 bundle.
src_raw = load(R/'cross_registry/pre_outer_synthesis/raw_mechanisms_after.json')
assert src_raw['mechanism_count'] == 72 and sem(src_raw) == '864e151dde3451a63a30ff960a02826f8d6a752fd3a4383cfe266caec890a3ce'
dump('restart/full_raw_mechanisms_iteration78.json', src_raw)
for src, dst in [
    ('cegar/dynamic_blocks.json', 'restart/dynamic_blocks_iteration90.json'),
    ('classification/installed_generalized_terms.json', 'restart/installed_generalized_terms_iteration90.json'),
    ('classification/online_mechanism_registry.json', 'restart/online_mechanism_registry_iteration90.json'),
    ('classification/full_raw_mechanisms.json', 'restart/full_raw_mechanisms_iteration90.json'),
]: shutil.copy2(R/src, R/dst)

pre = load(R/'cross_registry/pre_outer_synthesis/summary.json')
pre_install = load(R/'cross_registry/pre_outer_synthesis/install_result.json')
assert pre['status'] == 'PASS' and pre['retained_increment'] == 2826

outcomes=[]; chain=[]; online_summaries=[]; cross_summaries=[]
online_terms=[]; cross_terms=list(load(R/'cross_registry/pre_outer_synthesis/retained_terms.json')['terms'])
mechanisms=[]; formula=[]; processes=[]
previous = {
    'dynamic':'656be42225ee1fb1f51426eb5544208a6d58df8ef6a015d981561b8048d57082',
    'generalized':'420cb3ee23757d52f914e75dfe3c6de371a4702ef3205ee2401ec071069c5551',
    'registry':'bafc7e4c7fb5ebdd5d090790a603b1dc8c956e2260d1047c9f4b825478b103a9',
    'raw_mechanisms':'864e151dde3451a63a30ff960a02826f8d6a752fd3a4383cfe266caec890a3ce',
}
for i in range(78,90):
    d=R/'cegar'/f'iter{i}'
    o=load(d/'iteration_outcome.json'); c=load(d/'state_commit_complete.json')
    g=load(d/'generalization/summary.json'); x=load(d/'cross_registry/summary.json')
    dv=load(d/'direct_verification.json'); outer=load(d/'outer_result.json'); replay=load(d/'outer_independent_replay.json')
    assert o['iteration']==i and o['outer_status']=='SAT' and o['fresh_outer_process']
    assert all(o['all_dimacs_clauses_satisfied'].values()) and o['raw_replay_passed']
    assert c['status']=='PASS' and c['all_live_bindings_match'] and c['before_semantic_sha256']==previous
    assert g['status']=='PASS' and x['status']=='PASS'
    assert g['retained_increment']==o['online_generalized_retained_increment']
    assert x['retained_increment']==o['cross_registry_retained_increment']
    assert outer['status']=='SAT' and replay['status']=='PASS'
    assert all(dv['sectors'][s]['status']=='SATISFIABLE' and dv['sectors'][s]['all_dimacs_clauses_satisfied'] for s in ('Xerr','Zerr'))
    previous=dict(c['after_semantic_sha256'])
    outcomes.append(o); online_summaries.append(g); cross_summaries.append(x); processes.extend(o['process_records'])
    online_terms.extend(load(d/'generalization/retained_terms.json')['terms'])
    cross_terms.extend(load(d/'cross_registry/retained_terms.json')['terms'])
    mechanisms.extend(load(d/'generalization/mechanisms.json')['mechanisms'])
    formula.extend(load(d/'generalization/formula_raw_replay_bindings.json')['records'])
    chain.append({
        'iteration':i, 'candidate_sha256':o['candidate_sha256'], 'outer_status':'SAT',
        'before_counts':{'dynamic':o['dynamic_blocks_before'],'generalized':o['generalized_terms_before'],'registry':o['mechanism_registry_before'],'raw_mechanisms':o['raw_mechanisms_before'],'total_blocks':o['installed_blocks_before']},
        'increments':{'candidate_exact':2,'online_generalized':o['online_generalized_retained_increment'],'cross_registry':o['cross_registry_retained_increment']},
        'after_counts':{'dynamic':o['dynamic_blocks_after'],'generalized':o['generalized_terms_after'],'registry':o['mechanism_registry_after'],'raw_mechanisms':o['raw_mechanisms_after'],'total_blocks':o['installed_blocks_after']},
        'before_semantic_sha256':c['before_semantic_sha256'],'after_semantic_sha256':c['after_semantic_sha256'],
        'commit_complete_file_sha256':fsha(d/'state_commit_complete.json'),
        'direct_sector_statuses':o['sector_statuses'],'direct_fault_weights':o['sector_fault_weights'],
        'all_dimacs_clauses_satisfied':o['all_dimacs_clauses_satisfied'],'state_bundle_commit':'PASS'
    })

assert len(outcomes)==12 and len(mechanisms)==len(formula)==24
assert len(online_terms)==sum(x['retained_increment'] for x in online_summaries)==62
assert len(cross_terms)==pre['retained_increment']+sum(x['retained_increment'] for x in cross_summaries)==4790
assert previous == {
    'dynamic':'30227f09a28c318ea392ae0473cc7644c294ea02aac6007d30eaddd1884ee348',
    'generalized':'ba4e37e48c856f8966fd86540daab423468c551289856517aacc35cc1403c8f3',
    'registry':'6663a3a3036199de684255c622690ebf00e02b7e5fd0249af6bbafcfece42cdd',
    'raw_mechanisms':'6746258d7e045c211596ec264a1bcf9a748357e6b7a8f76008e532e189179f1f',
}

def sum_fields(rows, names): return {k:sum(int(r.get(k,0)) for r in rows) for k in names}
online_fields=['participating_catalogs','local_order_records','structural_pair_relations','structural_pair_cells_represented','positive_pair_relations','positive_pair_configurations','positive_pair_cells','positive_finder_misses','multi_check_exact_relations','pair_terms_generated','multi_check_terms_generated','raw_term_candidates','covered_by_full_evolving_union','retained_increment','literal_retained_tuple_replays','factorized_symbolically_proved_tuples','pair_domain_library_relative_new_tuples','multi_union_membership_class_checks','zero_domain_candidates_rejected']
cross_fields=['catalogs','local_order_records','unique_residual_options','structural_check_pairs','distinct_check_option_pair_attempts','positive_configurations','cross_candidate_positive_configurations','positive_pair_relations','pair_truth_cells','explicit_positive_pair_cells','raw_candidates','eligible_multi_selector_pairs','retained_increment','literal_pair_tuples_replayed','factorized_multi_tuples_proved']
online_agg=sum_fields(online_summaries,online_fields)
cross_all=[pre]+cross_summaries; cross_agg=sum_fields(cross_all,cross_fields)

cegar_summary={
    'schema':'round78-cross-registry-cegar-summary-v1','status':'PASS','iteration_range':[78,89],
    'completed_dual_sector_candidates':12,'outer_verdicts':{'SAT':12,'UNSAT':0,'UNKNOWN':0,'TIMEOUT':0},
    'direct_sector_verdicts':{'SATISFIABLE':24,'UNSAT_PROOFS_ACCEPTED':0,'UNKNOWN_OR_TIMEOUT':0},
    'fresh_outer_processes':12,'assignment_clause_replays':24,'raw_canonical_physical_replays':24,
    'candidate_exact_blocks_added':24,'online_generalized_terms_added':62,'post_outer_cross_registry_terms_added':1964,
    'accepted_absence_proofs':0,'repair_entered':False,'branch_closed':False,'root_closed':False,
    'outer_solve_seconds_total':sum(float(x['outer_seconds']) for x in outcomes),
    'sector_fault_weight_histogram':dict(sorted(collections.Counter(str(w) for o in outcomes for w in o['sector_fault_weights'].values()).items())),
    'iterations':chain,
    'restart':{'next_iteration':90,'base_blocks':1460,'generalized_blocks':10595,'dynamic_blocks':180,'registry_mechanisms':96,'raw_mechanisms':96,'next_outer_total_blocks':12235,
               'dynamic_state':'restart/dynamic_blocks_iteration90.json','generalized_state':'restart/installed_generalized_terms_iteration90.json','registry_state':'restart/online_mechanism_registry_iteration90.json','raw_mechanisms_state':'restart/full_raw_mechanisms_iteration90.json'}
}
dump('cegar/summary.json',cegar_summary); dump('cegar/iteration_state_chain.json',{'schema':'round78-state-chain-v1','status':'PASS','pre_outer_transition':'cross_registry/pre_outer_synthesis_transition.json','iterations':chain,'next_iteration':90,'final_semantic_sha256':previous})

classification_summary={
    'schema':'round78-online-generalization-aggregate-summary-v1','status':'PASS','iteration_range':[78,89],
    'source_mechanisms':24,'formula_assignment_raw_replays':24,'candidate_exact_blocks_preserved':24,
    'reviewed_generalized_terms_at_start':5743,'pre_outer_cross_registry_terms':2826,'online_retained_terms':62,'post_outer_cross_registry_terms':1964,
    'round78_generalized_additions':4852,'final_installed_generalized_terms':10595,
    **online_agg,
    'retained_deletion_controls':sum(len(t.get('deletion_controls',[])) for t in online_terms),
    'retained_relation_kinds':dict(sorted(collections.Counter(t['relation_kind'] for t in online_terms).items())),
    'literal_plus_factorized_tuples':online_agg['literal_retained_tuple_replays']+online_agg['factorized_symbolically_proved_tuples'],
    'claim_scope':'constructive positive sound online generalization; no absence, completeness, exhaustion, repair, or D-star closure claim',
    'zero_truth_cells_used_as_absence':0,'positive_finder_misses_used_as_absence':0,'deletion_countertuples_used_as_absence':0
}
dump('classification/summary.json',classification_summary)
dump('classification/round78_online_retained_terms.json',{'schema':'round78-online-retained-terms-aggregate-v1','terms':online_terms})
dump('classification/round78_mechanisms.json',{'schema':'round78-source-mechanisms-aggregate-v1','mechanisms':mechanisms})
dump('classification/round78_formula_raw_replay_bindings.json',{'schema':'round78-formula-raw-replay-bindings-aggregate-v1','records':formula})

xsummary={
    'schema':'round78-cross-registry-aggregate-summary-v1','status':'PASS','batch_range':['pre78','post078..post089'],'batch_count':13,
    'source_registry_range':[72,96],'pre_outer_retained_terms':2826,'post_outer_retained_terms':1964,'retained_terms_total':4790,
    **cross_agg,
    'retained_deletion_controls':sum(len(t.get('deletion_controls',[])) for t in cross_terms),
    'retained_relation_kinds':dict(sorted(collections.Counter(t['relation_kind'] for t in cross_terms).items())),
    'pre_outer_state_transition':'cross_registry/pre_outer_synthesis_transition.json',
    'batches':[{'batch_id':x['batch_id'],'registry':x['registry_count_unchanged'],'raw_candidates':x['raw_candidates'],'retained':x['retained_increment'],'literal_pair_tuples':x['literal_pair_tuples_replayed'],'factorized_multi_tuples':x['factorized_multi_tuples_proved']} for x in cross_all],
    'claim_scope':'constructive cross-registry sound order regions; semantic dedup/dominance against each full evolving library; no absence, completeness, global minimality, repair, exhaustion, or D-star inference',
    'zero_cells_used_as_absence':0,'negative_completion_misses_used_as_absence':0,'deletion_countertuples_used_as_absence':0
}
dump('cross_registry/summary.json',xsummary)
dump('cross_registry/round78_cross_registry_retained_terms.json',{'schema':'round78-cross-registry-retained-terms-aggregate-v1','terms':cross_terms})

# Mechanism cover is a transparent occurrence ledger, not an absence or minimality statement.
cover=collections.defaultdict(set)
for t in online_terms+cross_terms:
    tid=t['term_id']
    for mid in t.get('source_mechanisms',t.get('seed_source_mechanisms',[])): cover[mid].add(tid)
rows=[]
for m in load(R/'classification/full_raw_mechanisms.json')['mechanisms']:
    ids=sorted(cover[m['mechanism_id']])
    rows.append({'mechanism_id':m['mechanism_id'],'iteration':m['iteration'],'sector':m['sector'],'candidate_exact_block_preserved':True,'retained_terms_naming_as_source':len(ids),'retained_term_ids':ids,'no_cover_is_not_absence':True})
dump('classification/source_mechanism_cover.json',{'schema':'round78-source-mechanism-cover-v1','status':'PASS','scope':'term provenance occurrence only; not installed-union necessity, minimality, or absence','mechanisms':rows})

restart_files={
 'dynamic':R/'restart/dynamic_blocks_iteration90.json','generalized':R/'restart/installed_generalized_terms_iteration90.json',
 'registry':R/'restart/online_mechanism_registry_iteration90.json','raw_mechanisms':R/'restart/full_raw_mechanisms_iteration90.json'}
restart={'schema':'round78-exact-restart-state-v1','status':'PASS','next_iteration':90,'started':False,'fresh_outer_process_required':True,'base_blocks':1460,
 'counts':{'dynamic':180,'generalized':10595,'registry':96,'raw_mechanisms':96,'total_blocks':12235},
 'states':{k:{'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'file_sha256':fsha(p),'semantic_sha256':sem(load(p))} for k,p in restart_files.items()},
 'semantic_sha256':previous,'branch_closed':False,'verdict':'MATERIAL-CHECKED-PROGRESS-NOT-CLOSED','fresh_independent_review_required':True}
assert {k:v['semantic_sha256'] for k,v in restart['states'].items()}==previous
dump('restart/restart_state.json',restart)

# Preserve all external development and driver logs before compression.
(R/'development').mkdir(exist_ok=True)
for p in sorted((S/'work').glob('pre78_synthesis*'))+sorted((S/'work').glob('iteration*.runner.*')):
    if p.is_file(): shutil.copy2(p,R/'development'/p.name)
for p in sorted((S/'preflight').iterdir()):
    if p.is_file():
        (R/'preflight').mkdir(exist_ok=True); shutil.copy2(p,R/'preflight'/p.name)

attempts=[
 {'attempt':'v1','disposition':'INTERRUPTED_NO_STATE_MUTATION','wall_seconds':508.46,'maximum_resident_set_bytes':17801838592,'peak_memory_footprint_bytes':40066248976,'cause':'naive full vector DP memory growth; KeyboardInterrupt'},
 {'attempt':'v2','disposition':'INTERRUPTED_NO_STATE_MUTATION','wall_seconds':292.84,'maximum_resident_set_bytes':9262628864,'peak_memory_footprint_bytes':9258146584,'cause':'full terminal DP remained memory-growing; interrupted below renewed hard ceiling'},
 {'attempt':'v3','disposition':'INTERRUPTED_NO_STATE_MUTATION','wall_seconds':377.95,'maximum_resident_set_bytes':20533542912,'peak_memory_footprint_bytes':35033834240,'cause':'broader eight-pair MITM exceeded memory guard; SIGINT/SIGTERM'},
 {'attempt':'v4','disposition':'INTERRUPTED_NO_STATE_MUTATION','wall_seconds':715.44,'maximum_resident_set_bytes':1073250304,'peak_memory_footprint_bytes':1069401120,'cause':'safe two-pair design but repeated RREF made literal replay too slow'},
 {'attempt':'v5','disposition':'ASSERTION_FAILURE_NO_STATE_MUTATION','wall_seconds':149.72,'maximum_resident_set_bytes':1073479680,'peak_memory_footprint_bytes':1069630496,'cause':'validation assumed every candidate added tuples beyond old union; counterexample was already covered by evolving installed union'},
 {'attempt':'v6','disposition':'TEMPORARY_STAGING_MUTATION_ROLLED_BACK_BEFORE_OUTER','wall_seconds':194.60,'maximum_resident_set_bytes':2129215488,'peak_memory_footprint_bytes':2122991392,'cause':'post-run audit found three retained multi terms with zero tuple domain caused by contradictory local atoms','temporary_generalized_count':8572,'temporary_generalized_semantic_sha256':'e26c650f41a653774305a17871670a32cd7481115ffd589d74025ed9cc73aa7f','rollback':{'dynamic':'656be42225ee1fb1f51426eb5544208a6d58df8ef6a015d981561b8048d57082','generalized':'031794ebbcad05fc81e1f028a7e4833ced91779c44c888b98db73f4ebd20c3cd','registry':'bafc7e4c7fb5ebdd5d090790a603b1dc8c956e2260d1047c9f4b825478b103a9','raw_mechanisms':'864e151dde3451a63a30ff960a02826f8d6a752fd3a4383cfe266caec890a3ce'},'canonical_repository_mutated':False},
 {'attempt':'v7','disposition':'ACCEPTED_PASS','wall_seconds':148.11,'maximum_resident_set_bytes':2111930368,'peak_memory_footprint_bytes':2105722680,'corrections':['reject exact DP domains with total==0','minimizer cannot seed from empty/unsound region','reject zero local order masks','use memoized physical validation and full evolving union'],'retained_terms':2826,'literal_pair_tuples':25685232,'generalized_after_semantic_sha256':'420cb3ee23757d52f914e75dfe3c6de371a4702ef3205ee2401ec071069c5551'}]
dump('PROCESS_LEDGER.json',{'schema':'round78-process-ledger-v1','status':'PASS','strict_serial_execution':True,'concurrent_load_bearing_processes':0,'development_attempts':attempts,'accepted_cegar_process_records':processes,'accepted_cegar_process_count':len(processes),'accepted_iterations':12,'timeouts':0,'unknowns':0,'signals_in_accepted_computation':0,'canonical_repository_mutated':False,'source_package_mutated':False,'scratch_cleanup_required_before_completion':True})

result={'schema':'circdist-gross-cross-registry-round78-result-v1','status':'PASS','verdict':'MATERIAL-CHECKED-PROGRESS-NOT-CLOSED','branch_closed':False,
 'source_reviewed_restart':{'iteration':78,'dynamic':156,'generalized':5743,'registry':72,'total_blocks':7359},
 'pre_outer_cross_registry':{'retained':2826,'generalized_after':8569,'total_blocks_first_outer':10185},
 'cegar':{'iterations':[78,89],'fully_closed_candidates':12,'direct_sectors':24,'candidate_exact_blocks':24,'online_retained':62,'post_cross_registry_retained':1964},
 'final':{'next_iteration':90,'dynamic':180,'generalized':10595,'registry':96,'raw_mechanisms':96,'total_blocks':12235,'semantic_sha256':previous},
 'validation_domains':{'cross_registry_literal_pair_tuples':cross_agg['literal_pair_tuples_replayed'],'online_literal_tuples':online_agg['literal_retained_tuple_replays'],'online_factorized_multi_tuples':online_agg['factorized_symbolically_proved_tuples'],'total_literal_tuples':cross_agg['literal_pair_tuples_replayed']+online_agg['literal_retained_tuple_replays']},
 'accepted_gross_unsat_proofs':0,'accepted_outer_unsat_proofs':0,'repair_entered':False,'D_star_Gross_remaining_set':[11,12],
 'fresh_independent_review_required':True,'restart':'restart/restart_state.json'}
dump('RESULT.json',result)
print(json.dumps({'status':'PASS','online_terms':len(online_terms),'cross_terms':len(cross_terms),'mechanisms':len(mechanisms),'processes':len(processes),'restart':restart['counts'],'final_hashes':previous},sort_keys=True))
