#!/usr/bin/env python3
"""Bind Round126 preseal replay, gates, live inputs, and retained failures."""
import argparse
import hashlib
import json
from pathlib import Path


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


p = argparse.ArgumentParser()
p.add_argument("--repository", type=Path, required=True)
p.add_argument("--root", type=Path, required=True)
p.add_argument("--work", type=Path, required=True)
p.add_argument("--output", type=Path, required=True)
a = p.parse_args(); repo, root, work = a.repository.resolve(), a.root.resolve(), a.work.resolve()
expected = {
    "operations/circdist/SCHEDULER.yaml": "32ea25bdbc185a9fb81fc9f70b671e8f3bcd2ffd2132c3e11e29a5cb70566b20",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "81aa12cefb726fe3364b1d92563258dfd6463b7445d7ff7ee4e7a1ba2bf37d8c",
    "circdist/reviews/circdist_gross_iter197_order144_continuation_round124_exact_review_round125_20260905.md": "c820a120e2d938218b8fc3e5b235f29dd93d13b8d4c333d52e9c057a6da73a55",
}
assert {rel: sha(repo / rel) for rel in expected} == expected
assert sha(Path("/private/tmp/circdist-round126-proofpilot-rank.json")) == "b671a6c4ec3c4b896ec206c30a1c073cc8fc9e1e6dd8d01eb207a73b5baf3a2c"

replay = json.loads((work / "work/recovery/PRESEAL_REPLAY_PASS/summary.json").read_text())
replay_inv_path = work / "work/recovery/PRESEAL_REPLAY_PASS_INVENTORY.json"
replay_inv = json.loads(replay_inv_path.read_text())
failed_inv_path = work / "work/recovery/PRESEAL_REPLAY_FAILED1_INVENTORY.json"
failed_inv = json.loads(failed_inv_path.read_text())
assembly_inv_path = work / "work/recovery/FAILED_ASSEMBLY1_INVENTORY.json"
assembly_inv = json.loads(assembly_inv_path.read_text())
gates_path = work / "work/recovery/REPOSITORY_GATES_PRESEAL/summary.json"
gates = json.loads(gates_path.read_text())
result_path = work / "verification/preseal_result_check.json"
process_path = work / "verification/preseal_process_ledger_check.json"
result = json.loads(result_path.read_text()); process = json.loads(process_path.read_text())
assert replay["status"] == "PASS" and replay["run_count"] == 20 and replay["comparison_count"] == 35
assert replay["solver_invocations"] == 0 and replay["fresh_iter199_remained_unstarted"]
assert replay_inv["status"] == "PASS" and replay_inv["file_count"] == 100
assert replay_inv["canonical_inventory_sha256"] == "054408f8fcd635a264254df7b6e8532113560eeca1c493580ed90027e6bf8259"
assert failed_inv["canonical_inventory_sha256"] == "198bb3e9681b564c7b51bb0c51c07037278eaed0365524f22f424da428d31dd9"
assert assembly_inv["canonical_inventory_sha256"] == "50a13b8da91274e78ad7ea623e1fb8239fcfefeb98f7a5c7b0a44542e8e2513c"
assert gates["status"] == "PASS" and gates["check_count"] == 9
assert gates["all_children_reaped"] and gates["solver_invocations"] == 0
assert gates["evidence_closure_interpretation"]["status"] == "PASS"
assert result["status"] == process["status"] == "PASS"
assert process["solver_processes_total"] == 3 and process["iter199_solver_invocations"] == 0
assert not any((root / x).exists() for x in ("SEAL.json", "SHA256SUMS.txt", "FILE_INVENTORY.jsonl"))

out = {
    "schema": "circdist-gross-round126-preseal-verification-summary-v1", "status": "PASS",
    "live_canonical_hashes": expected,
    "proofpilot_sha256": "b671a6c4ec3c4b896ec206c30a1c073cc8fc9e1e6dd8d01eb207a73b5baf3a2c",
    "solver_free_replay": {"status": "PASS", "runs": 20, "comparisons": 35,
        "inventory_path": "recovery_state/recovery/PRESEAL_REPLAY_PASS_INVENTORY.json",
        "inventory_sha256": sha(replay_inv_path),
        "canonical_tree_inventory_sha256": replay_inv["canonical_inventory_sha256"],
        "tree_files": replay_inv["file_count"], "tree_bytes": replay_inv["total_bytes"]},
    "repository_gates": {"status": "PASS", "checks": 9, "solver_invocations": 0,
        "summary_path": "recovery_state/recovery/REPOSITORY_GATES_PRESEAL/summary.json",
        "summary_sha256": sha(gates_path), "evidence_closure_raw_exit": gates["evidence_closure_raw_exit"]},
    "preseal_result_check_sha256": sha(result_path),
    "preseal_process_ledger_check_sha256": sha(process_path),
    "failed_replay_tree_inventory_sha256": failed_inv["canonical_inventory_sha256"],
    "failed_assembly_tree_inventory_sha256": assembly_inv["canonical_inventory_sha256"],
    "seal_files_absent_at_check": True, "fresh_iter199_unstarted": True,
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
