#!/usr/bin/env python3
"""Round108 pre-science binding, full predecessor-seal, DIMACS, and freshness audit."""
from pathlib import Path, PurePosixPath
import argparse, gzip, hashlib, json, re

EXPECTED = {
    "operations/circdist/SCHEDULER.yaml": "13c74772427b20aaf8128633459ee995c62e60dd1b79090c458d00e9a0994343",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "8b805a806d5b704047f4ccca648c92efe11740d7c5b7825659eb1e6b7b5dc977",
    "circdist/reviews/circdist_gross_iter188_invariant_continuation_round106_exact_review_round107_20260901.md": "eda1d894cde8a56fd7eac9188ed2bb73bef4ddd7842e2fcb091435cbd759c036",
}
OLD = "circdist/artifacts/circdist_gross_iter188_invariant_quotient_continuation_round106_20260901"
MANIFEST_SHA = "0b9cc6d4074e8397062219ec8d079afbcf0388e14912ab925b5d66ac00c61c9d"
QUOTIENT_SHA = "3ece12a1ea0ee6502982fecfcaf75debae985ea2ddff93ea3b875552c0714df7"
BASE_SHA = "f5ccbe6aa4c0a0df5940cd979809003182416900e76a6cc6e3755e493cc6b178"
SOURCE_SHA = "b3bdfbe8924490da1e20230ff856515d13173966bc4170c6078b7aab9e36558b"
SEMANTIC_SHA = "e8b17eac5c55f1b1c32fb84972dcc2c52ce259c99a65200c8ed7bc046c811eb4"
STATE_SHA = "8bb97ba8ff7590f178aaff29f51da8ab6953b1fae90bcf6952546d31f59c6f97"
SELECTOR_STATE_SHA = "8e4db1fbf08e24b81995a6ac1b25f791480edebd06e560442e2ca49a5ad5cefa"
Q_ALLOW = {"independent_check.json", "metadata.json", "outer.cnf", "translation_roots.jsonl", "translation_trace.json.gz"}
B_ALLOW = {"assertion_map.jsonl", "definitions.json.gz", "encoding_check.json", "metadata.json", "outer.cnf"}
TOP_ALLOW = {"formula", "orbit_audit.json", "source.json.gz", "state.json"}
FORBIDDEN = re.compile(r"(?:^|[._-])(solver|model|assignment|proof|drat|lrat|stdout|stderr|log)(?:$|[._-])", re.I)


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(8<<20), b""): h.update(b)
    return h.hexdigest()


def dimacs(path):
    nv=declared=None; clauses=0
    with Path(path).open("rb") as f:
        for raw in f:
            line=raw.strip()
            if not line or line.startswith(b"c"): continue
            if line.startswith(b"p"):
                fields=line.split(); assert fields[:2]==[b"p",b"cnf"] and len(fields)==4
                nv,declared=map(int,fields[2:]); continue
            fields=line.split(); assert fields and fields[-1]==b"0"
            assert all(0 < abs(int(x)) <= nv for x in fields[:-1]); clauses += 1
    assert nv and clauses==declared
    return {"variables":nv,"clauses":clauses,"all_lines_zero_terminated":True}


def manifest_rows(root, path):
    rows=[]; seen=set()
    for number,line in enumerate(path.read_text().splitlines(),1):
        digest,sep,rel=line.partition("  "); assert sep and re.fullmatch(r"[0-9a-f]{64}",digest)
        posix=PurePosixPath(rel); assert rel==posix.as_posix() and not posix.is_absolute() and ".." not in posix.parts
        assert rel not in seen; seen.add(rel)
        target=root/rel; assert target.is_file() and not target.is_symlink(); observed=sha(target)
        assert observed==digest,(number,rel,observed,digest)
        rows.append({"line":number,"path":rel,"sha256":digest,"bytes":target.stat().st_size})
    actual={p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}
    assert set(seen)==actual-{"SHA256SUMS.txt"}
    return rows


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repository",type=Path,required=True); ap.add_argument("--package",type=Path,required=True); ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args(); repo=a.repository.resolve(); package=a.package.resolve()
    observed={}
    for rel,digest in EXPECTED.items():
        got=sha(repo/rel); assert got==digest; observed[rel]={"sha256":got,"bytes":(repo/rel).stat().st_size}
    old=repo/OLD; manifest=old/"SHA256SUMS.txt"; assert sha(manifest)==MANIFEST_SHA
    rows=manifest_rows(old,manifest); assert len(rows)==432
    rowmap={r["path"]:r["sha256"] for r in rows}
    # Exact copied input tree and file allowlists.
    qdir=package/"inputs/round106/frontier/iter189_full_invariant_quotient"
    btop=package/"inputs/round106/frontier/iter189_full_invariant"
    bdir=btop/"formula"
    assert {p.name for p in qdir.iterdir()}==Q_ALLOW
    assert {p.name for p in bdir.iterdir()}==B_ALLOW
    assert {p.name for p in btop.iterdir()}==TOP_ALLOW
    copied={}
    rels=[
      "frontier/iter189_full_invariant/source.json.gz",
      "frontier/iter189_full_invariant/state.json",
      "frontier/iter189_full_invariant/orbit_audit.json",
      *[f"frontier/iter189_full_invariant/formula/{x}" for x in sorted(B_ALLOW)],
      *[f"frontier/iter189_full_invariant_quotient/{x}" for x in sorted(Q_ALLOW)],
      "solver/iter188/candidate.json","solver/iter188/direct/direct_verification.json",
    ]
    mapping={
      "solver/iter188/candidate.json":"iter188_adjudication/candidate.json",
      "solver/iter188/direct/direct_verification.json":"iter188_adjudication/direct_verification.json",
    }
    for rel in rels:
        suffix=mapping.get(rel,rel)
        dst=package/"inputs/round106"/suffix; src=old/rel
        got=sha(dst); assert got==sha(src)==rowmap[rel]; copied[rel]={"copied_path":dst.relative_to(package).as_posix(),"sha256":got,"bytes":dst.stat().st_size}
    q=qdim=dimacs(qdir/"outer.cnf"); b=bdim=dimacs(bdir/"outer.cnf")
    assert sha(qdir/"outer.cnf")==QUOTIENT_SHA and qdim["variables"]==2460741 and qdim["clauses"]==11816927
    assert sha(bdir/"outer.cnf")==BASE_SHA and bdim["variables"]==1847301 and bdim["clauses"]==6909336
    assert sha(btop/"source.json.gz")==SOURCE_SHA and sha(btop/"state.json")==STATE_SHA
    state=json.loads((btop/"state.json").read_text()); assert state["next_iteration"]==189 and state["started"] is False and state["stop"] is None
    assert state["block_count"]==517140 and state["selector_count"]==24300 and state["selector_state_sha256"]==SELECTOR_STATE_SHA
    source=json.loads(gzip.decompress((btop/"source.json.gz").read_bytes())); assert len(source["blocks"])==517140 and len(source["selectors"])==24300
    assert source["semantic_payload_sha256"]==SEMANTIC_SHA==state["source_semantic_payload_sha256"]
    files=[p for p in (package/"inputs/round106/frontier").rglob("*") if p.is_file()]
    forbidden=[p.relative_to(package).as_posix() for p in files if FORBIDDEN.search(p.name)]; assert not forbidden
    scheduler=(repo/"operations/circdist/SCHEDULER.yaml").read_text(); assert "round 108 authorized and pending" in scheduler and "Budget remains 133/134" in scheduler
    gross=(repo/"circdist/proof-dag/nodes/CIRCDIST.gross.yaml").read_text(); assert gross.count("level: CONJECTURED")>=2 and "D*_Gross in {11,12}" in gross
    result={"schema":"circdist-gross-round108-input-audit-v1","status":"PASS","canonical_bindings":observed,
      "reviewed_package":{"path":OLD,"root_manifest_sha256":MANIFEST_SHA,"manifest_rows":len(rows),"all_rows_verified":True,"physical_files":433},
      "copied_input_files":copied,
      "frontier":{"iteration":189,"fresh_unstarted":True,"started":False,"stop":None,"blocks":517140,"selectors":24300,
       "source_sha256":SOURCE_SHA,"semantic_source_sha256":SEMANTIC_SHA,"state_sha256":STATE_SHA,"selector_state_sha256":SELECTOR_STATE_SHA,
       "translation_group":"Z_12 x Z_6","translation_group_order":72,"lex_leaders":71,
       "top_allowlist":sorted(TOP_ALLOW),"base_formula_allowlist":sorted(B_ALLOW),"quotient_allowlist":sorted(Q_ALLOW),
       "base":{**bdim,"sha256":BASE_SHA,"assertions":545838},"quotient":{**qdim,"sha256":QUOTIENT_SHA,"assertions":545909},
       "forbidden_artifact_names":forbidden},"canonical_state_modified":False}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":"PASS","manifest_rows":len(rows),"base":bdim,"quotient":qdim,"forbidden":0},sort_keys=True))
if __name__=="__main__": main()
