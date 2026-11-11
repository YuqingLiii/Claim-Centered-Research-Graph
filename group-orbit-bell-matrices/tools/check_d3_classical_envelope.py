#!/usr/bin/env python3
"""Exhaustive exact D3 classical envelope, Python standard library only.

Run from the repository root:
    python3 grothendieck-group-orbit/tools/check_d3_classical_envelope.py
Optionally verify a frozen certificate by adding --check PATH.
No floating point, optimization package, or symmetry reduction is used.
"""

import argparse
from fractions import Fraction as F
from itertools import combinations, product
import json
from pathlib import Path


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def d3_roots():
    roots = []
    for i, j in combinations(range(3), 2):
        for first, second in product((-1, 1), repeat=2):
            row = [0, 0, 0]
            row[i], row[j] = first, second
            roots.append(tuple(row))
    assert len(roots) == len(set(roots)) == 12
    return tuple(roots)


def qstr(x):
    return str(F(x))


def signed_rows(at, t, lam):
    return tuple(1 if x - lam * y >= 0 else -1 for x, y in zip(at, t))


def value(at, t, lam):
    return sum(abs(x - lam * y) for x, y in zip(at, t))


def compute():
    roots = d3_roots()
    # The full 12 by 12 rational matrix is built independently of a projector
    # optimization; each enumerated vector receives its full matrix product.
    a = tuple(tuple(F(dot(u, v), 8) for v in roots) for u in roots)
    assert all(dot(tuple(w[k] for w in roots), tuple(w[l] for w in roots))
               == (8 if k == l else 0) for k in range(3) for l in range(3))
    signs = tuple(product((-1, 1), repeat=12))
    assert len(signs) == len(set(signs)) == 4096
    records = tuple((t, tuple(dot(row, t) for row in a)) for t in signs)
    left, right = F(0), F(1, 2)
    knots = {left, right}
    for t, at in records:
        for x, y in zip(at, t):
            zero = x / y
            if left <= zero <= right:
                knots.add(zero)
    row_knots = sorted(knots)
    cells = []
    interval_reports = []
    for lo, hi in zip(row_knots, row_knots[1:]):
        mid = (lo + hi) / 2
        # Deduplicate identical affine functions but retain their multiplicity,
        # and one concrete (s,t) witness for each line.
        lines = {}
        for idx, (t, at) in enumerate(records):
            s = signed_rows(at, t, mid)
            intercept, slope = dot(s, at), -dot(s, t)
            assert intercept + slope * mid == value(at, t, mid)
            key = (intercept, slope)
            if key not in lines:
                lines[key] = {"record_index": idx, "s": s, "count": 0}
            lines[key]["count"] += 1
        assert sum(item["count"] for item in lines.values()) == 4096
        # Any switch of the maximizer occurs at the crossing of two lines.
        # Include ALL crossings inside this interval, including nonmaximal ones.
        boundaries = {lo, hi}
        for (b1, m1), (b2, m2) in combinations(lines, 2):
            if m1 != m2:
                crossing = F(b2 - b1, m1 - m2)
                if lo < crossing < hi:
                    boundaries.add(crossing)
        ordered = sorted(boundaries)
        interval_reports.append({
            "lo": qstr(lo), "hi": qstr(hi),
            "distinct_lines": len(lines),
            "line_multiplicity_total": sum(item["count"] for item in lines.values()),
            "lines": [{"intercept": qstr(b), "slope": qstr(m),
                       "multiplicity": lines[(b, m)]["count"]}
                      for b, m in sorted(lines)],
            "all_interior_crossings": [qstr(x) for x in ordered[1:-1]],
            "elementary_cells": len(ordered) - 1,
        })
        for low, high in zip(ordered, ordered[1:]):
            sample = (low + high) / 2
            key = max(lines, key=lambda line: line[0] + line[1] * sample)
            intercept, slope = key
            winner = lines[key]
            t, at = records[winner["record_index"]]
            s = winner["s"]
            # Affine inequalities are checked at both endpoints, so the
            # dominant line bounds every enumerated line on the entire cell.
            for point in (low, high):
                expected = intercept + slope * point
                assert all(b + m * point <= expected for b, m in lines)
                assert dot(s, tuple(x - point * y for x, y in zip(at, t))) == expected
                assert value(at, t, point) == expected
            piece = {"lo": low, "hi": high, "intercept": intercept,
                     "slope": slope, "s": s, "t": t}
            if (cells and cells[-1]["hi"] == low and
                    all(cells[-1][k] == piece[k] for k in ("intercept", "slope", "s", "t"))):
                cells[-1]["hi"] = high
            else:
                cells.append(piece)
    assert cells[0]["lo"] == left and cells[-1]["hi"] == right
    assert all(p["hi"] == q["lo"] for p, q in zip(cells, cells[1:]))
    # Directly re-evaluate ALL original absolute-value functions at every
    # merged-piece boundary, including all globally necessary endpoints.
    endpoint_checks = []
    for point in sorted({p[k] for p in cells for k in ("lo", "hi")}):
        exact = max(value(at, t, point) for t, at in records)
        touching = [p for p in cells if p["lo"] <= point <= p["hi"]]
        assert all(p["intercept"] + p["slope"] * point == exact for p in touching)
        endpoint_checks.append({"lambda": qstr(point), "beta": qstr(exact)})
    # Obtain a counterexample to the registered linear proposal if one exists,
    # testing only already computed exact envelope endpoints.
    counterexample = None
    for checked in endpoint_checks:
        point, exact = F(checked["lambda"]), F(checked["beta"])
        proposed = F(10) - 12 * point
        if exact > proposed:
            piece = next(p for p in cells if p["lo"] <= point <= p["hi"])
            s, t = piece["s"], piece["t"]
            bilinear = sum(s[i] * (a[i][j] - (point if i == j else 0)) * t[j]
                           for i in range(12) for j in range(12))
            assert bilinear == exact > proposed
            counterexample = {"lambda": qstr(point), "s": list(s), "t": list(t),
                              "s_transpose_B_t": qstr(bilinear),
                              "linear_proposal": qstr(proposed),
                              "strict_gap": qstr(bilinear - proposed)}
            break
    return {
        "schema": "d3-classical-envelope-v1",
        "arithmetic": "Python standard-library fractions.Fraction; no floats",
        "matrix": "A[i,j]=dot(roots[i],roots[j])/8; B=A-lambda*I",
        "roots": [list(w) for w in roots],
        "interval": ["0", "1/2"],
        "enumerated_bob_signs": len(records),
        "all_row_breakpoints": [qstr(x) for x in row_knots],
        "base_intervals": interval_reports,
        "total_elementary_cells": sum(p["elementary_cells"] for p in interval_reports),
        "pieces": [{k: list(v) if k in ("s", "t") else qstr(v) for k, v in p.items()}
                   for p in cells],
        "endpoint_checks": endpoint_checks,
        "linear_proposal_counterexample": counterexample,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="Require exact agreement with a frozen JSON certificate")
    args = parser.parse_args()
    certificate = compute()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        assert certificate == expected, "Frozen certificate differs from exhaustive rational replay"
        print("PASS: frozen certificate equals exhaustive exact rational envelope replay")
    else:
        print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
