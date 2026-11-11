#!/usr/bin/env python3
"""Run a Python certificate from a prehashed, read-only local-source snapshot.

The wrapper is intentionally independent of the SU(3) mathematics.  Its job is to
make a long-running exact certificate auditable: discover the recursive
project-local Python import closure without importing it, freeze that closure,
write a prelaunch manifest, tee the complete merged stdout/stderr stream, and
fail closed if either the frozen snapshot or the corresponding working-tree
sources change.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import selectors
import shutil
import signal
import subprocess
import sys
from datetime import datetime, timezone
from typing import Iterable, Sequence


SOURCE_DRIFT_EXIT = 86
WRAPPER_FAILURE_EXIT = 87
MANIFEST_SCHEMA = "source-bound-python-certificate-v1"
PROGRESS_RE = re.compile(
    r"(?:^|:\s)processed=(?P<processed>\d+),\s*"
    r"certified=(?P<certified>\d+),\s*pending=(?P<pending>\d+)"
)
FINAL_LEAVES_RE = re.compile(r"adaptive compact boxes certified:\s*(?P<leaves>\d+)")
MARGIN_RE = re.compile(r"smallest certified natural-log margin\s*>\s*(?P<margin>[^\s]+)")


class WrapperError(RuntimeError):
    """Fail-closed wrapper error."""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_json(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    payload = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)


def relative_to(path: Path, root: Path, label: str) -> Path:
    try:
        return path.resolve(strict=True).relative_to(root.resolve(strict=True))
    except ValueError as exc:
        raise WrapperError(f"{label} is outside {root}: {path}") from exc


def module_candidates(module: str, roots: Sequence[Path]) -> Iterable[Path]:
    parts = module.split(".") if module else []
    for root in roots:
        if parts:
            yield root.joinpath(*parts).with_suffix(".py")
            yield root.joinpath(*parts, "__init__.py")


def package_parts(path: Path, project_root: Path) -> list[str]:
    parts: list[str] = []
    parent = path.parent
    while parent != project_root.parent and (parent / "__init__.py").is_file():
        parts.append(parent.name)
        if parent == project_root:
            break
        parent = parent.parent
    return list(reversed(parts))


def import_requests(path: Path, project_root: Path) -> tuple[set[str], list[str]]:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (OSError, SyntaxError, UnicodeError) as exc:
        raise WrapperError(f"cannot parse local source {path}: {exc}") from exc

    requests: set[str] = set()
    dynamic_notes: list[str] = []
    package = package_parts(path, project_root)
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            requests.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            base_parts: list[str]
            if node.level:
                if node.level > len(package):
                    dynamic_notes.append(
                        f"{path}: unresolved relative import at line {node.lineno}"
                    )
                    continue
                base_parts = package[: len(package) - node.level + 1]
            else:
                base_parts = []
            if node.module:
                base_parts.extend(node.module.split("."))
            base = ".".join(base_parts)
            if base:
                requests.add(base)
            for alias in node.names:
                if alias.name != "*":
                    candidate = ".".join([part for part in (base, alias.name) if part])
                    if candidate:
                        requests.add(candidate)
        elif isinstance(node, ast.Call):
            name = None
            if isinstance(node.func, ast.Name) and node.func.id == "__import__":
                name = "__import__"
            elif (
                isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "importlib"
                and node.func.attr == "import_module"
            ):
                name = "importlib.import_module"
            if name:
                if node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                    requests.add(node.args[0].value)
                else:
                    dynamic_notes.append(
                        f"{path}: nonliteral {name} at line {node.lineno}"
                    )
    return requests, dynamic_notes


def resolve_local_module(module: str, roots: Sequence[Path], project_root: Path) -> Path | None:
    for candidate in module_candidates(module, roots):
        if not candidate.is_file():
            continue
        try:
            candidate.resolve().relative_to(project_root.resolve())
        except ValueError:
            continue
        return candidate.resolve()
    return None


def discover_import_closure(entry: Path, project_root: Path, repo_root: Path) -> tuple[list[Path], list[str]]:
    """Return a conservative recursive project-local AST import closure.

    Search order models direct script execution: the entry directory first, then
    the project root and repository root.  Nonliteral dynamic imports fail closed.
    Imports that do not resolve inside the project are recorded only implicitly as
    Python/third-party dependencies and are identified by the recorded interpreter.
    """

    roots = tuple(dict.fromkeys((entry.parent.resolve(), project_root.resolve(), repo_root.resolve())))
    pending = [entry.resolve()]
    seen: set[Path] = set()
    dynamic_notes: list[str] = []
    while pending:
        current = pending.pop()
        if current in seen:
            continue
        relative_to(current, project_root, "imported source")
        seen.add(current)
        requests, notes = import_requests(current, project_root)
        dynamic_notes.extend(notes)
        for module in sorted(requests):
            local = resolve_local_module(module, roots, project_root)
            if local is not None and local not in seen:
                pending.append(local)
    if dynamic_notes:
        raise WrapperError(
            "nonliteral or unresolved relative imports prevent a complete static closure: "
            + "; ".join(dynamic_notes)
        )
    return sorted(seen), dynamic_notes


def source_record(path: Path, repo_root: Path) -> dict[str, object]:
    stat = path.stat()
    return {
        "path": path.relative_to(repo_root).as_posix(),
        "sha256": sha256_file(path),
        "size_bytes": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
        "mtime_utc": datetime.fromtimestamp(stat.st_mtime_ns / 1_000_000_000, timezone.utc)
        .isoformat(timespec="microseconds")
        .replace("+00:00", "Z"),
    }


def file_identity(path: Path, repo_root: Path) -> dict[str, object]:
    stat = path.stat()
    try:
        displayed_path = path.relative_to(repo_root).as_posix()
        path_kind = "repository-relative"
    except ValueError:
        displayed_path = str(path)
        path_kind = "absolute"
    return {
        "path": displayed_path,
        "path_kind": path_kind,
        "sha256": sha256_file(path),
        "size_bytes": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
    }


def current_source_records(paths: Sequence[Path], repo_root: Path) -> list[dict[str, object]]:
    records = []
    for path in paths:
        if not path.is_file():
            records.append({"path": path.relative_to(repo_root).as_posix(), "missing": True})
        else:
            records.append(source_record(path, repo_root))
    return records


def record_map(records: Sequence[dict[str, object]]) -> dict[str, tuple[object, object, object]]:
    return {
        str(row["path"]): (row.get("sha256"), row.get("size_bytes"), row.get("mtime_ns"))
        for row in records
    }


def changed_sources(
    frozen_records: Sequence[dict[str, object]], current_records: Sequence[dict[str, object]]
) -> list[str]:
    before = record_map(frozen_records)
    after = record_map(current_records)
    return sorted(path for path in set(before) | set(after) if before.get(path) != after.get(path))


def changed_source_contents(
    frozen_records: Sequence[dict[str, object]], current_records: Sequence[dict[str, object]]
) -> list[str]:
    before = {
        str(row["path"]): (row.get("sha256"), row.get("size_bytes")) for row in frozen_records
    }
    after = {
        str(row["path"]): (row.get("sha256"), row.get("size_bytes")) for row in current_records
    }
    return sorted(path for path in set(before) | set(after) if before.get(path) != after.get(path))


def freeze_sources(
    paths: Sequence[Path], records: Sequence[dict[str, object]], repo_root: Path, snapshot_root: Path
) -> None:
    expected = {str(row["path"]): str(row["sha256"]) for row in records}
    for source in paths:
        relative = source.relative_to(repo_root)
        destination = snapshot_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        if sha256_file(destination) != expected[relative.as_posix()]:
            raise WrapperError(f"snapshot copy hash mismatch: {relative}")
        destination.chmod(0o444)
    directories = sorted(
        {parent for path in snapshot_root.rglob("*") for parent in [path.parent]},
        key=lambda item: len(item.parts),
        reverse=True,
    )
    for directory in directories:
        directory.chmod(0o555)
    snapshot_root.chmod(0o555)


def interpreter_record(python: Path, env: dict[str, str], cwd: Path) -> dict[str, object]:
    probe = (
        "import json,platform,sys;"
        "print(json.dumps({'executable':sys.executable,'version':sys.version,"
        "'version_info':list(sys.version_info[:5]),'implementation':platform.python_implementation(),"
        "'sys_path':sys.path},sort_keys=True))"
    )
    completed = subprocess.run(
        [str(python), "-c", probe], cwd=cwd, env=env, check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
    )
    return json.loads(completed.stdout)


def parse_terminal_fields(text: str, required_regexes: Sequence[str]) -> dict[str, object]:
    progress = list(PROGRESS_RE.finditer(text))
    leaves = list(FINAL_LEAVES_RE.finditer(text))
    margins = list(MARGIN_RE.finditer(text))
    required = []
    for pattern in required_regexes:
        match = re.search(pattern, text, flags=re.MULTILINE)
        required.append({"regex": pattern, "matched": bool(match), "match": match.group(0) if match else None})
    value: dict[str, object] = {
        "last_progress": None,
        "adaptive_compact_boxes_certified": None,
        "smallest_certified_natural_log_margin_text": None,
        "required_terminal_patterns": required,
        "all_required_terminal_patterns_matched": all(row["matched"] for row in required),
        "full_binary_tree_counts": None,
    }
    if progress:
        match = progress[-1]
        value["last_progress"] = {key: int(match.group(key)) for key in ("processed", "certified", "pending")}
    if leaves:
        leaf_count = int(leaves[-1].group("leaves"))
        value["adaptive_compact_boxes_certified"] = leaf_count
        value["full_binary_tree_counts"] = {
            "certified_leaf_boxes": leaf_count,
            "internal_split_boxes": leaf_count - 1,
            "processed_boxes": 2 * leaf_count - 1,
            "pending_boxes": 0,
            "derivation": (
                "The terminal leaf line is emitted only after stack exhaustion; each rejected box "
                "creates exactly two children, so the explored tree is full binary."
            ),
        }
    if margins:
        value["smallest_certified_natural_log_margin_text"] = margins[-1].group("margin")
    return value


def terminate_child(child: subprocess.Popen[bytes]) -> None:
    if child.poll() is not None:
        return
    child.terminate()
    try:
        child.wait(timeout=5)
    except subprocess.TimeoutExpired:
        child.kill()
        child.wait(timeout=5)


def tee_child(
    command: Sequence[str], cwd: Path, env: dict[str, str], log_path: Path,
    sources: Sequence[Path], initial_records: Sequence[dict[str, object]], repo_root: Path,
    drift_interval: float,
) -> tuple[int, list[str], str | None]:
    child = subprocess.Popen(
        list(command), cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        stdin=subprocess.DEVNULL, bufsize=0,
    )
    assert child.stdout is not None
    selector = selectors.DefaultSelector()
    selector.register(child.stdout, selectors.EVENT_READ)
    drift: list[str] = []
    interrupted: str | None = None
    previous_handlers: dict[int, object] = {}

    def forward_signal(signum: int, _frame: object) -> None:
        nonlocal interrupted
        interrupted = signal.Signals(signum).name
        terminate_child(child)

    for signum in (signal.SIGINT, signal.SIGTERM):
        previous_handlers[signum] = signal.signal(signum, forward_signal)
    try:
        with log_path.open("wb") as log:
            while True:
                events = selector.select(timeout=drift_interval)
                for key, _ in events:
                    block = os.read(key.fileobj.fileno(), 64 * 1024)
                    if block:
                        log.write(block)
                        log.flush()
                        sys.stdout.buffer.write(block)
                        sys.stdout.buffer.flush()
                    else:
                        selector.unregister(key.fileobj)
                current = current_source_records(sources, repo_root)
                drift = changed_sources(initial_records, current)
                if drift:
                    marker = (
                        "\nSOURCE-BOUND WRAPPER: source drift detected; terminating child: "
                        + ", ".join(drift) + "\n"
                    ).encode("utf-8")
                    log.write(marker)
                    log.flush()
                    sys.stdout.buffer.write(marker)
                    sys.stdout.buffer.flush()
                    terminate_child(child)
                if child.poll() is not None and not selector.get_map():
                    break
            log.flush()
            os.fsync(log.fileno())
    finally:
        selector.close()
        for signum, handler in previous_handlers.items():
            signal.signal(signum, handler)
    return child.returncode if child.returncode is not None else WRAPPER_FAILURE_EXIT, drift, interrupted


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--project-root", type=Path)
    parser.add_argument("--entry", type=Path, required=True, help="Repository-relative Python entry script")
    parser.add_argument("--config-name", required=True)
    parser.add_argument("--run-dir", type=Path, required=True, help="New repository-relative evidence directory")
    parser.add_argument("--python", type=Path, default=Path(sys.executable))
    parser.add_argument("--required-terminal-regex", action="append", default=[])
    parser.add_argument("--drift-check-seconds", type=float, default=5.0)
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("child_args", nargs=argparse.REMAINDER)
    return parser


def run(args: argparse.Namespace) -> int:
    repo_root = args.repo_root.resolve(strict=True)
    entry = (repo_root / args.entry).resolve(strict=True)
    if args.project_root:
        project_root = (repo_root / args.project_root).resolve(strict=True)
    else:
        project_root = entry.parent.parent
    relative_to(project_root, repo_root, "project root")
    relative_entry = relative_to(entry, project_root, "entry")
    if entry.suffix != ".py":
        raise WrapperError("entry must be a Python source file")
    run_dir = (repo_root / args.run_dir).resolve()
    try:
        run_dir.relative_to(repo_root)
    except ValueError as exc:
        raise WrapperError(f"run directory is outside {repo_root}: {run_dir}") from exc
    if run_dir.exists():
        raise WrapperError(f"run directory already exists (refusing overwrite): {run_dir}")
    run_dir.mkdir(parents=True)
    snapshot_root = run_dir / "source"
    snapshot_root.mkdir()

    sources, _ = discover_import_closure(entry, project_root, repo_root)
    initial_records = current_source_records(sources, repo_root)
    freeze_sources(sources, initial_records, repo_root, snapshot_root)
    after_freeze = current_source_records(sources, repo_root)
    drift_before_launch = changed_sources(initial_records, after_freeze)
    if drift_before_launch:
        raise WrapperError("source changed while snapshot was being created: " + ", ".join(drift_before_launch))

    frozen_entry = snapshot_root / entry.relative_to(repo_root)
    python = args.python.resolve(strict=True)
    child_args = list(args.child_args)
    if child_args and child_args[0] == "--":
        child_args = child_args[1:]
    command = [str(python), str(frozen_entry), *child_args]
    env = dict(os.environ)
    env.pop("PYTHONHOME", None)
    env["PYTHONPATH"] = os.pathsep.join((str(frozen_entry.parent), str(snapshot_root)))
    interpreter = interpreter_record(python, env, repo_root)
    required = args.required_terminal_regex or [
        r"adaptive compact boxes certified:\s*\d+",
        r"Bell-no-go",
    ]
    prelaunch = {
        "schema": MANIFEST_SCHEMA,
        "phase": "prelaunch",
        "config_name": args.config_name,
        "prepared_at_utc": utc_now(),
        "repo_root": str(repo_root),
        "project_root": project_root.relative_to(repo_root).as_posix(),
        "entry": entry.relative_to(repo_root).as_posix(),
        "entry_relative_to_project": relative_entry.as_posix(),
        "cwd": str(repo_root),
        "command": command,
        "command_shell_escaped": " ".join(__import__("shlex").quote(part) for part in command),
        "wrapper": file_identity(Path(__file__).resolve(strict=True), repo_root),
        "wrapper_argv": list(sys.argv),
        "wrapper_invocation_shell_escaped": " ".join(
            __import__("shlex").quote(part) for part in sys.argv
        ),
        "python": interpreter,
        "environment": {"PYTHONPATH": env["PYTHONPATH"], "PYTHONHOME_removed": True},
        "source_closure_method": "recursive AST imports; nonliteral dynamic imports fail closed",
        "source_closure": initial_records,
        "source_count": len(initial_records),
        "snapshot_root": snapshot_root.relative_to(repo_root).as_posix(),
        "required_terminal_regexes": required,
        "prepare_only": bool(args.prepare_only),
    }
    prelaunch_path = run_dir / "manifest.prelaunch.json"
    atomic_json(prelaunch_path, prelaunch)

    if args.prepare_only:
        final = {
            **prelaunch,
            "phase": "prepared-only",
            "ended_at_utc": utc_now(),
            "wrapper_status": "PREPARED_ONLY_NOT_EXECUTED",
            "prelaunch_manifest_sha256": sha256_file(prelaunch_path),
        }
        atomic_json(run_dir / "manifest.final.json", final)
        return 0

    started_at = utc_now()
    output_path = run_dir / "stdout-stderr.log"
    child_exit, observed_drift, interrupted = tee_child(
        command, repo_root, env, output_path, sources, initial_records, repo_root,
        max(0.05, args.drift_check_seconds),
    )
    final_sources = current_source_records(sources, repo_root)
    drift = sorted(set(observed_drift) | set(changed_sources(initial_records, final_sources)))
    snapshot_records = current_source_records(
        [snapshot_root / path.relative_to(repo_root) for path in sources], snapshot_root
    )
    snapshot_expected = [
        {**row, "path": (snapshot_root / str(row["path"])).relative_to(snapshot_root).as_posix()}
        for row in initial_records
    ]
    snapshot_drift = changed_source_contents(snapshot_expected, snapshot_records)
    output_text = output_path.read_text(encoding="utf-8", errors="replace")
    terminal = parse_terminal_fields(output_text, required)
    all_terminal = bool(terminal["all_required_terminal_patterns_matched"])
    if drift or snapshot_drift:
        status = "FAIL_SOURCE_DRIFT"
        wrapper_exit = SOURCE_DRIFT_EXIT
    elif interrupted:
        status = "FAIL_INTERRUPTED"
        wrapper_exit = WRAPPER_FAILURE_EXIT
    elif child_exit != 0:
        status = "FAIL_CHILD_EXIT"
        wrapper_exit = child_exit
    elif not all_terminal:
        status = "FAIL_TERMINAL_FIELDS"
        wrapper_exit = WRAPPER_FAILURE_EXIT
    else:
        status = "PASS"
        wrapper_exit = 0
    final = {
        **prelaunch,
        "phase": "final",
        "started_at_utc": started_at,
        "ended_at_utc": utc_now(),
        "child_exit_code": child_exit,
        "wrapper_exit_code": wrapper_exit,
        "wrapper_status": status,
        "interrupted_by_signal": interrupted,
        "workspace_source_drift": drift,
        "snapshot_source_drift": snapshot_drift,
        "final_workspace_source_closure": final_sources,
        "stdout_stderr_log": output_path.relative_to(repo_root).as_posix(),
        "stdout_stderr_sha256": sha256_file(output_path),
        "stdout_stderr_size_bytes": output_path.stat().st_size,
        "terminal_fields": terminal,
        "prelaunch_manifest_sha256": sha256_file(prelaunch_path),
    }
    atomic_json(run_dir / "manifest.final.json", final)
    return wrapper_exit


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return run(args)
    except (OSError, subprocess.SubprocessError, WrapperError) as exc:
        print(f"source-bound certificate wrapper failed closed: {exc}", file=sys.stderr)
        return WRAPPER_FAILURE_EXIT


if __name__ == "__main__":
    raise SystemExit(main())
