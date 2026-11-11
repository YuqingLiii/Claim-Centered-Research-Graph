#!/usr/bin/env python3
"""Independent binding, manifest, DIMACS, allowlist, and freshness audit."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import os
import re


EXPECTED = {
    "operations/circdist/SCHEDULER.yaml": "89767aecd57e32608cc75010c26a5d415af3330964c42e572aefed86796c259b",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "3fe41bc65891f94f65be55931c40f37cf3bbb3c5bdb7cca9cfa70a73489526ae",
    "circdist/reviews/circdist_gross_iter187_invariant_continuation_round104_exact_review_round105_20260901.md": "01d14be78fc75362c16340b4ba32df783a645084a819fc18a96f432d9a45e932",
}
OLD = "circdist/artifacts/circdist_gross_iter187_invariant_continuation_round104_20260901"
MANIFEST_SHA = "410807a787005a0fb5ebb1753f8b75712c798d9a15e9101f1265d0be25206ebb"
QUOTIENT_SHA = "29b16602aa5cdf0e4207271cb50045454ea0aba9254396d732414459a4029215"
BASE_SHA = "051dbece97d9cd94a69de7bff644dbb31b35076d0c43558b5408d9f3cc86b257"
Q_ALLOW = {"independent_check.json", "metadata.json", "outer.cnf",
           "translation_roots.jsonl", "translation_trace.json.gz"}
B_ALLOW = {"assertion_map.jsonl", "definitions.json.gz", "encoding_check.json",
           "metadata.json", "outer.cnf"}
FORBIDDEN = re.compile(r"(?:^|[._-])(solver|model|assignment|proof|drat|lrat|stdout|stderr|log)(?:$|[._-])", re.I)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


def dimacs(path):
    variables = clauses_expected = clauses = 0
    terminated = True
    with Path(path).open("rb") as f:
        for raw in f:
            if not raw or raw.startswith(b"c") or raw.strip() == b"":
                continue
            if raw.startswith(b"p"):
                fields = raw.split()
                assert fields[:2] == [b"p", b"cnf"] and len(fields) == 4
                variables, clauses_expected = map(int, fields[2:])
                continue
            fields = raw.split()
            assert fields and fields[-1] == b"0"
            assert all(0 < abs(int(x)) <= variables for x in fields[:-1])
            clauses += 1
    assert variables and clauses == clauses_expected
    return {"variables": variables, "clauses": clauses, "all_lines_zero_terminated": terminated}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repository", type=Path, required=True)
    ap.add_argument("--package", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    repo, package = args.repository.resolve(), args.package.resolve()
    observed = {}
    for rel, digest in EXPECTED.items():
        got = sha(repo / rel)
        assert got == digest
        observed[rel] = {"sha256": got, "bytes": (repo / rel).stat().st_size}
    old = repo / OLD
    manifest = old / "SHA256SUMS.txt"
    assert sha(manifest) == MANIFEST_SHA
    rows = []
    seen = set()
    for number, line in enumerate(manifest.read_text().splitlines(), 1):
        digest, rel = line.split("  ", 1)
        assert re.fullmatch(r"[0-9a-f]{64}", digest) and rel not in seen
        seen.add(rel)
        target = old / rel
        assert target.is_file() and not target.is_symlink() and sha(target) == digest
        rows.append({"line": number, "path": rel, "sha256": digest, "bytes": target.stat().st_size})

    qdir = package / "inputs/round104/frontier/iter188_full_invariant_quotient"
    bdir = package / "inputs/round104/frontier/iter188_full_invariant/formula"
    qfiles = {p.name for p in qdir.iterdir() if p.is_file()}
    bfiles = {p.name for p in bdir.iterdir() if p.is_file()}
    assert qfiles == Q_ALLOW and bfiles == B_ALLOW
    copied = {}
    for rel in [
        "frontier/iter188_full_invariant/source.json.gz",
        "frontier/iter188_full_invariant/state.json",
        "frontier/iter188_full_invariant/orbit_audit.json",
        *[f"frontier/iter188_full_invariant/formula/{x}" for x in sorted(B_ALLOW)],
        *[f"frontier/iter188_full_invariant_quotient/{x}" for x in sorted(Q_ALLOW)],
    ]:
        dst = package / "inputs/round104" / rel
        src = old / rel
        assert sha(dst) == sha(src)
        copied[rel] = sha(dst)
    qcnf, bcnf = qdir / "outer.cnf", bdir / "outer.cnf"
    assert sha(qcnf) == QUOTIENT_SHA and sha(bcnf) == BASE_SHA
    qdimacs, bdimacs = dimacs(qcnf), dimacs(bcnf)
    assert qdimacs == {"variables": 2455196, "clauses": 11798572, "all_lines_zero_terminated": True}
    assert bdimacs == {"variables": 1841756, "clauses": 6890981, "all_lines_zero_terminated": True}
    state = json.loads((package / "inputs/round104/frontier/iter188_full_invariant/state.json").read_text())
    assert state["next_iteration"] == 188 and state["started"] is False and state["stop"] is None
    assert state["block_count"] == 517140 and state["selector_count"] == 24156
    source = json.loads(gzip.decompress((package / "inputs/round104/frontier/iter188_full_invariant/source.json.gz").read_bytes()))
    assert len(source["blocks"]) == 517140 and len(source["selectors"]) == 24156
    assert source["semantic_payload_sha256"] == state["source_semantic_payload_sha256"]
    all_frontier_files = [p for p in (package / "inputs/round104/frontier").rglob("*") if p.is_file()]
    forbidden = [p.relative_to(package).as_posix() for p in all_frontier_files if FORBIDDEN.search(p.name)]
    # metadata is allowed to contain the word solver in values; only artifact names are prohibited.
    assert forbidden == []
    scheduler = (repo / "operations/circdist/SCHEDULER.yaml").read_text()
    assert "round 106 authorized and pending" in scheduler
    assert "Budget remains 131/132" in scheduler
    gross = (repo / "circdist/proof-dag/nodes/CIRCDIST.gross.yaml").read_text()
    assert gross.count("level: CONJECTURED") >= 2
    assert "D*_Gross in {11,12}" in gross
    result = {
        "schema": "circdist-gross-round106-input-audit-v1", "status": "PASS",
        "repository": str(repo), "package": str(package), "canonical_bindings": observed,
        "reviewed_package": {"path": OLD, "manifest_sha256": MANIFEST_SHA,
                             "manifest_rows": len(rows), "all_rows_verified": True},
        "copied_input_files": copied,
        "frontier": {"iteration": 188, "started": False, "stop": None,
                     "blocks": 517140, "selectors": 24156,
                     "translation_group": "Z_12 x Z_6", "translation_group_order": 72,
                     "lex_leaders": 71, "quotient_allowlist": sorted(Q_ALLOW),
                     "base_formula_allowlist": sorted(B_ALLOW),
                     "forbidden_artifact_names": forbidden,
                     "quotient": {**qdimacs, "sha256": QUOTIENT_SHA},
                     "base": {**bdimacs, "sha256": BASE_SHA}},
        "canonical_state_modified": False, "fresh_unstarted": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "manifest_rows": len(rows),
                      "quotient": qdimacs, "base": bdimacs,
                      "forbidden_artifact_names": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
