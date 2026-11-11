#!/usr/bin/env python3
"""Write Round120 public documentation from retained, checked evidence."""
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


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--session-ledger", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()
I = R / "input/iter195"
O = R / "output/iter195"
F = R / "frontier/iter196"
V = R / "verification"

outer_assignment = load(O / "solver/assignment_check.json")
outer_replay = load(O / "solver/replay.json")
outer_orbit = load(O / "solver/orbit_controls.json")
direct_build = load(O / "direct/build_summary.json")
direct_audit = load(O / "direct/independent_audit.json")
x_assignment = load(O / "direct/solver/Xerr.assignment_check.json")
z_assignment = load(O / "direct/solver/Zerr.assignment_check.json")
x_orbit = load(V / "Xerr_translation_orbit.json")
z_orbit = load(V / "Zerr_translation_orbit.json")
dual_audit = load(V / "css_dual_selector_orbits.json")
source_css = load(V / "css_duality_registry_audit_iter195_candidate.json")
sat_stream_check = load(V / "sat_trace_streams.json")
frontier_state = load(F / "state.json")
frontier_advance = load(F / "frontier_advance_audit.json")
frontier_translation = load(F / "translation_registry_check.json")
frontier_css = load(F / "css_closure_check.json")
frontier_base = load(F / "base_encoding_check.json")
frontier_qmeta = load(F / "order144_quotient/metadata.json")
frontier_qcheck = load(F / "order144_quotient/check.json")
frontier_unstarted = load(F / "CHECKED_UNSTARTED.json")
preseal = load(V / "preseal_replay/summary.json")
gates = load(V / "repository_gates/summary.json")
streams = {
    "outer": load(O / "solver/outer.drat.stream.json"),
    "Xerr": load(O / "direct/solver/Xerr.drat.stream.json"),
    "Zerr": load(O / "direct/solver/Zerr.drat.stream.json"),
}

ledger = [json.loads(line) for line in a.session_ledger.read_text().splitlines() if line.strip()]
solver_tags = {
    "outer": "solve-iter195-exact-order144-quotient-proof-first",
    "Xerr": "solve-iter195-Xerr-complete-direct360-proof-first-rerun",
    "Zerr": "solve-iter195-Zerr-complete-direct360-proof-first",
}
solver_process = {}
for label, tag in solver_tags.items():
    rows = [row for row in ledger if row.get("tag") == tag and row.get("state") == "REAPED"]
    assert len(rows) == 1 and rows[0]["rc"] == 10
    row = rows[0]
    solver_process[label] = {
        "tag": tag,
        "argv": row["argv"],
        "wrapper_pid": row["wrapper_pid"],
        "child_pid": row["child_pid"],
        "start_utc": row["start_utc"],
        "end_utc": row["end_utc"],
        "duration_ns": row["duration_ns"],
        "duration_seconds": row["duration_ns"] / 1e9,
        "returncode": row["rc"],
        "stdout_bytes": row["stdout_bytes"],
        "stderr_bytes": row["stderr_bytes"],
        "timeout_configured": row.get("timeout_configured", False),
        "timeout_triggered": row.get("timeout_triggered", False),
        "forwarded_signal": row.get("forwarded_signal"),
        "reaped": row.get("reaped", True),
        "detached": row.get("detached", False),
    }

binding_specs = {
    "scheduler": ("bindings/SCHEDULER.yaml", "0614734c7b1e4227935a0ec82e973d43e46be761baba6e3d5a706b01b0473177"),
    "canonical_gross": ("bindings/CIRCDIST.gross.yaml", "0b30330901d01b6eec2bb7dae69bf7aa9c4cc4530060cbed55382313ec9cbe96"),
    "round119_exact_review": ("bindings/round119_exact_review.md", "d79e9ca01e43f646bf1fdd2bcfd7fa05c3845da4d7d4e8f7cd75b37d3bdbdd46"),
    "round118_root_manifest": ("bindings/round118_SHA256SUMS.txt", "c4e089e3daaebccca09a4ba12b338e751321b62054b997440837c8b6d905d329"),
    "round120_proofpilot": ("bindings/round120_proofpilot_rank.json", "10b4cb531ff91bc13cbf926329a1a367baf71874f011d68b0132751f057bfcdd"),
}
bindings = {}
for name, (relative, expected) in binding_specs.items():
    actual = sha(R / relative)
    assert actual == expected, (name, expected, actual)
    bindings[name] = {"path": relative, "sha256": actual}

input_hashes = {
    "source": "e32f3e98e8c7b1a73a59a2e75b963abf080abcf23457aeb90bf25f17bcfdc16a",
    "source_semantic": "fa3a1b80b6b33a6ef14fa314aba2fd8acc394af588bb670a36d8bcffb44cb55b",
    "state": "4ad41e85dcb37973caec6ac8cc9939f3e3b9aa842ba2ff00e1c8c0007bd44be0",
    "selector_state": "231a37783821b049e50f3f9920413010bd497382f4c02f4beee7637757124857",
    "base": "952b2dc06d859cb8fa30a51ce3a6e32cd47ac6ffc310e6465ab205a0b084c099",
    "quotient": "cbab91a2bd7ba5e89db0e6cf52f8b5d3daaa9d6d1a33b1388b1db423e11cdbd6",
}
assert sha(I / "source.json.gz") == input_hashes["source"]
assert sha(I / "state.json") == input_hashes["state"]
assert sha(I / "formula/outer.cnf") == input_hashes["base"]
assert sha(I / "order144_quotient/outer.cnf") == input_hashes["quotient"]
assert sha(R / "tooling/cadical-1.9.5-arm64-macos") == "fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9"
assert all(item["status"] == "PASS" for item in (
    outer_assignment, outer_replay, outer_orbit, direct_build, direct_audit,
    x_assignment, z_assignment, x_orbit, z_orbit, dual_audit, source_css,
    sat_stream_check, frontier_advance, frontier_translation, frontier_css,
    frontier_base, frontier_qcheck, frontier_unstarted, preseal, gates,
))

sector_results = {}
for label, assignment, orbit in (("Xerr", x_assignment, x_orbit), ("Zerr", z_assignment, z_orbit)):
    formula = direct_build["sectors"][label]
    mechanism = direct_audit["sectors"][label]
    sector_results[label] = {
        "status": "SATISFIABLE",
        "query": "complete unrestricted direct-360",
        "threshold_W": 10,
        "complete_query": formula["complete_query"],
        "physical_columns": formula["primary_selection_variables"],
        "excluded_restrictions": formula["excluded_restrictions"],
        "formula": {
            "path": f"output/iter195/direct/direct360/{label}.cnf",
            "sha256": formula["dimacs_sha256"],
            "variables": formula["variables"],
            "clauses": formula["clauses"],
            "syndrome_xor_rows": formula["families"]["syndrome_xor_rows"],
            "logical_parity_rows": formula["families"]["logical_parity_rows"],
        },
        "solver": solver_process[label],
        "complete_assignment": {
            "path": f"output/iter195/direct/solver/{label}.assignment.dimacs",
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
            "negative_control": mechanism["negative_control"],
        },
        "translation_orbit": {
            "group_order": orbit["group_order"],
            "orbit_size": orbit["orbit_size"],
            "stabilizer_size": orbit["stabilizer_size"],
            "stabilizer_deltas": orbit["stabilizer_deltas"],
            "orbit_stabilizer_product": orbit["orbit_stabilizer_product"],
            "translated_physical_replays": orbit["translated_replay_count"],
            "collision_count": orbit["collision_count"],
            "all_schedules_legal": orbit["all_72_translated_schedules_legal"],
            "all_mechanisms_sound": orbit["all_72_translated_mechanisms_weight_at_most_10_zero_syndrome_nonstabilizer"],
        },
        "proof_output_stream": streams[label],
    }

result = {
    "schema": "circdist-gross-round120-proposer-result-v1",
    "status": "PASS_WITHOUT_ROOT_CLOSURE",
    "campaign_date": "2026-09-04",
    "role": "fresh proposer; no self-review or canonical promotion",
    "dispatch": {
        "winner": "CIRCDIST.gross@dstar-residual",
        "score": 0.0010998258664973192,
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
        "precise_result": "the exact iteration-195 schedule is killed by complete SAT witnesses in both CSS sectors; neither root branch closes",
        "fresh_review_required": True,
    },
    "iteration195": {
        "reviewed_frontier_genuinely_unstarted_before_science": True,
        "mandatory_quotient_solved_first": True,
        "input": {
            "source": {"path": "input/iter195/source.json.gz", "sha256": input_hashes["source"],
                       "semantic_sha256": input_hashes["source_semantic"], "blocks": 814392,
                       "selectors": 51048, "assertions": 869838},
            "state": {"path": "input/iter195/state.json", "sha256": input_hashes["state"],
                      "selector_state_sha256": input_hashes["selector_state"]},
            "base": {"path": "input/iter195/formula/outer.cnf", "sha256": input_hashes["base"],
                     "variables": 3124223, "clauses": 11459291},
            "quotient": {"path": "input/iter195/order144_quotient/outer.cnf", "sha256": input_hashes["quotient"],
                         "variables": 4359743, "clauses": 21343594, "group_order": 144,
                         "roots": 143, "non_strict_lex": True,
                         "reviewed_equisatisfiable_without_orbit_freeness": True},
        },
        "outer": {
            "status": "SATISFIABLE",
            "solver": solver_process["outer"],
            "solver_identity": {"name": "CaDiCaL", "version": "1.9.5",
                                "path": "tooling/cadical-1.9.5-arm64-macos",
                                "sha256": sha(R / "tooling/cadical-1.9.5-arm64-macos")},
            "proof_output_enabled_from_byte_zero": True,
            "complete_assignment": {"path": "output/iter195/solver/assignment.dimacs",
                                    "sha256": outer_assignment["assignment_sha256"],
                                    "variables_assigned_exactly_once": outer_assignment["assigned_variables"],
                                    "clauses_checked": outer_assignment["checked_clauses"],
                                    "all_clauses_satisfied": outer_assignment["all_dimacs_clauses_satisfied"]},
            "schedule": {
                "candidate_path": "output/iter195/solver/candidate.json",
                "candidate_sha256": outer_replay["candidate_sha256"],
                "raw_schedule_sha256": outer_replay["raw_schedule_sha256"],
                "compressed_schedule_sha256": outer_replay["compressed_schedule_sha256"],
                "edges": outer_replay["frozen_schedule_audit"]["edge_count"],
                "layers": outer_replay["frozen_schedule_audit"]["used_layers"],
                "min_time": outer_replay["frozen_schedule_audit"]["min_time"],
                "max_time": outer_replay["frozen_schedule_audit"]["max_time"],
                "resource_conflicts": len(outer_replay["frozen_schedule_audit"]["conflicts"]),
                "mc_overlaps_checked": outer_replay["frozen_schedule_audit"]["overlaps"],
                "mc_violations": len(outer_replay["frozen_schedule_audit"]["mc_violations"]),
                "global_interleaved": outer_replay["frozen_schedule_audit"]["global_interleaved"],
                "rank_compression_pairs_checked": outer_replay["rank_compression_pairs_checked"],
                "reviewed_block_hits": outer_replay["reviewed_block_hits"],
                "selector_hits": outer_replay["efssc_named_frozen_valid_selectors"] + outer_replay["efssc_symbolic_valid_selectors"],
            },
            "order144_action_audit": outer_orbit,
            "proof_output_stream": streams["outer"],
        },
        "direct": sector_results,
        "repair": {"entered": False, "status": "NOT_RUN_BY_PROTOCOL",
                   "reason": "both complete sectors are SAT; repair is authorized only after both independently prove UNSAT"},
        "exclusions": {
            "input_registry_css_closed": source_css["status"] == "PASS",
            "translation_group": "Z_12 x Z_6", "translation_group_order": 72,
            "css_involution": "D: Xerr<->Zerr, q->D(q), check->-check, residual kind fixed",
            "css_relations": ["D^2=1", "D T_delta D = T_-delta"],
            "translation_orbit_sizes": [row["orbit_size"] for row in dual_audit["orbit_summary"]],
            "translation_stabilizer_sizes": [row["stabilizer_size"] for row in dual_audit["orbit_summary"]],
            "distinct_orbits": dual_audit["distinct_candidate_translation_orbits"],
            "new_selectors": dual_audit["new_candidate_selectors"],
            "new_selectors_by_sector": frontier_advance["iter195_mechanism_exclusions"]["new_selectors_by_sector_including_inherited_closure"],
            "final_selector_count": dual_audit["final_selector_count"],
            "pairwise_disjoint": dual_audit["all_distinct_candidate_orbits_pairwise_disjoint"],
            "collision_free_against_existing": dual_audit["all_candidate_orbits_collision_free_against_css_closed_base"],
            "translation_closed": dual_audit["final_registry_translation_closed"],
            "css_closed": dual_audit["final_registry_css_closed"],
            "physical_group_element_replays": 288,
            "all_replays_sound": frontier_advance["iter195_mechanism_exclusions"]["all_288_original_and_dual_translated_physical_replays"],
            "exact_tuple_and_provenance_records": "frontier/iter196/source.json.gz and verification/*translation_orbit.json",
        },
        "sat_trace_retention": {
            "stream_count": sat_stream_check["stream_count"],
            "raw_bytes": sat_stream_check["raw_bytes"],
            "gzip_bytes": sat_stream_check["gzip_bytes"],
            "empty_clause_lines": sat_stream_check["empty_clause_lines"],
            "all_lossless_roundtrips_verified": sat_stream_check["all_lossless_roundtrips_verified"],
            "classification": "complete SAT search traces only",
            "unsat_certificate_credit": False,
        },
    },
    "iteration196_fresh_frontier": {
        "status": "CHECKED_UNSTARTED",
        "started": frontier_state["started"],
        "solver_invocations": frontier_unstarted["ledger_solver_invocations"],
        "sat_result": None, "unsat_result": None,
        "forbidden_solver_artifacts": frontier_unstarted["forbidden_solver_model_assignment_proof_artifacts"],
        "source": {"path": "frontier/iter196/source.json.gz", "sha256": sha(F / "source.json.gz"),
                   "semantic_sha256": frontier_state["source_semantic_payload_sha256"],
                   "state_sha256": sha(F / "state.json"), "selector_state_sha256": frontier_state["selector_state_sha256"],
                   "blocks": frontier_state["block_count"], "selectors": frontier_state["selector_count"],
                   "assertions": frontier_advance["output"]["assertions"]},
        "base": {"path": "frontier/iter196/formula/outer.cnf", "sha256": sha(F / "formula/outer.cnf"),
                 "variables": frontier_base["variables"], "clauses": frontier_base["clauses"],
                 "assertions": frontier_base["assertions"], "independent_check": frontier_base["status"]},
        "quotient": {"path": "frontier/iter196/order144_quotient/outer.cnf",
                     "sha256": sha(F / "order144_quotient/outer.cnf"),
                     "variables": frontier_qmeta["variables"], "clauses": frontier_qmeta["clauses"],
                     "roots": frontier_qmeta["symmetry_nonidentity_roots"], "group_order": frontier_qmeta["symmetry_group_order"],
                     "appended_clauses": frontier_qcheck["encoding"]["appended_clauses"],
                     "equisatisfiable_with_full_iter196_base": True, "independent_check": frontier_qcheck["status"]},
        "closure": {"translation": frontier_translation["status"], "css": frontier_css["status"],
                    "order144": frontier_qcheck["status"], "nonfree_orbits_explicitly_supported": True,
                    "installed_candidate_orbit_sizes": [72, 72, 72, 72], "installed_candidate_stabilizer_sizes": [1, 1, 1, 1]},
        "files_before_unstarted_marker": frontier_unstarted["file_count_before_audit_output"],
    },
    "documentation_defects": {
        "inherited_iter195_quotient_check_stale_iteration194_wording": {
            "classification": "non-load-bearing inherited prose defect",
            "machine_bindings_and_counts_correct": True,
            "parent_package_modified": False,
            "iter196_checker_corrected_and_fully_rerun": True,
        }
    },
    "preseal_verification": {
        "solver_free_replay": {"status": preseal["status"], "runs": preseal["run_count"],
                               "comparisons": preseal["comparison_count"], "solver_invocations": preseal["solver_invocations"],
                               "all_children_reaped": preseal["all_children_reaped"],
                               "fresh_iter196_remained_unstarted": preseal["fresh_iter196_remained_unstarted"],
                               "sat_streams_skipped_because_separately_fully_checked": preseal["sat_streams_skipped"]},
        "repository_gates": {"status": gates["status"], "checks": gates["check_count"],
                             "all_children_reaped": gates["all_children_reaped"],
                             "evidence_closure_raw_exit": gates["evidence_closure_raw_exit"],
                             "evidence_closure_unlinked_paths": gates["evidence_closure_interpretation"]["error_count"],
                             "all_evidence_closure_errors_under_this_package": gates["evidence_closure_interpretation"]["all_errors_under_new_package"]},
    },
    "limitations": [
        "One schedule is killed; neither a universal distance-at-most-11 theorem nor a certified distance-12 schedule is produced.",
        "The finite exclusion registry is not claimed complete for all distance-below-12 schedules.",
        "SAT proof-output streams are search traces, not DRAT or LRAT UNSAT certificates.",
        "Iteration 196 is prepared for independent review and deliberately has no solver disposition.",
    ],
}
write_json(R / "RESULT.json", result)

fresh = {
    "schema": "circdist-gross-round120-fresh-frontier-v1", "status": "CHECKED_UNSTARTED", "iteration": 196,
    "root_verdict_unchanged": result["root_verdict"],
    "source": result["iteration196_fresh_frontier"]["source"],
    "base": result["iteration196_fresh_frontier"]["base"],
    "quotient": result["iteration196_fresh_frontier"]["quotient"],
    "closure": result["iteration196_fresh_frontier"]["closure"],
    "unstarted": {"state_started": False, "solver_invocations": 0, "solver_status": None,
                  "sat": None, "unsat": None, "solver_model_assignment_proof_artifacts": [],
                  "audit_path": "frontier/iter196/CHECKED_UNSTARTED.json",
                  "audit_sha256": sha(F / "CHECKED_UNSTARTED.json")},
    "next_mandatory_action": "After independent review, solve exactly frontier/iter196/order144_quotient/outer.cnf proof-first before rebuilding or substituting the formula.",
}
write_json(R / "FRESH_FRONTIER.json", fresh)

write_json(R / "INPUT_BINDINGS.json", {
    "schema": "circdist-gross-round120-input-bindings-v1", "status": "PASS",
    "dispatch": result["dispatch"], "iteration195": result["iteration195"]["input"],
    "toolchain": {
        "cadical_1_9_5": {"path": "tooling/cadical-1.9.5-arm64-macos", "sha256": sha(R / "tooling/cadical-1.9.5-arm64-macos")},
        "drat_trim": {"path": "tooling/drat-trim-arm64-macos", "sha256": sha(R / "tooling/drat-trim-arm64-macos")},
        "lrat_check": {"path": "tooling/lrat-check-arm64-macos", "sha256": sha(R / "tooling/lrat-check-arm64-macos")},
    },
})

write_json(R / "ENVIRONMENT.json", {
    "schema": "circdist-gross-round120-environment-v1", "status": "PASS",
    "platform": platform.platform(), "machine": platform.machine(), "python": sys.version,
    "strict_process_serialization": True, "solver_checker_overlap": False,
    "solver_timeout": None, "solver_proof_output_enabled_from_start": True,
    "solver_processes": solver_process,
    "clean_environment_keys": ["LANG", "LC_ALL", "PATH", "PYTHONDONTWRITEBYTECODE", "TMPDIR", "TZ"],
    "network_required": False,
})

report = f"""# CIRCDIST.gross iteration-195 order-144 continuation — Round 120 proposer report

## Exact root verdict

The exact reviewed iteration-195 order-144 quotient is **SAT**. Its retained assignment covers all 4,359,743 DIMACS variables exactly once and satisfies all 21,343,594 clauses. The decoded frozen schedule has 864 edges, 325 used layers (0 through 324), no resource conflict, all 648 MC overlaps accepted, no MC violation, global interleaving, zero hits among 814,392 installed blocks, and zero hits among 51,048 installed selectors.

Both complete unrestricted direct-360 sectors at `W=10` are independently **SAT**. Xerr has 6,142 variables and 23,148 clauses; Zerr has 6,135 variables and 23,120 clauses. Every variable and every clause was checked. Independent physical reconstruction establishes weight ten, zero detector syndrome, nonzero logical action, and nonstabilizer status in canonical and physical coordinates for both mechanisms. The schedule is therefore killed. Repair was not entered because the protocol permits it only if both complete sectors prove UNSAT.

Neither root branch closes. `CIRCDIST.gross` and `gap-via-lift` remain **CONJECTURED**, and `D*_Gross={{11,12}}`. There is no certified distance-12 schedule and no universal proof that all legal frozen schedules have distance at most 11.

## Dispatch and immutable input

The sole authorized winner was `CIRCDIST.gross@dstar-residual`, score `0.0010998258664973192`. Bound SHA-256 values are scheduler `{bindings['scheduler']['sha256']}`, canonical node `{bindings['canonical_gross']['sha256']}`, Round119 exact review `{bindings['round119_exact_review']['sha256']}`, Round118 root manifest `{bindings['round118_root_manifest']['sha256']}`, and Round120 ProofPilot `{bindings['round120_proofpilot']['sha256']}`.

The independently reviewed source is `{input_hashes['source']}` (semantic `{input_hashes['source_semantic']}`), state `{input_hashes['state']}`, selector state `{input_hashes['selector_state']}`, base CNF `{input_hashes['base']}`, and order-144 quotient `{input_hashes['quotient']}`. Before science, `CHECKED_UNSTARTED` was independently replayed: 15 precursor files, state `started=false`, zero solver invocations, and no assignment/model/proof artifact.

## Quotient and proof-first solve

For the generalized-dihedral action `H=(Z_12 x Z_6) semidirect C_2`, `|H|=144`. The quotient is

`Q = B and AND_{{g in H, g != e}} [t <=_lex g.t]`.

The lex inequalities are non-strict. Every finite orbit has a lex-minimal element; stabilizer-equal images satisfy equality, so equisatisfiability never assumes a free orbit. The checker reconstructed the byte-exact 11,459,291-clause base prefix, all 9,884,303 appended clauses, the unique extension, 143 roots, the full action, and corrupt/truncated controls.

Pinned CaDiCaL 1.9.5 is `{sha(R/'tooling/cadical-1.9.5-arm64-macos')}`. No timeout was set. Solver child PIDs/times/rc were outer `{solver_process['outer']['child_pid']}` / `{solver_process['outer']['duration_seconds']:.6f}` s / 10, Xerr `{solver_process['Xerr']['child_pid']}` / `{solver_process['Xerr']['duration_seconds']:.6f}` s / 10, and Zerr `{solver_process['Zerr']['child_pid']}` / `{solver_process['Zerr']['duration_seconds']:.6f}` s / 10. All were foreground, nonoverlapping, and reaped. Proof output was enabled from byte zero.

Because all outcomes are SAT, the three retained proof-output streams receive zero UNSAT-certificate credit. They contain {sat_stream_check['raw_bytes']:,} raw bytes and {sat_stream_check['gzip_bytes']:,} deterministic-gzip bytes. Independent decompression reproduced each raw SHA-256, byte count, LF count, and zero empty-clause lines.

The schedule assignment is `{outer_assignment['assignment_sha256']}`; raw schedule `{outer_replay['raw_schedule_sha256']}`; compressed schedule `{outer_replay['compressed_schedule_sha256']}`. The full 144-image audit found orbit size 144 and trivial stabilizer, checked 8,640 primary time bits, 1,235,520 recurrence values, and all roots. Flipped, truncated, reversed-lex, and missing-root controls were rejected.

## Complete direct sectors

For each sector, all 360 physical columns are available. With selection bits `s_j`, the query enforces `sum_j s_j <= 10`, all 72 detector XOR equations equal zero, 12 logical parity equations, and a nonzero logical vector. No pool, residual-pattern, check-count, within-check-family, sampling, or partial-result restriction is present.

Xerr selects `{', '.join(direct_audit['sectors']['Xerr']['selected_names'])}`. Its physical support is `{direct_audit['sectors']['Xerr']['physical_net_support']}` and logical vector is `{direct_audit['sectors']['Xerr']['logical_parities']}`.

Zerr selects `{', '.join(direct_audit['sectors']['Zerr']['selected_names'])}`. Its physical support is `{direct_audit['sectors']['Zerr']['physical_net_support']}` and logical vector is `{direct_audit['sectors']['Zerr']['logical_parities']}`.

The vendor replay and an independent stdlib auditor rebuilt all 720 sector columns, both syndromes, logical rows, canonical/physical supports, and stabilizer spans. Flipping one selected variable caused clause failures in each negative control.

## Sound selector closure

Translations form `G=Z_12 x Z_6`, `|G|=72`. For each mechanism `m`, `|Orb(m)| |Stab(m)|=72`. The original Xerr and Zerr mechanisms and their CSS-dual mechanisms each have orbit size 72 and stabilizer `{{(0,0)}}`. The CSS involution swaps sectors, maps data qubits by `D`, checks by negation, preserves the residual-kind convention, and satisfies `D^2=1` and `D T_delta D=T_-delta`.

The four exact selector-tuple orbits are pairwise disjoint and collision-free against the inherited CSS-closed registry. Every translation was replayed physically for every original/dual mechanism: 288 replays. Exactly 288 selectors, 144 per sector, were added, giving 51,336 selectors; blocks remain 814,392. Tuple identities, realizing deltas, stabilizers, source schedule hashes, and provenance live in `frontier/iter196/source.json.gz` and the orbit audits.

## Fresh iteration-196 frontier

The deterministic source is `{sha(F/'source.json.gz')}`, semantic `{frontier_state['source_semantic_payload_sha256']}`, state `{sha(F/'state.json')}`, selector state `{frontier_state['selector_state_sha256']}`. It has 814,392 blocks, 51,336 selectors, and 870,126 assertions.

The checked base is 3,130,306 variables / 11,477,997 clauses, SHA-256 `{sha(F/'formula/outer.cnf')}`. The checked order-144 quotient is 4,365,826 variables / 21,362,300 clauses with 143 roots, SHA-256 `{sha(F/'order144_quotient/outer.cnf')}`. Iteration 196 is **CHECKED_UNSTARTED**: zero solver invocation and no assignment/model/proof artifact. It must receive fresh independent review before its exact retained quotient is solved proof-first.

## Controls, defects, and replay

`FAILURE_LEDGER.md` retains every failed branch and correction. The inherited iteration-195 quotient checker’s prose says “iteration-194”; its machine hashes, counts, schema inputs, and invocation bind iteration 195, so this is classified as non-load-bearing documentation. The new iteration-196 checker corrects the prose and was fully rerun.

The preseal solver-free replay passed {preseal['run_count']} serialized runs and {preseal['comparison_count']} comparisons with zero solver invocations. Eight ordinary repository gates passed. Evidence closure returned rc=1 with {gates['evidence_closure_interpretation']['error_count']} unique diagnostics, all under this single new unreviewed package; the retained interpreter classifies that as the expected pre-review condition. `replay.sh` writes only to an explicit external directory and never invokes a solver.
"""
(R / "REPORT.md").write_text(report)

theorem = """# Theorem notes — Round 120

## Proposer-level proved statements

1. The exact reviewed iteration-195 order-144 quotient is satisfiable; a complete assignment covers all 4,359,743 variables and 21,343,594 clauses.
2. Its projection is a legal 864-edge frozen-family schedule with no resource or MC violation, global interleaving, and zero inherited block/selector hits.
3. It is the strict lex leader of a 144-member action orbit with trivial stabilizer. Quotient equisatisfiability itself uses non-strict lex order and does not require freeness.
4. Both unrestricted direct-360 queries at W=10 are satisfiable. Independent physical reconstruction proves weight ten, zero detector syndrome, nonzero logical action, and nonstabilizer status in each CSS sector.
5. Repair is not entered because its required antecedent, complete UNSAT in both direct sectors, is false.
6. Four free translation orbits of size 72 are physically replayed for all group elements, CSS-dual accounted, pairwise disjoint, and collision-free. Their 288 exact selectors are sound exclusions.
7. Iteration 196 is translation/CSS closed, independently encoded, and CHECKED_UNSTARTED.

## Logical boundary

The evidence proves that this particular schedule is killed in both sectors. It does not prove a universal distance-at-most-11 statement and does not certify a distance-12 schedule. Both root branches remain open; CIRCDIST.gross and gap-via-lift remain CONJECTURED and D*_Gross={11,12}.

## Certificate semantics

All three solver outcomes are SAT. Their proof-output streams are retained complete but have zero UNSAT-certificate credit. The positive certificates are complete assignments plus every-clause and physical-semantic checks. No DRAT or LRAT UNSAT claim is made.
"""
(R / "THEOREM_NOTES.md").write_text(theorem)

failure = """# Failure ledger — Round 120

No failed run contributes positive evidence. Expected solver rc=10 is not a failure.

| ID | event / process tag | rc | defect | correction and consequence |
|---|---|---:|---|---|
| F120-001 | initial `sysctl` and unprivileged `ps` probes | blocked | The restricted host denied system/process inspection; a chained command prevented its second read-only probe. | An approved focused process query found no competing solver before science. No formula or evidence changed. |
| F120-002 | first direct-formula build | 1 | Clean environment omitted the reviewed vendored z3 module. | Reran the whole builder with the exact parent `python/site-packages`; both formulas were regenerated and passed. |
| F120-003 | first Xerr CaDiCaL start | 1 | The target proof directory did not yet exist, so CaDiCaL failed before search/output. | Created the directory through the serial wrapper; reran proof-first from byte zero with a new output and obtained the checked SAT result. |
| F120-004 | first vendor direct replay | 1 | The vendor interface expected retained `Xerr.solver.log` and `Zerr.solver.log` filenames. | Copied the exact solver stdout streams under those names; the full vendor replay passed. |
| F120-005 | first process-ledger self-check | 1 | It read the live ledger after its own STARTED row and before its REAPED row. | Final validation uses an atomic cutpoint produced by the self-excluding snapshot tool. |
| F120-006 | inherited iteration-195 quotient check prose | n/a | The conclusion says “iteration-194” although all input hashes/counts/invocation bind iteration 195. | Classified as non-load-bearing; the parent package was not edited. The iteration-196 checker was adapted, corrected, and fully rerun. |
| F120-007 | copied source edit attempts | n/a | Sealed parent modes initially made scratch copies read-only; one patch therefore failed. | Changed permissions only on scratch copies, then applied and syntax-checked adaptations. |
| F120-008 | `/dev/stdout` wrapper inspection | 1 before child start | The serial wrapper could not reopen `/dev/stdout` on this host. | Used retained-file reads for administration only; scientific children stayed under the lock. |
| F120-009 | initial compiler-source lookup | 2 | The first path omitted the inherited `round116_reviewed/` directory. | Located and used the exact reviewed compiler; compilation and independent checking passed. |
| F120-010 | syntax-check warnings | 0 | Clean `/usr/bin/python3` reported `confstr()` fallback warnings for its temp directory. | All syntax checks returned zero; runtime commands explicitly pinned `TMPDIR` to the unique scratch tree. |
| F120-011 | administrative interface boundary | n/a | Initial read-only discovery, tool-host wrapper launches, `apply_patch` scratch writes, and the approved repository copy are outside the inner child ledger. | Disclosed in `ADMIN_INTERFACE_OPERATIONS.json`; none invoked a solver/checker or supplied positive science. |
| F120-012 | first final cutpoint-ledger audit | 1 | The initial checker classified the earlier `cadical --version` identity probe as a query process. | Corrected the classifier to report one rc=0 identity probe separately from four query invocations; the unchanged 228-row cutpoint then passed. |
| F120-013 | first post-cutpoint documentation rewrite | 2 | The administrative invocation omitted the writer's required `--session-ledger` argument, so argparse exited before reading or writing package evidence. | Reran the writer with the immutable package cutpoint ledger; regenerated documents were then independently rechecked. |

All recorded scientific and construction children were foreground and serialized. No process was killed, detached, timed out, or left unreaped. Exact scratch cleanup and postseal survivor checks are recorded outside the immutable cutpoint at completion.
"""
(R / "FAILURE_LEDGER.md").write_text(failure)

write_json(R / "ADMIN_INTERFACE_OPERATIONS.json", {
    "schema": "circdist-gross-round120-admin-interface-operations-v1", "status": "DISCLOSED",
    "inner_process_ledger_scope": "all scientific children and most construction/admin children after wrapper installation",
    "outside_inner_ledger": [
        "tool-host launches of serial_exec_round120.py itself; the ledger records its foreground child",
        "initial read-only discovery and unique scratch-directory creation before wrapper installation",
        "read-only display commands used to inspect retained child stdout and JSON",
        "apply_patch writes of new scratch-only source adaptations",
        "approved ordinary-copy installation of the staged tree at the final repository path",
    ],
    "unlogged_solver_or_checker": False, "scientific_effect": None,
    "detached_or_background_process": False,
})

print(json.dumps({
    "status": "PASS", "result_sha256": sha(R / "RESULT.json"),
    "fresh_frontier_sha256": sha(R / "FRESH_FRONTIER.json"),
    "report_bytes": (R / "REPORT.md").stat().st_size,
    "frontier_source_sha256": sha(F / "source.json.gz"),
    "frontier_base_sha256": sha(F / "formula/outer.cnf"),
    "frontier_quotient_sha256": sha(F / "order144_quotient/outer.cnf"),
}, sort_keys=True))
