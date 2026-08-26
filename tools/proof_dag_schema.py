#!/usr/bin/env python3
"""Loader, validator, and generated views for the current KSUM and SE schema.

The schema treats a route as a directed hyperedge: a nonempty set of
premises together supports one parent claim.  Node and route assessments are
epistemic; the optional disposition block is scheduling metadata.  Reverse
dependencies, AND/OR labels, indexes, and diagrams are derived rather than
stored in node files.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
import re
from typing import Any

import yaml


LEVELS = {"OPEN", "CONJECTURED", "NUMERICAL", "CERTIFIED*", "PROVED", "REFUTED"}
LEVEL_RANK = {"REFUTED": -1, "OPEN": 0, "CONJECTURED": 1, "NUMERICAL": 2,
              "CERTIFIED*": 3, "PROVED": 4}
COMPLETION_LEVELS = {"CERTIFIED*", "PROVED"}
ROLES = {"proof", "obstruction", "tool", "outcome", "constraint"}
TOP_KEYS = {"id", "role", "aliases", "claim", "assumptions", "routes", "assessment",
            "disposition", "formalization", "frontier", "events"}
ROUTE_KEYS = {"premises", "assumptions", "implication", "proof", "assessment", "retired"}
ASSESSMENT_KEYS = {"level", "summary", "basis", "caveats"}
BASIS_KEYS = {"routes", "evidence", "reviews", "runs", "counterexamples"}
SOURCE_KEYS = {"path", "node", "locator", "kind", "note", "date", "hash",
               "scope", "verdict", "reviewed_hash", "result"}
ASSUMPTION_KEYS = {"kind", "statement", "source"}
FORMALIZATION_KEYS = {"lean"}
LEAN_KEYS = {"module", "file", "claim", "theorems", "state", "rel", "build",
             "claim_hash", "source_claim_hash", "sync_state", "synced"}
DISPOSITION_KEYS = {"state", "reason", "revive", "source"}
FRONTIER_KEYS = {"task", "kind", "since"}
EVENT_KEYS = {"date", "type", "summary", "sources", "from", "to", "route"}
EVENT_TYPES = {
    "created",
    "level-change",
    "route-added",
    "route-retired",
    "route-refuted",
    "review-completed",
    "repair-applied",
}
DONE_TOKEN = re.compile(r"(?:~~|\bDONE\b|\bCOMPLETED\b)", re.IGNORECASE)
STATUS_TOKEN = re.compile(
    r"\[(?:PROVED|OPEN|CONJECTURED|NUMERICAL|CERTIFIED\*?|REFUTED)(?:[^\]]*)\]",
    re.IGNORECASE,
)
GENERIC_REVIVE = (
    "Resume only after a reviewer identifies a concrete route that is not blocked "
    "by the recorded failure."
)


@dataclass
class LoadedProblem:
    nodes: dict[str, dict[str, Any]]
    paths: dict[str, Path]
    roots: list[str]


def claim_hash(claim: str) -> str:
    frozen = claim.replace("\r\n", "\n").strip()
    return "sha256:" + hashlib.sha256(frozen.encode("utf-8")).hexdigest()


def _load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_problem(problem_root: Path) -> LoadedProblem:
    dag_root = problem_root / "proof-dag"
    project = _load_yaml(dag_root / "PROJECT.yaml") or {}
    if not isinstance(project, dict):
        raise ValueError(f"{dag_root / 'PROJECT.yaml'}: manifest must be a mapping")
    nodes: dict[str, dict[str, Any]] = {}
    paths: dict[str, Path] = {}
    for path in sorted((dag_root / "nodes").glob("*.yaml")):
        data = _load_yaml(path)
        if not isinstance(data, dict):
            raise ValueError(f"{path}: node must be a mapping")
        node_id = data.get("id")
        if not isinstance(node_id, str):
            raise ValueError(f"{path}: id must be a string")
        if node_id in nodes:
            raise ValueError(f"{path}: duplicate id {node_id}")
        nodes[node_id] = data
        paths[node_id] = path
    return LoadedProblem(nodes, paths, list(project.get("roots") or []))


def _nonempty(value: Any) -> bool:
    return value not in (None, "", [], {})


def _check_closed(mapping: Any, allowed: set[str], label: str, errors: list[str]) -> bool:
    if not isinstance(mapping, dict):
        errors.append(f"{label} must be a mapping")
        return False
    unknown = set(mapping) - allowed
    if unknown:
        errors.append(f"{label} has unknown keys {sorted(unknown)}")
    return True


def _resolve_node_ref(ref: str, loaded: LoadedProblem) -> str | None:
    if ref in loaded.nodes:
        return ref
    return None


def _normalize_prose(text: str) -> str:
    """Normalize prose for conservative anti-circularity comparisons."""
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text.lower()).split())


def _review_scope_merely_restates(
    scope: str, target_statement: str | tuple[str, ...] | None
) -> bool:
    """Reject review metadata that substitutes the subject for review coverage."""
    if scope.startswith("Review coverage for "):
        return True
    normalized_scope = _normalize_prose(scope)
    targets = target_statement if isinstance(target_statement, tuple) else (target_statement,)
    for target in targets:
        if not target:
            continue
        normalized_target = _normalize_prose(target)
        if len(normalized_target) >= 30 and normalized_target in normalized_scope:
            return True
    return False


_LOCATOR_CONTEXT = re.compile(
    r"\b(?:sections?|reviews?|items?|phases?|attacks?|tasks?|defects?|parts?|rules?|"
    r"theorems?|lemmas?|corollaries?|lines?)\s+"
    r"([A-Z]?\d+(?:\.[A-Za-z0-9']+)*|[A-Z](?:\.\d+)+|"
    r"[A-Z][A-Z0-9']*(?:-[A-Z0-9']+)+)"
    r"(?:\s*--\s*([A-Z]?\d+(?:\.[A-Za-z0-9']+)*|[A-Z](?:\.\d+)+|"
    r"[A-Z][A-Z0-9']*(?:-[A-Z0-9']+)+))?",
    re.IGNORECASE,
)
_LOCATOR_LITERAL = re.compile(r"`([^`\n]+)`")
_LOCATOR_CODE = re.compile(
    r"\b(?:[A-Z][A-Z0-9']*-[A-Za-z0-9']+(?:-[A-Za-z0-9']+)*|"
    r"[A-Z][A-Z0-9']*\d[A-Za-z0-9'.-]*|(?:cor|thm):[A-Za-z0-9_-]+)\b"
)
_LOCATOR_HEADINGS = {
    "ruling", "verdict", "amendments", "boundary", "ledger", "census",
    "summary", "disposition", "comparison", "checks",
}


def _locator_anchors(locator: str) -> list[str]:
    """Extract stable section/label anchors from a human-readable locator."""
    normalized = locator.replace("–", "--").replace("—", "--")
    anchors: list[str] = []
    anchors.extend(_LOCATOR_LITERAL.findall(normalized))
    for match in _LOCATOR_CONTEXT.finditer(normalized):
        anchors.extend(group for group in match.groups() if group)
    anchors.extend(_LOCATOR_CODE.findall(normalized))
    anchors = [
        endpoint
        for anchor in anchors
        for endpoint in re.split(r"\s*--\s*", anchor)
        if endpoint
    ]
    if not anchors:
        lowered = normalized.lower()
        anchors.extend(word for word in sorted(_LOCATOR_HEADINGS) if word in lowered)
    return list(dict.fromkeys(anchor.strip(".,;:()[]") for anchor in anchors if anchor))


def _check_path_locator(
    source: dict[str, Any], label: str, root: Path, errors: list[str]
) -> None:
    """Check that a path locator names anchors present in the linked artifact."""
    locator = source.get("locator")
    source_path = source.get("path")
    if not isinstance(locator, str) or not locator.strip() or not isinstance(source_path, str):
        return
    path = root / source_path
    if not path.is_file():
        return
    anchors = _locator_anchors(locator)
    if not anchors:
        errors.append(f"{label}.locator has no mechanically checkable anchor")
        return
    text = path.read_text(encoding="utf-8", errors="replace").lower()
    text = text.replace("′", "'").replace("’", "'")
    if all(anchor.lower() in _LOCATOR_HEADINGS for anchor in anchors):
        if not any(anchor.lower() in text for anchor in anchors):
            errors.append(
                f"{label}.locator heading does not occur in {source_path}"
            )
        return
    missing = [
        anchor for anchor in anchors
        if anchor.lower().replace("′", "'").replace("’", "'") not in text
    ]
    if missing:
        errors.append(
            f"{label}.locator anchor(s) {missing} do not occur in {source_path}"
        )


def _check_source(
    source: Any,
    label: str,
    root: Path,
    loaded: LoadedProblem,
    errors: list[str],
) -> None:
    if not _check_closed(source, SOURCE_KEYS, label, errors):
        return
    if not any(key in source for key in ("path", "node", "note")):
        errors.append(f"{label} requires path, node, or note")
    if "path" in source:
        source_path = Path(str(source["path"]))
        if source_path.is_absolute() or ".." in source_path.parts:
            errors.append(f"{label}: path must be repository-relative")
            return
        if source.get("kind") == "review" and (
            len(source_path.parts) < 3
            or source_path.parts[1] != "reviews"
        ):
            errors.append(
                f"{label}: review reports are project-level objects and must live under "
                "<project>/reviews/"
            )
        path = root / source_path
        if not path.exists():
            errors.append(f"{label}: missing path {source['path']}")
    if "node" in source and _resolve_node_ref(str(source["node"]), loaded) is None:
        errors.append(f"{label}: unknown node reference {source['node']}")


def _check_basis(
    basis: Any,
    label: str,
    root: Path,
    loaded: LoadedProblem,
    route_ids: set[str],
    errors: list[str],
    target_statement: str | tuple[str, ...] | None = None,
) -> None:
    if not _check_closed(basis, BASIS_KEYS, label, errors):
        return
    for key, value in basis.items():
        if not isinstance(value, list) or not value:
            errors.append(f"{label}.{key} must be a nonempty list")
            continue
        if key == "routes":
            for route_id in value:
                if route_id not in route_ids:
                    errors.append(f"{label}.routes references unknown route {route_id}")
            continue
        for index, source in enumerate(value):
            _check_source(
                source, f"{label}.{key}[{index}]", root, loaded, errors
            )
            if isinstance(source, dict):
                expected_kind = {
                    "reviews": "review",
                    "runs": "run",
                    "counterexamples": "counterexample",
                }.get(key)
                if expected_kind and source.get("kind") != expected_kind:
                    errors.append(
                        f"{label}.{key}[{index}].kind must be {expected_kind!r}"
                    )
                if key == "evidence" and source.get("node"):
                    if source.get("kind") != "node-evidence":
                        errors.append(
                            f"{label}.evidence[{index}].kind must be 'node-evidence' "
                            "for a non-load-bearing node cross-reference; use a route "
                            "premise for a proof dependency"
                        )
                if key == "reviews":
                    scope = str(source.get("scope", ""))
                    if _review_scope_merely_restates(scope, target_statement):
                        errors.append(
                            f"{label}.reviews[{index}].scope merely restates the subject; "
                            "record what the linked review actually checked"
                        )
                    _check_path_locator(
                        source, f"{label}.reviews[{index}]", root, errors
                    )
                if key == "runs":
                    if not source.get("result"):
                        errors.append(f"{label}.runs[{index}] requires a scoped result")
                    if source.get("locator"):
                        _check_path_locator(source, f"{label}.runs[{index}]", root, errors)


def _check_assessment(
    assessment: Any,
    label: str,
    root: Path,
    loaded: LoadedProblem,
    route_ids: set[str],
    errors: list[str],
    target_statement: str | tuple[str, ...] | None = None,
) -> str | None:
    if not _check_closed(assessment, ASSESSMENT_KEYS, label, errors):
        return None
    level = assessment.get("level")
    if level not in LEVELS:
        errors.append(f"{label}.level is invalid: {level!r}")
    if not isinstance(assessment.get("summary"), str) or not assessment["summary"].strip():
        errors.append(f"{label}.summary must be nonempty")
    if "basis" in assessment:
        _check_basis(
            assessment["basis"], f"{label}.basis", root, loaded, route_ids, errors,
            target_statement,
        )
    if level in COMPLETION_LEVELS:
        reviewed_statement = (
            target_statement[0]
            if isinstance(target_statement, tuple) and target_statement
            else target_statement
        )
        if isinstance(reviewed_statement, str):
            expected_hash = claim_hash(reviewed_statement)
            reviews = ((assessment.get("basis") or {}).get("reviews") or [])
            for index, source in enumerate(reviews):
                if not isinstance(source, dict):
                    continue
                actual_hash = source.get("reviewed_hash")
                if actual_hash != expected_hash:
                    errors.append(
                        f"{label}.basis.reviews[{index}].reviewed_hash must equal "
                        f"{expected_hash}; the review must be bound to the current statement"
                    )
    if "caveats" in assessment:
        caveats = assessment["caveats"]
        if not isinstance(caveats, list) or not caveats or not all(isinstance(x, str) and x.strip() for x in caveats):
            errors.append(f"{label}.caveats must be a nonempty list of strings")
    return level if isinstance(level, str) else None


def _has_locatable_review(assessment: dict[str, Any]) -> bool:
    reviews = (assessment.get("basis") or {}).get("reviews") or []
    for source in reviews:
        if (isinstance(source, dict) and source.get("kind") == "review"
                and (source.get("path") or source.get("node"))
                and (source.get("locator") or source.get("scope"))):
            return True
    return False


def _has_typed_source(assessment: dict[str, Any], key: str, kind: str) -> bool:
    for source in ((assessment.get("basis") or {}).get(key) or []):
        if (isinstance(source, dict) and source.get("kind") == kind
                and (source.get("path") or source.get("node")
                     or (kind == "counterexample" and source.get("note")))):
            return True
    return False


def _check_assumptions(assumptions, label, root, loaded, errors):
    """Validate a route-level or route-free node-level assumptions mapping."""
    if assumptions is None:
        return
    if not isinstance(assumptions, dict) or not assumptions:
        errors.append(f"{label}.assumptions must be a nonempty mapping")
        return
    for aid, assumption in assumptions.items():
        alabel = f"{label}.assumptions.{aid}"
        if not _check_closed(assumption, ASSUMPTION_KEYS, alabel, errors):
            continue
        if assumption.get("kind") not in {"external-theorem", "model-fact"}:
            errors.append(f"{alabel}.kind must be external-theorem or model-fact")
        if not isinstance(assumption.get("statement"), str) or not assumption["statement"].strip():
            errors.append(f"{alabel}.statement must be nonempty")
        if "source" not in assumption:
            errors.append(f"{alabel}.source is required")
        else:
            source = assumption["source"]
            if not isinstance(source, dict) or not (
                source.get("path") or source.get("node") or source.get("note")
            ):
                errors.append(
                    f"{alabel}.source must identify a repository path, claim node, "
                    "or bibliographic note"
                )
            elif source.get("path") and not source.get("locator"):
                errors.append(
                    f"{alabel}.source.locator is required for a path source"
                )
            _check_source(source, f"{alabel}.source", root, loaded, errors)
            if isinstance(source, dict) and source.get("path"):
                _check_path_locator(
                    source, f"{alabel}.source", root, errors
                )


def validate_problem(
    root: Path,
    problem_root: Path,
    problem: str,
) -> tuple[list[str], list[str], int]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        loaded = load_problem(problem_root)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [f"{problem}: {exc}"], [], 0

    if not loaded.roots:
        errors.append(f"{problem}: PROJECT.yaml requires at least one explicit root")
    for root_id in loaded.roots:
        if _resolve_node_ref(root_id, loaded) is None:
            errors.append(f"{problem}: unknown root {root_id}")

    edges: dict[str, list[str]] = {node_id: [] for node_id in loaded.nodes}
    for node_id, node in loaded.nodes.items():
        path = loaded.paths[node_id]
        label = path.relative_to(root).as_posix()
        unknown = set(node) - TOP_KEYS
        if unknown:
            errors.append(f"{label}: unknown top-level keys {sorted(unknown)}")
        if path.stem != node_id:
            errors.append(f"{label}: filename stem must equal id {node_id}")
        for key in set(node) - {"id", "claim", "assessment"}:
            if not _nonempty(node[key]):
                errors.append(f"{label}: optional key {key} is present but empty")
        role = node.get("role", "proof")
        if role not in ROLES:
            errors.append(f"{label}: invalid role {role!r}")
        aliases = node.get("aliases")
        if aliases is not None and (not isinstance(aliases, list) or not aliases):
            errors.append(f"{label}: aliases must be a nonempty list when present")
        claim = node.get("claim")
        if not isinstance(claim, str) or not claim.strip():
            errors.append(f"{label}: claim must be a nonempty string")
        elif STATUS_TOKEN.search(claim):
            warnings.append(f"{node_id}: claim still contains a legacy status tag")

        routes = node.get("routes") or {}
        if not isinstance(routes, dict):
            errors.append(f"{label}: routes must be a mapping")
            routes = {}
        if node.get("assumptions") is not None and routes:
            errors.append(
                f"{label}.assumptions is only valid for a route-free direct proof; "
                "attach each assumption to every route that uses it"
            )
        _check_assumptions(node.get("assumptions"), label, root, loaded, errors)
        route_ids = set(routes)
        route_levels: dict[str, str | None] = {}
        for route_id, route in routes.items():
            route_label = f"{node_id}.routes.{route_id}"
            if not _check_closed(route, ROUTE_KEYS, route_label, errors):
                continue
            premises = route.get("premises")
            if not isinstance(premises, list) or not premises:
                errors.append(f"{route_label}.premises must be a nonempty list")
                premises = []
            if len(premises) != len(set(premises)):
                errors.append(f"{route_label}.premises contains duplicates")
            for premise in premises:
                resolved = _resolve_node_ref(str(premise), loaded)
                if resolved is None:
                    errors.append(f"{route_label}: unknown premise {premise}")
                else:
                    edges[node_id].append(resolved)
            implication = route.get("implication")
            if not isinstance(implication, str) or not implication.strip():
                errors.append(f"{route_label}.implication must be nonempty")
            _check_assumptions(route.get("assumptions"), route_label, root, loaded, errors)
            if "proof" in route:
                proof = route["proof"]
                if not isinstance(proof, dict) or not proof:
                    errors.append(f"{route_label}.proof must be a nonempty mapping")
                elif not any(_nonempty(proof.get(k)) for k in ("sketch", "sources")):
                    errors.append(f"{route_label}.proof requires sketch or sources")
                elif "sources" in proof:
                    for i, source in enumerate(proof["sources"]):
                        _check_source(
                            source, f"{route_label}.proof.sources[{i}]", root, loaded,
                            errors,
                        )
            route_levels[route_id] = _check_assessment(
                route.get("assessment"), f"{route_label}.assessment", root, loaded,
                set(), errors,
                (
                    implication,
                    claim if isinstance(claim, str) else "",
                ) if isinstance(implication, str) else None,
            )
            route_assessment = route.get("assessment") or {}
            route_level = route_levels[route_id]
            if route_level in COMPLETION_LEVELS:
                if not _has_locatable_review(route_assessment):
                    errors.append(
                        f"{route_label}: completion level requires a locatable review"
                    )
            if route_level == "NUMERICAL" and not _has_typed_source(
                route_assessment, "runs", "run"
            ):
                errors.append(f"{route_label}: NUMERICAL requires a structured run record")
            if route_level == "CERTIFIED*" and not route_assessment.get("caveats"):
                errors.append(f"{route_label}: CERTIFIED* requires caveats")
            if route_level == "REFUTED" and not _has_typed_source(
                route_assessment, "counterexamples", "counterexample"
            ):
                errors.append(f"{route_label}: REFUTED requires a structured counterexample or contradiction")
            if "retired" in route:
                retired = route["retired"]
                if not isinstance(retired, dict) or not retired.get("date") or not retired.get("sources"):
                    errors.append(f"{route_label}.retired requires date and sources")

        node_level = _check_assessment(
            node.get("assessment"), f"{node_id}.assessment", root, loaded, route_ids,
            errors, claim if isinstance(claim, str) else None,
        )
        caveats = node.get("assessment", {}).get("caveats") or []
        basis = node.get("assessment", {}).get("basis") or {}
        has_review = _has_locatable_review(node.get("assessment") or {})
        if node_level in COMPLETION_LEVELS and not has_review:
            errors.append(
                f"{node_id}: completion level requires a locatable review"
            )
        node_evidence = [
            source for source in basis.get("evidence", [])
            if isinstance(source, dict) and source.get("node")
        ]
        if (node_id in loaded.roots and role == "outcome"
                and node_level in COMPLETION_LEVELS and node_evidence
                and not basis.get("routes")):
            errors.append(
                f"{node_id}: a completion-level outcome cites supporting nodes only as "
                "evidence; encode load-bearing dependencies as assessed route premises"
            )
        if node_level == "NUMERICAL" and not _has_typed_source(
            node.get("assessment") or {}, "runs", "run"
        ):
            errors.append(f"{node_id}: NUMERICAL requires a structured run record")
        if node_level == "CERTIFIED*" and not caveats:
            errors.append(f"{node_id}: CERTIFIED* requires caveats")

        disposition = node.get("disposition")
        if disposition is not None:
            if _check_closed(disposition, DISPOSITION_KEYS, f"{node_id}.disposition", errors):
                state = disposition.get("state")
                if state not in {"DEAD", "PARKED"}:
                    errors.append(f"{node_id}.disposition.state is invalid")
                if not isinstance(disposition.get("reason"), str) or not disposition["reason"].strip():
                    errors.append(f"{node_id}.disposition.reason must be nonempty")
                if state == "PARKED" and (not isinstance(disposition.get("revive"), str) or not disposition["revive"].strip()):
                    errors.append(f"{node_id}: PARKED requires a concrete revive condition")
                elif state == "PARKED" and disposition.get("revive", "").strip() == GENERIC_REVIVE:
                    errors.append(f"{node_id}: PARKED revive condition is the rejected generic template")
                if "source" in disposition:
                    _check_source(
                        disposition["source"], f"{node_id}.disposition.source", root,
                        loaded, errors,
                    )
        if node_level == "REFUTED" and disposition is None:
            errors.append(f"{node_id}: REFUTED requires disposition")
        if node_level == "REFUTED" and not _has_typed_source(
            node.get("assessment") or {}, "counterexamples", "counterexample"
        ):
            errors.append(f"{node_id}: REFUTED requires a structured counterexample or contradiction")

        formalization = node.get("formalization")
        if formalization is not None:
            if _check_closed(formalization, FORMALIZATION_KEYS, f"{node_id}.formalization", errors):
                lean = formalization.get("lean")
                if _check_closed(lean, LEAN_KEYS, f"{node_id}.formalization.lean", errors):
                    for req in ("module", "file", "claim", "state", "claim_hash", "sync_state"):
                        if not _nonempty(lean.get(req)):
                            errors.append(f"{node_id}.formalization.lean.{req} is required")
                    if lean.get("sync_state") not in {"current", "stale"}:
                        errors.append(f"{node_id}: lean.sync_state must be current or stale")
                    if isinstance(claim, str) and lean.get("claim_hash") != claim_hash(claim):
                        errors.append(f"{node_id}: lean.claim_hash does not match the current claim")
                    lean_file = root / str(lean.get("file", ""))
                    if not lean_file.exists():
                        errors.append(f"{node_id}: missing Lean file {lean.get('file')}")
                    else:
                        lean_text = lean_file.read_text(encoding="utf-8")
                        claim_name = str(lean.get("claim") or "")
                        if claim_name and not re.search(
                            rf"^\s*(?:def|abbrev|theorem|lemma)\s+{re.escape(claim_name)}\b",
                            lean_text,
                            re.MULTILINE,
                        ):
                            errors.append(
                                f"{node_id}: declared Lean claim {claim_name!r} is absent from "
                                f"{lean.get('file')}"
                            )
                        for theorem in lean.get("theorems") or []:
                            if not re.search(
                                rf"^\s*(?:def|abbrev|theorem|lemma)\s+{re.escape(str(theorem))}\b",
                                lean_text,
                                re.MULTILINE,
                            ):
                                errors.append(
                                    f"{node_id}: declared Lean theorem {theorem!r} is absent from "
                                    f"{lean.get('file')}"
                                )
                    if lean_file.exists() and lean.get("sync_state") == "current":
                        lean_text = lean_file.read_text(encoding="utf-8")
                        if str(lean.get("claim_hash")).removeprefix("sha256:") not in lean_text[:5000]:
                            warnings.append(f"{node_id}: current Lean module does not quote the claim hash")
                    elif not any("Lean" in str(c) or "formal" in str(c) for c in caveats):
                        errors.append(f"{node_id}: stale linked formalization requires a node caveat")

        frontier = node.get("frontier") or {}
        if not isinstance(frontier, dict):
            errors.append(f"{node_id}.frontier must be a mapping")
        for task_id, task in frontier.items():
            tlabel = f"{node_id}.frontier.{task_id}"
            if not _check_closed(task, FRONTIER_KEYS, tlabel, errors):
                continue
            text = task.get("task")
            if not isinstance(text, str) or not text.strip():
                errors.append(f"{tlabel}.task must be nonempty")
            elif DONE_TOKEN.search(text):
                errors.append(f"{tlabel}.task contains a completed-task token")
            if task.get("kind", "task") not in {"task", "gate", "review"}:
                errors.append(f"{tlabel}.kind is invalid")

        events = node.get("events") or {}
        if not isinstance(events, dict):
            errors.append(f"{node_id}.events must be a mapping")
            events = {}
        for event_id, event in events.items():
            elabel = f"{node_id}.events.{event_id}"
            if not _check_closed(event, EVENT_KEYS, elabel, errors):
                continue
            if not isinstance(event.get("date"), str) or not event["date"].strip():
                errors.append(f"{elabel}.date must be nonempty")
            event_type = event.get("type")
            if event_type not in EVENT_TYPES:
                errors.append(f"{elabel}.type is invalid: {event_type!r}")
            if not isinstance(event.get("summary"), str) or not event["summary"].strip():
                errors.append(f"{elabel}.summary must be nonempty")
            sources = event.get("sources")
            if not isinstance(sources, list) or not sources:
                errors.append(f"{elabel}.sources must be a nonempty list")
            else:
                for index, source in enumerate(sources):
                    _check_source(
                        source, f"{elabel}.sources[{index}]", root, loaded, errors
                    )
            if event_type == "level-change":
                if event.get("from") not in LEVELS:
                    errors.append(f"{elabel}.from must be an evidence level")
                if event.get("to") not in LEVELS:
                    errors.append(f"{elabel}.to must be an evidence level")
                if event.get("from") == event.get("to"):
                    errors.append(f"{elabel}: level change must change the level")
            elif "from" in event or "to" in event:
                errors.append(f"{elabel}: from/to are only valid for level-change events")
            if "route" in event and event["route"] not in route_ids:
                errors.append(f"{elabel}.route references unknown route {event['route']}")

        # A route's implication and its premises are separate obligations. A review
        # of the parent does not make an open, refuted, or retired route usable.
        for route_id in basis.get("routes", []):
            route = routes.get(route_id, {})
            if node_level not in COMPLETION_LEVELS:
                continue
            route_level = route_levels.get(route_id)
            if route.get("retired"):
                errors.append(f"{node_id}: completion basis cites retired route {route_id}")
            if route_level not in COMPLETION_LEVELS:
                errors.append(
                    f"{node_id}: completion route {route_id} has non-completion "
                    f"implication level {route_level}"
                )
            premise_levels = {
                p: loaded.nodes.get(p, {}).get("assessment", {}).get("level")
                for p in route.get("premises", [])
            }
            refuted = [p for p, level in premise_levels.items() if level == "REFUTED"]
            if refuted:
                errors.append(
                    f"{node_id}: completion route {route_id} uses refuted premises {refuted}"
                )
            if node_level == "PROVED":
                unproved = [p for p, level in premise_levels.items() if level != "PROVED"]
                if route_level != "PROVED" or unproved:
                    errors.append(
                        f"{node_id}: PROVED requires a PROVED route implication and "
                        f"PROVED premises; route {route_id}, unproved premises {unproved}"
                    )
            below = [p for p in route.get("premises", [])
                     if loaded.nodes.get(p, {}).get("assessment", {}).get("level") not in COMPLETION_LEVELS]
            if below and not all(any(p in c for c in caveats) for p in below):
                errors.append(f"{node_id}: completion route {route_id} has sub-completion premises {below} without caveats")

    cycle = _find_cycle(edges)
    if cycle:
        errors.append(f"{problem}: hypergraph cycle: {' -> '.join(cycle)}")

    expected_index = render_index(problem, loaded)
    expected_graph = render_mermaid(problem, loaded)
    index_path = problem_root / "proof-dag" / "NODE_INDEX.md"
    graph_path = problem_root / "proof-dag" / "GRAPH.mmd"
    if not index_path.exists() or index_path.read_text(encoding="utf-8") != expected_index:
        errors.append(f"{problem}: generated NODE_INDEX.md is stale; run --write-generated")
    if not graph_path.exists() or graph_path.read_text(encoding="utf-8") != expected_graph:
        errors.append(f"{problem}: generated GRAPH.mmd is stale; run --write-generated")
    return errors, warnings, len(loaded.nodes)


def validate_preservation(previous: LoadedProblem, current: LoadedProblem) -> list[str]:
    """Check retention against an explicit earlier snapshot, without changing either.

    A single snapshot cannot establish append-only history. This comparison
    checks retention, not whether the historical events were truthfully recorded.
    Claims and assessments may be corrected; existing events remain immutable,
    and superseded routes stay registered rather than being silently deleted.
    """
    errors: list[str] = []
    for node_id, old in previous.nodes.items():
        if node_id not in current.nodes:
            errors.append(f"{node_id}: previously registered node was removed")
            continue
        new = current.nodes[node_id]
        for event_id, event in (old.get("events") or {}).items():
            if event_id not in (new.get("events") or {}):
                errors.append(f"{node_id}: previous event {event_id} was removed")
            elif new["events"][event_id] != event:
                errors.append(f"{node_id}: previous event {event_id} was rewritten")
        for route_id in old.get("routes") or {}:
            if route_id not in (new.get("routes") or {}):
                errors.append(
                    f"{node_id}: previous route {route_id} was removed; retain it "
                    "with its assessment and retirement record"
                )
    return errors


def _find_cycle(edges: dict[str, list[str]]) -> list[str] | None:
    visiting: set[str] = set()
    visited: set[str] = set()
    trail: list[str] = []

    def visit(node: str) -> list[str] | None:
        if node in visiting:
            return trail[trail.index(node):] + [node]
        if node in visited:
            return None
        visiting.add(node)
        trail.append(node)
        for child in edges.get(node, []):
            result = visit(child)
            if result:
                return result
        trail.pop()
        visiting.remove(node)
        visited.add(node)
        return None

    for node in edges:
        result = visit(node)
        if result:
            return result
    return None


def derived_shape(node: dict[str, Any]) -> str:
    routes = node.get("routes") or {}
    if not routes:
        return "leaf"
    live = [route for route in routes.values() if not route.get("retired")]
    if len(live) > 1:
        return "OR"
    if live and len(live[0].get("premises") or []) > 1:
        return "AND"
    return "route"


def render_index(problem: str, loaded: LoadedProblem) -> str:
    lines = [
        f"# {problem.upper()} proof-DAG index (generated)",
        "",
        "Do not edit this file by hand. It is generated from canonical node records.",
        "",
        "| Node | Role | Level | Shape | Disposition | Routes |",
        "|---|---|---|---|---|---:|",
    ]
    for node_id, node in sorted(loaded.nodes.items()):
        role = node.get("role", "proof")
        level = node["assessment"]["level"]
        disposition = (node.get("disposition") or {}).get("state", "-")
        lines.append(
            f"| `{node_id}` | {role} | {level} | {derived_shape(node)} | {disposition} | {len(node.get('routes') or {})} |"
        )
    return "\n".join(lines) + "\n"


def render_mermaid(problem: str, loaded: LoadedProblem) -> str:
    ids = {node_id: f"n{index}" for index, node_id in enumerate(sorted(loaded.nodes))}
    lines = [f"%% {problem.upper()} proof hypergraph (generated)", "flowchart BT"]
    for node_id, node in sorted(loaded.nodes.items()):
        level = node["assessment"]["level"]
        label = f"{node_id}\\n{level}".replace('"', "'")
        lines.append(f"  {ids[node_id]}[\"{label}\"]")
    edge_index = 0
    for parent_id, node in sorted(loaded.nodes.items()):
        for route_id, route in (node.get("routes") or {}).items():
            edge_index += 1
            join = f"r{edge_index}"
            route_level = route["assessment"]["level"]
            lines.append(f"  {join}((\"{route_id}\\n{route_level}\"))")
            for premise in route["premises"]:
                resolved = _resolve_node_ref(premise, loaded)
                if resolved:
                    lines.append(f"  {ids[resolved]} --> {join}")
            lines.append(f"  {join} --> {ids[parent_id]}")
    return "\n".join(lines) + "\n"


def write_generated(problem_root: Path, problem: str) -> None:
    loaded = load_problem(problem_root)
    (problem_root / "proof-dag" / "NODE_INDEX.md").write_text(
        render_index(problem, loaded), encoding="utf-8"
    )
    (problem_root / "proof-dag" / "GRAPH.mmd").write_text(
        render_mermaid(problem, loaded), encoding="utf-8"
    )


def chain_strength_report(problem_root: Path, problem: str) -> None:
    loaded = load_problem(problem_root)
    memo: dict[str, int] = {}

    def strength(node_id: str, stack: tuple[str, ...] = ()) -> int:
        if node_id in memo:
            return memo[node_id]
        if node_id in stack:
            return 0
        node = loaded.nodes[node_id]
        routes = node.get("routes") or {}
        if not routes:
            memo[node_id] = LEVEL_RANK[node["assessment"]["level"]]
            return memo[node_id]
        scores = []
        for route in routes.values():
            if route.get("retired") or route["assessment"]["level"] == "REFUTED":
                continue
            premise_score = min(strength(p, stack + (node_id,)) for p in route["premises"])
            scores.append(min(premise_score, LEVEL_RANK[route["assessment"]["level"]]))
        memo[node_id] = max(scores) if scores else -1
        return memo[node_id]

    inverse = {value: key for key, value in LEVEL_RANK.items()}
    rows = []
    for node_id, node in loaded.nodes.items():
        if not node.get("routes"):
            continue
        support = strength(node_id)
        own = LEVEL_RANK[node["assessment"]["level"]]
        if own > support:
            rows.append((node_id, node["assessment"]["level"], inverse.get(support, str(support))))
    print(f"[chain-strength] {problem}: {len(rows)} internal node(s) outrank route support")
    for row in sorted(rows):
        print(f"  {row[0]}: status {row[1]}, route support {row[2]}")
