#!/usr/bin/env python3
from pathlib import Path
import argparse,gzip,hashlib,json
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();x=json.loads((R/'RESULT.json').read_text());audit=json.loads((R/'verification/independent_campaign_audit.json').read_text());state=json.loads((R/'state/iter184_state.json').read_text())
assert x['status']=='PASS' and x['scientific_verdict']=='MATERIAL-CHECKED-PROGRESS-NOT-CLOSED' and x['D_star_Gross']==[11,12]
assert x['root_status']==x['route_status']=='CONJECTURED' and not any(x['closure'].values())
assert x['campaign']=={'iterations':[172,183],'completed_candidates':12,'outer_sat':12,'direct_sat':24,'outer_unsat':0,'direct_unsat':0,'unknown':0,'timeouts':0,'repair_entered':False,'selector_appends':24,'atomic_transitions':12}
assert x['fresh_frontier']==audit['fresh_frontier'] and state['next_iteration']==184 and not state['started'] and state['stop'] is None and state['selector_count']==328 and not (R/'iterations/iter184').exists()
assert x['synthesis']['order6']['full_domain']==6715648864 and x['synthesis']['order6']['combined_zero_candidates']==0 and not x['synthesis']['order6']['sampling']
assert x['synthesis']['full_span']['status']=='CHECKED_UNSAT_BOTH_SECTORS' and x['proof_counts']['synthesis_unsat_certificates']==2 and x['proof_counts']['outer_unsat_certificates']==x['proof_counts']['direct_unsat_certificates']==0
assert x['synthesis']['mixed_sector']['new_closure_beyond_components'] is False and x['canonical_files_modified'] is False and x['status_promotion_requested'] is False
f=json.loads((R/'FAILURE_LEDGER.json').read_text());assert f['failure_count']==x['failure_count']==12 and f['round98_disclosure']['events']==3 and not f['round98_disclosure']['inherited_as_round100_failures']
for name in ('REPORT.md','SYNTHESIS_PROOF.md','MATHEMATICAL_SCOPE_AND_SOUNDNESS.md','PROPOSED_CANONICAL_DELTA.md','INPUT_BINDINGS.json','PROCESS_LEDGER.json'):assert (R/name).is_file() and (R/name).stat().st_size>0
print(json.dumps({'status':'PASS','verdict':x['scientific_verdict'],'D_star_Gross':x['D_star_Gross'],'outer_sat':12,'direct_sat':24,'synthesis_unsat':2,'fresh_iteration':184},sort_keys=True))
