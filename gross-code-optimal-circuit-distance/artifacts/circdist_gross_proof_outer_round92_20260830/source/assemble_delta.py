#!/usr/bin/env python3
"""Assemble the Round92 Gross delta package in scratch.

The package content-addresses the reviewed Round90 package instead of copying its
toolchain and semantic vendor tree.  Replay verifies Round90's two seals before
using any dependency bytes.
"""
from pathlib import Path
import argparse
import gzip
import shutil


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def gzip_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(gzip.compress(source.read_bytes(), compresslevel=9, mtime=0))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--science", type=Path, required=True)
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    science = args.science.resolve()
    work = args.work.resolve()
    output = args.output.resolve()
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    round90 = repo / "circdist/artifacts/circdist_gross_proof_outer_round90_20260830"

    # Protected inputs and exact reviewed dependency bindings.
    bindings = output / "bindings"
    copy_file(repo / "operations/circdist/SCHEDULER.yaml", bindings / "canonical/SCHEDULER.yaml")
    copy_file(repo / "circdist/proof-dag/nodes/CIRCDIST.gross.yaml", bindings / "canonical/CIRCDIST.gross.yaml")
    copy_file(repo / "circdist/reviews/circdist_gross_proof_outer_exact_review_round91_20260830.md", bindings / "canonical/round91_review.md")
    for name in ("DAG_PROTOCOL.md", "FILE_PROTOCOL.md"):
        copy_file(repo / name, bindings / "protocols" / name)
    copy_file(repo / "circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md", bindings / "protocols/CIRCDIST_PROBLEMS.md")
    for name in ("SHA256SUMS.txt", "PAYLOAD_SHA256SUMS.txt", "REPORT.md", "RESULT.json"):
        copy_file(round90 / name, bindings / "round90" / name)
    copy_file(round90 / "continuation/final_state.json", bindings / "round90/final_state.json")
    copy_file(round90 / "formulas/iter124/source.json.gz", bindings / "round90/iter124_source.json.gz")
    copy_file(round90 / "formulas/iter124/metadata.json", bindings / "round90/iter124_metadata.json")
    shutil.copytree(repo / "circdist/proof-dag", bindings / "initial_proof_dag/circdist/proof-dag")

    # Phase A: complete synthesis proof object and exact strict-expansion witness.
    copy_file(work / "weight9_synthesis.json", output / "synthesis/weight9_synthesis.json")
    copy_file(science / "preouter/atomic_install.json", output / "preouter/atomic_install.json")
    for name in (
        "strict_expansion_query.json", "strict_expansion.solver.log",
        "strict_expansion.stderr.log", "strict_expansion.candidate.json",
        "strict_expansion.verification.json",
    ):
        copy_file(science / "preouter" / name, output / "preouter" / name)
    gzip_file(science / "preouter/strict_expansion.cnf", output / "preouter/strict_expansion.cnf.gz")
    gzip_file(science / "preouter/strict_expansion.assignment.dimacs", output / "preouter/strict_expansion.assignment.dimacs.gz")
    copy_file(science / "logs/preouter_strict_expansion.process.json", output / "logs/preouter_strict_expansion.process.json")

    # Reviewed starting state, post-synthesis atomic state, and fresh continuation.
    copy_file(science / "state/iter124_inherited_state.json", output / "continuation/inherited_iter124_state.json")
    copy_file(science / "state/iter124_state.json", output / "continuation/preouter_iter124_state.json")
    copy_file(science / "state/iter136_state.json", output / "continuation/final_state.json")

    # Exact augmented formulas 124--136.
    for iteration in range(124, 137):
        source = science / f"formulas/iter{iteration}"
        destination = output / f"formulas/iter{iteration}"
        copy_file(source / "source.json.gz", destination / "source.json.gz")
        gzip_file(source / "outer.cnf", destination / "outer.cnf.gz")
        gzip_file(source / "assertion_map.jsonl", destination / "assertion_map.jsonl.gz")
        copy_file(source / "circuit_trace.json.gz", destination / "circuit_trace.json.gz")
        copy_file(source / "metadata.json", destination / "metadata.json")
        copy_file(source / "encoding_check.json", destination / "encoding_check.json")

    # Twelve complete candidate closures. SAT-side .drat streams are non-certificates;
    # their full disposition is retained separately and the actual small control stream
    # is retained below.
    for iteration in range(124, 136):
        source = science / f"iter{iteration}"
        destination = output / f"iterations/iter{iteration}"
        copy_file(source / "record.json", destination / "record.json")
        for name in ("solver.log", "solver.stderr.log", "candidate.json", "replay.json"):
            copy_file(source / "outer" / name, destination / "outer" / name)
        gzip_file(source / "outer/assignment.dimacs", destination / "outer/assignment.dimacs.gz")
        for path in sorted((source / "direct").rglob("*")):
            if not path.is_file() or path.suffix == ".drat":
                continue
            copy_file(path, destination / "direct" / path.relative_to(source / "direct"))

    for path in sorted((science / "logs").glob("*.json")):
        copy_file(path, output / "logs" / path.name)
    copy_file(science / "campaign.log", output / "logs/campaign.log")
    copy_file(science / "data/campaign_summary.json", output / "data/campaign_summary.json")
    copy_file(science / "data/sat_drat_trace_disposition.json", output / "data/sat_drat_trace_disposition.json")
    copy_file(science / "data/sat_drat_trace_scan.log", output / "data/sat_drat_trace_scan.log")
    copy_file(science / "PROCESS_LEDGER.json", output / "data/original_process_ledger.json")

    # Actual-formula negative proof controls, including the exact retained streams.
    actual = science / "controls/actual_sat_trace"
    for path in sorted(actual.glob("*")):
        if path.is_file():
            copy_file(path, output / "controls/actual_sat_trace" / path.name)
    copy_file(science / "verification/proof_fixture_controls.json", output / "controls/proof_fixture_controls.json")

    # Exact science and replay sources. Intentionally exclude the canceled online
    # synthesis script, which produced no result or state mutation.
    inherited = [
        "check_manifests.py", "check_outer_encoding.py", "check_proof_controls.py",
        "compare_json.py", "compile_outer_cnf.py", "duplicate_yaml_scan.py",
        "run_bounded.py", "verify_outer_sat_model.py", "seal_package.py",
    ]
    for name in inherited:
        copy_file(round90 / "source" / name, output / "source" / name)
    for name in (
        "weight9_synthesis.py", "install_preouter.py", "build_strict_expansion_query.py",
        "verify_strict_expansion_sat.py", "record_sat_traces.py",
        "summarize_campaign.py", "make_actual_trace_summary.py", "assemble_delta.py",
    ):
        copy_file(work / name, output / "source" / name)
    for name in ("run_serial_campaign.py", "advance_round92.py", "build_direct_from_candidate.py"):
        copy_file(science / name, output / "source" / name)
    print(output)


if __name__ == "__main__":
    main()
