#!/usr/bin/env python3
"""Lightweight fixtures for run_source_bound_certificate.py."""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time


WRAPPER = Path(__file__).with_name("run_source_bound_certificate.py")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def command(root: Path, run_name: str, entry: str = "fixture_certificate.py") -> list[str]:
    return [
        sys.executable,
        str(WRAPPER),
        "--repo-root", str(root),
        "--project-root", "project",
        "--entry", f"project/tools/{entry}",
        "--config-name", "fixture-two-leaf-tree",
        "--run-dir", f"project/artifacts/{run_name}",
        "--drift-check-seconds", "0.05",
    ]


def unlock_tree(root: Path) -> None:
    for path in sorted(root.rglob("*"), key=lambda item: len(item.parts)):
        if path.is_dir():
            path.chmod(0o755)
        else:
            path.chmod(0o644)


def main() -> None:
    temporary = Path(tempfile.mkdtemp(prefix="source-bound-certificate-fixture-"))
    try:
        tools = temporary / "project" / "tools"
        write(tools / "fixture_helper.py", "VALUE = 2\n")
        write(
            tools / "fixture_certificate.py",
            "import time\n"
            "from fixture_helper import VALUE\n"
            "print(f'fixture: processed=1, certified=0, pending=2', flush=True)\n"
            "time.sleep(0.25)\n"
            "print(f'fixture: adaptive compact boxes certified: {VALUE}', flush=True)\n"
            "print('fixture: smallest certified natural-log margin > 1.25e-03 at box', flush=True)\n"
            "print('fixture: Bell-no-go', flush=True)\n",
        )

        passed = subprocess.run(command(temporary, "pass"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pass_dir = temporary / "project" / "artifacts" / "pass"
        if passed.returncode != 0:
            diagnostic = (pass_dir / "manifest.final.json").read_text(encoding="utf-8")
            raise AssertionError((passed.stdout.decode(), passed.stderr.decode(), diagnostic))
        prelaunch = json.loads((pass_dir / "manifest.prelaunch.json").read_text(encoding="utf-8"))
        final = json.loads((pass_dir / "manifest.final.json").read_text(encoding="utf-8"))
        assert prelaunch["source_count"] == 2
        assert final["wrapper_status"] == "PASS"
        assert final["stdout_stderr_sha256"]
        assert final["terminal_fields"]["full_binary_tree_counts"] == {
            "certified_leaf_boxes": 2,
            "internal_split_boxes": 1,
            "processed_boxes": 3,
            "pending_boxes": 0,
            "derivation": (
                "The terminal leaf line is emitted only after stack exhaustion; each rejected box "
                "creates exactly two children, so the explored tree is full binary."
            ),
        }

        overwrite = subprocess.run(
            command(temporary, "pass"), stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        assert overwrite.returncode == 87
        assert b"refusing overwrite" in overwrite.stderr

        write(
            tools / "missing_terminal_certificate.py",
            "print('clean child exit without certificate terminus', flush=True)\n",
        )
        missing = subprocess.run(
            command(temporary, "missing-terminal", "missing_terminal_certificate.py"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        missing_final = json.loads(
            (temporary / "project" / "artifacts" / "missing-terminal" / "manifest.final.json")
            .read_text(encoding="utf-8")
        )
        assert missing.returncode == 87
        assert missing_final["wrapper_status"] == "FAIL_TERMINAL_FIELDS"

        write(
            tools / "nonzero_certificate.py",
            "print('adaptive compact boxes certified: 1', flush=True)\n"
            "print('Bell-no-go', flush=True)\n"
            "raise SystemExit(3)\n",
        )
        nonzero = subprocess.run(
            command(temporary, "nonzero", "nonzero_certificate.py"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        nonzero_final = json.loads(
            (temporary / "project" / "artifacts" / "nonzero" / "manifest.final.json")
            .read_text(encoding="utf-8")
        )
        assert nonzero.returncode == 3
        assert nonzero_final["wrapper_status"] == "FAIL_CHILD_EXIT"

        write(
            tools / "dynamic_certificate.py",
            "MODULE = 'fixture_helper'\n"
            "__import__(MODULE)\n",
        )
        dynamic = subprocess.run(
            command(temporary, "dynamic", "dynamic_certificate.py"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        assert dynamic.returncode == 87
        assert b"nonliteral __import__" in dynamic.stderr

        drift_process = subprocess.Popen(
            command(temporary, "drift"), stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        drift_prelaunch = temporary / "project" / "artifacts" / "drift" / "manifest.prelaunch.json"
        deadline = time.monotonic() + 5
        while not drift_prelaunch.exists() and time.monotonic() < deadline:
            time.sleep(0.01)
        assert drift_prelaunch.exists(), "prelaunch manifest was not written"
        write(tools / "fixture_helper.py", "VALUE = 3\n")
        stdout, stderr = drift_process.communicate(timeout=5)
        assert drift_process.returncode == 86, (stdout.decode(), stderr.decode())
        drift_final = json.loads(
            (temporary / "project" / "artifacts" / "drift" / "manifest.final.json").read_text(
                encoding="utf-8"
            )
        )
        assert drift_final["wrapper_status"] == "FAIL_SOURCE_DRIFT"
        assert drift_final["workspace_source_drift"] == ["project/tools/fixture_helper.py"]
        assert drift_final["child_exit_code"] != 0
        print("source-bound certificate wrapper success and fail-closed fixtures PASS")
    finally:
        if temporary.exists():
            unlock_tree(temporary)
            shutil.rmtree(temporary)


if __name__ == "__main__":
    main()
