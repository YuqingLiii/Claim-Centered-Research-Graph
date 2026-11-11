#!/usr/bin/env python3
"""Assemble the Round108 input, environment, fresh-frontier, and verdict metadata."""
from pathlib import Path
import argparse, datetime, hashlib, json, os, platform, shutil, sys

CHUNK = 8 << 20

def scan(path):
    h = hashlib.sha256(); size = lf = 0
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(CHUNK), b''):
            h.update(block); size += len(block); lf += block.count(b'\n')
    return h.hexdigest(), size, lf

def load(path): return json.loads(Path(path).read_text())
def dump(path, value): Path(path).write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', type=Path, required=True)
    ap.add_argument('--preseal-replay', type=Path, required=True)
    args = ap.parse_args(); root = args.root.resolve(); replay_path = args.preseal_replay.resolve()
    pre = load(replay_path)
    assert pre['status'] == 'PASS' and pre['direct_child_count'] == 18
    assert pre['strict_serial'] and pre['strict_child_nonoverlap'] and pre['all_children_reaped']
    assert pre['detached_processes'] == 0 and all(r['returncode'] == 0 and r['reaped'] and not r['timed_out'] and not r['detached'] for r in pre['children'])
    shutil.copyfile(replay_path, root / 'verification/preseal_replay.json')
    pre_sha, pre_bytes, pre_lf = scan(replay_path)
    dump(root / 'verification/preseal_replay_binding.json', {
        'schema':'circdist-gross-round108-preseal-replay-binding-v1','status':'PASS',
        'external_record':str(replay_path),'sha256':pre_sha,'bytes':pre_bytes,'lf':pre_lf,
        'direct_child_count':18,'strict_serial':True,'strict_child_nonoverlap':True,
        'all_children_reaped':True,'detached_processes':0})

    input_audit = load(root/'verification/input_audit.json')
    package_check = load(root/'verification/package_binding_check.json')
    qcheck = load(root/'solver/iter189/assignment_check.json')
    model = load(root/'solver/iter189/replay.json')
    direct = load(root/'verification/iter189_direct_independent_audit.json')
    traces = load(root/'verification/iter189_sat_trace_streams.json')
    orbit_controls = load(root/'verification/iter189_sat_orbit_controls.json')
    orbit = load(root/'frontier/iter190_full_invariant/orbit_audit.json')
    closure = load(root/'verification/iter190_incremental_orbit_closure_independent.json')
    state = load(root/'frontier/iter190_full_invariant/state.json')
    base = load(root/'frontier/iter190_full_invariant/formula/metadata.json')
    base_check = load(root/'frontier/iter190_full_invariant/formula/encoding_check.json')
    quotient = load(root/'frontier/iter190_full_invariant_quotient/metadata.json')
    quotient_check = load(root/'frontier/iter190_full_invariant_quotient/independent_check.json')
    proof = load(root/'verification/proof_controls.json')
    gates = load(root/'verification/repository_validators/summary.json')
    assert all(x['status']=='PASS' for x in (input_audit,package_check,qcheck,model,direct,traces,orbit_controls,orbit,closure,state,base,base_check,quotient,quotient_check,proof,gates))

    tooling=[]
    for name in ('cadical-1.9.5-arm64-macos','drat-trim-arm64-macos','lrat-check-arm64-macos'):
        p=root/'tooling'/name; digest,size,lf=scan(p)
        tooling.append({'path':f'tooling/{name}','sha256':digest,'bytes':size,'lf':lf,'executable':os.access(p,os.X_OK)})
    bindings={
        'schema':'circdist-gross-round108-input-bindings-v1','status':'PASS',
        'canonical':input_audit['canonical_bindings'],'reviewed_package':input_audit['reviewed_package'],
        'reviewed_frontier':input_audit['frontier'],'copied_input_files':input_audit['copied_input_files'],
        'package_binding_recheck':package_check,'tooling':tooling,'canonical_state_modified':False,
        'scope':'Round108 starts only from the reviewed fresh/unstarted iteration-189 full-invariant quotient in the sealed Round106 predecessor.',
        'immutable_start':{'iteration':189,'quotient_sha256':qcheck['formula_sha256'],'variables':qcheck['variables'],'clauses':qcheck['clauses'],'assertions':545909}}
    dump(root/'INPUT_BINDINGS.json',bindings)

    records=[]
    for folder in ('logs/process','verification/logs/process'):
        for p in sorted((root/folder).glob('*.json')):
            row=load(p)
            if row.get('schema')=='circdist-gross-round108-process-record-v1': records.append({'path':p.relative_to(root).as_posix(),**row})
    solvers=[]
    for row in records:
        cmd=row.get('command',[])
        if cmd and 'cadical' in Path(str(cmd[0])).name:
            solvers.append({k:row[k] for k in ('name','child_pid','command','started_unix','ended_unix','started_utc','ended_utc','wall_seconds','child_user_seconds','child_system_seconds','child_maxrss_raw','returncode','timed_out','reaped','detached')})
    solvers.sort(key=lambda x:x['started_unix'])
    assert len(solvers)==3 and [x['returncode'] for x in solvers]==[10,10,10]
    assert all(a['ended_unix'] <= b['started_unix'] for a,b in zip(solvers,solvers[1:]))
    env={
        'schema':'circdist-gross-round108-environment-v1','status':'PASS',
        'captured_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'cwd':os.getcwd(),'package':str(root),'network_used':False,
        'platform':platform.platform(),'machine':platform.machine(),'os':{'uname':list(platform.uname())},
        'python':{'executable':sys.executable,'version':platform.python_version(),'sha256':scan(sys.executable)[0]},
        'selected_environment':{k:os.environ[k] for k in ('PATH','PYTHONPATH','LANG','LC_ALL','LC_CTYPE','TMPDIR','SHELL') if k in os.environ},
        'tooling':tooling,'strict_serial':True,'subagents_used':False,
        'solver_processes':solvers,'solver_interval_count':3,'strict_solver_nonoverlap':True,
        'retained_process_records_seen':len(records)}
    dump(root/'ENVIRONMENT.json',env)

    base_allow=['assertion_map.jsonl','definitions.json.gz','encoding_check.json','metadata.json','outer.cnf']
    quotient_allow=['independent_check.json','metadata.json','outer.cnf','translation_roots.jsonl','translation_trace.json.gz']
    fresh={
        'schema':'circdist-gross-round108-fresh-frontier-v1','status':'PASS','iteration':190,
        'started':False,'stop':None,'fresh_unstarted':True,'blocks':517140,'selectors':24444,
        'lex_leaders':71,'translation_group':'Z_12 x Z_6','translation_group_order':72,
        'source_file_sha256':state['source_file_sha256'],
        'source_semantic_payload_sha256':state['source_semantic_payload_sha256'],
        'state_file_sha256':scan(root/'frontier/iter190_full_invariant/state.json')[0],
        'selector_state_sha256':state['selector_state_sha256'],
        'base':{'path':'frontier/iter190_full_invariant/formula/outer.cnf','assertions':base['assertions'],'variables':base['variables'],'clauses':base['clauses'],'sha256':base['cnf_sha256'],'encoding_check':'PASS'},
        'quotient':{'path':'frontier/iter190_full_invariant_quotient/outer.cnf','assertions':quotient['assertions'],'variables':quotient['variables'],'clauses':quotient['clauses'],'sha256':quotient['cnf_sha256'],'independent_check':'PASS'},
        'base_formula_exact_file_set':base_allow,'quotient_exact_file_set':quotient_allow,
        'forbidden_solver_artifacts_absent':True,'iter190_solved':False,
        'smallest_honest_residual':'Solve the exact fresh iteration-190 full-invariant quotient proof-first; retain its proof/model and repeat complete unrestricted direct-sector adjudication if SAT.'}
    assert set(p.name for p in (root/'frontier/iter190_full_invariant/formula').iterdir())==set(base_allow)
    assert set(p.name for p in (root/'frontier/iter190_full_invariant_quotient').iterdir())==set(quotient_allow)
    dump(root/'FRESH_FRONTIER.json',fresh)

    sectors={}
    for label in ('Xerr','Zerr'):
        d=direct['sectors'][label]
        sectors[label]={k:d[k] for k in ('status','variables','clauses','cnf_sha256','assignment_sha256','fault_count','selected_names','canonical_net_support','physical_net_support','canonical_syndrome','physical_syndrome','logical_parities','canonical_nonstabilizer','physical_nonstabilizer')}
    result={
        'schema':'circdist-gross-round108-result-v1','status':'PASS','verdict':'MATERIAL-CHECKED-CONTINUATION-NOT-CLOSED',
        'package':'circdist/artifacts/'+root.name,'canonical_state_modified':False,'strict_serial':True,
        'root_closed':False,'root_branches':{'A_explicit_legal_distance_12_circuit':False,'B_universal_frozen_family_distance_at_most_11':False},
        'distance_status':{'CIRCDIST.gross':'CONJECTURED','gap-via-lift':'CONJECTURED','D_star_Gross':[11,12]},
        'mandatory_input':{'iteration':189,'fresh_unstarted_before_launch':True,'quotient_sha256':qcheck['formula_sha256'],'variables':qcheck['variables'],'clauses':qcheck['clauses'],'assertions':545909},
        'iteration189':{
            'quotient':{'status':'SATISFIABLE','all_variables_assigned_exactly_once':True,'assigned_variables':qcheck['assigned_variables'],'all_clauses_checked':qcheck['checked_clauses'],'all_clauses_satisfied':True,'assignment_sha256':qcheck['assignment_sha256'],'solver_log_sha256':qcheck['solver_log_sha256']},
            'quotient_orbit_controls':orbit_controls,'schedule':model['frozen_schedule_audit'],
            'compressed_schedule_sha256':model['compressed_schedule_sha256'],'raw_schedule_sha256':model['raw_schedule_sha256'],
            'distance12_result':False,'repair_entered':False,
            'repair_reason':'forbidden after complete SAT adjudication; both unrestricted direct sectors are SAT','direct':sectors},
        'solver_processes':solvers,'sat_trace_streams':traces,
        'orbit_continuation':{'old_selectors':24300,'new_selectors':24444,'added_selectors':144,'parent_orbit_sizes':orbit['parent_orbit_sizes'],'collisions':orbit['collision_count'],'block_generator_cases':closure['block_registry']['generator_invariance_cases'],'selector_generator_cases':closure['selector_registry']['generator_invariance_cases'],'translated_schedule_replays':closure['translated_schedule_replays'],'translated_physical_mechanism_replays':closure['translated_physical_mechanism_replays'],'full_registry_invariant':True},
        'fresh_frontier':fresh,
        'proof_disposition':{'actual_Gross_UNSAT':False,'drat_or_lrat_claim_for_iteration189':False,'proof_output_enabled_from_all_solver_launches':True,'sat_streams_are_search_traces_not_certificates':True,'valid_corrupt_truncated_toolchain_controls':'PASS','nested_control_children':len(proof['runs']),'all_nested_control_children_reaped':all(r['reaped'] and not r['timed_out'] and not r['detached'] for r in proof['runs'])},
        'verification':{'input_binding_and_manifest_audit':'PASS','input_source_base_bijection':'PASS','input_registry_group_invariance':'PASS','input_quotient_reconstruction':'PASS','complete_quotient_assignment':'PASS','physical_schedule_replay':'PASS','independent_direct_audit':'PASS','fresh_registry_invariance':'PASS','fresh_base_encoding_check':'PASS','fresh_quotient_encoding_check':'PASS','sat_trace_roundtrip':'PASS','proof_controls':'PASS','preseal_package_replay':'PASS','preseal_replay_children':18,'postpayload_package_replay':'PENDING'},
        'preseal_replay_binding':load(root/'verification/preseal_replay_binding.json'),
        'repository_gates':gates,
        'failures':{'scientific_failures_or_unknowns':0,'development_and_interface_failures_disclosed':True,'ledger':'FAILURE_LEDGER.md'},
        'proposed_canonical_yaml':{'path':'PROPOSED_CIRCDIST.gross.yaml','sha256':scan(root/'PROPOSED_CIRCDIST.gross.yaml')[0],'installed':False,'identical_to_bound_canonical':scan(root/'PROPOSED_CIRCDIST.gross.yaml')[0]==scan(root/'bindings/CIRCDIST.gross.yaml')[0],'level':'CONJECTURED','residual':[11,12]},
        'exact_residual':fresh['smallest_honest_residual']}
    dump(root/'RESULT.json',result)
    print(json.dumps({'status':'PASS','process_records':len(records),'solvers':3,'fresh_iteration':190,'preseal_replay_sha256':pre_sha,'preseal_children':18},sort_keys=True))

if __name__=='__main__': main()
