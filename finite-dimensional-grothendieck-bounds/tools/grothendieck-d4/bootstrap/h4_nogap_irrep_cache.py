#!/usr/bin/env python3
"""
h4_nogap_irrep_cache.py

Python-3.9-compatible, GAP-free exact construction of the GF(24001)
irreducible-representation cache consumed by h4_complete_K_isotypic.py.

Default cache filename (EXACTLY the filename expected by that program):

    <SYSTEM_JSON>.gap_irreps_GF24001.json

For the usual system file this is

    d4_n1_300x300.mat.H4_level2_exact_system.json.gap_irreps_GF24001.json

Usage
-----
Structural self-test only (no archived files needed):

    python h4_nogap_irrep_cache.py --self-test-structural

Construct and validate the cache against the certified signed action:

    python h4_nogap_irrep_cache.py \
        d4_n1_300x300.mat.H4_level2_exact_system.json

Construct cache and immediately invoke the complete-K program (which will
load the cache and therefore will NOT invoke GAP):

    python h4_nogap_irrep_cache.py \
        d4_n1_300x300.mat.H4_level2_exact_system.json \
        --run-complete d4_n1_300x300.mat h4_complete_K_isotypic.py

Dependencies: numpy only for the cache constructor.  The optional complete-K
run has the dependencies of h4_complete_K_isotypic.py (numpy, h5py).

Exact construction
------------------
We construct

    Q = SL(2,5), |Q|=120,
    G = ((Q x Q)/<(-I,-I)>) semidirect C2,

where C2 swaps the two Q factors.  G has 14400 elements.  A deterministic
search finds four involutions satisfying the H4 Coxeter matrix

       1 5 2 2
       5 1 3 2
       2 3 1 3
       2 2 3 1

and verifies that they generate all 14400 elements.

The nine irreducibles of Q over GF(24001) are constructed directly from the
split semisimple group algebra, with no character-table package:

  * enumerate the nine conjugacy classes;
  * diagonalize a deterministic central class-sum combination having nine
    distinct eigenvalues over GF(24001);
  * each primitive central component has rank d^2;
  * extract a d-dimensional left invariant minimal module using an exact
    right-regular eigenspace;
  * verify the nine characters are pairwise orthonormal and that the squared
    degrees sum to 120.

The center parity gives five Q irreps with z=-I acting as +1 and four with
z acting as -1.  Clifford theory for the factor swap then constructs exactly
34 irreducibles of G:

  * U != V, same center parity: one induced irrep of degree 2 dim(U)dim(V);
  * U = V: two extensions, with swap acting as +/- tensor flip, each of
    degree dim(U)^2.

The 34 full characters are checked pairwise orthonormal over GF(24001), and
sum(degree^2)=14400.

Certified-action matching
-------------------------
When SYSTEM_JSON is supplied, its four certified signed 300-line Coxeter
generators are loaded and checked.  The constructor uses the structural
Coxeter BFS parent words to evaluate the SAME words in the certified action,
then verifies the entire labelled Cayley graph generator-by-generator.  Thus
there is an explicit generator-labelled group isomorphism, not merely a
matching abstract order.  It also requires the certified full signed-action
SHA-256

    1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097.

The certified 300-line action is then used to compute the exact character of
W (all squarefree Boolean monomials of degree <=2 in x,y), and the modular
multiplicities of the 34 constructed irreps.  Those residues are promoted to
ordinary integer multiplicities ONLY if both exact global identities hold:

    sum_r d_r m_r = 180301,
    sum_r m_r^2   = 4523179,

and the trivial multiplicity is 55.  If any check fails, no cache is written.

Finite-field audit
------------------
24001 is checked prime by deterministic trial division;
gcd(24001,14400)=1 is checked; the exact element-order census of G is computed
and its lcm is required to equal 60.  Since 60 | 24000, GF(24001) contains a
primitive 60th root of unity.  By the standard splitting-field criterion for
a finite group in nonmodular characteristic, a field containing all roots of
unity whose orders divide the group exponent is a splitting field.  Hence
GF(24001) is a splitting field for H4.

Why modular saturation in h4_complete_K_isotypic.py proves characteristic-0
multiplicity
----------------------------------------------------------------------------
For a matched irreducible rho, an integer matrix over characteristic zero is
reduced modulo 24001.  Rank cannot increase under reduction, so

    rank_Fp <= rank_Q.

The characteristic-zero residual multiplicity also has the representation-
theoretic upper bound

    rank_Q <= min(m_W(rho)-m_D(rho), 14*dim(rho)).

Therefore, if the modular rank equals that upper bound, the two inequalities
force equality and determine the characteristic-zero multiplicity exactly.
This is blockwise; it does not rely on modular semisimplicity alone.  The
splitting-field construction supplies the one-to-one matched irreducible
blocks, while the rank sandwich supplies the characteristic-zero conclusion.

Cache schema
------------
The emitted JSON is exactly accepted by load_or_run_gap_irreps() in the
existing complete-K artifact:

{
  "prime": 24001,
  "action_sha256": "...certified action hash...",
  "gap_meta": {
      "group_order": 14400,
      "exponent": 60,
      "conjugacy_classes": 34
  },
  "irreps": [
      {
        "gap_id": 1,
        "degree": d,
        "generators": [M1,M2,M3,M4]
      }, ... 34 entries ...
  ],
  ...extra no-GAP audit metadata...,
  "cache_sha256": "SHA256(canonical JSON with cache_sha256 removed)"
}

No result about K or SOS is claimed by this constructor itself.
"""

from __future__ import print_function

import sys
import os
import json
import math
import hashlib
import collections
import subprocess

import numpy as np


PRIME = 24001
ORDER_Q = 120
ORDER_G = 14400
N = 300
EXPECTED_ACTION_SHA256 = (
    "1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097"
)
EXPECTED_W_DIM = 180301
EXPECTED_W_COMMUTANT_DIM = 4523179
EXPECTED_W_INVARIANT_DIM = 55

COXETER = (
    (1, 5, 2, 2),
    (5, 1, 3, 2),
    (2, 3, 1, 3),
    (2, 2, 3, 1),
)


def die(msg):
    raise SystemExit("ERROR: " + str(msg))


def canonical_json_bytes(obj):
    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


# =====================================================================
# Elementary exact finite-field arithmetic
# =====================================================================


def is_prime_trial(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def prime_factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.append(n)
    return out


def primitive_root_prime(p):
    fac = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g
    die("could not find primitive root modulo p")


def matmul_mod(A, B, p=PRIME):
    # Dimensions in this program are <= 120.  With p=24001, every
    # scalar product is far below signed-int64 overflow.
    return A.dot(B) % p


def matpow_mod(A, n, p=PRIME):
    R = np.eye(A.shape[0], dtype=np.int64) % p
    B = np.asarray(A, dtype=np.int64) % p
    while n:
        if n & 1:
            R = matmul_mod(R, B, p)
        B = matmul_mod(B, B, p)
        n //= 2
    return R


def rref_mod(A, p=PRIME):
    M = np.asarray(A, dtype=np.int64).copy() % p
    nr, nc = M.shape
    piv = []
    r = 0

    for c in range(nc):
        if r >= nr:
            break
        nz = np.flatnonzero(M[r:, c])
        if len(nz) == 0:
            continue
        q = r + int(nz[0])
        if q != r:
            M[[r, q]] = M[[q, r]]

        inv = pow(int(M[r, c]), p - 2, p)
        M[r] = (M[r] * inv) % p

        rows = np.flatnonzero(M[:, c])
        rows = rows[rows != r]
        for start in range(0, len(rows), 64):
            rr = rows[start:start + 64]
            fac = M[rr, c].copy()
            M[rr] = (
                M[rr]
                - fac[:, None] * M[r][None, :]
            ) % p

        piv.append(c)
        r += 1

    return M, piv


def rank_mod(A, p=PRIME):
    return len(rref_mod(A, p)[1])


def nullspace_mod(A, p=PRIME):
    R, piv = rref_mod(A, p)
    n = R.shape[1]
    pset = set(piv)
    free = [j for j in range(n) if j not in pset]

    B = np.zeros((n, len(free)), dtype=np.int64)
    for k, f in enumerate(free):
        B[f, k] = 1
        for ri, pc in enumerate(piv):
            B[pc, k] = (-int(R[ri, f])) % p
    return B


def inverse_mod(A, p=PRIME):
    A = np.asarray(A, dtype=np.int64).copy() % p
    n = A.shape[0]
    if A.shape != (n, n):
        die("inverse_mod requires square matrix")

    M = np.concatenate(
        [A, np.eye(n, dtype=np.int64)],
        axis=1,
    )

    for c in range(n):
        nz = np.flatnonzero(M[c:, c])
        if len(nz) == 0:
            die("singular matrix in inverse_mod")
        q = c + int(nz[0])
        if q != c:
            M[[c, q]] = M[[q, c]]

        inv = pow(int(M[c, c]), p - 2, p)
        M[c] = (M[c] * inv) % p

        rows = np.arange(n)
        rows = rows[rows != c]
        for start in range(0, len(rows), 64):
            rr = rows[start:start + 64]
            fac = M[rr, c].copy()
            M[rr] = (
                M[rr]
                - fac[:, None] * M[c][None, :]
            ) % p

    if not np.array_equal(
        M[:, :n] % p,
        np.eye(n, dtype=np.int64) % p,
    ):
        die("inverse_mod internal failure")

    return M[:, n:] % p


def column_basis(A, p=PRIME):
    A = np.asarray(A, dtype=np.int64) % p
    # Pivot columns of A are obtained from rref(A).
    _, piv = rref_mod(A, p)
    return A[:, piv].copy(), list(piv)


def pivot_rows_full_column(B, p=PRIME):
    B = np.asarray(B, dtype=np.int64) % p
    _, piv = rref_mod(B.T, p)
    if len(piv) != B.shape[1]:
        die("matrix does not have full column rank")
    return list(piv)


def restrict_operator(B, Y, p=PRIME):
    """Given full-column B and Y in col(B), solve B*T=Y exactly."""
    rows = pivot_rows_full_column(B, p)
    Binv = inverse_mod(B[rows, :], p)
    T = matmul_mod(Binv, Y[rows, :], p)
    if not np.array_equal(matmul_mod(B, T, p), Y % p):
        die("restrict_operator consistency failure")
    return T


def characteristic_polynomial_coeffs(A, p=PRIME):
    """
    det(t I-A)=t^n+c1 t^(n-1)+...+cn, by Newton identities.
    n<=9 in the only use below, and p>n.
    """
    A = np.asarray(A, dtype=np.int64) % p
    n = A.shape[0]
    traces = [0] * (n + 1)
    Pwr = np.eye(n, dtype=np.int64)

    for k in range(1, n + 1):
        Pwr = matmul_mod(Pwr, A, p)
        traces[k] = int(np.trace(Pwr)) % p

    c = [1]
    for k in range(1, n + 1):
        z = 0
        for i in range(1, k + 1):
            z = (z + c[k - i] * traces[i]) % p
        c.append((-z * pow(k, p - 2, p)) % p)
    return c


def poly_eval(coeff, x, p=PRIME):
    z = 0
    for c in coeff:
        z = (z * x + int(c)) % p
    return z


def roots_over_prime_field(coeff, p=PRIME):
    return [x for x in range(p) if poly_eval(coeff, x, p) == 0]


# =====================================================================
# Q = SL(2,5)
# =====================================================================


def qmatmul(A, B):
    a, b, c, d = A
    e, f, g, h = B
    return (
        (a * e + b * g) % 5,
        (a * f + b * h) % 5,
        (c * e + d * g) % 5,
        (c * f + d * h) % 5,
    )


def construct_Q():
    elems = []
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    if (a * d - b * c) % 5 == 1:
                        elems.append((a, b, c, d))

    if len(elems) != ORDER_Q:
        die("SL(2,5) enumeration did not give 120 elements")

    idx = {g: i for i, g in enumerate(elems)}
    I = idx[(1, 0, 0, 1)]
    z = idx[(4, 0, 0, 4)]

    mul = np.empty((ORDER_Q, ORDER_Q), dtype=np.int16)
    for i, A in enumerate(elems):
        for j, B in enumerate(elems):
            mul[i, j] = idx[qmatmul(A, B)]

    inv = np.empty(ORDER_Q, dtype=np.int16)
    for i in range(ORDER_Q):
        found = None
        for j in range(ORDER_Q):
            if int(mul[i, j]) == I and int(mul[j, i]) == I:
                found = j
                break
        if found is None:
            die("SL(2,5) inverse not found")
        inv[i] = found

    zin = mul[z].astype(np.int16)

    # Conjugacy classes.
    unseen = set(range(ORDER_Q))
    classes = []
    class_id = [-1] * ORDER_Q

    while unseen:
        x = min(unseen)
        C = set()
        for g in range(ORDER_Q):
            y = int(mul[int(mul[g, x]), int(inv[g])])
            C.add(y)
        cid = len(classes)
        CC = sorted(C)
        for y in CC:
            class_id[y] = cid
        classes.append(CC)
        unseen.difference_update(C)

    if len(classes) != 9:
        die("SL(2,5) should have 9 conjugacy classes")

    return {
        "elems": elems,
        "idx": idx,
        "I": I,
        "z": z,
        "mul": mul,
        "inv": inv,
        "zin": zin,
        "classes": classes,
        "class_id": class_id,
    }


def q_center_multiplication(Q, p=PRIME):
    classes = Q["classes"]
    mul = Q["mul"]
    nc = len(classes)
    mats = []

    for Ci in classes:
        M = np.zeros((nc, nc), dtype=np.int64)

        for j, Cj in enumerate(classes):
            cnt = [0] * ORDER_Q
            for a in Ci:
                for b in Cj:
                    cnt[int(mul[a, b])] += 1

            for k, Ck in enumerate(classes):
                vals = set(cnt[x] for x in Ck)
                if len(vals) != 1:
                    die("class-sum multiplication is not central")
                M[k, j] = next(iter(vals)) % p

        mats.append(M)

    for i in range(nc):
        for j in range(nc):
            if not np.array_equal(
                matmul_mod(mats[i], mats[j], p),
                matmul_mod(mats[j], mats[i], p),
            ):
                die("center multiplication matrices do not commute")

    return mats


def q_primitive_center_vectors(Q, p=PRIME):
    """
    Find a deterministic central combination with 9 distinct eigenvalues.
    A simple degree-2 class weight works for the canonical SL(2,5)
    enumeration, but the loop is retained as a fail-closed check.
    """
    Zmats = q_center_multiplication(Q, p)
    nc = len(Zmats)

    chosen = None

    for attempt in range(1, 25):
        weights = [pow(i + 2, attempt, p) for i in range(nc)]
        M = np.zeros((nc, nc), dtype=np.int64)
        for i in range(nc):
            M = (M + weights[i] * Zmats[i]) % p

        cp = characteristic_polynomial_coeffs(M, p)
        roots = roots_over_prime_field(cp, p)

        if len(roots) == nc and len(set(roots)) == nc:
            chosen = (attempt, weights, M, roots)
            break

    if chosen is None:
        die("failed to split the 9-dimensional center over GF(24001)")

    attempt, weights, M, roots = chosen
    vecs = []

    for lam in roots:
        E = nullspace_mod(
            (M - lam * np.eye(nc, dtype=np.int64)) % p,
            p,
        )
        if E.shape != (nc, 1):
            die("primitive center eigenspace is not one-dimensional")
        vecs.append(E[:, 0].copy())

    return {
        "attempt": attempt,
        "weights": weights,
        "roots": roots,
        "vectors": vecs,
    }


def q_left_multiplication_of_central_vector(Q, center_vec, p=PRIME):
    mul = Q["mul"]
    cid = Q["class_id"]

    coeff = np.asarray(
        [int(center_vec[cid[g]]) % p for g in range(ORDER_Q)],
        dtype=np.int64,
    )

    L = np.zeros((ORDER_Q, ORDER_Q), dtype=np.int64)

    # L_v delta_h = sum_g v_g delta_{g h}.
    for h in range(ORDER_Q):
        for g in range(ORDER_Q):
            row = int(mul[g, h])
            L[row, h] = (L[row, h] + int(coeff[g])) % p

    return L, coeff


def construct_Q_irreps(Q, p=PRIME):
    """
    Construct the complete nine irreducibles of SL(2,5).

    The final pairwise character-orthogonality and degree-square census are
    independent exact completeness checks.
    """
    center = q_primitive_center_vectors(Q, p)
    mul = Q["mul"]
    invQ = Q["inv"]
    zidx = Q["z"]

    # A primitive 60th root.  Q's exponent divides G's exponent 60.
    primitive = primitive_root_prime(p)
    zeta60 = pow(primitive, (p - 1) // 60, p)
    roots60 = sorted(set(pow(zeta60, k, p) for k in range(60)))

    if len(roots60) != 60:
        die("failed to obtain all 60th roots in GF(24001)")

    right_perm = np.empty((ORDER_Q, ORDER_Q), dtype=np.int16)
    for h in range(ORDER_Q):
        for g in range(ORDER_Q):
            right_perm[h, g] = mul[g, h]

    irreps = []

    for comp_id, cvec in enumerate(center["vectors"]):
        L, coeff = q_left_multiplication_of_central_vector(Q, cvec, p)
        B, piv = column_basis(L, p)
        r = B.shape[1]
        d = int(round(math.sqrt(r)))

        if d * d != r:
            die("primitive Q component rank is not a square")

        # Find a right-regular eigenspace of dimension exactly d.  Right
        # multiplication commutes with all left multiplication, hence this
        # eigenspace is a left Q-submodule.  Inside the primitive simple
        # component M_d(F), dimension d is minimal and therefore irreducible.
        chosen = None

        for h in range(ORDER_Q):
            Y = np.empty_like(B)
            Y[right_perm[h].astype(np.int64), :] = B
            T = restrict_operator(B, Y, p)

            for lam in roots60:
                E = nullspace_mod(
                    (T - lam * np.eye(r, dtype=np.int64)) % p,
                    p,
                )

                if E.shape[1] == d:
                    U = matmul_mod(B, E, p)
                    if rank_mod(U, p) != d:
                        continue
                    chosen = (h, lam, U)
                    break

            if chosen is not None:
                break

        if chosen is None:
            die("failed to extract a minimal Q module from primitive component")

        h_eig, lam_eig, U = chosen
        rows = pivot_rows_full_column(U, p)
        Uinv = inverse_mod(U[rows, :], p)

        rho = []

        for a in range(ORDER_Q):
            perm = mul[a].astype(np.int64)
            Y = np.empty_like(U)
            Y[perm, :] = U
            R = matmul_mod(Uinv, Y[rows, :], p)

            if not np.array_equal(matmul_mod(U, R, p), Y % p):
                die("Q representation coordinate solve failed")

            rho.append(R)

        # Full homomorphism check on a deterministic generating subset is
        # supplemented by character orthogonality below.  Here we check every
        # a against two explicit generators that generate SL(2,5), selected
        # deterministically by subgroup search.
        irreps.append({
            "component_id": comp_id,
            "degree": d,
            "rho": rho,
            "right_eigen_element": int(h_eig),
            "right_eigenvalue": int(lam_eig),
        })

    # Find two deterministic Q generators and verify every representation
    # against all group elements under those right transitions.
    I = Q["I"]

    def subgroup_generated_q(gens):
        seen = set([I])
        q = collections.deque([I])
        while q:
            a = q.popleft()
            for b in gens:
                c = int(mul[a, b])
                if c not in seen:
                    seen.add(c)
                    q.append(c)
        return seen

    qgens = None
    for a in range(ORDER_Q):
        for b in range(a + 1, ORDER_Q):
            if len(subgroup_generated_q([a, b])) == ORDER_Q:
                qgens = [a, b]
                break
        if qgens is not None:
            break

    if qgens is None:
        die("could not find two generators of SL(2,5)")

    for rr in irreps:
        rho = rr["rho"]
        d = rr["degree"]
        if not np.array_equal(rho[I] % p, np.eye(d, dtype=np.int64) % p):
            die("Q representation identity matrix is wrong")

        for a in range(ORDER_Q):
            for b in qgens:
                lhs = matmul_mod(rho[a], rho[b], p)
                rhs = rho[int(mul[a, b])] % p
                if not np.array_equal(lhs, rhs):
                    die("Q representation fails multiplication by generator")

        Z = rho[zidx] % p
        Iden = np.eye(d, dtype=np.int64) % p

        if np.array_equal(Z, Iden):
            parity = +1
        elif np.array_equal(Z, (-Iden) % p):
            parity = -1
        else:
            die("central -I does not act as scalar +/-1 in Q irrep")

        rr["center_parity"] = parity
        rr["character"] = np.asarray(
            [int(np.trace(M)) % p for M in rho],
            dtype=np.int64,
        )

    # Q character orthogonality.
    Gq = np.zeros((len(irreps), len(irreps)), dtype=np.int64)
    inv120 = pow(ORDER_Q % p, p - 2, p)

    for i, ri in enumerate(irreps):
        for j, rj in enumerate(irreps):
            total = 0
            for g in range(ORDER_Q):
                total += (
                    int(ri["character"][g])
                    * int(rj["character"][int(invQ[g])])
                )
            Gq[i, j] = (total % p) * inv120 % p

    if not np.array_equal(Gq, np.eye(9, dtype=np.int64) % p):
        die("nine Q characters are not pairwise orthonormal")

    degrees = sorted(rr["degree"] for rr in irreps)
    if degrees != [1, 2, 2, 3, 3, 4, 4, 5, 6]:
        die("unexpected SL(2,5) irreducible degree census: %r" % degrees)

    if sum(rr["degree"] ** 2 for rr in irreps) != ORDER_Q:
        die("sum of squared Q irrep degrees != 120")

    plus = sorted(rr["degree"] for rr in irreps if rr["center_parity"] == +1)
    minus = sorted(rr["degree"] for rr in irreps if rr["center_parity"] == -1)

    if plus != [1, 3, 3, 4, 5]:
        die("unexpected center-even Q irrep census: %r" % plus)

    if minus != [2, 2, 4, 6]:
        die("unexpected center-odd Q irrep census: %r" % minus)

    return {
        "irreps": irreps,
        "central_split_attempt": center["attempt"],
        "central_split_weights": center["weights"],
        "central_split_roots": center["roots"],
        "primitive_root_mod_p": primitive,
        "primitive_60th_root": zeta60,
        "q_generators": qgens,
        "character_orthogonality": True,
    }


# =====================================================================
# Structural H4 = ((Q x Q)/diag(-1)) semidirect swap
# =====================================================================


def construct_structural_G(Q):
    mulQ = Q["mul"]
    invQ = Q["inv"]
    zin = Q["zin"]
    Iq = Q["I"]

    def canpair(a, b):
        aa = int(zin[a])
        bb = int(zin[b])
        return min((int(a), int(b)), (aa, bb))

    pairs = []
    pair_idx = {}

    for a in range(ORDER_Q):
        for b in range(ORDER_Q):
            cp = canpair(a, b)
            if cp not in pair_idx:
                pair_idx[cp] = len(pairs)
                pairs.append(cp)

    if len(pairs) != 7200:
        die("central product pair quotient does not have 7200 elements")

    def pairmul(Pa, Pb):
        a, b = Pa
        c, d = Pb
        return canpair(
            int(mulQ[a, c]),
            int(mulQ[b, d]),
        )

    def gmul(g, h):
        pid, e = g
        qid, f = h
        A = pairs[pid]
        B = pairs[qid]
        if e:
            B = canpair(B[1], B[0])
        C = pairmul(A, B)
        return (pair_idx[C], (e + f) & 1)

    eid = (pair_idx[canpair(Iq, Iq)], 0)

    def ginv(g):
        pid, e = g
        a, b = pairs[pid]
        if e == 0:
            P = canpair(int(invQ[a]), int(invQ[b]))
        else:
            P = canpair(int(invQ[b]), int(invQ[a]))
        return (pair_idx[P], e)

    def order_of(g, cap=120):
        z = eid
        for k in range(1, cap + 1):
            z = gmul(z, g)
            if z == eid:
                return k
        die("structural element order exceeded cap")

    # All swap-coset involutions.  There are two 60-element conjugacy
    # classes; a lexicographic Coxeter search below chooses a valid H4
    # reflection generating tuple without presupposing which class.
    invol = []
    for pid in range(7200):
        g = (pid, 1)
        if gmul(g, g) == eid:
            invol.append(g)

    if len(invol) != 120:
        die("expected 120 orientation-reversing involutions")

    R = len(invol)
    pair_order = {}

    for i in range(R):
        for j in range(i + 1, R):
            pair_order[(i, j)] = order_of(gmul(invol[i], invol[j]), 60)

    def po(i, j):
        if i == j:
            return 1
        return pair_order[(min(i, j), max(i, j))]

    tuple_idx = None

    for i1 in range(R):
        for i2 in range(R):
            if po(i1, i2) != 5:
                continue
            for i3 in range(R):
                if po(i2, i3) != 3 or po(i1, i3) != 2:
                    continue
                for i4 in range(R):
                    if (
                        po(i3, i4) == 3
                        and po(i2, i4) == 2
                        and po(i1, i4) == 2
                    ):
                        tuple_idx = (i1, i2, i3, i4)
                        break
                if tuple_idx is not None:
                    break
            if tuple_idx is not None:
                break
        if tuple_idx is not None:
            break

    if tuple_idx is None:
        die("failed to find structural H4 Coxeter tuple")

    gens = [invol[i] for i in tuple_idx]

    # Generator-labelled BFS.
    elements = [eid]
    seen = {eid: 0}
    parent = [-1]
    parent_gen = [-1]
    q = collections.deque([0])

    while q:
        a = q.popleft()
        h = elements[a]
        for gi, gen in enumerate(gens):
            z = gmul(h, gen)
            if z not in seen:
                seen[z] = len(elements)
                elements.append(z)
                parent.append(a)
                parent_gen.append(gi)
                q.append(len(elements) - 1)

    if len(elements) != ORDER_G:
        die("structural Coxeter tuple does not generate all 14400 elements")

    right = np.empty((ORDER_G, 4), dtype=np.int32)
    for a, h in enumerate(elements):
        for gi, gen in enumerate(gens):
            right[a, gi] = seen[gmul(h, gen)]

    inv_idx = np.asarray(
        [seen[ginv(g)] for g in elements],
        dtype=np.int32,
    )

    # Full element-order census and exponent.
    census = collections.Counter()
    exponent = 1

    for g in elements:
        o = order_of(g, 120)
        census[o] += 1
        exponent = math.lcm(exponent, o)

    if exponent != 60:
        die("structural H4 exponent is %d, expected 60" % exponent)

    if sum(census.values()) != ORDER_G:
        die("element-order census does not sum to 14400")

    return {
        "pairs": pairs,
        "pair_idx": pair_idx,
        "canpair": canpair,
        "gmul": gmul,
        "ginv": ginv,
        "eid": eid,
        "gens": gens,
        "coxeter_tuple_in_involution_list": tuple_idx,
        "elements": elements,
        "seen": seen,
        "parent": parent,
        "parent_gen": parent_gen,
        "right": right,
        "inv_idx": inv_idx,
        "order_census": dict(sorted(census.items())),
        "exponent": exponent,
    }


# =====================================================================
# Clifford construction of all 34 H4 irreps
# =====================================================================


def kron_mod(A, B, p=PRIME):
    return np.kron(A, B).astype(np.int64) % p


def flip_matrix(du, dv):
    r = du * dv
    F = np.zeros((r, r), dtype=np.int64)
    for i in range(du):
        for j in range(dv):
            F[j * du + i, i * dv + j] = 1
    return F


def blockdiag2(A, B):
    r = A.shape[0]
    s = B.shape[0]
    M = np.zeros((r + s, r + s), dtype=np.int64)
    M[:r, :r] = A
    M[r:, r:] = B
    return M


def construct_H_irreps(Q, Qdata, G, p=PRIME):
    qirreps = Qdata["irreps"]
    pairs = G["pairs"]
    mulQ = Q["mul"]

    metas = []

    # Deterministic ordering by center parity, then Q component IDs as
    # produced by the primitive-center calculation.
    for parity in (+1, -1):
        inds = [
            i for i, rr in enumerate(qirreps)
            if rr["center_parity"] == parity
        ]

        for pos, i in enumerate(inds):
            d = qirreps[i]["degree"]

            metas.append({
                "type": "diagonal_extension",
                "i": i,
                "extension_sign": +1,
                "degree": d * d,
            })

            metas.append({
                "type": "diagonal_extension",
                "i": i,
                "extension_sign": -1,
                "degree": d * d,
            })

            for j in inds[pos + 1:]:
                metas.append({
                    "type": "offdiagonal_induced",
                    "i": i,
                    "j": j,
                    "degree": (
                        2
                        * qirreps[i]["degree"]
                        * qirreps[j]["degree"]
                    ),
                })

    if len(metas) != 34:
        die("Clifford construction did not produce 34 H4 irreps")

    if sum(m["degree"] ** 2 for m in metas) != ORDER_G:
        die("sum of squared H4 irrep degrees != 14400")

    def rep_matrix(meta, g):
        pid, e = g
        a, b = pairs[pid]

        if meta["type"] == "diagonal_extension":
            U = qirreps[meta["i"]]
            d = U["degree"]
            Nmat = kron_mod(U["rho"][a], U["rho"][b], p)

            if not e:
                return Nmat

            F = flip_matrix(d, d)
            T = F if meta["extension_sign"] == +1 else (-F) % p
            return matmul_mod(Nmat, T, p)

        U = qirreps[meta["i"]]
        V = qirreps[meta["j"]]
        du = U["degree"]
        dv = V["degree"]
        r = du * dv

        A = kron_mod(U["rho"][a], V["rho"][b], p)
        B = kron_mod(V["rho"][a], U["rho"][b], p)
        Nmat = blockdiag2(A, B) % p

        if not e:
            return Nmat

        F = flip_matrix(du, dv)
        T = np.zeros((2 * r, 2 * r), dtype=np.int64)
        T[:r, r:] = F.T
        T[r:, :r] = F
        return matmul_mod(Nmat, T, p)

    # Cheap closed character formulas avoid building 34*14400 matrices.
    qchars = [rr["character"] for rr in qirreps]

    def char_value(meta, g):
        pid, e = g
        a, b = pairs[pid]

        if meta["type"] == "offdiagonal_induced":
            if e:
                return 0
            i = meta["i"]
            j = meta["j"]
            return (
                int(qchars[i][a]) * int(qchars[j][b])
                + int(qchars[j][a]) * int(qchars[i][b])
            ) % p

        i = meta["i"]

        if not e:
            return (
                int(qchars[i][a])
                * int(qchars[i][b])
            ) % p

        # tr((rho(a) tensor rho(b)) Flip) = tr(rho(a)rho(b)).
        ab = int(mulQ[a, b])
        sg = meta["extension_sign"]
        return (sg * int(qchars[i][ab])) % p

    elements = G["elements"]
    inv_idx = G["inv_idx"]

    chars = np.empty((34, ORDER_G), dtype=np.int64)
    generator_matrices = []

    for ri, meta in enumerate(metas):
        chars[ri] = [char_value(meta, g) for g in elements]
        mats = [rep_matrix(meta, g) for g in G["gens"]]

        # Exact Coxeter relations on each representation.
        d = meta["degree"]
        Iden = np.eye(d, dtype=np.int64) % p
        for a in range(4):
            for b in range(4):
                Pab = matmul_mod(mats[a], mats[b], p)
                if not np.array_equal(
                    matpow_mod(Pab, COXETER[a][b], p),
                    Iden,
                ):
                    die("constructed H4 irrep fails a Coxeter relation")

        generator_matrices.append(mats)

    # Full 34x34 character orthogonality.
    inv_order = pow(ORDER_G % p, p - 2, p)
    Gram = np.empty((34, 34), dtype=np.int64)

    for i in range(34):
        for j in range(34):
            # Bound: 14400*(p-1)^2 < 2^63, so int64 dot is exact.
            total = int(np.dot(
                chars[i].astype(np.int64),
                chars[j, inv_idx].astype(np.int64),
            ))
            Gram[i, j] = (total % p) * inv_order % p

    if not np.array_equal(Gram, np.eye(34, dtype=np.int64) % p):
        die("34 H4 characters are not pairwise orthonormal")

    # Add useful fingerprints.
    out = []

    for ri, meta in enumerate(metas):
        charraw = b"".join(
            int(x).to_bytes(4, "little", signed=False)
            for x in chars[ri]
        )

        rr = dict(meta)
        rr["character_sha256_mod_p"] = sha256_bytes(charraw)
        rr["generators"] = generator_matrices[ri]
        out.append(rr)

    return {
        "irreps": out,
        "characters": chars,
        "character_orthogonality": True,
        "degree_square_sum": sum(m["degree"] ** 2 for m in metas),
    }


# =====================================================================
# Certified signed action and generator-labelled Cayley isomorphism
# =====================================================================


def signed_compose(g, h):
    p, s = g
    q, t = h
    return (
        q[p].astype(np.uint16, copy=False),
        (s * t[p]).astype(np.int8, copy=False),
    )


def signed_key(g):
    p, s = g
    return p.tobytes() + np.packbits(s > 0).tobytes()


def signed_identity():
    return (
        np.arange(N, dtype=np.uint16),
        np.ones(N, dtype=np.int8),
    )


def signed_order(g, cap=120):
    z = signed_identity()
    for k in range(1, cap + 1):
        z = signed_compose(z, g)
        if signed_key(z) == signed_key(signed_identity()):
            return k
    die("certified signed element order exceeded cap")


def signed_group_sha(elements):
    keys = sorted(signed_key(g) for g in elements)
    H = hashlib.sha256()
    for k in keys:
        H.update(k)
    return H.hexdigest()


def load_and_match_certified_action(system_path, G):
    with open(system_path, "r") as f:
        system = json.load(f)

    gj = system.get("group", {}).get("coxeter_generators")
    if not isinstance(gj, list) or len(gj) != 4:
        die("system JSON does not contain four Coxeter generators")

    cert_gens = []

    for i, gg in enumerate(gj):
        p = np.asarray(gg["perm"], dtype=np.uint16)
        s = np.asarray(gg["sign"], dtype=np.int8)

        if p.shape != (N,) or s.shape != (N,):
            die("certified generator %d has wrong shape" % i)

        if sorted(int(x) for x in p) != list(range(N)):
            die("certified generator %d is not a permutation" % i)

        if not np.all((s == 1) | (s == -1)):
            die("certified generator %d has a non-sign entry" % i)

        cert_gens.append((p, s))

    # Exact Coxeter matrix in the certified action.
    cox = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(signed_order(signed_compose(cert_gens[i], cert_gens[j]), 60))
        cox.append(tuple(row))

    if tuple(cox) != COXETER:
        die("certified generator Coxeter matrix mismatch: %r" % (cox,))

    # Evaluate structural BFS parent words in the certified action.
    cert_elements = [signed_identity()]

    for a in range(1, ORDER_G):
        par = G["parent"][a]
        gi = G["parent_gen"][a]
        cert_elements.append(
            signed_compose(cert_elements[par], cert_gens[gi])
        )

    keys = [signed_key(g) for g in cert_elements]

    if len(set(keys)) != ORDER_G:
        die(
            "structural parent words yield fewer than 14400 certified signed elements"
        )

    key_to_struct_idx = {k: i for i, k in enumerate(keys)}

    # Full labelled Cayley-graph isomorphism: every one of the 14400*4
    # generator transitions must agree.
    for a in range(ORDER_G):
        for gi in range(4):
            z = signed_compose(cert_elements[a], cert_gens[gi])
            k = signed_key(z)
            if k not in key_to_struct_idx:
                die("certified Cayley transition leaves structural word set")
            b = key_to_struct_idx[k]
            if b != int(G["right"][a, gi]):
                die(
                    "generator-labelled Cayley mismatch at structural element %d gen %d"
                    % (a, gi)
                )

    action_sha = signed_group_sha(cert_elements)

    if action_sha != EXPECTED_ACTION_SHA256:
        die(
            "certified full signed action SHA mismatch: %s != %s"
            % (action_sha, EXPECTED_ACTION_SHA256)
        )

    stated = system.get("group", {}).get("full_signed_action_sha256")
    if stated is not None and stated != EXPECTED_ACTION_SHA256:
        die("system JSON states a different full signed action SHA")

    return system, cert_elements, cert_gens, action_sha


# =====================================================================
# Exact W character and global multiplicity audit
# =====================================================================


def W_character_from_certified_elements(cert_elements):
    chiW = np.empty(ORDER_G, dtype=np.int64)
    arange = np.arange(N, dtype=np.uint16)

    for a, (p, s) in enumerate(cert_elements):
        fixed = (p == arange)
        chiV = int(s[fixed].astype(np.int64).sum(dtype=np.int64))
        fixcount = int(fixed.sum())

        p2 = p[p]
        s2 = s * s[p]
        fixed2 = (p2 == arange)
        chiV2 = int(s2[fixed2].astype(np.int64).sum(dtype=np.int64))

        num = chiV * chiV + chiV2
        if num % 2:
            die("Sym^2 character parity failure")

        offdiag_sym2 = num // 2 - fixcount

        # W = 1 + 2V + 2 OffDiagSym^2(V) + V tensor V.
        chiW[a] = (
            1
            + 2 * chiV
            + 2 * offdiag_sym2
            + chiV * chiV
        )

    if int(chiW[0]) != EXPECTED_W_DIM:
        die("W character at identity != 180301")

    if int(chiW.sum()) % ORDER_G:
        die("W invariant character average is not integral")

    if int(chiW.sum()) // ORDER_G != EXPECTED_W_INVARIANT_DIM:
        die("W invariant dimension != 55")

    return chiW


def exact_W_multiplicities(chiW, Hdata, G, p=PRIME):
    chars = Hdata["characters"]
    inv_idx = G["inv_idx"]
    inv_order = pow(ORDER_G % p, p - 2, p)

    residues = []

    for i in range(chars.shape[0]):
        ch = chars[i, inv_idx]
        # chiW can be negative; reduce term-by-term modulo p.  Dot bound is
        # still safely within int64 because |chiW| is <=180301 and d<=48:
        # 14400*180301*24000 ~ 6.2e13 < 2^63.
        total = int(np.dot(
            (chiW % p).astype(np.int64),
            ch.astype(np.int64),
        ))
        residues.append((total % p) * inv_order % p)

    degrees = [rr["degree"] for rr in Hdata["irreps"]]

    dim_from_residues = sum(d * m for d, m in zip(degrees, residues))
    comm_from_residues = sum(m * m for m in residues)

    # Promotion argument: actual multiplicities are nonnegative integers
    # congruent to these residues modulo p.  If their residue representatives
    # already reproduce the exact total dimension, no +p wrap is possible.
    if dim_from_residues != EXPECTED_W_DIM:
        die(
            "mod-p W multiplicity residues give dimension %d, not 180301; "
            "cannot promote them to characteristic-zero integers"
            % dim_from_residues
        )

    if comm_from_residues != EXPECTED_W_COMMUTANT_DIM:
        die(
            "promoted W multiplicities give commutant dimension %d, not 4523179"
            % comm_from_residues
        )

    trivial_candidates = []

    for i, rr in enumerate(Hdata["irreps"]):
        if rr["degree"] != 1:
            continue
        mats = rr["generators"]
        if all(int(M[0, 0]) % p == 1 for M in mats):
            trivial_candidates.append(i)

    if len(trivial_candidates) != 1:
        die("could not identify a unique trivial H4 irrep")

    triv = trivial_candidates[0]

    if residues[triv] != EXPECTED_W_INVARIANT_DIM:
        die(
            "trivial-irrep multiplicity %d != invariant dimension 55"
            % residues[triv]
        )

    return {
        "multiplicities": residues,
        "sum_d_times_m": dim_from_residues,
        "sum_m_squared": comm_from_residues,
        "trivial_irrep_index": triv,
        "trivial_multiplicity": residues[triv],
        "promotion_to_characteristic_zero": True,
    }


# =====================================================================
# Cache serialization
# =====================================================================


def cache_from_Hdata(Hdata, action_sha, G, finite_field_audit, W_audit):
    irreps_json = []

    for i, rr in enumerate(Hdata["irreps"]):
        irreps_json.append({
            "gap_id": i + 1,
            "degree": int(rr["degree"]),
            "generators": [
                M.astype(int).tolist()
                for M in rr["generators"]
            ],
        })

    core = {
        "prime": PRIME,
        "action_sha256": action_sha,
        "gap_meta": {
            "group_order": ORDER_G,
            "exponent": int(G["exponent"]),
            "conjugacy_classes": 34,
        },
        "irreps": irreps_json,
        "nogap_constructor": {
            "schema_version": 1,
            "group_model": "((SL(2,5)xSL(2,5))/<(-I,-I)>) semidirect C2_swap",
            "coxeter_tuple_in_structural_involution_list": list(
                G["coxeter_tuple_in_involution_list"]
            ),
            "finite_field_audit": finite_field_audit,
            "H4_character_orthogonality": True,
            "sum_irrep_degree_squares": Hdata["degree_square_sum"],
            "W_global_audit": W_audit,
            "prior_invariant_seed_SOS_status": "INCONCLUSIVE",
        },
    }

    raw = canonical_json_bytes(core)
    csha = sha256_bytes(raw)

    out = dict(core)
    out["cache_sha256"] = csha

    return out, csha


# =====================================================================
# Main construction
# =====================================================================


def structural_construction():
    # Required arithmetic audit first.
    if not is_prime_trial(PRIME):
        die("24001 is not prime")

    if math.gcd(PRIME, ORDER_G) != 1:
        die("gcd(24001,14400) != 1")

    Q = construct_Q()
    G = construct_structural_G(Q)

    if G["exponent"] != 60:
        die("H4 exponent != 60")

    if (PRIME - 1) % G["exponent"] != 0:
        die("H4 exponent does not divide 24000")

    Qdata = construct_Q_irreps(Q, PRIME)
    Hdata = construct_H_irreps(Q, Qdata, G, PRIME)

    finite_field_audit = {
        "prime": PRIME,
        "primality_trial_division": True,
        "gcd_prime_group_order": math.gcd(PRIME, ORDER_G),
        "group_order": ORDER_G,
        "group_exponent": G["exponent"],
        "p_minus_1": PRIME - 1,
        "exponent_divides_p_minus_1": ((PRIME - 1) % G["exponent"] == 0),
        "splitting_field_conclusion": True,
        "element_order_census": {
            str(k): int(v) for k, v in sorted(G["order_census"].items())
        },
        "SL2_5_irrep_count": len(Qdata["irreps"]),
        "SL2_5_degree_square_sum": sum(
            rr["degree"] ** 2 for rr in Qdata["irreps"]
        ),
        "SL2_5_character_orthogonality": True,
        "H4_irrep_count": len(Hdata["irreps"]),
        "H4_degree_square_sum": Hdata["degree_square_sum"],
        "H4_character_orthogonality": Hdata["character_orthogonality"],
    }

    # Hard required census.
    if finite_field_audit["H4_irrep_count"] != 34:
        die("H4 irrep count != 34")
    if finite_field_audit["H4_degree_square_sum"] != ORDER_G:
        die("H4 degree-square sum != 14400")

    return Q, Qdata, G, Hdata, finite_field_audit


def compact_structural_summary(Qdata, G, Hdata, ff):
    return {
        "status": "STRUCTURAL_SELF_TEST_PASSED",
        "prime": PRIME,
        "primality": True,
        "gcd_24001_14400": math.gcd(PRIME, ORDER_G),
        "group_order": ORDER_G,
        "group_exponent": G["exponent"],
        "element_order_census": ff["element_order_census"],
        "splitting_field": True,
        "SL2_5_irrep_degrees": sorted(rr["degree"] for rr in Qdata["irreps"]),
        "SL2_5_character_orthogonality": True,
        "H4_irrep_count": len(Hdata["irreps"]),
        "H4_irrep_degrees": sorted(rr["degree"] for rr in Hdata["irreps"]),
        "H4_sum_degree_squares": Hdata["degree_square_sum"],
        "H4_character_orthogonality": True,
        "structural_coxeter_tuple": list(G["coxeter_tuple_in_involution_list"]),
        "prior_invariant_seed_SOS_status": "INCONCLUSIVE",
    }


def main(argv):
    if len(argv) == 2 and argv[1] == "--self-test-structural":
        Q, Qdata, G, Hdata, ff = structural_construction()
        print(json.dumps(
            compact_structural_summary(Qdata, G, Hdata, ff),
            indent=2,
            sort_keys=True,
        ))
        return 0

    if len(argv) not in (2, 5):
        die(
            "usage:\n"
            "  python h4_nogap_irrep_cache.py --self-test-structural\n"
            "  python h4_nogap_irrep_cache.py SYSTEM_JSON\n"
            "  python h4_nogap_irrep_cache.py SYSTEM_JSON "
            "--run-complete MAT COMPLETE_K_SCRIPT"
        )

    system_path = argv[1]
    run_complete = False
    mat_path = None
    complete_script = None

    if len(argv) == 5:
        if argv[2] != "--run-complete":
            die("third argument must be --run-complete")
        run_complete = True
        mat_path = argv[3]
        complete_script = argv[4]

    Q, Qdata, G, Hdata, ff = structural_construction()

    system, cert_elements, cert_gens, action_sha = (
        load_and_match_certified_action(system_path, G)
    )

    chiW = W_character_from_certified_elements(cert_elements)
    Waudit0 = exact_W_multiplicities(chiW, Hdata, G, PRIME)

    Waudit = {
        "sum_d_times_m": int(Waudit0["sum_d_times_m"]),
        "sum_m_squared": int(Waudit0["sum_m_squared"]),
        "trivial_irrep_index_zero_based": int(Waudit0["trivial_irrep_index"]),
        "trivial_multiplicity": int(Waudit0["trivial_multiplicity"]),
        "multiplicities_exact": [int(x) for x in Waudit0["multiplicities"]],
        "promotion_to_characteristic_zero": True,
        "certified_generator_labelled_Cayley_isomorphism": True,
        "certified_action_sha256": action_sha,
    }

    cache, csha = cache_from_Hdata(
        Hdata,
        action_sha,
        G,
        ff,
        Waudit,
    )

    cache_path = system_path + ".gap_irreps_GF%d.json" % PRIME

    raw = canonical_json_bytes(cache)
    with open(cache_path, "wb") as f:
        f.write(raw)

    # Re-open and reproduce exactly the verification performed by the
    # complete-K cache loader: remove cache_sha256, canonicalize, hash.
    with open(cache_path, "r") as f:
        check = json.load(f)

    stored = check.pop("cache_sha256")
    check_sha = sha256_bytes(canonical_json_bytes(check))

    if stored != csha or check_sha != csha:
        die("written cache self-hash verification failed")

    summary = {
        "status": "NOGAP_CACHE_PROVED_AND_WRITTEN",
        "cache_path": cache_path,
        "cache_sha256": csha,
        "prime": PRIME,
        "primality": True,
        "gcd_24001_14400": math.gcd(PRIME, ORDER_G),
        "group_order": ORDER_G,
        "group_exponent": G["exponent"],
        "splitting_field": True,
        "H4_irrep_count": len(Hdata["irreps"]),
        "H4_sum_degree_squares": Hdata["degree_square_sum"],
        "H4_character_orthogonality": True,
        "certified_generator_labelled_Cayley_isomorphism": True,
        "full_signed_action_sha256": action_sha,
        "W_dimension_from_multiplicities": Waudit["sum_d_times_m"],
        "W_commutant_dimension_from_multiplicities": Waudit["sum_m_squared"],
        "W_trivial_multiplicity": Waudit["trivial_multiplicity"],
        "prior_invariant_seed_SOS_status": "INCONCLUSIVE",
    }

    print(json.dumps(summary, indent=2, sort_keys=True))

    if run_complete:
        if not os.path.exists(mat_path):
            die("MAT path for --run-complete does not exist: %s" % mat_path)
        if not os.path.exists(complete_script):
            die("complete-K script does not exist: %s" % complete_script)

        # The cache is now present at exactly the filename that the complete
        # script computes from system_path, so no GAP executable is needed.
        proc = subprocess.run(
            [sys.executable, complete_script, mat_path, system_path],
            universal_newlines=True,
        )
        return int(proc.returncode)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
