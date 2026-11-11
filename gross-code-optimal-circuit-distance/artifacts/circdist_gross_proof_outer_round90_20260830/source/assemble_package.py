#!/usr/bin/env python3
"""Assemble the single Round90 durable package in scratch before its atomic install."""
from pathlib import Path
import argparse
import gzip
import shutil


def copy_file(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def gzip_file(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(gzip.compress(source.read_bytes(), compresslevel=9, mtime=0))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--science", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    science = args.science.resolve()
    output = args.output.resolve()
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    round88 = repo / "circdist/artifacts/circdist_gross_proof_outer_round88_20260830"

    # Exact tooling and frozen semantic implementation.
    shutil.copytree(round88 / "tooling", output / "tooling")
    shutil.copytree(round88 / "vendor", output / "vendor")
    shutil.copytree(round88 / "controls/proof_checker", output / "controls/proof_checker")

    # Protected/canonical bindings and the reviewed starting frontier.
    bindings = output / "bindings"
    copy_file(repo / "operations/circdist/SCHEDULER.yaml", bindings / "canonical/SCHEDULER.yaml")
    copy_file(repo / "circdist/proof-dag/nodes/CIRCDIST.gross.yaml", bindings / "canonical/CIRCDIST.gross.yaml")
    copy_file(repo / "circdist/reviews/circdist_gross_proof_outer_exact_review_round89_20260830.md", bindings / "canonical/round89_review.md")
    copy_file(repo / "DAG_PROTOCOL.md", bindings / "protocols/DAG_PROTOCOL.md")
    copy_file(repo / "FILE_PROTOCOL.md", bindings / "protocols/FILE_PROTOCOL.md")
    copy_file(repo / "circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md", bindings / "protocols/CIRCDIST_PROBLEMS.md")
    copy_file(round88 / "SHA256SUMS.txt", bindings / "round88/SHA256SUMS.txt")
    copy_file(round88 / "PAYLOAD_SHA256SUMS.txt", bindings / "round88/PAYLOAD_SHA256SUMS.txt")
    copy_file(round88 / "REPORT.md", bindings / "round88/REPORT.md")
    copy_file(round88 / "continuation/final_state.json", bindings / "round88/final_state.json")
    shutil.copytree(repo / "circdist/proof-dag", bindings / "initial_proof_dag/circdist/proof-dag")

    # Complete exact formulas: reviewed iteration 112 plus new iterations 113--124.
    shutil.copytree(round88 / "formulas/iter112", output / "formulas/iter112")
    for iteration in range(113, 125):
        source = science / f"formulas/iter{iteration}"
        destination = output / f"formulas/iter{iteration}"
        copy_file(source / "source.json.gz", destination / "source.json.gz")
        gzip_file(source / "outer.cnf", destination / "outer.cnf.gz")
        copy_file(source / "metadata.json", destination / "metadata.json")
        gzip_file(source / "assertion_map.jsonl", destination / "assertion_map.jsonl.gz")
        copy_file(source / "circuit_trace.json.gz", destination / "circuit_trace.json.gz")
        copy_file(source / "encoding_check.json", destination / "encoding_check.json")

    # Complete assignments, direct formulas/dictionaries, solver logs, and replays.
    for iteration in range(112, 124):
        source = science / f"iter{iteration}"
        destination = output / f"iterations/iter{iteration}"
        copy_file(source / "record.json", destination / "record.json")
        for name in ("solver.log", "solver.stderr.log", "candidate.json", "replay.json"):
            copy_file(source / f"outer/{name}", destination / f"outer/{name}")
        gzip_file(source / "outer/assignment.dimacs", destination / "outer/assignment.dimacs.gz")
        for path in sorted((source / "direct").rglob("*")):
            if not path.is_file() or path.suffix == ".drat":
                continue
            relative = path.relative_to(source / "direct")
            copy_file(path, destination / "direct" / relative)

    # State, process records, proof-output disposition, and actual-formula controls.
    copy_file(science / "state/iter124_state.json", output / "continuation/final_state.json")
    for path in sorted((science / "logs").glob("*.json")):
        copy_file(path, output / "logs" / path.name)
    copy_file(science / "data/sat_drat_trace_disposition.json", output / "data/sat_drat_trace_disposition.json")
    actual = science / "controls/actual_gross_sat_trace"
    for path in sorted(actual.glob("*")):
        if path.is_file() and path.suffix != ".drat":
            copy_file(path, output / "controls/actual_gross_sat_trace" / path.name)

    # Proposer and replay sources.  The inherited compilers/checkers are copied,
    # while campaign-specific scripts are the exact corrected versions used here.
    inherited_sources = [
        "check_manifests.py",
        "check_outer_encoding.py",
        "check_proof_controls.py",
        "compare_json.py",
        "compile_outer_cnf.py",
        "duplicate_yaml_scan.py",
        "run_bounded.py",
        "verify_outer_sat_model.py",
    ]
    for name in inherited_sources:
        copy_file(round88 / "source" / name, output / "source" / name)
    for name in (
        "advance_round90.py",
        "assemble_package.py",
        "build_direct_from_candidate.py",
        "record_sat_traces.py",
        "run_serial_campaign.py",
    ):
        copy_file(science / name, output / "source" / name)

    print(output)


if __name__ == "__main__":
    main()
