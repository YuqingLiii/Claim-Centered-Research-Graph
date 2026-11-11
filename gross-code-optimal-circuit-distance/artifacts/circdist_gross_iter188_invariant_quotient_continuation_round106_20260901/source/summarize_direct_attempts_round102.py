#!/usr/bin/env python3
"""Summarize all corrected-candidate direct solver attempts without inference."""
from pathlib import Path
import argparse
import hashlib
import json
import re


CHUNK = 8 << 20


def scan(path):
    digest = hashlib.sha256()
    size = lf = empty = 0
    pending = b""
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(CHUNK), b""):
            digest.update(block)
            size += len(block)
            lf += block.count(b"\n")
            lines = (pending + block).split(b"\n")
            pending = lines.pop()
            empty += sum(line.strip() == b"0" for line in lines)
    if pending:
        empty += pending.strip() == b"0"
    return {"sha256": digest.hexdigest(), "bytes": size,
            "lf": lf, "empty_clause_lines": int(empty)}


def solver_status(log, returncode):
    text = log.read_text(errors="replace")
    explicit = re.findall(r"^s (SATISFIABLE|UNSATISFIABLE|UNKNOWN)\s*$", text,
                          flags=re.MULTILINE)
    expected = {10: "SATISFIABLE", 20: "UNSATISFIABLE", 0: "UNKNOWN"}[returncode]
    if explicit:
        assert explicit[-1] == expected, (log, explicit[-1], expected)
    return expected, text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    direct = root / "frontier/iter186_full_invariant_quotient/direct"
    build = json.loads((direct / "build_summary.json").read_text())
    attempts_by_sector = {"Xerr": [], "Zerr": []}
    records = sorted((root / "logs/process").glob(
        "iter186_full_invariant_quotient_direct_*cadical*.json"))
    for record_path in records:
        record = json.loads(record_path.read_text())
        sector = "Xerr" if "Xerr" in record["name"] else "Zerr"
        command = record["command"]
        cnf_arg = next(Path(value) for value in command if str(value).endswith(f"{sector}.cnf"))
        stream_arg = Path(command[-1])
        log = root.parent.parent.parent / record["stdout"] if not Path(record["stdout"]).is_absolute() else Path(record["stdout"])
        # Process paths are repository-relative; fall back to package-relative
        # for replayed records that use short paths.
        if not log.exists():
            log = root / record["stdout"]
        status, log_text = solver_status(log, record["returncode"])
        stream = root.parent.parent.parent / stream_arg
        if not stream.exists():
            stream = root / stream_arg
        descriptor_path = Path(str(stream) + ".stream.json")
        if stream.exists():
            stream_stats = scan(stream)
            stored = stream.relative_to(root).as_posix() if root in stream.parents else str(stream_arg)
        else:
            descriptor = json.loads(descriptor_path.read_text())
            stream_stats = {
                "sha256": descriptor["raw_sha256"],
                "bytes": descriptor["raw_bytes"],
                "lf": descriptor["raw_lf_count"],
                "empty_clause_lines": descriptor["raw_empty_clause_lines"],
            }
            stored = descriptor["gzip_path"]
        rss = re.findall(r"maximum resident set size of process:\s+([0-9.]+)\s+MB", log_text)
        attempts_by_sector[sector].append({
            "name": record["name"],
            "record": record_path.relative_to(root).as_posix(),
            "formula_sha256": build["sectors"][sector]["dimacs_sha256"],
            "variables": build["sectors"][sector]["variables"],
            "clauses": build["sectors"][sector]["clauses"],
            "complete_query": build["sectors"][sector]["complete_query"],
            "command": command,
            "pid": record["child_pid"],
            "started_utc": record["started_utc"],
            "ended_utc": record["ended_utc"],
            "wall_seconds": record["wall_seconds"],
            "returncode": record["returncode"],
            "solver_status": status,
            "stream": stored,
            "stream_stats": stream_stats,
            "proof_output_enabled_from_start": True,
            "certificate_disposition": (
                "candidate UNSAT proof; requires recorded DRAT and LRAT acceptance"
                if status == "UNSATISFIABLE" else
                "SAT-side output; not an absence certificate" if status == "SATISFIABLE" else
                "incomplete UNKNOWN prefix; not an absence certificate"
            ),
            "solver_reported_maximum_rss_value_and_label":
                None if not rss else {"value": float(rss[-1]), "label": "MB",
                                      "unit_warning": "CaDiCaL/macOS label appears to report KiB; retained verbatim"},
            "reaped": record["reaped"], "detached": record["detached"],
        })

    final = {}
    for sector, attempts in attempts_by_sector.items():
        assert attempts
        if any(item["solver_status"] == "SATISFIABLE" for item in attempts):
            disposition = "SATISFIABLE"
        elif any(item["solver_status"] == "UNSATISFIABLE" for item in attempts):
            disposition = "UNSATISFIABLE_PENDING_OR_CHECKED_CERTIFICATE"
        else:
            disposition = "UNKNOWN"
        final[sector] = {"disposition": disposition, "attempts": attempts}
    both_checked_unsat = all((direct / "certificate" / sector / "summary.json").exists()
                             and json.loads((direct / "certificate" / sector / "summary.json").read_text()).get("status") == "PASS"
                             for sector in ("Xerr", "Zerr"))
    result = {
        "schema": "circdist-gross-round102-corrected-candidate-direct-disposition-v1",
        "status": "PASS",
        "candidate_schedule_sha256": build["candidate_sha256"],
        "source_selector_count": build["source_selector_count"],
        "sectors": final,
        "both_direct_independently_proof_checked_unsat": both_checked_unsat,
        "repair_entered": False,
        "repair_gate": "forbidden unless both complete direct sectors have accepted DRAT and LRAT",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS",
                      "dispositions": {k: v["disposition"] for k, v in final.items()},
                      "both_checked_unsat": both_checked_unsat}, sort_keys=True))


if __name__ == "__main__":
    main()
