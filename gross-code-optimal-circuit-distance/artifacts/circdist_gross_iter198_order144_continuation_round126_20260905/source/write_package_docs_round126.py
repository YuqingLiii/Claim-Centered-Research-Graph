#!/usr/bin/env python3
"""Write the auditable Round126 proposer result and public mathematical report."""
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
assert R.name == "circdist_gross_iter198_order144_continuation_round126_20260905"
I, E, F = R / "input/iter198", R / "output/iter198", R / "frontier/iter199"

expected_bindings = {
    "bindings/SCHEDULER.yaml": "32ea25bdbc185a9fb81fc9f70b671e8f3bcd2ffd2132c3e11e29a5cb70566b20",
    "bindings/round126_proofpilot_rank.json": "b671a6c4ec3c4b896ec206c30a1c073cc8fc9e1e6dd8d01eb207a73b5baf3a2c",
    "bindings/CIRCDIST.gross.yaml": "81aa12cefb726fe3364b1d92563258dfd6463b7445d7ff7ee4e7a1ba2bf37d8c",
    "bindings/round125_exact_review.md": "c820a120e2d938218b8fc3e5b235f29dd93d13b8d4c333d52e9c057a6da73a55",
    "bindings/round124_parent/SHA256SUMS.txt": "dbc0d3941bf79b4aa4bdc25b17791853a69eb5b542612921aab713aea2e99047",
    "input/iter198/source.json.gz": "dd0e4f55943381e265b174a0360f2ee2dc0e9c93326b71c315632ffbda6d95a2",
    "input/iter198/state.json": "a60e1e378283153a3f24611a9e33cbb97df19bcbe231a9fa515b13fae0ff7287",
    "input/iter198/formula/outer.cnf": "4dc712e335bd3d22c753aaa61e8603026c514a070522a94aa2e239714e185f8f",
    "input/iter198/order144_quotient/outer.cnf": "ee72ce86b4191f6e2602d500e2dc157ea4aca9565028fa7c07073d8b8d19bd08",
    "input/iter198/CHECKED_UNSTARTED.json": "894686dbda1bb6c8da578aad828cb1122e5fe68c8b2e7ec47341c0fabdf8d03c",
}
actual_bindings = {rel: sha(R / rel) for rel in expected_bindings}
assert actual_bindings == expected_bindings

outer_replay = load(E / "solver/replay.json")
outer_assignment = load(E / "solver/assignment_check.json")
outer_orbit = load(E / "solver/orbit_controls.json")
direct = load(E / "direct/independent_audit.json")
direct_vendor = load(E / "direct/direct_verification.json")
x_orbit = load(R / "verification/Xerr_translation_orbit.json")
z_orbit = load(R / "verification/Zerr_translation_orbit.json")
css198 = load(R / "verification/css_duality_registry_audit_iter198_candidate.json")
css_orbits = load(R / "verification/css_dual_selector_orbits.json")
advance = load(F / "frontier_advance_audit.json")
base = load(F / "formula/metadata.json")
base_check = load(F / "formula/check.json")
quotient_meta = load(F / "order144_quotient/metadata.json")
quotient_check = load(F / "order144_quotient/check.json")
unstarted = load(F / "CHECKED_UNSTARTED.json")
state199 = load(F / "state.json")
translation199 = load(R / "verification/iter199_registry_invariance.json")
css199 = load(R / "verification/css_duality_registry_audit_iter199.json")
trace = {label: load(R / f"proof_streams/{label}.stream.json") for label in ("outer", "Xerr", "Zerr")}
preseal_path = W / "work/recovery/PRESEAL_VERIFICATION.json"
preseal = load(preseal_path)
ledger = [json.loads(x) for x in (W / "logs/PROCESS_LEDGER.jsonl").read_text().splitlines() if x.strip()]

solver_tags = {
    "outer": "solve-iter198-exact-order144-quotient-proof-first",
    "Xerr": "solve-iter198-Xerr-complete-direct360-proof-first",
    "Zerr": "solve-iter198-Zerr-complete-direct360-proof-first",
}
solver_runs = {}
for label, tag in solver_tags.items():
    rows = [x for x in ledger if x.get("state") == "REAPED" and x.get("tag") == tag]
    assert len(rows) == 1 and rows[0]["rc"] == 10 and rows[0]["reaped"]
    solver_runs[label] = {k: rows[0][k] for k in (
        "tag", "argv", "wrapper_pid", "child_pid", "start_utc", "end_utc",
        "duration_ns", "rc", "stdout_bytes", "stderr_bytes", "reaped",
        "detached", "timeout_configured")}

for obj in (outer_replay, outer_assignment, outer_orbit, direct,
            x_orbit, z_orbit, css198, css_orbits, advance, base_check,
            quotient_check, unstarted, translation199, css199):
    assert obj["status"] == "PASS"
assert not direct_vendor["repair_gate"]["entered"]
assert direct_vendor["schedule_audit"]["ok"]
assert all(x["all_dimacs_clauses_satisfied"] for x in direct_vendor["sectors"].values())
assert direct["sectors"]["Xerr"]["status"] == direct["sectors"]["Zerr"]["status"] == "SATISFIABLE"
assert [x_orbit["orbit_size"], z_orbit["orbit_size"]] == [72, 72]
assert [x["orbit_size"] for x in css_orbits["dual_results"]] == [72, 72]
assert css_orbits["new_candidate_selectors"] == 288 and css_orbits["final_selector_count"] == 52128
assert unstarted["ledger_solver_invocations"] == 0 and not unstarted["state_started"]
assert not unstarted["forbidden_solver_model_assignment_proof_artifacts"]
assert preseal["status"] == "PASS" and preseal["solver_free_replay"]["runs"] == 20
assert preseal["solver_free_replay"]["comparisons"] == 35
assert preseal["repository_gates"]["status"] == "PASS" and preseal["repository_gates"]["checks"] == 9
for d in trace.values():
    assert d["classification"] == "SAT_SEARCH_TRACE" and d["unsat_certificate_credit"] == 0
    assert d["raw_sha256"] == d["roundtrip_sha256"] and d["lossless_roundtrip_verified"]

input_bindings = {
    "schema": "circdist-gross-round126-input-bindings-v1",
    "status": "PASS",
    "dispatch_hashes": actual_bindings,
    "protocol_hashes": {
        "DAG_PROTOCOL.md": sha(R / "bindings/DAG_PROTOCOL.md"),
        "FILE_PROTOCOL.md": sha(R / "bindings/FILE_PROTOCOL.md"),
    },
    "mandatory_iter198_semantic_source_sha256": "d41be17da8e398e13b94cf38807d78187247e7318d61ebbeb6d21bc2e7f43f9d",
    "mandatory_iter198_selector_state_sha256": "e25d5ad244f42075e6e4c3f884bb33300c50dbfbdf1bfa74324b1dd964438f53",
    "mandatory_iter198_counts": {"blocks": 814392, "selectors": 51840, "assertions": 870630},
    "mandatory_iter198_base": {"sha256": actual_bindings["input/iter198/formula/outer.cnf"], "variables": 3152127, "clauses": 11550293},
    "mandatory_iter198_order144_quotient": {"sha256": actual_bindings["input/iter198/order144_quotient/outer.cnf"], "variables": 4387647, "clauses": 21434596, "roots": 143},
    "mandatory_iter198_checked_unstarted_sha256": actual_bindings["input/iter198/CHECKED_UNSTARTED.json"],
    "proofpilot": {
        "sha256": actual_bindings["bindings/round126_proofpilot_rank.json"],
        "sole_winner": "CIRCDIST.gross@dstar-residual",
        "score": 5.4757105608047234e-05,
        "why": "solve the reviewed iteration198 quotient first and completely adjudicate both direct sectors for a SAT candidate",
    },
    "reviewed_parent_root_manifest_sha256": actual_bindings["bindings/round124_parent/SHA256SUMS.txt"],
    "parent_full_seal_rehash": {"path": "recovery_state/PARENT_SEAL_REHASH.json", "sha256": sha(R / "recovery_state/PARENT_SEAL_REHASH.json")},
    "input_identity_rehash": {"path": "recovery_state/recovery/INPUT_IDENTITY_REHASH.json", "sha256": sha(R / "recovery_state/recovery/INPUT_IDENTITY_REHASH.json")},
}
(R / "INPUT_BINDINGS.json").write_text(json.dumps(input_bindings, indent=2, sort_keys=True) + "\n")

fresh = {
    "schema": "circdist-gross-round126-fresh-frontier-v1",
    "status": "CHECKED_UNSTARTED",
    "iteration": 199,
    "started": False,
    "source_sha256": sha(F / "source.json.gz"),
    "source_semantic_payload_sha256": state199["source_semantic_payload_sha256"],
    "state_sha256": sha(F / "state.json"),
    "selector_state_sha256": state199["selector_state_sha256"],
    "checked_unstarted_sha256": sha(F / "CHECKED_UNSTARTED.json"),
    "blocks": state199["block_count"],
    "selectors": state199["selector_count"],
    "assertions": advance["output"]["assertions"],
    "base": {"sha256": base["cnf_sha256"], "variables": base["variables"], "clauses": base["clauses"]},
    "order144_quotient": {"sha256": quotient_check["bindings"]["quotient_cnf_sha256"], "variables": quotient_check["encoding"]["final_variables"], "clauses": quotient_check["encoding"]["final_clauses"], "roots": quotient_check["group"]["nonidentity"]},
    "new_selector_orbits": {"sizes": [72, 72, 72, 72], "selectors": 288, "Xerr": 144, "Zerr": 144, "all_288_group_elements_physically_replayed": True},
    "closure": {"translations": True, "css_involution": True, "extended_group_order": 144, "pairwise_collision_free": True, "inherited_registry_collision_free": True},
    "solver_invocations": 0,
    "forbidden_artifacts": [],
    "boundary": "Iteration 199 is deterministically prepared and checked unstarted; it was not solved in Round126.",
}
assert fresh == {**fresh,
    "source_sha256": "ceb91b607e6434f9ef20c6177ba1ee5792b8688790f88f5ec89ee5b75d8f715f",
    "source_semantic_payload_sha256": "bb10d914be3f18a885513b482dee2573dba4b1e3123d84e2cc1ffb1682a5ec2b",
    "state_sha256": "ba0795e0f82282193e6fe5c6566127fb69b680803cf50a216bcdb859933e39ab",
    "selector_state_sha256": "faa8d3745780c593b5e4e430c8c49c8bb223beb28f8b0d8ecbf384636e75a049",
    "checked_unstarted_sha256": "6b421a829cec5b07b63b8208443301f60d3e482735f6d20f722fe78563019f71",
    "blocks": 814392, "selectors": 52128, "assertions": 870918,
    "base": {"sha256": "c08af6fc567c6d8554428eac5873c276ee4b89137d7c6bff192baca4608a1f9d", "variables": 3162788, "clauses": 11584428},
    "order144_quotient": {"sha256": "602f91c302883ec3ad6a1d9c4cc6b31b450d00feba059707fdc5c37a69aa71e1", "variables": 4398308, "clauses": 21468731, "roots": 143},
}
(R / "FRESH_FRONTIER.json").write_text(json.dumps(fresh, indent=2, sort_keys=True) + "\n")

result = {
    "schema": "circdist-gross-round126-proposer-result-v1",
    "status": "PASS",
    "verdict": "ITER198_CANDIDATE_KILLED_BY_BOTH_COMPLETE_DIRECT360_SECTORS__ROOT_REMAINS_OPEN__ITER199_CHECKED_UNSTARTED",
    "artifact_name": R.name,
    "dispatch": input_bindings,
    "outer": {
        "status": "SATISFIABLE", "exact_mandatory_formula": True,
        "solver_run": solver_runs["outer"], "assignment": outer_assignment,
        "semantic_replay": outer_replay,
        "order144_orbit_controls": {"path": "output/iter198/solver/orbit_controls.json", "sha256": sha(E / "solver/orbit_controls.json"), "status": outer_orbit["status"], "orbit": outer_orbit["orbit"], "negative_controls": outer_orbit["negative_controls"]},
        "licensed_consequence": "The exact reviewed full iteration-198 base is SAT and has the decoded legal frozen 864-edge schedule; no broader unrestricted claim follows from the quotient alone.",
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
            "Xerr": {"size": 72, "stabilizer": x_orbit["stabilizer_deltas"], "audit_sha256": sha(R / "verification/Xerr_translation_orbit.json")},
            "Zerr": {"size": 72, "stabilizer": z_orbit["stabilizer_deltas"], "audit_sha256": sha(R / "verification/Zerr_translation_orbit.json")},
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
    "verification": {
        "preseal_summary_path": "recovery_state/recovery/PRESEAL_VERIFICATION.json",
        "preseal_summary_sha256": sha(preseal_path),
        "solver_free_replay": preseal["solver_free_replay"],
        "repository_gates": preseal["repository_gates"],
    },
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
        "Iteration 199 is prepared and checked unstarted but was not solved in this round.",
    ],
}
(R / "RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

environment = {
    "schema": "circdist-gross-round126-environment-v1", "status": "PASS",
    "platform": platform.platform(), "python": platform.python_version(),
    "solver_executable_sha256": sha(R / "tooling/cadical-1.9.5-arm64-macos"),
    "clean_environment": {"LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"},
    "strict_serial": True, "background_or_detached_children": 0,
}
assert environment["solver_executable_sha256"] == "fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9"
(R / "ENVIRONMENT.json").write_text(json.dumps(environment, indent=2, sort_keys=True) + "\n")

nonzero = [x for x in ledger if x.get("state") == "REAPED" and x.get("rc") not in (0, 10)]
admin = {
    "schema": "circdist-gross-round126-admin-interface-operations-v1", "status": "DISCLOSED",
    "science_processes": "All solver runs and all scientific checks were foreground, lock-serialized, non-detached, and STARTED/REAPED in the append-only JSONL ledger.",
    "runner_recovery": "The original runner and original STARTED/REAPED parent-seal history are retained. V2 streams stdout and stderr to separate files without buffering multi-GB output in RAM.",
    "bounded_management_outside_inner_ledger": [
        "Read-only rg, sed, find, cat, diff, hash, and JSON inspections used by the Codex execution interface.",
        "Scratch-only apply_patch source creation; no canonical, scheduler, review, protocol, prior artifact, or generated-view edit.",
        "Approved filtered process censuses used only to establish safe recovery and absence of duplicate solvers.",
    ],
    "repository_mutations_before_install": 0,
    "nonzero_runner_children": [{"tag": x["tag"], "rc": x["rc"], "stderr": x["stderr"]} for x in nonzero],
}
(R / "ADMIN_INTERFACE_OPERATIONS.json").write_text(json.dumps(admin, indent=2, sort_keys=True) + "\n")

failure_text = """# Round126 recovery and failure ledger

All events below are retained and receive zero positive scientific credit. SAT return code 10 is an expected solver result, not a failure.

- **F126-R001 — managed-cache refusal before parsing.** An initial `python -m py_compile` syntax attempt could not create a cache below a sandbox-blocked user path. The exact source later passed a no-write `ast.parse` check.
- **F126-R002 — read-only hash command handle lost.** A multi-file read-only hash inspection outlived its tool projection. Work paused; an approved filtered process census found no Round126 or solver process. Zerr was rehashed separately and again during a complete compression/decompression pass.
- **F126-R003 — patch interface refused an absolute in-place update.** No file changed. A hash-bound adaptation program replaced that administrative route.
- **F126-R004 — first frontier-adapter count guard, rc1.** The expected `r124` literal count was 9 rather than 10. All replacements remained in memory; the target stayed byte-identical. The corrected full run passed.
- **F126-R005 — second frontier-adapter run, rc1.** The parent copy retained sealed read-only mode. It failed at the final write after all in-memory assertions. Scratch permission was changed explicitly and the complete adaptation passed.
- **F126-R006 — first checker-adapter count guard, rc1.** The quotient checker contained three `iteration-198` literals rather than two. The already written CSS checker was byte-correct; an idempotent full retry produced and parsed all three intended checkers.
- **F126-R007 — first package-tree assembly, rc1.** The ordinary copy inherited a read-only `source/` directory and could not overlay new Round126 sources. The original 915-byte stderr is retained at `logs/session_and_process/transcripts/assemble-round126-package-tree.stderr` (SHA-256 `ec345e341ac6ab0b3af113891d834b3e63cb64f08dcf41b8b8521c96207a99be`). The 333-file, 7,603,830,923-byte partial tree was renamed to `/private/tmp/circdist_gross_iter198_order144_continuation_round126_20260905.failed_assembly1` and remains preserved. `recovery_state/recovery/FAILED_ASSEMBLY1_INVENTORY.json` binds every file with canonical inventory SHA-256 `50a13b8da91274e78ad7ea623e1fb8239fcfefeb98f7a5c7b0a44542e8e2513c`. The exact failed source is reconstructed as `source/assemble_package_tree_round126.failed1.py` (SHA-256 `72e881bca05b15c35cb3ee2644377ef24d18fdeadd917b3f56e00225f9997182`). The only correction opens the newly copied destination `source/` directory to mode 0755 before adding ordinary copied Round126 sources; payload and scientific inputs are unchanged. The full retry passed.
- **F126-R008 — first document-writer invocation, rc1.** A generic status assertion included the inherited vendor direct replay, whose older schema has no top-level `status` field. No document had yet been written. The assertion was replaced by exact checks of its schedule `ok`, repair gate, and both all-clause flags; the complete retry passed.
- **F126-R009 — first solver-free preseal replay, rc1.** Result, process-ledger, complete outer assignment, and physical schedule replay passed. The order-144 orbit-control command then requested legacy filename `trace.json.gz`; the reviewed iteration-198 frontier names the same required trace `build_trace.json.gz`. The 23-file, 74,826,238-byte failed replay tree is retained verbatim at `recovery_state/recovery/PRESEAL_REPLAY_FAILED1`; its canonical inventory SHA-256 is `198bb3e9681b564c7b51bb0c51c07037278eaed0365524f22f424da428d31dd9`. The replay path alone was corrected and the complete replay restarted from byte zero; no solver ran and no scientific evidence changed.

The three proof-output streams are classified `SAT_SEARCH_TRACE` and receive zero UNSAT-certificate credit. No repair branch was entered because both complete direct sectors were SAT.
"""
(R / "FAILURE_LEDGER.md").write_text(failure_text)

theorem = """# Round126 theorem and scope notes

## 1. Exact quotient consequence

Let `B198(t,u)` be the reviewed base CNF. Its primary variables encode ten-bit edge times `t`, and `u` are uniquely constrained definitional auxiliaries. Let

`G = (Z_12 x Z_6) semidirect C_2`, with `|G|=144`.

The quotient is

`Q198 = B198 AND (AND over g != e of LexLE(t, g.t))`.

Every appended lex comparator is an exact Boolean recurrence, every appended clause was reconstructed independently, and the base CNF is a byte-exact prefix. Since `B198` is invariant under `G`, each finite `G`-orbit of base models has a lexicographically least primary-time vector. That least vector satisfies all 143 non-strict leaders, so `SAT(B198) => SAT(Q198)`. The reverse implication is immediate because `B198` is a conjunct of `Q198`. This argument permits stabilizers and assumes no free action. The retained model assigns all 4,387,647 variables, satisfies all 21,434,596 clauses, and is independently shown to be the least of 144 distinct schedule images.

## 2. Complete direct-360 mechanism criterion

For a sector `S`, enumerate all 360 physical fault columns `c_j` and Boolean selectors `y_j`. Let `H_S` contain all 72 detector rows and `L_S` all 12 logical rows. The direct query is exactly

`sum_j y_j <= 10`,

`H_S (sum_j y_j c_j) = 0 over GF(2)`,

`OR_r [L_S (sum_j y_j c_j)]_r = 1`.

There is no pool, residual-pattern, check-count, within-check-family, sampling, or partial restriction. Each sector returned a complete weight-10 SAT assignment. Separate clause checkers cover every variable and clause. A standard-library auditor reconstructs all 360 columns per sector, the canonical and physical supports, all 72 syndrome bits, all 12 logical bits, stabilizer membership in both representations, stabilizer rank 66, logical quotient dimension 12, and cross-pairing rank 12. Therefore either SAT sector is a sound candidate-kill certificate; both sectors are retained for symmetric adjudication.

## 3. Translation and CSS closure

Write a coordinate as `q=6i+j`, with `i in Z_12`, `j in Z_6`. Translation acts by

`T_(a,b)(q) = 6((i+a) mod 12) + ((j+b) mod 6)`

in each 72-qubit half. CSS duality swaps `X` and `Z`, negates the check coordinate, and maps data coordinates by exchanging halves and negating the within-half coordinate. Residual kind is fixed. Direct enumeration on all 864 named edges verifies `D^2=I` and `D T_delta D=T_-delta`, giving the order-144 action. Each of the Xerr, Zerr, CSS-dual-of-Xerr, and CSS-dual-of-Zerr translation orbits has identity stabilizer and size 72. All 288 schedules and mechanisms were physically replayed. Full semantic tuple comparisons prove the four orbits pairwise disjoint and collision-free against the 51,840-selector inherited registry.

## 4. Scientific boundary

The iteration-198 schedule candidate is killed and 288 sound selector exclusions are installed in a deterministic iteration-199 frontier. This is material progress, but it is not a legal distance-12 witness, a whole-family universal distance-at-most-11 theorem, root closure, exhaustion, or interval narrowing. `CIRCDIST.gross` and `gap-via-lift` remain `CONJECTURED`; `D*_Gross` remains in `{11,12}`.
"""
(R / "THEOREM_NOTES.md").write_text(theorem)

x, z = direct["sectors"]["Xerr"], direct["sectors"]["Zerr"]
raw_total = sum(d["raw_bytes"] for d in trace.values())
gzip_total = sum(d["gzip_bytes"] for d in trace.values())
report = f"""# CIRCDIST.gross Round126 exact iteration-198 continuation

## Verdict and safe boundary

The exact reviewed iteration-198 order-144 quotient is **SAT**. Its complete assignment covers all 4,387,647 variables exactly once and satisfies all 21,434,596 clauses. It decodes to a legal frozen 864-edge schedule. Both mandatory complete unrestricted direct-360 sectors are **SAT** at exact fault weight 10. Either checked sector kills the candidate; both were adjudicated. Repair and gap analysis were therefore forbidden and not attempted.

Four free generalized-dihedral selector orbits of size 72 add 288 distinct sound exclusions. Iteration 199 is sealed **CHECKED_UNSTARTED** and was never solved. Root status is unchanged: `CIRCDIST.gross = CONJECTURED`, `gap-via-lift = CONJECTURED`, and `D*_Gross = {{11,12}}`.

## Dispatch and exact reviewed input

The scheduler, ProofPilot record, canonical Gross node, Round125 review, and Round124 parent seal match `INPUT_BINDINGS.json`. A 608-file independent parent rehash passed before use. The mandatory frontier has source `{actual_bindings['input/iter198/source.json.gz']}`, semantic `d41be17da8e398e13b94cf38807d78187247e7318d61ebbeb6d21bc2e7f43f9d`, state `{actual_bindings['input/iter198/state.json']}`, selector-state `e25d5ad244f42075e6e4c3f884bb33300c50dbfbdf1bfa74324b1dd964438f53`, 814,392 blocks, 51,840 selectors, and 870,630 assertions. Its base has 3,152,127 variables and 11,550,293 clauses; the exact quotient has 4,387,647 variables, 21,434,596 clauses, and 143 nonidentity roots. Receipt `{actual_bindings['input/iter198/CHECKED_UNSTARTED.json']}` records zero prior solver starts and no forbidden artifacts.

## Proof-first outer solve and independent controls

Pinned CaDiCaL SHA-256 is `{environment['solver_executable_sha256']}`. The exact sealed quotient was passed directly, with the proof-output pathname present in the initial argv and binary proof mode disabled. Child PID {solver_runs['outer']['child_pid']} ran from `{solver_runs['outer']['start_utc']}` to `{solver_runs['outer']['end_utc']}`, returned 10, produced {solver_runs['outer']['stdout_bytes']:,} stdout bytes and zero stderr bytes, and was reaped without timeout or detachment.

The assignment checker covers every variable and clause. Independent semantic replay gives schedule SHA-256 `{outer_replay['compressed_schedule_sha256']}` with 343 layers `0..342`, zero conflicts, all 648 MC overlaps satisfied, global interleaving, 108 overlap-interleaved pairs, 375 whole-check-interleaved pairs, and zero block or selector hits. A separate orbit control enumerates all 144 schedule images, proves identity stabilizer and lexicographic minimality, checks 1,235,520 recurrence values and all 143 roots, and rejects constant-bit mutation, assignment truncation, reversed lex direction, and omitted-root controls.

The exact equivalence derivation is in `THEOREM_NOTES.md`: byte-exact base prefix plus finite-orbit least representatives proves `SAT(Q198) iff SAT(B198)` without assuming freeness.

## Complete unrestricted direct-360 adjudication

Both formulas sit outside the outer encoding and use every one of 360 physical columns. Their only semantic constraints are `W<=10`, all 72 detector parities zero, and a nonzero vector among all 12 logical rows.

### Xerr

- CNF `{x['cnf_sha256']}`, {x['variables']:,} variables / {x['clauses']:,} clauses; every clause checked.
- Selected faults: `{', '.join(x['selected_names'])}`.
- Canonical support `{x['canonical_net_support']}`; physical support `{x['physical_net_support']}`.
- Syndrome `{x['physical_syndrome']}`; logical vector `{x['logical_parities']}`; both canonical and physical supports are outside the stabilizer span.
- Flipping selected variable {x['negative_control']['flip_selected_var']} fails {x['negative_control']['failed_clause_count']} clauses, first at {x['negative_control']['first_failed_clause']}.

### Zerr

- CNF `{z['cnf_sha256']}`, {z['variables']:,} variables / {z['clauses']:,} clauses; every clause checked.
- Selected faults: `{', '.join(z['selected_names'])}`.
- Canonical and physical support `{z['physical_net_support']}`.
- Syndrome `{z['physical_syndrome']}`; logical vector `{z['logical_parities']}`; both canonical and physical supports are outside the stabilizer span.
- Flipping selected variable {z['negative_control']['flip_selected_var']} fails {z['negative_control']['failed_clause_count']} clauses, first at {z['negative_control']['first_failed_clause']}.

The vendored physical replay and an independent standard-library reconstruction agree. Because both complete sectors are SAT, the candidate is rejected and the protocol forbids a repair attempt.

## Exact orbit accounting and fresh iteration 199

The four translation orbits have sizes `[72,72,72,72]`, stabilizer `{{(0,0)}}` in each case, 288 distinct selector tuples, no pairwise collision, and no collision with the inherited registry. Every original and CSS-dual translated schedule is legal and every translated mechanism remains weight at most 10, zero-syndrome, and nonstabilizer. The full registry is closed under translations and the CSS involution.

Fresh identities are source `{fresh['source_sha256']}`, semantic `{fresh['source_semantic_payload_sha256']}`, state `{fresh['state_sha256']}`, selector-state `{fresh['selector_state_sha256']}`. Counts are 814,392 blocks, 52,128 selectors, and 870,918 assertions. The independently checked base is `{fresh['base']['sha256']}` with 3,162,788 variables / 11,584,428 clauses. The independently checked order-144 quotient is `{fresh['order144_quotient']['sha256']}` with 4,398,308 variables / 21,468,731 clauses / 143 roots. Receipt `{fresh['checked_unstarted_sha256']}` records zero iteration-199 solver invocations and no forbidden artifact.

## Streams, failures, and limits

Before sealing, the solver-free replay completed 20 strict-serial child runs and 35 byte-exact or runtime-normalized semantic comparisons. It regenerated iteration 199, reconstructed and checked every base and quotient clause, replayed all outer/direct/orbit/CSS evidence, and reconfirmed the never-solved boundary. Nine repository gates passed, including both proof-DAG scopes, migration/contracts/self-test checks, duplicate-YAML scan, `git diff --check`, and evidence closure. Their exact logs and run records are retained under `recovery_state/recovery`.

All three proof-output streams were enabled from byte zero. Because every solver result is SAT, they are search histories rather than UNSAT certificates. The complete streams contain {raw_total:,} raw bytes and {gzip_total:,} deterministic-gzip bytes. Each compressed file was decompressed in full and matched on byte count, LF count, and SHA-256. They receive zero UNSAT-certificate credit.

`FAILURE_LEDGER.md` discloses recovery, adapter, and first-assembly failures. They changed no scientific conclusion and receive no credit. The original interrupted-worker ledger history is preserved. All scientific children were foreground, strict-serial, non-detached, and reaped, with no solver timeout.

This package supplies a checked candidate kill and 288 additional sound CEGAR exclusions. It supplies neither a distance-12 witness nor a universal `<=11` theorem, so it does not close the root or narrow the interval.
"""
(R / "REPORT.md").write_text(report)

print(json.dumps({
    "status": "PASS", "result_sha256": sha(R / "RESULT.json"),
    "report_sha256": sha(R / "REPORT.md"),
    "fresh_frontier_sha256": sha(R / "FRESH_FRONTIER.json"),
    "raw_sat_trace_bytes": raw_total, "gzip_sat_trace_bytes": gzip_total,
}, sort_keys=True))
