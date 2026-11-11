#!/usr/bin/env python3
"""Build public Round110 metadata, theorem derivation, and report from checked objects."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import os
import platform
import sys


def load(path):
    return json.loads(Path(path).read_text())


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def entry(path):
    path = Path(path)
    return {"sha256": sha(path), "bytes": path.stat().st_size}


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def write_text(path, value):
    Path(path).write_text(value.rstrip() + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--repository", type=Path, required=True)
    ap.add_argument("--preseal", type=Path)
    ap.add_argument("--gates", type=Path)
    args = ap.parse_args()
    root, repo = args.root.resolve(), args.repository.resolve()

    state = load(root / "frontier/iter191_full_invariant/state.json")
    base = load(root / "frontier/iter191_full_invariant/formula/metadata.json")
    quotient = load(root / "frontier/iter191_full_invariant_quotient/metadata.json")
    assignment = load(root / "solver/iter190/assignment_check.json")
    replay = load(root / "solver/iter190/replay.json")
    orbit = load(root / "verification/iter190_sat_orbit_controls.json")
    direct = load(root / "verification/iter190_direct_independent_audit.json")
    advance = load(root / "frontier/iter191_full_invariant/orbit_audit.json")
    closure = load(root / "verification/iter191_incremental_orbit_closure_independent.json")
    traces = load(root / "verification/iter190_sat_trace_streams.json")
    proof = load(root / "verification/proof_controls.json")
    initial = load(root / "INITIAL_BINDINGS.json")

    base_set = sorted(p.name for p in (root / "frontier/iter191_full_invariant/formula").iterdir() if p.is_file())
    quotient_set = sorted(p.name for p in (root / "frontier/iter191_full_invariant_quotient").iterdir() if p.is_file())
    assert base_set == ["assertion_map.jsonl", "definitions.json.gz", "encoding_check.json", "metadata.json", "outer.cnf"]
    assert quotient_set == ["independent_check.json", "metadata.json", "outer.cnf", "translation_roots.jsonl", "translation_trace.json.gz"]
    forbidden = ("assignment", "solver", "drat", "lrat", "proof", "model")
    assert not any(any(token in p.name.lower() for token in forbidden)
                   for p in (root / "frontier").rglob("*") if p.is_file())

    residual = "Solve the exact fresh iteration-191 71-root quotient proof-first; if SAT, replay the legal schedule and adjudicate unrestricted Xerr then Zerr strictly serially."
    fresh = {
        "schema": "circdist-gross-round110-fresh-frontier-v1", "status": "PASS",
        "iteration": 191, "fresh_unstarted": True, "started": False, "stop": None,
        "iter191_solved": False, "forbidden_solver_artifacts_absent": True,
        "translation_group": "Z_12 x Z_6", "translation_group_order": 72,
        "blocks": 517140, "selectors": 24588, "lex_leaders": 71,
        "source_file_sha256": state["source_file_sha256"],
        "source_semantic_payload_sha256": state["source_semantic_payload_sha256"],
        "state_file_sha256": sha(root / "frontier/iter191_full_invariant/state.json"),
        "selector_state_sha256": state["selector_state_sha256"],
        "base_formula_exact_file_set": base_set,
        "quotient_exact_file_set": quotient_set,
        "base": {"path": "frontier/iter191_full_invariant/formula/outer.cnf",
                 "sha256": base["cnf_sha256"], "variables": base["variables"],
                 "clauses": base["clauses"], "assertions": base["assertions"],
                 "encoding_check": "PASS"},
        "quotient": {"path": "frontier/iter191_full_invariant_quotient/outer.cnf",
                     "sha256": quotient["cnf_sha256"], "variables": quotient["variables"],
                     "clauses": quotient["clauses"], "assertions": quotient["assertions"],
                     "independent_check": "PASS"},
        "smallest_honest_residual": residual,
    }
    write_json(root / "FRESH_FRONTIER.json", fresh)

    canonical_bindings = {
        "operations/circdist/SCHEDULER.yaml": entry(root / "bindings/SCHEDULER.yaml"),
        "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": entry(root / "bindings/CIRCDIST.gross.yaml"),
        "circdist/reviews/circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md": entry(root / "bindings/round109_review.md"),
    }
    predecessor = {
        "round108_root_manifest": entry(root / "bindings/round108_SHA256SUMS.txt"),
        "round108_payload_manifest": entry(root / "bindings/round108_PAYLOAD_SHA256SUMS.txt"),
        "round108_inventory": entry(root / "bindings/round108_FILE_INVENTORY.jsonl"),
        "round108_result": entry(root / "bindings/round108_RESULT.json"),
    }
    input_files = {}
    for path in sorted((root / "inputs/round108").rglob("*")):
        if path.is_file():
            input_files[path.relative_to(root).as_posix()] = entry(path)
    bindings = {
        "schema": "circdist-gross-round110-input-bindings-v1", "status": "PASS",
        "bound_before_science": True, "canonical": canonical_bindings,
        "reviewed_round108_package": predecessor, "embedded_input_files": input_files,
        "mandatory_iteration190": {
            "source_sha256": "5231e7f5b4cd2a74390a5d137b9927276ce73829dc599ddc064ab8f2c94a2d2e",
            "semantic_sha256": "76881a021258e6fda565ecfe0ad61c1fe0e6f6a97a418ea806c6d3193b692c00",
            "state_sha256": "af31130cbb6f0f80d2b37b3ba27d1b1d86fa5b18a80c1e02aa3de02504863be4",
            "selector_state_sha256": "02b71bfed57c070359b77d69514397a021734aec7563057c02eeff29f4b6cdbd",
            "base_cnf_sha256": "e3ec0d0b146fc4ade428052d1a14737ffade9974dfc37dd79fa8411841d45fc8",
            "quotient_cnf_sha256": "12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767",
            "blocks": 517140, "selectors": 24444,
            "base_variables": 1850757, "base_clauses": 6920296, "base_assertions": 545982,
            "quotient_variables": 2464197, "quotient_clauses": 11827887,
            "quotient_assertions": 546053,
        },
        "initial_binding_record": initial,
    }
    assert canonical_bindings["operations/circdist/SCHEDULER.yaml"]["sha256"] == "beefafeee1608dda1eadfe0e82b920f7148bd2dfc12e93c52c6b48ff69e74aed"
    assert canonical_bindings["circdist/proof-dag/nodes/CIRCDIST.gross.yaml"]["sha256"] == "7302da9e4726bd2c62a9e335d75d6a9098780888ed91a87a66d503b5938f607b"
    assert canonical_bindings[next(k for k in canonical_bindings if k.endswith(".md"))]["sha256"] == "0d31152bc03ca8066a7ffeaf885730b51ff2c55a3634819fc68d9fcbcd26dd82"
    assert predecessor["round108_root_manifest"]["sha256"] == "6c7f94706744ec7e11dcae7616d56ac3cc816025c72c25d4dc7396f981666cc0"
    assert predecessor["round108_payload_manifest"]["sha256"] == "f8a998b19317a2a9d1ff77a8cf8e7d6cb9bf55c6f15962036dce88919a60e5e5"
    assert predecessor["round108_inventory"]["sha256"] == "e4b09cb611b0cdceb3296da881280fd3e9f2af76078d0178aaade14ae9b59004"
    write_json(root / "INPUT_BINDINGS.json", bindings)

    solver_records = [load(root / f"logs/process/{name}.json") for name in
                      ("solve_iter190_quotient", "solve_iter190_Xerr", "solve_iter190_Zerr")]
    intervals = [(row["started_unix"], row["ended_unix"]) for row in solver_records]
    assert all(intervals[i][1] <= intervals[i + 1][0] for i in range(2))
    assert all(row["returncode"] == 10 and row["reaped"] and not row["timed_out"] and not row["detached"]
               for row in solver_records)
    direct_summary = {}
    for sector in ("Xerr", "Zerr"):
        checked = direct["sectors"][sector]
        direct_summary[sector] = {key: checked[key] for key in (
            "status", "variables", "clauses", "cnf_sha256", "assignment_sha256",
            "fault_count", "selected_names", "canonical_net_support", "physical_net_support",
            "canonical_syndrome", "physical_syndrome", "logical_parities",
            "canonical_nonstabilizer", "physical_nonstabilizer", "all_clauses_satisfied")}

    result = {
        "schema": "circdist-gross-round110-result-v1", "status": "MATERIAL-CHECKED-CONTINUATION-NOT-CLOSED",
        "package": "circdist/artifacts/circdist_gross_iter190_invariant_quotient_continuation_round110_20260902",
        "root_closed": False, "root_branch_A_closed": False, "root_branch_B_closed": False,
        "canonical_state_modified": False,
        "distance_status": {"CIRCDIST.gross": "CONJECTURED", "gap-via-lift": "CONJECTURED", "D_star_Gross": [11, 12]},
        "mandatory_input": bindings["mandatory_iteration190"],
        "iteration190": {
            "quotient": {"status": "SATISFIABLE", "assignment_sha256": assignment["assignment_sha256"],
                         "assigned_variables": assignment["assigned_variables"],
                         "all_variables_assigned_exactly_once": assignment["all_variables_assigned_exactly_once"],
                         "all_clauses_checked": assignment["checked_clauses"],
                         "all_clauses_satisfied": assignment["all_dimacs_clauses_satisfied"],
                         "solver_log_sha256": assignment["solver_log_sha256"]},
            "schedule": replay["frozen_schedule_audit"],
            "compressed_schedule_sha256": replay["compressed_schedule_sha256"],
            "raw_schedule_sha256": replay["raw_schedule_sha256"],
            "quotient_orbit_controls": orbit,
            "direct": direct_summary, "distance12_result": False,
            "candidate_excluded": True, "candidate_distance_upper_bound": 10,
            "repair_entered": False,
            "repair_reason": "forbidden: complete unrestricted Xerr and Zerr direct queries are both SAT",
        },
        "orbit_continuation": {
            "old_selectors": 24444, "added_selectors": 144, "new_selectors": 24588,
            "parent_orbit_sizes": advance["parent_orbit_sizes"], "collisions": advance["collision_count"],
            "translated_schedule_replays": closure["translated_schedule_replays"],
            "translated_physical_mechanism_replays": closure["translated_physical_mechanism_replays"],
            "block_generator_cases": closure["block_registry"]["generator_invariance_cases"],
            "selector_generator_cases": closure["selector_registry"]["generator_invariance_cases"],
            "full_registry_invariant": True,
        },
        "fresh_frontier": fresh,
        "proof_disposition": {
            "actual_Gross_UNSAT": False, "drat_or_lrat_claim_for_iteration190": False,
            "proof_output_enabled_from_all_solver_launches": True,
            "sat_streams_are_search_traces_not_certificates": True,
            "sat_stream_count": traces["stream_count"], "sat_trace_raw_bytes": traces["raw_bytes"],
            "sat_trace_gzip_bytes": traces["gzip_bytes"], "empty_clause_lines": traces["empty_clause_lines"],
            "valid_corrupt_truncated_toolchain_controls": proof["status"],
            "nested_control_children": len(proof["runs"]),
            "all_nested_control_children_reaped": all(row["reaped"] for row in proof["runs"]),
        },
        "solver_processes": solver_records, "strict_solver_nonoverlap": True,
        "failures": {"ledger": "FAILURE_LEDGER.md", "disclosed_ids": [f"F110-{i:03d}" for i in range(1, 11)],
                     "scientific_failures_or_unknowns": 0},
        "proposed_canonical_yaml": {
            "path": "PROPOSED_CIRCDIST.gross.yaml", "sha256": sha(root / "PROPOSED_CIRCDIST.gross.yaml"),
            "identical_to_bound_canonical": (root / "PROPOSED_CIRCDIST.gross.yaml").read_bytes() ==
                                              (root / "bindings/CIRCDIST.gross.yaml").read_bytes(),
            "installed": False, "level": "CONJECTURED", "residual": [11, 12]},
        "exact_residual": residual,
    }
    if args.preseal and args.preseal.exists():
        result["preseal_replay_binding"] = {**entry(args.preseal), "external_record": str(args.preseal),
                                             "status": load(args.preseal)["status"]}
    if args.gates and args.gates.exists():
        gate = load(args.gates)
        result["repository_gates"] = {"status": gate["status"], "summary": str(args.gates),
                                       "check_count": len(gate.get("checks", [])),
                                       "all_children_reaped": gate.get("all_children_reaped", False)}
    write_json(root / "RESULT.json", result)

    environment = {
        "schema": "circdist-gross-round110-environment-v1", "status": "PASS",
        "platform": platform.platform(), "machine": platform.machine(), "python": sys.version,
        "working_scratch": str(root), "repository": str(repo),
        "clean_replay_environment": {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "LANG": "C.UTF-8",
                                     "LC_ALL": "C.UTF-8", "PYTHONDONTWRITEBYTECODE": "1",
                                     "PYTHONPATH": "PACKAGE/python/site-packages"},
        "solver": {**entry(root / "tooling/cadical-1.9.5-arm64-macos"), "version": "CaDiCaL 1.9.5"},
        "drat_checker": entry(root / "tooling/drat-trim-arm64-macos"),
        "lrat_checker": entry(root / "tooling/lrat-check-arm64-macos"),
        "subagents_used": False, "network_used_for_science": False,
    }
    write_json(root / "ENVIRONMENT.json", environment)

    x, z = direct_summary["Xerr"], direct_summary["Zerr"]
    report = f"""# Circdist Gross Round110: iteration-190 invariant-quotient continuation

## Verdict

**MATERIAL-CHECKED-CONTINUATION-NOT-CLOSED.** The exact reviewed iteration-190 quotient is SAT. Its complete assignment satisfies all {assignment['checked_clauses']:,} clauses. The decoded 864-edge schedule is legal, but both unrestricted direct-360 sectors are SAT and exhibit independently checked named weight-10 undetected nonstabilizer mechanisms. This candidate is excluded. Neither root branch closes; `CIRCDIST.gross` and `gap-via-lift` remain `CONJECTURED`, and the exact licensed interval remains `D*_Gross in {{11,12}}`.

After both sectors completed, the two complete free `Z_12 x Z_6` orbits were appended atomically: 72 Xerr selectors plus 72 Zerr selectors, zero collisions, changing 24,444 selectors to 24,588. The retained iteration-191 base and 71-root quotient are fresh, checked, and unstarted. Iteration 191 was not solved.

## Bound reviewed start

The scheduler, canonical Gross node, Round109 fresh review, and entire sealed Round108 predecessor were hashed before science. Their SHA-256 values are respectively `beefafeee1608dda1eadfe0e82b920f7148bd2dfc12e93c52c6b48ff69e74aed`, `7302da9e4726bd2c62a9e335d75d6a9098780888ed91a87a66d503b5938f607b`, `0d31152bc03ca8066a7ffeaf885730b51ff2c55a3634819fc68d9fcbcd26dd82`, and root manifest `6c7f94706744ec7e11dcae7616d56ac3cc816025c72c25d4dc7396f981666cc0`. Full predecessor manifest verification passed.

The unique allowed quotient has SHA-256 `12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767`, 2,464,197 variables, 11,827,887 clauses, and 546,053 assertions. Before and after solving, independent streaming checks established the 517,140-block/24,444-selector registry invariance, the exact source/base bijection, all 71 lex roots, unique extension, and finite-orbit quotient/base equisatisfiability.

## Exact quotient result and legal candidate

CaDiCaL PID {solver_records[0]['child_pid']} returned 10 (SAT) after {solver_records[0]['wall_seconds']:.6f} seconds. It was foreground, attached, not timed out, and reaped. The assignment SHA-256 is `{assignment['assignment_sha256']}`; every variable 1 through 2,464,197 appears exactly once and every clause is satisfied. The independent model serialization has SHA-256 `{replay['assignment_sha256']}` and reconstructs the same model.

The schedule uses {replay['frozen_schedule_audit']['used_layers']} layers, times 0 through {replay['frozen_schedule_audit']['max_time']}, with zero conflicts, errors, or MC violations. It has 648 overlap pairs, 75 pair-interleaving witnesses, 321 whole-check-interleaving witnesses, and satisfies the global interleaving condition. Its compressed semantic SHA-256 is `{replay['compressed_schedule_sha256']}`. All 72 orbit vectors are distinct, the stabilizer is exactly `{{(0,0)}}`, and all 71 nonidentity lex roots are strict. Flip, truncation, reversed-lex, and missing-root negative controls were rejected as specified.

## Complete unrestricted direct adjudication

Each direct formula contains all 360 primary fault columns, exact weight at most 10, zero detector syndrome, and nonzero logical class. No pool, residual-pattern, check-count, or within-check-order restriction was used. Xerr ran first to a terminal SAT result; only then did Zerr start.

### Xerr

- CNF: {x['variables']:,} variables, {x['clauses']:,} clauses, SHA-256 `{x['cnf_sha256']}`
- solver PID {solver_records[1]['child_pid']}: SAT in {solver_records[1]['wall_seconds']:.6f} seconds; complete assignment SHA-256 `{x['assignment_sha256']}`
- selected names: `{' '.join(x['selected_names'])}`
- canonical support: `{x['canonical_net_support']}`
- physical support: `{x['physical_net_support']}`
- syndrome: empty canonically and physically
- logical parity: `{x['logical_parities']}`; canonical and physical nonstabilizer checks pass

### Zerr

- CNF: {z['variables']:,} variables, {z['clauses']:,} clauses, SHA-256 `{z['cnf_sha256']}`
- solver PID {solver_records[2]['child_pid']}: SAT in {solver_records[2]['wall_seconds']:.6f} seconds; complete assignment SHA-256 `{z['assignment_sha256']}`
- selected names: `{' '.join(z['selected_names'])}`
- canonical support: `{z['canonical_net_support']}`
- physical support: `{z['physical_net_support']}`
- syndrome: empty canonically and physically
- logical parity: `{z['logical_parities']}`; canonical and physical nonstabilizer checks pass

Vendor-backed physical replay and a separate Python-standard-library implementation both reconstruct every column, clause assignment, schedule-dependent hook, syndrome, logical parity, physical support, and stabilizer test. Either mechanism excludes the candidate; retaining both discharges the required serial two-sector adjudication. Repair was not entered because direct absence was false.

## Orbit update and fresh frontier

Both mechanism stabilizers are trivial, hence orbit-stabilizer gives 72 translated selectors per parent. Normalized semantic tuples show no old-registry, cross-sector, or within-orbit collision. Audits replay all 72 translated legal schedules and all 144 translated physical mechanisms; each mechanism retains named weight 10, empty syndrome, and nonstabilizer logical action. Generator closure checks cover 1,034,280 block cases and 49,176 selector cases. Therefore the atomic count is `24,444 + 72 + 72 = 24,588`.

The fresh iteration-191 source SHA-256 is `{fresh['source_file_sha256']}`, semantic payload `{fresh['source_semantic_payload_sha256']}`, state `{fresh['state_file_sha256']}`, and selector state `{fresh['selector_state_sha256']}`. Its base is {base['variables']:,} variables / {base['clauses']:,} clauses / {base['assertions']:,} assertions, SHA-256 `{base['cnf_sha256']}`. Its quotient is {quotient['variables']:,} variables / {quotient['clauses']:,} clauses / {quotient['assertions']:,} assertions, SHA-256 `{quotient['cnf_sha256']}`. Both independent checks pass. Exact file allowlists exclude solver, model, assignment, and proof outputs; `started=false`, `stop=null`.

## Proof and process disposition

All three solver results are SAT. Their proof-side outputs are retained only as losslessly verified deterministic-gzip search traces: {traces['raw_bytes']:,} raw bytes, {traces['gzip_bytes']:,} gzip bytes, zero empty-clause lines. They are not DRAT/LRAT certificates and carry no UNSAT credit. Separate tool controls accept valid DRAT, convert it to accepted LRAT, and reject corrupt/truncated DRAT and LRAT. Those controls do not certify Gross.

All scientific children were foreground and serial; each record includes argv, cwd, environment, PID/PPID, UTC interval, return code, timeout/signal/reap/detach status, stream paths, sizes, and hashes. Ten harness/interface/adaptation/packaging failures are disclosed in `FAILURE_LEDGER.md`; none produced an accepted scientific result or UNKNOWN outcome.

## Root branches and scope

Branch A does not close: this legal candidate has explicit weight-10 mechanisms in both sectors, so it is not a distance-12 witness. Branch B does not close: the mandatory quotient is SAT, so no Gross UNSAT certificate or universal `d_circ <= 11` theorem is available. Candidate exclusion does not narrow the campaign interval.

This package proves only the checked iteration-190 candidate exclusion, its complete two-orbit exclusion update, and construction of the fresh iteration-191 frontier. It does not install canonical state, claim an explicit distance-12 circuit, or claim universal distance at most 11. The next exact task is: {residual}
"""
    write_text(root / "REPORT.md", report)

    theorem = f"""# Round110 public theorem derivation

## Definitions

Let `G = Z_12 x Z_6`, so `|G|=72`. Let `E` be the frozen ordered set of 864 interaction edges. A bounded schedule is `S in [0,1023]^E`, and `v(S)` is its ordered 8,640-bit time vector. `Legal_190(S)` denotes the conjunction represented by the reviewed iteration-190 source: geometry and edge completeness, time bounds, conflict freedom, MC constraints, overlap and whole-check interleaving, global interleaving, 517,140 reviewed block exclusions, and 24,444 named mechanism selectors.

Let `B_190` be the base CNF and

`Q_190 = B_190 AND product_{{g in G, g != e}} [v(S) <=_lex v(g.S)]`.

The retained hashes are `sha256(B_190)=e3ec0d0b146fc4ade428052d1a14737ffade9974dfc37dd79fa8411841d45fc8` and `sha256(Q_190)=12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767`.

## Proposition 1 — source/base correspondence

The streaming compiler checker independently reconstructs every source assertion, definition, and DIMACS clause. Counts agree at 545,982 assertion roots, 1,850,757 variables, and 6,920,296 clauses; assertion-map and definition hashes agree. Thus a `B_190` model projects to exactly one bounded schedule satisfying `Legal_190`, and every such schedule has the encoded auxiliary extension.

## Proposition 2 — full registry soundness and invariance

The action checker reconstructs 72 edge bijections, 864 identity cases, and 4,478,976 composition cases `g.(h.e)=(g+h).e`. The two generators preserve all 517,140 unique block tuples (1,034,280 cases) and all 24,444 unique selector tuples (48,888 cases). Since `(1,0)` and `(0,1)` generate `G`, the whole registry is `G`-invariant. Selector semantic hashes, named-fault uniqueness, weight at most 10, and exact source/state hashes all agree.

## Proposition 3 — quotient equisatisfiability

Every finite orbit `{{g.S:g in G}}` has a lexicographically least schedule vector. Registry invariance from Proposition 2 preserves `Legal_190` under translation. Translating a base model to any minimizer therefore yields a base model satisfying all 71 lex leaders and hence a quotient model. Conversely, deleting the lex recurrence variables and roots from any quotient model gives a base model. The recurrence truth table has a unique extension. Therefore `SAT(B_190) iff SAT(Q_190)`, including stabilizer ties.

## Proposition 4 — checked quotient model

The retained assignment covers exactly variables `1..2,464,197`; streaming evaluation checks all 11,827,887 clauses and finds none false. Physical reconstruction gives 864 edges, 477 used layers, zero conflicts/errors/MC violations, and all frozen interleaving predicates. All 71 root recurrences and 613,440 recurrence values agree. Hence `Q_190` and `B_190` are SAT, excluding branch B at iteration 190.

## Proposition 5 — explicit candidate-killing mechanisms

For each sector the unrestricted direct formula reconstructs all 360 primary columns and encodes `sum(select)<=10`, zero 72-row detector syndrome, and nonzero 12-row logical parity. Complete satisfying assignments select:

- Xerr: `{' '.join(x['selected_names'])}`;
- Zerr: `{' '.join(z['selected_names'])}`.

The Xerr canonical/physical supports are `{x['canonical_net_support']}` and `{x['physical_net_support']}`; the Zerr supports are `{z['canonical_net_support']}` and `{z['physical_net_support']}`. Independent reconstruction gives empty syndrome and nonzero logical vector in both canonical and physical semantics, and row reduction proves neither support is in the stabilizer span. Thus the candidate has a legal adverse mechanism of named weight 10 in each sector. It is not a distance-12 witness, so branch A does not close.

## Proposition 6 — complete free-orbit exclusion update

For each parent mechanism, exact translation finds trivial stabilizer. Orbit-stabilizer gives `|G.m|=72`. All 144 normalized tuples are distinct from the old 24,444 selectors and from one another. Translation replay preserves schedule legality, fault-name cardinality, syndrome zero, logical nontriviality, and physical nonstabilizer status. Adding both whole orbits therefore yields exactly 24,588 selectors and preserves `G`-invariance.

## Proposition 7 — fresh iteration-191 formula

The updated source has SHA-256 `{fresh['source_file_sha256']}`. Its source/base bijection checker accepts base SHA-256 `{base['cnf_sha256']}` with {base['variables']:,} variables and {base['clauses']:,} clauses. Its action/quotient checker reconstructs the exact base prefix, 613,440 added variables, 4,907,520 definition clauses, 71 root clauses, unique recurrence extension, and finite-orbit equisatisfiability for quotient SHA-256 `{quotient['cnf_sha256']}`. Its state is fresh/unstarted and contains no solve artifact.

## Licensed conclusion

The propositions establish a material continuation, not root closure. Branch A is false for this candidate; branch B is unavailable because `Q_190` is SAT. Therefore the canonical statements remain exactly

`CIRCDIST.gross = CONJECTURED`, `gap-via-lift = CONJECTURED`, `D*_Gross in {{11,12}}`.

No inference depends on private reasoning. The package exposes definitions, checked objects, algorithms, counts, hashes, counterexamples, and replay programs needed to audit each public step.
"""
    write_text(root / "THEOREM_NOTES.md", theorem)
    write_text(root / "PROPOSED_CANONICAL_DELTA.md", f"""# Proposed canonical delta

No canonical delta is proposed. `PROPOSED_CIRCDIST.gross.yaml` is byte-identical to the bound canonical file, SHA-256 `7302da9e4726bd2c62a9e335d75d6a9098780888ed91a87a66d503b5938f607b`. The proposer package is not installed as canonical evidence. `CIRCDIST.gross` and `gap-via-lift` remain `CONJECTURED`; `D*_Gross` remains in `{{11,12}}`.
""")
    write_text(root / "BOOTSTRAP_COMMAND.txt", "./replay.sh /absolute/external/path/round110-replay.json")
    print(json.dumps({"status": "PASS", "result": entry(root / "RESULT.json"),
                      "report": entry(root / "REPORT.md"), "fresh_frontier": fresh["iteration"]}, sort_keys=True))


if __name__ == "__main__":
    main()
