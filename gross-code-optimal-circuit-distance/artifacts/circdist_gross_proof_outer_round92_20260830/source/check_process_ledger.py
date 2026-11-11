#!/usr/bin/env python3
from pathlib import Path
import argparse,json
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();L=json.loads((a.root.resolve()/'PROCESS_LEDGER.json').read_text())
assert L['status']=='PASS' and L['science_solver_children']==37 and L['actual_trace_checker_children']==3 and L['packaging_replay_solver_children']==1
assert L['bounded_foreground_children']==len(L['records'])==41 and L['proof_fixture_synchronous_children']==6
assert L['all_children_reaped'] and L['proof_fixture_children_reaped'] and L['weight9_synthesis_auxiliary_children_reaped']
assert L['background_processes']==L['survivors']==L['survivors_at_serialization']==L['timeouts']==0
names=set()
for p in L['records']:
    assert p['name'] not in names;names.add(p['name']);assert p['final_status']=='exited_and_reaped' and not p['timed_out']
    assert p['child_pid']>0 and p['runner_pid']>0
    if p['name'].startswith('round92_actual_sat_trace_'):assert p['returncode']==1
    else:assert p['returncode']==10
for i in range(124,136):
    assert f'outer_iter{i}_cadical' in names and f'direct_iter{i}_Xerr_cadical' in names and f'direct_iter{i}_Zerr_cadical' in names
assert 'round92_weight9_strict_expansion_query' in names and 'round92_package_regenerate_actual_sat_trace' in names
assert 'no result/state/source write' in L['canceled_packaging_experiment']['disposition']
print('ROUND92_PROCESS_LEDGER_PASS',len(names))

