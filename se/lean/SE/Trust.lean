/-
`SE/Trust.lean` — the machine-readable trust boundary of the node-linked formalization.

This file carries the trust list, the declared deviations, and `#print axioms` on every top-level
theorem.

════════════════════════════════════════════════════════════════════════════════════════════════
                                      TRUST LIST
════════════════════════════════════════════════════════════════════════════════════════════════

`sorry` count in this development: **0**.  `axiom` declarations added by this development: **0**.
`native_decide` uses: **0**.  Every assumption is an explicit HYPOTHESIS PARAMETER of the
composition theorem that consumes it (the current formalization trust-boundary rule), so it is visible in the theorem
statement and is counted by the elaborator rather than by a comment.

The trust boundary consists of the four hypothesis node Claims (A) and the cited interface (B).

TIER 2 (2026-08-17, node `SE.formal.t2`; baseline
`git:f0d686a:se/lean/SE/Interface.lean`).  `SE.SEFrame.Cited` went from **25**
fields to **23**: the three assumed analytic facts `rho_ge_one`, `rho_le`, `rhoConst_nonneg` are
now PROVED (`SE/Support/Hook.lean`, `SE/Support/RhoEnvelope.lean`), and one DEFINITIONAL field,
`rho_hook`, was added in their place (the hook-length evaluation of `ρ_d`, with no quantitative
content).  The abstract carrier field `SEFrame.rhoConst` was removed in favour of the explicit
`SE.rhoConst = 4`.  Independently, `SE.denom.taper`'s `Claim` grew from two of its three frozen
conjuncts to all three (ruling R2 discharged, §D1).

TIER 2b (2026-08-17, same node, frontier task-003/task-004).  `SE.SEFrame.Cited` went from **23**
fields to **21**: the four assumed sector facts `omega_le` (the manuscript's "reviewed-proved
range" eq:omega-range), `omega_pos`, `rtop_le_rho` and `rtop_pos` are now PROVED
(`SE/Support/Omega.lean`, `SE/Support/Hook.lean`, `SE/Support/RhoEnvelope.lean`); the tier-2a
field `rho_hook` was SHARPENED into `rho_isGreatest` (same single field, `IsGreatest` in place of
mere attainment — a STRONGER assumption, which the models satisfy because the maximizing shape is
explicit, `SE.rowShape`); and TWO definitional fields were added in place of the four:
`sector_hook` (the hook-length evaluation of the sector's own `r_top` and `ω`, plus the statement
that the sector's shape datum is a shape of `j`) and `admissible_window` (the manuscript's own
standing window `1 ≤ j`, `3j ≤ n` for admissible strict sectors).  `SEFrame` gained the two CARRIER
data `shapeLen`/`shapeCol` (the sector's shape `θ`; data, not assumptions), going 19 → 21.
COUNTING NOTE, declared; the conjunct arithmetic that stood here was WITHDRAWN on 2026-08-17 (fix 4
of `se/reviews/se_lean_t2b_review_20260817.md`, frontier task-008 of `SE.formal.t2`).  The count
reported here and on the node is the FIELD count: `SE.SEFrame.Cited` carries **21** assumption
fields (23 − 4 discharged + 2 added) and `SE.SEFrame` carries 21 carrier data.  The old note offered
"23 − 4 + 4 = 23 conjunct by conjunct" beside it; that number was not the conjunct count either,
because `sector_hook` is not the only bundling field — `rho_isGreatest` unfolds to two conjuncts
(`IsGreatest S a` = `a ∈ S ∧ a ∈ upperBounds S`) and `admissible_window` to two (`1 ≤ j ∧ 3j ≤ n`),
and a truthful conjunct ledger would have to unfold every surviving tier-1 field as well.  One
number is therefore reported, not two.

What is invariant under any counting convention, and is the fact that actually matters: **not one
conjunct added at tier 2b is QUANTITATIVE.**  Each is either a DEFINITIONAL identification
(`sector_hook`: the sector's shape datum is a shape of `j`, and its `r_top` and `ω` ARE the
Frame–Robinson–Thrall hook expressions), a maximality statement about those same hook expressions
(`rho_isGreatest`), or the manuscript's own standing admissibility window (`admissible_window`,
paper before eq:strict-sector).  None of them is an estimate, a numerical constant, or a bound the
reader is asked to take on trust; the estimates all moved the other way, out of `Cited` and into
proved theorems.

────────────────────────────────────────────────────────────────────────────────────────────────
A.  The four UNPROVED obligations of Conjecture H — one node module each
────────────────────────────────────────────────────────────────────────────────────────────────
  obligation  node id / module                         status on 2026-07-30
  ─────────   ──────────────────────────────────────   ────────────────────
  H1          `SE.denom.Phi.legal.trace.t6`            OPEN
  H2          `SE.denom.Phi.legal.gram.interface`      CONJECTURED
  H3          `SE.denom.Phi.legal.omega.interface`     CONJECTURED
  H4          `SE.denom.Phi.legal.sect`                OPEN

  Each module's `def Claim` is that node's tier-1 shadow; each docstring quotes the node's frozen
  Claim verbatim with its SHA-256 (the current composition-linking convention/§7.6) and states exactly what the shadow
  loses (H2's Schur lift and H4's exhaustiveness are INVISIBLE at tier 1 — a mis-typed H2 or a
  non-exhaustive H4 would not be caught here; that needs tier 3, not started).  All four are
  consumed as parameters of `SE.denom.Phi.legal.tame.composition` and reach every downstream
  composition through it.  Nothing in this development proves, or even evidences, any of them.

────────────────────────────────────────────────────────────────────────────────────────────────
B.  `SE.SEFrame.Cited` — results CITED, not reproved here (`SE/Interface.lean`)
────────────────────────────────────────────────────────────────────────────────────────────────
  B1. External literature
      `adv_ge`                 negative-weight adversary bound        HLS07, LMRSS11 (paper eq:adv)
      `mask_from_D`            filtered γ₂ + diamond device           paper eq:diamond-two,
                                                                     eq:mask-from-D
  B2. Reviewed analytic lemmas used by the Set Equality argument
      `numerator`              `lem:numerator`, `‖Γ_n‖ ≥ K`          node `SE.br.num`   PROVED
      `x_bound`, `y_bound`     `thm:xy` / eq:xybounds                nodes `SE.denom.X`,
                                                                     `SE.denom.Y`       PROVED
      `cDiag_bound`            eq:phi-matched + eq:phiambient        node
                                                                     `SE.denom.Phi.ambient` PROVED
      `cDiag_zero`,            `lem:phi-diag` ("for `k=1` only
      `cLower_zero`            defect 1 occurs, and `C_0 = 0`")
      `defect_orth`            eq:phi-regroup + eq:defect-D
                               + eq:orth-max                          node `SE.denom.crossk`
      `block_triangle`         eq:defect-D + triangle inequality      node `SE.denom.decomp`
      `rho_isGreatest`         eq:rtop + the Frame–Robinson–Thrall HOOK-LENGTH FORMULA and the
                               attainment of the maximum over the (finite, nonempty) partitions of
                               `d`.  DEFINITIONAL: it says `ρ_d` IS that maximum, evaluated as the
                               explicit product `SE.rtopHook`; nothing quantitative is assumed.  It
                               REPLACED the tier-1 analytic assumptions `rho_ge_one` / `rho_le` /
                               `rhoConst_nonneg` (tier 2a) and `rtop_le_rho` (tier 2b), which are
                               now the theorems `SEFrame.Cited.rho_ge_one`, `.rho_le`,
                               `.rtop_le_rho` and `SE.rhoConst_nonneg`.  The ENV node
                               `SE.denom.assembly.envelope` (whose own Claim has no rendering)
                               keeps this field as its tier-1 shadow
      `sector_hook`            eq:rtop + eq:parameters-can + the same HOOK-LENGTH FORMULA, applied
                               to `λ = (q-j,θ)` and `λ⁻ = (q-j-1,θ)`.  DEFINITIONAL and EQUATIONAL:
                               the sector's shape datum is a shape of `j`, its `r_top` IS
                               `SE.rtopHook (2n) j θ₁ θ'`, and its `ω` IS
                               `SE.omegaHook (2n) j θ'`.  It REPLACED the tier-1 assumptions
                               `omega_le`, `omega_pos`, `rtop_pos` (tier 2b), which are now the
                               theorems `SEFrame.Cited.omega_le`, `.omega_pos`, `.rtop_pos`
      `admissible_window`      paper, before/after eq:strict-sector: admissible strict sectors live
                               under the standing `j = k-1 ≥ 1` and require `n ≥ 3j`.  DEFINITIONAL
                               (a fact about the index set, no estimate).  It is what makes
                               `omega_pos` a theorem rather than an assumption: at `j = 0` the
                               manuscript's own `ω` is `0`
      `maskNorm_pos`           `se/reviews/se_cor16_certification_20260723.md`, the exact
                               `(2n-1)/(2n)` mask norm at `K = 1`   (part of `SE.br.def`)
  B3. Positivity/nonnegativity of the abstract carrier quantities
      `bthe_pos`, `mxi_nonneg`, `csect_nonneg`,
      `xNorm_nonneg`, `yNorm_nonneg`, `cDiag_nonneg`, `cLower_nonneg`
      — these are norms and ratios of dimensions; they carry no mathematical content beyond
      the objects being what the manuscript says they are.  (`omega_pos` and `rtop_pos` left this
      list at tier 2b: they are theorems now.)

────────────────────────────────────────────────────────────────────────────────────────────────
C.  What is PROVED here — no `sorry`
────────────────────────────────────────────────────────────────────────────────────────────────
  Support (non-node, §7.3):
  `SE/Support/Cbrt.lean`      `K³ ≤ n < (K+1)³`, uniqueness, `K = ⌊n^{1/3}⌋₊`, `n^{1/3}-1 ≤ K`
  `SE/Support/Constants.lean` `M = (4√6+3√10)/18`, `1/(2(1+M)) = 9/(18+4√6+3√10)`, 19 digits
  `SE/Support/Envelope.lean`  `(1-x)√x ≤ 2√3/9` and its three discrete instances (placed per
                              ruling R1 — see that file's header and §D below)
  `SE/Support/Limits.lean`    `errEnv ≤ 5·n^{-1/6}`, `envBound → 1 + M`
  TIER 2, added 2026-08-17 (node `SE.formal.t2`):
  `SE/Support/Hook.lean`      `r_top` DEFINED by the explicit hook product of eq:rtop; `1 ≤ r_top`;
                              the log envelope `log r_top ≤ d(d-1)/(2(q-d+1)) + d/(q-2d+1)` of
                              eq:rho-asymp; `E(2n,d) ≤ 1/K n` on the taper window;
                              `r_top ≤ 1 + 4·n^{-1/3}`; `e^x ≤ 1/(1-x) ≤ 1+2x`; the one-defect
                              completion identity `r_{j+1}(λ) = j·r_top(q,j,θ)` of `lem:phi-diag`
  `SE/Support/Telescope.lean` the two telescoping product identities over `ℝ` (`Finset.Ico` and
                              `Finset.range`, both orientations) that every hook product uses
  TIER 2b, added 2026-08-17 (node `SE.formal.t2`, frontier task-003/task-004):
  `SE/Support/Hook.lean`      (addition) the maximizing shape: `∏(1+θ'_c/(q-d-c+1))` is largest at
                              the single row `θ = (d)`, by the telescoping majorant
                              `1 + θ'_{i+1}/(A-i) ≤ (A-S_i+1)/(A-S_{i+1}+1)`; hence
                              `IsGreatest (rtopHookSet n d) (rhoHook n d)` for `d < n`
  `SE/Support/Omega.lean`     `p₀` DEFINED by its hook ratio, its reduction
                              `1/p₀ = q/(q-j-θ₁)·∏_{c≤θ₁}(1-1/h_c)` (one telescoping over
                              `Finset.Ico θ₁ (q-j-1)`), and the two-sided range of eq:omega-range
                              `j/q ≤ ω ≤ j/(q-2j)` on `1 ≤ j`, `6j ≤ q` — the two telescoping
                              majorants, with equality at `j = 1`, so neither majorant STEP is
                              lossy.  The ENDS of the range are not equally tight, and the module
                              header says so: the UPPER bound is attained (at `j = 1`,
                              `ω = 1/(q-2)` exactly), the LOWER bound `j/q ≤ ω` is attained in 0
                              cases in one exact-rational sweep (re-run and reproduced), corroborated by the
                              task-013 reviewer's independent branching-rule sweep — at `j = 1` already
                              `1/(q-2) > 1/q`.  Only the POSITIVITY of the lower half is
                              load-bearing (`Cited.omega_pos` via `.le_omega`)
  `SE/Support/RhoEnvelope.lean`  the discharged `SEFrame.Cited.rho_ge_one`, `.rho_le`,
                              `.rtop_le_rho`, `.rtop_pos`, `.omega_le`, `.omega_pos` (and
                              `.le_omega`, the lower half of eq:omega-range itself)
  `SE/Support/BranchFactors.lean`  `((|P|+2)/2)·2^{-max(0,|P|-4)/2} ≤ 3` with equality exactly at
                              `|P| = 4` (`lem:br-special-path`); the branch pair
                              `√(1/(x+1)+1/x) ≤ √2/√x` (eq:br-completion-explicit) and the
                              composition `√3·√2/√(n-2(k-ℓ)+1) ≤ √6/√(n-2k+1)`
                              (`lem:phi-ambient`)

  Node modules (each relative to the parameters listed in its own signature):
  `SE/denom/taper.lean`               `taper.holds : taper.Claim` (unconditional; ALL THREE frozen
                                       conjuncts since 2026-08-17 — §D1)
  `SE/denom/Phi/legal/tame.lean`      `tame.composition : Cited → H1 → H2 → H3 → H4 → tame.Claim`
  `SE/denom.lean`                     `denom.composition : Cited → taper.Claim → tame.Claim →
                                       denom.Claim`
  `SE/br.lean`                        `br.composition : Cited → denom.Claim → br.Claim`
  `SE/goal.lean`                      `goal.composition_via_br : Cited → br.Claim → goal.Claim`
                                      (= Theorem B, conditional)

  `SE/SelfTest.lean`          definition self-tests + THREE non-vacuity models (empty, live, and
                              the channel-nonzero `channelFrame` added per §7.10 review F3) + the
                              end-to-end plumbing checks `liveSectorFrame_goal` /
                              `channelFrame_goal`

────────────────────────────────────────────────────────────────────────────────────────────────
D.  DECLARED DEVIATIONS (coordinator rulings R1–R6, 2026-07-30; the current DAG premise rules)
────────────────────────────────────────────────────────────────────────────────────────────────
  D1 (R2 — `SE.denom.taper`).  **DISCHARGED 2026-08-17 (tier 2, node `SE.formal.t2`).**
      R2 declared conjunct 2, the TIGHT `|a_k| ≤ √(n/k)`, unrenderable because "its normalization
      constant is fixed by the operator layer".  In the paper's own normalization `a_k = α_k` the
      conjunct is the integer inequality `(K−k)²·k ≤ n`, which follows from `K³ ≤ n` by AM–GM
      (`SE.sq_alpha_mul_le`); no operator layer enters.  `taper.Claim` now renders all three
      conjuncts and `taper.holds` proves them unconditionally.  Residual scope, declared: the
      conjunct carries the binder `1 ≤ k`, because at `k = 0` the frozen right-hand side `√(n/0)`
      is not a real bound; the `k`-cleared equivalent `k·α_k² ≤ n` is proved for EVERY `k`
      (`SE.sq_alpha_mul_le'`), so no instance is lost.  No attainment is claimed by "TIGHT" — see
      that module's header.
  D2 (R3 — `SE.denom.Phi.legal.tame`).  The node's five children are gram/omega/trace/found/sect;
      `tame.composition` consumes the GRANDCHILDREN `t6` (via trace), `gram.interface`,
      `omega.interface` (the intermediate nodes carry no linked formalization), the child
      `sect`, and `Cited`.  The child `found` has NO tier-1 rendering (typed carriers are
      invisible without an operator layer); its rule-7b `c≥2` caveat rides along with the
      composition.
  D3 (R4 — `SE.denom`).  Of eight children, `taper` and (across the unmechanized path
      Phi → Phi.legal) `tame` enter as Claim parameters; `decomp`, `X`, `Y`, `familysplit`,
      `crossk` enter as the `Cited` fields listed in B2 (see the map in `SE/denom.lean`'s
      header).  `assembly` gets no composition theorem (R6): the node carries no formal mirror and
      is a declared DEPENDENCY-MODELLING DEBT with an empty premise list.
  D4 (R1 — `SE.denom.assembly.envelope`).  The ENV node's frozen Claim (the 32612-tuple
      numerical hook-envelope check) has NO tier-1 rendering; the node carries no `formalization`, and
      the analytic envelope calculus that previously sat in a node-shaped file lives in the support
      module `SE/Support/Envelope.lean`.  Since 2026-08-17 its shadow is the DEFINITIONAL field
      `Cited.rho_isGreatest` (`Cited.rho_hook` before the tier-2b sharpening), and the envelope
      itself (`1 ≤ ρ_d ≤ 1 + 4·n^{-1/3}` for `d < K n`) is
      PROVED in `SE/Support/Hook.lean`; the numerical check the node freezes (`ρ_{n,k} ≤ R_{n,k}`,
      in-spec max 16/15) is a SHARPER, shape-by-shape statement and is NOT what tier 2 proves.
  D5 (`SE.br`).  Children `num` and `def` enter as the `Cited` fields `numerator` and
      `maskNorm_pos` (both nodes PROVED on disk; no `Γ_n` exists at tier 1 to reprove them
      against).  Only `denom` is a Claim parameter.
  D6 (R5 — `SE.goal`).  Only `composition_via_br` exists.  The `ros` route is DISABLED by its
      REFUTED premise (§4: that disables the route, it does not refute the goal);
      `mdh`/`sdp`/`jz` have `proof: null` on the node (no prose route proof to mirror; for `jz`
      the multiplicative → `Adv±` transfer is unproved, so a rendered theorem would resolve a
      VARIANT of the goal).  §7.6 check 5 therefore does not hold literally; NO stub theorem was
      fabricated for any of the four, and each is declared route-by-route on the node (§D8).
  D7 (§7.10 review F1, applied 2026-07-30).  `sect.Claim` (H4) and `tame.Claim` are quantified
      over the frozen Claim's ACTIVE window `1 ≤ j`, `3j ≤ n`, `j < K n − 1` (the resolution of
      the manuscript's "active `j`": Conjecture H's preamble + `lem:omega-lower` (ii)'s scope).
      An earlier revision quantified both over all `(n, j)`, i.e. assumed MORE than Conjecture H
      states; that over-quantification was review finding F1 and is corrected — outside the
      window, `denom.block_le` now closes the lower-block term by `Cited.cLower_zero` (`d = 0`)
      and by `α_{d+1} = 0` (`d ≥ K−1`), so nothing is assumed there.
  D8 (2026-08-17, frontier task-006 of `SE.formal.t2`).  D2/D3/D5/D6 above are PROSE.  As of today
      each of them is ALSO written in machine-readable form on its node, one entry per deviating
      premise / non-child import / unrendered route, in `formalization.lean.rel`:

        premise-not-imported: <child-node-id>   - <mechanism the premise arrives by>
        import-not-child:     <imported-module> - <why this non-child is imported>
        route-not-formalized: <route-id>        - <why no composition_via_* exists>

      `tools/lean_dag_check.py` checks 5 and 6 now read those entries: a DECLARED deviation is
      INFO, an UNDECLARED one is still FAIL, and a declaration that is blanket, duplicated, names a
      non-existent `Cited.<field>`, names a premise the module actually imports, names a route that
      actually has a `composition_via_*` theorem, or names a non-child import that is NOT a DAG
      descendant of the declaring node, is itself a FAIL.  Nothing was weakened: before today the
      six honest deviations D2/D3/D5/D6 were simply unclearable FAILs, which is an invitation to
      fabricate stub theorems.  What the checker still CANNOT do is decide whether an English
      mechanism description is TRUE — that stays a review obligation (the node-audit protocol).
────────────────────────────────────────────────────────────────────────────────────────────────
E.  Declared work in progress
────────────────────────────────────────────────────────────────────────────────────────────────
  None.  There is no `sorry` in this development, so this section is empty by construction.
  A future `sorry` MUST be listed here with an owner and a target date (the current formalization trust-boundary rule).
════════════════════════════════════════════════════════════════════════════════════════════════
-/
import SE.SelfTest
import SE.Support.BranchFactors

namespace SE

/-! ## Axiom census

Everything below must print exactly Lean's three standard axioms
(`propext`, `Classical.choice`, `Quot.sound`).  Anything else is a defect. -/

#print axioms SE.goal.composition_via_br
#print axioms SE.goal.adv_quantitative
#print axioms SE.br.composition
#print axioms SE.denom.composition
#print axioms SE.denom.dNorm_le
#print axioms SE.denom.block_le
#print axioms SE.denom.Phi.legal.tame.composition
#print axioms SE.denom.Phi.legal.tame.csect_le
#print axioms SE.denom.Phi.legal.tame.gcan_le
#print axioms SE.denom.taper.holds
#print axioms SE.K_eq_floor_rpow
#print axioms SE.K_unique
#print axioms SE.taper_max
#print axioms SE.alpha_le_sqrt
#print axioms SE.Mconst_eq
#print axioms SE.inv_two_one_add_Mconst
#print axioms SE.Cconst_digits
#print axioms SE.one_sub_mul_sqrt_le
#print axioms SE.errEnv_le
#print axioms SE.tendsto_envBound
#print axioms SE.SelfTest.emptySectorFrame_cited
#print axioms SE.SelfTest.emptySectorFrame_t6
#print axioms SE.SelfTest.emptySectorFrame_gram
#print axioms SE.SelfTest.emptySectorFrame_omega
#print axioms SE.SelfTest.emptySectorFrame_sect
#print axioms SE.SelfTest.hypotheses_consistent
#print axioms SE.SelfTest.liveSectorFrame_cited
#print axioms SE.SelfTest.liveSectorFrame_t6
#print axioms SE.SelfTest.liveSectorFrame_gram
#print axioms SE.SelfTest.liveSectorFrame_omega
#print axioms SE.SelfTest.liveSectorFrame_sect
#print axioms SE.SelfTest.hypotheses_consistent_live
#print axioms SE.SelfTest.channelFrame_cited
#print axioms SE.SelfTest.channelFrame_t6
#print axioms SE.SelfTest.channelFrame_gram
#print axioms SE.SelfTest.channelFrame_omega
#print axioms SE.SelfTest.channelFrame_sect
#print axioms SE.SelfTest.channelFrame_channels_pos
#print axioms SE.SelfTest.hypotheses_consistent_channels
#print axioms SE.SelfTest.liveSectorFrame_goal
#print axioms SE.SelfTest.channelFrame_goal

/-! ### Tier-2 census (added 2026-08-17, node `SE.formal.t2`)

Every top-level theorem added by tier 2, including the two DISCHARGED interface fields. -/

#print axioms SE.SEFrame.Cited.rho_ge_one
#print axioms SE.SEFrame.Cited.rho_le
#print axioms SE.rhoConst_nonneg
#print axioms SE.rise_den_pos
#print axioms SE.hook_den_pos
#print axioms SE.one_le_rise_factor
#print axioms SE.one_le_hook_factor
#print axioms SE.two_pow_pos
#print axioms SE.SelfTest.modelRho_nonneg
#print axioms SE.SelfTest.lt_of_lt_K
#print axioms SE.cast_descFactorial_eq_prod
#print axioms SE.rise_eq_prod
#print axioms SE.one_le_rtopHook
#print axioms SE.rtopHook_pos
#print axioms SE.sum_range_cast_id
#print axioms SE.log_rtopHook_le
#print axioms SE.exp_le_inv_one_sub
#print axioms SE.le_one_add_two_mul_of_log_le
#print axioms SE.hookExponent_nonneg
#print axioms SE.hookExponent_le_inv_K
#print axioms SE.rtopHook_le_envelope
#print axioms SE.rdSucc_eq_mul_rtop
#print axioms SE.rdSucc_eq_mul_rtopHook
#print axioms SE.IsColumnData.length_le
#print axioms SE.IsColumnData.head_le
#print axioms SE.IsColumnData.le_length_mul_head
#print axioms SE.IsColumnData.head_add_length_le
#print axioms SE.sq_alpha_mul_le
#print axioms SE.sq_alpha_mul_le'
#print axioms SE.alpha_le_sqrt_div
#print axioms SE.alpha_mul_sqrt_le_one
#print axioms SE.succ_le_three_mul_pow
#print axioms SE.succ_lt_three_mul_pow
#print axioms SE.specialPathFactor_le_three
#print axioms SE.specialPathFactor_eq_three_iff
#print axioms SE.specialPathFactorLen_two_mul
#print axioms SE.specialPathFactorLen_le_three
#print axioms SE.sqrt_specialPathFactor_le
#print axioms SE.branch_pair_le
#print axioms SE.phi_branch_combine
#print axioms SE.phi_ambient_combine
#print axioms SE.phi_ambient_full
#print axioms SE.SelfTest.one_le_modelRho

/-! ### Tier-2b census (added 2026-08-17, node `SE.formal.t2`, frontier task-003/task-004)

Every top-level theorem added by tier 2b, including the six DISCHARGED interface fields. -/

#print axioms SE.SEFrame.Cited.rtop_le_rho
#print axioms SE.SEFrame.Cited.rtop_pos
#print axioms SE.SEFrame.Cited.omega_le
#print axioms SE.SEFrame.Cited.omega_pos
#print axioms SE.SEFrame.Cited.le_omega
#print axioms SE.SEFrame.Cited.sector_window
#print axioms SE.prod_Ico_ratio
#print axioms SE.prod_Ico_ratio'
#print axioms SE.prod_range_ratio
#print axioms SE.prod_range_ratio'
#print axioms SE.rowShape_isColumnData
#print axioms SE.prod_rowShape
#print axioms SE.prod_le_prod_rowShape
#print axioms SE.rtopHook_le_rowShape
#print axioms SE.isGreatest_rtopHookSet
#print axioms SE.omega_lower_core
#print axioms SE.omega_upper_core
#print axioms SE.length_le_window
#print axioms SE.one_le_length
#print axioms SE.rowHook_pos
#print axioms SE.rowHook_sub_one_pos
#print axioms SE.rowHook_top
#print axioms SE.p0Hook_eq_prod
#print axioms SE.p0Hook_eq_inv
#print axioms SE.prod_ge_lower
#print axioms SE.prod_le_upper
#print axioms SE.omegaHook_eq
#print axioms SE.le_omegaHook
#print axioms SE.omegaHook_le
#print axioms SE.omegaHook_pos
#print axioms SE.SelfTest.modelRtop_pos
#print axioms SE.SelfTest.modelOmega_pos
#print axioms SE.SelfTest.modelRho_isGreatest
#print axioms SE.SelfTest.model_sector_hook
#print axioms SE.SelfTest.modelCsect_nonneg
#print axioms SE.SelfTest.modelCsect_pos
#print axioms SE.SelfTest.modelCsect_sq
#print axioms SE.SelfTest.channelFrame_yNorm_nonneg
#print axioms SE.SelfTest.channelFrame_cDiag_nonneg
#print axioms SE.SelfTest.channelFrame_cLower_nonneg

end SE
