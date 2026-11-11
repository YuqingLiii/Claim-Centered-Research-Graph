#!/usr/bin/env python3
"""Write the Round118 public report and machine-readable verdict from retained evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from pathlib import Path


CHUNK = 8 << 20


def sha(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(CHUNK), b""):
            digest.update(block)
    return digest.hexdigest()


def load(path: Path):
    return json.loads(Path(path).read_text())


def write_json(path: Path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--session-ledger", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()

# Fixed evidence locations.
I = R / "input/iter194"
O = R / "output/iter194"
F = R / "frontier/iter195"

outer_assignment = load(O / "solver/assignment_check.json")
outer_replay = load(O / "solver/replay.json")
outer_orbit = load(O / "solver/orbit_controls.json")
direct_build = load(O / "direct/build_summary.json")
direct_audit = load(O / "direct/independent_audit.json")
x_assignment = load(O / "direct/solver/Xerr.assignment_check.json")
z_assignment = load(O / "direct/solver/Zerr.assignment_check.json")
x_orbit = load(O / "verification/Xerr_translation_orbit.json")
z_orbit = load(O / "verification/Zerr_translation_orbit.json")
dual_audit = load(O / "verification/css_dual_selector_orbits.json")
source_css = load(O / "verification/css_duality_registry_audit.json")
frontier_state = load(F / "state.json")
frontier_advance = load(F / "frontier_advance_audit.json")
frontier_translation = load(F / "translation_registry_check.json")
frontier_css = load(F / "css_closure_check.json")
frontier_base_check = load(F / "base_encoding_check.json")
frontier_qmeta = load(F / "order144_quotient/metadata.json")
frontier_qcheck = load(F / "order144_quotient/check.json")
frontier_unstarted = load(F / "CHECKED_UNSTARTED.json")
preseal_summary = load(R / "verification/preseal_replay/summary.json")
gate_summary = load(R / "verification/repository_gates/summary.json")
stream_paths = {
    "outer": O / "solver/outer.drat.stream.json",
    "Xerr": O / "direct/solver/Xerr.drat.stream.json",
    "Zerr": O / "direct/solver/Zerr.drat.stream.json",
}
streams = {name: load(path) for name, path in stream_paths.items()}

# Exact process records for the three serialized solver calls.
ledger = [json.loads(line) for line in a.session_ledger.read_text().splitlines() if line.strip()]
solver_tags = {
    "outer": "solve-iter194-exact-order144-quotient-proof-first",
    "Xerr": "solve-iter194-Xerr-complete-direct360",
    "Zerr": "solve-iter194-Zerr-complete-direct360",
}
solver_process = {}
for name, tag in solver_tags.items():
    rows = [row for row in ledger if row.get("tag") == tag and row.get("state") == "REAPED"]
    assert len(rows) == 1 and rows[0]["rc"] == 10
    row = rows[0]
    solver_process[name] = {
        "tag": tag,
        "argv": row["argv"],
        "child_pid": row["child_pid"],
        "wrapper_pid": row["wrapper_pid"],
        "start_utc": row["start_utc"],
        "end_utc": row["end_utc"],
        "duration_ns": row["duration_ns"],
        "returncode": row["rc"],
        "stdout_bytes": row["stdout_bytes"],
        "stderr_bytes": row["stderr_bytes"],
        "reaped": True,
        "detached": False,
    }

bindings_spec = {
    "scheduler": ("bindings/SCHEDULER.yaml", "9053f6d7de5acfccfed840381681991ad88f068b5f250f92b1e266ec2b936591"),
    "proofpilot": ("bindings/round118_proofpilot_rank.json", "165edab1701c04e1ac79e3b5eb7d5634c5a8f20d99332d552878164565296525"),
    "canonical_gross": ("bindings/CIRCDIST.gross.yaml", "792c2db47abbb62fa1db07c1d3ebf780501fb1c8356d33e371c3c6ad80d19f5b"),
    "round117_review": ("bindings/round117_exact_review.md", "26fd4c8c39910dae235348efc30e237c7f9ea3d93146076f3580b8c4459cf925"),
    "round116_root_manifest": ("bindings/round116_SHA256SUMS.txt", "2d214dc846b5cf8e7ef329e0baf9ed5204ad6340bcb9e93ac495e8e9e7a87143"),
}
bindings = {}
for name, (relative, expected) in bindings_spec.items():
    actual = sha(R / relative)
    assert actual == expected, (name, expected, actual)
    bindings[name] = {"path": relative, "sha256": actual}

# Exact immutable inputs.
assert sha(I / "source.json.gz") == "f4aafe384ae0a626671b95400f66727007942241cb6988ec9b68bb1a77893091"
assert sha(I / "state.json") == "522848f50de5f9d7015ca326be4a8f0a69e1342bf7c5e27886c6b4dcdaf25c4f"
assert sha(I / "formula/outer.cnf") == "2e72b7bdd8702340fcac7cc706ebb777d5d2a10cc6e670bbd196565e0ece725f"
assert sha(I / "order144_quotient/outer.cnf") == "7fade55daeabb8e2a6702552ce8fc9f0c899091cba64bc1d6806f6f93e7af8db"
assert sha(R / "tooling/cadical-1.9.5-arm64-macos") == "fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9"

sector_result = {}
for label, assignment, orbit in (("Xerr", x_assignment, x_orbit), ("Zerr", z_assignment, z_orbit)):
    formula = direct_build["sectors"][label]
    mechanism = direct_audit["sectors"][label]
    sector_result[label] = {
        "status": "SATISFIABLE",
        "query": "complete unrestricted direct-360",
        "W": 10,
        "complete_query": formula["complete_query"],
        "physical_columns": 360,
        "excluded_restrictions": formula["excluded_restrictions"],
        "formula": {
            "path": f"output/iter194/direct/direct360/{label}.cnf",
            "sha256": formula["dimacs_sha256"],
            "variables": formula["variables"],
            "clauses": formula["clauses"],
        },
        "solver": solver_process[label],
        "complete_assignment": {
            "path": f"output/iter194/direct/solver/{label}.assignment.dimacs",
            "sha256": assignment["assignment_sha256"],
            "variables_assigned_exactly_once": assignment["assigned_variables"],
            "clauses_checked": assignment["checked_clauses"],
            "all_clauses_satisfied": assignment["all_dimacs_clauses_satisfied"],
        },
        "mechanism": {
            "selected_indices": mechanism["selected_indices"],
            "selected_names": mechanism["selected_names"],
            "fault_count": mechanism["fault_count"],
            "canonical_support": mechanism["canonical_net_support"],
            "physical_support": mechanism["physical_net_support"],
            "canonical_syndrome": mechanism["canonical_syndrome"],
            "physical_syndrome": mechanism["physical_syndrome"],
            "logical_parities": mechanism["logical_parities"],
            "canonical_nonstabilizer": mechanism["canonical_nonstabilizer"],
            "physical_nonstabilizer": mechanism["physical_nonstabilizer"],
            "all_360_columns_reconstructed": mechanism["all_columns_reconstructed"] == 360,
            "all_clauses_satisfied": mechanism["all_clauses_satisfied"],
            "negative_control": mechanism["negative_control"],
        },
        "translation_exclusion": {
            "group_order": orbit["group_order"],
            "orbit_size": orbit["orbit_size"],
            "stabilizer_size": orbit["stabilizer_size"],
            "stabilizer_deltas": orbit["stabilizer_deltas"],
            "orbit_stabilizer_product": orbit["orbit_stabilizer_product"],
            "collision_count": orbit["collision_count"],
            "translated_physical_replays": orbit["translated_replay_count"],
            "all_translated_schedules_legal": orbit["all_72_translated_schedules_legal"],
            "all_translated_mechanisms_sound": orbit["all_72_translated_mechanisms_weight_at_most_10_zero_syndrome_nonstabilizer"],
        },
        "proof_output_stream": streams[label],
    }

result = {
    "schema": "circdist-gross-round118-proposer-result-v1",
    "status": "PASS_WITHOUT_ROOT_CLOSURE",
    "date": "2026-09-03",
    "role": "fresh proposer; no self-review or canonical promotion",
    "dispatch": {
        "winner": "CIRCDIST.gross@dstar-residual",
        "score": 0.001373516289473971,
        "sole_authorized_winner": True,
        "bindings": bindings,
    },
    "root_verdict": {
        "CIRCDIST.gross": "CONJECTURED",
        "gap_via_lift": "CONJECTURED",
        "Dstar_Gross": [11, 12],
        "branch_A_legal_distance12_schedule_established": False,
        "branch_B_universal_distance_at_most11_established": False,
        "promotion_or_narrowing": None,
        "precise_result": "one exact legal iter194 schedule is killed in both direct sectors; no root branch closes",
        "fresh_review_required": True,
    },
    "iteration194": {
        "mandatory_quotient_solved_first": True,
        "input": {
            "source": {"path": "input/iter194/source.json.gz", "sha256": sha(I / "source.json.gz"),
                       "semantic_sha256": "b1e7b4677de2549e3802b0e91af35d91f9d735218cd7630b5d9f9b284b15d9cc",
                       "blocks": 814392, "selectors": 50832},
            "state": {"path": "input/iter194/state.json", "sha256": sha(I / "state.json"),
                      "selector_state_sha256": "a0bf27750c0cf74196c2bb161ed70ad879b3bb7e117172adc34c13d8f02236d1"},
            "base": {"path": "input/iter194/formula/outer.cnf", "sha256": sha(I / "formula/outer.cnf"),
                     "variables": 3117683, "clauses": 11438824, "assertions": 869622},
            "quotient": {"path": "input/iter194/order144_quotient/outer.cnf",
                         "sha256": sha(I / "order144_quotient/outer.cnf"), "variables": 4353203,
                         "clauses": 21323127, "assertions": 869765, "group_order": 144, "roots": 143,
                         "reviewed_equisatisfiable_without_orbit_freeness": True},
        },
        "outer": {
            "status": "SATISFIABLE",
            "solver": solver_process["outer"],
            "tool_sha256": sha(R / "tooling/cadical-1.9.5-arm64-macos"),
            "proof_output_enabled_from_byte_zero": True,
            "complete_assignment": {
                "path": "output/iter194/solver/assignment.dimacs",
                "sha256": outer_assignment["assignment_sha256"],
                "variables_assigned_exactly_once": outer_assignment["assigned_variables"],
                "clauses_checked": outer_assignment["checked_clauses"],
                "all_clauses_satisfied": outer_assignment["all_dimacs_clauses_satisfied"],
            },
            "schedule": {
                "candidate_path": "output/iter194/solver/candidate.json",
                "candidate_sha256": outer_replay["candidate_sha256"],
                "raw_schedule_sha256": outer_replay["raw_schedule_sha256"],
                "compressed_schedule_sha256": outer_replay["compressed_schedule_sha256"],
                "edges": outer_replay["frozen_schedule_audit"]["edge_count"],
                "layers": outer_replay["frozen_schedule_audit"]["used_layers"],
                "min_time": outer_replay["frozen_schedule_audit"]["min_time"],
                "max_time": outer_replay["frozen_schedule_audit"]["max_time"],
                "resource_conflicts": len(outer_replay["frozen_schedule_audit"]["conflicts"]),
                "mc_overlaps": outer_replay["frozen_schedule_audit"]["overlaps"],
                "mc_violations": len(outer_replay["frozen_schedule_audit"]["mc_violations"]),
                "global_interleaved": outer_replay["frozen_schedule_audit"]["global_interleaved"],
                "rank_compression_pairs_checked": outer_replay["rank_compression_pairs_checked"],
                "reviewed_block_hits": outer_replay["reviewed_block_hits"],
                "selector_hits": outer_replay["efssc_named_frozen_valid_selectors"] + outer_replay["efssc_symbolic_valid_selectors"],
            },
            "order144_model_controls": outer_orbit,
            "proof_output_stream": streams["outer"],
        },
        "direct": sector_result,
        "repair": {
            "entered": False,
            "status": "NOT_RUN_BY_PROTOCOL",
            "reason": "both complete unrestricted direct sectors are SAT; repair/gap is authorized only if both are independently UNSAT",
        },
        "exclusions": {
            "input_registry_css_closed": source_css["status"] == "PASS",
            "four_translation_orbits": [72, 36, 72, 36],
            "new_selectors": dual_audit["new_candidate_selectors"],
            "final_selector_count": dual_audit["final_selector_count"],
            "pairwise_disjoint": dual_audit["all_distinct_candidate_orbits_pairwise_disjoint"],
            "collision_free_against_existing": dual_audit["all_candidate_orbits_collision_free_against_css_closed_base"],
            "translation_closed": dual_audit["final_registry_translation_closed"],
            "css_closed": dual_audit["final_registry_css_closed"],
            "physical_group_element_replays": 288,
            "all_replays_sound": frontier_advance["iter194_mechanism_exclusions"]["all_288_original_and_dual_translated_physical_replays"],
        },
        "sat_trace_retention": {
            "streams": 3,
            "raw_bytes": sum(x["raw_bytes"] for x in streams.values()),
            "gzip_bytes": sum(x["gzip_bytes"] for x in streams.values()),
            "empty_clause_lines": sum(x["raw_empty_clause_lines"] for x in streams.values()),
            "lossless_roundtrip_verified": all(x["lossless_roundtrip_verified"] for x in streams.values()),
            "classification": "SAT search traces only",
            "unsat_certificate_credit": False,
        },
    },
    "iteration195_fresh_frontier": {
        "status": "CHECKED_UNSTARTED",
        "solver_invocations": frontier_unstarted["ledger_solver_invocations"],
        "started": frontier_state["started"],
        "sat_result": None,
        "unsat_result": None,
        "forbidden_solver_artifacts": frontier_unstarted["forbidden_solver_model_assignment_proof_artifacts"],
        "source": {"path": "frontier/iter195/source.json.gz", "sha256": sha(F / "source.json.gz"),
                   "semantic_sha256": frontier_state["source_semantic_payload_sha256"],
                   "state_sha256": sha(F / "state.json"), "selector_state_sha256": frontier_state["selector_state_sha256"],
                   "blocks": frontier_state["block_count"], "selectors": frontier_state["selector_count"],
                   "assertions": 869838},
        "base": {"path": "frontier/iter195/formula/outer.cnf", "sha256": sha(F / "formula/outer.cnf"),
                 "variables": frontier_base_check["variables"], "clauses": frontier_base_check["clauses"],
                 "assertions": frontier_base_check["assertions"], "encoding_check": frontier_base_check["status"]},
        "quotient": {"path": "frontier/iter195/order144_quotient/outer.cnf",
                     "sha256": sha(F / "order144_quotient/outer.cnf"), "variables": frontier_qmeta["variables"],
                     "clauses": frontier_qmeta["clauses"], "roots": frontier_qmeta["symmetry_nonidentity_roots"],
                     "group_order": frontier_qmeta["symmetry_group_order"], "equisatisfiable_with_full_iter195_base": True,
                     "independent_check": frontier_qcheck["status"]},
        "closure": {"translation": frontier_translation["status"], "css": frontier_css["status"],
                    "order144": True, "nonfree_orbits_explicitly_handled": True,
                    "orbit_sizes": [72, 36, 72, 36], "stabilizer_sizes": [1, 2, 1, 2]},
    },
    "reviewed_parent_documentation_defects": {
        "preserved_parent_package": True,
        "parent_modified": False,
        "inventory_temporal_self_prefix": "The sealed Round116 inventory self-row describes the just-truncated empty inventory, while its root manifest binds the final 66,305-byte inventory.",
        "report_two_vs_four_rc1": "The sealed Round116 REPORT says two corrected rc=1 attempts; its complete process/failure ledgers record four.",
        "material_to_round118_science": False,
    },
    "preseal_verification": {
        "solver_free_replay": {
            "status": preseal_summary["status"],
            "runs": preseal_summary["run_count"],
            "comparisons": preseal_summary["comparison_count"],
            "solver_invocations": preseal_summary["solver_invocations"],
            "all_children_reaped": preseal_summary["all_children_reaped"],
            "fresh_iter195_remained_unstarted": preseal_summary["fresh_iter195_remained_unstarted"],
            "sat_streams_skipped_because_already_roundtrip_checked": preseal_summary["sat_streams_skipped"],
        },
        "repository_gates": {
            "status": gate_summary["status"],
            "checks": gate_summary["check_count"],
            "all_children_reaped": gate_summary["all_children_reaped"],
            "evidence_closure_raw_exit": gate_summary["evidence_closure_raw_exit"],
            "evidence_closure_unlinked_paths": gate_summary["evidence_closure_interpretation"]["error_count"],
            "all_evidence_closure_errors_under_this_package": gate_summary["evidence_closure_interpretation"]["all_errors_under_new_package"],
        },
    },
    "limitations": [
        "This proposer result kills one schedule and proves neither universal branch B nor existence branch A.",
        "The finite exclusion registry is not claimed to characterize every distance-below-12 schedule.",
        "SAT proof-output streams are search traces, not UNSAT certificates.",
        "The fresh frontier is prepared for a later authorized iteration and deliberately has no solver disposition.",
    ],
}

write_json(R / "RESULT.json", result)

fresh = {
    "schema": "circdist-gross-round118-fresh-frontier-v1",
    "status": "CHECKED_UNSTARTED",
    "iteration": 195,
    "root_verdict_unchanged": result["root_verdict"],
    "source": result["iteration195_fresh_frontier"]["source"],
    "base": result["iteration195_fresh_frontier"]["base"],
    "quotient": result["iteration195_fresh_frontier"]["quotient"],
    "closure": result["iteration195_fresh_frontier"]["closure"],
    "unstarted": {
        "state_started": False,
        "solver_invocations": 0,
        "solver_status": None,
        "sat": None,
        "unsat": None,
        "solver_model_assignment_proof_artifacts": [],
        "audit_path": "frontier/iter195/CHECKED_UNSTARTED.json",
        "audit_sha256": sha(F / "CHECKED_UNSTARTED.json"),
    },
    "next_mandatory_action": "Solve exactly frontier/iter195/order144_quotient/outer.cnf proof-first before rebuilding or substituting any formula.",
}
write_json(R / "FRESH_FRONTIER.json", fresh)

input_bindings = {
    "schema": "circdist-gross-round118-input-bindings-v1",
    "status": "PASS",
    "dispatch": result["dispatch"],
    "iteration194": result["iteration194"]["input"],
    "toolchain": {
        "cadical_1_9_5": {"path": "tooling/cadical-1.9.5-arm64-macos", "sha256": sha(R / "tooling/cadical-1.9.5-arm64-macos")},
        "drat_trim": {"path": "tooling/drat-trim-arm64-macos", "sha256": sha(R / "tooling/drat-trim-arm64-macos")},
        "lrat_check": {"path": "tooling/lrat-check-arm64-macos", "sha256": sha(R / "tooling/lrat-check-arm64-macos")},
    },
}
write_json(R / "INPUT_BINDINGS.json", input_bindings)

environment = {
    "schema": "circdist-gross-round118-environment-v1",
    "status": "PASS",
    "platform": platform.platform(),
    "machine": platform.machine(),
    "python": sys.version,
    "strict_process_serialization": True,
    "solver_checker_overlap": False,
    "solver_timeout_seconds": 21600,
    "solver_proof_output_enabled_from_start": True,
    "solver_processes": solver_process,
    "clean_environment_keys": ["LANG", "LC_ALL", "PATH", "PYTHONDONTWRITEBYTECODE", "TMPDIR", "TZ"],
    "network_required": False,
}
write_json(R / "ENVIRONMENT.json", environment)

report = f"""# CIRCDIST.gross iteration-194 order-144 continuation — Round 118 proposer report

## Exact verdict

The exact reviewed iteration-194 order-144 quotient is **SAT**. The retained assignment sets each of all 4,353,203 DIMACS variables exactly once and satisfies every one of 21,323,127 clauses. It decodes to a legal frozen-family schedule with 864 named edges, 648 MC overlaps, 310 used layers (0 through 309), no resource conflict, no MC violation, global interleaving, no hit in 814,392 installed blocks, and no hit in 50,832 installed selectors.

Both complete unrestricted direct-360 adversaries at canonical threshold W=10 are also **SAT**. The Xerr query has 6,154 variables and 23,196 clauses; the Zerr query has 6,179 variables and 23,296 clauses. Each complete assignment was checked variable-by-variable and clause-by-clause. Independent standard-library reconstruction of all 360 physical columns per sector proves exact fault count ten, empty detector syndrome, nonzero logical action, and nonstabilizer status in both canonical and physical coordinates. Thus this schedule is killed. The protocol forbids repair/gap adjudication because that branch is entered only after both complete direct queries prove UNSAT.

This does not close either root branch. `CIRCDIST.gross` and `gap-via-lift` remain **CONJECTURED**, and `D*_Gross` remains `{{11,12}}`. Branch A still lacks a legal schedule surviving both direct sectors plus repair/gap. Branch B still lacks a universal proof that every legal frozen schedule has distance at most 11. Fresh review is required before any canonical claim.

## Dispatch and immutable inputs

The sole scheduler winner was `CIRCDIST.gross@dstar-residual`, score `0.001373516289473971`. The bound SHA-256 values are:

- scheduler: `{bindings['scheduler']['sha256']}`
- ProofPilot: `{bindings['proofpilot']['sha256']}`
- canonical node: `{bindings['canonical_gross']['sha256']}`
- Round117 exact review: `{bindings['round117_review']['sha256']}`
- reviewed Round116 package root manifest: `{bindings['round116_root_manifest']['sha256']}`

The solved source is `{sha(I/'source.json.gz')}` with semantic source `b1e7b4677de2549e3802b0e91af35d91f9d735218cd7630b5d9f9b284b15d9cc`, state `{sha(I/'state.json')}`, selector state `a0bf27750c0cf74196c2bb161ed70ad879b3bb7e117172adc34c13d8f02236d1`, base CNF `{sha(I/'formula/outer.cnf')}`, and exact quotient `{sha(I/'order144_quotient/outer.cnf')}`. The reviewed quotient adds 143 lex roots for the complete 144-element translation/CSS action and is equisatisfiable with the full base without assuming free orbits.

## Proof-first solve and assignment checks

All scientific children ran in the foreground under `source/serial_exec.py` with a nonblocking exclusive lock. Each process record contains exact argv, wrapper/child PID, UTC timestamps, return code, streams, and reap state. There was never more than one active scientific child.

The pinned solver is CaDiCaL 1.9.5, SHA-256 `{sha(R/'tooling/cadical-1.9.5-arm64-macos')}`. The exact logical commands were:

```text
cadical -t 21600 --no-binary input/iter194/order144_quotient/outer.cnf output/iter194/solver/outer.drat
cadical -t 21600 --no-binary output/iter194/direct/direct360/Xerr.cnf output/iter194/direct/solver/Xerr.drat
cadical -t 21600 --no-binary output/iter194/direct/direct360/Zerr.cnf output/iter194/direct/solver/Zerr.drat
```

All returned rc=10 and were reaped. Durations were {solver_process['outer']['duration_ns']/1e9:.6f} s outer, {solver_process['Xerr']['duration_ns']/1e9:.6f} s Xerr, and {solver_process['Zerr']['duration_ns']/1e9:.6f} s Zerr. Proof output was enabled from byte zero. Because the results are SAT, these streams are search traces and receive no DRAT/LRAT UNSAT credit. Deterministic gzip retained all {sum(x['raw_bytes'] for x in streams.values()):,} raw bytes as {sum(x['gzip_bytes'] for x in streams.values()):,} compressed bytes; a full decompression rehash matched raw SHA-256, byte count, LF count, and zero empty-clause lines for every stream.

For the outer model, the assignment SHA-256 is `{outer_assignment['assignment_sha256']}`. The independent orbit-control audit also rechecked the 3,117,683-variable / 11,438,824-clause base prefix, 8,640 primary time bits, 1,235,520 recurrence values, all 143 edge-map hashes and lex roots, and the complete 144-image schedule orbit. This particular schedule has trivial stabilizer and 143 strict nonidentity roots. Corrupt, truncated, reversed-lex, and missing-root controls were rejected.

## Direct adversary derivation

For each sector the query selects from all 360 named physical columns. If `s_j` is the selection bit, the exact threshold constraint is `sum_j s_j <= 10`. For each detector row `h`, the CNF enforces `XOR_j(s_j * h_j)=0`; twelve independently reconstructed logical rows produce `ell`, and the query enforces `ell != 0`. No pool, residual pattern, check count, within-check family, sampling, or partial-result restriction is present.

Xerr selects `{', '.join(direct_audit['sectors']['Xerr']['selected_names'])}`. Its physical support is `{direct_audit['sectors']['Xerr']['physical_net_support']}`, detector syndrome is empty, and logical vector is `{direct_audit['sectors']['Xerr']['logical_parities']}`.

Zerr selects `{', '.join(direct_audit['sectors']['Zerr']['selected_names'])}`. Its physical support is `{direct_audit['sectors']['Zerr']['physical_net_support']}`, detector syndrome is empty, and logical vector is `{direct_audit['sectors']['Zerr']['logical_parities']}`.

The independent auditor rebuilt incidence, 720 sector columns, syndromes, logical rows, canonical/physical supports and stabilizer spans without importing the frozen model implementation. Flipping one selected primary variable caused clause failures in each negative control.

## Sound exclusion closure

Translations form `G = Z_12 x Z_6`, so `|G|=72`. For any selector mechanism `m`, orbit-stabilizer gives `|Orb(m)| = 72/|Stab(m)|`. Xerr has stabilizer `{{(0,0)}}`, hence orbit size 72. Zerr has stabilizer `{{(0,0),(0,3)}}`, hence orbit size 36. The CSS involution `D` swaps Xerr and Zerr and satisfies `D^2=1` and `D T_delta D = T_-delta`; its two dual translation orbits again have sizes 72 and 36. Exact semantic keys prove the four orbits pairwise disjoint and collision-free against all 50,832 installed selectors.

Every one of the 72 group elements was physically replayed for each original and CSS-dual representative: 288 replays total. All preserve legal scheduling, weight at most ten, zero syndrome, and nonstabilizer action. Therefore exactly 216 distinct selectors are soundly installed, giving 51,048 selectors. No blocks are added, leaving 814,392. The full registry is closed under translations and CSS, including the nonfree size-36 orbits.

## Fresh iteration-195 frontier

The deterministic next source is `{sha(F/'source.json.gz')}`, semantic SHA-256 `{frontier_state['source_semantic_payload_sha256']}`, state `{sha(F/'state.json')}`, and selector state `{frontier_state['selector_state_sha256']}`. It has 814,392 blocks, 51,048 selectors, and 869,838 assertions.

The checked base is 3,124,223 variables / 11,459,291 clauses, SHA-256 `{sha(F/'formula/outer.cnf')}`. The checked order-144 quotient is 4,359,743 variables / 21,343,594 clauses with 143 roots, SHA-256 `{sha(F/'order144_quotient/outer.cnf')}`. The quotient checker reconstructed all 9,884,303 appended clauses, established unique extension, checked all 144 group permutations, and rejected corrupt/truncated primitive controls.

Iteration 195 is genuinely **UNSTARTED**: state `started=false`, no SAT/UNSAT status, zero solver invocation in the session ledger referencing this frontier, and no solver/model/assignment/proof artifact anywhere beneath `frontier/iter195`. Its mandatory next action is to solve exactly this retained quotient proof-first.

## Failed attempts and controls

Nine wrapped rc=1 false starts are retained: an inherited order-72 orbit checker on 143 roots; an initial attempt to edit its read-only scratch copy; an iter193 CSS count assertion on iter194 data; a non-scientific `len(int)` summary probe; the rejected novel iter195 schema label; a mistyped recovery tag; the gzip trace suffix mismatch; an unstarted auditor that initially required a state field absent from the established schema; and the first documentation writer using the wrong reviewed metadata-key name. One later administrative log-copy command used a misspelled lock pathname while no other child was active; it returned rc=0, created no concurrency, and was corrected under the canonical lock. Each affected scientific check was rerun from the beginning after a narrow correction and passed. `FAILURE_LEDGER.md` gives paths and consequences. None is used as positive evidence.

## Reviewed parent documentation defects

The Round116 sealed parent is preserved byte-for-byte and was not edited. This package copies its original inventory and REPORT under `bindings/`. As Round117 found, the parent inventory has one non-load-bearing temporal self-prefix row for `FILE_INVENTORY.jsonl`; its root manifest still binds the final 66,305-byte inventory. The parent REPORT also says two corrected rc=1 attempts although the sealed process/failure ledgers show four. These are disclosed here and are not silently rewritten.

## Replay

The preseal solver-free science replay passed 20 serialized checker/builder runs and 35 exact or runtime-normalized comparisons; all children were reaped and iteration 195 remained unstarted. All eight ordinary zero-exit repository gates passed. Evidence closure returned rc=1 with 493 unique unlinked-evidence diagnostics, all and only beneath this single new unreviewed package; the retained interpreter classified that as the permitted pre-review condition.

After sealing, run:

```text
./replay.sh /private/tmp/circdist-round118-replay
```

The replay writes only to the requested external directory, never invokes a SAT solver, verifies the seal and result, rechecks all three complete assignments and clauses, replays schedule/orbit/direct evidence, regenerates and checks the fresh source outside the package, checks base and quotient encodings, fully decompresses and rehashes all SAT traces, and confirms iteration 195 remains unstarted.
"""
(R / "REPORT.md").write_text(report)

theorem = """# Theorem notes — Round 118

## Proposer-level proved statements

1. The exact reviewed iteration-194 order-144 quotient is satisfiable. A complete assignment covers 4,353,203 variables exactly once and satisfies all 21,323,127 clauses.
2. Its projection is a legal frozen-family schedule: 864 edges, no resource conflicts, all 648 MC overlap/orientation checks, global interleaving, valid layer/rank semantics, and zero hits in the inherited 814,392-block / 50,832-selector registry.
3. The schedule has a trivial stabilizer under the 144-element generalized-dihedral translation/CSS action and is the strict lex leader against all 143 nonidentity images. Quotient equisatisfiability itself does not require this orbit to be free: every finite orbit has at least one lex-minimal element, while stabilizer-equal images merely make the corresponding comparison non-strict.
4. Each complete unrestricted direct-360 query at W=10 is satisfiable. Independent physical reconstruction proves each selected ten-column set has zero detector syndrome, nonzero logical action, and is outside both the canonical and physical stabilizer spans.
5. Repair/gap is not entered because its protocol antecedent, complete UNSAT in both direct sectors, is false.
6. Four sound selector orbits of sizes 72, 36, 72, and 36 are collision-free and pairwise disjoint. Orbit-stabilizer is checked explicitly; no freeness assumption is made. All 288 group-element physical transports were replayed.
7. The exact iteration-195 registry is translation/CSS closed with 814,392 blocks and 51,048 selectors. Its base and order-144 quotient encodings are independently checked and it is unstarted.

## Logical boundary

The data proves `exists(schedule killed by Xerr and Zerr)` for this iteration. It does not prove `forall legal schedule, distance <= 11`, and it does not exhibit a schedule with certified distance 12. Therefore neither branch A nor branch B follows. `CIRCDIST.gross` and `gap-via-lift` stay CONJECTURED and `D*_Gross={11,12}`.

## Certificate semantics

CaDiCaL proof output was enabled for every solve. All three outcomes are SAT. Their retained streams contain no empty-clause line and are classified only as complete SAT search traces. The actual positive certificates are the complete assignments plus independent every-clause and physical-semantic checks. No DRAT or LRAT UNSAT claim is made.
"""
(R / "THEOREM_NOTES.md").write_text(theorem)

failure = """# Failure ledger — Round 118

Every row below is a retained false start. No failed run contributes positive evidence.

| ID | process tag / interface event | rc | failure | correction and final disposition |
|---|---|---:|---|---|
| F118-001 | `audit-iter194-order144-orbit-controls` | 1 | The inherited order-72 checker required 71 trace rows; the reviewed quotient has 143. | Adapted only the group enumeration/root expectations to the reviewed order-144 construction; the full all-clause/orbit checker passed. |
| F118-002 | `adapt-order144-orbit-auditor` | 1 | The copied source retained sealed mode 0444. | Changed permissions on the scratch copy only, then applied and hashed the adaptation. No sealed input changed. |
| F118-003 | `audit-iter194-css-duality-and-registry-gap` | 1 | The iter193 auditor asserted its old block/selector counts. | Used the reviewed iter194 auditor with exact 814,392/50,832 counts; it passed. |
| F118-004 | `read-new-orbit-summary` | 1 | A non-scientific display probe called `len()` on an integer summary field. | Corrected the display-only query; scientific orbit evidence was unaffected. |
| F118-005 | `check-iter195-translation-registry` | 1 | The first frontier draft used a novel `full-order144-closure` schema label rejected by the established checker. | Restored the established `full-translation-closure` label, regenerated the entire source/state/audit, and reran translation/CSS/base/quotient checks successfully. The rejected draft is not the retained frontier. |
| F118-006 | `recover-advance-command` | 1 | A display query searched for a nonexistent tag. | Located the command by executable path; no scientific output changed. |
| F118-007 | `check-iter195-order144-quotient` | 1 | The gzip build trace was initially named with a `.json` suffix, so the checker treated compressed bytes as UTF-8. | Renamed the unchanged bytes to `.json.gz`; the full quotient check passed. Final package uses `trace.json.gz`. |
| F118-008 | `run-iter195-unstarted-audit` | 1 | The first auditor required a `solver_invocations` state key not present in the established frontier schema. | Audited `started=false`, the complete process ledger, and the artifact tree; final result is zero solver invocations and zero solver/model/assignment/proof artifacts. |
| F118-009 | early interface inspection | n/a | A few initial read-only shell/interface operations and scratch-directory setup preceded the inner child ledger. | Disclosed in `ADMIN_INTERFACE_OPERATIONS.json`; no solver, checker, formula mutation, or durable evidence write occurred there. All scientific subprocesses are ledgered and serialized. |
| F118-010 | `write-round118-package-docs` | 1 | The first documentation writer referenced nonexistent quotient-metadata key `nonidentity_elements`. | Used the established keys `symmetry_nonidentity_roots` and `symmetry_group_order`, reran the writer, then independently validated `RESULT.json`. No scientific evidence changed. |
| F118-011 | `sync-final-session-logs` | 0 | This administrative copy accidentally used scratch lock pathname `scienced.lock` instead of the canonical `science.lock`. No other child was active, so serialization was not violated, but the empty lock file was copied into the session-log snapshot. | Removed the stray package lock file, reran final log synchronization under `science.lock`, and retained this disclosure. No science or evidence content changed. |

Expected solver rc=10 for SAT is not a failure. No child was killed, detached, or left unreaped. The repair/gap branch was not attempted because its required antecedent was false.
"""
(R / "FAILURE_LEDGER.md").write_text(failure)

admin = {
    "schema": "circdist-gross-round118-admin-interface-operations-v1",
    "status": "DISCLOSED",
    "inner_process_ledger_scope": "all scientific solver/checker/builder commands and most administrative inspections after scratch initialization",
    "outside_inner_ledger": [
        "API/tool-host launches of serial_exec.py itself (the ledger records the foreground child it controls)",
        "initial read-only repository/scratch discovery and creation of the unique scratch directory before the wrapper was installed",
        "apply_patch writes of newly authored scratch-only Python sources",
    ],
    "scientific_effect": None,
    "unlogged_solver_or_checker": False,
    "detached_or_background_process": False,
}
write_json(R / "ADMIN_INTERFACE_OPERATIONS.json", admin)

print(json.dumps({
    "status": "PASS",
    "result_sha256": sha(R / "RESULT.json"),
    "fresh_frontier_sha256": sha(R / "FRESH_FRONTIER.json"),
    "report_bytes": (R / "REPORT.md").stat().st_size,
    "frontier_source_sha256": sha(F / "source.json.gz"),
    "frontier_base_sha256": sha(F / "formula/outer.cnf"),
    "frontier_quotient_sha256": sha(F / "order144_quotient/outer.cnf"),
}, sort_keys=True))
