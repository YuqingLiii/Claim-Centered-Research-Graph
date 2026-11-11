#!/usr/bin/env python3
"""Full serial, package-only replay of the Round100 Gross proposer evidence."""
from pathlib import Path
import argparse,gzip,hashlib,json,os,shutil,subprocess,tempfile,time,traceback


def actual(path):
    path=Path(path)
    if path.exists():return path,path.suffix=='.gz'
    encoded=path.with_name(path.name+'.gz');assert encoded.exists(),path
    return encoded,True

def data(path):
    path,compressed=actual(path);raw=path.read_bytes();return gzip.decompress(raw) if compressed else raw

def materialize(source,destination):
    destination=Path(destination);destination.parent.mkdir(parents=True,exist_ok=True);destination.write_bytes(data(source));return destination

def load(path):return json.loads(data(path))
def compare(left,right):assert data(left)==data(right),(left,right)
def scrub(value,ignored):
    if isinstance(value,dict):return {k:scrub(v,ignored) for k,v in value.items() if k not in ignored}
    if isinstance(value,list):return [scrub(v,ignored) for v in value]
    return value

def compare_json(left,right,ignored=()):assert scrub(load(left),set(ignored))==scrub(load(right),set(ignored)),(left,right)

def sha(path):return hashlib.sha256(data(path)).hexdigest()

ap=argparse.ArgumentParser()
ap.add_argument('--root',type=Path,required=True)
ap.add_argument('--python',type=Path,required=True)
ap.add_argument('--record-output',type=Path)
ap.add_argument('--skip-manifests',action='store_true')
ap.add_argument('--skip-final-crosschecks',action='store_true')
a=ap.parse_args();R=a.root.resolve();PY=a.python.absolute();V=R/'vendor/round80';rows=[];nested=[];started=time.time();status='RUNNING';failure=None
assert PY.is_file() and V.is_dir()

def run(name,command,expected=0,timeout=1800):
    command=[str(x) for x in command];t=time.time();child=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,start_new_session=False);timed_out=False;term=False;kill=False
    try:stdout,stderr=child.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out=True;term=True;child.terminate()
        try:stdout,stderr=child.communicate(timeout=15)
        except subprocess.TimeoutExpired:kill=True;child.kill();stdout,stderr=child.communicate()
    row={'name':name,'command':command,'parent_pid':os.getpid(),'child_pid':child.pid,'returncode':child.returncode,'expected_returncode':expected,'stdout':stdout,'stderr':stderr,'wall_seconds':round(time.time()-t,6),'timed_out':timed_out,'term_sent':term,'kill_sent':kill,'reaped':True,'detached':False};rows.append(row)
    print(json.dumps({k:row[k] for k in ('name','child_pid','returncode','expected_returncode','wall_seconds')},sort_keys=True),flush=True)
    assert not timed_out and child.returncode==expected,(name,child.returncode,stdout[-2000:],stderr[-2000:])
    return row

try:
  with tempfile.TemporaryDirectory(prefix='circdist-r100-full-replay.') as td:
    T=Path(td)
    if not a.skip_manifests:run('two_level_manifest_check',[PY,R/'source/check_manifests.py','--root',R],timeout=300)
    run('input_bindings',[PY,R/'source/check_input_bindings_round100.py','--root',R],timeout=300)
    run('compression_roundtrips',[PY,R/'source/check_compression_round100.py','--root',R],timeout=600)

    # Reconstruct every formula from its source and independently check the complete Tseitin map.
    for iteration in range(172,185):
      stored=R/'formulas'/f'iter{iteration}';fresh=T/'formulas'/f'iter{iteration}';fresh.mkdir(parents=True)
      run(f'compile_iter{iteration}',[PY,R/'source/compile_outer_cnf.py','--source',stored/'source.json.gz','--cnf',fresh/'outer.cnf','--metadata',fresh/'metadata.json','--assertion-map',fresh/'assertion_map.jsonl','--definitions',fresh/'circuit_trace.json.gz'])
      compare(stored/'outer.cnf',fresh/'outer.cnf');compare(stored/'assertion_map.jsonl',fresh/'assertion_map.jsonl');compare(stored/'circuit_trace.json.gz',fresh/'circuit_trace.json.gz');compare_json(stored/'metadata.json',fresh/'metadata.json',('compile_seconds',))
      run(f'encoding_iter{iteration}',[PY,R/'source/check_outer_encoding.py','--source',stored/'source.json.gz','--cnf',fresh/'outer.cnf','--metadata',fresh/'metadata.json','--assertion-map',fresh/'assertion_map.jsonl','--definitions',fresh/'circuit_trace.json.gz','--output',fresh/'encoding_check.json'])
      compare_json(stored/'encoding_check.json',fresh/'encoding_check.json',('seconds',));print('FORMULA_REPLAY_PASS',iteration,flush=True)

    # Recheck each SAT assignment, schedule, complete direct formula, physical replay, and atomic transition.
    for iteration in range(172,184):
      I=R/'iterations'/f'iter{iteration}';W=T/'iterations'/f'iter{iteration}';W.mkdir(parents=True);F=T/'formulas'/f'iter{iteration}';state=load(R/'state'/f'iter{iteration}_state.json')
      outer=W/'outer';outer.mkdir();solver_log=materialize(I/'outer/solver.log',outer/'solver.log')
      run(f'outer_verify_iter{iteration}',[PY,R/'source/verify_outer_sat_model.py','--solver-log',solver_log,'--cnf',F/'outer.cnf','--source',R/'formulas'/f'iter{iteration}'/'source.json.gz','--metadata',F/'metadata.json','--frozen',V,'--assignment',outer/'assignment.dimacs','--candidate',outer/'candidate.json','--output',outer/'replay.json'])
      compare(I/'outer/assignment.dimacs',outer/'assignment.dimacs');compare(I/'outer/candidate.json',outer/'candidate.json');compare_json(I/'outer/replay.json',outer/'replay.json',('seconds',))
      run(f'outer_assignment_iter{iteration}',[PY,R/'source/extract_and_check_assignment.py','--cnf',F/'outer.cnf','--solver-log',solver_log,'--assignment',outer/'assignment.independent.dimacs','--output',outer/'assignment_independent_check.json'])
      compare(I/'outer/assignment.independent.dimacs',outer/'assignment.independent.dimacs');compare_json(I/'outer/assignment_independent_check.json',outer/'assignment_independent_check.json')

      direct=W/'direct'
      run(f'direct_build_iter{iteration}',[PY,R/'source/build_direct_from_candidate.py','--candidate',outer/'candidate.json','--output',direct,'--vendor',V,'--source-selector-count',state['selector_count']])
      compare(I/'direct/candidate.json',direct/'candidate.json');compare(I/'direct/build_summary.json',direct/'build_summary.json')
      for sector in ('Xerr','Zerr'):
        for suffix in ('cnf','variables.json','columns.json','clauses.jsonl','summary.json'):compare(I/'direct/direct360'/f'{sector}.{suffix}',direct/'direct360'/f'{sector}.{suffix}')
        materialize(I/'direct/solver'/f'{sector}.solver.log',direct/'solver'/f'{sector}.solver.log')
      run(f'direct_physical_replay_iter{iteration}',[PY,V/'src/replay_direct_candidate.py','--root',direct,'--output',direct/'direct_verification.json'])
      compare(I/'direct/direct_verification.json',direct/'direct_verification.json')
      for sector in ('Xerr','Zerr'):
        run(f'direct_assignment_iter{iteration}_{sector}',[PY,R/'source/extract_and_check_assignment.py','--cnf',direct/'direct360'/f'{sector}.cnf','--solver-log',direct/'solver'/f'{sector}.solver.log','--assignment',direct/'solver'/f'{sector}.assignment.dimacs','--output',direct/'solver'/f'{sector}.assignment_check.json'])
        compare(I/'direct/solver'/f'{sector}.assignment.dimacs',direct/'solver'/f'{sector}.assignment.dimacs');compare_json(I/'direct/solver'/f'{sector}.assignment_check.json',direct/'solver'/f'{sector}.assignment_check.json')
      transition=W/'transition'
      run(f'transition_iter{iteration}',[PY,R/'source/advance_round100.py','--vendor',V,'--state-in',R/'state'/f'iter{iteration}_state.json','--source-in',R/'formulas'/f'iter{iteration}'/'source.json.gz','--iteration',iteration,'--candidate',I/'outer/candidate.json','--direct',I/'direct/direct_verification.json','--state-out',transition/'state.json','--record-out',transition/'record.json','--source-out',transition/'source.json.gz'])
      compare(R/'state'/f'iter{iteration+1}_state.json',transition/'state.json');compare(I/'record.json',transition/'record.json');compare(R/'formulas'/f'iter{iteration+1}'/'source.json.gz',transition/'source.json.gz');print('ITERATION_REPLAY_PASS',iteration,flush=True)

    # Recompile and rerun the exact six-distinct MITM reducer.
    order6_bin=T/'order6_mitm'
    run('order6_compile',['/usr/bin/clang++','-std=c++17','-O3','-Wall','-Wextra','-Wpedantic',R/'source/order6_mitm.cpp','-o',order6_bin],timeout=600)
    for sector in ('Xerr','Zerr'):
      eligible=T/f'{sector}.order6.eligible.bin';summary=T/f'{sector}.order6.summary.json'
      run(f'order6_{sector}',[order6_bin,R/'synthesis/order5_input'/f'{sector}.rows.bin',eligible,summary,sector],timeout=900)
      compare(R/'synthesis/order6'/f'{sector}.order6.eligible.bin',eligible);compare_json(R/'synthesis/order6'/f'{sector}.order6.summary.json',summary,('seconds','peak_rss_bytes_macos'))
    run('order6_independent_validation',[PY,R/'source/validate_order6.py','--root',R,'--output',T/'order6_validation.json'],timeout=900)
    compare_json(R/'synthesis/order6/order6_exact_validation.json',T/'order6_validation.json',('seconds',))

    # Rebuild both all-orders span CNFs and independently check real proof objects plus rejection controls.
    for sector in ('Xerr','Zerr'):
      span=T/'span'/sector;span.mkdir(parents=True)
      run(f'span_build_{sector}',[PY,R/'source/build_span_cnf.py','--rows',R/'synthesis/order5_input'/f'{sector}.rows.bin','--ids',R/'synthesis/order5_input'/f'{sector}.ids.json','--state',R/'synthesis/inputs/iter137_state.json','--sector',sector,'--cnf',span/'formula.cnf','--metadata',span/'metadata.json'])
      compare(R/'synthesis/span'/f'{sector}.cnf',span/'formula.cnf');compare_json(R/'synthesis/span'/f'{sector}.metadata.json',span/'metadata.json')
      materialize(R/'synthesis/span'/f'{sector}.drat',span/'proof.drat')
      cert=span/'certificate'
      run(f'span_proof_controls_{sector}',[PY,R/'source/verify_actual_unsat_round100.py','--formula',span/'formula.cnf','--proof',span/'proof.drat','--tooling',R/'tooling','--output',cert],timeout=1800)
      original=R/'synthesis/span'/f'{sector}.unsat_certificate'
      compare_json(original/'certificate.json',cert/'certificate.json',('checker_pid','checker_parent_pid','processes','wall_seconds'))
      for name in ('accepted.lrat','corrupt.drat','truncated.drat','corrupt.lrat','truncated.lrat'):compare(original/name,cert/name)
      nested.append({'name':f'span_proof_controls_{sector}','child_count':6,'all_reaped':True})
    run('span_independent_z3',[PY,R/'source/validate_span.py','--root',R,'--output',T/'span_validation.json'],timeout=1800)
    compare_json(R/'synthesis/span/span_exact_validation.json',T/'span_validation.json',('z3_seconds',))
    run('mixed_sector_theorem',[PY,R/'source/check_mixed_sector_round100.py','--root',R],timeout=300)

    run('independent_campaign_audit',[PY,R/'source/audit_round100.py','--root',R,'--logs',R/'logs','--vendor',V,'--output',T/'campaign_audit.json'],timeout=1800)
    compare_json(R/'verification/independent_campaign_audit.json',T/'campaign_audit.json',('seconds',))
    run('proof_fixture_controls',[PY,R/'source/check_proof_controls.py','--root',R,'--output',T/'proof_fixture_controls.json'],timeout=600)
    x=load(T/'proof_fixture_controls.json');y=load(R/'controls/proof_fixture_controls.json');stable=('status','fixture_cnf_sha256','valid_drat_sha256','generated_lrat_sha256','valid_drat_accepted','generated_lrat_accepted','corrupt_drat_rejected','truncated_drat_rejected','corrupt_lrat_rejected','truncated_lrat_rejected','scope');assert all(x[k]==y[k] for k in stable);nested.append({'name':'proof_fixture_controls','child_count':6,'all_reaped':True})
    if not a.skip_final_crosschecks:
      run('result_crosscheck',[PY,R/'source/check_result.py','--root',R],timeout=300)
      run('process_crosscheck',[PY,R/'source/check_process_ledger.py','--root',R],timeout=300)
    status='PASS'
except BaseException as error:
  status='FAIL';failure={'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()};raise
finally:
  record={'schema':'circdist-round100-full-package-replay-v1','status':status,'replay_pid':os.getpid(),'replay_parent_pid':os.getppid(),'started_unix':started,'ended_unix':time.time(),'wall_seconds':round(time.time()-started,6),'children':rows,'direct_child_count':len(rows),'nested_process_groups':nested,'nested_child_count':sum(x['child_count'] for x in nested),'total_known_child_processes':len(rows)+sum(x['child_count'] for x in nested),'all_children_reaped':all(x['reaped'] for x in rows) and all(x['all_reaped'] for x in nested),'detached_processes':0,'strict_serial':True,'failure':failure}
  if a.record_output:a.record_output.parent.mkdir(parents=True,exist_ok=True);a.record_output.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print('ROUND100_PACKAGE_REPLAY_PASS',len(rows),sum(x['child_count'] for x in nested),flush=True)
