/-
`SE/denom.lean` — linked node module.
The aggregation step: channel bounds + taper arithmetic + defect orthogonality ⟹ the masked
denominator is O(1) — historically the place where obligation H4 hid one level below, which is
why the node's prose composition block (added 2026-07-30) is written out and mirrored here.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : SE.denom      (alias `DEN`)
node file      : se/proof-dag/nodes/SE.denom.yaml
decomposition / role    : AND / proof
children       : decomp, X, Y, Phi, familysplit, crossk, taper, assembly (eight)
epistemic status (read from the node file on 2026-07-30): **OPEN**
composition status on the node: **PROVED** ("as an aggregation schema"; certification A.27–A.31,
                 human review §8.5, second external review)
mechanization  : composition-checked, relative to Cited + taper.Claim + tame.Claim
claim_hash     : sha256:f12812b12baf1dc19543bb712e0f50f2d39680c0e28abdc2f90eb542d99b17a0
                 (SHA-256 of the frozen Claim text quoted below, UTF-8, LF, stripped)

FROZEN CLAIM (verbatim from `claim` in the node record):

  SE.denom — max_i ||Gamma o Delta_i|| = O(1) : THE OPEN PROBLEM (AND)

────────────────────────────────────────────────────────────────────────────────────────────────
WHAT `Claim` BELOW RENDERS.  The frozen Claim's `O(1)` is rendered QUANTITATIVELY (house rule:
explicit constants, never `O`/`Θ`):

  `max_i ‖Γ_n∘Δ_i‖ ≤ 2·envBound ρ_const n`   for every `n ≥ 27`,

where `envBound c n → 1 + M` (`SE.tendsto_envBound`), so the right side is the explicit
`2(1+M) + o(1)` of the paper's eq:Dfinal ⇒ eq:main chain.  `n ≥ 27` is the active taper window
(`K ≥ 3`, paper eq:taper-n).

────────────────────────────────────────────────────────────────────────────────────────────────
PREMISE DECLARATION (coordinator ruling R4, 2026-07-30; the current DAG premise rules).

Of the eight status-propagating children, `composition` below consumes as Claim parameters:

  * `taper.Claim`  — CHILD `SE.denom.taper` (its rendered fragment; conjunct 1 `|β_d| ≤ 1` is
                     used in the `X`-term of `block_le`);
  * `tame.Claim`   — via the UNFORMALIZED path `SE.denom.Phi` → `SE.denom.Phi.legal` →
                     `SE.denom.Phi.legal.tame` (neither intermediate node carries a
                     `formalization` block, so no module for them exists to import; the import
                     graph skips them, declared here and, entry by entry, in this node's
                     `formalization.lean.rel`).

The remaining five children enter as CITED fields of `SE.SEFrame.Cited` — cited, not reproved,
at tier 1 (each field names its node in `SE/Interface.lean`):

  * `decomp`      → `Cited.block_triangle` (the four-term split inside one defect) and, jointly
                    with `familysplit`, `Cited.mask_from_D` (steps 1–2 of the prose block: the
                    reduction to one query position and the factor 2; certification A.9–A.10,
                    A.32);
  * `X`           → `Cited.x_bound`   (node `SE.denom.X`, PROVED);
  * `Y`           → `Cited.y_bound`   (node `SE.denom.Y`, PROVED);
  * `familysplit` → `Cited.mask_from_D` (with `decomp`, above);
  * `crossk`      → `Cited.defect_orth` (`‖D‖ = max_d ‖D_d‖`; only the `≤` half is used).

  (The `Φ` channel's matched-defect half enters as `Cited.cDiag_bound` — node
  `SE.denom.Phi.ambient`, PROVED — and the defect-0 vanishing as `Cited.cDiag_zero`/`cLower_zero`;
  the OPEN half of `Φ` is exactly what `tame.Claim` carries.)

`assembly` gets NO composition theorem (coordinator ruling R6): the node carries
`composition: none  # DEPENDENCY-MODELLING DEBT` with an empty `children` list.  Its envelope
calculus is proved in the support module `SE/Support/Envelope.lean` (ruling R1), and the node
`SE.denom.assembly.envelope` carries no `formalization` block (its frozen Claim — the 32612-tuple numerical
hook-envelope check — has no tier-1 rendering; its shadow is `Cited.rho_ge_one`/`rho_le`).

Consequently §7.6 anti-drift check 4 does not hold literally for this node either; the deviation
is declared here, in `SE/Trust.lean` §D, and in the node's `lean.rel` field.

No `sorry`.  A green build says the AGGREGATION is machine-checked; with `Φ` OPEN the node stays
OPEN — the composition cannot manufacture the channel bounds (node file, "Status and scope").
-/
import SE.denom.taper
import SE.denom.Phi.legal.tame
import SE.Support.Cbrt
import SE.Support.Envelope
import SE.Support.Limits
import SE.Support.RhoEnvelope

namespace SE.denom

section
variable (F : SE.SEFrame)

/-- The node's Lean claim — the frozen `O(1)` rendered with its explicit constant:
**`max_i ‖Γ_n∘Δ_i‖ ≤ 2·envBound ρ_const n`** for `n ≥ 27`, where `envBound c n → 1+M`. -/
def Claim : Prop :=
  ∀ n : ℕ, 27 ≤ n → F.maskNorm n ≤ 2 * SE.envBound SE.rhoConst n

end

section
variable {F : SE.SEFrame}

/-! ## The taper window -/

/-- The arithmetic of the active window `n ≥ 27`, i.e. `K ≥ 3` (paper eq:taper-n: the fourth term
"is empty for `n<27`; its first active tuple is `(K,n,j)=(3,27,1)`"). -/
theorem K_window {n : ℕ} (hn : 27 ≤ n) :
    3 ≤ K n ∧ 4 * K n ≤ n ∧ (K n : ℝ) < (n : ℝ) ∧ (0 : ℝ) < (n : ℝ) - 2 * (K n : ℝ) + 1 := by
  have h3 : 3 ≤ K n := three_le_K hn
  have h9 : 9 * K n ≤ n := nine_mul_K_le hn
  have h4 : 4 * K n ≤ n := by omega
  have hKn : K n < n := by omega
  refine ⟨h3, h4, by exact_mod_cast hKn, ?_⟩
  have h4' : (4 : ℝ) * (K n : ℝ) ≤ (n : ℝ) := by exact_mod_cast h4
  have hK0 : (0 : ℝ) ≤ (K n : ℝ) := Nat.cast_nonneg _
  linarith

/-! ## Steps 3–5 of the node's composition block, per defect (paper eq:final-envelope) -/

/-- **The per-defect envelope**: for `d < K`,
`‖D_d‖ ≤ ρ_d·(1 + M + errEnv)`, which is eq:final-envelope after the three elementary maxima of
`SE/Support/Envelope.lean` are applied to its four summands.  The four terms consume, in order:
`taper.Claim` conjunct 1 + `Cited.x_bound`; `Cited.y_bound`; `Cited.cDiag_bound`; and
`tame.Claim` (the H1–H4-conditional lower block). -/
theorem block_le (hC : F.Cited) (htaper : taper.Claim) (htame : Phi.legal.tame.Claim F)
    {n d : ℕ} (hn : 27 ≤ n) (hd : d < K n) :
    F.blockNorm n d ≤ F.rho n d * (1 + Mconst + errEnv n (K n)) := by
  obtain ⟨hK3, hK4, hKlt, hKpos⟩ := K_window hn
  have hrho0 : (0 : ℝ) ≤ F.rho n d := le_trans zero_le_one (hC.rho_ge_one n d hd)
  have hcube : ((K n : ℝ)) ^ (3 : ℕ) ≤ (n : ℝ) := K_cube_le_real n
  -- term 1: the taper coefficient against the `X` channel
  have t1 : |beta (K n) d| * F.xNorm n d ≤ F.rho n d * 1 := by
    have hx := hC.x_bound n d hd
    have hx0 := hC.xNorm_nonneg n d
    have hb := htaper.1 (K n) d
    nlinarith [abs_nonneg (beta (K n) d)]
  -- term 2: the `Y` channel
  have t2 : alpha (K n) d * F.yNorm n d ≤ F.rho n d * (Real.sqrt 2 * (2 * Real.sqrt 3 / 9)) := by
    have hy := hC.y_bound n d hd
    have ha := alpha_nonneg (K n) d
    have hkey := alpha_mul_sqrt_div_le (n := n) (Kv := K n) (d := d) hcube hd
    have h2 : (0 : ℝ) ≤ Real.sqrt 2 := Real.sqrt_nonneg 2
    calc alpha (K n) d * F.yNorm n d
        ≤ alpha (K n) d * (F.rho n d * (Real.sqrt 2 * Real.sqrt ((d : ℝ) / (n : ℝ)))) :=
          mul_le_mul_of_nonneg_left hy ha
      _ = F.rho n d * (Real.sqrt 2 * (alpha (K n) d * Real.sqrt ((d : ℝ) / (n : ℝ)))) := by ring
      _ ≤ F.rho n d * (Real.sqrt 2 * (2 * Real.sqrt 3 / 9)) := by
          apply mul_le_mul_of_nonneg_left _ hrho0
          exact mul_le_mul_of_nonneg_left hkey h2
  -- term 3: the diagonal `Φ` channel
  have t3 : alpha (K n) d * F.cDiag n d ≤ F.rho n d * errDiag n (K n) := by
    have hc := hC.cDiag_bound n d hd
    have ha := alpha_nonneg (K n) d
    have hkey := diag_term_le (n := n) (Kv := K n) (d := d) hd hKpos
    calc alpha (K n) d * F.cDiag n d
        ≤ alpha (K n) d * (F.rho n d * (Real.sqrt 6 / Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1))) :=
          mul_le_mul_of_nonneg_left hc ha
      _ = F.rho n d * (Real.sqrt 6 * alpha (K n) d / Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1)) := by
          ring
      _ ≤ F.rho n d * errDiag n (K n) := mul_le_mul_of_nonneg_left hkey hrho0
  -- term 4: the correlated lower block — this is where H1–H4 enter, through `tame.Claim`.
  -- `tame.Claim` is scoped to the paper's active window `1 ≤ d < K−1` (§7.10 review F1);
  -- outside it the term vanishes on its own: at `d = 0` by `Cited.cLower_zero`, and at the
  -- endpoint `d ≥ K−1` because the taper coefficient `α_{d+1} = (K−(d+1))₊ = 0`.
  have t4 : alpha (K n) (d + 1) * F.cLower n d
      ≤ F.rho n d * (Real.sqrt (15 / 8) * ((2 * Real.sqrt 3 / 9) * distort n (K n))) := by
    have hdist : (0 : ℝ) ≤ distort n (K n) := distort_nonneg n (K n)
    have h158 : (0 : ℝ) ≤ Real.sqrt (15 / 8) := Real.sqrt_nonneg _
    have h3s : (0 : ℝ) ≤ Real.sqrt 3 := Real.sqrt_nonneg 3
    rcases Nat.eq_zero_or_pos d with rfl | hd1
    · rw [hC.cLower_zero n, mul_zero]
      positivity
    · by_cases hdK1 : d < K n - 1
      · -- the active window `1 ≤ d < K−1`: consume `tame.Claim`
        have h9 : 9 * K n ≤ n := nine_mul_K_le hn
        have h3d : 3 * d ≤ n := by omega
        have hlow := htame n d hd1 h3d hdK1
        have ha := alpha_nonneg (K n) (d + 1)
        have hkey := alpha_succ_mul_sqrt_lower_le (n := n) (Kv := K n) (d := d) hcube hd hKlt
        calc alpha (K n) (d + 1) * F.cLower n d
            ≤ alpha (K n) (d + 1)
                * (Real.sqrt (15 / 8) * F.rho n d
                    * Real.sqrt ((d : ℝ) / ((n : ℝ) - (d : ℝ)))) :=
              mul_le_mul_of_nonneg_left hlow ha
          _ = F.rho n d * (Real.sqrt (15 / 8)
                * (alpha (K n) (d + 1) * Real.sqrt ((d : ℝ) / ((n : ℝ) - (d : ℝ))))) := by ring
          _ ≤ F.rho n d * (Real.sqrt (15 / 8) * ((2 * Real.sqrt 3 / 9) * distort n (K n))) := by
              apply mul_le_mul_of_nonneg_left _ hrho0
              exact mul_le_mul_of_nonneg_left hkey h158
      · -- the endpoint `d ≥ K−1`: `α_{d+1} = 0`, the term is zero
        have hK1 : K n ≤ d + 1 := by omega
        rw [alpha_of_le hK1, zero_mul]
        positivity
  -- assemble
  have hsplit : F.rho n d * 1 + F.rho n d * (Real.sqrt 2 * (2 * Real.sqrt 3 / 9))
      + F.rho n d * errDiag n (K n)
      + F.rho n d * (Real.sqrt (15 / 8) * ((2 * Real.sqrt 3 / 9) * distort n (K n)))
      = F.rho n d * (1 + Mconst + errEnv n (K n)) := by
    unfold errEnv
    rw [Mconst_split]
    ring
  calc F.blockNorm n d
      ≤ |beta (K n) d| * F.xNorm n d + alpha (K n) d * F.yNorm n d
        + alpha (K n) d * F.cDiag n d + alpha (K n) (d + 1) * F.cLower n d :=
        hC.block_triangle n d
    _ ≤ F.rho n d * 1 + F.rho n d * (Real.sqrt 2 * (2 * Real.sqrt 3 / 9))
        + F.rho n d * errDiag n (K n)
        + F.rho n d * (Real.sqrt (15 / 8) * ((2 * Real.sqrt 3 / 9) * distort n (K n))) := by
        linarith [t1, t2, t3, t4]
    _ = F.rho n d * (1 + Mconst + errEnv n (K n)) := hsplit

/-- **`‖D‖ ≤ envBound`** — paper eq:Dfinal, `‖D‖ ≤ 1 + M + o(1)` with the `o(1)` explicit.
Step 4 of the node's composition block: cross-defect orthogonality (`Cited.defect_orth`, node
`crossk`) turns the per-defect bounds into a maximum. -/
theorem dNorm_le (hC : F.Cited) (htaper : taper.Claim) (htame : Phi.legal.tame.Claim F)
    {n : ℕ} (hn : 27 ≤ n) :
    F.dNorm n ≤ SE.envBound SE.rhoConst n := by
  refine hC.defect_orth n (by omega) _ ?_
  intro d hd
  refine le_trans (block_le hC htaper htame hn hd) ?_
  have hrle : F.rho n d ≤ 1 + SE.rhoConst / (n : ℝ) ^ ((1 : ℝ) / 3) := hC.rho_le n d hd
  have hM : 0 < Mconst := Mconst_pos
  have herr : 0 ≤ errEnv n (K n) := errEnv_nonneg' hn
  unfold envBound
  exact mul_le_mul_of_nonneg_right hrle (by linarith)

/-- **The node's composition theorem** (§7.4): Cited ∧ taper ∧ tame ⟹ `Claim`.

Steps 1–2 of the node's prose composition block (reduction to one query position; the factor 2)
are the cited field `Cited.mask_from_D` (nodes `decomp`+`familysplit`; certification A.9–A.10,
A.32); steps 3–5 are `block_le` and `dNorm_le` above.  See the header's PREMISE DECLARATION (R4)
for the full child ↔ premise map. -/
theorem composition (hC : F.Cited) (htaper : taper.Claim) (htame : Phi.legal.tame.Claim F) :
    Claim F := by
  intro n hn
  have h1 := hC.mask_from_D n
  have h2 := dNorm_le hC htaper htame hn
  linarith

end

end SE.denom
