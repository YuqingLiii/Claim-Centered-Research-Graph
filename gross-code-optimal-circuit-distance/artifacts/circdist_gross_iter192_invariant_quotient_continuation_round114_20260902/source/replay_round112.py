#!/usr/bin/env python3
"""Non-mutating, strict-serial replay for the Round112 package."""
from pathlib import Path, PurePosixPath
import argparse, datetime, gzip, hashlib, json, os, signal, subprocess, tempfile, time

CHUNK = 8 << 20

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(CHUNK), b""):
            h.update(b)
    return h.hexdigest()

def load(path): return json.loads(Path(path).read_text())

def normalized(value):
    if isinstance(value, dict):
        return {k: normalized(v) for k, v in value.items() if k not in {
            "seconds", "wall_seconds", "compile_seconds", "started_unix", "ended_unix",
            "started_utc", "ended_utc", "child_pid", "parent_pid", "runner_pid"}}
    if isinstance(value, list): return [normalized(x) for x in value]
    return value

ap = argparse.ArgumentParser()
ap.add_argument("--package", type=Path, required=True)
ap.add_argument("--repo", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
ap.add_argument("--mode", choices=("preseal", "installed"), required=True)
a = ap.parse_args()
P, R, O = a.package.resolve(), a.repo.resolve(), a.output.resolve()
assert P.is_dir() and R.is_dir()
assert P not in O.parents and O != P
O.parent.mkdir(parents=True, exist_ok=True)
run_root = O.parent / (O.stem + ".work")
if run_root.exists():
    import shutil; shutil.rmtree(run_root)
run_root.mkdir(parents=True)
tmp = run_root / "tmp"; tmp.mkdir()
env = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8",
       "PYTHONDONTWRITEBYTECODE": "1", "PYTHONPATH": str(P / "python/site-packages"), "TMPDIR": str(tmp)}
runs = []

def run(name, command, expected=0, timeout=3600):
    command = [str(x) for x in command]
    outp, errp = run_root / f"{name}.stdout", run_root / f"{name}.stderr"
    start = time.time()
    with outp.open("wb") as out, errp.open("wb") as err:
        child = subprocess.Popen(command, cwd=P, env=env, stdout=out, stderr=err, start_new_session=False)
        print(json.dumps({"event":"START","name":name,"child_pid":child.pid},sort_keys=True), flush=True)
        timed = term = killed = False
        try: rc = child.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed = term = True; child.send_signal(signal.SIGTERM)
            try: rc = child.wait(timeout=15)
            except subprocess.TimeoutExpired:
                killed = True; child.kill(); rc = child.wait()
    end = time.time()
    row = {"name":name,"argv":command,"cwd":str(P),"environment":env,"parent_pid":os.getpid(),
           "child_pid":child.pid,"returncode":rc,"expected_returncode":expected,
           "returncode_matches":rc==expected and not timed,"started_unix":start,"ended_unix":end,
           "started_utc":datetime.datetime.fromtimestamp(start,datetime.timezone.utc).isoformat(),
           "ended_utc":datetime.datetime.fromtimestamp(end,datetime.timezone.utc).isoformat(),
           "wall_seconds":round(end-start,6),"stdout_sha256":sha(outp),"stdout_bytes":outp.stat().st_size,
           "stderr_sha256":sha(errp),"stderr_bytes":errp.stat().st_size,"timed_out":timed,
           "term_sent":term,"kill_sent":killed,"reaped":True,"detached":False}
    runs.append(row); print(json.dumps({"event":"END","name":name,"child_pid":child.pid,"rc":rc,"seconds":row["wall_seconds"]},sort_keys=True),flush=True)
    assert row["returncode_matches"], (name,rc,outp.read_bytes()[-2000:],errp.read_bytes()[-2000:])
    return row

def compare_json(generated, retained):
    assert normalized(load(generated)) == normalized(load(retained)), (generated, retained)

expected = {
    P/"bindings/SCHEDULER.yaml": "e5b55acfbbc21380b28aa6758c6e9cf180491a51af0b1bf93bd597fd930be196",
    P/"bindings/CIRCDIST.gross.yaml": "7cc45da6ae90deb2f44aee40fa28a17c5f0a74a36970f4cef795d6ae317883d4",
    P/"PROPOSED_CIRCDIST.gross.yaml": "7cc45da6ae90deb2f44aee40fa28a17c5f0a74a36970f4cef795d6ae317883d4",
    P/"bindings/round111_exact_review.md": "36f2fdac0c74a0bfa3f67013590e21fd24c445295c488edc95c2114edef72e9e",
    P/"bindings/round110_SHA256SUMS.txt": "8ce014a0bc1b4273cec02e2af7d9da54691290dd35a82d7c3bfe6c522a031bc5",
    P/"input/iter191_full_invariant/source.json.gz": "0b0ac7e6daa69d8d3ab1b98b7228c43690a5406c52defe57e46027b185984a47",
    P/"input/iter191_full_invariant/state.json": "6059554d307e7c503bd1792dd77718a205346f5dce243e719ae057f402cf6c9f",
    P/"reconstructed/iter191_full_invariant/formula/outer.cnf": "d1e68e88eb4c22ffda58d3a1c73cb7dbf6082690c594e8c538f8cc70c432e223",
    P/"reconstructed/iter191_full_invariant_quotient/outer.cnf": "30ce7d14d96349e61d7105255cddc8899b8927ce728dfd147b641c75c97fe10f",
    P/"frontier/iter192_full_invariant/source.json.gz": "89ed11977cacaed4f46a8c0756fef77a9706a2f3ce65d6ec1b496424fb9533f3",
    P/"frontier/iter192_full_invariant/state.json": "e4085c5a776561bfc136d67f64988c31c0e26b063afd715d61a836a2f6ff06f1",
    P/"frontier/iter192_full_invariant/formula/outer.cnf": "3388c5f4927fecce693237cf0b1090d8c7e9b965067e70f10f54c85febb9393b",
    P/"frontier/iter192_full_invariant_quotient/outer.cnf": "00baea753d8ef3d47bbd1e3ca149d39bd2a36ef6475e957633d00770c0071e71",
}
for path, digest in expected.items(): assert sha(path) == digest, path
assert sha(R/"operations/circdist/SCHEDULER.yaml") == expected[P/"bindings/SCHEDULER.yaml"]
assert sha(R/"circdist/proof-dag/nodes/CIRCDIST.gross.yaml") == expected[P/"bindings/CIRCDIST.gross.yaml"]
assert sha(R/"circdist/reviews/circdist_gross_iter190_invariant_quotient_continuation_round110_exact_review_round111_20260902.md") == expected[P/"bindings/round111_exact_review.md"]
assert sha(R/"circdist/artifacts/circdist_gross_iter190_invariant_quotient_continuation_round110_20260902/SHA256SUMS.txt") == expected[P/"bindings/round110_SHA256SUMS.txt"]
assert not list(P.glob("solver/**/*.drat")) and not list(P.glob("batch/**/*.drat"))

# Exact reconstruction remains byte-bound to the reviewed predecessor (timing-only metadata excluded).
pred = R/"circdist/artifacts/circdist_gross_iter190_invariant_quotient_continuation_round110_20260902/frontier"
for sub, names in (("iter191_full_invariant/formula",("outer.cnf","assertion_map.jsonl","definitions.json.gz")),
                   ("iter191_full_invariant_quotient",("outer.cnf","translation_roots.jsonl","translation_trace.json.gz"))):
    for name in names: assert sha(P/"reconstructed"/sub/name) == sha(pred/sub/name)
for sub in ("iter191_full_invariant/formula","iter191_full_invariant_quotient"):
    assert normalized(load(P/"reconstructed"/sub/"metadata.json")) == normalized(load(pred/sub/"metadata.json"))

# Mandatory complete outer assignment and decoded model/orbit controls.
g = run_root/"outer_assignment.json"
run("outer_assignment_all_clauses", ["/usr/bin/python3",P/"source/extract_and_check_assignment.py","--cnf",P/"reconstructed/iter191_full_invariant_quotient/outer.cnf","--solver-log",P/"solver/iter191/solver.log","--assignment",P/"solver/iter191/assignment.dimacs","--output",g], timeout=1800)
compare_json(g,P/"solver/iter191/assignment_check.json")
gc, gr = run_root/"candidate.json", run_root/"outer_replay.json"
run("outer_model_schedule_replay", ["/usr/bin/python3",P/"source/verify_outer_sat_model.py","--solver-log",P/"solver/iter191/solver.log","--cnf",P/"reconstructed/iter191_full_invariant_quotient/outer.cnf","--source",P/"input/iter191_full_invariant/source.json.gz","--metadata",P/"reconstructed/iter191_full_invariant_quotient/metadata.json","--frozen",P/"vendor/round80","--assignment",P/"solver/iter191/assignment.replay.dimacs","--candidate",gc,"--output",gr], timeout=1800)
assert normalized(load(gr)) == normalized(load(P/"solver/iter191/replay.json"))
assert sha(gc) == sha(P/"solver/iter191/candidate.json")
go = run_root/"orbit_controls.json"
run("outer_orbit_lex_controls", ["/usr/bin/python3",P/"source/check_sat_orbit_controls_round102.py","--cnf",P/"reconstructed/iter191_full_invariant_quotient/outer.cnf","--metadata",P/"reconstructed/iter191_full_invariant_quotient/metadata.json","--source",P/"input/iter191_full_invariant/source.json.gz","--assignment",P/"solver/iter191/assignment.dimacs","--candidate",P/"solver/iter191/candidate.json","--trace",P/"reconstructed/iter191_full_invariant_quotient/translation_trace.json.gz","--output",go], timeout=1800)
compare_json(go,P/"verification/iter191_sat_orbit_controls.json")

# Vendor and independent physical direct replays.
gd = run_root/"direct_vendor.json"
run("direct_vendor_replay", ["/usr/bin/python3",P/"vendor/round80/src/replay_direct_candidate.py","--root",P/"solver/iter191/direct","--output",gd], timeout=1800)
compare_json(gd,P/"solver/iter191/direct/direct_verification.json")
gi = run_root/"direct_independent.json"
run("direct_independent_replay", ["/usr/bin/python3",P/"source/independent_iter191_direct_audit_round112.py","--root",P,"--output",gi], timeout=1800)
compare_json(gi,P/"verification/iter191_direct_independent_audit.json")

# Eight accepted parents, each complete CNF assignment and all 72 translated physical replays.
audits = []
for sector in ("Xerr","Zerr"):
    for attempt in range(1,5):
        retained = P/f"batch/{sector}/attempt{attempt:02}/audit.json"
        out = run_root/f"audit_{sector}_{attempt:02}.json"
        if attempt == 1:
            cnf = P/f"solver/iter191/direct/direct360/{sector}.cnf"
            assignment = P/f"solver/iter191/direct/solver/{sector}.assignment.dimacs"
        else:
            cnf = P/f"batch/{sector}/attempt{attempt:02}/query.cnf"
            assignment = P/f"batch/{sector}/attempt{attempt:02}/assignment.dimacs"
        cmd = ["/usr/bin/python3",P/"source/audit_batch_attempt_round112.py","--sector",sector,"--attempt",attempt,
               "--candidate",P/"solver/iter191/candidate.json","--source",P/"input/iter191_full_invariant/source.json.gz",
               "--direct-root",P/"solver/iter191/direct","--cnf",cnf,"--assignment",assignment]
        for prior in load(retained).get("prior_audits",[]): cmd += ["--prior-audit",P/prior]
        # Retained audit schema does not store its argv; use the exact prior list from process record.
        proc = load(P/f"logs/process/batch_{sector}_attempt{attempt:02}_audit.json")
        argv = proc["argv"]
        for i,x in enumerate(argv):
            if x == "--prior-audit": cmd += ["--prior-audit",P/argv[i+1]]
        cmd += ["--output",out]
        run(f"batch_{sector}_{attempt:02}_replay",cmd,timeout=1800)
        compare_json(out,retained); audits.append(retained)

# Deterministically regenerate the exact unstarted frontier and then recheck it.
fs, fst, fa = run_root/"iter192.source.json.gz", run_root/"iter192.state.json", run_root/"iter192.orbit_audit.json"
cmd = ["/usr/bin/python3",P/"source/advance_batch_frontier_round112.py","--source",P/"input/iter191_full_invariant/source.json.gz","--state",P/"input/iter191_full_invariant/state.json","--plan",P/"batch/BATCH_PLAN.json","--batch-result",P/"batch/BATCH_RESULT.json"]
for x in audits: cmd += ["--audit",x.relative_to(P)]
cmd += ["--output-source",fs,"--output-state",fst,"--output-audit",fa]
run("regenerate_iter192_atomic_frontier",cmd,timeout=1800)
assert sha(fs)==sha(P/"frontier/iter192_full_invariant/source.json.gz")
assert sha(fst)==sha(P/"frontier/iter192_full_invariant/state.json")
assert sha(fa)==sha(P/"frontier/iter192_full_invariant/orbit_audit.json")
rg = run_root/"registry.json"
run("iter192_full_registry_invariance",["/usr/bin/python3",P/"source/check_registry_invariance_round110.py","--source",fs,"--state",fst,"--output",rg,"--iteration",192,"--blocks",517140,"--selectors",25164,"--assertions",546702],timeout=1800)
compare_json(rg,P/"verification/iter192_registry_invariance.json")
be = run_root/"base_encoding.json"
run("iter192_base_encoding",["/usr/bin/python3",P/"source/check_outer_encoding.py","--source",fs,"--cnf",P/"frontier/iter192_full_invariant/formula/outer.cnf","--metadata",P/"frontier/iter192_full_invariant/formula/metadata.json","--assertion-map",P/"frontier/iter192_full_invariant/formula/assertion_map.jsonl","--definitions",P/"frontier/iter192_full_invariant/formula/definitions.json.gz","--output",be],timeout=1800)
compare_json(be,P/"verification/iter192_base_encoding.json")
qc = run_root/"quotient_check.json"
run("iter192_quotient_check",["/usr/bin/python3",P/"source/check_translation_quotient_round102.py","--base-cnf",P/"frontier/iter192_full_invariant/formula/outer.cnf","--base-metadata",P/"frontier/iter192_full_invariant/formula/metadata.json","--source",fs,"--quotient-cnf",P/"frontier/iter192_full_invariant_quotient/outer.cnf","--quotient-metadata",P/"frontier/iter192_full_invariant_quotient/metadata.json","--roots",P/"frontier/iter192_full_invariant_quotient/translation_roots.jsonl","--trace",P/"frontier/iter192_full_invariant_quotient/translation_trace.json.gz","--vendor",P/"vendor/round80","--candidate",P/"solver/iter191/candidate.json","--direct",P/"solver/iter191/direct/direct_verification.json","--output",qc],timeout=1800)
compare_json(qc,P/"verification/iter192_quotient_check.json")

# Every retained SAT trace round trips to its recorded raw stream.
stream_rows=[]
for desc in sorted(list(P.glob("solver/**/*.drat.stream.json"))+list(P.glob("batch/**/*.drat.stream.json"))):
    d=load(desc); gz=P/d["gzip_path"]; h=hashlib.sha256(); size=lf=empty=0; pending=b""
    with gzip.open(gz,"rb") as f:
        for b in iter(lambda:f.read(CHUNK),b""):
            h.update(b);size+=len(b);lf+=b.count(b"\n"); lines=(pending+b).split(b"\n");pending=lines.pop();empty+=sum(x.strip()==b"0" for x in lines)
    if pending: empty += pending.strip()==b"0"
    assert (h.hexdigest(),size,lf,empty)==(d["raw_sha256"],d["raw_bytes"],d["raw_lf_count"],d["raw_empty_clause_lines"])
    assert sha(gz)==d["gzip_sha256"]; stream_rows.append(d)
assert len(stream_rows)==9 and sum(x["raw_empty_clause_lines"] for x in stream_rows)==0

pc=run_root/"proof_controls.json"
run("proof_controls",["/usr/bin/python3",P/"source/check_proof_controls.py","--root",P,"--output",pc],timeout=300)
pco=load(pc); assert all(pco[k] for k in ("valid_drat_accepted","generated_lrat_accepted","corrupt_drat_rejected","truncated_drat_rejected","corrupt_lrat_rejected","truncated_lrat_rejected"))
assert all(x["reaped"] and not x["detached"] and not x["timed_out"] for x in pco["runs"])

# Solver/process launch audit and optional sealed manifests/modes.
for name in ("solve_iter191_quotient","solve_iter191_Xerr","solve_iter191_Zerr"):
    d=load(P/f"logs/process/{name}.json"); assert d["reaped"] and not d["detached"] and not d["timed_out"] and d["returncode"]==10 and d["argv"][-1].endswith(".drat")
for sector in ("Xerr","Zerr"):
    for attempt in range(2,5):
        d=load(P/f"logs/process/batch_{sector}_attempt{attempt:02}_solver.json"); assert d["reaped"] and not d["detached"] and not d["timed_out"] and d["returncode"]==10 and d["argv"][-1].endswith(".drat")

def verify_manifest(name):
    seen=[]
    for line in (P/name).read_text().splitlines():
        digest,sep,rel=line.partition("  "); pos=PurePosixPath(rel)
        assert sep and rel==pos.as_posix() and not pos.is_absolute() and ".." not in pos.parts and rel not in seen
        assert sha(P/rel)==digest;seen.append(rel)
    assert seen==sorted(seen);return seen
seal={"present":False}
if (P/"SHA256SUMS.txt").exists():
    payload=verify_manifest("PAYLOAD_SHA256SUMS.txt"); rootrows=verify_manifest("SHA256SUMS.txt")
    actual=sorted(x.relative_to(P).as_posix() for x in P.rglob("*") if x.is_file())
    assert set(rootrows)==set(actual)-{"SHA256SUMS.txt"}
    seal={"present":True,"root_sha256":sha(P/"SHA256SUMS.txt"),"root_rows":len(rootrows),"payload_rows":len(payload)}
if a.mode=="installed":
    assert seal["present"]
    objects=[P,*P.rglob("*")]; assert not [x for x in objects if x.is_symlink()]
    assert not [x for x in objects if x.stat().st_mode & 0o222]

out={"schema":"circdist-gross-round112-replay-v1","status":"PASS","mode":a.mode,"package":str(P),
     "strict_serial":True,"runs":runs,"child_count":len(runs),"all_children_reaped":all(x["reaped"] for x in runs),
     "detached_processes":0,"timed_out_processes":0,"mandatory_quotient":"SATISFIABLE",
     "direct":{"Xerr":"SATISFIABLE","Zerr":"SATISFIABLE"},"batch_parents":8,"translated_replays":576,
     "iter192_unstarted":True,"trace_streams":9,"trace_raw_bytes":sum(x["raw_bytes"] for x in stream_rows),
     "trace_gzip_bytes":sum(x["gzip_bytes"] for x in stream_rows),"proof_controls":"PASS","seal":seal}
O.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps({k:out[k] for k in ("status","mode","child_count","mandatory_quotient","direct","batch_parents","translated_replays","trace_streams","proof_controls","seal")},sort_keys=True))
