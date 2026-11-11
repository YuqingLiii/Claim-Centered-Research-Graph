#!/usr/bin/env python3
"""Cross-check Round92 RESULT.json against sealed evidence objects."""
from pathlib import Path
import argparse,gzip,hashlib,json

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def sho(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()

ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();x=load(R/'RESULT.json')
assert x['status']=='PASS' and x['verdict']=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED'
assert x['root_status']==x['route_status']=='CONJECTURED' and x['D_star_Gross']==[11,12]
assert x['completed_candidate_count']==12 and x['strict_serial']
assert x['all_outer_dispositions']==x['all_direct_dispositions']=='SATISFIABLE'
assert x['unknown_count']==x['timeout_count']==x['unsat_count']==0 and not x['repair_entered']
assert not x['canonical_edits'] and not x['commit'] and not x['push']
syn=load(R/'synthesis/weight9_synthesis.json');pa=x['phase_a']
assert sha(R/'synthesis/weight9_synthesis.json')==pa['synthesis_file_sha256']
assert syn['semantic_result_sha256']==pa['semantic_result_sha256'] and syn['retained_ordinary_selector_count']==44
assert syn['retained_relaxed_cube_count']==0 and pa['retained_ordinary_selector_count']==44
sv=load(R/'preouter/strict_expansion.verification.json');assert sv['status']=='PASS' and sv['all_dimacs_clauses_satisfied']
assert sv['old_valid_count']==0 and sv['new_valid_count']==1 and sv['strict_old_union_expansion_witness']
tr=load(R/'data/sat_drat_trace_disposition.json');assert tr['status']=='PASS' and tr['trace_count']==36
ti={(q['iteration'],q['query']):q for q in tr['traces']};assert len(ti)==36 and all(q['empty_clause_lines']==0 for q in tr['traces'])
assert len(x['iterations'])==12
for i,row in zip(range(124,136),x['iterations']):
    assert row['iteration']==i;F=R/f'formulas/iter{i}';E=R/f'iterations/iter{i}';M=load(F/'metadata.json');S=load(F/'source.json.gz')
    semantic=dict(S);recorded=semantic.pop('semantic_payload_sha256');assert sho(semantic)==recorded==row['source_semantic_sha256']
    assert sha(F/'source.json.gz')==row['source_file_sha256'] and M['selector_count']==row['source_selector_count']
    o=row['outer'];assert o['status']=='SATISFIABLE' and o['solver_returncode']==10 and o['all_dimacs_clauses_satisfied']
    for k in ('assertions','variables','clauses','cnf_sha256'):assert o[k]==M[k]
    assert hashlib.sha256(gzip.decompress((F/'outer.cnf.gz').read_bytes())).hexdigest()==o['cnf_sha256']
    assert sha(E/'outer/assignment.dimacs.gz')==o['assignment_sha256']
    assert hashlib.sha256(gzip.decompress((E/'outer/assignment.dimacs.gz').read_bytes())).hexdigest()==o['uncompressed_assignment_sha256']
    assert sha(E/'outer/solver.log')==o['solver_log_sha256'] and sha(E/'outer/candidate.json')==o['candidate_file_sha256']
    C=load(E/'outer/candidate.json');assert C['compressed_schedule_sha256']==o['schedule_sha256']
    A=C['frozen_audit'];assert A['ok'] and A['global_interleaved'] and A['edge_count']==864 and A['overlaps']==648 and not A['conflicts']
    rec=load(E/'record.json');assert rec['state_mutated_atomically'] and rec['state_after_sha256']==row['state_after_sha256'] and not rec['repair_entered']
    D=load(E/'direct/direct_verification.json');assert sha(E/'direct/direct_verification.json')==row['direct_verification_file_sha256'] and not D['repair_gate']['entered']
    for sec in ('Xerr','Zerr'):
        d=row['direct'][sec];z=D['sectors'][sec];m=z['mechanism'];summ=load(E/f'direct/direct360/{sec}.summary.json')
        assert d['status']==z['status']=='SATISFIABLE' and d['solver_returncode']==10 and z['all_dimacs_clauses_satisfied']
        assert d['complete_query'] and summ['complete_query'] and summ['excluded_restrictions']==['no pool restriction','no residual-pattern restriction','no check-count restriction','no within-check order family restriction']
        assert sha(E/f'direct/direct360/{sec}.cnf')==d['cnf_sha256']==summ['dimacs_sha256']
        assert sha(E/f'direct/solver/{sec}.solver.log')==d['solver_log_sha256']
        assert m['fault_count']==d['weight'] and 1<=d['weight']<=10 and m['physical_syndrome']==[] and m['physical_nontrivial'] and m['canonical_physical_parities_equal']
        assert sho(m)==d['mechanism_semantic_sha256'] and ti[(i,sec)]==d['sat_drat_trace']
    assert ti[(i,'outer')]==o['sat_drat_trace']
fresh=x['fresh_state'];assert fresh['next_iteration']==136 and not fresh['started'] and fresh['selector_count']==232
assert fresh['selector_state_sha256']=='1692d905120d2dcf51b949ce4a70ed4b8f1b270c2d07a1ddbf5813d20d80fa81'
assert sha(R/'continuation/final_state.json')==fresh['state_file_sha256'] and not (R/'iterations/iter136').exists()
assert x['proof_objects']['gross_unsat_drat'] is None and x['proof_objects']['gross_unsat_lrat'] is None and x['proof_objects']['direct_unsat_proofs']==[]
print('ROUND92_RESULT_CROSSCHECK_PASS',len(x['iterations']),len(tr['traces']))

