#!/usr/bin/env python3
"""Cross-check the Round108 verdict against retained primary evidence."""
from pathlib import Path
import argparse, hashlib, json, os

def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(8<<20),b''): h.update(b)
    return h.hexdigest()
def load(p): return json.loads(Path(p).read_text())
ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); ap.add_argument('--require-postpayload',action='store_true'); a=ap.parse_args(); r=a.root.resolve()
res=load(r/'RESULT.json')
assert res['status']=='PASS' and res['verdict']=='MATERIAL-CHECKED-CONTINUATION-NOT-CLOSED'
assert res['root_closed'] is False and res['canonical_state_modified'] is False
assert res['root_branches']=={'A_explicit_legal_distance_12_circuit':False,'B_universal_frozen_family_distance_at_most_11':False}
assert res['distance_status']=={'CIRCDIST.gross':'CONJECTURED','D_star_Gross':[11,12],'gap-via-lift':'CONJECTURED'}
assert res['iteration189']['repair_entered'] is False and res['iteration189']['distance12_result'] is False
for p in ('solver/iter189/assignment_check.json','solver/iter189/direct/solver/Xerr.assignment_check.json','solver/iter189/direct/solver/Zerr.assignment_check.json'):
    x=load(r/p); assert x['status']=='PASS' and x['solver_status']=='SATISFIABLE' and x['all_dimacs_clauses_satisfied'] and x['all_variables_assigned_exactly_once']
d=load(r/'verification/iter189_direct_independent_audit.json'); assert d['status']=='PASS'
for sec in ('Xerr','Zerr'):
    x=d['sectors'][sec]; assert x['status']=='SATISFIABLE' and x['fault_count']==10 and x['canonical_syndrome']==[] and x['physical_syndrome']==[] and x['canonical_nonstabilizer'] and x['physical_nonstabilizer']
state=load(r/'frontier/iter190_full_invariant/state.json'); assert state['next_iteration']==190 and state['started'] is False and state['stop'] is None and state['selector_count']==24444 and state['block_count']==517140
base=load(r/'frontier/iter190_full_invariant/formula/metadata.json'); q=load(r/'frontier/iter190_full_invariant_quotient/metadata.json')
assert (base['variables'],base['clauses'],base['assertions'],base['cnf_sha256'])==(1850757,6920296,545982,'e3ec0d0b146fc4ade428052d1a14737ffade9974dfc37dd79fa8411841d45fc8')
assert (q['variables'],q['clauses'],q['assertions'],q['cnf_sha256'])==(2464197,11827887,546053,'12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767')
assert sha(r/'frontier/iter190_full_invariant/formula/outer.cnf')==base['cnf_sha256'] and sha(r/'frontier/iter190_full_invariant_quotient/outer.cnf')==q['cnf_sha256']
assert {p.name for p in (r/'frontier/iter190_full_invariant/formula').iterdir()}=={'assertion_map.jsonl','definitions.json.gz','encoding_check.json','metadata.json','outer.cnf'}
assert {p.name for p in (r/'frontier/iter190_full_invariant_quotient').iterdir()}=={'independent_check.json','metadata.json','outer.cnf','translation_roots.jsonl','translation_trace.json.gz'}
assert load(r/'verification/iter190_incremental_orbit_closure_independent.json')['status']=='PASS'
assert load(r/'verification/iter189_sat_trace_streams.json')['certificate_claim'] is None
proof=load(r/'verification/proof_controls.json'); assert proof['status']=='PASS' and len(proof['runs'])==6 and all(x['reaped'] and not x['detached'] and not x['timed_out'] for x in proof['runs'])
pre=load(r/'verification/preseal_replay.json'); assert pre['status']=='PASS' and pre['direct_child_count']==18 and pre['all_children_reaped'] and pre['strict_child_nonoverlap']
assert load(r/'verification/repository_validators/summary.json')['status']=='PASS'
ledger_path=r/'PROCESS_FIX2_LEDGER.json'
if ledger_path.exists(): assert load(ledger_path)['status']=='PASS'
if a.require_postpayload:
    post=load(r/'verification/postseal_replay.json'); assert post['status']=='PASS' and post['direct_child_count']==18 and post['all_children_reaped'] and post['strict_child_nonoverlap']
    assert res['verification']['postpayload_package_replay']=='PASS'
assert sha(r/'PROPOSED_CIRCDIST.gross.yaml')==sha(r/'bindings/CIRCDIST.gross.yaml')=='8b805a806d5b704047f4ccca648c92efe11740d7c5b7825659eb1e6b7b5dc977'
assert os.access(r/'replay.sh',os.X_OK)
assert not [p for p in r.rglob('*') if p.is_symlink()]
for n in ('REPORT.md','RESULT.json','THEOREM_NOTES.md','FAILURE_LEDGER.md','FRESH_FRONTIER.json','INPUT_BINDINGS.json','ENVIRONMENT.json','PROPOSED_CANONICAL_DELTA.md','BOOTSTRAP_COMMAND.txt'):
    assert (r/n).is_file() and (r/n).stat().st_size>0
out={'schema':'circdist-gross-round108-result-consistency-check-v1','status':'PASS','verdict':res['verdict'],'root_closed':False,'solver_statuses':{'outer':'SATISFIABLE','Xerr':'SATISFIABLE','Zerr':'SATISFIABLE'},'fresh_iteration':190,'fresh_quotient_sha256':q['cnf_sha256'],'fresh_quotient_solved':False,'canonical_yaml_unchanged':True,'symlink_count':0,'postpayload_required':a.require_postpayload}
a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
