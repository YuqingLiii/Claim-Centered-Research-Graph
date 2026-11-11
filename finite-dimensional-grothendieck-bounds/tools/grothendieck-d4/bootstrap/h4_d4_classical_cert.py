#!/usr/bin/env python3

import sys
import os
import math
import json
import hashlib
import collections
from fractions import Fraction

import numpy as np
import h5py


EXPECTED_MD5 = "b5223ca2fd5c4cbe52e93a23a4570b9f"
EXPECTED_C = 2081044153087351400


# ============================================================
# Basic exact I/O
# ============================================================

def die(msg):
    raise SystemExit("ERROR: " + msg)


def file_md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def canon_int_matrix_sha256(A):
    """
    Platform-independent canonical serialization:
    row-major signed little-endian int64.
    """
    h = hashlib.sha256()
    for x in A.ravel(order="C"):
        h.update(int(x).to_bytes(8, "little", signed=True))
    return h.hexdigest()


def exact_int_matrix(raw, name):
    """
    Convert binary64 -> integer ONLY when the binary64 value itself
    is exactly integral. No rounding or tolerance is used.
    """
    a = np.asarray(raw)

    if a.ndim != 2:
        die(f"{name} is not 2D: shape={a.shape}")

    out = np.empty(a.shape, dtype=np.int64)

    it = np.nditer(a, flags=["multi_index", "refs_ok"])

    for z in it:
        x = float(z)

        if not math.isfinite(x):
            die(f"{name}{it.multi_index} is non-finite")

        q = int(x)

        if float(q) != x:
            die(
                f"{name}{it.multi_index} is not an exactly integral "
                f"binary64 value: {x!r}"
            )

        if not (-(1 << 63) <= q < (1 << 63)):
            die(f"{name}{it.multi_index} does not fit signed int64")

        out[it.multi_index] = q

    return out


def exact_sign_vector(raw, name, n):
    a = np.asarray(raw).reshape(-1)

    if a.size != n:
        die(f"{name} has {a.size} entries; expected {n}")

    out = []

    for k, z in enumerate(a):
        x = float(z)

        if x == 1.0:
            out.append(1)
        elif x == -1.0:
            out.append(-1)
        else:
            die(f"{name}[{k}] is not exactly ±1: {x!r}")

    return out


def dot_signs(A, x, y):
    """
    Python arbitrary-precision integer arithmetic throughout.
    """
    n, m = A.shape

    return sum(
        int(A[i, j]) * x[i] * y[j]
        for i in range(n)
        for j in range(m)
    )


def matvec_right(A, y):
    n, m = A.shape

    return [
        sum(int(A[i, j]) * y[j] for j in range(m))
        for i in range(n)
    ]


def matvec_left(x, A):
    n, m = A.shape

    return [
        sum(x[i] * int(A[i, j]) for i in range(n))
        for j in range(m)
    ]


def hist_dict(vals):
    c = collections.Counter(vals)

    return {
        str(k): int(c[k])
        for k in sorted(c)
    }


def sign_string(v):
    return "".join("+" if x == 1 else "-" for x in v)


# ============================================================
# Exact reduction after switching by archived witness
# ============================================================

def best_T_for_left_flip_set(B, rowm, colm, S):
    """
    Let the archived witness be switched to the all-+1 strategy.

    For fixed left flip set S, exactly minimizes W_B(S,T)
    over ALL 2^n choices of T.

    W(S,T)
      = sum_{i in S} r_i
        + sum_{j in T} [
              c_j - 2 sum_{i in S} B_ij
          ].

    Thus every j is chosen independently.
    """
    n = B.shape[0]

    ssum = [0] * n
    rpart = 0

    for i in S:
        rpart += rowm[i]
        bi = B[i]

        for j in range(n):
            ssum[j] += int(bi[j])

    T = []
    F = rpart

    for j in range(n):
        q = colm[j] - 2 * ssum[j]

        if q < 0:
            F += q
            T.append(j)

    return F, T


def enumerate_left_flip_support_0_1_2(B, rowm, colm):
    """
    Exhaust all S with |S| <= 2.
    For EACH such S, all T are eliminated exactly.

    By W(S,T)=W(S^c,T^c), this simultaneously treats
    |S| >= n-2.
    """
    n = B.shape[0]

    best = None
    bestS = None
    bestT = None
    tested = 0

    # |S| = 0
    F, T = best_T_for_left_flip_set(
        B, rowm, colm, ()
    )

    tested += 1
    best, bestS, bestT = F, (), T

    # |S| = 1
    for i in range(n):
        F, T = best_T_for_left_flip_set(
            B, rowm, colm, (i,)
        )

        tested += 1

        if F < best:
            best, bestS, bestT = F, (i,), T

    # |S| = 2
    for i in range(n):
        bi = B[i]

        for k in range(i + 1, n):
            bk = B[k]

            F = rowm[i] + rowm[k]
            T = []

            for j in range(n):
                q = (
                    colm[j]
                    - 2 * (
                        int(bi[j])
                        + int(bk[j])
                    )
                )

                if q < 0:
                    F += q
                    T.append(j)

            tested += 1

            if F < best:
                best = F
                bestS = (i, k)
                bestT = T

    return {
        "tested_left_subsets": tested,
        "min_cut_weight": int(best),
        "left_flip_set": list(bestS),
        "optimal_right_flip_set_for_that_left_set":
            list(bestT),
    }


# ============================================================
# Exact absolute/signed orbital algebra derived from A
# ============================================================

def build_abs_relations(A):
    """
    Switching-invariant ordinary relations use |A_ij|.

    Diagonal is split off even if its magnitude happened to
    coincide with an off-diagonal magnitude.

    sig_ij = sign(A_ij) is the signed carrier.
    """
    n = A.shape[0]

    diagvals = {
        abs(int(A[i, i]))
        for i in range(n)
    }

    if len(diagvals) != 1:
        die(
            "absolute diagonal is not constant: "
            + repr(sorted(diagvals))
        )

    diagmag = next(iter(diagvals))

    offmags = sorted({
        abs(int(A[i, j]))
        for i in range(n)
        for j in range(n)
        if i != j
    })

    keys = (
        [("diag", diagmag)]
        + [("off", m) for m in offmags]
    )

    off_id = {
        m: 1 + k
        for k, m in enumerate(offmags)
    }

    rel = np.empty(
        (n, n),
        dtype=np.int16
    )

    for i in range(n):
        for j in range(n):
            if i == j:
                rel[i, j] = 0
            else:
                rel[i, j] = off_id[
                    abs(int(A[i, j]))
                ]

    mags = [diagmag] + offmags

    # Exact sign carrier; 0 exactly where A_ij=0.
    sig = np.sign(A).astype(np.int8)

    return keys, mags, rel, sig


def orbital_closure(A, rel, sig):
    """
    Test exact coherent closure of the |A|-relations.

    For each ordered pair (i,j), compute the exact histogram

      #{ k :
          rel(i,k)=r,
          rel(k,j)=s }.

    Ordinary closure means that histogram depends only
    on rel(i,j).

    For nonzero A_ij we simultaneously compute the
    SIGNED intersection sum

      sum_k
        sig(i,k) sig(k,j)

    in each (r,s) class, normalized by sig(i,j).

    If this is constant on a target relation, then the signed
    adjacency matrices have exact structure constants there.

    No floating arithmetic enters this routine.
    """
    n = A.shape[0]
    R = int(rel.max()) + 1

    # Exact valencies.
    val = np.zeros(
        (n, R),
        dtype=np.int32
    )

    for i in range(n):
        val[i] = np.bincount(
            rel[i].astype(np.int64),
            minlength=R
        )

    homogeneous = bool(
        np.all(val == val[0])
    )

    valencies = [
        int(x)
        for x in val[0]
    ]

    # One representative per target relation.
    reps = [None] * R

    for i in range(n):
        for j in range(n):
            t = int(rel[i, j])

            if reps[t] is None:
                reps[t] = (i, j)

    ref_ord = [None] * R
    ref_sgn = [None] * R

    for t, (i, j) in enumerate(reps):
        codes = (
            rel[i].astype(np.int32) * R
            + rel[:, j].astype(np.int32)
        )

        ho = np.bincount(
            codes,
            minlength=R * R
        ).astype(np.int32)

        weights = (
            sig[i].astype(np.int16)
            * sig[:, j].astype(np.int16)
        )

        hp = np.bincount(
            codes[weights > 0],
            minlength=R * R
        ).astype(np.int32)

        hn = np.bincount(
            codes[weights < 0],
            minlength=R * R
        ).astype(np.int32)

        hs = hp - hn

        aij = int(A[i, j])

        if aij != 0:
            hs = hs * (
                1 if aij > 0 else -1
            )

        ref_ord[t] = ho
        ref_sgn[t] = hs

    ord_ok = True
    signed_nonzero_ok = True
    zero_target_all_products_zero = True

    ord_bad = None
    sgn_bad = None
    zero_bad = None

    # Exhaust every ordered pair.
    for i in range(n):
        left_codes = (
            rel[i].astype(np.int32) * R
        )

        si = sig[i].astype(np.int16)

        for j in range(n):
            t = int(rel[i, j])

            codes = (
                left_codes
                + rel[:, j].astype(np.int32)
            )

            ho = np.bincount(
                codes,
                minlength=R * R
            ).astype(np.int32)

            if (
                ord_ok
                and not np.array_equal(
                    ho,
                    ref_ord[t]
                )
            ):
                d = int(
                    np.flatnonzero(
                        ho != ref_ord[t]
                    )[0]
                )

                ord_bad = {
                    "pair": [i, j],
                    "target_relation": t,
                    "r": d // R,
                    "s": d % R,
                    "got": int(ho[d]),
                    "expected":
                        int(ref_ord[t][d]),
                }

                ord_ok = False

            weights = (
                si
                * sig[:, j].astype(np.int16)
            )

            hp = np.bincount(
                codes[weights > 0],
                minlength=R * R
            ).astype(np.int32)

            hn = np.bincount(
                codes[weights < 0],
                minlength=R * R
            ).astype(np.int32)

            hs = hp - hn

            aij = int(A[i, j])

            if aij != 0:
                hs = hs * (
                    1 if aij > 0 else -1
                )

                if (
                    signed_nonzero_ok
                    and not np.array_equal(
                        hs,
                        ref_sgn[t]
                    )
                ):
                    d = int(
                        np.flatnonzero(
                            hs != ref_sgn[t]
                        )[0]
                    )

                    sgn_bad = {
                        "pair": [i, j],
                        "target_relation": t,
                        "r": d // R,
                        "s": d % R,
                        "got": int(hs[d]),
                        "expected":
                            int(ref_sgn[t][d]),
                    }

                    signed_nonzero_ok = False

            else:
                nz = np.flatnonzero(hs)

                if nz.size:
                    zero_target_all_products_zero = False

                    if zero_bad is None:
                        d = int(nz[0])

                        zero_bad = {
                            "pair": [i, j],
                            "target_relation": t,
                            "r": d // R,
                            "s": d % R,
                            "signed_product_value":
                                int(hs[d]),
                        }

    ord_table = [
        x.reshape(R, R)
         .astype(int)
         .tolist()
        for x in ref_ord
    ]

    signed_table = [
        x.reshape(R, R)
         .astype(int)
         .tolist()
        for x in ref_sgn
    ]

    return {
        "relation_count": R,
        "homogeneous": homogeneous,
        "valencies": valencies,

        "ordinary_closure": ord_ok,
        "ordinary_closure_obstruction":
            ord_bad,

        "signed_closure_on_nonzero_targets":
            signed_nonzero_ok,

        "signed_closure_obstruction":
            sgn_bad,

        "zero_target_all_signed_products_zero":
            zero_target_all_products_zero,

        "zero_target_obstruction":
            zero_bad,

        "ordinary_intersection_numbers":
            ord_table,

        "signed_intersection_numbers":
            signed_table,
    }


def witness_signed_orbital_counts(
    A,
    rel,
    sig,
    ax,
    by
):
    """
    h_t =
      sum_{(i,j) in relation t}
        sig(A_ij) ax_i by_j.

    Since A_ij = magnitude_t * sig(A_ij),

      C = sum_t magnitude_t * h_t.

    This is an exact compact orbital decomposition of the
    archived witness.
    """
    R = int(rel.max()) + 1

    h = [0] * R
    edge_count = [0] * R

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            t = int(rel[i, j])

            edge_count[t] += 1

            h[t] += (
                int(sig[i, j])
                * ax[i]
                * by[j]
            )

    return edge_count, h


# ============================================================
# Canonical witness-colored equitable refinement
# ============================================================

def witness_equitable_refinement(
    rel,
    ax,
    by
):
    """
    Start with the four possible vertex colors (ax_i,by_i).

    Repeatedly refine by exact counts

      # { j :
           rel(i,j)=r,
           color(j)=c }.

    This is deterministic and exact.

    The stable cells are guaranteed equitable. They are useful
    for identifying the witness stabilizer structure, but the
    program does NOT incorrectly assume that arbitrary optimum
    signings are constant on these cells.
    """
    n = rel.shape[0]
    R = int(rel.max()) + 1

    initial_keys = [
        (ax[i], by[i])
        for i in range(n)
    ]

    uniq = {
        k: idx
        for idx, k
        in enumerate(
            sorted(set(initial_keys))
        )
    }

    colors = np.array(
        [uniq[k] for k in initial_keys],
        dtype=np.int32
    )

    rounds = 0

    while True:
        Cn = int(colors.max()) + 1

        sigs = []

        for i in range(n):
            cnt = np.zeros(
                (R, Cn),
                dtype=np.int16
            )

            for j in range(n):
                cnt[
                    int(rel[i, j]),
                    int(colors[j])
                ] += 1

            sigs.append(
                (
                    int(colors[i]),
                    tuple(
                        int(x)
                        for x in cnt.ravel()
                    ),
                )
            )

        uniq_sigs = sorted(set(sigs))

        mp = {
            s: k
            for k, s
            in enumerate(uniq_sigs)
        }

        newc = np.array(
            [mp[s] for s in sigs],
            dtype=np.int32
        )

        rounds += 1

        if np.array_equal(
            newc,
            colors
        ):
            break

        colors = newc

    Cn = int(colors.max()) + 1

    cells = [
        np.flatnonzero(
            colors == c
        ).astype(int).tolist()
        for c in range(Cn)
    ]

    quotient = []

    equitable = True
    bad = None

    for c, cell in enumerate(cells):
        rep = cell[0]

        base = np.zeros(
            (R, Cn),
            dtype=np.int16
        )

        for j in range(n):
            base[
                int(rel[rep, j]),
                int(colors[j])
            ] += 1

        for i in cell[1:]:
            cur = np.zeros(
                (R, Cn),
                dtype=np.int16
            )

            for j in range(n):
                cur[
                    int(rel[i, j]),
                    int(colors[j])
                ] += 1

            if not np.array_equal(
                base,
                cur
            ):
                equitable = False
                bad = [c, rep, i]
                break

        quotient.append(
            base.astype(int).tolist()
        )

        if not equitable:
            break

    return {
        "rounds": rounds,
        "cell_count": Cn,
        "cell_sizes": [
            len(c)
            for c in cells
        ],
        "cells": cells,
        "equitable_verified":
            equitable,
        "equitable_obstruction":
            bad,
        "quotient_relation_counts":
            quotient,
    }


# ============================================================
# Negative-edge graph:
# exact maximum matching and minimum vertex cover
# ============================================================

def hopcroft_karp(
    adj,
    nL,
    nR
):
    pairU = [-1] * nL
    pairV = [-1] * nR
    dist = [0] * nL

    INF = 10**9

    sys.setrecursionlimit(
        max(
            5000,
            10 * (nL + nR)
        )
    )

    def bfs():
        q = collections.deque()

        found = False

        for u in range(nL):
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF

        while q:
            u = q.popleft()

            for v in adj[u]:
                u2 = pairV[v]

                if u2 == -1:
                    found = True

                elif dist[u2] == INF:
                    dist[u2] = (
                        dist[u] + 1
                    )
                    q.append(u2)

        return found

    def dfs(u):
        for v in adj[u]:
            u2 = pairV[v]

            if (
                u2 == -1
                or (
                    dist[u2]
                    == dist[u] + 1
                    and dfs(u2)
                )
            ):
                pairU[u] = v
                pairV[v] = u
                return True

        dist[u] = INF
        return False

    matching = 0

    while bfs():
        for u in range(nL):
            if (
                pairU[u] == -1
                and dfs(u)
            ):
                matching += 1

    return (
        matching,
        pairU,
        pairV
    )


def min_vertex_cover_from_matching(
    adj,
    pairU,
    pairV
):
    """
    Standard Kőnig construction.

    From every unmatched left vertex, traverse alternating paths:
      unmatched L->R edges,
      then matched R->L edges.

    Minimum cover:
        (L \ Z_L) union Z_R.
    """
    nL = len(pairU)

    ZU = [False] * nL
    ZV = [False] * len(pairV)

    q = collections.deque()

    for u in range(nL):
        if pairU[u] == -1:
            ZU[u] = True
            q.append(u)

    while q:
        u = q.popleft()

        for v in adj[u]:
            # L -> R only along unmatched edges.
            if pairU[u] == v:
                continue

            if not ZV[v]:
                ZV[v] = True

                u2 = pairV[v]

                if (
                    u2 != -1
                    and not ZU[u2]
                ):
                    ZU[u2] = True
                    q.append(u2)

    coverU = [
        u
        for u in range(nL)
        if not ZU[u]
    ]

    coverV = [
        v
        for v in range(len(pairV))
        if ZV[v]
    ]

    return coverU, coverV


def negative_graph_certificate(B):
    n, m = B.shape

    adj = [
        []
        for _ in range(n)
    ]

    neg_edges = 0
    neg_sum = 0

    row_deg = [0] * n
    col_deg = [0] * m

    for i in range(n):
        for j in range(m):
            w = int(B[i, j])

            if w < 0:
                adj[i].append(j)

                neg_edges += 1
                neg_sum += w

                row_deg[i] += 1
                col_deg[j] += 1

    matching, pairU, pairV = (
        hopcroft_karp(
            adj,
            n,
            m
        )
    )

    coverU, coverV = (
        min_vertex_cover_from_matching(
            adj,
            pairU,
            pairV
        )
    )

    coverUset = set(coverU)
    coverVset = set(coverV)

    uncovered = [
        (i, j)
        for i in range(n)
        for j in adj[i]
        if (
            i not in coverUset
            and j not in coverVset
        )
    ]

    if uncovered:
        die(
            "internal error: "
            "minimum vertex cover misses "
            f"negative edge {uncovered[0]}"
        )

    if (
        len(coverU)
        + len(coverV)
        != matching
    ):
        die(
            "internal error: "
            "Kőnig equality failed"
        )

    return {
        "negative_edge_count":
            neg_edges,

        "negative_edge_weight_sum":
            int(neg_sum),

        "negative_row_degree_hist":
            hist_dict(row_deg),

        "negative_col_degree_hist":
            hist_dict(col_deg),

        "maximum_matching_size":
            matching,

        "minimum_vertex_cover_size":
            len(coverU) + len(coverV),

        "cover_left":
            coverU,

        "cover_right":
            coverV,

        "pairU":
            pairU,
    }


# ============================================================
# Exact integer max-flow
# ============================================================

class Dinic:

    def __init__(self, n):
        self.n = n

        self.g = [
            []
            for _ in range(n)
        ]

    def add_edge(
        self,
        u,
        v,
        c
    ):
        c = int(c)

        if c < 0:
            raise ValueError(
                "negative capacity"
            )

        a = [
            v,
            len(self.g[v]),
            c
        ]

        b = [
            u,
            len(self.g[u]),
            0
        ]

        self.g[u].append(a)
        self.g[v].append(b)

    def add_cut_edge(
        self,
        u,
        v,
        c
    ):
        """
        Cost c * [label_u != label_v].

        Two directed arcs of capacity c give exactly one
        crossing arc whichever orientation the cut has.
        """
        self.add_edge(u, v, c)
        self.add_edge(v, u, c)

    def maxflow(
        self,
        s,
        t
    ):
        flow = 0
        INF = 10**100

        while True:
            level = [-1] * self.n

            level[s] = 0

            q = collections.deque(
                [s]
            )

            while q:
                u = q.popleft()

                for e in self.g[u]:
                    if (
                        e[2] > 0
                        and level[e[0]] < 0
                    ):
                        level[e[0]] = (
                            level[u] + 1
                        )

                        q.append(e[0])

            if level[t] < 0:
                break

            it = [0] * self.n

            def dfs(u, f):
                if u == t:
                    return f

                while (
                    it[u]
                    < len(self.g[u])
                ):
                    e = self.g[u][
                        it[u]
                    ]

                    if (
                        e[2] > 0
                        and level[e[0]]
                        == level[u] + 1
                    ):
                        got = dfs(
                            e[0],
                            min(
                                f,
                                e[2]
                            )
                        )

                        if got:
                            e[2] -= got

                            self.g[
                                e[0]
                            ][
                                e[1]
                            ][2] += got

                            return got

                    it[u] += 1

                return 0

            while True:
                f = dfs(
                    s,
                    INF
                )

                if not f:
                    break

                flow += f

        return flow

    def reachable(
        self,
        s
    ):
        seen = [False] * self.n

        seen[s] = True

        q = collections.deque(
            [s]
        )

        while q:
            u = q.popleft()

            for e in self.g[u]:
                if (
                    e[2] > 0
                    and not seen[e[0]]
                ):
                    seen[e[0]] = True
                    q.append(e[0])

        return seen


# ============================================================
# Exact exhaustive branch verifier
# ============================================================

def build_all_edges(B):
    n, m = B.shape

    return [
        (
            i,
            n + j,
            int(B[i, j])
        )
        for i in range(n)
        for j in range(m)
    ]


def exact_cut_weight(
    edges,
    labels
):
    return sum(
        w
        for u, v, w in edges
        if labels[u] != labels[v]
    )


def relaxation_mincut(
    edges,
    Nverts,
    fixed
):
    """
    Rigorous lower bound at a partial branch.

    Edge cases:

    1. both endpoints fixed:
         exact constant.

    2. one endpoint fixed:
         exact unary term.

    3. both endpoints free, w >= 0:
         exact submodular cut term.

    4. both endpoints free, w < 0:
         w*[different] >= w.
       Replace by constant w.

    After (4), all remaining pairwise terms are nonnegative,
    hence exactly minimized by an s-t min-cut.

    Therefore returned lb <= every completion of the branch.
    """
    h = [0] * Nverts
    const = 0

    pos_free = []

    for u, v, w in edges:
        fu = fixed.get(u)
        fv = fixed.get(v)

        if (
            fu is not None
            and fv is not None
        ):
            if fu != fv:
                const += w

        elif fu is not None:
            # w * [fu != z_v]
            if fu == 0:
                # w z_v
                h[v] += w

            else:
                # w (1-z_v)
                const += w
                h[v] -= w

        elif fv is not None:
            # w * [z_u != fv]
            if fv == 0:
                h[u] += w

            else:
                const += w
                h[u] -= w

        else:
            if w >= 0:
                pos_free.append(
                    (u, v, w)
                )

            else:
                # exact independent lower bound
                const += w

    S = Nverts
    T = Nverts + 1

    D = Dinic(
        Nverts + 2
    )

    for u, v, w in pos_free:
        D.add_cut_edge(
            u,
            v,
            w
        )

    for v in range(Nverts):
        if v in fixed:
            continue

        hv = h[v]

        if hv >= 0:
            # D_v(0)=0, D_v(1)=hv
            if hv:
                D.add_edge(
                    S,
                    v,
                    hv
                )

        else:
            # hv*z
            # = hv + (-hv)*(1-z)
            const += hv

            D.add_edge(
                v,
                T,
                -hv
            )

    flow = D.maxflow(
        S,
        T
    )

    reach = D.reachable(S)

    labels = [0] * Nverts

    for v in range(Nverts):
        if v in fixed:
            labels[v] = fixed[v]

        else:
            # source side = 0
            # sink side   = 1
            labels[v] = (
                0
                if reach[v]
                else 1
            )

    lb = const + flow

    actual = exact_cut_weight(
        edges,
        labels
    )

    if actual < lb:
        die(
            "internal error: "
            "relaxation is not a lower bound: "
            f"actual={actual}, lb={lb}"
        )

    return (
        int(lb),
        int(actual),
        labels
    )


def branch_verify_cut_nonnegative(
    B,
    cover_left,
    cover_right,
    node_limit
):
    """
    COMPLETE proof logic:

      K = a vertex cover of every negative B-edge.

    Branch only on labels of K.

    Because K covers all negative edges, once all K-labels
    are fixed, every free-free edge has B_ij >= 0.

    Hence every leaf is solved exactly by min-cut.

    At internal nodes the relaxation is a rigorous lower bound.

    Global complementation of every label leaves every
    [different] indicator unchanged, so one cover vertex
    is fixed to 0 without loss.

    Thus, if every branch either
       (a) has lower bound >= 0, or
       (b) reaches an exact nonnegative leaf,
    then EVERY one of the 2^600 cuts has W >= 0.
    """
    n = B.shape[0]

    edges = build_all_edges(B)

    N = 2 * n

    K = (
        list(cover_left)
        + [
            n + j
            for j in cover_right
        ]
    )

    if not K:
        return {
            "status": "PROVED",
            "nodes": 0,
            "pruned": 0,
            "max_depth": 0,
            "transcript_sha256":
                hashlib.sha256(
                    b"no-negative-edges"
                ).hexdigest(),
            "counterexample_labels":
                None,
        }

    # Deterministic branching order:
    # largest total magnitude of incident negative weight first.
    neg_weight = [0] * N

    for u, v, w in edges:
        if w < 0:
            neg_weight[u] += -w
            neg_weight[v] += -w

    K = sorted(
        K,
        key=lambda v: (
            -neg_weight[v],
            v
        )
    )

    # Complement symmetry:
    # every cut is represented with anchor=0.
    anchor = K[0]

    order = K[1:]

    fixed = {
        anchor: 0
    }

    H = hashlib.sha256()

    stats = {
        "nodes": 0,
        "pruned": 0,
        "max_depth": 0,
    }

    found = {
        "labels": None,
        "weight": None,
    }

    aborted = {
        "flag": False
    }

    def dfs(
        depth,
        path
    ):
        if (
            aborted["flag"]
            or found["labels"]
               is not None
        ):
            return False

        if (
            node_limit is not None
            and stats["nodes"]
                >= node_limit
        ):
            aborted["flag"] = True
            return False

        stats["nodes"] += 1

        stats["max_depth"] = max(
            stats["max_depth"],
            depth
        )

        lb, actual, labels = (
            relaxation_mincut(
                edges,
                N,
                fixed
            )
        )

        H.update(
            (
                f"N {path} "
                f"{lb} {actual}\n"
            ).encode()
        )

        # The relaxed optimizer is itself a genuine
        # labeling. Evaluate the ORIGINAL cut.
        # If negative, we have an exact counterexample
        # immediately, even at an internal node.
        if actual < 0:
            found["labels"] = labels
            found["weight"] = actual

            H.update(
                (
                    "COUNTEREXAMPLE "
                    f"{path} {actual}\n"
                ).encode()
            )

            return False

        # Every completion has weight >= lb.
        if lb >= 0:
            stats["pruned"] += 1

            H.update(
                (
                    f"PRUNE "
                    f"{path} {lb}\n"
                ).encode()
            )

            return True

        if depth == len(order):
            # Entire negative-edge vertex cover is fixed.
            # Hence there are no remaining negative
            # free-free edges and the relaxation is exact.
            if lb != actual:
                die(
                    "leaf relaxation should be exact "
                    f"but lb={lb}, actual={actual}"
                )

            # actual < 0 was already caught.
            stats["pruned"] += 1

            H.update(
                (
                    f"LEAF "
                    f"{path} {lb}\n"
                ).encode()
            )

            return True

        v = order[depth]

        for bit in (0, 1):
            fixed[v] = bit

            ok = dfs(
                depth + 1,
                path + str(bit)
            )

            del fixed[v]

            if (
                found["labels"]
                    is not None
                or aborted["flag"]
            ):
                return False

            if not ok:
                return False

        return True

    complete = dfs(
        0,
        ""
    )

    if found["labels"] is not None:
        status = "COUNTEREXAMPLE"

    elif (
        complete
        and not aborted["flag"]
    ):
        status = "PROVED"

    else:
        status = (
            "INCOMPLETE_NODE_LIMIT"
        )

    return {
        "status":
            status,

        "cover_size":
            len(K),

        "anchor_fixed_zero":
            anchor,

        "branch_order":
            order,

        "nodes":
            stats["nodes"],

        "pruned":
            stats["pruned"],

        "max_depth":
            stats["max_depth"],

        "node_limit":
            node_limit,

        "transcript_sha256":
            H.hexdigest(),

        "counterexample_cut_weight":
            found["weight"],

        "counterexample_labels":
            found["labels"],
    }


# ============================================================
# Optional exact reconstruction of P in Q(sqrt(5))
#
# IMPORTANT:
# The stored P doubles are only used to GENERATE a candidate
# algebraic reconstruction.
#
# The numerator is emitted only after the reconstructed matrix
# passes the exact identity P^2 = 75 P and diag(P)=1 in Q(sqrt5).
# ============================================================

def qsqrt_str(a, b):
    a = Fraction(a)
    b = Fraction(b)

    def fs(q):
        if q.denominator == 1:
            return str(q.numerator)

        return (
            f"{q.numerator}/"
            f"{q.denominator}"
        )

    if b == 0:
        return fs(a)

    if a == 0:
        return (
            f"({fs(b)})*sqrt(5)"
        )

    sign = (
        "+"
        if b > 0
        else "-"
    )

    return (
        f"({fs(a)}) "
        f"{sign} "
        f"({fs(abs(b))})*sqrt(5)"
    )


def lcm(a, b):
    return abs(
        a // math.gcd(a, b) * b
    )


def reconstruct_P_exact(
    A,
    Pfloat
):
    try:
        import sympy as sp

    except Exception as e:
        return {
            "status":
                "SKIPPED_NO_SYMPY",
            "reason":
                repr(e),
        }

    n = A.shape[0]

    sq = sp.sqrt(5)

    # Group entries using:
    #   diagonal/off-diagonal status,
    #   |A_ij|,
    #   normalized approximate P-value.
    #
    # This grouping is candidate generation only.
    # The final algebraic matrix is checked exactly.
    groups = {}

    for i in range(n):
        for j in range(n):
            aij = int(A[i, j])
            p = float(Pfloat[i, j])

            carrier = (
                1
                if aij >= 0
                else -1
            )

            normp = (
                p * carrier
                if aij != 0
                else p
            )

            key = (
                i == j,
                abs(aij),
                int(
                    round(
                        normp
                        * 10**12
                    )
                ),
            )

            groups.setdefault(
                key,
                []
            ).append(
                (i, j, normp)
            )

    pair_by_key = {}

    max_err = 0.0

    for key, items in groups.items():

        rep = (
            sum(
                x[2]
                for x in items
            )
            / len(items)
        )

        if abs(rep) < 5e-14:
            a = Fraction(0)
            b = Fraction(0)

        else:
            try:
                expr = sp.expand(
                    sp.radsimp(
                        sp.nsimplify(
                            rep,
                            [sq],
                            tolerance=1e-11,
                            full=False,
                        )
                    )
                )

            except Exception as e:
                return {
                    "status":
                        "FAILED_NSIMPLIFY",
                    "key":
                        list(key),
                    "reason":
                        repr(e),
                }

            bb = (
                sp.expand(expr)
                  .coeff(sq)
            )

            aa = sp.simplify(
                expr - bb * sq
            )

            if (
                aa.is_Rational
                    is not True
                or bb.is_Rational
                    is not True
            ):
                return {
                    "status":
                        "FAILED_NOT_QSQRT5",
                    "key":
                        list(key),
                    "expr":
                        str(expr),
                }

            a = Fraction(
                int(aa.p),
                int(aa.q)
            )

            b = Fraction(
                int(bb.p),
                int(bb.q)
            )

            if (
                max(
                    abs(a.numerator),
                    abs(b.numerator)
                ) > 10**6
                or
                max(
                    a.denominator,
                    b.denominator
                ) > 10**6
            ):
                return {
                    "status":
                        "FAILED_COMPLEXITY_BOUND",
                    "key":
                        list(key),
                    "a":
                        str(a),
                    "b":
                        str(b),
                }

        approx = (
            float(a)
            + float(b)
              * math.sqrt(5.0)
        )

        group_err = max(
            abs(x - approx)
            for _, _, x in items
        )

        max_err = max(
            max_err,
            group_err
        )

        if group_err > 2e-10:
            return {
                "status":
                    "FAILED_CLUSTER_ERROR",
                "key":
                    list(key),
                "candidate":
                    qsqrt_str(a, b),
                "max_group_error":
                    group_err,
            }

        pair_by_key[key] = (
            a,
            b
        )

    # One common denominator.
    D = 1

    for a, b in pair_by_key.values():
        D = lcm(
            D,
            a.denominator
        )

        D = lcm(
            D,
            b.denominator
        )

    if D > 10**7:
        return {
            "status":
                "FAILED_DENOMINATOR_LCM_TOO_LARGE",
            "D":
                D,
        }

    # Reconstructed exact matrix:
    #
    # P = (X + Y sqrt(5))/D,
    #
    # X,Y integer matrices.
    X = np.zeros(
        (n, n),
        dtype=np.int64
    )

    Y = np.zeros(
        (n, n),
        dtype=np.int64
    )

    for key, items in groups.items():

        a, b = pair_by_key[key]

        xa = (
            a.numerator
            * (
                D // a.denominator
            )
        )

        yb = (
            b.numerator
            * (
                D // b.denominator
            )
        )

        for i, j, _ in items:

            aij = int(A[i, j])

            carrier = (
                1
                if aij >= 0
                else -1
            )

            if aij != 0:
                X[i, j] = (
                    carrier * xa
                )

                Y[i, j] = (
                    carrier * yb
                )

            else:
                X[i, j] = xa
                Y[i, j] = yb

    if (
        not np.array_equal(
            X,
            X.T
        )
        or
        not np.array_equal(
            Y,
            Y.T
        )
    ):
        return {
            "status":
                "FAILED_EXACT_SYMMETRY"
        }

    if any(
        int(X[i, i]) != D
        or int(Y[i, i]) != 0
        for i in range(n)
    ):
        return {
            "status":
                "FAILED_EXACT_DIAGONAL",
            "D":
                D,
        }

    mx = max(
        abs(int(x))
        for x in X.ravel()
    )

    my = max(
        abs(int(y))
        for y in Y.ravel()
    )

    # Before int64 matrix multiplication, certify that no
    # intermediate entry can overflow.
    boundR = n * (
        mx * mx
        + 5 * my * my
    )

    boundS = n * (
        2 * mx * my
    )

    safe = (
        max(
            boundR,
            boundS,
            75 * D * mx,
            75 * D * my,
        )
        < (1 << 62)
    )

    if safe:
        RR = (
            X @ X
            + 5 * (Y @ Y)
        )

        SS = (
            X @ Y
            + Y @ X
        )

        okR = np.array_equal(
            RR,
            (75 * D) * X
        )

        okS = np.array_equal(
            SS,
            (75 * D) * Y
        )

    else:
        # Arbitrary-precision fallback.
        XO = X.astype(object)
        YO = Y.astype(object)

        RR = (
            XO @ XO
            + 5 * (YO @ YO)
        )

        SS = (
            XO @ YO
            + YO @ XO
        )

        okR = np.array_equal(
            RR,
            (75 * D) * XO
        )

        okS = np.array_equal(
            SS,
            (75 * D) * YO
        )

    if not (okR and okS):
        return {
            "status":
                "FAILED_EXACT_PROJECTOR_IDENTITY",
            "D":
                D,
            "max_float_reconstruction_error":
                max_err,
        }

    # Only NOW form <A,P>, exactly.
    Nr = sum(
        int(A[i, j])
        * int(X[i, j])
        for i in range(n)
        for j in range(n)
    )

    Ns = sum(
        int(A[i, j])
        * int(Y[i, j])
        for i in range(n)
        for j in range(n)
    )

    ar = Fraction(
        Nr,
        D
    )

    br = Fraction(
        Ns,
        D
    )

    return {
        "status":
            "PROVED_EXACT_QSQRT5_PROJECTOR_RECONSTRUCTION",

        "cluster_count":
            len(groups),

        "common_denominator_D":
            D,

        "max_float_reconstruction_error":
            max_err,

        "projector_identity":
            "P^2 = 75 P exact in Q(sqrt(5))",

        "numerator_a":
            str(ar),

        "numerator_b":
            str(br),

        "numerator_exact":
            qsqrt_str(ar, br),
    }


# ============================================================
# Main
# ============================================================

def main():

    if len(sys.argv) != 2:
        die(
            "usage: python "
            "h4_d4_classical_cert.py "
            "/path/to/"
            "d4_n1_300x300.mat"
        )

    path = sys.argv[1]

    # --------------------------------------------------------
    # Check official bytes first.
    # --------------------------------------------------------

    md5 = file_md5(path)

    if md5 != EXPECTED_MD5:
        die(
            "MD5 mismatch: "
            f"got {md5}, "
            f"expected {EXPECTED_MD5}"
        )

    # --------------------------------------------------------
    # Load datasets.
    # --------------------------------------------------------

    with h5py.File(
        path,
        "r"
    ) as f:

        required = [
            "A",
            "P",
            "ax",
            "by",
            "SDP1A",
            "SDP4A",
        ]

        missing = [
            k
            for k in required
            if k not in f
        ]

        if missing:
            die(
                f"missing datasets: "
                f"{missing}"
            )

        A = exact_int_matrix(
            f["A"][()],
            "A"
        )

        Pfloat = np.asarray(
            f["P"][()],
            dtype=np.float64
        )

        axraw = f["ax"][()]
        byraw = f["by"][()]

        stored_sdp1 = np.asarray(
            f["SDP1A"][()]
        ).reshape(-1)

        stored_sdp4 = np.asarray(
            f["SDP4A"][()]
        ).reshape(-1)

    if A.shape != (300, 300):
        die(
            f"A shape {A.shape}; "
            "expected (300,300)"
        )

    if not np.array_equal(
        A,
        A.T
    ):
        die(
            "A is not exactly symmetric "
            "as an integer matrix"
        )

    n = 300

    ax = exact_sign_vector(
        axraw,
        "ax",
        n
    )

    by = exact_sign_vector(
        byraw,
        "by",
        n
    )

    summary = {}

    summary["mat_md5"] = md5

    summary["A_shape"] = list(
        A.shape
    )

    summary[
        "A_canonical_sha256"
    ] = canon_int_matrix_sha256(A)

    summary[
        "A_distinct_levels"
    ] = sorted({
        int(x)
        for x in A.ravel()
    })

    summary[
        "A_level_count"
    ] = len(
        summary[
            "A_distinct_levels"
        ]
    )

    summary[
        "A_diagonal"
    ] = int(A[0, 0])

    summary[
        "A_diagonal_constant"
    ] = all(
        int(A[i, i])
        == int(A[0, 0])
        for i in range(n)
    )

    # --------------------------------------------------------
    # Exact archived witness value.
    # --------------------------------------------------------

    C = dot_signs(
        A,
        ax,
        by
    )

    summary[
        "archived_witness_value_exact"
    ] = C

    summary[
        "matches_expected_C"
    ] = (
        C == EXPECTED_C
    )

    if C != EXPECTED_C:
        die(
            "archived witness value is "
            f"{C}, "
            f"not expected "
            f"{EXPECTED_C}"
        )

    # --------------------------------------------------------
    # Exact coordinate-wise optimality / best responses.
    # --------------------------------------------------------

    hleft = matvec_right(
        A,
        by
    )

    hright = matvec_left(
        ax,
        A
    )

    best_left = sum(
        abs(v)
        for v in hleft
    )

    best_right = sum(
        abs(v)
        for v in hright
    )

    left_mismatch = [
        i
        for i, v
        in enumerate(hleft)
        if (
            v != 0
            and ax[i] * v < 0
        )
    ]

    right_mismatch = [
        j
        for j, v
        in enumerate(hright)
        if (
            v != 0
            and by[j] * v < 0
        )
    ]

    summary[
        "best_response_checks"
    ] = {
        "max_over_ax_with_by_fixed":
            best_left,

        "max_over_by_with_ax_fixed":
            best_right,

        "left_mismatches":
            left_mismatch,

        "right_mismatches":
            right_mismatch,

        "left_zero_fields": [
            i
            for i, v
            in enumerate(hleft)
            if v == 0
        ],

        "right_zero_fields": [
            j
            for j, v
            in enumerate(hright)
            if v == 0
        ],
    }

    # --------------------------------------------------------
    # Switch archived witness to all +1.
    # --------------------------------------------------------

    axs = np.array(
        ax,
        dtype=np.int64
    )

    bys = np.array(
        by,
        dtype=np.int64
    )

    B = (
        A * axs[:, None]
    ) * bys[None, :]

    Bsum = sum(
        int(x)
        for x in B.ravel()
    )

    if Bsum != C:
        die(
            "internal error: "
            "switched B sum != C"
        )

    rowm = [
        sum(
            int(B[i, j])
            for j in range(n)
        )
        for i in range(n)
    ]

    colm = [
        sum(
            int(B[i, j])
            for i in range(n)
        )
        for j in range(n)
    ]

    summary[
        "switching"
    ] = {
        "B_sum":
            Bsum,

        "row_margin_min":
            min(rowm),

        "col_margin_min":
            min(colm),

        "row_margin_hist":
            hist_dict(rowm),

        "col_margin_hist":
            hist_dict(colm),

        "all_single_vertex_cuts_nonnegative":
            min(rowm + colm) >= 0,
    }

    # --------------------------------------------------------
    # Exact theorem for all |S| <= 2 and arbitrary T.
    # --------------------------------------------------------

    low = (
        enumerate_left_flip_support_0_1_2(
            B,
            rowm,
            colm
        )
    )

    summary[
        "exact_left_support_le_2"
    ] = low

    # A negative value here already refutes C.
    if low["min_cut_weight"] < 0:

        S = set(
            low["left_flip_set"]
        )

        T = set(
            low[
                "optimal_right_flip_set_for_that_left_set"
            ]
        )

        eps = [
            ax[i]
            * (
                -1
                if i in S
                else 1
            )
            for i in range(n)
        ]

        delta = [
            by[j]
            * (
                -1
                if j in T
                else 1
            )
            for j in range(n)
        ]

        val = dot_signs(
            A,
            eps,
            delta
        )

        summary[
            "COUNTEREXAMPLE"
        ] = {
            "value":
                val,

            "eps":
                sign_string(eps),

            "delta":
                sign_string(delta),

            "left_flip_set":
                sorted(S),

            "right_flip_set":
                sorted(T),
        }

    # --------------------------------------------------------
    # Exact signed/orbital algebra.
    # --------------------------------------------------------

    keys, mags, rel, sig = (
        build_abs_relations(A)
    )

    orb = orbital_closure(
        A,
        rel,
        sig
    )

    edge_count, wh = (
        witness_signed_orbital_counts(
            A,
            rel,
            sig,
            ax,
            by
        )
    )

    contrib = [
        int(mags[t])
        * int(wh[t])
        for t in range(
            len(mags)
        )
    ]

    if sum(contrib) != C:
        die(
            "signed orbital witness "
            "decomposition does not sum to C"
        )

    orb["relation_keys"] = [
        [a, int(b)]
        for a, b in keys
    ]

    orb["magnitudes"] = [
        int(x)
        for x in mags
    ]

    orb[
        "relation_edge_counts"
    ] = edge_count

    orb[
        "witness_signed_correlations"
    ] = wh

    orb[
        "witness_contributions"
    ] = contrib

    orbital_hash_payload = json.dumps(
        {
            "relation_keys":
                orb[
                    "relation_keys"
                ],

            "valencies":
                orb[
                    "valencies"
                ],

            "ordinary_intersection_numbers":
                orb[
                    "ordinary_intersection_numbers"
                ],

            "signed_intersection_numbers":
                orb[
                    "signed_intersection_numbers"
                ],
        },
        sort_keys=True,
        separators=(",", ":"),
    ).encode()

    orb[
        "orbital_table_sha256"
    ] = hashlib.sha256(
        orbital_hash_payload
    ).hexdigest()

    summary[
        "orbital_summary"
    ] = {
        "relation_count":
            orb[
                "relation_count"
            ],

        "relation_keys":
            orb[
                "relation_keys"
            ],

        "valencies":
            orb[
                "valencies"
            ],

        "ordinary_closure":
            orb[
                "ordinary_closure"
            ],

        "ordinary_closure_obstruction":
            orb[
                "ordinary_closure_obstruction"
            ],

        "signed_closure_on_nonzero_targets":
            orb[
                "signed_closure_on_nonzero_targets"
            ],

        "signed_closure_obstruction":
            orb[
                "signed_closure_obstruction"
            ],

        "zero_target_all_signed_products_zero":
            orb[
                "zero_target_all_signed_products_zero"
            ],

        "zero_target_obstruction":
            orb[
                "zero_target_obstruction"
            ],

        "witness_signed_correlations":
            wh,

        "witness_contributions":
            contrib,

        "orbital_table_sha256":
            orb[
                "orbital_table_sha256"
            ],
    }

    # --------------------------------------------------------
    # Witness stabilizer-compatible equitable refinement.
    # --------------------------------------------------------

    refinement = (
        witness_equitable_refinement(
            rel,
            ax,
            by
        )
    )

    summary[
        "witness_equitable_refinement"
    ] = {
        "rounds":
            refinement[
                "rounds"
            ],

        "cell_count":
            refinement[
                "cell_count"
            ],

        "cell_sizes":
            refinement[
                "cell_sizes"
            ],

        "equitable_verified":
            refinement[
                "equitable_verified"
            ],
    }

    # --------------------------------------------------------
    # Negative switched-edge graph.
    # --------------------------------------------------------

    neg = (
        negative_graph_certificate(B)
    )

    summary[
        "negative_graph"
    ] = {
        k: v
        for k, v
        in neg.items()
        if k != "pairU"
    }

    # --------------------------------------------------------
    # Exact vector numerator only after exact reconstruction.
    # --------------------------------------------------------

    if (
        Pfloat.shape
        == (300, 300)
        and np.allclose(
            Pfloat,
            Pfloat.T,
            atol=0,
            rtol=0
        )
    ):
        prec = reconstruct_P_exact(
            A,
            Pfloat
        )

    else:
        prec = {
            "status":
                "FAILED_P_SHAPE_OR_SYMMETRY",

            "shape":
                list(Pfloat.shape),
        }

    summary[
        "P_exact_reconstruction"
    ] = prec

    # --------------------------------------------------------
    # Exhaustive exact branch verifier.
    #
    # Default:
    #   auto-run unlimited only if the exact negative-edge
    #   minimum vertex cover has size <= 10.
    #
    # Otherwise it reports the exact cover size but does not
    # risk an enormous run.
    #
    # To run:
    #
    #   H4_BB_NODES=100 python cert.py file.mat
    #
    # for a 100-node exact probe, or
    #
    #   H4_BB_NODES=-1 python cert.py file.mat
    #
    # for an unlimited exhaustive proof attempt.
    # --------------------------------------------------------

    env = os.environ.get(
        "H4_BB_NODES"
    )

    if env is None:
        node_limit = (
            None
            if (
                neg[
                    "minimum_vertex_cover_size"
                ] <= 10
            )
            else 0
        )

    else:
        z = int(env)

        node_limit = (
            None
            if z < 0
            else z
        )

    if node_limit == 0:

        bb = {
            "status":
                "NOT_RUN",

            "reason":
                "set H4_BB_NODES=-1 "
                "for exhaustive, or a "
                "positive integer for a probe",

            "cover_size":
                neg[
                    "minimum_vertex_cover_size"
                ],
        }

    else:

        bb = (
            branch_verify_cut_nonnegative(
                B,

                neg[
                    "cover_left"
                ],

                neg[
                    "cover_right"
                ],

                node_limit
            )
        )

        if (
            bb.get(
                "counterexample_labels"
            )
            is not None
        ):

            labels = (
                bb[
                    "counterexample_labels"
                ]
            )

            S = {
                i
                for i in range(n)
                if labels[i]
            }

            T = {
                j
                for j in range(n)
                if labels[n + j]
            }

            eps = [
                ax[i]
                * (
                    -1
                    if i in S
                    else 1
                )
                for i in range(n)
            ]

            delta = [
                by[j]
                * (
                    -1
                    if j in T
                    else 1
                )
                for j in range(n)
            ]

            val = dot_signs(
                A,
                eps,
                delta
            )

            bb[
                "counterexample_value"
            ] = val

            bb[
                "counterexample_eps"
            ] = sign_string(eps)

            bb[
                "counterexample_delta"
            ] = sign_string(delta)

            # Exact signs above are enough.
            del bb[
                "counterexample_labels"
            ]

    summary[
        "branch_verifier"
    ] = bb

    # --------------------------------------------------------
    # Stored floating numbers are diagnostics ONLY.
    # --------------------------------------------------------

    summary[
        "stored_float_diagnostics"
    ] = {
        "SDP1A": [
            float(x)
            for x in stored_sdp1
        ],

        "SDP4A": [
            float(x)
            for x in stored_sdp4
        ],
    }

    # --------------------------------------------------------
    # Full tables to a deterministic JSON certificate-data file.
    # --------------------------------------------------------

    certdata = {
        "summary":
            summary,

        "orbital_full":
            orb,

        "witness_refinement_full":
            refinement,
    }

    outpath = (
        path
        + ".classical_certdata.json"
    )

    payload = json.dumps(
        certdata,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()

    with open(
        outpath,
        "wb"
    ) as f:
        f.write(payload)

    cert_sha = hashlib.sha256(
        payload
    ).hexdigest()

    summary[
        "certdata_path"
    ] = outpath

    summary[
        "certdata_sha256"
    ] = cert_sha

    print(
        json.dumps(
            summary,
            indent=2,
            sort_keys=True
        )
    )


if __name__ == "__main__":
    main()
