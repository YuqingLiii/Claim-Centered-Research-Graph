#!/usr/bin/env python3
"""Verify retained actual-formula SAT-side trace controls and their recorded runs."""
from pathlib import Path
import argparse,hashlib,json
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();C=a.root.resolve()/'controls/actual_sat_trace';S=json.loads((C/'summary.json').read_text())
assert S['status']=='PASS' and S['formula_sha256']=='5c50713ebd9620a69164f2bc9dce63a0c2ca7f5cf7f8ed2f387ed1746d9b94ff'
assert sha(C/'full.drat')==S['source_trace_sha256']=='5dd1dfa8829b528bb24587260ea9b516cd324fe1ee8be8fb2d917976b42b086c'
assert (C/'full.drat').stat().st_size==S['source_trace_bytes']==3603 and S['source_trace_empty_clause_lines']==0
for name in ('full','truncated','corrupt'):
    row=S['drat_checker_runs'][name];run=json.loads((C/f'{name}.run.json').read_text())
    assert sha(C/f'{name}.drat')==row['trace_sha256'] and (C/f'{name}.drat').stat().st_size==row['trace_bytes']
    assert row['returncode']==run['returncode']==1 and not row['accepted'] and not row['timed_out'] and not run['timed_out']
    assert sha(C/f'{name}.log')==row['log_sha256'] and 'NOT VERIFIED' in (C/f'{name}.log').read_text(errors='replace')
assert S['full_sat_trace_rejected'] and S['truncated_sat_trace_rejected'] and S['corrupt_sat_trace_rejected']
print('ROUND92_ACTUAL_SAT_TRACE_CONTROLS_PASS')

