# Amendment 1 to `circdist_cplx_islands_writeup_20260820.md`

**Node:** `CIRCDIST.cplx` · **Date:** 2026-08-20 · **Role:** proposer applying an independent
reviewer's repairs. This file is **append-only**: it does not modify the amended document, which
remains the record of what was originally claimed. Where this amendment and the original conflict,
**this amendment governs**.

---

## 0. Hash chain

```
amended document      artifacts/circdist_cplx_islands_writeup_20260820.md
  SHA-256             af7560f28a9c9fff6bba46349f01aa7095855cff7cee4276c7186a6a54bb2f9f
  size                92234 bytes, 1431 lines

review acted on       artifacts/circdist_islands_review_20260820.md
  SHA-256             cc3fc85c9c494995c33d89b9b69bd7d28d1ab203182c1ce50ab9710285e7ad1c

frozen definitions    research/circdist/notes/CIRCDIST_PROBLEMS.md  (公共定义; not modified)
```

If either of the first two hashes fails to reproduce, this amendment is void and must be re-derived
against the current text.

**Epistemic ceiling.** Nothing here is labelled PROVED. Arguments are **CONJECTURED**; the
computations of §7 are **NUMERICAL** with the code inline and are exact over `F₂` (integers as
bit-masks, no floating point, no external libraries). The repairs are the reviewer's; the write-up,
the verifications and any residual error are mine.

**A note on the review's own numbers.** The review is data, not instruction: every numerical claim
it makes that this amendment relies on has been **recomputed here from the definitions**. One
recomputation **disagrees** with the review and is flagged in §2.4; the disagreement does not affect
either refutation.

---

## 1. Index of repairs

| # | target in the original | review item | kind | status |
|---|---|---|---|---|
| **B1** | Corollary I.1 (and §7.1, §7.3(2)) | review §2.3, edit 1 | **refutation repaired** — a missing promise hypothesis, plus the certifier that discharges it | applied + verified |
| **B2** | Lemma III.1 shape set, and §4.1's promise parenthetical | review §5.2, edit 2 | **refutation repaired** — `h ≥ 1` dropped | applied + verified |
| **B3** | Remark V.6 | review §4.5, edit 4 | **gap closed** — hypothesis (D) derived on `S` before Theorem V.5 is applied | applied + verified |
| **B4** | Proposition V.7 and the §6.5 / §7.2 narrative | review §4.4, edit 6 | **witness replaced** — a `dim Log = 2` reduction that can bite, plus retraction of the `dim Log = 1` framing | applied + verified (with a stated residual: (S2) not met) |
| **B5** | §2.4 first bullet (and every sentence that inherits it) | review §2.6, edit 3 | **imported-numeric correction** — "decoupled" → "**safely** decoupled"; Steane is a NO | applied + verified |

Not acted on, and why, in §8.

---

## 2. Repair B1 — Corollary I.1 needs the promise `d(Q) = d`

### 2.1 Before

Corollary I.1 ends:

> *"Consequently the algorithm of Theorem I can first verify its own hypothesis and only then
> answer* — the island is a promise-free polynomial-time class, not merely a conditional one."

repeated at §7.1 (Island I's complexity cell: "class is self-certifying") and at §7.3 item 2
("so Island I is a promise-free polynomial class, not a conditional one").

### 2.2 Why it is wrong

The promise of §2.1 has **three** components: `d(Q) = d`; `k ≥ 1`; safely decoupled. Corollary I.1
certifies only the **third**.

The first is load-bearing. Theorem I(2)'s three-case split disposes of `scope(F) = ∅` by citing
Lemma 1.10, and Lemma 1.10's argument *is* the promise: a scope-0 mechanism is a data-only vector
`χ_D` with `|D| ≤ d−1`, and it is excluded only because `d ≤ d_X`. Neither `D_c` nor a coupling
witness can ever see such a mechanism, because Definition 2.2 requires `I_c ≠ ∅` and Definition 2.3
requires `|{c : J_c ≠ ∅}| ≥ 2`. A code with a low-weight **data-only** logical is therefore
invisible to both tests, and the "self-certified" algorithm answers YES on a NO instance of the
*total* language `Eff-Preserve≥` of Definition 1.9 — the language every algorithm in the file is
said to decide.

### 2.3 The witness, recomputed exactly this session

Rotated `[[9,1,3]]` surface code

```
   H_X rows : (0,1,3,4), (4,5,7,8), (1,2), (6,7)
   H_Z rows : (1,2,4,5), (3,4,6,7), (0,3), (5,8)
```

with **one unencoded free qubit** adjoined (index 9, in no check). Input `d := 3`.

| quantity | computed value |
|---|---|
| `n, k` | `10, 2` |
| `d_X, d_Z, d(Q)` | `1, 1, 1` |
| `|D_c|` per check, X-sector / Z-sector, at `d = 3` | `[16,16,2,2]` / `[16,16,2,2]` — all non-empty |
| safely decoupled (Definition 2.3) | **True**, both sectors (0 safe-coupling witnesses) |
| decoupled (Definition 2.3, strong form) | **False**, both sectors (16 strong witnesses) — see §2.4 |
| the promise's third component, as certified by Corollary I.1's safe-form enumeration | **passes** |
| Theorem I(3)'s test `∀c : D_c ≠ ∅` | **True** ⟹ output **YES** |
| truth of `∃M : d_eff(M) ≥ 3` | **NO** — Lemma 1.8 gives `d_eff(M) ≤ d(Q) = 1` for every `M` |

So the algorithm, run with its hypothesis "self-verified", returns YES on a NO instance.

### 2.4 One disagreement with the review, recorded

The review's §2.3 table lists this instance as "decoupled (strong, Def 2.3): **True**, both
sectors". My recomputation gives **False**, with 16 strong-coupling witnesses in each sector — the
same 16 the review itself reports for the *un*extended rotated `[[9,1,3]]` in its §2.6. That is the
consistent answer: adjoining a qubit that lies in no check cannot destroy a coupling witness, and
the review's explicit witness `A = {1} ⊆ supp(0,1,3,4)`, `A′ = {4,7} ⊆ supp(4,5,7,8)`,
`χ_A + χ_{A′} = e_1+e_4+e_7 ∈ L_X` survives the extension verbatim (verified, §7 block `[B5]`).

**This does not weaken the refutation.** The promise of §2.1 is *safely* decoupled, Theorem I(2)
uses *safe* decoupling, and safe decoupling is what the instance satisfies (0 safe-coupling
witnesses in both sectors, verified). The refutation is stated above against the safe form only.

### 2.5 After — Corollary I.1, repaired

> **Corollary I.1′ (the class is self-certifying, with the distance check) — CONJECTURED.** For
> fixed `d` and bounded check weight `w`, all three components of the promise of §2.1 are decidable
> in polynomial time:
>
> 1. **`d ≤ d(Q)`**: enumerate every `v ∈ F_2^n` of weight `≤ d − 1` (`O(n^{d−1})` of them) and
>    verify that none lies in `L_X ∪ L_Z`, at `O(n²)` per query against precomputed RREFs of `H_X`,
>    `H_Z`. Cost `O(n^{d−1} · n²) + O(n³)`. Together with Lemma 1.8 (`d_eff ≤ d(Q)` always) this
>    settles the instance immediately in the negative when it fails.
> 2. **`k ≥ 1`**: `k = n − rank H_X − rank H_Z`, `O(n³)`.
> 3. **safe decoupling**: as in the original — enumerate all tuples of at most `d − 1` elements of
>    the ground set `{e_q}_q ∪ ⋃_c {χ_A : ∅ ≠ A ⊊ supp(c)}`, discard those whose per-check parts are
>    not chains (Lemma 1.15), keep those realisable inside a locally safe order, and test `Σ ∈ L_X`
>    on those of scope `≥ 2`. Cost `O((n + Σ_c 2^{w_c})^{d−1} · n²)` **plus** the `O(Σ_c w_c! ·
>    (w_c+n)^{d−1} · n²)` needed to compute the `D_c` first (see §2.6).
>
> Consequently the algorithm of Theorem I can verify its own hypothesis and only then answer, and
> the island is a promise-free polynomial-time class for fixed `d` and bounded `w`. **Component 1
> is not optional**: without it the algorithm answers YES on instances with `d(Q) < d`, of which
> §2.3 exhibits one. ∎

Note this is precisely the sentence the original already states for Island IV (§5.4, fourth
bullet): "*The promise is load-bearing in exactly one place: Lemma 1.10 / Lemma IV.1, to exclude
data-only mechanisms. Without the promise the same algorithm still decides `Eff-Preserve≥` after
one extra check … which is `O(n³)`.*" The repair is to copy it to Island I. Note also the caveat
that sentence carries: for *general* `d` the extra check is the NP-hard distance problem
(ASSUMPTION A5) — it is polynomial only because `d` is fixed, which is exactly the regime Island I
is stated in.

**Propagation.** §7.1's Island I cell should read "P for fixed `d`, bounded `w`; class is
self-certifying **including the distance component (Cor. I.1′)**". §7.3 item 2's clause "so Island I
is a promise-free polynomial class, not a conditional one" is true only with Corollary I.1′ in
place, and should cite it.

### 2.6 Repair B1b — the cost bound in Corollary I.1 covers only the strong form

Review §2.4 (edit 8), applied inside Corollary I.1′ above. The displayed bound
`O((n + Σ_c 2^{w_c})^{d−1} · n²)` is the cost of the **strong** enumeration, where Lemma 1.15's
forward direction reduces "realisable" to "is a chain". For the **safe** form the sentence "safe
decoupling is decided by the same enumeration after computing the `D_c`" additionally requires, per
candidate chain `J_c`, the test `∃π ∈ D_c : J_c ⊆ Hooks(π)`, and computing the `D_c` costs
`Σ_c w_c! · (w_c + n)^{d−1} · n²` — Theorem I(3)'s own bound, absent from the displayed expression.
Still polynomial for fixed `d` and bounded `w`, and still FPT in `w` for fixed `d`; but the
displayed expression is incomplete as printed. Corrected above.

### 2.7 Repair B1c — Corollary I.2's complexity decoration

Review §2.5 (edit 7). `∀c : D_c ≠ ∅` is a polynomial-size **conjunction** of `Σ_1` statements, each
with a polynomial-time inner predicate for fixed `d`, hence the whole is in **NP**. A conjunction of
NP statements is NP; the `∀c` prefix does not produce a coNP half, and nothing in the corollary
supplies one. Corollary I.2's phrase "**decided in `NP ∩ coNP`-style form**" is **withdrawn**;
the corollary should read "…are decided **in NP**: a YES certificate is a single schedule,
verifiable in polynomial time for fixed `d`. We do **not** claim a polynomial algorithm in this
regime." The operative content (NP membership, single-schedule certificate, no polynomial claim) is
unchanged.

### 2.8 Repair B1d — Definition 2.3's circular parenthetical

Review §2.1 caveat 2 (edit 5). Definition 2.3's gloss —

> *"by Lemma 1.15 these are exactly the chains contained in `Hooks(π)` for some `π ∈ D_c`"*

— is circular as a justification, and read as "`𝒞_c = {all chains}`" it is **false**: Lemma 1.15
realises a chain by *some* order, not by a *locally safe* one. Explicit separation, verified here:
on the rotated `[[9,1,3]]` the singleton chain `{4,7} ⊆ supp(4,5,7,8)` is realisable (it is a hook
of e.g. the order `(5,8,4,7)`) but by **no** locally safe order of that check, while
`{1} ⊆ supp(0,1,3,4)` *is* realisable by a locally safe order (§7 block `[B5]`). Strike the
parenthetical. Definition 2.3 itself is unaffected: it defines `𝒞_c` directly.

---

## 3. Repair B2 — Lemma III.1 must allow `h = 0`

### 3.1 Before

The shape set of §4.3 is defined with

> "A **shape** is a triple `σ = (δ, h, (p_1,…,p_h))` with `δ, h ≥ 0`, `δ + h ≤ d − 1`, **`h ≥ 1`**,
> and `1 ≤ p_s ≤ w − 1`."

and Lemma III.1 is stated with **no promise hypothesis**:

> "`𝔗 ⊨ Φ_{t,w,d}` iff there is a schedule `M` with `d_eff(M) ≥ d`."

while its own `(⇒)` proof says in-line: "`h ≥ 1` **by Lemma 1.10 — this is where the promise is
used**". §4.1 compounds this: "*the algorithm actually decides the total surrogate `Eff-Preserve≥`
of Definition 1.9, so the promise is only needed to convert `≥ d` into `= d`*".

### 3.2 Why it is wrong, and the same witness

Because the shape set has `h ≥ 1`, `Φ` contains **no** conjunct forbidding a scope-0 (data-only)
mechanism. On an instance with `d > d(Q)`, `Φ` can be satisfied while every schedule has
`d_eff(M) ≤ d(Q) < d`.

Same witness as §2.3: rotated `[[9,1,3]]` ⊕ one free qubit, `d = 3`. At `d = 3`, a mechanism with
`h ≥ 1` is one of Lemma IV.1's kinds (a)–(d); kinds (a)–(c) are excluded because every check has a
locally safe order (`|D_c| = [16,16,2,2]` in both sectors, verified), and kind (d) is excluded
because the instance is safely decoupled (verified). So the schedule that picks a locally safe order
at every check satisfies `Sched ∧ ⋀_σ ¬Mech_σ`, i.e. `𝔗 ⊨ Φ_{t,w,3}` — yet `d_eff(M) = d(Q) = 1 < 3`
for every `M`.

### 3.3 After — one token deleted

> **Shapes, corrected.** A **shape** is a triple `σ = (δ, h, (p_1,…,p_h))` with `δ, h ≥ 0`,
> `δ + h ≤ d − 1`, and `1 ≤ p_s ≤ w − 1`. (The clause `h ≥ 1` is **deleted**. The degenerate shape
> `δ = h = 0` gives `Y = ∅`, and `¬InStab(∅)` is false because `0 ∈ S_X`, so that shape's conjunct
> is vacuous and may be kept or dropped at will.)
>
> **Lemma III.1′ (correctness, unconditional) — CONJECTURED.** `𝔗 ⊨ Φ_{t,w,d}` iff there is a
> schedule `M` with `d_eff(M) ≥ d`. **No promise is used.**
>
> *Proof.* `(⇐)` unchanged, with one extra case: if `Mech_σ^X` holds for a shape with `h = 0`, then
> `In_σ(q) = ⊕_{s≤δ}(q = q_s)` and `Y` is the support of `χ_{q_1} + ⋯ + χ_{q_δ}`; `Undet ∧ ¬InStab`
> puts that vector in `L_X`, so the multiset of the corresponding `δ ≤ d − 1` **data** columns of
> `Cols_X(M)` is a mechanism (data columns `e_q` lie in `Cols_X(M)` for every `M`, by Lemma 1.1 /
> the argument of Lemma 1.8), whence `d_eff(M) ≤ d − 1`. `(⇒)` unchanged **except** that the
> sentence "`h ≥ 1` by Lemma 1.10 — this is where the promise is used" is deleted and replaced by:
> a minimal mechanism `F = (D, (I_c)_c)` has `δ := |D|` data columns and `h := Σ_c |I_c| ≥ 0` hook
> columns with `δ + h ≤ d − 1`, and **every** such `(δ,h)` is now the index of a shape, so `Mech_σ`
> is satisfied and `Φ` is contradicted. ∎

`|Φ_{t,w,d}|` still depends only on `(w,d)`: the shape count rises from
`Σ_{δ+h≤d−1, h≥1}(w−1)^h` to `Σ_{δ+h≤d−1, h≥0}(w−1)^h`, which is a function of `(w,d)` alone. At
`d = 3, w = 4` the count of `(δ,h)` index pairs rises from 3 to 6 (verified). Theorem III and
Corollary III.1 go through verbatim with `Φ` so amended, and gain the property §4.1 advertised.

**§4.1, after.** The promise line becomes: *"Promise: `d(Q) = d`, `k ≥ 1`. The algorithm decides the
**total** surrogate `Eff-Preserve≥` of Definition 1.9 unconditionally (Lemma III.1′), so the promise
is used only to convert `≥ d` into `= d`."* Before this amendment that parenthetical was false; with
`h = 0` admitted it is true as written, which is why the review recommends this repair over adding a
promise hypothesis to Lemma III.1.

### 3.4 Local verification (NUMERICAL, §7 block `[B2]`)

On the same witness, the newly admitted shape fires:

```
σ = (δ = 1, h = 0, ()) ,  q_1 := qubit 9 ,  Y = supp(e_9)
Undet(Y)   ⟺  H_Z χ_Y = 0                            : True
InStab(Y)  ⟺  χ_Y ∈ S_X                              : False   ⟹  ¬InStab(Y) : True
⟹  Mech_σ^X is satisfied under EVERY labelling ⟹ Φ_{t,4,3} is unsatisfiable ⟹ answer NO.  Correct.
```

### 3.5 Repair B2b — the guards of §4.3 and Corollary III.1's `Θ` clause

Review §5.3 (edit 10), cosmetic, applied for the record. Read one-sortedly over `V ⊔ E`:
`∀e (⋁_p e ∈ E_p)` in *total* should carry the guard `Edge(e) :≡ ¬Data(e) ∧ ¬ChkX(e) ∧ ¬ChkZ(e)`;
`¬Data(c)` used as "c is a check" should be `ChkX(c) ∨ ChkZ(c)`; and the `q_1,…,q_δ` of `Φ` should
be guarded by `Data(·)` as the `c_s` are guarded by `ChkX(·)`. All three are harmless as written
(`inc(e,c)` is false when `c` is an edge, so the check-guarded clauses are vacuous there; a non-data
`q_s` contributes nothing to `In_σ`, yielding a constraint corresponding to a *shorter* mechanism,
which is implied by another shape) and all three vanish under the two-sorted reading of MSO₂, which
is the intended one. Corollary III.1 additionally omits totality and single-valuedness clauses for
`Θ_1,…,Θ_T` (every CNOT must receive exactly one time step); add one bounded conjunct of the same
shape as *total* and *single-valued* in `Sched`. None of this changes `|Φ|`'s dependence on
`(w,d)` or on `T`.

---

## 4. Repair B3 — Remark V.6 must derive (D) before invoking Theorem V.5

### 4.1 Before

Remark V.6 builds the bipartite graph `B` for the `K₄` composite of
`circdist_cplx_gadget_20260820.md` §5.3 and applies Hall, concluding that the Hall violation on
`S = {c_0,c_1,c_5,c_6}` "is the whole reason the instance is a NO". `B` and the Hall criterion are
equivalent to the CSP **only under hypothesis (D)** of Theorem V.5, and Remark V.6 never says so.
§7.2 asserts "(D) *does* hold for the `K₄` counterexample", but neither section derives it.

This is not optional. Without (D) the `K₄` configuration would be **trivially YES**: Corollary V.2
forbids a pair only when the two chosen values are equal in `Q/Log` **and unequal in `Q`**, so if the
four checks could all pick the *same* value in `Q`, no pair would be forbidden. Verified
exhaustively below.

### 4.2 After — (D) on `S`, derived, then Theorem V.5 applied

> **Remark V.6′ (Theorem V.5 explains the `K₄` obstruction) — CONJECTURED.**
>
> *Step 1 — (D) restricted to `S`.* The gadget document reports that the four X-checks
> `S = {c_0,c_1,c_5,c_6}` of the wired composite are **pairwise `≠₃`**: under the identification of
> each `L_c` with the common 3-element coset set `ν(L_{c_0}) = ν(L_{c_1}) = ν(L_{c_5}) = ν(L_{c_6})`,
> the constraint between any two of them is "the two chosen cosets differ", i.e.
> `forbidden(x_c, x_{c′}) ⟺ ν(x_c) = ν(x_{c′})`. Compare Corollary V.2:
> `forbidden(x_c, x_{c′}) ⟺ ν(x_c) = ν(x_{c′}) **and** x_c ≠ x_{c′}`. Combining, for `c ≠ c′` in `S`:
> if `ν(x_c) = ν(x_{c′})` then the pair is forbidden, hence `x_c ≠ x_{c′}`; and if
> `ν(x_c) ≠ ν(x_{c′})` then `x_c ≠ x_{c′}` automatically. So `x ≠ x′` for **all** `x ∈ L_c`,
> `x′ ∈ L_{c′}`, `c ≠ c′` in `S` — that is, `L_c ∩ L_{c′} = ∅` in `Q`, which is hypothesis (D)
> restricted to `S`.
>
> *Step 2 — only `(D)|_S` is needed.* Theorem V.5 assumes (D) globally, but the **NO** direction
> used here needs it only on `S`: under `(D)|_S`, for `c ≠ c′` in `S` we have
> `forbidden ⟺ ν(x_c) = ν(x_{c′})`, so any valid assignment restricts on `S` to an *injective* map
> `S → ν(⋃_{c∈S} L_c)`. Since `|S| = 4` and the image has 3 elements, no such map exists.
>
> *Step 3 — Hall.* Equivalently `|N_B(S)| = 3 < 4 = |S|`, so `B` has no left-saturating matching and
> the instance is a NO. ∎

The remark's downstream point stands and is now supported: *even without transitivity*,
list-all-different is in P, so any reduction whose output satisfies (D) is a reduction to a
polynomial problem — a cleaner and more general reason than "the `≠₃` edges form cliques" for why
local `≠₃` gadgets cannot give hardness.

### 4.3 Local verification (NUMERICAL, §7 block `[B3]`)

The abstract `K₄` configuration — four checks, each with a 3-element list, the three lists' `ν`-images
equal, and `(D)|_S` holding (distinct checks never share a value in `Q`):

```
exhaustive over all 3^4 = 81 assignments        : 0 satisfying assignments        (NO, as claimed)
Hall                                            : |N_B(S)| = 3 < 4 = |S|          (consistent)
same configuration WITHOUT (D) (all four checks may hold one common value x):
        forbidden(x, x) is False                : True  ⟹ the configuration is trivially YES
```

So (D) is exactly what separates the NO from a trivial YES, and Remark V.6 without it proves
nothing. The `K₄` data itself (the wired code, `k = 6`, the three shared cosets) is **imported and
NOT-REVIEWED here**; I did not reconstruct the code. What is verified is the abstract step.

---

## 5. Repair B4 — Proposition V.7's witness cannot bite; replacement

### 5.1 Before, and why it cannot bite

Proposition V.7 reduces 3-SAT to the abstract partial-section hitting problem of Theorem V.3(3),
using `N := F_2^M` and **`Log := F_2 = {0, ℓ}`**, i.e. `dim Log = 1`, i.e. `k = 1`. §6.5's first
bullet then says the side condition (S1) "*forces each clause to contain an even number of negated
literals, so the encoding as written produces only a restricted (**and possibly tractable**)
fragment*".

That is an understatement. With `dim Log = 1`, (S1) is **exactly** the parity hypothesis of
Theorem V.4, and the (S1)-restricted fragment is not "possibly tractable" — it is **all-YES**,
decided by outputting yes, by the writeup's own theorem four pages earlier:

> Over `Log = F_2`, a multiset `{ε_1,ε_2,ε_3}` with `ε_1+ε_2+ε_3 = 0` has an even number of `ℓ`s,
> hence contains `0`. So the total function `g ≡ 0` hits every (S1)-compliant list. In the 3-SAT
> encoding this is "set every variable to the value that satisfies its positive literals", and every
> (S1)-compliant clause has a positive literal.

Verified exhaustively (§7 block `[B4]`): the sum-zero triples over `F_2` are `(0,0,0)`, `(0,ℓ,ℓ)`
and its permutations, and every one contains `0`.

Consequently §7.2's framing — "*the polynomial claim needs either (D), or `k ≤ 1` (Theorem V.4), or
a new argument*" — misdescribes the situation, because the printed NP-completeness proof lives
**entirely inside the second escape**. A hardness statement with any bite on Island V must use
`dim Log ≥ 2`.

### 5.2 After — Proposition V.7′, with `dim Log = 2`

> **Proposition V.7′ (the target of the reduction is not a matching problem; (S1)-compliant form)
> — CONJECTURED.** Let `Log = F_2² = {0,a,b,c}` with `c = a+b`, so `dim Log = 2`. The problem
>
> > *given a finite `F_2`-space `N` and 3-element lists `L_1,…,L_m ⊆ N × Log`, each satisfying
> > (S1) `Σ_{r=1}^{3} ε_{t,r} = 0` in `Log`, decide whether there is a partial function
> > `g : N ⇀ Log` with, for every `t`, some `(n,ε) ∈ L_t` having `n ∈ dom(g)` and `g(n) = ε`*
>
> is **NP-complete**. In particular it remains NP-complete under (S1) and outside the reach of
> Theorem V.4.
>
> *Proof.* Membership in NP is as before (`g` restricted to the `≤ 3m` used points is a polynomial
> certificate). Hardness: reduce 3-SAT. Given a 3-CNF `ψ` over `v_1,…,v_M` with clauses
> `C_1,…,C_m`, take `N := F_2^{2M+m+1}` and let `π`, `ν_j`, `ν′_j` (`j ≤ M`), `τ_t` (`t ≤ m`) be
> distinct **non-zero** basis vectors. Emit the following lists (every one has `Σ_r ε_r = 0`):
>
> ```
>   (G1)  { (π,a), (π,b), (π,c) }                       a+b+c = 0     ⟹ g(π) ∈ {a,b,c}
>   (G2)  { (π,0), (π,b), (π,b) }                       0+b+b = 0     ⟹ g(π) ∈ {0,b}
>         (G1)+(G2)                                                   ⟹ g(π) = b
>   (G3)  { (p,0), (p,a), (p,a) }   for p ∈ {ν_j, ν′_j, τ_t}          ⟹ g(p) ∈ {0,a}   ("Boolean")
>   (G4)  { (π,0), (ν_j,a), (ν′_j,a) }                                ⟹ ν_j ∨ ν′_j
>   (G5)  { (π,0), (ν_j,0), (ν′_j,0) }                                ⟹ ¬ν_j ∨ ¬ν′_j
>         (G4)+(G5)                                                   ⟹ ν′_j = ¬ν_j
>   (G6)  { (τ_t,0), (p_1,a), (p_2,a) }                               ⟹ ¬τ_t ∨ l_1 ∨ l_2
>   (G7)  { (π,0), (τ_t,a), (p_3,a) }                                 ⟹ τ_t ∨ l_3
> ```
>
> where for clause `C_t = (l_1 ∨ l_2 ∨ l_3)` the point `p_i` is `ν_j` if `l_i = v_j` and `ν′_j` if
> `l_i = ¬v_j`. The literal `(π, 0)` is unsatisfiable because `g(π) = b`, so (G4), (G5), (G7) act as
> **2-clauses**; `TRUE := a`, `FALSE := 0` on Boolean points. (G6)∧(G7) is the standard splitting
> `(¬τ ∨ l_1 ∨ l_2) ∧ (τ ∨ l_3) ≡ (l_1 ∨ l_2 ∨ l_3)`. Hence a hitting `g` yields a satisfying
> assignment `α(v_j) := [g(ν_j) = a]`, and conversely a satisfying `α` yields `g` by setting
> `g(π) = b`, `g(ν_j), g(ν′_j)` from `α`, and `g(τ_t) = a` iff `l_1 ∨ l_2` is true under `α`. ∎
>
> **What the `dim Log = 2` room buys.** Over `F_2` the only sum-zero triples are `(0,0,0)` and
> `(0,ℓ,ℓ)`, both of which contain `0`, so `g ≡ 0` always wins. Over `F_2²` the triple `(a,b,c)` of
> pairwise-distinct non-zero values also sums to zero; (G1) uses it, and it is what kills every
> constant `g`. `g ≡ v` must satisfy (G1) (`v ∈ {a,b,c}`), (G2) (`v ∈ {0,b}`) and (G3)
> (`v ∈ {0,a}`) simultaneously, which is impossible.

### 5.3 What the replacement does **not** achieve — (S2)

The construction satisfies (S1) but **not** (S2) (`Σ_r m(x_c^{(r)}) = 0` in `N`). The obstruction is
structural, and worth recording because it sharpens the open question rather than merely admitting a
shortfall:

> **Observation.** Under (S2), a list with two options on the same point `n` forces the third
> option's `N`-part to be `n + n = 0`; and a list with all three options on one point forces
> `3n = n = 0`. Hence **no (S2)-compliant list can constrain a single non-zero point to a proper
> subset of `Log`** — the unary forcing gadgets (G1), (G2), (G3), which the reduction needs to make
> points Boolean and to pin `g(π)`, are exactly what (S2) forbids. (Note (S1)+(S2) together are the
> writeup's Lemma V.1(5), `x^{(1)}+x^{(2)}+x^{(3)} = 0` in `Q`.)

So Proposition V.7′ shows the abstract problem is hard **under (S1) with `dim Log ≥ 2`**, which is
what the review demands — the hardness no longer lives inside the fragment Theorem V.4 trivialises —
while leaving (S2) and realisability as the two remaining tamers.

### 5.4 After — §6.5 and §7.2, restated

* §6.5's bullet **(S1)** should read: "*(S1)* `Σ_r β(x_c^{(r)}) = 0`. In the `dim Log = 1` encoding
  of the original Proposition V.7 this forces each clause to contain an even number of negated
  literals, and the resulting fragment is **not merely 'possibly tractable' — it is all-YES**, by
  Theorem V.4 (equivalently: `g ≡ 0` hits every list). The original Proposition V.7 therefore has no
  bite on Island V and is superseded by Proposition V.7′, which is (S1)-compliant with
  `dim Log = 2`."
* §7.2's sentence "*Without (D) the abstract problem is NP-complete (Proposition V.7, by a two-line
  reduction from 3-SAT), so the polynomial claim needs either (D), or `k ≤ 1` (Theorem V.4), or a
  new argument using the two linear side conditions (S1), (S2)*" should read: "*Without (D) the
  abstract problem is NP-complete even under (S1) and with `dim Log = 2` (Proposition V.7′), so the
  polynomial claim needs either (D), or `k ≤ 1` (Theorem V.4), or a new argument using **(S2)**
  together with realisability. (S1) alone does not tame it; (S1) with `dim Log ≤ 1` is Theorem V.4
  and is a separate escape, not a taming of the abstract problem.*"
* §7.1's Island V cell is unchanged (**GAP FOUND**), and the **Repricing** paragraph of §6.5 is
  unchanged in its conclusion (certify the node's third minimal-acceptance branch on Islands I–IV,
  not on Island V), but its cost estimate should now read "decide whether **(S2)** plus
  realisability tame the hitting problem", (S1) having been removed from the list of candidate
  tamers.

### 5.5 Local verification (NUMERICAL, §7 block `[B4]`)

The reduction of §5.2 was implemented and its output solved by a complete backtracking search over
partial functions `g` (no heuristics; exhaustive by construction), then compared with brute-force
3-SAT:

```
   3-CNF instance                       #lists  #points  3-SAT  hitting  agree
   (x1 ∨ x2 ∨ x3)                          17       8     YES     YES     ✓
   mixed 2-clause instance                 20       9     YES     YES     ✓
   all 8 clauses on 3 variables (UNSAT)    38      15     NO      NO      ✓
   (S1) assertion on every emitted list                            0 violations
```

The UNSAT row is the load-bearing one: the reduction produces a genuine NO, so the encoding is not
vacuously all-YES the way the `dim Log = 1` fragment is.

---

## 6. Repair B5 — the imported-numeric correction, propagated

### 6.1 Before

§2.4's first bullet: "*Imported NUMERICAL evidence (`circdist_cplx_recon_20260820.md` §3): all five
structured `d = 3` families probed (rotated `[[9,1,3]]`, `3×3` toric, unrotated `[[13,1,3]]`,
Steane, quantum Hamming `[[15,7,3]]`) are **decoupled**, while 56 of 71 random self-orthogonal
weight-6 CSS codes with `d_X = 3` are not. Decoupling is therefore a property of structure, and
generic instances fall outside the island.*"

### 6.2 What is wrong, recomputed exactly (§7 block `[B5]`)

Definition 2.3 makes **decoupled** (all chains) strictly stronger than **safely decoupled** (chains
inside locally safe orders). Recomputing both at `d = 3`, exact over `F_2`, in **both** sectors:

| code | `|D_c|` X-sector / Z-sector | strong witnesses | **decoupled** | safe witnesses | **safely decoupled** |
|---|---|---|---|---|---|
| Steane `[[7,1,3]]` | `[0,0,0]` / `[0,0,0]` | 48 / 48 | **False** | 0 / 0 | True (vacuously — `𝒞_c = {∅}`) |
| rotated `[[9,1,3]]` | `[16,16,2,2]` / `[16,16,2,2]` | 16 / 16 | **False** | 0 / 0 | True |

Explicit strong witness, rotated `[[9,1,3]]`, X-sector: `A = {1} ⊆ supp(0,1,3,4)`,
`A′ = {4,7} ⊆ supp(4,5,7,8)`, `χ_A + χ_{A′} = e_1+e_4+e_7 ∈ L_X` (verified: in `ker H_Z`, not in
`S_X`). `A` **is** realisable by a locally safe order of its check; `A′` is **not** realisable by
any locally safe order of its — which is exactly why the instance is safely decoupled but not
decoupled.

Two further consequences:

1. **`|D_c| = 16` of `24` for the rotated code's weight-4 checks** reproduces the writeup's own
   §3.7 imported figure ("8 of 24 unsafe"), which is the cross-check licensing the rest of this
   computation.
2. **Steane `[[7,1,3]]` has zero locally safe orders at `d = 3`, in both sectors.** By Theorem I(1)
   it is therefore a **NO** instance — `∀M : d_eff(M) ≤ 2`. Listing it among "structured families
   that are decoupled", alongside genuine YES instances, obscures that one of the five is a NO.

### 6.3 After

§2.4's first bullet should read:

> * **It is a hypothesis, not a theorem about codes.** Island I says nothing about *which* codes are
>   (safely) decoupled. Imported NUMERICAL evidence (`circdist_cplx_recon_20260820.md` §3), as
>   corrected and re-verified in `circdist_cplx_islands_amendment1_20260820.md` §6: all five
>   structured `d = 3` families probed (rotated `[[9,1,3]]`, `3×3` toric, unrotated `[[13,1,3]]`,
>   Steane, quantum Hamming `[[15,7,3]]`) are **safely decoupled**; **two of them — Steane and the
>   rotated `[[9,1,3]]` — are *not* decoupled in the strong sense of Definition 2.3** (48 resp. 16
>   coupling witnesses per sector), so the evidence supports the *safe* form only. The two
>   hypergraph-product members of the list (`HGP(rep₃,rep₃) = [[13,1,3]]` and the `3×3` toric code)
>   are decoupled in both senses, with every local order safe, exactly as Theorem II.4 predicts.
>   **Note further that Steane is a NO instance**: it has `D_c = ∅` for every check in both sectors
>   at `d = 3`, so by Theorem I(1) `∀M : d_eff(M) ≤ 2`; safe decoupling holds vacuously there and
>   carries no information. Meanwhile 56 of 71 random self-orthogonal weight-6 CSS codes with
>   `d_X = 3` are not decoupled. Decoupling is therefore a property of structure, and generic
>   instances fall outside the island.

**Every other sentence inheriting the wrong form.** Searched exhaustively for the string
"decoupled" in the amended document; the occurrences are at lines 266, 269, 299, 314–316, 325, 337,
339, 376, 384, 394–396, 1321, 1356. Of these:

* **line 394–396 (§2.4 bullet 1)** — the only place using the imported five-family claim; corrected
  above. It is the **only sentence in the document that used the wrong form**.
* lines 266, 269, 299, 314–316, 325, 337, 339, 384 are definitional or state the promise, and all
  already say "**safely** decoupled" where safe decoupling is meant. No change.
* line 376 (Corollary I.1) says "*decoupled* (Definition 2.3, strong form)" and is correct as a
  statement about the strong form; but see §2.5–2.6 — the *promise* is the safe form, so the
  certifier that matters is the safe one and its cost bound is the corrected one.
* lines 1321 and 1356 (§7.1, §7.3) are covered by §2.5's propagation note.

Nothing else in the file depends on which form the imported evidence supports.

---

## 7. NUMERICAL — code and outputs

Python 3.9, standard library only. Exact over `F₂`; subsets of `[n]` are integer bit-masks.
Definitions 2.2 and 2.3 are implemented at `d = 3` directly from the writeup's text; Theorem I(1)/(3)
and Lemma 1.8 are used only as stated. Blocks `[B1]`, `[B2]`, `[B3]`, `[B4]`, `[B5]` correspond to
§§2.3, 3.4, 4.3, 5.5, 6.2.

```python
from itertools import combinations, permutations, product

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

def rank(rows, n): return len(rref(rows, n)[0])
def reduce_vec(v, R, piv):
    for i, p in enumerate(piv):
        if (v >> p) & 1: v ^= R[i]
    return v
def kernel(rows, ncols):
    R, piv = rref(rows, ncols)
    free = [c for c in range(ncols) if c not in piv]; basis = []
    for f in free:
        v = 1 << f
        for i, p in enumerate(piv):
            if (R[i] >> f) & 1: v |= 1 << p
        basis.append(v)
    return basis
def span(basis):
    els = {0}
    for b in basis: els |= {e ^ b for e in els}
    return els
def pc(x): return bin(x).count('1')
def mask(s): return sum(1 << q for q in s)

class CSS:
    def __init__(self, HXs, HZs, n, name=""):
        self.name, self.n, self.HXs, self.HZs = name, n, HXs, HZs
        self.HX = [mask(s) for s in HXs]; self.HZ = [mask(s) for s in HZs]
        for a in HXs:
            for b in HZs: assert len(set(a) & set(b)) % 2 == 0, "not CSS"
        self.RX, self.pX = rref(self.HX, n); self.RZ, self.pZ = rref(self.HZ, n)
        self.k = n - rank(self.HX, n) - rank(self.HZ, n)
    def synZ(self, v): return tuple(pc(v & h) % 2 for h in self.HZ)
    def synX(self, v): return tuple(pc(v & h) % 2 for h in self.HX)
    def inSX(self, v): return reduce_vec(v, self.RX, self.pX) == 0
    def inSZ(self, v): return reduce_vec(v, self.RZ, self.pZ) == 0
    def inLX(self, v): return all(x == 0 for x in self.synZ(v)) and not self.inSX(v)
    def inLZ(self, v): return all(x == 0 for x in self.synX(v)) and not self.inSZ(v)
    def dX(self):
        w = [pc(v) for v in span(kernel(self.HZ, self.n)) - span(self.RX) if v]
        return min(w) if w else float('inf')
    def dZ(self):
        w = [pc(v) for v in span(kernel(self.HX, self.n)) - span(self.RZ) if v]
        return min(w) if w else float('inf')

STE_CHK = [[3,4,5,6],[1,2,5,6],[0,2,4,6]]
STEANE  = CSS(STE_CHK, STE_CHK, 7, "Steane [[7,1,3]]")
ROT_X   = [[0,1,3,4],[4,5,7,8],[1,2],[6,7]]
ROT_Z   = [[1,2,4,5],[3,4,6,7],[0,3],[5,8]]
ROT     = CSS(ROT_X, ROT_Z,  9, "rotated [[9,1,3]]")
ROTF    = CSS(ROT_X, ROT_Z, 10, "rotated [[9,1,3]] + free qubit 9")   # <- the §2.3 witness

# ---- Definition 2.2 (local safety) at d = 3, and Definition 2.3 ------------------
def hooks_of_order(order):
    return [mask(order[j:]) for j in range(1, len(order))]      # S_1 .. S_{w-1}

def locally_safe(code, order, sector):
    """no mechanism of size <= 2 with I_c != empty and I_{c'} = empty for c' != c."""
    inL = code.inLX if sector == 'X' else code.inLZ
    red = (code.RX, code.pX) if sector == 'X' else (code.RZ, code.pZ)
    vals = {}
    for S in hooks_of_order(order): vals[reduce_vec(S, *red)] = S   # V(pi_c) as a SET in Q
    V = list(vals.values())
    for S in V:
        if inL(S): return False                                     # |J|=1, |D|=0
        for q in range(code.n):
            if inL(S ^ (1 << q)): return False                      # |J|=1, |D|=1
    for S1, S2 in combinations(V, 2):
        if inL(S1 ^ S2): return False                               # |J|=2, |D|=0
    return True

def safe_hook_sets(code, sector):
    chks = code.HXs if sector == 'X' else code.HZs
    Ds, hs = [], []
    for c in chks:
        D = [p for p in permutations(c) if locally_safe(code, p, sector)]
        s = set()
        for p in D: s |= set(hooks_of_order(p))
        Ds.append(D); hs.append(s)
    return Ds, hs

def all_proper_subsets(c):
    return [mask([c[t] for t in range(len(c)) if r >> t & 1])
            for r in range(1, (1 << len(c)) - 1)]

def coupling(code, sector, strong):
    """d = 3: two checks, one hook each, summing into L_X (resp. L_Z)."""
    chks = code.HXs if sector == 'X' else code.HZs
    inL  = code.inLX if sector == 'X' else code.inLZ
    fam  = ([all_proper_subsets(c) for c in chks] if strong
            else [sorted(h) for h in safe_hook_sets(code, sector)[1]])
    return [(i, A, j, B) for i, j in combinations(range(len(chks)), 2)
            for A in fam[i] for B in fam[j] if inL(A ^ B)]

# ---- [B5] / [B1] ----------------------------------------------------------------
for code in (STEANE, ROT, ROTF):
    for sec in ('X', 'Z'):
        Ds, _ = safe_hook_sets(code, sec)
        print(code.name, sec, [len(x) for x in Ds],
              "strong:", len(coupling(code, sec, True)),
              "safe:",   len(coupling(code, sec, False)))
print(ROTF.n, ROTF.k, ROTF.dX(), ROTF.dZ())                    # 10 2 1 1
print(ROT.inLX(mask([1]) ^ mask([4,7])))                       # True: e1+e4+e7 in L_X
print([v for v in range(1, 1 << ROTF.n)                        # the Cor. I.1' scan
       if pc(v) <= 2 and (ROTF.inLX(v) or ROTF.inLZ(v))])      # [512] = {e_9}

# ---- [B2] Lemma III.1 with h = 0 -------------------------------------------------
Y = 1 << 9
print(all(x == 0 for x in ROTF.synZ(Y)), ROTF.inSX(Y))         # Undet(Y)=True, InStab(Y)=False

# ---- [B3] the abstract K4 configuration -----------------------------------------
cos = [0, 1, 2]
def nu(x): return x[1]
def forbidden(x, y): return nu(x) == nu(y) and x != y
sat = sum(1 for pick in product(cos, repeat=4)
          if all(not forbidden((i, pick[i]), (j, pick[j]))
                 for i, j in combinations(range(4), 2)))
print(sat, forbidden((0,0),(0,0)))                             # 0  False

# ---- [B4] Proposition V.7' -------------------------------------------------------
A, B, C = 1, 2, 3                                # Log = F_2^2 = {0,A,B,C}, C = A+B
def build(cnf, M):
    pts = {}
    def P(nm):
        if nm not in pts: pts[nm] = len(pts) + 1          # distinct NON-ZERO identifiers
        return pts[nm]
    L = []; pi = P('pi')
    L.append([(pi,A),(pi,B),(pi,C)]); L.append([(pi,0),(pi,B),(pi,B)])      # g(pi) = B
    for j in range(M):
        v, vb = P(('v',j)), P(('nv',j))
        L.append([(v,0),(v,A),(v,A)]); L.append([(vb,0),(vb,A),(vb,A)])     # Boolean
        L.append([(pi,0),(v,A),(vb,A)]); L.append([(pi,0),(v,0),(vb,0)])    # vb = not v
    for t, cl in enumerate(cnf):
        tau = P(('t',t)); L.append([(tau,0),(tau,A),(tau,A)])
        p = [P(('v',j) if s else ('nv',j)) for (j,s) in cl]
        L.append([(tau,0),(p[0],A),(p[1],A)])                               # ~tau v l1 v l2
        L.append([(pi,0),(tau,A),(p[2],A)])                                 # tau v l3
    for l in L: assert (l[0][1] ^ l[1][1] ^ l[2][1]) == 0, "(S1) violated"
    return L, pts

def hittable(L):
    """complete DFS: pick the first unhit list, branch on which option satisfies it."""
    def rec(g):
        pend = None
        for l in L:
            if any(p in g and g[p] == e for (p, e) in l): continue
            if all(p in g for (p, _) in l): return None                     # dead branch
            pend = l; break
        if pend is None: return dict(g)
        for (p, e) in pend:
            if p in g: continue
            g[p] = e
            r = rec(g)
            if r is not None: return r
            del g[p]
        return None
    return rec({})

def sat3(cnf, M):
    return any(all(any(asg[j] == (1 if s else 0) for (j, s) in cl) for cl in cnf)
               for asg in product((0, 1), repeat=M))

for cnf, M in [([((0,True),(1,True),(2,True))], 3),
               ([((0,True),(1,False),(2,True)), ((0,False),(1,True),(2,False))], 3),
               ([tuple((j, bool(b >> j & 1)) for j in range(3)) for b in range(8)], 3)]:
    L, pts = build(cnf, M)
    print(len(L), len(pts), sat3(cnf, M), hittable(L) is not None)
```

**Measurement log.**

```
[B5] Steane  X / Z : |D_c| = [0,0,0] / [0,0,0] ; strong witnesses 48 / 48 ; safe 0 / 0
[B5] rotated X / Z : |D_c| = [16,16,2,2] (reproduces the writeup's "8 of 24 unsafe") ; strong 16 / 16 ; safe 0 / 0
[B5] e_1+e_4+e_7 ∈ L_X (rotated)                              : True
[B5] {4,7} realisable by a locally safe order of its check    : False
[B5] {1}   realisable by a locally safe order of its check    : True
[B1] rotated ⊕ free qubit : n,k,d_X,d_Z = 10, 2, 1, 1 ; d(Q) = 1
[B1] |D_c| both sectors [16,16,2,2] ; safe witnesses 0 / 0  → safely decoupled = True
[B1] strong witnesses 16 / 16  → decoupled = False   (DISAGREES with review §2.3; see §2.4)
[B1] Theorem I(3) test ∀c: D_c ≠ ∅ → True → output YES ; truth NO (d_eff ≤ d(Q) = 1 < 3)
[B1] Cor. I.1′ scan "no v, |v| ≤ 2, in L_X ∪ L_Z"             : 1 witness, v = e_9
[B2] shape (δ=1,h=0) on the witness: Undet True, InStab False → Φ unsatisfiable → NO
[B2] (δ,h) index-pair count at d=3: 3 with h≥1, 6 with h≥0    (still a function of (w,d))
[B3] abstract K₄ under (D)|_S, all 3^4 assignments             : 0 satisfying → NO
[B3] same without (D): forbidden(x,x) is False                 → trivially YES
[B4] sum-zero β-triples over F_2: (0,0,0),(0,ℓ,ℓ)&perms — all contain 0 → dim Log = 1 fragment all-YES
[B4] Prop V.7′ on 3 instances (2 SAT, 1 UNSAT)                 : 3/3 agreement with brute-force 3-SAT
[B4] (S1) assertion on every emitted list                      : 0 violations
```

---

## 8. What this amendment does **not** fix

1. **Nothing is proved.** The label ceiling of the original stands. Corollary I.1′, Lemma III.1′,
   Remark V.6′ and Proposition V.7′ are **CONJECTURED** and have had **no** independent review — they
   are one proposer's response to one reviewer.
2. **Proposition V.7′ does not satisfy (S2)** (§5.3), and I have *not* shown the (S1)+(S2)
   fragment is hard. Indeed §5.3's Observation shows the unary forcing gadgets that the reduction
   needs are impossible under (S2), so the general Island V question is genuinely still open and may
   well be polynomial. What changed is only that (S1) alone no longer tames it.
3. **The `K₄` data is still imported.** Remark V.6′ derives `(D)|_S` from the gadget document's
   "pairwise `≠₃`" report; it does **not** verify that report, the wired code, its `k = 6`, or the
   three shared cosets. Those remain **NOT-REVIEWED**.
4. **The five-family census is only two-thirds recomputed.** §6 recomputes Steane and the rotated
   `[[9,1,3]]` exactly. The unrotated `[[13,1,3]]`, the `3×3` toric code and the quantum Hamming
   `[[15,7,3]]` are quoted from the review's own recomputation and are **not** re-verified here; the
   `56 of 71` random-code figure remains imported and unverified.
5. **The remaining review edits 9 and 11 are not applied.** Edit 9 (record that Lemma II.5's
   hypothesis is poly-time checkable while Theorem II.4's is not, so the poly-time-recognisable
   constant-YES class is the Lemma II.5 class) and edit 11 (exhibit one code satisfying §6.1's
   promise verbatim — weight-4 X-checks, `d_X ≥ 4`, `d_Z = 3` — or relax the promise to what the
   proofs use) are both legitimate and both **left open**: edit 9 is a presentational contrast the
   task did not commission, and edit 11 requires a code search the review itself reports failing
   (`~10^6` random draws, no hit), which is outside this session's box.
6. **Island II is untouched**, as the review confirms it in full (VALUE CONFIRM,
   PRINTED-DERIVATION CONFIRM), except for the two cosmetic elisions the review itself calls
   cosmetic (Theorem II.3's unstated `ΣF ∈ ker H_Z` clause, and Theorem II.4's constant-time gloss).
   Island IV is likewise untouched and is the file's model for the promise-handling that Islands I
   and III were missing.
7. **Lemma 1.4's identification of `d_ext(E(M))` with the mechanism minimum** is asserted, not
   derived, in the original; the review declares it **NOT-REVIEWED**; this amendment does not touch
   it either. It underlies every island equally.
8. **Definition 2.2's quiet extra use of the promise** (review §7: the multiset→set passage from
   hook *indices* to *prefix-sum values* can empty `I_c` when two hook indices coincide in `Q`, and
   the resulting configuration is excluded only by Lemma 1.10, i.e. by the promise; the printed
   justification "multiplicities are irrelevant by Lemma 1.5" is about vectors in `F_2^n`, not
   classes in `Q`) is **not repaired here**. It is harmless under the promise, and Corollary I.1′
   now discharges the promise — but the footnote the review asks for has not been written.
9. **No proof-DAG object was created or modified**, no route was repriced, and no node file was
   touched. §7.1's status table is *recommended* to be amended (§2.5, §5.4); this session did not
   amend the node record.
