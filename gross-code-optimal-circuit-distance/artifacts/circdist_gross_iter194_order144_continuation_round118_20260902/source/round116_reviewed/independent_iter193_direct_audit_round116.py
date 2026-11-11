#!/usr/bin/env python3
"""Independent stdlib audit of the iteration-193 schedule and direct SAT witnesses.

This intentionally imports none of the frozen Gross model/build/replay modules.  It
reconstructs the Z_12 x Z_6 incidence geometry, all 720 direct columns, both CNFs,
and the physical hook suffixes from the public constants and retained files.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

L, M, G, N = 12, 6, 72, 144
A = ((3, 0), (0, 1), (0, 2))
B = ((0, 3), (1, 0), (2, 0))
RES_POS = ((0, 1), (3, 4, 5), (4, 5))
PHYS_POS = ((2, 3, 4, 5), (3, 4, 5), (4, 5))


def canonical_sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def gi(i, j):
    return (i % L) * M + (j % M)


def add(g, delta):
    i, j = divmod(g, M)
    return gi(i + delta[0], j + delta[1])


def edge(kind, check, q):
    return f"{kind}:{check}:{q}"


def mask(items):
    out = 0
    for q in items:
        out |= 1 << int(q)
    return out


def bits(value):
    return [q for q in range(N) if (value >> q) & 1]


def parity(a, b):
    return bin(a & b).count("1") & 1


def rref(rows, width=N):
    rows = [int(x) for x in rows if x]
    pivots = []
    r = 0
    for c in range(width - 1, -1, -1):
        pivot = next((k for k in range(r, len(rows)) if (rows[k] >> c) & 1), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        for k in range(len(rows)):
            if k != r and ((rows[k] >> c) & 1):
                rows[k] ^= rows[r]
        pivots.append(c)
        r += 1
        if r == len(rows):
            break
    return rows[:r], pivots


def rank(rows, width=N):
    return len(rref(rows, width)[0])


def inspan(value, rows, width=N):
    rr, pivots = rref(rows, width)
    for row, pivot in zip(rr, pivots):
        if (value >> pivot) & 1:
            value ^= row
    return value == 0


XSLOTS = [[add(g, a) for a in A] + [G + add(g, b) for b in B] for g in range(G)]
ZSLOTS = [[add(g, (-b[0], -b[1])) for b in B] +
          [G + add(g, (-a[0], -a[1])) for a in A] for g in range(G)]
XCHECKS = [sorted(row) for row in XSLOTS]
ZCHECKS = [sorted(row) for row in ZSLOTS]
HX = [mask(row) for row in XCHECKS]
HZ = [mask(row) for row in ZCHECKS]


def incidence(checks):
    result = [[] for _ in range(N)]
    for check, row in enumerate(checks):
        for q in row:
            result[q].append(check)
    return result


XOF, ZOF = incidence(XCHECKS), incidence(ZCHECKS)


def parse_assignment(path, nvars):
    values = {}
    for line in Path(path).read_text().splitlines():
        if not line.startswith("v "):
            continue
        for value in map(int, line[2:].split()):
            if value:
                assert abs(value) not in values
                values[abs(value)] = value > 0
    assert set(values) == set(range(1, nvars + 1))
    return values


def parse_cnf(path):
    nvars = declared = None
    clauses = []
    for raw in Path(path).read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("c"):
            continue
        if line.startswith("p "):
            _, fmt, nv, nc = line.split()
            assert fmt == "cnf"
            nvars, declared = int(nv), int(nc)
            continue
        row = list(map(int, line.split()))
        assert row and row[-1] == 0 and 0 not in row[:-1]
        clauses.append(row[:-1])
    assert nvars is not None and len(clauses) == declared
    assert max(abs(x) for row in clauses for x in row) <= nvars
    return nvars, clauses


def failed_clauses(clauses, assignment):
    return [i for i, row in enumerate(clauses, 1)
            if not any(assignment[abs(lit)] == (lit > 0) for lit in row)]


def audit_schedule(times):
    expected = {edge(kind, c, q)
                for kind, checks in (("X", XCHECKS), ("Z", ZCHECKS))
                for c, row in enumerate(checks) for q in row}
    assert len(expected) == 864 and set(times) == expected
    assert all(type(t) is int and t >= 0 for t in times.values())
    used = sorted(set(times.values()))
    assert used == list(range(len(used)))
    occupied = {}
    conflicts = []
    for name, t in times.items():
        kind, c, q = name.split(":")
        for node in ((kind, int(c)), ("D", int(q))):
            if (node, t) in occupied:
                conflicts.append((occupied[(node, t)], name, t))
            occupied[(node, t)] = name
    assert not conflicts
    overlaps = []
    mc_bad = []
    pair_interleaved = whole_interleaved = 0
    for x, xr in enumerate(XCHECKS):
        for z, zr in enumerate(ZCHECKS):
            shared = sorted(set(xr) & set(zr))
            if not shared:
                continue
            assert len(shared) == 2
            overlaps.append((x, z, shared))
            orientations = [times[edge("Z", z, q)] < times[edge("X", x, q)] for q in shared]
            if orientations[0] != orientations[1]:
                mc_bad.append((x, z, shared, orientations))
            xt = [times[edge("X", x, q)] for q in shared]
            zt = [times[edge("Z", z, q)] for q in shared]
            pair_interleaved += int(not (max(xt) < min(zt) or max(zt) < min(xt)))
            xt = [times[edge("X", x, q)] for q in xr]
            zt = [times[edge("Z", z, q)] for q in zr]
            whole_interleaved += int(not (max(xt) < min(zt) or max(zt) < min(xt)))
    assert len(overlaps) == 648 and not mc_bad
    xv = [t for name, t in times.items() if name.startswith("X:")]
    zv = [t for name, t in times.items() if name.startswith("Z:")]
    global_interleaved = not (max(xv) < min(zv) or max(zv) < min(xv))
    assert global_interleaved
    return {"ok": True, "edge_count": 864, "used_layers": len(used),
            "min_time": used[0], "max_time": used[-1], "conflicts": 0,
            "overlaps": len(overlaps), "mc_violations": 0,
            "global_interleaved": True,
            "overlap_interleaved_pairs": pair_interleaved,
            "whole_check_interleaved_pairs": whole_interleaved}


def public_column(index, name, kind, check, residual_kind, support, physical, syndrome, u_options):
    return {"index": index, "primary_var": index + 1, "name": name, "kind": kind,
            "check": check, "residual_kind": residual_kind,
            "support": bits(support), "support_mask_hex": hex(support),
            "physical_support": bits(physical),
            "syndrome": bits(syndrome), "syndrome_mask_hex": hex(syndrome),
            "u_options": [{"bits": bits(u), "mask_hex": hex(u)} for u in u_options]}


def reconstruct_sector(label, times):
    if label == "Xerr":
        hook, detector, det_of, stabilizers, hk, dk = XCHECKS, ZCHECKS, ZOF, HX, "X", "Z"
    else:
        hook, detector, det_of, stabilizers, hk, dk = ZCHECKS, XCHECKS, XOF, HZ, "Z", "X"
    detrows = [mask(row) for row in detector]

    def syndrome(support):
        return sum((parity(support, row) << i) for i, row in enumerate(detrows))

    orders = [sorted(row, key=lambda q, a=a: times[edge(hk, a, q)])
              for a, row in enumerate(hook)]
    columns = []
    for q in range(N):
        support = 1 << q
        qorder = sorted(det_of[q], key=lambda b: times[edge(dk, b, q)])
        options, value = [0], 0
        for b in reversed(qorder):
            value |= 1 << b
            options.append(value)
        columns.append(public_column(len(columns), f"D:{q}", "data", None, None,
                                     support, support, syndrome(support), options))
    for a, order in enumerate(orders):
        assert len(order) == 6 and len(set(times[edge(hk, a, q)] for q in order)) == 6
        for k, positions in enumerate(RES_POS):
            support = mask(order[p] for p in positions)
            physical = mask(order[p] for p in PHYS_POS[k])
            assert syndrome(support) == syndrome(physical)
            u = 0
            for q in bits(physical):
                for b in det_of[q]:
                    if times[edge(dk, b, q)] > times[edge(hk, a, q)]:
                        u ^= 1 << b
            columns.append(public_column(len(columns), f"R:{a}:{k}", "residual", a, k,
                                         support, physical, syndrome(support), (u,)))
    assert len(columns) == 360
    return {"columns": columns, "orders": orders, "detrows": detrows,
            "stabilizers": stabilizers, "syndrome": syndrome, "hook_kind": hk}


def check_sector(root, label, times, independent):
    direct = root / "output/iter193/direct"
    prefix = direct / "direct360" / label
    cold = json.loads(prefix.with_suffix(".columns.json").read_text())
    vard = json.loads(prefix.with_suffix(".variables.json").read_text())
    summary = json.loads(prefix.with_suffix(".summary.json").read_text())
    rebuilt = reconstruct_sector(label, times)
    assert cold["sector"] == label and cold["column_count"] == 360
    assert cold["columns"] == rebuilt["columns"]
    expected_det = [{"row": i, "support": bits(row), "mask_hex": hex(row)}
                    for i, row in enumerate(rebuilt["detrows"])]
    expected_stab = [{"row": i, "support": bits(row), "mask_hex": hex(row)}
                     for i, row in enumerate(rebuilt["stabilizers"])]
    assert cold["detector_rows"] == expected_det
    assert cold["stabilizer_rows"] == expected_stab
    logical_duals = [mask(row["support"]) for row in cold["logical_duals"]]
    assert len(logical_duals) == 12 and all(bin(x).count("1") == 12 for x in logical_duals)
    for b in range(G):
        indices = [c["index"] for c in rebuilt["columns"] if b in c["syndrome"]]
        row = cold["syndrome_equations"][b]
        assert row["row"] == b and row["column_indices"] == indices
        assert row["literals"] == [i + 1 for i in indices]
    for r, logical in enumerate(logical_duals):
        indices = [c["index"] for c in rebuilt["columns"]
                   if parity(mask(c["support"]), logical)]
        row = cold["logical_equations"][r]
        assert row["row"] == r and row["logical_dual_support"] == bits(logical)
        assert row["logical_dual_mask_hex"] == hex(logical)
        assert row["column_indices"] == indices and row["literals"] == [i + 1 for i in indices]
    nvars, clauses = parse_cnf(prefix.with_suffix(".cnf"))
    assert nvars == summary["variables"] == vard["variable_count"]
    assert len(clauses) == summary["clauses"]
    assert file_sha(prefix.with_suffix(".cnf")) == summary["dimacs_sha256"]
    assert summary["complete_query"] and summary["primary_selection_variables"] == 360
    assert summary["W"] == 10 and summary["excluded_restrictions"] == [
        "no pool restriction", "no residual-pattern restriction",
        "no check-count restriction", "no within-check order family restriction"]
    assert [v["id"] for v in vard["variables"]] == list(range(1, nvars + 1))
    for i in range(360):
        v = vard["variables"][i]
        assert v["id"] == i + 1 and v["role"] == "direct_column_selection"
        assert v["context"] == {"column_index": i, "column_name": rebuilt["columns"][i]["name"]}
    dictionary = [json.loads(line) for line in prefix.with_suffix(".clauses.jsonl").read_text().splitlines()]
    assert [row["id"] for row in dictionary] == list(range(1, len(clauses) + 1))
    assert [row["lits"] for row in dictionary] == clauses
    assignment_path = direct / "solver" / f"{label}.assignment.dimacs"
    assignment = parse_assignment(assignment_path, nvars)
    failed = failed_clauses(clauses, assignment)
    assert not failed
    selected = [i for i in range(360) if assignment[i + 1]]
    assert len(selected) == 10
    canonical = physical = 0
    for i in selected:
        canonical ^= mask(rebuilt["columns"][i]["support"])
        physical ^= mask(rebuilt["columns"][i]["physical_support"])
    can_syn, phy_syn = rebuilt["syndrome"](canonical), rebuilt["syndrome"](physical)
    can_par = [parity(canonical, logical) for logical in logical_duals]
    phy_par = [parity(physical, logical) for logical in logical_duals]
    assert can_syn == phy_syn == 0 and can_par == phy_par and any(can_par)
    assert not inspan(canonical, rebuilt["stabilizers"])
    assert not inspan(physical, rebuilt["stabilizers"])
    recorded = independent["sectors"][label]["mechanism"]
    assert recorded["selected_indices"] == selected
    assert recorded["selected_names"] == [rebuilt["columns"][i]["name"] for i in selected]
    assert recorded["canonical_replay"]["net_support"] == bits(canonical)
    assert recorded["physical_net_support"] == bits(physical)
    assert recorded["canonical_replay"]["logical_parities"] == can_par
    assert recorded["physical_logical_parities"] == phy_par
    flipped = dict(assignment)
    flipped[selected[0] + 1] = False
    flip_failures = failed_clauses(clauses, flipped)
    assert flip_failures
    return {"status": "SATISFIABLE", "variables": nvars, "clauses": len(clauses),
            "cnf_sha256": file_sha(prefix.with_suffix(".cnf")),
            "assignment_sha256": file_sha(assignment_path),
            "all_clauses_checked": len(clauses), "all_clauses_satisfied": True,
            "all_columns_reconstructed": 360, "syndrome_rows_reconstructed": 72,
            "logical_rows_reconstructed": 12, "selected_indices": selected,
            "selected_names": [rebuilt["columns"][i]["name"] for i in selected],
            "fault_count": 10, "canonical_net_support": bits(canonical),
            "physical_net_support": bits(physical), "canonical_syndrome": bits(can_syn),
            "physical_syndrome": bits(phy_syn), "logical_parities": can_par,
            "canonical_physical_parities_equal": True,
            "canonical_nonstabilizer": True, "physical_nonstabilizer": True,
            "negative_control": {"flip_selected_var": selected[0] + 1,
                                 "failed_clause_count": len(flip_failures),
                                 "first_failed_clause": flip_failures[0]}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    root = args.root.resolve()
    candidate = json.loads((root / "output/iter193/solver/candidate.json").read_text())
    times = {str(k): int(v) for k, v in candidate["compressed_times"].items()}
    assert canonical_sha(times) == candidate["compressed_schedule_sha256"]
    schedule = audit_schedule(times)
    frozen = candidate["frozen_audit"]
    for key in ("edge_count", "used_layers", "min_time", "max_time", "overlaps",
                "global_interleaved", "overlap_interleaved_pairs", "whole_check_interleaved_pairs"):
        assert schedule[key] == frozen[key]
    assert frozen["ok"] and not frozen["errors"] and not frozen["conflicts"] and not frozen["mc_violations"]
    recorded = json.loads((root / "output/iter193/direct/direct_verification.json").read_text())
    reconstructed = {label: reconstruct_sector(label, times) for label in ("Xerr", "Zerr")}
    x_duals = [mask(x["support"]) for x in json.loads(
        (root / "output/iter193/direct/direct360/Zerr.columns.json").read_text())["logical_duals"]]
    z_duals = [mask(x["support"]) for x in json.loads(
        (root / "output/iter193/direct/direct360/Xerr.columns.json").read_text())["logical_duals"]]
    assert rank(HX) == rank(HZ) == 66
    assert all(parity(x, z) == 0 for x in HX for z in HZ)
    assert rank(HX + x_duals) == rank(HZ + z_duals) == 78
    pairing = [sum(parity(x, z) << j for j, z in enumerate(z_duals)) for x in x_duals]
    assert rank(pairing, 12) == 12
    sectors = {label: check_sector(root, label, times, recorded) for label in ("Xerr", "Zerr")}
    result = {
        "schema": "circdist-gross-round116-independent-iter193-direct-audit-v1",
        "status": "PASS", "implementation_independence": {
            "language": "Python standard library only",
            "frozen_model_modules_imported": [],
            "reconstruction": "incidence, schedule constraints, 720 columns, CNF assignments, physical hooks"},
        "geometry": {"L": L, "M": M, "data_qubits": N, "checks_per_sector": G,
                     "check_weight": 6, "stabilizer_rank_per_sector": 66,
                     "logical_dimension": 12, "cross_pairing_rank": 12},
        "schedule_sha256": canonical_sha(times), "schedule": schedule,
        "sectors": sectors,
        "scientific_conclusion": "Both unrestricted complete direct sectors contain a checked weight-10 nontrivial undetected physical mechanism; this candidate cannot certify distance 12 and repair is forbidden."}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "schedule_sha256": result["schedule_sha256"],
                      "sectors": {k: {"status": v["status"], "fault_count": v["fault_count"],
                                      "physical_net_support": v["physical_net_support"]}
                                  for k, v in sectors.items()}}, sort_keys=True))


if __name__ == "__main__":
    main()
