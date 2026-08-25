/-
`KsumAudit/T2KFloor.lean` — tier **T2**, the `k`-floor combinatorial cores.

Proof-DAG node: `KSUM.LEAN.T2.rosmanis-kfloor` (registered OPEN under rule 8a, 2026-07-30).

Manuscript targets (`ksum/paper/ksum_small_alphabet.tex`, appendix `app:k3`):

  `lem:core`          core well-formedness
  `prop:core-even`    the reduction identity, even live count
  `lem:core-odd`      the parity step: one parked coordinate
  `lem:transl-cover`  the translation identity and the window/coset covering (combinatorial half)

Everything in this file is finite arithmetic: there is **no `QueryModel`** here, so every theorem
of this module is UNCONDITIONAL.  The query-complexity half of `lem:transl-cover` lives in
`KSUM/A1c.lean`, where the interface is available.

House rules: no `sorry`, no `axiom`, no `native_decide`.
-/
import KsumAudit.MainLine
import Mathlib.Data.Fin.Embedding
import Mathlib.Data.Finset.Fin
import Mathlib.Algebra.BigOperators.Fin

namespace KsumAudit
namespace KFloor

open Finset

/-! ## 1. Splitting a `k`-subset of an appended string

A `k`-subset `S` of the `2n + m` positions of `Fin.append (live) (core)` decomposes into its live
part and its core part.  These two lemmas are the bookkeeping behind the phrase *"a `k`-subset `S`
of positions uses a subset `A` of the core and `ℓ = k - a` live coordinates"* in the proof of
`prop:core-even`. -/

/-- The live positions selected by `S`. -/
def livePart {N M : ℕ} (S : Finset (Fin (N + M))) : Finset (Fin N) :=
  Finset.univ.filter fun i : Fin N => Fin.castAdd M i ∈ S

/-- The core positions selected by `S`. -/
def corePart {N M : ℕ} (S : Finset (Fin (N + M))) : Finset (Fin M) :=
  Finset.univ.filter fun j : Fin M => Fin.natAdd N j ∈ S

@[simp] theorem mem_livePart {N M : ℕ} (S : Finset (Fin (N + M))) (i : Fin N) :
    i ∈ livePart S ↔ Fin.castAdd M i ∈ S := by simp [livePart]

@[simp] theorem mem_corePart {N M : ℕ} (S : Finset (Fin (N + M))) (j : Fin M) :
    j ∈ corePart S ↔ Fin.natAdd N j ∈ S := by simp [corePart]

/-- The sum over `S` splits as live sum plus core sum. -/
theorem sum_append_split {G : Type*} [AddCommMonoid G] {N M : ℕ}
    (f : Fin N → G) (g : Fin M → G) (S : Finset (Fin (N + M))) :
    ∑ p ∈ S, Fin.append f g p
      = (∑ i ∈ livePart S, f i) + ∑ j ∈ corePart S, g j := by
  classical
  have key : ∑ p ∈ S, Fin.append f g p
      = ∑ p : Fin (N + M), (if p ∈ S then Fin.append f g p else 0) := by
    rw [Finset.sum_ite_mem, Finset.univ_inter]
  rw [key, Fin.sum_univ_add, livePart, corePart, Finset.sum_filter, Finset.sum_filter]
  congr 1
  · refine Finset.sum_congr rfl fun i _ => ?_
    by_cases h : Fin.castAdd M i ∈ S <;> simp [h, Fin.append_left]
  · refine Finset.sum_congr rfl fun j _ => ?_
    by_cases h : Fin.natAdd N j ∈ S <;> simp [h, Fin.append_right]

/-- The cardinality of `S` splits the same way. -/
theorem card_append_split {N M : ℕ} (S : Finset (Fin (N + M))) :
    S.card = (livePart S).card + (corePart S).card := by
  classical
  have key : (S.card : ℕ) = ∑ p : Fin (N + M), (if p ∈ S then 1 else 0) := by
    rw [Finset.sum_ite_mem, Finset.univ_inter, Finset.sum_const, smul_eq_mul, mul_one]
  rw [key, Fin.sum_univ_add, livePart, corePart, Finset.card_filter, Finset.card_filter]

/-! ## 2. The frozen core (`sec:k3` items (a) and (c), `lem:core`)

The manuscript's core is `c_i = U` for `i ≤ k-3` and `c_{k-2} = t - (k-3)U`.  We instantiate at the
**base window target** `t₀ := (k-2)U`, the left endpoint of both `W_even` and `W_odd`; at that
target `c_{k-2} = (k-2)U - (k-3)U = U` as well, so the core is the constant vector `U` of length
`k-2`.  This is the manuscript's construction, not a different one: it is the manuscript's core
evaluated at one particular admissible target, and `lem:transl-cover` is what moves the result to
the remaining targets. -/

/-- `U = kK + 1`, the core unit of `sec:k3` item (a). -/
def coreUnit (k κ : ℕ) : ℕ := k * κ + 1

/-- The base window target `t₀ = (k-2)U`, the left endpoint of both `W_even` and `W_odd`. -/
def baseTarget (k κ : ℕ) : ℕ := (k - 2) * coreUnit k κ

/-- The parked value `v = t + (k-1)K + 1` of `sec:k3` item (c), at `t = t₀`. -/
def parkedVal (k κ : ℕ) : ℕ := baseTarget k κ + ((k - 1) * κ + 1)

/-- The frozen block of `m ∈ {k-2, k-1}` coordinates: the `k-2` core coordinates all carry `U`,
and — in the odd case `m = k-1` — the last one carries the parked value `v`. -/
def coreVec (k κ q m : ℕ) : Fin m → ZMod q :=
  fun j => if (j : ℕ) < k - 2 then ((coreUnit k κ : ℕ) : ZMod q) else ((parkedVal k κ : ℕ) : ZMod q)

/-- **The frozen block at a general window target** `t = t₀ + r` (added 2026-07-30 by the
`R-A1-1`/`R-A1-3` repair batch).  This is the manuscript's core verbatim — `c_i = U` for
`i ≤ k-3` and `c_{k-2} = t - (k-3)U`, plus the parked value `v = t + (k-1)K + 1` when `m = k-1` —
written at `t = t₀ + r`, where `t - (k-3)U = (k-2)U + r - (k-3)U = U + r`.

`coreVecAt … 0 = coreVec …` (`coreVecAt_zero`), so the base-target development is the `r = 0`
case of this one and nothing proved earlier is weakened. -/
def coreVecAt (k κ q m r : ℕ) : Fin m → ZMod q :=
  fun j =>
    if (j : ℕ) + 1 < k - 2 then ((coreUnit k κ : ℕ) : ZMod q)
    else if (j : ℕ) < k - 2 then ((coreUnit k κ + r : ℕ) : ZMod q)
    else ((parkedVal k κ + r : ℕ) : ZMod q)

/-- At `r = 0` the general core is the base-target core, definitionally on each branch. -/
theorem coreVecAt_zero (k κ q m : ℕ) : coreVecAt k κ q m 0 = coreVec k κ q m := by
  funext j
  simp only [coreVecAt, coreVec, Nat.add_zero]
  by_cases h1 : (j : ℕ) + 1 < k - 2
  · rw [if_pos h1, if_pos (show (j : ℕ) < k - 2 by omega)]
  · rw [if_neg h1]

/-- The `k-2` genuine core positions inside `Fin m`. -/
def coreIdx (k m : ℕ) (h : k - 2 ≤ m) : Finset (Fin m) :=
  (Finset.range (k - 2)).attachFin (fun _ hi => lt_of_lt_of_le (Finset.mem_range.mp hi) h)

@[simp] theorem mem_coreIdx {k m : ℕ} (h : k - 2 ≤ m) (j : Fin m) :
    j ∈ coreIdx k m h ↔ (j : ℕ) < k - 2 := by
  simp [coreIdx, Finset.mem_attachFin]

@[simp] theorem card_coreIdx {k m : ℕ} (h : k - 2 ≤ m) : (coreIdx k m h).card = k - 2 := by
  simp [coreIdx, Finset.card_attachFin]

/-- **`lem:core` at the base target.**  The whole core sums to `t₀ = (k-2)U`. -/
theorem sum_coreIdx {k κ q m : ℕ} (h : k - 2 ≤ m) :
    ∑ j ∈ coreIdx k m h, coreVec k κ q m j = ((baseTarget k κ : ℕ) : ZMod q) := by
  classical
  have hconst : ∀ j ∈ coreIdx k m h, coreVec k κ q m j = ((coreUnit k κ : ℕ) : ZMod q) := by
    intro j hj
    simp only [mem_coreIdx] at hj
    simp only [coreVec, if_pos hj]
  rw [Finset.sum_congr rfl hconst, Finset.sum_const, card_coreIdx, nsmul_eq_mul, baseTarget]
  push_cast
  ring

/-- **`lem:core` at a general window target.**  The whole core sums to `t = t₀ + r`: the first
`k-3` entries carry `U`, the last one carries `U + r`. -/
theorem sum_coreIdxAt {k κ q m r : ℕ} (hk : 3 ≤ k) (h : k - 2 ≤ m) :
    ∑ j ∈ coreIdx k m h, coreVecAt k κ q m r j = ((baseTarget k κ + r : ℕ) : ZMod q) := by
  classical
  set S := coreIdx k m h with hS
  set S₀ := S.filter (fun z : Fin m => (z : ℕ) + 1 < k - 2) with hS0
  set S₁ := S.filter (fun z : Fin m => ¬ ((z : ℕ) + 1 < k - 2)) with hS1
  -- `S₁` is the single last core position `k-3`
  have hlast : (k - 3) < m := by omega
  have hS1eq : S₁ = {(⟨k - 3, hlast⟩ : Fin m)} := by
    ext z
    simp only [hS1, hS, Finset.mem_filter, mem_coreIdx, Finset.mem_singleton]
    constructor
    · rintro ⟨hz1, hz2⟩
      apply Fin.ext
      show (z : ℕ) = k - 3
      omega
    · rintro rfl
      refine ⟨?_, ?_⟩
      · show (k - 3 : ℕ) < k - 2
        omega
      · show ¬ ((k - 3 : ℕ) + 1 < k - 2)
        omega
  have hcard1 : S₁.card = 1 := by rw [hS1eq]; simp
  have hcard0 : S₀.card = k - 3 := by
    have hsplit : S₀.card + S₁.card = S.card := Finset.card_filter_add_card_filter_not _
    have hSc : S.card = k - 2 := by rw [hS]; exact card_coreIdx h
    omega
  have hsum0 : ∑ j ∈ S₀, coreVecAt k κ q m r j
      = (S₀.card : ZMod q) * ((coreUnit k κ : ℕ) : ZMod q) := by
    have hc : ∀ z ∈ S₀, coreVecAt k κ q m r z = ((coreUnit k κ : ℕ) : ZMod q) := by
      intro z hz
      simp only [hS0, Finset.mem_filter] at hz
      simp only [coreVecAt, if_pos hz.2]
    rw [Finset.sum_congr rfl hc, Finset.sum_const, nsmul_eq_mul]
  have hsum1 : ∑ j ∈ S₁, coreVecAt k κ q m r j
      = (S₁.card : ZMod q) * ((coreUnit k κ + r : ℕ) : ZMod q) := by
    have hc : ∀ z ∈ S₁, coreVecAt k κ q m r z = ((coreUnit k κ + r : ℕ) : ZMod q) := by
      intro z hz
      simp only [hS1, hS, Finset.mem_filter, mem_coreIdx] at hz
      simp only [coreVecAt, if_neg hz.2, if_pos hz.1]
    rw [Finset.sum_congr rfl hc, Finset.sum_const, nsmul_eq_mul]
  have hnat : (k - 3) * coreUnit k κ + (coreUnit k κ + r) = baseTarget k κ + r := by
    have h3 : k - 2 = (k - 3) + 1 := by omega
    simp only [baseTarget, h3]
    ring
  calc ∑ j ∈ S, coreVecAt k κ q m r j
      = ∑ j ∈ S₀, coreVecAt k κ q m r j + ∑ j ∈ S₁, coreVecAt k κ q m r j := by
        rw [hS0, hS1, Finset.sum_filter_add_sum_filter_not]
    _ = ((k - 3 : ℕ) : ZMod q) * ((coreUnit k κ : ℕ) : ZMod q)
          + (1 : ZMod q) * ((coreUnit k κ + r : ℕ) : ZMod q) := by
        rw [hsum0, hsum1, hcard0, hcard1]; push_cast; ring
    _ = (((k - 3) * coreUnit k κ + (coreUnit k κ + r) : ℕ) : ZMod q) := by push_cast; ring
    _ = ((baseTarget k κ + r : ℕ) : ZMod q) := by rw [hnat]

/-- **`lem:core`, the manuscript's statement of core well-formedness, at the base target.**
Every core coordinate is `≥ U`; every nonempty subset of the core has integer sum in `[U, t₀]`;
and the sum equals `t₀` exactly when the subset is the whole core. -/
theorem core_wellformed {k κ : ℕ} (_hk : 3 ≤ k) (a : ℕ) (ha : a ≤ k - 2) :
    (0 < a → coreUnit k κ ≤ a * coreUnit k κ ∧ a * coreUnit k κ ≤ baseTarget k κ) ∧
      (a * coreUnit k κ = baseTarget k κ ↔ a = k - 2) := by
  have hU : 0 < coreUnit k κ := by simp [coreUnit]
  refine ⟨fun hapos => ⟨?_, ?_⟩, ?_, ?_⟩
  · exact Nat.le_mul_of_pos_left _ hapos
  · exact Nat.mul_le_mul_right _ ha
  · intro h
    rw [baseTarget] at h
    exact Nat.eq_of_mul_eq_mul_right hU h
  · rintro rfl; rfl

/-! ## 3. The signed value of a live coordinate (`app:k3`, opening paragraph)

*"A live value is stored as `f(i) ∈ {1,…,K}` or as `q - g(j) ≡ -g(j)`; the integer signed value of
a live coordinate therefore lies in `[-K,K] \ {0}`."* -/

/-- The integer signed value of live position `p`. -/
def signedVal {n κ : ℕ} (y : Fin (2 * n) → Fin κ) (p : Fin (2 * n)) : ℤ :=
  if (p : ℕ) < n then ((y p : ℕ) : ℤ) + 1 else -(((y p : ℕ) : ℤ) + 1)

theorem encode_cyc_eq_intCast {n κ : ℕ} (q : ℕ) (y : Fin (2 * n) → Fin κ) (p : Fin (2 * n)) :
    encode n (cyc q κ) y p = ((signedVal y p : ℤ) : ZMod q) := by
  simp only [encode, encMap, cyc, signedVal]
  by_cases h : (p : ℕ) < n <;> simp [h]

/-- `|signed value| ≤ K`. -/
theorem abs_signedVal_le {n κ : ℕ} (y : Fin (2 * n) → Fin κ) (p : Fin (2 * n)) :
    |signedVal y p| ≤ (κ : ℤ) := by
  have h1 : ((y p : ℕ) : ℤ) + 1 ≤ (κ : ℤ) := by
    have := (y p).isLt
    omega
  have h0 : (0 : ℤ) ≤ ((y p : ℕ) : ℤ) := Int.natCast_nonneg _
  simp only [signedVal]
  by_cases hp : (p : ℕ) < n
  · rw [if_pos hp, abs_le]; omega
  · rw [if_neg hp, abs_le]; omega

/-- `|S_live| ≤ ℓ·K`, the bound used in every case of `prop:core-even` and `lem:core-odd`. -/
theorem abs_live_sum_le {n κ : ℕ} (y : Fin (2 * n) → Fin κ) (Sl : Finset (Fin (2 * n))) :
    |∑ i ∈ Sl, signedVal y i| ≤ (Sl.card : ℤ) * (κ : ℤ) := by
  calc |∑ i ∈ Sl, signedVal y i| ≤ ∑ i ∈ Sl, |signedVal y i| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ _i ∈ Sl, (κ : ℤ) := Finset.sum_le_sum fun i _ => abs_signedVal_le y i
    _ = (Sl.card : ℤ) * (κ : ℤ) := by rw [Finset.sum_const, nsmul_eq_mul]

theorem live_sum_cast {n κ q : ℕ} (y : Fin (2 * n) → Fin κ) (Sl : Finset (Fin (2 * n))) :
    ∑ i ∈ Sl, encode n (cyc q κ) y i = (((∑ i ∈ Sl, signedVal y i : ℤ)) : ZMod q) := by
  rw [Int.cast_sum]
  exact Finset.sum_congr rfl fun i _ => encode_cyc_eq_intCast q y i

/-! ## 4. `prop:core-even` and `lem:core-odd`, in one statement

The two manuscript statements differ only in the size `m` of the frozen block (`k-2` without the
parked coordinate, `k-1` with it) and in which window the target must lie in.  At the base target
`t₀ = (k-2)U` the *odd* window condition `q ≥ (k²-2)K + 2k-1` implies the even one, so a single
theorem covers both, quantified over `k-2 ≤ m ≤ k-1`. -/

set_option maxHeartbeats 2000000 in
/-- **`prop:core-even` + `lem:core-odd`, AT EVERY WINDOW TARGET.**
*(Repair batch 2026-07-30, review findings R-A1-1 / R-A1-3; the base-target-only version is now
the `r = 0` corollary `core_reduction` below.)*

With the frozen block `coreVecAt` of size `m ∈ {k-2, k-1}` and **any** window target
`t = t₀ + r` with `r < k` — `t₀ = (k-2)(kK+1)` being the left endpoint of `W_even` and `W_odd`,
and `[t₀, t₀+k)` the `k` consecutive residues `lem:transl-cover` covers each coset with —
`k`-Sum on the `2n + m` coordinates of the encoded live block agrees with `2`-Sum at target `0`
on the `2n` live coordinates.  Composed with `lem:encode` (`KsumAudit.twoSum_encode_cyc`) this is
exactly the manuscript's `kSum_{Z_q,t,N}(x) = Claw_{m→K}(f,g)`.

**The window hypothesis is unchanged.**  `(k²-2)K + 2k-1 ≤ q` is exactly the master inequality at
the RIGHTMOST window target `r = k-1` (it is tight there: the two sides differ by `0`), so all
four case bounds go through at every window target with the same modulus condition — which is
also why `lem:transl-cover`(ii) and `lem:core-odd` carry the same threshold in the manuscript. -/
theorem core_reduction_at {k q n m κ r : ℕ} [NeZero q]
    (hk : 3 ≤ k) (hm1 : k - 2 ≤ m) (hm2 : m ≤ k - 1)
    (hwin : (k ^ 2 - 2) * κ + 2 * k - 1 ≤ q) (hr : r < k)
    (y : Fin (2 * n) → Fin κ) :
    kSum (ZMod q) k ((baseTarget k κ + r : ℕ) : ZMod q) (2 * n + m)
        (Fin.append (encode n (cyc q κ) y) (coreVecAt k κ q m r))
      = twoSum (ZMod q) 0 (2 * n) (encode n (cyc q κ) y) := by
  classical
  obtain ⟨j, rfl⟩ : ∃ j, k = j + 3 := ⟨k - 3, by omega⟩
  -- normalise the truncated subtractions
  have e2 : j + 3 - 2 = j + 1 := by omega
  have e1 : j + 3 - 1 = j + 2 := by omega
  have hwin' : (j ^ 2 + 6 * j + 7) * κ + (2 * j + 5) ≤ q := by
    have h9 : (j + 3) ^ 2 - 2 = j ^ 2 + 6 * j + 7 := by
      have hsq : (j + 3) ^ 2 = j ^ 2 + 6 * j + 9 := by ring
      omega
    rw [h9] at hwin
    omega
  -- the master inequality, over ℤ — now carrying the window offset `r ≤ k-1`
  have hjz : (0 : ℤ) ≤ (j : ℤ) := Int.natCast_nonneg _
  have hκz : (0 : ℤ) ≤ (κ : ℤ) := Int.natCast_nonneg _
  have hrz : (0 : ℤ) ≤ (r : ℤ) := Int.natCast_nonneg _
  have hrleN : r ≤ j + 2 := by omega
  have hrle : (r : ℤ) ≤ (j : ℤ) + 2 := by exact_mod_cast hrleN
  have hwinZ : ((j : ℤ) ^ 2 + 6 * j + 7) * (κ : ℤ) + (2 * j + 5) ≤ (q : ℤ) := by exact_mod_cast hwin'
  have hUq : ((coreUnit (j + 3) κ : ℕ) : ZMod q)
      = (((j : ℕ) : ZMod q) + 3) * ((κ : ℕ) : ZMod q) + 1 := by
    simp only [coreUnit]; push_cast; ring
  have hTq : ((baseTarget (j + 3) κ + r : ℕ) : ZMod q)
      = (((j : ℕ) : ZMod q) + 1) * ((((j : ℕ) : ZMod q) + 3) * ((κ : ℕ) : ZMod q) + 1)
        + ((r : ℕ) : ZMod q) := by
    simp only [baseTarget, coreUnit, e2]; push_cast; ring
  have hVq : ((parkedVal (j + 3) κ + r : ℕ) : ZMod q)
      = (((j : ℕ) : ZMod q) + 1) * ((((j : ℕ) : ZMod q) + 3) * ((κ : ℕ) : ZMod q) + 1)
        + ((((j : ℕ) : ZMod q) + 2) * ((κ : ℕ) : ZMod q) + 1) + ((r : ℕ) : ZMod q) := by
    simp only [parkedVal, baseTarget, coreUnit, e1, e2]; push_cast; ring
  have hUpos : (0 : ℤ) ≤ ((j : ℤ) + 3) * (κ : ℤ) + 1 := by nlinarith
  have hmaster : ((j : ℤ) + 1) * (((j : ℤ) + 3) * (κ : ℤ) + 1) + (r : ℤ)
      + 2 * ((j : ℤ) + 2) * (κ : ℤ) + 2 ≤ (q : ℤ) := by nlinarith [hwinZ, hjz, hκz, hrle]
  refine decide_eq_decide.mpr ⟨?_, ?_⟩
  · -- FORWARD: a `k`-subset hitting `t` forces the good pattern, hence a live pair summing to `0`
    rintro ⟨S, hcard, hsum⟩
    set Sl := livePart S with hSl
    set Sc := corePart S with hSc
    set A := Sc.filter (fun z : Fin m => (z : ℕ) < j + 1) with hA
    set B := Sc.filter (fun z : Fin m => ¬ ((z : ℕ) < j + 1)) with hB
    -- inside the core, the LAST position (index `k-3 = j`) is the one carrying `U + r`
    set A₀ := A.filter (fun z : Fin m => (z : ℕ) + 1 < j + 1) with hA0
    set A₁ := A.filter (fun z : Fin m => ¬ ((z : ℕ) + 1 < j + 1)) with hA1
    have hcards : Sl.card + Sc.card = j + 3 := by rw [← hcard, card_append_split]
    have hAB : A.card + B.card = Sc.card := Finset.card_filter_add_card_filter_not _
    have hA01 : A₀.card + A₁.card = A.card := Finset.card_filter_add_card_filter_not _
    have hm1' : j + 1 ≤ m := by omega
    have hAle : A.card ≤ j + 1 := by
      have hsub : A ⊆ coreIdx (j + 3) m hm1 := by
        intro z hz
        simp only [hA, Finset.mem_filter] at hz
        simp only [mem_coreIdx, e2]
        exact hz.2
      have hcc := Finset.card_le_card hsub
      rwa [card_coreIdx, e2] at hcc
    have hA0le : A₀.card ≤ j := by
      have hsub : A₀ ⊆ coreIdx (j + 2) m (by omega) := by
        intro z hz
        simp only [hA0, Finset.mem_filter] at hz
        obtain ⟨-, hz2⟩ := hz
        simp only [mem_coreIdx]
        omega
      have hcc := Finset.card_le_card hsub
      rw [card_coreIdx] at hcc
      omega
    have hA1le : A₁.card ≤ 1 := by
      refine Finset.card_le_one.mpr fun z hz w hw => ?_
      simp only [hA1, hA, Finset.mem_filter, not_lt] at hz hw
      obtain ⟨⟨-, hz1⟩, hz2⟩ := hz
      obtain ⟨⟨-, hw1⟩, hw2⟩ := hw
      exact Fin.ext (by omega)
    have hBle : B.card ≤ 1 := by
      refine Finset.card_le_one.mpr fun z hz w hw => ?_
      simp only [hB, Finset.mem_filter, not_lt] at hz hw
      have hz2 : (z : ℕ) < m := z.isLt
      have hw2 : (w : ℕ) < m := w.isLt
      exact Fin.ext (by omega)
    -- the core sum: `a·U + ε·r` on the genuine core (`ε = 1` iff the last core position is used),
    -- `b·(v + r)` on the parked coordinate
    have hA0sum : ∑ z ∈ A₀, coreVecAt (j + 3) κ q m r z
        = (A₀.card : ZMod q) * ((coreUnit (j + 3) κ : ℕ) : ZMod q) := by
      have hc : ∀ z ∈ A₀, coreVecAt (j + 3) κ q m r z = ((coreUnit (j + 3) κ : ℕ) : ZMod q) := by
        intro z hz
        simp only [hA0, Finset.mem_filter] at hz
        obtain ⟨-, hz2⟩ := hz
        have hyes : (z : ℕ) + 1 < j + 3 - 2 := by rw [e2]; exact hz2
        simp only [coreVecAt, if_pos hyes]
      rw [Finset.sum_congr rfl hc, Finset.sum_const, nsmul_eq_mul]
    have hA1sum : ∑ z ∈ A₁, coreVecAt (j + 3) κ q m r z
        = (A₁.card : ZMod q) * ((coreUnit (j + 3) κ + r : ℕ) : ZMod q) := by
      have hc : ∀ z ∈ A₁,
          coreVecAt (j + 3) κ q m r z = ((coreUnit (j + 3) κ + r : ℕ) : ZMod q) := by
        intro z hz
        simp only [hA1, hA, Finset.mem_filter, not_lt] at hz
        obtain ⟨⟨-, hz1⟩, hz2⟩ := hz
        have hno : ¬ ((z : ℕ) + 1 < j + 3 - 2) := by rw [e2]; omega
        have hyes : (z : ℕ) < j + 3 - 2 := by rw [e2]; exact hz1
        simp only [coreVecAt, if_neg hno, if_pos hyes]
      rw [Finset.sum_congr rfl hc, Finset.sum_const, nsmul_eq_mul]
    have hAsum : ∑ z ∈ A, coreVecAt (j + 3) κ q m r z
        = (A.card : ZMod q) * ((coreUnit (j + 3) κ : ℕ) : ZMod q)
          + (A₁.card : ZMod q) * ((r : ℕ) : ZMod q) := by
      have hsplit : ∑ z ∈ A, coreVecAt (j + 3) κ q m r z
          = ∑ z ∈ A₀, coreVecAt (j + 3) κ q m r z + ∑ z ∈ A₁, coreVecAt (j + 3) κ q m r z := by
        rw [hA0, hA1, Finset.sum_filter_add_sum_filter_not]
      rw [hsplit, hA0sum, hA1sum, ← hA01]
      push_cast
      ring
    have hBsum : ∑ z ∈ B, coreVecAt (j + 3) κ q m r z
        = (B.card : ZMod q) * ((parkedVal (j + 3) κ + r : ℕ) : ZMod q) := by
      have hc : ∀ z ∈ B,
          coreVecAt (j + 3) κ q m r z = ((parkedVal (j + 3) κ + r : ℕ) : ZMod q) := by
        intro z hz
        simp only [hB, Finset.mem_filter, not_lt] at hz
        have hno : ¬ ((z : ℕ) < j + 3 - 2) := by rw [e2]; omega
        have hno' : ¬ ((z : ℕ) + 1 < j + 3 - 2) := by rw [e2]; omega
        simp only [coreVecAt, if_neg hno', if_neg hno]
      rw [Finset.sum_congr rfl hc, Finset.sum_const, nsmul_eq_mul]
    have hSCsum : ∑ z ∈ Sc, coreVecAt (j + 3) κ q m r z
        = (A.card : ZMod q) * ((coreUnit (j + 3) κ : ℕ) : ZMod q)
          + (A₁.card : ZMod q) * ((r : ℕ) : ZMod q)
          + (B.card : ZMod q) * ((parkedVal (j + 3) κ + r : ℕ) : ZMod q) := by
      rw [← hAsum, ← hBsum, hA, hB, Finset.sum_filter_add_sum_filter_not]
    rw [sum_append_split, live_sum_cast, hSCsum] at hsum
    set Z : ℤ := ∑ i ∈ Sl, signedVal y i with hZ
    have habs : |Z| ≤ (Sl.card : ℤ) * (κ : ℤ) := abs_live_sum_le y Sl
    have hZle : Z ≤ (Sl.card : ℤ) * (κ : ℤ) := (abs_le.mp habs).2
    have hZge : -((Sl.card : ℤ) * (κ : ℤ)) ≤ Z := (abs_le.mp habs).1
    have hAz : (0 : ℤ) ≤ (A.card : ℤ) := Int.natCast_nonneg _
    have hAzle : (A.card : ℤ) ≤ (j : ℤ) + 1 := by exact_mod_cast hAle
    have hεnn : (0 : ℤ) ≤ (A₁.card : ℤ) := Int.natCast_nonneg _
    have hεle : (A₁.card : ℤ) ≤ 1 := by exact_mod_cast hA1le
    have hεr : (0 : ℤ) ≤ (A₁.card : ℤ) * (r : ℤ) := mul_nonneg hεnn hrz
    have hεrle : (A₁.card : ℤ) * (r : ℤ) ≤ (r : ℤ) := by nlinarith
    -- the single integer divisibility, in the manuscript's shape:
    -- `Z + (a + (b-1)(k-2))·U + (ε + b - 1)·r + b·((k-1)K+1) ≡ 0 (mod q)`
    have hdvd : (q : ℤ) ∣ (Z + ((A.card : ℤ) + ((B.card : ℤ) - 1) * ((j : ℤ) + 1))
        * (((j : ℤ) + 3) * (κ : ℤ) + 1)
        + ((A₁.card : ℤ) + (B.card : ℤ) - 1) * (r : ℤ)
        + (B.card : ℤ) * (((j : ℤ) + 2) * (κ : ℤ) + 1)) := by
      rw [hUq, hVq, hTq] at hsum
      rw [← ZMod.intCast_zmod_eq_zero_iff_dvd]
      push_cast
      linear_combination hsum
    -- split on whether the parked coordinate is used
    have hBcases : B.card = 0 ∨ B.card = 1 := by omega
    rcases hBcases with hBc | hBc
    · -- the parked coordinate is NOT used
      rw [hBc] at hdvd hAB
      have hSlz : (Sl.card : ℤ) = ((j : ℤ) + 3) - (A.card : ℤ) := by
        have : Sl.card + A.card = j + 3 := by omega
        have h' : ((Sl.card : ℤ)) + (A.card : ℤ) = (j : ℤ) + 3 := by exact_mod_cast this
        linarith
      rcases Nat.lt_or_ge A.card (j + 1) with hlt | hge
      · -- BAD PATTERN `a ≤ k-3`: no hit is possible
        exfalso
        have hAzlt : (A.card : ℤ) ≤ (j : ℤ) := by exact_mod_cast Nat.lt_succ_iff.mp hlt
        set E : ℤ := ((j : ℤ) + 1) - (A.card : ℤ) with hE
        have hE1 : (1 : ℤ) ≤ E := by simp only [hE]; linarith
        have hEle : E ≤ (j : ℤ) + 1 := by simp only [hE]; linarith
        have hSlE : (Sl.card : ℤ) = E + 2 := by simp only [hE]; linarith
        have hw : (q : ℤ) ∣ (E * (((j : ℤ) + 3) * (κ : ℤ) + 1)
            + (1 - (A₁.card : ℤ)) * (r : ℤ) - Z) := by
          have hneg := (dvd_neg (α := ℤ)).mpr hdvd
          have hrw : -(Z + ((A.card : ℤ) + (((0 : ℕ) : ℤ) - 1) * ((j : ℤ) + 1))
              * (((j : ℤ) + 3) * (κ : ℤ) + 1)
              + ((A₁.card : ℤ) + ((0 : ℕ) : ℤ) - 1) * (r : ℤ)
              + ((0 : ℕ) : ℤ) * (((j : ℤ) + 2) * (κ : ℤ) + 1))
              = E * (((j : ℤ) + 3) * (κ : ℤ) + 1) + (1 - (A₁.card : ℤ)) * (r : ℤ) - Z := by
            simp only [hE]; push_cast; ring
          rwa [hrw] at hneg
        have hZupper : Z ≤ (E + 2) * (κ : ℤ) := by rw [← hSlE]; exact hZle
        have hZlower : -((E + 2) * (κ : ℤ)) ≤ Z := by rw [← hSlE]; exact hZge
        have hEprod : (0 : ℤ) ≤ (κ : ℤ) * (E * ((j : ℤ) + 2) - 2) :=
          mul_nonneg hκz (by nlinarith)
        have hpos0 : 0 < E * (((j : ℤ) + 3) * (κ : ℤ) + 1) - Z := by nlinarith
        have hrshift : (0 : ℤ) ≤ (1 - (A₁.card : ℤ)) * (r : ℤ) := mul_nonneg (by linarith) hrz
        have hrshift' : (1 - (A₁.card : ℤ)) * (r : ℤ) ≤ (r : ℤ) := by nlinarith
        have hpos : 0 < E * (((j : ℤ) + 3) * (κ : ℤ) + 1)
            + (1 - (A₁.card : ℤ)) * (r : ℤ) - Z := by linarith
        have hEU : E * (((j : ℤ) + 3) * (κ : ℤ) + 1)
            ≤ ((j : ℤ) + 1) * (((j : ℤ) + 3) * (κ : ℤ) + 1) :=
          mul_le_mul_of_nonneg_right hEle hUpos
        have hEκ : (E + 2) * (κ : ℤ) ≤ 2 * ((j : ℤ) + 2) * (κ : ℤ) :=
          mul_le_mul_of_nonneg_right (by linarith) hκz
        have hlt' : E * (((j : ℤ) + 3) * (κ : ℤ) + 1)
            + (1 - (A₁.card : ℤ)) * (r : ℤ) - Z < (q : ℤ) := by linarith
        have := Int.le_of_dvd hpos hw
        linarith
      · -- GOOD PATTERN `a = k-2`: the whole core is used, so `ε = 1`, `ℓ = 2`, and the live pair
        -- sums to `0`
        have hAeq : A.card = j + 1 := le_antisymm hAle hge
        have hA1eq : A₁.card = 1 := by omega
        have hSl2 : Sl.card = 2 := by omega
        have hZ0 : (q : ℤ) ∣ Z := by
          have hrw : Z + ((A.card : ℤ) + (((0 : ℕ) : ℤ) - 1) * ((j : ℤ) + 1))
              * (((j : ℤ) + 3) * (κ : ℤ) + 1)
              + ((A₁.card : ℤ) + ((0 : ℕ) : ℤ) - 1) * (r : ℤ)
              + ((0 : ℕ) : ℤ) * (((j : ℤ) + 2) * (κ : ℤ) + 1) = Z := by
            rw [hAeq, hA1eq]; push_cast; ring
          rwa [hrw] at hdvd
        refine ⟨Sl, hSl2, ?_⟩
        rw [live_sum_cast, ← hZ]
        exact (ZMod.intCast_zmod_eq_zero_iff_dvd Z q).mpr hZ0
    · -- the parked coordinate IS used.  `lem:core-odd`: `W ∈ [1, q-1]`, so no hit.
      exfalso
      rw [hBc] at hdvd hAB
      have hSlz : (Sl.card : ℤ) ≤ (j : ℤ) + 2 := by
        have : Sl.card ≤ j + 2 := by omega
        exact_mod_cast this
      have hSlnn : (0 : ℤ) ≤ (Sl.card : ℤ) := Int.natCast_nonneg _
      -- `W = (k-1)K + 1 + Σ_A c + S_live`, the manuscript's quantity
      have hw : (q : ℤ) ∣ (Z + (A.card : ℤ) * (((j : ℤ) + 3) * (κ : ℤ) + 1)
          + (A₁.card : ℤ) * (r : ℤ) + (((j : ℤ) + 2) * (κ : ℤ) + 1)) := by
        have hrw : Z + ((A.card : ℤ) + (((1 : ℕ) : ℤ) - 1) * ((j : ℤ) + 1))
            * (((j : ℤ) + 3) * (κ : ℤ) + 1)
            + ((A₁.card : ℤ) + ((1 : ℕ) : ℤ) - 1) * (r : ℤ)
            + ((1 : ℕ) : ℤ) * (((j : ℤ) + 2) * (κ : ℤ) + 1)
            = Z + (A.card : ℤ) * (((j : ℤ) + 3) * (κ : ℤ) + 1)
              + (A₁.card : ℤ) * (r : ℤ) + (((j : ℤ) + 2) * (κ : ℤ) + 1) := by push_cast; ring
        rwa [hrw] at hdvd
      have hSlκ : (Sl.card : ℤ) * (κ : ℤ) ≤ ((j : ℤ) + 2) * (κ : ℤ) :=
        mul_le_mul_of_nonneg_right hSlz hκz
      have haU0 : (0 : ℤ) ≤ (A.card : ℤ) * (((j : ℤ) + 3) * (κ : ℤ) + 1) := mul_nonneg hAz hUpos
      have haU1 : (A.card : ℤ) * (((j : ℤ) + 3) * (κ : ℤ) + 1)
          ≤ ((j : ℤ) + 1) * (((j : ℤ) + 3) * (κ : ℤ) + 1) :=
        mul_le_mul_of_nonneg_right hAzle hUpos
      have hWpos : 0 < Z + (A.card : ℤ) * (((j : ℤ) + 3) * (κ : ℤ) + 1)
          + (A₁.card : ℤ) * (r : ℤ) + (((j : ℤ) + 2) * (κ : ℤ) + 1) := by linarith
      have hWlt : Z + (A.card : ℤ) * (((j : ℤ) + 3) * (κ : ℤ) + 1)
          + (A₁.card : ℤ) * (r : ℤ) + (((j : ℤ) + 2) * (κ : ℤ) + 1) < (q : ℤ) := by linarith
      have := Int.le_of_dvd hWpos hw
      linarith
  · -- BACKWARD: a live pair summing to `0` plus the whole core is a `k`-subset hitting `t`
    rintro ⟨S', hcard2, hsum0⟩
    have hdisj : Disjoint (S'.map (Fin.castAddEmb m))
        ((coreIdx (j + 3) m hm1).map (Fin.natAddEmb (2 * n))) := by
      rw [Finset.disjoint_left]
      rintro z hz hz'
      simp only [Finset.mem_map, Fin.castAddEmb_apply, Fin.natAddEmb_apply] at hz hz'
      obtain ⟨i, _, hi⟩ := hz
      obtain ⟨w, _, hw⟩ := hz'
      have h1 : (z : ℕ) < 2 * n := by rw [← hi]; exact i.isLt
      have h2 : (z : ℕ) = 2 * n + (w : ℕ) := by rw [← hw]; rfl
      omega
    refine ⟨(S'.map (Fin.castAddEmb m)) ∪ ((coreIdx (j + 3) m hm1).map (Fin.natAddEmb (2 * n))),
      ?_, ?_⟩
    · rw [Finset.card_union_of_disjoint hdisj, Finset.card_map, Finset.card_map, hcard2,
        card_coreIdx, e2]
      omega
    · rw [Finset.sum_union hdisj, Finset.sum_map, Finset.sum_map]
      simp only [Fin.castAddEmb_apply, Fin.natAddEmb_apply, Fin.append_left, Fin.append_right]
      rw [hsum0, sum_coreIdxAt hk hm1, zero_add]

/-- **`prop:core-even` + `lem:core-odd` at the BASE window target** — the `r = 0` case of
`core_reduction_at`, kept with its original statement because tier T2's witnesses and report cite
it under this name. -/
theorem core_reduction {k q n m κ : ℕ} [NeZero q]
    (hk : 3 ≤ k) (hm1 : k - 2 ≤ m) (hm2 : m ≤ k - 1)
    (hwin : (k ^ 2 - 2) * κ + 2 * k - 1 ≤ q)
    (y : Fin (2 * n) → Fin κ) :
    kSum (ZMod q) k ((baseTarget k κ : ℕ) : ZMod q) (2 * n + m)
        (Fin.append (encode n (cyc q κ) y) (coreVec k κ q m))
      = twoSum (ZMod q) 0 (2 * n) (encode n (cyc q κ) y) := by
  have h := core_reduction_at (r := 0) hk hm1 hm2 hwin (by omega) y
  rwa [coreVecAt_zero, Nat.add_zero] at h

/-! ## 5. `lem:transl-cover`: window lengths and coset covering (combinatorial half)

The manuscript's covering argument has three ingredients: the translation identity (query half,
`KSUM/A1c.lean`), the two window-length computations (i)/(ii), and the elementary observation that
a window of at least `gcd(k,q)` consecutive residues meets every coset `t + kZ_q`.

Note what the covering argument does **NOT** say: it does not relate two arbitrary targets.  It
relates a target to a *window* target **inside its own coset**.  Targets in different classes mod
`gcd(k,q)` are not compared by any argument in the manuscript — see `not_reachable_k3_q21` in
`KSUM/A1c.lean`. -/

/-- **`lem:transl-cover`(ii).**  `q ≥ (k²-2)K + 2k-1` makes `W_odd = [(k-2)(kK+1), q-2(k-1)K-2]`
contain at least `k` consecutive residues.  Written subtraction-free: `lo + (k-1) ≤ hi`. -/
theorem window_odd_length {k κ q : ℕ} (hk : 3 ≤ k) (h : (k ^ 2 - 2) * κ + 2 * k - 1 ≤ q) :
    baseTarget k κ + k + (2 * (k - 1) * κ + 2) ≤ q + 1 := by
  obtain ⟨j, rfl⟩ : ∃ j, k = j + 3 := ⟨k - 3, by omega⟩
  have h9 : (j + 3) ^ 2 - 2 = j ^ 2 + 6 * j + 7 := by
    have hsq : (j + 3) ^ 2 = j ^ 2 + 6 * j + 9 := by ring
    omega
  rw [h9] at h
  have hexp : baseTarget (j + 3) κ + (j + 3) + (2 * (j + 3 - 1) * κ + 2)
      = (j ^ 2 + 6 * j + 7) * κ + (2 * j + 6) := by
    simp only [baseTarget, coreUnit, show j + 3 - 2 = j + 1 from rfl, show j + 3 - 1 = j + 2 from rfl]
    ring
  omega

/-- **`lem:transl-cover`(i).**  The weaker even-case threshold `q ≥ (k-1)(kK+2)` already makes
`W_even = [(k-2)(kK+1), q-kK-1]` contain at least `k` consecutive residues. -/
theorem window_even_length {k κ q : ℕ} (hk : 3 ≤ k) (h : (k - 1) * (k * κ + 2) ≤ q) :
    baseTarget k κ + k + (k * κ + 1) ≤ q + 1 := by
  obtain ⟨j, rfl⟩ : ∃ j, k = j + 3 := ⟨k - 3, by omega⟩
  have hh : (j ^ 2 + 5 * j + 6) * κ + (2 * j + 4) ≤ q := by
    have : (j + 3 - 1) * ((j + 3) * κ + 2) = (j ^ 2 + 5 * j + 6) * κ + (2 * j + 4) := by
      simp only [show j + 3 - 1 = j + 2 from rfl]; ring
    omega
  have hexp : baseTarget (j + 3) κ + (j + 3) + ((j + 3) * κ + 1)
      = (j ^ 2 + 5 * j + 6) * κ + (2 * j + 5) := by
    simp only [baseTarget, coreUnit, show j + 3 - 2 = j + 1 from rfl]
    ring
  omega

/-- **`lem:transl-cover`, the covering step.**  *"`gcd(k,q) ≤ k`, and the coset `t + kZ_q` consists
of the residues `≡ t (mod gcd(k,q))`, spaced `gcd(k,q)` apart; any window of at least `gcd(k,q)`
consecutive residues contains one of them."*

Formally: for a window `[lo, lo+L)` inside `[0,q)` with `gcd(k,q) ≤ L`, every `t` admits a shift
`a` with `t + k·a` equal to an explicit window residue `s`.  No coprimality hypothesis: the
covering runs off the window LENGTH, exactly as the manuscript says. -/
theorem exists_shift_into_window {q : ℕ} [NeZero q] (k lo L : ℕ)
    (hL : Nat.gcd k q ≤ L) (_hwin : lo + L ≤ q) (t : ZMod q) :
    ∃ (a : ZMod q) (s : ℕ), lo ≤ s ∧ s < lo + L ∧ t + k • a = (s : ZMod q) := by
  have hq0 : 0 < q := Nat.pos_of_ne_zero (NeZero.ne q)
  set g := Nat.gcd k q with hg
  have hg0 : 0 < g := Nat.gcd_pos_of_pos_right k hq0
  set δ : ℕ := (t.val + g * (lo + 1) - lo) % g with hδ
  have hδlt : δ < g := Nat.mod_lt _ hg0
  set s : ℕ := lo + δ with hs
  -- (1) `s ≡ t.val (mod g)`
  have hlomul : lo ≤ t.val + g * (lo + 1) := by
    have : lo + 1 ≤ g * (lo + 1) := Nat.le_mul_of_pos_left _ hg0
    omega
  have hcong : s ≡ t.val [MOD g] := by
    have h1 : δ ≡ (t.val + g * (lo + 1) - lo) [MOD g] := Nat.mod_modEq _ _
    have h2 : lo + δ ≡ lo + (t.val + g * (lo + 1) - lo) [MOD g] := Nat.ModEq.add_left lo h1
    have h3 : lo + (t.val + g * (lo + 1) - lo) = t.val + g * (lo + 1) := by omega
    rw [h3] at h2
    refine h2.trans ?_
    show (t.val + g * (lo + 1)) % g = t.val % g
    exact Nat.add_mul_mod_self_left _ _ _
  -- (2) turn the congruence into an integer factorisation
  obtain ⟨i, hi⟩ : ∃ i : ℤ, (s : ℤ) - (t.val : ℤ) = (g : ℤ) * i := by
    have := (Nat.modEq_iff_dvd (n := g) (a := t.val) (b := s)).mp hcong.symm
    obtain ⟨i, hi⟩ := this
    exact ⟨i, by linarith⟩
  -- (3) Bezout: `g = k·u` in `ZMod q`
  have hbez : ((g : ℕ) : ZMod q) = ((k : ℕ) : ZMod q) * ((Nat.gcdA k q : ℤ) : ZMod q) := by
    have h := Nat.gcd_eq_gcd_ab k q
    have := congrArg (fun z : ℤ => ((z : ℤ) : ZMod q)) h
    push_cast at this
    simpa [ZMod.natCast_self] using this
  refine ⟨((Nat.gcdA k q * i : ℤ) : ZMod q), s, Nat.le_add_right _ _, by omega, ?_⟩
  have hval : ((t.val : ℕ) : ZMod q) = t := ZMod.natCast_rightInverse t
  have hdiff : ((s : ℕ) : ZMod q) - t = ((g : ℕ) : ZMod q) * ((i : ℤ) : ZMod q) := by
    have := congrArg (fun z : ℤ => ((z : ℤ) : ZMod q)) hi
    push_cast at this
    rw [hval] at this
    rw [this]
  rw [nsmul_eq_mul]
  have hcast : ((Nat.gcdA k q * i : ℤ) : ZMod q)
      = ((Nat.gcdA k q : ℤ) : ZMod q) * ((i : ℤ) : ZMod q) := by push_cast; ring
  rw [hcast, ← mul_assoc, ← hbez, ← hdiff]
  ring

/-! ## 6. Non-vacuity witnesses (house rule: every theorem gets one)

The smallest legal instance of `core_reduction` is `k = 3, K = 2`, where the window condition
`q ≥ (k²-2)K + 2k-1` reads `q ≥ 19 = q₀(3) = 2k²+2k-5` — so these witnesses also machine-check
that `thm:kfloor`'s floor `q₀(k)` is exactly the smallest modulus at which the construction runs
with `K = 2`.  `U = kK+1 = 7`, `t₀ = (k-2)U = 7`, parked value `v = t₀ + (k-1)K + 1 = 12`. -/

theorem witness_q0_three : (3 ^ 2 - 2) * 2 + 2 * 3 - 1 = 2 * 3 ^ 2 + 2 * 3 - 5 := by decide

theorem witness_coreUnit : coreUnit 3 2 = 7 ∧ baseTarget 3 2 = 7 ∧ parkedVal 3 2 = 12 := by
  refine ⟨rfl, rfl, rfl⟩

/-- Even case (`prop:core-even`, `m = k-2 = 1`): a claw input is a hit. -/
theorem witness_even_pos :
    kSum (ZMod 19) 3 ((baseTarget 3 2 : ℕ) : ZMod 19) (2 * 2 + 1)
      (Fin.append (encode 2 (cyc 19 2) ![0, 0, 0, 0]) (coreVec 3 2 19 1)) = true := by
  rw [core_reduction (by norm_num) (by norm_num) (by norm_num) (by norm_num),
    twoSum_encode_cyc (by norm_num)]
  decide

/-- Even case: a non-claw input is not a hit — so the identity is not the constant `true`. -/
theorem witness_even_neg :
    kSum (ZMod 19) 3 ((baseTarget 3 2 : ℕ) : ZMod 19) (2 * 2 + 1)
      (Fin.append (encode 2 (cyc 19 2) ![0, 0, 1, 1]) (coreVec 3 2 19 1)) = false := by
  rw [core_reduction (by norm_num) (by norm_num) (by norm_num) (by norm_num),
    twoSum_encode_cyc (by norm_num)]
  decide

/-- Odd case (`lem:core-odd`, `m = k-1 = 2`, i.e. the parked coordinate is present): a claw input
is a hit, and the parked coordinate has not destroyed the reduction. -/
theorem witness_odd_pos :
    kSum (ZMod 19) 3 ((baseTarget 3 2 : ℕ) : ZMod 19) (2 * 2 + 2)
      (Fin.append (encode 2 (cyc 19 2) ![0, 0, 0, 0]) (coreVec 3 2 19 2)) = true := by
  rw [core_reduction (by norm_num) (by norm_num) (by norm_num) (by norm_num),
    twoSum_encode_cyc (by norm_num)]
  decide

/-- Odd case: a non-claw input is not a hit — this is the clause that the *naive* uniform-shift
and odd-live-coordinate variants failed (they admitted unintended target-summing subsets, the two
DEAD leaves of `sec:branch-ledger`). -/
theorem witness_odd_neg :
    kSum (ZMod 19) 3 ((baseTarget 3 2 : ℕ) : ZMod 19) (2 * 2 + 2)
      (Fin.append (encode 2 (cyc 19 2) ![0, 0, 1, 1]) (coreVec 3 2 19 2)) = false := by
  rw [core_reduction (by norm_num) (by norm_num) (by norm_num) (by norm_num),
    twoSum_encode_cyc (by norm_num)]
  decide

/-! ### Witnesses at a NON-BASE window target `r ≥ 1`

**Closeout item C-4(c), 2026-07-31.**  Statement-fidelity review
`ksum/reviews/ksum_lean_statement_fidelity_review_20260731.md` §7.4 recorded the one gap in the T3/T2
witness table: the four witnesses above all instantiate `core_reduction`, i.e. `r = 0`, so the
**new content of the 2026-07-30 repair batch — the generalization from the base target `t₀` to
every window target `t₀ + r`, `r < k` — had no witness at all.**  Non-vacuity of
`core_reduction_at` was never in doubt (its hypotheses admit `r = 0`), which is exactly why the
gap mattered: a witness at `r = 0` cannot distinguish the generalized theorem from the one it
generalizes.

The witnesses below sit at the smallest legal instance `k = 3, K = 2, q = 19 = q₀(3)` and at
`r = 2 = k - 1`, the **rightmost** window target — the one at which the modulus hypothesis
`(k²-2)K + 2k-1 ≤ q` is tight, so they exercise the master inequality at its extreme point — plus
one odd-case (parked-coordinate) witness at `r = 1`.  Each carries both a positive and a negative
instance, so the identity is neither constantly `true` nor constantly `false` at a shifted
target. -/

/-- The shifted core really is a different vector: at `r = 2` the last core entry carries `U + r`
`= 9`, where the base core carries `U = 7`.  Without this the witnesses below could be read as
`r = 0` in disguise. -/
theorem witness_coreVecAt_shifted :
    coreVecAt 3 2 19 1 2 (0 : Fin 1) = ((9 : ℕ) : ZMod 19) ∧
      coreVec 3 2 19 1 (0 : Fin 1) = ((7 : ℕ) : ZMod 19) :=
  ⟨rfl, rfl⟩

/-- Even case (`prop:core-even`, `m = k-2 = 1`) at the rightmost window target `t = t₀ + 2`:
a claw input is a hit. -/
theorem witness_even_pos_at :
    kSum (ZMod 19) 3 ((baseTarget 3 2 + 2 : ℕ) : ZMod 19) (2 * 2 + 1)
      (Fin.append (encode 2 (cyc 19 2) ![0, 0, 0, 0]) (coreVecAt 3 2 19 1 2)) = true := by
  rw [core_reduction_at (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num),
    twoSum_encode_cyc (by norm_num)]
  decide

/-- Even case at `t = t₀ + 2`: a non-claw input is not a hit.  This is the clause that would break
if the shifted core admitted an unintended target-summing subset. -/
theorem witness_even_neg_at :
    kSum (ZMod 19) 3 ((baseTarget 3 2 + 2 : ℕ) : ZMod 19) (2 * 2 + 1)
      (Fin.append (encode 2 (cyc 19 2) ![0, 0, 1, 1]) (coreVecAt 3 2 19 1 2)) = false := by
  rw [core_reduction_at (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num),
    twoSum_encode_cyc (by norm_num)]
  decide

/-- Odd case (`lem:core-odd`, `m = k-1 = 2`, parked coordinate present) at `t = t₀ + 1`: the
parked value moves with the target (`v + r`) and the reduction survives. -/
theorem witness_odd_pos_at :
    kSum (ZMod 19) 3 ((baseTarget 3 2 + 1 : ℕ) : ZMod 19) (2 * 2 + 2)
      (Fin.append (encode 2 (cyc 19 2) ![0, 0, 0, 0]) (coreVecAt 3 2 19 2 1)) = true := by
  rw [core_reduction_at (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num),
    twoSum_encode_cyc (by norm_num)]
  decide

/-- Odd case at `t = t₀ + 1`: a non-claw input is not a hit. -/
theorem witness_odd_neg_at :
    kSum (ZMod 19) 3 ((baseTarget 3 2 + 1 : ℕ) : ZMod 19) (2 * 2 + 2)
      (Fin.append (encode 2 (cyc 19 2) ![0, 0, 1, 1]) (coreVecAt 3 2 19 2 1)) = false := by
  rw [core_reduction_at (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num),
    twoSum_encode_cyc (by norm_num)]
  decide

end KFloor
end KsumAudit
