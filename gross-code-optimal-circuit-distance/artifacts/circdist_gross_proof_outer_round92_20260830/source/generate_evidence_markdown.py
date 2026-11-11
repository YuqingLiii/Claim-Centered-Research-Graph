#!/usr/bin/env python3
from pathlib import Path
import argparse,json
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();x=json.loads((R/'RESULT.json').read_text())
o=['# Load-bearing evidence hashes','', 'Complete byte closure is in the two manifests and file inventory.  The table below is an audit index.','',
'| iter | outer CNF | outer assignment (raw) | outer model log | X CNF | X mechanism | Z CNF | Z mechanism |','|---:|---|---|---|---|---|---|---|']
for r in x['iterations']:
 i=r['iteration'];q=r['outer'];X=r['direct']['Xerr'];Z=r['direct']['Zerr'];o.append(f"| {i} | `{q['cnf_sha256']}` | `{q['uncompressed_assignment_sha256']}` | `{q['solver_log_sha256']}` | `{X['cnf_sha256']}` | `{X['mechanism_semantic_sha256']}` | `{Z['cnf_sha256']}` | `{Z['mechanism_semantic_sha256']}` |")
o += ['','## Phase A','',f"- synthesis file: `{x['phase_a']['synthesis_file_sha256']}`",f"- synthesis semantic result: `{x['phase_a']['semantic_result_sha256']}`",f"- strict-expansion CNF: `{x['phase_a']['strict_expansion_query_cnf_sha256']}`",f"- strict-expansion assignment: `{x['phase_a']['strict_expansion_assignment_sha256']}`",f"- strict-expansion schedule: `{x['phase_a']['strict_expansion_schedule_sha256']}`",'','## Fresh frontier','',f"- state file: `{x['fresh_state']['state_file_sha256']}`",f"- selector-state semantic hash: `{x['fresh_state']['selector_state_sha256']}`",f"- source file: `{x['fresh_state']['source_file_sha256']}`",f"- source semantic hash: `{x['fresh_state']['source_semantic_sha256']}`",f"- CNF: `{x['fresh_state']['cnf_sha256']}`",'','All 36 SAT-side proof streams are indexed with formula hash, stream hash, bytes, LF count, and empty-clause count in `data/sat_drat_trace_disposition.json`. None is an UNSAT certificate.','']
(R/'EVIDENCE_HASHES.md').write_text('\n'.join(o))
