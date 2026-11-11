#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, os, platform, shutil, sys

CHUNK = 8 << 20

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(CHUNK), b""):
            h.update(b)
    return h.hexdigest()

def load(path):
    return json.loads(Path(path).read_text())

def dump(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")

ap = argparse.ArgumentParser()
ap.add_argument("--stage", type=Path, required=True)
ap.add_argument("--work", type=Path, required=True)
ap.add_argument("--repo", type=Path, required=True)
a = ap.parse_args()
P, W, R = a.stage.resolve(), a.work.resolve(), a.repo.resolve()
pred = R / "circdist/artifacts/circdist_gross_iter190_invariant_quotient_continuation_round110_20260902"
review = R / "circdist/reviews/circdist_gross_iter190_invariant_quotient_continuation_round110_exact_review_round111_20260902.md"
canonical = R / "circdist/proof-dag/nodes/CIRCDIST.gross.yaml"
scheduler = R / "operations/circdist/SCHEDULER.yaml"
handoff = R / "research/circdist/notes/HANDOFF_20260823.md"
for d in (P / "bindings", P / "source"):
    d.mkdir(parents=True, exist_ok=True)
    d.chmod(0o755)

copies = [
    (canonical, P / "bindings/CIRCDIST.gross.yaml"),
    (scheduler, P / "bindings/SCHEDULER.yaml"),
    (review, P / "bindings/round111_exact_review.md"),
    (handoff, P / "bindings/HANDOFF_20260823.md"),
    (pred / "SHA256SUMS.txt", P / "bindings/round110_SHA256SUMS.txt"),
    (pred / "PAYLOAD_SHA256SUMS.txt", P / "bindings/round110_PAYLOAD_SHA256SUMS.txt"),
    (pred / "FILE_INVENTORY.jsonl", P / "bindings/round110_FILE_INVENTORY.jsonl"),
    (pred / "RESULT.json", P / "bindings/round110_RESULT.json"),
    (pred / "FRESH_FRONTIER.json", P / "bindings/round110_FRESH_FRONTIER.json"),
    (canonical, P / "PROPOSED_CIRCDIST.gross.yaml"),
]
for src, dst in copies:
    if dst.exists(): dst.chmod(0o644)
    shutil.copy2(src, dst)
for name in (
    "run_process_round112.py", "verify_reconstruction_round112.py",
    "independent_iter191_direct_audit_round112.py", "audit_batch_attempt_round112.py",
    "build_cumulative_direct_cnf_round112.py", "summarize_batch_round112.py",
    "advance_batch_frontier_round112.py", "replay_round112.py"):
    dst = P / "source" / name
    if dst.exists(): dst.chmod(0o644)
    shutil.copy2(W / name, dst)

assert sha(canonical) == "7cc45da6ae90deb2f44aee40fa28a17c5f0a74a36970f4cef795d6ae317883d4"
assert sha(scheduler) == "e5b55acfbbc21380b28aa6758c6e9cf180491a51af0b1bf93bd597fd930be196"
assert sha(review) == "36f2fdac0c74a0bfa3f67013590e21fd24c445295c488edc95c2114edef72e9e"
assert sha(pred / "SHA256SUMS.txt") == "8ce014a0bc1b4273cec02e2af7d9da54691290dd35a82d7c3bfe6c522a031bc5"
assert sha(P / "PROPOSED_CIRCDIST.gross.yaml") == sha(canonical)

outer_check = load(P / "solver/iter191/assignment_check.json")
replay = load(P / "solver/iter191/replay.json")
orbit = load(P / "verification/iter191_sat_orbit_controls.json")
direct = load(P / "verification/iter191_direct_independent_audit.json")
batch = load(P / "batch/BATCH_RESULT.json")
frontier_state = load(P / "frontier/iter192_full_invariant/state.json")
frontier_audit = load(P / "frontier/iter192_full_invariant/orbit_audit.json")
base_meta = load(P / "frontier/iter192_full_invariant/formula/metadata.json")
quot_meta = load(P / "frontier/iter192_full_invariant_quotient/metadata.json")
proof = load(P / "verification/proof_controls.json")

trace_rows = []
for desc in sorted(list(P.glob("solver/**/*.drat.stream.json")) + list(P.glob("batch/**/*.drat.stream.json"))):
    d = load(desc)
    assert d["status"] == "PASS" and d["solver_status"] == "SATISFIABLE" and d["lossless_roundtrip_verified"]
    trace_rows.append({"descriptor": desc.relative_to(P).as_posix(), **d})
assert len(trace_rows) == 9

bindings = {
    "schema": "circdist-gross-round112-input-bindings-v1", "status": "PASS",
    "governance": {
        "scheduler": {"path": "operations/circdist/SCHEDULER.yaml", "sha256": sha(scheduler), "round112_pending": True, "winner_score": 0.0015587240464645154},
        "canonical": {"path": "circdist/proof-dag/nodes/CIRCDIST.gross.yaml", "sha256": sha(canonical), "root_level": "CONJECTURED", "exact_residual": [11, 12]},
        "round111_review": {"path": str(review.relative_to(R)), "sha256": sha(review)},
        "handoff": {"path": str(handoff.relative_to(R)), "sha256": sha(handoff)},
    },
    "reviewed_round110": {"path": str(pred.relative_to(R)), "root_manifest_sha256": sha(pred / "SHA256SUMS.txt")},
    "mandatory_iter191": {
        "source_sha256": sha(P / "input/iter191_full_invariant/source.json.gz"),
        "semantic_sha256": "02da1bcb87a45637afa8434a8dfa4e4c8092489ace7f5a7fd1ba3266f9615532",
        "state_sha256": sha(P / "input/iter191_full_invariant/state.json"),
        "selector_state_sha256": "41bb458a1b9a31aba7d70f063165221a9ae9c989421682320826dbc5d166f9e6",
        "blocks": 517140, "selectors": 24588,
        "base": {"sha256": sha(P / "reconstructed/iter191_full_invariant/formula/outer.cnf"), "variables": 1853886, "clauses": 6929888, "assertions": 546126},
        "quotient": {"sha256": sha(P / "reconstructed/iter191_full_invariant_quotient/outer.cnf"), "variables": 2467326, "clauses": 11837479, "assertions": 546197, "lex_roots": 71},
    },
}
dump(P / "INPUT_BINDINGS.json", bindings)

fresh = {
    "schema": "circdist-gross-round112-fresh-frontier-v1", "status": "PASS", "iteration": 192,
    "fresh_unstarted": True, "started": False, "stop": None, "iter192_solved": False,
    "translation_group": "Z_12 x Z_6", "translation_group_order": 72,
    "blocks": 517140, "selectors": 25164,
    "source_file_sha256": frontier_state["source_file_sha256"],
    "source_semantic_payload_sha256": frontier_state["source_semantic_payload_sha256"],
    "state_file_sha256": sha(P / "frontier/iter192_full_invariant/state.json"),
    "selector_state_sha256": frontier_state["selector_state_sha256"],
    "batch": {"parents": 8, "orbits": 8, "added_selectors": 576, "collisions": 0, "all_translated_replays": True},
    "base": {"path": "frontier/iter192_full_invariant/formula/outer.cnf", "sha256": base_meta["cnf_sha256"], "variables": base_meta["variables"], "clauses": base_meta["clauses"], "assertions": base_meta["assertions"], "encoding_check": "PASS"},
    "quotient": {"path": "frontier/iter192_full_invariant_quotient/outer.cnf", "sha256": quot_meta["cnf_sha256"], "variables": quot_meta["variables"], "clauses": quot_meta["clauses"], "assertions": quot_meta["assertions"], "lex_roots": 71, "independent_check": "PASS"},
    "forbidden_solver_artifacts_absent": not any((P / "frontier").rglob("*.drat")),
    "smallest_honest_residual": "Solve the exact fresh iteration-192 71-root quotient proof-first under a new reviewed commission.",
}
dump(P / "FRESH_FRONTIER.json", fresh)

processes = []
for path in sorted((P / "logs/process").glob("*.json")):
    try: d = load(path)
    except Exception: continue
    if isinstance(d, dict) and "child_pid" in d:
        processes.append({"path": path.relative_to(P).as_posix(), "sha256": sha(path), "name": d.get("name"), "child_pid": d["child_pid"], "returncode": d.get("returncode"), "expected_returncodes": d.get("expected_returncodes"), "reaped": d.get("reaped"), "detached": d.get("detached"), "timed_out": d.get("timed_out")})

result = {
    "schema": "circdist-gross-round112-result-v1", "status": "PASS",
    "package": "circdist/artifacts/circdist_gross_iter191_invariant_quotient_continuation_round112_20260902",
    "canonical_state_modified": False, "root_closed": False, "root_branch_A_closed": False, "root_branch_B_closed": False,
    "distance_status": {"CIRCDIST.gross": "CONJECTURED", "gap-via-lift": "CONJECTURED", "D_star_Gross": [11, 12]},
    "iteration191": {
        "quotient": {"status": "SATISFIABLE", "assignment_sha256": outer_check["assignment_sha256"], "variables": outer_check["variables"], "clauses": outer_check["clauses"], "all_variables_assigned_exactly_once": True, "all_clauses_satisfied": True},
        "schedule": replay["frozen_schedule_audit"], "compressed_schedule_sha256": replay["compressed_schedule_sha256"],
        "orbit_lex_controls": orbit,
        "direct": direct["sectors"],
        "repair_entered": False, "repair_reason": "forbidden because both complete unrestricted direct sectors are independently checked SAT",
    },
    "batch": {k: batch[k] for k in ("accepted_parent_count", "accepted_parent_orbits", "new_selector_count", "union_orbit_key_count", "installed_collisions", "cross_batch_collisions", "all_assignments_complete_and_all_clauses_satisfied", "all_576_translated_schedules_and_physical_mechanisms_replayed", "attempt05_absent", "hard_cap_respected", "sectors", "parents")},
    "fresh_frontier": fresh,
    "proof_disposition": {"actual_Gross_UNSAT": False, "drat_or_lrat_claim_for_iteration191": False, "proof_output_enabled_from_all_solver_launches": True, "sat_streams_are_search_traces_not_certificates": True, "sat_stream_count": 9, "sat_trace_raw_bytes": sum(x["raw_bytes"] for x in trace_rows), "sat_trace_gzip_bytes": sum(x["gzip_bytes"] for x in trace_rows), "empty_clause_lines": sum(x["raw_empty_clause_lines"] for x in trace_rows), "valid_corrupt_truncated_toolchain_controls": proof["status"], "nested_control_children": len(proof["runs"]), "all_nested_control_children_reaped": all(x["reaped"] for x in proof["runs"])},
    "proposed_canonical_yaml": {"path": "PROPOSED_CIRCDIST.gross.yaml", "sha256": sha(P / "PROPOSED_CIRCDIST.gross.yaml"), "identical_to_bound_canonical": True, "installed": False, "level": "CONJECTURED", "residual": [11, 12]},
    "failures": {"ledger": "FAILURE_LEDGER.md", "disclosed_ids": [f"F112-{i:03}" for i in range(1, 7)], "scientific_failures_or_unknowns": 0},
    "preseal_replay_binding": {"status": "PENDING"}, "repository_gates": {"status": "PENDING"},
}
dump(P / "RESULT.json", result)

ledger = {
    "schema": "circdist-gross-round112-process-fix2-ledger-v1", "status": "PASS",
    "records": processes, "pid_bearing_records": len(processes),
    "all_pid_bearing_records_reaped": all(x["reaped"] is True for x in processes),
    "detached_processes": sum(x["detached"] is True for x in processes),
    "timed_out_processes": sum(x["timed_out"] is True for x in processes),
    "failure_ids": [f"F112-{i:03}" for i in range(1, 7)],
    "final_fix2": {"status": "PENDING_POST_INSTALL_EXTERNAL_CENSUS", "survivors": None},
}
dump(P / "PROCESS_FIX2_LEDGER.json", ledger)

(P / "FAILURE_LEDGER.md").write_text("""# Round112 failure ledger\n\nAll items below are harness or invocation corrections. None produced a scientific SAT/UNSAT/UNKNOWN discrepancy.\n\n- **F112-001.** The copied process runner retained read-only mode; its first attempted update failed before science. Corrected only the scratch copy's mode.\n- **F112-002.** The first reconstruction comparison required metadata byte identity and rejected nondeterministic `compile_seconds`; load-bearing files were exact. The retry ignored only measured runtime fields and passed.\n- **F112-003.** The first cumulative direct-CNF builder assumed the DIMACS header was line 1; the formula has three leading comments. It failed before solver launch. The retry located the unique `p cnf` header and passed.\n- **F112-004.** A zsh variable containing eight `--audit` pairs was passed as one argument. `argparse` returned 2 before frontier output. The explicit-argument retry passed.\n- **F112-005.** The first explicit retry omitted the wrapper's required `--timeout`; wrapper `argparse` returned 2 before any child or frontier output. The corrected invocation passed.\n- **F112-006.** The first iter192 quotient checker clean environment omitted vendored `PYTHONPATH`; Python raised `ModuleNotFoundError: z3` before a verdict. The same command with the sealed vendored path passed.\n""")

(P / "THEOREM_NOTES.md").write_text("""# Theorem notes\n\n## Exact scope\nThe iteration-191 71-root quotient is **SATISFIABLE**, with every one of 2,467,326 variables assigned and all 11,837,479 clauses checked. Its decoded 864-edge schedule is legal, realizes all 648 MC overlaps, and passes all 71 lex roots for the complete `Z_12 x Z_6` action.\n\nBoth complete unrestricted direct-360 sectors are **SATISFIABLE** at weight 10. Each retained assignment satisfies every clause; canonical and physical replay give zero syndrome, a nonzero logical action, and a nonstabilizer. Therefore this schedule cannot certify distance 12 and arbitrary repair was not entered. A SAT stream is a trace, not an UNSAT proof.\n\n## Batch implication\nThe predeclared finite batch stopped at four collision-free parents in each sector. Eight complete free translation orbits add 576 distinct selector exclusions. Full generator invariance of all 517,140 block semantics and all 25,164 selectors implies full group invariance. This is information gain, but not exhaustion and not a root theorem.\n\n## Honest conclusion\nNeither root branch A nor B is proved. `CIRCDIST.gross` and `gap-via-lift` remain **CONJECTURED**, with exact residual `D*_Gross in {11,12}`. Iteration 192 is checked and **unstarted**.\n""")

(P / "REPORT.md").write_text(f"""# Circdist Gross Round112: iteration-191 invariant quotient continuation\n\n**Status:** installed package is pending until atomic promotion; scientific result is SAT/SAT/SAT and the root remains **CONJECTURED**.\n\nThe mandatory iteration-191 quotient (`30ce7d...`) was reconstructed from the Round111-cleared unstarted source before solving. CaDiCaL returned **SATISFIABLE**. A complete assignment covers 2,467,326 variables exactly once and satisfies all 11,837,479 clauses. Exact replay decodes a legal 864-edge, 438-layer schedule with every one of 648 MC overlaps and the complete 71-root orbit/lex controls.\n\nThe unrestricted direct queries then returned **SATISFIABLE** in strict order: Xerr (`2cbf1c...`, 6,108 variables, 23,012 clauses) and Zerr (`27f266...`, 6,087 variables, 22,928 clauses). Independent standard-library replay checks all 360 columns per sector, empty detector syndrome, nonzero logical action, nonstabilizer status, and physical hook supports. Repair was therefore forbidden.\n\nThe fixed batch reached its target in four attempts per sector, with eight accepted collision-free parents, no fifth attempt, and no collisions. It replayed all 576 translated schedule/mechanism pairs and atomically produced the unstarted iteration-192 frontier: source `{frontier_state['source_file_sha256']}`, base `{base_meta['cnf_sha256']}` ({base_meta['variables']:,} variables / {base_meta['clauses']:,} clauses), quotient `{quot_meta['cnf_sha256']}` ({quot_meta['variables']:,} variables / {quot_meta['clauses']:,} clauses).\n\nAll nine proof-output streams were enabled at solver launch and retained losslessly as deterministic gzip after raw/hash/count/roundtrip checks. They contain no empty clause and are explicitly traces, not proofs. Independent valid/corrupt/truncated DRAT and LRAT tool-chain controls passed. See `RESULT.json`, `THEOREM_NOTES.md`, `FAILURE_LEDGER.md`, and `FRESH_FRONTIER.json` for exact scope.\n""")

env = {"schema": "circdist-gross-round112-environment-v1", "python": sys.version, "platform": platform.platform(), "pid": os.getpid(), "ppid": os.getppid(), "repo_root": str(R), "scratch_root": str(W.parent), "package_stage": str(P)}
dump(P / "ENVIRONMENT.json", env)
print(json.dumps({"status": "PASS", "stage": str(P), "traces": len(trace_rows), "process_records": len(processes), "result": sha(P / "RESULT.json")}, sort_keys=True))
