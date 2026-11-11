# R12 — independent §7.10 review of the WHGAP LEAN-2 batch (WP-A / WP-B / WP-C)

Reviewer: fresh Opus 5 instance, 2026-07-31.
Commission under review: `channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_LEAN2_20260731.md`.
Executor report under review: `artifacts/whgap_lean2_20260731.md`.
Review commission: R12 (decision layer), rule-7 embeds from
`channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md` §§1–3.

**VERDICT: LICENSE (A).** The LEAN-2 batch is a faithful extension of the licensed
mirror; the three route deviations are sound substitutions (each *strictly stronger*
than the frozen route it replaced, none weaker); the reduced trust boundary is honestly
displayed. **0 MAJOR, 8 minor** (all documentation / record-accuracy / hygiene; none
changes what is proved, none is an over-claim that survives reading the surrounding text).

---

## PRE-ACTION REPORT

* **Target node** `WHGAP.goal`, status on disk **OPEN**
  (`channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.goal.md:7`),
  `lean.state: composition-checked`, `rel: ["P13 unresolved", "hS : S ⊆ [2/5,1/2)"]`.
* **Role: reviewer.** Independence statement: I did not author any part of the LEAN-2
  batch (WP-A, WP-B or WP-C), I did not author the commission, and I was given no
  desired outcome — the licensing menu was presented as two alternatives.
* **Highest status my evidence could license per §2:** this review, being a COMPLETED
  independent fresh-instance review archived on disk, opens the rule-6 completion gate;
  the *statuses themselves* are written by the decision layer / independent checker, not
  by me, and are capped by each node's own imported hypotheses (§7.1: a green build never
  promotes a node by itself).
* **Gates/deliverables** (one line each): reproduce the clean build with true exit status;
  `#print axioms` on every top declaration; forbidden-construct scan; freeze-check;
  `tools/lean_dag_check.py`; special audit of the three route deviations; trust-boundary
  honesty enumeration; satisfiability / vacuity of the two new bridge theorems;
  own-script numerical spot-checks of ≥2 collapse and ≥2 `IcScalar` values.
* **Conflict between commission text and disk protocols: none.** The single-writer
  deviation (no node / index / DAG markdown written by me) is commissioned and noted.
  Anchoring-ban note (7c, disclosed): my statement-vs-paper comparison, my
  Kraus→lift→defect reconstruction and my re-derivation of `a_k`, `b_k` were performed in
  my own script from `paper/main.tex` and the Lean sources; the executor report was a
  mandated input to this commission and was read before those derivations were run, so I
  flag the ordering rather than claiming a blind first pass. No executor script was read
  or re-run (`whgap_lean2_wpa_codegen.py`, `whgap_lean2_wpa_project.py`,
  `whgap_lean2_wpb_check.py`, `whgap_lean2_wpc_check.py` were all left untouched).

---

## 1. Mandatory §7.10 checks — all PASS

| check | command | result |
|---|---|---|
| clean rebuild (WHGAP build outputs only deleted) | `rm -rf .lake/build/lib .lake/build/ir; lake build` | **exit 0**, 3200 jobs, 0 errors, 12 warnings (deprecated `push_neg` ×6, two `all_goals ring` no-ops, two "tactic never executed", one `<;>` lint) — `logs_whgap_lean2_20260731/r12_build.log:233` |
| `#print axioms`, every top declaration | in-build via `WHGAP/Trust.lean` | **146/146**, all `[propext, Classical.choice, Quot.sound]` or a subset (`DefectChoi.E5_symm`: `[propext, Quot.sound]`). Counts reconcile with the report: 82 (WP-A) + 32 (WP-B) + 32 (WP-C) = 146 |
| forbidden constructs | own 13-pattern scan | **0 in code**: `sorry`, `native_decide`, `implemented_by`, `axiom`, `unsafe`, `partial def`, `admit`, `extern` — every hit is prose inside a docstring — `r12_forbidden_scan.txt` |
| frozen Claims | `tools/whgap_lean_freeze_claims.py --check` | **8/8 ok**, exit 0. No Claim changed in this batch, as the commission required |
| §7.6 authoritative gate | `tools/lean_dag_check.py --problem werner-holevo-gap` | **exit 0 — 0 FAIL, 2 WARN, 1 INFO**; the two WARNs are the pre-existing, documented scoped-input exceptions on P4/P6 |
| structure closeout | `tools/proof_dag_check.py --problem werner-holevo-gap` | exit 0, 16 nodes; only the registered `WHGAP/Model.lean` orphan WARNING (M7-F2) |
| literature closeout | `tools/literature_check.py` | exit 0, 51 papers / 5 libraries |
| evidence integrity | own audit of `SHA256SUMS.txt` | **21/21 verify** under the batch's stated LF convention (`r12_sha_audit.txt`) — see minor **m7** |
| source provenance | LF sha256 of the three new/changed modules and the two executor scripts | **all five match the report byte for byte** (`IcScalar.lean` `ef5ea4cb…` 515 lines; `Entropy.lean` `f81ae9ef…` 231 lines; `private-boundary.lean` `d980d990…`; `whgap_lean2_wpb_check.py` `41d8c61f…`; `whgap_lean2_wpc_check.py` `ece5a4c9…`) |

Type audit (7a) performed on every reviewed display; recorded inline in §§2–4 below.
Value-vs-formula status (7f) is stated for every gate. Standing failure modes (7e,
R5 §2) screened item by item; two of them bit **my own first script** and were fixed, not
papered over: **#1** (sympy left `conjugate(sqrt(x))` on the symbolic Kraus prefactors —
repaired by carrying `c0, c1` as positive symbols with an explicit monomial reduction
`c0²→1−x, c1²→x/2, c0c1→β`) and **#7/#8** (my first `to_mp` truncated through Python
`float`, producing spurious ~1e-19 residuals at 60 dps — repaired by a genuine
high-precision conversion; agreement then reached 25+ significant digits). **#5** avoided
throughout by comparing eigenvalue *multisets through characteristic polynomials*, never
by sorting symbolic eigenvalues. **#6**: see m7.

---

## 2. SPECIAL AUDIT (a) — WP-A's `x`-independent factorization replacing PIT

**Own script:** `tools/whgap_r12_wpa_check.py`, log `r12_wpa_crosscheck.txt`, **34/34 gates
PASS**. It reads no executor artifact.

**Type audit.** `Cmat x : Matrix (Fin 27) (Fin 27) ℝ`; row index `(i,b,b') ↦ 9i+3b+b'`,
column index `(j,r,s) ↦ 9j+3r+s` — the packing in `leg1/leg2/leg3` is `I/9`, `I/3 %3`,
`I%3`, consistent with the paper's `ℂ³_A ⊗ (ℂ³_B ⊗ ℂ³_B')` with the input leg first and the
row-major `E_{bb'} ↔ |b⟩|b'⟩` identification. `R5, R3 : Matrix (Fin 27) (Fin 27) ℤ`;
`V5, W5 : 27×5`, `V3 : 27×3`, `E5 : 5×5` over `ℤ`; `toR` is the entrywise `ℤ→ℝ` ring-hom
map, and `toR_mul` is `Matrix.map_mul` — the transport is type-correct and no cast is
dropped. `lam5, lam3 : ℝ → ℝ`. `multiplicity_unique` is a pure scalar lemma over `ℝ`
(`m5, m3 : ℝ`, *not* `ℕ`) — see minor **m6**.

### (i) Is the master formula transcribed correctly? — cross-checked at **15/15** patterns

The mandate asked for ≥5 randomly chosen patterns; I did all fifteen, twice over.

* **Gate C1** — the fifteen delta triples in the Lean `pat` match `eq:master`'s fifteen
  patterns, pattern by pattern, in the table's own order (`15/15`).
* **Gate C2** — the Lean `cco` values match the paper's *forced value* column
  symbolically in `x` (`15/15`).
* **Gate A3** — the paper's *general chart* column specializes at `p = 1/3`,
  `d = 2(1−x)/3` to the forced column (`15/15`), so both displayed columns are mutually
  consistent (a transcription check of the paper against itself).
* **Gate A2 — the strongest check, and one that did not previously exist independently.**
  I rebuilt the 27×27 defect Choi matrix **from the definitions**: Kraus `eq:kraus` →
  complement `eq:comp` (gate A0: the displayed block form equals `Tr(K_a Y K_b^†)`
  symbolically, 16/16 entries; gate A1: `Σ_a K_a Y K_aᵀ = Λ_x(Y)`) → the ansatz `eq:ansatz`
  with the residual `eq:residual` at `p = 1/3`, `d = 2(1−x)/3` → the HS adjoint `J†` as the
  transpose of `J`'s 16×9 superoperator matrix → the defect
  `Δ_J(τ)(Y) = Λ_x(τ)Y − J†(Λ^c_x(τ) J(Y))` → the Choi
  `C_{(i,b,b'),(j,r,s)} = [Δ_J(E_{ij})(E_{rs})]_{b,b'}`.
  This agrees with my transcription of `eq:master` at the forced point on **729/729
  entries, symbolically in `x`**.
  *Value-vs-formula (7f):* this is a FORMULA verification (identity in `x`), by an
  INDEPENDENT construction, not by re-running the proposer's code. It therefore
  independently corroborates the one bridge the report itself declares to be outside
  Lean (WP-A scope item 7). That bridge remains outside Lean; it now has two independent
  sympy witnesses instead of one.

### (ii) Is the 15-coefficient claim `c_k = a_k λ₅ + b_k λ₃` **proved**, or assumed?

**Proved.** Two independent lines of evidence.

* **In Lean.** `Cmat_eq` is `ext I J; simp only [Cmat, R5, R3, A5, A3, …, cco, lam5, lam3];
  push_cast; field_simp; ring`. After `ext`, `I` and `J` are *free variables*, so the
  fifteen `pat k I J` terms are stuck applications and `ring` normalizes with them as
  independent indeterminates. An equality of two linear forms in fifteen independent
  indeterminates closes under `ring` **iff** the coefficients agree one by one. So
  `Cmat_eq` *is* the fifteen-fold statement `c_k(x) = (R5_k/12)λ₅(x) + (R3_k/16)λ₃(x)`,
  proved for every `x ≠ 0`, not sampled and not assumed. (Even if `simp only` unfolds
  `pat` — it does not appear in the simp set — the resulting monomials in the `dl` atoms
  are pairwise distinct, so the conclusion is unchanged.)
* **Independently, by me.** Gate **D1**: for each `k` I solved
  `c_k(x) − a λ₅(x) − b λ₃(x) ≡ 0` as a polynomial identity in `x` for *constant* `a, b`,
  and compared the unique solution against the Lean integer vectors: `a_k = R5_k/12`,
  `b_k = R3_k/16` for all fifteen `k`. Exact match, no free choices.

### (iii) Do the four small decidable certificates really carry the identities?

Traced through the Lean proof term and re-verified numerically. The dependency graph is:

```
V5T_W5, V3T_V3, V5T_V3, V3T_W5   (5×5, 3×3, 5×3, 3×5 `decide`)
W5_eq, E5_symm                   (27×5, 5×5 `decide`)
R5_factor, R3_factor             (729-entry `decide`)
   ⇒ R5_sq, R3_sq, R5_R3, R3_R5, R5_trace, R3_trace, R5_symm, R3_symm
   ⇒ (toR) A5_sq, A3_sq, A5_A3, A3_A5, A5_trace, A3_trace, A5_symm, A3_symm
   ⇒ with Cmat_eq:  annihilator (via triple_zero), trace_Cmat, trace_Cmat_sq, Cmat_symm
```

No 27×27×27 product is ever reduced by the kernel; `R5_trace`/`R3_trace` go through
`Matrix.trace_mul_comm` and the *small* certificates. I re-verified all eight
certificates (gates **E1–E8**) with `R5`, `R3` built from **my own** pattern table — i.e.
the factorizations are certified against an independently constructed target — and then
the algebra they are supposed to imply (**E9–E14**: `R5² = 12R5`, `R3² = 16R3`,
`R5R3 = R3R5 = 0`, `tr = 60/48`, symmetry, `rank = 5/3`). All PASS.

Finally, **F1–F5**: `C_x = (λ₅/12)R5 + (λ₃/16)R3` on 729 entries symbolically in `x`; the
annihilator symbolically; `Tr C = 5λ₅+3λ₃`; `Tr C² = 5λ₅²+3λ₃²`; and both of the paper's
*closed-form* traces `4(1−x)(42x−19)/(3x)` and `16(1−x)²(684x²−636x+151)/(27x²)`.
**F6/F7**: the exact eigenvalue multiset is `{0¹⁹, λ₅⁵, λ₃³}` at `x = 26/51, 4/7, 3/4`
(with the Appendix C eigenvalue column `50/663, 200/221`; `3/7, 20/21`; `2/3, 20/27`
reproduced exactly) and at `x = 49/100` (`λ₅ = −102/1225`, matching the paper's
Theorem 3.3 claim (3) verbatim).

**Deviation verdict (a): SOUND SUBSTITUTION, strictly stronger.** The frozen PIT route
would have produced the identities only via a degree bound plus seven evaluations; the
delivered route proves them for **all** `x ≠ 0` with no `hdeg`, no interpolation lemma and
no sampling, and the abandoned route's cost estimate (one 27×27 `decide` product = 6 m 25 s,
logged in `wpa_pilot_timing.txt`) is a documented, commission-mandated pilot. The
commissioned seven-point verification survives in the weaker but honest form of the three
Appendix C corollaries, and the report says so.

---

## 3. SPECIAL AUDIT (b) — WP-B's three-group split

**Own script:** `tools/whgap_r12_wpbc_check.py`, log `r12_wpbc_crosscheck.txt`,
**43/43 gates PASS**. Own Kraus rebuild throughout; no executor script read.

**Type audit.** `BOut : ℝ→ℝ→Matrix (Fin 3) (Fin 3) ℝ` (B side, 3×3, a *state* after
`BOut_trace`); `blockA, blockB : Matrix (Fin 2) (Fin 2) ℝ`;
`EOut : Matrix (Fin 2 ⊕ Fin 2) (Fin 2 ⊕ Fin 2) ℝ` via `Matrix.fromBlocks` — note the index
type is a **sum type**, not `Fin 4`, so `EOut_offBlock_zero` is stated on `Sum.inl/inr` and
is structurally true; that is disclosed. `β` is a *free real variable* constrained only by
`hβ : β² = x(1−x)/2`, so no `Real.sqrt` enters the identity layer; `Real.sqrt` appears only
from `discE` onward. `IcScalar : ℝ→ℝ→ℝ` is a scalar, defined over two explicit **lists**,
so `List.sum ∘ List.map` — order-independent, no eigenvalue-sorting hazard (failure mode #5
does not apply). `dOne : ℝ→ℝ`.

**Own derivation of the identification layer, before comparing.** With
`ψ = (e₁+ie₂)/√2`, `ρ_ε = (1−ε)P_ψ + εP_ψ̄`: in the orthonormal frame `(ψ, ψ̄, e₃)`,
`ρ_ε = diag(1−ε, ε, 0)` and `ρ_εᵀ = diag(ε, 1−ε, 0)`, so
`Λ_x(ρ_ε) = diag((1−ε)(1−x/2), ε(1−x/2), x/2)` — exactly the Lean `specB` (gate **B1b**,
charpoly comparison, symbolic). On the environment side I computed
`Λ^c(ρ_ε)_{ab} = Tr(K_a ρ_ε K_bᵀ)` directly: the `{0,3}⊔{1,2}` split holds (gate **B1c**,
all eight cross entries zero), the `{0,3}` block has `tr = 1−x/2` and
`det = 2x(1−x)ε(1−ε)` (gate **B1d** — this *is* `blockA_charpoly`), and the `{1,2}` block
has spectrum `{x(1−ε)/2, xε/2}` (gate **B1e**). The Hermitian blocks' off-diagonals are
`∓iβ(1−2ε)` and `∓i(x/4)(1−2ε)`; the real symmetric stand-ins have the same trace and the
same determinant because only `|z|²` enters — the module says exactly this in prose, and
the claim is correct (I checked both sides). Gate **B1f** confirms the Lean `discE` is
literally `tr² − 4 det` of the block I built.

**The sharp bracket `λ₋ ≤ μ_A ε`, re-derived by me.**
`discE = (1−3x/2)² + 2x(1−x)(1−2ε)²` (gate **B1g**, exact SOS ⇒ `discE ≥ 0` for all `ε`,
with only `0 ≤ x ≤ 1` — *better* than the commissioned "on the domain") and
`discE − ((1−x/2)(1−2ε))² = 4ε(1−ε)(1−3x/2)²` (gate **B3a**). The second gives
`√discE ≥ (1−x/2)(1−2ε)`, hence `λ₋ = ((1−x/2) − √discE)/2 ≤ ε(1−x/2)` — the *sharp*
bracket, on `0 ≤ ε ≤ 1` and no constraint on `x`. Then `λ₊ ≥ (1−ε)(1−x/2)` from
`λ₊+λ₋ = 1−x/2`, and `λ₋·(1−ε)(1−x/2) ≤ λ₋λ₊ = 2x(1−x)ε(1−ε)` gives
`λ₋ ≤ μ_A ε` with `μ_A = 2x(1−x)/(1−x/2)`. Gate **B3b**: `(1−x) − μ_A = d₁(x)` exactly.
This is what makes the surviving leading coefficient exactly `d₁` with **no loss**; the
commissioned two-sided `√(a²−b) ∈ [a − b/a, a]` bracket would have been lossy. Confirmed.

**The bare-2 remainder, re-derived by me.** Group split (gate **B4**: an exact
re-association of the seven `negMulLog` terms — no term dropped, none duplicated, which is
precisely `IcScalar_eq` + the three group lemmas):

* `G3 = ε·nml(c) − c·nml(1−ε) ≥ 0` from `nml(1−ε) ≤ ε` (Gibbs) and `nml(c) ≥ c` (needs
  `log c ≤ −1`, i.e. `c = x/2 ≤ e⁻¹`; discharged from `x < 2/5 ⇒ x/2 < 1/5 < 1/3 < e⁻¹`);
* `G2 ≥ 0` from `λ₊ ≥ (1−ε)(1−x/2) ≥ 8/15 > e⁻¹` and antitonicity of `nml` on `[e⁻¹,∞)`;
* `G1 ≥ d₁·nml ε + ε(nml β₁ − nml c − nml μ_A) ≥ d₁·nml ε − 2ε`, using
  `nml(ab) = b·nml a + a·nml b`, `nml β₁ ≥ 0` (`β₁ = 1−x/2 ∈ (4/5,1)`), `nml c ≤ 1`,
  `nml μ_A ≤ 1` (from `nml y ≤ 1 − y`), and `μ_A ≤ 1` (equivalent to `2x² − 5x/2 + 1 ≥ 0`,
  discriminant `< 0`, true for all real `x`).

Remainder constant **2**, exactly as the module claims; the two `e⁻¹` side conditions are
what pins the witness window at `ε ≤ 1/3`, and `1/3 < e⁻¹ < 2/5` is proved from
`Real.exp_one_lt_d9/gt_d9`. The witness `ε(x) = min(1/3, exp(−3/d₁(x)))` then gives
`Ic ≥ 3ε − 2ε = ε > 0`.

**Hypotheses of the main theorem.** Read off the Lean type:

```
theorem exists_eps_IcScalar_pos (x : ℝ) (hx0 : 0 < x) (hx25 : x < 2 / 5) :
    ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧ 0 < IcScalar x ε
```

**`0 < x` and `x < 2/5` and nothing else** — no `hexp`, no `C`, no `ε₀`, no `d`, no
`Real.sqrt` side condition, no implicit typeclass assumption. Every downstream lemma's
side conditions (`x/2 ≤ e⁻¹`, `μ_A ε ≤ e⁻¹`, `(1−ε)β₁ ≥ e⁻¹`, `0 < dOne x`) are
**discharged** from those two, not assumed. I re-confirmed this in Lean by instantiating
the theorem at `x = 1/5` with `by norm_num` and by eta-expanding it at a general `x`
(`r12_satisfiability.lean` §4, compiles). The node-level restatement
`«no-ascent-hierarchy».witness_Ic_pos` carries the same two hypotheses.

**Numerical spot-checks (mandate item 5, ≥2 `IcScalar` values — I did four).** Gate **B2**
computes `Ic = S(Λ_x(ρ_ε)) − S(Λ^c_x(ρ_ε))` from the *numerical Hermitian spectra of my
Kraus-rebuilt matrices* at 60 working digits and compares with the Lean closed form:

| `x` | `ε` | `Ic` (Kraus, independent) | `IcScalar` (Lean closed form) |
|---|---|---|---|
| 1/5 | 1/20 | 0.07363680054888547617634128 | identical to 26 s.f. |
| 3/10 | 1/3 | 0.08272336451194763623950776 | identical to 26 s.f. |
| 1/10 | 1/100 | 0.03682294697783721258974261 | identical to 26 s.f. |
| 9/20 | 1/4 | −0.06867335130983698079494621 | identical to 26 s.f. (sanity: `x > 2/5`, `Ic < 0`) |

Gate **B5a** confirms `d₁·nml ε − 2ε ≤ Ic` at each in-domain point; gate **B5b** confirms
the explicit witness at `x = 1/5, 1/10, 39/100` (at `x = 39/100`, `ε ≈ 1.68e−69` and
`Ic ≈ 4.76e−69 ≥ ε`, at adaptively raised precision).
*Value-vs-formula (7f):* B2/B5 are VALUE checks by an independent construction; the
FORMULA-level content (the group split, the two SOS identities, `d₁`) was verified
symbolically (B1b–B1g, B3a, B3b, B4).

**Deviation verdict (b): SOUND SUBSTITUTION, strictly stronger.** Grouping instead of a
global expansion; two exact algebraic identities instead of the lossy `√(a²−b)` bracket;
`Real.log_le_sub_one_of_pos` instead of concavity machinery. The result is unconditional,
the leading coefficient is sharp, and the remainder constant `2` beats the prose note's
`C(x) = 14/x + 11 + 4log(3/x)` (which blows up as `x→0`). The commissioned intermediate
object does not appear in the tree; the report records this as a substitution, not an
omission, and that record is accurate.

---

## 4. SPECIAL AUDIT (c) — WP-C's rational-similarity payoff path

**Type audit.** `vnEntropy {A : Matrix n n ℝ} (hA : A.IsHermitian) : ℝ` is indexed by the
*symmetry proof*, not by `A` explicitly. Since `Matrix.IsHermitian A` is a `Prop`, Lean's
definitional proof irrelevance makes `vnEntropy` a function of `A` alone; I verified this
in Lean with `example (h1 h2 : (outB α b u).IsHermitian) : vnEntropy h1 = vnEntropy h2 :=
rfl` (`r12_satisfiability.lean` §6, compiles by `rfl`). So no theorem can silently change
which object it is talking about. `outB : ℝ→ℝ→ℝ→Matrix (Fin 3) (Fin 3) ℝ`;
`outE : ℝ→ℝ→ℝ→ℝ→Matrix (Fin 4) (Fin 4) ℝ` (a literal `Fin 4`, *not* a sum type — which is
exactly why the block route is not on the payoff path); `chiB, chiE : ℝ→ℝ→ℝ→ℝ→ℝ` with the
fourth argument `r` standing for `√2`; `f : ℝ→ℝ`; `Delta : ℝ→ℝ`.

**The certificates `U`, `V` (mandate: exact inverses? spectra multisets right?).**

* Gate **C1a**: `V₃U₃ = U₃V₃ = 1` for `U₃ = !![1,0,0; 0,1,1; 0,1,−1]`,
  `V₃ = !![1,0,0; 0,½,½; 0,½,−½]`. **They are exact two-sided inverses** — the Lean lemma
  `vnEntropy_of_conj_diagonal` requires only the one-sided `V*U = 1`, so the hypothesis
  actually used is *weaker* than what holds.
* Gate **C1b**: the same for the 4×4 pair.
* Gates **C1c/C1d**: `U₃ diag(α, b+u, b−u) V₃ = outB α b u` and
  `U₄ diag(a, c, e+w, e−w) V₄ = outE a c e w`, symbolically in all parameters.
* Gates **C1e/C1f**: the eigenvalue **multisets** are right —
  `charpoly(outB) = (λ−α)(λ−b−u)(λ−b+u)` and
  `charpoly(outE) = (λ−a)(λ−c)(λ−e−w)(λ−e+w)`, checked as polynomial identities (no
  ordering assumption, failure mode #5 avoided).

**Own re-derivation of the Lemma 7.1 collapse (7c: before reading `two_point_collapse`).**
For a symmetric two-point ensemble whose two outputs commute with the average and differ
from it only inside one degenerate `2×2` block of common eigenvalue `b`:
`χ = S(ρ̄) − ½S(ρ₊) − ½S(ρ₋)`; the `α` (and, on the E side, the `1−x` and `xε`) eigenvalues
are identical in all three matrices and cancel exactly; what is left is
`−2b log b + (b+u)log(b+u) + (b−u)log(b−u) = (b+u)log((b+u)/b) + (b−u)log((b−u)/b)
= b·f(u/b)`. That is exactly `two_point_collapse`, and its side conditions
`b, b±u ≠ 0` are exactly what `Real.log_div` needs (and are correctly stated as `≠ 0`, not
`> 0`, which is the right strength since `Real.log` is `log|·|`).

**`chiB_collapse` / `chiE_collapse` / `Delta_eq_chi_diff` against paper §7, symbol by symbol.**

| paper §7 | Lean | agree? |
|---|---|---|
| `b = x/2 + (1−3x/2)ε` | `Support.b x ε` | ✓ |
| `u = (t/√2)(1−3x/2)` | `Support.u x t r = t(1−3x/2)/r`, `r = √2` | ✓ |
| `e = (x/2)(1−ε)` | `Support.e x ε` | ✓ |
| `v = tx/(2√2)` | `Support.v x t r = tx/(2r)` | ✓ |
| `ε_c = 2(1−2x)/(2−3x)`, frozen point `ε = t = ε_c/2` | `epsC x / 2` | ✓ |
| `f(s) = (1+s)log(1+s)+(1−s)log(1−s)` | `Support.f` | ✓ |
| `Λ_x(ρ_ε)` has eigenvalues `{α, b, b}`, `Λ_x(ρ_ε±tX)` has `{α, b±u}` | `outB α b 0`, `outB α b (±u)` | ✓ (gate **C0a**) |
| `Λ^c_x(ρ_ε) = diag(1−x, xε, e, e)`, `Λ^c_x(X) = 0 ⊕ (−x/2)X` | `outE (1−x) (xε) e 0`, `outE … (∓v)` | ✓ (gate **C0b**) |
| `eq:chis`: `χ(E,B) = b f(u/b)`, `χ(E,E) = e f(v/e)` | `chiB_collapse`, `chiE_collapse` | ✓ |
| `thm:private`: `u/b = v/e = s* = (1−2x)/(√2(1−x))` at the frozen point | `argument_coincidence` | ✓ (gate **C3a**) |
| `b − e = ε(1−x)`, `Δ(x) = (b−e)f(s*)` | `prefactor_eq`, `Delta_eq_prefactor_mul`, `Delta_eq_chi_diff` | ✓ (gates **C3c/C3d**) |

The **sign convention** (which the report explicitly asked me to check) is right:
`Λ_x(X) = (1−3x/2)X` gives off-diagonal `+u` for `ρ_ε + tX`, whereas
`Λ^c_x(X) = 0 ⊕ (−x/2)X` gives off-diagonal `−v` for the same member — and `chiE` is
written with `−v` first and `+v` second, matching. (Entropy is even in the off-diagonal, so
nothing depends on it; but the convention is nevertheless consistent.) `α` is **the same
for both ensemble members** — `X` lives entirely in the `{1,2}` block — which is what makes
`α` cancel; my gate **C0a** confirms this symbolically, and gate **C3b** confirms
`α(x, ε_c/2) = x`.

`chiB α`-argument check requested by the report: `outB α b 0` really is `Λ_x(ρ̄)` with
`ρ̄ = ρ_ε` (the ensemble average of `ρ_ε ± tX`) — gate **C0a** at `t = 0`. ✓

**Numerical spot-checks (mandate item 5, ≥2 collapse values — I did three pairs).**
Gate **C2**: `χ` computed as `S(avg) − ½S(out₊) − ½S(out₋)` from the *numerical Hermitian
spectra of my Kraus-rebuilt matrices* at 60 digits:

| `x` | `ε` | `t` | `χ(E,B)` from Kraus | vs `b f(u/b)` | `χ(E,E)` from Kraus | vs `e f(v/e)` |
|---|---|---|---|---|---|---|
| 1/5 | 1/10 | 1/20 | 0.003615776960209782268466835 | agree | 0.0001389246334088778106326807 | agree |
| 9/20 | 1/4 | **−1/8** | 0.00269848052293483885245818 | agree | 0.002349205714258768156451031 | agree |
| 2/5 | **3/5** | 1/10 | 0.001819436083847980367939528 | agree | 0.002513186372670750835430013 | agree |

(all to `< 1e−40`; deliberately including `t < 0`, `ε > 1/2` and `x > 2/5`). Gate **C3e**:
`Δ(x) = χ_B − χ_E` at `x = 1/5, 2/5, 49/100` (the last with `Δ ≈ 1.48e−5`), agreeing to
25+ significant digits.
*Value-vs-formula (7f):* C0/C1/C3a–d are FORMULA verifications (symbolic identities);
C2/C3e are VALUE verifications by an independent construction.

**Deviation verdict (c): SOUND SUBSTITUTION.** The commissioned orthogonal-conjugation
lemma **is** delivered (`vnEntropy_conj_orthogonal`) and simply is not used, because the
orthogonal diagonalizer of `!![b,u; u,b]` carries `1/√2`; the substitute
`vnEntropy_of_conj_diagonal` needs only a one-sided rational inverse — a *weaker*
hypothesis with entirely rational certificates. The commissioned block-additivity lemma is
also delivered (`vnEntropy_fromBlocks_add`, `vnEntropy_two_by_two_blocks`) and is honestly
labelled as not load-bearing. Neither deviation weakens anything; both are recorded in the
module's append-only deviation record, and I confirmed the record matches the code.

---

## 5. TRUST-BOUNDARY HONESTY

### (i) Every remaining hypothesis parameter and interface field — enumerated and located

| carrier | parameter | displayed in `Trust.lean`? | comment |
|---|---|---|---|
| `«private-boundary».Delta_lower_bound` | `hsq : ∀ s∈[0,1), s² ≤ f s` | **yes** | formalization gap only (R11 m15); nothing else depends on it |
| `«private-boundary».Claim_of_delta_le` | `hbridge : Δ x ≤ Pone x` | **yes** | retained, general bridge |
| `«private-boundary».Claim_of_devetak` | `hdev : χ_B − χ_E ≤ Pone x` | **yes** | **new**; strictly weaker than `hbridge` — I verified the implication `hdev ⟹ hbridge` is exactly `Delta_eq_chi_diff` and is unconditional on `0<x<1/2` |
| `«no-ascent-hierarchy».exists_pos_of_expansion` | `hexp` | **yes** | retained for the *general* family only; correctly described as no longer needed for the §6 witness |
| `«no-ascent-hierarchy».Claim_of_witness` | `hach` | **yes** | **new**; the achievability reading |
| `«order-boundary».composition` | `hHolds`, `hFails` | **yes** | unchanged |
| `goal.composition` | `h13`, `hS` | **yes** | unchanged; this is why the goal is OPEN |
| `CapacityInterface` | `lsd_devetak`, `zw_hrsf_zero`, `q_pos_of_ic_pos` | **yes**, with citations in `Interface.lean` | unchanged |
| — | `hconj`, `hdeg` | n/a | the two commissioned degradation legs; **neither was needed and neither exists** — confirmed by grep and by reading every new theorem's type |

I searched every new declaration for hypothesis parameters that are *open obligations*
rather than discharged side conditions. The general lemmas of `Entropy.lean`
(`vnEntropy_eq_sum_of_charpoly`, `vnEntropy_of_conj_diagonal`,
`vnEntropy_fromBlocks_add`) carry charpoly/inverse hypotheses that are **discharged at
every use site**; `two_point_collapse`, `chiB_collapse`, `chiE_collapse` carry `≠ 0` side
conditions that are **discharged** by `frozen_B_ne`/`frozen_E_ne` at the witness point, so
`Delta_eq_chi_diff` and `Claim_of_devetak` carry nothing beyond `0 < x < 1/2`. **No
undisclosed hypothesis parameter exists.**

### (ii) Is the README's "what a green build does NOT establish" list complete and current?

Substantially yes — items 1, 3, 6 and 7 were rewritten for LEAN-2 and are accurate; item 3
names the two residuals of `hdev` explicitly and correctly. Two qualifications:

* **The removal of `lem:holevo` from the unchecked list is justified *under the paragraph's
  own stated scope*** ("Displayed scalar content that is **not** checked anywhere here"):
  the displayed identity `eq:chis` *is* now a machine-checked identity between the
  entropies of the displayed matrices. It is **not** justified as a claim about paper
  Lemma 7.1 *as a statement about the channel's ensemble*, because that reading needs the
  identification residual (i). The README does state residual (i) forty lines earlier, in
  item 3, prominently — so the document as a whole is honest — but the sentence in the
  §7.9-governed "What it does mean" paragraph stands unqualified. See minor **m1**.
* The README's "Building" section still points only at `artifacts/logs_whgap_lean_20260730/`
  and dates the build evidence 2026-07-30. See minor **m2**.

### (iii) Does anything imply an original theorem is verified when only the reduced form was checked?

No statement in a **Lean type** does — every `Claim`, every composition and every new
theorem states exactly what it proves, and the three modules' honesty notes are accurate
and specific. Three *prose* statements read stronger than the underlying content when
quoted in isolation, all repaired by adjacent text: the README sentence above (**m1**), the
WP-C report headline "paper Lemma 7.1 (`lem:holevo`) is now machine-checked" / Trust.lean's
"the entropy collapse of paper Lemma 7.1 is now PROVED" (**m1**), and the WP-A report's
"Stretch — DELIVERED" for a stretch whose spectral-theorem half is explicitly *not*
formalized (**m6**). The three commit subjects also use the word "PROVED in Lean" for
work whose node correctly reads `pending-review:` (**m8**).

---

## 6. SATISFIABILITY / VACUITY (§7.10.5)

`WHGAP/Model.lean` still discharges everything it claims — `R11_P2`, `R11_P9`, `R11_P3`,
`R11_P4`, `R11_P13`, `R11_goal`, `R11_goal_conj`, `R11_P6`, `R11_bridge`, `R11_P14` all
build and are axiom-clean in my rebuild — but it was **not extended by LEAN-2**, so the two
NEW bridge theorems shipped without an in-tree inhabitation certificate. I supplied one
out-of-tree: `artifacts/logs_whgap_lean2_20260731/r12_satisfiability.lean`, compiled with
`lake env lean`, **exit 0** (`r12_satisfiability.txt`), all four declarations on the three
standard axioms:

* `r12_hach` — `Claim_of_witness`'s `hach` **is inhabited** in the same model `R11I`
  (`IcLB x c := 0<x ∧ x<2/5 ∧ 0<c`), so `Claim_of_witness` is **not vacuous**;
  `r12_P9_via_witness : «no-ascent-hierarchy».Claim R11I` follows through the new route.
* `r12_hdev` — `Claim_of_devetak`'s `hdev` **is inhabited with equality**, discharged
  *using `Delta_eq_chi_diff` itself*, so `Claim_of_devetak` is **not vacuous**;
  `r12_P14_via_devetak : «private-boundary».Claim R11I` follows.
* Non-triviality of the conclusions: in that model the P14 conclusion unfolds to the
  genuine `0 < Δ(x)` (not `True`), and `χ_B − χ_E > 0` on `(0,1/2)` — both proved in the
  same file. So the collapse theorems are not degenerate (`χ_B` and `χ_E` do not both
  collapse to `0`).
* Also checked there: the WP-B main theorem instantiates at a concrete `x = 1/5` with only
  `by norm_num`, and `trace_Cmat` instantiates at `x = 3/4` with only `x ≠ 0`.

See minor **m3**: this certificate ought to live in `Model.lean`.

---

## 7. Findings

**MAJOR: none.**

**m1 — the `lem:holevo` "now proved" wording is unqualified in three places.**
`lean/README.md:107–109` ("The `lem:holevo` collapse … **is now proved**"), the WP-C report
heading "paper **Lemma 7.1** (`lem:holevo`) is now machine-checked" and Trust.lean's
`Claim_of_devetak` row ("The entropy collapse of paper Lemma 7.1 is now PROVED") all omit,
*in place*, the identification residual (i) that separates the Lean statement (an identity
about hand-posited matrices) from the paper's statement (about the channel's ensemble).
DAG protocol §7.9 governs exactly the paragraph in which the README sentence sits.
**Fix:** append "(as an identity for the displayed matrices; the identification of
`outB`/`outE` with the channel outputs remains outside Lean — item 3(i))" to each of the
three. No content change.

**m2 — node `lean:` metadata and the README build pointer are stale after LEAN-2.**
All four relevant node blocks still read `build: "artifacts/logs_whgap_lean_20260730/"`,
`synced: "2026-07-30"` — a build that contains none of `DefectChoi.lean`,
`IcScalar.lean`, `Entropy.lean`. `WHGAP.private-boundary`'s `composition:` still lists only
`Claim_of_delta_le` (not `Claim_of_devetak`) and its `rel:` still displays the *unreduced*
`hbridge`; `WHGAP.no-ascent-hierarchy`'s `rel:` still displays `hexp` without the WP-B
carve-out. `lean/README.md:155–157` likewise dates the build evidence 2026-07-30.
Direction of the error is **under-claim** for `rel:` (safe) but the `build:` pointer cites
evidence that does not contain the new theorems (rule 1). This is a decision-layer closeout
item — the executors correctly took the single-writer deviation. **Fix at closeout:** set
`build: "artifacts/logs_whgap_lean2_20260731/"`, `synced: "2026-07-31"`, add
`Claim_of_devetak` / `Claim_of_witness`, and restate the two `rel:` lines.

**m3 — the two new bridge theorems ship without an in-tree satisfiability certificate.**
`Model.lean` was not extended (neither WP-B nor WP-C touched it; both reports mention only
`SelfTest.lean`). Both hypotheses *are* satisfiable — I proved it (§6) — but §7.10.5's
vacuity check should ship with the development. **Fix:** fold the four declarations of
`artifacts/logs_whgap_lean2_20260731/r12_satisfiability.lean` into `WHGAP/Model.lean`
(they compile against the tree unchanged) and add them to `Trust.lean`'s `#print axioms`
list.

**m4 — `signed-lift-extension.lean` imports `Support.DefectChoi` but uses nothing from it,
and duplicates `lam5`/`lam3`.** There are now two definitionally identical but formally
unrelated pairs — `WHGAP.DefectChoi.lam5/lam3` and
`WHGAP.«signed-lift-extension».lam5/lam3` — with no linking lemma, and
`lam5_nonneg_iff` / `lam3_nonneg_iff` / `defect_eigenvalues_sign` / the `SelfTest`
examples all reference the *signed-lift* copies. The "serves P2" relation asserted in the
`DefectChoi` docstring and in the WP-A report is therefore currently **nominal**: nothing
in P2 depends on the spectrum core. Not a protocol violation (`Support` is exempt from
§7.6 check 6, and `lean_dag_check` is green), but a real drift hazard: editing one copy
would silently desynchronize the other. **Fix:** either delete the duplicates and have
`«signed-lift-extension»` use `DefectChoi.lam5/lam3` directly, or add two one-line
`rfl`/`unfold` bridging lemmas and route `defect_eigenvalues_sign` through them.

**m5 — `Trust.lean` is billed as "the trust list" but omits the definitional-identification
residuals.** Its framing "Every obligation that could not be closed is an explicit theorem
hypothesis" is not literally true: three obligations are neither closed nor hypothesis
parameters, because they are gaps between a Lean *definition* and its intended referent —
(a) `Cmat x` is the defect Choi matrix of the residual family (WP-A item 7);
(b) `specB`/`specE` are the spectra of `Λ_x(ρ_ε)`/`Λ^c_x(ρ_ε)` (WP-B item 11);
(c) `outB`/`outE` are `Λ_x(ρ_ε±tX)`/`Λ^c_x(ρ_ε±tX)` (WP-C item 17). All three *are* named
in the corresponding module docstrings and in README items 1/3, so nothing is hidden — but
a reader of `Trust.lean` alone would not learn of them. **Fix:** add a short
"definitional-identification residuals" section to `Trust.lean` listing (a)–(c) with
pointers.

**m6 — `multiplicity_unique`'s docstring asserts an unformalized implication; the WP-A
report calls the stretch "DELIVERED".** The docstring says "Together with `annihilator` …
and `Cmat_symm` …, this is exactly the spectrum statement `{0¹⁹, λ₅⁵, λ₃³}`". The step
"real symmetric ⟹ orthogonally diagonalizable with 27 real eigenvalues, so `Tr C = Σλᵢ`
and `Tr C² = Σλᵢ²`" is *not* in Lean (the report's own scope item 10 says so, and the
implication also silently needs `x ∉ {1/3, 1/2, 5/6}`, i.e. it does not cover the
physically decisive point `x = 1/2` at which the paper claims `rank C = 3`). Note also the
type audit point that `m5, m3 : ℝ`, not `ℕ`, so the lemma is an arithmetic statement about
real coefficients rather than about multiplicities as such. Direction: mild over-read, but
self-corrected two paragraphs later in the report and covered by the README's "`eq:charpoly`
… not checked anywhere here". **Fix:** add "— that last step is not formalized here" to the
docstring, and change the report's "Stretch — DELIVERED" to "Stretch — partially delivered
(the multiplicity solve; the spectral-theorem step remains outside Lean)".

**m7 — `SHA256SUMS.txt` is not verifiable with `sha256sum -c` as stored.** The digests are
taken over **LF-normalized** bytes (per the commission's "LF SHA256SUMS"), while the files
themselves are stored with CRLF; a reviewer running the obvious command sees
`10 computed checksums did NOT match`, which reads as an evidence-integrity failure. It is
not one: I re-verified **all 21 rows** under the intended convention and every one matches
(`r12_sha_audit.txt`, `21 verified, 0 bad`). **Fix:** state the normalization in a header
line of `SHA256SUMS.txt`, or record native-byte digests.

**m8 — the three LEAN-2 commit subjects use the completion word "PROVED".**
`8e89b2a` "… PROVED in Lean for ALL x != 0", `2ccda12` "… PROVED in Lean", `38a43eb`
"paper Lemma 7.1 PROVED in Lean". §7.1 is explicit that "`lean-checked` is an evidence
attribute, never a status", and rule 6 caps unreviewed work at NUMERICAL with a
`pending-review:` marker — which the node and the report both do correctly. Git history is
immutable, so this is a note for future commit hygiene, not a repair.

---

## 8. Rule-7 compliance declaration

* **7a type audit** — performed per display; recorded in §§2–4 (including the
  proof-irrelevance point for `vnEntropy` and the `Fin 4` vs `Fin 2 ⊕ Fin 2` point).
* **7b regime-complete gates** — every algebraic identity confirmed either **fully
  symbolically** in the relevant parameters, or at **≥ 3 independent parameter values**;
  the numerical gates deliberately exercise `t < 0`, `ε > 1/2`, `x > 2/5` and `x` near
  `1/2` (`49/100`), i.e. every qualitatively distinct regime including the ones where the
  theorems are *supposed* to stop working (`Ic < 0` at `x = 9/20` reproduced).
* **7c anchoring ban** — own scripts, own Kraus construction, own index packing, own
  transcription of `eq:master` from `main.tex`, own solve for `a_k`, `b_k`; no executor
  script read or re-run. Ordering caveat disclosed in the PRE-ACTION REPORT. My
  `PAT_LEAN` / `PAT_PAPER` tables coincide notationally with the executor's `pat` — that
  coincidence is expected (both transcribe the same displayed table in its own order) and
  is flagged here per 7c; the *values* were nevertheless solved independently.
* **7d frozen-input scope** — I relied only on the R5 §1 conventions and the paper text.
  The P2/P3/P4 reviewed results were **not** leaned on: the one place they would have been
  (that `Cmat` is the defect Choi) I re-derived from scratch instead.
* **7e failure-mode diversity** — R5 §2 screened item by item; #1, #5, #6, #7/#8 all bit or
  were actively avoided, as recorded in §1.
* **7f value-vs-formula** — stated per gate in §§2–4.
* **7g quantifier hygiene** — every term of art in the reviewed statements resolves:
  "forced point" (`p=1/3, d=2(1−x)/3`, `prop:unique`), "frozen point" (`ε=t=ε_c/2`),
  "real symmetric stand-in" (defined in both module docstrings), "achievability reading"
  (`hach`, defined in `Interface.lean` as `IcLB`), "identification step" (README item 3(i)).
  The one term that does **not** resolve to a Lean object — "the defect Choi matrix of the
  residual family" — is exactly the residual named in m5(a).

## 9. Artifacts produced by this review

| file | what |
|---|---|
| `artifacts/whgap_r12_lean2_review_20260731.md` | this report (immutable) |
| `tools/whgap_r12_wpa_check.py` | own WP-A verification (Kraus→lift→defect rebuild; 34 gates) |
| `tools/whgap_r12_wpbc_check.py` | own WP-B/WP-C verification (Kraus rebuild; 43 gates) |
| `artifacts/logs_whgap_lean2_20260731/r12_build.log` | clean rebuild, exit 0, 3200 jobs, 146 `#print axioms` |
| `artifacts/logs_whgap_lean2_20260731/r12_forbidden_scan.txt` | 13-pattern forbidden-construct scan |
| `artifacts/logs_whgap_lean2_20260731/r12_gates.txt` | freeze-check + `lean_dag_check` + `proof_dag_check` + `literature_check` |
| `artifacts/logs_whgap_lean2_20260731/r12_wpa_crosscheck.txt` | WP-A gate log |
| `artifacts/logs_whgap_lean2_20260731/r12_wpbc_crosscheck.txt` | WP-B/WP-C gate log |
| `artifacts/logs_whgap_lean2_20260731/r12_satisfiability.lean` / `.txt` | §7.10.5 vacuity certificate for `Claim_of_witness` and `Claim_of_devetak`, `lake env lean` exit 0 |
| `artifacts/logs_whgap_lean2_20260731/r12_sha_audit.txt` | 21/21 evidence rows verified under the LF convention |

`SHA256SUMS.txt` extended **additively** with `r12_*` rows; no pre-existing row touched.

---

## 10. Licensing statement

**(A)** — *the LEAN-2 batch is a faithful extension of the licensed mirror; the three
deviations are sound substitutions; the reduced trust boundary is honestly displayed.*

Scope of the license: the build reproduces at exit 0 with 146/146 axiom-clean top
declarations and zero forbidden constructs; the three WP-A identities hold for every
`x ≠ 0` and I re-derived their entire input chain from the paper's own definitions,
including the 729-entry bridge that Lean does not contain; the WP-B main theorem's
hypotheses are exactly `0 < x < 2/5` and its analytic chain is sharp and correct; the WP-C
payoff reproduces paper Lemma 7.1 as an identity for the displayed matrices, with the
identification of those matrices with the channel outputs the one named residual (which I
also re-derived symbolically in `(x, ε, t)` from the Kraus set). Neither new bridge theorem
is vacuous. The eight minors are documentation, record-accuracy and hygiene items to be
applied at closeout; none of them changes what is proved, and none is required for this
license.

Per §7.1 and the README's own scope clause, this license makes the LEAN-2 build
citable evidence at the rule-6 gate; it does **not** by itself move `WHGAP.goal`, which
stays **OPEN** on `P13`, and it does not upgrade any node above what its own imported
hypotheses allow.

