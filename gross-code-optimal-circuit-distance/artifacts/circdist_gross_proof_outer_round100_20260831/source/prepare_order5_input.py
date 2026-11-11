#!/usr/bin/env python3
"""Build exact fixed-width order-5 rows from the reviewed post-i136 selector basis."""
from pathlib import Path
import argparse, hashlib, json, struct, sys

def canon(o): return json.dumps(o, sort_keys=True, separators=(",", ":")).encode()
def objsha(o): return hashlib.sha256(canon(o)).hexdigest()
def filesha(p):
    h = hashlib.sha256()
    with Path(p).open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
def words(v, n): return [(v >> (64*i)) & ((1 << 64)-1) for i in range(n)]
def parity_mask(support, duals, popcount):
    out = 0
    for i, d in enumerate(duals): out |= ((popcount(support & d) & 1) << i)
    return out

ap = argparse.ArgumentParser()
ap.add_argument("--state", type=Path, required=True)
ap.add_argument("--candidate", type=Path, required=True)
ap.add_argument("--direct", type=Path, required=True)
ap.add_argument("--vendor", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
expected = {
    "state": "ba670045a69722f9625d04d3f07d62e207db38f15e9323f8c32d89194bb585cd",
    "candidate": "9596d1456ea66c086c06b4b7b4aaf4e442da9943644ae9839d113f10d937a640",
    "direct": "f206cb75b7af6cbf2c5421f58c9ebc0c1c0b51d7e44eb3f1c5713a47987a485e",
}
assert filesha(a.state) == expected["state"]
assert filesha(a.candidate) == expected["candidate"]
assert filesha(a.direct) == expected["direct"]
state = json.loads(a.state.read_text())
cand = json.loads(a.candidate.read_text())
assert state["next_iteration"] == 137 and state["started"] is False and state["stop"] is None
assert state["selector_count"] == len(state["selectors"]) == 234
keys = ("mechanism_id", "sector", "selected_names", "data_support", "group_kinds", "selector_semantic_sha256")
assert objsha([{k:s.get(k) for k in keys} for s in state["selectors"]]) == state["selector_state_sha256"] == "47792a8f8e757482604723abb0e08916f49b252f4ba07deae03cf4295159d0b6"
sys.path[:0] = [str(a.vendor / "src/round63_src"), str(a.vendor / "src")]
import model
import round68_build as builder
_, _, lx, lz = builder.load_context()
times = {k:int(v) for k,v in cand["compressed_times"].items()}
assert objsha(times) == cand["compressed_schedule_sha256"] == "45051af0b08e6647d50c6fb0535894173016fd013279e7a0eaee8b2e69ee2e44"
assert model.audit_schedule(times, True) == cand["frozen_audit"] and cand["frozen_audit"]["ok"]
sectors = builder.sectors(times, lx, lz)
names = sorted(c.name for c in sectors["Xerr"].columns)
assert len(names) == len(set(names)) == 360
assert set(names) == set(c.name for c in sectors["Zerr"].columns)
name_bit = {n:i for i,n in enumerate(names)}
out = a.output
out.mkdir(parents=True, exist_ok=True)
(out / "name_universe.json").write_text(json.dumps(names, indent=2) + "\n")
results = {}
for label in ("Xerr", "Zerr"):
    sec = sectors[label]
    byname = {c.name:c for c in sec.columns}
    rows = []
    for gi, s in enumerate(state["selectors"]):
        if s["sector"] != label: continue
        selected = s["selected_names"]
        assert len(selected) == len(set(selected))
        nm = sum(1 << name_bit[n] for n in selected)
        can = phys = 0
        for n in selected:
            can ^= byname[n].support
            phys ^= byname[n].physical_support
        csyn = sec.syndrome_of(can)
        psyn = sec.syndrome_of(phys)
        clog = parity_mask(can, sec.logical_duals, model.popcount)
        plog = parity_mask(phys, sec.logical_duals, model.popcount)
        vals = [gi] + words(nm,6) + words(can,3) + words(phys,3) + words(csyn,2) + words(psyn,2) + [clog,plog]
        assert len(vals) == 19
        rows.append((s["mechanism_id"], vals))
    assert len(rows) == {"Xerr":125,"Zerr":109}[label]
    b = b"CDR98O5V1\0\0\0\0\0\0\0" + struct.pack("<Q", len(rows)) + b"".join(struct.pack("<19Q", *vals) for _,vals in rows)
    path = out / f"{label}.rows.bin"
    path.write_bytes(b)
    ids = [x for x,_ in rows]
    (out / f"{label}.ids.json").write_text(json.dumps(ids, indent=2) + "\n")
    results[label] = {"rows":len(rows), "row_file":path.name, "row_file_sha256":filesha(path), "row_bytes":len(b), "ids_file_sha256":filesha(out / f"{label}.ids.json")}
meta = {
    "schema":"circdist-round98-order5-fixed-row-input-v1", "status":"PASS",
    "state_file_sha256":filesha(a.state), "selector_state_sha256":state["selector_state_sha256"],
    "candidate_file_sha256":filesha(a.candidate), "source_schedule_sha256":cand["compressed_schedule_sha256"],
    "direct_file_sha256":filesha(a.direct), "name_universe_sha256":filesha(out / "name_universe.json"),
    "sectors":results,
    "layout":"16-byte magic, uint64 row count, then per row 19 little-endian uint64: global index; names[6]; canonical[3]; physical[3]; canonical syndrome[2]; physical syndrome[2]; canonical logical; physical logical",
    "all_effects_recomputed_from_frozen_physical_model":True,
}
(out / "input_metadata.json").write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
print(json.dumps(meta, sort_keys=True))
