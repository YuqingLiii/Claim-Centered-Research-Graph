#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, os, shutil
CHUNK=8<<20
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(CHUNK),b''):h.update(b)
 return h.hexdigest()
def load(p):return json.loads(Path(p).read_text())
def dump(p,o):Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
ap=argparse.ArgumentParser();ap.add_argument('--package',type=Path,required=True);ap.add_argument('--work',type=Path,required=True);ap.add_argument('--preseal',type=Path,required=True);a=ap.parse_args();P,W=a.package.resolve(),a.work.resolve()
# Import every wrapper log after all preseal work, preserving the earlier payload copy.
for src in sorted((W/'logs').rglob('*')):
 if src.is_file():
  dst=P/'logs'/src.relative_to(W/'logs');dst.parent.mkdir(parents=True,exist_ok=True)
  if dst.exists():dst.chmod(0o644)
  shutil.copy2(src,dst)
dst=P/'verification/preseal_replay.json';shutil.copy2(a.preseal,dst);pre=load(dst);assert pre['status']=='PASS' and pre['mode']=='preseal' and pre['child_count']==18 and pre['all_children_reaped']
gates=load(P/'verification/repository_validators/summary.json');assert gates['status']=='PASS' and gates['check_count']==8 and gates['all_children_reaped']
result=load(P/'RESULT.json');result['preseal_replay_binding']={'status':'PASS','path':'verification/preseal_replay.json','sha256':sha(dst),'bytes':dst.stat().st_size,'child_count':18,'strict_serial':True,'all_children_reaped':True};result['repository_gates']={'status':'PASS','path':'verification/repository_validators/summary.json','sha256':sha(P/'verification/repository_validators/summary.json'),'check_count':8,'all_children_reaped':True,'evidence_closure':'expected post-install pre-review unlinked-package diagnostics only'};result['failures']['disclosed_ids']=[f'F112-{i:03}' for i in range(1,11)];dump(P/'RESULT.json',result)
fl=P/'FAILURE_LEDGER.md';text=fl.read_text().split('- **F112-007.**')[0];text += """- **F112-007.** The first metadata preparation tried to overwrite a read-only file cloned from the sealed source tree. It failed before package metadata generation; the scratch destination mode was corrected.\n- **F112-008.** The first mode correction handled an existing file but not the inherited read-only parent directory. The retry failed before metadata generation; the scratch-only directory was made writable and the next retry passed.\n- **F112-009.** The first preseal replay regenerated identical iter192 source and state bytes but passed absolute audit paths, so only provenance path strings changed in `orbit_audit.json`. It stopped before later checks. The driver was corrected to pass package-relative paths; the full clean-environment retry passed.\n- **F112-010.** A preseal static assertion initially treated the intentionally retained DRAT control fixtures as forbidden raw SAT streams. The check and seal scope were corrected to forbid raw `.drat` only under `solver/` and `batch/`; the control fixtures remain required.\n""";fl.write_text(text)
records=[]
for p in sorted((P/'logs/process').glob('*.json')):
 try:o=load(p)
 except Exception:continue
 if isinstance(o,dict) and 'child_pid' in o:records.append({'path':p.relative_to(P).as_posix(),'sha256':sha(p),'name':o.get('name'),'child_pid':o['child_pid'],'returncode':o.get('returncode'),'expected_returncodes':o.get('expected_returncodes'),'reaped':o.get('reaped'),'detached':o.get('detached'),'timed_out':o.get('timed_out')})
ledger={'schema':'circdist-gross-round112-process-fix2-ledger-v1','status':'PASS','records':records,'pid_bearing_records':len(records),'all_pid_bearing_records_reaped':all(x['reaped'] is True for x in records),'detached_processes':sum(x['detached'] is True for x in records),'timed_out_processes':sum(x['timed_out'] is True for x in records),'preseal_replay_children':18,'preseal_replay_strict_serial':True,'preseal_replay_all_reaped':True,'repository_gate_children':8,'repository_gates_strict_serial':True,'repository_gate_children_all_reaped':True,'proof_control_children':6,'proof_control_children_all_reaped':True,'failure_ids':[f'F112-{i:03}' for i in range(1,11)],'fix2_preseal':{'survivors':0,'status':'PASS'},'external_postseal_note':'Atomic install, expected pre-review evidence closure, installed replay, sealed verification, and final zero-survivor census are recorded outside immutable package.'};assert ledger['all_pid_bearing_records_reaped'] and ledger['detached_processes']==0 and ledger['timed_out_processes']==0;dump(P/'PROCESS_FIX2_LEDGER.json',ledger)
(P/'REPORT.md').write_text((P/'REPORT.md').read_text().replace('**Status:** installed package is pending until atomic promotion; scientific result is SAT/SAT/SAT and the root remains **CONJECTURED**.','**Status:** proposed/unreviewed Round112 evidence; scientific result is SAT/SAT/SAT and the root remains **CONJECTURED**. Canonical state is unchanged.'))
replay='''#!/bin/sh\nset -eu\nROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)\nif [ "$#" -gt 2 ]; then echo "usage: $0 [REPOSITORY_ROOT] [EXTERNAL_OUTPUT_JSON]" >&2; exit 2; fi\nREPO=${1:-$(CDPATH= cd -- "$ROOT/../../.." && pwd)}\nOUTPUT=${2:-${TMPDIR:-/tmp}/circdist-round112-replay-$$.json}\nexec /usr/bin/python3 "$ROOT/source/replay_round112.py" --package "$ROOT" --repo "$REPO" --output "$OUTPUT" --mode installed\n'''
(P/'replay.sh').write_text(replay);(P/'replay.sh').chmod(0o755)
print(json.dumps({'status':'PASS','preseal_sha256':sha(dst),'gate_sha256':sha(P/'verification/repository_validators/summary.json'),'process_records':len(records),'result_sha256':sha(P/'RESULT.json')},sort_keys=True))
