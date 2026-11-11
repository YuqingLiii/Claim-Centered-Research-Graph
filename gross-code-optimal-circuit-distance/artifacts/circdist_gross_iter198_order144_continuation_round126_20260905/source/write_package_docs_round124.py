#!/usr/bin/env python3
"""Write the auditable Round124 proposer result and public report."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load(path: Path):
    return json.loads(path.read_text())


p = argparse.ArgumentParser()
p.add_argument("--root", type=Path, required=True)
p.add_argument("--work", type=Path, required=True)
a = p.parse_args()
R, W = a.root.resolve(), a.work.resolve()
I, E, F = R / "input/iter197", R / "output/iter197", R / "frontier/iter198"
assert R.is_dir()

expected_bindings = {
    "bindings/SCHEDULER.yaml": "614e571512506e8b5e0306fbd01fa52077a98eef449939fb784bfe06d4f4e6f3",
    "bindings/round124_proofpilot_rank.json": "c363db975d3436eccbdbc57e6d952bee52bf49f0c010484369cb5c0ad46ddbdf",
    "bindings/CIRCDIST.gross.yaml": "1ff87b5e421e72c8df4557f23efac5becbf1da35cd6077577b8c211ce5a2b140",
    "bindings/round123_exact_review.md": "436ee1dc38e0506d0048dd07084417964637de50de848ed076449fdf0311b0cb",
    "bindings/round122_parent/SHA256SUMS.txt": "8871b88af19ea26b051f9fc1cdeea12e2fcb00dc43e486710748e2493ec36a28",
    "input/iter197/source.json.gz": "6ce8b8593fabc80ce0917f342126e351da30114802765a46773da348115aec44",
    "input/iter197/state.json": "cd005e436ff92c66badefb5a30e83531d81d9339bfbc047ebbdbb32627eb1ed0",
    "input/iter197/formula/outer.cnf": "f46bc3862e2c4db10570d73d5a364750fa1892d90ecd0fa3d08fe411c3755ef3",
    "input/iter197/order144_quotient/outer.cnf": "fe73a93b7a171fd2afcffe210729f165684297d3d85f4260d883e5ed69ffd334",
    "input/iter197/CHECKED_UNSTARTED.json": "68e06e13c5242beb3d0170565968b911ba68e2b0715d8c3b91a33c4a8f8761b5",
}
actual_bindings = {rel: sha(R / rel) for rel in expected_bindings}
assert actual_bindings == expected_bindings
proofpilot = load(R / "bindings/round124_proofpilot_rank.json")

outer_replay = load(E / "solver/replay.json")
outer_assignment = load(E / "solver/assignment_check.json")
outer_orbit = load(E / "solver/orbit_controls.json")
direct = load(E / "direct/independent_audit.json")
direct_vendor = load(E / "direct/direct_verification.json")
x_orbit = load(R / "verification/Xerr_translation_orbit.json")
z_orbit = load(R / "verification/Zerr_translation_orbit.json")
css197 = load(R / "verification/css_duality_registry_audit_iter197_candidate.json")
css_orbits = load(R / "verification/css_dual_selector_orbits.json")
advance = load(F / "frontier_advance_audit.json")
base = load(F / "formula/metadata.json")
base_check = load(F / "formula/check.json")
quotient_meta = load(F / "order144_quotient/metadata.json")
quotient = load(F / "order144_quotient/check.json")
unstarted = load(F / "CHECKED_UNSTARTED.json")
state198 = load(F / "state.json")
trace = {label: load(R / f"proof_streams/{label}.stream.json") for label in ("outer", "Xerr", "Zerr")}
ledger_path = W / "logs/process/session_process.jsonl"
ledger = [json.loads(x) for x in ledger_path.read_text().splitlines() if x.strip()]
solver_tags = {
    "outer": "solve-iter197-exact-order144-quotient-proof-first",
    "Xerr": "solve-iter197-Xerr-complete-direct360-proof-first",
    "Zerr": "solve-iter197-Zerr-complete-direct360-proof-first",
}
solver_runs = {}
for label, tag in solver_tags.items():
    rows = [x for x in ledger if x.get("state") == "REAPED" and x.get("tag") == tag]
    assert len(rows) == 1 and rows[0]["rc"] == 10 and rows[0]["reaped"]
    row = rows[0]
    solver_runs[label] = {k: row[k] for k in (
        "tag", "argv", "wrapper_pid", "child_pid", "start_utc", "end_utc",
        "duration_ns", "rc", "stdout_bytes", "stderr_bytes", "reaped",
        "detached", "timeout_configured")}

for obj in (outer_replay, outer_assignment, outer_orbit, direct, x_orbit, z_orbit,
            css197, css_orbits, advance, base_check, quotient, unstarted):
    assert obj["status"] == "PASS"
assert direct["sectors"]["Xerr"]["status"] == direct["sectors"]["Zerr"]["status"] == "SATISFIABLE"
assert [x_orbit["orbit_size"], z_orbit["orbit_size"]] == [72, 72]
assert [x["orbit_size"] for x in css_orbits["dual_results"]] == [72, 72]
assert unstarted["ledger_solver_invocations"] == 0 and not unstarted["state_started"]
assert not unstarted["forbidden_solver_model_assignment_proof_artifacts"]
for d in trace.values():
    assert d["classification"] == "SAT_SEARCH_TRACE" and d["unsat_certificate_credit"] == 0
    assert d["raw_sha256"] == d["roundtrip_sha256"] and d["lossless_roundtrip_verified"]

input_bindings = {
    "schema": "circdist-gross-round124-input-bindings-v1",
    "status": "PASS",
    "dispatch_hashes": actual_bindings,
    "mandatory_iter197_semantic_source_sha256": "bee49435279caa3fb6cc02e0f1b145e3568eb54e6d3ac02c49e5bae3c5fa42f4",
    "mandatory_iter197_selector_state_sha256": "2b5d1178c5532d62f8e6266d627aaa4c228fa18526e7f79156cc667b1e207608",
    "mandatory_iter197_counts": {"blocks": 814392, "selectors": 51552, "assertions": 870342},
    "mandatory_iter197_base": {"sha256": actual_bindings["input/iter197/formula/outer.cnf"], "variables": 3140244, "clauses": 11511680},
    "mandatory_iter197_order144_quotient": {"sha256": actual_bindings["input/iter197/order144_quotient/outer.cnf"], "variables": 4375764, "clauses": 21395983, "roots": 143},
    "mandatory_iter197_checked_unstarted_sha256": actual_bindings["input/iter197/CHECKED_UNSTARTED.json"],
    "proofpilot": {"sha256": actual_bindings["bindings/round124_proofpilot_rank.json"], "sole_winner": "CIRCDIST.gross@dstar-residual", "score": 0.00014884524515336767, "override": "continuing-until-complete/theta"},
    "reviewed_parent_root_manifest_sha256": actual_bindings["bindings/round122_parent/SHA256SUMS.txt"],
    "preflight_rehash_audit": {"path": "verification/preflight_binding.json", "sha256": sha(R / "verification/preflight_binding.json")},
}
(R / "INPUT_BINDINGS.json").write_text(json.dumps(input_bindings, indent=2, sort_keys=True) + "\n")

fresh = {
    "schema": "circdist-gross-round124-fresh-frontier-v1",
    "status": "CHECKED_UNSTARTED",
    "iteration": 198,
    "started": False,
    "source_sha256": sha(F / "source.json.gz"),
    "source_semantic_payload_sha256": state198["source_semantic_payload_sha256"],
    "state_sha256": sha(F / "state.json"),
    "selector_state_sha256": state198["selector_state_sha256"],
    "checked_unstarted_sha256": sha(F / "CHECKED_UNSTARTED.json"),
    "blocks": state198["block_count"],
    "selectors": state198["selector_count"],
    "assertions": advance["output"]["assertions"],
    "base": {"sha256": base["cnf_sha256"], "variables": base["variables"], "clauses": base["clauses"]},
    "order144_quotient": {"sha256": quotient["bindings"]["quotient_cnf_sha256"], "variables": quotient["encoding"]["final_variables"], "clauses": quotient["encoding"]["final_clauses"], "roots": quotient["group"]["nonidentity"]},
    "new_selector_orbits": {"sizes": [72, 72, 72, 72], "selectors": 288, "Xerr": 144, "Zerr": 144, "all_288_group_elements_physically_replayed": True},
    "closure": {"translations": True, "css_involution": True, "extended_group_order": 144, "pairwise_collision_free": True, "inherited_registry_collision_free": True},
    "solver_invocations": 0,
    "forbidden_artifacts": [],
    "boundary": "Do not solve iteration 198 in this proposer package or across this proposer/reviewer boundary.",
}
assert fresh["source_sha256"] == "dd0e4f55943381e265b174a0360f2ee2dc0e9c93326b71c315632ffbda6d95a2"
assert fresh["checked_unstarted_sha256"] == "894686dbda1bb6c8da578aad828cb1122e5fe68c8b2e7ec47341c0fabdf8d03c"
(R / "FRESH_FRONTIER.json").write_text(json.dumps(fresh, indent=2, sort_keys=True) + "\n")

result = {
    "schema": "circdist-gross-round124-proposer-result-v1",
    "status": "PASS",
    "verdict": "ITER197_CANDIDATE_KILLED_BY_BOTH_COMPLETE_DIRECT360_SECTORS__ROOT_REMAINS_OPEN__ITER198_CHECKED_UNSTARTED",
    "artifact_name": "circdist_gross_iter197_order144_continuation_round124_20260905",
    "dispatch": input_bindings,
    "outer": {
        "status": "SATISFIABLE", "exact_mandatory_formula": True,
        "solver_run": solver_runs["outer"], "assignment": outer_assignment,
        "semantic_replay": outer_replay,
        "order144_orbit_controls": {"path": "output/iter197/solver/orbit_controls.json", "sha256": sha(E / "solver/orbit_controls.json"), "status": outer_orbit["status"]},
        "licensed_consequence": "The exact reviewed full iteration-197 base is SAT and has the decoded legal frozen 864-edge schedule; no broader unrestricted claim follows from the quotient alone.",
    },
    "direct360": {
        "scope": "two complete unrestricted direct-360 W<=10 queries outside the outer encoding; no pool, residual-pattern, check-count, within-check-family, sampling, or partial restriction",
        "solver_runs": {k: solver_runs[k] for k in ("Xerr", "Zerr")},
        "sectors": direct["sectors"], "geometry": direct["geometry"], "schedule": direct["schedule"],
        "vendor_replay_sha256": sha(E / "direct/direct_verification.json"),
        "independent_stdlib_replay_sha256": sha(E / "direct/independent_audit.json"),
        "kill_rule": "One checked complete SAT sector kills the candidate; both sectors are SAT. Repair/gap analysis was therefore forbidden and not run.",
    },
    "selector_lineage": {
        "original_orbits": {
            "Xerr": {"size": 72, "stabilizer": [[0, 0]], "audit_sha256": sha(R / "verification/Xerr_translation_orbit.json")},
            "Zerr": {"size": 72, "stabilizer": [[0, 0]], "audit_sha256": sha(R / "verification/Zerr_translation_orbit.json")},
        },
        "css_dual_orbits": [{"source": x["source_sector"], "target": x["target_sector"], "size": x["orbit_size"], "stabilizer": x["stabilizer_deltas"], "replays": x["translated_replay_count"]} for x in css_orbits["dual_results"]],
        "D_squared_identity": True, "D_T_delta_D_equals_T_neg_delta": True,
        "all_physical_group_element_replays": 288, "distinct_installed_selectors": 288,
        "pairwise_and_inherited_collision_checks": "PASS",
    },
    "sat_search_traces": {label: {k: trace[label][k] for k in (
        "package_gzip_path", "gzip_sha256", "gzip_bytes", "raw_sha256", "raw_bytes",
        "raw_lf_count", "classification", "unsat_certificate_credit",
        "proof_output_enabled_from_byte_zero")} for label in trace},
    "fresh_frontier": fresh,
    "scientific_status": {
        "CIRCDIST.gross": "CONJECTURED", "gap-via-lift": "CONJECTURED",
        "D*_Gross": [11, 12], "distance_12_witness": None,
        "universal_distance_at_most_11_theorem": None, "root_closed": False,
        "search_exhausted": False, "interval_narrowed": False,
    },
    "limitations": [
        "SAT search traces are retained losslessly but are not UNSAT certificates and receive zero certificate credit.",
        "This result kills one schedule candidate and installs its sound generalized-dihedral selector images; it does not settle CIRCDIST.gross.",
        "Iteration 198 is prepared and checked unstarted but deliberately not solved.",
    ],
}
(R / "RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

solver_path = R / "tooling/cadical-1.9.5-arm64-macos"
environment = {
    "schema": "circdist-gross-round124-environment-v1", "status": "PASS",
    "platform": platform.platform(), "python": platform.python_version(),
    "solver_executable_sha256": sha(solver_path),
    "clean_environment": {"LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"},
    "strict_serial": True, "background_or_detached_children": 0,
}
(R / "ENVIRONMENT.json").write_text(json.dumps(environment, indent=2, sort_keys=True) + "\n")

admin = {
    "schema": "circdist-gross-round124-admin-interface-operations-v1", "status": "DISCLOSED",
    "science_processes": "All solver runs, assignment/semantic/physical/orbit checks, frontier generation, CNF generation/checks, and trace compression were foreground, lock-serialized, and STARTED/REAPED in the inner JSONL ledger.",
    "bounded_management_outside_inner_ledger": [
        "Read-only rg/sed/find/cat/hash inspections used by the Codex execution interface.",
        "Scratch-only cp and apply_patch adaptations; no repository file was edited.",
        "Lead-only read-only process census used to recover one lost unified-exec handle; it ran after the frontier child had already exited.",
    ],
    "repository_mutations_before_install": 0,
    "lost_unified_session": {"wrapper_pid": 67611, "child_pid": 67614, "actual_end_utc": "2026-09-05T17:45:37.336294Z", "recovered_utc": "2026-09-05T18:26:39.904472Z", "science_overlap": False},
}
(R / "ADMIN_INTERFACE_OPERATIONS.json").write_text(json.dumps(admin, indent=2, sort_keys=True) + "\n")

interruptions = {
    "schema": "circdist-gross-round124-interruption-latency-ledger-v1", "status": "DISCLOSED",
    "events": [{
        "id": "I124-001", "category": "unified_exec_handle_projection_loss",
        "started_child_pid": 67614, "wrapper_pid": 67611,
        "child_actual_end_utc": "2026-09-05T17:45:37.336294Z",
        "durable_reap_recovered_utc": "2026-09-05T18:26:39.904472Z",
        "effect": "No science child overlap. Work remained paused until lead census showed both PIDs absent, then the durable ledger supplied the exact rc0 reap record.",
        "lead_census": ["restricted ps attempt: rc127/operation not permitted", "approved read-only ps -p 67611,67614: rc1 with empty stdout; both absent"],
    }],
}
(R / "INTERRUPTION_LATENCY_LEDGER.json").write_text(json.dumps(interruptions, indent=2, sort_keys=True) + "\n")

failure_text = """# Round124 failure ledger

All failures below are disclosed and receive zero positive scientific credit.

- **F124-001 — unified exec session handle not retained.** The iter198 frontier builder's first 30-second yield was projected to stdout without retaining its unified session id. The builder actually reaped rc0 after 114.576172708 seconds, but work remained paused until the durable ledger was safely recovered. No overlapping local process was launched.
- **F124-002 — first lead census blocked.** A minimal restricted `ps` census failed rc127 with operation-not-permitted before producing process data. It has no scientific role.
- **F124-003 — approved lead census empty.** The escalated read-only `ps -p 67611,67614` returned rc1 with empty stdout, correctly showing both prior PIDs absent. It is management evidence only and has no scientific credit.
- **F124-004 — first iter198 quotient checker, rc1.** The builder writes roots as plain JSONL and the build trace as gzip regardless of suffix. The first invocation had those two extensions reversed and failed while decoding the trace, before any quotient-check result was emitted. The bytes and metadata hashes were unchanged; the two files were renamed to `.jsonl` and `.json.gz`, and a complete corrected checker rerun reaped rc0. The failed branch receives zero credit.
- **F124-005 — first packaged result checker, rc1.** Every structural and numeric assertion before the final report-phrase audit passed. The report expressed the correct boundary as `UNSAT credit zero`, while the checker required the literal phrase `zero UNSAT-certificate credit`. The report wording was made explicit and the whole result checker was rerun. The partial first check receives zero completion credit.
- **F124-006 — first finalization capture, rc1.** The inherited guard required the final installed basename while the valid mutable staging tree intentionally used `circdist-round124-package-preseal`. It failed before copying any evidence. The guard was restricted to those two exact approved basenames and the capture was rerun from the same passing replay/gate inputs.
- **F124-007 — first final stage sync, rc1.** Source, verification, and log refreshes completed, but the final write of the already executable read-only `replay.sh` was denied. The partial sync receives zero completion credit. The sync now makes that single preseal file writable before replacement and restores mode 0555; a complete corrected sync was run.

SAT return code 10 is an expected solver result, not a failure. The three proof-output streams are classified `SAT_SEARCH_TRACE` with zero UNSAT-certificate credit. No repair/gap branch was entered after the bilateral SAT kill.
"""
(R / "FAILURE_LEDGER.md").write_text(failure_text)

theorem = """# Round124 theorem and scope notes

## Exact quotient consequence

Let `B197` be the reviewed 3,140,244-variable / 11,511,680-clause base CNF and `Q197` its stabilizer-safe order-144 quotient. The reviewed checker proves `SAT(Q197) iff SAT(B197)` by a byte-exact base prefix and 143 non-strict lex leaders over the complete generalized-dihedral orbit. Non-strict comparison explicitly permits nonfree orbits. The complete observed quotient model therefore licenses `SAT(B197)` and the independently decoded schedule semantics, no larger unrestricted claim.

## Direct mechanism criterion

For each sector the direct formula contains all 360 physical fault columns. It imposes Hamming weight at most 10, all 72 detector parities zero, and a disjunction requiring at least one of 12 logical pairings to be one. Every SAT variable and clause was checked. An independent standard-library reconstruction rebuilt all columns, exact weight, physical support, detector syndrome, logical vector, and both canonical and physical stabilizer-membership tests.

## Generalized-dihedral closure

Write `q=6i+j`. Translation is `T_(a,b)(q)=6((i+a) mod 12)+((j+b) mod 6)` in each 72-qubit half. CSS duality swaps sectors and sends coordinates to their negatives, with residual kind fixed. Direct enumeration verifies `D^2=I` and `D T_delta D=T_-delta`. All four mechanism orbits are free of size 72, so 288 physical group-element replays yield 288 distinct selector keys. Pairwise and inherited-registry collision tests are empty.

## Scientific boundary

The candidate is killed. This is material proposer progress, but it is not a distance-12 witness, a universal distance-at-most-11 theorem, root closure, exhaustion, or interval narrowing. `CIRCDIST.gross` and `gap-via-lift` remain CONJECTURED and `D*_Gross` remains `{11,12}`.
"""
(R / "THEOREM_NOTES.md").write_text(theorem)

x = direct["sectors"]["Xerr"]
z = direct["sectors"]["Zerr"]
report = f"""# CIRCDIST.gross Round124 exact iter197 continuation

## Verdict and safe boundary

The exact reviewed iteration-197 order-144 quotient is **SAT**. Its complete assignment covers all 4,375,764 variables exactly once and satisfies all 21,395,983 clauses. It decodes to a legal frozen 864-edge schedule. Both mandatory complete unrestricted direct-360 sectors are also **SAT** at exact fault weight 10. Either checked sector kills the candidate; both were adjudicated for the symmetric ledger. Repair and gap analysis were therefore forbidden and not attempted.

The only scientific advance after the kill is sound registry growth: four free generalized-dihedral selector orbits of size 72 add 288 distinct selectors. Iteration 198 is sealed **CHECKED_UNSTARTED** and has never been solved. Root status is unchanged.

## Dispatch and reviewed starting frontier

The scheduler, ProofPilot record, canonical Gross node, Round123 exact review, and reviewed Round122 root manifest match the SHA256 values in `INPUT_BINDINGS.json`. Before science, an independent preflight rehashed the sealed input:

- source `6ce8b8593fabc80ce0917f342126e351da30114802765a46773da348115aec44`, semantic `bee49435279caa3fb6cc02e0f1b145e3568eb54e6d3ac02c49e5bae3c5fa42f4`;
- state `cd005e436ff92c66badefb5a30e83531d81d9339bfbc047ebbdbb32627eb1ed0`, selector state `2b5d1178c5532d62f8e6266d627aaa4c228fa18526e7f79156cc667b1e207608`;
- 814,392 blocks, 51,552 selectors, 870,342 assertions;
- base `f46bc3862e2c4db10570d73d5a364750fa1892d90ecd0fa3d08fe411c3755ef3`, 3,140,244 variables / 11,511,680 clauses;
- quotient `fe73a93b7a171fd2afcffe210729f165684297d3d85f4260d883e5ed69ffd334`, 4,375,764 variables / 21,395,983 clauses / 143 nonidentity roots;
- checked-unstarted receipt `68e06e13c5242beb3d0170565968b911ba68e2b0715d8c3b91a33c4a8f8761b5`, state `started=false`, forbidden artifacts empty, solver starts targeting iter197 zero.

The quotient is used only through its checked equisatisfiability with that exact base. Its 143 non-strict lex leaders permit stabilizers and make no free-orbit assumption.

## Mandatory proof-first outer solve

Pinned CaDiCaL SHA256 is `{environment['solver_executable_sha256']}`. The exact sealed quotient was passed directly; proof output was enabled from byte zero. The solver returned 10 and reaped normally. Exact argv, PIDs, UTC start/end, byte counts, stderr, and return code are in `RESULT.json` and the JSONL process ledger.

`output/iter197/solver/assignment_check.json` verifies every variable exactly once and all clauses. The decoded schedule has 864 edges, 228 used layers `0..227`, no resource conflict, all 648 MC overlaps satisfied, global interleaving, 102 overlap-interleaved pairs, 351 whole-check-interleaved pairs, and zero reviewed block/selector hits. Candidate schedule SHA256 is `{outer_replay['compressed_schedule_sha256']}`. The independent orbit audit checks all 144 schedules, all 143 roots, identity stabilizer, lex minimality, base-prefix and quotient clause satisfaction, plus flipped-variable, truncated-assignment, reversed-lex, and omitted-root controls.

Because the solve is SAT, its proof stream is evidence of the proof-enabled search only. It is not a DRAT/LRAT UNSAT certificate.

## Complete unrestricted direct-360 adjudication

The two formulas are outside the outer encoding and use every one of 360 physical columns, with only complete `W<=10`, 72 detector equations, and a nonzero 12-logical-row condition. There is no pool, residual-pattern, check-count, within-check-family, sample, or partial restriction.

### Xerr

- CNF `{x['cnf_sha256']}`, {x['variables']:,} variables / {x['clauses']:,} clauses; every clause checked.
- Selected faults: `{', '.join(x['selected_names'])}`.
- Exact weight 10; canonical support `{x['canonical_net_support']}`; physical support `{x['physical_net_support']}`.
- Detector syndrome `{x['physical_syndrome']}`; logical vector `{x['logical_parities']}`.
- Canonical and physical nonstabilizer tests pass. Flipping selected variable {x['negative_control']['flip_selected_var']} fails {x['negative_control']['failed_clause_count']} clauses.

### Zerr

- CNF `{z['cnf_sha256']}`, {z['variables']:,} variables / {z['clauses']:,} clauses; every clause checked.
- Selected faults: `{', '.join(z['selected_names'])}`.
- Exact weight 10; canonical support `{z['canonical_net_support']}`; physical support `{z['physical_net_support']}`.
- Detector syndrome `{z['physical_syndrome']}`; logical vector `{z['logical_parities']}`.
- Canonical and physical nonstabilizer tests pass. Flipping selected variable {z['negative_control']['flip_selected_var']} fails {z['negative_control']['failed_clause_count']} clauses.

The independent implementation uses only the Python standard library and reconstructs all 720 sector columns, both CNFs and assignments, exact physical hooks, both 72-row syndromes, both 12-row logical systems, stabilizer rank 66 in each sector, and cross-pairing rank 12. The vendored verifier agrees.

## Orbit lineage and iter198 frontier

For translations `T_delta` and CSS involution `D`, the audits enumerate stabilizers rather than assuming freeness. Here Xerr, Zerr, and both CSS-dual selector orbits each have identity stabilizer and size 72. All 288 physical group-element replays preserve schedule legality, exact weight, zero syndrome, logical action, and nonstabilizer status. Full selector tuples establish pairwise disjointness and no inherited collision. The source registry is closed under translations and CSS duality before and after atomic insertion.

Fresh iter198 identities:

- source `{fresh['source_sha256']}`, semantic `{fresh['source_semantic_payload_sha256']}`;
- state `{fresh['state_sha256']}`, selector state `{fresh['selector_state_sha256']}`;
- 814,392 blocks / 51,840 selectors / 870,630 assertions;
- base `{fresh['base']['sha256']}`, 3,152,127 variables / 11,550,293 clauses;
- order-144 quotient `{fresh['order144_quotient']['sha256']}`, 4,387,647 variables / 21,434,596 clauses / 143 roots;
- checked-unstarted `{fresh['checked_unstarted_sha256']}`, zero iter198 solver invocations and no forbidden artifacts.

The base checker binds every compiled definition and clause. The quotient checker reconstructs the byte-exact base prefix and every appended recurrence/root clause, verifies the concrete order-144 action and group law, and states only equisatisfiability with the exact invariant base. Iter198 was not solved.

## Streams, controls, failures, and limits

The three complete proof-output streams contain 15,199,582,159 raw bytes total. Each is retained as deterministic gzip, re-expanded in a streaming pass, and matched on byte count, LF count, and SHA256. All are classified `SAT_SEARCH_TRACE` with zero UNSAT-certificate credit. Raw scratch streams were deleted only after those checks; `verification/raw_sat_trace_cleanup.json` records the transition.

`FAILURE_LEDGER.md` records the lost unified-session handle, both lead census outcomes, and the first quotient-check extension mistake. None contributes scientific credit. All scientific children were foreground, lock-serialized, non-detached, and reaped; no solver timeout was configured.

Scientific status remains `CIRCDIST.gross = CONJECTURED`, `gap-via-lift = CONJECTURED`, `D*_Gross = {{11,12}}`. This package gives a candidate kill and 288 additional sound CEGAR exclusions, not a root proof, witness, exhaustion claim, or interval narrowing.
"""
(R / "REPORT.md").write_text(report)

print(json.dumps({
    "status": "PASS", "result_sha256": sha(R / "RESULT.json"),
    "report_sha256": sha(R / "REPORT.md"),
    "fresh_frontier_sha256": sha(R / "FRESH_FRONTIER.json"),
}, sort_keys=True))
