#!/usr/bin/env python3
"""Write auditable Round122 proposer result and public report documents."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import shutil
from pathlib import Path


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as fh:
        for chunk in iter(lambda: fh.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


p = argparse.ArgumentParser()
p.add_argument("--root", type=Path, required=True)
p.add_argument("--work", type=Path, required=True)
a = p.parse_args()
R, W = a.root.resolve(), a.work.resolve()
assert R.is_dir()
I, E, F = R / "input/iter196", R / "output/iter196", R / "frontier/iter197"

expected_bindings = {
    "bindings/SCHEDULER.yaml": "4b91623164ec9c5a9ece1b81a35561945146befbe2c3edd05b669fac1a177eb1",
    "bindings/round122_proofpilot_rank.json": "58cff681f9a5eb7d1db149f9ab2d6d6a111bdb4624058373199cd551faff5e44",
    "bindings/CIRCDIST.gross.yaml": "5e94918dbbe3ecc730d1eaa80e70c3b5713e2d87c4b9c44ca33b979b5ef10095",
    "bindings/round121_exact_review.md": "fc4b1c7e33c1a5f8e6dbad1715baa24b2a6d1a88c8368bc3a3632d768ce05d6d",
    "bindings/round120_parent/SHA256SUMS.txt": "e004f8b28e1bd88916f81b1de55e43efcedb4f4924f0f39a2b52830ba143150d",
    "input/iter196/source.json.gz": "31256761866d464eba48c278e2247d6f396a1372ad0508886e06e3f24ea6f51a",
    "input/iter196/state.json": "ab064886695d712b62fddadb8639a75e9d230faa9e8e2d870605ebaf72946da9",
    "input/iter196/formula/outer.cnf": "cf1907663bca93d838d85ba7a4eb8f682f3939b601d4a0295905699f1118e639",
    "input/iter196/order144_quotient/outer.cnf": "12d86dfec0d588760a42edc7a8d43ac6f0172415956384bce461da592e08a593",
}
actual_bindings = {rel: sha(R / rel) for rel in expected_bindings}
assert actual_bindings == expected_bindings
proofpilot = load(R / "bindings/round122_proofpilot_rank.json")

outer_replay = load(E / "solver/replay.json")
outer_assignment = load(E / "solver/assignment_check.json")
outer_orbit = load(E / "solver/orbit_controls.json")
direct = load(E / "direct/independent_audit.json")
direct_vendor = load(E / "direct/direct_verification.json")
x_orbit = load(R / "verification/Xerr_translation_orbit.json")
z_orbit = load(R / "verification/Zerr_translation_orbit.json")
css196 = load(R / "verification/css_duality_registry_audit_iter196_candidate.json")
css_orbits = load(R / "verification/css_dual_selector_orbits.json")
advance = load(F / "frontier_advance_audit.json")
base = load(F / "base_encoding_check.json")
quotient = load(F / "order144_quotient/check.json")
unstarted = load(F / "CHECKED_UNSTARTED.json")
state197 = load(F / "state.json")
trace = {label: load(R / f"proof_streams/{label}.stream.json") for label in ("outer", "Xerr", "Zerr")}
ledger_path = R / "logs/session_and_process/process/session_process.jsonl"
ledger = [json.loads(x) for x in ledger_path.read_text().splitlines() if x.strip()]
solver_tags = {
    "outer": "solve-iter196-exact-order144-quotient-proof-first",
    "Xerr": "solve-iter196-Xerr-complete-direct360-proof-first",
    "Zerr": "solve-iter196-Zerr-complete-direct360-proof-first",
}
solver_runs = {}
for label, tag in solver_tags.items():
    rows = [x for x in ledger if x.get("state") == "REAPED" and x.get("tag") == tag]
    assert len(rows) == 1 and rows[0]["rc"] == 10 and rows[0]["reaped"]
    row = rows[0]
    solver_runs[label] = {k: row[k] for k in ("tag", "argv", "wrapper_pid", "child_pid", "start_utc", "end_utc", "duration_ns", "rc", "stdout_bytes", "stderr_bytes", "reaped", "detached", "timeout_configured")}

for obj in (outer_replay, outer_assignment, outer_orbit, direct, x_orbit, z_orbit, css196, css_orbits, advance, base, quotient, unstarted):
    assert obj["status"] == "PASS"
assert direct["sectors"]["Xerr"]["status"] == direct["sectors"]["Zerr"]["status"] == "SATISFIABLE"
assert [x_orbit["orbit_size"], z_orbit["orbit_size"]] == [36, 72]
assert [x["orbit_size"] for x in css_orbits["dual_results"]] == [36, 72]
assert unstarted["ledger_solver_invocations"] == 0 and not unstarted["state_started"]

input_bindings = {
    "schema": "circdist-gross-round122-input-bindings-v1",
    "status": "PASS",
    "dispatch_hashes": actual_bindings,
    "mandatory_iter196_semantic_source_sha256": "f93cd8e600e1b02db801d84a5b6b2eb0def408f3bca65528c8b0a6b5b0e0b73d",
    "mandatory_iter196_selector_state_sha256": "a960134b6315978cd800261ab5dd6ce287a3fd96c7dda5c33abd19c8671527c9",
    "mandatory_iter196_counts": {"blocks": 814392, "selectors": 51336, "assertions": 870126},
    "mandatory_iter196_base": {"sha256": actual_bindings["input/iter196/formula/outer.cnf"], "variables": 3130306, "clauses": 11477997},
    "mandatory_iter196_order144_quotient": {"sha256": actual_bindings["input/iter196/order144_quotient/outer.cnf"], "variables": 4365826, "clauses": 21362300, "roots": 143},
    "proofpilot": {"sha256": actual_bindings["bindings/round122_proofpilot_rank.json"], "sole_winner": "CIRCDIST.gross@dstar-residual", "score": 0.00040460332515293107},
    "reviewed_parent_root_manifest_sha256": actual_bindings["bindings/round120_parent/SHA256SUMS.txt"],
    "preflight_rehash_audit": {"path": "verification/preflight_binding.json", "sha256": sha(R / "verification/preflight_binding.json")},
    "reviewed_unstarted_recheck": {"path": "verification/rechecked_iter196_unstarted.json", "sha256": sha(R / "verification/rechecked_iter196_unstarted.json")},
}
(R / "INPUT_BINDINGS.json").write_text(json.dumps(input_bindings, indent=2, sort_keys=True) + "\n")

fresh = {
    "schema": "circdist-gross-round122-fresh-frontier-v1",
    "status": "CHECKED_UNSTARTED",
    "iteration": 197,
    "started": False,
    "source_sha256": sha(F / "source.json.gz"),
    "source_semantic_payload_sha256": state197["source_semantic_payload_sha256"],
    "state_sha256": sha(F / "state.json"),
    "selector_state_sha256": state197["selector_state_sha256"],
    "checked_unstarted_sha256": sha(F / "CHECKED_UNSTARTED.json"),
    "blocks": state197["block_count"],
    "selectors": state197["selector_count"],
    "assertions": advance["output"]["assertions"],
    "base": {"sha256": base["cnf_sha256"], "variables": base["variables"], "clauses": base["clauses"]},
    "order144_quotient": {"sha256": quotient["bindings"]["quotient_cnf_sha256"], "variables": quotient["encoding"]["final_variables"], "clauses": quotient["encoding"]["final_clauses"], "roots": quotient["group"]["nonidentity"]},
    "new_selector_orbits": {"sizes": [36, 72, 36, 72], "selectors": 216, "Xerr": 108, "Zerr": 108, "all_288_group_elements_physically_replayed": True},
    "closure": {"translations": True, "css_involution": True, "extended_group_order": 144, "pairwise_collision_free": True, "inherited_registry_collision_free": True},
    "solver_invocations": 0,
    "forbidden_artifacts": [],
    "boundary": "Do not solve iteration 197 in this proposer package or across this proposer/reviewer boundary.",
}
(R / "FRESH_FRONTIER.json").write_text(json.dumps(fresh, indent=2, sort_keys=True) + "\n")

result = {
    "schema": "circdist-gross-round122-proposer-result-v1",
    "status": "PASS",
    "verdict": "ITER196_CANDIDATE_KILLED_BY_BOTH_COMPLETE_DIRECT360_SECTORS__ROOT_REMAINS_OPEN__ITER197_CHECKED_UNSTARTED",
    "artifact_name": R.name,
    "dispatch": input_bindings,
    "outer": {
        "status": "SATISFIABLE",
        "exact_mandatory_formula": True,
        "solver_run": solver_runs["outer"],
        "assignment": outer_assignment,
        "semantic_replay": outer_replay,
        "order144_orbit_controls": {"path": "output/iter196/solver/orbit_controls.json", "sha256": sha(E / "solver/orbit_controls.json"), "status": outer_orbit["status"]},
        "equisatisfiable_full_base_consequence": "The exact reviewed full iteration-196 base is SAT and has the decoded legal frozen 864-edge schedule.",
    },
    "direct360": {
        "scope": "two complete unrestricted direct-360 W<=10 queries outside the outer encoding; no pool, residual-pattern, check-count, within-check-family, sampling, or partial restriction",
        "solver_runs": {k: solver_runs[k] for k in ("Xerr", "Zerr")},
        "sectors": direct["sectors"],
        "geometry": direct["geometry"],
        "schedule": direct["schedule"],
        "vendor_replay_sha256": sha(E / "direct/direct_verification.json"),
        "independent_stdlib_replay_sha256": sha(E / "direct/independent_audit.json"),
        "kill_rule": "One complete SAT sector kills the candidate; both sectors are SAT here. Repair/gap analysis is forbidden and was not run.",
    },
    "selector_lineage": {
        "original_orbits": {"Xerr": {"size": 36, "stabilizer": [[0, 0], [6, 0]], "audit_sha256": sha(R / "verification/Xerr_translation_orbit.json")}, "Zerr": {"size": 72, "stabilizer": [[0, 0]], "audit_sha256": sha(R / "verification/Zerr_translation_orbit.json")}},
        "css_dual_orbits": [{"source": x["source_sector"], "target": x["target_sector"], "size": x["orbit_size"], "stabilizer": x["stabilizer_deltas"], "replays": x["translated_replay_count"]} for x in css_orbits["dual_results"]],
        "D_squared_identity": True,
        "D_T_delta_D_equals_T_neg_delta": True,
        "all_physical_group_element_replays": 288,
        "distinct_installed_selectors": 216,
        "pairwise_and_inherited_collision_checks": "PASS",
    },
    "sat_search_traces": {label: {k: trace[label][k] for k in ("package_gzip_path", "gzip_sha256", "gzip_bytes", "raw_sha256", "raw_bytes", "raw_lf_count", "classification", "unsat_certificate_credit", "proof_output_enabled_from_byte_zero")} for label in trace},
    "fresh_frontier": fresh,
    "scientific_status": {
        "CIRCDIST.gross": "CONJECTURED",
        "gap-via-lift": "CONJECTURED",
        "D*_Gross": [11, 12],
        "distance_12_witness": None,
        "universal_distance_at_most_11_theorem": None,
        "root_closed": False,
        "search_exhausted": False,
        "interval_narrowed": False,
    },
    "limitations": [
        "SAT search traces are retained losslessly but are not UNSAT certificates and receive zero certificate credit.",
        "This result kills one schedule candidate and installs its sound generalized-dihedral selector images; it does not settle CIRCDIST.gross.",
        "Iteration 197 is prepared and checked unstarted but deliberately not solved.",
    ],
}
(R / "RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

environment = {
    "schema": "circdist-gross-round122-environment-v1", "status": "PASS",
    "platform": platform.platform(), "python": platform.python_version(),
    "solver_executable_sha256": "fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9",
    "solver_identity_log": "logs/session_and_process/session/identify-pinned-cadical-round122.stdout",
    "clean_environment": {"LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"},
    "strict_serial": True, "background_or_detached_children": 0,
}
(R / "ENVIRONMENT.json").write_text(json.dumps(environment, indent=2, sort_keys=True) + "\n")

admin = {
    "schema": "circdist-gross-round122-admin-interface-operations-v1", "status": "DISCLOSED",
    "science_children": "All solver, checker, builder, replay, hashing, compression, copying, and inspection children after initialization are STARTED/REAPED in the inner JSONL ledger.",
    "initialization": [
        "Initial scratch mkdir/read-only protocol discovery and targeted rg inspection preceded installation of the inner serial wrapper; process-ledger-preflight.jsonl and targeted-inspection.txt are retained.",
        "No solver was invoked during initialization; the independent preflight audit found prior_round122_solver_starts=0.",
    ],
    "wrapper_pre_spawn_errors": [
        "A guessed /usr/local/bin/rg executable did not exist; the wrapper failed before child spawn. /usr/bin/grep fallback was used and logged.",
        "An attempted /dev/stdout display target was denied before child spawn; serial_display_round122.py was then used for logged small inspections.",
    ],
    "non_process_edits": "Scratch-only apply_patch edits created/adapted Round122 scripts; no repository file was edited.",
    "repository_mutations_before_install": 0,
}
(R / "ADMIN_INTERFACE_OPERATIONS.json").write_text(json.dumps(admin, indent=2, sort_keys=True) + "\n")

failure_text = """# Round122 failure ledger

All failures below are disclosed and receive no positive scientific credit.

- **F122-001 — first independent direct audit, rc=1.** The inherited checker still referenced the iter195 `direct_verification.json`. The path was corrected; no result from the failed run was used.
- **F122-002 — unavailable inspection executable, pre-spawn.** `/usr/local/bin/rg` was absent. The serial wrapper failed before spawning a child; a logged `/usr/bin/grep` fallback was used.
- **F122-003 — second independent direct audit, rc=1.** Two inherited iter195 logical-dual paths remained. Both were corrected and a clean full rerun passed all 720 column reconstructions and all clauses.
- **F122-004 — expected empty grep, rc=1.** The stale-token fallback grep returned 1 because no stale `iter195` match remained; this was an administrative expected-empty result.
- **F122-005 — wrong parent quotient directory, rc=1.** A read-only `ls` used `formula/order144`; the sealed parent uses `order144_quotient`. The corrected read-only listing succeeded.
- **F122-006 — read-only copied templates.** Initial scratch patch attempts failed until copied sealed templates were explicitly made user-writable. No science ran from partially edited files.
- **F122-007 — denied `/dev/stdout` display target, pre-spawn.** The inherited wrapper could not open `/dev/stdout`; no child started. A scratch-only locked display wrapper was used thereafter.
- **F122-008 — first package-document writer, rc=1.** The writer incorrectly required the legacy vendor replay JSON to expose a top-level `status`; that older schema has no such key. The unsupported assertion was removed, while the independently checked Round122 direct audit remains status-bound. No document from the failed writer was retained as evidence.
- **F122-009 — first preseal replay, rc=1.** The replay referenced the outer orbit checker one ancestry level too high. Earlier replay stages (result, ledger, outer assignment, outer semantics) had passed, but the partial replay receives no completion credit. The checker path was corrected to the packaged Round118 ancestry before a clean replay from a new external directory.
- **F122-010 — stage sync rerun, rc=1.** The sync attempted to rewrite an already executable read-only `replay.sh`. Sources, logs, and verification had already refreshed, but the partial sync receives no completion credit. The sync now makes that single preseal file writable before replacing it, then restores mode 0555.
- **F122-011 — first seal-template inspection wrapper, rc=2 before child spawn.** The scratch display wrapper was called with obsolete option names. No child or science started; the corrected argument contract was then used.
- **F122-012 — recursive read-only FIX scan latency/handle loss.** A read-only grep over the sealed parent package was broader than needed and the executor response omitted the live session handle. No overlapping child was started: the proposer held all OS work for more than thirteen minutes, then the serial lock admitted the next command. A later approved focused census matched only its own wrapper and proved that no grep, solver, or other Round122 child survived. The scan supplies no scientific evidence.
- **F122-013 — first recovery process census, pre-spawn failure.** Restricted `/bin/ps` raised `PermissionError` before the requested child was spawned. The approved read-only retry completed and a focused `pgrep` matched only its current census wrapper.
- **F122-014 — first final sync wrapper invocation, rc=2 before child spawn.** The parent serial wrapper was given the display wrapper's `--transcript` option instead of `--stdout/--stderr`. No target child started.
- **F122-015 — second final sync invocation, rc=2.** The sync target rejected an obsolete `--ledger` argument; the logged target child was reaped. A corrected clean invocation refreshed the single stage root.
- **F122-016 — first preseal repository-gate run, rc=1.** Six standard gates passed, but the duplicate-YAML gate used an ancestry path one level too shallow and returned 2. All nested children were foreground and reaped; the partial suite receives no completion credit. The packaged ancestry path was located within the bounded stage tree and the whole suite was rerun in a fresh output directory.
- **F122-017 — second preseal repository-gate run, rc=1 after nine passing children.** The wrapper-level rc=0 branch incorrectly required evidence closure to be silent, while the repository tool correctly prints the exact success line `circdist: evidence closure OK, 188 structured paths; all evidence project-local and linked`. The exact line was bound, every nested child was already reaped, and the whole suite was rerun from a third fresh output directory.
- **F122-018 — combined scratch patch, no child.** One administrative `apply_patch` attempted to modify two files while using a context line from the wrong target and was rejected atomically. No file changed; the two narrow patches were then applied with correct file contexts.
- **F122-019 — first finalization-capture run, rc=1.** The capture script expected scalar `runs` and `comparisons` fields, while the replay schema stores arrays plus `run_count` and `comparison_count`. The assertion failed before any copy. The exact schema was inspected and a clean rerun copied the complete flat replay/gate records.
- **F122-020 — recursive sealer draft rejected before execution.** An initial scratch-only seal/check/install draft used recursive `rglob`. It was never run. After the lead tightened the bounded-manifest rule, the draft was replaced by a one-time fixed `find` path list, a single streaming file pass, fixed manifest additions, and inventory-only verification/copy.
- **F122-021 — first bounded static-list seal attempt, rc=1 before hashing.** The static path list exposed retained empty directories, while the initial bounded sealer asserted that none existed. It failed before creating any manifest addition or hashing a package file. The fixed directory inventory was extended to record and preserve empty directories, and the same 703-entry list was reused.
- **F122-022 — first completed seal rejected by its independent checker.** The seal was internally hash-consistent, but two sealer-created process-boundary records were root-bound and omitted from the payload manifest. The checker returned 1. No repository copy occurred. The sealed scratch tree was not patched: a rollback tool copied only its fixed `initial_files`, checked every copied digest, deleted the failed seal through its fixed inventory, restored the same stage path, and the corrected sealer included both records in the payload before rebuilding from the same 703-entry list.

Two lead interruptions occurred at safe administrative boundaries, and one lead-only task-name typo did not reach this proposer. They changed no file or scientific result and are recorded, with the long read-only scan hold and both clean survivor censuses, in `INTERRUPTION_LATENCY_LEDGER.json` rather than being misclassified as scientific failures.

Darwin `confstr()` warnings of 110 stderr bytes occurred on many Python children under the clean environment. All cited runs returned their expected codes; the warning has no scientific role.
"""
(R / "FAILURE_LEDGER.md").write_text(failure_text)

theorem = """# Round122 theorem and scope notes

## Exact quotient consequence

Let `B196` be the reviewed 3,130,306-variable / 11,477,997-clause base CNF and `Q196` its stabilizer-safe order-144 quotient. The reviewed checker proves `SAT(Q196) iff SAT(B196)` by a byte-exact base prefix and 143 non-strict lex leaders over the complete generalized-dihedral orbit. The observed complete model therefore licenses only `SAT(B196)` plus the independently decoded schedule semantics.

## Direct mechanism criterion

For each error sector, the direct formula contains all 360 physical fault columns. It asserts Hamming weight at most 10, all 72 syndrome parities zero, and a disjunction that at least one of 12 logical pairings is one. A satisfying assignment is independently checked against every clause and reconstructed from all physical columns. Its zero syndrome and nonzero logical pairing prove the net operator is outside the canonical and physical stabilizer spaces.

## Generalized-dihedral closure

Write `q=6i+j`. Translation is `T_(a,b)(q)=6((i+a) mod 12)+((j+b) mod 6)` in each 72-qubit half. The CSS involution swaps sectors and sends coordinates to their negatives. Direct enumeration verifies `D^2=I` and `D T_delta D=T_-delta`. Orbit-stabilizer gives sizes 36,72,36,72: the Xerr mechanism and its dual have stabilizer `{(0,0),(6,0)}`; the Zerr mechanism and its dual are free. Every one of the 288 group-element replays is legal and preserves weight, zero syndrome, and nonstabilizer action; exactly 216 distinct selector keys are installed once.

## Scientific boundary

The candidate is killed. This is material proposer progress, but it is not a distance-12 witness, a universal distance-at-most-11 theorem, root closure, exhaustion, or interval narrowing. `CIRCDIST.gross` and `gap-via-lift` remain CONJECTURED and `D*_Gross` remains `{11,12}`.
"""
(R / "THEOREM_NOTES.md").write_text(theorem)

report = f"""# CIRCDIST.gross Round122 exact iter196 continuation

## Verdict

The exact reviewed iteration-196 order-144 quotient is **SAT**. Its complete assignment satisfies all 21,362,300 clauses and decodes to a legal frozen 864-edge schedule. Both mandatory complete unrestricted direct-360 sectors are also **SAT** at exact fault weight 10. Either sector alone kills the candidate; both were independently reconstructed, so repair was forbidden and not attempted.

The only scientific advance after the kill is sound registry growth: four exact generalized-dihedral selector orbits of sizes `36,72,36,72` add 216 distinct selectors. Iteration 197 is sealed **CHECKED_UNSTARTED** and has never been solved.

## Dispatch and mandatory starting frontier

The live scheduler, ProofPilot dispatch, canonical Gross node, Round121 exact review, and reviewed Round120 root manifest match the five dispatch SHA256 values in `INPUT_BINDINGS.json`. The independent preflight rehashed the sealed starting frontier:

- source `31256761866d464eba48c278e2247d6f396a1372ad0508886e06e3f24ea6f51a`, semantic source `f93cd8e600e1b02db801d84a5b6b2eb0def408f3bca65528c8b0a6b5b0e0b73d`;
- state `ab064886695d712b62fddadb8639a75e9d230faa9e8e2d870605ebaf72946da9`, selector state `a960134b6315978cd800261ab5dd6ce287a3fd96c7dda5c33abd19c8671527c9`;
- 814,392 blocks, 51,336 selectors, 870,126 assertions;
- base `cf190...e639`, 3,130,306 variables / 11,477,997 clauses;
- quotient `12d86...593`, 4,365,826 variables / 21,362,300 clauses / 143 roots.

No solver/model/assignment/proof artifact existed in that frontier, and the Round122 ledger had zero prior starts targeting it.

## Exact outer solve and schedule replay

Pinned CaDiCaL SHA256 is `fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9`. The exact sealed quotient was supplied directly, with ASCII proof output enabled from byte zero. The solver returned 10 and was reaped. `output/iter196/solver/assignment_check.json` verifies all 4,365,826 variables exactly once and every clause.

Physical replay reports 356 used layers (`0..355`), 864 edges, 0 resource conflicts, 648 overlap relations, 0 MC violations, global interleaving, 100 overlap-interleaved pairs, 378 whole-check-interleaved pairs, and zero inherited block/selector hits. Raw schedule SHA256 is `{outer_replay['raw_schedule_sha256']}` and compressed schedule SHA256 is `{outer_replay['compressed_schedule_sha256']}`. All 143 roots and 144 images, including stabilizer cases and corrupt/truncated/reversed/missing-root controls, pass in the orbit audit.

## Complete direct-360 results

The direct queries are outside the outer encoding and use every one of the 360 physical columns. They impose only complete `W<=10`, 72 exact syndrome equations, and a nonzero disjunction over 12 logical rows. No pool, residual pattern, check count, within-check family, sample, or partial restriction appears.

### Xerr

- CNF `8368f46f95e2a2d5960348e66bb1a3dc46fc24dec54d38f6199022788f1c93b2`, 6,124 variables / 23,076 clauses; all checked.
- Selected faults: `{', '.join(direct['sectors']['Xerr']['selected_names'])}`.
- Exact weight 10; physical net support `{direct['sectors']['Xerr']['physical_net_support']}`; syndrome empty; logical vector `{direct['sectors']['Xerr']['logical_parities']}`.
- Canonical and physical nonstabilizer checks pass. Flipping selected variable {direct['sectors']['Xerr']['negative_control']['flip_selected_var']} fails {direct['sectors']['Xerr']['negative_control']['failed_clause_count']} clauses.

### Zerr

- CNF `c91b4367d97cf9ba928e8b106f15be2ed1c945995515fffdc04ba5cfc39cc812`, 6,126 variables / 23,084 clauses; all checked.
- Selected faults: `{', '.join(direct['sectors']['Zerr']['selected_names'])}`.
- Exact weight 10; physical net support `{direct['sectors']['Zerr']['physical_net_support']}`; syndrome empty; logical vector `{direct['sectors']['Zerr']['logical_parities']}`.
- Canonical and physical nonstabilizer checks pass. Flipping selected variable {direct['sectors']['Zerr']['negative_control']['flip_selected_var']} fails {direct['sectors']['Zerr']['negative_control']['failed_clause_count']} clauses.

An independent standard-library implementation reconstructs all 720 columns, all clauses, both 72-row syndromes, both 12-row logical systems, stabilizer ranks 66, cross-pairing rank 12, and schedule/resource semantics. The vendored verifier agrees.

## Exact selector closure and iteration 197

All 72 physical translations were replayed for each original and CSS-dual mechanism. Xerr has a size-36 orbit with stabilizer `(0,0),(6,0)`; Zerr is free of size 72. Their CSS images have the same respective sizes. Pairwise collision and inherited-registry checks are zero. The advance installs 108 Xerr and 108 Zerr selectors atomically.

Fresh iter197 identities:

- source `{fresh['source_sha256']}`, semantic `{fresh['source_semantic_payload_sha256']}`;
- state `{fresh['state_sha256']}`, selector state `{fresh['selector_state_sha256']}`;
- 814,392 blocks / 51,552 selectors / 870,342 assertions;
- base `{fresh['base']['sha256']}`, 3,140,244 variables / 11,511,680 clauses;
- order-144 quotient `{fresh['order144_quotient']['sha256']}`, 4,375,764 variables / 21,395,983 clauses / 143 roots;
- `CHECKED_UNSTARTED.json` `{fresh['checked_unstarted_sha256']}`, zero iter197 solver invocations and no forbidden artifacts.

## Trace disposition, failures, and limits

All three proof-output streams are retained losslessly as deterministic gzip files and independently round-trip checked. They are SAT search traces, contain no empty-clause line, and receive zero UNSAT-certificate credit. See `proof_streams/*.stream.json`.

`FAILURE_LEDGER.md` records every failed administrative/checker branch and its clean correction. None contributes positive evidence. `PROCESS_LEDGER_CHECK.json` proves exact STARTED/REAPED pairing, no interval overlap, three serial SAT solver runs, no detached/background children, and zero solver invocation targeting iter197.

The replay is solver-free, strictly serial, read-only, and accepts an arbitrary external output directory. Scientific status remains: `CIRCDIST.gross = CONJECTURED`, `gap-via-lift = CONJECTURED`, `D*_Gross = {{11,12}}`.
"""
(R / "REPORT.md").write_text(report)

shutil.copy2(W / "verification/process_ledger_check.json", R / "PROCESS_LEDGER_CHECK.json")
print(json.dumps({"status": "PASS", "result_sha256": sha(R / "RESULT.json"), "report_sha256": sha(R / "REPORT.md"), "fresh_frontier_sha256": sha(R / "FRESH_FRONTIER.json")}, sort_keys=True))
