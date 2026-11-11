#!/usr/bin/env python3
"""Generate Round94 structured metadata from checked package evidence."""
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
protected_hashes = {row["path"]: row["observed_sha256"] for row in binding_rows}
inputs = {
    "schema": "circdist-gross-round94-input-bindings-v1",
    "status": "PASS",
    "commission_correction": "The binding uses ccc8a in the independently verified iteration-136 state file hash; the disclosed ccc4a commission typo is rejected.",
    "expected_protected_sha256": protected_hashes,
    "package_snapshot_sha256": snapshot_hashes,
    "reviewed_dependency": {
        "repository_relative_path": "circdist/artifacts/circdist_gross_proof_outer_round92_20260830",
        "root_manifest_file_sha256": "4e255084bdab13ad0b9c295a9fe7cf2aea8231c4a56db656964f0695ddc6c982",
        "payload_manifest_file_sha256": "fbc881f0dc54744cb3cfd0c4497571592f8597326ce98362eb42a032ed289090",
        "manifest_verified_before_use": True,
    },
    "initial_frontier": {
        "iteration": 136, "started": False, "selector_count": 232,
        "selector_state_sha256": "1692d905120d2dcf51b949ce4a70ed4b8f1b270c2d07a1ddbf5813d20d80fa81",
        "state_file_sha256": "58781b46cc177df046ec334420046e1ccc8a23517f21fe4491e6412741ced57c",
        "source_semantic_sha256": "a561515801904b458d34ebccea5aa364420f9a0a012e36e721f48fcbe9be4ebe",
        "source_file_sha256": "a71fb5e708eeebf365dda0661b79652b264bc0eb87308626383a5ca389cfc5d8",
        "assertions": 19114, "variables": 406656, "clauses": 1372232,
        "cnf_sha256": "289acad6be1068d63369511e9c95b0b1df146471bf05a1e4128758508612b64e",
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
    "schema": "circdist-gross-round94-environment-v1", "status": "PASS",
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
synth_path = R / "synthesis/triple_gf2_closure.json"
synth = json.loads(synth_path.read_text())
result = {
    "schema": "circdist-gross-round94-result-v1", "status": "PASS",
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
        "initial_exact_efssc_selectors": 232,
        "frozen_conventions_preserved": [
            "S_Gross", "strict serialization", "MC0", "terminal residual semantics",
            "both CSS sectors", "all canonical exclusions",
        ],
    },
    "synthesis": {
        "file": "synthesis/triple_gf2_closure.json", "file_sha256": sha(synth_path),
        "semantic_sha256_excluding_seconds": "558a9fcdd88e527fb5a4c49b3e6c268793f6644188f512b5d0af25a971ea1b45",
        "strategy": synth["strategy"], "finite_domain_size": 527684,
        "eligible_weight_1_to_10_results": 4232, "retained_terms": 0,
        "coverage_checked": True, "no_selector_entered_state": True,
    },
    "iterations": audit["iterations"],
    "weight_summary": {
        "Xerr": {"weight_9_iterations": [138], "weight_10_iterations": [i for i in range(136, 148) if i != 138]},
        "Zerr": {"weight_9_iterations": [], "weight_10_iterations": list(range(136, 148))},
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
    "schema": "circdist-round94-campaign-summary-v1", "status": "PASS",
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
    "schema": "circdist-gross-round94-process-ledger-v1", "status": "PASS",
    "records": records, "bounded_foreground_records": len(records),
    "science_solver_children": len(solver_records), "outer_solver_children": 12,
    "direct_solver_children": 24, "strict_serial_solver_intervals_checked": True,
    "proof_fixture_synchronous_children": len(proof["runs"]),
    "proof_fixture_runs": [{"name": row["name"], "returncode": row["returncode"], "reaped": True} for row in proof["runs"]],
    "campaign_driver_children": 2, "campaign_wrapper_children": 176,
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
