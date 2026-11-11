#!/usr/bin/env python3
"""Check that a prepared CIRCDIST frontier has never been solver-started."""
import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--frontier", type=Path, required=True)
ap.add_argument("--ledger", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()

root = a.frontier.resolve()
state_path = root / "state.json"
assert state_path.is_file()
state = json.loads(state_path.read_text())

false_fields = {
    "started": False,
}
null_fields = {
    "solver_status": None,
    "sat": None,
    "unsat": None,
}
for key, value in false_fields.items():
    assert state.get(key) is value, (key, state.get(key))
for key, value in null_fields.items():
    if key in state:
        assert state[key] is value, (key, state[key])

allowed_solver_word = {"base_encoding_check.json", "translation_registry_check.json"}
forbidden_suffixes = {".drat", ".lrat", ".proof", ".model", ".assignment"}
forbidden = []
files = []
for path in sorted(p for p in root.rglob("*") if p.is_file()):
    if path.resolve() == a.output.resolve():
        continue
    rel = path.relative_to(root).as_posix()
    lower = rel.lower()
    files.append({"path": rel, "bytes": path.stat().st_size, "sha256": sha256(path)})
    base = path.name.lower()
    if any(base.endswith(s) for s in forbidden_suffixes):
        forbidden.append(rel)
    if any(token in base for token in ("solver.log", "solver.stderr", "assignment.dimacs", "model.dimacs")):
        forbidden.append(rel)
    if "solver" in base and base not in allowed_solver_word:
        forbidden.append(rel)

ledger_rows = [json.loads(line) for line in a.ledger.read_text().splitlines() if line.strip()]
solver_names = {"cadical", "kissat", "minisat", "glucose", "cryptominisat5"}
solver_invocations = []
for row in ledger_rows:
    if row.get("state") != "STARTED" or not row.get("argv"):
        continue
    executable = Path(row["argv"][0]).name.lower()
    if executable in solver_names and any(str(root) in str(arg) for arg in row["argv"]):
        solver_invocations.append(row)

result = {
    "schema": "circdist-gross-round126-frontier-unstarted-audit-v1",
    "status": "PASS" if not forbidden and not solver_invocations else "FAIL",
    "frontier": str(root),
    "state_sha256": sha256(state_path),
    "state_started": state.get("started"),
    "state_solver_invocations_field": state.get("solver_invocations"),
    "state_solver_status": state.get("solver_status"),
    "ledger_solver_invocations": len(solver_invocations),
    "forbidden_solver_model_assignment_proof_artifacts": forbidden,
    "file_count_before_audit_output": len(files),
    "files_before_audit_output": files,
}
a.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
assert result["status"] == "PASS", {"forbidden": forbidden, "solver_invocations": solver_invocations}
print(json.dumps({k: result[k] for k in (
    "status", "state_started", "ledger_solver_invocations", "state_solver_status",
    "file_count_before_audit_output")}, sort_keys=True))
