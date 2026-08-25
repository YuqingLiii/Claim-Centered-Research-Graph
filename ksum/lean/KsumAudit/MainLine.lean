/-
The `k = 2` lower-bound main line of

  `ksum/paper/ksum_small_alphabet.tex`

formalized in Lean 4 + Mathlib.  Proof-DAG node: `KSUM.LEAN.T1.k2-main-line`
(registered OPEN under rule 8a, 2026-07-30).

LaTeX label ↔ Lean name map: see the table in
`ksum/artifacts/ksum_lean_T1_k2_main_line_20260730.md`.

Everything with an `M : QueryModel` argument is CONDITIONAL on the fields of that structure
(`Q` itself, `sec:prelim` facts (i)–(iv) — the last two, `freeze` = (i)+(iii) and `constQ` = (iv),
were **explicitly recorded after external review**, audit findings F1/F2, and are STATED in the manuscript since
v5.2 — and the imported bounds `thm:abi` / `thm:tani`).  Everything without one is unconditional
finite mathematics.
-/
import KsumAudit.QueryModel

namespace KsumAudit

open Finset

/-! ## `lem:encode` — the encoding lemma, combinatorial core

The core is proved once for an arbitrary finite abelian group `G` and an arbitrary injection
`s : Fin κ → G` whose value set is **sum-free at `0`**: `s a + s b ≠ 0` for all `a, b`.
`lem:encode` is the instance `G = ZMod q`, `s a = a+1`; `thm:main-general` is the instance where
`s` enumerates one representative of each pair `{a, -a}`. -/

section EncodeCore

variable {G : Type} [AddCommGroup G] [DecidableEq G] {κ : ℕ}

omit [DecidableEq G] in
/-- Sum-freeness at `0` (with repetition allowed) forces every value to be nonzero. -/
theorem s_ne_zero (s : Fin κ → G) (hs : ∀ a b, s a + s b ≠ 0) (a : Fin κ) : s a ≠ 0 := by
  intro h
  exact hs a a (by rw [h, add_zero])

omit [DecidableEq G] in
/-- No coordinate of an encoded string carries the value `0`.  This is the hypothesis
`0 ∉ S ∪ (-S)` that `lem:oddN` needs, and it is a *consequence* of sum-freeness, not an extra
assumption. -/
theorem encode_ne_zero (n : ℕ) (s : Fin κ → G) (hs : ∀ a b, s a + s b ≠ 0)
    (y : Fin (2 * n) → Fin κ) (p : Fin (2 * n)) : encode n s y p ≠ 0 := by
  rcases lo_or_hi n p with ⟨i, rfl⟩ | ⟨j, rfl⟩
  · rw [encode_lo]; exact s_ne_zero s hs _
  · rw [encode_hi]; simpa using s_ne_zero s hs _

/-- **`lem:encode`, identity part** (arbitrary abelian group form).

`2Sum_{G,0,2n}(E(y)) = Claw_{n→κ}(y)`.  The three cases of the paper's proof appear as the three
non-trivial branches: two first-half values (`s a + s b ≠ 0`), two second-half values
(`-s a + -s b = -(s a + s b) ≠ 0`), and a cross pair (`s a - s b = 0 ↔ a = b`). -/
theorem twoSum_encode (n : ℕ) (s : Fin κ → G) (hs : ∀ a b, s a + s b ≠ 0)
    (hinj : Function.Injective s) (y : Fin (2 * n) → Fin κ) :
    twoSum G 0 (2 * n) (encode n s y) = Claw n κ y := by
  rw [twoSum_eq_decide, Claw]
  refine decide_eq_decide.mpr ⟨?_, ?_⟩
  · rintro ⟨p, p', hne, hsum⟩
    rcases lo_or_hi n p with ⟨i, rfl⟩ | ⟨i, rfl⟩ <;>
      rcases lo_or_hi n p' with ⟨j, rfl⟩ | ⟨j, rfl⟩
    · -- both in the first half: sum lies in `[2, 2κ]`, never `0`
      rw [encode_lo, encode_lo] at hsum
      exact absurd hsum (hs _ _)
    · -- cross pair `f i - g j`
      rw [encode_lo, encode_hi] at hsum
      exact ⟨i, j, hinj (neg_injective (neg_eq_of_add_eq_zero_right hsum))⟩
    · -- cross pair, other orientation
      rw [encode_hi, encode_lo] at hsum
      exact ⟨j, i, hinj (neg_injective (neg_eq_of_add_eq_zero_left hsum))⟩
    · -- both in the second half: sum lies in `-[2, 2κ]`, never `0`
      rw [encode_hi, encode_hi, ← neg_add] at hsum
      exact absurd (neg_eq_zero.mp hsum) (hs _ _)
  · rintro ⟨i, j, hij⟩
    exact ⟨lo n i, hi n j, lo_ne_hi n i j, by rw [encode_lo, encode_hi, hij]; simp⟩

/-- **`lem:oddN`, combinatorial core.**  Appending a frozen coordinate of value `0` to a string
that carries no `0` does not change the `0`-sum predicate: "`0 + v = 0` forces `v = 0`, and there
is only one `0`". -/
theorem twoSum_snoc_zero (m : ℕ) (z : Fin m → G) (hz : ∀ p, z p ≠ 0) :
    twoSum G 0 (m + 1) (Fin.snoc z (0 : G)) = twoSum G 0 m z := by
  rw [twoSum_eq_decide, twoSum_eq_decide]
  refine decide_eq_decide.mpr ⟨?_, ?_⟩
  · rintro ⟨p, p', hne, hsum⟩
    rcases Fin.eq_castSucc_or_eq_last p with ⟨i, rfl⟩ | rfl <;>
      rcases Fin.eq_castSucc_or_eq_last p' with ⟨j, rfl⟩ | rfl
    · rw [Fin.snoc_castSucc, Fin.snoc_castSucc] at hsum
      exact ⟨i, j, fun h => hne (by rw [h]), hsum⟩
    · rw [Fin.snoc_castSucc, Fin.snoc_last, add_zero] at hsum
      exact absurd hsum (hz i)
    · rw [Fin.snoc_last, Fin.snoc_castSucc, zero_add] at hsum
      exact absurd hsum (hz j)
    · exact absurd rfl hne
  · rintro ⟨i, j, hne, hsum⟩
    refine ⟨i.castSucc, j.castSucc, fun h => hne (Fin.castSucc_injective _ h), ?_⟩
    rwa [Fin.snoc_castSucc, Fin.snoc_castSucc]

/-- **`lem:oddN`, identity part.** -/
theorem twoSum_encode_snoc (n : ℕ) (s : Fin κ → G) (hs : ∀ a b, s a + s b ≠ 0)
    (hinj : Function.Injective s) (y : Fin (2 * n) → Fin κ) :
    twoSum G 0 (2 * n + 1) (Fin.snoc (encode n s y) (0 : G)) = Claw n κ y := by
  rw [twoSum_snoc_zero _ _ (encode_ne_zero n s hs y), twoSum_encode n s hs hinj y]

end EncodeCore

/-! ## The cyclic value set of `lem:encode`

`E(f,g) = (f(1),…,f(n), -g(1),…,-g(n))`, values in `{1,…,κ} ∪ {q-κ,…,q-1} ⊆ ZMod q`. -/

section Cyclic

variable {q κ : ℕ}

/-- First-half values are `{1,…,κ}`: `s a = a+1` has `ZMod`-value `a+1 ∈ [1, κ]`. -/
theorem cyc_val (hq : κ < q) (a : Fin κ) :
    (cyc q κ a).val = (a : ℕ) + 1 ∧ 1 ≤ (cyc q κ a).val ∧ (cyc q κ a).val ≤ κ := by
  have ha := a.isLt
  have h : (a : ℕ) + 1 < q := by omega
  have hv : (cyc q κ a).val = (a : ℕ) + 1 := by
    simp only [cyc]; exact ZMod.val_cast_of_lt h
  refine ⟨hv, ?_, ?_⟩ <;> rw [hv] <;> omega

/-- Second-half values are `{q-κ,…,q-1}`. -/
theorem neg_cyc_val (hq : κ < q) (a : Fin κ) :
    (-(cyc q κ a)).val = q - ((a : ℕ) + 1) ∧ q - κ ≤ (-(cyc q κ a)).val ∧
      (-(cyc q κ a)).val ≤ q - 1 := by
  have ha := a.isLt
  have hne : -(cyc q κ a) = ((q - ((a : ℕ) + 1) : ℕ) : ZMod q) := by
    refine neg_eq_of_add_eq_zero_right ?_
    simp only [cyc, ← Nat.cast_add]
    rw [show (a : ℕ) + 1 + (q - ((a : ℕ) + 1)) = q by omega]
    exact ZMod.natCast_self q
  have hlt : q - ((a : ℕ) + 1) < q := by omega
  refine ⟨by rw [hne]; exact ZMod.val_cast_of_lt hlt, ?_, ?_⟩ <;>
    rw [hne, ZMod.val_cast_of_lt hlt] <;> omega

/-- **`lem:encode`, case 1 and case 2.**  Sums of two first-half values lie in `[2, 2κ]`, so for
`q ≥ 2κ+1` they are nonzero in `ZMod q`; the same computation covers the second half, whose sums
lie in `-[2, 2κ]`. -/
theorem cyc_add_ne_zero (hq : 2 * κ + 1 ≤ q) (a b : Fin κ) : cyc q κ a + cyc q κ b ≠ 0 := by
  have ha := a.isLt
  have hb := b.isLt
  have hrange : 2 ≤ ((a : ℕ) + 1) + ((b : ℕ) + 1) ∧ ((a : ℕ) + 1) + ((b : ℕ) + 1) ≤ 2 * κ := by
    omega
  simp only [cyc, ← Nat.cast_add, Ne, ZMod.natCast_eq_zero_iff]
  exact Nat.not_dvd_of_pos_of_lt (by omega) (by omega)

/-- **`lem:encode`, case 3.**  A cross sum is `f(i) - g(j) ∈ [-(κ-1), κ-1]`, which vanishes in
`ZMod q` iff `f(i) = g(j)`, since `q > 2κ > 2(κ-1)`. -/
theorem cyc_injective (hq : 2 * κ + 1 ≤ q) : Function.Injective (cyc q κ) := by
  intro a b hab
  have ha : (a : ℕ) + 1 < q := by have := a.isLt; omega
  have hb : (b : ℕ) + 1 < q := by have := b.isLt; omega
  have h := congrArg ZMod.val hab
  simp only [cyc, ZMod.val_cast_of_lt ha, ZMod.val_cast_of_lt hb] at h
  exact Fin.ext (by omega)

theorem cyc_sub_eq_zero_iff (hq : 2 * κ + 1 ≤ q) (a b : Fin κ) :
    cyc q κ a + -(cyc q κ b) = 0 ↔ a = b := by
  constructor
  · intro h
    exact cyc_injective hq (neg_injective (neg_eq_of_add_eq_zero_right h))
  · rintro rfl; simp

/-- **`lem:encode`, identity part, exactly as displayed in the paper.**

`2Sum_{Z_q, 0, 2n}(E(f,g)) = Claw_{n→κ}(f,g)` for `q ≥ 2κ+1` (any parity).

The paper's `κ ≥ 2` is *not* needed for the identity — it is needed only where the claw bound is
imported.  Stating the identity without it is strictly stronger. -/
theorem twoSum_encode_cyc (hq : 2 * κ + 1 ≤ q) (n : ℕ) (y : Fin (2 * n) → Fin κ) :
    twoSum (ZMod q) 0 (2 * n) (encode n (cyc q κ) y) = Claw n κ y :=
  twoSum_encode n _ (cyc_add_ne_zero hq) (cyc_injective hq) y

/-- The same identity in the paper's `(f, g)` notation. -/
theorem twoSum_encode_cyc_pair (hq : 2 * κ + 1 ≤ q) (n : ℕ) (f g : Fin n → Fin κ) :
    twoSum (ZMod q) 0 (2 * n) (encode n (cyc q κ) (pairUp n f g))
      = decide (∃ i j : Fin n, f i = g j) := by
  rw [twoSum_encode_cyc hq, Claw_pairUp]

/-- `E(f,g)` really is `(f(1),…,f(n), -g(1),…,-g(n))`. -/
theorem encode_pairUp_lo (n : ℕ) (f g : Fin n → Fin κ) (i : Fin n) :
    encode n (cyc q κ) (pairUp n f g) (lo n i) = cyc q κ (f i) := by simp

theorem encode_pairUp_hi (n : ℕ) (f g : Fin n → Fin κ) (j : Fin n) :
    encode n (cyc q κ) (pairUp n f g) (hi n j) = -(cyc q κ (g j)) := by simp

/-- **`lem:oddN`, identity part, cyclic form.** -/
theorem twoSum_encode_snoc_cyc (hq : 2 * κ + 1 ≤ q) (n : ℕ) (y : Fin (2 * n) → Fin κ) :
    twoSum (ZMod q) 0 (2 * n + 1) (Fin.snoc (encode n (cyc q κ) y) (0 : ZMod q)) = Claw n κ y :=
  twoSum_encode_snoc n _ (cyc_add_ne_zero hq) (cyc_injective hq) y

end Cyclic

/-! ## The query transfer: `Q(2Sum) = Ω(Q(Claw))`, with the constant made explicit -/

section QTransfer

variable {G : Type} [AddCommGroup G] [DecidableEq G] [Fintype G] {κ : ℕ}

omit [DecidableEq G] [Fintype G] in
/-- Each per-position map of the encoding is injective (`s` on the first half, `-s` on the
second).  Note it is *not* surjective onto `G`: this is exactly why fact (i) is needed alongside
fact (ii). -/
theorem encMap_injective (n : ℕ) (s : Fin κ → G) (hinj : Function.Injective s)
    (p : Fin (2 * n)) : Function.Injective (encMap n s p) := by
  intro a b hab
  simp only [encMap] at hab
  by_cases h : (p : ℕ) < n
  · rw [if_pos h, if_pos h] at hab; exact hinj hab
  · rw [if_neg h, if_neg h] at hab; exact hinj (neg_injective hab)

/-- **`lem:encode`, query part.**  `Q(Claw_{n→κ}) ≤ 2 · Q(2Sum_{G,0,2n})`, which is the paper's
`Q(2Sum) = Ω(Q(Claw))` with the absolute constant exhibited.
Uses only `sec:prelim` facts (i) and (ii), through `QueryModel.relabel_inj`. -/
theorem Q_claw_le_encode (M : QueryModel) (n : ℕ) (s : Fin κ → G)
    (hs : ∀ a b, s a + s b ≠ 0) (hinj : Function.Injective s) :
    M.Q (Claw n κ) ≤ 2 * M.Q (twoSum G 0 (2 * n)) := by
  have h : (fun y : Fin (2 * n) → Fin κ =>
      twoSum G 0 (2 * n) (fun p => encMap n s p (y p))) = Claw n κ := by
    funext y; exact twoSum_encode n s hs hinj y
  have key := M.relabel_inj (Alph := fun _ : Fin (2 * n) => G)
      (Alph' := fun _ : Fin (2 * n) => Fin κ) (fun p => encMap n s p)
      (encMap_injective n s hinj) (twoSum G 0 (2 * n))
  rwa [h] at key

/-- **`lem:oddN`, query part.**  Same bound at odd length `2n+1`. -/
theorem Q_claw_le_encode_odd (M : QueryModel) (n : ℕ) (s : Fin κ → G)
    (hs : ∀ a b, s a + s b ≠ 0) (hinj : Function.Injective s) :
    M.Q (Claw n κ) ≤ 2 * M.Q (twoSum G 0 (2 * n + 1)) := by
  have h : (fun y : Fin (2 * n) → Fin κ =>
      (fun z : Fin (2 * n) → G => twoSum G 0 (2 * n + 1) (Fin.snoc z (0 : G)))
        (fun p => encMap n s p (y p))) = Claw n κ := by
    funext y; exact twoSum_encode_snoc n s hs hinj y
  have key := M.relabel_inj (Alph := fun _ : Fin (2 * n) => G)
      (Alph' := fun _ : Fin (2 * n) => Fin κ) (fun p => encMap n s p)
      (encMap_injective n s hinj)
      (fun z : Fin (2 * n) → G => twoSum G 0 (2 * n + 1) (Fin.snoc z (0 : G)))
  rw [h] at key
  have hfr : M.Q (fun z : Fin (2 * n) → G => twoSum G 0 (2 * n + 1) (Fin.snoc z (0 : G)))
      ≤ M.Q (twoSum G 0 (2 * n + 1)) :=
    M.freeze (Alph := fun _ : Fin (2 * n + 1) => G) (0 : G) (twoSum G 0 (2 * n + 1))
  linarith

/-- Both parities of `N` at once. -/
theorem Q_claw_le_twoSum_zero (M : QueryModel) (N n : ℕ) (hN : N = 2 * n ∨ N = 2 * n + 1)
    (s : Fin κ → G) (hs : ∀ a b, s a + s b ≠ 0) (hinj : Function.Injective s) :
    M.Q (Claw n κ) ≤ 2 * M.Q (twoSum G 0 N) := by
  rcases hN with rfl | rfl
  · exact Q_claw_le_encode M n s hs hinj
  · exact Q_claw_le_encode_odd M n s hs hinj

end QTransfer

/-! ## `lem:shift` — translation -/

section Shift

variable {G : Type} [AddCommGroup G] [DecidableEq G] [Fintype G]

omit [Fintype G] in
/-- **`lem:shift`, identity part.**  With `2c = t' - t`, translating every coordinate by `c`
carries `2Sum_{G,t,N}` to `2Sum_{G,t',N}`: `2Sum_{G,t,N} = 2Sum_{G,t',N} ∘ φ`, `φ_i(x) = x + c`. -/
theorem twoSum_shift (t t' c : G) (hc : c + c = t' - t) (N : ℕ) (x : Fin N → G) :
    twoSum G t' N (fun i => x i + c) = twoSum G t N x := by
  rw [twoSum_eq_decide, twoSum_eq_decide]
  refine decide_eq_decide.mpr
    (exists_congr fun i => exists_congr fun j => and_congr_right fun _ => ?_)
  have key : (x i + c) + (x j + c) = (x i + x j) + (t' - t) := by rw [← hc]; abel
  rw [key]
  constructor
  · intro h
    have h2 := congrArg (fun w => w - (t' - t)) h
    simpa using h2
  · intro h; rw [h]; abel

/-- **`lem:shift`, query part.**  `Q(2Sum_{G,t,N}) ≤ 2 · Q(2Sum_{G,t',N})`; applying it to `-c`
gives the reverse inequality, which is the paper's `Θ`. -/
theorem Q_twoSum_shift (M : QueryModel) (t t' c : G) (hc : c + c = t' - t) (N : ℕ) :
    M.Q (twoSum G t N) ≤ 2 * M.Q (twoSum G t' N) := by
  have h : (fun x : Fin N → G => twoSum G t' N (fun i => (Equiv.addRight c) (x i)))
      = twoSum G t N := by
    funext x; exact twoSum_shift t t' c hc N x
  have key := M.relabel (Alph := fun _ : Fin N => G) (Alph' := fun _ : Fin N => G)
      (fun _ => Equiv.addRight c) (twoSum G t' N)
  rwa [h] at key

end Shift

/-- For odd `q`, every element of `ZMod q` is `2c` for an explicit `c = ((q-1)/2 + 1)·u`.
This is the paper's "`2` is invertible mod odd `q`". -/
theorem exists_half_odd {q : ℕ} (hq : Odd q) (u : ZMod q) : ∃ c : ZMod q, c + c = u := by
  obtain ⟨r, hr⟩ := hq
  have hr' : q = 2 * r + 1 := by omega
  have hzero : (2 : ZMod q) * (r : ZMod q) + 1 = 0 := by
    have h : ((2 * r + 1 : ℕ) : ZMod q) = 0 := by rw [← hr']; exact ZMod.natCast_self q
    push_cast at h
    exact h
  refine ⟨((r : ZMod q) + 1) * u, ?_⟩
  have expand : ((r : ZMod q) + 1) * u + ((r : ZMod q) + 1) * u
      = ((2 : ZMod q) * (r : ZMod q) + 1) * u + u := by ring
  rw [expand, hzero, zero_mul, zero_add]

/-! ## Explicit-constant arithmetic

`Ω(√n · κ^{1/6}) ⟹ Ω(√N · q^{1/6})` with every constant exhibited.  The two steps of the paper's
proof — `n = ⌊N/2⌋ ≥ (N-1)/2` and `κ = (q-1)/2 ≥ q/3` — appear as the two divisor hypotheses
`N ≤ d₁ n` and `q ≤ d₂ κ`. -/

theorem sqrt_div_le (N n d : ℕ) (h : N ≤ d * n) :
    Real.sqrt N / Real.sqrt d ≤ Real.sqrt n := by
  rcases Nat.eq_zero_or_pos d with rfl | hd
  · simp at h; simp [h]
  have hd' : (0 : ℝ) < Real.sqrt d := Real.sqrt_pos.mpr (by exact_mod_cast hd)
  rw [div_le_iff₀ hd']
  calc Real.sqrt N ≤ Real.sqrt ((d : ℝ) * (n : ℝ)) := by
        apply Real.sqrt_le_sqrt; exact_mod_cast h
    _ = Real.sqrt d * Real.sqrt n := Real.sqrt_mul (by positivity) _
    _ = Real.sqrt n * Real.sqrt d := mul_comm _ _

theorem rpow6_div_le (q κ d : ℕ) (h : q ≤ d * κ) :
    (q : ℝ) ^ (1 / 6 : ℝ) / (d : ℝ) ^ (1 / 6 : ℝ) ≤ (κ : ℝ) ^ (1 / 6 : ℝ) := by
  rcases Nat.eq_zero_or_pos d with rfl | hd
  · have hq0 : q = 0 := by omega
    subst hq0
    rw [Nat.cast_zero, Real.zero_rpow (by norm_num), zero_div]
    positivity
  have hd' : (0 : ℝ) < (d : ℝ) ^ (1 / 6 : ℝ) :=
    Real.rpow_pos_of_pos (by exact_mod_cast hd) _
  rw [div_le_iff₀ hd']
  calc (q : ℝ) ^ (1 / 6 : ℝ) ≤ ((d : ℝ) * (κ : ℝ)) ^ (1 / 6 : ℝ) := by
        apply Real.rpow_le_rpow (by positivity) _ (by norm_num); exact_mod_cast h
    _ = (d : ℝ) ^ (1 / 6 : ℝ) * (κ : ℝ) ^ (1 / 6 : ℝ) :=
        Real.mul_rpow (by positivity) (by positivity)
    _ = (κ : ℝ) ^ (1 / 6 : ℝ) * (d : ℝ) ^ (1 / 6 : ℝ) := mul_comm _ _

/-- The combined explicit-constant step. -/
theorem combine_bound (cA : ℝ) (hcA : 0 < cA) (N n q κ d₁ d₂ : ℕ)
    (hd₁ : 0 < d₁) (hd₂ : 0 < d₂) (h1 : N ≤ d₁ * n) (h2 : q ≤ d₂ * κ) (X : ℝ)
    (hX : cA * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ) ≤ X) :
    cA / (Real.sqrt d₁ * (d₂ : ℝ) ^ (1 / 6 : ℝ)) * Real.sqrt N * (q : ℝ) ^ (1 / 6 : ℝ) ≤ X := by
  have hs1 : Real.sqrt N / Real.sqrt d₁ ≤ Real.sqrt n := sqrt_div_le N n d₁ h1
  have hs2 : (q : ℝ) ^ (1 / 6 : ℝ) / (d₂ : ℝ) ^ (1 / 6 : ℝ) ≤ (κ : ℝ) ^ (1 / 6 : ℝ) :=
    rpow6_div_le q κ d₂ h2
  have hd₁' : (0 : ℝ) < Real.sqrt d₁ := Real.sqrt_pos.mpr (by exact_mod_cast hd₁)
  have hd₂' : (0 : ℝ) < (d₂ : ℝ) ^ (1 / 6 : ℝ) := Real.rpow_pos_of_pos (by exact_mod_cast hd₂) _
  have hrw : cA / (Real.sqrt d₁ * (d₂ : ℝ) ^ (1 / 6 : ℝ)) * Real.sqrt N * (q : ℝ) ^ (1 / 6 : ℝ)
      = cA * (Real.sqrt N / Real.sqrt d₁) * ((q : ℝ) ^ (1 / 6 : ℝ) / (d₂ : ℝ) ^ (1 / 6 : ℝ)) := by
    field_simp
  rw [hrw]
  refine le_trans ?_ hX
  have hnn1 : (0 : ℝ) ≤ Real.sqrt N / Real.sqrt d₁ := by positivity
  have hnn2 : (0 : ℝ) ≤ (q : ℝ) ^ (1 / 6 : ℝ) / (d₂ : ℝ) ^ (1 / 6 : ℝ) := by positivity
  gcongr

/-! ## `thm:main-odd` — the main theorem over odd cyclic groups -/

/-- **`thm:main-odd`.**  For odd `q ≥ 5`, every target `t`, and every `N` with `q ≤ 4⌊N/2⌋ - 1`,
`Q(2Sum_{Z_q,t,N}) ≥ (c_ABI / (4√3 · 3^{1/6})) · √N · q^{1/6}`, i.e. `Ω(√N · q^{1/6})` with the
constant exhibited.  `q ≤ 4n-1` is written `q + 1 ≤ 4n` to avoid truncated subtraction.
Range use: `κ = (q-1)/2 ≤ 2n-1` puts this in `thm:tani`'s range. -/
theorem main_odd (M : QueryModel) (N q : ℕ) [NeZero q] (t : ZMod q)
    (hodd : Odd q) (hq5 : 5 ≤ q) (hrange : q + 1 ≤ 4 * (N / 2)) :
    M.cABI / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))) * Real.sqrt N * (q : ℝ) ^ (1 / 6 : ℝ)
      ≤ M.Q (twoSum (ZMod q) t N) := by
  obtain ⟨r, hr⟩ := hodd
  set n := N / 2 with hn
  set κ := (q - 1) / 2 with hκ
  have hNn : N = 2 * n ∨ N = 2 * n + 1 := by omega
  have hκ2 : 2 ≤ κ := by omega
  have hκrange : κ < 2 * n := by omega
  have hqκ : 2 * κ + 1 ≤ q := by omega
  have hd1 : N ≤ 3 * n := by omega
  have hd2 : q ≤ 3 * κ := by omega
  -- claw bound
  have hclaw := M.tani n κ hκ2 hκrange
  -- transfer to `2Sum` at target 0
  have htr := Q_claw_le_twoSum_zero M N n hNn (cyc q κ) (cyc_add_ne_zero hqκ) (cyc_injective hqκ)
  -- translate to an arbitrary target
  obtain ⟨c, hc⟩ := exists_half_odd ⟨r, hr⟩ (t - 0)
  have hshift := Q_twoSum_shift M (0 : ZMod q) t c hc N
  have hchain : M.cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ)
      ≤ 4 * M.Q (twoSum (ZMod q) t N) := by linarith
  have hfin := combine_bound M.cABI M.cABI_pos N n q κ 3 3 (by norm_num) (by norm_num) hd1 hd2
    (4 * M.Q (twoSum (ZMod q) t N)) hchain
  push_cast at hfin
  rw [show (4 : ℝ) * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))
        = (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ)) * 4 from mul_comm _ _,
      ← div_div, div_mul_eq_mul_div, div_mul_eq_mul_div]
  linarith

/-- **`thm:main-odd`, `thm:abi`-only subrange.**  When `q ≤ 2n-1` the encoding lands in
`κ < n`, so `thm:abi` alone suffices; `thm:tani` is needed only for `2n-1 < q ≤ 4n-1`. -/
theorem main_odd_abi (M : QueryModel) (N q : ℕ) [NeZero q] (t : ZMod q)
    (hodd : Odd q) (hq5 : 5 ≤ q) (hrange : q + 1 ≤ 2 * (N / 2)) :
    M.cABI / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))) * Real.sqrt N * (q : ℝ) ^ (1 / 6 : ℝ)
      ≤ M.Q (twoSum (ZMod q) t N) := by
  obtain ⟨r, hr⟩ := hodd
  set n := N / 2 with hn
  set κ := (q - 1) / 2 with hκ
  have hNn : N = 2 * n ∨ N = 2 * n + 1 := by omega
  have hκ2 : 2 ≤ κ := by omega
  have hκrange : κ < n := by omega
  have hqκ : 2 * κ + 1 ≤ q := by omega
  have hd1 : N ≤ 3 * n := by omega
  have hd2 : q ≤ 3 * κ := by omega
  have hclaw := M.abi n κ hκ2 hκrange
  have htr := Q_claw_le_twoSum_zero M N n hNn (cyc q κ) (cyc_add_ne_zero hqκ) (cyc_injective hqκ)
  obtain ⟨c, hc⟩ := exists_half_odd ⟨r, hr⟩ (t - 0)
  have hshift := Q_twoSum_shift M (0 : ZMod q) t c hc N
  have hchain : M.cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ)
      ≤ 4 * M.Q (twoSum (ZMod q) t N) := by linarith
  have hfin := combine_bound M.cABI M.cABI_pos N n q κ 3 3 (by norm_num) (by norm_num) hd1 hd2
    (4 * M.Q (twoSum (ZMod q) t N)) hchain
  push_cast at hfin
  rw [show (4 : ℝ) * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))
        = (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ)) * 4 from mul_comm _ _,
      ← div_div, div_mul_eq_mul_div, div_mul_eq_mul_div]
  linarith

/-! ## `thm:main-general` — arbitrary finite abelian groups at `t = 0` -/

/-- The `2`-torsion subgroup `G[2] = {a : 2a = 0}` of `G`, as a `Finset`. -/
def torsion2 (G : Type) [AddCommGroup G] [Fintype G] [DecidableEq G] : Finset G :=
  Finset.univ.filter (fun a => a + a = 0)

section General

variable {G : Type} [AddCommGroup G] [Fintype G] [DecidableEq G]

/-- **`thm:main-general`, the representative construction.**  The non-`2`-torsion elements split
into `(q - |G[2]|)/2` pairs `{a, -a}` with `a ≠ -a`; choosing one representative from each pair
gives `S` with `S ∩ (-S) = ∅`, equivalently `s + s' ≠ 0` for all `s, s' ∈ S`. -/
theorem exists_repr_set :
    ∃ S : Finset G, (∀ a ∈ S, ∀ b ∈ S, a + b ≠ 0) ∧
      2 * S.card = Fintype.card G - (torsion2 G).card := by
  classical
  obtain ⟨e⟩ : Nonempty (G ≃ Fin (Fintype.card G)) := ⟨Fintype.equivFin G⟩
  set T : Finset G := Finset.univ.filter (fun a : G => a + a ≠ 0) with hT
  set S : Finset G := T.filter (fun a => e a < e (-a)) with hS
  set S' : Finset G := T.filter (fun a => e (-a) < e a) with hS'
  have hmemT : ∀ a : G, a ∈ T ↔ a + a ≠ 0 := by intro a; rw [hT]; simp
  have hmemS : ∀ a : G, a ∈ S ↔ (a + a ≠ 0 ∧ e a < e (-a)) := by
    intro a; rw [hS]; simp [hmemT]
  have hmemS' : ∀ a : G, a ∈ S' ↔ (a + a ≠ 0 ∧ e (-a) < e a) := by
    intro a; rw [hS']; simp [hmemT]
  -- `a ≠ -a` on `T`
  have hne : ∀ a : G, a + a ≠ 0 → e a ≠ e (-a) := by
    intro a ha h
    apply ha
    have h2 : a = -a := e.injective h
    nth_rewrite 1 [h2]
    simp
  -- sum-freeness of `S`
  have hsumfree : ∀ a ∈ S, ∀ b ∈ S, a + b ≠ 0 := by
    intro a ha b hb hab
    rw [hmemS] at ha hb
    have hb' : b = -a := by
      have := congrArg (fun w => w - a) hab
      simpa [sub_eq_add_neg, add_comm] using this
    subst hb'
    have := ha.2
    have h2 := hb.2
    rw [neg_neg] at h2
    omega
  -- `S'` is the image of `S` under negation
  have hneg : S' = S.image (fun a => -a) := by
    ext b
    rw [hmemS', Finset.mem_image]
    constructor
    · intro hb
      refine ⟨-b, ?_, neg_neg b⟩
      rw [hmemS, neg_neg]
      refine ⟨?_, hb.2⟩
      rw [← neg_add, neg_ne_zero]
      exact hb.1
    · rintro ⟨a, ha, rfl⟩
      rw [hmemS] at ha
      refine ⟨?_, ?_⟩
      · rw [← neg_add, neg_ne_zero]; exact ha.1
      · rw [neg_neg]; exact ha.2
  have hcardS' : S'.card = S.card := by
    rw [hneg]; exact Finset.card_image_of_injective S neg_injective
  -- `T` is the disjoint union of `S` and `S'`
  have hdisj : Disjoint S S' := by
    rw [Finset.disjoint_left]
    intro a ha ha'
    rw [hmemS] at ha; rw [hmemS'] at ha'
    omega
  have hunion : S ∪ S' = T := by
    ext a
    rw [Finset.mem_union, hmemS, hmemS', hmemT]
    constructor
    · rintro (h | h) <;> exact h.1
    · intro h
      rcases lt_or_gt_of_ne (hne a h) with h' | h'
      · exact Or.inl ⟨h, h'⟩
      · exact Or.inr ⟨h, h'⟩
  have hcardT : S.card + S'.card = T.card := by
    rw [← hunion, Finset.card_union_of_disjoint hdisj]
  -- `|T| = q - |G[2]|`
  have hsplit : (torsion2 G).card + T.card = Fintype.card G := by
    rw [torsion2, hT]
    exact Finset.card_filter_add_card_filter_not _
  refine ⟨S, hsumfree, ?_⟩
  omega

/-- **`thm:main-general`.**  For a finite abelian `G` of order `q` with `κ = (q - |G[2]|)/2 ≥ 2`
and `κ ≤ 2n-1` (written `κ < 2n`),
`Q(2Sum_{G,0,N}) ≥ (c_ABI / (2√3)) · √N · κ^{1/6}`. -/
theorem main_general (M : QueryModel) (N n κ : ℕ) (hN : N = 2 * n ∨ N = 2 * n + 1)
    (hκ : κ = (Fintype.card G - (torsion2 G).card) / 2) (hκ2 : 2 ≤ κ) (hrange : κ < 2 * n) :
    M.cABI / (2 * Real.sqrt 3) * Real.sqrt N * (κ : ℝ) ^ (1 / 6 : ℝ) ≤ M.Q (twoSum G 0 N) := by
  obtain ⟨S, hsumfree, hcard⟩ := exists_repr_set (G := G)
  have hSκ : S.card = κ := by omega
  have hd1 : N ≤ 3 * n := by omega
  set s : Fin κ → G := fun i => ((Finset.equivFinOfCardEq hSκ).symm i : G) with hs
  have hmem : ∀ i, s i ∈ S := fun i => ((Finset.equivFinOfCardEq hSκ).symm i).2
  have hsf : ∀ a b, s a + s b ≠ 0 := fun a b => hsumfree _ (hmem a) _ (hmem b)
  have hinj : Function.Injective s := by
    intro a b hab
    exact (Finset.equivFinOfCardEq hSκ).symm.injective (Subtype.ext hab)
  have hclaw := M.tani n κ hκ2 hrange
  have htr := Q_claw_le_twoSum_zero M N n hN s hsf hinj
  have hchain : M.cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ)
      ≤ 2 * M.Q (twoSum G 0 N) := by linarith
  have hfin := combine_bound M.cABI M.cABI_pos N n κ κ 3 1 (by norm_num) (by norm_num) hd1
    (by omega) (2 * M.Q (twoSum G 0 N)) hchain
  simp only [Nat.cast_one, Real.one_rpow, mul_one, Nat.cast_ofNat] at hfin
  rw [show (2 : ℝ) * Real.sqrt 3 = Real.sqrt 3 * 2 from mul_comm _ _,
      ← div_div, div_mul_eq_mul_div, div_mul_eq_mul_div]
  linarith

end General

/-! ## `cor:threshold` — the threshold drops to `q = Θ(N)`

The corollary is split into its two cases so that the paper's claim — that the `c`-dependence
arises ONLY in the case `cN ≤ q < N-1` — is visible in the *statements*, not just in the prose.
`threshold_large` mentions no `c` at all, in its constant or in its hypotheses. -/

/-- Target reduction: at `t = 0` nothing is needed; for odd `q` and arbitrary `t`, `lem:shift`
costs the absolute factor `2`. -/
theorem Q_zero_le_target (M : QueryModel) (N q : ℕ) [NeZero q] (t : ZMod q)
    (ht : t = 0 ∨ Odd q) (X : ℝ) (hX : X ≤ M.Q (twoSum (ZMod q) 0 N)) (hX0 : 0 ≤ X) :
    X / 2 ≤ M.Q (twoSum (ZMod q) t N) := by
  rcases ht with rfl | hodd
  · linarith
  · obtain ⟨c, hc⟩ := exists_half_odd hodd (t - 0)
    have := Q_twoSum_shift M (0 : ZMod q) t c hc N
    linarith

/-- **`cor:threshold`, Case 1: `q ≥ N-1`.**  NO `c` appears — not in the constant, not in the
hypotheses.  Uses `thm:abi` only, with `κ = n-1 < n`. -/
theorem threshold_large (M : QueryModel) (N q : ℕ) [NeZero q] (t : ZMod q)
    (ht : t = 0 ∨ Odd q) (hN : 6 ≤ N) (hq : N - 1 ≤ q) :
    M.cABI / (4 * (Real.sqrt 3 * (6 : ℝ) ^ (1 / 6 : ℝ))) * Real.sqrt N * (N : ℝ) ^ (1 / 6 : ℝ)
      ≤ M.Q (twoSum (ZMod q) t N) := by
  set n := N / 2 with hn
  set κ := n - 1 with hκ
  have hNn : N = 2 * n ∨ N = 2 * n + 1 := by omega
  have hκ2 : 2 ≤ κ := by omega
  have hκn : κ < n := by omega
  have hqκ : 2 * κ + 1 ≤ q := by omega
  have hd1 : N ≤ 3 * n := by omega
  have hd2 : N ≤ 6 * κ := by omega
  have hclaw := M.abi n κ hκ2 hκn
  have htr := Q_claw_le_twoSum_zero M N n hNn (cyc q κ) (cyc_add_ne_zero hqκ) (cyc_injective hqκ)
  have hnn : (0 : ℝ) ≤ M.cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ) :=
    mul_nonneg (mul_nonneg M.cABI_pos.le (Real.sqrt_nonneg _))
      (Real.rpow_nonneg (Nat.cast_nonneg _) _)
  have h0 := Q_zero_le_target M N q t ht (M.cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ) / 2)
    (by linarith) (by linarith)
  have hchain : M.cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ)
      ≤ 4 * M.Q (twoSum (ZMod q) t N) := by linarith
  have hfin := combine_bound M.cABI M.cABI_pos N n N κ 3 6 (by norm_num) (by norm_num) hd1 hd2
    (4 * M.Q (twoSum (ZMod q) t N)) hchain
  push_cast at hfin
  rw [show (4 : ℝ) * (Real.sqrt 3 * (6 : ℝ) ^ (1 / 6 : ℝ))
        = (Real.sqrt 3 * (6 : ℝ) ^ (1 / 6 : ℝ)) * 4 from mul_comm _ _,
      ← div_div, div_mul_eq_mul_div, div_mul_eq_mul_div]
  linarith

/-- **`cor:threshold`, Case 2: `cN ≤ q < N-1`.**  This is the ONLY place `c` enters: it appears
in the constant as `c^{1/6}` and in the validity threshold as `5 ≤ cN`. -/
theorem threshold_small (M : QueryModel) (c : ℝ) (hc : 0 < c) (N q : ℕ) [NeZero q] (t : ZMod q)
    (ht : t = 0 ∨ Odd q) (hN : 6 ≤ N) (hcN : 5 ≤ c * N) (hcq : c * N ≤ q) (hlt : q + 1 < N) :
    M.cABI * c ^ (1 / 6 : ℝ) / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))) * Real.sqrt N *
        (N : ℝ) ^ (1 / 6 : ℝ) ≤ M.Q (twoSum (ZMod q) t N) := by
  have hq5 : 5 ≤ q := by
    have h : (5 : ℝ) ≤ (q : ℝ) := le_trans hcN hcq
    exact_mod_cast h
  set n := N / 2 with hn
  set κ := (q - 1) / 2 with hκ
  have hNn : N = 2 * n ∨ N = 2 * n + 1 := by omega
  have hκ2 : 2 ≤ κ := by omega
  have hκrange : κ < 2 * n := by omega
  have hqκ : 2 * κ + 1 ≤ q := by omega
  have hd1 : N ≤ 3 * n := by omega
  have hd2 : q ≤ 3 * κ := by omega
  have hclaw := M.tani n κ hκ2 hκrange
  have htr := Q_claw_le_twoSum_zero M N n hNn (cyc q κ) (cyc_add_ne_zero hqκ) (cyc_injective hqκ)
  have hnn : (0 : ℝ) ≤ M.cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ) :=
    mul_nonneg (mul_nonneg M.cABI_pos.le (Real.sqrt_nonneg _))
      (Real.rpow_nonneg (Nat.cast_nonneg _) _)
  have h0 := Q_zero_le_target M N q t ht (M.cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ) / 2)
    (by linarith) (by linarith)
  have hchain : M.cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ)
      ≤ 4 * M.Q (twoSum (ZMod q) t N) := by linarith
  have hfin := combine_bound M.cABI M.cABI_pos N n q κ 3 3 (by norm_num) (by norm_num) hd1 hd2
    (4 * M.Q (twoSum (ZMod q) t N)) hchain
  push_cast at hfin
  -- `q^{1/6} ≥ (cN)^{1/6} = c^{1/6} N^{1/6}` — the only step in which `c` occurs
  have hrq : c ^ (1 / 6 : ℝ) * (N : ℝ) ^ (1 / 6 : ℝ) ≤ (q : ℝ) ^ (1 / 6 : ℝ) := by
    rw [← Real.mul_rpow hc.le (Nat.cast_nonneg _)]
    exact Real.rpow_le_rpow (by positivity) hcq (by norm_num)
  have hmul : (0 : ℝ) ≤ M.cABI / (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ)) * Real.sqrt N :=
    mul_nonneg (div_nonneg M.cABI_pos.le (by positivity)) (Real.sqrt_nonneg _)
  have hstep := mul_le_mul_of_nonneg_left hrq hmul
  have heq : M.cABI * c ^ (1 / 6 : ℝ) / (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ)) * Real.sqrt N *
        (N : ℝ) ^ (1 / 6 : ℝ)
      = M.cABI / (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ)) * Real.sqrt N *
        (c ^ (1 / 6 : ℝ) * (N : ℝ) ^ (1 / 6 : ℝ)) := by ring
  rw [show (4 : ℝ) * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))
        = (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ)) * 4 from mul_comm _ _,
      ← div_div, div_mul_eq_mul_div, div_mul_eq_mul_div, heq]
  linarith

/-- **AUDIT FINDING (machine-checked).**  The paper justifies Case 2 by verifying `κ ≤ 2n-1` and
citing `thm:tani`.  In fact `κ < n` always holds there (`q ≤ N-2` forces `κ ≤ (N-3)/2 < ⌊N/2⌋`),
so `thm:abi` alone suffices and `cor:threshold` does not depend on `thm:tani` at all.  This
theorem is `threshold_small` with `M.tani` replaced by `M.abi`; its existence is the proof.
(`thm:main-odd` genuinely does need `thm:tani` in the subrange `2n-1 < q ≤ 4n-1`.) -/
theorem threshold_small_abi (M : QueryModel) (c : ℝ) (hc : 0 < c) (N q : ℕ) [NeZero q]
    (t : ZMod q) (ht : t = 0 ∨ Odd q) (hN : 6 ≤ N) (hcN : 5 ≤ c * N) (hcq : c * N ≤ q)
    (hlt : q + 1 < N) :
    M.cABI * c ^ (1 / 6 : ℝ) / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))) * Real.sqrt N *
        (N : ℝ) ^ (1 / 6 : ℝ) ≤ M.Q (twoSum (ZMod q) t N) := by
  have hq5 : 5 ≤ q := by
    have h : (5 : ℝ) ≤ (q : ℝ) := le_trans hcN hcq
    exact_mod_cast h
  set n := N / 2 with hn
  set κ := (q - 1) / 2 with hκ
  have hNn : N = 2 * n ∨ N = 2 * n + 1 := by omega
  have hκ2 : 2 ≤ κ := by omega
  have hκn : κ < n := by omega
  have hqκ : 2 * κ + 1 ≤ q := by omega
  have hd1 : N ≤ 3 * n := by omega
  have hd2 : q ≤ 3 * κ := by omega
  have hclaw := M.abi n κ hκ2 hκn
  have htr := Q_claw_le_twoSum_zero M N n hNn (cyc q κ) (cyc_add_ne_zero hqκ) (cyc_injective hqκ)
  have hnn : (0 : ℝ) ≤ M.cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ) :=
    mul_nonneg (mul_nonneg M.cABI_pos.le (Real.sqrt_nonneg _))
      (Real.rpow_nonneg (Nat.cast_nonneg _) _)
  have h0 := Q_zero_le_target M N q t ht (M.cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ) / 2)
    (by linarith) (by linarith)
  have hchain : M.cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ)
      ≤ 4 * M.Q (twoSum (ZMod q) t N) := by linarith
  have hfin := combine_bound M.cABI M.cABI_pos N n q κ 3 3 (by norm_num) (by norm_num) hd1 hd2
    (4 * M.Q (twoSum (ZMod q) t N)) hchain
  push_cast at hfin
  have hrq : c ^ (1 / 6 : ℝ) * (N : ℝ) ^ (1 / 6 : ℝ) ≤ (q : ℝ) ^ (1 / 6 : ℝ) := by
    rw [← Real.mul_rpow hc.le (Nat.cast_nonneg _)]
    exact Real.rpow_le_rpow (by positivity) hcq (by norm_num)
  have hmul : (0 : ℝ) ≤ M.cABI / (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ)) * Real.sqrt N :=
    mul_nonneg (div_nonneg M.cABI_pos.le (by positivity)) (Real.sqrt_nonneg _)
  have hstep := mul_le_mul_of_nonneg_left hrq hmul
  have heq : M.cABI * c ^ (1 / 6 : ℝ) / (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ)) * Real.sqrt N *
        (N : ℝ) ^ (1 / 6 : ℝ)
      = M.cABI / (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ)) * Real.sqrt N *
        (c ^ (1 / 6 : ℝ) * (N : ℝ) ^ (1 / 6 : ℝ)) := by ring
  rw [show (4 : ℝ) * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))
        = (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ)) * 4 from mul_comm _ _,
      ← div_div, div_mul_eq_mul_div, div_mul_eq_mul_div, heq]
  linarith

/-- **`cor:threshold`, lower-bound half.**  For every `c > 0` and every `q ≥ cN` (any parity when
`t = 0`; every `t` when `q` is odd), `Q(2Sum_{Z_q,t,N}) ≥ A_c · N^{2/3}` where `A_c` is the
minimum of the two case constants.  The FIRST entry (case `q ≥ N-1`) contains no `c`; the SECOND
(case `cN ≤ q < N-1`) carries the factor `c^{1/6}`.  This is the formal content of the paper's
"the `c`-dependence arises only in the case `cN ≤ q < N-1`".
The matching `O(N^{2/3})` upper bound of Ambainis / Childs–Eisenberg is not formalized here. -/
theorem threshold (M : QueryModel) (c : ℝ) (hc : 0 < c) (N q : ℕ) [NeZero q] (t : ZMod q)
    (ht : t = 0 ∨ Odd q) (hN : 6 ≤ N) (hcN : 5 ≤ c * N) (hcq : c * N ≤ q) :
    min (M.cABI / (4 * (Real.sqrt 3 * (6 : ℝ) ^ (1 / 6 : ℝ))))
        (M.cABI * c ^ (1 / 6 : ℝ) / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))))
      * Real.sqrt N * (N : ℝ) ^ (1 / 6 : ℝ) ≤ M.Q (twoSum (ZMod q) t N) := by
  have hP : (0 : ℝ) ≤ Real.sqrt N * (N : ℝ) ^ (1 / 6 : ℝ) := by positivity
  by_cases hcase : q + 1 < N
  · have h := threshold_small M c hc N q t ht hN hcN hcq hcase
    calc min (M.cABI / (4 * (Real.sqrt 3 * (6 : ℝ) ^ (1 / 6 : ℝ))))
            (M.cABI * c ^ (1 / 6 : ℝ) / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))))
          * Real.sqrt N * (N : ℝ) ^ (1 / 6 : ℝ)
        = min (M.cABI / (4 * (Real.sqrt 3 * (6 : ℝ) ^ (1 / 6 : ℝ))))
            (M.cABI * c ^ (1 / 6 : ℝ) / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))))
          * (Real.sqrt N * (N : ℝ) ^ (1 / 6 : ℝ)) := by ring
      _ ≤ M.cABI * c ^ (1 / 6 : ℝ) / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ)))
          * (Real.sqrt N * (N : ℝ) ^ (1 / 6 : ℝ)) :=
          mul_le_mul_of_nonneg_right (min_le_right _ _) hP
      _ = M.cABI * c ^ (1 / 6 : ℝ) / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ)))
          * Real.sqrt N * (N : ℝ) ^ (1 / 6 : ℝ) := by ring
      _ ≤ _ := h
  · have h := threshold_large M N q t ht hN (by omega)
    calc min (M.cABI / (4 * (Real.sqrt 3 * (6 : ℝ) ^ (1 / 6 : ℝ))))
            (M.cABI * c ^ (1 / 6 : ℝ) / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))))
          * Real.sqrt N * (N : ℝ) ^ (1 / 6 : ℝ)
        = min (M.cABI / (4 * (Real.sqrt 3 * (6 : ℝ) ^ (1 / 6 : ℝ))))
            (M.cABI * c ^ (1 / 6 : ℝ) / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))))
          * (Real.sqrt N * (N : ℝ) ^ (1 / 6 : ℝ)) := by ring
      _ ≤ M.cABI / (4 * (Real.sqrt 3 * (6 : ℝ) ^ (1 / 6 : ℝ)))
          * (Real.sqrt N * (N : ℝ) ^ (1 / 6 : ℝ)) :=
          mul_le_mul_of_nonneg_right (min_le_left _ _) hP
      _ = M.cABI / (4 * (Real.sqrt 3 * (6 : ℝ) ^ (1 / 6 : ℝ)))
          * Real.sqrt N * (N : ℝ) ^ (1 / 6 : ℝ) := by ring
      _ ≤ _ := h

/-- `√N · N^{1/6} = N^{2/3}`: the corollary's bound really is `Ω(N^{2/3})`. -/
theorem sqrt_mul_rpow_eq (N : ℕ) (hN : 0 < N) :
    Real.sqrt N * (N : ℝ) ^ (1 / 6 : ℝ) = (N : ℝ) ^ (2 / 3 : ℝ) := by
  have h : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hN
  rw [Real.sqrt_eq_rpow, ← Real.rpow_add h]
  norm_num

/-! ## `thm:oabarrier` — the orthogonal-array barrier -/

/-- The diagonal array `T = {(x,x)}` really is an index-1 array. -/
theorem ED_isIndexOne (q : ℕ) : IsIndexOne2 (fun a b : Fin q => a = b) :=
  ⟨fun a => ⟨a, rfl, fun _ h => h.symm⟩, fun b => ⟨b, rfl, fun _ h => h⟩⟩

/-- **`thm:oabarrier`(i).**  For `k = 2` and `q < N`, pigeonhole makes the element-distinctness
orthogonal-array problem identically `1`. -/
theorem oabarrier_ED (N q : ℕ) (hq : q < N) (x : Fin N → Fin q) : ED N q x = true := by
  simp only [ED, twoOAProblem, decide_eq_true_eq]
  have hni : ¬ Function.Injective x := by
    intro hinj
    have h := Fintype.card_le_of_injective x hinj
    simp only [Fintype.card_fin] at h
    omega
  rw [Function.not_injective_iff] at hni
  obtain ⟨i, j, hfe, hne⟩ := hni
  exact ⟨i, j, hne, hfe⟩

/-- **`thm:oabarrier`(i), consequence.**  Hence `Q = 0` there, so no bound uniform over the arrays
can be positive. -/
theorem oabarrier_ED_Q (M : QueryModel) (N q : ℕ) (hq : q < N) : M.Q (ED N q) = 0 :=
  M.constQ (ED N q) true (oabarrier_ED N q hq)

/-- **`thm:oabarrier`(ii).**  Over `G = (Z_p)^m` with `p ∣ k` and `N > (k-1)p^m`, some value
occurs `k` times and those `k` positions sum to `0`, so `kSum` is identically `1`.

AUDIT NOTE: the paper hypothesizes `p` **prime**.  Primality is not used — only `p ∣ k` and the
fact that `(Z_p)^m` has exponent dividing `p`.  The statement below is therefore strictly stronger
than the paper's. -/
theorem oabarrier_kSum {p m k N : ℕ} [NeZero p] (hpk : p ∣ k)
    (hN : (k - 1) * p ^ m < N) (x : Fin N → (Fin m → ZMod p)) :
    kSum (Fin m → ZMod p) k 0 N x = true := by
  classical
  have hcard : Fintype.card (Fin m → ZMod p) = p ^ m := by
    simp [ZMod.card]
  have hlt : Fintype.card (Fin m → ZMod p) * (k - 1) < Fintype.card (Fin N) := by
    rw [hcard, Fintype.card_fin, mul_comm]; exact hN
  obtain ⟨y, hy⟩ := Fintype.exists_lt_card_fiber_of_mul_lt_card x hlt
  have hk : k ≤ (Finset.univ.filter (fun i => x i = y)).card := by omega
  obtain ⟨S, hSsub, hScard⟩ := Finset.exists_subset_card_eq hk
  have hval : ∀ i ∈ S, x i = y := by
    intro i hi
    have := hSsub hi
    simpa using this
  have hpz : ∀ z : Fin m → ZMod p, (p : ℕ) • z = 0 := by
    intro z
    funext i
    simp [nsmul_eq_mul]
  have hsum : ∑ i ∈ S, x i = 0 := by
    rw [Finset.sum_congr rfl hval, Finset.sum_const, hScard]
    obtain ⟨u, rfl⟩ := hpk
    rw [mul_comm, mul_smul, hpz, smul_zero]
  simp only [kSum, decide_eq_true_eq]
  exact ⟨S, hScard, hsum⟩

/-! ## Witness examples: the encoding identity is not vacuous

`q = 5, κ = 2, n = 3`, and a concrete `(f,g)` pair on each side of the identity. -/

example : (2 : ℕ) * 2 + 1 ≤ 5 := by norm_num

/-- A concrete claw (`f 0 = g 1`) is seen by the encoded `2Sum` instance. -/
example :
    twoSum (ZMod 5) 0 (2 * 3)
        (encode 3 (cyc 5 2) (pairUp 3 ![0, 1, 1] ![1, 0, 1])) = true := by
  rw [twoSum_encode_cyc_pair (by norm_num)]
  decide

/-- A concrete non-claw (`f` only takes the value `0`, `g` only the value `1`) is seen as a
negative instance: the encoded string has no `0`-sum pair. -/
example :
    twoSum (ZMod 5) 0 (2 * 3)
        (encode 3 (cyc 5 2) (pairUp 3 ![0, 0, 0] ![1, 1, 1])) = false := by
  rw [twoSum_encode_cyc_pair (by norm_num)]
  decide

/-- Both sides of `lem:oddN` at `q = 5, κ = 2, n = 3`, length `7`. -/
example :
    twoSum (ZMod 5) 0 (2 * 3 + 1)
        (Fin.snoc (encode 3 (cyc 5 2) (pairUp 3 ![0, 0, 0] ![1, 1, 1])) (0 : ZMod 5)) = false := by
  rw [twoSum_encode_snoc_cyc (by norm_num), Claw_pairUp]
  decide

/-- The encoded values really do lie in `{1,…,κ} ∪ {q-κ,…,q-1}` (`q = 5, κ = 2`). -/
example : (cyc 5 2 0).val = 1 ∧ (cyc 5 2 1).val = 2 ∧ (-(cyc 5 2 0)).val = 4 ∧
    (-(cyc 5 2 1)).val = 3 := by decide

example : (cyc 5 2 0).val = 1 ∧ 1 ≤ (cyc 5 2 0).val ∧ (cyc 5 2 0).val ≤ 2 :=
  cyc_val (by norm_num) 0

example : (-(cyc 5 2 1)).val = 5 - (1 + 1) ∧ 5 - 2 ≤ (-(cyc 5 2 1)).val ∧
    (-(cyc 5 2 1)).val ≤ 5 - 1 := neg_cyc_val (by norm_num) 1

example (a b : Fin 2) : cyc 5 2 a + cyc 5 2 b ≠ 0 := cyc_add_ne_zero (by norm_num) a b

example : Function.Injective (cyc 5 2) := cyc_injective (by norm_num)

example (a b : Fin 2) : cyc 5 2 a + -(cyc 5 2 b) = 0 ↔ a = b := cyc_sub_eq_zero_iff (by norm_num) a b

/-- `lem:shift` at `q = 5, t = 0, t' = 1, c = 3` (`3 + 3 = 6 = 1` in `ZMod 5`). -/
example (x : Fin 4 → ZMod 5) :
    twoSum (ZMod 5) 1 4 (fun i => x i + 3) = twoSum (ZMod 5) 0 4 x :=
  twoSum_shift 0 1 3 (by decide) 4 x

example (M : QueryModel) : M.Q (twoSum (ZMod 5) 0 4) ≤ 2 * M.Q (twoSum (ZMod 5) 1 4) :=
  Q_twoSum_shift M 0 1 3 (by decide) 4

example : ∃ c : ZMod 5, c + c = 1 := exists_half_odd (by decide) 1

/-- `lem:encode` query part at `q = 5, κ = 2, n = 3` (`N = 6`), and `lem:oddN` at `N = 7`. -/
example (M : QueryModel) : M.Q (Claw 3 2) ≤ 2 * M.Q (twoSum (ZMod 5) 0 (2 * 3)) :=
  Q_claw_le_encode M 3 (cyc 5 2) (cyc_add_ne_zero (by norm_num)) (cyc_injective (by norm_num))

example (M : QueryModel) : M.Q (Claw 3 2) ≤ 2 * M.Q (twoSum (ZMod 5) 0 (2 * 3 + 1)) :=
  Q_claw_le_encode_odd M 3 (cyc 5 2) (cyc_add_ne_zero (by norm_num)) (cyc_injective (by norm_num))

example (M : QueryModel) : M.Q (Claw 3 2) ≤ 2 * M.Q (twoSum (ZMod 5) 0 7) :=
  Q_claw_le_twoSum_zero M 7 3 (by norm_num) (cyc 5 2) (cyc_add_ne_zero (by norm_num))
    (cyc_injective (by norm_num))

/-- The arithmetic helpers at concrete values. -/
example : Real.sqrt 12 / Real.sqrt 3 ≤ Real.sqrt 6 := sqrt_div_le 12 6 3 (by norm_num)

example : (5 : ℝ) ^ (1 / 6 : ℝ) / (3 : ℝ) ^ (1 / 6 : ℝ) ≤ (2 : ℝ) ^ (1 / 6 : ℝ) := by
  have := rpow6_div_le 5 2 3 (by norm_num)
  norm_num at this ⊢
  exact this

/-- **`thm:main-odd` witness**: `q = 5` (odd, `≥ 5`), `N = 12`, so `n = 6` and `q+1 = 6 ≤ 24 = 4n`. -/
example (M : QueryModel) :
    M.cABI / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))) * Real.sqrt 12 * (5 : ℝ) ^ (1 / 6 : ℝ)
      ≤ M.Q (twoSum (ZMod 5) 0 12) := by
  have h := main_odd M 12 5 0 (by decide) (by norm_num) (by norm_num)
  norm_num at h ⊢
  exact h

/-- **`thm:main-odd` (`thm:abi`-only subrange) witness**: `q + 1 = 6 ≤ 12 = 2n`. -/
example (M : QueryModel) :
    M.cABI / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))) * Real.sqrt 12 * (5 : ℝ) ^ (1 / 6 : ℝ)
      ≤ M.Q (twoSum (ZMod 5) 0 12) := by
  have h := main_odd_abi M 12 5 0 (by decide) (by norm_num) (by norm_num)
  norm_num at h ⊢
  exact h

/-- **`thm:main-general` witness**: `G = ZMod 5`, `|G| = 5`, `|G[2]| = 1`, `κ = 2`, `N = 12`. -/
example : Fintype.card (ZMod 5) = 5 ∧ (torsion2 (ZMod 5)).card = 1 := by decide

example : ∀ a ∈ ({1, 2} : Finset (ZMod 5)), ∀ b ∈ ({1, 2} : Finset (ZMod 5)), a + b ≠ 0 := by decide

example (M : QueryModel) :
    M.cABI / (2 * Real.sqrt 3) * Real.sqrt 12 * (2 : ℝ) ^ (1 / 6 : ℝ)
      ≤ M.Q (twoSum (ZMod 5) 0 12) := by
  have h := main_general (G := ZMod 5) M 12 6 2 (by norm_num) (by decide) (by norm_num)
    (by norm_num)
  norm_num at h ⊢
  exact h

/-- **`cor:threshold` Case 1 witness**: `N = 12`, `q = 11 ≥ N-1`, `t = 0`. -/
example (M : QueryModel) :
    M.cABI / (4 * (Real.sqrt 3 * (6 : ℝ) ^ (1 / 6 : ℝ))) * Real.sqrt 12 * (12 : ℝ) ^ (1 / 6 : ℝ)
      ≤ M.Q (twoSum (ZMod 11) 0 12) := by
  have h := threshold_large M 12 11 0 (Or.inl rfl) (by norm_num) (by norm_num)
  norm_num at h ⊢
  exact h

/-- **`cor:threshold` Case 2 witness**: `c = 1/2`, `N = 12`, `q = 6`, so `cN = 6 ≤ q` and
`q + 1 = 7 < 12 = N`. -/
example (M : QueryModel) :
    M.cABI * (1 / 2 : ℝ) ^ (1 / 6 : ℝ) / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ)))
        * Real.sqrt 12 * (12 : ℝ) ^ (1 / 6 : ℝ) ≤ M.Q (twoSum (ZMod 6) 0 12) := by
  have h := threshold_small M (1 / 2) (by norm_num) 12 6 0 (Or.inl rfl) (by norm_num)
    (by norm_num) (by norm_num) (by norm_num)
  norm_num at h ⊢
  exact h

/-- **Audit finding witness**: the same Case-2 bound proved from `thm:abi` alone. -/
example (M : QueryModel) :
    M.cABI * (1 / 2 : ℝ) ^ (1 / 6 : ℝ) / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ)))
        * Real.sqrt 12 * (12 : ℝ) ^ (1 / 6 : ℝ) ≤ M.Q (twoSum (ZMod 6) 0 12) := by
  have h := threshold_small_abi M (1 / 2) (by norm_num) 12 6 0 (Or.inl rfl) (by norm_num)
    (by norm_num) (by norm_num) (by norm_num)
  norm_num at h ⊢
  exact h

/-- **`cor:threshold` witness** (combined form). -/
example (M : QueryModel) :
    min (M.cABI / (4 * (Real.sqrt 3 * (6 : ℝ) ^ (1 / 6 : ℝ))))
        (M.cABI * (1 / 2 : ℝ) ^ (1 / 6 : ℝ) / (4 * (Real.sqrt 3 * (3 : ℝ) ^ (1 / 6 : ℝ))))
      * Real.sqrt 12 * (12 : ℝ) ^ (1 / 6 : ℝ) ≤ M.Q (twoSum (ZMod 6) 0 12) := by
  have h := threshold M (1 / 2) (by norm_num) 12 6 0 (Or.inl rfl) (by norm_num) (by norm_num)
    (by norm_num)
  norm_num at h ⊢
  exact h

example : Real.sqrt 12 * (12 : ℝ) ^ (1 / 6 : ℝ) = (12 : ℝ) ^ (2 / 3 : ℝ) := by
  have := sqrt_mul_rpow_eq 12 (by norm_num)
  norm_num at this ⊢
  exact this

/-- **`thm:oabarrier` witnesses.**  (i) `q = 2 < 3 = N`; (ii) `p = 2 ∣ k = 2`, `m = 1`,
`(k-1)p^m = 2 < 5 = N`. -/
example : IsIndexOne2 (fun a b : Fin 2 => a = b) := ED_isIndexOne 2

example (x : Fin 3 → Fin 2) : ED 3 2 x = true := oabarrier_ED 3 2 (by norm_num) x

example : ED 3 2 ![0, 1, 0] = true := by decide

example (M : QueryModel) : M.Q (ED 3 2) = 0 := oabarrier_ED_Q M 3 2 (by norm_num)

example (x : Fin 5 → (Fin 1 → ZMod 2)) : kSum (Fin 1 → ZMod 2) 2 0 5 x = true :=
  oabarrier_kSum (by norm_num) (by norm_num) x

/-! ## Non-vacuity of the interface itself

Every theorem above that mentions `M : QueryModel` is CONDITIONAL.  If `QueryModel` were
uninhabited, all of them would be vacuously true and this audit would be worthless.  The model
below inhabits it.

**`demoModel` is NOT quantum query complexity and makes no claim to be.**  It is a consistency
witness only: `0` on constant functions, and a function of the input LENGTH otherwise.  The
intended model is the bounded-error quantum query complexity of `sec:prelim`, whose `abi`/`tani`
fields are the imported theorems of Ambainis–Balodis–Iraids and Tani, not proved here. -/

open Classical in
/-- The consistency-witness complexity measure. -/
noncomputable def demoQ : {M : ℕ} → {Alph : Fin M → Type} → [∀ i, Fintype (Alph i)] →
    (((i : Fin M) → Alph i) → Bool) → ℝ :=
  fun {M} {_} _ f => if (∀ y z, f y = f z) then 0 else Real.sqrt M * (M : ℝ) ^ (1 / 6 : ℝ)

theorem demoB_nonneg (M : ℕ) : (0 : ℝ) ≤ Real.sqrt M * (M : ℝ) ^ (1 / 6 : ℝ) := by positivity

theorem demoB_mono {M M' : ℕ} (h : M ≤ M') :
    Real.sqrt M * (M : ℝ) ^ (1 / 6 : ℝ) ≤ Real.sqrt M' * (M' : ℝ) ^ (1 / 6 : ℝ) :=
  mul_le_mul (Real.sqrt_le_sqrt (by exact_mod_cast h))
    (Real.rpow_le_rpow (by positivity) (by exact_mod_cast h) (by norm_num)) (by positivity)
    (Real.sqrt_nonneg _)

theorem demoQ_const {M : ℕ} {Alph : Fin M → Type} [∀ i, Fintype (Alph i)]
    (f : ((i : Fin M) → Alph i) → Bool) (h : ∀ y z, f y = f z) : demoQ f = 0 := by
  classical
  simp only [demoQ]
  rw [if_pos h]

theorem demoQ_nonconst {M : ℕ} {Alph : Fin M → Type} [∀ i, Fintype (Alph i)]
    (f : ((i : Fin M) → Alph i) → Bool) (h : ¬ ∀ y z, f y = f z) :
    demoQ f = Real.sqrt M * (M : ℝ) ^ (1 / 6 : ℝ) := by
  classical
  simp only [demoQ]
  rw [if_neg h]

theorem demoQ_le {M : ℕ} {Alph : Fin M → Type} [∀ i, Fintype (Alph i)]
    (f : ((i : Fin M) → Alph i) → Bool) : demoQ f ≤ Real.sqrt M * (M : ℝ) ^ (1 / 6 : ℝ) := by
  by_cases h : ∀ y z, f y = f z
  · rw [demoQ_const f h]; exact demoB_nonneg M
  · rw [demoQ_nonconst f h]

/-- `Claw_{n→κ}` is not a constant function when `2 ≤ κ` and `1 ≤ n` — needed so that the
consistency witness can satisfy `abi` and `tani`.  (It also shows those fields are not vacuous.) -/
theorem Claw_nonconst (n κ : ℕ) (hκ : 2 ≤ κ) (hn : 1 ≤ n) :
    ¬ (∀ y z : Fin (2 * n) → Fin κ, Claw n κ y = Claw n κ z) := by
  intro h
  have h0 : (0 : ℕ) < κ := by omega
  have h1 : (1 : ℕ) < κ := by omega
  have hc1 : Claw n κ (pairUp n (fun _ => ⟨0, h0⟩) (fun _ => ⟨0, h0⟩)) = true := by
    rw [Claw_pairUp, decide_eq_true_eq]
    exact ⟨⟨0, by omega⟩, ⟨0, by omega⟩, rfl⟩
  have hc2 : Claw n κ (pairUp n (fun _ => ⟨0, h0⟩) (fun _ => ⟨1, h1⟩)) = false := by
    rw [Claw_pairUp, decide_eq_false_iff_not]
    rintro ⟨i, j, hij⟩
    have := congrArg Fin.val hij
    simp at this
  have := h (pairUp n (fun _ => ⟨0, h0⟩) (fun _ => ⟨0, h0⟩))
    (pairUp n (fun _ => ⟨0, h0⟩) (fun _ => ⟨1, h1⟩))
  rw [hc1, hc2] at this
  exact Bool.noConfusion this

/-- **`QueryModel` is inhabited**, so every conditional theorem above is non-vacuous. -/
noncomputable def demoModel : QueryModel where
  Q := demoQ
  restrict := by
    intro M Alph inst D f
    by_cases hf : ∀ y z, f y = f z
    · rw [demoQ_const _ (fun y z => hf _ _), demoQ_const _ hf]
    · rw [demoQ_nonconst _ hf]; exact demoQ_le _
  relabel := by
    intro M Alph Alph' inst inst' e f
    by_cases hf : ∀ y z, f y = f z
    · rw [demoQ_const _ (fun y z => hf _ _), demoQ_const _ hf]; norm_num
    · rw [demoQ_nonconst _ hf]
      have h1 := demoQ_le (fun y : ((i : Fin M) → Alph' i) => f (fun i => e i (y i)))
      have h2 := demoB_nonneg M
      linarith
  freeze := by
    intro M Alph inst a f
    by_cases hf : ∀ y z, f y = f z
    · rw [demoQ_const _ (fun y z => hf _ _), demoQ_const _ hf]
    · rw [demoQ_nonconst _ hf]
      exact le_trans (demoQ_le _) (demoB_mono (Nat.le_succ M))
  constQ := by
    intro M Alph inst f b hb
    exact demoQ_const f (fun y z => by rw [hb y, hb z])
  cABI := 1
  cABI_pos := one_pos
  abi := by
    intro n κ h2 hn
    rw [demoQ_nonconst _ (Claw_nonconst n κ h2 (by omega)), one_mul]
    exact mul_le_mul (Real.sqrt_le_sqrt (by exact_mod_cast (by omega : n ≤ 2 * n)))
      (Real.rpow_le_rpow (by positivity) (by exact_mod_cast (by omega : κ ≤ 2 * n))
        (by norm_num)) (by positivity) (Real.sqrt_nonneg _)
  tani := by
    intro n κ h2 hn
    rw [demoQ_nonconst _ (Claw_nonconst n κ h2 (by omega)), one_mul]
    exact mul_le_mul (Real.sqrt_le_sqrt (by exact_mod_cast (by omega : n ≤ 2 * n)))
      (Real.rpow_le_rpow (by positivity) (by exact_mod_cast (by omega : κ ≤ 2 * n))
        (by norm_num)) (by positivity) (Real.sqrt_nonneg _)

/-! ## Machine-checked citation manifest (`#print axioms`)

The current protocol's source-registration requirement is made mechanical: every
top-level theorem below must depend on Lean's three standard axioms and nothing else.  In
particular there is no `axiom` in this development — the imported bounds are structure FIELDS. -/

#print axioms twoSum_encode
#print axioms twoSum_encode_cyc
#print axioms twoSum_encode_cyc_pair
#print axioms twoSum_snoc_zero
#print axioms twoSum_encode_snoc
#print axioms twoSum_encode_snoc_cyc
#print axioms QueryModel.relabel_inj
#print axioms Q_claw_le_encode
#print axioms Q_claw_le_encode_odd
#print axioms Q_claw_le_twoSum_zero
#print axioms twoSum_shift
#print axioms Q_twoSum_shift
#print axioms exists_half_odd
#print axioms combine_bound
#print axioms main_odd
#print axioms main_odd_abi
#print axioms exists_repr_set
#print axioms main_general
#print axioms Q_zero_le_target
#print axioms threshold_large
#print axioms threshold_small
#print axioms threshold_small_abi
#print axioms threshold
#print axioms sqrt_mul_rpow_eq
#print axioms ED_isIndexOne
#print axioms oabarrier_ED
#print axioms oabarrier_ED_Q
#print axioms oabarrier_kSum
#print axioms demoModel

end KsumAudit
