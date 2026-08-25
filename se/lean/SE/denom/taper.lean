/-
`SE/denom/taper.lean` — linked node module.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : SE.denom.taper                (alias `TAP`)
node file      : se/proof-dag/nodes/SE.denom.taper.yaml
decomposition / role    : none / proof
epistemic status (read from the node file on 2026-08-17): **PROVED**
mechanization  : proved, for the WHOLE frozen Claim (see "Scope" below; ruling R2's unrendered
                 conjunct was discharged at tier 2 on 2026-08-17, node `SE.formal.t2`).
claim_hash     : sha256:d181c0bdb60c41fdfca5b888339302081d5908caf23350ecfd3c88d297ae8221
                 (SHA-256 of the frozen Claim text quoted below, UTF-8, LF, stripped)

current_claim_hash: sha256:d9c47838a0eab4bfcd80edc9ebc30b00cc8a215194d98c41e0632708ed67fa20

CURRENT CANONICAL CLAIM (verbatim from the node record):

  For the linear taper coefficients a_k=(K-k)_+, |a_(k-1)-a_k|<=1, |a_k|<=sqrt(n/k) for k>=1, and |a_k|<=sqrt(n).

END CURRENT CANONICAL CLAIM

FROZEN CLAIM (verbatim from `claim` in the node record):

  SE.denom.taper — taper scalar arithmetic |a_{k-1}-a_k|<=1, |a_k|<=sqrt(n/k) TIGHT, <=sqrt n

────────────────────────────────────────────────────────────────────────────────────────────────
SCOPE — ruling R2 (2026-07-30) DISCHARGED at tier 2 (2026-08-17, node `SE.formal.t2`).

The frozen Claim has THREE conjuncts; `Claim` below now renders ALL THREE, in the paper's
linear-taper normalization `a_k = α_k = (K−k)_+` with `K = K n = ⌊n^{1/3}⌋`:

* conjunct 1: `|a_{k-1} − a_k| ≤ 1`, i.e. `|β_d| ≤ 1` (`SE.abs_beta_le_one`);
* conjunct 2, the TIGHT `|a_k| ≤ √(n/k)` (`SE.alpha_le_sqrt_div`), for `1 ≤ k`;
* conjunct 3: `|a_k| ≤ √n`, via `α_k ≤ K ≤ √n` (`SE.alpha_le_K` + `SE.K_le_sqrt`;
  the absolute value is the plain value since `α_k ≥ 0`).

HOW CONJUNCT 2 IS NOW PROVED, and what its `1 ≤ k` binder means (tier-2 record).  The tier-1
ruling R2 declared conjunct 2 unrenderable because its "normalization constant is fixed by the
operator layer".  That reading was too pessimistic: in the paper's own normalization `a_k = α_k`
the conjunct is an INTEGER inequality, `(K−k)²·k ≤ n`, and it follows from `K³ ≤ n` by AM–GM,
`4(m+k)³ − 27m²k = (m−2k)²(4m+k) ≥ 0` at `m = K−k` (`SE.sq_alpha_mul_le`).  No operator layer and
no normalization choice enters.

The binder `1 ≤ k` is not a weakening: at `k = 0` the frozen text's right-hand side `√(n/0)` is
not a real number (the bound is vacuous, `α₀ = K ≤ ∞`), while Lean's `n/0 = 0` convention would
turn the instance into the FALSE statement `K ≤ 0`.  The `k`-cleared form of the same conjunct,
`k·α_k² ≤ n`, IS true for every `k` including `0` and is proved unconditionally as
`SE.sq_alpha_mul_le'`; for `k ≥ 1` the two are equivalent.  The load-bearing consequence named in
the proof note ("without it the stay channel is Θ(K), cancelling ‖Γ‖≥K") is the product form
`α_k·√(k/n) ≤ 1` (`SE.alpha_mul_sqrt_le_one`), also proved here for every `k`.  Nothing about
attainment is claimed: the word TIGHT in the frozen text distinguishes the `k`-dependent bound
from the crude `√n` conjunct — the true maximum of `α_d√(d/n)` on the window is `2√3/9 < 1`
(`SE.alpha_mul_sqrt_div_le`, `SE/Support/Envelope.lean`).

`holds` therefore mechanizes the WHOLE frozen Claim.  The module also
proves the exact discrete maximum `max_{0≤d<K} d(K−d−1) = ⌊(K−1)²/4⌋` (`SE.taper_max`) — that is
Theorem-A arithmetic named by the node `SE.formal.t1`, kept here with the rest of the taper
arithmetic; it is deliberately NOT part of `Claim` (it is not one of the frozen conjuncts).

No `sorry`.
-/
import SE.Support.Defs
import SE.Support.Cbrt

namespace SE

/-! ## Values of the taper coefficients -/

theorem alpha_nonneg (Kv k : ℕ) : 0 ≤ alpha Kv k := by
  unfold alpha; positivity

theorem alpha_le_K (Kv k : ℕ) : alpha Kv k ≤ (Kv : ℝ) := by
  unfold alpha
  exact_mod_cast Nat.sub_le Kv k

theorem alpha_antitone {Kv k l : ℕ} (h : k ≤ l) : alpha Kv l ≤ alpha Kv k := by
  unfold alpha
  exact_mod_cast Nat.sub_le_sub_left h Kv

theorem alpha_of_le {Kv k : ℕ} (h : Kv ≤ k) : alpha Kv k = 0 := by
  unfold alpha
  simp [Nat.sub_eq_zero_of_le h]

/-- `β_d = 1` for `0 ≤ d < K` — the linear taper (paper §9). -/
theorem beta_eq_one {Kv d : ℕ} (h : d < Kv) : beta Kv d = 1 := by
  have h1 : Kv - d = (Kv - (d + 1)) + 1 := by omega
  unfold beta alpha
  rw [h1]
  push_cast
  ring

/-- `β_d = 0` outside the taper window. -/
theorem beta_eq_zero {Kv d : ℕ} (h : Kv ≤ d) : beta Kv d = 0 := by
  unfold beta
  rw [alpha_of_le h, alpha_of_le (le_trans h (Nat.le_succ d))]
  ring

/-- The frozen Claim's first conjunct, `|a_{k-1} − a_k| ≤ 1`, for the linear taper. -/
theorem abs_beta_le_one {Kv d : ℕ} : |beta Kv d| ≤ 1 := by
  by_cases h : d < Kv
  · rw [beta_eq_one h]; norm_num
  · rw [beta_eq_zero (by omega)]; norm_num

/-- `K n ≤ √n`: from `K² ≤ K³ ≤ n` (with the `K = 0` case trivial).  This is the bridge for the
frozen Claim's third conjunct `|a_k| ≤ √n`. -/
theorem K_le_sqrt (n : ℕ) : (K n : ℝ) ≤ Real.sqrt (n : ℝ) := by
  have hsq : (K n : ℝ) ^ 2 ≤ (n : ℝ) := by
    have h : K n ^ 2 ≤ n := by
      rcases Nat.eq_zero_or_pos (K n) with h0 | h1
      · rw [h0]; simp
      · calc K n ^ 2 ≤ K n ^ 3 := Nat.pow_le_pow_right h1 (by norm_num)
          _ ≤ n := K_pow_le n
    exact_mod_cast h
  calc (K n : ℝ) = Real.sqrt ((K n : ℝ) ^ 2) := (Real.sqrt_sq (by positivity)).symm
    _ ≤ Real.sqrt (n : ℝ) := Real.sqrt_le_sqrt hsq

/-- The frozen Claim's third conjunct, `|a_k| ≤ √n`, for the linear taper at `K = K n`
(`α_k ≥ 0`, so the absolute value is the plain value). -/
theorem alpha_le_sqrt (n k : ℕ) : alpha (K n) k ≤ Real.sqrt (n : ℝ) :=
  le_trans (alpha_le_K _ _) (K_le_sqrt n)

/-! ## The frozen Claim's second conjunct: the TIGHT bound `|a_k| ≤ √(n/k)`

Tier 2 (2026-08-17, node `SE.formal.t2`); this discharges coordinator ruling R2's UNRENDERED
declaration.  Everything here is integer arithmetic on `K³ ≤ n`. -/

/-- The integer core of the TIGHT taper bound: `(K−k)²·k ≤ n`.

By AM–GM in the exact form `4(m+k)³ − 27m²k = (m−2k)²(4m+k) ≥ 0` with `m = K−k`, so
`(K−k)²·k ≤ 4K³/27 ≤ K³ ≤ n` (`SE.K_pow_le`). -/
theorem sq_alpha_mul_le (n k : ℕ) : ((K n - k : ℕ) : ℝ) ^ 2 * (k : ℝ) ≤ (n : ℝ) := by
  have hn0 : (0 : ℝ) ≤ (n : ℝ) := Nat.cast_nonneg n
  by_cases hk : K n ≤ k
  · rw [show (K n - k : ℕ) = 0 by omega]
    simpa using hn0
  · have hkK : k ≤ K n := by omega
    set m : ℕ := K n - k with hmdef
    have hmk : m + k = K n := by omega
    have hcube : ((K n : ℝ)) ^ (3 : ℕ) ≤ (n : ℝ) := K_cube_le_real n
    have hsum : (m : ℝ) + (k : ℝ) = (K n : ℝ) := by
      rw [← hmk]; push_cast; ring
    have hm0 : (0 : ℝ) ≤ (m : ℝ) := Nat.cast_nonneg m
    have hk0 : (0 : ℝ) ≤ (k : ℝ) := Nat.cast_nonneg k
    have hcube' : ((m : ℝ) + (k : ℝ)) ^ (3 : ℕ) ≤ (n : ℝ) := by rw [hsum]; exact hcube
    nlinarith [sq_nonneg ((m : ℝ) - 2 * (k : ℝ)), mul_nonneg hm0 hk0,
      mul_nonneg (mul_nonneg hm0 hm0) hk0]

/-- The `k`-cleared form of the second conjunct, true for EVERY `k` (including `k = 0`, where the
frozen `√(n/k)` is not a real bound): `k·α_k² ≤ n`. -/
theorem sq_alpha_mul_le' (n k : ℕ) : (k : ℝ) * (alpha (K n) k) ^ 2 ≤ (n : ℝ) := by
  have h := sq_alpha_mul_le n k
  have hα : alpha (K n) k = ((K n - k : ℕ) : ℝ) := rfl
  rw [hα]
  linarith [h]

/-- **The frozen Claim's second conjunct, the TIGHT bound**: `|a_k| = α_k ≤ √(n/k)` for `k ≥ 1`
(`α_k ≥ 0`, so the absolute value is the plain value).  See the module header for why `k = 0` is
excluded and for the `k`-cleared form that covers it. -/
theorem alpha_le_sqrt_div (n k : ℕ) (hk : 1 ≤ k) :
    alpha (K n) k ≤ Real.sqrt ((n : ℝ) / (k : ℝ)) := by
  have hk0 : (0 : ℝ) < (k : ℝ) := by exact_mod_cast hk
  have hsq : (alpha (K n) k) ^ 2 ≤ (n : ℝ) / (k : ℝ) := by
    rw [le_div_iff₀ hk0]
    have h := sq_alpha_mul_le n k
    have hα : alpha (K n) k = ((K n - k : ℕ) : ℝ) := rfl
    rw [hα]
    linarith [h]
  calc alpha (K n) k = Real.sqrt ((alpha (K n) k) ^ 2) :=
        (Real.sqrt_sq (alpha_nonneg _ _)).symm
    _ ≤ Real.sqrt ((n : ℝ) / (k : ℝ)) := Real.sqrt_le_sqrt hsq

/-- The load-bearing reading of the second conjunct (proof note: "without it the stay channel
is Θ(K)"): `α_k·√(k/n) ≤ 1`, for every `k` and every `n`. -/
theorem alpha_mul_sqrt_le_one (n k : ℕ) :
    alpha (K n) k * Real.sqrt ((k : ℝ) / (n : ℝ)) ≤ 1 := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · have h0 : K 0 = 0 := K_unique (by norm_num) (by norm_num)
    rw [h0, alpha_of_le (Nat.zero_le k)]
    simp
  have hn0 : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hn
  have hq : (0 : ℝ) ≤ (k : ℝ) / (n : ℝ) := div_nonneg (Nat.cast_nonneg k) hn0.le
  have ha := alpha_nonneg (K n) k
  have hprod : (alpha (K n) k * Real.sqrt ((k : ℝ) / (n : ℝ))) ^ 2 ≤ 1 := by
    rw [mul_pow, Real.sq_sqrt hq]
    have key : alpha (K n) k ^ 2 * ((k : ℝ) / (n : ℝ))
        = ((k : ℝ) * alpha (K n) k ^ 2) / (n : ℝ) := by ring
    rw [key, div_le_one hn0]
    exact sq_alpha_mul_le' n k
  nlinarith [mul_nonneg ha (Real.sqrt_nonneg ((k : ℝ) / (n : ℝ)))]

/-! ## The exact discrete maximum -/

private lemma taper_quadratic_le (m d : ℕ) (hd : d ≤ m) : d * (m - d) ≤ m ^ 2 / 4 := by
  rw [Nat.le_div_iff_mul_le (by norm_num : 0 < 4)]
  obtain ⟨e, he⟩ : ∃ e, m = d + e := ⟨m - d, by omega⟩
  subst he
  have : d + e - d = e := by omega
  rw [this]
  zify
  nlinarith [sq_nonneg ((d : ℤ) - (e : ℤ))]

private lemma taper_quadratic_attained (m : ℕ) : (m / 2) * (m - m / 2) = m ^ 2 / 4 := by
  rcases Nat.even_or_odd m with ⟨t, ht⟩ | ⟨t, ht⟩
  · subst ht
    have h1 : (t + t) / 2 = t := by omega
    have h2 : t + t - t = t := by omega
    rw [h1, h2, show (t + t) ^ 2 = 4 * (t * t) by ring, Nat.mul_div_cancel_left _ (by norm_num)]
  · subst ht
    have h1 : (2 * t + 1) / 2 = t := by omega
    have h2 : 2 * t + 1 - t = t + 1 := by omega
    have hdiv : (4 * (t * t + t) + 1) / 4 = t * t + t := by
      rw [Nat.mul_add_div (by norm_num)]
      simp
    rw [h1, h2, show (2 * t + 1) ^ 2 = 4 * (t * t + t) + 1 by ring, hdiv]
    ring

/-- **The exact discrete taper maximum**:
`max_{0 ≤ d < K} d·(K - d - 1) = ⌊(K-1)²/4⌋`, over `ℕ` (so `/` is floor division).

This is the arithmetic identity behind the `n^{1/6}` envelope of Theorem A
(`d(K-d-1) = (K-1)²/4 - (d-(K-1)/2)²`), and the node
`se/proof-dag/nodes/SE.formal.t1.yaml` names it explicitly. -/
theorem taper_max (Kv : ℕ) :
    (Finset.range Kv).sup (fun d => d * (Kv - d - 1)) = (Kv - 1) ^ 2 / 4 := by
  rcases Nat.eq_zero_or_pos Kv with rfl | hKv
  · simp
  refine le_antisymm (Finset.sup_le ?_) ?_
  · intro d hd
    rw [Finset.mem_range] at hd
    have h1 : Kv - d - 1 = (Kv - 1) - d := by omega
    rw [h1]
    exact taper_quadratic_le _ _ (by omega)
  · have hmem : (Kv - 1) / 2 ∈ Finset.range Kv := by
      rw [Finset.mem_range]; omega
    have := Finset.le_sup (f := fun d => d * (Kv - d - 1)) hmem
    have h1 : Kv - (Kv - 1) / 2 - 1 = (Kv - 1) - (Kv - 1) / 2 := by omega
    rw [h1] at this
    rwa [taper_quadratic_attained (Kv - 1)] at this

end SE

namespace SE.denom.taper

/-- The node's Lean claim — ALL THREE conjuncts of `SE.denom.taper`'s frozen Claim in the paper's
linear-taper normalization `a_k = α_k = (K−k)_+` (conjunct 2 added at tier 2, 2026-08-17,
discharging ruling R2; see the module header):

1. the taper differences are bounded by `1`: `|a_{k-1} − a_k| = |β_d| ≤ 1`;
2. the TIGHT bound `|a_k| = α_k ≤ √(n/k)` for `k ≥ 1`;
3. the taper coefficients are bounded by `√n`: `|a_k| = α_k ≤ √n` at `K = K n`. -/
def Claim : Prop :=
  (∀ Kv d : ℕ, |SE.beta Kv d| ≤ 1) ∧
    (∀ n k : ℕ, 1 ≤ k → SE.alpha (SE.K n) k ≤ Real.sqrt ((n : ℝ) / (k : ℝ))) ∧
    (∀ n k : ℕ, SE.alpha (SE.K n) k ≤ Real.sqrt (n : ℝ))

/-- `Claim` holds unconditionally (no hypotheses, no interface). -/
theorem holds : Claim :=
  ⟨fun _ _ => SE.abs_beta_le_one, SE.alpha_le_sqrt_div, SE.alpha_le_sqrt⟩

end SE.denom.taper
