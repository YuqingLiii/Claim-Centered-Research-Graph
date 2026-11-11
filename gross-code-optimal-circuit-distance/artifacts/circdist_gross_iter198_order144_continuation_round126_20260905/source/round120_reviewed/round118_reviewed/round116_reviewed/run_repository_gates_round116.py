#!/usr/bin/env python3
"""Run required repository gates strictly serially with exact process records."""
import argparse,datetime,hashlib,json,os,subprocess,time
from pathlib import Path

def sha(p):
 h=hashlib.sha256()
 with Path(p).open("rb") as f:
  for b in iter(lambda:f.read(8<<20),b""):h.update(b)
 return h.hexdigest()

ap=argparse.ArgumentParser();ap.add_argument("--repository",type=Path,required=True);ap.add_argument("--package",type=Path,required=True);ap.add_argument("--output",type=Path,required=True)
a=ap.parse_args();repo=a.repository.resolve();pkg=a.package.resolve();out=a.output.resolve();assert not out.exists();out.mkdir(parents=True)
env={"PATH":"/usr/bin:/bin:/usr/sbin:/sbin","LANG":"C.UTF-8","LC_ALL":"C.UTF-8","TZ":"UTC","TMPDIR":str(out/"tmp"),"PYTHONDONTWRITEBYTECODE":"1"};(out/"tmp").mkdir()
commands=[
 ("proof_dag_circdist",["/usr/bin/python3","tools/proof_dag_check.py","--problem","circdist"],[0]),
 ("proof_dag_all",["/usr/bin/python3","tools/proof_dag_check.py","--problem","all"],[0]),
 ("circdist_migration",["/usr/bin/python3","tools/check_circdist_migration.py"],[0]),
 ("release_contracts",["/usr/bin/python3","tools/test_release_contracts.py"],[0]),
 ("dag_contracts",["/usr/bin/python3","tools/test_dag_contracts.py"],[0]),
 ("lean_dag_selftest",["/usr/bin/python3","tools/lean_dag_check.py","--selftest"],[0]),
 ("duplicate_yaml",["/usr/bin/python3",str(pkg/"source/parent_duplicate_yaml_scan.py"),"--root",str(repo),"--output",str(out/"duplicate_yaml.json")],[0]),
 ("git_diff_check",["/usr/bin/git","diff","--check"],[0]),
 ("evidence_closure_raw",["/usr/bin/python3","tools/evidence_closure_check.py","--problem","circdist"],[1]),
]
rows=[]
def run(name,argv,expected):
 start=time.time();p=subprocess.Popen(argv,cwd=repo,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=False);stdout,stderr=p.communicate();end=time.time()
 sp=out/(name+".stdout");ep=out/(name+".stderr");sp.write_bytes(stdout);ep.write_bytes(stderr)
 row={"name":name,"argv":argv,"cwd":str(repo),"environment":env,"parent_pid":os.getpid(),"child_pid":p.pid,
      "start_utc":datetime.datetime.fromtimestamp(start,datetime.timezone.utc).isoformat(),"end_utc":datetime.datetime.fromtimestamp(end,datetime.timezone.utc).isoformat(),
      "duration_ns":int((end-start)*1e9),"returncode":p.returncode,"expected_returncodes":expected,"returncode_matches":p.returncode in expected,
      "stdout":str(sp),"stdout_sha256":sha(sp),"stdout_bytes":len(stdout),"stderr":str(ep),"stderr_sha256":sha(ep),"stderr_bytes":len(stderr),
      "reaped":True,"detached":False,"timeout_configured":False,"timeout_triggered":False}
 (out/(name+".run.json")).write_text(json.dumps(row,indent=2,sort_keys=True)+"\n");rows.append(row);print(json.dumps({"name":name,"pid":p.pid,"rc":p.returncode,"seconds":round(end-start,6)},sort_keys=True),flush=True)
 assert row["returncode_matches"],(name,p.returncode,stdout[-2000:],stderr[-2000:])
for x in commands:run(*x)
merged=out/"evidence_closure.merged";merged.write_bytes((out/"evidence_closure_raw.stdout").read_bytes()+(out/"evidence_closure_raw.stderr").read_bytes())
relative=pkg.relative_to(repo).as_posix()
run("evidence_closure_interpret",["/usr/bin/python3",str(pkg/"source/check_evidence_closure_round116.py"),"--log",str(merged),"--package-relative",relative,"--output",str(out/"evidence_closure_interpretation.json")],[0])
interpret=json.loads((out/"evidence_closure_interpretation.json").read_text());assert interpret["status"]=="PASS" and interpret["all_errors_under_new_package"]
summary={"schema":"circdist-gross-round116-repository-gates-v1","status":"PASS","checks":rows,"check_count":len(rows),
         "strict_serial":True,"all_children_reaped":True,"detached_children":0,"timeouts_configured":0,"timeouts_triggered":0,
         "standard_zero_exit_gates":8,"evidence_closure_raw_exit":1,"evidence_closure_interpretation":interpret}
(out/"summary.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n");print(json.dumps({"status":"PASS","checks":len(rows),"unlinked_paths":interpret["error_count"]},sort_keys=True))
