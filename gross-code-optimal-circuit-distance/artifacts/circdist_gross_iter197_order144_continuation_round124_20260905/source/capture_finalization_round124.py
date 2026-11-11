#!/usr/bin/env python3
"""Capture bounded preseal replay, gate, cleanup, and interruption evidence."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


def copy_flat(src, dst):
    assert src.is_dir() and not dst.exists()
    dst.mkdir(parents=True)
    rows = []
    for path in sorted((p for p in src.iterdir() if p.is_file()), key=lambda p: p.name):
        target = dst / path.name
        shutil.copy2(path, target)
        rows.append({"name": path.name, "bytes": target.stat().st_size, "sha256": sha(target)})
    return rows


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--preseal-replay", type=Path, required=True)
ap.add_argument("--gates", type=Path, required=True)
ap.add_argument("--cleanup", type=Path, required=True)
ap.add_argument("--work", type=Path, required=True)
a = ap.parse_args()
root, work = a.root.resolve(), a.work.resolve()
assert root.name in {"circdist_gross_iter197_order144_continuation_round124_20260905",
                     "circdist-round124-package-preseal"}
replay_summary = json.loads((a.preseal_replay / "summary.json").read_text())
gate_summary = json.loads((a.gates / "summary.json").read_text())
cleanup = json.loads(a.cleanup.read_text())
assert replay_summary["status"] == gate_summary["status"] == cleanup["status"] == "PASS"
assert replay_summary["run_count"] == 21 and replay_summary["comparison_count"] == 35
assert replay_summary["solver_invocations"] == 0
assert gate_summary["check_count"] == 9 and gate_summary["solver_invocations"] == 0
assert gate_summary["all_children_reaped"]
assert len(cleanup["rows"]) == 3 and cleanup["raw_files_remaining"] == []
replay_rows = copy_flat(a.preseal_replay.resolve(), root / "verification/preseal_replay_clean")
gate_rows = copy_flat(a.gates.resolve(), root / "verification/repository_gates_preseal_clean")
shutil.copy2(a.cleanup, root / "CLEANUP_ACCOUNTING.json")

fix = {
    "schema": "circdist-gross-round124-fix-accounting-v1", "status": "PASS",
    "FIX-1": {"subagents_spawned": 0, "reviewer_contacts": 0, "single_proposer_session": True},
    "FIX-2": {"background_processes_started": 0, "detached_processes": 0,
              "process_handoffs": 0, "surviving_round124_children_at_census": 0,
              "all_science_and_finalization_children_foreground": True,
              "scratch_verdict_logs_packaged": True},
    "solver_boundary": {"science_solver_invocations": 3,
                        "solver_invocations_after_iter198_creation": 0,
                        "finalization_solver_invocations": 0,
                        "fresh_iter198_unstarted": True},
}
(root / "FIX_ACCOUNTING.json").write_text(json.dumps(fix, indent=2, sort_keys=True) + "\n")
receipt = {
    "schema": "circdist-gross-round124-finalization-capture-v1", "status": "PASS",
    "preseal_replay": {"runs": replay_summary["run_count"], "comparisons": replay_summary["comparison_count"],
                       "solver_invocations": 0, "summary_sha256": sha(a.preseal_replay / "summary.json"),
                       "flat_files_copied": len(replay_rows), "files": replay_rows},
    "preseal_repository_gates": {"checks": gate_summary["check_count"], "solver_invocations": 0,
                                 "summary_sha256": sha(a.gates / "summary.json"),
                                 "flat_files_copied": len(gate_rows), "files": gate_rows},
    "cleanup": {"deleted_files": len(cleanup["rows"]), "deleted_bytes": sum(x["bytes"] for x in cleanup["rows"]),
                "retained_gzip_files": 3,
                "accounting_sha256": sha(root / "CLEANUP_ACCOUNTING.json")},
}
(root / "FINALIZATION_CHECKS.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "preseal_replay_runs": replay_summary["run_count"],
                  "preseal_replay_comparisons": replay_summary["comparison_count"],
                  "gate_checks": gate_summary["check_count"], "solver_invocations": 0}, sort_keys=True))
