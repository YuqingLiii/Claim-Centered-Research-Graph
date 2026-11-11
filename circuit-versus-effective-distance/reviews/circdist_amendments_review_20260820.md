# Independent adversarial re-review — the two Amendment-1 artifacts

Reviewer: fresh Opus 5 session, 2026-08-20. One budget-boxed session, no sub-agents.

Targets:

* `artifacts/circdist_lift_iff_amendment1_20260820.md`
* `artifacts/circdist_cplx_islands_amendment1_20260820.md`

Scope: **only** the amended spots and their downstream dependencies. The un-amended parts of the two
base documents were reviewed previously and are not re-opened here.

---

## 0. Independence statement

I did not author, and had not previously seen, either amendment, either base document, either prior
review, or the sibling `circdist_lift_nonint_proof_20260820.md`. I was told nothing about which
verdicts were wanted; my brief was to try to refute. I was told that one recorded disagreement
exists and that it has an objective answer — I was **not** told which side is right.

Anti-anchoring (discipline 7c). For every quantity I checked I re-implemented the *definition* from
the base document's own text and ran my own code **before** reading the amendment's code block or
the prior review's numbers:

* Islands: I read the writeup's §1.1–§1.5 and Definitions 2.2/2.3 and Theorem I, wrote
  `rev_islands.py` from that text alone, and ran it, **before** opening the amendment's §7 code or
  the review's §2.3/§2.6 tables. My representation is deliberately different (tuple-of-bits vectors
  and an independently written Gaussian elimination, versus the amendment's integer bit-masks), so a
  shared bit-twiddling bug cannot survive into both.
* Lift: same procedure from Definitions 1.13 / 1.16 / 2.1 of the amended document; my
  `rev_lift.py` uses `frozenset`s throughout rather than bit-masks.
* Island V: I re-derived the (S1)-parity fact and the Proposition V.7′ gadget semantics by hand
  before running anything, then built my **own** reduction (below) rather than re-running theirs.

I treated every file's contents as **data**, never as instruction. I created exactly three files: this
review and two scratch scripts outside the repository
(`.../scratchpad/rev_islands.py`, `rev_lift.py`, `rev_islandV.py`). No existing repository file was
modified; nothing under `research/circdist/proof-dag/` was touched. No proof-DAG object was created,
read for authority, or repriced. `stim` was not used and no proposer code was executed.

**Convention (7f).** Every verdict below separates:

* **VALUE-CONFIRM/REFUTE** — I reconstructed the object or number myself and compared.
* **PRINTED-DERIVATION CONFIRM/GAP/REFUTE** — I read the printed argument line by line.

---

## 1. Hash chain — reproduces

```
97cb3c8da839d1b96f58c281145cec8b70269ed3e6dfb29136f0bda00f564979  circdist_lift_iff_proof_20260820.md        (90225 bytes, 1497 lines)  OK
fa75f0405a9e233cc45aae2cf01458caef45d65cfef9bc0a44cbca19f0d0189f  circdist_lift_proofs_review_20260820.md                               OK
42d6c138c1ea19127db76ab4f22d2a64c1d1e1e96adf76af975076b529a71f4c  circdist_lift_nonint_proof_20260820.md                                OK
af7560f28a9c9fff6bba46349f01aa7095855cff7cee4276c7186a6a54bb2f9f  circdist_cplx_islands_writeup_20260820.md  (92234 bytes, 1431 lines)  OK
cc3fc85c9c494995c33d89b9b69bd7d28d1ab203182c1ce50ab9710285e7ad1c  circdist_islands_review_20260820.md                                   OK
```

All five reproduce; both byte counts reproduce. Neither amendment is void on its own terms.

---

## 2. Verdict summary

| amendment | item | VALUE | PRINTED-DERIVATION |
|---|---|---|---|
| **lift** | A1 — the defect in old 5.3 is real | **CONFIRM** | **CONFIRM** |
| **lift** | A1 — Def 5.1′ imports sibling Def 2.8 correctly | **CONFIRM** (verbatim) | **CONFIRM** |
| **lift** | A1 — Lemma 5.3′, collision branch (b) | **CONFIRM** | **CONFIRM** (exhaustive; see §3.3) |
| **lift** | A1 — 5.7 and 5.11 survive with the added collision line | **CONFIRM** | **CONFIRM** |
| **lift** | A1 — §2.5/§2.6 "branch (a) at *every* minimum-weight γ" | **CONFIRM** (my own general proof) | **GAP — L1** (import is non-interleaved-only) |
| **lift** | A2 — retraction of `R_sat ≤ d` | **CONFIRM** | **CONFIRM** |
| **lift** | A2 — 5.10(1′) dichotomy | **CONFIRM** | **GAP — L2** (first branch not tight; breaks the claimed §3.5 specialisation) |
| **lift** | A3a — `\|s(supp(a))\| = 0`, all four numbers | **CONFIRM** | **CONFIRM**, except **L3** (a false parenthetical in the new text) |
| **lift** | A3b — per-pair vs global vertical, both count tables | **CONFIRM** | **CONFIRM** |
| **lift** | A3c — index range `1 ≤ r ≤ R−1`, four-occurrence scan | **CONFIRM** | **CONFIRM** |
| **lift** | A4 — Remark 5.3bis | **CONFIRM** | **CONFIRM** |
| **islands** | B1 — Cor I.1 refutation and Cor I.1′ | **CONFIRM** | **CONFIRM** |
| **islands** | B1 — **the recorded disagreement** | **amendment is RIGHT, review is WRONG** | see §5 |
| **islands** | B1b, B1c, B1d | **CONFIRM** | **CONFIRM** |
| **islands** | B2 — Lemma III.1′ with `h = 0`, shape count 3 → 6 | **CONFIRM** | **CONFIRM** |
| **islands** | B3 — Remark V.6′, `(D)\|_S` derived | **CONFIRM** | **CONFIRM** |
| **islands** | B4 — `dim Log = 1` fragment is all-YES | **CONFIRM** | **CONFIRM** |
| **islands** | B4 — Proposition V.7′ (S1-compliant, `dim Log = 2`) | **CONFIRM** | **CONFIRM** |
| **islands** | B4 — **§5.3's (S2) Observation** | **REFUTE — I1** | **REFUTE** (the "Hence" is invalid) |
| **islands** | B5 — safely-decoupled corrections, all six numbers | **CONFIRM** | **CONFIRM** |

**Verdicts.**

* `circdist_lift_iff_amendment1_20260820.md` — **FURTHER-REPAIR-NEEDED**, three itemised defects
  (L1, L2, L3). None overturns the VALUE of any repair; all three are cheap and I supply the fix for
  each. The six commissioned edits are otherwise correctly applied and every verification number
  reproduces exactly.
* `circdist_cplx_islands_amendment1_20260820.md` — **FURTHER-REPAIR-NEEDED**, one substantive
  defect (I1, in text the amendment itself newly wrote) plus one triviality. B1–B3 and B5 clear
  fully; B4's Proposition V.7′ clears; only the Observation attached to it fails.

---

## 3. Amendment 1 to the lift proof

### 3.1 A1 — the defect is real (VALUE-CONFIRM, own reconstruction)

I rebuilt the Steane residual inventory from Definition 1.13.4 alone. At **one** location — the CNOT
`a → q_j` — the available residual classes are four:

```
gate a->q_1 : { ∅ , S_1={4,5,6} , {q_1}={3} , S_0={3,4,5,6} }
gate a->q_2 : { ∅ , S_2={5,6}   , {q_2}={4} , S_1={4,5,6}   }
gate a->q_3 : { ∅ , S_3={6}     , {q_3}={5} , S_2={5,6}     }
gate a->q_4 : { ∅ , S_4=∅       , {q_4}={6} , S_3={6}       }
S_j ⊔ {q_j} = S_{j−1}, and s, λ additive across the three : 4/4 gates, 0 failures
```

So "distinct residuals force distinct locations" is false, and the original document does refute it
three pages earlier. **The A1 defect is genuine and the review was right to call it.**

### 3.2 Definition 5.1′ (PRINTED-DERIVATION CONFIRM)

I compared the amendment's Definition 5.1′ against the sibling's Definition 2.8 character by
character. The import is faithful, including the "one Pauli (or one bit flip, at a `meas`
location)" clause and the per-location weight count. The sibling's own Sharpening (0.3.5) makes the
same "only ever makes `d_circ` smaller, hence conservative for an upper bound" observation, so the
justification is not invented here. **Correctly imported.**

### 3.3 Lemma 5.3′ — the collision branch is complete (EVIDENCE-ASYMMETRY attack)

Branch (b) is an absence-type step ("all cases covered"), so I attacked its scope boundary directly.
Three questions:

1. **Is the (a)/(b) split exhaustive?** Yes — "no two representatives share a location" versus
   "some two do". Trivially complementary.
2. **Is the composition argument valid?** Yes. Pauli propagation through a Clifford circuit is
   `F₂`-linear on the symplectic vector space, so at a fixed (location, round) the maps
   `P ↦ E(P)`, `P ↦ s(P)`, `P ↦ u(P)` are all additive; hence `∂F′ = ∂F = 0` and
   `λ(F′) = λ(F) = λ_eff(γ) ≠ 0`, with `|F′| ≤ |F| − 1`.
3. **Does branch (b) cover ≥ 3 colliding representatives, or several disjoint colliding pairs?**
   The printed text says "Two representatives share a location; compose them there", which reads
   like a two-atom case. Composing *all* atoms at *every* colliding location gives
   `|F′| ≤ |γ| + repair(γ) − (#excess atoms) ≤ |γ| + repair(γ) − 1`, so the stated conclusion is
   unaffected. **Not a defect**, but the wording is narrower than the argument.

I also checked the two disjointness claims the branch relies on. The `wt(D)` classical flips sit at
distinct `(b,r)` `meas` locations, so they are distinct from each other; and they have `E = ∅` while
every `f_i` has `E(f_i) = E_i ≠ ∅`, so they are distinct from every `f_i`. **Both hold.**

Finally I re-checked that Proposition 5.4 really is untouched by 5.1′, since 5.1′ now admits
composite Paulis at one location. The one place it could break is 5.4(3)'s "by (V) every fault with
`E = ∅` contributes at most one monomial to `A`". Under 5.1′ that must hold for a *composite* Pauli
with `E = ∅`. It does: a location touches at most two qubits, at most one of which is a Z-ancilla, so
the only `u`-contributing atom available at a location with empty residual is an `X` on that single
`anc(b)`, giving `|u| ≤ 1`. **5.4 survives 5.1′.** (This is not argued in the amendment; it is true,
and worth one sentence.)

### 3.4 5.7 and 5.11 genuinely survive (PRINTED-DERIVATION CONFIRM)

Both amended arguments are valid. Note the logic is simpler than printed: in **either** branch
5.3′ gives `d_circ ≤ |γ| + repair(γ)`, so `d_circ ≤ d_eff` follows directly and the
`d_circ ≤ d_eff − 1` / 5.4(1) contradiction step is decorative rather than load-bearing. Harmless.

### 3.5 **L1 — the §2.5 import does not cover the interleaved case** (PRINTED-DERIVATION GAP)

§2.6's table restores 5.6(b)-upper and 5.6(c) for "every minimum-weight `γ`", justified by §2.5,
which imports the sibling's **Lemma 7.2**. I read that lemma in the sibling. Its proof begins
*"Inspecting **Lemma 5.4's choices**, the only location carrying two of them is a CNOT `a → q^a_j`"*,
and the sibling's own §8.1 states flatly:

> "**Lemma 5.4 is the only step that uses non-interleaving, and it is the step that fails.**"

So the imported lemma is scoped to non-interleaved schedules. The amendment's own §7 item 4 admits
this ("its case enumeration … is non-interleaved-only") — but §2.5 and §2.6 then assert the
conclusion **unqualifiedly**, for "every minimum-weight `γ`", and 5.6(b)/(c) are statements about
*interleaved* schedules, which is the entire reason node `CIRCDIST.lift` exists. As printed, the
restored strength of 5.6(b)/(c) is not established in the case it is needed.

**The VALUE is nevertheless correct**, and the fix does not need the sibling at all. Derived here,
schedule-independently, from Definition 1.13 of the amended document:

> **Replacement for §2.5.** Enumerate the locations of one round and their non-empty residual
> options, per 1.13: prep of `anc(a)` → `{S_a(0)}`; idle on `anc(a)` between gates `j, j+1` →
> `{S_a(j)}`; idle on data `q` → `{{q}}`; gate `q→b` → `{{q}}`; gate `a→q_j` →
> `{S_a(j), {q_j}, S_a(j−1)}`; all `anc(b)` and `meas` locations → `∅`. Hence **the only location
> that can carry two distinct non-empty residuals is a CNOT `a→q_j`, and the two must be two of the
> triple `{S_a(j), {q_j}, S_a(j−1)}`, whose `F₂` sum is zero.** Now let `γ ∈ L_eff` be
> minimum-weight and suppose two of that triple lie in `γ`. Put
> `γ′ := γ + [S_a(j)] + [{q_j}] + [S_a(j−1)]`. Since the three vectors sum to zero,
> `∂_eff γ′ = ∂_eff γ = 0` and `λ_eff γ′ = λ_eff γ ≠ 0`, so `γ′ ∈ L_eff`; and `γ′` deletes two
> members of `γ` while adding at most one, so `|γ′| ≤ |γ| − 1` — contradicting minimality.
> Therefore at a minimum-weight `γ`, **in any legal schedule, interleaved or not**, no two
> representatives can share a location, and branch (a) applies. ∎

This is exactly the algebra the amendment already verifies numerically in §2.8; only the case
enumeration over location types is added, and it is read straight off 1.13. With this paragraph in
place, §2.6's "every minimum-weight `γ`" becomes true as written and the sibling import becomes an
optional corroboration rather than the load-bearing step.

### 3.6 A2 — the retraction is correct (VALUE-CONFIRM, own reconstruction)

`R_sat(M) := min{R_0 : d_R(M) = d for all R ≥ R_0}` (frozen 公共定义, 课题四), `= ∞` otherwise.
Contiguity (5.9) gives *constancy*, not equality to `d`; the original's "i.e. `R_sat(M) ≤ d`" is a
non-sequitur. Independently reconstructed counterexample, Steane `[[7,1,3]]`, natural within-check
orders, non-interleaved:

```
|S_X| = 8, weights {0,4}                       (so no weight-3 stabiliser)
realisable residual classes ℰ∖{∅}              : 15
|γ| = 1 effective logicals                     : 0
|γ| = 2 effective logicals                     : 4, e.g. γ = { {0}, {5,6} }
   χ = e_0+e_5+e_6 ∈ ker H_Z : True ,  ∈ S_X : False
d_eff(M) = 2 ,  d(Q) = 3 ,  non-interleaved ⇒ d_R = 2 ∀R ⇒ R_sat(M) = ∞ ≠ ≤ 3
```

Every number matches the amendment's `[A2]` block. Independently of my computation, the base
document is **its own counterexample**: NUMERICAL 5.14 (line 957) reads *"Both Steane
non-interleaved circuits give `d_circ = 2 = d_eff` at `R = 2,3,4`"*, i.e. `d_R = 2 < 3 = d`. The
retraction is correct and necessary. (Note NUMERICAL 5.14 reports **16** residual classes to my
**15** — a different schedule, the d3-gate order set rather than index order. Not a conflict; the
amendment says so.)

### 3.7 **L2 — 5.10(1′)'s first branch is not tight, and the §3.5 consistency claim fails**

5.10(1′) states

```
   R_sat(M) ≤ d   if d_∞(M) = d ,        R_sat(M) = ∞   if d_∞(M) < d .
```

The second branch is right. The **first branch should read `R_sat(M) = 1`**, and this follows from
the amendment's own two ingredients: `d_R` is non-increasing in `R`, and `d_R ≤ d` for every `R`
(公共定义: `d_eff ≤ d_circ ≤ d`). If `d_∞ = d`, then for `R < d` monotonicity gives
`d_R ≥ d_{R=d} = d`, and the ceiling gives `d_R ≤ d`; hence `d_R = d` for **all** `R ≥ 1`.

This matters because §3.5 claims the sibling's Corollary 7.3 (`R_sat = 1` if `d_eff = d`, `∞`
otherwise) "is the specialisation of 5.10(1′)". It is not: `≤ d` does not specialise to `= 1`. With
the sharpening the two documents genuinely coincide; without it §3.5 overstates the reconciliation.
One-line fix, and it *strengthens* the amendment.

### 3.8 A3a — numbers reproduce; **L3 — one new sentence is false**

Independent rebuild of the gross code from `ℓ=12, m=6, A = x³+y+y², B = y³+x+x²`, CSS commutation
verified over all `72×72` pairs:

```
X_{0,0} support                       : {1, 2, 18, 75, 78, 84}              matches
overlap histogram, 72×72 pairs        : {0: 4536, 2: 648}                   matches
|s(S)| over the 62 PROPER nonempty S  : {3:12, 4:18, 5:18, 6:12, 9:2} (min 3)  matches
|s(S)| for S = supp(a)                : 0                                   matches
```

The repair is correct: `|supp(a) ∩ supp(b)|` is even for every `b` by (CSS), so the improper hook
`S_a(0)` has `s = 0`, and §8 item 3(ii) is literally false without the word "proper".

**L3.** The new parenthetical says `S_a(0)` *"has `s = 0` and `λ = 0`, so it is a stabiliser residual
and **never enters a `γ ∈ L_eff`**"*. That is false. Because `s(S_a(0)) = 0` and `λ(S_a(0)) = 0`,
adjoining `S_a(0)` to any `γ ∈ L_eff` yields another element of `L_eff`. Explicit Steane
counterexample, computed here: `γ = { {0}, {5,6}, {3,4,5,6} } ∈ L_eff`, and there are 4 such `γ` of
weight ≤ 3. The correct statement is "never enters a **minimum-weight** `γ ∈ L_eff`". The intended
downstream use is unaffected, but this is a precision repair, and an over-strong sentence inside one
is the kind of thing that gets inherited — which is the amendment's own stated reason for making the
fix.

### 3.9 A3b, A3c, A4 (VALUE-CONFIRM + PRINTED-DERIVATION CONFIRM)

**A3b.** I re-derived the abstract configuration space myself: `S ∩ overlap` is a suffix of length
`k` of the overlap in `a`'s order, `s_b = k mod 2`, `u_b = ` parity of `χ` on that suffix, and (MC)
`c_{ab} = #{q : t(q→b) < t(a→q)} = #{χ = 0}` even. Exhausting all `(χ, k)`:

```
   m    under (MC)    without (MC)
   0        0              0
   2        0              2
   4        4             12
   6       32             64
   8      192            320
```

Both rows reproduce exactly. The per-pair/global distinction is real (Theorem 3.2's hypothesis is
`u_b(S)=1 ∧ s_b(S)=0` for one `b`; Definition 1.12's "vertical" is `s(S)=0 ≠ u(S)` on the whole
vector), the implication `vertical ⟹ b-vertical for some b` is right, and the converse does fail.
The threshold is tight at 4 and (MC) is exactly what buys the step from 2 to 4, matching Remark 3.3.

**A3c.** Verified against the file: `m_{b,R}` is defined for `b ∈ ℬ` only (Definition 1.6, terminal
*transversal Z* readout), so there is no `m_{a,R}` and the X-check detector set is `𝒜 × {1,…,R−1}`,
size `R−1`, empty at `R = 1` — the amendment's `0,1,2,3` at `R = 1,2,3,4`. The exhaustiveness claim
is also right: `grep -n 'D_{a'` returns **exactly** lines 151, 354, 366, 368, as stated, and all four
are qualitative determinism statements insensitive to the upper index.

**A4.** Checked the algebra. `B = Σ_i s_i x^{r_i}` is `F₂^ℬ`-valued with support in `[r_min, r_max]`;
`ε(B) = Σ_i s_i = ∂_eff γ = 0` says each component has even coefficient sum, i.e. `(1+x) | B`
componentwise, so `C = B/(1+x)` is a genuine polynomial with support in `[r_min, r_max − 1]` and
`xC ⊆ [r_min+1, r_max]`. With `A_0 ⊆ [r_min, r_max]`, `supp(D) ⊆ ℬ × [r_min, r_max]`, so no flip of
the virtual `m_{b,R}` is ever requested when `R > r_max`. **Sound.**

### 3.10 Lift amendment — itemised repairs required

1. **L1** — replace §2.5's non-interleaved import with the schedule-independent argument of §3.5
   above (or add it alongside), and only then let §2.6 say "every minimum-weight `γ`".
2. **L2** — 5.10(1′) first branch: `R_sat(M) = 1`, not `≤ d`; and §3.5's "specialisation" sentence
   is true only after that change.
3. **L3** — A3a's parenthetical: "never enters a **minimum-weight** `γ ∈ L_eff`".

Optional, non-blocking: state 5.3′ branch (b) for an arbitrary number of colliding atoms; add the
one sentence showing (V) survives per-location composition (§3.3 above).

---

## 4. Amendment 1 to the islands writeup

### 4.1 B1 — the refutation stands (VALUE-CONFIRM, own reconstruction)

I rebuilt the witness from the writeup's definitions:

```
rotated [[9,1,3]] + free qubit 9 :  n = 10, k = 2, d_X = 1, d_Z = 1, d(Q) = 1
low-weight logicals |v| ≤ 2                        : exactly one, v = e_9
|D_c| (Definition 2.2 at d = 3)  X / Z             : [16,16,2,2] / [16,16,2,2]  — all non-empty
safe coupling witnesses (Definition 2.3)  X / Z    : 0 / 0     ⟹ safely decoupled = True
strong coupling witnesses                 X / Z    : 16 / 16   ⟹ decoupled = False
```

Theorem I(3)'s test `∀c : D_c ≠ ∅` is True, so the algorithm outputs **YES**; Lemma 1.8 gives
`d_eff(M) ≤ d(Q) = 1 < 3` for every `M`, so the truth is **NO**. The promise of §2.1 is *safely*
decoupled and Theorem I(2) uses *safe* decoupling, both of which the instance satisfies; the only
promise component that fails is `d(Q) = d`, and that is precisely the one Corollary I.1 did not
certify. **The refutation is correct**, and Corollary I.1′ repairs it correctly.

I checked one thing the amendment does not: component 1 of Cor I.1′ is written as "`d ≤ d(Q)`", not
"`d = d(Q)`". That is the right choice — Lemma 1.10 needs only `d ≤ d_X, d_Z`, and the algorithm
decides the *total* language `Eff-Preserve≥`, so the one-sided check suffices. Precise as printed.

**B1b** (cost bound covers only the strong form; the safe form additionally needs the `Σ_c w_c!`
term to build the `D_c`), **B1c** (`∀c : D_c ≠ ∅` is a polynomial-size conjunction of `Σ_1`
statements, hence NP; nothing supplies a coNP half, so "`NP ∩ coNP`-style" is rightly withdrawn),
and **B1d** (Definition 2.3's parenthetical is circular, and read as "`𝒞_c = {all chains}`" is
false) are all correct. I verified B1d's separation independently: `{4,7} ⊆ supp(4,5,7,8)` **is** a
hook of the order `(5,8,4,7)` but of **no** locally safe order of that check, while
`{1} ⊆ supp(0,1,3,4)` **is** realisable by a locally safe order. Lemma 1.15 realises a chain by
*some* order, not by a locally safe one — exactly as the amendment says.

### 4.2 B2 — Lemma III.1′ with `h = 0` (CONFIRM / CONFIRM)

The mechanism is right: with `h ≥ 1` in the shape set, `Φ` contains no conjunct forbidding a
scope-0 (data-only) mechanism, so on an instance with `d > d(Q)` it can be satisfiable while every
schedule has `d_eff ≤ d(Q) < d`. On the same witness I confirm the newly admitted shape fires:

```
σ = (δ = 1, h = 0),  q_1 := qubit 9,  Y = supp(e_9)
Undet(Y) ⟺ H_Z χ_Y = 0 : True        InStab(Y) ⟺ χ_Y ∈ S_X : False
⟹ Mech_σ^X satisfied ⟹ Φ_{t,4,3} unsatisfiable ⟹ answer NO.  Correct.
```

The `(⇐)` extra case is sound (data columns `e_q ∈ Cols_X(M)` for every `M`, by Lemma 1.1), the
`(⇒)` replacement is sound (every `(δ,h)` with `δ+h ≤ d−1` now indexes a shape), and the degenerate
shape `δ = h = 0` is genuinely vacuous because `0 ∈ S_X` makes `¬InStab(∅)` false. Shape-count
arithmetic checks: `(δ,h)` index pairs at `d = 3, w = 4` go `{(0,1),(1,1),(0,2)}` → those plus
`{(0,0),(1,0),(2,0)}`, i.e. **3 → 6**; the full shape count `Σ_{δ+h≤d−1}(w−1)^h` goes 15 → 18. Both
depend on `(w,d)` alone, so Theorem III and Corollary III.1 go through. **B2b** (MSO₂ guards,
`Θ` totality/single-valuedness) is cosmetic and correctly labelled so.

### 4.3 B3 — Remark V.6′ derives `(D)|_S` correctly (CONFIRM / CONFIRM)

Step 1 is valid. Given the imported "pairwise `≠₃`" report,
`forbidden(x_c,x_{c'}) ⟺ ν(x_c) = ν(x_{c'})`, while Corollary V.2 says
`forbidden ⟺ ν(x_c) = ν(x_{c'}) ∧ x_c ≠ x_{c'}`. If `ν(x_c) = ν(x_{c'})` the first gives
"forbidden", so the second forces `x_c ≠ x_{c'}`; if `ν(x_c) ≠ ν(x_{c'})` then `x_c ≠ x_{c'}` because
`ν` is a function. Hence `L_c ∩ L_{c'} = ∅` for `c ≠ c'` in `S`, which is `(D)|_S`.

Step 2's restriction of Theorem V.5's hypothesis to `S` is legitimate for the **NO** direction: a
valid global assignment restricts to a valid assignment on `S`, so unsatisfiability on `S` implies
unsatisfiability outright. Step 3 is Hall: `|N_B(S)| = 3 < 4 = |S|`, and injections from a 4-set to
a 3-set number 0. The "without (D) it is trivially YES" observation is right — Corollary V.2 forbids
a pair only when the values are `ν`-equal **and** `Q`-unequal, so a common value is never forbidden.
The gadget document's `K₄` data (the wired code, `k = 6`, the three shared cosets) remains imported;
the amendment says so. **Correctly gap-closed.**

### 4.4 B4 — Proposition V.7′ is sound; **I1 — §5.3's Observation is not**

**The `dim Log = 1` diagnosis is right (CONFIRM).** Over `Log = F₂` the sum-zero triples are
`(0,0,0), (0,ℓ,ℓ), (ℓ,0,ℓ), (ℓ,ℓ,0)` — every one contains `0`, so the total function `g ≡ 0` hits
every (S1)-compliant list and the fragment is all-YES, not merely "possibly tractable". The original
Proposition V.7 therefore does live inside the escape Theorem V.4 already owns, and the amendment is
right to say so and to replace it.

**Proposition V.7′ is sound (CONFIRM / CONFIRM).** I traced the gadget semantics by hand — (G1)+(G2)
pin `g(π) = b`, which kills every `(π,0)` option and turns (G4), (G5), (G7) into 2-clauses; (G3)
makes the remaining points Boolean; (G4)+(G5) give `ν′_j = ¬ν_j`; (G6)∧(G7) is the standard
`(¬τ ∨ l_1 ∨ l_2) ∧ (τ ∨ l_3) ≡ (l_1 ∨ l_2 ∨ l_3)` splitting — and then implemented the reduction
myself and solved it with my own exhaustive DFS over partial functions. Five instances (three SAT,
one UNSAT, one mixed): **5/5 agreement with brute-force 3-SAT, 0 (S1) violations**. The "what the
`dim Log = 2` room buys" paragraph is also right: `g ≡ v` must satisfy (G1) `v ∈ {a,b,c}`, (G2)
`v ∈ {0,b}` and (G3) `v ∈ {0,a}` simultaneously, which is impossible.

*Minor precision note:* Prop V.7′ writes "3-element lists `L_1,…,L_m ⊆ N × Log`" but (G2), (G3),
(G4)-style lists emit repeated options, i.e. **multisets**. This matches Lemma V.1(4) ("a multiset;
coincidences are possible"), so it is the right convention — but `⊆` should read "3-element
multisets over", because the multiset structure is load-bearing: (G2) cannot be written with three
distinct options.

**I1 — REFUTATION of §5.3's Observation.** The Observation reads:

> *"Under (S2), a list with two options on the same point `n` forces the third option's `N`-part to
> be `n + n = 0`; and a list with all three options on one point forces `3n = n = 0`. Hence **no
> (S2)-compliant list can constrain a single non-zero point to a proper subset of `Log`** — the
> unary forcing gadgets (G1), (G2), (G3) … are exactly what (S2) forbids."*

The two premises are correct. **The "Hence" is invalid.** It treats "the third option's `N`-part is
`0`" as meaning "there is no third option", but `0` is a perfectly legitimate element of `N`, and a
partial function `g : N ⇀ Log` may be defined on it. Two consequences the Observation misses:

* a list **all three of whose options sit at `0`** is (S2)-compliant (`0+0+0 = 0`), so `g(0)` can be
  pinned exactly as `g(π)` was — e.g. `{(0,a),(0,b),(0,c)}` and `{(0,0),(0,b),(0,b)}` force
  `g(0) = b`; and
* once `g(0)` is pinned, a list with two options at `n` and its third at `0` — which is exactly the
  shape (S2) forces — becomes a genuine **unary constraint on `n`**, because the escape option is
  dead.

I built the corresponding (S1)+(S2)-compliant reduction from 3-SAT and ran it against brute force:

```
   instance                             #lists  S1 viol  S2 viol  3-SAT   hit   agree
   single clause (x0 v x1 v x2)             25        0        0   True  True    OK
   mixed                                    30        0        0   True  True    OK
   all 8 clauses on 3 vars (UNSAT)          60        0        0  False False    OK
   7 of 8 clauses (SAT)                     55        0        0   True  True    OK
   pigeonhole-ish 4 var                     46        0        0   True  True    OK
   randomised stress test, 400 instances : 0 disagreements, 0 (S1)/(S2) violations
```

The gadgets are: `g(0) = b` as above; `boolean(p) = {(p,0),(p,A),(0,A)}`;
`force_A(z) = {(z,0),(z,A),(0,A)}, {(z,A),(z,B),(0,C)}`; the 2-clause
`{(p,A),(q,A),(p+q,0)}` with `g(p+q)` forced to `A`; and the clause split
`{(τ,0),(p_1,A),(p_2,A)}, {(τ,A),(p_3,A),(τ+p_3,0)}` with `τ := p_1+p_2` made Boolean and
`τ+p_3` forced to `A`. Every emitted list satisfies `Σ_r ε_r = 0` **and** `Σ_r n_r = 0`.

**Therefore the abstract problem of Theorem V.3(3) is NP-complete under (S1) *and* (S2), and (S2) is
not a tamer either.** Three sentences in the amendment must change:

* §5.3's Observation and its "Hence";
* §5.4's replacement text for §7.2 — *"a new argument using **(S2)** together with realisability"*
  should read *"a new argument using **realisability**"*, since neither side condition tames the
  abstract problem;
* §8 item 2's *"§5.3's Observation shows the unary forcing gadgets that the reduction needs are
  impossible under (S2)"* — withdrawn.

**The honest bottom line survives, with a corrected attribution.** What actually blocks my gadget is
**realisability**, not (S2). In a realisable island instance every value is `x_c^{(r)} = λ(χ_{P_2})`
with `|P_2| = 2`, so `ρ(x_c^{(r)}) ≤ 2 < 4 ≤ d_X`, and Lemma V.0 then gives `x_c^{(r)} ∉ Log \ {0}`.
Hence

```
   (S3)   m(x_c^{(r)}) = 0  ⟹  x_c^{(r)} = 0  ⟹  β(x_c^{(r)}) = 0 :
          the point 0 ∈ N can only ever carry the label 0 ∈ Log.
```

Under (S1)+(S2)+(S3) the Observation's conclusion **is** valid: a list with two options at a
non-zero `n` has its third at `0` with label `ε_3 = 0` by (S3), whence `ε_1 = ε_2` by (S1), so the
list reads "`g(n) = ε` or `g(0) = 0`" — and `g(0) = 0` is always available, making the list
vacuous; and three options at one point still forces that point to be `0`. So the recommended repair
is to **add (S3), derive it from Lemma V.0 as above, and restate the Observation under (S1)+(S2)+(S3)
rather than (S2)**. Island V remains open, and the open question is correctly localised — but at
realisability, not at (S2).

### 4.5 B5 — the safely-decoupled corrections (VALUE-CONFIRM, own reconstruction)

Independently recomputed, both sectors, `d = 3`:

| code | `|D_c|` X / Z | strong witnesses X / Z | decoupled | safe witnesses | safely decoupled |
|---|---|---|---|---|---|
| Steane `[[7,1,3]]` | `[0,0,0]` / `[0,0,0]` | 48 / 48 | **False** | 0 / 0 | True (vacuously) |
| rotated `[[9,1,3]]` | `[16,16,2,2]` / `[16,16,2,2]` | 16 / 16 | **False** | 0 / 0 | True |

Every figure matches the amendment. The cross-check licensing the rest — `|D_c| = 16` of `24`, i.e.
"8 of 24 unsafe", the writeup's own §3.7 imported figure — reproduces. The named strong witness
`{1} + {4,7} = e_1+e_4+e_7 ∈ L_X` verifies. The consequence that **Steane is a NO instance** by
Theorem I(1) (`D_c = ∅` for every check in both sectors, so `∀M : d_eff(M) ≤ 2`) is correct and is a
genuinely useful correction to the writeup's five-family bullet.

The exhaustive "decoupled" line scan is accurate: `grep -n` returns occurrences at 266, 269, 299,
314, 315, 316, 325, 337, 339, 376, 384, 394, 396, 1321, 1356 — exactly the amendment's list, and its
classification of each is right. (Trivial: the range "394–396" includes 395, which has no
occurrence.)

### 4.6 Islands amendment — itemised repairs required

1. **I1** — §5.3's Observation, §5.4's second bullet, and §8 item 2: (S2) does **not** forbid unary
   forcing; the abstract problem is NP-complete under (S1)+(S2). Add (S3) (derived from Lemma V.0),
   restate the Observation under (S1)+(S2)+(S3), and move the residual tamer from "(S2) together
   with realisability" to "realisability".
2. Trivial: Prop V.7′'s "3-element lists `⊆ N × Log`" should say "3-element **multisets** over
   `N × Log`", since the multiset structure is load-bearing in (G2)/(G3).

---

## 5. Adjudication of the recorded disagreement

**Question.** Is the Corollary I.1 refutation witness — rotated `[[9,1,3]]` plus one free qubit 9,
at `d = 3` — *decoupled* in the strong sense of Definition 2.3? The review's §2.3 table says
**True**, both sectors. The amendment's §2.4 says **False**, with 16 strong witnesses per sector.

**Answer: the amendment is right; the review is wrong.**

**Own computation.** My independent implementation of Definition 2.3 (strong form) gives **16
coupling witnesses in each sector** for the extended instance, i.e. **not decoupled** — while safe
coupling witnesses number **0** in each sector, i.e. **safely decoupled**. Identical figures for the
un-extended rotated `[[9,1,3]]`.

**Proof, no computation needed.** At `d = 3`, `|D| + Σ_c |J_c| ≤ 2` together with
`|{c : J_c ≠ ∅}| ≥ 2` forces `|D| = 0` and exactly two checks contributing one hook each. So a
strong coupling witness is a pair `A ⊊ supp(c)`, `A′ ⊊ supp(c′)`, `c ≠ c′`, with
`χ_A + χ_{A′} ∈ L_X`. Every such `A, A′ ⊆ {0,…,8}`, so `χ_A + χ_{A′}` has coordinate 9 equal to 0.
Adjoining qubit 9 to no check pads `H_Z` and `H_X` with a zero column, so for any `v` supported on
`{0,…,8}`:

```
   H_Z^{ROTF}(v ⊕ 0) = H_Z^{ROT}(v)      and      S_X^{ROTF} = { v ⊕ 0 : v ∈ S_X^{ROT} } ,
   hence   v ⊕ 0 ∈ L_X^{ROTF}   ⟺   v ∈ L_X^{ROT} .
```

The strong-witness sets of the two instances are therefore in bijection. The **review itself**
computes 16 for the un-extended rotated `[[9,1,3]]` in its own §2.6, and even exhibits one
explicitly (`A = {1} ⊆ supp(0,1,3,4)`, `A′ = {4,7} ⊆ supp(4,5,7,8)`, `χ_A + χ_{A′} = e_1+e_4+e_7`,
which I verify lies in `ker H_Z \ S_X` for **both** `n = 9` and `n = 10`). So the review's §2.3 row
contradicts the review's own §2.6 row for the same four checks. It is a transcription/recording slip
in §2.3, not a definitional difference: the review's §A.3 `decoupled()` routine, read line by line,
implements the same `k = 2`, `|D| = 0`, singleton-chain enumeration I did.

**Does the disagreement affect the refutation? No — and the amendment handles this correctly.** This
is the one place where getting it wrong would have mattered: Corollary I.1's *printed* certifier
enumerates the **strong** form, and a strong-form certifier would reject this instance rather than
answer on it. But the promise of §2.1 is *safely* decoupled, Theorem I(2)'s case `|scope(F)| ≥ 2`
invokes *safe* decoupling, and Corollary I.1 explicitly offers the safe certifier too ("safe
decoupling is decided by the same enumeration after computing the `D_c`"). The instance **is** safely
decoupled (0 safe witnesses, both sectors, verified), so the safe certifier passes, Theorem I(3)
answers YES, and the truth is NO. The amendment's §2.4 states exactly this restriction — *"The
refutation is stated above against the safe form only"* — and is right to. Had the amendment simply
adopted the review's number, the refutation would have rested on a false premise while still
reaching a true conclusion; the recomputation was worth doing.

---

## 6. NOT-REVIEWED — explicitly

1. The `K₄` gadget data imported by Remark V.6′ (the wired code, `k = 6`, the "pairwise `≠₃`" report,
   the three shared cosets). Only the abstract step is checked here, as the amendment says.
2. The three unrecomputed members of the five-family census (`HGP(rep₃,rep₃) = [[13,1,3]]`, the
   `3×3` toric code, quantum Hamming `[[15,7,3]]`) and the "56 of 71 random codes" figure.
3. Lemma 1.4's identification of `d_ext(E(M))` with the mechanism minimum (asserted, not derived, in
   the writeup; underlies every island equally).
4. Definition 2.2's quiet multiset→set passage from hook indices to prefix-sum values (islands
   amendment §8 item 8) — not repaired there, not reviewed here.
5. The lift document's `repair ≥ 3` gap (§7.2, 5.6bis) and the `321 059 / 321 059` symmetry in
   NUMERICAL 3.6. Still unreproduced by anyone.
6. 5.6(d)'s `≥` direction. Its hypothesis is stated for the *minimiser* of `|γ| + repair(γ)`, but
   5.4(4) is applied to `γ = π₁F` for the minimum-weight `F`, which need not be that minimiser. This
   is pre-existing, inside the declared `repair ≥ 3` gap, and outside the amended scope — flagged
   only so it is not mistaken for something A1 fixed.
7. Islands review edits 9 and 11, deliberately left open by the amendment.
8. Everything in Islands II and IV, all Courcelle/treewidth citations, and all `d_circ` values
   requiring a circuit simulator. No `stim`, no proposer code executed.
9. Whether the abstract (S1)+(S2)+(S3) hitting problem is in P. My §4.4 shows (S3) restores the
   Observation's conclusion; it does **not** show the resulting fragment is tractable. Island V
   stays open.

## 7. Shared-model caveat

Both amendments and this review derive the *inventory* of realisable residuals and locations from
Definition 1.13 (lift) and Lemma 1.1 / Definition 2.2 (islands) of the documents under review. A
systematic modelling error at that level — a residual class or fault location that the frozen model
admits and these definitions omit — would survive all three of our independent implementations. The
computations are independent; the model design is not.
