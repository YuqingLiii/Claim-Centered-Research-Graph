#!/usr/bin/env python3
"""Strictly serial, read-only replay of the sealed Round116 package."""
from __future__ import annotations
import argparse, datetime, hashlib, json, os, shutil, subprocess, sys, time
from pathlib import Path


def sha(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as f:
        for b in iter(lambda:f.read(8<<20),b""):h.update(b)
    return h.hexdigest()


def strip_runtime(value):
    ignored={"seconds","wall_seconds","compile_seconds"}
    if isinstance(value,dict): return {k:strip_runtime(v) for k,v in value.items() if k not in ignored}
    if isinstance(value,list): return [strip_runtime(v) for v in value]
    return value


ap=argparse.ArgumentParser()
ap.add_argument("--root",type=Path,required=True)
ap.add_argument("--output",type=Path,required=True)
ap.add_argument("--allow-writable-root",action="store_true")
ap.add_argument("--skip-sat-streams",action="store_true")
a=ap.parse_args(); R=a.root.resolve(); O=a.output.resolve()
assert R.is_dir() and not O.exists(); O.mkdir(parents=True)
py="/usr/bin/python3"
env={"PATH":"/usr/bin:/bin:/usr/sbin:/sbin","LANG":"C.UTF-8","LC_ALL":"C.UTF-8","TZ":"UTC",
     "TMPDIR":str(O/"tmp"),"PYTHONDONTWRITEBYTECODE":"1",
     "PYTHONPATH":str(R/"source")+":"+str(R/"python/site-packages")}
(O/"tmp").mkdir()
runs=[]; comparisons=[]


def run(name,argv,cwd=None):
    assert not any(not row["reaped"] for row in runs)
    start=time.time(); child=subprocess.Popen(argv,cwd=str(cwd or R),env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=False)
    stdout,stderr=child.communicate(); end=time.time()
    sp=O/(name+".stdout"); ep=O/(name+".stderr"); sp.write_bytes(stdout);ep.write_bytes(stderr)
    row={"name":name,"argv":[str(x) for x in argv],"cwd":str((cwd or R).resolve()),"environment":env,
         "parent_pid":os.getpid(),"child_pid":child.pid,"start_utc":datetime.datetime.fromtimestamp(start,datetime.timezone.utc).isoformat(),
         "end_utc":datetime.datetime.fromtimestamp(end,datetime.timezone.utc).isoformat(),"duration_ns":int((end-start)*1e9),
         "returncode":child.returncode,"stdout":str(sp),"stdout_sha256":sha(sp),"stdout_bytes":len(stdout),
         "stderr":str(ep),"stderr_sha256":sha(ep),"stderr_bytes":len(stderr),"reaped":True,"detached":False,
         "timeout_configured":False,"timeout_triggered":False}
    (O/(name+".run.json")).write_text(json.dumps(row,indent=2,sort_keys=True)+"\n");runs.append(row)
    print(json.dumps({"name":name,"pid":child.pid,"rc":child.returncode,"seconds":round(end-start,6)},sort_keys=True),flush=True)
    assert child.returncode==0,(name,child.returncode,stdout[-2000:],stderr[-2000:])


def exact(name,left,right):
    left,right=Path(left),Path(right); assert sha(left)==sha(right)
    comparisons.append({"name":name,"kind":"byte_exact","left":str(left),"right":str(right),"sha256":sha(left)})


def semantic(name,left,right):
    left,right=Path(left),Path(right)
    assert strip_runtime(json.loads(left.read_text()))==strip_runtime(json.loads(right.read_text()))
    comparisons.append({"name":name,"kind":"JSON_equal_after_removing_runtime_fields","left":str(left),"right":str(right)})


S=R/"source"; generated=O/"generated"; generated.mkdir()
if not a.allow_writable_root:
    run("sealed_package",[py,S/"check_sealed_package_round116.py","--root",R,"--output",O/"sealed_package.json"])
run("result",[py,S/"check_result_round116.py","--root",R,"--output",O/"result.json"])

run("outer_assignment",[py,S/"parent_extract_and_check_assignment.py","--cnf",R/"input/iter193/translation_quotient/outer.cnf",
    "--solver-log",R/"output/iter193/solver/solver.log","--assignment",O/"outer.assignment.dimacs","--output",O/"outer.assignment_check.json"])
exact("outer assignment",O/"outer.assignment.dimacs",R/"output/iter193/solver/assignment.dimacs")
exact("outer assignment check",O/"outer.assignment_check.json",R/"output/iter193/solver/assignment_check.json")
run("outer_semantics",[py,S/"parent_verify_outer_sat_model.py","--solver-log",R/"output/iter193/solver/solver.log",
    "--cnf",R/"input/iter193/translation_quotient/outer.cnf","--source",R/"input/iter193/base/source.json.gz",
    "--metadata",R/"input/iter193/translation_quotient/metadata.json","--frozen",R/"vendor/round80",
    "--assignment",O/"outer.replay.assignment.dimacs","--candidate",O/"outer.candidate.json","--output",O/"outer.replay.json"])
exact("outer replay assignment",O/"outer.replay.assignment.dimacs",R/"output/iter193/solver/assignment.replay.dimacs")
exact("outer candidate",O/"outer.candidate.json",R/"output/iter193/solver/candidate.json")
semantic("outer semantic replay",O/"outer.replay.json",R/"output/iter193/solver/replay.json")
run("outer_orbit_controls",[py,S/"parent_check_sat_orbit_controls_round102.py","--cnf",R/"input/iter193/translation_quotient/outer.cnf",
    "--metadata",R/"input/iter193/translation_quotient/metadata.json","--source",R/"input/iter193/base/source.json.gz",
    "--assignment",R/"output/iter193/solver/assignment.dimacs","--candidate",R/"output/iter193/solver/candidate.json",
    "--trace",R/"input/iter193/translation_quotient/translation_trace.json.gz","--output",O/"outer.orbit_controls.json"])
exact("outer orbit controls",O/"outer.orbit_controls.json",R/"output/iter193/solver/orbit_controls.json")

for label in ("Xerr","Zerr"):
    run(label+"_assignment",[py,S/"parent_extract_and_check_assignment.py","--cnf",R/f"output/iter193/direct/direct360/{label}.cnf",
        "--solver-log",R/f"output/iter193/direct/solver/{label}.solver.log","--assignment",O/f"{label}.assignment.dimacs",
        "--output",O/f"{label}.assignment_check.json"])
    exact(label+" assignment",O/f"{label}.assignment.dimacs",R/f"output/iter193/direct/solver/{label}.assignment.dimacs")
    exact(label+" assignment check",O/f"{label}.assignment_check.json",R/f"output/iter193/direct/solver/{label}.assignment_check.json")
run("direct_vendor_replay",[py,R/"vendor/round80/src/replay_direct_candidate.py","--root",R/"output/iter193/direct","--output",O/"direct.vendor.json"])
exact("vendor direct replay",O/"direct.vendor.json",R/"output/iter193/direct/direct_verification.json")
run("direct_independent",[py,S/"independent_iter193_direct_audit_round116.py","--root",R,"--output",O/"direct.independent.json"])
exact("independent direct replay",O/"direct.independent.json",R/"output/iter193/direct/independent_audit.json")

run("Xerr_orbit",[py,S/"audit_selector_translation_orbit_round116.py","--sector","Xerr","--candidate",R/"output/iter193/solver/candidate.json",
    "--source",R/"input/iter193/base/source.json.gz","--direct-root",R/"output/iter193/direct",
    "--cnf",R/"output/iter193/direct/direct360/Xerr.cnf","--assignment",R/"output/iter193/direct/solver/Xerr.assignment.dimacs","--output",O/"Xerr.orbit.json"])
exact("Xerr orbit",O/"Xerr.orbit.json",R/"output/iter193/verification/Xerr_translation_orbit.json")
run("Zerr_orbit",[py,S/"audit_selector_translation_orbit_round116.py","--sector","Zerr","--candidate",R/"output/iter193/solver/candidate.json",
    "--source",R/"input/iter193/base/source.json.gz","--direct-root",R/"output/iter193/direct",
    "--cnf",R/"output/iter193/direct/direct360/Zerr.cnf","--assignment",R/"output/iter193/direct/solver/Zerr.assignment.dimacs",
    "--prior-audit",O/"Xerr.orbit.json","--output",O/"Zerr.orbit.json"])
exact("Zerr orbit",O/"Zerr.orbit.json",R/"output/iter193/verification/Zerr_translation_orbit.json")
run("css_iter193",[py,S/"audit_css_duality_iter193_round116.py","--source",R/"input/iter193/base/source.json.gz",
    "--state",R/"input/iter193/base/state.json","--candidate",R/"output/iter193/solver/candidate.json","--output",O/"css.iter193.json"])
exact("iter193 CSS audit",O/"css.iter193.json",R/"output/iter193/verification/css_duality_registry_audit.json")
run("candidate_css_duals",[py,S/"audit_css_dual_selector_orbits_round116.py","--source",R/"input/iter193/base/source.json.gz",
    "--candidate",R/"output/iter193/solver/candidate.json","--direct-root",R/"output/iter193/direct",
    "--x-audit",O/"Xerr.orbit.json","--z-audit",O/"Zerr.orbit.json","--css-audit",O/"css.iter193.json","--output",O/"candidate.css_duals.json"])
exact("candidate CSS duals",O/"candidate.css_duals.json",R/"output/iter193/verification/css_dual_selector_orbits.json")

# Deterministically regenerate the fresh frontier and formulas outside the package.
run("regenerate_iter194_source",[py,S/"advance_css_closed_frontier_round116.py","--source",R/"input/iter193/base/source.json.gz",
    "--state",R/"input/iter193/base/state.json","--candidate",R/"output/iter193/solver/candidate.json","--css-audit",O/"css.iter193.json",
    "--x-audit",O/"Xerr.orbit.json","--z-audit",O/"Zerr.orbit.json","--dual-audit",O/"candidate.css_duals.json",
    "--canonical-yaml",R/"bindings/CIRCDIST.gross.yaml","--scheduler",R/"bindings/SCHEDULER.yaml","--review",R/"bindings/round115_exact_review.md",
    "--prior-manifest",R/"bindings/round114_SHA256SUMS.txt","--proofpilot",R/"bindings/round116_proofpilot_rank.json",
    "--output-source",generated/"source.json.gz","--output-state",generated/"state.json","--output-audit",generated/"advance.json"])
exact("iter194 source regeneration",generated/"source.json.gz",R/"frontier/iter194/source.json.gz")
exact("iter194 state regeneration",generated/"state.json",R/"frontier/iter194/state.json")
exact("iter194 advance audit",generated/"advance.json",R/"frontier/iter194/frontier_advance_audit.json")
run("iter194_translation",[py,S/"parent_check_registry_invariance_round110.py","--source",generated/"source.json.gz","--state",generated/"state.json",
    "--output",generated/"translation.json","--iteration","194","--blocks","814392","--selectors","50832","--assertions","869622"])
exact("iter194 translation closure",generated/"translation.json",R/"frontier/iter194/translation_registry_check.json")
run("iter194_css",[py,S/"audit_css_duality_iter194_round116.py","--source",generated/"source.json.gz","--state",generated/"state.json",
    "--candidate",R/"output/iter193/solver/candidate.json","--output",generated/"css.json"])
exact("iter194 CSS closure",generated/"css.json",R/"frontier/iter194/css_closure_check.json")
(generated/"formula").mkdir()
run("compile_iter194_base",[py,S/"parent_compile_outer_cnf.py","--source",generated/"source.json.gz","--cnf",generated/"formula/outer.cnf",
    "--metadata",generated/"formula/metadata.json","--assertion-map",generated/"formula/assertion_map.jsonl","--definitions",generated/"formula/definitions.json.gz"])
for name in ("outer.cnf","assertion_map.jsonl","definitions.json.gz"):
    exact("iter194 base "+name,generated/"formula"/name,R/"frontier/iter194/formula"/name)
semantic("iter194 base metadata",generated/"formula/metadata.json",R/"frontier/iter194/formula/metadata.json")
run("check_iter194_base",[py,S/"parent_check_outer_encoding.py","--source",generated/"source.json.gz","--cnf",generated/"formula/outer.cnf",
    "--metadata",generated/"formula/metadata.json","--assertion-map",generated/"formula/assertion_map.jsonl","--definitions",generated/"formula/definitions.json.gz",
    "--output",generated/"base_check.json"])
semantic("iter194 base encoding check",generated/"base_check.json",R/"frontier/iter194/base_encoding_check.json")
(generated/"quotient").mkdir()
run("build_order144",[py,S/"build_order144_quotient_round116.py","--base-cnf",generated/"formula/outer.cnf","--base-metadata",generated/"formula/metadata.json",
    "--source",generated/"source.json.gz","--output-cnf",generated/"quotient/outer.cnf","--output-metadata",generated/"quotient/metadata.json",
    "--output-roots",generated/"quotient/roots.jsonl","--output-trace",generated/"quotient/trace.json.gz"])
for name in ("outer.cnf","roots.jsonl","trace.json.gz"):
    exact("order144 "+name,generated/"quotient"/name,R/"frontier/iter194/order144_quotient"/name)
semantic("order144 metadata",generated/"quotient/metadata.json",R/"frontier/iter194/order144_quotient/metadata.json")
run("check_order144",[py,S/"check_order144_quotient_round116.py","--base-cnf",R/"frontier/iter194/formula/outer.cnf",
    "--base-metadata",R/"frontier/iter194/formula/metadata.json","--source",R/"frontier/iter194/source.json.gz",
    "--quotient-cnf",R/"frontier/iter194/order144_quotient/outer.cnf","--quotient-metadata",R/"frontier/iter194/order144_quotient/metadata.json",
    "--roots",R/"frontier/iter194/order144_quotient/roots.jsonl","--trace",R/"frontier/iter194/order144_quotient/trace.json.gz",
    "--base-encoding-check",R/"frontier/iter194/base_encoding_check.json","--translation-registry-check",R/"frontier/iter194/translation_registry_check.json",
    "--css-closure-check",R/"frontier/iter194/css_closure_check.json","--output",O/"order144.check.json"])
semantic("order144 independent check",O/"order144.check.json",R/"frontier/iter194/order144_quotient/check.json")

if not a.skip_sat_streams:
    run("sat_trace_streams",[py,S/"check_sat_trace_streams_round116.py","--root",R,"--output",O/"sat_trace_streams.json"])

summary={"schema":"circdist-gross-round116-sealed-replay-v1","status":"PASS","root":str(R),"output":str(O),
         "parent_pid":os.getpid(),"allow_writable_root":a.allow_writable_root,"sat_streams_skipped":a.skip_sat_streams,
         "strict_serial":True,"max_simultaneous_children":1,"runs":runs,"run_count":len(runs),"comparisons":comparisons,
         "comparison_count":len(comparisons),"all_children_reaped":True,"detached_children":0,"timeouts_configured":0,
         "timeouts_triggered":0,"solver_invocations":0,"fresh_iter194_remained_unstarted":True}
(O/"summary.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":"PASS","runs":len(runs),"comparisons":len(comparisons),"sat_streams_skipped":a.skip_sat_streams},sort_keys=True))
