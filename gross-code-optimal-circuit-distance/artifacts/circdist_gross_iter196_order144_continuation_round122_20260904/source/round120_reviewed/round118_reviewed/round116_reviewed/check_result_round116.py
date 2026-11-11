#!/usr/bin/env python3
"""Check the machine verdict against durable evidence and reject overclaiming."""
import argparse, hashlib, json
from pathlib import Path


def sha(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as f:
        for b in iter(lambda:f.read(8<<20),b""):h.update(b)
    return h.hexdigest()


ap=argparse.ArgumentParser();ap.add_argument("--root",type=Path,required=True);ap.add_argument("--output",type=Path,required=True)
a=ap.parse_args();R=a.root.resolve();d=json.loads((R/"RESULT.json").read_text())
assert d["status"]=="PASS_WITHOUT_ROOT_CLOSURE"
rv=d["root_verdict"]
assert rv["CIRCDIST.gross"]==rv["gap_via_lift"]=="CONJECTURED" and rv["Dstar_Gross"]==[11,12]
assert not rv["branch_A_legal_distance12_schedule_established"] and not rv["branch_B_universal_distance_at_most11_established"]
assert rv["promotion_or_narrowing"] is None
for key,expected in {
"canonical_gross":"5fe0aebccc3b97757b0c2560ca18db8fbdbe1c4468ea49153382fbe0fbc51df0",
"scheduler":"e47e27cef7ef026edca8e0cb73eeb3ba969a17212de922f6c29b7a8029c029a4",
"round115_review":"15c31086b2aa8c7f6eaa6bbdd2a4c4b7d61bfaba55b60a142c07e0ac6801f9b5",
"round114_root_manifest":"b041e4919cdd21e834d6bf8bd252302ef7d9449af7bf10a70bf20ff0d01f9b58",
"round116_proofpilot":"1571799f7532a85026a38d32f0596543e98207a3a4d202c9f65028bcd3fb5c67"}.items():
    b=d["dispatch"]["bindings"][key];assert b["sha256"]==expected==sha(R/b["path"])
i=d["iteration193"]
assert i["mandatory_quotient_solved_first"] and i["solver"]["status"]=="SATISFIABLE"
assert i["complete_assignment"]["all_dimacs_clauses_satisfied"] and i["complete_assignment"]["checked_clauses"]==16301485
assert i["schedule"]["edges"]==864 and i["schedule"]["layers"]==460 and i["schedule"]["reviewed_block_hits"]==i["schedule"]["selector_hits"]==0
for label in ("Xerr","Zerr"):
    x=i["direct"][label];assert x["status"]=="SATISFIABLE" and x["query"]=="complete unrestricted direct-360"
    m=x["mechanism"];assert m["fault_count"]==10 and not m["physical_syndrome"] and any(m["logical_parities"])
    assert m["canonical_nonstabilizer"] and m["physical_nonstabilizer"] and m["all_clauses_satisfied"]
assert not i["repair"]["entered"] and i["sat_trace_retention"]["unsat_certificate_credit"] is False
f=d["iteration194_fresh_frontier"]
assert f["status"]=="CHECKED_UNSTARTED" and f["solver_invocations"]==0 and f["sat_result"] is f["unsat_result"] is None
assert f["source"]["blocks"]==814392 and f["source"]["selectors"]==50832 and f["source"]["assertions"]==869622
assert f["closure"]["order144"] and f["closure"]["nonfree_orbits_explicitly_handled"]
assert f["quotient"]["group_order"]==144 and f["quotient"]["roots"]==143 and f["quotient"]["equisatisfiable_with_full_iter194_base"]
assert f["source"]["sha256"]==sha(R/"frontier/iter194/source.json.gz")
assert f["base"]["sha256"]==sha(R/"frontier/iter194/formula/outer.cnf")
assert f["quotient"]["sha256"]==sha(R/"frontier/iter194/order144_quotient/outer.cnf")
forbidden=[]
for p in (R/"frontier/iter194").rglob("*"):
    if p.is_file() and (p.suffix in (".drat",".lrat") or "solver.log" in p.name or "assignment" in p.name.lower()): forbidden.append(p.relative_to(R).as_posix())
assert not forbidden
out={"schema":"circdist-gross-round116-result-check-v1","status":"PASS","root_overclaim_rejected":True,
     "iter193_disposition":["SAT","SAT","SAT"],"iter194_status":"CHECKED_UNSTARTED","forbidden_iter194_solver_artifacts":forbidden,
     "checked_hashes":{"source":f["source"]["sha256"],"base":f["base"]["sha256"],"quotient":f["quotient"]["sha256"]}}
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n");print(json.dumps(out,sort_keys=True))
