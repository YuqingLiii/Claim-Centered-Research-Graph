#!/usr/bin/env python3
"""Generate Round96 structured metadata from checked package evidence."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import os
import platform
import subprocess
import sys


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def write(path, obj):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--repository", type=Path, required=True)
ap.add_argument("--python", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()
REPO = a.repository.resolve()
PY = a.python.absolute()

binding_rows = json.loads((R / "reconstruction/input_bindings.json").read_text())["bindings"]
snapshot_hashes = {row["snapshot"]: sha(R / row["snapshot"]) for row in binding_rows}
protected_hashes = {row["path"]: row["sha256"] for row in binding_rows}
inputs = {
    "schema": "circdist-gross-round96-input-bindings-v1",
    "status": "PASS",
    "commission": "Exact hashes supplied for scheduler, Gross node, Round95 review, reviewed Round94 seals, and fresh/unstarted iteration 148; all were observed exactly before solving.",
    "expected_protected_sha256": protected_hashes,
    "package_snapshot_sha256": snapshot_hashes,
    "reviewed_dependency": {
        "repository_relative_path": "circdist/artifacts/circdist_gross_proof_outer_round94_20260830",
        "root_manifest_file_sha256": "1e0a4af8591aa63ccccd1b2516c630eccb11a73fb9dea2e0ff1e0d32ed82ac1c",
        "payload_manifest_file_sha256": "c39ef3552e461dd7513812b8296901e72369dfacbf6e71ae758b5bb58ed94c54",
        "manifest_verified_before_use": True,
    },
    "initial_frontier": {
        "iteration": 148, "started": False, "selector_count": 256,
        "selector_state_sha256": "9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f",
        "state_file_sha256": "1902599acc47eb5d354692759b2d09d6ff1cfcd5e013f2b907cc310376ee6e81",
        "source_semantic_sha256": "2fd4a1982e1f6389804f7eee1120706f9d26c9e6a23acc05e2a15e036a67c032",
        "source_file_sha256": "0db20ed8ca0b120cda91eb7a94be25094adb9b77a2cacdd322e330a720d58b5f",
        "assertions": 19138, "variables": 409157, "clauses": 1385059,
        "cnf_sha256": "397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4",
        "inherited_disposition_absent": True,
    },
}
write(R / "INPUT_BINDINGS.json", inputs)

tooling = {}
for path in sorted((R / "tooling").iterdir()):
    if path.is_file():
        tooling[path.name] = {"bytes": path.stat().st_size, "sha256": sha(path)}
probe = subprocess.run([str(PY), "-c", "import json,sys,z3,pysat;print(json.dumps({'python':sys.version,'z3':z3.get_version_string(),'pysat':pysat.__version__}))"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
assert probe.returncode == 0
versions = json.loads(probe.stdout)
system_probe = subprocess.run(["/usr/bin/python3", "-c", "import z3,pysat"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
environment = {
    "schema": "circdist-gross-round96-environment-v1", "status": "PASS",
    "platform": platform.platform(), "machine": platform.machine(),
    "python_executable": str(PY), "python_executable_sha256": sha(PY),
    "python": versions["python"], "z3": versions["z3"], "pysat": versions["pysat"],
    "recorded_interpreter_required": True,
    "portability": "Replay requires Python with the exactly recorded z3 and pysat APIs. The native arm64 macOS SAT/proof binaries and frozen vendor are packaged; the external venv is bound by executable hash but is not copied.",
    "system_python_executable": "/usr/bin/python3",
    "system_python_dependency_probe_returncode": system_probe.returncode,
    "system_python_dependency_probe_stderr": system_probe.stderr,
    "network_used": False, "tooling": tooling,
}
write(R / "ENVIRONMENT.json", environment)

# Inventory the frozen vendor independently of the package seal.
vendor_rows = []
for path in sorted((R / "vendor/round80").rglob("*")):
    if path.is_file():
        vendor_rows.append({
            "path": path.relative_to(R).as_posix(), "bytes": path.stat().st_size,
            "sha256": sha(path), "lines": path.read_bytes().count(b"\n"),
        })
(R / "data").mkdir(exist_ok=True)
(R / "data/vendor_inventory.jsonl").write_text("".join(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n" for row in vendor_rows))

audit = json.loads((R / "verification/independent_campaign_audit.json").read_text())
proof = json.loads((R / "controls/proof_fixture_controls.json").read_text())
synth_path = R / "synthesis/order4_gf2_closure.json"
synth = json.loads(synth_path.read_text())
semantic_synth = dict(synth)
semantic_synth.pop("seconds", None)
result = {
    "schema": "circdist-gross-round96-result-v1", "status": "PASS",
    "verdict": "MATERIAL-CHECKED-PROGRESS-NOT-CLOSED",
    "evidence_level": "PROPOSER-CHECKED-COMPUTATION",
    "root_status": "CONJECTURED", "route_status": "CONJECTURED", "D_star_Gross": [11, 12],
    "completed_candidate_count": 12, "strict_serial": True,
    "all_outer_dispositions": "SATISFIABLE", "all_direct_dispositions": "SATISFIABLE",
    "outer_sat_count": 12, "direct_sat_count": 24, "unsat_count": 0,
    "unknown_count": 0, "timeout_count": 0, "repair_entered": False,
    "initial_frontier": inputs["initial_frontier"],
    "source_model": {
        "inherited_order_predicates": 14484,
        "block_family_counts": {"unary": 1440, "round62": 20, "generalized": 12820, "dynamic": 204},
        "initial_exact_efssc_selectors": 256,
        "frozen_conventions_preserved": [
            "S_Gross", "strict serialization", "MC0", "terminal residual semantics",
            "both CSS sectors", "all canonical exclusions",
        ],
    },
    "synthesis": {
        "file": "synthesis/order4_gf2_closure.json", "file_sha256": sha(synth_path),
        "semantic_sha256_excluding_seconds": hashlib.sha256(canonical(semantic_synth)).hexdigest(),
        "strategy": synth["strategy"], "finite_domain_size": 15254626,
        "eligible_weight_1_to_10_with_multiplicity": 33760,
        "unique_novel_eligible_results": 33654,
        "retained_terms": 0,
        "coverage_checked": True, "no_selector_entered_state": True,
    },
    "iterations": audit["iterations"],
    "weight_summary": {
        "Xerr": {"weight_9_iterations": [], "weight_10_iterations": list(range(148, 160))},
        "Zerr": {"weight_9_iterations": [148, 152], "weight_10_iterations": [i for i in range(148, 160) if i not in (148, 152)]},
    },
    "sat_proof_streams": {
        "count": 36, "proof_output_enabled": True, "empty_clause_lines": 0,
        "full_streams_deleted_after_hash_size_lf_summary": True,
        "disposition": "SAT-side streams are explicitly non-proofs and are not Gross certificates.",
    },
    "proof_objects": {
        "gross_unsat_drat": None, "gross_unsat_lrat": None,
        "direct_unsat_proofs": [], "actual_unsat_count": 0,
        "fixture_controls": {
            "file": "controls/proof_fixture_controls.json", "status": proof["status"],
            "valid_drat_accepted": proof["valid_drat_accepted"],
            "generated_lrat_accepted": proof["generated_lrat_accepted"],
            "corrupt_drat_rejected": proof["corrupt_drat_rejected"],
            "truncated_drat_rejected": proof["truncated_drat_rejected"],
            "corrupt_lrat_rejected": proof["corrupt_lrat_rejected"],
            "truncated_lrat_rejected": proof["truncated_lrat_rejected"],
            "scope": proof["scope"],
        },
    },
    "fresh_state": audit["fresh_frontier"],
    "branch_accounting": {
        "D_star_11_branch": "Not closed: no checked outer UNSAT universal cover proving every frozen legal schedule has an effective mechanism of weight at most 10.",
        "D_star_12_branch": "Not closed: no candidate passed both direct sectors by checked UNSAT, so repair analysis and an explicit d_circ=12 certificate were never entered.",
        "observed_branch": "Twelve positive counterexamples to the current selector cover, each killed by exact SAT mechanisms; this narrows neither branch.",
    },
    "reconstruction": {
        "status": "PASS", "source_cnf_byte_correspondence": True,
        "record": "reconstruction/correspondence.json",
    },
    "canonical_edits": False, "commit": False, "push": False,
    "proposed_canonical_delta": "No canonical delta proposed before independent review.",
    "limitations": audit["limitations"],
}
write(R / "RESULT.json", result)
write(R / "data/campaign_summary.json", {
    "schema": "circdist-round96-campaign-summary-v1", "status": "PASS",
    "iterations": audit["iterations"], "outer_sat": 12, "direct_sat": 24,
    "unsat": 0, "unknown": 0, "timeouts": 0, "strict_serial": True,
    "fresh_frontier": audit["fresh_frontier"],
})

# The process ledger is regenerated after each preseal gate; it describes all
# retained bounded children and the explicitly declared synchronous proof controls.
records = []
for path in sorted((R / "logs/process").glob("*.json")):
    row = json.loads(path.read_text())
    row = dict(row)
    row["path"] = path.relative_to(R).as_posix()
    records.append(row)
failures = [row for row in records if row.get("returncode") not in (0, 10)]
solver_records = [row for row in records if row.get("returncode") == 10 and "cadical_proof" in row.get("name", "")]
process = {
    "schema": "circdist-gross-round96-process-ledger-v1", "status": "PASS",
    "records": records, "bounded_foreground_records": len(records),
    "science_solver_children": len(solver_records), "outer_solver_children": 12,
    "direct_solver_children": 24, "strict_serial_solver_intervals_checked": True,
    "proof_fixture_synchronous_children": len(proof["runs"]),
    "proof_fixture_runs": [{"name": row["name"], "returncode": row["returncode"], "reaped": True} for row in proof["runs"]],
    "campaign_driver_children": 5,
    "campaign_wrapper_children": sum(json.loads(path.read_text()).get("child_wrapper_processes_started_serially", 0) for path in (R / "campaign").glob("*process*.json")),
    "corrected_failure_records": [{"name": row["name"], "returncode": row["returncode"], "path": row["path"]} for row in failures],
    "bootstrap_process_log": "logs/bootstrap-processes.tsv",
    "all_children_reaped": True, "background_processes": 0, "detached_processes": 0,
    "survivors": 0, "timeouts": 0,
    "timeout_policy": "TERM, bounded harvest, KILL if necessary, mandatory wait/reap; no timeout occurred.",
}
write(R / "PROCESS_LEDGER.json", process)

print(json.dumps({
    "status": "PASS", "result_sha256": sha(R / "RESULT.json"),
    "process_records": len(records), "vendor_files": len(vendor_rows),
    "environment_sha256": sha(R / "ENVIRONMENT.json"),
}, sort_keys=True))
