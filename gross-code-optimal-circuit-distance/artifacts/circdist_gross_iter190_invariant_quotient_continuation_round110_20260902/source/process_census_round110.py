#!/usr/bin/env python3
"""Reject surviving Round110 science processes and replay temporary directories."""
from pathlib import Path
import argparse, datetime, json, os, subprocess, tempfile, time
ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args(); root=a.root.resolve(); start=time.time()
child=subprocess.Popen(['/bin/ps','-axo','pid=,ppid=,stat=,etime=,command='],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,start_new_session=False)
out,err=child.communicate(timeout=30); assert child.returncode==0
patterns=[root.parent.name,'cadical-1.9.5-arm64-macos','drat-trim-arm64-macos','lrat-check-arm64-macos','replay_round110.py','advance_full_invariant_frontier_round110.py','check_incremental_orbit_closure_round110.py','compile_outer_cnf.py','check_translation_quotient_round102.py']
excluded={os.getpid(),os.getppid(),child.pid}; raw=[]; survivors=[]
for line in out.splitlines():
 if not any(x in line for x in patterns): continue
 raw.append(line); fields=line.strip().split(None,4); pid=int(fields[0]) if fields else -1
 if pid not in excluded and '/bin/ps -axo' not in line: survivors.append(line)
assert not survivors,survivors
temporary=sorted(str(p) for p in Path(tempfile.gettempdir()).glob('circdist-round110-replay.*')); assert not temporary,temporary
result={'schema':'circdist-gross-round110-process-census-v1','status':'PASS','checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'checked_unix':time.time(),'package':str(root),'patterns':patterns,'argv':['/bin/ps','-axo','pid=,ppid=,stat=,etime=,command='],
 'cwd':os.getcwd(),'environment':{k:os.environ[k] for k in ('PATH','LANG','LC_ALL') if k in os.environ},
 'census_parent_pid':os.getpid(),'census_wrapper_pid':os.getppid(),'ps_child_pid':child.pid,'ps_returncode':child.returncode,
 'ps_child_reaped':True,'ps_stderr':err,'raw_pattern_matches':raw,'excluded_pids':sorted(excluded),
 'matching_live_science_processes':survivors,'science_survivor_count':0,'detached_processes':0,
 'replay_temporary_matches':temporary,'wall_seconds':round(time.time()-start,6)}
a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(json.dumps({'status':'PASS','science_survivor_count':0,'ps_child_pid':child.pid,'temporary_matches':0},sort_keys=True))
