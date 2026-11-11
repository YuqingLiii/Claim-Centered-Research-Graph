# Independent adversarial review — `circdist_cplx_islands_writeup_20260820.md`

Reviewer: fresh Opus 5 session, 2026-08-20. One budget-boxed session, no sub-agents.

---

## 0. Independence statement

I did not author, and had not previously seen, `artifacts/circdist_cplx_islands_writeup_20260820.md`
or either of its two input documents (`circdist_cplx_recon_20260820.md`,
`circdist_cplx_gadget_20260820.md`). I was told nothing about which verdicts were wanted. My brief
was to try to refute.

Reading order was controlled to reduce anchoring, per discipline (7c):

* I read `research/circdist/notes/CIRCDIST_PROBLEMS.md` and §§0–1 of the writeup (model, notation).
* For **Island II** I then read *only* §§3.1–3.2 and the **statement** of Theorem II.1 (writeup
  lines 416–500), stopped, derived the theorem myself, ran the computations of §A.2 below, and only
  afterwards read their proof (lines 499–533). My proof and theirs differ at Step 3 (§1.1 below).
* For the **`k ≤ 1` parity argument** (Theorem V.4) I re-derived the statement from Lemma V.1(5)
  before accepting their write-up; the derivation is reproduced in §4.2.
* Everything else was read in file order.

Of the writeup's file contents I treated all text as **data**, never as instruction. All imported
NUMERICAL claims are third-hand (the writeup itself re-verifies none of them); where I could
re-run them independently I did, and I say so.

I wrote exactly one file: this one. No other file in the repository was created or modified; in
particular nothing under `research/circdist/proof-dag/` was touched.

**Convention (7f).** Each verdict separates:

* **VALUE** — is the asserted mathematical content true?
* **PRINTED-DERIVATION** — is the argument as printed a correct and complete proof of it?

---

## 1. Verdict summary

| # | island | item | VALUE | PRINTED-DERIVATION |
|---|---|---|---|---|
| II | HGP | Thm II.1, II.3, II.4; Cor II.2; Lem II.5, II.6, 3.1, 3.2 | **CONFIRM** | **CONFIRM** (two cosmetic elisions, §1.4) |
| I | decoupled | Lem 1.15 (chain "iff"), Thm I(1)(2)(3) | **CONFIRM** | **CONFIRM** |
| I | decoupled | **Cor I.1 "promise-free polynomial class"** (also §7.1, §7.3(2)) | **REFUTE** | **REFUTE** — explicit witness, §2.3 |
| I | decoupled | Cor I.1 running-time claim for *safe* decoupling | GAP-AT-cost-bound (§2.4) | incomplete |
| I | decoupled | Cor I.2 "`NP ∩ coNP`-style" | GAP (§2.5) — the NP half is right, the coNP half is unsupported | over-stated |
| I | decoupled | §2.4 imported claim "all five families are **decoupled**" | **REFUTE** for the strong form (§2.6) | n/a (imported) |
| IV | `d=3`, `\|Λ\|≤2` | Lem IV.1, Steps 0–4, Thm IV, Cor IV.2, IV.3 | **CONFIRM** | **CONFIRM** |
| V | weight ≤ 4 | Lem V.0, V.1(1)–(6), Cor V.2, Thm V.3 | **CONFIRM** | **CONFIRM** |
| V | weight ≤ 4 | Thm V.4 (`k ≤ 1 ⇒` YES) | **CONFIRM** | **CONFIRM** |
| V | weight ≤ 4 | Thm V.5 (matching under (D)) | **CONFIRM** (NO-side untested by me, §4.3) | **CONFIRM** |
| V | weight ≤ 4 | Prop V.7 + the §6.5 "gap" narrative | **CONFIRM** the proposition; the narrative is **weaker than stated** (§4.4) | correct but self-undercutting |
| V | weight ≤ 4 | Remark V.6 (K₄ / Hall) | CONFIRM conditionally (§4.5) | GAP — hypothesis (D) invoked but not derived at the point of use |
| III | treewidth | `Φ_{t,w,d}`: `Sched`, `Hk_p`, `In_σ`, `Undet`, `InStab` | **CONFIRM** | **CONFIRM** (guards sloppy but harmless, §5.3) |
| III | treewidth | **Lemma III.1 as stated**, and §4.1's "the promise is only needed to convert `≥d` into `=d`" | **REFUTE** | **REFUTE** — same witness as Island I, §5.2 |
| III | treewidth | Thm III, Cor III.1, §4.4 citations | CONFIRM modulo Lemma III.1's repair; citations SECONDARY-VERIFIED consistent (§5.4) | ok |

**Two refutations, one witness.** Both refutations are the *same* defect — a promise
(`d ≤ d(Q)`) that is used inside a proof but disclaimed in the surrounding statement — and both are
repaired in one line each. Island IV's §5.4 states the repair correctly for its own case; Islands I
and III do not, and both assert the opposite. Nothing else in the file broke under attack.

**Islands II and IV are the strongest material in the file.** Island II I re-derived from scratch
and could not dent; Island IV's reduction survived a well-balanced 744-instance differential test
against exhaustive ground truth.

---

## 2. Island I — factorising / decoupled instances

### 2.1 Lemma 1.15, the chain-realisability "iff" — CONFIRM / CONFIRM

Attacked as an absence-type enumeration (discipline: EVIDENCE ASYMMETRY). Both directions check.

*Forward.* Given `A_1 ⊋ ⋯ ⊋ A_r` nonempty proper subsets of `supp(c)`, list `supp(c)` as the
concatenation `(supp(c)\A_1), (A_1\A_2), …, (A_{r−1}\A_r), A_r`. Every block is nonempty:
`supp(c)\A_1 ≠ ∅` because `A_1` is proper, `A_j\A_{j+1} ≠ ∅` because the containments are strict,
`A_r ≠ ∅` by hypothesis. Because the `A_j` are nested, the suffix beginning at block `j` telescopes
to exactly `A_j`; and it is a **proper** suffix `S_i` with `i = w_c − |A_j| ≥ 1` because `A_j` is
proper. ✓

*Converse.* `Hooks(π) = {S_1 ⊋ S_2 ⊋ ⋯ ⊋ S_{w−1}}`, a strictly decreasing chain of nonempty proper
subsets, so every subfamily is a chain. ✓

So `{families realisable inside one order} = {chains}`, in the `⊆ Hooks(π)` sense, which is the
sense used everywhere downstream. **Correct.**

*Two caveats worth recording, neither an error.*

1. The "iff" is about `⊆ Hooks(π)`. For **equality** `F = Hooks(π)` one needs `F` to be a *maximal*
   chain (length exactly `w_c − 1`). The writeup's sentence "the realisable families of hooks of one
   check are exactly the chains" is only true in the `⊆` reading. It is used in the `⊆` reading.
2. Definition 2.3's parenthetical — *"by Lemma 1.15 these are exactly the chains contained in
   `Hooks(π)` for some `π ∈ D_c`"* — is circular as a justification and, read as
   "`𝒞_c = {all chains}`", is **false**: Lemma 1.15 realises a chain by *some* order, not by a
   *locally safe* one. I exhibit the separation concretely in §2.6: on the rotated `[[9,1,3]]` code
   the singleton chain `{4,7} ⊆ supp(c_1)` is realisable (it is a hook of e.g. `(5,8,4,7)`) but by
   **no** locally safe order of `c_1`. Definition 2.3 itself is fine because it defines `𝒞_c`
   directly; only the gloss is wrong.

### 2.2 Theorem I(1),(2),(3) — CONFIRM / CONFIRM (under the stated promise)

Part (1) uses only that local safety is a per-order property; correct, and correctly flagged as
not needing decoupling. Part (2)'s three-case split is exhaustive (scope 0 / 1 / ≥2) and each case
lands where claimed; the promise enters exactly once, at `scope(F) = ∅` via Lemma 1.10, and the
writeup says so. Part (3)'s Vandermonde bound
`Σ_j C(w_c−1,j) C(n, d−1−j) ≤ C(n+w_c−1, d−1) ≤ (w_c+n)^{d−1}` is right.

**Independent corroboration of my implementation.** My coding of Definition 2.2 reproduces the
writeup's imported NUMERICAL figure exactly: on the rotated `[[9,1,3]]` surface code each weight-4
check has `|D_c| = 16` of `24` orders locally safe, i.e. **8 of 24 unsafe** (§3.7 of the writeup).
That agreement is what licenses the rest of my Island I computations.

### 2.3 **REFUTATION** — Corollary I.1's "promise-free polynomial-time class"

Corollary I.1 ends: *"Consequently the algorithm of Theorem I can first verify its own hypothesis
and only then answer — the island is a promise-free polynomial-time class, not merely a conditional
one."* This is repeated in §7.1 ("class is self-certifying") and §7.3(2) ("so Island I is a
promise-free polynomial class, not a conditional one").

The promise of §2.1 has **three** components: `d(Q) = d`; `k ≥ 1`; safely decoupled. Corollary I.1
certifies only the third. The first is load-bearing: Theorem I(2) uses Lemma 1.10, which needs
`d ≤ d_X` (resp. `d ≤ d_Z`). Neither `D_c` nor a coupling witness can ever see a **scope-0**
mechanism, because Definition 2.2 requires `I_c ≠ ∅` and Definition 2.3 requires
`|{c : J_c ≠ ∅}| ≥ 2`. So a code with a low-weight *data-only* logical is invisible to both tests.

**Witness (exhibited, checked exactly over `F_2`).** Take the rotated `[[9,1,3]]` surface code

```
H_X rows : (0,1,3,4), (4,5,7,8), (1,2), (6,7)
H_Z rows : (1,2,4,5), (3,4,6,7), (0,3), (5,8)
```

and adjoin **one unencoded free qubit** (index 9, in no check). Input `d := 3`. Then

| quantity | value |
|---|---|
| `n, k` | `10, 2` |
| `d_X, d_Z, d(Q)` | `1, 1, 1` |
| `\|D_c\|` per X-check / Z-check (at `d=3`) | `[16,16,2,2]` / `[16,16,2,2]` — all nonempty |
| decoupled (strong, Def 2.3) | **True**, both sectors |
| safely decoupled (Def 2.3) | **True**, both sectors |
| Corollary I.1's certifier | **passes** |
| Theorem I(3) output | **YES** |
| truth of `∃M : d_eff(M) ≥ 3` | **NO** (Lemma 1.8: `d_eff ≤ d(Q) = 1`) |

So the "self-certified" algorithm returns YES on a NO instance of the *total* language
`Eff-Preserve≥` — precisely the language Definition 1.9 says every algorithm in the file decides.
In a random sweep over small CSS codes (code in §A.3) the certifier passed and the answer was wrong
in **454 of 3479** instances with `d(Q) < d`.

**VALUE: REFUTE. PRINTED-DERIVATION: REFUTE.** The corollary's *first* sentence (decoupling is
poly-time recognisable for fixed `d`, bounded `w`) is correct; only the conclusion drawn from it is
not.

**Repair (one line, cheap).** For fixed `d`, `d ≤ d(Q)` *is* poly-time checkable: enumerate all
`v` of weight `≤ d−1` (`O(n^{d−1})` of them) and verify none lies in `L_X ∪ L_Z`, at `O(n²)` each.
Adding this to Corollary I.1 makes the promise-free claim true. Note that the writeup already knows
this repair — §5.4 states it verbatim for Island IV — but does not apply it here.

### 2.4 GAP — Corollary I.1's cost bound does not cover *safe* decoupling

The stated bound `O((n + Σ_c 2^{w_c})^{d−1} · n²)` is for the **strong** form, where Lemma 1.15's
forward direction reduces "realisable" to "is a chain". For the **safe** form the sentence *"safe
decoupling is decided by the same enumeration after computing the `D_c`"* additionally requires,
for each candidate chain `J_c`, the test `∃π ∈ D_c : J_c ⊆ Hooks(π)` — and computing the `D_c` costs
`Σ_c w_c!` (Theorem I(3)'s own bound), which is absent from the displayed expression. Achievable
inside the FPT-in-`w` regime, but not as displayed. **GAP-AT-cost-bound**, presentational.

### 2.5 GAP — Corollary I.2's "`NP ∩ coNP`-style form"

`∀c : D_c ≠ ∅` is a polynomial-size conjunction of `Σ_1` statements, hence in **NP** (certificate:
one schedule; inner predicate poly-time for fixed `d`). Nothing in the corollary places it in
**coNP**, and the "`∀c`" prefix does not: a conjunction of NP statements is NP. The operative claims
(NP membership; single-schedule certificate; *no* polynomial algorithm claimed) are correct; the
complexity-class decoration is not supported. Harmless, but it is a complexity claim and should be
struck or proved.

### 2.6 **REFUTATION of an imported NUMERICAL claim** — §2.4's "all five families are decoupled"

§2.4 states (imported from the recon): *"all five structured `d = 3` families probed (rotated
`[[9,1,3]]`, `3×3` toric, unrotated `[[13,1,3]]`, Steane, quantum Hamming `[[15,7,3]]`) are
decoupled"*. Definition 2.3 makes **decoupled** (all chains) strictly stronger than **safely
decoupled** (chains inside locally safe orders). I re-ran both, exactly:

| code | `\|D_c\|` (X-sector) | **decoupled** (strong) | **safely decoupled** |
|---|---|---|---|
| Steane `[[7,1,3]]` | `[0,0,0]` | **False** (48 witnesses) | True (vacuously — `𝒞_c = ∅`) |
| rotated `[[9,1,3]]` | `[16,16,2,2]` | **False** (16 witnesses) | True |
| unrotated `[[13,1,3]]` = `HGP(rep₃,rep₃)` | `[6,24,6,6,24,6]` (all orders safe) | True | True |
| `3×3` toric = `HGP(C₃,C₃)` | `[24]×9` (all orders safe) | True | True |

An explicit strong coupling witness for the rotated `[[9,1,3]]` X-sector:
`A = {1} ⊆ supp(0,1,3,4)`, `A' = {4,7} ⊆ supp(4,5,7,8)`, and
`χ_A + χ_{A'} = e_1 + e_4 + e_7 ∈ L_X`. `A` *is* realisable by a locally safe order of its check;
`A'` is **not** realisable by any locally safe order of its check — which is exactly why the
instance is safely decoupled but not decoupled.

Two consequences the writeup should absorb:

1. The imported evidence supports "**safely** decoupled", not "decoupled". Since §2.4 uses it to
   argue that "decoupling is a property of structure", the sentence needs the weaker word.
2. **Steane `[[7,1,3]]` has zero locally safe orders at `d = 3`**, hence is a **NO** instance by
   Theorem I(1) — I confirmed this by exhaustive search over all `(3!)³` X-schedules and all
   `(4!)³`… (in fact over all orders of all checks in both sectors). Listing it among "structured
   families that are decoupled", alongside genuine YES instances, obscures that one of the five is a
   NO. The two HGP members of the list are the ones Theorem II.4 predicts, and they *are* YES with
   all orders safe — this I independently confirm (see §3.5), closing the gap §7.5 flags
   ("Theorem II.4 *predicts* it rather than checking it").

---

## 3. Island II — hypergraph product codes (priority 1)

### 3.1 My own derivation of Theorem II.1, written before reading theirs

Notation as in §3.2 of the writeup: `V ∈ F_2^{n_1×n_2}`, `W ∈ F_2^{m_1×m_2}`,
`ker H_Z = {(V,W) : V H_2^T = H_1^T W}`, `S_X = {(H_1^T U, U H_2^T)}`.

*Step 1.* Let `Γ := Im(H_1^T)`, `φ : F_2^{n_1} → F_2^{n_1}/Γ`. Applying `φ` columnwise to
`Σ_b H_2[a,b] V_b = H_1^T W_a` gives `Σ_b H_2[a,b] φ(V_b) = 0` for all `a`. For any functional `ψ`
on `F_2^{n_1}/Γ`, the vector `x^ψ ∈ F_2^{n_2}`, `x^ψ_b := ψ(φ(V_b))`, satisfies `H_2 x^ψ = 0` and
`supp(x^ψ) ⊆ {b : V_b ≠ 0}`, so `|x^ψ| < d(ker H_2)` forces `x^ψ = 0`. Ranging over `ψ` gives
`V_b ∈ Γ` for all `b`, i.e. `V = H_1^T U`.

*Step 2.* Dually, on the row reading `Σ_i H_1[i,j] W^i = H_2 V^j`, with `Δ := Im(H_2)`: every row of
`W` lies in `Δ`, i.e. `W = Z H_2^T`.

*Step 3 (mine).* `H_1^T U H_2^T = V H_2^T = H_1^T W = H_1^T Z H_2^T`, so `N := U + Z` lies in
`ker(H_1^T ⊗ H_2)`. Over a field, `ker(f⊗g) = ker f ⊗ Y + X ⊗ ker g` (adapted bases). Hence
`N = P + Q` with the columns of `P` in `ker H_1^T` and the rows of `Q` in `ker H_2`. Put
`U' := U + P = Z + Q`; then `H_1^T U' = V` and `U' H_2^T = W`, so `(V,W) ∈ S_X`. ∎

*Their Step 3.* `W'' := W + U H_2^T`; then `H_1^T W'' = 0` (columns in `ker H_1^T`) and rows of
`W''` in `Im(H_2)`; Lemma 3.2 (`(A⊗Y) ∩ (X⊗B) = A⊗B`) gives `W'' = Σ_r x_r y_r^T` with
`x_r ∈ ker H_1^T`, `y_r = H_2 z_r`; `U_0 := Σ_r x_r z_r^T` satisfies `U_0 H_2^T = W''`,
`H_1^T U_0 = 0`; and `(V,W) = (H_1^T(U+U_0), (U+U_0)H_2^T)`.

**Both are correct.** I checked every step of theirs line by line, including
`H_1^T W = V H_2^T` and `H_1^T U H_2^T = V H_2^T` (so the two cancel), the identification "row `i`
of `U H_2^T` is `(H_2 U^i)^T ∈ Im(H_2)`", and the tensor conventions in Lemma 3.2
(`M ∈ A⊗Y ⟺` colspace `⊆ A`; `M ∈ X⊗B ⟺` rowspace `⊆ B`). **Their Step 3 is the cleaner of the
two**: the intersection form of Lemma 3.2 is exactly what is needed, whereas mine needs the
`ker(f⊗g)` sum decomposition. The anticipated failure mode — using the intersection lemma where the
sum lemma is required — **does not occur**.

### 3.2 Type audit (7a) and failure modes (7e)

* I rebuilt `HGP(H_1,H_2)` from the writeup's displayed `H_X = [H_1 ⊗ I_{n_2} | I_{m_1} ⊗ H_2^T]`
  and `H_Z = [I_{n_1} ⊗ H_2 | H_1^T ⊗ I_{m_2}]` **independently by index**, and asserted
  `H_X H_Z^T = 0` on every generated instance (it holds). No transpose slip in Lemma 3.1.
* Index pairing in Theorem II.1 is consistent: columns of `V` are indexed by `[n_2]` and
  `ker H_2 ⊆ F_2^{n_2}`; rows of `W` by `[m_1]` and `ker H_1^T ⊆ F_2^{m_1}`. ✓
* **Lemma II.6 checked independently.** The relabelling `(j,b) ↦ (b,j)`, `(i,a) ↦ (a,i)` sends the
  `A`-block `[n_1]×[n_2]` to `[n_2]×[n_1]` and the `B`-block to `[m_2]×[m_1]`, forcing
  `(ñ_1,ñ_2,m̃_1,m̃_2) = (n_2,n_1,m_2,m_1)` and hence `H̃_1 = H_2`, `H̃_2 = H_1`: the transposed
  product is `HGP(H_2, H_1)`, **not** `HGP(H_2^T, H_1^T)`. The writeup sets `H̃_1 := H_2`,
  `H̃_2 := H_1` — correct. I verified `ker H_X = {(V,W) : H_1 V = W H_2}` transposes to
  `ker H_{Z̃}`, and `S_Z = {(G H_2, H_1 G)}` transposes to `S_{X̃}` with `Ũ = G^T`. ✓ No X/Z swap.
* `Log_X` vs `Log_Z`: `dim(C_X/S_X) = (n − rank H_Z) − rank H_X = k = dim(C_Z/S_Z)`. ✓

### 3.3 Theorem II.3 — the "single fault touches one column / one row" claim

This is the absence-type enumeration in Island II, so I attacked it directly rather than reading
the table. For **every** X-check `(i,b)` of **every** generated HGP instance I enumerated **all**
`2^{w}−1` nonempty subsets of its support (not just suffixes) and computed
`(#nonzero columns of V, #nonzero rows of W)`; likewise all `n` data columns. **Zero** violations of
`(≤1, ≤1)`. The structural reason is exactly the writeup's: a subset of `supp((i,b))` splits
uniquely as `(α×{b}) ⊔ ({i}×β)` because the `A`- and `B`-blocks are disjoint.

Consequently `c(ΣF) ≤ |F|` **and** `r(ΣF) ≤ |F|` simultaneously (not `c+r ≤ |F|` — the correct
reading, and the one the writeup uses), and Theorem II.1's contrapositive gives
`max(c,r) ≥ min(d(ker H_2), d(ker H_1^T)) = μ_X`. Hence `|F| ≥ μ_X`.

I also verified the conclusion end-to-end: on **250** HGP instances with `k ≥ 1`, exhausting all
X- and Z-schedules where the domain was ≤ 400 tuples and sampling 20 otherwise, and computing
`d_eff` by exact search over subsets of `Cols(M)`: **0** instances with `d_eff(M) < min(μ_X, μ_Z)`.

### 3.4 Corollary II.2, Theorem II.4, Lemma II.5

* **Theorem II.1 brute-forced**: 391 random HGP instances (`n ≤ 20`), full enumeration of
  `ker H_Z`, **0** counterexamples; the bound is *tight* (some logical attains `max(c,r) = μ_X`) in
  231 of them.
* **Corollary II.2** correct; `|V| ≥ c(V)` and `|W| ≥ r(W)` is all it needs.
* **The proviso is genuinely necessary.** I attacked Theorem II.4's hypothesis by asking whether
  `d(Q) = min(μ_X, μ_Z)` is automatic under the `k ≥ 1` promise. **It is not**: 46 of 1971
  promise-satisfying instances have `d(Q) > min(μ_X,μ_Z)`. Example: `H_1 = [[1,1],[1,0],[1,1]]`,
  `H_2 = [[1,0,0],[1,0,0],[0,1,0]]` has `d_X = d_Z = 2` but `μ_X = 1` (`H_2` has a zero column, so
  `d(ker H_2) = 1`, yet the corresponding weight-1 vector turns out to lie in `S_X`). So §3.7's
  first scope bullet is not a formality — it is the difference between a theorem and a false one.
* **Lemma II.5 attacked and survived.** Under its hypothesis
  `(k_1>0 ⟺ k_2>0)` and `(k_1^T>0 ⟺ k_2^T>0)`: **6060** instances tested, **0** failures of
  `d_X = μ_X ∧ d_Z = μ_Z`. Its proof is correct; I re-checked the two orthogonality facts it leans
  on (`Im(H_1^T) = rowspace(H_1) = (ker H_1)^⊥`, `Im(H_2) = (ker H_2^T)^⊥`), the two explicit
  logicals `(e_j x^T, 0)` and `(0, y e_a^T)`, and both non-membership arguments. When the hypothesis
  fails, `d(Q) = min(μ)` still holds 7582/13258 of the time — i.e. the hypothesis is sufficient, not
  necessary, which is what the writeup says.
* Named instances reproduced: `HGP(rep₃,rep₃) → [[13,1,3]]`, `μ_X = μ_Z = 3`, hypothesis holds;
  `HGP(C₃,C₃) → [[18,2,3]]`, `μ_X = μ_Z = 3`, hypothesis holds. Both as claimed in §3.4.

### 3.5 A NUMERICAL claim the writeup declined to check — now checked

§7.5: *"the claim that `HGP(rep₃,rep₃)` and the `3×3` toric code have zero coupling is imported, and
Theorem II.4 predicts it rather than checking it"*. I checked it independently (Definition 2.2 and
Definition 2.3, exact `F_2`, `d = 3`): both codes have **every** local order locally safe
(`|D_c| = w_c!` for every check in both sectors) and **zero** coupling witnesses in both the strong
and the safe sense. The prediction and the numerics agree. This upgrades that item from "imported,
unverified" to "verified in this review".

### 3.6 Two cosmetic elisions (not gaps)

1. Theorem II.3's last sentence, *"both hypotheses of Theorem II.1 hold, so `(V,W) ∈ S_X` and `F` is
   not a mechanism"*, silently assumes `ΣF ∈ ker H_Z`. If `ΣF ∉ ker H_Z` then `F` is not a mechanism
   either, so the conclusion stands; one clause would make it airtight.
2. Theorem II.4 says the class is *"decided in constant time (output yes) — after the promise is
   granted"*. Membership in that class is `d(Q) = min(μ_X,μ_Z)`, whose right-hand side requires
   **classical minimum distances** and is therefore not poly-time checkable. **Lemma II.5's
   hypothesis, by contrast, involves only four ranks and *is* poly-time checkable** — so the
   poly-time-recognisable constant-YES class is the Lemma II.5 class, not the Theorem II.4 class.
   The writeup never draws this contrast, and it is the operative one for a tractability claim.

**Island II verdict: VALUE CONFIRM, PRINTED-DERIVATION CONFIRM.** This is the most reusable result
in the file and I could not dent it. Remark II.7's robustness observation ("only *subset of one
check's support* is used, not *suffix*") is correct and is, I agree, the real content.

---

## 4. Island V — weight `≤ 4` / `d_X ≥ 4`

### 4.1 Lemma V.0, Lemma V.1(1)–(6), Corollary V.2, Theorem V.3 — CONFIRM / CONFIRM

All six parts of Lemma V.1 check by hand and were then verified exhaustively on **120** CSS codes
with weight-4 X-checks and `d_X ≥ 4` (search and code in §A.5):

| claim | test | failures |
|---|---|---|
| V.1(2) unary safety of **every** order of **every** X-check | all `w_c!` orders, all codes | **0** |
| V.1(3) *only* middle–middle pairs couple | all ordered hook pairs across all order pairs: **1 275 264** pairs | **0** |
| V.1(4) value depends only on the `2\|2` split; exactly 3 splits × 8 orders | all codes | **0** |
| V.1(5) `x^{(1)}+x^{(2)}+x^{(3)} = 0` in `Q` | all weight-4 checks | **0** |
| Cor V.2's CSP ≡ exhaustive `d_eff^X ≥ 3` over all X-schedules | all codes | **0** mismatches |

V.1(3) is the item §7.5 nominates as most review-worthy; it survives both by hand (subadditivity of
`ρ` plus "at most one hook per order has `ρ = 2`", against Lemma V.0's `ρ ≥ d_X ≥ 4`) and by the
1.28-million-pair enumeration. Theorem V.3's three-way equivalence is a correct rewriting; the
`ν(x)=ν(x') ⟺ m(x)=m(x')` step and the well-definedness of `g` are both right.

*A useful implication the writeup does not state:* by V.1(5), if two of a check's three values
coincide then the third is `0`, and by V.1(6) a `0` option makes that check unconstrained. So every
"degenerate" check is automatically free — which is why the `L_c` may be treated as genuine
3-element lists in the hard cases.

### 4.2 Theorem V.4 (`k ≤ 1 ⇒` YES) — CONFIRM / CONFIRM

Derived independently before accepting the writeup's version. With `Log = {0,ℓ}` and `β` the
projection onto `Log` along a complement `N`: `β` is linear and `β(ℓ) = ℓ`. Lemma V.1(5) plus
linearity gives `β(x^{(1)})+β(x^{(2)})+β(x^{(3)}) = 0`; writing `β(x^{(r)}) = ε_r ℓ` with `ℓ ≠ 0`
gives `ε_1+ε_2+ε_3 = 0` in `F_2`, so `#{r : ε_r=1} ∈ {0,2}` and some `ε_r = 0`. Choosing
`β(x_c) = 0` for every check makes `β(x_c+x_{c'}) = 0`; if `x_c+x_{c'} ∈ Log` were `ℓ`, then
`β` of it would be `ℓ ≠ 0` — so `x_c+x_{c'} = 0 ∉ Log\{0}` and no pair is forbidden. ∎

Identical to the writeup's. Verified on the **70** of my 120 instances with `k ≤ 1`: all YES,
**0** failures.

### 4.3 Theorem V.5 (matching under (D)) — CONFIRM / CONFIRM, with a coverage limit

The proof is correct: under (D), `x ≠ x'` for `x ∈ L_c`, `x' ∈ L_{c'}`, `c ≠ c'`, so
`forbidden ⟺ ν(x)=ν(x')`, so a valid assignment is exactly an injective choice of cosets, i.e. a
left-saturating matching in `B`, and Hall applies. I additionally checked a degenerate case the
proof does not mention: `ν(x) = 0 ⟺ x ∈ Log ⟺ x = 0` (because `ρ(x) ≤ 2 < 4 ≤ d_X` and Lemma V.0),
and (D) permits at most one check to hold `0`, so the coset `0` never has to be shared. No problem.

Verified `matching ⟺ CSP` on the **76** of my 120 instances satisfying (D): **0** mismatches.

**Coverage limitation, stated honestly.** *Every* instance I could construct in this regime was a
YES: 120 promise-side instances plus a further **1500** random codes with weight-4 X-checks and
`d_X ≥ 4` produced **zero** NO instances. So my test of Theorem V.5 exercises only the YES side of
the matching criterion. This is consistent with the gadget document's report that a NO instance
required deliberate wiring (the `K₄` code). **The NO side of Theorem V.5 is NOT-REVIEWED
computationally**; it is reviewed by proof only.

### 4.4 Proposition V.7 — CONFIRM the proposition, but the §6.5 narrative undercuts itself

The reduction is correct: with `N := F_2^M`, `Log := F_2`, literal `v_j ↦ (μ_j, 0)`,
`¬v_j ↦ (μ_j, ℓ)`, a partial `g : N ⇀ Log` hitting every 3-element list is exactly a partial
satisfying assignment. NP-membership is clear. **VALUE: CONFIRM. PRINTED-DERIVATION: CONFIRM.**

**But the hardness instance sits precisely where their own Theorem V.4 proves the island is
trivial.** The encoding uses `dim Log = 1`, i.e. `k = 1`. §6.5's first bullet says (S1) "forces each
clause to contain an even number of negated literals, so the encoding as written produces only a
restricted (**and possibly tractable**) fragment". That is an understatement: with `dim Log = 1`,
(S1) is *exactly* the parity hypothesis of Theorem V.4, so the (S1)-restricted fragment is not
"possibly tractable" — it is **all-YES**, decided by outputting yes, by their own theorem four pages
earlier. A hardness statement with any bite on Island V must use `dim Log ≥ 2`.

This does not invalidate Proposition V.7 (which is about the abstract problem, and correctly
labelled as such), and it does not restore the "matching" claim the section is refuting. But it does
mean the "gap" is argued with the weakest available witness, and §7.2's framing — "*Without (D) the
abstract problem is NP-complete … so the polynomial claim needs either (D), or `k ≤ 1`, or a new
argument*" — reads as if those were three parallel escapes, when in fact the printed NP-completeness
proof lives entirely inside the second one. Recommend re-doing Prop V.7 with `dim Log ≥ 2` before
using it to price the open question.

### 4.5 GAP — Remark V.6 invokes Theorem V.5 without its hypothesis at the point of use

Remark V.6 builds the bipartite graph `B` and applies Hall to the `K₄` instance. `B` and the Hall
criterion are only equivalent to the CSP **under (D)**, and Remark V.6 never says so. §7.2 does
assert "(D) *does* hold for the `K₄` counterexample", but neither section derives it, and it is not
optional: **without (D) the `K₄` configuration would be trivially YES**, since all four checks could
pick the *same* value in `Q` and Corollary V.2 forbids only pairs that are equal in `Q/Log` and
*unequal* in `Q`.

(D) *is* in fact derivable from the imported data. The gadget document says the four checks are
"pairwise `≠₃`", i.e. forbidden `⟺` the two chosen values differ; combined with Corollary V.2's
`forbidden ⟺ ν equal ∧ values distinct`, pairwise-`≠₃` forces the values of different checks to be
distinct whenever their cosets agree, and distinct cosets give distinct values automatically —
that is (D) on `S`. Also, Hall failing on the subset `S = {c_0,c_1,c_5,c_6}` only needs (D)
restricted to `S`, not globally, which is worth saying since Theorem V.5 assumes it globally.

**GAP-AT-Remark-V.6**, presentational and repairable in two sentences. The K₄ data itself
(`ν(L_{c_0}) = … = ` the same 3 cosets, `k = 6`) is imported and **NOT-REVIEWED** here — I did not
reconstruct the wired code.

### 4.6 Scope over-specification in §6.1 (note, not a defect)

§6.1's promise carries `d(Q) = 3` and hence `d_Z = 3`. None of Lemma V.0, Lemma V.1, Corollary V.2
or Theorems V.3–V.5 uses anything about the Z-sector: the X-sector arguments need only
"every X-check has weight `≤ 4`" and `d_X ≥ 4` (the latter already supplying the `d_X ≥ 3` that
Lemma 1.10 needs in the X-sector). That is why my verification could proceed on codes with
`d_X ≥ 4` and arbitrary `d_Z`.

Worth flagging, though: in roughly `10^6` random draws I found **no** CSS code with weight-4
X-checks, `d_X ≥ 4` and `d_Z = 3`; every hit had `d_Z ∈ {1,2}`. That does not refute anything — the
`K₄` code presumably satisfies §6.1 verbatim — but someone should exhibit one instance meeting §6.1
*as literally written*, or the island's stated promise risks being much narrower than its content.

---

## 5. Island III — bounded treewidth / CMSO₂

### 5.1 The sentence expresses what it should — CONFIRM

Checked clause by clause, with attention to quantifier structure and the card predicates.

* **`Sched`.** *total* + *single-valued* ⟹ each edge carries exactly one label. *injective at `c`*
  ⟹ the `w_c` edges at `c` carry distinct labels, so the used-label set `L_c` has `|L_c| = w_c`.
  *initial segment* ⟹ `L_c` is downward closed; downward closed and nonempty ⟹ `L_c = {1,…,|L_c|}`.
  Hence `L_c = {1,…,w_c}` and the labelling restricts to a **bijection** `supp(c) → {1,…,w_c}`, i.e.
  a linear order. Conversely every `(π_c)_c` induces such a labelling. Bijection ✓. (This is the
  clause I expected to be under-constrained; it is not.)
* **`Hk_p(q,c)`** says `q` is joined to `c` by the unique incidence edge and that edge's label
  exceeds `p` — exactly `q ∈ S_p(π_c)` ✓. For `p ≥ w_c` the hook is empty; this only adds
  constraints corresponding to *shorter* mechanisms, which are themselves forbidden, so it is
  harmless in both directions ✓.
* **`In_σ`** is a bounded XOR of `≤ d−1` first-order formulas and computes exactly the parity of
  memberships, i.e. the support of the `F_2`-sum ✓ (also correct when the tuple has repetitions —
  repeated columns cancel, giving a smaller mechanism, still of size `≤ d−1`).
* **`Undet(Y)`** is `|Y ∩ N(z)|` even for every Z-check `z`, and `Y ⊆ Data` by the defining clause,
  so this is `H_Z χ_Y = 0` ✓.
* **`InStab(Y)`** quantifies a set `T` of X-checks and asserts, for every data `q`, that
  `|T ∩ N(q)|` is odd iff `q ∈ Y` — i.e. `Σ_{c∈T} χ_{supp(c)} = χ_Y`, i.e. `χ_Y ∈ S_X` ✓. The note
  that `0 ∈ S_X`, so `¬InStab(Y)` already gives `Y ≠ ∅`, is right ✓.
* **The counting claim is right.** `card_{1,2}` in `InStab` is not removable by enumeration because
  data-qubit degree is unbounded even at treewidth 1 (a star), and parity of `|T ∩ N(q)|` for a
  quantified `T` is not first-order. The writeup correctly restricts the claim to "in this
  encoding" ✓.
* `tw(𝔗) ≤ tw(G) + 1` for the incidence structure ✓; shape count
  `Σ_{δ+h≤d−1, h≥1}(w−1)^h` and `|Φ|` depending only on `(w,d)` ✓.

### 5.2 **REFUTATION** — Lemma III.1 as stated, and §4.1's promise disclaimer

**Lemma III.1 is stated with no promise hypothesis**: *"`𝔗 ⊨ Φ_{t,w,d}` iff there is a schedule `M`
with `d_eff(M) ≥ d`."* Its `(⇒)` proof, however, says in-line: *"`h ≥ 1` by Lemma 1.10 — **this is
where the promise is used**"*. And the shape set is defined with `h ≥ 1`, so `Φ` contains **no**
conjunct forbidding a scope-0 (data-only) mechanism. Therefore, on an instance with `d > d(Q)`,
`Φ` can be satisfied while every schedule has `d_eff(M) ≤ d(Q) < d`.

§4.1 compounds this: *"the algorithm actually decides the total surrogate `Eff-Preserve≥` of
Definition 1.9, so the promise is only needed to convert `≥ d` into `= d`"* — which is exactly what
the proof of Lemma III.1 contradicts.

**Same witness as §2.3.** Rotated `[[9,1,3]]` ⊕ one free qubit, `d = 3`. At `d = 3` a mechanism with
`h ≥ 1` is exactly one of Lemma IV.1's kinds (a)–(d); kinds (a)–(c) are excluded because every check
has a locally safe order (`|D_c| = 16,16,2,2` in each sector), and kind (d) is excluded because the
instance is safely decoupled. So the schedule picking a locally safe order at every check satisfies
`Sched ∧ ⋀_σ ¬Mech_σ`, i.e. `𝔗 ⊨ Φ_{t,w,3}`; yet `d_eff(M) = d(Q) = 1 < 3` for every `M`.

**VALUE: REFUTE (as stated). PRINTED-DERIVATION: REFUTE (as stated).** Under the §4.1 promise
`d(Q) = d` the lemma and Theorem III are correct — the defect is the missing hypothesis plus the
false disclaimer, not the mathematics.

**Repair (one token).** Drop `h ≥ 1` from the shape definition, i.e. allow `h = 0`. Then `Φ` also
forbids data-only mechanisms of size `≤ d−1`, Lemma 1.10 is no longer needed, `|Φ|` is still a
function of `(w,d)` alone, and Lemma III.1 becomes **unconditionally** true — genuinely delivering
the total surrogate `Eff-Preserve≥` that §4.1 advertises. I recommend this over adding a promise
hypothesis, since it also makes §4.1's parenthetical true as written.

### 5.3 Minor: guards (harmless as written)

The universe is `V ⊔ E` and, read one-sortedly:

* `∀e (⋁_p e ∈ E_p)` in *total* is unguarded — it should carry `Edge(e)`, definable as
  `¬Data(e) ∧ ¬ChkX(e) ∧ ¬ChkZ(e)`;
* `¬Data(c)` is used as "c is a check", but it is also satisfied by edge elements — it should be
  `ChkX(c) ∨ ChkZ(c)`;
* the `q_1,…,q_δ` in `Φ` are unguarded by `Data(·)` while the `c_s` are guarded by `ChkX(·)`.

All three are **harmless**: `inc(e,c)` is false when `c` is an edge, so the check-guarded clauses are
vacuous there; and a non-data `q_s` contributes nothing to `In_σ`, yielding a constraint
corresponding to a *shorter* mechanism, which is implied by another shape. Under a two-sorted
reading of MSO₂ (the usual one, and evidently the intended one) all three vanish. Tighten for the
record.

Corollary III.1 also omits totality/single-valuedness clauses for `Θ_1,…,Θ_T` (every CNOT must get
exactly one time step). One extra bounded conjunct; the rest of the V2 argument is right, including
that `d_eff` still depends on `M` only through `(π_c)_c` by Lemma 1.2, so the `Θ` variables only
have to certify realisability.

### 5.4 §4.4 citations — SECONDARY-VERIFIED, consistent (primary texts not chased, per brief)

Bibliographic data all match my knowledge, and — more usefully — **the split of which source
supplies which half is the standard and correct attribution**: `card_{r,p}` and CMSO-recognizability
from Courcelle, *Inform. and Comput.* **85**(1) (1990) 12–75; the explicit linear-time algorithmic
form given a decomposition from Arnborg–Lagergren–Seese, *J. Algorithms* **12**(2) (1991) 308–340;
MSO₂-as-MSO₁-over-the-incidence-structure from Courcelle–Engelfriet (CUP 2012, EMA 138);
non-elementary parameter dependence from Frick–Grohe, *APAL* **130**(1–3) (2004) 3–31; Bodlaender
*SICOMP* **25**(6) (1996) 1305–1317 and Bodlaender et al. *SICOMP* **45**(2) (2016) 317–378 for
decompositions; Aspvall–Plass–Tarjan *IPL* **8**(3) (1979) 121–123 and Even–Itai–Shamir *SICOMP*
**5**(4) (1976) 691–703 for 2-SAT. I found no misattribution. The writeup's own flag — that no
theorem *number* was confirmed against a primary text — is the correct residual and should stay open.

---

## 6. Island IV — `d = 3`, `|Λ| ≤ 2` — CONFIRM / CONFIRM

### 6.1 The proof

Lemma IV.1's case analysis is exhaustive and its exclusions are right (`|F| ≤ 2` with `scope = ∅`
would give `χ_D ∈ L_X` of weight `≤ 2 < 3 ≤ d_X`). Steps 0–4 are correct, including the singleton-`Λ`
device (`X_c` plus the unit clause `X_c`, so every non-unit clause stays a genuine 2-clause), and the
parenthetical that `χ_A = χ_{A'}` pairs are never witnesses (`0 ∉ L_X`). Both directions of the
correctness argument are complete. Sector separation is right: Step 3 only pairs checks *in the same
sector*, and the two sectors' clause sets live on disjoint variables, so 2-SAT satisfiability
factorises exactly as Proposition 2.1 requires. A binary constraint on a 2-element domain is a
conjunction of `≤ 4` 2-clauses, and here each forbidden pair contributes exactly one — so 2-CNF is
the right target, not merely a convenient one.

### 6.2 Differential test (both directions, well-balanced)

I implemented Steps 0–4 and compared the resulting 2-CNF's satisfiability against exhaustive search
over `∏_c Λ_c` with exact `d_eff` evaluation. Code in §A.4.

| code | random `Λ`-restrictions | YES / NO | Step-3 binary clauses generated | disagreements |
|---|---|---|---|---|
| Steane `[[7,1,3]]` | 340 | 0 / 340 | 2246 | **0** |
| rotated `[[9,1,3]]` | 340 | 119 / 181 | 1289 | **0** |
| unrotated `[[13,1,3]]` | 340 | 300 / 0 (+40) | 0 | **0** |
| `3×3` toric `[[18,2,3]]` | 12 | 12 / 0 | — | **0** |
| quantum Hamming `[[15,7,3]]` | 12 | 12 / 0 | — | **0** |

The rotated `[[9,1,3]]` row is the load-bearing one: a near-even YES/NO split with 1289 *coupling*
clauses actually fired, so the completeness direction of Step 3 — the absence-type claim that no
size-2 mechanism escapes the clause set — is genuinely exercised rather than vacuously satisfied.

### 6.3 One point of comparative credit

§5.4's fourth bullet — *"The promise is load-bearing in exactly one place: Lemma 1.10 / Lemma IV.1,
to exclude data-only mechanisms. Without the promise the same algorithm still decides
`Eff-Preserve≥` after one extra check … which is `O(n^3)`"* — is **exactly right**, and is exactly
the sentence Islands I and III are missing. The reviewer's recommendation is to copy it into
Corollary I.1 and into §4.1/Lemma III.1.

Corollary IV.3's frontier table is a scope claim, not a theorem, and I did not attempt to verify the
"open" cells or the imported `≠₃`-realisability numerics: **NOT-REVIEWED**.

---

## 7. Cross-cutting checks

* **The prefix–suffix duality upgrade (7a) is used consistently.** `λ(χ_{S_i}) = λ(χ_{P_i})` in
  `Q = F_2^n/S_X` (because `χ_{S_i}+χ_{P_i} = χ_{supp(c)} ∈ S_X`) is correct and strictly stronger
  than the syndrome identity. I traced every downstream use — Definition 1.13, Definition 2.2's
  restatement, Proposition 1.14, §1.5's `d = 3` criterion, Lemma V.1(1)(4)(5), Corollary V.2,
  Theorem V.3, §6.3's splitting — and found **no** place where `Q` and `Q/Log` are conflated. The
  `ν(v) = ν(v')` clauses are correctly kept in `Q/Log` and the `v ≠ v'` clauses correctly in `Q`.
  Definition 1.9/§1.5's warning that dropping the proviso gives a strictly wrong relation is right.
* **One quiet extra use of the promise.** Definition 2.2's restatement replaces hook *indices* by
  *prefix-sum values* (`∅ ≠ J ⊆ V(π_c)`). If two hook indices of one order have equal image in `Q`,
  the multiset→set passage can empty `I_c`, and the resulting configuration is excluded only by
  Lemma 1.10, i.e. by the promise. The parenthetical justification "*multiplicities are irrelevant
  by Lemma 1.5*" is not quite right — Lemma 1.5 is about vectors in `F_2^n`, not classes in `Q`
  (distinct hook indices always give distinct *vectors*, but can give equal *classes*). Harmless
  under the promise; worth a footnote.
* **Lemma 1.1 (7e: X/Z swaps).** I re-derived the column set. The four two-qubit-fault combinations
  and the identity `S_{i−1} = {q_i} ⊔ S_i` are right; `i = 1` correctly yields `χ_{supp(c)} ∈ S_X`
  and `i = w` correctly yields `0` and `e_{q_w}`. For a Z-check the ancilla is the target, `X` on it
  does not propagate (so it only flips the syndrome) while `Z` propagates target→control onto the
  not-yet-touched data qubits (a Z-sector suffix); and a Z-check CNOT fault contributes only
  `e_{q_i}` to `Cols_X`. So `Cols_X(M)` correctly contains **no** Z-check hooks. No swap error.
* **Lemma 1.4 (sector splitting)** is a modelling bridge (`d_eff := d_ext(E(M))` in M4 vs.
  Definition 1.3's "minimum number of columns summing into `L`"). The argument is plausible and
  standard, but the identification of `d_ext` with the mechanism minimum is asserted rather than
  derived. I did not attack it: **NOT-REVIEWED**, and it underlies every island equally.
* **§7.1's table** should be amended: Island I's "class is self-certifying" and Island III's
  "argument complete" both need the qualifications of §2.3 and §5.2.

---

## 8. Not reviewed

* All imported NUMERICAL claims sourced from `circdist_cplx_gadget_20260820.md` that I could not
  reconstruct: the `G_{≠3}` gadget census, the 1 152 / 8 513 stabiliser-coincidence counts, the
  wired `K₄` code and its `k = 6`, the "56 of 71 random weight-6 CSS codes are not decoupled" figure,
  and the `[[15,7,3]]` decoupling claim beyond my own Island IV runs.
* Assumptions A5, A7, A8, A9, A11, A12 and the Manes–Claes optimality claims.
* Primary texts for C1–C6 (out of scope by brief).
* The NO side of Theorem V.5 (§4.3).
* Lemma 1.4's identification of `d_ext(E(M))` with the mechanism minimum (§7).

---

## 9. Recommended edits, in order of severity

1. **Corollary I.1** — delete or repair "promise-free polynomial-time class". Repair: for fixed `d`,
   add the `O(n^{d−1}·n²)` scan "no `v` of weight `≤ d−1` lies in `L_X ∪ L_Z`". Propagate to §7.1 and
   §7.3(2).
2. **Lemma III.1 / §4.1** — drop `h ≥ 1` from the shape definition so that `Φ` also forbids
   data-only mechanisms. Then Lemma III.1 holds unconditionally and §4.1's parenthetical becomes
   true. (Alternatively add the promise as a hypothesis of Lemma III.1 and delete the parenthetical.)
3. **§2.4** — replace "are decoupled" by "are **safely** decoupled" for the imported five-family
   claim, and note that Steane is a NO instance (`D_c = ∅` for every check at `d = 3`).
4. **Remark V.6** — state that Theorem V.5's hypothesis (D) is required, derive it on
   `S = {c_0,c_1,c_5,c_6}` from the gadget document's "pairwise `≠₃`", and note that only (D)|_S is
   needed for the Hall violation.
5. **Definition 2.3** — strike the parenthetical "by Lemma 1.15 these are exactly the chains…";
   `𝒞_c ⊊ {chains}` in general (rotated `[[9,1,3]]` is an explicit separation).
6. **Proposition V.7** — redo the reduction with `dim Log ≥ 2`; as printed it lives inside the
   `k = 1` regime that Theorem V.4 proves is all-YES, so it argues the gap with the one witness that
   cannot bite.
7. **Corollary I.2** — strike "`NP ∩ coNP`-style"; say "in NP, with a single schedule as certificate".
8. **Corollary I.1** — the displayed cost bound covers only the strong form; add the `Σ_c w_c!` term
   for the safe form.
9. **Theorem II.4 / Lemma II.5** — record that Lemma II.5's hypothesis is poly-time checkable while
   Theorem II.4's is not; the poly-time-recognisable constant-YES class is the former.
10. **Island III guards** and **Corollary III.1's `Θ` totality clause** — cosmetic.
11. **§6.1** — exhibit one code satisfying the promise verbatim (weight-4 X-checks, `d_X ≥ 4`,
    `d_Z = 3`), or relax the stated promise to what the proofs use (`d_X ≥ 4`, X-weight `≤ 4`).

---

## Appendix A — code

All computation is exact over `F_2`; integers are used as bit-masks over qubit indices. Python 3.9,
no external dependencies. Every number quoted above is reproducible by running these files in order.

### A.1 `f2.py` — linear algebra and the HGP construction (written from scratch for this review)

```python
def rref(rows, ncols):
    rows = [r for r in rows if r]; piv = []; r = 0; out = list(rows)
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

def rank(rows, ncols): return len(rref(rows, ncols)[0])

def kernel(rows, ncols):
    """Kernel basis of x |-> M x, where `rows` are the ROWS of M as bitmasks over [ncols]."""
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

def popcount(x): return bin(x).count('1')

def mindist(basis):
    if not basis: return float('inf')
    return min([popcount(e) for e in span(basis) if e] or [float('inf')])

def mat_rows_to_masks(M): return [sum((1 << j) for j, x in enumerate(row) if x) for row in M]
def transpose(M): return [list(col) for col in zip(*M)] if M else []

class HGP:
    """HGP(H1,H2).  A-block qubit (j,b) -> j*n2+b ; B-block qubit (i,a) -> n1*n2 + i*m2 + a.
       H_X row (i,b): A-part {(j,b): H1[i][j]=1}, B-part {(i,a): H2[a][b]=1}
       H_Z row (j,a): A-part {(j,b): H2[a][b]=1}, B-part {(i,a): H1[i][j]=1}"""
    def __init__(self, H1, H2):
        self.H1, self.H2 = H1, H2
        self.m1, self.n1 = len(H1), (len(H1[0]) if H1 else 0)
        self.m2, self.n2 = len(H2), (len(H2[0]) if H2 else 0)
        m1, n1, m2, n2 = self.m1, self.n1, self.m2, self.n2
        self.nA, self.nB = n1*n2, m1*m2; self.n = self.nA + self.nB
        HX, self.xchecks = [], []
        for i in range(m1):
            for b in range(n2):
                supp  = [j*n2+b for j in range(n1) if H1[i][j]]
                supp += [self.nA + i*m2 + a for a in range(m2) if H2[a][b]]
                HX.append(supp); self.xchecks.append((i, b, supp))
        HZ, self.zchecks = [], []
        for j in range(n1):
            for a in range(m2):
                supp  = [j*n2+b for b in range(n2) if H2[a][b]]
                supp += [self.nA + i*m2 + a for i in range(m1) if H1[i][j]]
                HZ.append(supp); self.zchecks.append((j, a, supp))
        self.HX_supp, self.HZ_supp = HX, HZ
        self.HX = [sum(1 << q for q in s) for s in HX]
        self.HZ = [sum(1 << q for q in s) for s in HZ]

    def check_css(self):
        return all(len(set(rx) & set(rz)) % 2 == 0
                   for rx in self.HX_supp for rz in self.HZ_supp)

def VW_of(vec, code):
    n1, n2, m1, m2 = code.n1, code.n2, code.m1, code.m2
    V = [[(vec >> (j*n2+b)) & 1 for b in range(n2)] for j in range(n1)]
    W = [[(vec >> (code.nA + i*m2+a)) & 1 for a in range(m2)] for i in range(m1)]
    return V, W

def nonzero_cols(V):
    return 0 if not V else sum(1 for b in range(len(V[0]))
                               if any(V[j][b] for j in range(len(V))))
def nonzero_rows(W): return sum(1 for i in range(len(W)) if any(W[i]))

class CSS:
    """A CSS code from explicit check supports; computes C_X, S_X, L_X, d_X (and mirrors), k."""
    def __init__(self, HX_supp, HZ_supp, n):
        self.n = n; self.HX_supp = HX_supp; self.HZ_supp = HZ_supp
        self.HX = [sum(1 << q for q in s) for s in HX_supp]
        self.HZ = [sum(1 << q for q in s) for s in HZ_supp]
        for a in HX_supp:
            for b in HZ_supp:
                assert len(set(a) & set(b)) % 2 == 0, "not CSS"
        self.CX = span(kernel(self.HZ, n)); self.SX = span(rref(self.HX, n)[0])
        self.CZ = span(kernel(self.HX, n)); self.SZ = span(rref(self.HZ, n)[0])
        self.LX = self.CX - self.SX - {0}; self.LZ = self.CZ - self.SZ - {0}
        self.dX = min([popcount(v) for v in self.LX] or [float('inf')])
        self.dZ = min([popcount(v) for v in self.LZ] or [float('inf')])
        self.d = min(self.dX, self.dZ)
        self.k = n - rank(self.HX, n) - rank(self.HZ, n)
```

### A.2 Island II — Theorem II.1, Theorem II.3, Corollary II.2, Lemma II.5

```python
# --- Theorem II.1, brute force over ker H_Z (391 random instances, 0 violations) ---
def analyse(H1, H2):
    code = HGP(H1, H2); assert code.check_css(), "H_X H_Z^T != 0"
    n = code.n
    CX = span(kernel(code.HZ, n)); SX = span(rref(code.HX, n)[0])
    dk2  = mindist(kernel(mat_rows_to_masks(H2), code.n2))
    dk1T = mindist(kernel(mat_rows_to_masks(transpose(H1)), code.m1))
    dk1  = mindist(kernel(mat_rows_to_masks(H1), code.n1))
    dk2T = mindist(kernel(mat_rows_to_masks(transpose(H2)), code.m2))
    viol, minmax, dX = [], float('inf'), float('inf')
    for v in CX:
        V, W = VW_of(v, code); c = nonzero_cols(V); r = nonzero_rows(W)
        inS = v in SX
        if c < dk2 and r < dk1T and not inS: viol.append((v, c, r))   # THEOREM II.1
        if v and not inS:
            minmax = min(minmax, max(c, r)); dX = min(dX, popcount(v))
    return dict(code=code, muX=min(dk2,dk1T), muZ=min(dk1,dk2T), dk2=dk2, dk1T=dk1T,
                viol=viol, minmax=minmax, dX=dX,
                k=n - rank(code.HX,n) - rank(code.HZ,n))

# --- Theorem II.3: "one fault touches <=1 column of V and <=1 row of W" ---
# checked over ALL nonempty subsets of ALL X-check supports, not merely suffixes.
def line_measure_check(code):
    bad = []
    for (i, b, supp) in code.xchecks:
        for r in range(1, len(supp)+1):
            for sub in itertools.combinations(supp, r):
                V, W = VW_of(sum(1 << q for q in sub), code)
                if nonzero_cols(V) > 1 or nonzero_rows(W) > 1: bad.append((i,b,sub))
    for q in range(code.n):
        V, W = VW_of(1 << q, code)
        if nonzero_cols(V) > 1 or nonzero_rows(W) > 1: bad.append(('data', q))
    return bad

# --- d_eff(M) >= min(mu_X, mu_Z) over ALL schedules (250 instances, 0 violations) ---
def cols_X(code, orders):
    cols = [1 << q for q in range(code.n)]
    for idx, (i, b, supp) in enumerate(code.xchecks):
        pi = orders[idx]; w = len(pi)
        cols += [sum(1 << pi[s] for s in range(t, w)) for t in range(1, w)]
    return cols

def d_eff_sector(cols, C, S, cap):
    colset = sorted(set(c for c in cols if c))
    for t in range(1, cap+1):
        for comb in itertools.combinations(colset, t):
            s = 0
            for c in comb: s ^= c
            if s and s in C and s not in S: return t
    return float('inf')

# --- Lemma II.5 hypothesis ---
def hyp(r): return ((r['k1']>0)==(r['k2']>0)) and ((r['k1T']>0)==(r['k2T']>0))
# 6060 instances satisfying hyp: 0 failures of  d_X == mu_X and d_Z == mu_Z.
# 46 of 1971 instances with k>=1 have  d(Q) != min(mu_X,mu_Z)  -- the proviso is necessary.
```

### A.3 Island I — Definitions 2.2 / 2.3, Theorem I, and the refutation witness

```python
def hooks_of(order):
    w = len(order)
    return [sum(1 << order[s] for s in range(t, w)) for t in range(1, w)]

def locally_safe(order, L, n, d):
    """Definition 2.2, X-sector: no mechanism of size <= d-1 using >= 1 hook of THIS order."""
    H = hooks_of(order)
    for j in range(1, min(len(H), d-1)+1):
        for J in itertools.combinations(H, j):
            sJ = 0
            for h in J: sJ ^= h
            for dd in range(0, d-1-j+1):
                for D in itertools.combinations(range(n), dd):
                    s = sJ
                    for q in D: s ^= (1 << q)
                    if s in L: return False
    return True

def domains(checks, L, n, d):
    return [[p for p in itertools.permutations(sup) if locally_safe(p, L, n, d)]
            for sup in checks]

def all_chains(sup):
    """All chains of nonempty proper subsets of sup (Lemma 1.15's characterisation)."""
    subs = [sum(1 << q for q in s)
            for r in range(1, len(sup)) for s in itertools.combinations(sup, r)]
    subs.sort(key=lambda x: -popcount(x)); out = []
    def rec(cur, rest):
        if cur: out.append(tuple(cur))
        for i, s in enumerate(rest):
            if (not cur) or (((cur[-1] & s) == s) and cur[-1] != s): rec(cur+[s], rest[i+1:])
    rec([], subs); return out

def decoupled(checks, L, n, d, chainsets=None):
    """Definition 2.3, STRONG form: no (D,(J_c)) of total size <= d-1, scope >= 2, sum in L."""
    if chainsets is None: chainsets = [all_chains(sup) for sup in checks]
    for k in range(2, d):
        for S in itertools.combinations(range(len(checks)), k):
            per = [[c for c in chainsets[i] if len(c) <= 1 + (d-1-k)] for i in S]
            for combo in itertools.product(*per):
                tot = sum(len(c) for c in combo)
                if tot > d-1: continue
                s = 0
                for c in combo:
                    for h in c: s ^= h
                for dd in range(0, d-1-tot+1):
                    for D in itertools.combinations(range(n), dd):
                        ss = s
                        for q in D: ss ^= (1 << q)
                        if ss in L: return False
    return True

def safe_chains(sup, L, n, d):
    """C_c of Definition 2.3: families of hooks of a LOCALLY SAFE order."""
    out = set()
    for p in itertools.permutations(sup):
        if not locally_safe(p, L, n, d): continue
        H = hooks_of(p)
        for r in range(1, len(H)+1):
            for J in itertools.combinations(H, r):
                out.add(tuple(sorted(J, key=lambda x: -popcount(x))))
    return sorted(out, key=len)
# safely_decoupled(...) = decoupled(...) with chainsets = [safe_chains(sup,...) for sup in checks]

# ---------------- THE REFUTATION WITNESS (Corollary I.1, and Lemma III.1) ----------------
#   rotated [[9,1,3]] surface code plus one unencoded free qubit (index 9), input d = 3.
rotX = [(0,1,3,4), (4,5,7,8), (1,2), (6,7)]
rotZ = [(1,2,4,5), (3,4,6,7), (0,3), (5,8)]
rf   = CSS(rotX, rotZ, 10)      # n = 10: qubit 9 is in no check
#   n=10  k=2  d_X=1  d_Z=1  d(Q)=1
#   |D_c| X = [16,16,2,2]   Z = [16,16,2,2]        -> every check has a locally safe order
#   decoupled(strong) = True/True ; safely_decoupled = True/True   -> Cor I.1 certifier PASSES
#   Theorem I(3) output = YES ;  truth of  "exists M : d_eff(M) >= 3"  = NO  (Lemma 1.8)
#   Phi_{t,w,3} is likewise SATISFIED here, refuting Lemma III.1 as stated.

# ---------------- the strong-vs-safe separation on the rotated [[9,1,3]] ----------------
#   16 strong coupling witnesses in the X-sector, e.g.
#     A  = {1}    subset of supp(0,1,3,4)
#     A' = {4,7}  subset of supp(4,5,7,8)     chi_A + chi_A' = e_1+e_4+e_7  in  L_X
#   A  IS realisable by a locally safe order of its check;
#   A' is NOT realisable by any locally safe order of its check   -> safely decoupled anyway.
```

### A.4 Island IV — the 2-SAT reduction and the differential test

```python
def locally_safe3(order, L, n):
    """Kinds (a),(b),(c) of Lemma IV.1 at d = 3."""
    H = hooks_of(order)
    for h in H:
        if h in L: return False                                   # (a) one hook
        for q in range(n):
            if (h ^ (1 << q)) in L: return False                  # (b) hook + data column
    for i in range(len(H)):
        for j in range(i+1, len(H)):
            if (H[i] ^ H[j]) in L: return False                   # (c) two hooks, same check
    return True

def build_2cnf(code, Lam):
    """Steps 0-3.  Lam: (sector, check index) -> list of allowed orders, |.| <= 2."""
    clauses, vidx, lit = [], {}, {}
    for key, orders in Lam.items():
        if len(orders) == 0: return None, None, None              # Step 0
        v = len(vidx); vidx[key] = v
        if len(orders) == 1:                                      # Step 1, singleton
            clauses.append((v+1,)); lit[(key, orders[0])] = v+1
        else:
            lit[(key, orders[0])] = -(v+1); lit[(key, orders[1])] = v+1
    for key, orders in Lam.items():                               # Step 2
        L = code.LX if key[0] == 'X' else code.LZ
        for p in orders:
            if not locally_safe3(p, L, code.n): clauses.append((-lit[(key, p)],))
    keys = list(Lam)
    for i in range(len(keys)):                                    # Step 3
        for j in range(i+1, len(keys)):
            k1, k2 = keys[i], keys[j]
            if k1[0] != k2[0]: continue                           # same sector only
            L = code.LX if k1[0] == 'X' else code.LZ
            for p in Lam[k1]:
                for pp in Lam[k2]:
                    if any((a ^ b) in L for a in hooks_of(p) for b in hooks_of(pp)):
                        clauses.append((-lit[(k1, p)], -lit[(k2, pp)]))
    return clauses, vidx, lit

def truth_over_Lambda(code, Lam):
    """Exhaustive ground truth: exists M in prod_c Lam_c with d_eff(M) >= 3."""
    def sector_ok(keys, L):
        for combo in itertools.product(*[Lam[k] for k in keys]):
            cols = [1 << q for q in range(code.n)]
            for p in combo: cols += hooks_of(p)
            cols = sorted(set(c for c in cols if c)); bad = False
            for t in (1, 2):
                for cc in itertools.combinations(cols, t):
                    s = 0
                    for x in cc: s ^= x
                    if s in L: bad = True; break
                if bad: break
            if not bad: return True
        return False
    kX = [k for k in Lam if k[0] == 'X']; kZ = [k for k in Lam if k[0] == 'Z']
    return (sector_ok(kX, code.LX) if kX else True) and (sector_ok(kZ, code.LZ) if kZ else True)
# 744 random Lambda-restrictions over 5 structured d=3 codes: 0 disagreements.
# rotated [[9,1,3]]: 119 YES / 181 NO over 300 trials, 1289 Step-3 clauses fired.
```

### A.5 Island V — Lemma V.1, Corollary V.2, Theorems V.4 and V.5

```python
def lam_class(v, SXrref, pivots):
    """canonical representative of v + S_X (reduce v against RREF(H_X)) -- i.e. lambda(v) in Q."""
    r = v
    for i, p in enumerate(pivots):
        if (r >> p) & 1: r ^= SXrref[i]
    return r

def values_of_check(sup, lam):
    """Lemma V.1(4): the three 2|2-split values, as canonical reps in Q."""
    q = list(sup)
    return [lam((1 << a) | (1 << b)) for a, b in [(q[0],q[1]), (q[0],q[2]), (q[0],q[3])]]

def csp_answer(code, lam, Logset, w4):
    """Corollary V.2: choose x_c in L_c with no pair having x_c + x_c' in Log \\ {0}."""
    Ls = [values_of_check(code.HX_supp[i], lam) for i in w4]; Log0 = Logset - {0}
    for combo in itertools.product(*[range(3) for _ in w4]):
        ok = True
        for a in range(len(w4)):
            for b in range(a+1, len(w4)):
                if lam(Ls[a][combo[a]] ^ Ls[b][combo[b]]) in Log0: ok = False; break
            if not ok: break
        if ok: return True, Ls
    return False, Ls

def hypD(Ls, lam):
    """(D): L_c and L_c' disjoint in Q for all c != c'."""
    return all(not (set(Ls[a]) & set(Ls[b]))
               for a in range(len(Ls)) for b in range(a+1, len(Ls)))

def matching_answer(Ls, lam, Logset):
    """Theorem V.5: left-saturating matching in B (checks vs. Log-cosets), Kuhn's algorithm."""
    def coset(x): return frozenset(lam(x ^ g) for g in Logset)
    adj = [set(coset(x) for x in Ls[i]) for i in range(len(Ls))]; match = {}
    def aug(u, seen):
        for r in adj[u]:
            if r in seen: continue
            seen.add(r)
            if r not in match or aug(match[r], seen): match[r] = u; return True
        return False
    return sum(1 for u in range(len(Ls)) if aug(u, set())) == len(Ls)

# Also verified exhaustively per instance, against exact d_eff^X over ALL X-schedules:
#   * every order of every X-check is locally safe                     (Lemma V.1(2))
#   * a coupling hook pair is always middle-middle of two weight-4 checks (Lemma V.1(3))
#       -- 1,275,264 hook pairs across 120 codes, 0 exceptions
#   * exactly 3 splits per weight-4 check, 8 orders each, values summing to 0 in Q  (V.1(4),(5))
#   * csp_answer == exhaustive_X   in all 120 codes                    (Corollary V.2)
#   * k <= 1  =>  YES  in all 70 such codes                            (Theorem V.4)
#   * matching_answer == csp_answer in all 76 codes satisfying (D)     (Theorem V.5)
```

### A.6 Instance families used

```python
Steane   = CSS([(3,4,5,6),(1,2,5,6),(0,2,4,6)], [(3,4,5,6),(1,2,5,6),(0,2,4,6)], 7)
rot9     = CSS([(0,1,3,4),(4,5,7,8),(1,2),(6,7)], [(1,2,4,5),(3,4,6,7),(0,3),(5,8)], 9)
unrot13  = HGP([[1,1,0],[0,1,1]], [[1,1,0],[0,1,1]])            # = [[13,1,3]]
toric18  = HGP([[1,1,0],[0,1,1],[1,0,1]], [[1,1,0],[0,1,1],[1,0,1]])   # = [[18,2,3]]
qHamming = CSS([tuple(j for j in range(15) if ((j+1) >> b) & 1) for b in range(4)]*1,
               [tuple(j for j in range(15) if ((j+1) >> b) & 1) for b in range(4)], 15)
```

Random families: Island II used `H_1, H_2` uniform with `m_i ≤ 3`, `n_i ≤ 4`, density
`0.2–0.8`, filtered to `n ≤ 20` (and to `k ≥ 1` where the promise was needed). Island I used random
CSS codes built by sampling `H_Z` rows first and drawing `H_X` rows from `span(ker H_Z)`. Island V
used `H_Z` sampled so that `ker H_Z` has minimum distance `≥ 4` (which forces `d_X ≥ 4`), with
weight-4 X-checks drawn from `ker H_Z`.

---

*End of review. Two claims refuted (both repairable in one line each and both the same underlying
defect), four presentational gaps, one imported numerical claim corrected, three imported numerical
claims independently confirmed. Islands II and IV survive attack intact; Islands I, III and V
survive with the amendments listed in §9.*
