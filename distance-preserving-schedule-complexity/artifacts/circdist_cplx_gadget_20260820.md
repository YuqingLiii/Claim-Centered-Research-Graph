# CIRCDIST.cplx — the `controllable-coupling-gadget` gate

Session: Opus 5 executor / proposer, budget-boxed, 2026-08-20.
Target node: `CIRCDIST.cplx` (课题三, `research/circdist/notes/CIRCDIST_PROBLEMS.md`).
Input: `artifacts/circdist_cplx_recon_20260820.md` §6 (the gate).

**Labels.** Nothing here is PROVED. Structural statements are **CONJECTURED** (written-out
arguments, no independent adversarial review). Statements produced by exhaustive `F_2`
computation on a *specific finite code* are **NUMERICAL**, and for objects of this size the
enumeration *is* the certificate (every kernel and rowspace below was enumerated in full, not
sampled). No proof-DAG file was touched.

---

## 0. Verdict in one paragraph

The gate asked three things of a small CSS gadget: (i) prescribe a non-product binary relation on
the local CNOT orders of two checks, (ii) certify the promised static distance exactly, (iii) pad.
**(i) and (ii) hold: there is an explicit `n = 12`, weight-4-check, `d = 3` CSS gadget whose two
designated checks induce exactly `≠` on a 3-element value set, with `d` certified by full
enumeration.** **(iii) fails, and it fails for a structural reason rather than by accident: the
mechanism that produces `≠₃` is "the two checks have the same 2-dimensional syndrome subspace",
which is an *equivalence relation*, so every wiring installs the transitive closure — a clique —
instead of a prescribed edge.** The composition experiment confirms this concretely: wiring two
copies of the gadget yields a `K₄` of `≠₃` constraints on 3 values, hence a NO-instance by
pigeonhole, and there is no way to install only the edge that was wanted. Per the pre-committed
readings this is **"padding fails ⇒ go global-algebraic, `P(R1) → 0.2`, tractable islands become
the realistic headline."** The session also produced the island: in the weight-4 / `d_X ≥ 4`
regime the whole CSP collapses to a *list-all-different* problem, which is bipartite matching.

---

## 1. Reproduction of the recon baseline (NUMERICAL)

Before anything new, the machinery was checked against §3 of the recon. Exact agreement:

| code | safe local orders per check | coupling |
|---|---|---|
| rotated `[[9,1,3]]` | 16/24, 16/24, 2/2, 2/2 | 0 |
| unrotated `[[13,1,3]]` = HGP(rep₃,rep₃) | 6/6, 24/24, 6/6, 6/6, 24/24, 6/6 | 0 |
| Steane `[[7,1,3]]` | 0/24 on every check | 0 (vacuous) |

Both sectors, `d = 3`, budget 2 columns. This reproduces the recon numbers exactly and validates
the `F_2` layer used for everything below.

---

## 2. A sharper reformulation of the `d = 3` CSP (CONJECTURED)

This is the main structural output of the session and it drives every result that follows.

Let `σ(v) = H_Z v ∈ F_2^{m_Z}` be the syndrome map (X-sector; the Z-sector is the mirror). For a
check `c` with local order `π = (q_1,…,q_w)` write `S_i = {q_{i+1},…,q_w}` (the hook) and
`P_i = {q_1,…,q_i}` (the prefix), so `S_i = supp(c) \ P_i`.

**Lemma A (prefix-syndrome law).** Since `H_X H_Z^T = 0`, `σ(c) = 0`, hence `σ(S_i) = σ(P_i)`.
Because "`A ⊕ B` is undetectable" is exactly `σ(A) = σ(B)`,

```
  forbidden(π₁, π₂)  ⟺  ∃ i, j :  σ(P_i(π₁)) = σ(P_j(π₂))   and   S_i(π₁) ⊕ S_j(π₂) ∉ S_X .
```

Writing `a_q := σ(e_q)` for the syndrome of data qubit `q`, and noting `Σ_{q ∈ supp(c)} a_q = 0`:

> **The value of a local order is the set of *proper prefix sums* of the multiset
> `{a_q : q ∈ supp(c)}`, and two checks conflict iff their prefix-sum sets meet.**

So Eff-Preserve at `d = 3` is: *order each check's syndrome multiset (which sums to `0`) so that
the resulting prefix-sum sets are pairwise disjoint*, together with the unary requirement that
each set be free of `0` and of the singleton syndromes `a_q` — all "modulo `S_X`", i.e. a
collision is harmless when the two hooks differ by a stabiliser.

**Verification (NUMERICAL).** On the gadget of §3, brute force vs. the law over
5 760 X-sector and 29 760 Z-sector order pairs: **0 mismatches**. The stabiliser proviso is *not*
decorative — 1 152 X-sector and 8 513 Z-sector pairs have colliding syndromes but a stabiliser
difference, and are therefore safe. Dropping the proviso gives a strictly wrong relation.

**Why this matters.** It replaces "search over `w!` orders and test linear algebra" by a
transparent combinatorial object, and it makes the reachable-value structure computable:
`Reach(c) ∪ {0} = span{a_q : q ∈ supp(c)}` is always a *subspace*. That subspace-ness is the seed
of the obstruction in §5.

---

## 3. The gadget: prescribability (i) and distance certification (ii) — both hold

### 3.1 The design principle (CONJECTURED)

**Lemma B (weight-4 law).** Let every X-check have weight 4 and let `d_X ≥ 4`. Then

1. *every* one of the 24 local orders of *every* X-check is unarily safe;
2. the only surviving coupling is between the **middle** hooks: the hook `S_2 = {q_3,q_4}` is
   congruent mod the stabiliser `c` to the prefix `P_2 = {q_1,q_2}`, so the value of an order is
   the **2|2 split** `{P, P^c}` of the support — exactly **3 values**, each realised by 8 orders;
3. put `W_c := {0} ∪ {σ(P) : P a 2-subset of supp(c)}`. This is a 2-dimensional subspace
   (`σ({q_1,q_2}) + σ({q_1,q_3}) = σ({q_1,q_4})` because `σ(c) = 0`), and the number of forbidden
   value pairs between `c` and `c'` is `|W_c ∩ W_{c'}| − 1 ∈ {0, 1, 3}` (minus stabiliser
   coincidences);
4. hence the relation is **exactly `≠₃`** iff `W_c = W_{c'}`.

*Reason for 1–2:* the hooks of a weight-4 check are `S_1 ≡ {q_1}`, `S_2 ≡ {q_1,q_2}`, `S_3 = {q_4}`
mod `c`; every unary test and every `(1,·)` coupling produces a coset containing a representative
of weight `≤ 3 < d_X`, so it cannot be a logical. Only `(2,2)` survives, and both of its
representatives-pairs lie in one coset, so "forbidden" is well defined on the 3 values.

The design recipe follows: fix `c₁ = {0,1,2,3}`, `c₂ = {4,5,6,7}` and force
`{0,1,4,5}, {0,2,4,6} ∈ ker(H_Z)` — i.e. `σ({0,1}) = σ({4,5})` and `σ({0,2}) = σ({4,6})`, which
makes `W_{c₁} = W_{c₂}` and therefore `≠₃`. Then search for the rest of the code subject to
`min wt ker(H_Z) ≥ 4` (giving `d_X ≥ 4`), `d_Z = 3`, `k ≥ 1`, all check weights `≤ 6`.

### 3.2 `G_≠₃` — the gadget (NUMERICAL, exact enumeration)

```
n = 12
X-checks (weight 4):  (0,1,2,3) (4,5,6,7) (1,4,8,10) (0,6,8,11) (3,7,9,10)
Z-checks (weight 4-6): (1,2,4,7,9) (0,1,6,7,10) (0,1,2,3,8,9) (0,1,4,5,11)
                       (0,2,4,6,8,11) (4,5,6,7,10,11) (8,9,10,11)
```

**Distance certificate (requirement ii).** `ker(H_Z)` and `ker(H_X)` were enumerated in full
(128 elements each), and the stabiliser rowspaces likewise:

```
dim ker(H_Z) = 7,  dim S_X = 5,  k = 2
X-logical weight spectrum:  {4: 32, 6: 36, 8: 24, 10: 4}   ->  d_X = 4  exactly
Z-logical weight spectrum:  {3: 8, 4: 14, 5: 16, 6: 20, 7: 16, 8: 14, 9: 8}
                                                            ->  d_Z = 3  exactly
static distance d = min(d_X, d_Z) = 3    (the promise holds, exactly)
```

This is a complete enumeration, not a sample: **requirement (ii) holds**.

**The safety table (requirement i).** All 24 orders of `c₀ = (0,1,2,3)` and all 24 of
`c₁ = (4,5,6,7)` are unarily safe, as Lemma B predicts. The full `24 × 24` table
(`X` = the pair of orders admits a weight-2 undetectable logical, i.e. jointly unsafe;
columns labelled by the first two qubits of the `c₁` order):

```
             45 45 46 46 47 47 54 54 56 56 57 57 64 64 65 65 67 67 74 74 75 75 76 76
      0123    X  X  .  .  .  .  X  X  .  .  .  .  .  .  .  .  X  X  .  .  .  .  X  X
      0132    X  X  .  .  .  .  X  X  .  .  .  .  .  .  .  .  X  X  .  .  .  .  X  X
      0213    .  .  X  X  .  .  .  .  .  .  X  X  X  X  .  .  .  .  .  .  X  X  .  .
      0231    .  .  X  X  .  .  .  .  .  .  X  X  X  X  .  .  .  .  .  .  X  X  .  .
      0312    .  .  .  .  X  X  .  .  X  X  .  .  .  .  X  X  .  .  X  X  .  .  .  .
      0321    .  .  .  .  X  X  .  .  X  X  .  .  .  .  X  X  .  .  X  X  .  .  .  .
      1023    X  X  .  .  .  .  X  X  .  .  .  .  .  .  .  .  X  X  .  .  .  .  X  X
      1032    X  X  .  .  .  .  X  X  .  .  .  .  .  .  .  .  X  X  .  .  .  .  X  X
      1203    .  .  .  .  X  X  .  .  X  X  .  .  .  .  X  X  .  .  X  X  .  .  .  .
      1230    .  .  .  .  X  X  .  .  X  X  .  .  .  .  X  X  .  .  X  X  .  .  .  .
      1302    .  .  X  X  .  .  .  .  .  .  X  X  X  X  .  .  .  .  .  .  X  X  .  .
      1320    .  .  X  X  .  .  .  .  .  .  X  X  X  X  .  .  .  .  .  .  X  X  .  .
      2013    .  .  X  X  .  .  .  .  .  .  X  X  X  X  .  .  .  .  .  .  X  X  .  .
      2031    .  .  X  X  .  .  .  .  .  .  X  X  X  X  .  .  .  .  .  .  X  X  .  .
      2103    .  .  .  .  X  X  .  .  X  X  .  .  .  .  X  X  .  .  X  X  .  .  .  .
      2130    .  .  .  .  X  X  .  .  X  X  .  .  .  .  X  X  .  .  X  X  .  .  .  .
      2301    X  X  .  .  .  .  X  X  .  .  .  .  .  .  .  .  X  X  .  .  .  .  X  X
      2310    X  X  .  .  .  .  X  X  .  .  .  .  .  .  .  .  X  X  .  .  .  .  X  X
      3012    .  .  .  .  X  X  .  .  X  X  .  .  .  .  X  X  .  .  X  X  .  .  .  .
      3021    .  .  .  .  X  X  .  .  X  X  .  .  .  .  X  X  .  .  X  X  .  .  .  .
      3102    .  .  X  X  .  .  .  .  .  .  X  X  X  X  .  .  .  .  .  .  X  X  .  .
      3120    .  .  X  X  .  .  .  .  .  .  X  X  X  X  .  .  .  .  .  .  X  X  .  .
      3201    X  X  .  .  .  .  X  X  .  .  .  .  .  .  .  .  X  X  .  .  .  .  X  X
      3210    X  X  .  .  .  .  X  X  .  .  .  .  .  .  .  .  X  X  .  .  .  .  X  X
```

Collapsing duplicate rows/columns gives multiplicities `8 : 8 : 8` on each side and the value map
`π ↦ {first two qubits}` up to complementation. The collapsed table is

```
                {45|67}   {46|57}   {47|56}
      {01|23}      X         .         .
      {02|13}      .         X         .
      {03|12}      .         .         X
```

— the complement of a permutation matrix, i.e. **exactly `≠` on a 3-element domain**, the
3-colouring template named in the gate. **Requirement (i) holds** in the form asked for
(non-product, and in fact the target NP-hard template rather than merely an inequality).

The remaining X-sector pairs of `G_≠₃` obey Lemma B exactly; predicted vs. observed forbidden
value pairs, all ten pairs:

| pair | `\|W_i ∩ W_j\|` | predicted | observed |
|---|---|---|---|
| 0,1 | 4 | 3 | 3 |
| 3,4 | 2 | 1 | 1 |
| 0,2 / 0,3 / 0,4 / 1,2 / 1,3 / 1,4 / 2,3 / 2,4 | 1 | 0 | 0 |

---

## 4. Which relations are realizable (prescribability, enumerated)

### 4.1 Weight-4 checks with `d_X ≥ 4` — exactly three relation types

By Lemma B the induced binary relation on the 3-element value sets has `|W_c ∩ W_{c'}| − 1`
forbidden pairs, so the complete list of realizable relations in this regime is:

* **0 forbidden** — the trivial (product) relation;
* **1 forbidden** — a single forbidden value pair, i.e. the 2-clause
  `¬(x_c = w ∧ x_{c'} = w)` for the unique shared `w`;
* **3 forbidden** — a perfect matching, i.e. `≠₃`.

Nothing else. In particular no XOR/affine relation and no NAE-shaped relation appears here.

### 4.2 Check weight 5–6 — much richer

Once a check has a hook whose *reduced* weight is 3 (weight-6 checks: `S_3 ≡ {q_1,q_2,q_3}`), the
value of an order is a genuine **set** of prefix syndromes and the relation is set-*disjointness*,
not equality of a single value. Observed reduced relation shapes in the Z-sector of `G_≠₃` alone
(all exact, `X` = forbidden):

```
  5x5 staircase                 7x7 double staircase           3x3 with two forbidden per row
  X X X X .                     X X X X . . .                  X X .
  X X X . .                     X X X . . . .                  X . .
  X X . . .                     X X . . . . .                  . . .
  X . . . .                     X . . X X . .
  . . . . .                     . . . X X X X
                                . . . . X X X
                                . . . . X X .
```

and, from the random census, a `6 × 6` two-block relation with **no universal value on either
side** (weight-(5,6) pair, `n = 12`, `d = 3`, `k = 1`):

```
    X = [(2,3,7,9,11) (3,5,8,9,11) (1,3,4,5,7,8) (3,4,6,8,11) (1,5,6,11) (0,2,3,4,7,10)]
    Z = [(3,4,6,11) (0,1,4,9,11) (1,3,6,9,10) (0,5,8,9,10,11) (2,4,6,8,11)]
    checks 1,2   row multiplicities 8x6   column multiplicities 48x6

      X X X . . .
      X X . . . .
      X . X . . .
      . . . X X X
      . . . X X .
      . . . X . X
```

**Census of relation quality** (NUMERICAL; random self-orthogonal and random general CSS codes,
`n ∈ [12,18]`, all check weights `≤ 6`, `d = 3` exactly, both sectors; 6 452 coupled check pairs):

| | count | share |
|---|---|---|
| universal value on **both** sides (relation is decorative) | 5 407 | 83.8 % |
| universal value on one side | 225 | 3.5 % |
| **no universal value — usable in a reduction** | **692** | **10.7 %** |
| empty relation (the pair is jointly unsatisfiable — a degenerate, arc-consistency-visible NO) | 128 | 2.0 % |

So non-product, universal-value-free relations are *not* rare. The strong-form refutation
contemplated by the gate ("only product/unary relations are realizable, hence 2-SAT-like, hence
in P") is **false**: it is refuted by the explicit `≠₃` gadget of §3.

### 4.3 The coupling graph can be non-transitive

A separate scan found triples of checks `i ~ j`, `j ~ l`, `i ≁ l` with non-product relations on
both edges, at check weight `≤ 6` (e.g. `n = 12`, `d = 3`, `k = 1`,
`X = [(0,5,6,7,8,11) (0,3,7,8,9) (0,4,5,6,8,9) (2,4,6,9,10) (1,2,4,6,8)]`,
`Z = [(1,3,4,5,7,10) (0,2,6,7,11) (0,3,7,9,10) (0,5,7,11) (1,5,6,10) (1,2,4,7,8)]`,
X-sector checks `2 ~ 0 ~ 3` with `2 ≁ 3`). So the *coupling* graph is not forced to be
transitive in general. What **is** forced is transitivity of the `≠₃` relation specifically —
see §5, and that is what breaks the reduction.

---

## 5. Padding (iii) — it fails, and here is exactly how

### 5.1 Disjoint composition is perfect (NUMERICAL)

Two copies of `G_≠₃` on disjoint qubits (`n = 24`, block-diagonal `H_X`, `H_Z`):

```
  composed: n = 24, k = 4, d_X = 4, d_Z = 3, d = 3      (distance preserved)
  safe-order counts preserved:                 True
  copy-1 internal tables identical to single:  True
  copy-2 internal tables identical:            True
  cross-copy check pairs: 25   total forbidden entries across all of them: 0
  (Z-sector: identical conclusion, 0 cross-copy forbidden entries)
```

*Reason (CONJECTURED).* For a direct sum, `H_Z` is block diagonal, so a hook of copy 1 and a hook
of copy 2 have syndromes supported in different coordinate blocks; by Lemma A they can only
collide if both are `0`, which is the unary condition. Equivalently a `≤ (d−1)`-column mechanism
splits into per-copy parts, each of which must already be a mechanism of its own copy. So the
constraint set of a disjoint union is exactly the union of the constraint sets — **there are no
spurious low-weight logicals.** This is the "gadgets side by side keep their tables independent"
half of the composition lemma, and it holds cleanly.

### 5.2 …but disjoint composition also carries **zero** coupling, so a wiring is mandatory

The same argument shows the connectors cannot be optional: with block-diagonal `H_Z` no
cross-copy constraint of any kind exists. By Lemma A the only way to create one is to make
copy-1 and copy-2 syndrome coordinates *shared*. The CSS-legal primitive is to **merge** a
Z-check `z^{(1)}` of copy 1 with a Z-check `z^{(2)}` of copy 2 into the single check
`z^{(1)} ∪ z^{(2)}` (legal because every X-check lives inside one copy, so all overlaps stay even).

Merging a *single* Z-check installs nothing (NUMERICAL): for six different single merges the
cross-copy forbidden count stayed `0`, because a cross collision needs a prefix whose syndrome is
exactly `e_z`, and in `G_≠₃` only `z₂` has such prefixes — and `z₂`'s coset leader has weight 1,
so merging it drops the distance to `d = 2`. Both failure modes are predicted by Lemma A:

* new cross logicals have weight (coset leader of `z^{(1)}`) + (coset leader of `z^{(2)}`), so the
  distance survives iff both coset leaders have weight `≥ 2`;
* a coupling appears only if the *whole* syndrome support of the intended value lives inside the
  merged coordinates.

### 5.3 The wiring that works installs a **clique**, not an edge (NUMERICAL)

`W_{c₀} = W_{c₁} = {0x0, 0x0b, 0x11, 0x1a}` has syndrome support `{z₀, z₁, z₃, z₄}`. Merging
exactly those four Z-checks between the two copies gives:

```
  wired composite: n = 24, k = 6, d_X = 4, d_Z = 3, d = 3     (distance still certified 3)
  unary-safe domains: all ten X-checks keep all 24 orders
  coupling graph (X-sector):
      intra 0-1 : 3x3, !=_3        <- copy 1's own edge
      CROSS 0-5 : 3x3, !=_3
      CROSS 0-6 : 3x3, !=_3
      CROSS 1-5 : 3x3, !=_3
      CROSS 1-6 : 3x3, !=_3
      intra 5-6 : 3x3, !=_3        <- copy 2's own edge
      intra 3-4 : 2x2, single forbidden pair
      intra 8-9 : 2x2, single forbidden pair
```

The four checks `{0, 1, 5, 6}` are now **pairwise** `≠₃`. Exhaustive check on the collapsed
domains: the sub-CSP on `{0,1,5}` is satisfiable (witness
`c₀ = (0,1,2,3)`, `c₁ = (4,6,5,7)`, `c₅ = (12,15,13,14)`), and the sub-CSP on `{0,1,5,6}` is
**unsatisfiable** — 4 variables, 3 values, all-different. Hence the wired code is a NO-instance of
Eff-Preserve, and it is a NO-instance *for a reason nobody asked for*.

**Why no wiring variant repairs this (CONJECTURED).** By Lemma B(4), `≠₃` between `c` and `c'`
holds **iff `W_c = W_{c'}`**. Equality of subspaces is an equivalence relation, so the set of
`≠₃` edges is always a **disjoint union of cliques**. It is therefore impossible — not merely
awkward — to install `≠` on `{u,v}` and on `{v,w}` while leaving `{u,w}` free. Any reduction that
maps graph vertices to weight-4 checks and graph edges to `≠₃` can only ever produce a disjoint
union of cliques as its constraint graph, and 3-colourability of a union of cliques is decided by
checking that each clique has `≤ 3` vertices. **Requirement (iii) fails.**

Two further costs of the wiring, recorded for completeness: the merged Z-checks have weight
10 and 12, violating the `≤ 6` bounded-weight hypothesis; and each merge raises `k`, which is not
harmful but is not free either.

### 5.4 The whole weight-4 regime is a tractable island (CONJECTURED)

Lemma B can be pushed to a closed form. Let `Q = F_2^n / S_X`, let `λ : F_2^n → Q` be the quotient
map, and let `Log = ker(H_Z)/S_X ≅ F_2^k`. Then in the weight-4, `d_X ≥ 4` regime:

* the value of check `c` is `x_c = λ(P)` for one of the three 2|2 splits `P`, and the three
  available values satisfy `x^{(1)} + x^{(2)} + x^{(3)} = 0` in `Q` (because the three 2-subsets
  containing a fixed qubit sum to `supp(c) ∈ S_X`);
* `forbidden(x_c, x_{c'}) ⟺ x_c + x_{c'} ∈ Log \ {0}`, i.e. **two checks may share a `Log`-coset
  only by choosing the identical value**. Since `Q/Log` is the syndrome space, this is exactly a
  *list-all-different* condition refined by `Log`;
* therefore the X-sector is a **list all-different / bipartite matching problem**, decided in
  polynomial time by Hall's theorem when `Log` is trivial on the relevant cosets;
* **if `k = 1` the instance is always YES.** *Argument:* pick a linear splitting `Q = Log ⊕ M`
  with projection `β : Q → Log`. Linearity gives `β(x^{(1)}) + β(x^{(2)}) + β(x^{(3)}) = 0`; with
  `Log = {0, ℓ}` an odd number of `ℓ`'s is impossible, so every check has an option with `β = 0`.
  Choosing those options everywhere makes all `β`-components equal, so no forbidden pair can occur.

The `K₄` instance of §5.3 has `k = 6`, consistent with this: `k ≥ 2` is genuinely needed for a
weight-4 NO-instance. This is a new, self-contained **tractable island** and it is exactly the
shape of the node's third minimal-acceptance branch.

---

## 6. How hard are the instances really? (NUMERICAL)

The gate's readings hinge on whether the coupling constraints ever *decide* anything. Two scans.

**Scan 1 — does coupling decide instances?** 294 random self-orthogonal `d = 3` codes, check
weight `≤ 6`, both sectors, exact solve: 13 sector-instances NO for a unary reason (some check has
no safe order at all), **18 NO with every unary domain non-empty** — i.e. decided by coupling —
89 with a universal order (coupling decorative), 174 satisfiable but with no universal order.
So coupling is not decorative.

**Scan 2 — but is it decided by *arc consistency*?** A CSP all of whose instances are settled by
arc consistency has width 1 and is in P; a hardness proof needs instances that are arc-consistent
yet unsatisfiable. Over **1 001 random codes / 2 002 sector-instances** (`d = 3`, check weight `≤ 6`,
self-orthogonal and general generators):

| outcome | count |
|---|---|
| unary-empty (trivial NO) | 102 |
| arc consistency wipes a domain (NO, poly-time visible) | 108 |
| SAT, found greedily right after arc consistency | 1 789 |
| SAT, needed backtracking | 3 |
| **arc-consistent but UNSAT** | **0** |

Inspecting a Scan-1 witness explains the gap: its unsatisfiability came from a *vacuous pair* —
two checks whose entire `8 × 8` table is forbidden, which arc consistency sees immediately.

**But the constructed instance escapes.** The wired `K₄` code of §5.3 is **arc-consistent** (all
ten domains survive at 24 orders), greedy fails, and it is unsatisfiable. So:

> Random bounded-weight `d = 3` instances are, in 2 002/2 002 trials, width-1. Instances with
> genuine CSP content exist but have to be *built*. The building recipe we have produces
> all-different-on-a-clique, which is itself polynomial (matching), so the constructed hardness is
> so far only "beyond arc consistency", not "beyond P".

---

## 7. Gate verdict and route repricing

| gate requirement | outcome |
|---|---|
| (i) prescribability — non-product relation | **HOLDS**; `≠₃` realized exactly, plus a full classification of the weight-4 regime (0/1/3 forbidden pairs only) and a rich weight-5/6 zoo, 10.7 % of coupled pairs universal-value-free |
| (ii) distance certification | **HOLDS**; `d = 3` exactly, by full enumeration of `ker H_Z`, `ker H_X`, `S_X`, `S_Z` |
| (iii) padding / composition | **FAILS** — disjoint side-by-side composition is perfect, but *wiring* installs the transitive closure of the intended edge, provably, because `≠₃ ⟺ W_c = W_{c'}` is an equivalence |

**The pre-committed reading that fires: "padding fails ⇒ go global-algebraic (`P(R1) → 0.2`) and
tractable islands become the realistic headline."** Recommended repricing, scheduler-side only:

* `R1 order-csp-fixed-d-hardness`: `P 0.35 → 0.2`, `D 4 → 6+`. The local gadget/pp-definability
  strategy is dead *in the weight-4 mechanism*. Do not start the wiring construction.
* `R6 tractable-islands-and-factorisation`: `P 0.7 → 0.8`, and it now has a genuinely new member —
  §5.4, the weight-4 / `d_X ≥ 4` island, which is a *matching* algorithm rather than a
  factorisation argument, plus the `k = 1` always-YES corollary. This is the realistic headline.
* `R5 depth-bound-scheduling-lever`: re-price upward as the near-term NP-hardness result, exactly
  as the recon's outcome-2 branch anticipated, with the standing caveat that it is not about hook
  errors.
* `R2 sigma2-upper-bound-clean`: unchanged, still the cheapest completed item; promote to review.
* `R3`, `R4`: unchanged; do not start.

**The one repair worth registering.** The clique obstruction is specific to the weight-4
mechanism, where the effective prefix-sum set is a *single* syndrome, so the relation degenerates
to equality of 2-dimensional subspaces. At check weight 5–6 the relation is genuine **set
disjointness** on `(w−1)`-element prefix-sum sets (§2), which is not an equivalence — and §4.3
exhibits non-transitive coupling graphs at weight `≤ 6`. Choosing one set per variable from a list
so that all chosen sets are pairwise disjoint is the "multiple-choice matching / rainbow matching"
problem, NP-complete in the abstract for sets of size `≥ 2` (Garey & Johnson GT55 — **assumption,
search-level only, needs a primary check**). So the honest repair is: *abandon weight-4 gadgets and
try to realize a prescribed rainbow-matching instance with weight-6 checks*, where the ground set
is the syndrome space and the lists are prefix-sum sets. I did not achieve this in this session —
usable relations exist there (§4.2) but were not brought under control — and it should be
registered as its own premise, not as an expectation.

---

## 8. Honest limits of this session

* Everything is proposer-side; no independent adversarial review of Lemmas A and B.
* Lemma B assumes *all* X-checks have weight 4 and `d_X ≥ 4`; mixed-weight codes are not covered
  by it, and the §5.4 tractability claim inherits that hypothesis.
* The `k = 1` always-YES argument uses a linear splitting `Q = Log ⊕ M`, which exists over `F_2`;
  the argument is short but has not been checked by anyone else.
* Scan 2's "0 arc-consistent UNSAT instances" is a statement about *these* random generators at
  `n ≤ 18`; it is evidence about the typical case, not a theorem, and the constructed `K₄` code
  shows the population is not exhaustive.
* The Garey–Johnson GT55 (multiple-choice matching) citation is search-level and must be verified
  from a primary source before any route leans on it.
* The recon's §6 also folded in a 15-minute primary-source check of Assumption A9 (`Π_2`-
  completeness of the covering radius problem). **That was not done this session** — the budget
  went entirely to the gate. It remains outstanding and still gates `R4`.

---

## Appendix — self-contained probe

Reproduces §1, §3 and the `≠₃` table. Pure Python, exact `F_2`, no dependencies.

```python
import itertools

def pc(x): return bin(x).count("1")
def mask(s):
    m = 0
    for q in s: m |= 1 << q
    return m

def rref(rows, n):
    rows = [r for r in rows if r]; piv = []; r = 0
    for c in range(n):
        p = next((i for i in range(r, len(rows)) if (rows[i] >> c) & 1), None)
        if p is None: continue
        rows[r], rows[p] = rows[p], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> c) & 1): rows[i] ^= rows[r]
        piv.append(c); r += 1
        if r == len(rows): break
    return rows[:r], piv

def span(rows, n):
    R, _ = rref(rows, n); s = {0}
    for x in R: s |= {y ^ x for y in s}
    return s

def kernel(rows, n):
    R, piv = rref(rows, n); ps = set(piv); b = []
    for f in (c for c in range(n) if c not in ps):
        v = 1 << f
        for i, c in enumerate(piv):
            if (R[i] >> f) & 1: v |= 1 << c
        b.append(v)
    s = {0}
    for x in b: s |= {y ^ x for y in s}
    return s

def analyse(n, xchecks, zchecks):
    HX = [mask(s) for s in xchecks]; HZ = [mask(s) for s in zchecks]
    assert all(pc(a & b) % 2 == 0 for a in HX for b in HZ)
    SX, SZ = span(HX, n), span(HZ, n)
    LX, LZ = kernel(HZ, n) - SX, kernel(HX, n) - SZ
    dX = min((pc(v) for v in LX), default=None)
    dZ = min((pc(v) for v in LZ), default=None)
    isL = LX.__contains__
    singles = [1 << q for q in range(n)]
    safe = []
    for s in xchecks:                       # unary-safe local orders, budget d-1 = 2
        good = []
        for perm in itertools.permutations(s):
            h = [mask(perm[i:]) for i in range(1, len(perm))]
            bad = any(isL(x) or any(isL(x ^ e) for e in singles) for x in h) or \
                  any(isL(a ^ b) for a, b in itertools.combinations(h, 2))
            if not bad: good.append((perm, h))
        safe.append(good)
    return dX, dZ, min(dX, dZ), safe, isL

def table(safe_i, safe_j, isL):
    return [[0 if any(isL(a ^ b) for a in hi for b in hj) else 1
             for _, hj in safe_j] for _, hi in safe_i]

# --- recon baselines
for name, n, xc, zc in [
    ("rotated [[9,1,3]]", 9, [(1,2,4,5),(3,4,6,7),(0,1),(7,8)],
                             [(0,1,3,4),(4,5,7,8),(2,5),(3,6)]),
    ("HGP [[13,1,3]]", 13, [(0,3,9),(1,4,9,10),(2,5,10),(3,6,11),(4,7,11,12),(5,8,12)],
                           [(0,1,9),(1,2,10),(3,4,9,11),(4,5,10,12),(6,7,11),(7,8,12)]),
    ("Steane [[7,1,3]]", 7, [(3,4,5,6),(1,2,5,6),(0,2,4,6)],
                            [(3,4,5,6),(1,2,5,6),(0,2,4,6)])]:
    dX, dZ, d, safe, isL = analyse(n, xc, zc)
    print(name, "dX,dZ,d =", dX, dZ, d, "| safe/check:", [len(s) for s in safe])

# --- the gadget G_neq3
XC = [(0,1,2,3),(4,5,6,7),(1,4,8,10),(0,6,8,11),(3,7,9,10)]
ZC = [(1,2,4,7,9),(0,1,6,7,10),(0,1,2,3,8,9),(0,1,4,5,11),
      (0,2,4,6,8,11),(4,5,6,7,10,11),(8,9,10,11)]
dX, dZ, d, safe, isL = analyse(12, XC, ZC)
print("\nG_neq3: dX =", dX, " dZ =", dZ, " d =", d,
      "| safe orders:", [len(s) for s in safe])
M = table(safe[0], safe[1], isL)
for a, (p, _) in enumerate(safe[0]):
    print("".join(map(str, p)), " ".join("X" if v == 0 else "." for v in M[a]))
```
