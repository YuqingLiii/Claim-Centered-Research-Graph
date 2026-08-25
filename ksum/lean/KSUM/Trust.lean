/-
`KSUM/Trust.lean` — THE TRUST BOUNDARY OF THIS LAYER, machine-readable.

This module carries the trust list and the `#print axioms` manifest. An assumed obligation is an
explicit theorem parameter, variable, structure field, or named external interface, never a
hidden lemma closed with `sorry`.

**MANIFEST COVERAGE.** The manifest covers **every culminating result, not every declaration**.
Counts below are from a
comment-stripping parse of all **37** sources outside `.lake/`, build of 2026-08-01:

    `#print axioms` DIRECTIVES in the sources        283     (= 283 printed lines in the build
      · this module                                  117       transcript; was 237 after batch 1
      · tier T1, `KsumAudit/MainLine.lean`            29       and 193 at the 2026-07-31 baseline)
      · tier T3, `KsumAudit/Obstructions*.lean`       95
      · tier T3, `KsumAudit/FactorialFiltration.lean` 19
      · tier T3, `KsumAudit/JointLP.lean`              8
      · node modules `KSUM/{B1,B2,Support/Embed}`     15
    DISTINCT declaration names printed               268     (15 names printed twice — once in
      · of which `theorem`/`lemma`                   240       the owning module, once in this
      · of which `def` (the `Claim`s, `demoModel`,    28       manifest — so 283 lines, 268 names)
        `sandwichModel`, `genEmbed`, `demoEmbed`, …)
    `theorem` + `lemma` declarations in the sources   401     (294 `theorem` + 107 `lemma`)
    all named declarations (+ `def`/`instance`/…)     569     (plus 127 `example` witnesses)

**Read the coverage arithmetic in this direction and no other:** 240 of the 401 `theorem`/`lemma`
declarations carry a printed axiom line, so about **161 do not**.  283 > 401 is not the
comparison; 283 counts *lines*, 268 counts *names*, and only 240 of those names are theorems.
**Every unprinted declaration is a helper lemma that some printed result transitively depends
on** — `prod_ite_forall`, `axis_sum_eq`, `cyc_val`, `reynolds_apply`, `occ_split`,
`equivFunOnFinite_symm_add`, `sq_pow_comm`, the `erase*`/`wμ_row`/`occ_vals` rows, the `demo*`
lemmas, and so on — and `#print axioms` reports the axioms of the whole dependency closure, so an
axiom appearing anywhere below a printed result appears on that result's line.  A helper that no
printed result depends on could hide, but such a helper is by definition load-bearing for nothing.
(For comparison: the 2026-07-31 review's census gave 176/235 under a column-anchored parse that
skipped indented and attribute-prefixed declarations; its successor gave 268/401 but formed
"~133 unprinted" as 401 − 268, which mixes theorem/lemma with `def` and so still over-states
coverage.  The figures above separate the two kinds and are the conservative reading.)

════════════════════════════════════════════════════════════════════════════════════════════════
  (a)  PERMITTED AXIOM SET — and nothing else
════════════════════════════════════════════════════════════════════════════════════════════════

    propext          Classical.choice          Quot.sound

These are Lean's three standard axioms.  **Any other axiom appearing in the `#print axioms`
output below is a DEFECT, not a design choice**, and must be reported before anything in this
layer is cited.  This development declares no `axiom` of its own: every assumption is a structure
field or an explicit theorem parameter, so it is counted by the elaborator and visible in the
theorem's type rather than in a comment.

════════════════════════════════════════════════════════════════════════════════════════════════
  (b)  THE INTERFACE — every field, and what it cites
════════════════════════════════════════════════════════════════════════════════════════════════

`KSUM.QueryModel = KsumAudit.QueryModel` (see `KSUM/Interface.lean` for the full table):

    Q            bounded-error quantum query complexity            sec:prelim — DEFINITION given
    restrict     fact (i), domain restriction                      sec:prelim — CITED
    relabel      fact (ii), per-coordinate relabeling, factor 2     sec:prelim — CITED
    freeze       coordinate freezing = facts (i) + (iii)           sec:prelim — CITED
                 composed at the last position                      (STATED in the reviewed manuscript;
                                                                    explicitly recorded after external review,
                                                                    audit finding F1, discharged
                                                                    by manuscript repair M-1)
    constQ       a constant function has `Q = 0`                    sec:prelim fact (iv) — CITED
                                                                    (STATED in the reviewed manuscript;
                                                                    explicitly recorded after external review,
                                                                    audit finding F2, discharged
                                                                    by manuscript repair M-2)
    cABI         the absolute constant of the claw bounds           bookkeeping
    abi          `thm:abi` (Ambainis–Balodis–Iraids)                EXTERNAL, CITED, NOT PROVED
    tani         `thm:tani` (Tani)                                  EXTERNAL, CITED, NOT PROVED

Used by this layer: `tani`, `restrict` + `relabel` (via `QueryModel.relabel_inj`), `freeze` (via
`KSUM.Support.Q_frozen_le`), `cABI`/`cABI_pos`.  `abi` and `constQ` are not used here (they are
used by the tier-T1 modules).

`KSUM.Support.EmbedData` (`KSUM/Support/Embed.lean`) is the second interface: the DATA of
`lem:embed`.  Its fields `enc`, `enc_inj`, `k_dvd_P`, `two_mul_Mv`, `cP_pos`, `P_lower`,
`P_upper` are properties of the manuscript's explicit payload/tag formulas, each cited in its
docstring.
**Since gap-closure batch 2 (2026-08-01) the structure is no longer trust-only:**
`KSUM.Support.genEmbed` CONSTRUCTS an `EmbedData` from the manuscript's own parameter display for
every `k ≥ 3`, `n ≥ 1`, `R ≥ 2`, discharging `enc_inj`, `k_dvd_P`, `two_mul_Mv`, `cP_pos`,
`P_lower` and `P_upper` as theorems (`embed_enc_inj`, `embed_two_mul_M`, `embed_P_lower`,
`embed_P_upper`, …), with `c_P = k(k-1)2^{k-2}` depending only on `k`; `demoEmbed` is the earlier
single instance.  What is STILL NOT proved anywhere is the **encoding identity** of `prop:embed`
(`kSum_{Z_q,0,kn}(encoded) = Coll_{k,n→R}(g)`): that is `KSUM.A2a.Claim`/`KSUM.A2b.Claim`, and
both remain `def Claim : Prop` with no proving theorem in this development.

**A theorem proved against these interfaces is exactly as strong as what they cite, and not one
notch stronger.**  If ABI21 is wrong, `KSUM.A1.composition` is wrong and the kernel is silent.

════════════════════════════════════════════════════════════════════════════════════════════════
  (c)  DECLARED WORK IN PROGRESS — the `sorry` census
════════════════════════════════════════════════════════════════════════════════════════════════

    `sorry` occurrences in `KSUM/**`        : 0
    `sorry` occurrences in `KsumAudit/**`   : 0
    `axiom` declarations in either          : 0
    `native_decide` / `implemented_by`      : 0

Unmechanized obligations are carried as `Prop`s that are STATED and not proved — the leaf Claims
`KSUM.A2a.Claim`, `KSUM.A2b.Claim`, `KSUM.B4a.Claim` — and as the two out-of-list child claims
written out in place, `KSUM.B4.B4bClaim` and `KSUM.B2.DonorClaim`.  Each of those is a hypothesis
of the composition that consumes it, so it appears in that theorem's type.

**Updated 2026-07-30 by tier T2.**  TWO leaves became proved unconditionally — `KSUM.A1b.Claim`
(`KSUM.A1b.holds`, from tier T1's `lem:encode`) and `KSUM.A1a.Claim` (`KSUM.A1a.holds`, from
`KsumAudit.KFloor.core_reduction` = `prop:core-even` + `lem:core-odd`).  Neither takes a
`QueryModel` argument, so neither is even relative to the cited bounds.

**Updated again 2026-07-30 by the R-A1-1 / R-A1-3 / R-B4-1 repair batch.**

* `KSUM.A1a.Claim` was WIDENED to hold at **every window target** `s ∈ [t₀, t₀+k)` (it was
  existential in `t₀`) and is still proved unconditionally, from the generalized core reduction
  `KsumAudit.KFloor.core_reduction_at`.  The base-target statement survives as
  `KsumAudit.KFloor.core_reduction` / `KSUM.A1a.holds_base`.
* `KSUM.A1c.Claim` was RESTATED in the coset-covering form — *for every `t` there is a window
  target `s ∈ t + kZ_q` with `Q(kSum_s) ≤ C·Q(kSum_t)`* — and is now **PROVED**
  (`KSUM.A1c.holds`, `C = 2`).  The previous all-pairs-of-targets rendering, which the manuscript
  never proves (the covering argument is coset-local) and which is not derivable from this
  interface, is retained unproved and unconsumed as `KSUM.A1c.ClaimAllPairs`, next to the
  machine-checked obstruction `KSUM.A1c.not_reachable_k3_q21`.  Source: finding R-A1-3 of
  `ksum/reviews/ksum_composition_layer_review_20260730.md`; report
  `ksum/artifacts/ksum_lean_repair_batch_20260730.md`.
* `KSUM.B4.B4bClaim` had its `q`-range restricted to `q` odd with `5 ≤ q ≤ N`: as written it was
  **unsatisfiable** (at `q = 2` the function is constant, so `Q = 0`), which made
  `KSUM.B4.composition` vacuous.  Finding R-B4-1 of the same review.  It remains STATED — it is
  the open lower bound — but it is now a hypothesis that could in principle be met.

**Consequence for non-vacuity (finding F-R8 of the reorg pass): CLOSED.**  All three inputs of
`KSUM.A1.composition` are now theorems (`KSUM.A1a.holds`, `KSUM.A1b.holds`, `KSUM.A1c.holds`), so
they are jointly satisfiable for every `M` and `KSUM.A1.holds` composes them into `A1d`'s
conclusion relative to the interface.  The composition is therefore not vacuous — while remaining
exactly as strong as ABI21/Tani24 and the `sec:prelim` facts, and no stronger.

**Updated again 2026-07-31 by the statement-fidelity closeout batch** (review
`ksum/reviews/ksum_lean_statement_fidelity_review_20260731.md`; report
`ksum/artifacts/ksum_lean_closeout_20260731.md`).  Three things moved in this section's scope:

* `KSUM.B4a.Claim` GAINED the manuscript's `q ≥ 2` hypothesis (review §10 caveat (1), the single
  WIDER verdict of the whole audit).  The interface field no longer grants more than
  `thm:k2-upper` states.  `KSUM.B4.composition` is unchanged in content: it consumes the Claim
  only under `5 ≤ q`.
* The two remaining non-vacuity gaps the review found are CLOSED with explicit witnesses, so no
  `∀ D : EmbedData, …` Claim and no side of the `B4` sandwich is any longer a statement about a
  possibly-empty class: `KSUM.Support.demoEmbed` inhabits `EmbedData`, and
  `KSUM.B4.sandwichModel` satisfies `KSUM.B4a.Claim` and `KSUM.B4.B4bClaim` SIMULTANEOUSLY
  (`sandwich_nonvacuous`).  **Neither is quantum query complexity**; both are consistency
  witnesses exactly as `KsumAudit.demoModel` is, and neither is evidence that the true `Q`
  satisfies anything.  The standing open obligation of §(b) is untouched.
* `KsumAudit.KFloor.core_reduction_at`'s general-`r` content acquired witnesses at `r ≥ 1`
  (`witness_{even,odd}_{pos,neg}_at`); the four pre-existing ones were all at `r = 0`, i.e. they
  witnessed only the corollary `core_reduction`.

════════════════════════════════════════════════════════════════════════════════════════════════
  (d)  TIER-T3 OBSTRUCTION GROUP — AUDITED 2026-07-30 (was UNADOPTED)
════════════════════════════════════════════════════════════════════════════════════════════════

`KsumAudit.Obstructions*` (eight modules) were left by an interrupted tier-T3 executor on
2026-07-30.  **Status flipped from UNVERIFIED/UNADOPTED to AUDITED on 2026-07-30** by the T3
adopt-or-rewrite audit; report `ksum/artifacts/ksum_lean_T3_obstructions_20260730.md`, evidence
`ksum/artifacts/logs_ksum_lean_T3_20260730/`.

    modules audited        : 8/8   (Core, PairTensor, Product, Block, Orientation,
                                    BandMult, TiltedBand, Transfer)
    theorem verdicts       : ADOPT 44 / REPAIR 0 / REJECT 0, plus 14 theorems ADDED
    declarations printed   : 58, all at exactly {propext, Classical.choice, Quot.sound}
    `sorry` / `axiom`      : 0 / 0        `native_decide` / `implemented_by` : 0 / 0
    build warnings         : 0 (were 16)

**This is an evidence attribute, not a status.**  Of the ten formalized (LaTeX target, node)
pairs, six are FAITHFUL and four are NARROWER; two further labels
(`lem:factorial-filtration`, `prop:joint-lp`) are not formalized at all and have no DAG node.  The
node `KSUM.LEAN.T3.obstruction-theorems` therefore sits at **NUMERICAL ·
pending-review: KSUM.LEAN.statement-fidelity** — not at any completion tier.  No obstruction
node's status was touched.

═════════════════════════════════════════════════════════════════════════════════════════════
  (e)  TIER-T2 — the `k`-floor cores and the Rosmanis barrier, 2026-07-30
═════════════════════════════════════════════════════════════════════════════════════════════

`KsumAudit.KFloor` (`KsumAudit/T2KFloor.lean`) and `KsumAudit.Rosmanis`
(`KsumAudit/RosmanisBarrier.lean`).  Report `ksum/artifacts/ksum_lean_T2_rosmanis_kfloor_20260730.md`,
evidence `ksum/artifacts/logs_ksum_lean_T2_20260730/`.

    LaTeX label            Lean name                                        verdict
    ────────────────────   ──────────────────────────────────────────────   ────────────────────
    lem:core               KFloor.core_wellformed, KFloor.sum_coreIdx       NARROWER (base target)
                           KFloor.sum_coreIdxAt                             the WHOLE-CORE-SUM
                                                                            SUB-CLAUSE only:
                                                                            FAITHFUL at every
                                                                            window target
                                                                            (2026-07-30)

           *** `lem:core` AS A WHOLE REMAINS **NARROWER**. ***  Row corrected 2026-07-31
           (statement-fidelity review defect H-7): as previously written, the second line read
           "FAITHFUL (2026-07-30: every window target)" against the label `lem:core`, which a
           reader could take as "`lem:core` is now faithful".  It is not.  `lem:core` has two
           clauses; only the first is closed:
             (1) the whole core sums to the target  — `sum_coreIdxAt`, proved at EVERY window
                 target `t₀ + r`, `r < k`.  FAITHFUL.
             (2) every NONEMPTY subset `A` of the core has `∑_{i∈A} c_i ∈ [U, t]`, with equality
                 iff `A` is the whole core — `core_wellformed`, proved at the BASE target `t = t₀`
                 ONLY, where all core entries equal `U` and the manuscript's two sub-cases
                 collapse.  The general-`t` subset-range clause is NOT formalized.
           Nothing downstream is weakened by this: `core_reduction_at` does not consume clause (2)
           in its general-`t` form, it redoes the case analysis inline.
    prop:core-even         KFloor.core_reduction_at (m = k-2 case)          FAITHFUL (2026-07-30:
                                                                            every window target;
                                                                            was NARROWER)
    lem:core-odd           KFloor.core_reduction_at (m = k-1 case)          FAITHFUL (2026-07-30,
                                                                            same repair)
    lem:transl-cover (id)  KSUM.A1c.kSum_translate                          FAITHFUL
    lem:transl-cover (Q)   KSUM.A1c.Q_kSum_translate_le                     FAITHFUL (constant 2)
    lem:transl-cover (i)   KFloor.window_even_length                        FAITHFUL
    lem:transl-cover (ii)  KFloor.window_odd_length                         FAITHFUL
    lem:transl-cover (cov) KFloor.exists_shift_into_window                  FAITHFUL
    lem:transl-cover (all) KSUM.A1c.Q_window_cover_coset, KSUM.A1c.holds    FAITHFUL (2026-07-30:
                                                                            the assembled
                                                                            coset-covering Claim)
    prop:rosmanis (1) >=2  Rosmanis.two_orbits_of_two_cycles /
                           two_orbits_of_one_cycle / not_single_orbit       ORBIT-PROPER; the
                                                                           count FORMULA is NOT
                                                                           formalized
    prop:rosmanis (2)      Rosmanis.existence_fails_q3 /
                           uniqueness_fails_q5                              witnesses only; the
                                                                           rep-theory sentence is
                                                                           NOT formalized
    prop:rosmanis (3)      Rosmanis.positive_blocks_empty                   FAITHFUL
    prop:embed             — NOT FORMALIZED (outside this run's budget)
    lem:embed-allt         — the gcd half is `KSUM.A2.coprime_k_q` (reorg pass); the translation
                             half is `KSUM.A1c.Q_le_of_coprime`

**Neither T2 module imports `QueryModel`**, so every theorem in them is UNCONDITIONAL; the only
interface-relative T2 results are the three in `KSUM/A1c.lean`, whose types show `M : QueryModel`.

No `sorry`.
-/
import KsumAudit.T2KFloor
import KsumAudit.RosmanisBarrier
import KSUM.goal
import KSUM.B4
import KSUM.A1
import KSUM.A1d
import KSUM.SelfTest
import KsumAudit.Smoke
import KsumAudit.MainLine
import KsumAudit.Obstructions

/-! ## `#print axioms` — the machine-checked citation manifest for the DAG layer

The current protocol's source-registration requirement, made mechanical.
The tier-T1 and tier-T3 modules carry their own `#print axioms` blocks at the end of
`KsumAudit/MainLine.lean` and each `KsumAudit/Obstructions*.lean`; importing them above puts
that output in the same build transcript. -/

-- support
#print axioms KSUM.Support.frozen
#print axioms KSUM.Support.append_nil
#print axioms KSUM.Support.frozen_eq_append
#print axioms KSUM.Support.Q_frozen_le
#print axioms KSUM.Support.blockPos
#print axioms KSUM.Support.Coll
#print axioms KSUM.Support.EmbedData.q_pos
#print axioms KSUM.Support.EmbedData.encodeInst

-- the A1 group
#print axioms KSUM.A1a.Claim
#print axioms KSUM.A1a.holds
#print axioms KSUM.A1a.holds_base
#print axioms KSUM.A1a.frozen_form
#print axioms KSUM.A1b.Claim
#print axioms KSUM.A1b.holds
#print axioms KSUM.A1c.kSum_translate
#print axioms KSUM.A1c.Q_kSum_translate_le
#print axioms KSUM.A1c.Q_window_cover_coset
#print axioms KSUM.A1c.Q_window_cover
#print axioms KSUM.A1c.Q_le_of_coprime
#print axioms KSUM.A1c.not_reachable_k3_q21
#print axioms KSUM.A1c.k3_q21_in_range
#print axioms KSUM.A1c.Claim
#print axioms KSUM.A1c.ClaimAllPairs
#print axioms KSUM.A1c.holds
#print axioms KSUM.A1d.Claim
#print axioms KSUM.A1.Claim
#print axioms KSUM.A1.composition
#print axioms KSUM.A1.holds

-- gap-closure batch 2 (2026-08-01): the general `lem:embed` construction
#print axioms KSUM.Support.geom_mul_add_one
#print axioms KSUM.Support.embed_two_mul_M
#print axioms KSUM.Support.embed_P_lower
#print axioms KSUM.Support.embed_P_upper
#print axioms KSUM.Support.embed_enc_inj
#print axioms KSUM.Support.genEmbed

-- the A2 group
#print axioms KSUM.A2a.Claim
#print axioms KSUM.A2b.Claim
#print axioms KSUM.A2.coprime_k_succ_of_dvd
#print axioms KSUM.A2.coprime_k_MvSucc
#print axioms KSUM.A2.coprime_k_q
#print axioms KSUM.A2.nsmul_surjective
#print axioms KSUM.A2.Claim
#print axioms KSUM.A2.composition

-- the B group
#print axioms KSUM.B1.Claim
#print axioms KSUM.B1.composition_via_frozen_core_reduction
#print axioms KSUM.B1.holds
#print axioms KSUM.B2.DonorClaim
#print axioms KSUM.B2.demoDonor
#print axioms KSUM.B2.Claim
#print axioms KSUM.B2.composition
#print axioms KSUM.B2.composition_with_donor
#print axioms KSUM.B4a.Claim
#print axioms KSUM.B4.B4bClaim
#print axioms KSUM.B4.Claim
#print axioms KSUM.B4.composition

-- tier T2: the `k`-floor cores (`KsumAudit/T2KFloor.lean`)
#print axioms KsumAudit.KFloor.sum_append_split
#print axioms KsumAudit.KFloor.card_append_split
#print axioms KsumAudit.KFloor.mem_coreIdx
#print axioms KsumAudit.KFloor.card_coreIdx
#print axioms KsumAudit.KFloor.sum_coreIdx
#print axioms KsumAudit.KFloor.coreVecAt_zero
#print axioms KsumAudit.KFloor.sum_coreIdxAt
#print axioms KsumAudit.KFloor.core_wellformed
#print axioms KsumAudit.KFloor.encode_cyc_eq_intCast
#print axioms KsumAudit.KFloor.abs_signedVal_le
#print axioms KsumAudit.KFloor.abs_live_sum_le
#print axioms KsumAudit.KFloor.live_sum_cast
#print axioms KsumAudit.KFloor.core_reduction_at
#print axioms KsumAudit.KFloor.core_reduction
#print axioms KsumAudit.KFloor.window_odd_length
#print axioms KsumAudit.KFloor.window_even_length
#print axioms KsumAudit.KFloor.exists_shift_into_window
#print axioms KsumAudit.KFloor.witness_q0_three
#print axioms KsumAudit.KFloor.witness_coreUnit
#print axioms KsumAudit.KFloor.witness_even_pos
#print axioms KsumAudit.KFloor.witness_even_neg
#print axioms KsumAudit.KFloor.witness_odd_pos
#print axioms KsumAudit.KFloor.witness_odd_neg
-- non-base window target `r ≥ 1` (closeout C-4(c), review §7.4)
#print axioms KsumAudit.KFloor.witness_coreVecAt_shifted
#print axioms KsumAudit.KFloor.witness_even_pos_at
#print axioms KsumAudit.KFloor.witness_even_neg_at
#print axioms KsumAudit.KFloor.witness_odd_pos_at
#print axioms KsumAudit.KFloor.witness_odd_neg_at

-- non-vacuity witnesses added by the 2026-07-31 closeout batch
#print axioms KSUM.Support.demoEmbed
#print axioms KSUM.Support.demoEmbed_q
#print axioms KSUM.B4.maxAlph
#print axioms KSUM.B4.sandwichQ
#print axioms KSUM.B4.sandwichModel
#print axioms KSUM.B4.twoSum_nonconst
#print axioms KSUM.B4.sandwich_B4a
#print axioms KSUM.B4.sandwich_B4b
#print axioms KSUM.B4.sandwich_nonvacuous

/-! ### Three culminating declarations added to the manifest 2026-07-31

Statement-fidelity review §2.2 defect **m-2** (called `m-1` in the closeout commission — the
labels are swapped there; both halves are done): three declarations that read as culminating
results were absent from the manifest.  Each was already *sound* — every one is consumed by a
printed theorem, so a bad dependency would have surfaced anyway — but a reader had to reconstruct
that argument instead of reading the line.  They live in `KsumAudit/Obstructions*`, which
`KsumAudit.Obstructions` (imported above) pulls in. -/

#print axioms KsumAudit.Obstructions.Orientation.orientation_corr_le_half
#print axioms KsumAudit.Obstructions.not_pureHighDegree_succ_of_moment_zero_ne_zero
#print axioms KsumAudit.Obstructions.PairTensor.exists_light_pair

-- tier T2: the Rosmanis barrier (`KsumAudit/RosmanisBarrier.lean`)
#print axioms KsumAudit.Rosmanis.isNegative_iff_twoSum_false
#print axioms KsumAudit.Rosmanis.isNegative_iff
#print axioms KsumAudit.Rosmanis.isNegative_act
#print axioms KsumAudit.Rosmanis.valueCount_act
#print axioms KsumAudit.Rosmanis.not_same_orbit
#print axioms KsumAudit.Rosmanis.not_single_orbit
#print axioms KsumAudit.Rosmanis.valueCount_constStr
#print axioms KsumAudit.Rosmanis.valueCount_oneOffStr
#print axioms KsumAudit.Rosmanis.isNegative_constStr
#print axioms KsumAudit.Rosmanis.isNegative_oneOffStr
#print axioms KsumAudit.Rosmanis.two_orbits_aux
#print axioms KsumAudit.Rosmanis.two_orbits_of_two_cycles
#print axioms KsumAudit.Rosmanis.two_orbits_of_one_cycle
#print axioms KsumAudit.Rosmanis.positive_blocks_empty
#print axioms KsumAudit.Rosmanis.involutive_sub
#print axioms KsumAudit.Rosmanis.twoSum_not_single_orbit
#print axioms KsumAudit.Rosmanis.existence_fails_q3
#print axioms KsumAudit.Rosmanis.swapped_string_q3
#print axioms KsumAudit.Rosmanis.uniqueness_fails_q5
#print axioms KsumAudit.Rosmanis.q5_cycle_type
#print axioms KsumAudit.Rosmanis.witness_two_cycles_q5
#print axioms KsumAudit.Rosmanis.witness_one_cycle_q3
