/-
`SE/SelfTest.lean` — non-node module: decidable checks that the DEFINITIONS
reproduce independently known values, plus the non-vacuity witnesses.

Why this file exists.  The node `SE.formal.t1` records the residual risk that Lean does *not*
cover: **mis-formalized definitions**.  A green build proves nothing if `K` is the wrong function
or the taper is off by one.  Every check below is decided by the kernel (`decide` / `norm_num`)
against a value obtained OUTSIDE this development.

`native_decide` is deliberately not used anywhere (the formalization audit checklist item 2).
-/
import SE.goal

namespace SE

namespace SelfTest

/-! ## 1. `K n = ⌊n^{1/3}⌋` at the boundaries

Checked through `SE.K_unique`, i.e. against the characterization `k³ ≤ n < (k+1)³` — and
`SE.K_eq_floor_rpow` separately proves that this characterization *is* `⌊n^{1/3}⌋₊`. -/

example : K 0 = 0 := K_unique (by norm_num) (by norm_num)
example : K 1 = 1 := K_unique (by norm_num) (by norm_num)
example : K 2 = 1 := K_unique (by norm_num) (by norm_num)
example : K 3 = 1 := K_unique (by norm_num) (by norm_num)
example : K 7 = 1 := K_unique (by norm_num) (by norm_num)
example : K 8 = 2 := K_unique (by norm_num) (by norm_num)
example : K 26 = 2 := K_unique (by norm_num) (by norm_num)
example : K 27 = 3 := K_unique (by norm_num) (by norm_num)
example : K 63 = 3 := K_unique (by norm_num) (by norm_num)
example : K 64 = 4 := K_unique (by norm_num) (by norm_num)
example : K 999 = 9 := K_unique (by norm_num) (by norm_num)
example : K 1000 = 10 := K_unique (by norm_num) (by norm_num)

/-! ## 2. The exact discrete taper maximum

`max_{0≤d<K} d(K-d-1) = ⌊(K-1)²/4⌋`.  The left-hand sides below are evaluated by the kernel
(`decide`), independently of `SE.taper_max`; the right-hand sides are `⌊(K-1)²/4⌋`. -/

example : (Finset.range 1).sup (fun d => d * (1 - d - 1)) = 0 := by decide
example : (Finset.range 2).sup (fun d => d * (2 - d - 1)) = 0 := by decide
example : (Finset.range 3).sup (fun d => d * (3 - d - 1)) = 1 := by decide
example : (Finset.range 4).sup (fun d => d * (4 - d - 1)) = 2 := by decide
example : (Finset.range 5).sup (fun d => d * (5 - d - 1)) = 4 := by decide
example : (Finset.range 6).sup (fun d => d * (6 - d - 1)) = 6 := by decide
example : (Finset.range 7).sup (fun d => d * (7 - d - 1)) = 9 := by decide
example : (Finset.range 10).sup (fun d => d * (10 - d - 1)) = 20 := by decide

-- and the proved formula agrees with each of those, for the same `K`
example : (Finset.range 7).sup (fun d => d * (7 - d - 1)) = (7 - 1) ^ 2 / 4 := taper_max 7
example : (Finset.range 10).sup (fun d => d * (10 - d - 1)) = (10 - 1) ^ 2 / 4 := taper_max 10

/-! ## 3. The taper coefficients -/

example : alpha 3 0 = 3 := by norm_num [alpha]
example : alpha 3 3 = 0 := by norm_num [alpha]
example : alpha 3 5 = 0 := by norm_num [alpha]
example : beta 3 0 = 1 := beta_eq_one (by norm_num)
example : beta 3 2 = 1 := beta_eq_one (by norm_num)
example : beta 3 3 = 0 := beta_eq_zero (by norm_num)

/-! ## 4. The closed constants

`SE.Cconst_digits` pins `9/(18+4√6+3√10)` to the 19 digits the manuscript prints,
`0.2413852814754581733…`, and `SE.Mconst_eq` / `SE.inv_two_one_add_Mconst` are the two closed
forms.  Restated here as the definition self-test the node asks for. -/

example : Mconst = (4 * Real.sqrt 6 + 3 * Real.sqrt 10) / 18 := Mconst_eq
example : 1 / (2 * (1 + Mconst)) = Cconst := inv_two_one_add_Mconst
example : (2413852814754581732 : ℝ) / 10 ^ 19 < Cconst := Cconst_digits.1
example : Cconst < (2413852814754581734 : ℝ) / 10 ^ 19 := Cconst_digits.2

/-! ## 5. The `n = 1,2,3` frozen witness ratios

`se/reviews/se_cor16_certification_20260723.md` ("Independent-construction checks") enumerates the
legal inputs and masks by brute force and reports

  | n | ‖Γ_n‖ | max_i ‖Γ_n ∘ Δ_i‖ | ratio |
  | 1 |   1   |       1/2         |   2   |
  | 2 |   1   |       3/4         |  4/3  |
  | 3 |   1   |       5/6         |  6/5  |

**What tier 1 can and cannot check here.**  The ratio `2n/(2n-1)` is a property of the concrete
matrix `Γ_n`, which needs the representation-theoretic layer (tier 3) to define; tier 1 therefore
cannot *derive* it.  What tier 1 *can* check — and does, below — is the definitional fact that
makes the table meaningful: at `n = 1,2,3` the frozen floor gives `K = 1`, so the taper collapses
to the single `k = 0` atom (`α₀ = 1`, `α_k = 0` for `k ≥ 1`), which is exactly the hypothesis
under which the artifact computes the table.  The recorded ratios are then reproduced from
`(2n)/(2n-1)` as a decidable rational check. -/

/-- The mask-norm ratio recorded by the certification artifact in the collapsed regime `K = 1`,
where `Γ_n` is the normalized `k = 0` atom: `‖Γ_n‖ / max_i‖Γ_n ∘ Δ_i‖ = 1 / ((2n-1)/(2n))`. -/
def collapseRatio (n : ℕ) : ℚ := (2 * n : ℚ) / ((2 * n : ℚ) - 1)

example : collapseRatio 1 = 2 := by norm_num [collapseRatio]
example : collapseRatio 2 = 4 / 3 := by norm_num [collapseRatio]
example : collapseRatio 3 = 6 / 5 := by norm_num [collapseRatio]

-- the taper really does collapse at n = 1,2,3 (this part IS derived here)
example : K 1 = 1 ∧ K 2 = 1 ∧ K 3 = 1 :=
  ⟨K_unique (by norm_num) (by norm_num), K_unique (by norm_num) (by norm_num),
    K_unique (by norm_num) (by norm_num)⟩
example : alpha (K 3) 0 = 1 := by rw [K_unique (by norm_num : (1:ℕ) ^ 3 ≤ 3) (by norm_num)]; norm_num [alpha]
example : alpha (K 3) 1 = 0 := by rw [K_unique (by norm_num : (1:ℕ) ^ 3 ≤ 3) (by norm_num)]; norm_num [alpha]

/-! ## 6. Non-vacuity witnesses (the formalization audit checklist, item 5)

A conditional theorem whose hypotheses are contradictory is worthless.  The three frames below
SATISFY `Cited` together with the four hypothesis node Claims (H1–H4), so the conditional chain
`tame.composition → denom.composition → br.composition → goal.composition_via_br` is not
vacuously true: `emptySectorFrame` (no admissible sector), `liveSectorFrame` (admissible sectors
with the physical `ω`, H1 with equality), and `channelFrame` (added per §7.10 review finding F3:
every channel norm the theorem bounds is STRICTLY POSITIVE wherever the cited facts allow).

They are *models*, not the real Set Equality data: they show consistency, nothing more. -/

/-- A sector level is non-degenerate when it has at least one admissible sector.  The H4 shadow
(`sect.Claim`) is deliberately stated so that a level with NO admissible sector forces
`cLower n j ≤ B` for every `B ≥ 0` — the (correct) statement that an empty direct sum has norm
`0` — so the assembly never needs this predicate; it is used only to state the stronger
non-vacuity witness below. -/
def HasAdmissibleSector (F : SEFrame) (n j : ℕ) : Prop :=
  ∃ s : F.Sector n j, F.admissible n j s

/-! ### The model shape

TIER 2b rework (2026-08-17, node `SE.formal.t2` frontier task-004).  The interface now carries the
sector's shape `θ` as carrier data (`SEFrame.shapeLen`/`shapeCol`) and evaluates BOTH sector
scalars by the hook-length formula (`Cited.sector_hook`), so a model can no longer pick `r_top` and
`ω` freely: at level `j` it must supply a genuine shape of `j` and the hook values that shape
forces.  Every model below therefore takes the SINGLE-ROW shape `θ = (j)` (`SE.rowShape`, whose
conjugate is `θ'_c = 1` for `c ≤ j`), which is also the maximizer of the hook product
(`SE.isGreatest_rtopHookSet`), so the same choice discharges `Cited.rho_isGreatest`.

  `ρ_d = r_top(2n,d,(d))`   (`modelRho`, the genuine MAXIMUM over shapes of `d`)
  `r_top = r_top(2n,j,(j))` (`modelRtop`; `modelRtop n j = modelRho n j` by definition)
  `ω = ω(2n,j,(j))`         (`modelOmega`, the hook ratio of `SE/Support/Omega.lean`)

Tier 1 could take `ρ ≡ 1` and `ω = j/(2(n-j))` exactly; neither is a hook value, so both are gone.
The downstream H1/H2/H3 data (`mxiS`, `gcanS`, `cnprobS`, `csectS`) is rebuilt on top of the hook
values, and H1/H2/H3 still hold WITH EQUALITY. -/

/-- `ρ_d` in the models: the maximizing hook value `SE.rhoHook n d = r_top(2n,d,(d))`. -/
noncomputable def modelRho (n d : ℕ) : ℝ := rhoHook n d

/-- `r_top` of the models' sector at level `j`: the single-row hook value.  Definitionally equal to
`modelRho n j`, which is why `Cited.rtop_le_rho` holds in the models with equality. -/
noncomputable def modelRtop (n j : ℕ) : ℝ := rtopHook (2 * n) j j (rowShape j)

/-- `ω` of the models' sector at level `j`: the hook ratio of the single-row shape. -/
noncomputable def modelOmega (n j : ℕ) : ℝ := omegaHook (2 * n) j (rowShape j)

theorem one_le_modelRho {n d : ℕ} (hd : d < n) : 1 ≤ modelRho n d :=
  one_le_rtopHook (by omega) (le_refl d)

theorem modelRho_nonneg {n d : ℕ} (hd : d < n) : 0 ≤ modelRho n d :=
  le_trans zero_le_one (one_le_modelRho hd)

theorem modelRtop_pos {n j : ℕ} (hj : j < n) : 0 < modelRtop n j :=
  rtopHook_pos (by omega) (le_refl j)

theorem modelOmega_pos {n j : ℕ} (hj1 : 1 ≤ j) (hj3 : 3 * j ≤ n) : 0 < modelOmega n j :=
  omegaHook_pos hj1 (by omega) (rowShape_isColumnData j)

/-- The taper window sits inside `d < n`. -/
theorem lt_of_lt_K {n d : ℕ} (hd : d < K n) : d < n := lt_of_lt_of_le hd (K_le_self n)

/-- The tier-2b field `Cited.rho_isGreatest` in the models: `ρ` IS the maximum hook value, by
construction (`SE.isGreatest_rtopHookSet`). -/
theorem modelRho_isGreatest {n d : ℕ} (hd : d < n) :
    IsGreatest (rtopHookSet n d) (modelRho n d) := isGreatest_rtopHookSet hd

/-- The tier-2b field `Cited.sector_hook` in the models: the sector's shape is the single row and
both scalars are its hook values, by construction. -/
theorem model_sector_hook (n j : ℕ) :
    IsColumnData j (rowShape j) j ∧ modelRtop n j = rtopHook (2 * n) j j (rowShape j)
      ∧ modelOmega n j = omegaHook (2 * n) j (rowShape j) :=
  ⟨rowShape_isColumnData j, rfl, rfl⟩

/-- A model with no admissible sector.  Establishes plain consistency of the hypotheses. -/
noncomputable def emptySectorFrame : SEFrame where
  Sector := fun _ _ => PUnit
  admissible := fun _ _ _ => False
  rtopS := fun n j _ => modelRtop n j
  omegaS := fun n j _ => modelOmega n j
  btheS := fun _ _ _ => 1
  mxiS := fun n j _ => 15 / 4 * modelOmega n j
  gcanS := fun n j _ => 15 / 4 * modelRtop n j
  cnprobS := fun n j _ => modelRtop n j * modelOmega n j
  csectS := fun _ _ _ => 0
  rho := modelRho
  adv := fun n => (K n : ℝ)
  gammaNorm := fun n => (K n : ℝ)
  maskNorm := fun _ => 1
  dNorm := fun _ => 1
  blockNorm := fun n d => |beta (K n) d|
  xNorm := fun _ _ => 1
  yNorm := fun _ _ => 0
  cDiag := fun _ _ => 0
  cLower := fun _ _ => 0
  shapeLen := fun _ j _ => j
  shapeCol := fun _ j _ => rowShape j

private lemma one_le_K {n : ℕ} (h : 1 ≤ n) : 1 ≤ K n := le_K (by simpa using h)

theorem emptySectorFrame_cited : emptySectorFrame.Cited where
  adv_ge := by intro n _; simp [emptySectorFrame]
  numerator := by intro n; simp [emptySectorFrame]
  maskNorm_pos := by intro n _; norm_num [emptySectorFrame]
  mask_from_D := by intro n; norm_num [emptySectorFrame]
  defect_orth := by
    intro n hn B hB
    have h0 : (0 : ℕ) < K n := one_le_K hn
    have := hB 0 h0
    rw [show emptySectorFrame.blockNorm n 0 = |beta (K n) 0| from rfl,
      beta_eq_one h0] at this
    simpa [emptySectorFrame] using (by simpa using this : (1 : ℝ) ≤ B)
  block_triangle := by intro n d; simp [emptySectorFrame]
  x_bound := by
    intro n d hd
    show (1 : ℝ) ≤ modelRho n d
    exact one_le_modelRho (lt_of_lt_K hd)
  y_bound := by
    intro n d hd
    show (0 : ℝ) ≤ modelRho n d * (Real.sqrt 2 * Real.sqrt ((d : ℝ) / (n : ℝ)))
    exact mul_nonneg (modelRho_nonneg (lt_of_lt_K hd)) (by positivity)
  cDiag_bound := by
    intro n d hd
    show (0 : ℝ) ≤ modelRho n d * (Real.sqrt 6 / Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1))
    exact mul_nonneg (modelRho_nonneg (lt_of_lt_K hd)) (by positivity)
  cDiag_zero := by intro n; rfl
  cLower_zero := by intro n; rfl
  rho_isGreatest := by intro n d hd; exact modelRho_isGreatest hd
  admissible_window := by intro n j s h; exact h.elim
  sector_hook := by intro n j s h; exact h.elim
  bthe_pos := by intro n j s h; exact h.elim
  mxi_nonneg := by intro n j s h; exact h.elim
  csect_nonneg := by intro n j s h; exact h.elim
  xNorm_nonneg := by intro n d; norm_num [emptySectorFrame]
  yNorm_nonneg := by intro n d; norm_num [emptySectorFrame]
  cDiag_nonneg := by intro n d; norm_num [emptySectorFrame]
  cLower_nonneg := by intro n d; norm_num [emptySectorFrame]

/-- H1 holds vacuously in the empty model. -/
theorem emptySectorFrame_t6 : denom.Phi.legal.trace.t6.Claim emptySectorFrame := by
  intro n j s h; exact h.elim

/-- H2 holds vacuously in the empty model. -/
theorem emptySectorFrame_gram : denom.Phi.legal.gram.interface.Claim emptySectorFrame := by
  intro n j s h; exact h.elim

/-- H3 holds vacuously in the empty model. -/
theorem emptySectorFrame_omega : denom.Phi.legal.omega.interface.Claim emptySectorFrame :=
  ⟨fun _ _ _ h => h.elim, fun _ _ _ h => h.elim⟩

/-- H4 holds in the empty model: `cLower = 0`, the norm of the empty direct sum. -/
theorem emptySectorFrame_sect : denom.Phi.legal.sect.Claim emptySectorFrame := by
  intro n j B _ _ _ hB _
  simpa [emptySectorFrame] using hB

/-- **The conditional chain is not vacuously true**: its hypotheses have a model. -/
theorem hypotheses_consistent :
    ∃ F : SEFrame, F.Cited ∧ denom.Phi.legal.trace.t6.Claim F
      ∧ denom.Phi.legal.gram.interface.Claim F
      ∧ denom.Phi.legal.omega.interface.Claim F
      ∧ denom.Phi.legal.sect.Claim F :=
  ⟨emptySectorFrame, emptySectorFrame_cited, emptySectorFrame_t6, emptySectorFrame_gram,
    emptySectorFrame_omega, emptySectorFrame_sect⟩

/-- A stronger model: admissible sectors exist at every `(n,j)` with `1 ≤ j` and `3j ≤ n`, and
H1/H2/H3 hold there with the physical shape (H1 and H2 with equality). -/
noncomputable def liveSectorFrame : SEFrame :=
  { emptySectorFrame with
    admissible := fun n j _ => 1 ≤ j ∧ 3 * j ≤ n }

private lemma live_window {n j : ℕ} (h : 1 ≤ j ∧ 3 * j ≤ n) : 1 ≤ j ∧ 3 * j ≤ n := h

private lemma live_omega_pos {n j : ℕ} (h : 1 ≤ j ∧ 3 * j ≤ n) : 0 < modelOmega n j :=
  modelOmega_pos h.1 h.2

private lemma live_rtop_pos {n j : ℕ} (h : 1 ≤ j ∧ 3 * j ≤ n) : 0 < modelRtop n j :=
  modelRtop_pos (by omega)

theorem liveSectorFrame_cited : liveSectorFrame.Cited where
  adv_ge := by intro n _; simp [liveSectorFrame, emptySectorFrame]
  numerator := by intro n; simp [liveSectorFrame, emptySectorFrame]
  maskNorm_pos := by intro n _; norm_num [liveSectorFrame, emptySectorFrame]
  mask_from_D := by intro n; norm_num [liveSectorFrame, emptySectorFrame]
  defect_orth := by
    intro n hn B hB
    have h0 : (0 : ℕ) < K n := one_le_K hn
    have := hB 0 h0
    rw [show liveSectorFrame.blockNorm n 0 = |beta (K n) 0| from rfl,
      beta_eq_one h0] at this
    simpa [liveSectorFrame, emptySectorFrame] using (by simpa using this : (1 : ℝ) ≤ B)
  block_triangle := by intro n d; simp [liveSectorFrame, emptySectorFrame]
  x_bound := by
    intro n d hd
    show (1 : ℝ) ≤ modelRho n d
    exact one_le_modelRho (lt_of_lt_K hd)
  y_bound := by
    intro n d hd
    show (0 : ℝ) ≤ modelRho n d * (Real.sqrt 2 * Real.sqrt ((d : ℝ) / (n : ℝ)))
    exact mul_nonneg (modelRho_nonneg (lt_of_lt_K hd)) (by positivity)
  cDiag_bound := by
    intro n d hd
    show (0 : ℝ) ≤ modelRho n d * (Real.sqrt 6 / Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1))
    exact mul_nonneg (modelRho_nonneg (lt_of_lt_K hd)) (by positivity)
  cDiag_zero := by intro n; rfl
  cLower_zero := by intro n; rfl
  rho_isGreatest := by intro n d hd; exact modelRho_isGreatest hd
  admissible_window := by intro n j s h; exact h
  sector_hook := by intro n j s _; exact model_sector_hook n j
  bthe_pos := by intro n j s _; show (0 : ℝ) < 1; norm_num
  mxi_nonneg := by
    intro n j s h
    show (0 : ℝ) ≤ 15 / 4 * modelOmega n j
    have := live_omega_pos h
    linarith
  csect_nonneg := by intro n j s _; show (0 : ℝ) ≤ 0; exact le_rfl
  xNorm_nonneg := by intro n d; norm_num [liveSectorFrame, emptySectorFrame]
  yNorm_nonneg := by intro n d; norm_num [liveSectorFrame, emptySectorFrame]
  cDiag_nonneg := by intro n d; norm_num [liveSectorFrame, emptySectorFrame]
  cLower_nonneg := by intro n d; norm_num [liveSectorFrame, emptySectorFrame]

/-- H1 in the live model, with the physical shape (equality at `B_θ = 1`). -/
theorem liveSectorFrame_t6 : denom.Phi.legal.trace.t6.Claim liveSectorFrame := by
  intro n j s h
  show 15 / 4 * modelOmega n j ≤ 15 / 4 * (1 : ℝ) ^ 2 * modelOmega n j
  ring_nf
  exact le_refl _

/-- H2 in the live model, with equality: `‖G_can‖ = (15/4)·r_top` and
`r_top/(B²ω)·‖M_ξ‖ = r_top/ω·(15/4)ω`. -/
theorem liveSectorFrame_gram : denom.Phi.legal.gram.interface.Claim liveSectorFrame := by
  intro n j s h
  have hw := live_omega_pos h
  show 15 / 4 * modelRtop n j
      = modelRtop n j / ((1 : ℝ) ^ 2 * modelOmega n j) * (15 / 4 * modelOmega n j)
  field_simp

/-- H3 in the live model: the sandwich holds because the compression vanishes, the polar with
equality by construction. -/
theorem liveSectorFrame_omega : denom.Phi.legal.omega.interface.Claim liveSectorFrame := by
  constructor
  · intro n j s h
    have hw := live_omega_pos h
    have hr := live_rtop_pos h
    show (0 : ℝ) ^ 2 ≤ modelRtop n j * modelOmega n j * (15 / 4 * modelRtop n j)
    have : (0 : ℝ) ≤ modelRtop n j * modelOmega n j * (15 / 4 * modelRtop n j) := by positivity
    simpa using this
  · intro n j s _
    rfl

/-- H4 in the live model (`cLower = 0` is inherited from the empty model). -/
theorem liveSectorFrame_sect : denom.Phi.legal.sect.Claim liveSectorFrame := by
  intro n j B _ _ _ hB _
  simpa [liveSectorFrame, emptySectorFrame] using hB

/-- The stronger non-vacuity statement: a model with admissible sectors present. -/
theorem hypotheses_consistent_live :
    ∃ F : SEFrame, F.Cited ∧ denom.Phi.legal.trace.t6.Claim F
      ∧ denom.Phi.legal.gram.interface.Claim F
      ∧ denom.Phi.legal.omega.interface.Claim F
      ∧ denom.Phi.legal.sect.Claim F
      ∧ ∀ n j, 1 ≤ j → 3 * j ≤ n → HasAdmissibleSector F n j :=
  ⟨liveSectorFrame, liveSectorFrame_cited, liveSectorFrame_t6, liveSectorFrame_gram,
    liveSectorFrame_omega, liveSectorFrame_sect,
    fun _ _ h1 h2 => ⟨PUnit.unit, ⟨h1, h2⟩⟩⟩

/-! ## 6b. The channel-nonzero model (§7.10 review finding F3; TIER 2b rework)

`emptySectorFrame` and `liveSectorFrame` are degenerate in exactly the four channel norms the
theorem is about (`cLower = csectS = yNorm = cDiag = 0`), so they witness consistency of the
hypothesis bundle but not consistency with nonzero channels.  `channelFrame` closes that gap:
`x` and the `Φ`-diagonal sit exactly ON their cited bounds at the model's own `ρ`
(`x = 1 ≤ ρ`, `y = √2·√(d/n)`, `Φ-diag = √6/√(n−2d+1)`), the sector compression is the LARGEST
value H3 allows, `‖C̃‖ = √(‖C_{N,prob}‖·‖G_can‖) = √((15/4)·r_top²·ω)` (so H3(i) holds with
EQUALITY), the lower block EQUALS that compression (so H4 holds by identity, not by both sides
vanishing), and the only vanishing values are the ones the CITED facts force to vanish
(`lem:phi-diag`: the defect-0 entries, `Cited.cDiag_zero`/`cLower_zero`).  A trivial all-zero frame
would NOT satisfy `channelFrame_channels_pos` below.

TIER 2b: `csectS` is no longer the tier-2a constant `√(15/8)·√(j/(n−j))`, which was tied to the
now-impossible `ω = j/(2(n−j))` exactly; it is rebuilt on the hook value of `ω`, and it is still
strictly positive on the whole admissible window. -/

/-- The channel model's sector compression: the value that makes H3(i) an EQUALITY,
`‖C̃_{λ,ξ}‖ = √(‖C_{N,prob}‖·‖𝖦_can‖) = √((15/4)·r_top²·ω)`. -/
noncomputable def modelCsect (n j : ℕ) : ℝ :=
  Real.sqrt (15 / 4 * (modelRtop n j) ^ 2 * modelOmega n j)

theorem modelCsect_nonneg (n j : ℕ) : 0 ≤ modelCsect n j := Real.sqrt_nonneg _

theorem modelCsect_pos {n j : ℕ} (hj1 : 1 ≤ j) (hj3 : 3 * j ≤ n) : 0 < modelCsect n j := by
  have hw := modelOmega_pos hj1 hj3
  have hr := modelRtop_pos (by omega : j < n)
  exact Real.sqrt_pos.mpr (by positivity)

theorem modelCsect_sq {n j : ℕ} (hj1 : 1 ≤ j) (hj3 : 3 * j ≤ n) :
    (modelCsect n j) ^ 2 = 15 / 4 * (modelRtop n j) ^ 2 * modelOmega n j := by
  have hw := modelOmega_pos hj1 hj3
  have hr := modelRtop_pos (by omega : j < n)
  exact Real.sq_sqrt (by positivity)

/-- The channel-nonzero model (review F3, tier-2b rework).  Built from scratch (not by
structure-update) so every projection reduces in one step. -/
noncomputable def channelFrame : SEFrame where
  Sector := fun _ _ => PUnit
  admissible := fun n j _ => 1 ≤ j ∧ 3 * j ≤ n
  rtopS := fun n j _ => modelRtop n j
  omegaS := fun n j _ => modelOmega n j
  btheS := fun _ _ _ => 1
  mxiS := fun n j _ => 15 / 4 * modelOmega n j
  gcanS := fun n j _ => 15 / 4 * modelRtop n j
  cnprobS := fun n j _ => modelRtop n j * modelOmega n j
  csectS := fun n j _ => modelCsect n j
  rho := modelRho
  adv := fun n => (K n : ℝ)
  gammaNorm := fun n => (K n : ℝ)
  maskNorm := fun _ => 1
  dNorm := fun _ => 1
  blockNorm := fun n d => |beta (K n) d|
  xNorm := fun _ _ => 1
  yNorm := fun n d => Real.sqrt 2 * Real.sqrt ((d : ℝ) / (n : ℝ))
  cDiag := fun n d =>
    if d = 0 then 0 else Real.sqrt 6 / Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1)
  cLower := fun n j => if j = 0 then 0 else modelCsect n j
  shapeLen := fun _ j _ => j
  shapeCol := fun _ j _ => rowShape j

theorem channelFrame_yNorm_nonneg (n d : ℕ) : 0 ≤ channelFrame.yNorm n d := by
  show (0 : ℝ) ≤ Real.sqrt 2 * Real.sqrt ((d : ℝ) / (n : ℝ))
  positivity

theorem channelFrame_cDiag_nonneg (n d : ℕ) : 0 ≤ channelFrame.cDiag n d := by
  show (0 : ℝ) ≤ if d = 0 then (0 : ℝ)
      else Real.sqrt 6 / Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1)
  split_ifs
  · exact le_rfl
  · positivity

theorem channelFrame_cLower_nonneg (n d : ℕ) : 0 ≤ channelFrame.cLower n d := by
  show (0 : ℝ) ≤ if d = 0 then (0 : ℝ) else modelCsect n d
  split_ifs
  · exact le_rfl
  · exact modelCsect_nonneg n d

theorem channelFrame_cited : channelFrame.Cited where
  adv_ge := by intro n _; simp [channelFrame]
  numerator := by intro n; simp [channelFrame]
  maskNorm_pos := by intro n _; norm_num [channelFrame]
  mask_from_D := by intro n; norm_num [channelFrame]
  defect_orth := by
    intro n hn B hB
    have h0 : (0 : ℕ) < K n := one_le_K hn
    have := hB 0 h0
    rw [show channelFrame.blockNorm n 0 = |beta (K n) 0| from rfl,
      beta_eq_one h0] at this
    simpa [channelFrame] using (by simpa using this : (1 : ℝ) ≤ B)
  block_triangle := by
    intro n d
    have hb : channelFrame.blockNorm n d = |beta (K n) d| := rfl
    have hx : channelFrame.xNorm n d = 1 := rfl
    have t1 := mul_nonneg (alpha_nonneg (K n) d) (channelFrame_yNorm_nonneg n d)
    have t2 := mul_nonneg (alpha_nonneg (K n) d) (channelFrame_cDiag_nonneg n d)
    have t3 := mul_nonneg (alpha_nonneg (K n) (d + 1)) (channelFrame_cLower_nonneg n d)
    rw [hb, hx, mul_one]
    linarith
  x_bound := by
    intro n d hd
    show (1 : ℝ) ≤ modelRho n d
    exact one_le_modelRho (lt_of_lt_K hd)
  y_bound := by
    intro n d hd
    show Real.sqrt 2 * Real.sqrt ((d : ℝ) / (n : ℝ))
        ≤ modelRho n d * (Real.sqrt 2 * Real.sqrt ((d : ℝ) / (n : ℝ)))
    exact le_mul_of_one_le_left (by positivity) (one_le_modelRho (lt_of_lt_K hd))
  cDiag_bound := by
    intro n d hd
    show (if d = 0 then (0 : ℝ) else Real.sqrt 6 / Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1))
        ≤ modelRho n d * (Real.sqrt 6 / Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1))
    have hpos : (0 : ℝ) ≤ Real.sqrt 6 / Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1) := by positivity
    have hmain : Real.sqrt 6 / Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1)
        ≤ modelRho n d * (Real.sqrt 6 / Real.sqrt ((n : ℝ) - 2 * (d : ℝ) + 1)) :=
      le_mul_of_one_le_left hpos (one_le_modelRho (lt_of_lt_K hd))
    split_ifs
    · exact le_trans hpos hmain
    · exact hmain
  cDiag_zero := by intro n; simp [channelFrame]
  cLower_zero := by intro n; simp [channelFrame]
  rho_isGreatest := by intro n d hd; exact modelRho_isGreatest hd
  admissible_window := by intro n j s h; exact h
  sector_hook := by intro n j s _; exact model_sector_hook n j
  bthe_pos := by intro n j s _; show (0 : ℝ) < 1; norm_num
  mxi_nonneg := by
    intro n j s h
    show (0 : ℝ) ≤ 15 / 4 * modelOmega n j
    have := modelOmega_pos h.1 h.2
    linarith
  csect_nonneg := by intro n j s _; exact modelCsect_nonneg n j
  xNorm_nonneg := by intro n d; show (0 : ℝ) ≤ 1; norm_num
  yNorm_nonneg := channelFrame_yNorm_nonneg
  cDiag_nonneg := channelFrame_cDiag_nonneg
  cLower_nonneg := channelFrame_cLower_nonneg

/-- H1 in the channel model (with equality, as in the live model). -/
theorem channelFrame_t6 : denom.Phi.legal.trace.t6.Claim channelFrame := by
  intro n j s _
  show 15 / 4 * modelOmega n j ≤ 15 / 4 * (1 : ℝ) ^ 2 * modelOmega n j
  ring_nf
  exact le_refl _

/-- H2 in the channel model, with equality. -/
theorem channelFrame_gram : denom.Phi.legal.gram.interface.Claim channelFrame := by
  intro n j s h
  have hw := modelOmega_pos h.1 h.2
  show 15 / 4 * modelRtop n j
      = modelRtop n j / ((1 : ℝ) ^ 2 * modelOmega n j) * (15 / 4 * modelOmega n j)
  field_simp

/-- H3 in the channel model: the sandwich holds WITH EQUALITY
(`‖C̃‖² = (15/4)·r_top²·ω = ‖C_{N,prob}‖·‖𝖦_can‖`), the polar by construction. -/
theorem channelFrame_omega : denom.Phi.legal.omega.interface.Claim channelFrame := by
  constructor
  · intro n j s h
    show (modelCsect n j) ^ 2 ≤ modelRtop n j * modelOmega n j * (15 / 4 * modelRtop n j)
    rw [modelCsect_sq h.1 h.2]
    apply le_of_eq
    ring
  · intro n j s _
    rfl

/-- H4 in the channel model, BY IDENTITY: on the active window the lower block equals the (only)
sector compression, so the sup-bound is inherited directly — not by both sides being zero. -/
theorem channelFrame_sect : denom.Phi.legal.sect.Claim channelFrame := by
  intro n j B hj1 hj3 _ _ hs
  have h := hs PUnit.unit ⟨hj1, hj3⟩
  have hj0 : j ≠ 0 := by omega
  show (if j = 0 then (0 : ℝ) else modelCsect n j) ≤ B
  rw [if_neg hj0]
  exact h

/-- The channel norms really are NONZERO (sample point `(n, d) = (100, 7)`, admissible since
`1 ≤ 7`, `21 ≤ 100`): a trivial all-zero frame would fail this.  The sector compression and the
lower block are positive because the hook value of `ω` is (`SE.omegaHook_pos`, i.e. the LOWER half
`j/q ≤ ω` of eq:omega-range proved at tier 2b) — at tier 2a they were positive by fiat. -/
theorem channelFrame_channels_pos :
    0 < channelFrame.xNorm 100 7 ∧ 0 < channelFrame.yNorm 100 7
      ∧ 0 < channelFrame.cDiag 100 7 ∧ 0 < channelFrame.cLower 100 7
      ∧ 0 < channelFrame.csectS 100 7 PUnit.unit := by
  have c7 : ((7 : ℕ) : ℝ) = 7 := by norm_num
  have c100 : ((100 : ℕ) : ℝ) = 100 := by norm_num
  have s2 : 0 < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  have s6 : 0 < Real.sqrt 6 := Real.sqrt_pos.mpr (by norm_num)
  have hcs : 0 < modelCsect 100 7 := modelCsect_pos (by norm_num) (by norm_num)
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · show (0 : ℝ) < 1
    norm_num
  · show (0 : ℝ) < Real.sqrt 2 * Real.sqrt (((7 : ℕ) : ℝ) / (((100 : ℕ)) : ℝ))
    rw [c7, c100]
    exact mul_pos s2 (Real.sqrt_pos.mpr (by norm_num))
  · show (0 : ℝ) < if (7 : ℕ) = 0 then (0 : ℝ)
        else Real.sqrt 6 / Real.sqrt ((((100 : ℕ)) : ℝ) - 2 * (((7 : ℕ)) : ℝ) + 1)
    rw [if_neg (by norm_num : (7 : ℕ) ≠ 0), c7, c100]
    exact div_pos s6 (Real.sqrt_pos.mpr (by norm_num))
  · show (0 : ℝ) < if (7 : ℕ) = 0 then (0 : ℝ) else modelCsect 100 7
    rw [if_neg (by norm_num : (7 : ℕ) ≠ 0)]
    exact hcs
  · show (0 : ℝ) < modelCsect 100 7
    exact hcs

/-- Consistency witnessed with NONZERO channel norms (review F3): `Cited ∧ H1–H4` does not force
the bounded quantities to vanish. -/
theorem hypotheses_consistent_channels :
    ∃ F : SEFrame, F.Cited ∧ denom.Phi.legal.trace.t6.Claim F
      ∧ denom.Phi.legal.gram.interface.Claim F
      ∧ denom.Phi.legal.omega.interface.Claim F
      ∧ denom.Phi.legal.sect.Claim F
      ∧ 0 < F.yNorm 100 7 ∧ 0 < F.cDiag 100 7 ∧ 0 < F.cLower 100 7 :=
  ⟨channelFrame, channelFrame_cited, channelFrame_t6, channelFrame_gram, channelFrame_omega,
    channelFrame_sect, channelFrame_channels_pos.2.1, channelFrame_channels_pos.2.2.1,
    channelFrame_channels_pos.2.2.2.1⟩

/-! ## 7. End-to-end composition check

The full pipeline `tame → denom → br → goal` COMPOSES on the models: every composition theorem
accepts the previous one's output, so the four modules' Claim/composition signatures fit together
exactly as the DAG says they should — on the live model AND on the channel-nonzero model, where
the bounded quantities do not vanish.  (This checks the PLUMBING on models; it says nothing about
the real Set Equality data.) -/

theorem liveSectorFrame_goal : goal.Claim liveSectorFrame :=
  goal.composition_via_br liveSectorFrame_cited
    (br.composition liveSectorFrame_cited
      (denom.composition liveSectorFrame_cited denom.taper.holds
        (denom.Phi.legal.tame.composition liveSectorFrame_cited
          liveSectorFrame_t6 liveSectorFrame_gram liveSectorFrame_omega liveSectorFrame_sect)))

theorem channelFrame_goal : goal.Claim channelFrame :=
  goal.composition_via_br channelFrame_cited
    (br.composition channelFrame_cited
      (denom.composition channelFrame_cited denom.taper.holds
        (denom.Phi.legal.tame.composition channelFrame_cited
          channelFrame_t6 channelFrame_gram channelFrame_omega channelFrame_sect)))

end SelfTest

end SE
