# Amendment 1 to `circdist_lift_iff_proof_20260820.md`

**Node:** `CIRCDIST.lift` · **Date:** 2026-08-20 · **Role:** proposer applying an independent
reviewer's repairs. This file is **append-only**: it does not modify the amended document, which
remains the record of what was originally claimed. Where this amendment and the original conflict,
**this amendment governs**.

---

## 0. Hash chain

```
amended document      artifacts/circdist_lift_iff_proof_20260820.md
  SHA-256             97cb3c8da839d1b96f58c281145cec8b70269ed3e6dfb29136f0bda00f564979
  size                90225 bytes, 1497 lines

review acted on       artifacts/circdist_lift_proofs_review_20260820.md
  SHA-256             fa75f0405a9e233cc45aae2cf01458caef45d65cfef9bc0a44cbca19f0d0189f

sibling document      artifacts/circdist_lift_nonint_proof_20260820.md   (source of the imported
  SHA-256             42d6c138c1ea19127db76ab4f22d2a64c1d1e1e96adf76af975076b529a71f4c
                      collision convention: its Definition 2.8 and Lemma 7.2)

frozen definitions    research/circdist/notes/CIRCDIST_PROBLEMS.md  (公共定义; not modified)
```

If any of the three hashes above fails to reproduce, this amendment is void and must be re-derived
against the current text.

**Epistemic ceiling.** Nothing here is labelled PROVED. Arguments are **CONJECTURED**; the
computations of §6 are **NUMERICAL** with the code inline and are exact over `F₂` (integers used as
bit-masks; no floating point, no external libraries, no `stim`). The repairs are the reviewer's;
the write-up, the verifications and any residual error are mine.

**Scope discipline.** This amendment applies exactly the six edits the review requests
(its §7 table) and nothing else. It does not re-open any result the review confirms, does not
strengthen any statement, and does not touch `research/circdist/proof-dag/`.

---

## 1. Index of repairs

| # | target in the original | review item | kind | status |
|---|---|---|---|---|
| **A1** | Definition 5.1, Lemma 5.3; the (⟸) of 5.7 and of 5.11 | review §3.1, §3.2 (edit 2) | **correction** — false justification replaced; statement about `ℓ(γ)` weakened, every downstream use intact | applied + verified |
| **A2** | §5.10(1) and §8 item 4 | review §3.3 (edit 1) | **RETRACTION** — the statement is false as written | applied + verified |
| **A3a** | §8 item 3(ii) (from NUMERICAL 3.7) | review §3.4(a) (edit 3) | precision | applied + verified |
| **A3b** | §3.2 vs NUMERICAL 3.6 | review §2.2, §7 (edit 4) | precision (disambiguation) | applied + verified |
| **A3c** | Definition 1.6, and the last line of §2.2 Step 3 | review §3.4(b) (edit 5) | precision (index range) | applied + verified |
| **A4** | §5.2 (Lemma 5.3's construction) | review §4.3 final paragraph (edit 6) | addition of a true-but-unstated fact | applied |

---

## 2. Repair A1 — the `≤` direction: one Pauli per location

### 2.1 Before

Definition 5.1 of the original reads

> `ℓ_R(γ) := min{ |F| : F ⊆ 𝔽 × {0,…,R−1}, ∂F = 0, π_1 F = γ }`

— a minimum over **formal subsets of (fault type) × (round)** — and the derivation of Lemma 5.3
contains the sentence

> "these are `w = |γ|` distinct circuit locations, **since distinct residuals force distinct
> locations**."

### 2.2 Why it is wrong

The quoted sentence is false, and the original refutes it three pages earlier. Its own
Proposition 1.13.4 states that

> "on a gate `a→q_j` the possible residuals are `∅, S_j, {q_j}, S_{j−1}`"

— four distinct residual classes available at **one** location. Under the frozen fault model
(Definition 1.8, and the sibling document's Definition 2.8) a location carries **one** Pauli, so two
of those four cannot be placed as two weight-1 faults: the `X⊗X` composite at that gate is a
*single* weight-1 fault, whose residual is `S_{j−1}` and whose `π₁`-image is the basis vector
`[S_{j−1}]`, **not** `[S_j] + [{q_j}]`.

The `≥` direction is untouched: a realisable configuration has at most one Pauli per location, so it
*is* a subset of `𝔽 × {0,…,R−1}` in the sense of Definition 5.1, and Proposition 5.4 counts `n_E`
per fault, i.e. per location. Only the `≤` direction is exposed.

### 2.3 After — corrected Definition 5.1

> **Definition 5.1′ (lift length, realisable form).** A *fault configuration* of `C_R(M)` is a
> choice, for each location of the circuit, of one Pauli (or one bit flip, at a `meas` location),
> all but finitely many trivial; `|F|` is the number of non-trivial locations. This is Definition
> 2.8 of `circdist_lift_nonint_proof_20260820.md`, adopted here verbatim. Then
>
> ```
>    ℓ_R(γ) := min{ |F| : F a fault configuration of C_R(M), ∂F = 0, π₁F = γ }   (= +∞ if none),
>    ℓ(γ)  := lim_{R→∞} ℓ_R(γ).
> ```
>
> Composition of two elementary Paulis at one location is the same `F₂` sum, so `∂`, `E`, `s`, `u`
> and `λ` are unchanged by re-reading a two-atom same-location pair as one fault; only `|F|` drops
> by one. The convention therefore only ever makes `d_circ` **smaller**, which is the conservative
> choice for an upper bound.

### 2.4 After — corrected Lemma 5.3

> **CONJECTURED 5.3′ (`≤` direction).** For every `γ ∈ L_eff`,
>
> ```
>    d_circ( C_R(M) )  ≤  |γ| + repair(γ)  <  ∞
> ```
>
> as soon as `R` exceeds the round-span of the optimal certificate. Moreover, if the optimal
> certificate admits representatives `f_1,…,f_{|γ|}` occupying `|γ|` **distinct** locations, then
> also `ℓ(γ) ≤ |γ| + repair(γ)`.
>
> *Derivation.* Take an optimal certificate `(r_i, u_i)` and, for each `i`, a fault `f_i` with
> `E(f_i) = E_i`, `u(f_i) = u_i`, placed in round `r_i`. Put `D := A_0 + xC` and add, for each
> `(b,r) ∈ supp(D)`, the classical flip of `m_{b,r}` — by (V) a weight-1 fault with `E = ∅`,
> `s = 0`, `u = e_b`. These `wt(D)` faults are at `meas` locations, hence distinct from each other
> and from every `f_i`. Two cases.
>
> *(a) No collision.* The `f_i` occupy `|γ|` distinct locations. Then `F` is a fault configuration
> of weight exactly `|γ| + wt(D) = |γ| + repair(γ)`, with total detector chain
> `(1+x)(D + D) = 0` and `π₁F = γ`, so `λ(F) = λ_eff(γ) ≠ 0`. Hence `ℓ(γ) ≤ |γ| + repair(γ)` and
> `d_circ ≤ |γ| + repair(γ)`.
>
> *(b) Collision.* Two representatives share a location; compose them there. `∂` is additive at a
> common (location, round) — it is `F₂`-linear in the Pauli — so the composed configuration `F′`
> still has `∂F′ = 0`; and the observable is the parity functional of `Σ_f E(f)`, which is likewise
> additive at a common location, so `λ(F′) = λ_eff(γ) ≠ 0`. Thus `F′` is an undetectable
> observable-flipping fault configuration with `|F′| ≤ |γ| + repair(γ) − 1`, and
> `d_circ ≤ |γ| + repair(γ)` holds **a fortiori**. (`π₁F′ ≠ γ` in this branch — at a gate
> `a→q_j` the composite has residual `S_{j−1}`, not `[S_j]+[{q_j}]` — so no claim about `ℓ(γ)`
> for that particular `γ` is made.) ∎
> *Derivation status: complete. Model inputs: (V), and Definition 5.1′'s per-location weight.*

### 2.5 When branch (b) cannot occur

Imported from the sibling document, whose treatment the review confirms (verdict M, "the correct
treatment of exactly the defect in F"):

> **Lemma 7.2 of `circdist_lift_nonint_proof_20260820.md` (imported).** With `γ` a **minimum-weight**
> effective logical and the representatives of that document's Lemma 5.4, the only location that can
> carry two representatives is a CNOT `a → q^a_j`, whose control-`X` represents `S_a(j)` and whose
> target-`X` represents `{q^a_j}`. If both `S_a(j)` and `{q^a_j}` lie in `γ`, then since
> `q^a_j ∉ S_a(j)` we have `S_a(j) + {q^a_j} = S_a(j−1) ∈ ℰ`, and
> `γ′ := γ + [S_a(j)] + [{q^a_j}] + [S_a(j−1)]` satisfies `∂_eff γ′ = 0`, `λ_eff γ′ ≠ 0` and
> `|γ′| ≤ |γ| − 1` — contradicting minimality.

So at a minimum-weight `γ`, under those representatives, branch (a) applies and `ℓ(γ)` itself is
bounded. That is exactly the case every downstream use needs.

### 2.6 What survives, item by item

| original statement | after A1 |
|---|---|
| **5.4** (all four parts) | **unchanged.** It counts `n_E` per fault, i.e. per location, and (V) bounds the monomials of an empty-residual fault per location. Nothing in it reads Definition 5.1. |
| **5.6(a)** `d_circ = min_γ ℓ(γ)` | **survives verbatim** under 5.1′. `≤`: a closed lift is an undetectable logical configuration. `≥`: a minimum-weight `F` is itself a configuration and a closed lift of `γ = π₁F`. |
| **5.6(b)** lower `|γ| + min(repair,2) ≤ ℓ(γ)` | **survives verbatim** (it is 5.4(4), untouched). |
| **5.6(b)** upper `ℓ(γ) ≤ |γ| + repair(γ)` | **weakened**: holds when the optimal certificate admits distinct-location representatives (5.3′(a)); unconditionally only in the form `d_circ ≤ |γ| + repair(γ)`. |
| **5.6(c)** `ℓ(γ) = |γ| + repair(γ)` for `repair ≤ 2` | **weakened** in the same way; the two-sided sandwich still pins `ℓ(γ)` whenever branch (a) applies, which by §2.5 includes every minimum-weight `γ`. |
| **5.6(d)** `d_circ = min_γ(|γ| + repair(γ))` when the minimiser has `repair ≤ 2` | **survives verbatim.** `≤` is 5.3′ a fortiori; `≥` is 5.4(4). |
| **5.7** the node's biconditional | **survives verbatim** — see §2.7. |
| **5.8** the `|γ| = 2` closed form | **unchanged** (it computes `wt(A_0 + xC)`, a statement about certificates, not about locations). |
| **5.9 / 5.10(2),(3)** | **unchanged.** |
| **5.11** non-interleaved equality | **survives verbatim** — see §2.7. |

### 2.7 The two places that cite 5.3, with the collision line added

**5.7 (⟸), amended.** *If `∃γ ∈ L_eff` with `|γ| = d_eff` and `repair(γ) = 0`, then
`d_circ = d_eff`.* By 5.3′, `d_circ ≤ |γ| + repair(γ) = d_eff`, **in either branch**: if the
representatives collide, composing them at the common location leaves `∂` and `λ` unchanged (both
are `F₂`-linear in the Pauli at a fixed location and round) and only lowers the weight, so
`d_circ ≤ d_eff − 1`, which together with `d_circ ≥ d_eff` from 5.4(1) is a contradiction — i.e. the
collision cannot occur here, and either way `d_circ ≤ d_eff`. With 5.4(1) (`d_circ ≥ d_eff`),
equality. The **(⟹)** direction never cites 5.3 and is unchanged.

**5.11, amended.** The non-interleaved argument exhibits a same-round certificate with `A_0 = 0`,
`C = 0`, hence `repair(γ) = 0` for every `γ`. Applying 5.3′ to a minimum-weight `γ` gives
`d_circ ≤ |γ| = d_eff` in branch (a), and `d_circ ≤ d_eff − 1` in branch (b) — which 5.4(1)
excludes. So `d_circ ≤ d_eff`, and with 5.4(1), equality, for all `R ≥ 1`. Unchanged conclusion.
(The sibling document's Lemma 7.2 makes branch (b) impossible outright at a minimum-weight `γ`;
the cross-reference already in §5.11 should now be read as covering this point too.)

### 2.8 Local verification (NUMERICAL, §6 code, block `[A1]`)

Steane `[[7,1,3]]`, `H_X = H_Z = {345 6, 1256, 0246}`, X-check `a = (3,4,5,6)` in that CNOT order:

```
gate a->q_2 : residuals available at this ONE location = { ∅ , S_2={5,6} , {q_2}={4} , S_1={4,5,6} }
              -> four distinct classes at one location; "distinct residuals force distinct
                 locations" is false, exactly as Proposition 1.13.4 says.

for every j : S_j ⊔ {q_j} = S_{j−1}  and  s(S_j)+s({q_j}) = s(S_{j−1})  and  λ(S_j)+λ({q_j}) = λ(S_{j−1})
              failures = 0 / 4   (exact F₂, all three identities)
```

and the weight bookkeeping of Lemma 7.2 is algebraic: `γ′` deletes two basis vectors of `γ` and adds
at most one, so `|γ′| ≤ |γ| − 1` strictly.

---

## 3. Repair A2 — **RETRACTION** of `R_sat(M) ≤ d`

### 3.1 What is retracted

Two sentences of the original:

* **§5.10(1):** "`d_R(M)` is non-increasing in `R` and **constant for all `R ≥ d`**; i.e.
  `R_sat(M) ≤ d` in the sense of `CIRCDIST.sat`, for this model."
* **§8 item 4:** "A `CIRCDIST.sat` deliverable falls out. 5.10(1): `R_sat(M) ≤ d` for every
  single-ancilla CSS schedule with ideal boundaries, per sector."

The clause "`i.e. R_sat(M) ≤ d`" in the first, and the whole of the second, are **withdrawn as
false**. This is a retraction, not a rewording: a `CIRCDIST.sat` session adopting §8 item 4 verbatim
would adopt a false statement.

### 3.2 Why it is false

The frozen definition (公共定义, 课题四) saturates at the **code distance**:

```
   R_sat(M) = min{ R_0 : d_R(M) = d  for all R ≥ R_0 } ,      = ∞ if no such R_0 .
```

Contiguity (5.9) proves that `d_R` is eventually **constant**, with limiting value `d_∞(M)`. It says
nothing about that constant being `d`. Whenever `d_∞(M) < d` — the generic hook-damaged case —
no `R_0` exists at all and `R_sat(M) = ∞`.

The original document already contains a counterexample to its own claim: NUMERICAL 5.14 reports
"Both Steane non-interleaved circuits give `d_circ = 2 = d_eff` at `R = 2,3,4`", i.e. `d_R = 2 < 3 = d`
for those `R`, so `R_sat = ∞ > 3 = d`.

### 3.3 Counterexample, recomputed this session (NUMERICAL, §6 block `[A2]`)

Steane `[[7,1,3]]`, natural within-check orders (`supp` in index order), **non-interleaved** (either
block order), legal, `MC = ∅` (non-interleaving makes every `c_{ab}` equal to `0` or to the even
number `|supp(a) ∩ supp(b)|`):

```
realisable residual classes ℰ∖{∅}                      : 15
minimum-weight effective logical                       : |γ| = 2,  γ = { {0} , {5,6} }
     {0}   is a singleton residual;   {5,6} = S_2 is a suffix of the order (3,4,5,6)
     χ_{0} + χ_{5,6} = e_0+e_5+e_6 ∈ ker H_Z ∖ S_X      (checked exactly)
d_eff(M) = 2 ,  d(Q) = 3
non-interleaved ⇒ d_R(M) = d_eff(M) = 2 for every R ≥ 1     (5.11 / sibling Theorem 7.1)
⇒ d_R never equals d = 3 ⇒ R_sat(M) = ∞ , not ≤ d = 3 .
```

### 3.4 Corrected statements

Replace §5.10(1) by:

> **CONJECTURED 5.10(1′) (finite window; corrected).** `d_R(M)` is non-increasing in `R` and
> **constant for all `R ≥ d`**, with limiting value `d_∞(M) = d_{R=d}(M)`. Equivalently, in the
> `CIRCDIST.sat` window language, `B(r,d) = d`: whether a given value is attained is decided by
> finitely many `R`, and `R ≤ d` suffices. **Consequently**
>
> ```
>       R_sat(M)  ≤  d       if  d_∞(M) = d ,
>       R_sat(M)  =  ∞       if  d_∞(M) < d ,
> ```
>
> and in either case `R_sat(M)` is decided by inspecting `R = 1,…,d`. *Derivation:* the
> monotonicity and constancy statements are the original derivation of 5.10(1), unchanged (a
> minimum-weight witness of weight `w ≤ d` has round-span `≤ w ≤ d` by 5.9, and the bulk is
> time-translation invariant with both temporal boundaries fully detectored by 4.1, so it embeds in
> every `C_{R′}` with `R′ ≥ w`). The dichotomy is then immediate from the frozen definition of
> `R_sat` together with `d_eff ≤ d_circ ≤ d`. ∎

Replace §8 item 4 by:

> 4. **A `CIRCDIST.sat` deliverable falls out, in the corrected form.** 5.10(1′): for every
>    single-ancilla CSS schedule with ideal boundaries, per sector, `d_R` is constant for `R ≥ d`,
>    so the window bound is `B(r,d) = d`; and `R_sat(M) ≤ d` **iff** `d_∞(M) = d`, otherwise
>    `R_sat(M) = ∞`. The finite-window content is the real deliverable; the identification of it
>    with `R_sat` was an error and is withdrawn. The `sat` node should check whether its
>    commission's model coincides with §1 before adopting even the corrected form.

### 3.5 Consistency with the sibling document

The sibling document's **Corollary 7.3** —

```
   R_sat(M) = 1   if d_eff(M) = d ,          R_sat(M) = ∞   if d_eff(M) < d
```

for non-interleaved `M` — is correct, and is the specialisation of 5.10(1′) to the class where
`d_∞ = d_eff` at `R = 1`. Before this amendment the two documents **contradicted** each other on
exactly this point; after it they agree, with 5.10(1′) the general statement and Corollary 7.3 the
non-interleaved instance.

### 3.6 What does **not** change

`R_sat` is a cross-node corollary. It is not a premise of Theorem 1, of the (MC) equivalence, of
5.4, of 5.6, of 5.7, of 5.9 or of 5.11 — the finite-window fact (`span ≤ weight ≤ d`) is what those
use, and it survives intact. §8 item 2's "`P1.4` (finite window) is **discharged** by 5.9 with
`B(r,d) = d`" is therefore also unaffected.

---

## 4. Repair A3 — three precision defects

### 4.1 A3a — "every gross-code hook has `|s| ≥ 3`" is false for `S = supp(a)`

**Before** (§8 item 3(ii)): "*(ii)* every gross-code hook has `|s| ≥ 3` (NUMERICAL 3.7), so diagonal
hooks are the generic case and the surface-code `|s| = 1` argument has no analogue".

**Why it is wrong.** NUMERICAL 3.7 tabulates the `62` **proper** non-empty subsets of a
weight-6 X-check support (`2^6 − 2 = 62`). The 63rd non-empty subset is `S = supp(a) = S_a(0)`,
which is a genuinely realisable hook — an `X` on `anc(a)` inserted before its first CNOT — and it
has `s = 0`, because `|supp(a) ∩ supp(b)|` is even for every `b` by (CSS).

**After.** §8 item 3(ii) should read:

> *(ii)* every **proper** gross-code hook has `|s| ≥ 3` (NUMERICAL 3.7; the improper hook
> `S_a(0) = supp(a)` has `s = 0` and `λ = 0`, so it is a stabiliser residual and never enters a
> `γ ∈ L_eff`), so diagonal hooks are the generic case and the surface-code `|s| = 1` argument has
> no analogue.

The parenthetical matters because this item is being registered as a cross-node premise for
`CIRCDIST.gross`; the unqualified form is literally false and would be inherited as such.

**Verification** (NUMERICAL, §6 block `[A3a]`; independent rebuild of the gross code from
`ℓ=12, m=6, A = x³+y+y², B = y³+x+x²`):

```
X_{0,0} support                       : {1, 2, 18, 75, 78, 84}    (matches the document)
overlap histogram over 72×72 pairs    : {0: 4536, 2: 648}          (matches)
|s(S)| over the 62 PROPER nonempty S  : {3: 12, 4: 18, 5: 18, 6: 12, 9: 2}   (matches; min = 3)
|s(S)| for S = supp(a) (the 63rd)     : 0                          <-- the counterexample
```

The `(i)` and `(iii)` clauses of §8 item 3 are unaffected: `(i)` is Theorem 1, which is about
*vertical* hooks and holds for all hooks including `S_a(0)` (which is horizontal, `u ∈ {0,s} = {0}`),
and `(iii)` is a restatement of 5.7.

### 4.2 A3b — per-pair vs global "vertical"

**The equivocation.** Theorem 3.2's hypothesis is the **per-pair** condition
`u_b(S) = 1 ∧ s_b(S) = 0` for one Z-check `b`. Definition 1.12's word "vertical" is the **global**
condition `s(S) = 0 ≠ u(S)` on the whole vector. NUMERICAL 3.6's table row is labelled
"VERTICAL (`s = 0 ≠ u`)", i.e. it measures the global version, and therefore does **not** test the
theorem's actual hypothesis. The reported `0` is true, but it is the weaker of the two facts.

**After.** Adopt the following terminology and restatements.

> **Definition 1.12′ (per-pair refinement).** For a fault `f` and a Z-check `b`, say `f` is
> *`b`-vertical* if `s_b(f) = 0 ≠ u_b(f)`. Say `f` is *vertical* (Definition 1.12, unchanged) if
> `s(f) = 0 ≠ u(f)`. Then
>
> ```
>       f vertical   ⟹   f is b-vertical for some b ,
> ```
>
> and the converse fails in general.

* **Theorem 3.2, restated:** "if a hook `S` of `a` is **`b`-vertical** for some `b ∈ ℬ` — that is,
  `u_b(S) = 1` and `s_b(S) = 0` — then `|supp(a) ∩ supp(b)| ≥ 4`." This is what the derivation
  actually proves, and it is **stronger** than the global reading (by the implication above,
  it implies "no vertical hook at overlap ≤ 2" but not conversely).
* **NUMERICAL 3.6, restated:** the last row should be labelled
  "**VERTICAL** (global, `s = 0 ≠ u`) | **0**" and a second row added,
  "**`b`-VERTICAL for some `b`** (per-pair, the hypothesis of Theorem 3.2) | **0**". The scan as
  reported measured the first; the second is what licenses the "Theorem 1, confirmed" gloss.
  The gloss is correct — because the per-pair count is also zero — but for a reason the printed
  table does not exhibit.
* Everywhere else in the document, "vertical" means the global condition and is used only in
  Definition 1.12's taxonomy and in §3.5's abundance discussion, where the global reading is the
  intended one. §8 item 3(i) ("no gross-code hook is a **vertical** edge") should be read in the
  stronger per-pair sense, which is what Theorem 1 delivers.

**Verification** (NUMERICAL, §6 block `[A3b]`). Theorem 3.2 depends on the schedule only through
(i) which overlap qubits lie in the suffix `S` (necessarily a suffix of the overlap in `a`'s order)
and (ii) the bit `χ(q) = [t(q→b) > t(a→q)]`. Exhausting **all** such configurations at every even
overlap size — a complete verification of the per-pair statement over all codes and all schedules
simultaneously, conditional only on the propagation inventory 1.13.2:

```
   m   #(u_b = 1, s_b = 0) under (MC)   without (MC)
   0            0                              0
   2            0                              2
   4            4                             12
   6           32                             64
   8          192                            320
```

Zero at `m ≤ 2` under (MC), non-zero at `m ≥ 4`: the threshold is exactly 4 and is tight. Since
global-vertical implies `b`-vertical for some `b`, the per-pair zero implies the table's global zero.

### 4.3 A3c — the missing `r ≤ R−1` in Definition 1.6

**Before** (Definition 1.6, last sentence but one): "In addition the Z-memory carries X-check
detectors `D_{a,r} = m_{a,r} + m_{a,r−1}` for `r ≥ 1` only (the round-0 X outcome is random)."

**Why it is wrong.** The upper limit is missing. The terminal readout of Definition 1.5 is
**transversal Z**, so it supplies a virtual `m_{b,R}` for `b ∈ ℬ` but **no** `m_{a,R}` for
`a ∈ 𝒜`. The index set of X-check detectors is therefore the interval `1 ≤ r ≤ R−1`, of size
`R−1` per X-check (and empty at `R = 1`). The sibling document's Definition 2.7 states the range
correctly; this document does not.

**After.** Definition 1.6's sentence should read:

> In addition the Z-memory carries X-check detectors `D_{a,r} = m_{a,r} + m_{a,r−1}` for
> `1 ≤ r ≤ R−1` (there is no `D_{a,0}` — the round-0 X outcome is random — and no `D_{a,R}`,
> because the terminal readout is in the Z basis and supplies no `m_{a,R}`). The X-check detector
> set is thus `𝒜 × {1,…,R−1}`, empty when `R = 1`.

The same bound must be carried into the last line of §2.2 Step 3, which currently concludes
"`D_{a,r} = 0` for `r ≥ 1`"; read "`for 1 ≤ r ≤ R−1`". The determinism argument itself is
unaffected — it shows `m_{a,r} = m_{a,0}` for every recorded `r`, and the recorded `r` run to `R−1`.

**Nothing downstream used the unbounded form.** Checked exhaustively: the string `D_{a` occurs in
the document at four places only — Definition 1.6 (line 151), §2.2 Step 2's parenthetical
"(Dually `D_{a,r}` fails via `X_{anc(b)}` versus `|0⟩`.)" (line 354), and §2.2 Step 3's lines 366
and 368. All four are qualitative statements about determinism, insensitive to the upper index.
Every argument of §§4–5 works exclusively with the **Z-check** detector set `ℬ × {0,…,R}`, which
CONJECTURED 1.9 (sector decoupling) licenses; `∂` in (∂) has codomain `F₂^{ℬ × {0,…,R}}` throughout.
The defect is therefore harmless in this document but is the kind of index slip that matters if
Definition 1.6 is reused, which is why it is corrected here.

**Verification** (NUMERICAL, §6 block `[A3c]`): the recorded X outcomes are `m_{a,r}`,
`r ∈ {0,…,R−1}`; `D_{a,r} = m_{a,r} + m_{a,r−1}` requires both indices to be recorded, giving
`R−1` X-check detectors per check at `R = 1,2,3,4`, namely `0, 1, 2, 3`. The unbounded reading
"`r ≥ 1`" names detectors that do not exist for every `r ≥ R`.

---

## 5. Repair A4 — the repair monomials never ask for a non-existent measurement

Review edit 6 records a fact that is true but unstated. Added to §5.2, after the construction of
`D = A_0 + xC`:

> **Remark 5.3bis.** The classical flips added by 5.3′ all lie in existing rounds. Write
> `[r_min, r_max]` for the round range of the certificate. `B = Σ_i s_i x^{r_i}` has
> `ε(B) := Σ_i s_i = ∂_eff γ = 0`, so `C = B/(1+x)` has support in `[r_min, r_max − 1]` and `xC` in
> `[r_min + 1, r_max]`; `A_0` has support in `[r_min, r_max]`. Hence
> `supp(D) ⊆ ℬ × [r_min, r_max] ⊆ ℬ × [0, R−1]`, and in particular no flip of the virtual terminal
> outcome `m_{b,R}` is ever required. The construction is realisable in `C_R(M)` exactly when
> `R > r_max`, which is the hypothesis already stated in 5.3.

Status: **applied** (a one-paragraph addition; the algebra is the definition of `C` and the
vanishing of `ε(B)`, both already in Definition 5.2). Not separately verified numerically.

---

## 6. NUMERICAL — code and outputs

Python 3.9, standard library only. Exact over `F₂`; subsets of `[n]` are integer bit-masks. No
`stim`, no imported base layer: `Code`, syndromes, residual inventories and the gross-code
construction are re-implemented in this file from the definitions of §1 of the amended document.
Blocks `[A1]`, `[A2]`, `[A3a]`, `[A3b]`, `[A3c]` correspond to §§2.8, 3.3, 4.1, 4.2, 4.3.

```python
def rref(rows, ncols):
    out = [r for r in rows if r]; piv = []; r = 0
    for c in range(ncols):
        bit = 1 << c; sel = None
        for i in range(r, len(out)):
            if out[i] & bit: sel = i; break
        if sel is None: continue
        out[r], out[sel] = out[sel], out[r]
        for i in range(len(out)):
            if i != r and (out[i] & bit): out[i] ^= out[r]
        piv.append(c); r += 1
    return out[:r], piv

def reduce_vec(v, R, piv):
    for i, p in enumerate(piv):
        if (v >> p) & 1: v ^= R[i]
    return v

def pc(x): return bin(x).count('1')
def mask(s): return sum(1 << q for q in s)

class CSS:
    """A CSS code from explicit check supports; S_X membership by RREF, C_X by syndrome."""
    def __init__(self, HXs, HZs, n):
        self.n = n; self.HXs, self.HZs = HXs, HZs
        self.HX = [mask(s) for s in HXs]; self.HZ = [mask(s) for s in HZs]
        for a in HXs:
            for b in HZs:
                assert len(set(a) & set(b)) % 2 == 0, "not CSS"
        self.RX, self.pX = rref(self.HX, n)
    def synZ(self, v): return tuple(pc(v & h) % 2 for h in self.HZ)      # s(E)
    def inCX(self, v): return all(x == 0 for x in self.synZ(v))
    def inSX(self, v): return reduce_vec(v, self.RX, self.pX) == 0
    def inLX(self, v): return self.inCX(v) and not self.inSX(v)

STEANE_CHK = [[3,4,5,6],[1,2,5,6],[0,2,4,6]]
STEANE = CSS(STEANE_CHK, STEANE_CHK, 7)

# ---- [A1] four residuals at one location; the collision algebra -----------------
ZL = mask(range(7))                      # Steane logical Z support
def lam(E): return pc(E & ZL) % 2
a   = STEANE_CHK[0]                                   # CNOT order (3,4,5,6)
Sfx = [mask(a[j:]) for j in range(len(a)+1)]          # S_0 = supp(a), ..., S_4 = ∅
bad = 0
for j in range(1, len(a)+1):
    Sj, qj, Sjm1 = Sfx[j], mask([a[j-1]]), Sfx[j-1]
    ok  = (Sj & qj == 0) and (Sj | qj == Sjm1)                        # S_j ⊔ {q_j} = S_{j-1}
    ok &= tuple(x ^ y for x, y in zip(STEANE.synZ(Sj), STEANE.synZ(qj))) == STEANE.synZ(Sjm1)
    ok &= (lam(Sj) ^ lam(qj)) == lam(Sjm1)
    bad += (not ok)
# -> at the gate a->q_2 the four available residuals are ∅, {5,6}, {4}, {4,5,6}
# -> failures = 0/4

# ---- [A2] Steane non-interleaved: d_eff = 2 -------------------------------------
from itertools import combinations
E_classes = set()
for c in STEANE_CHK:
    for j in range(len(c)): E_classes.add(mask(c[j:]))      # suffixes S_0..S_{w-1}
for q in range(7): E_classes.add(1 << q)                    # singletons
E_classes = sorted(E_classes)                               # 15 classes
def xorsum(g):
    v = 0
    for E in g: v ^= E
    return v
found = None
for w in (1, 2, 3):
    for g in combinations(E_classes, w):
        if STEANE.inLX(xorsum(g)): found = (w, g); break
    if found: break
# -> w = 2, γ = {{0}, {5,6}} ; d_eff = 2 < 3 = d ; non-interleaved ⇒ d_R = 2 ∀R ⇒ R_sat = ∞

# ---- [A3a] gross code ------------------------------------------------------------
L, M = 12, 6
def idxL(i, j): return (i % L) * M + (j % M)
def idxR(i, j): return 72 + (i % L) * M + (j % M)
A_mono = [(3,0),(0,1),(0,2)]          # A = x^3 + y + y^2
B_mono = [(0,3),(1,0),(2,0)]          # B = y^3 + x + x^2
gxs, gzs = [], []
for i in range(L):
    for j in range(M):
        gxs.append([idxL(i+di, j+dj) for (di,dj) in A_mono] +
                   [idxR(i+di, j+dj) for (di,dj) in B_mono])
        gzs.append([idxL(i-di, j-dj) for (di,dj) in B_mono] +      # H_Z = [B^T | A^T]
                   [idxR(i-di, j-dj) for (di,dj) in A_mono])
GROSS = CSS(gxs, gzs, 144)
ov = {}
for ax in gxs:
    for bz in gzs:
        t = len(set(ax) & set(bz)); ov[t] = ov.get(t, 0) + 1
sup = gxs[0]; hist = {}; full = None
for r in range(1, 1 << 6):
    S = mask([sup[t] for t in range(6) if r >> t & 1])
    wgt = sum(pc(S & h) % 2 for h in GROSS.HZ)
    if r == (1 << 6) - 1: full = wgt
    else: hist[wgt] = hist.get(wgt, 0) + 1
# -> overlap histogram {0: 4536, 2: 648}
# -> |s| over the 62 PROPER subsets {3:12, 4:18, 5:18, 6:12, 9:2}; |s(supp(a))| = 0

# ---- [A3b] Theorem 3.2, exhaustive at the abstract level -------------------------
from itertools import product
for m in (0, 2, 4, 6, 8):
    wmc = wo = 0
    for chi in product((0, 1), repeat=m):                 # chi(q) = [t(q->b) > t(a->q)]
        mc = (sum(1 for c in chi if c == 0) % 2 == 0)     # (MC): #{chi = 0} even
        for k in range(m + 1):                            # |S ∩ overlap| = k, a suffix
            sub = chi[m - k:] if k > 0 else ()
            if (sum(sub) % 2 == 1) and (k % 2 == 0):      # u_b = 1 and s_b = 0
                wmc += mc; wo += (not mc)
    print(m, wmc, wo)
# -> 0 0 0 / 2 0 2 / 4 4 12 / 6 32 64 / 8 192 320
```

**Measurement log.**

```
[A1] S_j ⊔ {q_j} = S_{j−1}; s and λ additive                 : 0 failures / 4 gates
[A1] distinct residuals at one location                      : 4 at the gate a→q_2  (refutes 5.3)
[A2] Steane non-interleaved residual classes                 : 15
[A2] minimum-weight effective logical                        : |γ| = 2 = d_eff < 3 = d
[A2] ⇒ R_sat                                                 : ∞   (counterexample to §5.10(1))
[A3a] gross overlap histogram                                : {0: 4536, 2: 648}     (matches)
[A3a] gross |s| over 62 proper subsets                       : {3:12,4:18,5:18,6:12,9:2} (matches)
[A3a] gross |s| for S = supp(a)                              : 0   (counterexample to §8 3(ii))
[A3b] per-pair vertical count under (MC), m = 0,2,4,6,8      : 0, 0, 4, 32, 192
[A3b] same without (MC)                                      : 0, 2, 12, 64, 320
[A3c] X-check detectors per check at R = 1,2,3,4             : 0, 1, 2, 3   (= R−1, not unbounded)
```

**Independence caveat.** These are my own re-implementations, written this session, but the *model
design* (which locations exist, which residual classes arise) is inherited from Definitions 1.8 and
1.13 of the amended document. A systematic modelling error against `stim`'s conventions would
survive these checks. `stim` was not used.

---

## 7. What this amendment does **not** fix

Stated so that no reader mistakes the scope of the repairs.

1. **The `repair ≥ 3` gap (§7.2) is untouched.** 5.6(c)/(d) remain conditional on
   `repair ≤ 2`, and 5.6bis's pair gadget still shows the plain-count form of `ℓ(γ)` should not be
   expected in general. The review declares this NOT-REVIEWED and I have not narrowed it.
2. **Nothing is proved.** The label ceiling of the original stands. In particular Lemma 5.3′ and the
   corrected 5.10(1′) are CONJECTURED and have had **no** independent review — they are the
   proposer's response to one reviewer, not a second reviewed result.
3. **`ℓ(γ)` for a fixed non-minimal `γ` is now weaker than the original claimed** (§2.6). I have
   *not* proved that collisions never occur for such `γ`; the review's search found zero *forced*
   collisions in 180 schedules but non-forced collisions in all 180, which is evidence, not a proof.
   Anyone who needs `ℓ(γ) = |γ| + repair(γ)` for a specific `γ` must check the distinct-location
   proviso for that `γ`.
4. **The imported Lemma 7.2 is imported.** Its proof lives in the sibling document and is
   reproduced here only in statement. I checked its algebra on Steane (§2.8) but did not
   re-derive its case enumeration, which rests on the sibling's Lemma 5.4 and is non-interleaved-only.
5. **`d_∞(M)` is not computed anywhere.** 5.10(1′) says `R_sat` is decided by `R = 1,…,d`; it does
   not give a formula for `d_∞`. For the non-interleaved class the sibling's Corollary 7.3 does
   (`d_∞ = d_eff`); for the interleaved class this is exactly the open content of Theorem 2.
6. **Review items I did not act on because they are not defects.** Review §5's five "residual
   concerns" (the `repair ≥ 3` regime, the shared-model-design caveat, `k > 1`, 5.10(3)'s own status
   line, and the exactly-equal `321 059 / 321 059` symmetry in NUMERICAL 3.6) are left as the review
   leaves them. The last of these in particular remains **NOT-REVIEWED**: neither the reviewer nor I
   reproduced that scan, and the exact equality of the two horizontal counts is unexplained.
7. **§8 item 5(b)'s scope observation is not revisited.** The claim that the campaign's `d = 3`
   Steane witness is not graph-like stands unamended; the review confirms it independently.
8. **No proof-DAG object was created or modified**, and no route was repriced. The `CIRCDIST.sat`
   consequences of §3 are stated here only; propagating them into the node record is a separate act
   that this session did not perform.
