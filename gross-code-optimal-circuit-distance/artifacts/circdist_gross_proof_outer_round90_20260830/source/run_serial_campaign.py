#!/usr/bin/env python3
"""Run the Round90 continuation strictly serially; stop on any non-SAT branch."""
from pathlib import Path
import argparse
import json
import subprocess
import sys


def run(command):
    print(json.dumps({"campaign_event": "COMMAND", "command": [str(x) for x in command]}), flush=True)
    subprocess.run([str(x) for x in command], check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--scratch", type=Path, required=True)
    parser.add_argument("--first", type=int, required=True)
    parser.add_argument("--last", type=int, required=True)
    args = parser.parse_args()

    repo = args.repo.resolve()
    root = args.scratch.resolve()
    package = repo / "circdist/artifacts/circdist_gross_proof_outer_round88_20260830"
    python = Path(sys.executable)
    runner = package / "source/run_bounded.py"
    solver = package / "tooling/cadical-1.9.5-arm64-macos"
    verifier = package / "source/verify_outer_sat_model.py"
    compiler = package / "source/compile_outer_cnf.py"
    encoding_checker = package / "source/check_outer_encoding.py"
    vendor = package / "vendor/round80"
    direct_replay = vendor / "src/replay_direct_candidate.py"
    direct_builder = root / "build_direct_from_candidate.py"
    advance = root / "advance_round90.py"

    for iteration in range(args.first, args.last + 1):
        formula = root / f"formulas/iter{iteration}"
        iteration_root = root / f"iter{iteration}"
        outer = iteration_root / "outer"
        outer.mkdir(parents=True, exist_ok=True)
        process_record = root / f"logs/outer_iter{iteration}.process.json"
        run(
            [
                python,
                runner,
                "--name",
                f"outer_iter{iteration}_cadical",
                "--timeout",
                "900",
                "--stdout",
                outer / "solver.log",
                "--stderr",
                outer / "solver.stderr.log",
                "--record",
                process_record,
                "--",
                solver,
                "-t",
                "890",
                "--no-binary",
                formula / "outer.cnf",
                outer / "outer.drat",
            ]
        )
        outer_code = json.loads(process_record.read_text())["returncode"]
        print(json.dumps({"campaign_event": "OUTER_DISPOSITION", "iteration": iteration, "returncode": outer_code}), flush=True)
        if outer_code != 10:
            print(json.dumps({"campaign_event": "STOP_NON_SAT_OUTER", "iteration": iteration, "returncode": outer_code}), flush=True)
            return

        run(
            [
                python,
                verifier,
                "--solver-log",
                outer / "solver.log",
                "--cnf",
                formula / "outer.cnf",
                "--source",
                formula / "source.json.gz",
                "--metadata",
                formula / "metadata.json",
                "--frozen",
                vendor,
                "--assignment",
                outer / "assignment.dimacs",
                "--candidate",
                outer / "candidate.json",
                "--output",
                outer / "replay.json",
            ]
        )
        state_in = root / f"state/iter{iteration}_state.json"
        selector_count = json.loads(state_in.read_text())["selector_count"]
        direct = iteration_root / "direct"
        run(
            [
                python,
                direct_builder,
                "--candidate",
                outer / "candidate.json",
                "--output",
                direct,
                "--vendor",
                vendor,
                "--source-selector-count",
                str(selector_count),
            ]
        )
        direct_codes = {}
        for label in ("Xerr", "Zerr"):
            record = root / f"logs/direct_iter{iteration}_{label}.process.json"
            run(
                [
                    python,
                    runner,
                    "--name",
                    f"direct_iter{iteration}_{label}_cadical",
                    "--timeout",
                    "900",
                    "--stdout",
                    direct / f"solver/{label}.solver.log",
                    "--stderr",
                    direct / f"solver/{label}.stderr.log",
                    "--record",
                    record,
                    "--",
                    solver,
                    "-t",
                    "890",
                    "--no-binary",
                    direct / f"direct360/{label}.cnf",
                    direct / f"solver/{label}.drat",
                ]
            )
            direct_codes[label] = json.loads(record.read_text())["returncode"]
            print(json.dumps({"campaign_event": "DIRECT_DISPOSITION", "iteration": iteration, "sector": label, "returncode": direct_codes[label]}), flush=True)
        if set(direct_codes.values()) != {10}:
            print(json.dumps({"campaign_event": "STOP_NON_SAT_DIRECT", "iteration": iteration, "returncodes": direct_codes}), flush=True)
            return

        run(
            [
                python,
                direct_replay,
                "--root",
                direct,
                "--output",
                direct / "direct_verification.json",
            ]
        )
        next_state = root / f"state/iter{iteration + 1}_state.json"
        next_formula = root / f"formulas/iter{iteration + 1}"
        run(
            [
                python,
                advance,
                "--vendor",
                vendor,
                "--state-in",
                state_in,
                "--source-in",
                formula / "source.json.gz",
                "--iteration",
                str(iteration),
                "--candidate",
                outer / "candidate.json",
                "--direct",
                direct / "direct_verification.json",
                "--state-out",
                next_state,
                "--record-out",
                iteration_root / "record.json",
                "--source-out",
                next_formula / "source.json.gz",
            ]
        )
        run(
            [
                python,
                compiler,
                "--source",
                next_formula / "source.json.gz",
                "--cnf",
                next_formula / "outer.cnf",
                "--metadata",
                next_formula / "metadata.json",
                "--assertion-map",
                next_formula / "assertion_map.jsonl",
                "--definitions",
                next_formula / "circuit_trace.json.gz",
            ]
        )
        run(
            [
                python,
                encoding_checker,
                "--source",
                next_formula / "source.json.gz",
                "--cnf",
                next_formula / "outer.cnf",
                "--metadata",
                next_formula / "metadata.json",
                "--assertion-map",
                next_formula / "assertion_map.jsonl",
                "--definitions",
                next_formula / "circuit_trace.json.gz",
                "--output",
                next_formula / "encoding_check.json",
            ]
        )
        print(json.dumps({"campaign_event": "ITERATION_CLOSED", "iteration": iteration, "next_iteration": iteration + 1}), flush=True)

    print(json.dumps({"campaign_event": "CAMPAIGN_SAT_PREFIX_COMPLETE", "first": args.first, "last": args.last, "fresh_next": args.last + 1}), flush=True)


if __name__ == "__main__":
    main()
