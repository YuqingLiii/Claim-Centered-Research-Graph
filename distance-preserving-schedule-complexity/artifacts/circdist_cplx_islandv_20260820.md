# CIRCDIST.cplx — Island V, the general case: realizability does **not** collapse the CSP

Session: Opus 5 executor, budget-boxed (islands node frontier task-004, box = 2 sessions),
2026-08-20. Target node: `CIRCDIST.cplx` (课题三). Inputs:
`research/circdist/notes/CIRCDIST_PROBLEMS.md`, `artifacts/circdist_cplx_islands_writeup_20260820.md`
§6, `artifacts/circdist_islands_review_20260820.md` §4, `artifacts/circdist_cplx_gadget_20260820.md`.
No proof-DAG file was touched; no existing file was modified.

**Labels.** Nothing here is PROVED. Structural statements are **CONJECTURED** (written-out
arguments, internally checked, never independently reviewed). Statements produced by exact `F_2`
computation on specific finite codes are **NUMERICAL**, and at these sizes the enumeration *is*
the certificate (every kernel, rowspace and order-pair table below was enumerated in full, not
sampled). All code is inline in §9 and runs standalone.

---

## 0. Verdict in one paragraph

**Reading (a) fired, at the level of the island's own Question.** Code-realizable instances *do*
express general list-section hardness: the collapse-to-matching is not a theorem about the regime,
it is a theorem about a *sub*-regime. The reason the gadget session saw only cliques is now exact:
`≠₃` between two weight-4 X-checks is `W_c = W_{c'}` **and** the lift-difference
`δ = s_c + s_{c'} : L → Log` injective; `W_c = W_{c'}` is an equivalence, but `δ` is **not** a
function of the syndrome data — it is a nonlocal datum, it takes `≥ 3` distinct values for
`dim Log ≥ 2`, and a single extra weight-4 X-check ("connector") sets any prescribed component of
it to zero. This produces a **2-forbidden-pair** relation that the gadget document's classification
(§4.1: "0, 1 or 3 forbidden, nothing else") omits, and it is exactly the non-transitive relation the
`K₄` obstruction was supposed to forbid. Building on it: **Theorem 1 (CONJECTURED + NUMERICAL).
`Eff-Preserve≥^X[w ≤ 4, d_X ≥ 4]` — the question posed verbatim in the writeup's §6.1 — is
NP-complete**, by an explicit polynomial reduction from 3-SAT whose output is an explicit CSS code
with weight-4 X-checks and `d_X = 4` certified by a cap-set argument (no enumeration needed). The
reduction was verified end-to-end on 75 instances, 8 of them genuine NO instances, and the CSP it
produces was verified against the first-principles hook/prefix mechanics on **383 616** order pairs
with 0 mismatches. Two *new* tractable sub-islands fall out of the same analysis and explain why
random search never found hard instances (§2.6). What is **not** delivered: the promotion from the
X-sector question to `Eff-Preserve` itself, which by Proposition 2.1 needs the Z-sector of the
constructed family to be a YES; §6 states the exact remaining design target, gives a poly-time
sufficient certificate for it, shows the certificate fails for the present layout, and prices the
repair at 1 session. **Weight-6 set-disjointness is thereby demoted from "the only hardness path"
to "an independent and now redundant path" — with one caveat (§7).**

---

## 1. What was asked, and what the answer is

> *In the weight-`≤4` / `d_X ≥ 4` regime of Eff-Preserve, do code-realizable instances express
> general list-section hardness, or does realizability collapse the CSP to matching (poly)?*

Answer: **they express it.** More precisely, three nested statements:

| statement | status |
|---|---|
| realizable list families are *not* arbitrary 3-element lists — they are the nonzero sets of **2-dimensional subspaces `V_c ≤ Q` with `V_c ∩ Log = 0`** (§2) | CONJECTURED, and this is exactly (S1)+(S2) plus a third condition the writeup does not record |
| the local Hall/`K₄` obstruction is a theorem about *one* invariant (the syndrome subspace `W_c`) and is escaped by the *lift* `s_c`, which is nonlocal and freely prescribable by adding weight-4 X-checks (§2.3–§2.4, §2.7) | CONJECTURED + NUMERICAL (explicit `n = 8` witness) |
| the X-sector question of §6.1 is **NP-complete** (§4–§5) | CONJECTURED (construction) + NUMERICAL (exact verification) |

---

## 2. Task 1 — the exact characterisation of realizable list families

Notation as in the writeup: `Q = F_2^n/S_X`, `λ : F_2^n → Q`, `α_q := λ(e_q)`,
`Log = ker(H_Z)/S_X ≅ F_2^k`, `ν : Q → S := Q/Log`, and `S` is canonically the syndrome space, with
`ν(α_q) = a_q :=` the `q`-th column of `H_Z`.

### 2.1 The lists are 2-dimensional subspaces — (S1)+(S2) is exactly "subspace"

**Lemma 1 (CONJECTURED).** Let `c` be a weight-4 X-check with support `{q_1,q_2,q_3,q_4}` and let
`x_c^{(1)}, x_c^{(2)}, x_c^{(3)}` be its three `2|2`-split values (Lemma V.1(4)). Then
`V_c := {0} ∪ L_c` is an **`F_2`-subspace of `Q`**, of dimension 2 in the non-degenerate case.

*Proof.* `x^{(1)} = α_{q_1}+α_{q_2}`, `x^{(2)} = α_{q_1}+α_{q_3}`, `x^{(3)} = α_{q_1}+α_{q_4}`, and
`χ_{supp(c)} ∈ S_X` gives `α_{q_1}+α_{q_2}+α_{q_3}+α_{q_4}=0`, whence
`x^{(1)}+x^{(2)} = α_{q_2}+α_{q_3} = α_{q_1}+α_{q_4} = x^{(3)}`. ∎

For three elements of an `F_2`-space, "closed under addition" is literally
`x^{(1)}+x^{(2)}+x^{(3)} = 0`, i.e. **(S1) and (S2) together are precisely the subspace condition**
— they are not two independent side conditions but one, stated in coordinates after a splitting.
This is the first simplification the writeup's §6.5 was missing, and it is what makes the rest
tractable.

### 2.2 A third side condition the writeup does not record

**Lemma 2 ((S3), CONJECTURED).** Under the §6.1 promise, `V_c ∩ Log = 0` for every non-degenerate
weight-4 X-check.

*Proof.* An element of `V_c \ {0}` is `λ(P)` for a 2-subset `P`, so `ρ(λ(P)) ≤ 2 < 4 ≤ d_X`;
Lemma V.0 says every nonzero element of `Log` has `ρ ≥ d_X`. ∎

Consequently `ν|_{V_c}` is injective, `U_c := ν(V_c)` is a **2-dimensional subspace of the syndrome
space `S`** (a *line* of `PG(dim S - 1, 2)`), and `V_c` is the **graph of a linear map**
`τ_c : U_c → Log` — equivalently `s_c := (ν|_{V_c})^{-1} : U_c → Q` is a linear **section** of `ν`
over `U_c`. `U_c` is the gadget document's `W_c` (Lemma B(3)), so:

> **The intrinsic data of a weight-4 X-check is a pair (line `U_c ≤ S`, linear section
> `s_c : U_c → Q`).** The gadget document sees only the first component. All of the escape lives in
> the second.

### 2.3 The exact local relation classification — the gadget document's list is incomplete

For `c ≠ c'` define `δ_{cc'} := s_c + s_{c'}` on `U_c ∩ U_{c'}`; it lands in `Log` (because `ν` kills
it) and it is **linear**.

**Proposition 3 (CONJECTURED).** `forbidden(x_c, x_{c'})` holds exactly for the pairs
`(s_c(u), s_{c'}(u))` with `u ∈ (U_c ∩ U_{c'}) \ {0}` and `δ_{cc'}(u) ≠ 0`. Hence the number of
forbidden value pairs is

```
   dim(U_c ∩ U_{c'}) = 0                       ->  0   (product relation)
   dim(U_c ∩ U_{c'}) = 1, δ(u) ≠ 0             ->  1   (single forbidden pair)
   dim(U_c ∩ U_{c'}) = 1, δ(u) = 0             ->  0
   U_c = U_{c'}, δ = 0                         ->  0
   U_c = U_{c'}, dim ker δ = 1                 ->  2   ***
   U_c = U_{c'}, δ injective                   ->  3   (≠₃)
```

`circdist_cplx_gadget_20260820.md` §4.1 enumerates the realizable relations as "0, 1 or 3 forbidden
— nothing else". Its Lemma B(3) does carry the parenthetical "minus stabiliser coincidences", but
the enumerated list drops the `2` case, and the whole padding argument of §5.3 ("`≠₃` ⟺ `W_c = W_{c'}`,
equality of subspaces is an equivalence, so `≠₃` edges form disjoint cliques") is *only* valid if
the `2` case cannot occur.

**It occurs.** Minimal witness (NUMERICAL, exact): `n = 8` qubits with `H_Z` columns

```
   B, B+u1, B+u2, B+u3, B', B'+u1, B'+u2, B'+u3    with  u1=0001, u2=0010, u3=0011,
                                                          B=0100, B'=1000   (in F_2^4)
```

and three weight-4 X-checks — the two cosets `c = B+L`, `c' = B'+L` (`L = {0,u1,u2,u3}`) and the
**connector** `K = {B, B+u1, B', B'+u1}`. The column set is a cap set (no three columns sum to `0`),
hence `d(ker H_Z) ≥ 4`, i.e. `d_X ≥ 4`; the run in §9 reports `d_X = 4`, `k = 1`, and

```
   lists:  L_c  = {3, 5, 6},   L_c' = {3, 80, 83}      (canonical Q-representatives)
   forbidden value pairs between c and c':  2   ->  [(5,80), (6,83)]
```

exactly two. The relation `{(5,80),(6,83)}` forbidden, `(3,3)` allowed, is **not** an equivalence
and not `≠₃`.

### 2.4 Why the clique obstruction is *local*, and what escapes it

Fix a line `U` and let `C_U` be the checks with `U_c = U`. Choosing any reference section of `ν`
over `U` identifies `s_c` with `τ_c ∈ Hom(U, Log)`, and `δ_{cc'} = τ_c + τ_{c'}`. So the relation
between two checks of `C_U` is governed by the *difference* `τ_c - τ_{c'}` inside the group
`Hom(U, Log)`, and

```
   c ≠₃ c'   <=>   τ_c + τ_{c'}  ∈  Iso(U, Log)  ⊆  Hom(U, Log).
```

The `≠₃`-graph on `C_U` is therefore an induced subgraph of the Cayley graph
`Cay(Hom(U,Log), Iso(U,Log))`. For `dim Log = 1` there are no isomorphisms `U → Log` at all, so no
`≠₃` — which is Theorem V.4 seen from a different side. For `dim Log ≥ 2`, take `dim Log = 2`:
`Hom(U,Log) ≅ M_2(F_2) ≅ F_2^4` and the connection set is `GL_2(F_2)`, `6` elements. The connection
set is **not** a subgroup (`I + [[0,1],[1,0]] = [[1,1],[1,1]]` has rank 1), so the Cayley graph is
not a disjoint union of cliques.

> **The gadget document's obstruction is real but it is an obstruction on `W_c` only. `W_c = W_{c'}`
> is an equivalence; `τ_c + τ_{c'} ∈ Iso` is not. Nonlocal wiring escapes the `K₄`/Hall obstruction
> exactly when `dim Log ≥ 2`.**

This also settles, in the affirmative, the review's demand (§4.4) that "a hardness statement with any
bite on Island V must use `dim Log ≥ 2`": everything below uses `dim Log ≥ 2` and in fact `k` grows
linearly with the instance.

### 2.5 The concrete escape mechanism: classes = connected components

The abstract statement above becomes completely explicit in the following picture, which is the
working tool for the rest of the report.

For a syndrome point `u ∈ S` call a **`u`-pair** a pair of qubits `{q, q'}` with `a_q + a_{q'} = u`.
The `u`-pairs are pairwise disjoint (if `a_q + a_{q'} = a_q + a_{q''} = u` then `q' = q''`). A
weight-4 X-check `c` with `u ∈ U_c` contains exactly two `u`-pairs, and `λ` agrees on them
(their union is `χ_c ∈ S_X`), so `c` has a well-defined **class at `u`**, namely `s_c(u) = λ(P)`.

**Lemma 4 (CONJECTURED).** Two checks `c, c'` through `u` have the same class at `u` iff
`χ_{P} + χ_{P'} ∈ S_X` for their `u`-pairs `P, P'`. In particular, if `P ∪ P'` is itself an X-check
(a legal weight-4 zero-sum 4-set) then they are merged. Writing `G_u` for the graph whose vertices
are the `u`-pairs and whose edges are the checks through `u` (each check joins its two `u`-pairs),
the **classes in use at `u` are the connected components of `G_u` that contain an edge**.

*Proof.* `λ(P) = λ(P')` iff `χ_P + χ_{P'} ∈ S_X`, which is a subspace, so class-equality is an
equivalence; a check's own edge merges its two endpoints; conversely merging can only be generated
by elements of `S_X`, and adjacency in `G_u` generates exactly the merges witnessed by single
checks, with sums of checks generating the rest. ∎

The X-sector CSP (Theorem V.3(3)) is now:

> **choose, for each syndrome point `u`, one class (component) — every weight-4 X-check must lie in
> the chosen class at at least one of its three points.**

A check with a point carrying only one class-in-use is served there for free; call it **free**.
Connectors are free by construction (§4.3).

### 2.6 The counting theorem, and two new tractable sub-islands

**Theorem A (class-count bound, CONJECTURED).** For every syndrome point `u`, the number of
`u`-pairs is at most `min { wt(z) : z ∈ supp(u) }`, the minimum weight of a Z-check in the support
of `u`. Hence the number of classes in use at `u` is at most `⌊ min_z wt(z) / 2 ⌋`.

*Proof.* Fix any coordinate `z ∈ supp(u)`. For each `u`-pair `{q, q+u}` exactly one of the two
qubits has a `1` in row `z` (their columns differ exactly on `supp(u)`), and distinct `u`-pairs are
disjoint, so the `u`-pairs inject into the support of row `z`. A component with an edge needs two
vertices. ∎

**Corollary A1 (new tractable sub-island, CONJECTURED).** If **every Z-check has weight `≤ 3`**
(with `w_X ≤ 4`, `d_X ≥ 4`), then every point carries at most one class in use, hence every X-check
is served at every one of its points, hence the X-sector is a **YES** and any schedule works —
decided in `O(1)` after reading the promise.

**Corollary A2 (new tractable sub-island, CONJECTURED).** If every qubit lies in exactly two
Z-checks (equivalently `H_Z` is the vertex–edge incidence matrix of a graph `G`, qubits = edges,
Z-checks = vertices, weight-4 X-checks = 4-cycles), then the X-sector is a **YES**. *Reason:* the
third point of a 4-cycle `A-x-B-y` is the "quad" `{A,B,x,y} ∈ S`, whose `u`-pairs are the pairs of
disjoint edges with that boundary, i.e. at most the `3` perfect matchings of a 4-set; so that point
carries one class in use and the check is free. This holds **regardless of the degrees of `G`** and
so is not a special case of A1.

Corollaries A1 and A2 explain the review's coverage limitation (§4.3: "every instance I could
construct in this regime was a YES; 120 + 1500 random codes produced zero NO instances"). Sparse
random codes in this regime tend to have low-weight Z-checks or degree-2 qubits, and those are
*provably* all-YES. Verified: `extras.py` (§9) draws random codes with all Z-check weights `≤ 3`,
weight-4 X-checks and `d_X ≥ 4`, and finds the maximum number of `u`-pairs at any point equal to `3`
and zero violations of "one class in use everywhere, X-sector YES".

**Corollary A3 (the price of hardness).** Any NO instance — indeed any instance in which the CSP is
not trivially YES — must have a Z-check of weight `≥ 4` in the support of a contested point, and
`≥ 6` for a point with three classes. Hardness in this regime therefore *cannot* be had with
bounded Z-weight `≤ 3`. This is the structural reason §6 below is not free.

### 2.7 What the code can and cannot prescribe

The last piece of Task 1: exactly which "list intersection patterns" are reachable.

**Proposition 5 (prescribability, CONJECTURED).** Fix a line `L = {0,u_1,u_2,u_3} ≤ S` and a set of
checks on it — necessarily disjoint cosets `B_i + L` of the qubit-column set. Write
`φ_r(i) ∈ Log` for the class label of check `i` at `u_r` relative to a reference section chosen with
`z(u_3) = z(u_1)+z(u_2)`. Then

1. **`φ_1(i) + φ_2(i) + φ_3(i) = 0` is forced** — not a design choice. *Proof:* the three "cross"
   4-sets `W^r_{ij} = {B_i, B_i+u_r, B_j, B_j+u_r}` satisfy `W^1_{ij}+W^2_{ij}+W^3_{ij} = χ_{c_i} +
   χ_{c_j} ∈ S_X`, so the three class-differences sum to `0`; the same for the labels. ∎
2. **The only relations that can be imposed are `φ_r(i) = φ_r(j)`**, and each is imposed by
   declaring the single weight-4 X-check `W^r_{ij}` (a legal coset 4-set) to be a stabiliser — a
   *connector*. Any consistent system of such relations is realisable, and everything not forced is
   generically independent in `Log`.
3. Consequently the realisable label systems on a line are exactly the triples of partitions
   `(Π_1,Π_2,Π_3)` of the checks with `Π_a ∧ Π_b = Π_1∧Π_2∧Π_3` for all `a ≠ b`.

**Corollary 5a (two classes per point ⇒ NAE, and nothing else).** If every point of the line carries
exactly two classes, with class difference `h_{u_r} ∈ Log\{0}`, then a check's sign vector
`ε ∈ F_2^3` must satisfy `Σ_r ε_r h_{u_r} = 0`, so the realisable sign patterns form a coset of a
subgroup of `F_2^3`:

* `h_{u_1}, h_{u_2}, h_{u_3}` distinct with sum `0` → patterns `{000, 111}` → **exactly `NAE`**;
* `h_{u_1} = h_{u_2} ≠ h_{u_3}` → patterns `{000, 110}`;
* all three equal → patterns = even-weight vectors → satisfied by "select class `0` everywhere",
  i.e. **useless**;
* `h`'s linearly independent → one pattern → useless.

and moreover if two checks on a line differ in class at all three points then automatically
`h_{u_1}+h_{u_2}+h_{u_3} = 0`, so the `NAE` case needs no extra engineering: *two checks per line,
in different classes at all three points, realise `NAE` on the line's three points, for free.*

**Corollary 5b (three classes per point ⇒ full expressive power).** With three classes at the two
"external" points of a line and a gadget-private third point, the realisable languages include
`COPY` and `NEGATE` on arbitrary pairs of points — see §4.2. This is the route taken below, because
it removes the last structural obstruction (§3).

---

## 3. The one structural obstruction that survives, and how it is removed

Reformulate. Choose a splitting `Q = S̃ ⊕ Log`. The whole X-sector question becomes:

> **LINE-SECTION.** Given `F_2`-spaces `S`, `Log`; 2-dimensional subspaces (lines) `U_1,…,U_m ≤ S`;
> and linear maps `τ_i : U_i → Log`. Is there `g : S → Log` such that for each `i` there is
> `u ∈ U_i \{0}` with `g(u) = τ_i(u)`?

(The partial-vs-total distinction is vacuous: extending `g` never destroys a hit, so total `g` is
WLOG. This is Theorem V.3(3) with (S1)+(S2)+(S3) put back in.)

Written out with variables = points and values = `Log`, LINE-SECTION is 3-SAT over the alphabet
`Log`, whose clauses are `g(u_1)=φ_1 ∨ g(u_2)=φ_2 ∨ g(u_3)=φ_3`, subject to **two** restrictions,
both of which are exactly the realizability constraints:

* **(S1) `φ_1+φ_2+φ_3 = 0`** — handled by Proposition 5 and the gadgets;
* **(S2) `u_1+u_2+u_3 = 0`** — the clause's three variables must be a *line*. This is the only real
  obstruction, and it is what killed a first attempt of mine: the natural SAT-level trick "pad a
  2-clause `(x ∨ ¬y)` to `(x ∨ ¬y ∨ z) ∧ (x ∨ ¬y ∨ ¬z)` with a fresh `z`" is **not realizable**,
  because Proposition 5(1) forces two checks that agree at two points of a line to agree at the
  third. (Verified: the first build produced "pos/neg merged" at every such point.)

The removal is Corollary 5b: with three classes per point the language contains `COPY` and
`NEGATE` on *arbitrary* pairs of points, so all clause variables can be routed to fresh
clause-local points chosen to sum to zero, and (S2) becomes free.

---

## 4. Task 2(a) — the reduction

### 4.1 Statement

**Theorem 1 (CONJECTURED construction, NUMERICAL verification).**
`Eff-Preserve≥^X[w ≤ 4, d_X ≥ 4]` is NP-complete. Explicitly: there is a polynomial-time map from
3-CNF formulas `ψ` to pairs `(H_X, H_Z)` such that

* every X-check has weight exactly 4;
* `d_X ≥ 4`, **certified without enumeration** (the columns of `H_Z` form a cap set, so
  `d(ker H_Z) ≥ 4`, hence every X-logical has weight `≥ 4`); the run reports `d_X = 4` exactly;
* `k ≥ 2` (in fact `k` grows linearly with `|ψ|`);
* there is a tuple of local orders of the X-checks with `d_eff^X(M) ≥ 3` **iff** `ψ` is satisfiable.

Membership in NP is the writeup's (a section of `g` on the `≤ 3m` used syndromes is a polynomial
certificate).

### 4.2 The two gadgets

Take `Log ⊇ F_2^2` and write `0, 1, 2, 3` for `0, ℓ_1, ℓ_2, ℓ_1+ℓ_2`. A gadget is five checks on one
line `(u_1, u_2, u_3)` given by their label triples `(φ_1, φ_2, φ_3)` with `φ_3 = φ_1 + φ_2`:

```
   COPY    (0,1,1) (0,2,2) (1,0,1) (1,1,0) (2,0,2)
   NEGATE  (0,0,0) (0,1,1) (1,1,0) (1,3,2) (2,0,2)
```

With the third point `u_3` gadget-private (its class is existentially quantified), the induced
relation on the class choices at `(u_1, u_2)`, computed by exhaustive enumeration over `Log ∪ {*}`
where `*` stands for any value of a larger `Log` (so the gadgets survive `dim Log > 2`), is

```
   COPY    -> {(0,0), (1,1)}          NEGATE -> {(0,1), (1,0)}
```

i.e. each **pins both points into the two-element domain `{0, ℓ_1}`** and equates / negates them.
These were found by exhaustive search over all `2^16` subsets of the 16 zero-sum triples of
`Log = F_2^2` (`relsearch.py`, `gadgets.py`); `5` checks is minimum for each.

*Realizability (Proposition 5).* The label systems solve consistently. For `COPY`, imposing
`φ_1(a)=φ_1(b)`, `φ_1(c)=φ_1(d)`, `φ_2(a)=φ_2(d)`, `φ_2(c)=φ_2(e)`, `φ_3(a)=φ_3(c)`,
`φ_3(b)=φ_3(e)` and normalising `φ_1(a)=0`, `φ_2(c)=0` gives, with `ℓ_1 := φ_1(c)`,
`ℓ_2 := φ_1(e)` free and independent,

```
   φ_1 = (0, 0, ℓ_1, ℓ_1, ℓ_2)   φ_2 = (ℓ_1, ℓ_2, 0, ℓ_1, 0)   φ_3 = (ℓ_1, ℓ_2, ℓ_1, 0, ℓ_2)
```

— exactly the table. `NEGATE` likewise with the relations `φ_1(a)=φ_1(b)`, `φ_1(c)=φ_1(d)`,
`φ_2(a)=φ_2(e)`, `φ_2(b)=φ_2(c)`, `φ_3(a)=φ_3(c)`, `φ_3(d)=φ_3(e)`. Note the *alignment* between
the two points (the same `ℓ_1` appears at `u_1` and at `u_2`) is not assumed — it is **forced** by
the two `φ_3` connectors, which is precisely the nonlocal wiring of §2.4 at work.

### 4.3 The layout

Everything lives in an ambient `F_2^T`; qubits are distinct nonzero vectors (the columns of `H_Z`),
X-checks are 4-subsets forming cosets `B + L` of 2-dimensional subspaces `L` (hence automatically
zero-sum, hence automatically orthogonal to `H_Z`), and the column set is kept a **cap set** by
rejection at placement time, which is what certifies `d_X ≥ 4`.

* **variable `v`** → point `p_v` (fresh); its Boolean domain is the pair of named classes `0`, `L1`
  created by the gadgets attached to it; `v` is TRUE iff class `L1` is selected at `p_v`.
* **clause `t`** → fresh points `q_1, q_2` and `q_3 := q_1 + q_2` (a line by construction), carrying
  **one** check in class `0` at all three points. That check is the constraint
  `¬Y_1 ∨ ¬Y_2 ∨ ¬Y_3` where `Y_i := [class L1 selected at q_i]`.
* **literal `l_i`** → a gadget on the line `{p_v, q_i, p_v + q_i}`: `NEGATE` if `l_i` is positive
  (so `¬Y_i = v`), `COPY` if `l_i` is negative (so `¬Y_i = ¬v`).
* **connectors** — the `6` per gadget imposing Proposition 5's relations, plus the cross-line
  connectors that make the classes named `0` and `L1` agree between gadgets sharing a point. A
  connector `W^r_{ij}` has line `{u_r, B_i+B_j, B_i+B_j+u_r}`; its other two points are generic and
  are used by nothing else, so the connector carries **one class in use** there and is **free**
  (always served). This is the "gadgets side by side keep their tables independent" half of the
  composition lemma, now at list level, and it is verified instance by instance (§5).

Sizes: `16` constraint checks and `21` connectors per clause, `64` qubits per clause, `T = 30`.

### 4.4 The gadget gate's three requirements, at list level

| requirement (gadget doc §0) | at list level | status |
|---|---|---|
| (i) prescribability — a non-product relation | Proposition 5: **any** consistent system of label identifications `φ_r(i)=φ_r(j)` is realizable by adding connectors; in particular the `2`-forbidden relation of §2.3, `COPY`, and `NEGATE` | **HOLDS** |
| (ii) distance certification | cap-set argument: columns distinct, nonzero, no three summing to `0` ⟹ `d(ker H_Z) ≥ 4` ⟹ `d_X ≥ 4`, in `O(n²)`, with no enumeration of `ker H_Z` | **HOLDS**, and now scalable — this replaces the gadget session's full enumeration, which was the reason it could only certify one `n = 12` code |
| (iii) padding / composition | **the failure mode is removed, not repaired.** Disjoint composition still carries zero coupling (gadget doc §5.1), so wiring is still mandatory; but the wiring primitive is no longer "merge two Z-checks so that `W_c = W_{c'}`" (which installs a clique). It is "add one weight-4 X-check `W^r_{ij}`", which sets **one component** of `δ_{cc'}` to zero and installs a **single prescribed identification**. Connectors have generic third points, so they add no constraints of their own | **HOLDS** |

The gadget session's "requirement (iii) fails, provably" is therefore correct *about its own
primitive* (Z-check merging) and wrong as a statement about the regime. The primitive it needed was
on the X side.

---

## 5. Exact verification

All runs are exact `F_2` computations; every table below is the verbatim output of the code in §9.

### 5.1 Baseline: reproduction of `G_≠₃`

The library was first validated by reconstructing the gadget document's `n = 12` code from its
printed check lists (`test_gadget.py`):

```
dim ker H_Z = 7   dim S_X = 5   k = 2        d_X = 4   d_Z = 3
X-logical weight spectrum: {4: 32, 6: 36, 8: 24, 10: 4}
checks 0,1: 3 forbidden value pairs (≠₃)      checks 3,4: 1 forbidden value pair
all other pairs: 0        hypothesis (D): True        X-sector CSP satisfiable: True
```

Every number matches `circdist_cplx_gadget_20260820.md` §3.2 and §3.3 exactly, including the
`|W_i ∩ W_j|`-driven table. This also **discharges the review's GAP-AT-Remark-V.6** on the data
side: hypothesis (D) *does* hold for that code, computed rather than asserted.

### 5.2 Corollary V.2 checked against first-principles hook mechanics

On a reduction instance (`n = 64`, `37` X-checks, `k = 6`), all `24` local orders of all `37` checks
and all `24 × 24` order pairs for all `666` check pairs were expanded into their actual hook sets
`S_1, S_2, S_3` and tested directly for undetectable weight-`≤2` X-logicals (`u ∈ ker H_Z \ S_X`),
i.e. from the gadget document's Lemma A rather than from the `2|2`-split value map:

```
   unarily UNSAFE orders                       :        0     (Lemma V.1(2) predicts 0)
   order-pair relation vs Corollary V.2        :        0 mismatches out of 383 616
   Z-check weights present                     :  22 … 40 over 30 rows
   d_Z (exhaustive to weight 5)                :        4
```

So the CSP being solved below **is** the X-sector question, on these instances, not a proxy for it.

### 5.3 The reduction, end to end

`run3.py` / `battery.py`. Each row: build the code from `ψ`, solve the X-sector CSP exactly, compare
with a brute-force satisfiability decision for `ψ`, and audit the class structure (every named point
must carry at least the two Boolean classes in use; every auxiliary point that is not a
gadget-private third point must carry exactly one, i.e. every connector must be free).

```
all 8 clauses on 3 vars (UNSAT)   n= 512 checks=338 k=144 dX=4 (D)=False | CSP=False SAT=False OK
7 of the 8            (SAT)       n= 448 checks=295 k=123 dX=4 (D)=False | CSP=True  SAT=True  OK
(a|b|c)                           n=  64 checks= 37 k=  6 dX=4 (D)=False | CSP=True  SAT=True  OK
(a|b|c)&(~a|~b|~c)                n= 128 checks= 80 k= 22 dX=4 (D)=False | CSP=True  SAT=True  OK
(a|b|c)&(~a|b|c)&(a|~b|c)         n= 192 checks=123 k= 43 dX=4 (D)=False | CSP=True  SAT=True  OK
+ 8 random N=4 instances                                                                     OK
```

Two further batteries (`battery.py`, `battery2.py`), all exact:

```
battery : 40 random instances (N in {3,4}, M in 5..8), all SAT           mismatches = 0
          n = 320..512 qubits, 209..338 X-checks, k = 81..146,
          core after eliminating free checks: 80..128 checks
battery2: 22 instances straddling the SAT/UNSAT boundary (subsets of the 8
          sign patterns on 3 variables, plus 4-variable formulas containing
          an unsatisfiable 3-variable core)
          15 SAT, 7 UNSAT                                                failures = 0
          hypothesis (D) on every instance: False       d_X on every instance: 4
```

Totals over all runs quoted here: **75 constructed codes, 8 of them NO instances; zero mismatches
with the 3-SAT answer and zero violations of the class-structure audit**.

Two facts worth isolating:

* **hypothesis (D) is false on every constructed instance.** Theorem V.5 does not apply; these are
  genuinely not matching problems. That is the direct answer to the commission's question.
* the **NO** instance (`all 8 clauses on 3 variables`, the minimum-size unsatisfiable 3-CNF) is a NO
  for a reason that is *not* pigeonhole-on-a-clique: the reduced core after removing free checks is
  a 3-SAT core, and the CSP solver has to refute it.

---

## 6. What is *not* delivered: the Z-sector, and the exact remaining step

By Proposition 2.1 the full `Eff-Preserve` answer is `(X-sector YES) ∧ (Z-sector YES)`. §6.1's
*Question* is the X-sector one, and that is what Theorem 1 settles. To promote it to
`Eff-Preserve` under §6.1's *Promise* two more things are needed, and I record their exact status.

**(a) `d(Q) = 3` — SETTLED.** The constructed family has `d_X = 4` and, measured exactly,
`d_Z = 4`; so on its own it has `d = 4` and misses §6.1's promise. The fix is a direct sum with a
fixed constant-size block of `d_X ≥ 4`, `d_Z = 3`, X-check weight `≤ 4` and *both* sectors YES.
Disjoint composition is exact (gadget doc §5.1, reproved here by Lemma 4: every `u`-pair of a point
of one summand lies inside that summand), so the composite has `d = 3`, `d_X ≥ 4`, and an unchanged
X-sector answer. `G_≠₃` is such a block, and this session verified all four conditions for it:
`d_X = 4`, `d_Z = 3`, X-weight 4, X-sector YES (§5.1), and — new here — its **Z-sector is
satisfiable**: all seven Z-checks have unarily safe orders
(`56/120, 56/120, 112/720, 56/120, 112/720, 112/720, 24/24`), all `115 584` cross-check order pairs
were tabulated, and forward-checking search returns the witness order-indices
`[0, 0, 12, 0, 6, 40, 0]` (`zg2.py`, exact). So the `d = 3` half is done.

**(b) the Z-sector of the main block must be YES.** This is *not* established, and it is the
single thing standing between Theorem 1 and NP-completeness of `Eff-Preserve` itself at
X-check weight `≤ 4`.

* A clean sufficient criterion (CONJECTURED, mirror of Lemma V.1's counting): a hook of a
  weight-`W` check has reduced weight `≤ ⌊W/2⌋` (take the shorter of hook and prefix), so every
  size-`≤2` Z-mechanism has reduced weight `≤ 2⌊W/2⌋` (two hooks) or `≤ ⌊W/2⌋ + 1` (hook + data
  column). Hence **`d_Z ≥ 2⌊W/2⌋ + 1` ⟹ every Z-schedule is safe**, `W` the maximum Z-check
  weight. Concretely `W = 5` needs `d_Z ≥ 5`; `W = 6` needs `d_Z ≥ 7`.
* A poly-time *exact-support* certificate is implemented (`zsector.py`): the Z-sector is YES for
  every schedule if no vector of `ker H_X \ S_Z` is supported inside `supp(z)`, inside
  `supp(z) ∪ {q}`, or inside `supp(z) ∪ supp(z')`. On the present layout this **fails**
  (`('hook+data', z=0, q=22)`), because the layout's `H_Z` is the coordinate matrix of a generic
  ambient `F_2^T`, giving Z-checks of weight `22…40` against `d_Z = 4`.
* **The remaining design target is therefore precise:** re-realise the same combinatorial structure
  with a *sparse* `H_Z` — row weight `≤ 6`, `ker H_Z` of distance `≥ 4` (this is what `d_X ≥ 4`
  already is), and `d_Z ≥ 7` — i.e. a classical LDPC pair. Theorem A says row weight `≤ 3` is
  impossible (it forces all-YES) and that three classes per point need a row of weight `≥ 6`; so
  `W = 6`, `d_Z ≥ 7` is the tight target for the `COPY`/`NEGATE` route, and `W = 5`, `d_Z ≥ 5` is
  the tight target for a two-classes-per-point route. **Price: 1 session.** It is a construction
  task, not a conceptual one — every ingredient (which 4-sets are checks, which connectors to add)
  is unchanged; only the ambient embedding must be made sparse.
* Alternative route for the two-classes-per-point variant: by Corollary 5a it needs only `NAE`
  clauses, i.e. hypergraph 2-colouring restricted to **line hypergraphs of `F_2^t`**. I searched for
  `EQ`/`NEQ` gadgets inside the `t = 3` line hypergraph (all `2^7` subsets of the Fano lines) and
  found none with `≤ 5` lines; whether that restricted 2-colouring problem is NP-hard is **OPEN**
  and is the one genuinely new mathematical question this session leaves behind.

**Honest summary of §6.** Theorem 1 is a theorem about the *X-sector question of §6.1*, which is what
the island is; the writeup itself states (§6.1, §6.6) that this "is a genuine half of an answer" and
"is not by itself a decision procedure for Eff-Preserve". The half that is now missing for the full
problem is a *sparsification*, with a stated target and a stated price — not a missing idea.

---

## 7. Consequence for `CIRCDIST.cplx.fixed-d`, and the weight-6 repricing

### 7.1 Where the hardness lives

**Hardness lives at weight `≤ 4`, in the X-sector, and it needs `k ≥ 2` and a Z-check of weight
`≥ 4`.** Concretely, the frontier is now:

| regime | verdict |
|---|---|
| `w_X ≤ 4`, `d_X ≥ 4`, `k ≤ 1` | **P** (Theorem V.4) |
| `w_X ≤ 4`, `d_X ≥ 4`, hypothesis (D) | **P** (Theorem V.5) |
| `w_X ≤ 4`, `d_X ≥ 4`, **all Z-checks weight `≤ 3`** | **P, trivially YES** (Corollary A1 — new) |
| `w_X ≤ 4`, `d_X ≥ 4`, **every qubit in exactly 2 Z-checks** | **P, trivially YES** (Corollary A2 — new) |
| `w_X ≤ 4`, `d_X ≥ 4`, `k ≥ 2`, general | **NP-complete** (Theorem 1) — the X-sector question |
| `Eff-Preserve` itself at `w_X ≤ 4` | open by one sparsification step (§6) |

So the writeup's §7.1 row for Island V should read: not "GAP FOUND / general case open" but
"general case **hard**; two further poly sub-islands identified; the residue is a Z-sector
companion".

### 7.2 The node's minimal-acceptance branches

课题三's minimal acceptance asks for *one* of: (i) fixed-`d` NP-hardness/completeness; (ii) a strict
PH classification; (iii) a nontrivial restricted class with a polynomial algorithm and correctness
proof. Before this session the node's third branch was to be certified on Islands I–IV (per the
writeup's own repricing). After it:

* branch (iii) is **strengthened**: Corollaries A1 and A2 are two more restricted classes with
  polynomial algorithms and proofs, and they are *code-intrinsic* (recognisable from `H_Z` alone in
  linear time), which is the property Island I had to assume;
* branch (i) is **within one construction step**: the X-sector half is done with an explicit,
  verified reduction; the Z-sector half is a sparsification with a stated target.

Repricing of the node: `P(fixed-d NP-completeness lands) 0.35 → 0.7`. The pre-committed reading for
(a) is "fixed-d NP-completeness essentially lands (P → 0.7)"; I take it, but with the §6 caveat
stated in the same breath — the 0.7 is *conditional on* the sparsification, which I price at
1 session and at high probability of success (it is standard LDPC construction, and Theorem A tells
us exactly which parameters are and are not available).

### 7.3 Weight-6 set-disjointness: **demoted, not moot**

The pre-commitment says "(a) succeeds ⇒ weight-6 moot". I decline the strong form and record the
weaker one, for a reason that is now visible rather than cautious:

* **Demoted from "the only hardness path" to "a redundant second path."** The weight-6 direction
  existed because the weight-`≤4` regime was believed to collapse to matching. It does not. The
  main reason to spend sessions on weight-6 is gone.
* **Not moot, for two reasons.** (1) *The bounded-weight headline.* 课题三 asks for hardness under
  "stabilizer weight at most 4 or 6" — for *stabilizers*, not just X-stabilizers. Theorem A3 says
  weight-4 hardness **forces** Z-checks of weight `≥ 4`, and the `COPY`/`NEGATE` route forces
  weight `≥ 6`; so the sharpest achievable bounded-weight statement on this route is "X-checks
  weight 4, Z-checks weight 6", which is *exactly* the weight-6 regime seen from the other sector.
  The two directions have converged rather than one eliminating the other. (2) *Insurance.* If the
  §6 sparsification hits an obstruction — and Theorem A shows this regime does have real
  obstructions — the weight-5/6 zoo (gadget doc §4.2: staircases, a `6×6` two-block relation with no
  universal value, `10.7 %` of coupled pairs universal-value-free) is the fallback with genuinely
  richer relations, where set-disjointness gives more room than single-value equality.
* **Concrete reprice.** Weight-6 set-disjointness: from *urgent / sole path* to **low priority,
  1 session, opportunistic**, and its natural form is no longer "find hardness at weight 6" but
  "supply the sparse `H_Z` for §6, whose Z-checks will have weight 5–6" — i.e. it merges into the
  §6 task rather than competing with it.

---

## 8. Honest limits

* **Nothing is PROVED.** Lemmas 1, 2, 4, Propositions 3, 5, Theorem A and its corollaries, and the
  correctness of the reduction are CONJECTURED: written out and internally checked, never
  independently reviewed. The verification runs are NUMERICAL.
* **Everything rests on imported results I did not re-derive:** Lemma 1.12 (hook value law),
  Lemma IV.1 (mechanism taxonomy at `d = 3`), Lemma V.0, Lemma V.1(1)(4)(5), Proposition 2.1
  (sector factorisation), and Corollary V.2. Of these, Corollary V.2 was *re-verified here* on
  383 616 order pairs of a constructed instance (§5.2), and Lemma V.1(2) with it; the others are
  taken from the writeup and its review, which confirmed them.
* **`d_eff`, not `d_circ`.** Same caveat as every other island.
* **One sector.** §6 states exactly what is missing and what it costs.
* **The reduction's size is not optimised** (64 qubits and 37 checks per clause). Nothing depends on
  that; it is polynomial and that is all the theorem needs.
* **NOT-REVIEWED here:** the wired `K₄` composite of gadget doc §5.3 (I reconstructed `G_≠₃` but not
  the `n = 24` wiring); the Z-sector satisfiability of the main block (that is §6); the claim that
  the sparsification of §6 succeeds.
* **Open question left behind:** is 3-uniform hypergraph 2-colouring NP-hard when the hypergraph is
  a set of lines of `PG(t-1,2)` (all points distinct)? A yes gives a second, two-classes-per-point
  route to Theorem 1 with `W = 5` instead of `W = 6`, which is the more comfortable Z-sector target.

---

## 9. Code

Six standalone files; all outputs quoted above are reproduced by running them in order. They are
exact — no sampling, no floating point.

### 9.1 `islandv.py` — core library (codes, `Q`, the CSP, classes)

```python
"""Island V core library.  CSS code given by qubit columns of H_Z + weight-4 X-checks.
All arithmetic exact over F_2 (python ints as bitmasks).  Nothing here is sampled."""
from itertools import combinations

# ---------------- F_2 linear algebra ----------------
def rref(vs):
    basis, piv = [], []
    for v in vs:
        for b, p in zip(basis, piv):
            if v >> p & 1: v ^= b
        if v:
            p = v.bit_length() - 1
            for i in range(len(basis)):
                if basis[i] >> p & 1: basis[i] ^= v
            basis.append(v); piv.append(p)
    return basis, piv

def reduce_vec(v, basis, piv):
    for b, p in zip(basis, piv):
        if v >> p & 1: v ^= b
    return v

def in_span(v, basis, piv):
    return reduce_vec(v, basis, piv) == 0

def kernel_cols(cols, n):
    """basis of {v in F_2^n : XOR_{i: v_i=1} cols[i] = 0}"""
    piv, ker = {}, []
    for i in range(n):
        c, m = cols[i], 1 << i
        while c:
            r = c.bit_length() - 1
            if r in piv:
                pc, pm = piv[r]; c ^= pc; m ^= pm
            else:
                piv[r] = (c, m); m = 0; break
        if m: ker.append(m)
    return ker

def kernel_rows(rows, n):
    """basis of {v in F_2^n : <r,v> = 0 for every r in rows}"""
    b, p = rref(rows)
    free = [i for i in range(n) if i not in p]
    out = []
    for f in free:
        v = 1 << f
        for bb, pp in zip(b, p):
            if bb >> f & 1: v |= 1 << pp
        out.append(v)
    return out

def span(basis):
    out = [0]
    for b in basis: out += [x ^ b for x in out]
    return out

def wt(x): return bin(x).count('1')

# ---------------- the code ----------------
class Code:
    def __init__(self, cols, xchecks, t, check_cap=True):
        self.cols, self.t = list(cols), t
        self.n = len(cols)
        self.xchecks = [tuple(sorted(c)) for c in xchecks]
        for c in self.xchecks:
            assert len(set(c)) == 4
            s = 0
            for q in c: s ^= self.cols[q]
            assert s == 0, f"X-check {c} columns do not sum to 0"
        if check_cap:
            assert 0 not in self.cols and len(set(self.cols)) == self.n, "columns not distinct/nonzero"
            cs = set(self.cols)
            for a, b in combinations(range(self.n), 2):
                assert (self.cols[a] ^ self.cols[b]) not in cs, f"3 columns sum to 0 at {(a,b)}"
        self.SX = [sum(1 << q for q in c) for c in self.xchecks]
        self.sxb, self.sxp = rref(self.SX)
        self.kerZ = kernel_cols(self.cols, self.n)
        self.kzb, self.kzp = rref(self.kerZ)
        self.k = len(self.kzb) - len(self.sxb)
        self.zrows = [sum(1 << q for q in range(self.n) if self.cols[q] >> z & 1) for z in range(t)]

    # Q = F_2^n / S_X
    def canon(self, v): return reduce_vec(v, self.sxb, self.sxp)
    def syn(self, v):
        s = 0
        for q in range(self.n):
            if v >> q & 1: s ^= self.cols[q]
        return s
    def in_Log(self, x):        # x a Q-representative
        return x != 0 and self.syn(x) == 0

    def dX(self):
        best = None
        for v in span(self.kzb):
            if v and not in_span(v, self.sxb, self.sxp):
                if best is None or wt(v) < best: best = wt(v)
        return best
    def dX_cert(self):
        """d_X for a cap-set code: >=4 by construction; =4 iff some zero-sum 4-set is
        outside S_X.  O(n^2), no enumeration of ker H_Z."""
        by = {}
        for a, b in combinations(range(self.n), 2):
            by.setdefault(self.cols[a] ^ self.cols[b], []).append((a, b))
        for u, ps in by.items():
            for (a, b), (c, d) in combinations(ps, 2):
                if len({a, b, c, d}) == 4:
                    v = (1 << a) | (1 << b) | (1 << c) | (1 << d)
                    if not in_span(v, self.sxb, self.sxp): return 4
        return ">=5"
    def dZ_low(self, maxw=4):
        """smallest weight <= maxw of a vector in ker H_X \\ S_Z, or None."""
        szb, szp = rref(self.zrows)
        rows = self.SX
        for w in range(1, maxw + 1):
            for sub in combinations(range(self.n), w):
                v = 0
                for q in sub: v |= 1 << q
                if all(bin(r & v).count('1') % 2 == 0 for r in rows) and not in_span(v, szb, szp):
                    return w
        return None
    def dZ(self):
        kerX = kernel_rows(self.SX, self.n)
        kb, kp = rref(kerX)
        szb, szp = rref(self.zrows)
        best = None
        for v in span(kb):
            if v and not in_span(v, szb, szp):
                if best is None or wt(v) < best: best = wt(v)
        return best

    # Corollary V.2 CSP
    def values(self, c):
        q1, q2, q3, q4 = c
        return [self.canon((1 << q1) | (1 << q2)),
                self.canon((1 << q1) | (1 << q3)),
                self.canon((1 << q1) | (1 << q4))]
    def csp(self): return [self.values(c) for c in self.xchecks]
    def forbidden(self, x, y): return self.in_Log(self.canon(x ^ y))
    def reduced_csp(self):
        """Sound preprocessing: a check owning a value whose SYNDROME no other live check
        can use is always servable there, so it may be deleted.  Iterate to a fixed point.
        Returns (list of live check indices, lists, syndromes)."""
        L = [list(dict.fromkeys(v)) for v in self.csp()]
        SY = [[self.syn(x) for x in v] for v in L]
        live = set(range(len(L)))
        changed = True
        while changed:
            changed = False
            cnt = {}
            for i in live:
                for s in set(SY[i]): cnt[s] = cnt.get(s, 0) + 1
            for i in list(live):
                if any(cnt[s] == 1 for s in set(SY[i])):
                    live.discard(i); changed = True
        return sorted(live), L, SY

    def solve(self, reduce_first=True):
        """Theorem V.3(3): choose a partial section g of nu hitting every list."""
        if reduce_first:
            idxs, L, SY = self.reduced_csp()
        else:
            L = [list(dict.fromkeys(v)) for v in self.csp()]
            SY = [[self.syn(x) for x in v] for v in L]
            idxs = list(range(len(L)))
        LL = [L[i] for i in idxs]; SS = [SY[i] for i in idxs]
        m = len(LL); g = {}; done = [False] * m
        def live(i):
            return [j for j, x in enumerate(LL[i]) if SS[i][j] not in g or g[SS[i][j]] == x]
        def bt(nleft):
            if nleft == 0: return True
            best = None
            for i in range(m):
                if done[i]: continue
                lv = live(i)
                if not lv: return False
                if len(lv) == 1: best = (i, lv); break
                if best is None or len(lv) < len(best[1]): best = (i, lv)
            i, lv = best
            for j in lv:
                s = SS[i][j]; new = s not in g
                g[s] = LL[i][j]; done[i] = True
                if bt(nleft - 1): return True
                done[i] = False
                if new: del g[s]
            return False
        return dict(g) if bt(m) else None
    def hypD(self):
        L = self.csp()
        return all(not (set(L[i]) & set(L[j])) for i, j in combinations(range(len(L)), 2))

    # class / component structure at each syndrome point
    def points(self):
        used = {}
        for ci, c in enumerate(self.xchecks):
            q1, q2, q3, q4 = c
            for (a, b) in ((q1, q2), (q1, q3), (q1, q4)):
                used.setdefault(self.cols[a] ^ self.cols[b], set()).add(ci)
        out = {}
        diffs = {}
        for a, b in combinations(range(self.n), 2):
            diffs.setdefault(self.cols[a] ^ self.cols[b], []).append((a, b))
        for u, checks in used.items():
            pairs = diffs.get(u, [])
            cls = {p: self.canon((1 << p[0]) | (1 << p[1])) for p in pairs}
            inuse = set()
            for ci in checks:
                q1, q2, q3, q4 = self.xchecks[ci]
                for (a, b) in ((q1, q2), (q1, q3), (q1, q4)):
                    if self.cols[a] ^ self.cols[b] == u:
                        inuse.add(cls[(a, b)])
            out[u] = dict(checks=sorted(checks), npairs=len(pairs),
                          nclass_total=len(set(cls.values())), nclass_used=len(inuse),
                          pairs=pairs, cls=cls)
        return out

def from_checks(n, zchecks, xchecks):
    """build a Code from explicit Z-check supports (rows) and X-check supports."""
    t = len(zchecks)
    cols = [sum(1 << z for z, s in enumerate(zchecks) if q in s) for q in range(n)]
    return Code(cols, xchecks, t, check_cap=False)
```

### 9.2 `build2.py` — the reduction

```python
"""Full reduction  3-SAT  ->  Eff-Preserve_X[w<=4, d_X>=4],  realised as an explicit CSS code.

Layout (all points are elements of F_2^T, all checks are cosets q+L of a 2-dim subspace L):

  * variable v            -> point  p_v          (Boolean domain {class '0', class 'L1'})
  * clause t              -> fresh points q1,q2 and q3 = q1+q2 (a LINE), carrying ONE check
                             in class '0' at all three  ==  the clause (~Y1 v ~Y2 v ~Y3)
  * literal l_i of t      -> a COPY (l_i negative) or NEGATE (l_i positive) gadget on the
                             line {p_v, q_i, p_v+q_i}: 5 checks + 6 connectors.

Label algebra used by the gadgets (phi_3 = phi_1 + phi_2 is FORCED by the code, it is not a
design choice); the connectors are the X-checks that impose  phi_r(i) = phi_r(j).
"""
import random
from itertools import combinations
from islandv import Code

COPY   = dict(phi=[(0,1,1),(0,2,2),(1,0,1),(1,1,0),(2,0,2)])
NEGATE = dict(phi=[(0,0,0),(0,1,1),(1,1,0),(1,3,2),(2,0,2)])

class Builder:
    def __init__(self, T=26, seed=0):
        self.T, self.rng = T, random.Random(seed)
        self.cols, self.idx, self.checks = [], {}, []
        self.colset, self.pointset = set(), set()
        self.registry = {}          # (point, classname) -> base B
        self.named_pts = set()
        self.gadget_pts = set()   # gadget-private third points (3 classes by design)
    def fresh_point(self):
        while True:
            p = self.rng.randrange(1, 1 << self.T)
            if p not in self.pointset:
                self.pointset.add(p); return p
    def q(self, val):
        if val not in self.idx:
            self.idx[val] = len(self.cols); self.cols.append(val); self.colset.add(val)
        return self.idx[val]
    def place(self, line):
        """choose a base B whose coset B+line is fresh and keeps the cap property"""
        u1, u2, u3 = line
        for _ in range(200000):
            B = self.rng.randrange(1, 1 << self.T)
            cand = [B, B ^ u1, B ^ u2, B ^ u3]
            if 0 in cand or len(set(cand)) != 4 or (set(cand) & self.colset): continue
            A = self.colset | set(cand)
            ok = True
            for x in cand:
                for y in A:
                    if x != y and (x ^ y) in A: ok = False; break
                if not ok: break
            if ok: return B
        raise RuntimeError("placement failed")
    def add_check(self, B, line):
        self.checks.append(tuple(self.q(v) for v in (B, B ^ line[0], B ^ line[1], B ^ line[2])))
        return B
    def connect(self, B1, B2, u):
        """X-check forcing phi_u(B1) = phi_u(B2); its other two points are fresh -> it is FREE"""
        assert B1 != B2
        self.checks.append(tuple(self.q(v) for v in (B1, B1 ^ u, B2, B2 ^ u)))
    def name(self, u, nm, B):
        key = (u, nm); self.named_pts.add(u)
        if key in self.registry:
            if self.registry[key] != B: self.connect(self.registry[key], B, u)
        else:
            self.registry[key] = B

    def gadget(self, kind, u1, u2):
        """COPY / NEGATE between the Boolean domains of points u1 and u2."""
        u3 = u1 ^ u2
        assert u3 not in self.pointset, 'gadget third point collides'
        self.pointset.add(u3); self.gadget_pts.add(u3)
        line = (u1, u2, u3)
        phi = (COPY if kind == 'copy' else NEGATE)['phi']
        Bs = [self.add_check(self.place(line), line) for _ in phi]
        for r, u in enumerate(line):
            groups = {}
            for i, f in enumerate(phi):
                groups.setdefault(f[r], []).append(i)
            for val, mem in groups.items():
                for a, b in zip(mem, mem[1:]):
                    self.connect(Bs[a], Bs[b], u)
                if r < 2 and val in (0, 1):     # 0 -> class '0', 1 -> class 'L1'
                    self.name(u, '0' if val == 0 else 'L1', Bs[mem[0]])

    def clause(self, lits):
        """lits = [(varpoint, polarity), x3] ; returns nothing.  polarity True = positive literal"""
        q1, q2 = self.fresh_point(), self.fresh_point()
        q3 = q1 ^ q2
        assert q3 not in self.pointset
        self.pointset.add(q3)
        line = (q1, q2, q3)
        B = self.add_check(self.place(line), line)
        for (pv, pol), qi in zip(lits, line):
            self.gadget('negate' if pol else 'copy', pv, qi)
            self.name(qi, '0', B)

    def build(self):
        return Code(self.cols, self.checks, self.T)
```

### 9.3 The verification scripts

#### `gadgets.py` — the exhaustive search that produced the COPY / NEGATE label sets

```python
"""Explicit minimal check-sets Phi realising the COPY and NEGATE gadgets."""
import itertools

K = 2
D = 1 << K
LOG = list(range(D))
TRIPLES = [(a, b, a ^ b) for a in LOG for b in LOG]
NT = len(TRIPLES)

M = {}
for y1 in LOG:
    for y2 in LOG:
        for y3 in LOG:
            m = 0
            for i, (f1, f2, f3) in enumerate(TRIPLES):
                if y1 == f1 or y2 == f2 or y3 == f3:
                    m |= 1 << i
            M[(y1, y2, y3)] = m

def rel_of(phi):
    out = []
    for y1 in LOG:
        for y2 in LOG:
            if any(phi & ~M[(y1, y2, y3)] == 0 for y3 in LOG):
                out.append((y1, y2))
    return frozenset(out)

targets = {
    "COPY   {(0,0),(1,1)}": frozenset({(0, 0), (1, 1)}),
    "NEGATE {(0,1),(1,0)}": frozenset({(0, 1), (1, 0)}),
}
best = {k: None for k in targets}
for phi in range(1 << NT):
    r = rel_of(phi)
    for k, t in targets.items():
        if r == t and (best[k] is None or bin(phi).count('1') < bin(best[k]).count('1')):
            best[k] = phi

for k, phi in best.items():
    tr = sorted(TRIPLES[i] for i in range(NT) if phi >> i & 1)
    print(f"{k}: |Phi| = {len(tr)}")
    for t in tr:
        print("      ", t)
    # witness y3 for each surviving pair
    for (y1, y2) in sorted(rel_of(phi)):
        ws = [y3 for y3 in LOG if phi & ~M[(y1, y2, y3)] == 0]
        print(f"      (y1,y2)=({y1},{y2}) admissible y3: {ws}")
```

#### `gadgetcheck.py` — re-verification of both gadgets with a value outside {0,l1,l2}

```python
"""Re-verify COPY and NEGATE with a NULL value added to Log (models dim Log > 2:
values outside {0,l1,l2} match no phi and must not create spurious solutions)."""
LOG = [0, 1, 2, 3]          # 0, l1, l2, l1+l2
EXTRA = ['N']               # any further value of a bigger Log
DOM = LOG + EXTRA

COPY = [(0,1,1),(0,2,2),(1,0,1),(1,1,0),(2,0,2)]
NEG  = [(0,0,0),(0,1,1),(1,1,0),(1,3,2),(2,0,2)]

def rel(phis):
    out = set()
    for y1 in DOM:
        for y2 in DOM:
            for y3 in DOM:
                if all(y1 == f1 or y2 == f2 or y3 == f3 for (f1, f2, f3) in phis):
                    out.add((y1, y2)); break
    return sorted(out)

for name, P in (("COPY", COPY), ("NEGATE", NEG)):
    print(f"{name}: zero-sum check", all((a ^ b) == c for a, b, c in P), " relation on (y1,y2):", rel(P))
```

#### `test_gadget.py` — reproduction of the gadget document's G_neq3

```python
"""Independent re-verification of the gadget document's G_neq3 (n=12) with our library."""
from islandv import from_checks, span, wt, in_span
from collections import Counter

Z = [(1,2,4,7,9),(0,1,6,7,10),(0,1,2,3,8,9),(0,1,4,5,11),
     (0,2,4,6,8,11),(4,5,6,7,10,11),(8,9,10,11)]
X = [(0,1,2,3),(4,5,6,7),(1,4,8,10),(0,6,8,11),(3,7,9,10)]
C = from_checks(12, [set(z) for z in Z], X)

print("dim ker H_Z =", len(C.kzb), " dim S_X =", len(C.sxb), " k =", C.k)
print("d_X =", C.dX(), " d_Z =", C.dZ())
spec = Counter(wt(v) for v in span(C.kzb) if v and not in_span(v, C.sxb, C.sxp))
print("X-logical weight spectrum:", dict(sorted(spec.items())))
L = C.csp()
for i, l in enumerate(L):
    print(f"  check {i} {C.xchecks[i]}  values {l}")
print("hypothesis (D):", C.hypD())
print("forbidden pairs:")
for i in range(len(L)):
    for j in range(i+1, len(L)):
        f = [(a, b) for a in set(L[i]) for b in set(L[j]) if C.forbidden(a, b)]
        if f: print(f"   checks {i},{j}: {len(f)} forbidden value pairs")
print("solution:", C.solve() is not None)
pts = C.points()
print("points: u -> (#pairs, #classes total, #classes used, checks)")
for u, d in sorted(pts.items()):
    print(f"   {u:#06x}: {d['npairs']:2d} {d['nclass_total']:2d} {d['nclass_used']:2d}  {d['checks']}")
```

#### `diag.py` — Corollary V.2 vs first-principles hook mechanics; Z diagnostics

```python
"""(1) Independent check of Corollary V.2 on a reduction instance, from the hook/prefix
       definition rather than from the 2|2-split value map.
   (2) Z-sector diagnostics: d_Z, Z-check weights."""
import itertools, time
from build2 import Builder
from islandv import in_span, rref, wt

def build(N, clauses, T=30, seed=3):
    b = Builder(T=T, seed=seed)
    pv = [b.fresh_point() for _ in range(N)]
    for cl in clauses: b.clause([(pv[v], pol) for (v, pol) in cl])
    return b.build(), b

def hooks(C, ci):
    """all (order -> list of hook indicator vectors) for a weight-4 X-check"""
    sup = list(C.xchecks[ci]); out = {}
    for pi in itertools.permutations(sup):
        out[pi] = [sum(1 << q for q in pi[i:]) for i in range(1, 4)]   # S_1,S_2,S_3
    return out

def is_logical(C, v):
    return C.syn(v) == 0 and not in_span(v, C.sxb, C.sxp)

def unary_safe(C, hs, datacols):
    """kinds (a) one hook, (b) hook + one data column, (c) two hooks of the same order"""
    for h in hs:
        if is_logical(C, h): return False
        for d in datacols:
            if is_logical(C, h ^ d): return False
    for a, b in itertools.combinations(hs, 2):
        if is_logical(C, a ^ b): return False
    return True

def pair_forbidden(C, hs1, hs2):
    return any(is_logical(C, a ^ b) for a in hs1 for b in hs2)

def verify_corV2(C, limit_pairs=None):
    m = len(C.xchecks)
    H = [hooks(C, i) for i in range(m)]
    datacols = [1 << q for q in range(C.n)]
    t0 = time.time()
    nun = 0
    for i in range(m):
        for pi, hs in H[i].items():
            if not unary_safe(C, hs, datacols): nun += 1
    # value map: order -> 2|2 split value in Q
    def val(i, pi):
        return C.canon((1 << pi[0]) | (1 << pi[1]))
    mism = 0; tested = 0
    pairs = list(itertools.combinations(range(m), 2))
    if limit_pairs: pairs = pairs[:limit_pairs]
    for i, j in pairs:
        for pi, hi in H[i].items():
            for pj, hj in H[j].items():
                a = pair_forbidden(C, hi, hj)
                b = C.forbidden(val(i, pi), val(j, pj))
                tested += 1
                if a != b: mism += 1
    return nun, mism, tested, time.time() - t0

if __name__ == "__main__":
    cls = [[(0, True), (1, True), (2, True)]]
    C, b = build(3, cls)
    print(f"instance: n={C.n}, {len(C.xchecks)} X-checks, k={C.k}")
    nun, mism, tested, el = verify_corV2(C)
    print(f"  unarily UNSAFE orders (Lemma V.1(2) predicts 0): {nun}")
    print(f"  order-pair relation vs Corollary V.2: {mism} mismatches out of {tested}  ({el:.1f}s)")
    zw = sorted({wt(r) for r in C.zrows})
    print(f"  Z-check weights present: {zw[:5]}...{zw[-3:]}  (#rows {len(C.zrows)})")
    print(f"  d_Z (search to weight 5): {C.dZ_low(5)}")
```

#### `extras.py` — the 2-forbidden relation; Corollary A1 on random codes

```python
"""(A) the '2 forbidden pairs' relation the gadget document's classification omits
   (B) Theorem: max Z-check weight <= 3  =>  the X-sector is a YES (verified on random codes)"""
import random, itertools
from islandv import Code, wt

# ---------- (A) ----------
def two_forbidden():
    # line L = {u1,u2,u3}; two checks c (base B), c' (base B'); ONE connector at u1.
    u1, u2 = 0b0001, 0b0010; u3 = u1 ^ u2
    B, Bp = 0b0100, 0b1000
    cols = [B, B^u1, B^u2, B^u3, Bp, Bp^u1, Bp^u2, Bp^u3]
    idx = {v: i for i, v in enumerate(cols)}
    c  = tuple(idx[v] for v in (B, B^u1, B^u2, B^u3))
    cp = tuple(idx[v] for v in (Bp, Bp^u1, Bp^u2, Bp^u3))
    K  = tuple(idx[v] for v in (B, B^u1, Bp, Bp^u1))          # the connector
    C = Code(cols, [c, cp, K], 4)
    L = C.csp()
    fb = [(a, b) for a in dict.fromkeys(L[0]) for b in dict.fromkeys(L[1]) if C.forbidden(a, b)]
    return C, L, fb

C, L, fb = two_forbidden()
print("(A) n=8, 3 weight-4 X-checks, cap set OK, k =", C.k, " d_X =", C.dX_cert())
print("    lists:", [sorted(set(x)) for x in L[:2]])
print("    forbidden value pairs between the two same-line checks:", len(fb), fb)
print("    (gadget doc 4.1 lists only 0, 1, 3 as possible)")

# ---------- (B) ----------
def rand_zweight3(rng, t=14, n=16):
    for _ in range(3000):
        cols = []
        cover = [0]*t
        ok = True
        for _ in range(n):
            for _try in range(200):
                w = rng.choice([2,3])
                s = rng.sample([z for z in range(t) if cover[z] < 3], w) if sum(1 for z in range(t) if cover[z]<3) >= w else None
                if s is None: break
                v = sum(1 << z for z in s)
                if v in cols: continue
                if any((v ^ x) in set(cols) for x in cols): continue
                cols.append(v)
                for z in s: cover[z] += 1
                break
            else:
                ok = False; break
        if not ok or len(cols) < 8: continue
        # zero-sum 4-subsets
        quads = []
        for q in itertools.combinations(range(len(cols)), 4):
            if cols[q[0]]^cols[q[1]]^cols[q[2]]^cols[q[3]] == 0: quads.append(q)
        if len(quads) >= 3:
            k = min(len(quads), rng.randint(3, 8))
            return cols, rng.sample(quads, k), t
    return None

rng = random.Random(5)
bad = 0; tested = 0; maxpairs = 0
for trial in range(300):
    r = rand_zweight3(rng)
    if r is None: continue
    cols, X, t = r
    try: C = Code(cols, X, t)
    except AssertionError: continue
    tested += 1
    P = C.points()
    maxpairs = max(maxpairs, max((d['npairs'] for d in P.values()), default=0))
    if max((d['nclass_used'] for d in P.values()), default=1) != 1: bad += 1
    if C.solve() is None: bad += 1
print(f"(B) random codes with all Z-check weights <= 3: {tested} tested, "
      f"max #u-pairs at any point = {maxpairs}, violations of "
      f"'1 class in use everywhere & X-sector YES' = {bad}")
```

#### `run3.py` — the named-formula runs of §5.3

```python
import itertools, random, time
from build2 import Builder

def sat(N, clauses):
    for a in itertools.product([False, True], repeat=N):
        if all(any(a[v] == pol for (v, pol) in cl) for cl in clauses): return True
    return False

def run(name, N, clauses, T=30, seed=0):
    t0 = time.time(); b = Builder(T=T, seed=seed)
    pv = [b.fresh_point() for _ in range(N)]
    for cl in clauses: b.clause([(pv[v], pol) for (v, pol) in cl])
    C = b.build(); ans = C.solve() is not None; exp = sat(N, clauses)
    P = C.points()
    bad = [(u, d['nclass_used']) for u, d in P.items()
           if u not in b.named_pts and u not in b.gadget_pts and d['nclass_used'] != 1]
    varbad = [(u, d['nclass_used']) for u, d in P.items() if u in b.named_pts and d['nclass_used'] < 2]
    ok = (ans == exp) and not bad
    print(f"{name:34s} n={C.n:4d} checks={len(C.xchecks):4d} k={C.k:3d} dX={C.dX_cert()} (D)={C.hypD()}"
          f" | CSP={ans!s:5s} SAT={exp!s:5s} {'OK ' if ok else '*** MISMATCH ***'}"
          f" free-aux-violations={len(bad)} thin-named={len(varbad)}  {time.time()-t0:5.1f}s", flush=True)
    return ok

ALL8 = [[(0,a),(1,b),(2,c)] for a in (True,False) for b in (True,False) for c in (True,False)]
tests = [("all 8 clauses on 3 vars (UNSAT)", 3, ALL8),
         ("7 of the 8 (SAT)", 3, ALL8[:7])]
ok = all(run(n,N,c,seed=3) for n,N,c in tests)
rng = random.Random(11)
for trial in range(8):
    N = 4; M = rng.choice([4,5,6])
    cls = []
    for _ in range(M):
        vs = rng.sample(range(N), 3)
        cls.append([(v, rng.random() < .5) for v in vs])
    ok &= run(f"random N=4 M={M} #{trial}", N, cls, seed=100+trial)
print("ALL OK:", ok)
```

#### `battery.py` — the 40-instance random battery

```python
import itertools, random, time
from build2 import Builder

def sat(N, cls):
    return any(all(any(a[v]==p for (v,p) in c) for c in cls)
               for a in itertools.product([False,True], repeat=N))

def run(N, clauses, seed):
    b = Builder(T=30, seed=seed)
    pv = [b.fresh_point() for _ in range(N)]
    for cl in clauses: b.clause([(pv[v], pol) for (v, pol) in cl])
    C = b.build()
    core, L, SY = C.reduced_csp()
    ans = C.solve() is not None; exp = sat(N, clauses)
    P = C.points()
    bad = sum(1 for u,d in P.items()
              if u not in b.named_pts and u not in b.gadget_pts and d['nclass_used'] != 1)
    return ans, exp, C, len(core), bad

rng = random.Random(2024)
nsat = nunsat = 0; fails = 0; t0=time.time()
rows=[]
for trial in range(40):
    N = rng.choice([3,4]); M = rng.choice([5,6,7,8])
    cls=[]
    for _ in range(M):
        vs = rng.sample(range(N),3)
        cls.append([(v, rng.random()<.5) for v in vs])
    ans, exp, C, core, bad = run(N, cls, seed=trial)
    if ans!=exp or bad: fails += 1; print("MISMATCH", trial, ans, exp, bad, flush=True)
    if exp: nsat += 1
    else: nunsat += 1
    rows.append((N,M,C.n,len(C.xchecks),core,C.k,ans,exp))
print(f"battery: {len(rows)} instances ({nsat} SAT, {nunsat} UNSAT), mismatches/structure-failures = {fails}, {time.time()-t0:.0f}s")
print("  sample rows (N,M,n,checks,core-after-reduction,k,CSP,SAT):")
for r in rows[:6]: print("   ", r)
print("  qubit counts:", min(r[2] for r in rows), "..", max(r[2] for r in rows),
      " checks:", min(r[3] for r in rows), "..", max(r[3] for r in rows),
      " core:", min(r[4] for r in rows), "..", max(r[4] for r in rows))
```

#### `battery2.py` — the SAT/UNSAT battery

```python
"""UNSAT-heavy battery: over 3 variables the 8 sign patterns are the only clauses that use
all three, so subsets of size 6,7,8 straddle the SAT/UNSAT boundary; plus 4-variable formulas
built to be unsatisfiable."""
import itertools, random, time
from build2 import Builder

def sat(N, cls):
    return any(all(any(a[v]==p for (v,p) in c) for c in cls)
               for a in itertools.product([False,True], repeat=N))

def run(N, clauses, seed):
    b = Builder(T=30, seed=seed)
    pv = [b.fresh_point() for _ in range(N)]
    for cl in clauses: b.clause([(pv[v], pol) for (v, pol) in cl])
    C = b.build()
    core, L, SY = C.reduced_csp()
    ans = C.solve() is not None; exp = sat(N, clauses)
    P = C.points()
    bad = sum(1 for u,d in P.items()
              if u not in b.named_pts and u not in b.gadget_pts and d['nclass_used'] != 1)
    thin = sum(1 for u,d in P.items() if u in b.named_pts and d['nclass_used'] < 2)
    return ans, exp, C, len(core), bad, thin

ALL8 = [[(0,a),(1,b),(2,c)] for a in (True,False) for b in (True,False) for c in (True,False)]
cases = []
for r in (6,7,8):
    for sub in itertools.combinations(range(8), r):
        cases.append((3, [ALL8[i] for i in sub]))
rng = random.Random(7)
# 4-variable unsatisfiable cores: all 8 patterns on {0,1,2} plus random extra clauses
for _ in range(6):
    extra = [[(v, rng.random()<.5) for v in rng.sample(range(4),3)] for _ in range(2)]
    cases.append((4, ALL8 + extra))
rng.shuffle(cases)
cases = [c for c in cases if len(c[1])>=7][:14] + [c for c in cases if len(c[1])<7][:8]
ns=nu=f=0; t0=time.time(); allD=set(); dxs=set()
for i,(N,cls) in enumerate(cases):
    ans, exp, C, core, bad, thin = run(N, cls, seed=i)
    allD.add(C.hypD()); dxs.add(C.dX_cert())
    if ans!=exp or bad or thin: f+=1; print("FAIL", i, N, len(cls), ans, exp, bad, thin, flush=True)
    (ns:=ns) ; 
    if exp: ns+=1
    else: nu+=1
print(f"battery2: {len(cases)} instances ({ns} SAT, {nu} UNSAT), failures = {f}, {time.time()-t0:.0f}s")
print("  hypothesis (D) values seen:", allD, "  d_X values seen:", dxs)
```

#### `zsector.py` — the poly-time all-schedules-safe certificate

```python
"""Z-sector: (a) a poly-time SUFFICIENT certificate that EVERY Z-schedule is safe;
              (b) an explicit safe Z-schedule for the d_Z = 3 block G_neq3."""
import itertools, random
from islandv import rref, in_span, kernel_rows, wt, from_checks
from build2 import Builder

def supported_subspace(basis, S):
    """basis of {v in span(basis) : supp(v) subset of S}"""
    mask = 0
    for q in S: mask |= 1 << q
    out = list(basis)
    # eliminate coordinates outside S
    for q in range(max((b.bit_length() for b in basis), default=0)):
        if mask >> q & 1: continue
        piv = None
        for i, v in enumerate(out):
            if v >> q & 1: piv = i; break
        if piv is None: continue
        p = out.pop(piv)
        out = [v ^ p if v >> q & 1 else v for v in out]
    return [v for v in out if v]

def all_orders_safe(C, extra=1, verbose=False):
    """TRUE  =>  every Z-schedule of C has d_eff^Z >= 3 (sufficient, not necessary).
    Checks: no vector of ker H_X \\ S_Z is supported inside supp(z) u supp(z') u {<=extra qubits}."""
    kerX = kernel_rows(C.SX, C.n)
    kb, kp = rref(kerX)
    szb, szp = rref(C.zrows)
    sup = [[q for q in range(C.n) if C.zrows[z] >> q & 1] for z in range(C.t)]
    def bad(S):
        for v in supported_subspace(kb, S):
            if v and not in_span(v, szb, szp): return v
        return None
    for z in range(C.t):
        b = bad(sup[z])
        if b: return False, ('single', z, b)
        for q in range(C.n):
            if C.zrows[z] >> q & 1: continue
            b = bad(sup[z] + [q])
            if b: return False, ('hook+data', z, q, b)
    for z1, z2 in itertools.combinations(range(C.t), 2):
        b = bad(sorted(set(sup[z1]) | set(sup[z2])))
        if b: return False, ('two hooks', z1, z2, b)
    return True, None

# ---------------- explicit safe Z-schedule for G_neq3 ----------------
Zc = [(1,2,4,7,9),(0,1,6,7,10),(0,1,2,3,8,9),(0,1,4,5,11),
      (0,2,4,6,8,11),(4,5,6,7,10,11),(8,9,10,11)]
Xc = [(0,1,2,3),(4,5,6,7),(1,4,8,10),(0,6,8,11),(3,7,9,10)]

def zsched_search(seed=0, tries=200000):
    C = from_checks(12, [set(z) for z in Zc], Xc)
    kerX = kernel_rows(C.SX, C.n); kb, kp = rref(kerX)
    szb, szp = rref(C.zrows)
    def islog(v):
        return v != 0 and in_span(v, kb, kp) and not in_span(v, szb, szp)
    datacols = [1 << q for q in range(12)]
    def hooks(order):
        return [sum(1 << q for q in order[i:]) for i in range(1, len(order))]
    rng = random.Random(seed)
    for _ in range(tries):
        orders = [tuple(rng.sample(z, len(z))) for z in Zc]
        H = [hooks(o) for o in orders]
        ok = True
        flat = [(i, h) for i, hs in enumerate(H) for h in hs]
        for i, h in flat:
            if islog(h): ok = False; break
            if any(islog(h ^ d) for d in datacols): ok = False; break
        if ok:
            for (i, a), (j, b) in itertools.combinations(flat, 2):
                if islog(a ^ b): ok = False; break
        if ok: return orders
    return None

if __name__ == "__main__":
    cls = [[(0, True), (1, True), (2, True)]]
    b = Builder(T=30, seed=3)
    pv = [b.fresh_point() for _ in range(3)]
    for cl in cls: b.clause([(pv[v], pol) for (v, pol) in cl])
    C = b.build()
    ok, w = all_orders_safe(C)
    print("main block: every Z-schedule safe?", ok, "" if ok else w)
    o = zsched_search()
    print("G_neq3 safe Z-schedule:", o)
```

#### `zg2.py` — exact decision of G_neq3's Z-sector

```python
"""Exact decision of the Z-sector of G_neq3 (d_Z = 3): full pair tables + forward checking."""
import itertools
from islandv import rref, in_span, kernel_rows, from_checks
Zc=[(1,2,4,7,9),(0,1,6,7,10),(0,1,2,3,8,9),(0,1,4,5,11),(0,2,4,6,8,11),(4,5,6,7,10,11),(8,9,10,11)]
Xc=[(0,1,2,3),(4,5,6,7),(1,4,8,10),(0,6,8,11),(3,7,9,10)]
C=from_checks(12,[set(z) for z in Zc],Xc)
kb,kp=rref(kernel_rows(C.SX,C.n)); szb,szp=rref(C.zrows)
LOG={}
def islog(v):
    r=LOG.get(v)
    if r is None:
        r = v!=0 and in_span(v,kb,kp) and not in_span(v,szb,szp); LOG[v]=r
    return r
dat=[1<<q for q in range(12)]
def hooks(o): return [sum(1<<q for q in o[i:]) for i in range(1,len(o))]
D=[]
for z in Zc:
    safe=[]
    for o in itertools.permutations(z):
        hs=hooks(o)
        if any(islog(h) for h in hs): continue
        if any(islog(h^d) for h in hs for d in dat): continue
        if any(islog(a^b) for a,b in itertools.combinations(hs,2)): continue
        safe.append(hs)
    D.append(safe)
print("domain sizes:", [len(d) for d in D], flush=True)
m=len(D)
comp={}
for i in range(m):
    for j in range(i+1,m):
        tab=[]
        for a in D[i]:
            mask=0
            for bj,b in enumerate(D[j]):
                if not any(islog(x^y) for x in a for y in b): mask |= 1<<bj
            tab.append(mask)
        comp[(i,j)]=tab
print("pair tables built", flush=True)
FULL=[(1<<len(d))-1 for d in D]
def bt(i, doms):
    if i==m: return []
    d=doms[i]
    while d:
        b=d & -d; ai=b.bit_length()-1; d^=b
        nd=list(doms)
        ok=True
        for j in range(i+1,m):
            nd[j] &= comp[(i,j)][ai]
            if nd[j]==0: ok=False; break
        if ok:
            r=bt(i+1,nd)
            if r is not None: return [ai]+r
    return None
r=bt(0,FULL)
print("G_neq3 Z-sector satisfiable:", r is not None)
if r: print("  witness order indices:", r)
```

#### `relsearch.py` — full enumeration of the expressible one-line binary language

```python
"""Which binary relations can a single LINE with a PRIVATE third point express?

Setting (LINE-SECTION, see report):  variables are points u of S; value g~(u) in Log.
A check on the line L = {u1,u2,w} is a zero-sum triple (f1,f2,f3) in Log^3
(f1^f2^f3 = 0) and is satisfied iff  y1=f1 or y2=f2 or y3=f3.
If w is private to this line, y3 is existentially quantified.
"""
import itertools, sys

K = int(sys.argv[1]) if len(sys.argv) > 1 else 2   # dim Log
D = 1 << K                                          # |Log|
LOG = list(range(D))

TRIPLES = [(a, b, a ^ b) for a in LOG for b in LOG]  # f1^f2^f3 = 0
NT = len(TRIPLES)
assert NT == D * D

# M[y1][y2][y3] = bitmask of triples satisfied by (y1,y2,y3)
M = {}
for y1 in LOG:
    for y2 in LOG:
        for y3 in LOG:
            m = 0
            for i, (f1, f2, f3) in enumerate(TRIPLES):
                if y1 == f1 or y2 == f2 or y3 == f3:
                    m |= 1 << i
            M[(y1, y2, y3)] = m

def rel_of(phi):
    """phi = bitmask over TRIPLES -> frozenset of (y1,y2) surviving."""
    out = []
    for y1 in LOG:
        for y2 in LOG:
            if any(phi & ~M[(y1, y2, y3)] == 0 for y3 in LOG):
                out.append((y1, y2))
    return frozenset(out)

seen = {}
for phi in range(1 << NT):
    r = rel_of(phi)
    if r not in seen or bin(phi).count('1') < bin(seen[r]).count('1'):
        seen[r] = phi

print(f"dim Log = {K}, |Log| = {D}, #zero-sum triples = {NT}")
print(f"distinct expressible binary relations: {len(seen)}")

# classify by size
from collections import Counter
print("sizes:", sorted(Counter(len(r) for r in seen).items()))

# is a "not-equal on a 3-subset" among them?
targets = {}
for Dsub in itertools.combinations(LOG, 3):
    neq = frozenset((a, b) for a in Dsub for b in Dsub if a != b)
    targets[f"NEQ3 on {Dsub}"] = neq
for Dsub in itertools.combinations(LOG, 3):
    eq = frozenset((a, a) for a in Dsub)
    targets[f"EQ3 on {Dsub}"] = eq
for Dsub in itertools.combinations(LOG, 2):
    eq = frozenset((a, a) for a in Dsub)
    targets[f"EQ2 on {Dsub}"] = eq
    neq = frozenset((a, b) for a in Dsub for b in Dsub if a != b)
    targets[f"NEQ2 on {Dsub}"] = neq

for name, t in sorted(targets.items()):
    print(f"  {name:22s} expressible: {t in seen}")
```

#### `nae.py` — the (negative) search for EQ/NEQ gadgets in the Fano line hypergraph

```python
"""Hypergraph 2-colouring on LINE hypergraphs of F_2^t: gadget search.

A line is {u,v,u+v}.  A NAE constraint on a line = the line is not monochromatic.
We look for a set of lines that pp-defines  col(x) != col(y)  (auxiliaries existential).
"""
import itertools, sys

def lines(t, pts=None):
    P = pts if pts is not None else [x for x in range(1, 1 << t)]
    S = set(P)
    out = set()
    for a, b in itertools.combinations(P, 2):
        c = a ^ b
        if c in S: out.add(frozenset((a, b, c)))
    return sorted(out, key=lambda l: sorted(l))

def induced(t, L, x, y):
    """set of (col(x),col(y)) over all 2-colourings of F_2^t\\{0} with no monochromatic line in L"""
    P = sorted({p for l in L for p in l})
    idx = {p: i for i, p in enumerate(P)}
    res = set()
    for mask in range(1 << len(P)):
        ok = True
        for l in L:
            bits = [mask >> idx[p] & 1 for p in l]
            if bits[0] == bits[1] == bits[2]: ok = False; break
        if ok:
            res.add((mask >> idx[x] & 1, mask >> idx[y] & 1))
    return res

def search(t, maxlines, x, y, target):
    P = [p for p in range(1, 1 << t)]
    L = lines(t)
    L = [l for l in L]
    best = None
    for r in range(2, maxlines + 1):
        for sub in itertools.combinations(L, r):
            pts = {p for l in sub for p in l}
            if x not in pts or y not in pts: continue
            if induced(t, sub, x, y) == target:
                return sub
    return None

if __name__ == "__main__":
    t = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    x, y = 1, 2
    NEQ = {(0, 1), (1, 0)}
    EQ = {(0, 0), (1, 1)}
    print(f"t={t}: #points={2**t-1}, #lines={len(lines(t))}")
    for name, tgt in (("NEQ", NEQ), ("EQ", EQ)):
        g = search(t, 5, x, y, tgt)
        print(f"  {name} gadget:", [sorted(l) for l in g] if g else "none with <=5 lines")
```
