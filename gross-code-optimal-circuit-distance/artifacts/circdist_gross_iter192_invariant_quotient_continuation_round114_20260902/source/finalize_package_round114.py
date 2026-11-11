#!/usr/bin/env python3
"""Finalize reports, replay/gates, provenance, and FIX-2 ledger before sealing."""
from __future__ import annotations
import argparse,hashlib,json,os,shutil,stat
from pathlib import Path
CHUNK=8<<20

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(CHUNK),b''):h.update(b)
 return h.hexdigest()
def load(p):return json.loads(Path(p).read_text())
def make_owner_writable(p):
 p=Path(p)
 if p.exists():p.chmod(p.stat().st_mode|stat.S_IWUSR)
def dump(p,o):
 p=Path(p);make_owner_writable(p);p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def copy2_replace(src,dst):
 src,dst=Path(src),Path(dst);dst.parent.mkdir(parents=True,exist_ok=True);make_owner_writable(dst);shutil.copy2(src,dst)
 assert dst.stat().st_nlink==1 and (src.stat().st_dev,src.stat().st_ino)!=(dst.stat().st_dev,dst.stat().st_ino)
def sync_tree(src,dst):
 for p in sorted(src.rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc':
   q=dst/p.relative_to(src);copy2_replace(p,q)
ap=argparse.ArgumentParser();ap.add_argument('--package',type=Path,required=True);ap.add_argument('--work',type=Path,required=True);ap.add_argument('--preseal',type=Path,required=True);a=ap.parse_args();P,W=a.package.resolve(),a.work.resolve()
# Synchronize final scripts and all wrapper records/logs accumulated after initial staging.
for name in ('source','logs','admin'):sync_tree(W/name,P/name)
pre_dst=P/'verification/preseal_replay.json';copy2_replace(a.preseal,pre_dst);pre=load(pre_dst)
assert pre['status']=='PASS' and pre['mode']=='preseal' and pre['child_count']==16 and pre['all_children_reaped']
pc_src=a.preseal.parent/(a.preseal.stem+'.work')/'proof_controls.json';pc_dst=P/'verification/preseal_proof_controls.json';copy2_replace(pc_src,pc_dst)
gates=load(P/'verification/repository_validators/summary.json');assert gates['status']=='PASS' and gates['check_count']==8 and gates['all_children_reaped']
# Update durable result with completed replay/gate binding.
result=load(P/'RESULT.json');result['preseal_replay_binding']={'status':'PASS','path':'verification/preseal_replay.json','sha256':sha(pre_dst),
 'bytes':pre_dst.stat().st_size,'child_count':16,'strict_serial':True,'all_children_reaped':True,'nested_proof_control_children':6}
result['repository_gates']={'status':'PASS','path':'verification/repository_validators/summary.json','sha256':sha(P/'verification/repository_validators/summary.json'),
 'check_count':8,'strict_serial':True,'all_children_reaped':True,
 'evidence_closure':'preinstall canonical gates pass; post-install unlinked-package diagnostics are expected until independent review links this proposer package'}
result['package_seal']={'status':'SELF_AUTHENTICATING_MANIFESTS_TO_BE_WRITTEN_AFTER_THIS_RESULT','payload':'PAYLOAD_SHA256SUMS.txt','inventory':'FILE_INVENTORY.jsonl','root':'SHA256SUMS.txt'}
result['failures']['disclosed_ids']=[f'F114-{i:03}' for i in range(1,12)]
dump(P/'RESULT.json',result)
# Complete process inventory: runner records, replay children, nested proof controls,
# repository-gate children, and every early executor-only foreground invocation.
records=[]
for base in (W/'admin/process',W/'logs/process'):
 for path in sorted(base.glob('*.json')):
  try:o=load(path)
  except Exception:continue
  if isinstance(o,dict) and 'child_pid' in o:
   records.append({'class':'recorded_child','record_source':str(path),'record_sha256':sha(path),'name':o.get('name'),
    'child_pid':o['child_pid'],'returncode':o.get('returncode'),'returncode_matches':o.get('returncode_matches'),
    'reaped':o.get('reaped'),'detached':o.get('detached'),'timed_out':o.get('timed_out'),'started_utc':o.get('started_utc'),'ended_utc':o.get('ended_utc')})
for origin,obj in (('initial_proof_controls',load(P/'verification/proof_controls.json')),('preseal_proof_controls',load(pc_dst))):
 for row in obj['runs']:
  records.append({'class':'nested_child','origin':origin,'name':row['name'],'child_pid':row['child_pid'],'returncode':row['returncode'],
   'returncode_matches':row['returncode']==row['expected_returncode'] and not row['timed_out'],'reaped':row['reaped'],'detached':row['detached'],
   'timed_out':row['timed_out'],'started_utc':row['started_utc'],'ended_utc':row['ended_utc']})
for row in gates['checks']:
 records.append({'class':'nested_child','origin':'repository_gates','name':row['name'],'child_pid':row['child_pid'],'returncode':row['returncode'],
  'returncode_matches':row['returncode_matches'],'reaped':row['reaped'],'detached':row['detached'],'timed_out':row['timed_out'],
  'started_utc':row['started_utc'],'ended_utc':row['ended_utc']})
for row in pre['runs']:
 records.append({'class':'nested_child','origin':'preseal_replay','name':row['name'],'child_pid':row['child_pid'],'returncode':row['returncode'],
  'returncode_matches':row['returncode_matches'],'reaped':row['reaped'],'detached':row['detached'],'timed_out':row['timed_out'],
  'started_utc':row['started_utc'],'ended_utc':row['ended_utc']})
initial=load(W/'admin/SESSION_PROCESS_LEDGER.initial.json')['rows']
unwrapped=list(initial)
extra=[
 ('U014','create input/plan preparation script and chmod',0),('U015','read and hash frozen plans',0),('U016','first verifier creation against inherited 0555 scratch source directory',1),
 ('U017','create verifier after scratch-only directory chmod',0),('U018','inspect reviewed historical solver/replay argv',0),('U019','read first model-replay dependency stderr',0),
 ('U020','create independent iter192 audit by transparent retained-source adaptation',0),('U021','read independent direct results',0),('U022','inspect source top-level schema/counts',0),
 ('U023','process-runner help inspection',0),('U024','read key-definition grep bundle',0),('U025','read block/selector/quotient helper source ranges',0),
 ('U026','schema probe with wrong input source path',1),('U027','locate corrected input/reconstructed paths',0),('U028','inspect corrected source schema and sector definitions',0),
 ('U029','inspect sector field types and residual positions',0),('U030','verify qubit-signature bit encoding',0),('U031','create CSS-duality audit source and chmod',0),
 ('U032','read CSS-audit Python3.9 failure stderr',0),('U033','read successful CSS audit summary',0),('U034','read mandatory X/Z orbit summaries',0),
 ('U035','create mandatory CSS-dual orbit audit source and chmod',0),('U036','create CSS-dual frontier advance source and chmod',0),('U037','list and hash frozen plans',0),
 ('U038','read frontier advance summary and source size',0),('U039','initial reconstruction-record name probe',0),('U040','locate reconstruction/quotient process records',0),
 ('U041','read reconstruction/quotient argv',0),('U042','read iter193 base compiler summary',0),('U043','read first quotient-check failure stderr',0),
 ('U044','inspect copied vendor layout',0),('U045','locate reviewed prior quotient-check record',0),('U046','read reviewed prior quotient-check argv',0),
 ('U047','read second quotient-check failure stderr',0),('U048','inventory current solver stream sizes',0),('U049','inventory reviewed prior solver stream sizes',0),
 ('U050','locate retained stream-compression/check tools',0),('U051','read retained stream-compression/check source',0),('U052','read compressed stream summary and sizes',0),
 ('U053','inspect reviewed Round112 package topology',0),('U054','read reviewed package preparation/finalization/replay sources',0),('U055','read initial ledger and current process-record inventory',0),
 ('U056','read reconstruction verifier and retained process argv',0),('U057','read proof controls/base output/quotient summaries',0),('U058','read Round112 repository-gate summary and runner',0),
 ('U059','read evidence-closure and duplicate-YAML helpers',0),('U060','repository-status wrapper invoked with unavailable scratch-relative runner from repository cwd',2),
 ('U061','read corrected repository-status output',0),('U062','read scientific result summaries for report binding',0),('U063','create package preparation source and chmod',0),
 ('U064','inspect and patch package copy-audit rows',0),('U065','create replay source, update copy-method wording, sync replay into stage',0),
 ('U066','read preseal replay summary/run durations',0),('U067','create finalizer source and chmod',0)]
extra.extend([
 ('U068','read first finalizer permission failure stderr',0),('U069','patch finalizer for idempotent ordinary-copy replacement of read-only staged destinations',0),
 ('U070','append disclosed first-finalizer failure to failure ledger',0),('U071','inspection invoked unavailable /usr/bin/rg path',127),
 ('U072','discover bundled rg executable path',0),('U073','repeat report failure-reference inspection with bundled rg',0),
 ('U074','patch finalizer failure bindings and expanded unwrapped-process inventory',0),('U075','append rg-path failure and compile-check corrected finalizer',0),
 ('U076','inspect first finalizer process record',0),('U077','locate retained foreground process runner',0),('U078','inspect process-runner command interface',0),
 ('U079','inspect successful retry output and assembled status objects',0),('U080','complete finalizer unwrapped-process inventory before definitive run',0)])
extra.extend([
 ('U081','create retained seal, independent root verifier, ordinary-copy installer, and evidence-closure interpreter',0),
 ('U082','preinstall evidence-closure wrapper invoked with unavailable scratch-relative runner from repository cwd',2),
 ('U083','create retained serial postinstall gate runner',0),
 ('U084','append runner-path failure, chmod new scratch tools, and compile-check all new tools',0),
 ('U085','complete finalizer failure and unwrapped-process bindings before immutable seal',0)])
for ident,description,rc in extra:
 unwrapped.append({'id':'PL114-'+ident,'class':'executor_foreground','description':description,'pid':'executor_pid_unavailable','returncode':rc,
  'foreground':True,'reaped':'on_command_return','detached':False,'timed_out':False,'science_output':False})
# This finalizer is itself foreground and will be reaped by the retained wrapper after it writes the ledger.
unwrapped.append({'id':'PL114-FINALIZER','class':'self_boundary','description':'finalize package metadata and FIX-2 ledger','pid':os.getpid(),
 'returncode':'written only if process reaches this row; parent wrapper records final exit','foreground':True,'reaped':'by_parent_wrapper_on_return','detached':False,'timed_out':False,'science_output':False})
all_records=records+unwrapped
assert all(x.get('detached') in (False,None) for x in all_records) and all(x.get('timed_out') in (False,None) for x in all_records)
assert all(x.get('reaped') in (True,'on_command_return','by_parent_wrapper_on_return') for x in all_records)
ledger={'schema':'circdist-gross-round114-process-fix2-ledger-v1','status':'PASS','records':all_records,'record_count':len(all_records),
 'pid_bearing_completed_records':sum(isinstance(x.get('child_pid'),int) for x in records),'executor_pid_unavailable_records':sum(x.get('pid')=='executor_pid_unavailable' for x in unwrapped),
 'all_foreground':True,'all_completed_children_reaped':True,'detached_processes':0,'timed_out_processes':0,
 'strict_serial_scientific_processes':True,'proof_control_nested_children':12,'repository_gate_children':8,'preseal_replay_children':16,
 'failure_ids':[f'F114-{i:03}' for i in range(1,12)],
 'finalization_boundary':'the finalizer self-row is reaped by its foreground parent wrapper after ledger write; seal/install/installed-replay/postinstall-gate/cleanup dispositions are necessarily external to the immutable preseal ledger and are reported in the proposer handoff'}
dump(P/'PROCESS_FIX2_LEDGER.json',ledger)
# Human-facing replay entrypoint; all outputs remain outside a read-only package.
replay='''#!/bin/sh\nset -eu\nROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)\nif [ "$#" -gt 2 ]; then echo "usage: $0 [REPOSITORY_ROOT] [EXTERNAL_OUTPUT_JSON]" >&2; exit 2; fi\nREPO=${1:-$(CDPATH= cd -- "$ROOT/../../.." && pwd)}\nOUTPUT=${2:-${TMPDIR:-/tmp}/circdist-round114-replay-$$.json}\nexec /usr/bin/python3 "$ROOT/source/replay_round114.py" --package "$ROOT" --repo "$REPO" --output "$OUTPUT" --mode installed\n'''
make_owner_writable(P/'replay.sh');(P/'replay.sh').write_text(replay);(P/'replay.sh').chmod(0o755)
# Post-assembly no-hardlink/symlink census (the audit file itself is checked by seal).
paths=[p for p in P.rglob('*') if p.is_file()];assert not [p for p in P.rglob('*') if p.is_symlink()] and not [p for p in paths if p.stat().st_nlink!=1]
hard={'schema':'circdist-gross-round114-postassembly-filesystem-audit-v1','status':'PASS','regular_files_before_this_record':len(paths),
 'symlinks':0,'files_with_nlink_not_one':0,'hardlinks':0,'ctime_provenance_claimed':False,
 'note':'Round113 ctime provenance is invalid; this audit claims current bytes, inode/link state, and absence of symlinks only.'};dump(P/'verification/postassembly_filesystem_audit.json',hard)
print(json.dumps({'status':'PASS','preseal_sha256':sha(pre_dst),'gates_sha256':sha(P/'verification/repository_validators/summary.json'),
 'process_records':len(all_records),'result_sha256':sha(P/'RESULT.json'),'ledger_sha256':sha(P/'PROCESS_FIX2_LEDGER.json')},sort_keys=True))
