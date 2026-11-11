#!/usr/bin/env python3
"""Replay the exact two-hop routing certificate for the 217-variable p-cut.

The compressed certificate contains only nonnegative integer path flows.
This checker reconstructs the exact H4 matrix and archived p-gauge, verifies
every negative-edge demand and every positive-edge capacity with Python
integers, and checks that every positive edge has strictly positive residual
capacity.  No floating-point inequality is used.
"""

from __future__ import annotations

from collections import defaultdict, deque
import hashlib
from pathlib import Path
import sys

import h5py
import numpy as np


HERE = Path(__file__).resolve()
PROJECT = HERE.parents[1]
TOOLS = PROJECT / "tools"
BOOTSTRAP = TOOLS / "bootstrap"
sys.path[:0] = [str(TOOLS), str(BOOTSTRAP)]

from h4_exact_instance_checker import exact_int_matrix, exact_signs  # noqa: E402


MAT = PROJECT / "artifacts/frozen-instance/d4_n1_300x300.mat"
CERTIFICATE = PROJECT / "artifacts/certificates/d4-pcut-twohop-flow-certificate-20260830.npz"
EXPECTED_CERTIFICATE_SHA256 = (
    "1dda1ad4a4d79b370a0a93eb8bd22dad2ce5e87917aad45344db9dad9347253b"
)
EXPECTED_RECORDS = 473_676
EXPECTED_MINIMUM_SLACK = 95_963_447_132


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def edge(i: int, j: int) -> tuple[int, int]:
    return (i, j) if i < j else (j, i)


def main() -> None:
    assert sha256(CERTIFICATE) == EXPECTED_CERTIFICATE_SHA256

    with h5py.File(MAT, "r") as archive:
        matrix = exact_int_matrix(archive["A"][()])
        x = np.asarray(exact_signs(archive["ax"][()], "ax"), dtype=np.int64)
        y = np.asarray(exact_signs(archive["by"][()], "by"), dtype=np.int64)

    p = (x + y) // 2
    support = np.flatnonzero(p)
    assert len(support) == 217
    signs = p[support]
    gauged = matrix[np.ix_(support, support)].astype(np.int64) * np.outer(signs, signs)
    assert np.array_equal(gauged, gauged.T)

    positive: dict[tuple[int, int], int] = {}
    negative: dict[tuple[int, int], int] = {}
    zero_count = 0
    for i in range(217):
        for j in range(i + 1, 217):
            weight = int(gauged[i, j])
            if weight > 0:
                positive[(i, j)] = weight
            elif weight < 0:
                negative[(i, j)] = -weight
            else:
                zero_count += 1
    assert (len(positive), len(negative), zero_count) == (15_066, 6_294, 2_076)

    with np.load(CERTIFICATE, allow_pickle=False) as stored:
        assert set(stored.files) == {"u", "v", "h", "flow"}
        u = stored["u"]
        v = stored["v"]
        h = stored["h"]
        flow = stored["flow"]
    assert u.dtype == v.dtype == h.dtype == np.dtype("uint16")
    assert flow.dtype == np.dtype("int64")
    assert u.ndim == v.ndim == h.ndim == flow.ndim == 1
    assert len(u) == len(v) == len(h) == len(flow) == EXPECTED_RECORDS

    routed: defaultdict[tuple[int, int], int] = defaultdict(int)
    usage: defaultdict[tuple[int, int], int] = defaultdict(int)
    previous = (-1, -1, -1)
    for uu_raw, vv_raw, hh_raw, amount_raw in zip(u, v, h, flow):
        uu, vv, hh, amount = (
            int(uu_raw), int(vv_raw), int(hh_raw), int(amount_raw)
        )
        assert 0 <= uu < vv < 217
        assert 0 <= hh < 217 and hh not in (uu, vv)
        assert amount > 0
        current = (uu, vv, hh)
        assert current > previous
        previous = current

        demand_edge = (uu, vv)
        first = edge(uu, hh)
        second = edge(hh, vv)
        assert demand_edge in negative
        assert first in positive and second in positive
        routed[demand_edge] += amount
        usage[first] += amount
        usage[second] += amount

    # Exact demand equalities and exact positive-edge capacity inequalities.
    assert dict(routed) == negative
    slacks = {e: capacity - usage[e] for e, capacity in positive.items()}
    assert min(slacks.values()) == EXPECTED_MINIMUM_SLACK
    assert all(slack > 0 for slack in slacks.values())

    # Positive residual capacity on a connected graph also proves that the
    # only equality cuts are the two constant sign vectors.
    adjacency = [[] for _ in range(217)]
    for i, j in positive:
        adjacency[i].append(j)
        adjacency[j].append(i)
    reached = {0}
    queue = deque([0])
    while queue:
        i = queue.popleft()
        for j in adjacency[i]:
            if j not in reached:
                reached.add(j)
                queue.append(j)
    assert len(reached) == 217

    print("certificate SHA256 =", EXPECTED_CERTIFICATE_SHA256)
    print("positive/negative/zero off-diagonal edges =", 15_066, 6_294, 2_076)
    print("exact routed path records =", EXPECTED_RECORDS)
    print("minimum exact residual positive-edge capacity =", min(slacks.values()))
    print("all negative demands are routed through positive two-hop paths")
    print("therefore s^T L_p s >= 0 for every Boolean sign vector s")
    print("strict residual plus connectivity: equality only for s=+1 or s=-1")


if __name__ == "__main__":
    main()
