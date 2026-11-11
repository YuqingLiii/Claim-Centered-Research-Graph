#!/usr/bin/env python3
"""Verify commissioned bindings and materialize the fresh iteration-148 formula."""
from pathlib import Path, PurePosixPath
from collections import Counter
import argparse, gzip, hashlib, json


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def verify_manifest(root, name):
    rows = []
    for line in (root / name).read_text().splitlines():
        digest, sep, rel = line.partition("  ")
        q = PurePosixPath(rel)
        assert sep == "  " and len(digest) == 64
        assert not q.is_absolute() and ".." not in q.parts and q.as_posix() == rel
        rows.append((rel, digest))
    assert rows == sorted(rows) and len(rows) == len({r for r, _ in rows})
    for rel, digest in rows:
        path = root / rel
        assert path.is_file() and sha(path) == digest, (name, rel)
    return {r for r, _ in rows}


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--repository", type=Path, required=True)
a = ap.parse_args()
P = a.root.resolve()
R = a.repository.resolve()
old = R / "circdist/artifacts/circdist_gross_proof_outer_round94_20260830"

expected = {
    "operations/circdist/SCHEDULER.yaml": "3c8965b3cc30f6ebcdc5f051073f2c0eb0dc39d537cd9f3f171633d6eac7bab1",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "f84492190a1dad3b5d69bf38a9a62d3212f0c3844ee3338dc96517fbb0671135",
    "circdist/reviews/circdist_gross_proof_outer_round94_exact_review_round95_20260830.md": "b6a23911b5f9974454a4f4291eaa09e30308547925aa71972d5199e3715c9450",
    "circdist/artifacts/circdist_gross_proof_outer_round94_20260830/SHA256SUMS.txt": "1e0a4af8591aa63ccccd1b2516c630eccb11a73fb9dea2e0ff1e0d32ed82ac1c",
    "circdist/artifacts/circdist_gross_proof_outer_round94_20260830/PAYLOAD_SHA256SUMS.txt": "c39ef3552e461dd7513812b8296901e72369dfacbf6e71ae758b5bb58ed94c54",
}
snapshots = {
    "operations/circdist/SCHEDULER.yaml": "bindings/operations__circdist__SCHEDULER.yaml",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "bindings/circdist__proof-dag__nodes__CIRCDIST.gross.yaml",
    "circdist/reviews/circdist_gross_proof_outer_round94_exact_review_round95_20260830.md": "bindings/circdist__reviews__circdist_gross_proof_outer_round94_exact_review_round95_20260830.md",
    "circdist/artifacts/circdist_gross_proof_outer_round94_20260830/SHA256SUMS.txt": "bindings/circdist__artifacts__circdist_gross_proof_outer_round94_20260830__SHA256SUMS.txt",
    "circdist/artifacts/circdist_gross_proof_outer_round94_20260830/PAYLOAD_SHA256SUMS.txt": "bindings/circdist__artifacts__circdist_gross_proof_outer_round94_20260830__PAYLOAD_SHA256SUMS.txt",
}
binding_rows = []
for rel, digest in expected.items():
    assert sha(R / rel) == digest
    assert sha(P / snapshots[rel]) == digest
    binding_rows.append({"path": rel, "sha256": digest, "snapshot": snapshots[rel]})

root_rows = verify_manifest(old, "SHA256SUMS.txt")
payload_rows = verify_manifest(old, "PAYLOAD_SHA256SUMS.txt")
actual = {p.relative_to(old).as_posix() for p in old.rglob("*") if p.is_file()}
assert root_rows == actual - {"SHA256SUMS.txt"}
assert payload_rows == actual - {"SHA256SUMS.txt", "PAYLOAD_SHA256SUMS.txt"}
assert root_rows == payload_rows | {"PAYLOAD_SHA256SUMS.txt"}

F = P / "formulas/iter148"
state_path = P / "state/iter148_state.json"
state = json.loads(state_path.read_text())
source = json.loads(gzip.decompress((F / "source.json.gz").read_bytes()))
recorded_semantic = source.pop("semantic_payload_sha256")
assert hashlib.sha256(canonical(source)).hexdigest() == recorded_semantic
source["semantic_payload_sha256"] = recorded_semantic
state_keys = ("mechanism_id", "sector", "selected_names", "data_support", "group_kinds", "selector_semantic_sha256")
state_semantic = hashlib.sha256(canonical([{k: s.get(k) for k in state_keys} for s in state["selectors"]])).hexdigest()
assert state["next_iteration"] == 148 and state["started"] is False and state["stop"] is None
assert state["selector_count"] == len(state["selectors"]) == len(source["selectors"]) == 256
assert state_semantic == state["selector_state_sha256"] == "9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f"
assert sha(state_path) == "1902599acc47eb5d354692759b2d09d6ff1cfcd5e013f2b907cc310376ee6e81"
assert sha(F / "source.json.gz") == "0db20ed8ca0b120cda91eb7a94be25094adb9b77a2cacdd322e330a720d58b5f"
assert recorded_semantic == "2fd4a1982e1f6389804f7eee1120706f9d26c9e6a23acc05e2a15e036a67c032"
meta = json.loads((F / "metadata.json").read_text())
assert (meta["assertions"], meta["variables"], meta["clauses"]) == (19138, 409157, 1385059)
assert meta["cnf_sha256"] == "397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4"
assert Counter(x["family"] for x in source["blocks"]) == Counter({"unary": 1440, "round62": 20, "generalized": 12820, "dynamic": 204})
assert len(source["blocks"]) == 14484
raw_cnf = gzip.decompress((F / "outer.cnf.gz").read_bytes())
raw_map = gzip.decompress((F / "assertion_map.jsonl.gz").read_bytes())
assert hashlib.sha256(raw_cnf).hexdigest() == meta["cnf_sha256"]
assert hashlib.sha256(raw_map).hexdigest() == meta["assertion_map_sha256"]
assert len(raw_map.splitlines()) == 19138
(P / "reconstruction/stored.outer.cnf").write_bytes(raw_cnf)
(P / "reconstruction/stored.assertion_map.jsonl").write_bytes(raw_map)

# The reviewed package may contain compile logs for the pending formula, but no solve/disposition tree.
paths = sorted(p.relative_to(old).as_posix() for p in old.rglob("*") if p.is_file() and "iter148" in p.relative_to(old).as_posix())
assert not (old / "iterations/iter148").exists()
for rel in paths:
    low = rel.lower()
    assert not any(token in low for token in ("solver", "assignment", "model", ".drat", ".lrat", "disposition")), rel

out = {
    "schema": "circdist-round96-initial-binding-and-frontier-v1",
    "status": "PASS",
    "bindings": binding_rows,
    "reviewed_round94_manifest": {
        "root_sha256": expected["circdist/artifacts/circdist_gross_proof_outer_round94_20260830/SHA256SUMS.txt"],
        "payload_sha256": expected["circdist/artifacts/circdist_gross_proof_outer_round94_20260830/PAYLOAD_SHA256SUMS.txt"],
        "root_rows": len(root_rows), "payload_rows": len(payload_rows), "files": len(actual), "all_payload_files_verified": True,
    },
    "frontier": {
        "iteration": 148, "started": False, "stop": None, "selector_count": 256,
        "selector_state_sha256": state_semantic, "state_file_sha256": sha(state_path),
        "source_file_sha256": sha(F / "source.json.gz"), "source_semantic_sha256": recorded_semantic,
        "assertions": meta["assertions"], "variables": meta["variables"], "clauses": meta["clauses"],
        "cnf_sha256": meta["cnf_sha256"], "inherited_order_predicates": len(source["blocks"]),
        "block_family_counts": dict(sorted(Counter(x["family"] for x in source["blocks"]).items())),
        "inherited_disposition_absent": True, "iter148_reviewed_paths": paths,
    },
}
(P / "reconstruction/input_bindings.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "root_rows": len(root_rows), "payload_rows": len(payload_rows), "iter148_paths": len(paths), "cnf_sha256": meta["cnf_sha256"]}, sort_keys=True))
