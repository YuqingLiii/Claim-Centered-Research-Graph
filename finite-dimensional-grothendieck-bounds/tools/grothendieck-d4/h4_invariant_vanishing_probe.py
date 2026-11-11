#!/usr/bin/env python3
"""
h4_invariant_vanishing_probe.py

Exact small-sector probe for the symmetric d=4 Grothendieck instance.

This program does NOT claim completeness for the full degree-2 SOS problem.
It exactly analyzes the trivial-isotypic (H4-invariant seed) sector forced
by the known equality 6-faces.

Usage:
    python h4_invariant_vanishing_probe.py \
        d4_n1_300x300.mat \
        d4_n1_300x300.mat.H4_level2_exact_system.json

Dependencies:
    numpy, h5py, sympy

Decisive arithmetic:
    - A is converted from binary64 only if every entry is exactly integral.
    - all group actions are signed permutations with integer signs;
    - all equality-face restriction matrices are integer;
    - nullspaces are computed over QQ by SymPy;
    - the quick invariant-SOS obstruction uses exact finite-field Gaussian
      elimination only in a logically sufficient full-column-rank case;
    - fallback ranks use exact QQ arithmetic.

What a negative result proves:
    If invariant_seed_SOS_obstruction == PROVED_IMPOSSIBLE, then there is
    no certificate
        f = sum_k q_k^2
    with every q_k individually H4-invariant and deg(q_k)<=2.
    This does NOT exclude covariant/nontrivial-isotypic SOS summands.
"""

import sys
import json
import math
import hashlib
import collections
from fractions import Fraction

import numpy as np
import h5py
import sympy as sp


EXPECTED_MD5 = "b5223ca2fd5c4cbe52e93a23a4570b9f"
EXPECTED_A_SHA = (
    "5fc272a61a97c0aa9f42ef86266756500401c701a6f33a3b30bde4dbe6f113e5"
)
EXPECTED_ACTION_SHA = (
    "1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097"
)
EXPECTED_C = 2081044153087351400

N = 300
NV = 600
PAIR_OFFSET = 1 + NV
NPAIRS = NV * (NV - 1) // 2
MON_DIM = PAIR_OFFSET + NPAIRS


def die(msg):
    raise SystemExit("ERROR: " + msg)


def file_md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def canonical_A_sha(A):
    h = hashlib.sha256()
    for x in A.ravel(order="C"):
        h.update(int(x).to_bytes(8, "little", signed=True))
    return h.hexdigest()


def exact_int_matrix(raw, name):
    a = np.asarray(raw)
    if a.shape != (N, N):
        die(f"{name}: shape {a.shape}, expected {(N,N)}")
    out = np.empty((N, N), dtype=np.int64)
    it = np.nditer(a, flags=["multi_index"])
    for z in it:
        x = float(z)
        if not math.isfinite(x):
            die(f"{name}{it.multi_index}: nonfinite")
        q = int(x)
        if float(q) != x:
            die(f"{name}{it.multi_index}: not exactly integral: {x!r}")
        out[it.multi_index] = q
    return out


def exact_sign_vector(raw, name):
    a = np.asarray(raw).reshape(-1)
    if len(a) != N:
        die(f"{name}: expected {N}, got {len(a)}")
    out = np.empty(N, dtype=np.int8)
    for i, z in enumerate(a):
        x = float(z)
        if x == 1.0:
            out[i] = 1
        elif x == -1.0:
            out[i] = -1
        else:
            die(f"{name}[{i}] is not exactly +/-1: {x!r}")
    return out


# ----------------------------------------------------------------------
# Degree <= 2 monomial indexing
# ----------------------------------------------------------------------

PAIR_U = np.empty(NPAIRS, dtype=np.uint16)
PAIR_V = np.empty(NPAIRS, dtype=np.uint16)

def init_pairs():
    k = 0
    for u in range(NV - 1):
        for v in range(u + 1, NV):
            PAIR_U[k] = u
            PAIR_V[k] = v
            k += 1
    assert k == NPAIRS


def pair_rank(u, v):
    if u > v:
        u, v = v, u
    if u == v:
        raise ValueError("pair_rank requires distinct variables")
    return u * (2 * NV - u - 1) // 2 + (v - u - 1)


def pair_mid(u, v):
    return PAIR_OFFSET + pair_rank(u, v)


def mon_from_id(mid):
    if mid == 0:
        return ()
    if mid < PAIR_OFFSET:
        return (mid - 1,)
    k = mid - PAIR_OFFSET
    return (int(PAIR_U[k]), int(PAIR_V[k]))


def map_variable(v, p, s):
    if v < N:
        return int(p[v]), int(s[v])
    i = v - N
    return N + int(p[i]), int(s[i])


def act_mid(mid, p, s):
    if mid == 0:
        return 0, 1
    if mid < PAIR_OFFSET:
        v, sg = map_variable(mid - 1, p, s)
        return 1 + v, sg

    k = mid - PAIR_OFFSET
    u = int(PAIR_U[k])
    v = int(PAIR_V[k])
    uu, su = map_variable(u, p, s)
    vv, sv = map_variable(v, p, s)
    if uu > vv:
        uu, vv = vv, uu
    return pair_mid(uu, vv), su * sv


# ----------------------------------------------------------------------
# Signed group
# ----------------------------------------------------------------------

def compose(g, h):
    """
    Apply g, then h:
        i --g--> p[i] with sign s[i]
          --h--> q[p[i]] with sign t[p[i]]
    """
    p, s = g
    q, t = h
    return (
        q[p].astype(np.uint16, copy=False),
        (s * t[p]).astype(np.int8, copy=False),
    )


def gkey(g):
    p, s = g
    return p.tobytes() + np.packbits(s > 0).tobytes()


def generate_group(gens):
    e = (
        np.arange(N, dtype=np.uint16),
        np.ones(N, dtype=np.int8),
    )
    P = [e[0].copy()]
    S = [e[1].copy()]
    parent = [-1]
    parent_gen = [-1]
    seen = {gkey(e): 0}
    q = collections.deque([0])

    while q:
        a = q.popleft()
        h = (P[a], S[a])
        for gi, gen in enumerate(gens):
            z = compose(h, gen)
            k = gkey(z)
            if k not in seen:
                seen[k] = len(P)
                P.append(z[0].copy())
                S.append(z[1].copy())
                parent.append(a)
                parent_gen.append(gi)
                q.append(len(P) - 1)
                if len(P) > 14400:
                    die("generated group exceeded 14400")
    return np.stack(P), np.stack(S), parent, parent_gen


def group_sha(GP, GS):
    H = hashlib.sha256()
    keys = []
    for p, s in zip(GP, GS):
        keys.append(p.tobytes() + np.packbits(s > 0).tobytes())
    for k in sorted(keys):
        H.update(k)
    return H.hexdigest()


def preserves_A(A, g):
    p, s = g
    R = A[np.ix_(p, p)] * s[:, None] * s[None, :]
    return np.array_equal(R, A)


# ----------------------------------------------------------------------
# Exact invariant monomial orbit basis
# ----------------------------------------------------------------------

def invariant_monomial_basis(gens, GP, GS):
    """
    Enumerate support orbits in monomials of degree <=2.

    For an orbit to support a one-dimensional invariant vector, the
    stabilizer character must be +1.  We propagate the signed coefficient
    orientation exactly.  A sign conflict means no invariant vector exists
    on that support orbit.

    Returns:
        basis_id[mid] = invariant-basis number, or -1 if no invariant
        orient[mid]   = coefficient +/-1 in that orbit sum
        records       = all support orbit metadata
    """
    rel = np.full(MON_DIM, -1, dtype=np.int32)
    ori = np.zeros(MON_DIM, dtype=np.int8)

    provisional_orbits = []
    oid = 0

    for start in range(MON_DIM):
        if rel[start] >= 0:
            continue

        rel[start] = oid
        ori[start] = 1
        q = collections.deque([start])
        members = []
        conflict = False

        while q:
            z = q.popleft()
            members.append(z)
            oz = int(ori[z])

            for p, s in gens:
                zz, ss = act_mid(z, p, s)
                oo = oz * ss
                if rel[zz] < 0:
                    rel[zz] = oid
                    ori[zz] = oo
                    q.append(zz)
                else:
                    if rel[zz] != oid:
                        die("monomial orbit crossed relation ids")
                    if int(ori[zz]) != oo:
                        conflict = True

        provisional_orbits.append({
            "orbit_id": oid,
            "rep": start,
            "rep_monomial": list(mon_from_id(start)),
            "size": len(members),
            "conflict": conflict,
            "members": members,
        })
        oid += 1

    # Stabilizer character sanity check in the FULL group.
    for rec in provisional_orbits:
        r = rec["rep"]
        plus = 0
        minus = 0
        for p, s in zip(GP, GS):
            rr, ss = act_mid(r, p, s)
            if rr == r:
                if ss == 1:
                    plus += 1
                else:
                    minus += 1
        rec["stabilizer_plus"] = plus
        rec["stabilizer_minus"] = minus

        if (plus + minus) * rec["size"] != len(GP):
            die("orbit-stabilizer identity failed")

        if rec["conflict"] != (minus > 0):
            die("orientation conflict != negative stabilizer character")

    basis_id = np.full(MON_DIM, -1, dtype=np.int16)
    inv_records = []

    for rec in provisional_orbits:
        if rec["conflict"]:
            continue
        b = len(inv_records)
        for mid in rec["members"]:
            basis_id[mid] = b
        inv_records.append({
            k: v for k, v in rec.items() if k != "members"
        })

    return basis_id, ori, provisional_orbits, inv_records


def eval_invariant_basis(z, basis_id, ori, nbasis):
    """
    Exact integer evaluation of each invariant orbit sum.
    """
    vals = np.empty(MON_DIM, dtype=np.int8)
    vals[0] = 1
    vals[1:PAIR_OFFSET] = z
    vals[PAIR_OFFSET:] = z[PAIR_U] * z[PAIR_V]

    mask = basis_id >= 0
    out = np.zeros(nbasis, dtype=np.int64)
    # integer scatter-add; no floating-point summation.
    np.add.at(
        out,
        basis_id[mask].astype(np.int64),
        ori[mask].astype(np.int64) * vals[mask].astype(np.int64),
    )
    return out


# ----------------------------------------------------------------------
# Equality 6-faces and their Fourier restrictions
# ----------------------------------------------------------------------

def face_corners(center, free_vars):
    out = []
    for mask in range(1 << len(free_vars)):
        z = center.copy()
        for a, v in enumerate(free_vars):
            if (mask >> a) & 1:
                z[v] *= -1
        out.append(z)
    return out


def walsh_masks_0_1_2(m=6):
    out = [0]
    out.extend(1 << i for i in range(m))
    for i in range(m):
        for j in range(i + 1, m):
            out.append((1 << i) | (1 << j))
    assert len(out) == 1 + m + m * (m - 1) // 2
    return out


def face_restriction_matrix(face_values):
    """
    face_values: 64 x nbasis exact integer evaluations.
    Returns the unnormalized Walsh/Fourier coefficients of degrees 0,1,2.
    Vanishing is equivalent with or without the factor 1/64.
    """
    W = walsh_masks_0_1_2(6)
    rows = []
    for sm in W:
        r = np.zeros(face_values.shape[1], dtype=object)
        for mask in range(64):
            sg = -1 if ((mask & sm).bit_count() & 1) else 1
            if sg == 1:
                r += face_values[mask].astype(object)
            else:
                r -= face_values[mask].astype(object)
        rows.append([int(x) for x in r])
    return rows


# ----------------------------------------------------------------------
# Target f in invariant orbit coordinates
# ----------------------------------------------------------------------

def target_coeff_mid(A, mid):
    if mid == 0:
        return EXPECTED_C
    if mid < PAIR_OFFSET:
        return 0

    k = mid - PAIR_OFFSET
    u = int(PAIR_U[k])
    v = int(PAIR_V[k])

    # only x_i y_j coefficients
    if u < N and v >= N:
        return -int(A[u, v - N])
    return 0


def target_invariant_coordinates(A, basis_id, ori, nbasis):
    alpha = [None] * nbasis

    for mid in range(MON_DIM):
        c = target_coeff_mid(A, mid)
        b = int(basis_id[mid])

        if b < 0:
            if c != 0:
                die(
                    "target has nonzero coefficient on a "
                    "non-orientable monomial support orbit"
                )
            continue

        want = c * int(ori[mid])

        if alpha[b] is None:
            alpha[b] = want
        elif alpha[b] != want:
            die(
                "target coefficients are not constant in an "
                "actual signed monomial orbit"
            )

    return [0 if x is None else int(x) for x in alpha]


def primitive_integer_vector(v):
    vals = [sp.Rational(x) for x in v]
    D = 1
    for x in vals:
        D = math.lcm(D, int(x.q))
    z = [int(x * D) for x in vals]
    g = 0
    for x in z:
        g = math.gcd(g, abs(x))
    if g:
        z = [x // g for x in z]
    for x in z:
        if x:
            if x < 0:
                z = [-y for y in z]
            break
    return z


# ----------------------------------------------------------------------
# Single/double flip evaluations for the small invariant-seed SOS ansatz
# ----------------------------------------------------------------------

def build_incident_updates(z0, basis_id, ori, nbasis):
    """
    For an invariant quadratic polynomial basis, flipping variable v changes
    its value by -2 times the sum of all monomial contributions containing v.
    """
    base = eval_invariant_basis(z0, basis_id, ori, nbasis)
    inc = np.zeros((NV, nbasis), dtype=np.int64)

    # degree-one invariant components would be handled here if present.
    for v in range(NV):
        mid = 1 + v
        b = int(basis_id[mid])
        if b >= 0:
            inc[v, b] += int(ori[mid]) * int(z0[v])

    # quadratic
    for k in range(NPAIRS):
        mid = PAIR_OFFSET + k
        b = int(basis_id[mid])
        if b < 0:
            continue
        u = int(PAIR_U[k])
        v = int(PAIR_V[k])
        val = int(ori[mid]) * int(z0[u]) * int(z0[v])
        inc[u, b] += val
        inc[v, b] += val

    return base, inc


def pair_basis_contribution(z0, a, b, basis_id, ori, nbasis):
    if a == b:
        return np.zeros(nbasis, dtype=np.int64)
    mid = pair_mid(a, b)
    ob = int(basis_id[mid])
    out = np.zeros(nbasis, dtype=np.int64)
    if ob >= 0:
        out[ob] = int(ori[mid]) * int(z0[a]) * int(z0[b])
    return out


def f_single_flip(A, ax, by, hleft, hright, v):
    if v < N:
        i = v
        return 2 * int(ax[i]) * int(hleft[i])
    j = v - N
    return 2 * int(by[j]) * int(hright[j])


def f_double_flip(A, ax, by, hleft, hright, a, b):
    if a > b:
        a, b = b, a
    fa = f_single_flip(A, ax, by, hleft, hright, a)
    fb = f_single_flip(A, ax, by, hleft, hright, b)

    # Cross x_i / y_j has one bilinear interaction counted twice.
    if a < N <= b:
        i = a
        j = b - N
        correction = 4 * int(A[i, j]) * int(ax[i]) * int(by[j])
        return fa + fb - correction

    return fa + fb


def q_values(invvals, Kcols):
    return [
        sum(int(c) * int(v) for c, v in zip(col, invvals))
        for col in Kcols
    ]


def gram_feature_row(qv):
    """
    If Q is symmetric, q^T Q q uses:
      Q_aa * q_a^2
      Q_ab * (2 q_a q_b), a<b.
    """
    r = len(qv)
    out = []
    for a in range(r):
        out.append(qv[a] * qv[a])
        for b in range(a + 1, r):
            out.append(2 * qv[a] * qv[b])
    return out


def rank_mod(rows, p):
    """
    Exact deterministic Gaussian elimination over F_p.
    Matrix is small here (<= about 2000 x 100).
    """
    if not rows:
        return 0

    A = [[int(x) % p for x in row] for row in rows]
    m = len(A)
    n = len(A[0])
    r = 0

    for c in range(n):
        piv = None
        for i in range(r, m):
            if A[i][c] % p:
                piv = i
                break
        if piv is None:
            continue

        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], p - 2, p)
        A[r] = [(x * inv) % p for x in A[r]]

        for i in range(m):
            if i == r:
                continue
            q = A[i][c] % p
            if q:
                A[i] = [
                    (A[i][j] - q * A[r][j]) % p
                    for j in range(n)
                ]

        r += 1
        if r == m:
            break

    return r


# ----------------------------------------------------------------------
# Exact rational PSD test for a small symmetric matrix
# ----------------------------------------------------------------------

def exact_psd_schur(Q):
    """
    Exact recursive congruence/Schur test.

    For a PSD matrix:
      - a negative diagonal is impossible;
      - a zero diagonal forces its entire row/column to be zero;
      - a positive diagonal allows a Schur-complement reduction.
    """
    M = [[Fraction(x) for x in row] for row in Q]

    while M:
        n = len(M)

        # Any negative diagonal => not PSD.
        for i in range(n):
            if M[i][i] < 0:
                return False

        # Zero diagonal in PSD matrix forces row zero.
        removed = False
        for i in range(n):
            if M[i][i] == 0:
                if any(M[i][j] != 0 for j in range(n)):
                    return False
                M = [
                    [M[r][c] for c in range(n) if c != i]
                    for r in range(n) if r != i
                ]
                removed = True
                break
        if removed:
            continue

        # All diagonal positive: pivot on 0.
        a = M[0][0]
        b = [M[i][0] for i in range(1, n)]
        C = [[M[i][j] for j in range(1, n)] for i in range(1, n)]

        M = [
            [
                C[i][j] - b[i] * b[j] / a
                for j in range(n - 1)
            ]
            for i in range(n - 1)
        ]

    return True


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main():
    if len(sys.argv) != 3:
        die(
            "usage: python h4_invariant_vanishing_probe.py "
            "d4_n1_300x300.mat "
            "d4_n1_300x300.mat.H4_level2_exact_system.json"
        )

    mat_path = sys.argv[1]
    sys_path = sys.argv[2]

    if file_md5(mat_path) != EXPECTED_MD5:
        die("MAT MD5 mismatch")

    with h5py.File(mat_path, "r") as f:
        A = exact_int_matrix(f["A"][()], "A")
        ax = exact_sign_vector(f["ax"][()], "ax")
        by = exact_sign_vector(f["by"][()], "by")

    Asha = canonical_A_sha(A)
    if Asha != EXPECTED_A_SHA:
        die("canonical A SHA256 mismatch")

    with open(sys_path, "r") as f:
        old = json.load(f)

    gj = old["group"]["coxeter_generators"]
    if len(gj) != 4:
        die("expected four Coxeter generators")

    gens = []
    for g in gj:
        p = np.asarray(g["perm"], dtype=np.uint16)
        s = np.asarray(g["sign"], dtype=np.int8)
        if p.shape != (N,) or s.shape != (N,):
            die("bad generator shape")
        if sorted(int(x) for x in p) != list(range(N)):
            die("generator perm is not a permutation")
        if not np.all((s == 1) | (s == -1)):
            die("generator signs are not +/-1")
        if not preserves_A(A, (p, s)):
            die("generator fails exact A invariance")
        gens.append((p, s))

    GP, GS, parent, parent_gen = generate_group(gens)
    if len(GP) != 14400:
        die(f"signed group order {len(GP)} != 14400")

    act_sha = group_sha(GP, GS)
    if act_sha != EXPECTED_ACTION_SHA:
        die(
            "full signed action SHA mismatch: "
            f"{act_sha} != {EXPECTED_ACTION_SHA}"
        )

    projective_order = len({p.tobytes() for p in GP})
    if projective_order != 7200:
        die(f"projective order {projective_order} != 7200")

    # Exact witness and fields.
    hleft = [
        sum(int(A[i, j]) * int(by[j]) for j in range(N))
        for i in range(N)
    ]
    hright = [
        sum(int(ax[i]) * int(A[i, j]) for i in range(N))
        for j in range(N)
    ]
    C = sum(int(ax[i]) * int(A[i, j]) * int(by[j])
            for i in range(N) for j in range(N))
    if C != EXPECTED_C:
        die(f"witness C={C}, expected {EXPECTED_C}")

    Z = [j for j, h in enumerate(hright) if h == 0]
    if Z != [46, 56, 85, 99, 131, 148]:
        die(f"unexpected right-zero set {Z}")

    if any(int(ax[i]) * hleft[i] <= 0 for i in range(N)):
        die("left witness is not strictly best-response")
    if any(int(by[j]) * hright[j] < 0 for j in range(N)):
        die("right witness has a wrong-sign field")

    # Degree <=2 invariant monomial basis.
    init_pairs()
    basis_id, orient, all_orbits, inv_orbits = invariant_monomial_basis(
        gens, GP, GS
    )
    nbasis = len(inv_orbits)

    # The previous character count says 1 + 54 = 55 invariants.
    if nbasis != 55:
        die(
            f"explicit invariant monomial basis has dimension {nbasis}, "
            "expected 55"
        )

    conflict_hist = collections.Counter()
    for rec in all_orbits:
        typ = (
            "constant" if len(rec["rep_monomial"]) == 0 else
            "linear" if len(rec["rep_monomial"]) == 1 else
            "quadratic"
        )
        conflict_hist[(typ, rec["conflict"])] += 1

    # Base equality faces:
    # right face: x=ax fixed, six y coordinates free;
    # left face:  y=ax fixed after swapping (by,ax), same six x coordinates free.
    zR = np.concatenate([ax, by]).astype(np.int8)
    zL = np.concatenate([by, ax]).astype(np.int8)

    corners_R = face_corners(zR, [N + j for j in Z])
    corners_L = face_corners(zL, Z)

    vals_R = np.stack([
        eval_invariant_basis(z, basis_id, orient, nbasis)
        for z in corners_R
    ])
    vals_L = np.stack([
        eval_invariant_basis(z, basis_id, orient, nbasis)
        for z in corners_L
    ])

    RR = face_restriction_matrix(vals_R)
    RL = face_restriction_matrix(vals_L)
    Rrows = RR + RL

    Rsp = sp.Matrix(Rrows)
    restriction_rank = int(Rsp.rank())
    null = Rsp.nullspace()
    nullity = len(null)

    if restriction_rank + nullity != nbasis:
        die("rank-nullity failed")

    # 44 rows imply nullity >= 11, now compute the exact value.
    if nullity < 11:
        die("impossible: 44 equality-face conditions killed >44 dimensions")

    Kcols = [primitive_integer_vector(v) for v in null]

    # Verify every primitive null vector exactly.
    for k, col in enumerate(Kcols):
        if any(
            sum(int(Rrows[i][j]) * int(col[j]) for j in range(nbasis))
            != 0
            for i in range(len(Rrows))
        ):
            die(f"null vector {k} failed exact verification")

    # Target f=C-x^T A y must be one of these vanishing invariant quadratics.
    fvec = target_invariant_coordinates(A, basis_id, orient, nbasis)

    if any(
        sum(int(Rrows[i][j]) * int(fvec[j]) for j in range(nbasis))
        != 0
        for i in range(len(Rrows))
    ):
        die("target f is not in equality-face nullspace")

    # Hash canonical invariant-kernel data.
    kernel_payload = json.dumps(
        {
            "restriction_rows": Rrows,
            "primitive_nullspace_basis": Kcols,
            "target_coordinates": fvec,
        },
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    kernel_sha = hashlib.sha256(kernel_payload).hexdigest()

    # ------------------------------------------------------------------
    # Small, explicitly NON-COMPLETE ansatz:
    # all SOS seed polynomials are individually H4-invariant.
    #
    # Any such seed must lie in the nullspace K above.  Search whether
    # f can be a PSD quadratic form in a basis of K.
    #
    # First try to refute this ansatz by exact evaluations.  If f were
    # in span{q_a q_b}, then at every finite set of Boolean points its
    # evaluation column would lie in the product-evaluation column span.
    # A single exact rank increase therefore proves impossibility.
    # ------------------------------------------------------------------

    base_inv, incident = build_incident_updates(
        zR, basis_id, orient, nbasis
    )

    eval_rows = []
    fvals = []

    # All 600 single flips.
    for v in range(NV):
        invv = base_inv - 2 * incident[v]
        qv = q_values(invv, Kcols)
        eval_rows.append(gram_feature_row(qv))
        fvals.append(
            f_single_flip(A, ax, by, hleft, hright, v)
        )

    # Deterministic extra double flips.  These are NOT random.
    seen_pairs = set()
    for a in range(NV):
        b = (137 * a + 53) % NV
        if b == a:
            b = (b + 1) % NV
        u, v = sorted((a, b))
        if (u, v) in seen_pairs:
            continue
        seen_pairs.add((u, v))

        paircorr = pair_basis_contribution(
            zR, u, v, basis_id, orient, nbasis
        )
        invv = (
            base_inv
            - 2 * incident[u]
            - 2 * incident[v]
            + 4 * paircorr
        )
        qv = q_values(invv, Kcols)
        eval_rows.append(gram_feature_row(qv))
        fvals.append(
            f_double_flip(A, ax, by, hleft, hright, u, v)
        )

    nprod = len(eval_rows[0]) if eval_rows else 0

    obstruction = {
        "status": "INCONCLUSIVE",
        "test_points": len(eval_rows),
        "kernel_dimension": nullity,
        "symmetric_product_columns": nprod,
    }

    # Fast exact sufficient proof over F_p:
    # if product columns are FULL column rank nprod mod p and appending f
    # has rank nprod+1 mod p, then f is not in the product span over Q.
    proof_prime = None
    for p in (1000003, 1000033, 1000037, 1000039, 1000081):
        if not sp.isprime(p):
            continue
        rp = rank_mod(eval_rows, p)
        aug = [
            row + [fv]
            for row, fv in zip(eval_rows, fvals)
        ]
        ra = rank_mod(aug, p)

        if rp == nprod and ra == nprod + 1:
            obstruction = {
                "status": "PROVED_IMPOSSIBLE",
                "meaning": (
                    "No degree-2 SOS certificate exists in which every "
                    "seed polynomial is individually H4-invariant."
                ),
                "proof_type": (
                    "exact finite evaluation rank witness over F_p; "
                    "full product-column rank plus one augmented rank"
                ),
                "prime": p,
                "product_rank_mod_p": rp,
                "augmented_rank_mod_p": ra,
                "test_points": len(eval_rows),
                "kernel_dimension": nullity,
                "symmetric_product_columns": nprod,
            }
            proof_prime = p
            break

    # If the easy sufficient modular certificate does not fire,
    # exact QQ ranks are still small enough for this sector.
    candidate_Q = None

    if proof_prime is None:
        H = sp.Matrix(eval_rows)
        fv = sp.Matrix(fvals)

        rq = int(H.rank())
        raq = int(H.row_join(fv).rank())

        obstruction.update({
            "product_rank_QQ": rq,
            "augmented_rank_QQ": raq,
        })

        if raq > rq:
            obstruction.update({
                "status": "PROVED_IMPOSSIBLE",
                "meaning": (
                    "No degree-2 SOS certificate exists in which every "
                    "seed polynomial is individually H4-invariant."
                ),
                "proof_type": "exact QQ evaluation-rank obstruction",
            })

        elif raq == rq:
            # A relation on the chosen evaluation set exists.
            # Solve one exact system; this is only a candidate polynomial
            # identity until coefficient-wise verification is supplied.
            sol = sp.linsolve((H, fv))
            tup = next(iter(sol))

            # Only analyze if the solution is unique (no free symbols).
            free = set()
            for x in tup:
                free |= x.free_symbols

            if not free:
                qs = [Fraction(int(x.p), int(x.q)) for x in tup]

                # Convert vech coefficients to Q.
                r = nullity
                Q = [[Fraction(0) for _ in range(r)] for __ in range(r)]
                t = 0
                for a in range(r):
                    Q[a][a] = qs[t]
                    t += 1
                    for b in range(a + 1, r):
                        Q[a][b] = qs[t]
                        Q[b][a] = qs[t]
                        t += 1

                psd = exact_psd_schur(Q)

                candidate_Q = {
                    "unique_on_test_set": True,
                    "exact_psd": psd,
                    "Q": [
                        [str(x) for x in row]
                        for row in Q
                    ],
                    "IMPORTANT": (
                        "This is NOT a certificate until the polynomial "
                        "identity is verified coefficient-wise in the "
                        "Boolean quotient.  The current program deliberately "
                        "does not promote test-point agreement to a proof."
                    ),
                }

    # Exact face-value sanity: all 128 corners attain C.
    def objective(z):
        x = z[:N]
        y = z[N:]
        return sum(
            int(x[i]) * int(A[i, j]) * int(y[j])
            for i in range(N) for j in range(N)
        )

    # Only 128 * 90000 integer multiplies would be unnecessary.
    # Prove base faces instead by zero-field algebra:
    right_face_cert = (
        C == EXPECTED_C
        and all(hright[j] == 0 for j in Z)
    )
    # Swapped follows from exact A symmetry.
    left_face_cert = right_face_cert and np.array_equal(A, A.T)

    result = {
        "mat_md5": EXPECTED_MD5,
        "A_sha256": Asha,
        "signed_H4_order": len(GP),
        "projective_order": projective_order,
        "full_signed_action_sha256": act_sha,

        "witness_C_exact": C,
        "right_zero_fields": Z,
        "right_equality_6face_exact": bool(right_face_cert),
        "left_swapped_equality_6face_exact": bool(left_face_cert),

        "degree_le_2_monomial_dimension": MON_DIM,
        "support_orbit_count": len(all_orbits),
        "invariant_degree_le_2_dimension": nbasis,
        "orbit_stabilizer_character_counts": {
            f"{typ}|conflict={str(conflict).lower()}": int(v)
            for (typ, conflict), v in sorted(conflict_hist.items())
        },

        "equality_face_fourier_conditions_per_side": 22,
        "combined_restriction_rows": 44,
        "combined_restriction_rank_QQ": restriction_rank,
        "invariant_vanishing_dimension": nullity,
        "dimension_lower_bound_from_55_minus_44": 11,
        "target_f_in_vanishing_space": True,
        "invariant_kernel_sha256": kernel_sha,

        "invariant_seed_SOS_obstruction": obstruction,
        "candidate_Q_if_any": candidate_Q,

        "scope_warning": (
            "The invariant-seed test covers only the trivial H4 isotypic "
            "component of degree<=2 seed polynomials.  A general group-"
            "averaged SOS may use nontrivial covariant seed modules."
        ),
    }

    outpath = mat_path + ".H4_invariant_vanishing_probe.json"
    payload = json.dumps(
        result, sort_keys=True, separators=(",", ":")
    ).encode()
    with open(outpath, "wb") as f:
        f.write(payload)

    result["output_path"] = outpath
    result["output_sha256"] = hashlib.sha256(payload).hexdigest()

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
