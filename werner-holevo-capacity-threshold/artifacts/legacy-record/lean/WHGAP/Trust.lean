import WHGAP.goal
import WHGAP.Support.SelfComplement
import WHGAP.Support.Channel
import WHGAP.«order-boundary»
import WHGAP.«private-boundary»
import WHGAP.SelfTest
import WHGAP.Model

/-!
# `WHGAP.Trust` (DAG protocol §7.3, §7.5)

The trust list for this development.

## `sorry` census

**Zero.**  There is no `sorry`, no `axiom` declaration, no `native_decide` and no
`implemented_by` anywhere under `channel-capacity/werner-holevo-gap/proof-dag/lean/WHGAP/`.
Every obligation that could not be closed is an explicit theorem hypothesis:

| where | hypothesis | what it stands for |
|---|---|---|
| `«private-boundary».Claim_of_delta_le` | `hbridge : ∀ x ∈ (0,1/2), Δ x ≤ P^{(1)} x` | the one-shot ensemble/Devetak step, in its ORIGINAL opaque form (retained as the general bridge).  The step `P^{(1)} ≤ P` is *not* hypothesised — it is the cited interface field `lsd_devetak` |
| `«private-boundary».Claim_of_devetak` | `hdev : ∀ x ∈ (0,1/2), χ(E,B) - χ(E,E) ≤ P^{(1)} x` | **LEAN-2 WP-C (2026-07-31): the reduced trust boundary.**  The entropy collapse of paper Lemma 7.1 is now PROVED (`chiB_collapse`, `chiE_collapse`, `Delta_eq_chi_diff`) *(as an identity for the displayed matrices; the identification of `outB`/`outE` with the channel outputs remains outside Lean — README item 3(i), and residual (c) of the "Definitional-identification residuals" section below)*, so this hypothesis is exactly (i) "the explicit matrices `outB`/`outE` are the channel outputs" (sympy gate G1, `tools/whgap_lean2_wpc_check.py`) plus (ii) Devetak's formula for `P^{(1)}`.  Strictly weaker than `hbridge` |
| `«no-ascent-hierarchy».exists_pos_of_expansion` | `hexp` | Lemma 5.1 of the N1' note (the `ε log(1/ε)` expansion with uniform remainder).  **LEAN-2 WP-B (2026-07-31):** no longer needed for the §6 witness family — `«no-ascent-hierarchy».witness_Ic_pos` carries its own proof and has NO hypothesis beyond `0 < x < 2/5`.  `hexp` survives only in the general-family lemma |
| `«no-ascent-hierarchy».Claim_of_witness` | `hach` | the achievability *reading* of the scalar `IcScalar`: that the number computed from the explicit output spectra is an achievable coherent information of `Λ_x`.  This is the missing channel/entropy layer (README scope item 1), not an analytic gap.  **2026-08-01 (LEAN-5 WP-H): REDUCED, not discharged** — the row stays, and the theorem stays exactly as it was, but the *entropy layer* half of what it carried is now in Lean: `«no-ascent-hierarchy».Claim_of_entropy_witness` is the same bridge with the hypothesis `hach'` stated over `S(Λ_x(ρ_ε)) − S(Λ^c_x(ρ_ε))` instead of over the `IcScalar` formula.  See the dated LEAN-5 subsection below for the exact (non-)gain: `hach'` is *equivalent* to `hach`, so the reduction is in what the hypothesis has to be believed **about**, not in its logical strength |
| `«order-boundary».composition` | `hHolds`, `hFails` | the ZW criterion step and the R5b necessity theorem |
| `goal.composition` | `h13`, `hS` | `WHGAP.onset-two-fifths` — CONJECTURED on disk; this is why the goal is OPEN |

### Append-only census removals

* **2026-08-01 (LEAN-3 WP-F) — `«private-boundary».Delta_lower_bound` / `hsq` REMOVED from the
  table above.**  The row read: *"`«private-boundary».Delta_lower_bound` | `hsq : ∀ s ∈ [0,1),
  s² ≤ f s` | elementary inequality, not proved here (see that module's deviation record)"*.
  It is struck because the hypothesis is now the **theorem**
  `WHGAP.«private-boundary».f_ge_sq` (two-level `monotoneOn_of_deriv_nonneg` argument), and
  `Delta_lower_bound` is restated with `0 < x` and `x < 1/2` only.  This is a removal by
  *discharge*, not by re-scoping: the theorem's conclusion is unchanged and no other
  declaration consumed `hsq`.  Nothing was weakened anywhere else in this file.  (Rule: rows
  leave this table only by discharge, and only with a dated note here saying so.)

## Definitional-identification residuals (R12 minor m5, added 2026-07-31)

The `sorry`-census framing above — "every obligation that could not be closed is an explicit
theorem hypothesis" — is true of the *analytic* obligations only.  **Three further obligations
are neither closed nor hypothesis parameters**, because they are gaps between a Lean
*definition* and its intended referent: nothing inside Lean can state them, since the referent
(the channel `Λ_x`, its complement, the signed lift) does not exist in this development at all.
They are named in the corresponding module docstrings and in README items 1 and 3, but a reader
of `Trust.lean` alone would not learn of them, so they are listed here:

| # | Lean definition | intended referent (NOT checked in Lean) | where the identification is discharged instead | pointer |
|---|---|---|---|---|
| (a) | `WHGAP.DefectChoi.Cmat x` | the 27×27 **defect Choi matrix of the residual family** at the forced point `p = 1/3`, `d = 2(1−x)/3` | exact sympy: gate V1 of `tools/whgap_lean2_wpa_codegen.py`, independently re-derived from the Kraus set by the R12 reviewer (`tools/whgap_r12_wpa_check.py`, gate A2, 729/729 entries symbolically in `x`) | README item 1; WP-A report scope item 7 |
| (b) | `WHGAP.Support.specB`, `WHGAP.Support.specE` (and the matrices `BOut`/`EOut` they are read off) | the **spectra of `Λ_x(ρ_ε)` and `Λ^c_x(ρ_ε)`** for the §6 witness family | exact sympy: `tools/whgap_lean2_wpb_check.py`, re-derived by R12 (`tools/whgap_r12_wpbc_check.py`, gates B1b–B1e) | README items 1 and 3; WP-B report scope item 11 |
| (c) | `WHGAP.«private-boundary».outB`, `outE` | the **channel ensemble outputs** `Λ_x(ρ_ε ± tX)` and `Λ^c_x(ρ_ε ± tX)` of the §7 witness ensemble | exact sympy: gate G1 of `tools/whgap_lean2_wpc_check.py`, re-derived by R12 (`tools/whgap_r12_wpbc_check.py`, gates C0a/C0b) | README item 3(i); WP-C report scope item 17 |

### 2026-08-01 (LEAN-3 WP-D) — status of the three residuals

`WHGAP/Support/Channel.lean` now builds the channel itself — the Kraus set
`K₀ = t·1, K_{μ+1} = s·A_μ` with `s² = x/2`, `t² = 1−x`; the Kraus sum (`LamK_eq`, and
`LamK_tp` for trace preservation); the padded complement `(Λ^c(X))_{ab} = Tr(K_a X K_bᵀ)`
(`LamCK_eq`); the forced-point lift of `eq:Jintro` and its HS adjoint (`Jdag_adjoint`); and
the defect superoperator — so two of the three rows above are **discharged inside Lean**:

| # | 2026-08-01 status | the Lean theorem that closes it |
|---|---|---|
| (a) | **CLOSED** | `WHGAP.Support.Channel.choi_defect_eq_Cmat` : `choiOf (Defect x q) = DefectChoi.Cmat x`, all 729 entries, for every `x, q` with `9xq² = 2(1−x)` (the chart `q = (1/3)√(2(1−x)/x) = t/(3s)`, inhabited on `0 < x < 1` by `exists_chart`).  Route: `defect_eq` (nine entry identities, the `s,t` dependence cancelling into rational functions of `q`) plus the fifteen `word_choi` pattern identities |
| (c) | **CLOSED** | `WHGAP.«private-boundary».outB_eq` and `outE_eq` : `Λ_x(ρ_ε + θX) = outB(α, b, u)` and `Λ^c_x(ρ_ε + θX) = outE(1−x, xε, e, −v)` entrywise, for both ensemble signs (`u`, `v` are odd in `θ`: `u_neg`, `v_neg`).  `hdev` therefore no longer carries the identification step — only Devetak's formula for `P^{(1)}` |
| (b) | **STILL OPEN** — unchanged | *not* closed by WP-D.  The §6 witness state `ρ_ε = (1−ε)P_ψ + εP_ψ̄` is genuinely **complex**, and the charpoly identification `charpoly Λ(ρ_ε) = ∏(X − specBᵢ)`, `charpoly Λ^c(ρ_ε) = ∏(X − specEᵢ)` was **verified in exact sympy only** (`tools/whgap_lean3_wpd_check.py`, gates D9a–D9e) and was **not** reached in Lean inside the WP-D budget.  Residual (b) stands exactly as written above |

### 2026-08-01 (LEAN-4 WP-G) — residual (b): CLOSED AT CHARPOLY LEVEL

`WHGAP/Support/Channel.lean` §8 now carries the §6 witness over `ℂ`.  The witness state
`ρ_ε = (1−ε)P_ψ + εP_ψ̄`, `ψ = (e₁ + i e₂)/√2`, is built as a genuinely complex matrix
(`rhoWit`, `Pwit_eq_outer`), both outputs are written out (`LamWit_eq`, `LamCWit_eq`) and
proved Hermitian for real parameters (`LamWit_isHermitian`, `LamCWit_isHermitian`), and:

| what | the Lean theorem |
|---|---|
| B-side charpoly | `Channel.specB_charpoly` : `charpoly (Lam x (rhoWit ε)) = (X − (1−ε)(1−x/2))(X − ε(1−x/2))(X − x/2)`, all `x, ε : ℂ`; in `IcScalar`-list form `Channel.specB_charpoly_list`; for the Kraus sum itself `Channel.specB_charpoly_kraus` |
| E-side charpoly | `Channel.specE_charpoly` : `charpoly (LamC x β (rhoWit ε)) = (X² − (1−x/2)X + 2x(1−x)ε(1−ε))(X − x(1−ε)/2)(X − xε/2)` under `hβ : β² = x(1−x)/2` — **square-root free**, the `λ±` pair kept as the quadratic factor; in `IcScalar`-list form (with `lamP`/`lamM`, hence needing `0 ≤ x ≤ 1`) `Channel.specE_charpoly_list`; for the Kraus-overlap complement `Channel.specE_charpoly_kraus` |

**Residual (b) is REDUCED, not removed, and the remaining glue is named:** *"same
characteristic polynomial ⟹ same `vnEntropy`" is not available for COMPLEX Hermitian
matrices in this development.*  `WHGAP.Support.Entropy` (`vnEntropy`,
`vnEntropy_congr_charpoly`, `vnEntropy_eq_sum_of_charpoly`) is stated for **real
symmetric** matrices over `ℝ` only, and the real-symmetric layer does not apply verbatim to
the complex Hermitian §6 outputs: `Matrix.IsHermitian.eigenvalues` and the
`roots_charpoly_eq_eigenvalues` bridge would have to be re-run over `ℂ`.  So the step from
the two charpolys above to `IcScalar x ε = S(Λ(ρ_ε)) − S(Λ^c(ρ_ε))` is **still outside
Lean**, and `hach` (the achievability reading) is untouched.  What HAS moved: the row (b)
of the table above — "the spectra of `Λ_x(ρ_ε)` and `Λ^c_x(ρ_ε)` are `specB`/`specE`" — is
no longer an exact-sympy-only claim; it is a Lean theorem about the Kraus-built channel,
at characteristic-polynomial granularity.  The sympy gates D9a–D9e and the independent
WP-G gates G0–G13 (`tools/whgap_lean4_wpg_check.py`) remain as cross-checks.

### 2026-08-01 (LEAN-5 WP-H) — residual (b): DISCHARGED

The glue named in the paragraph immediately above — *"same characteristic polynomial ⟹ same
`vnEntropy`" is not available for COMPLEX Hermitian matrices in this development* — now
exists: `WHGAP/Support/EntropyC.lean`.

| what | the Lean theorem |
|---|---|
| the definition over `ℂ` | `Support.vnEntropyC hA = ∑ i, Real.negMulLog (hA.eigenvalues i)` for `A : Matrix n n ℂ`, `hA : A.IsHermitian` — same shape as the real `vnEntropy` (Mathlib's `IsHermitian.eigenvalues` is `RCLike`-generic and real-valued) |
| the multiset bridge | `Support.eigenvaluesC_multiset_eq` (and `…_multiset`, `…_list`): a split charpoly over REAL data pins the eigenvalue **multiset**.  The real layer's `RCLike.ofReal_real_eq_id` rewrite is unavailable over `ℂ`; the `ofReal` layer is stripped by `Multiset.map_injective Complex.ofReal_injective` instead.  No ordering is used anywhere, so repeated eigenvalues need no side condition |
| the workhorse | `Support.vnEntropyC_eq_sum_of_charpoly` (Fin-indexed) and `Support.vnEntropyC_eq_sum_of_charpoly_list` (the literal WP-G shape); `Support.charpolyC_list_length` FORCES the list length (`l.length = Fintype.card n`) *(headline corrected 2026-08-01 per R15 m4: this is a necessary condition — it excludes mismatched lists — NOT a satisfiability statement; genuine non-vacuity is witnessed by the payoff's own two applications, `specB` at `Matrix (Fin 3) (Fin 3) ℂ` and `specE` at `Matrix (Fin 4) (Fin 4) ℂ`, and in-tree by `Model.R15_hach'`/`R15_P9_via_entropy` §3c)* |
| **the payoff** | `Support.IcScalar_eq_vnEntropyC_diff` : for `0 ≤ x ≤ 1` and any `β` with `β² = x(1−x)/2`, `IcScalar x ε = vnEntropyC (Λ_x(ρ_ε)) − vnEntropyC (Λ^c_x(ρ_ε))` — the step that was outside Lean |
| node-level | `«no-ascent-hierarchy».exists_eps_entropy_pos` (quantifier-congruent to `Support.exists_eps_IcScalar_pos`; only the conclusion's quantity differs) and `«no-ascent-hierarchy».Claim_of_entropy_witness` (the `Claim` bridge with the achievability hypothesis stated at the entropy level), tied together by `«no-ascent-hierarchy».entropy_witness_eq_IcScalar` |

**What this does NOT buy — both directions, stated so neither is over- nor under-claimed.**

* Over-claim guard: `hach'` of `Claim_of_entropy_witness` is **not logically weaker** than
  `hach`.  `entropy_witness_eq_IcScalar` proves the two quantities EQUAL on the applied
  range, so the two hypotheses are interchangeable.  The gain is that the *identification*
  "the number `IcScalar x ε` is the von Neumann entropy difference of the two channel
  outputs" is a Lean theorem rather than an exact-sympy gate plus prose.
* Under-claim guard: the passage really is in Lean now, at full identity granularity and
  for the Kraus-built outputs (`specB_charpoly_list`/`specE_charpoly_list` are statements
  about `Lam`/`LamC`, and `specB_charpoly_kraus`/`specE_charpoly_kraus` about `LamK`/`LamCK`
  themselves).  Residual (b) as written in the table above — the spectra identification —
  is **discharged**.
* **The named remainder that `hach'` still carries** is exactly two interface-tier items:
  **(i)** that `LamCK` is *the* complementary channel of `Lam` (a Stinespring/dilation
  statement: this development has a Kraus sum and a matrix of Kraus overlaps, no complete
  positivity, no dilation theory, no channel object), and **(ii)** LSD/Devetak
  achievability — that a strictly positive coherent information at one input lower-bounds
  `Q`.  Both are cited in `WHGAP/Interface.lean` (`q_pos_of_ic_pos`, `lsd_devetak`) and
  neither is touched here.
* `WHGAP.Support.Entropy` (real symmetric) is unchanged and still says what it always said;
  the complex layer is a *sibling*, not a replacement, and the P14 payoff chain still runs
  through the real one.

Pre-verification (exact/high-precision, before any of this Lean was written):
`tools/whgap_lean5_wph_check.py`, gates GH0–GH3, log
`artifacts/logs_whgap_lean5_20260801/wph_sympy_gates.txt` — the identity checked to
`< 1e-35` at six rational `(x, ε)` points against mpmath eigenvalues of the Kraus-built
outputs (an independent construction, DAG rule 7f), including one exactly degenerate point.

**In-tree §7.10.5 satisfiability (added 2026-08-01, R15 m3):** `WHGAP/Model.lean` §3c carries
the R15 reviewer's certificate — `Model.R15_hach'` inhabits `hach'` in the model `R11I`,
`Model.R15_P9_via_entropy` derives the P9 `Claim` through the NEW entropy route, and
`Model.R15_hach_iff_hach'` proves the `hach ↔ hach'` equivalence in both directions for an
arbitrary `CapacityInterface`.  So `Claim_of_entropy_witness` is **not vacuous**.

*(Section boundary, added 2026-08-01 per R15 m2: **the LEAN-5 subsection ends here; the
following paragraphs are the earlier WP-D/R13-era record**, which predates LEAN-5 and was
not authored as part of it.  The LEAN-5 block was inserted above them rather than below, and
the text is left in place rather than moved, per the append-only rule.)*

Two further scope facts about (a) and (c), which the closure does **not** remove:

* `Λ_x` in `Channel.lean` is a **linear map given by a Kraus sum**, not a channel object:
  complete positivity, the Stinespring dilation, the claim that `LamCK` is *the*
  complementary channel, and every capacity remain outside Lean.  Residual (a) being closed
  means `Cmat x` **is** the Choi matrix of `Λ(τ)·(−) − J†(Λ^c(τ)·J(−))`; it does **not**
  mean that PSD-ness of that matrix certifies `Q = P = 0` — that is still the Zhu–Wang
  interface.
* The lift is checked at the **forced point only** (`p = 1/3`, `d = 2(1−x)/3`).

Consequence for reading the table above (as of 2026-08-01, residual (c) discharged):
`Claim_of_devetak` reduces `hbridge` to `hdev`, and what `hdev` still carries — before WP-D it
was residual (c) *plus* the following — is exactly:

1. **Devetak's formula** `P^{(1)} = max over ensembles of [χ(·,B) − χ(·,E)]`, the cited
   external result; and
2. **the validity of the ensemble it is applied to**: that the two members `ρ_ε ± tX` are
   *states* (PSD and trace one) and that they satisfy the `eq:ens` constraint `|t| ≤ √2 ε`.
   Nothing in Lean checks positivity of the inputs — `outB_trace`/`outE_trace` check
   trace-one of the two **averages** only — and `|t| ≤ √2 ε` is nowhere represented in this
   development.  The obligation is discharged in the manuscript and was spot-verified at the
   frozen point `ε = t = ε_c/2`, three `x`, by the R13 reviewer (gate R8d,
   `artifacts/whgap_r13_lean3_review_20260801.md`).

*(Corrected 2026-08-01 by R13 m5: this paragraph previously said `hdev` carries "Devetak's
formula alone", which omitted item 2.)*  The *entropy collapse* half
of paper Lemma 7.1 is proved, **as an identity for the displayed matrices**, and only that.
The same qualification applies to `Claim_of_witness`/`hach` through residual (b), and to the
P2 spectrum core through residual (a).  These three are the "identification steps"; they are
not analytic gaps and no Lean hypothesis parameter can carry them.

*(**Correction 2026-08-01, per R15 m1 — the sentence immediately above is stale and is kept
as history.**  Residual (b) is DISCHARGED (see the dated LEAN-5 subsection above), so it is
no longer what qualifies `Claim_of_witness`/`hach` — nor `Claim_of_entropy_witness`/`hach'`,
which is equivalent to it.  What those two hypotheses still carry is exactly the two
interface-tier items: **(i)** the Stinespring/dilation identification of `LamCK` as *the*
complementary channel of `Lam`, and **(ii)** the LSD/Devetak achievability reading — a
strictly positive coherent information at one input lower-bounds `Q`.  Both are cited fields
of `WHGAP/Interface.lean` (`q_pos_of_ic_pos`, `lsd_devetak`), not residuals of the
spectra-identification table.  The sentence's other two clauses are unaffected: residual (a)
still qualifies the P2 spectrum core in the sense named above, and residual (c)'s
qualification of `hdev` stands as written.)*

## Interface (the real trust boundary)

`WHGAP.CapacityInterface` has three assumption fields — `lsd_devetak`, `zw_hrsf_zero`,
`q_pos_of_ic_pos` — each carrying its citation in `WHGAP/Interface.lean`.  Per §7.9:

> A theorem proved against an abstract interface is exactly as strong as the results that
> interface cites, and not one notch stronger.

## `#print axioms`

Expected output for every declaration below: `[propext, Classical.choice, Quot.sound]`
(or a subset).  Anything else is a G-L2 failure.
-/

namespace WHGAP.Trust

-- Interface
#print axioms WHGAP.CapacityInterface

-- P2 (`WHGAP.signed-lift-extension`)
#print axioms WHGAP.«signed-lift-extension».Claim
#print axioms WHGAP.«signed-lift-extension».forcing_p
#print axioms WHGAP.«signed-lift-extension».forcing_d
#print axioms WHGAP.«signed-lift-extension».lam5_nonneg_iff
#print axioms WHGAP.«signed-lift-extension».lam3_nonneg_iff
#print axioms WHGAP.«signed-lift-extension».defect_eigenvalues_sign

-- Support.Entropy (LEAN-2 WP-C: the minimal real-symmetric von Neumann entropy layer, T3)
#print axioms WHGAP.Support.vnEntropy
#print axioms WHGAP.Support.isHermitian_of_transpose
#print axioms WHGAP.Support.eigenvalues_multiset_eq
#print axioms WHGAP.Support.vnEntropy_eq_sum_of_charpoly
#print axioms WHGAP.Support.vnEntropy_diagonal
#print axioms WHGAP.Support.charpoly_conj
#print axioms WHGAP.Support.vnEntropy_congr_charpoly
#print axioms WHGAP.Support.vnEntropy_conj_orthogonal
#print axioms WHGAP.Support.vnEntropy_of_conj_diagonal
#print axioms WHGAP.Support.diagonal_fin_two
#print axioms WHGAP.Support.diagonal_fin_three
#print axioms WHGAP.Support.diagonal_fin_four
#print axioms WHGAP.Support.vnEntropy_fromBlocks_add
#print axioms WHGAP.Support.vnEntropy_two_by_two_blocks
#print axioms WHGAP.Support.two_point_collapse

-- P14 (`WHGAP.private-boundary`) LEAN-2 WP-C: paper Lemma 7.1 and the reduced bridge
#print axioms WHGAP.«private-boundary».outB
#print axioms WHGAP.«private-boundary».outE
#print axioms WHGAP.«private-boundary».alphaB
#print axioms WHGAP.«private-boundary».outB_isHermitian
#print axioms WHGAP.«private-boundary».outE_isHermitian
#print axioms WHGAP.«private-boundary».outB_trace
#print axioms WHGAP.«private-boundary».outE_trace
#print axioms WHGAP.«private-boundary».vnEntropy_outB
#print axioms WHGAP.«private-boundary».vnEntropy_outE
#print axioms WHGAP.«private-boundary».chiB
#print axioms WHGAP.«private-boundary».chiE
#print axioms WHGAP.«private-boundary».chiB_collapse
#print axioms WHGAP.«private-boundary».chiE_collapse
#print axioms WHGAP.«private-boundary».frozen_B_ne
#print axioms WHGAP.«private-boundary».frozen_E_ne
#print axioms WHGAP.«private-boundary».Delta_eq_chi_diff
#print axioms WHGAP.«private-boundary».Claim_of_devetak

-- Support.DefectChoi (LEAN-2 WP-A: the basis-free core of paper Thm 3.3)
#print axioms WHGAP.DefectChoi.V5T_W5
#print axioms WHGAP.DefectChoi.V3T_V3
#print axioms WHGAP.DefectChoi.V5T_V3
#print axioms WHGAP.DefectChoi.V3T_W5
#print axioms WHGAP.DefectChoi.W5_eq
#print axioms WHGAP.DefectChoi.E5_symm
#print axioms WHGAP.DefectChoi.R5_factor
#print axioms WHGAP.DefectChoi.R3_factor
#print axioms WHGAP.DefectChoi.R5_sq
#print axioms WHGAP.DefectChoi.R3_sq
#print axioms WHGAP.DefectChoi.R5_R3
#print axioms WHGAP.DefectChoi.R3_R5
#print axioms WHGAP.DefectChoi.R5_trace
#print axioms WHGAP.DefectChoi.R3_trace
#print axioms WHGAP.DefectChoi.R5_symm
#print axioms WHGAP.DefectChoi.R3_symm
#print axioms WHGAP.DefectChoi.Cmat_eq
#print axioms WHGAP.DefectChoi.annihilator
#print axioms WHGAP.DefectChoi.trace_Cmat
#print axioms WHGAP.DefectChoi.trace_Cmat_sq
#print axioms WHGAP.DefectChoi.Cmat_symm
#print axioms WHGAP.DefectChoi.multiplicity_unique
#print axioms WHGAP.DefectChoi.lam5_eq_zero_iff
#print axioms WHGAP.DefectChoi.lam3_eq_zero_iff
#print axioms WHGAP.DefectChoi.lam5_eq_lam3_iff
#print axioms WHGAP.DefectChoi.sample_26_51
#print axioms WHGAP.DefectChoi.sample_4_7
#print axioms WHGAP.DefectChoi.sample_3_4

-- Support.DefectChoi (LEAN-3 WP-E: the characteristic polynomial, unconditional)
#print axioms WHGAP.DefectChoi.mapR
#print axioms WHGAP.DefectChoi.mapR_mul
#print axioms WHGAP.DefectChoi.mapR_transpose
#print axioms WHGAP.DefectChoi.mapR_zsmul
#print axioms WHGAP.DefectChoi.mapR_one
#print axioms WHGAP.DefectChoi.cert_V5R_W5R
#print axioms WHGAP.DefectChoi.cert_V3R_V3R
#print axioms WHGAP.DefectChoi.cert_V5R_V3R
#print axioms WHGAP.DefectChoi.cert_V3R_W5R
#print axioms WHGAP.DefectChoi.A5_eq
#print axioms WHGAP.DefectChoi.A3_eq
#print axioms WHGAP.DefectChoi.Fmat
#print axioms WHGAP.DefectChoi.Gmat
#print axioms WHGAP.DefectChoi.Fmat_mul_Gmat
#print axioms WHGAP.DefectChoi.Gmat_mul_Fmat
#print axioms WHGAP.DefectChoi.charpoly_Cmat_of_ne_zero
#print axioms WHGAP.DefectChoi.Cmat_zero
#print axioms WHGAP.DefectChoi.lam5_zero
#print axioms WHGAP.DefectChoi.lam3_zero
#print axioms WHGAP.DefectChoi.charpoly_Cmat
#print axioms WHGAP.DefectChoi.charpoly_sample_26_51
#print axioms WHGAP.DefectChoi.charpoly_sample_4_7
#print axioms WHGAP.DefectChoi.charpoly_sample_3_4
#print axioms WHGAP.DefectChoi.charpoly_half

-- Support.DefectChoi (LEAN-3.2, R13 MAJOR-2: the rank at x = 1/2, NOT an inference from
-- charpoly_half)
#print axioms WHGAP.DefectChoi.Cmat_half_factor
#print axioms WHGAP.DefectChoi.V3R_Cmat_half_V3R
#print axioms WHGAP.DefectChoi.rank_Cmat_half

-- P6 (`WHGAP.order-boundary`)
#print axioms WHGAP.«order-boundary».Claim
#print axioms WHGAP.«order-boundary».gap_identity
#print axioms WHGAP.«order-boundary».gap_neg_below_half
#print axioms WHGAP.«order-boundary».threshold_factorization
#print axioms WHGAP.«order-boundary».strict_violation_window
#print axioms WHGAP.«order-boundary».composition

-- P14 (`WHGAP.private-boundary`) — the flagship
#print axioms WHGAP.«private-boundary».mul_log_gt
#print axioms WHGAP.«private-boundary».f_pos
#print axioms WHGAP.«private-boundary».b_at
#print axioms WHGAP.«private-boundary».e_at
#print axioms WHGAP.«private-boundary».u_at
#print axioms WHGAP.«private-boundary».v_at
#print axioms WHGAP.«private-boundary».argument_coincidence
#print axioms WHGAP.«private-boundary».prefactor_eq
#print axioms WHGAP.«private-boundary».prefactor_pos
#print axioms WHGAP.«private-boundary».sStar_pos
#print axioms WHGAP.«private-boundary».sStar_lt_one
#print axioms WHGAP.«private-boundary».Delta_eq_prefactor_mul
#print axioms WHGAP.«private-boundary».Delta_closed_form_pos
#print axioms WHGAP.«private-boundary».f_ge_sq
#print axioms WHGAP.«private-boundary».Delta_lower_bound
#print axioms WHGAP.«private-boundary».Claim
#print axioms WHGAP.«private-boundary».Claim_of_delta_le

-- P9 (`WHGAP.no-ascent-hierarchy`)
#print axioms WHGAP.«no-ascent-hierarchy».d1_at_two_fifths
#print axioms WHGAP.«no-ascent-hierarchy».d1_sign
#print axioms WHGAP.«no-ascent-hierarchy».exists_pos_of_expansion
#print axioms WHGAP.«no-ascent-hierarchy».blockA_trace_det
#print axioms WHGAP.«no-ascent-hierarchy».Claim
#print axioms WHGAP.«no-ascent-hierarchy».witness_Ic_pos
#print axioms WHGAP.«no-ascent-hierarchy».witness_Ic_lower_bound
#print axioms WHGAP.«no-ascent-hierarchy».Claim_of_witness

-- Support.SelfComplement (LEAN-3 WP-F: paper Lemma 4.1, the x = 1 self-complementarity display)
#print axioms WHGAP.Support.SelfComplement.A_transpose
#print axioms WHGAP.Support.SelfComplement.lamCmin_apply
#print axioms WHGAP.Support.SelfComplement.lamCmin_eq_lamOne
#print axioms WHGAP.Support.SelfComplement.defect_identity_zero

-- P6 (`WHGAP.order-boundary`) — LEAN-3 WP-F: the §5 witness BKM scalars
#print axioms WHGAP.«order-boundary».epsC_lt_one
#print axioms WHGAP.«order-boundary».b_pos_of
#print axioms WHGAP.«order-boundary».gE_lt_gB

-- Support.IcScalar (LEAN-2 WP-B: the §6 witness family's scalar coherent information)
#print axioms WHGAP.Support.BOut_mulVec_psi
#print axioms WHGAP.Support.BOut_mulVec_psibar
#print axioms WHGAP.Support.BOut_mulVec_e3
#print axioms WHGAP.Support.BOut_trace
#print axioms WHGAP.Support.EOut_offBlock_zero
#print axioms WHGAP.Support.EOut_trace
#print axioms WHGAP.Support.blockA_charpoly
#print axioms WHGAP.Support.blockB_mulVec_large
#print axioms WHGAP.Support.blockB_mulVec_small
#print axioms WHGAP.Support.discE_eq
#print axioms WHGAP.Support.discE_nonneg
#print axioms WHGAP.Support.IcScalar_eq
#print axioms WHGAP.Support.lamP_add_lamM
#print axioms WHGAP.Support.lamP_mul_lamM
#print axioms WHGAP.Support.sqrt_discE_le
#print axioms WHGAP.Support.lamM_le_eps_beta
#print axioms WHGAP.Support.lamP_ge
#print axioms WHGAP.Support.lamM_nonneg
#print axioms WHGAP.Support.lamM_pos
#print axioms WHGAP.Support.lamM_le_muA
#print axioms WHGAP.Support.negMulLog_antitone
#print axioms WHGAP.Support.negMulLog_mono
#print axioms WHGAP.Support.exp_neg_one_lt
#print axioms WHGAP.Support.exp_neg_one_gt
#print axioms WHGAP.Support.group3_nonneg
#print axioms WHGAP.Support.group2_nonneg
#print axioms WHGAP.Support.group1_lower
#print axioms WHGAP.Support.IcScalar_lower_bound
#print axioms WHGAP.Support.exists_eps_IcScalar_pos

-- P3 (`WHGAP.qpositive-onset`)
#print axioms WHGAP.«qpositive-onset».Claim
#print axioms WHGAP.«qpositive-onset».composition

-- P4 (`WHGAP.zero-capacity-application`)
#print axioms WHGAP.«zero-capacity-application».Claim
#print axioms WHGAP.«zero-capacity-application».composition
#print axioms WHGAP.«zero-capacity-application».composition_one_shot

-- P13 (`WHGAP.onset-two-fifths`) — stated only
#print axioms WHGAP.«onset-two-fifths».Claim
#print axioms WHGAP.«onset-two-fifths».conjecturedS

-- Support.Channel (LEAN-3 WP-D: the channel, the lift, the defect, and the Cmat bridge)
#print axioms WHGAP.Support.Channel.A
#print axioms WHGAP.Support.Channel.K
#print axioms WHGAP.Support.Channel.K_zero_eq
#print axioms WHGAP.Support.Channel.K_succ_eq
#print axioms WHGAP.Support.Channel.LamK_st
#print axioms WHGAP.Support.Channel.LamK_eq
#print axioms WHGAP.Support.Channel.LamK_tp
#print axioms WHGAP.Support.Channel.LamCK_st
#print axioms WHGAP.Support.Channel.LamCK_eq
#print axioms WHGAP.Support.Channel.Jdag_adjoint
#print axioms WHGAP.Support.Channel.chart_beta
#print axioms WHGAP.Support.Channel.chart_q
#print axioms WHGAP.Support.Channel.chart_q_beta
#print axioms WHGAP.Support.Channel.exists_chart
#print axioms WHGAP.Support.Channel.defect_eq
#print axioms WHGAP.Support.Channel.word_choi
#print axioms WHGAP.Support.Channel.choi_defect_eq_Cmat

-- P14 (`WHGAP.private-boundary`) LEAN-3 WP-D: residual (c), the outB/outE identification
#print axioms WHGAP.«private-boundary».u_neg
#print axioms WHGAP.«private-boundary».v_neg
#print axioms WHGAP.«private-boundary».outB_eq
#print axioms WHGAP.«private-boundary».outE_eq

-- Support.Channel (LEAN-4 WP-G: the §6 witness over ℂ; residual (b) at charpoly level)
#print axioms WHGAP.Support.Channel.psiWit
#print axioms WHGAP.Support.Channel.Pwit
#print axioms WHGAP.Support.Channel.PwitBar
#print axioms WHGAP.Support.Channel.Pwit_eq_outer
#print axioms WHGAP.Support.Channel.PwitBar_eq_outer
#print axioms WHGAP.Support.Channel.rhoWit
#print axioms WHGAP.Support.Channel.rhoWit_eq
#print axioms WHGAP.Support.Channel.rhoWit_trace
#print axioms WHGAP.Support.Channel.rhoWit_isHermitian
#print axioms WHGAP.Support.Channel.LamWit_eq
#print axioms WHGAP.Support.Channel.LamCWit_eq
#print axioms WHGAP.Support.Channel.LamWit_isHermitian
#print axioms WHGAP.Support.Channel.LamCWit_isHermitian
#print axioms WHGAP.Support.Channel.split3
#print axioms WHGAP.Support.Channel.split4
#print axioms WHGAP.Support.Channel.charpoly_of_reindex_blocks
#print axioms WHGAP.Support.Channel.charpoly_fin_one_eq
#print axioms WHGAP.Support.Channel.charpoly_fin_two_eq
#print axioms WHGAP.Support.Channel.charpoly_fin_two_quad
#print axioms WHGAP.Support.Channel.specB_charpoly
#print axioms WHGAP.Support.Channel.specE_charpoly
#print axioms WHGAP.Support.Channel.specB_charpoly_kraus
#print axioms WHGAP.Support.Channel.specE_charpoly_kraus
#print axioms WHGAP.Support.Channel.specB_charpoly_list
#print axioms WHGAP.Support.Channel.quad_eq_lamP_lamM
#print axioms WHGAP.Support.Channel.specE_charpoly_list

-- Support.EntropyC (LEAN-5 WP-H: the complex-Hermitian entropy layer; residual (b) discharged)
#print axioms WHGAP.Support.vnEntropyC
#print axioms WHGAP.Support.charpolyC_roots_of_prod
#print axioms WHGAP.Support.eigenvaluesC_multiset_of_roots
#print axioms WHGAP.Support.eigenvaluesC_multiset_eq_multiset
#print axioms WHGAP.Support.eigenvaluesC_multiset_eq
#print axioms WHGAP.Support.vnEntropyC_eq_sum_of_charpoly
#print axioms WHGAP.Support.vnEntropyC_eq_sum_of_charpoly_list
#print axioms WHGAP.Support.charpolyC_list_length
#print axioms WHGAP.Support.vnEntropyC_congr_charpoly
#print axioms WHGAP.Support.IcScalar_eq_vnEntropyC_diff

-- P9 (`WHGAP.no-ascent-hierarchy`) — LEAN-5 WP-H: the same statements at the entropy level
#print axioms WHGAP.«no-ascent-hierarchy».entropy_witness_eq_IcScalar
#print axioms WHGAP.«no-ascent-hierarchy».exists_eps_entropy_pos
#print axioms WHGAP.«no-ascent-hierarchy».Claim_of_entropy_witness

-- G (`WHGAP.goal`) — the union assembly
#print axioms WHGAP.goal.Claim
#print axioms WHGAP.goal.composition
#print axioms WHGAP.goal.composition_conjectured

-- Satisfiability witness (`WHGAP.Model`, from the R11 review — DAG protocol §7.10.5)
#print axioms WHGAP.Model.R11_P2
#print axioms WHGAP.Model.R11_P9
#print axioms WHGAP.Model.R11_P3
#print axioms WHGAP.Model.R11_P4
#print axioms WHGAP.Model.R11_P13
#print axioms WHGAP.Model.R11_goal
#print axioms WHGAP.Model.R11_goal_conj
#print axioms WHGAP.Model.R11_P6
#print axioms WHGAP.Model.R11_bridge
#print axioms WHGAP.Model.R11_P14

-- Satisfiability witness for the two NEW LEAN-2 bridges (`WHGAP.Model` §3b, from the R12
-- review — DAG protocol §7.10.5, R12 minor m3)
#print axioms WHGAP.Model.R12_hach
#print axioms WHGAP.Model.R12_P9_via_witness
#print axioms WHGAP.Model.R12_hdev
#print axioms WHGAP.Model.R12_P14_via_devetak

-- Satisfiability witness for the NEW LEAN-5 entropy-level bridge (`WHGAP.Model` §3c, from
-- the R15 review — DAG protocol §7.10.5, R15 minor m3)
#print axioms WHGAP.Model.R15_hach'
#print axioms WHGAP.Model.R15_P9_via_entropy
#print axioms WHGAP.Model.R15_hach_iff_hach'

end WHGAP.Trust

