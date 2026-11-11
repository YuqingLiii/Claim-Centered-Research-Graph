#!/usr/bin/env python3
"""Production-path regression tests for DAG and public-release contracts."""

from __future__ import annotations

from contextlib import redirect_stdout
import hashlib
import io
from pathlib import Path
import tempfile
import unittest

import yaml

import build_public_release
import proof_dag_v6
import verify_public_release


def write_yaml(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")


def review(statement: str, scope: str, locator: str = "Section 1") -> dict:
    return {
        "path": "review.md",
        "kind": "review",
        "scope": scope,
        "locator": locator,
        "reviewed_hash": proof_dag_v6.claim_hash(statement),
    }


class ValidatorIntegrationTests(unittest.TestCase):
    def make_problem(self, root: Path) -> Path:
        problem = root / "research/test"
        dag = problem / "proof-dag"
        (dag / "nodes").mkdir(parents=True)
        (root / "review.md").write_text(
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
            "events": {"created-2026-08-19": {
                "date": "2026-08-19", "type": "created",
                "summary": "Registered fixture child.", "sources": [{"note": "fixture"}],
            }},
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
            "events": {"created-2026-08-19": {
                "date": "2026-08-19", "type": "created",
                "summary": "Registered fixture parent.", "sources": [{"note": "fixture"}],
            }},
        }
        write_yaml(dag / "nodes/TEST.child.yaml", child)
        write_yaml(dag / "nodes/TEST.parent.yaml", parent)
        write_yaml(dag / "PROJECT.yaml", {"schema_version": 6, "project": "test", "roots": ["TEST.parent"]})
        write_yaml(dag / "REDIRECTS.yaml", {"redirects": {}})
        proof_dag_v6.write_generated(problem, "test")
        return problem

    def validate(self, root: Path, problem: Path) -> list[str]:
        return proof_dag_v6.validate_problem(root, problem, "test")[0]

    def test_valid_fixture_passes_production_validator(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(self.validate(root, self.make_problem(root)), [])

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


class PublicReleaseIntegrationTests(unittest.TestCase):
    def test_broad_reference_excludes_manuscripts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            destination = root / "public"
            (source / "research/ksum/paper").mkdir(parents=True)
            (source / "research/ksum/notes").mkdir(parents=True)
            (source / "research/ksum/paper/main.tex").write_text("private version", encoding="utf-8")
            paper = destination / "research/ksum/paper/main.tex"
            (source / "research/ksum/notes/evidence.md").write_text("evidence", encoding="utf-8")
            old_source = build_public_release.SOURCE
            build_public_release.SOURCE = source
            try:
                build_public_release.copy_reference(Path("research/ksum"), destination, [])
            finally:
                build_public_release.SOURCE = old_source
            self.assertFalse(paper.exists())
            self.assertTrue((destination / "research/ksum/notes/evidence.md").is_file())

    def test_redactor_handles_spaces_bomless_unicode_and_identifiers(self) -> None:
        private = (
            "/" + "Users/alice/My Project/secret.txt "
            + "f4ab3248-5f45-4ef5-" + "b6f7-2b1658baf158 " + "yuq" + "ingli Pro"
        )
        for encoding in ("utf-8", "utf-16-le", "utf-32-le"):
            redacted, changed = build_public_release.redact_text(private.encode(encoding))
            self.assertTrue(changed, encoding)
            decoded = build_public_release.decode_text(redacted)
            self.assertIsNotNone(decoded)
            self.assertNotIn("alice", decoded[0])
            self.assertNotIn("My Project", decoded[0])
            self.assertNotIn("f4ab3248", decoded[0])
            self.assertNotIn("yuq" + "ingli", decoded[0])

    def test_public_verifier_scans_snapshot_tree_in_main(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            snapshot = root / "provenance/git-snapshots/deadbee/research/x.yaml"
            snapshot.parent.mkdir(parents=True)
            snapshot.write_text("author: " + "yuq" + "ingli Pro\n", encoding="utf-8")
            ledger = root / "provenance/git-snapshots/SHA256SUMS"
            ledger.write_text(
                hashlib.sha256(snapshot.read_bytes()).hexdigest()
                + "  provenance/git-snapshots/deadbee/research/x.yaml\n", encoding="utf-8"
            )
            (root / "provenance/EXPORT_REDACTIONS.tsv").write_text(
                "path\tprivate_sha256\tpublic_sha256\n", encoding="utf-8"
            )
            (root / "provenance/REDACTIONS.md").write_text("current\n", encoding="utf-8")
            manifest = root / "PUBLIC_MANIFEST.sha256"
            rows = [
                f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(root).as_posix()}"
                for path in sorted(root.rglob("*")) if path.is_file() and path != manifest
            ]
            manifest.write_text("\n".join(rows) + "\n", encoding="utf-8")
            old = verify_public_release.ROOT, verify_public_release.SNAPSHOTS, verify_public_release.MANIFEST
            verify_public_release.ROOT = root
            verify_public_release.SNAPSHOTS = root / "provenance/git-snapshots"
            verify_public_release.MANIFEST = manifest
            try:
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(verify_public_release.main(), 1)
            finally:
                verify_public_release.ROOT, verify_public_release.SNAPSHOTS, verify_public_release.MANIFEST = old


if __name__ == "__main__":
    unittest.main()
