#!/usr/bin/env python3
#
# h4_level2_sos.py
#
# Usage:
#
#   python h4_level2_sos.py d4_n1_300x300.mat
#
# To verify a rational degree-2 SOS certificate:
#
#   python h4_level2_sos.py d4_n1_300x300.mat --verify cert.json
#
# Dependencies:
#   numpy
#   h5py
#   sympy
#
# No optimization status is treated as proof.
# All decisive checks after reconstruction use exact integers /
# rationals / Q(sqrt(5)).
#
# ------------------------------------------------------------
# Certificate format
# ------------------------------------------------------------
#
# {
#   "degree": 2,
#   "seeds": [
#     {
#       "weight": "3/7",
#       "terms": [
#         ["2/5", []],
#         ["-1", [0]],
#         ["7/3", [17, 300+41]]
#       ]
#     }
#   ]
# }
#
# Variable IDs:
#   x_i  = i,       0 <= i < 300
#   y_j  = 300 + j, 0 <= j < 300
#
# Each seed q has degree <= 2.
#
# The verifier checks exactly
#
#   C - x^T A y
#     =
#   (1/|H4|) sum_g sum_k w_k (g q_k)^2
#
# modulo x_i^2 = y_j^2 = 1.
#
# Nonnegative rational weights are allowed.  Therefore every
# accepted certificate is a genuine real SOS certificate.
#

import sys
import os
import json
import math
import hashlib
import collections
from fractions import Fraction

import numpy as np
import h5py
import sympy as sp


EXPECTED_MD5 = "b5223ca2fd5c4cbe52e93a23a4570b9f"
EXPECTED_A_SHA256 = (
    "5fc272a61a97c0aa9f42ef8626675650"
    "0401c701a6f33a3b30bde4dbe6f113e5"
)
EXPECTED_C = 2081044153087351400

N = 300
NV = 600

SQ5 = sp.sqrt(5)


# ============================================================
# Utilities
# ============================================================

def die(s):
    raise SystemExit("ERROR: " + s)


def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def matrix_sha256(A):
    h = hashlib.sha256()
    for z in A.ravel(order="C"):
        h.update(
            int(z).to_bytes(
                8, "little", signed=True
            )
        )
    return h.hexdigest()


def parse_fraction(x):
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, str):
        return Fraction(x)
    raise ValueError(
        f"cannot parse rational {x!r}"
    )


def exact_integer_matrix(raw, name):
    a = np.asarray(raw)

    if a.shape != (N, N):
        die(
            f"{name}: expected 300x300, "
            f"got {a.shape}"
        )

    out = np.empty(
        (N, N),
        dtype=np.int64
    )

    it = np.nditer(
        a,
        flags=["multi_index"]
    )

    for z in it:
        x = float(z)

        if not math.isfinite(x):
            die(
                f"{name}{it.multi_index}: "
                "non-finite"
            )

        q = int(x)

        # No tolerance and no rounding.
        if float(q) != x:
            die(
                f"{name}{it.multi_index}: "
                f"binary64 value {x!r} "
                "is not exactly integral"
            )

        out[it.multi_index] = q

    return out


# ============================================================
# Exact Q(sqrt(5)) reconstruction of P
# ============================================================

def q5str(a, b):
    a = Fraction(a)
    b = Fraction(b)

    if b == 0:
        return str(a)

    if a == 0:
        return f"({b})*sqrt(5)"

    sg = "+" if b > 0 else "-"

    return (
        f"({a}) {sg} "
        f"({abs(b)})*sqrt(5)"
    )


def lcm(a, b):
    return abs(
        a // math.gcd(a, b) * b
    )


def reconstruct_P(A, Pfloat):
    """
    Candidate algebraic reconstruction may use floating P,
    but the result is accepted ONLY after the exact identities

       P^T = P,
       diag(P) = 1,
       P^2 = 75 P

    are verified in Q(sqrt(5)).
    """

    groups = {}

    for i in range(N):
        for j in range(N):
            aij = int(A[i, j])
            p = float(Pfloat[i, j])

            carrier = (
                1 if aij >= 0 else -1
            )

            p0 = (
                carrier * p
                if aij != 0
                else p
            )

            key = (
                i == j,
                abs(aij),
                int(round(p0 * 10**12)),
            )

            groups.setdefault(
                key, []
            ).append((i, j, p0))

    ab = {}
    maxerr = 0.0

    for key, vals in groups.items():
        rep = (
            sum(x[2] for x in vals)
            / len(vals)
        )

        if abs(rep) < 5e-14:
            aa = Fraction(0)
            bb = Fraction(0)

        else:
            e = sp.expand(
                sp.radsimp(
                    sp.nsimplify(
                        rep,
                        [SQ5],
                        tolerance=1e-11,
                        full=False,
                    )
                )
            )

            b0 = sp.expand(e).coeff(SQ5)
            a0 = sp.simplify(e - b0 * SQ5)

            if not (
                a0.is_Rational is True
                and b0.is_Rational is True
            ):
                die(
                    "P reconstruction left "
                    "Q(sqrt(5)): "
                    + str(e)
                )

            aa = Fraction(
                int(a0.p), int(a0.q)
            )
            bb = Fraction(
                int(b0.p), int(b0.q)
            )

        appr = (
            float(aa)
            + float(bb) * math.sqrt(5)
        )

        err = max(
            abs(v[2] - appr)
            for v in vals
        )

        maxerr = max(maxerr, err)

        if err > 2e-10:
            die(
                "P reconstruction error "
                f"{err}"
            )

        ab[key] = (aa, bb)

    D = 1

    for aa, bb in ab.values():
        D = lcm(D, aa.denominator)
        D = lcm(D, bb.denominator)

    X = np.zeros(
        (N, N),
        dtype=np.int64
    )
    Y = np.zeros(
        (N, N),
        dtype=np.int64
    )

    for key, vals in groups.items():
        aa, bb = ab[key]

        xa = (
            aa.numerator
            * (D // aa.denominator)
        )
        yb = (
            bb.numerator
            * (D // bb.denominator)
        )

        for i, j, _ in vals:
            aij = int(A[i, j])
            carrier = (
                1 if aij >= 0 else -1
            )

            if aij != 0:
                X[i, j] = carrier * xa
                Y[i, j] = carrier * yb
            else:
                X[i, j] = xa
                Y[i, j] = yb

    if not (
        np.array_equal(X, X.T)
        and np.array_equal(Y, Y.T)
    ):
        die("reconstructed P not symmetric")

    for i in range(N):
        if (
            int(X[i, i]) != D
            or int(Y[i, i]) != 0
        ):
            die(
                "reconstructed diag(P) != 1"
            )

    mx = max(
        abs(int(z))
        for z in X.ravel()
    )
    my = max(
        abs(int(z))
        for z in Y.ravel()
    )

    bound = max(
        N * (mx * mx + 5 * my * my),
        N * 2 * mx * my,
        75 * D * mx,
        75 * D * my,
    )

    if bound < (1 << 62):
        RR = X @ X + 5 * (Y @ Y)
        SS = X @ Y + Y @ X

        ok = (
            np.array_equal(
                RR, (75 * D) * X
            )
            and
            np.array_equal(
                SS, (75 * D) * Y
            )
        )

    else:
        XO = X.astype(object)
        YO = Y.astype(object)

        RR = XO @ XO + 5 * (YO @ YO)
        SS = XO @ YO + YO @ XO

        ok = (
            np.array_equal(
                RR, (75 * D) * XO
            )
            and
            np.array_equal(
                SS, (75 * D) * YO
            )
        )

    if not ok:
        die(
            "exact P^2 = 75 P check failed"
        )

    Nr = sum(
        int(A[i, j]) * int(X[i, j])
        for i in range(N)
        for j in range(N)
    )
    Ns = sum(
        int(A[i, j]) * int(Y[i, j])
        for i in range(N)
        for j in range(N)
    )

    ar = Fraction(Nr, D)
    br = Fraction(Ns, D)

    return {
        "X": X,
        "Y": Y,
        "D": D,
        "a": ar,
        "b": br,
        "max_error": maxerr,
    }


# ============================================================
# Exact P tokens
# ============================================================

def tok(X, Y, i, j):
    return (
        int(X[i, j]),
        int(Y[i, j])
    )


def st(tok0, s):
    return (
        s * tok0[0],
        s * tok0[1]
    )


def key_against(
    X, Y,
    j,
    images,
    signs,
    candidate_sign
):
    return tuple(
        st(
            tok(X, Y, j, images[a]),
            candidate_sign * signs[a]
        )
        for a in range(len(images))
    )


# ============================================================
# Choose an exact spanning four-line base
# ============================================================

def choose_base(X, Y, Pfloat):
    base = [0]

    while len(base) < 4:

        # Count signed fingerprints relative to
        # the current base.
        cnt = collections.Counter()

        for j in range(N):
            for s in (1, -1):
                k = tuple(
                    st(
                        tok(X, Y, j, b),
                        s
                    )
                    for b in base
                )
                cnt[k] += 1

        candidates = []

        for k in range(N):
            if k in base:
                continue

            bb = base + [k]

            # Candidate selection only.
            # Exact nonsingularity is checked below.
            G = Pfloat[np.ix_(bb, bb)]

            if (
                np.linalg.matrix_rank(
                    G,
                    tol=1e-9
                )
                != len(bb)
            ):
                continue

            target = tuple(
                tok(X, Y, k, b)
                for b in base
            )

            candidates.append(
                (
                    cnt[target],
                    k
                )
            )

        if not candidates:
            die(
                "could not extend spanning base"
            )

        candidates.sort()

        base.append(
            candidates[0][1]
        )

    M = sp.Matrix([
        [
            sp.Integer(
                int(X[i, j])
            )
            +
            sp.Integer(
                int(Y[i, j])
            ) * SQ5
            for j in base
        ]
        for i in base
    ])

    det = sp.simplify(M.det())

    if det == 0:
        die(
            "chosen base is not exactly "
            "independent"
        )

    return base, str(det)


# ============================================================
# Exhaustively reconstruct every projective P automorphism
# ============================================================

def enumerate_projective_autos(
    X, Y, base
):
    """
    An orthogonal symmetry is determined by the images of
    four spanning lines.

    We fix the sign on base[0] to +1.  This removes the
    central -I ambiguity.

    Every complete image assignment is then extended to all
    300 lines using exact Gram coordinates relative to the
    spanning base.

    Therefore this enumeration is exhaustive.
    """

    autos = {}

    def recurse(
        a,
        images,
        signs
    ):
        if a == 4:

            lookup = {}

            for j in range(N):
                for s in (1, -1):

                    k = key_against(
                        X, Y,
                        j,
                        images,
                        signs,
                        s
                    )

                    val = (j, s)

                    if (
                        k in lookup
                        and lookup[k] != val
                    ):
                        die(
                            "nonunique signed vector "
                            "from spanning coordinates"
                        )

                    lookup[k] = val

            p = np.empty(
                N,
                dtype=np.uint16
            )
            sg = np.empty(
                N,
                dtype=np.int8
            )

            for k in range(N):

                target = tuple(
                    tok(
                        X, Y,
                        k,
                        base[t]
                    )
                    for t in range(4)
                )

                if target not in lookup:
                    die(
                        "complete base assignment "
                        "does not extend"
                    )

                j, s = lookup[target]

                p[k] = j
                sg[k] = s

            if len(set(
                int(x) for x in p
            )) != N:
                die(
                    "extended map is not "
                    "a permutation"
                )

            pk = p.tobytes()

            if pk in autos:

                old = autos[pk][1]

                if not np.array_equal(
                    old, sg
                ):
                    die(
                        "same projective permutation "
                        "has two normalized lifts"
                    )

            else:
                autos[pk] = (
                    p.copy(),
                    sg.copy()
                )

            return

        # Required inner products between
        # base[a] and previous base lines.
        target = tuple(
            tok(
                X, Y,
                base[a],
                base[c]
            )
            for c in range(a)
        )

        for j in range(N):

            if j in images:
                continue

            for s in (1, -1):

                got = tuple(
                    st(
                        tok(
                            X, Y,
                            j,
                            images[c]
                        ),
                        s * signs[c]
                    )
                    for c in range(a)
                )

                if got == target:

                    recurse(
                        a + 1,
                        images + [j],
                        signs + [s]
                    )

    # base[0] may go to any projective line.
    # Fix its orientation sign to +.
    for j0 in range(N):
        recurse(
            1,
            [j0],
            [1]
        )

    return list(autos.values())


# ============================================================
# Signed monomial maps
# ============================================================

def compose(g, h):
    """
    Apply g, then h.

    x_i --g--> s_i x_{p_i}
        --h--> s_i t_{p_i}
                 x_{q_{p_i}}
    """
    p, s = g
    q, t = h

    return (
        q[p].astype(
            np.uint16,
            copy=False
        ),
        (
            s * t[p]
        ).astype(
            np.int8,
            copy=False
        ),
    )


def identity_map():
    return (
        np.arange(
            N,
            dtype=np.uint16
        ),
        np.ones(
            N,
            dtype=np.int8
        ),
    )


def map_key(g):
    p, s = g

    return (
        p.tobytes()
        +
        np.packbits(
            s > 0
        ).tobytes()
    )


def is_identity(g):
    p, s = g

    return (
        np.array_equal(
            p,
            np.arange(
                N,
                dtype=np.uint16
            )
        )
        and
        np.all(s == 1)
    )


def signed_order(g, max_order=120):
    h = identity_map()

    for k in range(
        1,
        max_order + 1
    ):
        h = compose(h, g)

        if is_identity(h):
            return k

    return None


def preserves_exact_matrix(M, g):
    p, s = g

    R = (
        M[np.ix_(p, p)]
        *
        s[:, None]
        *
        s[None, :]
    )

    return np.array_equal(
        M, R
    )


def geometric_trace_pair(
    X, Y, D, g
):
    """
    P/75 is the exact orthogonal projector onto
    the natural four-dimensional H4 module.

    trace(g | R^4)
       = trace((P/75) T_g).

    Return numerator pair before division by 75D.
    """
    p, s = g

    aa = 0
    bb = 0

    for j in range(N):
        aa += (
            int(s[j])
            * int(X[
                int(p[j]), j
            ])
        )
        bb += (
            int(s[j])
            * int(Y[
                int(p[j]), j
            ])
        )

    return aa, bb


# ============================================================
# Find actual Coxeter H4 generators
# ============================================================

def generate_signed_group(
    generators,
    size_cap=20000
):
    e = identity_map()

    Gp = [e[0].copy()]
    Gs = [e[1].copy()]

    seen = {
        map_key(e): 0
    }

    q = collections.deque([0])

    while q:

        idx = q.popleft()

        h = (
            Gp[idx],
            Gs[idx]
        )

        for gen in generators:

            z = compose(
                h, gen
            )

            k = map_key(z)

            if k not in seen:

                seen[k] = len(Gp)

                Gp.append(
                    z[0].copy()
                )
                Gs.append(
                    z[1].copy()
                )

                q.append(
                    len(Gp) - 1
                )

                if len(Gp) > size_cap:
                    return None

    return (
        np.stack(Gp),
        np.stack(Gs)
    )


def find_h4_coxeter_generators(
    A, X, Y, D, autos
):
    reflections = []

    # A reflection in the exact natural 4D module:
    #   involution + trace 2.
    target_trace_a = (
        2 * 75 * D
    )

    for p, s0 in autos:

        for z in (1, -1):

            s = (
                z * s0
            ).astype(np.int8)

            g = (p, s)

            if signed_order(
                g, max_order=2
            ) != 2:
                continue

            aa, bb = (
                geometric_trace_pair(
                    X, Y, D, g
                )
            )

            if not (
                aa == target_trace_a
                and bb == 0
            ):
                continue

            if not preserves_exact_matrix(
                A, g
            ):
                continue

            if not (
                preserves_exact_matrix(
                    X, g
                )
                and
                preserves_exact_matrix(
                    Y, g
                )
            ):
                continue

            reflections.append(
                (
                    p.copy(),
                    s.copy()
                )
            )

    # Remove accidental duplicates.
    tmp = {}

    for g in reflections:
        tmp[map_key(g)] = g

    reflections = list(
        tmp.values()
    )

    print(
        "reflection candidates =",
        len(reflections),
        file=sys.stderr
    )

    # Pair-product orders.
    cache = {}

    def op(i, j):
        k = (
            min(i, j),
            max(i, j)
        )

        if k not in cache:
            cache[k] = signed_order(
                compose(
                    reflections[i],
                    reflections[j]
                ),
                max_order=30
            )

        return cache[k]

    # H4 Coxeter diagram:
    #
    #   s1 --5-- s2 --3-- s3 --3-- s4
    #
    # nonadjacent pairs commute, i.e. product order 2.
    #
    # Reflection transitivity means fixing a first
    # reflection is sufficient if the complete reflection
    # class was recovered, but loop over all for robustness.
    R = len(reflections)

    for i1 in range(R):

        cand2 = [
            i
            for i in range(R)
            if op(i1, i) == 5
        ]

        for i2 in cand2:

            cand3 = [
                i
                for i in range(R)
                if (
                    op(i2, i) == 3
                    and
                    op(i1, i) == 2
                )
            ]

            for i3 in cand3:

                cand4 = [
                    i
                    for i in range(R)
                    if (
                        op(i3, i) == 3
                        and
                        op(i2, i) == 2
                        and
                        op(i1, i) == 2
                    )
                ]

                for i4 in cand4:

                    gens = [
                        reflections[i1],
                        reflections[i2],
                        reflections[i3],
                        reflections[i4],
                    ]

                    G = generate_signed_group(
                        gens,
                        size_cap=14400
                    )

                    if G is None:
                        continue

                    Gp, Gs = G

                    if len(Gp) != 14400:
                        continue

                    proj_order = len({
                        p.tobytes()
                        for p in Gp
                    })

                    if proj_order != 7200:
                        continue

                    # Exact Coxeter matrix recheck.
                    ords = [
                        [
                            signed_order(
                                compose(
                                    gens[a],
                                    gens[b]
                                ),
                                max_order=10
                            )
                            for b in range(4)
                        ]
                        for a in range(4)
                    ]

                    expected = [
                        [1, 5, 2, 2],
                        [5, 1, 3, 2],
                        [2, 3, 1, 3],
                        [2, 2, 3, 1],
                    ]

                    if ords != expected:
                        continue

                    return {
                        "generators": gens,
                        "Gp": Gp,
                        "Gs": Gs,
                        "reflection_count":
                            len(reflections),
                        "coxeter_matrix":
                            ords,
                    }

    die(
        "could not find an exact "
        "H4 Coxeter generating tuple"
    )


# ============================================================
# Actual signed orbital algebra on the 300 lines
# ============================================================

def true_signed_orbitals(
    A,
    generators
):
    """
    These are orbitals of the ACTUAL signed H4 action.

    No use is made of equality of |A_ij| levels.
    """

    rel = np.full(
        N * N,
        -1,
        dtype=np.int32
    )

    ori = np.zeros(
        N * N,
        dtype=np.int8
    )

    records = []

    rid = 0

    for start in range(N * N):

        if rel[start] >= 0:
            continue

        rel[start] = rid
        ori[start] = 1

        q = collections.deque(
            [start]
        )

        members = []
        conflict = False

        while q:

            z = q.popleft()
            members.append(z)

            i = z // N
            j = z % N

            oz = int(ori[z])

            for p, s in generators:

                ii = int(p[i])
                jj = int(p[j])

                zz = ii * N + jj

                oo = (
                    oz
                    * int(s[i])
                    * int(s[j])
                )

                if rel[zz] < 0:

                    rel[zz] = rid
                    ori[zz] = oo
                    q.append(zz)

                else:

                    if rel[zz] != rid:
                        die(
                            "orbital construction "
                            "crossed relation IDs"
                        )

                    if int(ori[zz]) != oo:
                        conflict = True

        rep_i = start // N
        rep_j = start % N

        if conflict:

            nz = [
                z
                for z in members
                if int(
                    A[
                        z // N,
                        z % N
                    ]
                ) != 0
            ]

            if nz:
                die(
                    "signed orbital has sign "
                    "conflict but A is nonzero"
                )

            coeff = None

        else:

            coeff = int(
                A[
                    rep_i,
                    rep_j
                ]
            )

            for z in members:

                i = z // N
                j = z % N

                if (
                    int(A[i, j])
                    !=
                    coeff
                    * int(ori[z])
                ):
                    die(
                        "A fails invariance on "
                        "a true signed orbital"
                    )

        records.append({
            "support_orbit_id":
                rid,
            "size":
                len(members),
            "representative":
                [rep_i, rep_j],
            "sign_conflict":
                conflict,
            "A_coefficient":
                coeff,
        })

        rid += 1

    rel = rel.reshape(
        N, N
    )
    ori = ori.reshape(
        N, N
    )

    orientable = [
        r
        for r in records
        if not r[
            "sign_conflict"
        ]
    ]

    # Construct the actual invariant orbital basis.
    B = []

    for rec in orientable:

        r = rec[
            "support_orbit_id"
        ]

        M = np.zeros(
            (N, N),
            dtype=np.int16
        )

        mask = (
            rel == r
        )

        M[mask] = ori[mask]

        B.append(M)

    # Verify A expansion.
    R = np.zeros(
        (N, N),
        dtype=np.int64
    )

    coeffs = []

    for M, rec in zip(
        B, orientable
    ):
        c = int(
            rec[
                "A_coefficient"
            ]
        )

        coeffs.append(c)

        R += (
            c
            * M.astype(np.int64)
        )

    if not np.array_equal(
        R, A
    ):
        die(
            "true orbital expansion "
            "does not reconstruct A"
        )

    # Multiplication table in the true invariant algebra.
    #
    # Product of two invariant matrices is invariant.
    # Values on one representative of each orientable signed
    # orbital therefore determine the complete product.
    m = len(B)

    mult = [
        [
            [0] * m
            for _ in range(m)
        ]
        for __ in range(m)
    ]

    reps = [
        rec["representative"]
        for rec in orientable
    ]

    for r in range(m):
        for s in range(m):

            Br = B[r]
            Bs = B[s]

            for t, (i, j) in enumerate(reps):

                v = sum(
                    int(Br[i, k])
                    * int(Bs[k, j])
                    for k in range(N)
                )

                # B_t(rep_t) = +1 by construction.
                mult[r][s][t] = v

    payload = {
        "support_orbits":
            records,

        "orientable_orbital_count":
            m,

        "A_coefficients":
            coeffs,

        "multiplication_table":
            mult,
    }

    raw = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()

    payload[
        "sha256"
    ] = hashlib.sha256(
        raw
    ).hexdigest()

    return payload


# ============================================================
# Degree <=2 Boolean monomial representation
# ============================================================

PAIR_OFFSET = 1 + NV
NPAIRS = NV * (NV - 1) // 2
MON_DIM = PAIR_OFFSET + NPAIRS


def pair_rank(u, v):
    assert 0 <= u < v < NV

    return (
        u * (
            2 * NV - u - 1
        ) // 2
        +
        (v - u - 1)
    )


PAIR_U = np.empty(
    NPAIRS,
    dtype=np.uint16
)
PAIR_V = np.empty(
    NPAIRS,
    dtype=np.uint16
)

def init_pair_tables():
    k = 0

    for u in range(NV - 1):
        for v in range(
            u + 1, NV
        ):
            PAIR_U[k] = u
            PAIR_V[k] = v
            k += 1

    assert k == NPAIRS


def mon_from_id(mid):

    if mid == 0:
        return ()

    if mid < PAIR_OFFSET:
        return (
            mid - 1,
        )

    k = mid - PAIR_OFFSET

    return (
        int(PAIR_U[k]),
        int(PAIR_V[k]),
    )


def mon_to_id(mon):

    if len(mon) == 0:
        return 0

    if len(mon) == 1:
        return 1 + mon[0]

    if len(mon) == 2:

        u, v = sorted(mon)

        return (
            PAIR_OFFSET
            + pair_rank(u, v)
        )

    raise ValueError(
        "degree >2 monomial"
    )


def map_variable(v, p, s):

    if v < N:
        return (
            int(p[v]),
            int(s[v])
        )

    i = v - N

    return (
        N + int(p[i]),
        int(s[i])
    )


def act_monomial_id(
    mid,
    p,
    s
):
    mon = mon_from_id(mid)

    if not mon:
        return 0, 1

    image = []
    sg = 1

    for v in mon:

        vv, ss = map_variable(
            v, p, s
        )

        image.append(vv)
        sg *= ss

    image.sort()

    return (
        mon_to_id(
            tuple(image)
        ),
        sg
    )


def mon_type(mid):

    mon = mon_from_id(mid)

    if len(mon) == 0:
        return "constant"

    if len(mon) == 1:
        return (
            "x"
            if mon[0] < N
            else "y"
        )

    a, b = mon

    if a < N and b < N:
        return "xx"

    if a >= N and b >= N:
        return "yy"

    return "xy"


def monomial_orbit_modules(
    generators,
    Gp,
    Gs
):
    """
    Exact support-orbit decomposition of the degree<=2
    monomial module.

    IMPORTANT:
    These are induced orbit modules, NOT claimed to be
    Wedderburn / irreducible PSD blocks.
    """

    init_pair_tables()

    orb = np.full(
        MON_DIM,
        -1,
        dtype=np.int32
    )

    ori = np.zeros(
        MON_DIM,
        dtype=np.int8
    )

    out = []

    oid = 0

    for start in range(MON_DIM):

        if orb[start] >= 0:
            continue

        orb[start] = oid
        ori[start] = 1

        q = collections.deque(
            [start]
        )

        size = 0
        sign_conflict = False

        while q:

            z = q.popleft()
            size += 1

            oz = int(ori[z])

            for p, s in generators:

                zz, ss = (
                    act_monomial_id(
                        z, p, s
                    )
                )

                oo = oz * ss

                if orb[zz] < 0:

                    orb[zz] = oid
                    ori[zz] = oo
                    q.append(zz)

                else:

                    if orb[zz] != oid:
                        die(
                            "monomial orbit "
                            "crossing error"
                        )

                    if int(ori[zz]) != oo:
                        sign_conflict = True

        # Exact stabilizer character census in full H4.
        plus = 0
        minus = 0

        for k in range(len(Gp)):

            zz, ss = (
                act_monomial_id(
                    start,
                    Gp[k],
                    Gs[k]
                )
            )

            if zz == start:

                if ss == 1:
                    plus += 1
                else:
                    minus += 1

        if (
            (plus + minus) * size
            != len(Gp)
        ):
            die(
                "orbit-stabilizer check failed "
                "for monomial module"
            )

        out.append({
            "orbit_id":
                oid,

            "representative_id":
                start,

            "representative":
                list(
                    mon_from_id(start)
                ),

            "type":
                mon_type(start),

            "dimension":
                size,

            "stabilizer_plus":
                plus,

            "stabilizer_minus":
                minus,

            "negative_stabilizer_character":
                sign_conflict,
        })

        oid += 1

    return out


# ============================================================
# Exact character counts for the full level-2 SOS system
# ============================================================

def boolean_character_coeffs(
    p,
    s,
    kmax
):
    """
    Character of the signed action on squarefree Boolean
    monomials of the 600 variables x_i,y_i.

    A fixed subset must be a union of cycles.
    If a cycle c is selected, its sign contribution is
       product_{i in c} s_i.

    There are two copies of every index cycle: x and y.

    Hence generating function

       prod_c (1 + sigma_c t^{|c|})^2.
    """
    seen = [False] * N
    cycles = []

    for i in range(N):

        if seen[i]:
            continue

        z = i
        L = 0
        sg = 1

        while not seen[z]:

            seen[z] = True
            L += 1
            sg *= int(s[z])

            z = int(p[z])

        cycles.append(
            (L, sg)
        )

    a = [0] * (kmax + 1)
    a[0] = 1

    for L, sg in cycles:

        # Two party copies.
        for _ in range(2):

            b = a[:]

            for d in range(
                0,
                kmax - L + 1
            ):
                b[d + L] += (
                    sg * a[d]
                )

            a = b

    return a


def square_map(p, s):
    return (
        p[p].astype(
            np.uint16,
            copy=False
        ),
        (
            s * s[p]
        ).astype(
            np.int8,
            copy=False
        ),
    )


def level2_character_census(
    Gp,
    Gs
):
    order = len(Gp)

    sum_chi2 = 0
    sum_sym = 0

    invpoly = [0] * 5

    for k in range(order):

        p = Gp[k]
        s = Gs[k]

        c4 = (
            boolean_character_coeffs(
                p, s, 4
            )
        )

        for d in range(5):
            invpoly[d] += c4[d]

        chiW = sum(
            c4[:3]
        )

        p2, s2 = square_map(
            p, s
        )

        c2sq = (
            boolean_character_coeffs(
                p2, s2, 2
            )
        )

        chiW2 = sum(
            c2sq
        )

        sum_chi2 += (
            chiW * chiW
        )

        sum_sym += (
            chiW * chiW
            + chiW2
        )

    if sum_chi2 % order:
        die(
            "commutant Burnside sum "
            "not divisible by |G|"
        )

    if sum_sym % (
        2 * order
    ):
        die(
            "Sym^2 character sum "
            "not divisible by 2|G|"
        )

    dims = []

    for x in invpoly:

        if x % order:
            die(
                "invariant polynomial "
                "character average "
                "not integral"
            )

        dims.append(
            x // order
        )

    comm_dim = (
        sum_chi2 // order
    )

    sym_gram_dim = (
        sum_sym
        // (2 * order)
    )

    constraint_count = sum(dims)

    if sym_gram_dim < constraint_count:
        die(
            "impossible dimension count: "
            "multiplication map should be "
            "surjective"
        )

    return {
        "monomial_basis_dimension":
            MON_DIM,

        "commutant_dimension_EndG_W":
            comm_dim,

        "symmetric_invariant_gram_dimension":
            sym_gram_dim,

        "invariant_boolean_polynomial_dimensions_degree_0_to_4":
            dims,

        "independent_linear_coefficient_constraints":
            constraint_count,

        # The multiplication map
        #
        #    Sym^2(W) -> Boolean monomials degree <=4
        #
        # is surjective because every degree<=4 squarefree
        # monomial factors into two degree<=2 monomials.
        #
        # Since averaging over a finite group in characteristic
        # zero is exact, the restriction to invariant spaces is
        # also surjective.
        "affine_kernel_dimension_before_PSD":
            sym_gram_dim
            - constraint_count,
    }


# ============================================================
# Exact degree-1 SOS obstruction
# ============================================================

def degree1_obstruction(
    C,
    Pa,
    Pb
):
    """
    P satisfies exactly:
      P=P^T,
      diag P=1,
      P^2=75P.

    Hence P is PSD.

    The degree-1 Boolean moment matrix

          [1   0   0]
      M = [0   P   P]
          [0   P   P]

    is PSD.

    Its evaluation on f=C-x^TAy is C-<A,P>.
    """

    da = Fraction(C) - Pa
    db = -Pb

    # N > C, hence C-N <0.
    # Record exact algebraic obstruction.
    return {
        "status":
            "IMPOSSIBLE",

        "pseudoexpectation_value":
            q5str(da, db),

        "moment_matrix":
            "diag(1, [[P,P],[P,P]])",

        "reason":
            (
                "exact PSD degree-2 moment "
                "functional evaluates "
                "C-x^T A y negatively"
            ),
    }


# ============================================================
# Exact group-averaged degree-2 SOS certificate verifier
# ============================================================

def symdiff(a, b):
    return tuple(
        sorted(
            set(a) ^ set(b)
        )
    )


def normalize_cert_monomial(mon):

    mon = list(mon)

    for v in mon:
        if not (
            isinstance(v, int)
            and 0 <= v < NV
        ):
            raise ValueError(
                f"bad variable ID {v}"
            )

    # Boolean reduction modulo z_i^2=1.
    c = collections.Counter(mon)

    out = sorted(
        v
        for v, m in c.items()
        if m % 2
    )

    if len(out) > 2:
        raise ValueError(
            "seed has degree >2"
        )

    return tuple(out)


def transform_support(
    mon,
    p,
    s
):
    out = []
    sg = 1

    for v in mon:

        vv, ss = map_variable(
            v, p, s
        )

        out.append(vv)
        sg *= ss

    out.sort()

    return tuple(out), sg


def verify_certificate(
    cert_path,
    A,
    Gp,
    Gs
):
    with open(
        cert_path, "rb"
    ) as f:
        cert_bytes = f.read()

    cert_sha = hashlib.sha256(
        cert_bytes
    ).hexdigest()

    cert = json.loads(
        cert_bytes
    )

    if cert.get("degree") != 2:
        die(
            "certificate degree must be 2"
        )

    seeds = cert.get(
        "seeds", []
    )

    acc = collections.defaultdict(
        Fraction
    )

    order = len(Gp)

    for seedno, seed in enumerate(seeds):

        w = parse_fraction(
            seed["weight"]
        )

        if w < 0:
            die(
                f"seed {seedno}: "
                "negative SOS weight"
            )

        q0 = collections.defaultdict(
            Fraction
        )

        for coeff, mon in seed["terms"]:

            c = parse_fraction(coeff)

            m = normalize_cert_monomial(
                mon
            )

            q0[m] += c

        q0 = {
            m: c
            for m, c in q0.items()
            if c
        }

        for gi in range(order):

            p = Gp[gi]
            s = Gs[gi]

            q = collections.defaultdict(
                Fraction
            )

            for mon, c in q0.items():

                mm, sg = (
                    transform_support(
                        mon, p, s
                    )
                )

                q[mm] += (
                    sg * c
                )

            terms = [
                (m, c)
                for m, c in q.items()
                if c
            ]

            # Exact square.
            for ma, ca in terms:
                for mb, cb in terms:

                    mm = symdiff(
                        ma, mb
                    )

                    acc[mm] += (
                        w * ca * cb
                    )

    # Reynolds average.
    for m in list(acc):
        acc[m] /= order

        if acc[m] == 0:
            del acc[m]

    # Target constant.
    got = acc.pop(
        (), Fraction(0)
    )

    if got != C:
        die(
            "certificate constant mismatch: "
            f"{got} != {C}"
        )

    # Target bilinear coefficients.
    for i in range(N):
        for j in range(N):

            m = (
                i,
                N + j
            )

            got = acc.pop(
                m,
                Fraction(0)
            )

            want = Fraction(
                -int(A[i, j])
            )

            if got != want:
                die(
                    "certificate x_i y_j "
                    "coefficient mismatch at "
                    f"({i},{j}): "
                    f"{got} != {want}"
                )

    # Everything else must vanish.
    bad = [
        (m, c)
        for m, c in acc.items()
        if c
    ]

    if bad:

        bad.sort(
            key=lambda z: (
                len(z[0]),
                z[0]
            )
        )

        die(
            "certificate has unwanted "
            "coefficient: "
            f"{bad[0]}"
        )

    return {
        "status":
            "PROVED",

        "certificate_sha256":
            cert_sha,

        "seed_count":
            len(seeds),

        "group_order":
            order,
    }


# ============================================================
# Action hash
# ============================================================

def group_sha256(
    Gp, Gs
):
    H = hashlib.sha256()

    keys = []

    for p, s in zip(
        Gp, Gs
    ):
        keys.append(
            map_key((p, s))
        )

    for k in sorted(keys):
        H.update(k)

    return H.hexdigest()


# ============================================================
# Main
# ============================================================

def main():

    if len(sys.argv) not in (
        2, 4
    ):
        die(
            "usage:\n"
            "  python h4_level2_sos.py file.mat\n"
            "  python h4_level2_sos.py "
            "file.mat --verify cert.json"
        )

    path = sys.argv[1]

    verify_path = None

    if len(sys.argv) == 4:

        if sys.argv[2] != "--verify":
            die(
                "expected --verify"
            )

        verify_path = sys.argv[3]

    # --------------------------------------------------------
    # Official bytes and exact A
    # --------------------------------------------------------

    md5 = md5_file(path)

    if md5 != EXPECTED_MD5:
        die(
            f"MD5 {md5} != "
            f"{EXPECTED_MD5}"
        )

    with h5py.File(
        path, "r"
    ) as f:

        A = exact_integer_matrix(
            f["A"][()],
            "A"
        )

        Pfloat = np.asarray(
            f["P"][()],
            dtype=np.float64
        )

    if not np.array_equal(
        A, A.T
    ):
        die(
            "A not exactly symmetric"
        )

    Asha = matrix_sha256(A)

    if Asha != EXPECTED_A_SHA256:
        die(
            "A canonical SHA mismatch: "
            + Asha
        )

    # --------------------------------------------------------
    # Exact P and vector numerator
    # --------------------------------------------------------

    Prec = reconstruct_P(
        A, Pfloat
    )

    X = Prec["X"]
    Y = Prec["Y"]
    D = Prec["D"]

    Pa = Prec["a"]
    Pb = Prec["b"]

    vector_numerator = q5str(
        Pa, Pb
    )

    # --------------------------------------------------------
    # Degree-1 impossibility
    # --------------------------------------------------------

    deg1 = degree1_obstruction(
        EXPECTED_C,
        Pa,
        Pb
    )

    # --------------------------------------------------------
    # Recover complete projective symmetry group from P
    # --------------------------------------------------------

    base, base_det = (
        choose_base(
            X, Y, Pfloat
        )
    )

    print(
        "spanning base =",
        base,
        file=sys.stderr
    )

    autos = (
        enumerate_projective_autos(
            X, Y, base
        )
    )

    if len(autos) != 7200:
        die(
            "expected exactly 7200 "
            "normalized projective "
            "automorphisms, got "
            f"{len(autos)}"
        )

    # --------------------------------------------------------
    # Locate simple reflections and recover H4 exactly
    # --------------------------------------------------------

    H4 = (
        find_h4_coxeter_generators(
            A, X, Y, D, autos
        )
    )

    gens = H4[
        "generators"
    ]

    Gp = H4["Gp"]
    Gs = H4["Gs"]

    if len(Gp) != 14400:
        die(
            "signed H4 order != 14400"
        )

    # Every generator exactly preserves A and P;
    # closure therefore does too.
    for g in gens:

        if not preserves_exact_matrix(
            A, g
        ):
            die(
                "Coxeter generator fails A"
            )

        if not (
            preserves_exact_matrix(
                X, g
            )
            and
            preserves_exact_matrix(
                Y, g
            )
        ):
            die(
                "Coxeter generator fails P"
            )

    group_hash = group_sha256(
        Gp, Gs
    )

    # --------------------------------------------------------
    # Actual signed H4 orbital algebra
    # --------------------------------------------------------

    orbital = true_signed_orbitals(
        A, gens
    )

    orbital_path = (
        path
        + ".true_H4_signed_orbitals.json"
    )

    with open(
        orbital_path, "w"
    ) as f:

        json.dump(
            orbital,
            f,
            sort_keys=True,
            separators=(",", ":"),
        )

    # --------------------------------------------------------
    # Exact degree<=2 monomial orbit modules
    # --------------------------------------------------------

    modules = (
        monomial_orbit_modules(
            gens,
            Gp,
            Gs
        )
    )

    # --------------------------------------------------------
    # Exact invariant degree-2 Gram dimension census
    # --------------------------------------------------------

    census = (
        level2_character_census(
            Gp, Gs
        )
    )

    # --------------------------------------------------------
    # Export complete basis-free reduced level-2 system
    # --------------------------------------------------------

    generators_json = []

    for p, s in gens:

        generators_json.append({
            "perm": [
                int(x)
                for x in p
            ],

            "sign": [
                int(x)
                for x in s
            ],
        })

    system = {
        "mat_md5":
            md5,

        "A_sha256":
            Asha,

        "classical_target_C":
            EXPECTED_C,

        "vector_numerator_exact":
            vector_numerator,

        "P_exact_identity":
            "P^2 = 75 P",

        "degree1_sos":
            deg1,

        "group": {
            "abstract_identification":
                "H4",

            "signed_order":
                14400,

            "projective_order":
                7200,

            "reflection_count":
                H4[
                    "reflection_count"
                ],

            "coxeter_matrix":
                H4[
                    "coxeter_matrix"
                ],

            "spanning_base":
                base,

            "spanning_base_exact_det":
                base_det,

            "full_signed_action_sha256":
                group_hash,

            "coxeter_generators":
                generators_json,
        },

        "true_signed_orbital_algebra": {
            "path":
                orbital_path,

            "sha256":
                orbital[
                    "sha256"
                ],

            "orientable_orbital_count":
                orbital[
                    "orientable_orbital_count"
                ],
        },

        "degree2_sos": {
            # W = squarefree Boolean monomials
            # of degree <= 2 in 600 variables.
            "monomial_module_dimension":
                MON_DIM,

            "monomial_orbit_modules":
                modules,

            "character_census":
                census,

            "exact_system":
                (
                    "Find Q in "
                    "(Sym^2 W)^H4, Q >= 0, "
                    "with mu(Q)=C-x^T A y "
                    "mod z_i^2=1."
                ),

            "multiplication_rule":
                (
                    "squarefree supports "
                    "multiply by symmetric "
                    "difference"
                ),

            "why_coefficient_map_is_surjective":
                (
                    "Every squarefree Boolean "
                    "monomial of degree <=4 "
                    "factors into two monomials "
                    "of degree <=2. "
                    "Reynolds averaging preserves "
                    "surjectivity on H4-invariants."
                ),

            "certificate_representation":
                (
                    "An exact certificate may "
                    "be supplied as rational "
                    "seed polynomials q_k of "
                    "degree <=2 and nonnegative "
                    "rational weights w_k; "
                    "the verifier checks "
                    "(1/14400) sum_g,k "
                    "w_k (g q_k)^2 exactly."
                ),
        },
    }

    system_bytes = json.dumps(
        system,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()

    system_path = (
        path
        + ".H4_level2_exact_system.json"
    )

    with open(
        system_path, "wb"
    ) as f:
        f.write(system_bytes)

    system_sha = hashlib.sha256(
        system_bytes
    ).hexdigest()

    # --------------------------------------------------------
    # Optional exact certificate verification
    # --------------------------------------------------------

    cert_result = None

    if verify_path is not None:

        cert_result = (
            verify_certificate(
                verify_path,
                A,
                Gp,
                Gs
            )
        )

    # --------------------------------------------------------
    # Compact output
    # --------------------------------------------------------

    typ = collections.Counter(
        x["type"]
        for x in modules
    )

    summary = {
        "mat_md5":
            md5,

        "A_sha256":
            Asha,

        "C":
            EXPECTED_C,

        "vector_numerator_exact":
            vector_numerator,

        "degree1_SOS":
            "IMPOSSIBLE",

        "degree1_obstruction_value":
            deg1[
                "pseudoexpectation_value"
            ],

        "projective_P_automorphisms":
            len(autos),

        "signed_H4_order":
            len(Gp),

        "reflection_count":
            H4[
                "reflection_count"
            ],

        "coxeter_matrix":
            H4[
                "coxeter_matrix"
            ],

        "full_signed_action_sha256":
            group_hash,

        "true_signed_orbital_count":
            orbital[
                "orientable_orbital_count"
            ],

        "true_signed_orbital_algebra_sha256":
            orbital[
                "sha256"
            ],

        "degree2_monomial_basis_dimension":
            MON_DIM,

        "degree2_monomial_orbit_module_count":
            len(modules),

        "degree2_monomial_orbit_modules_by_type":
            dict(
                sorted(
                    typ.items()
                )
            ),

        "degree2_commutant_dimension":
            census[
                "commutant_dimension_EndG_W"
            ],

        "degree2_symmetric_invariant_gram_dimension":
            census[
                "symmetric_invariant_gram_dimension"
            ],

        "invariant_polynomial_dimensions_deg0_to4":
            census[
                "invariant_boolean_polynomial_dimensions_degree_0_to_4"
            ],

        "degree2_independent_coefficient_constraints":
            census[
                "independent_linear_coefficient_constraints"
            ],

        "degree2_affine_kernel_dimension_before_PSD":
            census[
                "affine_kernel_dimension_before_PSD"
            ],

        "system_path":
            system_path,

        "system_sha256":
            system_sha,

        "orbital_path":
            orbital_path,

        "certificate_verification":
            cert_result,
    }

    print(
        json.dumps(
            summary,
            indent=2,
            sort_keys=True
        )
    )


if __name__ == "__main__":
    main()
