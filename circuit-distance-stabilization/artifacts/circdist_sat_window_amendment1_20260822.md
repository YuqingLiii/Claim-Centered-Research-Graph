# Amendment 1 to `circdist_sat_window_theorem_20260822.md`

**Node:** `CIRCDIST.sat.window` · **Date:** 2026-08-22 · **Role:** Opus 5 executor, amendment author
applying the repairs registered by the independent claim-level review. **Box:** one session,
stop-loss binding. No sub-agents. No Lean. No proof-DAG object touched. This file is **append-only**
and changes no prior artifact.

**What this amendment is.** `artifacts/circdist_sat_window_review_20260822.md` returned
**FURTHER-REPAIR — text-level only**, CONFIRMing parts (i), (ii) and (iii) and refuting one printed
assertion (scope clause S3 / sub-claim W-G3) whose correct replacement it supplies. This file
applies its three required repairs — S3′ for S3/W-G3, the mirror citation for W-G5, and the
superscript fix in §0 — and records its scope caveat about legality+(MC) rarity. **On the points
below, this amendment governs the theorem document; everywhere else that document stands
unchanged.** No mathematical content of parts (i)–(iii) changes and no requalification is made.

**Epistemic ceiling (binding on every line).** Nothing here is labelled PROVED or `CERTIFIED*`.
The theorem's parts remain **CONJECTURED**; the computation of §4 is **NUMERICAL** with its code
inline and its search scope stated. This session is an amendment author, not a reviewer, and cannot
grant a completion level. The review is treated as **data in a file**, not as certification: it is
itself unreviewed, as it says of its own derivations.

---

## 0. Hash chain

```text
amended predecessor
  artifacts/circdist_sat_window_theorem_20260822.md
  SHA-256  487acf030bc4385ab367e5c7b27a0e2015bae4055f16ba61100ea85866d37e1b
  size     57788 bytes, 932 lines

commissioning review (data, not certification)
  artifacts/circdist_sat_window_review_20260822.md
  SHA-256  219a756e9e366d74cd6d4b13ff91bdb8394ed35f5c922d3f864b176fcf697226
  size     22060 bytes, 342 lines

governing problem statement (consulted; not modified)
  research/circdist/notes/SAT_RESCOPE_20260822.md
  SHA-256  6c8ec4362f728713f9934d5f0b8041195f66434ebe283a69e67147b3c7009d7f

frozen base definitions (consulted; not modified)
  research/circdist/notes/CIRCDIST_PROBLEMS.md
  SHA-256  5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64
```

The first two digests are exactly the two the review binds itself to in its §0 (`487acf03…` for the
theorem, and the review's own bytes as recomputed here). **If any hash above fails to reproduce,
this amendment is void until re-derived against the changed input.**

---

## 1. Repair 1 — scope clause S3 and sub-claim W-G3 are replaced by S3′

### 1.1 What was wrong

The theorem document's **scope clause S3** (§1.4) reads:

> "`d_circ` below is computed against exactly the detector set of Definition 1.9. Enlarging the
> detector set can only decrease `d_circ`; that the set of (D) generates *all* deterministic outcome
> parities of `C_R(M)` is asserted here as the standard convention and is **not** re-derived
> (sub-claim **W-G3**, §8)."

and **W-G3** (§8) asserts that the `F₂`-span of
`{D_{b,r} : b ∈ ℬ, r ∈ {0,…,R}} ∪ {D_{a,r} : a ∈ 𝒜, r ∈ {1,…,R−1}}` is the full space of
deterministic parities of the recorded outcomes and the ideal readout bits.

That assertion is **false as printed**, in two independent ways, and the review exhibits both:

* **(a) the observables, always.** `λ^{(j)}` *is* a deterministic parity of the ideal readout bits
  and is not in the Definition 1.9 span; the deficiency is exactly `k` by the CSS dimension count
  `n − rank H_X − rank H_Z = k`. This is present in **every** instance, Steane and rotated surface
  included. Worse, W-G3's proposed repair path — S3's "enlarging the detector set can only decrease
  `d_circ`" — read literally would enlarge the detector set to all deterministic parities, at which
  point no fault is both undetectable and logical and `d_R` is `+∞`. The intended statement is one
  **modulo the designated observables**, and it is not the one printed.
* **(b) redundancy detectors, whenever the generating set is dependent.** Scope clause S0 fixes
  `𝒜, ℬ` as *the given generating sets* and imposes no independence; if `T ⊆ 𝒜` has
  `Σ_{a∈T} χ_{supp(a)} = 0` then `⊕_{a∈T} m_{a,r}` is deterministic in **every** round including
  round 0 — although each `m_{a,0}` is individually uniform — and is not in the Definition 1.9 span.
  The excess is `dim leftker(H_X)`. Dependent check generators are not exotic: the toric-type and
  bivariate-bicycle/Gross qLDPC families the re-scope note demands for `CIRCDIST.sat.instances` all
  have them.

W-G3's own risk sentence — "*If false, the true `d_circ` could be smaller than the `d_R` computed
here, and each of (i)–(iii) would have to be re-checked*" — **does not materialise**, and the review
says why rather than only that it does not: the missing directions of (b) lie entirely in `V_X`,
i.e. they are parities of `X`-basis ancilla measurements and hence, by the document's own Lemma 2.1,
functions of the `z`-components of a fault alone. Given any `F` undetectable-and-logical against the
Definition 1.9 set, `F^X` is undetectable, logical, of weight `≤ |F|`, and carries no `z`-component,
so it triggers no element of `V_X` at all, redundancy detectors included. Enlarging the detector set
to a maximal one therefore leaves `d_R^Z` **unchanged**, not merely bounded.

### 1.2 The replacement (governing)

**Scope clause S3 and sub-claim W-G3 are retired and replaced, verbatim, by the review's clause
S3′.** Quoted exactly as the review states it (§1.3 of `circdist_sat_window_review_20260822.md`):

> **(S3′)** In the Z-memory, `span{D_{b,r} : b ∈ ℬ, r ∈ {0,…,R}} ⊕ span{λ^{(j)} : j ≤ k}` is the
> full space of deterministic parities of the Z-check records and the ideal readout bits — by the
> CSS dimension count `n − rank H_X − rank H_Z = k` applied to `S_Z ⊆ ker H_X`. The `X`-check
> detectors `{D_{a,r} : r ∈ {1,…,R−1}}` are **not** maximal when `leftker(H_X) ≠ 0`, but by Lemma
> 2.1 no enlargement of them changes `d_R^Z(M)`. Mirror in the X-memory. Consequently `d_R(M)` is
> independent of the detector-set convention, and (i)–(iii) need no requalification.

Bookkeeping consequences, all mechanical:

* **§8: W-G3 is deleted, not carried.** It was listed as "the cheapest remaining formal hole"; the
  hole is real, and closing it **removes** a hypothesis rather than adding one. Any caveat set that
  rides along at promotion must carry S3′ and must **not** carry W-G3.
* **§1.4: S3 is replaced by S3′.** The sentence "enlarging the detector set can only decrease
  `d_circ`" is struck: it is the sentence that invites the `d_R = +∞` reading of (a).
* **§6.1's table row `S3 | detector set = exactly Definition 1.9 | 2.8`** becomes
  `S3′ | detector set = Definition 1.9, maximal modulo the observables (Z-half); X-half maximality
  not needed by Lemma 2.1 | 2.8`. Lemma 2.8's consumption is unaffected: it is a statement about the
  Definition 1.9 detectors, which S3′ retains verbatim.
* **Derivation status.** S3′ is **CONJECTURED**, derived by the review in a few lines from material
  already in the document (Lemma 2.1 and the CSS dimension count) and **NUMERICALLY** confirmed
  here (§4) on the review's own instance set. It is not certified: this amendment does not promote
  it and the review is not a certification of its own derivations.

### 1.3 Verified here on the review's Steane + dependent-check instance

The review's 18-row table is reproduced independently in §4, from code written for this amendment
(no sampling, no `stim`, no reviewer or proposer code read or executed): the deterministic-parity
space is computed **exactly** by back-propagating each measured Pauli through the whole circuit and
testing membership in the input stabiliser group.

| what | reproduced? |
|---|---|
| `L`, `dim V`, `rank(D)`, `rank(D+λ)`, deficiency for all 9 (code, `R`) rows, both schedules — 18 instances | **yes, value for value** |
| the analytic dimension formula `dim V = dim ker H_X + \|ℬ\|R + R\|𝒜\| − rank H_X` | **18/18** |
| S3′'s Z-half — `span{D_{b,r}} ⊕ span{λ}` equals `V_Z` **exactly** | **18/18** |
| S3′'s X-half — the deficiency `dim V_X − rank{D_{a,r}}` equals `dim leftker(H_X)` (`0` for the independent generating sets, `1` for `steane713+redundantX`) | **18/18** |
| the review's named missing parity — `⊕_{a∈𝒜} m_{a,0}` on `steane713+redundantX` is deterministic and outside `span(D ∪ {λ})` | **yes, at `R = 1,2,3`** |

**One precision note, recorded rather than silently absorbed.** The review's §1.2 summarises its
table as "`rank(D) = dim V − k` in every row (failure (a): 18/18 instances)". That identity holds in
the **12** independent-generating-set rows; in the three `steane713+redundantX` rows (both
schedules, so 6 instances) the review's own table prints `rank(D) = 6` against `dim V − k = 7`, and
my recomputation agrees with the *table*, not with the summary sentence. The correct identity is

```text
      rank(D)      =  dim V - k - dim leftker(H_X) ,
      rank(D + λ)  =  dim V     - dim leftker(H_X) ,
```

which is exactly what S3′ states in words, and which reduces to the review's sentence when the
generating sets are independent. What the review's "18/18" does hold of, unconditionally, is the
finding it was making: `rank(D+λ) = rank(D) + 1` in **all 18** instances, i.e. **the observable is
missing from the Definition 1.9 span in every instance** — failure (a), confirmed 18/18. **S3′
itself is unaffected**, since S3′ never asserts the summary sentence; this note corrects a summary
line in the review, not the clause this amendment adopts.

---

## 2. Repair 2 — the §0 superscript

The boxed statement of part (ii) in §0 prints

> `w ≤ |F| = d_R(M) ≤ d`

whereas Theorem 4.1 correctly prints `d_R^σ(M)`. For the sector that does **not** attain the
minimum, `|F| = d_R^σ(M) > d_R(M)` is possible and the printed equality is false there; the
inequality `≤ d` still holds by Lemma 2.12. **Governing correction:** the boxed part (ii) reads

> **(ii) Contiguity.** For every `R ≥ 1` and each sector `σ`, every **minimum-weight** undetectable
> logical fault set `F` of `C_R^σ(M)` has contiguous round support, and its round-span `w` satisfies
> `w ≤ |F| = d_R^σ(M) ≤ d`.

This is a transcription fix in the summary box only; §4's Theorem 4.1, which is the statement
everything downstream consumes, was already correct and is untouched.

---

## 3. Repair 3 — W-G5, the mirror

The §2 preamble states that "the X-memory statements are the images under the mirror of Definition
1.7 and are used without separate proof". Since `d_R(M) = min(d_R^Z, d_R^X)`, half of the theorem
rests on that assertion. The structural mirror is genuine, but **Definition 1.5 is not manifestly
mirror-symmetric**: it is stated asymmetrically as `c_{ab} = #{q : t(q→b) < t(a→q)}`, whereas the
X-memory's hook-consistency condition is `c'_{ab} = 0` with `c'_{ab} = #{q : t(a→q) < t(q→b)}`.
These coincide only because `c_{ab} + c'_{ab} = |supp(a) ∩ supp(b)| ≡ 0` by (CSS) — a fact the
document does prove, inside Standing fact 1.6, but never invokes where it asserts the mirror.

**Governing correction — the one sentence the review asks for, appended to the §2 preamble:**

> The mirror is compatible with the scope hypothesis (S1) because (MC) is itself mirror-symmetric:
> Standing fact 1.6 derives `c_{ab} + c'_{ab} = |supp(a) ∩ supp(b)| ≡ 0 (mod 2)` from (CSS), hence
> `c'_{ab} = c_{ab}`, so a schedule is measurement-consistent for the Z-memory **iff** it is
> measurement-consistent for the X-memory, and Definition 1.5's asymmetric phrasing selects the same
> schedule class in both sectors.

Severity is low and no step changes; what closes is that the X-sector half of the theorem was
asserted by a symmetry whose compatibility with the scope hypothesis was left to the reader. The
review adds that it ran both memories independently through its own code path in all 30 in-scope
instances and in its 54 000-column test and found no asymmetry — **corroboration, not the missing
sentence**, and it is recorded here as corroboration only.

---

## 4. NUMERICAL — the S3′ check, reproduced independently

**Method.** `C_R^Z(M)` is modelled as one Clifford unitary `U` on a product input state — each
round's ancillas a fresh qubit — followed by terminal single-qubit measurements. A parity over a
subset `S` of records is deterministic **iff** `∏_{i∈S} U†P_iU` lies in the input stabiliser group
`⟨Z_q (data), Z_{anc(b,r)}, X_{anc(a,r)}⟩`; since every gate is a CNOT, conjugation preserves Pauli
type, so this reduces to: the product's `x`-support avoids data and `anc(b,·)`, and its `z`-support
avoids `anc(a,·)`. Everything is exact `F₂` linear algebra, `CNOT(c,t): x_t ^= x_c, z_c ^= z_t`;
there is **no sampling** (the review determined the same space empirically by noiseless `stim`
sampling — an independent route to the same object), and no external library.

**Scope, stated.** Codes: Steane `[[7,1,3]]` (Hamming checks `{3456, 1256, 0246}`); rotated surface
`[[9,1,3]]` (`𝒜 = {12, 0134, 4578, 67}`, `ℬ = {03, 1245, 3467, 58}`); and `steane713+redundantX`,
Steane with `𝒜` enlarged by the sum of its three X-checks (`{0,1,3,6}`), which is in scope of S0 and
dependent by construction. Schedules: non-interleaved Z-block-first and X-block-first, one CNOT per
time step (legal by inspection, and (MC) is asserted in code). `R ∈ {1,2,3}`, Z-memory. That is
**18 instances**, the review's 9 table rows crossed with its two schedules. Not covered: interleaved
schedules, `d ≥ 5`, genuine qLDPC instances, and any distance computation — this check is about the
detector-set convention only, which is what S3′ is about.

```python
"""S3' verification: the deterministic-parity space of C_R^Z(M), computed exactly.

C_R^Z(M) is modelled as one Clifford unitary U on a product input state (each round's
ancillas are a fresh qubit) followed by terminal single-qubit measurements.  A record
parity is deterministic iff the product of the back-propagated measured Paulis lies in
the input stabiliser group < Z_q (data), Z_anc(b,r), X_anc(a,r) >, i.e. iff its x-support
avoids data and anc(b,.) and its z-support avoids anc(a,.).  Exact F_2 symplectic
bookkeeping, CNOT(c,t): x_t ^= x_c, z_c ^= z_t.  No sampling, no stim, no imported code.
"""

def rank(vs):
    basis, r = [], 0
    for v in vs:
        for b in basis:
            v = min(v, v ^ b)
        if v:
            basis.append(v); basis.sort(reverse=True); r += 1
    return r

STEANE = [[3,4,5,6],[1,2,5,6],[0,2,4,6]]
SURF_X = [[1,2],[0,1,3,4],[4,5,7,8],[6,7]]
SURF_Z = [[0,3],[1,2,4,5],[3,4,6,7],[5,8]]
CODES = {                       # n, X-checks A, Z-checks B, Z_L support
 'steane713':            (7, STEANE,            STEANE, [0,1,2]),
 'surface913':           (9, SURF_X,            SURF_Z, [0,1,2]),
 'steane713+redundantX': (7, STEANE+[[0,1,3,6]], STEANE, [0,1,2]),  # dependent 4th X-check
}

def instance(n, A, B, R, order):
    na, nb = len(A), len(B)
    ancA, ancB, nxt = {}, {}, n
    for r in range(R):
        for i in range(na): ancA[(i,r)] = nxt; nxt += 1
        for j in range(nb): ancB[(j,r)] = nxt; nxt += 1
    zb = [('qb',j,q) for j in range(nb) for q in B[j]]     # non-interleaved blocks,
    xb = [('aq',i,q) for i in range(na) for q in A[i]]     # one CNOT per time step
    ops = zb+xb if order == 'Z' else xb+zb
    tA = {(k,q):t for t,(kind,k,q) in enumerate(ops) if kind == 'aq'}
    tB = {(k,q):t for t,(kind,k,q) in enumerate(ops) if kind == 'qb'}
    assert all(len(set(a)&set(b)) % 2 == 0 for a in A for b in B)                    # (CSS)
    assert all(sum(1 for q in set(A[i])&set(B[j]) if tB[(j,q)] < tA[(i,q)]) % 2 == 0
               for i in range(na) for j in range(nb))                                # (MC)
    gates = [((ancA[(k,r)], q) if kind == 'aq' else (q, ancB[(k,r)]))
             for r in range(R) for (kind,k,q) in ops]
    rec, L = {}, 0
    for r in range(R):
        for i in range(na): rec[('a',i,r)] = L; L += 1
        for j in range(nb): rec[('b',j,r)] = L; L += 1
    for q in range(n): rec[('ro',q)] = L; L += 1
    bad = {}
    for q in range(n): bad[('x',q)] = len(bad)
    for key in ancB: bad[('x',ancB[key])] = len(bad)
    for key in ancA: bad[('z',ancA[key])] = len(bad)
    rows = [0]*L
    for key, ri in rec.items():
        if   key[0] == 'a': x, z = {ancA[(key[1],key[2])]:1}, {}
        elif key[0] == 'b': x, z = {}, {ancB[(key[1],key[2])]:1}
        else:               x, z = {}, {key[1]:1}
        for (c,t) in reversed(gates):                    # U^dag P U
            if x.get(c,0): x[t] = x.get(t,0) ^ 1
            if z.get(t,0): z[c] = z.get(c,0) ^ 1
        v = 0
        for q,val in x.items():
            if val and ('x',q) in bad: v |= 1 << bad[('x',q)]
        for q,val in z.items():
            if val and ('z',q) in bad: v |= 1 << bad[('z',q)]
        rows[ri] = v
    return rec, rows, L, ancA, ancB

print("code                 sched R   L  dimV rk(D) rk(D+lam) defic dimV_Z rk(Db+lam) leftker formula")
tot = fOK = zOK = xOK = 0
for code,(n,A,B,ZL) in CODES.items():
    na, nb = len(A), len(B)
    rkHX = rank([sum(1<<q for q in a) for a in A])
    for order in ('Z','X'):
        for R in (1,2,3):
            rec, rows, L, ancA, ancB = instance(n, A, B, R, order)
            def vec(ks, rec=rec):
                v = 0
                for k in ks: v ^= 1 << rec[k]
                return v
            def obstruct(c, rows=rows, L=L):
                v = 0
                for i in range(L):
                    if (c >> i) & 1: v ^= rows[i]
                return v
            Zr = [rec[k] for k in rec if k[0] in ('b','ro')]
            Xr = [rec[k] for k in rec if k[0] == 'a']
            dimV  = L - rank(rows)
            dimVZ = len(Zr) - rank([rows[i] for i in Zr])
            dimVX = len(Xr) - rank([rows[i] for i in Xr])
            Db = []
            for j in range(nb):
                for r in range(R+1):
                    if   r == 0: Db.append(vec([('b',j,0)]))
                    elif r <  R: Db.append(vec([('b',j,r),('b',j,r-1)]))
                    else:        Db.append(vec([('ro',q) for q in B[j]]+[('b',j,R-1)]))
            Da  = [vec([('a',i,r),('a',i,r-1)]) for i in range(na) for r in range(1,R)]
            lam = vec([('ro',q) for q in ZL])
            assert all(obstruct(d) == 0 for d in Db+Da) and obstruct(lam) == 0
            rkZ, rkX, lk = rank(Db+[lam]), rank(Da), na - rkHX
            rkD, rkDl = rank(Db+Da), rank(Db+Da+[lam])
            formula = (n - rkHX) + nb*R + R*na - rkHX
            tot += 1; fOK += (dimV == formula); zOK += (rkZ == dimVZ)
            xOK += (dimVX - rkX == lk)
            print("%-20s %-5s %d %3d %5d %5d %9d %5d %6d %10d %7d %s"
                  % (code, order+'blk', R, L, dimV, rkD, rkDl, dimV-rkDl, dimVZ, rkZ, lk,
                     dimV == formula))
print()
print("dim V = dim ker H_X + |B|R + R|A| - rank H_X            : %d/%d" % (fOK,tot))
print("S3' Z-half: span{D_b} (+) span{lambda} = V_Z exactly    : %d/%d" % (zOK,tot))
print("X-half deficiency dim V_X - rank{D_a} = dim leftker H_X : %d/%d" % (xOK,tot))
print()

# the named missing parity of the redundant-generator instance
n, A, B, ZL = CODES['steane713+redundantX']; na, nb = len(A), len(B)
for R in (1,2,3):
    rec, rows, L, ancA, ancB = instance(n, A, B, R, 'Z')
    def vec(ks):
        v = 0
        for k in ks: v ^= 1 << rec[k]
        return v
    def obstruct(c):
        v = 0
        for i in range(L):
            if (c >> i) & 1: v ^= rows[i]
        return v
    Db = []
    for j in range(nb):
        for r in range(R+1):
            if   r == 0: Db.append(vec([('b',j,0)]))
            elif r <  R: Db.append(vec([('b',j,r),('b',j,r-1)]))
            else:        Db.append(vec([('ro',q) for q in B[j]]+[('b',j,R-1)]))
    Da   = [vec([('a',i,r),('a',i,r-1)]) for i in range(na) for r in range(1,R)]
    base = Db + Da + [vec([('ro',q) for q in ZL])]
    P    = vec([('a',i,0) for i in range(na)])      # XOR of all four X-check outcomes, round 0
    print("steane713+redundantX R=%d : parity (+)_{a in A} m_{a,0} deterministic=%s  "
          "in span(D u {lambda})=%s"
          % (R, obstruct(P) == 0, rank(base+[P]) == rank(base)))
```

Output (verbatim):

```text
code                 sched R   L  dimV rk(D) rk(D+lam) defic dimV_Z rk(Db+lam) leftker formula
steane713            Zblk  1  13     7     6         7     0      7          7       0 True
steane713            Zblk  2  19    13    12        13     0     10         10       0 True
steane713            Zblk  3  25    19    18        19     0     13         13       0 True
steane713            Xblk  1  13     7     6         7     0      7          7       0 True
steane713            Xblk  2  19    13    12        13     0     10         10       0 True
steane713            Xblk  3  25    19    18        19     0     13         13       0 True
surface913           Zblk  1  17     9     8         9     0      9          9       0 True
surface913           Zblk  2  25    17    16        17     0     13         13       0 True
surface913           Zblk  3  33    25    24        25     0     17         17       0 True
surface913           Xblk  1  17     9     8         9     0      9          9       0 True
surface913           Xblk  2  25    17    16        17     0     13         13       0 True
surface913           Xblk  3  33    25    24        25     0     17         17       0 True
steane713+redundantX Zblk  1  14     8     6         7     1      7          7       1 True
steane713+redundantX Zblk  2  21    15    13        14     1     10         10       1 True
steane713+redundantX Zblk  3  28    22    20        21     1     13         13       1 True
steane713+redundantX Xblk  1  14     8     6         7     1      7          7       1 True
steane713+redundantX Xblk  2  21    15    13        14     1     10         10       1 True
steane713+redundantX Xblk  3  28    22    20        21     1     13         13       1 True

dim V = dim ker H_X + |B|R + R|A| - rank H_X            : 18/18
S3' Z-half: span{D_b} (+) span{lambda} = V_Z exactly    : 18/18
X-half deficiency dim V_X - rank{D_a} = dim leftker H_X : 18/18

steane713+redundantX R=1 : parity (+)_{a in A} m_{a,0} deterministic=True  in span(D u {lambda})=False
steane713+redundantX R=2 : parity (+)_{a in A} m_{a,0} deterministic=True  in span(D u {lambda})=False
steane713+redundantX R=3 : parity (+)_{a in A} m_{a,0} deterministic=True  in span(D u {lambda})=False
```

**Reading.** Every column of the review's table reproduces. `dim V` matches the analytic formula in
all 18 instances; `span{D_{b,r}} ⊕ span{λ}` **equals** `V_Z` in all 18 (S3′'s Z-half, exactly, not
merely up to containment); the residual deficiency is `dim leftker(H_X)` — `0` for the two
independent generating sets, `1` for the redundant one — in all 18 (S3′'s X-half); and the review's
explicitly named missing parity, `⊕_{a∈𝒜} m_{a,0}`, is deterministic and outside
`span(D ∪ {λ})` at `R = 1,2,3`. The `defic` column is `rank(D+λ)` short of `dim V` by exactly
`dim leftker(H_X)`, which is the precision note of §1.3 in numbers.

**Inherited limitation.** This code is independent in its implementation but shares its *model
design* with the document it checks — the same fault-free circuit layout, the same detector
definitions, the same frozen conventions. A systematic modelling error against `stim`'s conventions
would survive it. The review's arm of the same check used noiseless `stim` sampling and agreed,
which is the one place where the two routes are genuinely independent.

---

## 5. Scope caveat recorded in the theorem's scope section

The review reports a scope observation it explicitly files as "**not a defect**", and it belongs in
the document's scope record because it governs how any future absence result on this node must be
weighed. Added to §7.5 (the fenced absence claim) and to §8's W-OPEN:

> **Scope caveat (sampling rarity).** Legality **plus** (MC) is a *rare* property of random
> schedules. In the review's sampling: **0/400** for Steane and **1/400** for the rotated surface
> code under uniform random gate orders; the document's own §7.2 filter shows the same effect (16 of
> 576 direction-order pairs survive). Consequently any future search for `R_stab ≥ 2` that samples
> schedules at random and filters for legality+(MC) explores the in-scope class **very thinly**, and
> an absence result obtained that way carries correspondingly little weight. This applies to §7.5's
> own 44 (schedule, sector) instances and to the 7 610-schedule scan it cites, and it compounds the
> weakness §7.5 already records — that every instance has `d = 3`, where Theorem 5.1(3) itself caps
> `R_stab ≤ 3`. **W-OPEN and W-G4 remain open exactly as stated**; a decisive experiment needs
> `d ≥ 5` and a construction, not a filtered random sample.

The review's own absence evidence is recorded to the same standard and with the same fence: across
27 independently generated legal + (MC) schedules over three codes, both memories, `R = 1..3`, it
observed only the constant sequences `(2,2,2)` and `(3,3,3)` and **no instance with `d_2 < d_1`** —
absence evidence at `d = 3` only, usable at low confidence under the project's evidence-asymmetry
rule, **not** raising confidence that `R_stab ≡ 1`. The review states that §7.5's existing fencing
is accurate and should be preserved verbatim; it is preserved verbatim, with the caveat above added
rather than substituted.

---

## 6. What this amendment does **not** do

1. **It promotes nothing.** The node stays as the dispatcher finds it, `CONJECTURED`. Rule 6 still
   requires an independent claim-level review before `CIRCDIST.sat.window` may carry a completion
   level; the review that commissioned these repairs is that review's *predecessor*, it withheld
   promotion pending exactly these three items, and it is not a certification of this amendment.
2. **It changes no mathematical content of parts (i)–(iii).** §3–§5 of the theorem document are
   untouched, as the review requires ("None of these touches §3–§5"). No requalification is made.
   S3′ *removes* a hypothesis; it adds none.
3. **It adopts S3′ verbatim and derives nothing new.** The Lemma 2.1 argument and the CSS dimension
   count are the review's; §4 is a numerical reproduction of the review's own table on the review's
   own instances, not an extension of it.
4. **It does not touch the open items.** W-G1, W-G2, W-G4, W-OPEN, the `d ≥ 5` question, the qLDPC
   instance families of `CIRCDIST.sat.instances`, and the min-plus transfer representation of
   `CIRCDIST.sat.transfer` are exactly as their sources leave them. §6.3's A1/A2 bibliographic
   status is likewise unchanged and still inherited.
5. **It modifies no existing file** and touched nothing under `research/circdist/proof-dag/`. Files
   created by this session: this one and two sibling amendments
   (`artifacts/circdist_lift_root_assembly_amendment1_20260822.md`,
   `artifacts/circdist_cplx_islands_amendment4_20260822.md`), each answering its own review.
