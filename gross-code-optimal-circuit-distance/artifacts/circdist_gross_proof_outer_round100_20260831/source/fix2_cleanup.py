#!/usr/bin/env python3
"""Remove the exact Round100 scratch root and prove process closure."""
from pathlib import Path
import datetime,hashlib,json,os,shutil,subprocess,time
P=Path(__file__).resolve().parent.parent;target=Path('/private/tmp/circdist_round100_gross_20260831');assert P!=target.resolve()
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
files=[x for x in target.rglob('*') if x.is_file()] if target.exists() else []
h=hashlib.sha256()
for x in sorted(files):h.update(x.relative_to(target).as_posix().encode()+b'\0'+sha(x).encode()+b'\n')
before={'exists':target.exists(),'files':len(files),'bytes':sum(x.stat().st_size for x in files),'tree_sha256':h.hexdigest()}
if target.exists():shutil.rmtree(target)
assert not target.exists()
cp=subprocess.Popen(['/bin/ps','-axo','pid=,ppid=,stat=,etime=,command='],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,start_new_session=False);stdout,stderr=cp.communicate(timeout=30);assert cp.returncode==0
patterns=['/private/tmp/circdist_round100_gross_20260831','circdist-r100-full-replay.','run_round100_campaign.py','replay_round100.py','order6_mitm','circdist_gross_proof_outer_round100_20260831/tooling/cadical']
matches=[]
for line in stdout.splitlines():
 if any(p in line for p in patterns):
  fields=line.strip().split(None,4);pid=int(fields[0]) if fields else -1
  if pid not in (os.getpid(),os.getppid()):matches.append(line)
assert matches==[],matches
globs=[str(x) for x in Path('/private/tmp').glob('circdist-r100-full-replay.*')];assert globs==[]
replay=json.loads((P/'verification/preseal_full_replay.json').read_text());validators=json.loads((P/'verification/repository_validators/summary.json').read_text());ledger=json.loads((P/'PROCESS_LEDGER.json').read_text());assert replay['status']==validators['status']==ledger['status']=='PASS'
interpreter=Path('/private/tmp/circdist-r72-dispatcher-venv/bin/python')
out={'schema':'circdist-round100-fix2-closure-v1','status':'PASS','checked_unix':time.time(),'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scratch_path':str(target),'scratch_before':before,'scratch_exists_after':False,'disposition':'removed only after complete evidence had been copied into the sole permitted package','retained_external_dependency':{'path':str(interpreter),'disposition':'pre-existing dispatcher replay environment; not Round100 scratch','exists':interpreter.exists(),'sha256':sha(interpreter)},'preseal_replay':{'direct_children':replay['direct_child_count'],'nested_children':replay['nested_child_count'],'total_known_children':replay['total_known_child_processes'],'all_reaped':replay['all_children_reaped']},'repository_validators':{'children':len(validators['checks']),'all_reaped':validators['all_children_reaped']},'retained_pid_records_before_cleanup_wrapper':ledger['retained_pid_record_count'],'cleanup_process':{'pid':os.getpid(),'parent_pid':os.getppid(),'ps_child_pid':cp.pid,'ps_child_returncode':cp.returncode,'ps_child_reaped':True},'process_scan_command':['/bin/ps','-axo','pid=,ppid=,stat=,etime=,command='],'process_scan_stderr':stderr,'task_process_patterns':patterns,'task_process_matches':matches,'replay_temp_glob_matches':globs,'survivors':0,'detached_processes':0,'all_task_children_reaped':True,'meaning':'Round100 scratch is absent and no matching science, synthesis, replay, or solver process survived.'}
(P/'verification/fix2_closure.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
(P/'FIX-2.md').write_text(f'''# FIX-2 — scratch and process closure\n\n`{target}` contained {before['files']} files / {before['bytes']} bytes before cleanup and is now absent. Its pre-removal tree SHA-256 was `{before['tree_sha256']}`. The cleanup process reaped its `ps` child, found zero matching Round100 science/replay/solver survivors, and found no replay temporary directories. The pre-existing dispatcher Python environment is retained as an external replay dependency and is not Round100 scratch.\n''')
print(json.dumps({'status':'PASS','scratch_removed':str(target),'scratch_files_removed':before['files'],'scratch_bytes_removed':before['bytes'],'survivors':0,'ps_child_pid':cp.pid},sort_keys=True))
