#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,json,subprocess,sys,time
ap=argparse.ArgumentParser();ap.add_argument('--first',type=int,required=True);ap.add_argument('--last',type=int,required=True);ap.add_argument('--engine-root',type=Path,required=True);ap.add_argument('--work-root',type=Path,required=True);ap.add_argument('--python',type=Path,required=True);a=ap.parse_args()
ledger=a.work_root/'cegar'/'range_driver.json'
records=[]
for iteration in range(a.first,a.last+1):
    started=datetime.datetime.now(datetime.timezone.utc).isoformat();t0=time.monotonic()
    cmd=[str(a.python),str(a.engine_root/'src/run_online_iteration.py'),'--iteration',str(iteration),'--engine-root',str(a.engine_root),'--work-root',str(a.work_root),'--python',str(a.python)]
    log=a.work_root/'cegar'/f'iter{iteration}.driver.log'
    with log.open('wb') as out: cp=subprocess.run(cmd,stdout=out,stderr=subprocess.STDOUT)
    rec={'iteration':iteration,'started_utc':started,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'wall_seconds':time.monotonic()-t0,'exit_code':cp.returncode,'log':str(log),'argv':cmd}
    records.append(rec);ledger.write_text(json.dumps({'schema':'round76-serial-range-driver-v1','first':a.first,'last':a.last,'records':records},indent=2,sort_keys=True)+'\n')
    print(json.dumps(rec,sort_keys=True),flush=True)
    if cp.returncode!=0:raise SystemExit(cp.returncode)
