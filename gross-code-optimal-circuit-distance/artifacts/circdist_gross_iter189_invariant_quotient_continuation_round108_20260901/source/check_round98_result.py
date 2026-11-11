#!/usr/bin/env python3
"""Cross-check the Round98 result against the independent audit and exact order-5 object."""
from pathlib import Path
import argparse,hashlib,json
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);a=p.parse_args();R=a.root.resolve()
x=json.loads((R/'RESULT.json').read_text());u=json.loads((R/'verification/dispatcher_independent_campaign_audit.json').read_text());s=json.loads((R/'synthesis/order5_gf2_closure.json').read_text())
assert x['status']==u['status']==s['status']=='PASS' and x['verdict']==u['scientific_verdict']=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED'
assert x['root_status']==x['route_status']=='CONJECTURED' and x['D_star_Gross']==[11,12]
assert x['completed_candidate_count']==u['completed_candidate_count']==12 and x['outer_sat_count']==12 and x['direct_sat_count']==24
assert x['unsat_count']==x['unknown_count']==x['timeout_count']==0 and x['repair_entered'] is False
assert x['synthesis']['finite_domain_size']==u['synthesis']['finite_domain_size']==s['finite_domain']['unordered_distinct_quintuples_enumerated']==351359546
assert x['synthesis']['unique_eligible_results']==u['synthesis']['unique_eligible_results']==40153 and s['potentially_valid_witness_count']==s['retained_term_count']==0
assert x['iterations']==u['iterations']
f=x['fresh_state'];assert f==u['fresh_frontier'] and f['next_iteration']==172 and f['selector_count']==304 and f['started'] is False
assert sha(R/'state/iter172_state.json')==f['state_file_sha256']=='9fd675be9712a28dd625fba7cce95f75a8a3b9bdf7edc3f398bfa8b13844d2be'
assert f['cnf_sha256']=='f86b8db36af1df3877ca1d9dbafb171b6173ddc8b6c2f045a808dd6c71f98342' and (f['assertions'],f['variables'],f['clauses'])==(19186,413646,1406245)
assert not (R/'iterations/iter172').exists()
print('ROUND98_RESULT_CROSSCHECK_PASS',len(x['iterations']),f['selector_count'])
