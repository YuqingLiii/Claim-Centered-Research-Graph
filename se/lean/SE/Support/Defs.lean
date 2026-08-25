/-
`SE/Support/Defs.lean` — non-node support module.

Nodes served (≥ 2, which is why this is `Support/` and not a node module):
`SE.denom.taper`, `SE.denom.assembly.envelope`, `SE.denom`, `SE.br`, `SE.goal`,
plus the non-node modules `SE.Interface`, `SE.SelfTest`.

Everything here is *analytic-combinatorial*: integers, taper coefficients, real constants and the
error functions of the assembly envelope.  No representation theory appears at tier 1; symmetric
group / Littlewood–Richardson data enters only as abstract parameters (`SE/Interface.lean` and the
four hypothesis node modules under `SE/denom/Phi/legal/`).

The definitions correspond to the Set Equality construction recorded by the linked claim nodes.

No `sorry`.
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Tactic

namespace SE

/-! ## The taper length `K n = ⌊n^{1/3}⌋` -/

/-- `K n` is the taper length of the witness, `K n = ⌊n^{1/3}⌋` (paper: `\S`\,eq:witness-intro,
`K=\lfloor n^{1/3}\rfloor`).

It is defined here *combinatorially*, by the characterization `K^3 ≤ n < (K+1)^3`, which is proved
in `SE/Support/Cbrt.lean` (`SE.K_pow_le`, `SE.lt_K_succ_pow`, `SE.K_unique`).  The bridge to the
real cube root, `K n = ⌊(n : ℝ)^(1/3)⌋₊`, is `SE.K_eq_floor_rpow` in the same file, so the reader
may take either as the definition. -/
def K (n : ℕ) : ℕ := Nat.findGreatest (fun k => k ^ 3 ≤ n) n

/-! ## Taper coefficients -/

/-- The taper coefficient `α_k = (K - k)_+` (paper §4: `\alpha_k=(K-k)_+`, extended by zero outside
`0 ≤ k < K`).  Truncated natural subtraction *is* the positive part. -/
def alpha (Kv k : ℕ) : ℝ := ((Kv - k : ℕ) : ℝ)

/-- The defect-regrouping coefficient `β_d = α_d - α_{d+1}` (paper §9, before eq:defect-D). -/
def beta (Kv d : ℕ) : ℝ := alpha Kv d - alpha Kv (d + 1)

/-! ## The closed constants of Theorem B -/

/-- `M = (2/(3√3))·(√2 + √(15/8))`, the envelope constant of the paper's eq:Mconstant.

`SE.Mconst_eq` (in `SE/Support/Constants.lean`) proves the closed form `M = (4√6+3√10)/18`. -/
noncomputable def Mconst : ℝ := (2 / (3 * Real.sqrt 3)) * (Real.sqrt 2 + Real.sqrt (15 / 8))

/-- `C = 9/(18+4√6+3√10) = 0.2413852814754581733…`, the conditional constant of Theorem B
(paper eq:main).  `SE.inv_two_one_add_Mconst` proves `1/(2(1+M)) = C`. -/
noncomputable def Cconst : ℝ := 9 / (18 + 4 * Real.sqrt 6 + 3 * Real.sqrt 10)

/-! ## The envelope error functions

These name the two vanishing pieces of the paper's eq:final-envelope, so that the assembly can be
stated *quantitatively* (with explicit errors) and only then packaged asymptotically. -/

/-- The diagonal-`Φ` error term: the uniform bound on `√6·α_d/√(n-2d+1)` over `0 ≤ d < K`
(paper eq:final-envelope, third summand; it is `O(K/√n) = O(n^{-1/6})`). -/
noncomputable def errDiag (n Kv : ℕ) : ℝ :=
  Real.sqrt 6 * (Kv : ℝ) / Real.sqrt ((n : ℝ) - 2 * (Kv : ℝ) + 1)

/-- The distortion factor `√(n/(n-K))` by which the fourth (lower-block) term of
eq:final-envelope exceeds its `√(d/n)` model. -/
noncomputable def distort (n Kv : ℕ) : ℝ := Real.sqrt ((n : ℝ) / ((n : ℝ) - (Kv : ℝ)))

/-- The total envelope error: `‖D‖ ≤ ρ_max · (1 + M + errEnv n)`.  It is `O(n^{-1/6})`
(`SE.errEnv_le` and `SE.tendsto_errEnv` in `SE/Support/Limits.lean`). -/
noncomputable def errEnv (n Kv : ℕ) : ℝ :=
  errDiag n Kv + Real.sqrt (15 / 8) * (2 * Real.sqrt 3 / 9) * (distort n Kv - 1)

/-- The fully explicit right-hand side of the paper's eq:Dfinal, `‖D‖ ≤ 1 + M + o(1)`, with the
`o(1)` made concrete.  `c` is the implied constant of the hook envelope eq:rho-asymp. -/
noncomputable def envBound (c : ℝ) (n : ℕ) : ℝ :=
  (1 + c / (n : ℝ) ^ ((1 : ℝ) / 3)) * (1 + Mconst + errEnv n (K n))

/-- The explicit `o(1)` of Theorem B: `Adv ≥ (C - ε_n)·n^{1/3}` with `ε_n → 0`
(`SE.goal.composition_via_br`).  It collects the taper rounding `K ≥ n^{1/3} - 1` and the envelope
error `envBound c n - (1+M)`. -/
noncomputable def epsB (c : ℝ) (n : ℕ) : ℝ :=
  Cconst - (1 - 1 / (n : ℝ) ^ ((1 : ℝ) / 3)) / (2 * envBound c n)

end SE
