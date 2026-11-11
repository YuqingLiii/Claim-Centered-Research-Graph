import WHGAP.Interface
import WHGAP.Support.IcScalar
import WHGAP.Support.EntropyC

/-!
# `WHGAP.no-ascent-hierarchy` (P9)

* node id: `WHGAP.no-ascent-hierarchy`
* node file: `channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.no-ascent-hierarchy.md`
* epistemic status on disk (2026-07-30): **CERTIFIED\*** — the `n = 1` isotropic layer is
  PROVED (R5c + R5d, both LICENSE A); the general hierarchy stays CONJECTURED.
* mechanization state: `proved` for the `d₁` sign analysis, the `ε log(1/ε)` witness
  extraction, and the 2×2 block invariants of paper Lemma 6.1 (`blockA_trace_det`);
  `stated` for `Claim`; `rel`: the expansion `hexp` is a hypothesis parameter.
* DAG parent: `WHGAP.qpositive-onset`.

## Frozen Claim (verbatim from the node file, `## Claim` section)

**(No-ascent hierarchy, necessity):** If Q(N) = 0 then, for every blocklength n, every pure
input psi on A^n, and every state phi on A^n with
supp (N^c)^{⊗n}(phi) ⊆ supp (N^c)^{⊗n}(psi),
\[ Tr[(N^c)^{⊗n}(phi) · log (N^c)^{⊗n}(psi)] ≤ Tr[N^{⊗n}(phi) · log N^{⊗n}(psi)] . \]
(The n = 1 instance for our family: for every pure qutrit psi and every kernel-avoiding phi,
Tr[Λ^c(phi) log Λ^c(psi)] ≤ Tr[Λ(phi) log Λ(psi)].) **[CERTIFIED\* — the repaired n = 1
isotropic layer is PROVED after two completed fresh-instance reviews (R5c: closed form +
orbit transport; R5d: expansion lemma + Theorem Q > 0 on (0, 2/5)); the general hierarchy
(n ≥ 2, non-isotropic strata, balanced layer N1'-b) remains CONJECTURED.]**

* frozen-claim SHA-256: `542edac65af8d29b3bf7a10c14298e587d9422dd87d80ccd24cad3ec65363d37`

## Statement-fidelity note (G-L5)

The prose Claim is the *necessity* direction of the no-ascent hierarchy (an operator
inequality between `Tr[Λ^c(φ) log Λ^c(ψ)]` and `Tr[Λ(φ) log Λ(ψ)]` at every blocklength).
That statement is **not** representable here: there is no operator, no logarithm of an
operator, and no blocklength in this development.

What this module formalizes is exactly the part of P9 that the parent P3 consumes — the
subset that R5c/R5d licensed at PROVED tier and that Theorem 8.1 of the N1' note actually
uses:

1. `d1_sign` / `d1_at_two_fifths` — the isotropic first-order weight
   `d₁(x) = (1-x)(2-5x)/(2-x)` is strictly positive exactly on `x < 2/5` (within `0 < x < 1`)
   and vanishes at `x = 2/5`;
2. `exists_pos_of_expansion` — the `ε log(1/ε)` witness-extraction step: if a coherent
   information `Ic` obeys `|Ic ε - d₁ ε log(1/ε)| ≤ C ε` on `(0, ε₀)` and `d₁ > 0`, then some
   `ε` in that window has `Ic ε > 0`.  The expansion itself (Lemma 5.1 of the N1' note, with
   its explicit uniform remainder) is a **hypothesis parameter** `hexp`, never a `sorry`;
3. `blockA_trace_det` — the trace and determinant of the 2×2 block `A(ε)` of paper
   **Lemma 6.1 (`lem:exactspec`, §6 "Positive capacity below 2/5")**, i.e. of the exact
   spectrum of the isotropic state `ρ_ε = (1-ε)P + εP̄` that the first-order expansion above
   is taken around.  `β` is carried as a variable constrained only by `β² = x(1-x)/2`, so no
   `Real.sqrt` enters the identity.  This is a **real symmetric stand-in** for the Hermitian
   block (whose off-diagonals are `∓iβ(1-2ε)`): only the moduli of the off-diagonal entries
   enter trace and determinant, so the real form carries the same two invariants, but it is
   not the Hermitian matrix itself.

`Claim I` below is correspondingly the *tier-1 shadow* used by the P3 composition: "at every
`x ∈ (0, 2/5)` some strictly positive coherent-information lower bound is available".  Its
relation to the prose Claim (R11 m2): the Lean `Claim` is the tier-1 shadow that Theorem 8.1
of the N1-prime note *produces*, and is what P3 consumes; no implication from the prose Claim
is asserted.

## Append-only deviation record

* 2026-07-30 (R11 MAJOR-1) — `blockA_trace_det` was **moved into this module** from
  `WHGAP.«private-boundary»`, where it had been filed and attributed to paper Lemma 7.1
  (`lem:holevo`).  Lemma 7.1 contains no 2×2 block; the matrix is `eq:Eexact` of paper
  Lemma 6.1 (`lem:exactspec`), an ingredient of the positivity layer served by this node and
  by `WHGAP.qpositive-onset`.  The identity itself was and is correct; only its attribution
  and its placement changed (DAG protocol §7.3).
* 2026-07-31 (LEAN-2 WP-B) — the expansion is no longer abstract **for the §6 witness
  family**.  `WHGAP.Support.IcScalar` now defines the scalar coherent information
  `IcScalar x ε` over the *explicit* eigenvalue lists of paper Lemma 6.1 and proves
  `exists_eps_IcScalar_pos : ∀ x, 0 < x → x < 2/5 → ∃ ε, 0 < ε ∧ ε < 1 ∧ 0 < IcScalar x ε`
  outright.  Consequences for the trust boundary of THIS module:
  - `witness_Ic_pos` (below) is the node-level restatement.  It has **no** `hexp`, no `d`,
    no `C`, no `ε₀`: the two-term expansion, its remainder, and the threshold `ε₁(x)` are
    all discharged inside the Lean proof.
  - `Claim_of_witness` (below) derives the node `Claim` from the carried theorem plus a
    single *achievability reading* hypothesis (`IcLB` is an interface predicate about a
    channel that does not exist in this development — it cannot be discharged here).
    The previous route to `Claim` needed BOTH an achievability reading AND `hexp`.
  - `exists_pos_of_expansion` is **retained unchanged**, and is still the only Lean content
    covering the *general* shape of Lemma 5.1 of the N1′ note (arbitrary `Ic`, arbitrary
    weight `d > 0`, arbitrary uniform remainder `C`).  The relation is: `witness_Ic_pos` is
    the single instance `Ic = IcScalar x ·` of the family that `exists_pos_of_expansion`
    parameterizes, proved *without* assuming the expansion; `exists_pos_of_expansion`
    remains the tool for any OTHER witness family.  Neither subsumes the other, and the
    WP-B proof does not go through it (the constants differ: the carried proof absorbs the
    remainder into the explicit `2ε`, so its threshold is `exp(-3/d₁(x))`, not the note's
    `exp(-C(x)/d₁(x))`).
* 2026-08-01 (LEAN-5 WP-H) — the scalar `IcScalar` is no longer only a formula: with
  `WHGAP.Support.EntropyC` there is now a Lean theorem that it **is the entropy difference**
  `S(Λ_x(ρ_ε)) − S(Λ^c_x(ρ_ε))` of the Kraus-built §6 outputs
  (`Support.IcScalar_eq_vnEntropyC_diff`).  Two declarations are added below:
  `exists_eps_entropy_pos` (the quantifier-congruent restatement of
  `Support.exists_eps_IcScalar_pos` with the conclusion's quantity written as the entropy
  difference) and `Claim_of_entropy_witness` (the same bridge as `Claim_of_witness` with
  the achievability hypothesis stated at the entropy level).  **Honest relation, reported
  rather than overstated:** `hach'` is *equivalent* to `hach` on the applied range — the
  equivalence is itself a Lean theorem, `entropy_witness_eq_IcScalar` — so this is a
  restatement, not a logical weakening.  What genuinely moved out of the trust boundary is
  the *identification* "the number `IcScalar x ε` is the von Neumann entropy difference of
  the two outputs", which used to be prose plus exact sympy and is now Lean.  The original
  `Claim_of_witness`/`hach` are retained unchanged (append-only census discipline).
-/

namespace WHGAP.«no-ascent-hierarchy»

open WHGAP WHGAP.Support

/-! ## T2 core — the sign of the isotropic first-order weight -/

/-- `d₁(2/5) = 0`. -/
theorem d1_at_two_fifths : dOne (2 / 5) = 0 := by
  unfold dOne
  norm_num

/-- **`d1_sign`.**  On `0 < x < 1`, `d₁(x) > 0` exactly when `x < 2/5`. -/
theorem d1_sign {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) : 0 < dOne x ↔ x < 2 / 5 := by
  have h2x : (0:ℝ) < 2 - x := by linarith
  unfold dOne
  constructor
  · intro h
    by_contra hc
    push_neg at hc
    have : (1 - x) * (2 - 5 * x) / (2 - x) ≤ 0 :=
      div_nonpos_of_nonpos_of_nonneg (by nlinarith) h2x.le
    linarith
  · intro h
    exact div_pos (by nlinarith) h2x

/-! ## T1 core — extracting a positive coherent information from the `ε log(1/ε)` expansion -/

/-- **`exists_pos_of_expansion`.**  Given a two-term expansion with linear remainder,
`|Ic ε - d ε log(1/ε)| ≤ C ε` for all `ε ∈ (0, ε₀)`, together with `d > 0`, `C ≥ 0`,
`ε₀ > 0`, there is an `ε ∈ (0, ε₀)` with `Ic ε > 0`.

The witness is `ε = min (ε₀/2) (exp (-((C+1)/d)))`, i.e. the explicit threshold
`ε₁(x)` of Theorem 8.1 of `notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md`.  `Ic` is an
abstract real function and `hexp` is a hypothesis: this checks the *witness extraction*, not
the expansion. -/
theorem exists_pos_of_expansion {Ic : ℝ → ℝ} {d C ε₀ : ℝ}
    (hd : 0 < d) (hC : 0 ≤ C) (hε₀ : 0 < ε₀)
    (hexp : ∀ ε : ℝ, 0 < ε → ε < ε₀ → |Ic ε - d * ε * Real.log (1 / ε)| ≤ C * ε) :
    ∃ ε : ℝ, 0 < ε ∧ ε < ε₀ ∧ 0 < Ic ε := by
  set E : ℝ := Real.exp (-((C + 1) / d)) with hEdef
  have hEpos : 0 < E := Real.exp_pos _
  set ε : ℝ := min (ε₀ / 2) E with hεdef
  have hεpos : 0 < ε := lt_min (by linarith) hEpos
  have hεlt : ε < ε₀ := lt_of_le_of_lt (min_le_left _ _) (by linarith)
  have hεE : ε ≤ E := min_le_right _ _
  have hlog : Real.log ε ≤ -((C + 1) / d) := by
    have h := Real.log_le_log hεpos hεE
    rwa [hEdef, Real.log_exp] at h
  have hlog1 : Real.log (1 / ε) = -Real.log ε := by
    rw [one_div, Real.log_inv]
  have hkey : (C + 1) / d ≤ Real.log (1 / ε) := by
    rw [hlog1]; linarith
  have hdε : 0 < d * ε := mul_pos hd hεpos
  have hmul : d * ε * ((C + 1) / d) ≤ d * ε * Real.log (1 / ε) :=
    mul_le_mul_of_nonneg_left hkey hdε.le
  have hval : d * ε * ((C + 1) / d) = ε * (C + 1) := by
    field_simp
    all_goals ring
  rw [hval] at hmul
  have habs := abs_le.mp (hexp ε hεpos hεlt)
  refine ⟨ε, hεpos, hεlt, ?_⟩
  nlinarith [habs.1, hmul, hεpos]

/-! ## T2 core — the 2×2 block invariants of paper Lemma 6.1 (`lem:exactspec`) -/

/-- **`blockA_trace_det`.**  For the real symmetric stand-in
`A = !![1-x, -β(1-2ε); -β(1-2ε), x/2]` with `β² = x(1-x)/2`:
`tr A = 1 - x/2` and `det A = 2x(1-x)ε(1-ε)`.  No `Real.sqrt` appears: `β` is a variable
constrained only by its square.

This supports paper **Lemma 6.1 (`lem:exactspec`, §6)** — the exact spectrum of the isotropic
family `ρ_ε = (1-ε)P + εP̄` whose `ε log(1/ε)` expansion drives the positivity layer — and
**not** Lemma 7.1 (`lem:holevo`), to which it was mis-attributed before R11 (MAJOR-1). -/
theorem blockA_trace_det (x ε β : ℝ) (hβ : β ^ 2 = x * (1 - x) / 2) :
    Matrix.trace (!![1 - x, -(β * (1 - 2 * ε)); -(β * (1 - 2 * ε)), x / 2] :
        Matrix (Fin 2) (Fin 2) ℝ) = 1 - x / 2 ∧
    Matrix.det (!![1 - x, -(β * (1 - 2 * ε)); -(β * (1 - 2 * ε)), x / 2] :
        Matrix (Fin 2) (Fin 2) ℝ) = 2 * x * (1 - x) * ε * (1 - ε) := by
  constructor
  · rw [Matrix.trace_fin_two_of]
    ring
  · rw [Matrix.det_fin_two_of]
    linear_combination (-(1 - 2 * ε) ^ 2) * hβ

/-! ## T2 core (LEAN-2 WP-B) — the carried positivity theorem for the §6 witness family

This is the part that used to be `hexp`.  See the deviation record above for the exact
relation between this theorem and the retained general `exists_pos_of_expansion`. -/

/-- **`witness_Ic_pos`.**  For every `x ∈ (0, 2/5)` there is an `ε ∈ (0,1)` at which the
scalar coherent information of the §6 witness family `ρ_ε = (1-ε)P_ψ + εP_ψ̄` is strictly
positive.  **No hypothesis beyond `0 < x < 2/5`** — in particular no expansion hypothesis:
the `ε log(1/ε)` argument, its remainder bound, and the explicit threshold are all proved
in `WHGAP.Support.IcScalar`.

`IcScalar` is built from the *explicit closed-form eigenvalue lists* of paper Lemma 6.1
(`lem:exactspec`), not from a channel; see that module's honesty note. -/
theorem witness_Ic_pos {x : ℝ} (hx0 : 0 < x) (hx : x < 2 / 5) :
    ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧ 0 < IcScalar x ε :=
  Support.exists_eps_IcScalar_pos x hx0 hx

/-- **`witness_Ic_lower_bound`.**  The quantitative form actually proved: on `0 < ε ≤ 1/3`
the scalar coherent information dominates `d₁(x)·(-ε log ε) - 2ε`, with `d₁ = dOne` the
isotropic first-order weight whose sign is `d1_sign`. -/
theorem witness_Ic_lower_bound {x ε : ℝ} (hx0 : 0 < x) (hx : x < 2 / 5)
    (hε0 : 0 < ε) (hε3 : ε ≤ 1 / 3) :
    dOne x * Real.negMulLog ε - 2 * ε ≤ IcScalar x ε :=
  Support.IcScalar_lower_bound hx0 hx hε0 hε3

/-! ## T1 layer — the node Claim -/

/-- **P9 Claim, tier-1 form (the subset P3 consumes).**  At every `x ∈ (0, 2/5)` there is a
strictly positive achievable coherent-information lower bound. -/
def Claim (I : CapacityInterface) : Prop :=
  ∀ x : ℝ, 0 < x → x < 2 / 5 → ∃ c : ℝ, 0 < c ∧ I.IcLB x c

/-- **`Claim_of_witness` (LEAN-2 WP-B).**  The node Claim follows from the CARRIED
positivity theorem plus one hypothesis only: the *achievability reading* `hach`, i.e. that
the scalar `IcScalar x ε` computed from the explicit output spectra really is an achievable
coherent-information value of `Λ_x` at the input `ρ_ε`.

That reading is exactly the missing channel/entropy layer (project README scope item 1) and
is not discharged here.  What WP-B removed is the *other* hypothesis: no expansion lemma,
no remainder constant, and no threshold are assumed any more — compare
`exists_pos_of_expansion`, which needs `hexp` on top of an achievability reading. -/
theorem Claim_of_witness (I : CapacityInterface)
    (hach : ∀ x ε : ℝ, 0 < x → x < 2 / 5 → 0 < ε → ε < 1 → 0 < IcScalar x ε →
      I.IcLB x (IcScalar x ε)) : Claim I := by
  intro x hx0 hx
  obtain ⟨ε, hε0, hε1, hpos⟩ := witness_Ic_pos hx0 hx
  exact ⟨IcScalar x ε, hpos, hach x ε hx0 hx hε0 hε1 hpos⟩

/-! ## LEAN-5 WP-H — the same two statements at the ENTROPY level

`WHGAP.Support.EntropyC` proves `IcScalar x ε = S(Λ_x(ρ_ε)) − S(Λ^c_x(ρ_ε))` for the
Kraus-built §6 outputs over `ℂ`.  The two declarations below are the node-level
consequences.  Nothing above is modified or weakened. -/

/-- **`entropy_witness_eq_IcScalar`.**  At the canonical `β = √(x(1−x)/2)`, the entropy
difference of the two §6 witness outputs IS the scalar `IcScalar x ε`.  Stated on
`0 < x < 2/5` — the range the node uses; `Support.IcScalar_eq_vnEntropyC_diff` is the
general form (`0 ≤ x ≤ 1`, any `β` with `β² = x(1−x)/2`).

This is the theorem that makes the relation between `hach` and `hach'` below **exact**:
they are equivalent hypotheses, so `Claim_of_entropy_witness` is a restatement of
`Claim_of_witness` at the entropy level, not a logical weakening. -/
theorem entropy_witness_eq_IcScalar {x : ℝ} (hx0 : 0 < x) (hx25 : x < 2 / 5) (ε : ℝ) :
    vnEntropyC (Channel.LamWit_isHermitian x ε)
        - vnEntropyC (Channel.LamCWit_isHermitian x ε (Real.sqrt (x * (1 - x) / 2)))
      = IcScalar x ε := by
  have hβ : Real.sqrt (x * (1 - x) / 2) ^ 2 = x * (1 - x) / 2 :=
    Real.sq_sqrt (by nlinarith)
  exact (Support.IcScalar_eq_vnEntropyC_diff (by linarith) (by linarith) ε _ hβ).symm

/-- **`exists_eps_entropy_pos`.**  The quantifier-congruent restatement of
`Support.exists_eps_IcScalar_pos`: for every `x ∈ (0, 2/5)` there is an `ε ∈ (0,1)` at
which the **von Neumann entropy difference** of the two §6 witness outputs — the B-side
`Λ_x(ρ_ε)` and the E-side `Λ^c_x(ρ_ε)`, both complex Hermitian, both built from the Kraus
set in `WHGAP.Support.Channel` — is strictly positive.

Binders and hypotheses are literally those of `Support.exists_eps_IcScalar_pos`; only the
conclusion's left-hand quantity changed (pre-registered gate GH3,
`tools/whgap_lean5_wph_check.py`).  `β` is discharged at the canonical
`√(x(1−x)/2)` by `Real.sq_sqrt`. -/
theorem exists_eps_entropy_pos (x : ℝ) (hx0 : 0 < x) (hx25 : x < 2 / 5) :
    ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧
      0 < vnEntropyC (Channel.LamWit_isHermitian x ε)
            - vnEntropyC (Channel.LamCWit_isHermitian x ε (Real.sqrt (x * (1 - x) / 2))) := by
  obtain ⟨ε, hε0, hε1, hpos⟩ := Support.exists_eps_IcScalar_pos x hx0 hx25
  exact ⟨ε, hε0, hε1, by rw [entropy_witness_eq_IcScalar hx0 hx25 ε]; exact hpos⟩

/-- **`Claim_of_entropy_witness` (LEAN-5 WP-H).**  The node `Claim` from the carried
positivity theorem plus an achievability reading stated **at the entropy level**: `hach'`
says that a strictly positive value of `S(Λ_x(ρ_ε)) − S(Λ^c_x(ρ_ε))` is an achievable
coherent-information lower bound for `Λ_x`.

What this does and does not buy, stated honestly (the wording R15 should check):

* it does **not** make the hypothesis logically weaker than `Claim_of_witness`'s `hach`:
  by `entropy_witness_eq_IcScalar` the two quantities are equal on the applied range, so
  `hach` and `hach'` are interchangeable;
* what it *does* is remove the charpoly→entropy identification from the trust boundary.
  `hach` spoke about a number defined by a formula over two eigenvalue **lists**; `hach'`
  speaks about the entropies of the two output **matrices**.  The step between them is now
  a Lean theorem (`Support.IcScalar_eq_vnEntropyC_diff`) instead of an exact-sympy gate;
* what `hach'` still carries is exactly (i) that `LamC`/`LamCK` is *the* complementary
  channel of `Lam` (a Stinespring identification — there is no complete positivity and no
  dilation theory in this development) and (ii) LSD/Devetak achievability, i.e. that a
  positive coherent information at one input is a capacity lower bound.  Both are
  interface-tier, cited in `WHGAP/Interface.lean`. -/
theorem Claim_of_entropy_witness (I : CapacityInterface)
    (hach' : ∀ x ε : ℝ, 0 < x → x < 2 / 5 → 0 < ε → ε < 1 →
      0 < vnEntropyC (Channel.LamWit_isHermitian x ε)
            - vnEntropyC (Channel.LamCWit_isHermitian x ε (Real.sqrt (x * (1 - x) / 2))) →
      I.IcLB x (vnEntropyC (Channel.LamWit_isHermitian x ε)
            - vnEntropyC (Channel.LamCWit_isHermitian x ε (Real.sqrt (x * (1 - x) / 2))))) :
    Claim I := by
  intro x hx0 hx
  obtain ⟨ε, hε0, hε1, hpos⟩ := exists_eps_entropy_pos x hx0 hx
  exact ⟨_, hpos, hach' x ε hx0 hx hε0 hε1 hpos⟩

end WHGAP.«no-ascent-hierarchy»

