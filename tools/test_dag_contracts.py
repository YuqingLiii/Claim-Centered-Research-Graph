#!/usr/bin/env python3
"""Production-path regression tests for the proof-DAG contract."""

from __future__ import annotations

from pathlib import Path
import tempfile
import unittest
from copy import deepcopy

import yaml

import proof_dag_schema


def write_yaml(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")


def review(statement: str, scope: str, locator: str = "Section 1") -> dict:
    return {
        "path": "test/reviews/review.md",
        "kind": "review",
        "scope": scope,
        "locator": locator,
        "reviewed_hash": proof_dag_schema.claim_hash(statement),
    }


class ValidatorIntegrationTests(unittest.TestCase):
    def make_problem(self, root: Path) -> Path:
        problem = root / "test"
        dag = problem / "proof-dag"
        (dag / "nodes").mkdir(parents=True)
        (root / "test/reviews").mkdir(parents=True)
        (root / "test/reviews/review.md").write_text(
            "# Independent review\n\n## Section 1\nChecks algebra and endpoints.\n"
            "\n## Section 2\nChecks the assembled implication.\n",
            encoding="utf-8",
        )
        (root / "theorem.md").write_text(
            "# Imported result\n\n## Theorem 1\n"
            "For every integer n, adding n to itself gives 2*n.\n",
            encoding="utf-8",
        )
        child_claim = "For every integer n>=1, n+n=2*n."
        parent_claim = "For every integer n>=1, 2*n is even."
        implication = "The identity n+n=2*n implies that 2*n is divisible by two."
        child = {
            "id": "TEST.child",
            "claim": child_claim,
            "assessment": {
                "level": "PROVED",
                "summary": "Elementary identity checked independently.",
                "basis": {"reviews": [review(child_claim, "Checks the integer identity and its domain.")]},
            },
        }
        parent = {
            "id": "TEST.parent", "role": "outcome", "claim": parent_claim,
            "routes": {"joint": {
                "premises": ["TEST.child"], "implication": implication,
                "assessment": {
                    "level": "PROVED", "summary": "Implication checked independently.",
                    "basis": {"reviews": [review(
                        implication, "Checks divisibility and transfer from the premise.", "Section 2"
                    )]},
                },
            }},
            "assessment": {
                "level": "PROVED", "summary": "Assembled claim checked independently.",
                "basis": {
                    "routes": ["joint"],
                    "reviews": [review(parent_claim, "Checks the final quantified parity statement.")],
                },
            },
        }
        write_yaml(dag / "nodes/TEST.child.yaml", child)
        write_yaml(dag / "nodes/TEST.parent.yaml", parent)
        write_yaml(dag / "PROJECT.yaml", {"schema_version": 1, "project": "test", "roots": ["TEST.parent"]})
        proof_dag_schema.write_generated(problem, "test")
        return problem

    def validate(self, root: Path, problem: Path) -> list[str]:
        return proof_dag_schema.validate_problem(root, problem, "test")[0]

    def test_valid_fixture_passes_production_validator(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(self.validate(root, self.make_problem(root)), [])

    def test_completion_rejects_unfinished_or_refuted_route(self) -> None:
        for level in ("OPEN", "CONJECTURED", "NUMERICAL", "REFUTED"):
            with self.subTest(level=level), tempfile.TemporaryDirectory() as directory:
                root = Path(directory); problem = self.make_problem(root)
                path = problem / "proof-dag/nodes/TEST.parent.yaml"
                node = yaml.safe_load(path.read_text())
                node["routes"]["joint"]["assessment"]["level"] = level
                write_yaml(path, node)
                proof_dag_schema.write_generated(problem, "test")
                self.assertTrue(any("non-completion implication level" in e
                                    for e in self.validate(root, problem)))

    def test_completion_rejects_retired_route(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.parent.yaml"
            node = yaml.safe_load(path.read_text())
            node["routes"]["joint"]["retired"] = {
                "date": "2026-08-25", "reason": "Superseded route.",
                "sources": [{"path": "test/reviews/review.md", "kind": "review"}],
            }
            write_yaml(path, node)
            proof_dag_schema.write_generated(problem, "test")
            self.assertTrue(any("completion basis cites retired route" in e
                                for e in self.validate(root, problem)))

    def test_proved_parent_cannot_hide_unproved_inputs_in_caveats(self) -> None:
        for child_level, route_level in (("OPEN", "PROVED"), ("CERTIFIED*", "PROVED"),
                                          ("PROVED", "CERTIFIED*")):
            with self.subTest(child=child_level, route=route_level), tempfile.TemporaryDirectory() as directory:
                root = Path(directory); problem = self.make_problem(root)
                path = problem / "proof-dag/nodes/TEST.parent.yaml"
                node = yaml.safe_load(path.read_text())
                node["routes"]["joint"]["assessment"]["level"] = route_level
                node["assessment"]["caveats"] = ["Conditional on TEST.child."]
                write_yaml(path, node)
                child_path = problem / "proof-dag/nodes/TEST.child.yaml"
                child = yaml.safe_load(child_path.read_text())
                child["assessment"]["level"] = child_level
                write_yaml(child_path, child)
                proof_dag_schema.write_generated(problem, "test")
                self.assertTrue(any("PROVED requires a PROVED route" in e
                                    for e in self.validate(root, problem)))

    def test_certified_parent_can_explicitly_depend_on_open_premise(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.parent.yaml"
            node = yaml.safe_load(path.read_text())
            node["assessment"]["level"] = "CERTIFIED*"
            node["assessment"]["caveats"] = ["Conditional on the open TEST.child."]
            write_yaml(path, node)
            child_path = problem / "proof-dag/nodes/TEST.child.yaml"
            child = yaml.safe_load(child_path.read_text())
            child["assessment"]["level"] = "OPEN"
            write_yaml(child_path, child)
            proof_dag_schema.write_generated(problem, "test")
            self.assertEqual(self.validate(root, problem), [])
            child["assessment"]["level"] = "REFUTED"
            write_yaml(child_path, child)
            proof_dag_schema.write_generated(problem, "test")
            self.assertTrue(any("uses refuted premises" in e for e in self.validate(root, problem)))

    def test_preservation_accepts_appended_events_and_retired_routes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            previous = proof_dag_schema.load_problem(problem)
            current = deepcopy(previous)
            current.nodes["TEST.parent"]["events"] = {"new": {"summary": "New evidence."}}
            current.nodes["TEST.parent"]["routes"]["joint"]["retired"] = {
                "date": "2026-08-25", "reason": "Superseded.",
                "sources": [{"path": "test/reviews/review.md", "kind": "review"}],
            }
            self.assertEqual(proof_dag_schema.validate_preservation(previous, current), [])

    def test_preservation_rejects_removed_nodes_routes_and_events(self) -> None:
        for target in ("node", "route", "event", "rewritten-event"):
            with self.subTest(target=target), tempfile.TemporaryDirectory() as directory:
                root = Path(directory); problem = self.make_problem(root)
                previous = proof_dag_schema.load_problem(problem)
                previous.nodes["TEST.parent"]["events"] = {"old": {"summary": "Original evidence."}}
                current = deepcopy(previous)
                if target == "node":
                    del current.nodes["TEST.parent"]
                elif target == "route":
                    del current.nodes["TEST.parent"]["routes"]["joint"]
                elif target == "event":
                    del current.nodes["TEST.parent"]["events"]["old"]
                else:
                    current.nodes["TEST.parent"]["events"]["old"]["summary"] = "Changed history."
                self.assertTrue(proof_dag_schema.validate_preservation(previous, current))

    def test_review_report_must_be_project_level(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            (root / "test/artifacts").mkdir()
            (root / "test/artifacts/review.md").write_text(
                (root / "test/reviews/review.md").read_text(), encoding="utf-8"
            )
            path = problem / "proof-dag/nodes/TEST.child.yaml"
            node = yaml.safe_load(path.read_text())
            node["assessment"]["basis"]["reviews"][0]["path"] = "test/artifacts/review.md"
            write_yaml(path, node)
            self.assertTrue(any(
                "project-level objects" in error for error in self.validate(root, problem)
            ))

    def test_node_scope_restatement_fails_production_validator(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.parent.yaml"
            node = yaml.safe_load(path.read_text())
            node["assessment"]["basis"]["reviews"][0]["scope"] = "Covers the canonical subject: " + node["claim"]
            write_yaml(path, node)
            self.assertTrue(any("merely restates" in e for e in self.validate(root, problem)))

    def test_false_locator_fails_production_validator(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.parent.yaml"
            node = yaml.safe_load(path.read_text())
            node["assessment"]["basis"]["reviews"][0]["locator"] = "Section 99.99"
            write_yaml(path, node)
            self.assertTrue(any("99.99" in e for e in self.validate(root, problem)))

    def test_run_locator_must_resolve(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.child.yaml"
            node = yaml.safe_load(path.read_text())
            node["assessment"]["basis"]["runs"] = [{
                "path": "test/reviews/review.md", "kind": "run",
                "locator": "`nonexistent finite scan`", "result": "Finite check claimed.",
            }]
            write_yaml(path, node)
            self.assertTrue(any("runs[0].locator anchor" in e for e in self.validate(root, problem)))

    def test_previous_state_missing_or_empty_fails_cleanly(self) -> None:
        from unittest.mock import patch
        import contextlib
        import io
        import proof_dag_check
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            for previous in (root / "missing", root / "empty"):
                if previous.name == "empty":
                    write_yaml(previous / "test/proof-dag/PROJECT.yaml", {"roots": ["TEST.parent"]})
                with patch.object(proof_dag_check, "ROOT", root), \
                     patch.object(proof_dag_check, "PROBLEMS", {"test": problem}), \
                     patch("sys.argv", ["check", "--previous-state", str(previous)]), \
                     contextlib.redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(proof_dag_check.main(), 1)
                    self.assertIn("cannot compare previous state", output.getvalue())

    def test_route_scope_cannot_restate_parent_claim(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.parent.yaml"
            node = yaml.safe_load(path.read_text())
            node["routes"]["joint"]["assessment"]["basis"]["reviews"][0]["scope"] = "Covers the canonical subject: " + node["claim"]
            write_yaml(path, node)
            self.assertTrue(any("merely restates" in e for e in self.validate(root, problem)))

    def test_silent_claim_change_invalidates_review(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.parent.yaml"
            node = yaml.safe_load(path.read_text())
            node["claim"] = "For every integer n>=1, 2*n is even and greater than n."
            write_yaml(path, node)
            self.assertTrue(any("reviewed_hash" in e for e in self.validate(root, problem)))

    def test_route_free_node_accepts_sourced_assumption(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.child.yaml"
            node = yaml.safe_load(path.read_text())
            node["assumptions"] = {"doubling-identity": {
                "kind": "external-theorem",
                "statement": "For every integer n, n+n=2*n.",
                "source": {
                    "path": "theorem.md", "kind": "text", "locator": "Theorem 1",
                },
            }}
            write_yaml(path, node)
            self.assertEqual(self.validate(root, problem), [])

    def test_assumption_requires_source(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.child.yaml"
            node = yaml.safe_load(path.read_text())
            node["assumptions"] = {"doubling-identity": {
                "kind": "external-theorem",
                "statement": "For every integer n, n+n=2*n.",
            }}
            write_yaml(path, node)
            self.assertTrue(any("source is required" in e for e in self.validate(root, problem)))

    def test_assumption_path_requires_locator(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.child.yaml"
            node = yaml.safe_load(path.read_text())
            node["assumptions"] = {"doubling-identity": {
                "kind": "external-theorem",
                "statement": "For every integer n, n+n=2*n.",
                "source": {"path": "theorem.md", "kind": "text"},
            }}
            write_yaml(path, node)
            self.assertTrue(any(
                "source.locator is required" in e for e in self.validate(root, problem)
            ))

    def test_assumption_locator_must_resolve_in_source(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.child.yaml"
            node = yaml.safe_load(path.read_text())
            node["assumptions"] = {"doubling-identity": {
                "kind": "external-theorem",
                "statement": "For every integer n, n+n=2*n.",
                "source": {
                    "path": "theorem.md", "kind": "text", "locator": "Theorem 99",
                },
            }}
            write_yaml(path, node)
            self.assertTrue(any(
                "locator anchor" in e and "99" in e
                for e in self.validate(root, problem)
            ))

    def test_assumption_accepts_bibliographic_note(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.child.yaml"
            node = yaml.safe_load(path.read_text())
            node["assumptions"] = {"doubling-identity": {
                "kind": "external-theorem",
                "statement": "For every integer n, n+n=2*n.",
                "source": {"note": "Example, Theorem 1 (2026), pp. 1--2."},
            }}
            write_yaml(path, node)
            self.assertEqual(self.validate(root, problem), [])

    def test_node_assumption_is_rejected_when_routes_exist(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.parent.yaml"
            node = yaml.safe_load(path.read_text())
            node["assumptions"] = {"doubling-identity": {
                "kind": "external-theorem",
                "statement": "For every integer n, n+n=2*n.",
                "source": {
                    "path": "theorem.md", "kind": "text", "locator": "Theorem 1",
                },
            }}
            write_yaml(path, node)
            self.assertTrue(any(
                "only valid for a route-free direct proof" in e
                for e in self.validate(root, problem)
            ))

    def test_current_research_event_is_valid(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.child.yaml"
            node = yaml.safe_load(path.read_text())
            node["events"] = {"independent-review-completed": {
                "date": "2026-08-25",
                "type": "review-completed",
                "summary": "An independent reviewer checked the current claim.",
                "sources": [{"path": "test/reviews/review.md", "kind": "review"}],
            }}
            write_yaml(path, node)
            self.assertEqual(self.validate(root, problem), [])

    def test_repository_maintenance_is_not_a_research_event(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); problem = self.make_problem(root)
            path = problem / "proof-dag/nodes/TEST.child.yaml"
            node = yaml.safe_load(path.read_text())
            node["events"] = {"repository-maintenance": {
                "date": "2026-08-25",
                "type": "maintenance",
                "summary": "Changed repository bookkeeping.",
                "sources": [{"note": "Repository maintenance"}],
            }}
            write_yaml(path, node)
            self.assertTrue(any("type is invalid" in e for e in self.validate(root, problem)))


if __name__ == "__main__":
    unittest.main()
