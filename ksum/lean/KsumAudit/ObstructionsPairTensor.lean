/-
# `thm:pair-tensor` — Pair-tensor annihilation

LaTeX: `ksum/paper/ksum_small_alphabet.tex`, label `thm:pair-tensor`, line 830
(construction in equation (40)).
DAG node: `KSUM.B4b.L2.M1` (`ksum/proof-dag/nodes/KSUM.B4b.L2.M1.yaml`, status PROVED).

## The quantifier structure the LaTeX asserts (written out BEFORE formalizing)

∀ odd `q ≥ 3`, ∀ `N ≥ q`, ∀ `t ∈ ℤ_q`:  ∃ an `S_N × C(σ)`-invariant signed measure `μ` on
`ℤ_q^N` with `‖μ‖₁ = 1` that annihilates every query polynomial of degree below `q-1`; and the
cancellation already holds on each LABELED exact pair-total slice, before the slices are mixed.

This is an EXISTENCE claim, so the deliverable is a construction, not a class exclusion.

## SCOPE — what is and is not formalized here (read together with the artifact)

Formalized, at the paper's own quantifiers (`∀` odd `q ≥ 3`, `∀ N ≥ q`, `∀` admissible
pair-permutation-invariant slice law):

  * the local kernel `κ_s = (I_s - A_s)/2` of (40): `‖κ_s‖₁ = 1`, total mass `0`, and vanishing
    moments against `1`, `i`, `j` — for EVERY `s`, both parities;
  * the `r`-fold tensor on a fixed labeled exact-total slice: `ℓ¹` norm exactly `1`, and
    annihilation of EVERY falling-factorial row of total order `< 2r = q-1` (the pigeonhole step
    of the paper's proof);  this is the paper's "the cancellation holds on each labeled exact
    pair-total slice before those slices are mixed";
  * the slice mixture: any probability law on admissible slices keeps `ℓ¹ = 1` and inherits the
    annihilation;
  * non-emptiness of the admissible slice set for every `N ≥ q` (the paper's `N-1 ≥ 2r`);
  * `C(σ)`-invariance of the tensor: endpoint swap `C₂` on each pair, and pair permutation `S_r`.

NOT formalized (reported, not worked around):

  * the uniform lift of an occupancy weight to its `S_N` STRING orbit, and hence `S_N`-invariance
    on `ℤ_q^N`.  Everything here lives at the occupancy/pair-histogram level, which is the level
    the paper's own proof works at; the query-degree statement is obtained from the occupancy
    statement by `lem:factorial-filtration`.
  * the pushforward of the labeled slice space onto occupancy vectors.  The paper asserts
    "different labeled pair-total vectors have disjoint support"; that is true (the local
    occupancy `(i,j)` determines `s = i+j`), but the pushforward `ℓ¹`-identity is not proved
    here — the `ℓ¹` computations below are on the LABELED space, exactly as the paper's proof
    computes them.
  * the alphabet `ℤ_q` and the target `t` do not appear at all: for this theorem they enter only
    through `r = (q-1)/2`, which is how the paper's proof uses them.
-/
import KsumAudit.ObstructionsCore

namespace KsumAudit.Obstructions.PairTensor

open Finset KsumAudit.Obstructions

set_option linter.unusedSectionVars false

/-! ## The local kernel `κ_s = (I_s - A_s)/2` of equation (40) -/

/-- Local states of one nonfixed σ-pair on the exact-total slice `i + j = s`:
`0, 1` are the two AXIS states `(s,0)`, `(0,s)` (the support of `A_s`) and `2, 3` are the two
INTERIOR states (the support of `I_s`), which coincide when `s` is even — exactly reproducing
`I_s = δ_{(s/2,s/2)}` for even `s` and the symmetric two-point law for odd `s`. -/
def occLocal (s : ℕ) : Fin 4 → ℕ × ℕ := ![(s, 0), (0, s), (s / 2, s - s / 2), (s - s / 2, s / 2)]

/-- `κ_s = (I_s - A_s)/2`: mass `-1/4` on each axis state, `+1/4` on each interior state. -/
def kappa : Fin 4 → ℚ := ![-(1/4), -(1/4), 1/4, 1/4]

/-- The local falling-factorial row `(i)_a (j)_b`. -/
def ffLocal (a b : ℕ) (p : ℕ × ℕ) : ℚ :=
  ((p.1.descFactorial a : ℚ)) * ((p.2.descFactorial b : ℚ))

lemma occ_split (s : ℕ) : ((s / 2 : ℕ) : ℚ) + ((s - s / 2 : ℕ) : ℚ) = (s : ℚ) := by
  have h : s / 2 ≤ s := Nat.div_le_self s 2
  rw [Nat.cast_sub h]
  ring

@[simp] lemma kappa_zero : kappa 0 = -(1/4) := rfl
@[simp] lemma kappa_one : kappa 1 = -(1/4) := rfl
@[simp] lemma kappa_two : kappa 2 = 1/4 := rfl
@[simp] lemma kappa_three : kappa 3 = 1/4 := rfl
@[simp] lemma occLocal_zero (s : ℕ) : occLocal s 0 = (s, 0) := rfl
@[simp] lemma occLocal_one (s : ℕ) : occLocal s 1 = (0, s) := rfl
@[simp] lemma occLocal_two (s : ℕ) : occLocal s 2 = (s / 2, s - s / 2) := rfl
@[simp] lemma occLocal_three (s : ℕ) : occLocal s 3 = (s - s / 2, s / 2) := rfl

/-- `‖κ_s‖₁ = 1`. -/
lemma kappa_l1 : ∑ u, |kappa u| = 1 := by
  norm_num [Fin.sum_univ_four]

/-- `κ_s` has total mass zero. -/
lemma kappa_total : ∑ u, kappa u = 0 := by
  norm_num [Fin.sum_univ_four]

/-- `κ_s` annihilates the local row `i`. -/
lemma kappa_moment_fst (s : ℕ) :
    ∑ u, kappa u * ((occLocal s u).1 : ℚ) = 0 := by
  have h := occ_split s
  rw [Fin.sum_univ_four]
  simp only [kappa_zero, kappa_one, kappa_two, kappa_three, occLocal_zero, occLocal_one,
    occLocal_two, occLocal_three, Nat.cast_zero]
  linarith

/-- `κ_s` annihilates the local row `j`. -/
lemma kappa_moment_snd (s : ℕ) :
    ∑ u, kappa u * ((occLocal s u).2 : ℚ) = 0 := by
  have h := occ_split s
  rw [Fin.sum_univ_four]
  simp only [kappa_zero, kappa_one, kappa_two, kappa_three, occLocal_zero, occLocal_one,
    occLocal_two, occLocal_three, Nat.cast_zero]
  linarith

/-- **The local annihilation step.**  Every local falling-factorial row of order below two —
i.e. `1`, `i`, or `j` — is annihilated by `κ_s`, for every `s` and both parities. -/
lemma kappa_annihilates {a b : ℕ} (hab : a + b ≤ 1) (s : ℕ) :
    ∑ u, kappa u * ffLocal a b (occLocal s u) = 0 := by
  rcases Nat.lt_or_ge a 1 with h1 | h1
  · have ha0 : a = 0 := by omega
    subst ha0
    rcases Nat.lt_or_ge b 1 with h2 | h2
    · have hb0 : b = 0 := by omega
      subst hb0
      simpa [ffLocal] using kappa_total
    · have hb1 : b = 1 := by omega
      subst hb1
      simpa [ffLocal, Nat.descFactorial_one] using kappa_moment_snd s
  · have ha1 : a = 1 := by omega
    have hb0 : b = 0 := by omega
    subst ha1; subst hb0
    simpa [ffLocal, Nat.descFactorial_one] using kappa_moment_fst s

/-! ## The `r`-fold tensor on one labeled exact-total slice -/

variable {r : ℕ}

/-- `⨂_c κ_{s_c}` as a function of the local-state vector. -/
def prodKappa (x : Fin r → Fin 4) : ℚ := ∏ c, kappa (x c)

/-- The falling-factorial row of the pair part, at local orders `α c = (a_c, b_c)`. -/
def prodRow (s : Fin r → ℕ) (α : Fin r → ℕ × ℕ) (x : Fin r → Fin 4) : ℚ :=
  ∏ c, ffLocal (α c).1 (α c).2 (occLocal (s c) (x c))

/-- A fixed-size tensor has `ℓ¹` norm one. -/
theorem prodKappa_l1 : ∑ x : Fin r → Fin 4, |prodKappa x| = 1 := by
  have h : ∏ _c : Fin r, ∑ u ∈ (univ : Finset (Fin 4)), |kappa u|
      = ∑ x ∈ Fintype.piFinset (fun _ : Fin r => (univ : Finset (Fin 4))), ∏ c, |kappa (x c)| :=
    Finset.prod_univ_sum _ _
  rw [Fintype.piFinset_univ] at h
  have h2 : ∑ x : Fin r → Fin 4, |prodKappa x| = ∏ _c : Fin r, ∑ u, |kappa u| := by
    rw [h]
    refine Finset.sum_congr rfl fun x _ => ?_
    simp only [prodKappa]
    exact Finset.abs_prod _ _
  rw [h2, kappa_l1, Finset.prod_const_one]

/-- The tensor moment factorizes into local moments. -/
theorem prodKappa_moment (s : Fin r → ℕ) (α : Fin r → ℕ × ℕ) :
    ∑ x : Fin r → Fin 4, prodKappa x * prodRow s α x
      = ∏ c, ∑ u, kappa u * ffLocal (α c).1 (α c).2 (occLocal (s c) u) := by
  have h : ∏ c : Fin r, ∑ u ∈ (univ : Finset (Fin 4)),
        kappa u * ffLocal (α c).1 (α c).2 (occLocal (s c) u)
      = ∑ x ∈ Fintype.piFinset (fun _ : Fin r => (univ : Finset (Fin 4))),
        ∏ c, (kappa (x c) * ffLocal (α c).1 (α c).2 (occLocal (s c) (x c))) :=
    Finset.prod_univ_sum _ _
  rw [Fintype.piFinset_univ] at h
  rw [h]
  refine Finset.sum_congr rfl fun x _ => ?_
  simp only [prodKappa, prodRow]
  rw [Finset.prod_mul_distrib]

/-- Pigeonhole: `r` pairs whose local orders sum to less than `2r` must contain a pair of local
order below two. -/
lemma exists_light_pair (_hr : 1 ≤ r) (g : Fin r → ℕ) (h : ∑ c, g c < 2 * r) :
    ∃ c, g c ≤ 1 := by
  by_contra hc
  rw [not_exists] at hc
  have hge : ∀ c ∈ (univ : Finset (Fin r)), 2 ≤ g c := fun c _ => by have := hc c; omega
  have := Finset.sum_le_sum hge
  rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, smul_eq_mul] at this
  omega

/-- **`thm:pair-tensor`, slice-wise cancellation.**
On EVERY labeled exact pair-total slice, the tensor annihilates EVERY falling-factorial row of
total order below `2r = q-1` — including the fixed-point order `αf` (the fixed point carries
occupancy exactly one). -/
theorem slice_annihilation (hr : 1 ≤ r) (s : Fin r → ℕ) (αf : ℕ) (α : Fin r → ℕ × ℕ)
    (hord : αf + ∑ c, ((α c).1 + (α c).2) < 2 * r) :
    ∑ x : Fin r → Fin 4,
      prodKappa x * (((1:ℕ).descFactorial αf : ℚ) * prodRow s α x) = 0 := by
  have hsum : ∑ c, ((α c).1 + (α c).2) < 2 * r := by omega
  obtain ⟨c₀, hc₀⟩ := exists_light_pair hr (fun c => (α c).1 + (α c).2) hsum
  have hzero : ∑ u, kappa u * ffLocal (α c₀).1 (α c₀).2 (occLocal (s c₀) u) = 0 :=
    kappa_annihilates hc₀ _
  have hfac : ∑ x : Fin r → Fin 4, prodKappa x * prodRow s α x = 0 := by
    rw [prodKappa_moment]
    exact Finset.prod_eq_zero (Finset.mem_univ c₀) hzero
  calc ∑ x : Fin r → Fin 4, prodKappa x * (((1:ℕ).descFactorial αf : ℚ) * prodRow s α x)
      = ((1:ℕ).descFactorial αf : ℚ) * ∑ x : Fin r → Fin 4, prodKappa x * prodRow s α x := by
        rw [Finset.mul_sum]; exact Finset.sum_congr rfl fun x _ => by ring
    _ = 0 := by rw [hfac, mul_zero]

/-! ## `C(σ) ≅ C₂ ≀ S_r`-invariance of the tensor -/

/-- Endpoint swap on one pair: `(i,j) ↦ (j,i)`, i.e. `0↔1`, `2↔3` on local states. -/
def swapState : Fin 4 → Fin 4 := ![1, 0, 3, 2]

lemma occLocal_swap (s : ℕ) (u : Fin 4) :
    occLocal s (swapState u) = ((occLocal s u).2, (occLocal s u).1) := by
  fin_cases u <;> simp [occLocal, swapState]

lemma kappa_swap (u : Fin 4) : kappa (swapState u) = kappa u := by
  fin_cases u <;> simp [kappa, swapState]

/-- **`C₂^r` (endpoint-swap) invariance.**  Flipping the endpoint orientation of an ARBITRARY
subset of the pairs leaves the tensor unchanged. -/
theorem prodKappa_endpoint_swap (flip : Fin r → Bool) (x : Fin r → Fin 4) :
    prodKappa (fun c => if flip c then swapState (x c) else x c) = prodKappa x := by
  simp only [prodKappa]
  refine Finset.prod_congr rfl fun c _ => ?_
  by_cases h : flip c = true
  · rw [if_pos h]; exact kappa_swap (x c)
  · rw [if_neg h]

/-- **`S_r` (pair-exchangeability) invariance.**  Permuting the pairs leaves the tensor
unchanged. -/
theorem prodKappa_perm (π : Equiv.Perm (Fin r)) (x : Fin r → Fin 4) :
    prodKappa (fun c => x (π c)) = prodKappa x := by
  simp only [prodKappa]
  exact Equiv.prod_comp π (fun c => kappa (x c))

/-! ## Admissible slices and the mixture -/

/-- The admissible exact-total slice vectors: `s_c ≥ 2` on every pair and `∑_c s_c = N-1`
(one item sits at the fixed point).  Manifestly `S_r`-stable. -/
def admissible (N : ℕ) : Finset (Fin r → ℕ) :=
  (Fintype.piFinset (fun _ : Fin r => Finset.range N)).filter
    (fun s => (∀ c, 2 ≤ s c) ∧ ∑ c, s c = N - 1)

lemma mem_admissible {N : ℕ} {s : Fin r → ℕ} :
    s ∈ admissible N ↔ (∀ c, s c < N) ∧ (∀ c, 2 ≤ s c) ∧ ∑ c, s c = N - 1 := by
  simp [admissible, Fintype.mem_piFinset, Finset.mem_range]

/-- The paper's `N-1 ≥ 2r`: for `N ≥ 2r+1` there IS an admissible slice vector. -/
theorem admissible_nonempty (hr : 1 ≤ r) {N : ℕ} (hN : 2 * r + 1 ≤ N) :
    (admissible (r := r) N).Nonempty := by
  classical
  set c₀ : Fin r := ⟨0, hr⟩ with hc₀
  set k : ℕ := N - 1 - 2 * r with hk
  refine ⟨fun c => if c = c₀ then 2 + k else 2, ?_⟩
  have hsum : ∑ c : Fin r, (if c = c₀ then 2 + k else 2) = (2 + k) + 2 * (r - 1) := by
    rw [← Finset.add_sum_erase univ _ (Finset.mem_univ c₀), if_pos rfl]
    congr 1
    rw [Finset.sum_congr rfl (fun c hc => if_neg (Finset.mem_erase.mp hc).1),
      Finset.sum_const, Finset.card_erase_of_mem (Finset.mem_univ c₀), Finset.card_univ,
      Fintype.card_fin, smul_eq_mul, Nat.mul_comm]
  rw [mem_admissible]
  refine ⟨fun c => ?_, fun c => ?_, ?_⟩
  · by_cases h : c = c₀ <;> simp only [h, if_true, if_false] <;> omega
  · by_cases h : c = c₀ <;> simp only [h, if_true, if_false] <;> omega
  · rw [hsum]; omega

/-- **`thm:pair-tensor`, the mixture.**
For ANY probability law `w` on ANY set of admissible slices, the slice mixture has `ℓ¹` norm
exactly one and annihilates every falling-factorial row of total order below `2r = q-1`. -/
theorem mixture_l1_and_annihilation (hr : 1 ≤ r) (T : Finset (Fin r → ℕ))
    (w : (Fin r → ℕ) → ℚ) (hw : ∀ s ∈ T, 0 ≤ w s) (hw1 : ∑ s ∈ T, w s = 1) :
    (∑ s ∈ T, ∑ x : Fin r → Fin 4, |w s * prodKappa x| = 1)
      ∧ ∀ (αf : ℕ) (α : Fin r → ℕ × ℕ),
          αf + ∑ c, ((α c).1 + (α c).2) < 2 * r →
          ∑ s ∈ T, ∑ x : Fin r → Fin 4,
            (w s * prodKappa x) * (((1:ℕ).descFactorial αf : ℚ) * prodRow s α x) = 0 := by
  constructor
  · rw [← hw1]
    refine Finset.sum_congr rfl fun s hs => ?_
    have : ∑ x : Fin r → Fin 4, |w s * prodKappa x|
        = |w s| * ∑ x : Fin r → Fin 4, |prodKappa x| := by
      rw [Finset.mul_sum]
      exact Finset.sum_congr rfl fun x _ => abs_mul _ _
    rw [this, prodKappa_l1, mul_one, abs_of_nonneg (hw s hs)]
  · intro αf α hord
    refine Finset.sum_eq_zero fun s _ => ?_
    have hrw : ∑ x : Fin r → Fin 4,
          (w s * prodKappa x) * (((1:ℕ).descFactorial αf : ℚ) * prodRow s α x)
        = w s * ∑ x : Fin r → Fin 4,
            prodKappa x * (((1:ℕ).descFactorial αf : ℚ) * prodRow s α x) := by
      rw [Finset.mul_sum]
      exact Finset.sum_congr rfl fun x _ => by ring
    rw [hrw, slice_annihilation hr s αf α hord, mul_zero]

/-- **`thm:pair-tensor`, assembled at the paper's quantifiers.**

For every odd `q ≥ 3` and every `N ≥ q` there is a nonempty set of admissible exact-total pair
slices and a probability law on it whose slice mixture has `ℓ¹` norm exactly one and annihilates
every falling-factorial row of total order below `q-1`, slice-wise before mixing.

(`t ∈ ℤ_q` is absent because it enters the paper's proof only through `r = (q-1)/2`.) -/
theorem pair_tensor (q N : ℕ) (hq : Odd q) (hq3 : 3 ≤ q) (hN : q ≤ N) :
    ∃ (T : Finset (Fin ((q - 1) / 2) → ℕ)) (w : (Fin ((q - 1) / 2) → ℕ) → ℚ),
      T.Nonempty
      ∧ (∀ s ∈ T, 0 ≤ w s)
      ∧ (∑ s ∈ T, w s = 1)
      ∧ (∀ s ∈ T, (∀ c, 2 ≤ s c) ∧ ∑ c, s c = N - 1)
      ∧ (∑ s ∈ T, ∑ x : Fin ((q - 1) / 2) → Fin 4, |w s * prodKappa x| = 1)
      ∧ (∀ (αf : ℕ) (α : Fin ((q - 1) / 2) → ℕ × ℕ),
          αf + ∑ c, ((α c).1 + (α c).2) < q - 1 →
          ∑ s ∈ T, ∑ x : Fin ((q - 1) / 2) → Fin 4,
            (w s * prodKappa x) * (((1:ℕ).descFactorial αf : ℚ) * prodRow s α x) = 0) := by
  classical
  obtain ⟨k, hk⟩ := hq
  set r : ℕ := (q - 1) / 2 with hrdef
  have hr2 : 2 * r = q - 1 := by omega
  have hr : 1 ≤ r := by omega
  have hNr : 2 * r + 1 ≤ N := by omega
  obtain ⟨s₀, hs₀⟩ := admissible_nonempty (r := r) hr hNr
  set T : Finset (Fin r → ℕ) := admissible (r := r) N with hT
  have hTne : T.Nonempty := ⟨s₀, hs₀⟩
  have hTcard : (0 : ℚ) < (T.card : ℚ) := by
    exact_mod_cast Finset.card_pos.mpr hTne
  refine ⟨T, fun _ => 1 / (T.card : ℚ), hTne, fun s _ => by positivity, ?_, ?_, ?_, ?_⟩
  · rw [Finset.sum_const, nsmul_eq_mul]
    field_simp
  · intro s hs
    have := mem_admissible.mp hs
    exact ⟨this.2.1, this.2.2⟩
  · exact (mixture_l1_and_annihilation hr T _ (fun s _ => by positivity)
      (by rw [Finset.sum_const, nsmul_eq_mul]; field_simp)).1
  · intro αf α hord
    exact (mixture_l1_and_annihilation hr T _ (fun s _ => by positivity)
      (by rw [Finset.sum_const, nsmul_eq_mul]; field_simp)).2 αf α (by omega)

/-! ## Non-vacuity witnesses -/

/-- `q = 3` (`r = 1`), `N = 3`: the admissible slice set is nonempty and the tensor has unit
`ℓ¹` norm, so the existence theorem is not vacuous. -/
example : (admissible (r := 1) 3).Nonempty := admissible_nonempty (by norm_num) (by norm_num)

example : ∑ x : Fin 1 → Fin 4, |prodKappa x| = 1 := prodKappa_l1

example : ∑ x : Fin 3 → Fin 4, |prodKappa x| = 1 := prodKappa_l1

/-- The local kernel really is nonzero and really has the claimed norm. -/
example : ∑ u, |kappa u| = 1 ∧ ∑ u, kappa u = 0 := ⟨kappa_l1, kappa_total⟩

/-- Concrete `q = 5` (`r = 2`) instance of the slice cancellation at a row of total order
`3 < 4 = q-1`. -/
example (s : Fin 2 → ℕ) :
    ∑ x : Fin 2 → Fin 4,
      prodKappa x * (((1:ℕ).descFactorial 1 : ℚ) *
        prodRow s (fun c => if c = 0 then (2, 0) else (0, 0)) x) = 0 := by
  refine slice_annihilation (by norm_num) s 1 _ ?_
  simp [Fin.sum_univ_two]

#print axioms kappa_annihilates
#print axioms prodKappa_l1
#print axioms prodKappa_moment
#print axioms slice_annihilation
#print axioms prodKappa_endpoint_swap
#print axioms prodKappa_perm
#print axioms admissible_nonempty
#print axioms mixture_l1_and_annihilation
#print axioms pair_tensor

end KsumAudit.Obstructions.PairTensor
