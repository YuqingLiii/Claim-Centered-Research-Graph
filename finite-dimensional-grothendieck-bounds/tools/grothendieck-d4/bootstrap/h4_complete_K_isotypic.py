#!/usr/bin/env python3
"""
h4_complete_K_isotypic.py

Complete equality-face vanishing-module calculation for the exact
300 x 300 H4 Grothendieck instance.

Python: 3.9+
External dependency: GAP >= 4.12 (the command `gap` must be on PATH)
Python dependencies: numpy, h5py

Usage:
  python h4_complete_K_isotypic.py \
      d4_n1_300x300.mat \
      d4_n1_300x300.mat.H4_level2_exact_system.json

What is proved if final_status == "PROVED_COMPLETE_K_DECOMPOSITION":

Let W be the 180301-dimensional real vector space of squarefree Boolean
polynomials in x_0,...,x_299,y_0,...,y_299 of degree <= 2.

Let S be the union of all signed-H4 images of
  (a) the archived right equality 6-face, and
  (b) its x<->y transpose.

Let
    K = { q in W : q(z)=0 for every z in S }.

The program computes the FULL H4-isotypic multiplicities of K.

The proof is exact and uses the following non-modular splitting prime:
    p = 24001.
We verify p is prime in GAP, p does not divide |H4|, and
    exponent(H4) | p-1,
so GF(p) is a splitting field for H4.

The 44 Fourier restrictions per pair of base faces decompose as:
  - 30 degree-two pair-coordinate restrictions.  Their full H4 orbits
    generate an explicit coordinate submodule D.
  - 14 residual restrictions: Fourier degrees 0 and 1 on the two faces.

For each irreducible GF(p)H4-module rho of dimension d, GAP constructs
an exact irreducible representation.  The program computes:
  m_W(rho): multiplicity in W,
  m_D(rho): multiplicity in D,
  r_p(rho): exact rank over GF(p) of the 14-seed group-Fourier Gram block.

Over characteristic zero the residual row-module multiplicity r_Q obeys

    r_p(rho) <= r_Q(rho)
              <= min(m_W(rho)-m_D(rho), 14*d).

Therefore if the finite-field rank equals this upper bound, that block
is proved complete in characteristic zero.

If EVERY irreducible block saturates, then

    m_K(rho) = m_W(rho)-m_D(rho)-r_p(rho)

is exact for every rho, and consequently K itself is completely
determined as an H4-module.

No SOS feasibility or PSD claim is made by this file.

Important exactness point for the large Fourier products:
all input residues are represented in [0,p-1], and

   |H4| (p-1)^2
     = 8294400000000
     < 2^53.

Thus every scalar product of length 14400 used in the NumPy float64
matrix multiplication is an EXACT integer: every product and every
partial nonnegative sum is exactly representable in IEEE binary64.
The program additionally recomputes deterministic entries with Python
arbitrary-precision integers as a sanity check before accepting each
Fourier product.
"""

import sys
import os
import json
import math
import hashlib
import tempfile
import subprocess
import shutil
import collections

import numpy as np
import h5py


# ---------------------------------------------------------------------
# Immutable provenance
# ---------------------------------------------------------------------

EXPECTED_MD5 = "b5223ca2fd5c4cbe52e93a23a4570b9f"
EXPECTED_A_SHA256 = (
    "5fc272a61a97c0aa9f42ef86266756500401c701a6f33a3b30bde4dbe6f113e5"
)
EXPECTED_ACTION_SHA256 = (
    "1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097"
)
EXPECTED_C = 2081044153087351400
EXPECTED_W_DIM = 180301
EXPECTED_W_COMMUTANT_DIM = 4523179
EXPECTED_W_SYMGRAM_DIM = 2265571
EXPECTED_W_INVARIANT_DIM = 55

N = 300
NV = 600
ORDER = 14400

# Prime with p-1 = 24000 divisible by 60.
# p is checked independently by GAP.
PRIME = 24001

# Residual Fourier seeds: empty + 6 singletons on each of 2 faces.
KSEED = 14

# Coxeter matrix for the signed H4 simple reflections.
COXETER = (
    (1, 5, 2, 2),
    (5, 1, 3, 2),
    (2, 3, 1, 3),
    (2, 2, 3, 1),
)


# ---------------------------------------------------------------------
# File / integer utilities
# ---------------------------------------------------------------------

def die(msg):
    raise SystemExit("ERROR: " + str(msg))


def file_md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            b = f.read(1 << 20)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def canonical_A_sha(A):
    h = hashlib.sha256()
    for x in A.ravel(order="C"):
        h.update(int(x).to_bytes(8, "little", signed=True))
    return h.hexdigest()


def exact_int_matrix(raw, name):
    a = np.asarray(raw)
    if a.shape != (N, N):
        die("%s has shape %r, expected (300,300)" % (name, a.shape))
    out = np.empty((N, N), dtype=np.int64)
    it = np.nditer(a, flags=["multi_index"])
    for z in it:
        x = float(z)
        if not math.isfinite(x):
            die("%s%s is nonfinite" % (name, it.multi_index))
        q = int(x)
        # No tolerance and no rounding.
        if float(q) != x:
            die("%s%s is not an exactly integral binary64: %r"
                % (name, it.multi_index, x))
        out[it.multi_index] = q
    return out


def exact_sign_vector(raw, name):
    a = np.asarray(raw).reshape(-1)
    if len(a) != N:
        die("%s has length %d, expected 300" % (name, len(a)))
    out = np.empty(N, dtype=np.int8)
    for i, z in enumerate(a):
        x = float(z)
        if x == 1.0:
            out[i] = 1
        elif x == -1.0:
            out[i] = -1
        else:
            die("%s[%d] is not exactly +/-1: %r" % (name, i, x))
    return out


# ---------------------------------------------------------------------
# Signed H4 group in the 300-line monomial action
# ---------------------------------------------------------------------

def compose(g, h):
    """
    Apply g, then h.

      e_i --g--> s[i] e_{p[i]}
          --h--> s[i] t[p[i]] e_{q[p[i]]}.
    """
    p, s = g
    q, t = h
    return (
        q[p].astype(np.uint16, copy=False),
        (s * t[p]).astype(np.int8, copy=False),
    )


def group_key(g):
    p, s = g
    return p.tobytes() + np.packbits(s > 0).tobytes()


def identity_map():
    return (
        np.arange(N, dtype=np.uint16),
        np.ones(N, dtype=np.int8),
    )


def generate_group(gens):
    """
    BFS enumeration.

    Returns group elements in a deterministic order together with the
    parent word, right-generator transition table, and key->index map.
    """
    e = identity_map()

    GP = [e[0].copy()]
    GS = [e[1].copy()]
    parent = [-1]
    parent_gen = [-1]
    seen = {group_key(e): 0}
    q = collections.deque([0])

    while q:
        idx = q.popleft()
        h = (GP[idx], GS[idx])

        for gi, gen in enumerate(gens):
            z = compose(h, gen)
            k = group_key(z)

            if k not in seen:
                seen[k] = len(GP)
                GP.append(z[0].copy())
                GS.append(z[1].copy())
                parent.append(idx)
                parent_gen.append(gi)
                q.append(len(GP) - 1)

                if len(GP) > ORDER:
                    die("signed group exceeded order 14400")

    GP = np.stack(GP)
    GS = np.stack(GS)

    if len(GP) != ORDER:
        die("generated signed group has order %d, expected 14400" % len(GP))

    # Right multiplication by the four generators.
    right = np.empty((ORDER, 4), dtype=np.int32)

    for idx in range(ORDER):
        h = (GP[idx], GS[idx])
        for gi, gen in enumerate(gens):
            z = compose(h, gen)
            right[idx, gi] = seen[group_key(z)]

    return GP, GS, parent, parent_gen, right, seen



def square_indices(GP, GS, seen):
    sq = np.empty(ORDER, dtype=np.int32)

    for a in range(ORDER):
        z = compose(
            (GP[a], GS[a]),
            (GP[a], GS[a]),
        )
        sq[a] = seen[group_key(z)]

    return sq


def group_sha256(GP, GS):
    keys = []
    for p, s in zip(GP, GS):
        keys.append(p.tobytes() + np.packbits(s > 0).tobytes())
    H = hashlib.sha256()
    for k in sorted(keys):
        H.update(k)
    return H.hexdigest()


def inverse_indices(GP, GS, seen):
    inv = np.empty(ORDER, dtype=np.int32)

    for a in range(ORDER):
        p = GP[a]
        s = GS[a]

        q = np.empty(N, dtype=np.uint16)
        q[p] = np.arange(N, dtype=np.uint16)

        # If e_i -> s_i e_{p_i}, then
        # e_j -> s_{q_j} e_{q_j} under the inverse.
        t = s[q].astype(np.int8, copy=False)

        inv[a] = seen[group_key((q, t))]

    # exact involution sanity
    for a in range(ORDER):
        if int(inv[int(inv[a])]) != a:
            die("inverse table failed involution check")

    return inv


# ---------------------------------------------------------------------
# Pair support orbits and the exact coordinate submodule D
# ---------------------------------------------------------------------

def enumerate_pair_support_orbits(gens):
    """
    H4 support orbits on unordered pairs of the 300 line indices.

    Signs are intentionally ignored here: the degree-two pair Fourier
    equations are coordinate equations c_{ij}=0, so their signed H4
    orbit generates the full coordinate subspace on the corresponding
    SUPPORT orbit regardless of the stabilizer character.
    """
    rel = np.full((N, N), -1, dtype=np.int16)
    records = []
    oid = 0

    for i0 in range(N):
        for j0 in range(i0 + 1, N):
            if rel[i0, j0] >= 0:
                continue

            rel[i0, j0] = oid
            rel[j0, i0] = oid
            q = collections.deque([(i0, j0)])
            members = []

            while q:
                i, j = q.popleft()
                members.append((i, j))

                for p, s in gens:
                    # support action only
                    ii = int(p[i])
                    jj = int(p[j])
                    if ii > jj:
                        ii, jj = jj, ii

                    if rel[ii, jj] < 0:
                        rel[ii, jj] = oid
                        rel[jj, ii] = oid
                        q.append((ii, jj))
                    elif int(rel[ii, jj]) != oid:
                        die("pair support orbit crossed an existing orbit")

            records.append({
                "orbit_id": oid,
                "representative": [i0, j0],
                "size": len(members),
            })
            oid += 1

    if oid != 18:
        die("expected exactly 18 unordered-pair support orbits, got %d" % oid)

    if sum(r["size"] for r in records) != N * (N - 1) // 2:
        die("pair orbit sizes do not sum to C(300,2)")

    return rel, records


def pair_orbit_stabilizer_characters(GP, GS, pair_records):
    """
    For each support orbit representative {i,j}, count stabilizer elements
    acting as +1 or -1 on the polynomial monomial z_i z_j.
    """
    out = []

    for rec in pair_records:
        i, j = rec["representative"]
        plus = 0
        minus = 0

        for p, s in zip(GP, GS):
            pi = int(p[i])
            pj = int(p[j])

            if (
                (pi == i and pj == j)
                or
                (pi == j and pj == i)
            ):
                sg = int(s[i]) * int(s[j])
                if sg == 1:
                    plus += 1
                elif sg == -1:
                    minus += 1
                else:
                    die("bad pair stabilizer sign")

        if (plus + minus) * rec["size"] != ORDER:
            die("pair orbit-stabilizer identity failed")

        rr = dict(rec)
        rr["stabilizer_plus"] = plus
        rr["stabilizer_minus"] = minus
        out.append(rr)

    return out


def build_killed_pair_edges(pair_rel, zero_lines):
    """
    The 15 |S|=2 Fourier constraints on the right equality face set
    y_i y_j coefficients to zero for the 15 pairs among zero_lines.
    H4 propagation kills the complete pair SUPPORT orbits containing
    those pairs.  The transposed face kills the same support orbits in
    the xx party.

    D is therefore two copies of the coordinate span of these edges.
    """
    killed_ids = set()

    for a in range(len(zero_lines)):
        for b in range(a + 1, len(zero_lines)):
            i = zero_lines[a]
            j = zero_lines[b]
            killed_ids.add(int(pair_rel[i, j]))

    eu = []
    ev = []

    for i in range(N):
        for j in range(i + 1, N):
            if int(pair_rel[i, j]) in killed_ids:
                eu.append(i)
                ev.append(j)

    eu = np.asarray(eu, dtype=np.int16)
    ev = np.asarray(ev, dtype=np.int16)

    killed_bool = np.zeros((N, N), dtype=np.bool_)
    killed_bool[eu, ev] = True
    killed_bool[ev, eu] = True

    neigh = []
    for i in range(N):
        js = np.flatnonzero(killed_bool[i]).astype(np.int16)
        neigh.append(js)

    return sorted(killed_ids), eu, ev, killed_bool, neigh


# ---------------------------------------------------------------------
# Equality faces
# ---------------------------------------------------------------------

class Face(object):
    def __init__(self, cx, cy, free_party, free_lines, mode_lines=None, phases=None):
        self.cx = np.asarray(cx, dtype=np.int8)
        self.cy = np.asarray(cy, dtype=np.int8)
        self.free_party = str(free_party)
        self.free_lines = tuple(int(x) for x in free_lines)

        if mode_lines is None:
            # mode 0 = empty; modes 1..6 = the six singleton Fourier modes
            self.mode_lines = (None,) + self.free_lines
        else:
            self.mode_lines = tuple(mode_lines)

        if phases is None:
            self.phases = (1,) * 7
        else:
            self.phases = tuple(int(x) for x in phases)

        if len(self.free_lines) != 6:
            die("every equality face must have six free lines")
        if len(self.mode_lines) != 7 or len(self.phases) != 7:
            die("face mode metadata must have length seven")

    def full_center(self):
        return np.concatenate([self.cx, self.cy]).astype(np.int8)

    def free_vars(self):
        if self.free_party == "x":
            return tuple(self.free_lines)
        if self.free_party == "y":
            return tuple(N + i for i in self.free_lines)
        die("bad free party")

    def singleton_var(self, mode):
        if mode == 0:
            return None
        line = self.mode_lines[mode]
        if self.free_party == "x":
            return int(line)
        return N + int(line)


def transform_face(face, p, s):
    cx = np.empty(N, dtype=np.int8)
    cy = np.empty(N, dtype=np.int8)

    # T_g e_i = s_i e_{p_i}; point centers transform by the same
    # signed monomial matrix:
    #   new[p_i] = s_i old[i].
    cx[p] = s * face.cx
    cy[p] = s * face.cy

    free = tuple(int(p[i]) for i in face.free_lines)

    mode_lines = [None]

    for old_line in face.free_lines:
        mode_lines.append(int(p[old_line]))

    # IMPORTANT: there is no extra Fourier-mode phase here.  The chosen
    # face center transforms too.  For example the singleton Fourier
    # functional has linear coefficient z_i; after the signed action it
    # becomes s_i z_i at p(i), exactly the singleton functional of the
    # transformed center.
    return Face(
        cx,
        cy,
        face.free_party,
        free,
        mode_lines=tuple(mode_lines),
        phases=(1,) * 7,
    )


def faces_equal_as_sets(a, b):
    if a.free_party != b.free_party:
        return False

    FA = set(a.free_lines)
    FB = set(b.free_lines)

    if FA != FB:
        return False

    # Free coordinates are irrelevant to the affine Boolean face center.
    for i in range(N):
        if not (a.free_party == "x" and i in FA):
            if int(a.cx[i]) != int(b.cx[i]):
                return False

        if not (a.free_party == "y" and i in FA):
            if int(a.cy[i]) != int(b.cy[i]):
                return False

    return True


def face_stabilizer_summary(face, GP, GS):
    hist = collections.Counter()
    count = 0
    element_indices = []
    residual_characters = []

    for gi, (p, s) in enumerate(zip(GP, GS)):
        f = transform_face(face, p, s)

        if not faces_equal_as_sets(face, f):
            continue

        count += 1
        element_indices.append(int(gi))

        # Trace on residual 7-dimensional Fourier mode space.
        # empty mode contributes 1.  A singleton contributes its phase
        # only if that free line is fixed.
        ch1 = 1

        # Trace on the 15 pair Fourier modes.
        ch2 = 0

        base_pos = {line: k for k, line in enumerate(face.free_lines)}

        for old in face.free_lines:
            new = int(p[old])
            if new == old:
                ch1 += int(s[old])

        for aa in range(6):
            i = face.free_lines[aa]
            for bb in range(aa + 1, 6):
                j = face.free_lines[bb]
                pi = int(p[i])
                pj = int(p[j])

                if (
                    (pi == i and pj == j)
                    or
                    (pi == j and pj == i)
                ):
                    ch2 += int(s[i]) * int(s[j])

        hist[(ch1, ch2)] += 1
        residual_characters.append(int(ch1))

    if ORDER % count != 0:
        die("face stabilizer size does not divide 14400")

    return {
        "stabilizer_order": count,
        "face_orbit_size": ORDER // count,
        "element_indices": element_indices,
        "residual_characters": residual_characters,
        "residual_pair_character_histogram": {
            "%d,%d" % k: int(v)
            for k, v in sorted(hist.items())
        },
    }


def induced_residual_source_multiplicity(face_info, charvals, inv_idx, prime):
    total = 0
    for gi, chi_u in zip(
        face_info["element_indices"],
        face_info["residual_characters"],
    ):
        total += int(chi_u) * int(charvals[int(inv_idx[int(gi)])])
    residue = (total % prime) * pow(int(face_info["stabilizer_order"]), -1, prime)
    residue %= prime
    if residue > 7 * len(face_info["element_indices"]) * 100:
        die("unexpected wrapped stabilizer multiplicity residue")
    return int(residue)


# ---------------------------------------------------------------------
# Degree <=2 feature-kernel correlation for Fourier face restrictions
# ---------------------------------------------------------------------

def raw_face_kernel_dictionary(faceA, faceB):
    """
    Exact raw inner products of ALL Fourier modes are coefficients of the
    degree<=2 feature kernel

       K_2(u,v)
         = 1 + D + (D^2 - 600)/2,
       D = sum_i u_i v_i.

    The two faces have independent six-bit flip variables.  We encode
    A-face flip bits as 0..5 and B-face flip bits as 6..11.

    Returns a dictionary mask -> exact integer Fourier coefficient.
    """
    zA = faceA.full_center()
    zB = faceB.full_center()

    FA = faceA.free_vars()
    FB = faceB.free_vars()

    posA = {int(v): i for i, v in enumerate(FA)}
    posB = {int(v): 6 + i for i, v in enumerate(FB)}

    Dpoly = collections.defaultdict(int)

    for v in range(NV):
        mask = 0
        if v in posA:
            mask ^= (1 << posA[v])
        if v in posB:
            mask ^= (1 << posB[v])

        Dpoly[mask] += int(zA[v]) * int(zB[v])

    # Twice the kernel avoids fractions:
    #
    #   2 K_2 = 2 - 600 + 2D + D^2.
    K2 = collections.defaultdict(int)
    K2[0] += 2 - NV

    items = list(Dpoly.items())

    for m, c in items:
        K2[m] += 2 * c

    for m, c in items:
        for n, d in items:
            K2[m ^ n] += c * d

    out = {}

    for m, c in K2.items():
        if c % 2:
            die("degree<=2 kernel Fourier coefficient is unexpectedly half-integral")
        out[m] = c // 2

    # Sanity for the same face, empty mode:
    # 1 + 594 + C(594,2) = 176716.
    if faces_equal_as_sets(faceA, faceB):
        # centers on free entries may differ, but the empty Fourier norm
        # is independent of those center signs.
        if out.get(0, 0) != 176716:
            die("same-face empty Fourier norm != 176716")

    return out


def mode_fourier_mask(faceA, modeA, faceB, modeB):
    mask = 0

    if modeA != 0:
        va = faceA.singleton_var(modeA)
        FA = faceA.free_vars()
        try:
            a = FA.index(va)
        except ValueError:
            die("A singleton mode is not in A free set")
        mask ^= (1 << a)

    if modeB != 0:
        vb = faceB.singleton_var(modeB)
        FB = faceB.free_vars()
        try:
            b = FB.index(vb)
        except ValueError:
            die("B singleton mode is not in B free set")
        mask ^= (1 << (6 + b))

    return mask


# ---------------------------------------------------------------------
# Projection away from the pair-coordinate submodule D
# ---------------------------------------------------------------------

def party_center(face, party):
    return face.cx if party == "x" else face.cy


def party_free_set(face, party):
    if face.free_party == party:
        return set(face.free_lines)
    return set()


def mode_line_in_party(face, mode, party):
    if mode == 0:
        return None
    if face.free_party != party:
        return None
    return int(face.mode_lines[mode])


def d_pair_inner_one_party(
    faceA,
    modeA,
    faceB,
    modeB,
    party,
    eu,
    ev,
    killed_bool,
    neigh,
):
    """
    Inner product of the two Fourier-restriction coefficient vectors
    restricted to the killed same-party pair coordinates.

    The formulas are simply the exact support rule

      coeff_{u v}(lambda_{F,S,z}) =
        product_{w in {u,v}} z_w
        if {u,v} cap F = S,
        0 otherwise.

    Here |S| is 0 or 1.
    """
    zA = party_center(faceA, party)
    zB = party_center(faceB, party)

    FA = party_free_set(faceA, party)
    FB = party_free_set(faceB, party)

    sa = mode_line_in_party(faceA, modeA, party)
    sb = mode_line_in_party(faceB, modeB, party)

    # If the mode is a singleton belonging to the OTHER party, this
    # face restriction has no same-party pair coefficients here.
    if modeA != 0 and sa is None:
        return 0
    if modeB != 0 and sb is None:
        return 0

    # empty / empty -- the only dense case
    if sa is None and sb is None:
        if len(eu) == 0:
            return 0

        mask = np.ones(len(eu), dtype=np.bool_)

        if FA:
            f = np.zeros(N, dtype=np.bool_)
            f[list(FA)] = True
            mask &= (~f[eu]) & (~f[ev])

        if FB:
            f = np.zeros(N, dtype=np.bool_)
            f[list(FB)] = True
            mask &= (~f[eu]) & (~f[ev])

        uu = eu[mask].astype(np.int64)
        vv = ev[mask].astype(np.int64)

        # Every summand is +/-1; int64 is far from overflow.
        vals = (
            zA[uu].astype(np.int64)
            * zA[vv].astype(np.int64)
            * zB[uu].astype(np.int64)
            * zB[vv].astype(np.int64)
        )

        return int(vals.sum(dtype=np.int64))

    # singleton A / empty B
    if sa is not None and sb is None:
        if sa in FB:
            return 0

        total = 0

        for w0 in neigh[sa]:
            w = int(w0)

            if w in FA or w in FB:
                continue

            total += (
                int(zA[sa])
                * int(zA[w])
                * int(zB[sa])
                * int(zB[w])
            )

        return total

    # empty A / singleton B
    if sa is None and sb is not None:
        if sb in FA:
            return 0

        total = 0

        for w0 in neigh[sb]:
            w = int(w0)

            if w in FA or w in FB:
                continue

            total += (
                int(zA[sb])
                * int(zA[w])
                * int(zB[sb])
                * int(zB[w])
            )

        return total

    # singleton / singleton
    if sa == sb:
        total = 0

        for w0 in neigh[sa]:
            w = int(w0)

            if w in FA or w in FB:
                continue

            total += (
                int(zA[sa]) * int(zA[w])
                * int(zB[sa]) * int(zB[w])
            )

        return total

    # Different singleton centers can intersect only on their common edge.
    if (
        bool(killed_bool[sa, sb])
        and sb not in FA
        and sa not in FB
    ):
        return (
            int(zA[sa]) * int(zA[sb])
            * int(zB[sa]) * int(zB[sb])
        )

    return 0


def d_pair_inner(
    faceA,
    modeA,
    faceB,
    modeB,
    eu,
    ev,
    killed_bool,
    neigh,
):
    return (
        d_pair_inner_one_party(
            faceA, modeA, faceB, modeB,
            "x", eu, ev, killed_bool, neigh
        )
        +
        d_pair_inner_one_party(
            faceA, modeA, faceB, modeB,
            "y", eu, ev, killed_bool, neigh
        )
    )


# ---------------------------------------------------------------------
# 14 x 14 exact correlation function C(g)
# ---------------------------------------------------------------------

def residual_seed_correlation(
    base_faces,
    transformed_faces,
    eu,
    ev,
    killed_bool,
    neigh,
):
    C = np.zeros((KSEED, KSEED), dtype=np.int64)

    for a_face in range(2):
        Aface = base_faces[a_face]

        for b_face in range(2):
            Bface = transformed_faces[b_face]

            rawdict = raw_face_kernel_dictionary(Aface, Bface)

            for ma in range(7):
                row = 7 * a_face + ma

                for mb in range(7):
                    col = 7 * b_face + mb

                    mask = mode_fourier_mask(
                        Aface, ma, Bface, mb
                    )

                    raw = int(rawdict.get(mask, 0))

                    dpair = d_pair_inner(
                        Aface, ma, Bface, mb,
                        eu, ev, killed_bool, neigh
                    )

                    # The transformed face center already absorbs the
                    # signed monomial action, so there is no additional
                    # singleton phase here.
                    C[row, col] = raw - dpair

    return C


def build_all_correlations(
    base_faces,
    GP,
    GS,
    inv_idx,
    eu,
    ev,
    killed_bool,
    neigh,
):
    Corr = np.empty((ORDER, KSEED, KSEED), dtype=np.int64)

    for a in range(ORDER):
        p = GP[a]
        s = GS[a]

        tf = [
            transform_face(base_faces[0], p, s),
            transform_face(base_faces[1], p, s),
        ]

        Corr[a] = residual_seed_correlation(
            base_faces, tf,
            eu, ev, killed_bool, neigh
        )

        if (a + 1) % 500 == 0:
            print(
                "correlations: %d / %d" % (a + 1, ORDER),
                file=sys.stderr,
            )

    # Orthogonal representation sanity:
    # C(g^{-1}) = C(g)^T.
    for a in range(ORDER):
        b = int(inv_idx[a])
        if not np.array_equal(Corr[b], Corr[a].T):
            die(
                "residual correlation sign/action check failed at group index %d"
                % a
            )

    return Corr



# ---------------------------------------------------------------------
# Direct coefficient-vector audit of the compact correlation formulas
# ---------------------------------------------------------------------

def all_boolean_pair_arrays():
    pu = np.empty(NV * (NV - 1) // 2, dtype=np.int16)
    pv = np.empty_like(pu)
    k = 0
    for u in range(NV - 1):
        for v in range(u + 1, NV):
            pu[k] = u
            pv[k] = v
            k += 1
    if k != len(pu):
        die("global Boolean pair enumeration failed")
    return pu, pv


def direct_residual_seed_matrix(face, killed_bool, pu, pv):
    """
    Build the seven residual Fourier restriction vectors directly in the
    standard degree<=2 coefficient basis, then orthogonally project off D
    by zeroing exactly the killed xx/yy pair coordinates.

    This is intentionally independent of raw_face_kernel_dictionary() and
    d_pair_inner().  It is used only as a sign/projection audit.
    """
    M = 1 + NV + len(pu)
    R = np.zeros((7, M), dtype=np.int8)

    z = face.full_center()
    free = set(face.free_vars())
    fmask = np.zeros(NV, dtype=np.bool_)
    if free:
        fmask[list(free)] = True

    pair_coeff = (
        z[pu.astype(np.int64)]
        * z[pv.astype(np.int64)]
    ).astype(np.int8)

    # D consists exactly of killed same-party unordered pair coordinates.
    dmask = np.zeros(len(pu), dtype=np.bool_)

    bothx = (pu < N) & (pv < N)
    if np.any(bothx):
        ii = pu[bothx].astype(np.int64)
        jj = pv[bothx].astype(np.int64)
        dmask[bothx] = killed_bool[ii, jj]

    bothy = (pu >= N) & (pv >= N)
    if np.any(bothy):
        ii = (pu[bothy] - N).astype(np.int64)
        jj = (pv[bothy] - N).astype(np.int64)
        dmask[bothy] = killed_bool[ii, jj]

    # Empty Fourier mode.
    R[0, 0] = 1
    keep_linear = ~fmask
    R[0, 1:1 + NV][keep_linear] = z[keep_linear]

    keep_pair0 = (
        (~fmask[pu.astype(np.int64)])
        & (~fmask[pv.astype(np.int64)])
        & (~dmask)
    )
    R[0, 1 + NV:][keep_pair0] = pair_coeff[keep_pair0]

    # Singleton Fourier modes.
    for mode in range(1, 7):
        sv = face.singleton_var(mode)

        R[mode, 1 + sv] = int(z[sv])

        contains = (
            (pu == sv)
            | (pv == sv)
        )

        other = np.where(
            pu == sv,
            pv,
            pu,
        ).astype(np.int64)

        keep = (
            contains
            & (~fmask[other])
            & (~dmask)
        )

        R[mode, 1 + NV:][keep] = pair_coeff[keep]

    return R


def direct_correlation_audit(
    faces,
    gens,
    right,
    Corr,
    killed_bool,
    GP,
    GS,
):
    """
    Check Corr(g)=<r_a,g r_b> by explicit coefficient vectors for
    g=e and for all four Coxeter generators.

    int32 products are exact because every vector coefficient is 0,+/-1
    and there are only 180301 coordinates.
    """
    pu, pv = all_boolean_pair_arrays()

    base = np.vstack([
        direct_residual_seed_matrix(faces[0], killed_bool, pu, pv),
        direct_residual_seed_matrix(faces[1], killed_bool, pu, pv),
    ]).astype(np.int32)

    tests = [0] + [int(right[0, gi]) for gi in range(4)]

    for a in tests:
        p = GP[a]
        s = GS[a]

        tf = [
            transform_face(faces[0], p, s),
            transform_face(faces[1], p, s),
        ]

        trans = np.vstack([
            direct_residual_seed_matrix(tf[0], killed_bool, pu, pv),
            direct_residual_seed_matrix(tf[1], killed_bool, pu, pv),
        ]).astype(np.int32)

        direct = base.dot(trans.T).astype(np.int64)

        if not np.array_equal(direct, Corr[a]):
            bad = np.argwhere(direct != Corr[a])[0]
            i = int(bad[0])
            j = int(bad[1])
            die(
                "direct residual-correlation audit failed at group %d, "
                "entry (%d,%d): direct=%d compact=%d"
                % (
                    a, i, j,
                    int(direct[i, j]),
                    int(Corr[a, i, j]),
                )
            )

    return {
        "audited_group_indices": tests,
        "identity_and_four_Coxeter_generators": True,
        "coefficient_basis_dimension": int(base.shape[1]),
    }


# ---------------------------------------------------------------------
# Exact characters of W and D
# ---------------------------------------------------------------------

def exact_W_and_D_characters(GP, GS, eu, ev):
    chiW = np.empty(ORDER, dtype=np.int64)
    chiD = np.empty(ORDER, dtype=np.int64)

    EU = eu.astype(np.int64)
    EV = ev.astype(np.int64)

    for a in range(ORDER):
        p = GP[a]
        s = GS[a]

        fixed = (p == np.arange(N, dtype=np.uint16))

        chiV = int(
            s[fixed].astype(np.int64).sum(dtype=np.int64)
        )

        fixcount = int(fixed.sum())

        p2 = p[p]
        s2 = s * s[p]

        fixed2 = (p2 == np.arange(N, dtype=np.uint16))

        chiV2 = int(
            s2[fixed2].astype(np.int64).sum(dtype=np.int64)
        )

        # Off-diagonal squarefree symmetric-square trace.
        num = chiV * chiV + chiV2
        if num % 2:
            die("Sym^2 character parity failure")

        pairtrace_all = num // 2 - fixcount

        # W = 1 + 2 V + 2 OffDiagSym^2(V) + V tensor V.
        chiW[a] = (
            1
            + 2 * chiV
            + 2 * pairtrace_all
            + chiV * chiV
        )

        if len(EU):
            pu = p[EU]
            pv = p[EV]

            pair_fixed = (
                ((pu == EU) & (pv == EV))
                |
                ((pu == EV) & (pv == EU))
            )

            pair_sign = (
                s[EU].astype(np.int64)
                * s[EV].astype(np.int64)
            )

            tr_one_party = int(
                pair_sign[pair_fixed].sum(dtype=np.int64)
            )
        else:
            tr_one_party = 0

        # D has identical killed-pair coordinate modules in xx and yy.
        chiD[a] = 2 * tr_one_party

    if int(chiW.sum()) % ORDER:
        die("W invariant character average is nonintegral")

    invdim = int(chiW.sum()) // ORDER

    if invdim != EXPECTED_W_INVARIANT_DIM:
        die(
            "W invariant dimension %d != expected 55"
            % invdim
        )

    return chiW, chiD


# ---------------------------------------------------------------------
# GAP exact finite-field irreducible representations
# ---------------------------------------------------------------------

def signed_generator_as_perm600(p, s):
    """
    Point convention:
      1..300   = +e_i
      301..600 = -e_i
    """
    images = [0] * (2 * N)

    for i in range(N):
        j = int(p[i])
        sg = int(s[i])

        if sg == 1:
            images[i] = j + 1
            images[N + i] = N + j + 1
        elif sg == -1:
            images[i] = N + j + 1
            images[N + i] = j + 1
        else:
            die("bad signed generator entry")

    if sorted(images) != list(range(1, 2 * N + 1)):
        die("signed 600-point generator is not a permutation")

    return images


def write_gap_script(path, gens, prime):
    perm_lists = [
        signed_generator_as_perm600(p, s)
        for p, s in gens
    ]

    with open(path, "w") as f:
        f.write('SetInfoLevel(InfoWarning,0);;\n')

        for gi, im in enumerate(perm_lists):
            f.write(
                "g%d:=PermList([%s]);;\n"
                % (gi + 1, ",".join(str(x) for x in im))
            )

        f.write("gens:=[g1,g2,g3,g4];;\n")
        f.write("G:=Group(gens);;\n")
        f.write("p:=%d;;\n" % prime)
        f.write(
            'if not IsPrimeInt(p) then Error("p not prime"); fi;;\n'
        )
        f.write("ex:=Exponent(G);;\n")
        f.write(
            'if (p-1) mod ex <> 0 then '
            'Error("GF(p) does not contain all exponent roots"); fi;;\n'
        )
        f.write("F:=GF(p);;\n")
        f.write(
            'Print("META ",Size(G)," ",ex," ",'
            'NrConjugacyClasses(G),"\\n");\n'
        )
        f.write(
            "reps:=IrreducibleRepresentations(G,F);;\n"
        )
        f.write(
            'Print("NREP ",Length(reps),"\\n");\n'
        )
        f.write("for ri in [1..Length(reps)] do\n")
        f.write("  hom:=reps[ri];;\n")
        f.write("  M:=Image(hom,gens[1]);;\n")
        f.write("  d:=Length(M);;\n")
        f.write('  Print("REP ",ri," ",d,"\\n");\n')
        f.write("  for gi in [1..4] do\n")
        f.write("    M:=Image(hom,gens[gi]);;\n")
        f.write('    Print("GEN ",gi);\n')
        f.write("    for r in [1..d] do\n")
        f.write("      for c in [1..d] do\n")
        f.write('        Print(" ",IntFFE(M[r][c]));\n')
        f.write("      od;\n")
        f.write("    od;\n")
        f.write('    Print("\\n");\n')
        f.write("  od;\n")
        f.write('  Print("ENDREP\\n");\n')
        f.write("od;\n")
        f.write('Print("DONE\\n");\n')
        f.write("QUIT;\n")


def parse_gap_irreps(text, prime):
    meta = None
    nrep = None
    reps = []
    cur = None

    for raw in text.splitlines():
        line = raw.strip()

        if not line:
            continue

        if line.startswith("META "):
            z = line.split()
            meta = {
                "group_order": int(z[1]),
                "exponent": int(z[2]),
                "conjugacy_classes": int(z[3]),
            }

        elif line.startswith("NREP "):
            nrep = int(line.split()[1])

        elif line.startswith("REP "):
            z = line.split()
            cur = {
                "gap_id": int(z[1]),
                "degree": int(z[2]),
                "gens": [None] * 4,
            }

        elif line.startswith("GEN "):
            if cur is None:
                die("GAP GEN line outside REP block")

            z = line.split()
            gi = int(z[1]) - 1
            d = cur["degree"]
            vals = [int(x) % prime for x in z[2:]]

            if len(vals) != d * d:
                die(
                    "GAP generator matrix has %d entries, expected %d"
                    % (len(vals), d * d)
                )

            cur["gens"][gi] = np.asarray(
                vals, dtype=np.int64
            ).reshape(d, d)

        elif line == "ENDREP":
            if cur is None:
                die("ENDREP without REP")
            if any(x is None for x in cur["gens"]):
                die("incomplete GAP generator block")
            reps.append(cur)
            cur = None

        elif line == "DONE":
            pass

        else:
            # GAP may print progress/info lines depending on installation.
            # Unknown lines are retained only in stderr by the caller when
            # verbose; they are not parsed as mathematical output.
            pass

    if meta is None or nrep is None:
        die("failed to parse GAP metadata")

    if len(reps) != nrep:
        die(
            "parsed %d GAP reps, declared %d"
            % (len(reps), nrep)
        )

    if meta["group_order"] != ORDER:
        die(
            "GAP group order %d != 14400"
            % meta["group_order"]
        )

    if (prime - 1) % meta["exponent"] != 0:
        die("chosen finite field is not splitting by exponent criterion")

    if nrep != meta["conjugacy_classes"]:
        die(
            "GAP returned %d irreps but group has %d classes"
            % (nrep, meta["conjugacy_classes"])
        )

    if sum(r["degree"] ** 2 for r in reps) != ORDER:
        die("sum of squared GAP irrep degrees != |H4|")

    return meta, reps


def load_or_run_gap_irreps(gens, action_sha, prime, cache_path):
    if os.path.exists(cache_path):
        with open(cache_path, "r") as f:
            js = json.load(f)

        if (
            js.get("prime") == prime
            and js.get("action_sha256") == action_sha
        ):
            stored_sha = js.get("cache_sha256")

            core = dict(js)
            core.pop("cache_sha256", None)

            check_raw = json.dumps(
                core,
                sort_keys=True,
                separators=(",", ":"),
            ).encode()

            check_sha = sha256_bytes(check_raw)

            if stored_sha != check_sha:
                die(
                    "cached GAP irrep file SHA mismatch: "
                    "%r != %s" % (stored_sha, check_sha)
                )

            meta = js["gap_meta"]

            if meta["group_order"] != ORDER:
                die("cached GAP group order != 14400")

            if (prime - 1) % int(meta["exponent"]) != 0:
                die("cached GAP exponent does not divide p-1")

            reps = []

            for rr in js["irreps"]:
                d = int(rr["degree"])
                mats = []

                for M in rr["generators"]:
                    mats.append(
                        np.asarray(M, dtype=np.int64).reshape(d, d) % prime
                    )

                reps.append({
                    "gap_id": int(rr["gap_id"]),
                    "degree": d,
                    "gens": mats,
                })

            if len(reps) != int(meta["conjugacy_classes"]):
                die("cached GAP irrep count != conjugacy-class count")

            if sum(r["degree"] ** 2 for r in reps) != ORDER:
                die("cached GAP sum of squared irrep degrees != |H4|")

            return meta, reps, check_sha

    gap = shutil.which("gap")

    if gap is None:
        die(
            "GAP is required for the complete isotypic calculation. "
            "Install GAP >= 4.12 and ensure `gap` is on PATH."
        )

    with tempfile.TemporaryDirectory(prefix="h4gap_") as td:
        script = os.path.join(td, "irreps.g")
        write_gap_script(script, gens, prime)

        proc = subprocess.run(
            [gap, "-q", script],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

        if proc.returncode != 0:
            sys.stderr.write(proc.stdout)
            sys.stderr.write(proc.stderr)
            die("GAP irreducible-representation computation failed")

        meta, reps = parse_gap_irreps(proc.stdout, prime)

    serial_reps = []

    for rr in reps:
        serial_reps.append({
            "gap_id": rr["gap_id"],
            "degree": rr["degree"],
            "generators": [
                M.astype(int).tolist()
                for M in rr["gens"]
            ],
        })

    payload0 = {
        "prime": prime,
        "action_sha256": action_sha,
        "gap_meta": meta,
        "irreps": serial_reps,
    }

    raw0 = json.dumps(
        payload0,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()

    csha = sha256_bytes(raw0)
    payload0["cache_sha256"] = csha

    with open(cache_path, "w") as f:
        json.dump(
            payload0,
            f,
            sort_keys=True,
            separators=(",", ":"),
        )

    return meta, reps, csha


# ---------------------------------------------------------------------
# Exact modular linear algebra
# ---------------------------------------------------------------------

def matmul_mod(A, B, p):
    """
    Dense small-matrix product.  A,B entries are canonical residues.
    The largest irrep degree is tiny relative to int64 overflow:
       d * (p-1)^2 << 2^63.
    """
    C = A.dot(B)
    C %= p
    return C


def mat_pow_mod(A, n, p):
    d = A.shape[0]
    R = np.eye(d, dtype=np.int64)
    B = A.copy() % p

    while n:
        if n & 1:
            R = matmul_mod(R, B, p)
        B = matmul_mod(B, B, p)
        n //= 2

    return R


def verify_coxeter_representation(genmats, p):
    d = genmats[0].shape[0]
    I = np.eye(d, dtype=np.int64) % p

    for a in range(4):
        for b in range(4):
            M = matmul_mod(genmats[a], genmats[b], p)
            if not np.array_equal(
                mat_pow_mod(M, COXETER[a][b], p),
                I
            ):
                die("finite-field irrep fails Coxeter relation")

    return True


def build_rep_on_group(genmats, parent, parent_gen, p):
    d = genmats[0].shape[0]

    # int32 storage is exact because residues are in [0,24000].
    # Products are formed against int64 generator matrices and reduced mod p.
    R = np.empty((ORDER, d, d), dtype=np.int32)
    R[0] = np.eye(d, dtype=np.int32)

    for a in range(1, ORDER):
        par = parent[a]
        gi = parent_gen[a]

        R[a] = matmul_mod(
            R[par],
            genmats[gi],
            p,
        )

    return R


def rank_mod_numpy(A, p):
    """
    Exact Gaussian elimination over GF(p).

    Vectorized row operations use int64.  Products are < p^2 and
    differences are far below int64 overflow for p=24001.
    """
    M = np.asarray(A, dtype=np.int64).copy() % p
    nr, nc = M.shape
    r = 0

    for c in range(nc):
        nz = np.flatnonzero(M[r:, c])

        if len(nz) == 0:
            continue

        piv = r + int(nz[0])

        if piv != r:
            M[[r, piv]] = M[[piv, r]]

        inv = pow(int(M[r, c]), p - 2, p)
        M[r] = (M[r] * inv) % p

        # Eliminate in moderate batches to avoid huge temporary matrices.
        rows = np.flatnonzero(M[:, c])
        rows = rows[rows != r]

        batch = 128

        for start in range(0, len(rows), batch):
            rr = rows[start:start + batch]
            fac = M[rr, c].copy()

            M[rr] = (
                M[rr]
                - fac[:, None] * M[r][None, :]
            ) % p

        r += 1

        if r == nr:
            break

    return r


# ---------------------------------------------------------------------
# Exact finite-field multiplicities and Fourier blocks
# ---------------------------------------------------------------------

def multiplicity_mod_p(character_integer, R, inv_idx, p):
    """
       <chi, trace rho>
       = (1/|G|) sum_g chi(g) Tr rho(g^{-1})
    in GF(p).

    The result is later promoted to an ordinary integer only after the
    complete dimension and commutant sanity identities succeed.
    """
    trinv = np.asarray(
        [
            int(np.trace(R[int(inv_idx[g])]) % p)
            for g in range(ORDER)
        ],
        dtype=np.int64,
    )

    ch = np.asarray(character_integer, dtype=np.int64) % p

    # Bound < 14400 * p^2 < 2^63.
    total = int(
        np.dot(ch.astype(np.int64), trinv.astype(np.int64))
    )

    return (
        (total % p)
        * pow(ORDER % p, p - 2, p)
    ) % p


def exact_float_fourier_product(Cflat_mod, Rinv_flat, p, audit_seed):
    """
    Return

       F[(a,b),(r,c)]
         = sum_g C_ab(g) rho(g^{-1})_{r,c} mod p.

    Although NumPy uses float64 BLAS, this computation is EXACT:
    all summands are products of integers in [0,p-1], and the entire
    nonnegative dot product is < 2^53.

    Deterministic Python-bigint entry audits are performed afterwards.
    """
    bound = ORDER * (p - 1) * (p - 1)

    if bound >= (1 << 53):
        die(
            "float64 exact-dot bound failed: %d >= 2^53"
            % bound
        )

    A = Cflat_mod.astype(np.float64).T
    B = Rinv_flat.astype(np.float64)

    Ff = A.dot(B)

    if not np.all(np.isfinite(Ff)):
        die("nonfinite Fourier matrix product")

    rounded = np.rint(Ff)

    if not np.array_equal(Ff, rounded):
        # Under the stated exactness bound this should be impossible.
        die("float64 Fourier product produced a noninteger")

    Fi = rounded.astype(np.int64) % p

    # Deterministic arbitrary-precision audits.
    nr, nc = Fi.shape

    tests = [
        (0, 0),
        (nr - 1, nc - 1),
        (audit_seed % nr, (audit_seed * 17 + 3) % nc),
        ((audit_seed * 29 + 5) % nr, (audit_seed * 43 + 7) % nc),
    ]

    for i, j in tests:
        exact = 0
        for g in range(ORDER):
            exact += (
                int(Cflat_mod[g, i])
                * int(Rinv_flat[g, j])
            )

        if exact % p != int(Fi[i, j]):
            die(
                "arbitrary-precision Fourier audit failed "
                "at (%d,%d)" % (i, j)
            )

    return Fi


def fourier_gram_rank(Corr, R, inv_idx, d, p, audit_seed):
    Cmod = Corr.reshape(ORDER, KSEED * KSEED).astype(np.int64) % p

    Rinv = R[inv_idx].reshape(ORDER, d * d) % p

    F = exact_float_fourier_product(
        Cmod,
        Rinv,
        p,
        audit_seed,
    )

    # F is indexed by (a,b) and (r,c).  Rearrange it as
    #
    #     H[(a,r),(b,c)]
    #
    # which is the k*d by k*d Fourier Gram block.
    H = (
        F.reshape(KSEED, KSEED, d, d)
         .transpose(0, 2, 1, 3)
         .reshape(KSEED * d, KSEED * d)
    )

    rank = rank_mod_numpy(H, p)

    return rank, H


def character_hash_mod_p(R, p):
    vals = [
        int(np.trace(R[g]) % p)
        for g in range(ORDER)
    ]

    raw = b"".join(
        int(x).to_bytes(4, "little", signed=False)
        for x in vals
    )

    return sha256_bytes(raw), vals


def frobenius_schur_indicator_mod_p(charvals, square_idx, p):
    total = 0

    for a in range(ORDER):
        total += int(charvals[int(square_idx[a])])

    nu = (
        (total % p)
        * pow(ORDER % p, p - 2, p)
    ) % p

    if nu == 0:
        return 0

    if nu == 1:
        return 1

    if nu == p - 1:
        return -1

    die(
        "Frobenius-Schur indicator is not 0,+1,-1 mod p: %d"
        % nu
    )


def real_symmetric_commutant_dimension(results, charvals_all, inv_idx):
    """
    Convert the complex/splitting-field isotypic multiplicities to the
    real self-adjoint commutant dimension.

    FS=+1: M_m(R), self-adjoint dimension m(m+1)/2.
    FS= 0: a dual pair gives M_m(C), Hermitian dimension m^2.
    FS=-1: m is even and the real multiplicity is m/2 over H;
           Hermitian dimension (m/2)(m-1) = m(m-1)/2.
    """
    char_map = {
        tuple(int(x) for x in vals): i
        for i, vals in enumerate(charvals_all)
    }

    if len(char_map) != len(charvals_all):
        die("two finite-field irreducible characters are identical")

    used = set()
    total_W = 0
    blocks_W = []

    for i, r in enumerate(results):
        if i in used:
            continue

        fs = int(r["frobenius_schur_indicator"])
        m = int(r["m_W_exact"])

        if fs == 1:
            dim = m * (m + 1) // 2
            blocks_W.append({
                "type": "real",
                "irreps": [int(r["gap_irrep_id"])],
                "matrix_size": m,
                "real_symmetric_parameter_dimension": dim,
            })
            total_W += dim
            used.add(i)

        elif fs == -1:
            if m % 2:
                die(
                    "quaternionic-type irrep has odd complex multiplicity in W"
                )
            rr = m // 2
            dim = rr * (2 * rr - 1)
            if dim != m * (m - 1) // 2:
                die("internal quaternionic dimension formula mismatch")
            blocks_W.append({
                "type": "quaternionic",
                "irreps": [int(r["gap_irrep_id"])],
                "quaternionic_matrix_size": rr,
                "complex_multiplicity": m,
                "real_symmetric_parameter_dimension": dim,
            })
            total_W += dim
            used.add(i)

        elif fs == 0:
            vals = charvals_all[i]
            dual = tuple(
                int(vals[int(inv_idx[g])])
                for g in range(ORDER)
            )

            if dual not in char_map:
                die("complex-type irrep has no dual character in list")

            j = char_map[dual]

            if j == i:
                die("FS=0 irrep is unexpectedly self-dual")

            if int(results[j]["frobenius_schur_indicator"]) != 0:
                die("dual of FS=0 irrep does not have FS=0")

            if int(results[j]["m_W_exact"]) != m:
                die("complex-conjugate pair has unequal W multiplicities")

            dim = m * m

            blocks_W.append({
                "type": "complex",
                "irreps": sorted([
                    int(r["gap_irrep_id"]),
                    int(results[j]["gap_irrep_id"]),
                ]),
                "complex_matrix_size": m,
                "real_symmetric_parameter_dimension": dim,
            })

            total_W += dim
            used.add(i)
            used.add(j)

        else:
            die("bad Frobenius-Schur indicator")

    return total_W, blocks_W


def real_K_psd_blocks_if_complete(results, charvals_all, inv_idx):
    """
    Real Wedderburn block sizes for invariant PSD Gram matrices supported
    on K, assuming every K multiplicity has already been certified.
    """
    char_map = {
        tuple(int(x) for x in vals): i
        for i, vals in enumerate(charvals_all)
    }

    used = set()
    blocks = []
    total = 0

    for i, r in enumerate(results):
        if i in used:
            continue

        m = int(r["m_K_if_certified"])
        fs = int(r["frobenius_schur_indicator"])

        if fs == 1:
            dim = m * (m + 1) // 2
            blocks.append({
                "type": "real_symmetric_PSD",
                "irreps": [int(r["gap_irrep_id"])],
                "matrix_size": m,
                "parameter_dimension": dim,
            })
            total += dim
            used.add(i)

        elif fs == -1:
            if m % 2:
                die(
                    "certified K multiplicity is odd in quaternionic sector"
                )
            rr = m // 2
            dim = rr * (2 * rr - 1)
            blocks.append({
                "type": "quaternionic_Hermitian_PSD",
                "irreps": [int(r["gap_irrep_id"])],
                "quaternionic_matrix_size": rr,
                "complex_multiplicity": m,
                "parameter_dimension": dim,
            })
            total += dim
            used.add(i)

        elif fs == 0:
            vals = charvals_all[i]
            dual = tuple(
                int(vals[int(inv_idx[g])])
                for g in range(ORDER)
            )
            j = char_map.get(dual)

            if j is None or j == i:
                die("cannot pair complex K irreducible")

            if int(results[j]["m_K_if_certified"]) != m:
                die("complex-conjugate K multiplicities disagree")

            dim = m * m
            blocks.append({
                "type": "complex_Hermitian_PSD",
                "irreps": sorted([
                    int(r["gap_irrep_id"]),
                    int(results[j]["gap_irrep_id"]),
                ]),
                "complex_matrix_size": m,
                "parameter_dimension": dim,
            })
            total += dim
            used.add(i)
            used.add(j)

        else:
            die("bad FS indicator")

    return total, blocks


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main():
    if len(sys.argv) != 3:
        die(
            "usage: python h4_complete_K_isotypic.py "
            "d4_n1_300x300.mat "
            "d4_n1_300x300.mat.H4_level2_exact_system.json"
        )

    mat_path = sys.argv[1]
    system_path = sys.argv[2]

    # ---------------------------------------------------------------
    # Official data and exact witness
    # ---------------------------------------------------------------

    if file_md5(mat_path) != EXPECTED_MD5:
        die("official MAT MD5 mismatch")

    with h5py.File(mat_path, "r") as f:
        A = exact_int_matrix(f["A"][()], "A")
        ax = exact_sign_vector(f["ax"][()], "ax")
        by = exact_sign_vector(f["by"][()], "by")

    Asha = canonical_A_sha(A)

    if Asha != EXPECTED_A_SHA256:
        die("canonical A SHA256 mismatch")

    if not np.array_equal(A, A.T):
        die("A is not exactly symmetric")

    C = sum(
        int(ax[i]) * int(A[i, j]) * int(by[j])
        for i in range(N)
        for j in range(N)
    )

    if C != EXPECTED_C:
        die("archived witness value mismatch")

    hleft = [
        sum(
            int(A[i, j]) * int(by[j])
            for j in range(N)
        )
        for i in range(N)
    ]

    hright = [
        sum(
            int(ax[i]) * int(A[i, j])
            for i in range(N)
        )
        for j in range(N)
    ]

    Z = [
        j
        for j, h in enumerate(hright)
        if h == 0
    ]

    if Z != [46, 56, 85, 99, 131, 148]:
        die("unexpected exact right-zero set: %r" % Z)

    if any(int(ax[i]) * hleft[i] <= 0 for i in range(N)):
        die("left archived strategy is not a strict best response")

    if any(int(by[j]) * hright[j] < 0 for j in range(N)):
        die("right archived strategy has a wrong-sign field")

    # ---------------------------------------------------------------
    # Load the already-certified H4 Coxeter generators
    # ---------------------------------------------------------------

    with open(system_path, "r") as f:
        system = json.load(f)

    if system.get("mat_md5") != EXPECTED_MD5:
        die("level2 system MAT provenance mismatch")

    if system.get("A_sha256") != EXPECTED_A_SHA256:
        die("level2 system A provenance mismatch")

    gj = system["group"]["coxeter_generators"]

    if len(gj) != 4:
        die("expected four Coxeter generators")

    gens = []

    for gg in gj:
        p = np.asarray(gg["perm"], dtype=np.uint16)
        s = np.asarray(gg["sign"], dtype=np.int8)

        if p.shape != (N,) or s.shape != (N,):
            die("bad Coxeter generator shape")

        if sorted(int(x) for x in p) != list(range(N)):
            die("Coxeter generator is not a permutation")

        if not np.all((s == 1) | (s == -1)):
            die("Coxeter generator has a non-sign entry")

        R = (
            A[np.ix_(p, p)]
            * s[:, None]
            * s[None, :]
        )

        if not np.array_equal(R, A):
            die("Coxeter generator fails exact A invariance")

        gens.append((p, s))

    GP, GS, parent, parent_gen, right, seen = generate_group(gens)

    action_sha = group_sha256(GP, GS)

    if action_sha != EXPECTED_ACTION_SHA256:
        die(
            "signed action SHA mismatch: %s"
            % action_sha
        )

    inv_idx = inverse_indices(GP, GS, seen)
    square_idx = square_indices(GP, GS, seen)

    projective_order = len({
        GP[a].tobytes()
        for a in range(ORDER)
    })

    if projective_order != 7200:
        die("projective group order != 7200")

    # ---------------------------------------------------------------
    # Exact pair-coordinate module D
    # ---------------------------------------------------------------

    pair_rel, pair_records = enumerate_pair_support_orbits(gens)

    pair_stab = pair_orbit_stabilizer_characters(
        GP, GS, pair_records
    )

    killed_ids, eu, ev, killed_bool, neigh = build_killed_pair_edges(
        pair_rel, Z
    )

    Ddim = 2 * len(eu)

    # ---------------------------------------------------------------
    # Two exact equality faces
    # ---------------------------------------------------------------

    faceR = Face(
        ax,
        by,
        "y",
        Z,
    )

    faceL = Face(
        by,
        ax,
        "x",
        Z,
    )

    faces = [faceR, faceL]

    face_stabs = {
        "right": face_stabilizer_summary(faceR, GP, GS),
        "left": face_stabilizer_summary(faceL, GP, GS),
    }

    # ---------------------------------------------------------------
    # Exact characters of W and D
    # ---------------------------------------------------------------

    chiW, chiD = exact_W_and_D_characters(
        GP, GS, eu, ev
    )

    # D dimension from character must agree with coordinate count.
    if int(chiD[0]) != Ddim:
        die(
            "chi_D(identity)=%d but D coordinate dimension=%d"
            % (int(chiD[0]), Ddim)
        )

    # ---------------------------------------------------------------
    # Exact 14-seed residual correlation function
    # ---------------------------------------------------------------

    Corr = build_all_correlations(
        faces,
        GP,
        GS,
        inv_idx,
        eu,
        ev,
        killed_bool,
        neigh,
    )

    corr_payload = Corr.astype("<i8", copy=False).tobytes(order="C")
    corr_sha = sha256_bytes(corr_payload)

    direct_corr_audit = direct_correlation_audit(
        faces,
        gens,
        right,
        Corr,
        killed_bool,
        GP,
        GS,
    )

    # Identity Gram matrix is exact symmetric.
    if not np.array_equal(Corr[0], Corr[0].T):
        die("identity residual seed Gram matrix is not symmetric")

    # ---------------------------------------------------------------
    # GAP splitting-field irreducible representations
    # ---------------------------------------------------------------

    cache_path = (
        system_path
        + ".gap_irreps_GF%d.json" % PRIME
    )

    gap_meta, irreps, gap_cache_sha = load_or_run_gap_irreps(
        gens,
        action_sha,
        PRIME,
        cache_path,
    )

    if gap_meta["exponent"] <= 0:
        die("GAP returned invalid group exponent")

    if (PRIME - 1) % gap_meta["exponent"] != 0:
        die("GF(p) splitting-field exponent check failed")

    # ---------------------------------------------------------------
    # Per-irrep exact block calculation
    # ---------------------------------------------------------------

    results = []
    charvals_all = []

    sum_W_dim = 0
    sum_W_comm = 0
    sum_D_dim = 0
    sum_Lprime_dim_mod = 0

    all_saturated = True

    for ri, rr in enumerate(irreps):
        d = int(rr["degree"])
        gm = rr["gens"]

        verify_coxeter_representation(
            gm, PRIME
        )

        print(
            "irrep %d/%d: degree %d -- building all group matrices"
            % (ri + 1, len(irreps), d),
            file=sys.stderr,
        )

        Rall = build_rep_on_group(
            gm,
            parent,
            parent_gen,
            PRIME,
        )

        char_sha, charvals = character_hash_mod_p(
            Rall,
            PRIME,
        )

        fs_indicator = frobenius_schur_indicator_mod_p(
            charvals,
            square_idx,
            PRIME,
        )

        charvals_all.append(charvals)

        mW = int(
            multiplicity_mod_p(
                chiW,
                Rall,
                inv_idx,
                PRIME,
            )
        )

        mD = int(
            multiplicity_mod_p(
                chiD,
                Rall,
                inv_idx,
                PRIME,
            )
        )

        if mD > mW:
            die(
                "modular multiplicity m_D > m_W "
                "for irrep %d" % rr["gap_id"]
            )

        mWp = mW - mD

        print(
            "  mW=%d mD=%d; computing %dx%d Fourier block"
            % (
                mW,
                mD,
                KSEED * d,
                KSEED * d,
            ),
            file=sys.stderr,
        )

        rmod, H = fourier_gram_rank(
            Corr,
            Rall,
            inv_idx,
            d,
            PRIME,
            audit_seed=7919 + 104729 * ri,
        )

        source_upper = sum(
            induced_residual_source_multiplicity(
                face_stabs[name],
                charvals,
                inv_idx,
                PRIME,
            )
            for name in ("right", "left")
        )

        upper = min(
            mWp,
            source_upper,
        )

        saturated = (
            rmod == upper
        )

        if not saturated:
            all_saturated = False

        mK_if_certified = (
            mWp - rmod
            if saturated
            else None
        )

        # Generator trace fingerprint is useful for human cross-checking.
        gen_traces = [
            int(np.trace(M) % PRIME)
            for M in gm
        ]

        results.append({
            "gap_irrep_id": int(rr["gap_id"]),
            "degree": d,
            "generator_traces_mod_p": gen_traces,
            "full_character_sha256_mod_p": char_sha,
            "frobenius_schur_indicator": int(fs_indicator),
            "real_division_algebra": (
                "R" if fs_indicator == 1 else
                "C" if fs_indicator == 0 else
                "H"
            ),

            "m_W_mod_p_candidate": mW,
            "m_D_mod_p_candidate": mD,
            "m_W_minus_D_candidate": mWp,

            "residual_fourier_rank_mod_p": int(rmod),
            "frobenius_source_multiplicity_upper_bound": int(source_upper),
            "characteristic_zero_upper_bound": int(upper),
            "upper_bound_saturated": bool(saturated),

            "m_K_if_certified": (
                int(mK_if_certified)
                if mK_if_certified is not None
                else None
            ),
        })

        sum_W_dim += d * mW
        sum_W_comm += mW * mW
        sum_D_dim += d * mD
        sum_Lprime_dim_mod += d * rmod

        # Release the potentially largest per-irrep arrays before next block.
        del Rall
        del H

    # ---------------------------------------------------------------
    # Promotion of modular multiplicities to exact ordinary integers
    # ---------------------------------------------------------------

    # Each actual multiplicity is a nonnegative integer congruent to the
    # modular result.  Since reduction cannot make an ordinary multiplicity
    # negative, any wrap would add PRIME*d to this total.  Exact agreement
    # with W's known dimension therefore proves there was NO wrap.
    multiplicities_promoted = True

    if sum_W_dim != EXPECTED_W_DIM:
        multiplicities_promoted = False

    # Independent exact character sanity supplied by the previous run:
    # dim End_G(W) = sum m_rho^2.
    if sum_W_comm != EXPECTED_W_COMMUTANT_DIM:
        multiplicities_promoted = False

    if sum_D_dim != Ddim:
        multiplicities_promoted = False

    if not multiplicities_promoted:
        die(
            "finite-field multiplicity residues did not satisfy the exact "
            "W/D dimension and commutant identities; no characteristic-zero "
            "promotion is allowed"
        )

    # Rename promoted fields in result.
    for r in results:
        r["m_W_exact"] = r.pop("m_W_mod_p_candidate")
        r["m_D_exact"] = r.pop("m_D_mod_p_candidate")
        r["m_W_minus_D_exact"] = r.pop("m_W_minus_D_candidate")

        if (
            int(r["frobenius_schur_indicator"]) == -1
            and int(r["m_W_exact"]) % 2
        ):
            die(
                "quaternionic irrep has odd exact W multiplicity"
            )

        if (
            int(r["frobenius_schur_indicator"]) == -1
            and int(r["m_D_exact"]) % 2
        ):
            die(
                "quaternionic irrep has odd exact D multiplicity"
            )

    W_symgram_from_types, W_real_blocks = (
        real_symmetric_commutant_dimension(
            results,
            charvals_all,
            inv_idx,
        )
    )

    if W_symgram_from_types != EXPECTED_W_SYMGRAM_DIM:
        die(
            "real/complex/quaternionic block bookkeeping gives "
            "Sym^2(W)^G dimension %d, expected %d"
            % (
                W_symgram_from_types,
                EXPECTED_W_SYMGRAM_DIM,
            )
        )

    # ---------------------------------------------------------------
    # Complete-K conclusion
    # ---------------------------------------------------------------

    Lrank_exact = None
    Kdim_exact = None
    Kcomm_exact = None
    K_symgram_exact = None
    K_real_psd_blocks = None

    if all_saturated:
        Lrank_exact = Ddim + sum_Lprime_dim_mod
        Kdim_exact = EXPECTED_W_DIM - Lrank_exact

        # Since every block is certified, its exact K multiplicity is known.
        Kcomm_exact = sum(
            int(r["m_K_if_certified"]) ** 2
            for r in results
        )

        if Kdim_exact != sum(
            int(r["degree"]) * int(r["m_K_if_certified"])
            for r in results
        ):
            die("certified K isotypic dimensions do not sum to K dimension")

        for r in results:
            if (
                int(r["frobenius_schur_indicator"]) == -1
                and int(r["m_K_if_certified"]) % 2
            ):
                die(
                    "certified quaternionic K multiplicity is odd"
                )

        K_symgram_exact, K_real_psd_blocks = (
            real_K_psd_blocks_if_complete(
                results,
                charvals_all,
                inv_idx,
            )
        )

        final_status = "PROVED_COMPLETE_K_DECOMPOSITION"

    else:
        final_status = "PARTIAL_UNSATURATED_IRREP_BLOCKS"

    unsaturated = [
        {
            "gap_irrep_id": r["gap_irrep_id"],
            "degree": r["degree"],
            "m_W_minus_D_exact": r["m_W_minus_D_exact"],
            "rank_mod_p": r["residual_fourier_rank_mod_p"],
            "upper_bound": r["characteristic_zero_upper_bound"],
            "character_sha256_mod_p": r["full_character_sha256_mod_p"],
        }
        for r in results
        if not r["upper_bound_saturated"]
    ]

    # ---------------------------------------------------------------
    # Exact theorem / audit output
    # ---------------------------------------------------------------

    pair_payload = json.dumps(
        pair_stab,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()

    isotypic_payload = json.dumps(
        results,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()

    summary = {
        "final_status": final_status,

        "provenance": {
            "mat_md5": EXPECTED_MD5,
            "A_sha256": Asha,
            "full_signed_action_sha256": action_sha,
            "signed_group_order": ORDER,
            "projective_group_order": projective_order,
        },

        "elliptope_lemma_external_input": {
            "status": "PROVED_BY_USER_EXACT_MINOR",
            "rank_P_hadamard_square": 10,
            "minor_indices": [0,1,2,3,4,5,6,7,9,10],
            "scaled_minor_determinant": (
                "327892164673536 - 146637833895936*sqrt(5)"
            ),
            "conclusion": (
                "natural rank-4 Gram point is an extreme non-cut elliptope "
                "point and therefore does not itself extend to the degree-4 "
                "generalized elliptope"
            ),
        },

        "witness": {
            "C_exact": C,
            "right_zero_fields": Z,
            "strict_left_best_response": True,
            "nonnegative_right_best_response": True,
        },

        "pair_coordinate_submodule_D": {
            "pair_support_orbit_count": 18,
            "killed_pair_support_orbit_ids": killed_ids,
            "one_party_killed_pair_coordinates": int(len(eu)),
            "D_dimension_exact": int(Ddim),
            "pair_orbit_stabilizer_character_sha256":
                sha256_bytes(pair_payload),
            "pair_orbit_stabilizer_characters": pair_stab,
        },

        "equality_face_stabilizers": face_stabs,

        "residual_seed_module": {
            "seed_count": KSEED,
            "correlation_tensor_shape": list(Corr.shape),
            "correlation_tensor_sha256": corr_sha,
            "orthogonality_identity_C_ginv_equals_C_gT": True,
            "direct_coefficient_vector_audit": direct_corr_audit,
            "identity_Gram_rank_mod_p":
                int(rank_mod_numpy(Corr[0] % PRIME, PRIME)),
        },

        "splitting_field": {
            "prime": PRIME,
            "GAP_group_exponent": gap_meta["exponent"],
            "p_minus_1_divisible_by_exponent": True,
            "Maschke_nonmodular": (ORDER % PRIME != 0),
            "GAP_conjugacy_classes": gap_meta["conjugacy_classes"],
            "GAP_irrep_count": len(irreps),
            "sum_irrep_degree_squares": sum(
                int(r["degree"]) ** 2
                for r in results
            ),
            "GAP_irrep_cache_path": cache_path,
            "GAP_irrep_cache_sha256": gap_cache_sha,
            "float64_exact_dot_bound":
                ORDER * (PRIME - 1) * (PRIME - 1),
            "two_to_53": 1 << 53,
        },

        "ordinary_W_sanity": {
            "W_dimension_exact": EXPECTED_W_DIM,
            "sum_d_times_mW": int(sum_W_dim),
            "W_commutant_dimension_exact": EXPECTED_W_COMMUTANT_DIM,
            "sum_mW_squared": int(sum_W_comm),
            "W_symmetric_invariant_Gram_dimension_exact":
                EXPECTED_W_SYMGRAM_DIM,
            "W_symmetric_invariant_Gram_dimension_from_real_types":
                int(W_symgram_from_types),
            "W_invariant_dimension_exact": EXPECTED_W_INVARIANT_DIM,
            "multiplicity_residues_promoted_to_exact_integers": True,
            "real_Wedderburn_block_summary": W_real_blocks,
        },

        "isotypic_blocks": results,
        "isotypic_table_sha256":
            sha256_bytes(isotypic_payload),

        "coefficient_map": {
            "meaning": (
                "full row span of all H4-translated degree<=2 Fourier "
                "restriction functionals from the two equality 6-faces"
            ),
            "D_rank_exact": int(Ddim),
            "residual_rank_mod_p":
                int(sum_Lprime_dim_mod),
            "full_rank_exact_if_all_blocks_saturate":
                (
                    int(Lrank_exact)
                    if Lrank_exact is not None
                    else None
                ),
            "K_dimension_exact_if_all_blocks_saturate":
                (
                    int(Kdim_exact)
                    if Kdim_exact is not None
                    else None
                ),
            "K_commutant_dimension_if_all_blocks_saturate":
                (
                    int(Kcomm_exact)
                    if Kcomm_exact is not None
                    else None
                ),
            "K_symmetric_PSD_parameter_dimension_if_all_blocks_saturate":
                (
                    int(K_symgram_exact)
                    if K_symgram_exact is not None
                    else None
                ),
            "K_real_PSD_blocks_if_all_blocks_saturate":
                K_real_psd_blocks,
        },

        "unsaturated_blocks": unsaturated,

        "scope": (
            "This program completely determines K exactly iff final_status "
            "is PROVED_COMPLETE_K_DECOMPOSITION. It does NOT solve the "
            "degree-2 PSD/SOS feasibility problem; K is the exact seed space "
            "in which every SOS summand must lie."
        ),
    }

    outpath = (
        mat_path
        + ".complete_K_isotypic.json"
    )

    raw = json.dumps(
        summary,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()

    with open(outpath, "wb") as f:
        f.write(raw)

    # Printed copy includes the artifact hash but the file hash is of the
    # canonical payload above (without a self-referential hash field).
    display = dict(summary)
    display["output_path"] = outpath
    display["output_sha256"] = sha256_bytes(raw)

    print(
        json.dumps(
            display,
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
