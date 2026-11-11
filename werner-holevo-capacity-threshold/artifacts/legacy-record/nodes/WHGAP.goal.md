---
id: "WHGAP.goal"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.goal.md"
aliases: ["G"]
kind: GOAL
role: proof
status: OPEN
status_source: "problem-scaffold-2026-07-28"
disposition: null
parents: []
children: ["WHGAP.qpositive-onset", "WHGAP.zero-capacity-application", "WHGAP.onset-two-fifths"]
related: ["WHGAP.antideg-boundary", "WHGAP.signed-lift-extension", "WHGAP.order-boundary", "WHGAP.relaxed-lift", "WHGAP.more-capable-route", "WHGAP.no-ascent-hierarchy", "WHGAP.choi-distillation-necessary", "WHGAP.order-converse", "WHGAP.restricted-order", "WHGAP.private-boundary", "WHGAP.pure-anchor-order", "WHGAP.direction-restricted-order"]
---

# WHGAP.goal — Zero-capacity boundary of the noisy Werner–Holevo family

## Claim

Determine {x : Q(Lambda_x) = 0} for the qutrit family Lambda_x(X) = (1-x) X + (x/2)(Tr(X) 1 - X^T); close the gap x in (1/2, 4/7). **[OPEN]**

## Role in DAG

Problem GOAL. **Edge normalization 2026-07-30 (protocol update: edges are obligations):**
children are now ONLY the three status-propagating pieces of the determination — P3
(the lower piece Q > 0), P4 (the upper piece Q = 0), P13 (the remaining strip). All other
campaign nodes (P1, P2, P6–P12, P14–P16) are methodological inputs, companion theorems, or
dead routes and moved to `related`; P2 and P9 remain in the graph as CHILDREN OF P4 and P3
respectively, where their status actually propagates.

## Composition proof

```yaml
composition:
  claim: >
    (P3) Q(Lambda_x) > 0 for every x in (0, 2/5)  AND
    (P4) Q(Lambda_x) = P(Lambda_x) = 0 for every x in [1/2, 1)  AND
    (P13) a determination of {x in [2/5, 1/2) : Q(Lambda_x) = 0}
    together determine {x in (0, 1) : Q(Lambda_x) = 0} completely
    (= [1/2, 1) union the P13 set; the x = 1 endpoint is carried by P4's corollary
    at CERTIFIED* via the cite-only RK24 antidegradability input, or by the paper's
    Lemma 4.1 at written-proof tier).
  proof: inline (below)
  review: null   # inline set logic; review folded into the next full-DAG review
  status: OPEN   # rel: P13 unresolved — this is exactly why the GOAL is OPEN
  rel: ["P13 (the strip) is CONJECTURED, not resolved", "x = 1 endpoint tier per P4"]
```

**Inline proof of the assembly claim.** (0,1) is the disjoint union of (0, 2/5),
[2/5, 1/2), and [1/2, 1). On the first piece P3 gives Q > 0, so the piece contributes
nothing to {x : Q = 0}. On the third piece P4 gives Q = 0, so the whole piece is
contained in {x : Q = 0}. The second piece is precisely P13's claim set. Hence
{x in (0,1) : Q = 0} = [1/2, 1) ∪ {x in [2/5, 1/2) : Q = 0}, and the determination is
complete exactly when P13 is resolved. No other input is used; the pieces are exhaustive
and pairwise disjoint by the ordering 0 < 2/5 < 1/2 < 1. ∎

Status arithmetic (§1 of the protocol): status(G) = min over the AND inputs =
min(status(P3 route), status(P4 route), status(P13)) = min(CERTIFIED*, PROVED,
CONJECTURED) = capped by P13 ⟹ **G = OPEN with the explicit relative display "resolved
except on [2/5, 1/2)"**. This matches the hand-written header status.

## Current status

OPEN. Antidegradable for x >= 4/7 (Roofeh–Karimipour, PRA 109, 052620 (2024)); x=1/2 has Q=P=0 by the signed-lift certificate (Zhu–Wang, one day old; see `../../../literature/papers/zhu-wang-2026-quantum-incapacity/`). Ranked the easiest active target in the 2026-07-28 assessment: minimal dimensions, published worked example, no competition observed. Note: qutrit finite-dimensional family — correctly filed under channel-capacity (the initial survey map placed it in the bosonic block in error).

2026-07-28 update: child P1 (`WHGAP.antideg-boundary`) reached CERTIFIED\* at narrow scope —
"4/7 numerically tight (1e-6)" — via the completed fresh-session rule-7 review
(`artifacts/whgap_p1_review_20260728.md`); the exact boundary remains GAP there. This GOAL stays
OPEN per the same-date propagation adjudication in the Work record: its registered children are
contributory sub-steps, neither of which alone decides the goal claim, so OR-max does not lift
this node.

**2026-07-30 late update — the PRIVATE-capacity half of the question is CLOSED.** New
child P14 [`WHGAP.private-boundary`](WHGAP.private-boundary.md) = PROVED (R8 review):
P^{(1)}(Lambda_x) > 0 for every x < 1/2 with an exact closed-form witness value, hence
{x in (0,1) : P(Lambda_x) = 0} = [1/2, 1) exactly (closed interval at CERTIFIED\*). So the
goal's private half is settled and coincides with the order boundary; only the QUANTUM
half on the strip [2/5, 1/2) remains open — and there the family would exhibit
**P > 0 = Q** if Q vanishes. The restricted-order programme (P12) is correspondingly
resolved in the large (every P^{(1)}-implying class is FALSE below 1/2) with two surviving
candidates registered: P15 [`WHGAP.pure-anchor-order`](WHGAP.pure-anchor-order.md) and P16
[`WHGAP.direction-restricted-order`](WHGAP.direction-restricted-order.md).

**2026-07-30 update — the open strip shrinks to [2/5, 1/2), and the order picture is
exact.** From the R5 batch reviews: (i) **Q(Lambda_x) > 0 for ALL x in (0, 2/5) is
PROVED** (E-N1 expansion-lemma note, R5d review LICENSE A — one isotropic witness family
does the whole interval), upgrading child P3's scope and subsuming its (0, x_1) package;
(ii) **the cBKM/cRE order boundary is exactly 1/2, PROVED** (lead's necessity witness,
paper §5, R5b review LICENSE A) — child P6 ANSWERED, and with P2/P4 this gives the exact
phase classification cBKM ⟺ cRE ⟺ signed-lift ⟺ x ∈ [1/2, 1); (iii) the onset conjecture
x_D = 2/5 is registered as new child P13 `WHGAP.onset-two-fifths` (CONJECTURED). The goal
claim {x : Q = 0} is now pinned except on the strip **[2/5, 1/2)** (width 0.1).

**2026-07-28 late update — the named gap is CLOSED.** Child P4
(`WHGAP.zero-capacity-application`) is PROVED (R3 review, licensing statement 1):
Q(Lambda_x) = P(Lambda_x) = 0 for every x in [1/2, 1) at every blocklength, via the P2-PROVED
covariant signed-lift family. The claim's second clause — "close the gap x in (1/2, 4/7)" — is
therefore resolved (R3 states the substatement has no RK24 dependency). With cite-only RK24 at
the endpoint, {x : Q=0} ⊇ [1/2, 1] (CERTIFIED\* scope). The GOAL remains OPEN only for the
FIRST clause — the full determination of {x : Q(Lambda_x) = 0} — whose remaining frontier is
x < 1/2 (child P3 `WHGAP.qpositive-onset`, OPEN; RK25 literature lead on file).

## Dependencies

None recorded yet beyond the shared field literature in `../../../literature/` (catalog + per-paper pages; see `../../README.md`).

## Work record

- 2026-08-01 — **commission LEAN-3 dispatched** (rule 8a; lead directive of the same day:
  continue formalizing the residual gaps notwithstanding diminishing returns):
  [WHGAP_COMMISSION_LEAN3_20260801.md](../../notes/WHGAP_COMMISSION_LEAN3_20260801.md) —
  three sequential Opus 5 packages with checkpoint commits: **WP-F** small closures (hsq
  discharged so Delta_lower_bound goes unconditional; the Lemma 4.1 x=1
  self-complementarity display; optional §5 witness scalars); **WP-E** the eigenvalue
  multiset completed via charpoly(Cmat) = X¹⁹(X−λ₅)⁵(X−λ₃)³ for all x ≠ 0 — the
  small-certificate similarity route exploits WP-A's x-independent projections so NO
  large kernel product is needed beyond one S⁻¹S = 𝟙 check; **WP-D** the identification
  layer (channel, complement, forced-point lift, defect and its Choi DEFINED in Lean;
  choi_defect_eq_Cmat closing Trust residual (a); outB/outE = channel outputs closing
  (c); specB/specE at charpoly level closing (b) modulo the stated complex-entropy
  glue). R13 review to follow.

- 2026-08-01 — **LEAN-3 WP-F LANDED, all three items incl. the optional one, sorry-free**
  (`pending-review:` R13): (1) **hsq DISCHARGED** — f_ge_sq proved (two-level
  monotoneOn_of_deriv_nonneg; the commission's route note was factually wrong — f_pos
  uses the Gibbs inequality, not derivatives — executor wrote the derivative argument
  from scratch and recorded two paper-checked dead ends), Delta_lower_bound now
  UNCONDITIONAL (only 0 < x < 1/2); Trust census row struck via a dated append-only
  removals subsection. (2) New `WHGAP/Support/SelfComplement.lean`: **paper Lemma 4.1's
  x = 1 entrywise display machine-checked** (½Tr(A_μXA_νᵀ) = Λ₁(X)_μν for all real X)
  with the honest scope block (capacity conclusion stays the ZW interface). (3) §5
  witness BKM scalars g_B, g_E defined and gE_lt_gB (strict violation on
  0 < ε < ε_c(x)) proved FROM the existing factorizations — wired, not duplicated.
  Build green, 0 sorry, axioms clean, all gates at baseline. Report:
  [whgap_lean3_20260801.md](../../../../artifacts/whgap_lean3_20260801.md) §WP-F.

- 2026-08-01 — **LEAN-3 WP-E LANDED: charpoly(Cmat) = X¹⁹(X−λ₅)⁵(X−λ₃)³ machine-checked
  for EVERY real x, NO side condition** (`pending-review:` R13). R12 m6's spectral
  residual is CLOSED: the symmetric-diagonalizability step is no longer used, the
  exponent 19 is DERIVED (27−8), coincidence points covered — **charpoly_half gives
  the eigenvalue multiset X²⁴(X−8/9)³ at x = 1/2** (a point multiplicity_unique could
  not reach; the paper's rank-3 READING is an extra diagonalizability step — completed
  by rank_Cmat_half in LEAN-3.2 per R13 MAJOR-2, which flagged the original "i.e.
  rank C = 3" gloss here as an invalid charpoly⟹rank inference). **Route substitution (reported, not
  silent):** the frozen kernel-basis/similarity route was replaced — the WP-A
  decomposition IS already a rank-8 factorization C = F_x·G, and the reversed 8×8
  product G·F_x = diag(λ₅𝟙₅, λ₃𝟙₃) follows from the four existing small certificates;
  Mathlib's rectangular Weinstein–Aronszajn (charpoly_mul_comm_of_le) finishes it. The
  expensive step DOES NOT EXIST (~80 s compile vs the ~8-min allowance); result strictly
  stronger (all real x); the frozen route was verified in sympy anyway (det S =
  −63700992, S⁻¹CS = D — gates E1–E4) so a reviewer can confirm the substitution was for
  cost/strength, not failure. Honesty: x = 0 branch is Lean's junk-convention artifact
  (stated in the docstring; charpoly_Cmat_of_ne_zero is the loaded branch); this
  machine-checks eq:charpoly OF THE APPENDIX A DISPLAY (Trust residual (a) untouched —
  WP-D's target); the paper's spin-reduction/pencil narrative remains unformalized (the
  Lean proof reaches the same polynomial by an unrelated road); no PSD/sign content.
  Pre-verification: 31/31 sympy gates incl. an INDEPENDENT Berkowitz determinant at nine
  rational x (7f value-vs-formula). Budget note: ~100 min vs 90 allowed (two rebuild
  cycles on a maxRecDepth fix), reported. Report §WP-E; logs wpe_*.

- 2026-08-01 — **LEAN-3 WP-D LANDED (partially): the channel exists in Lean; residuals (a)
  and (c) of `Trust.lean` are CLOSED, residual (b) is NOT** — status **NUMERICAL,
  `pending-review:` R13** (rule 6: a green build is a run, DAG §2; no completion tier
  without an independent review). New module
  [`WHGAP/Support/Channel.lean`](../lean/WHGAP/Support/Channel.lean) builds the Kraus set
  `K₀ = t·1`, `K_{μ+1} = s·A_μ` (`s² = x/2`, `t² = 1−x`), the Kraus sum (`LamK_eq`) and its
  trace preservation (`LamK_tp`), the padded 4×4 complement `(Λ^c(X))_{ab} = Tr(K_a X K_bᵀ)`
  with the `eq:comp` block form (`LamCK_eq`, `β = s t`), the forced-point lift of `eq:Jintro`
  and its Hilbert–Schmidt adjoint (`Jdag_adjoint`), the `q`-chart
  (`q = t/(3s) = (1/3)√(2(1−x)/x)`, `β = (3x/2)q`, `9xq² = 2(1−x)`, `qβ = (1−x)/3`;
  `exists_chart` shows it is inhabited on `0 < x < 1`, so nothing is vacuous), and the defect
  superoperator. **`choi_defect_eq_Cmat`**: the Choi matrix of
  `Δ_J(τ)(Y) = Λ(τ)Y − J†(Λ^c(τ)J(Y))` **is** `DefectChoi.Cmat x`, all 729 entries, every `x`
  on the chart — this is residual (a), the bridge R12 had verified 729/729 in sympy only.
  **`«private-boundary».outB_eq`/`outE_eq`**: `outB`/`outE` **are** `Λ_x(ρ_ε ± θX)` and
  `Λ^c_x(ρ_ε ± θX)` entrywise (residual (c)), so `hdev` now carries Devetak's formula alone.
  **Not landed: residual (b)** — the §6 witness's COMPLEX `specB`/`specE` charpolys were not
  reached in the budget; they stay exact-sympy only (gates D9a–D9e) and `Trust.lean`'s
  residual block says so in those words. Route (the reason the 729-entry bridge fit the
  budget at all): factor it into NINE entry identities for general `τ, Y` plus fifteen
  generic word↔`pat` identities — no 27×27 product, no `decide`, no codegen; and remove
  every square root by substituting `x = 2/(9q²+2)`, after which each entry closes by
  `field_simp; ring` with no side relation. Scope UNCHANGED and restated in README items 1,
  7, 11: no complete positivity, no Stinespring, no proof that `LamCK` is *the* complementary
  channel, **and the coding-theorem interfaces (`lsd_devetak`, `zw_hrsf_zero`,
  `q_pos_of_ic_pos`) plus the §4 entropy assembly (`hach`) remain outside Lean**. Closing (a)
  also upgrades WP-E's `charpoly_Cmat` from a statement about the Appendix A display to a
  statement about the actual defect Choi matrix. Pre-verification (before any Lean):
  [`tools/whgap_lean3_wpd_check.py`](../../../../tools/whgap_lean3_wpd_check.py), 24/24 gates
  D0–D9e. Closeout: clean rebuild exit 0, `#print axioms` = the 3 standard (or subsets) on
  203 declarations, forbidden scan clean, freeze-check 8/8 unchanged, `lean_dag_check` 0 FAIL,
  `proof_dag_check`/`literature_check` OK. Budget note: ~165 min vs 150 allowed (three
  tactic-repair rebuild cycles), reported. Report
  [whgap_lean3_20260801.md](../../../../artifacts/whgap_lean3_20260801.md) §WP-D; logs
  `artifacts/logs_whgap_lean3_20260801/wpd_*`.

- 2026-08-01 — m7 hygiene note (decision layer, applying R13): a near-duplicate shorter
  WP-D entry authored by the decision layer was MERGED into the detailed entry above
  (content fully contained). Provenance flag, recorded honestly: the detailed entry's
  authorship is ambiguous — the WP-D executor reported "no node markdown edited", yet
  the entry contains its closeout results; either the executor slipped on the
  single-writer deviation or a records overlap occurred. The mathematics is unaffected;
  the discipline question is noted for the next commission's checklist.

- 2026-08-01 — **obligations batch CLEARED (LEAN-4/R9/M6 parallel + R14 chained; commission
  [WHGAP_COMMISSION_LEAN4_R9_M6_20260801.md](../../notes/WHGAP_COMMISSION_LEAN4_R9_M6_20260801.md)):**
  **WP-G** landed sorry-free — specB_charpoly/specE_charpoly over ℂ (statements
  square-root free via the quadratic factor; strictly stronger than the physical case:
  arbitrary complex x, ε), plus the _list forms matching IcScalar's literal lists;
  **Trust residual (b) is REDUCED to exactly the complex charpoly→vnEntropy glue**
  (named identically in Trust/Channel/README; neither "closed" nor "not reached" —
  reduced). **R9 on P15-A** completed (FINDINGS, applied on
  [[WHGAP.pure-anchor-order]]): strictness at 2/5 CONFIRMED, but the strip null was
  CORRECTED — P_b2 is violated at 41/100 (the note's own data; R9 agrees to 9 digits);
  the false A3.3 criterion is struck and not registered. **M6** discharged: BGSW25
  ingested (arXiv:2411.19890, PDF + README + catalog entry; the bridge identified as
  their Lemma 4.1 with THREE scope gaps honestly recorded — we use one direction only;
  the reference-system-free form vs the complete orders; support vs faithfulness —
  literature_check 52 papers green). **R14: LICENSE A, 0 MAJOR, 5 doc minors** —
  rank_Cmat_half re-derived by own route ("genuinely repaired the strong way"), both
  WP-G charpolys re-derived symbolically with hβ shown load-bearing, regime gate run
  (rank = 8/5/3 at the three regimes), non-vacuity established in-Lean; minors applied
  same-day (script header; IcScalar stale under-claim cross-referenced; BOut gloss
  marked "(true, not formalized)"; the unformalized rank-8 conjunct named; paper
  Lean-status paragraph refreshed — v5.3). Checker harmonization committed separately
  (2151761). 232 Lean declarations, 0 non-standard axioms, 0 sorry.
  **All four registered obligations from the LEAN-2/3 era are now CLOSED or reduced to
  named residues**; remaining review debt: none (rank_Cmat_half reviewed by R14).

## Adversarial reviews

- 2026-08-01 — **R13 (fresh Opus 5 instance, §7.10 review of the LEAN-3 batch): FINDINGS
  — 2 MAJOR + 10 minor, NEITHER a soundness defect; everything the batch proves checks
  out.** Own-route verification before reading executor notes (7c): exact-sympy rebuild
  of the 27×27 defect Choi from the Kraus chain matched entry-by-entry 729/729 at four
  rational x; all nine defect_eq identities verified under a DIFFERENT ideal reduction
  (q² → 2(1−x)/(9x)); Berkowitz charpolys of TWO independent constructions at four x;
  outB/outE symbolically incl. the every-β claim; Lemma 4.1 by hand; 203/203 axiom
  checks; the Weinstein–Aronszajn route confirmed sound with the exponent 19 DERIVED;
  vacuity excluded in-Lean out-of-tree. **MAJOR-1:** Channel.lean's own scope block
  referenced PHANTOM declarations (specB_charpoly/specE_charpoly — leftovers of the
  un-landed item) presenting the honestly-degraded residual (b) as closed. **MAJOR-2:**
  "charpoly_half i.e. rank C = 3" was an INVALID inference (a charpoly does not
  determine rank) in four places — the fact is true (R13 computed rank = 3) but was not
  machine-checked. Minors m1–m10 (stale under-claims mirroring MAJOR-1; stale node
  metadata; dead import; README numbering; hdev enumeration incomplete — ensemble
  validity named; hach mislabeled; goal-node section hygiene; ledger pinning a live
  file; linter noise; vestigial hr0). Report:
  [whgap_r13_lean3_review_20260801.md](../../../../artifacts/whgap_r13_lean3_review_20260801.md).
- 2026-08-01 — **LEAN-3.2 repair applied (Opus 5) + decision-layer m2/m7 closeout — R13's
  conditional license DISCHARGED.** MAJOR-1: scope block rewritten, phantom names deleted
  (tree-wide grep zero hits), dead import dropped. **MAJOR-2: fixed the STRONG way —
  `rank_Cmat_half : (Cmat (1/2)).rank = 3` is now a REAL theorem** (route deviation
  reported: the factorization route via rank_mul_le/rank_of_isUnit needs NO
  diagonalizability step, unlike R13's squarefree-annihilator sketch — the paper's
  rank-3 claim at the decisive point is machine-checked outright); all four glosses
  corrected. m1/m4/m5/m6/m9/m10 applied (incl. hdev's complete enumeration with the
  ensemble-validity residual; hr0 dropped — theorems strictly stronger); m8 ledger
  regenerated with the live node-file row removed via a dated header amendment
  (05c03ee1… recorded, nothing silent); m2/m7 by the decision layer (metadata refreshed;
  single-section structure restored; the WP-D entry provenance ambiguity recorded
  honestly). Final state: rebuild exit 0 (3202 jobs), **206 declarations — 0
  non-standard axioms, 0 sorry**, freeze 8/8, lean_dag_check 0 FAIL, warnings 35 → 22
  (all accounted). Evidence tier NUMERICAL (rank_Cmat_half is new unreviewed executor
  work; proposer ≠ checker applies — flagged for the next review batch).

- 2026-07-31 — **R12 (fresh Opus 5 instance, §7.10 review of the complete LEAN-2 batch):
  LICENSE A — 0 MAJOR, 8 minors (all documentation/record-accuracy; none changes what is
  proved).** Reproduced clean rebuild (3200 jobs, exit 0); 146/146 axiom checks;
  freeze 8/8; lean_dag_check 0 FAIL. **All three route deviations audited as SOUND
  SUBSTITUTIONS, each strictly stronger than the frozen route:** (a) WP-A — R12 rebuilt
  the 27×27 defect Choi FROM SCRATCH from the Kraus chain and matched the App A forced
  column 729/729 SYMBOLICALLY (the declared outside-Lean bridge now has a second
  independent witness); the 15-coefficient constant-combination claim verified as PROVED
  (the ext+ring structure IS the fifteen-fold identity), all eight certificates
  re-verified against R12's own pattern table, App C eigenvalue column reproduced incl.
  λ₅(49/100) = −102/1225; (b) WP-B — the SOS discriminant identity and the sharp bracket
  re-derived independently (the commissioned two-sided bracket would have been LOSSY);
  bare-2 remainder re-derived; hypotheses confirmed as only 0 < x < 2/5 off the type;
  (c) WP-C — exact two-sided inverses verified, spectra as multisets via charpoly (no
  sorting), symbol-by-symbol match against paper §7, and the outB/outE identification
  matched SYMBOLICALLY against R12's own Kraus rebuild. Trust boundary enumerated
  complete (no undisclosed hypothesis; hconj/hdeg never existed); the two new bridge
  theorems proved NON-VACUOUS by an out-of-tree satisfiability certificate (hdev
  inhabited WITH EQUALITY via Delta_eq_chi_diff). Minors m1–m8 (wording qualifiers,
  stale metadata, in-tree satisfiability fold-in, lam5/lam3 dedup, Trust residuals
  section, multiplicity_unique scope, ledger header, commit-subject hygiene). Report:
  [whgap_r12_lean2_review_20260731.md](../../../../artifacts/whgap_r12_lean2_review_20260731.md).
- 2026-07-31 — **LEAN-2.1 repair applied (Opus 5) + decision-layer m2 closeout — the R12
  minors are DISCHARGED:** m1 wording qualified in all three places; m3 R12's
  satisfiability declarations folded in-tree (WHGAP/Model.lean §3b, R12 credited); m4
  lam5/lam3 deduplicated (delete-and-reuse — the "serves P2" import is now genuinely
  consumed); m5 Trust.lean gained the "Definitional-identification residuals" section
  (the three definition-vs-referent gaps named with their discharge locations); m6
  multiplicity_unique docstring scoped (spectral-theorem step outside Lean; excludes
  x ∈ {1/3, 1/2, 5/6}; ℝ-coefficients note) and the report's stretch claim downgraded to
  "partially delivered"; m7 ledger header states the LF convention (33/33 re-verified);
  m2 node lean: blocks refreshed this session (build pointer → logs_whgap_lean2_20260731;
  P14 composition lists Claim_of_devetak with the REDUCED rel display; P9 rel carries the
  WP-B carve-out + hach); m8 noted for future commit hygiene (three LEAN-2 commit
  subjects said "PROVED" for pending-review work — git history immutable, discipline
  recorded in memory). Rebuild green: 150/150 axioms clean, 0 sorry, all gates.
  **R12's license (A) stands on the repaired tree: the LEAN-2 batch is a faithful
  extension of the licensed mirror.** Evidence tier NUMERICAL (a green build is a run).

- 2026-07-30 — **R11 (fresh Opus 5 instance, §7.10 statement-fidelity review of the Lean
  development — the completion gate): FINDINGS — 2 MAJOR + 15 minor, NEITHER MAJOR a
  soundness defect** (both attribution/metadata). REPRODUCED, not trusted: full clean
  rebuild (build outputs deleted, exit 0 in 491 s, 3051 jobs — same count as the
  executor); 44/44 axiom checks; 13-pattern forbidden-construct scan clean; **8/8 frozen
  Claims verified in both hash and verbatim text by THREE non-shared instruments** (the
  authoring tool, an own from-scratch auditor, and shell-only awk+sha256sum on four
  nodes); import graph = skeleton; per 7c the reviewer derived its own Claim-vs-prose
  comparison BEFORE opening the executor's self-table; every T2 scalar identity re-derived
  by hand and matched to its manuscript display; endpoint discipline clean throughout.
  **Satisfiability established by construction**: an out-of-tree machine-checked
  NON-TRIVIAL CapacityInterface model discharging all composition theorems in one model
  (exit 0) — nothing is vacuous. The P14 flagship chain confirmed genuinely unconditional
  from elaborated signatures. **MAJOR-1:** blockA_trace_det misattributed (belongs to
  paper Lemma 6.1 / the P9-P3 positivity layer, not P14/"Lemma 7.1") — theorem moved and
  both nodes' metadata corrected. **MAJOR-2:** P9's recorded lean.state
  "composition-checked" was UNBACKED (no composition theorem in that module; a
  decision-layer transcription of an executor-report error) — corrected to proved+stated.
  Minors applied or registered (see the repair record below). R11's conditional license:
  once the two MAJORs are corrected, statement (A) — "the Lean development is a faithful
  machine-checked mirror at the stated tiers" — is fully supported. Report:
  [whgap_r11_lean_review_20260730.md](../../../../artifacts/whgap_r11_lean_review_20260730.md).

### Earlier work record (2026-07-28 → 2026-07-31 campaigns)

- 2026-07-31 — **LEAN-2 WP-C LANDED (T3), sorry-free and UNCONDITIONAL — the hconj
  degradation was NOT needed** (`pending-review:` R12): new
  `WHGAP/Support/Entropy.lean` (231 lines) defines vnEntropy for real symmetric matrices
  with a dedicated scope block; the needed Mathlib glue ALREADY EXISTED
  (IsHermitian.roots_charpoly_eq_eigenvalues, eigenvalues_eq_eigenvalues_iff,
  charpoly_diagonal, charpoly_fromBlocks_zero₁₂ — API exploration recorded). Core
  lemmas (a) diagonal, (b) orthogonal-conjugation invariance AND the rational-similarity
  form, (c) block additivity + the scalar two_point_collapse. **PAYOFF (paper Lemma 7.1
  in Lean): chiB_collapse (χ_B = b·f(u/b)), chiE_collapse (χ_E = e·f(v/e)),
  Delta_eq_chi_diff (Δ(x) = χ_B − χ_E on all of (0,1/2), unconditional), and
  Claim_of_devetak — P14's Claim now follows from hdev = the Devetak interface reading
  of ONE explicit ensemble** plus the sympy-checked (non-Lean) identification of
  outB/outE with the channel outputs. Two route deviations reported not silent: the
  payoff path uses rational-similarity certificates (U with rational inverse) instead of
  the orthogonal form (which is also proved, but carries 1/√2); the blocks lemma is
  delivered but not load-bearing. Pre-formalization: 39/39 sympy gates incl. SYMBOLIC
  entrywise match of outB/outE against the Kraus-rebuilt channel in (x,ε,t). Honesty
  layer updated: the old opaque hbridge gap is now split into the PROVED entropy
  collapse + two named residuals (identification; Devetak); README declares the minimal
  T3 tier with the lead authorization and removes lem:holevo from the unchecked list.
  Gates green. Report §WP-C; logs wpc_*.

- 2026-07-31 — **LEAN-2 WP-B LANDED, main theorem sorry-free and UNCONDITIONAL**
  (`pending-review:` R12): new `WHGAP/Support/IcScalar.lean` (515 lines). Matrix
  identification layer (explicit B-side 3×3 with mulVec eigen-equations; E-side
  fromBlocks A⊕B with the eight cross entries proved zero; blockA charpoly; blockB
  spectrum by explicit eigenvectors); IcScalar over Real.negMulLog with the discriminant
  handled by the exact SOS identity discE = (1−3x/2)² + 2x(1−x)(1−2ε)²;
  **exists_eps_IcScalar_pos: ∀ x ∈ (0, 2/5), ∃ ε: IcScalar > 0** with hypotheses ONLY
  0 < x < 2/5, plus the quantitative bound d₁·negMulLog(ε) − 2ε ≤ IcScalar on (0, 1/3].
  **Route deviation, reported not silent — and SHARPER than commissioned:** the
  three-group split + two exact algebraic identities give λ₋ ≤ μ_A ε sharply, so the
  remainder constant is a bare 2 instead of the prose note's C(x) = 14/x + 11 + 4log(3/x);
  witness ε(x) = min(1/3, exp(−3/d₁)). Pre-formalization numeric verification at 42
  (x,ε) points vs the Kraus-rebuilt channel (< 1e-12) and adaptive mpmath to ~14000
  digits (at x = 0.3999 the witness is ε ~ 1e-6948). **Trust-boundary reduction:** the
  wiring (Claim_of_witness) replaces the pair {achievability reading, hexp} by the
  SINGLE hypothesis hach (the achievability reading = the entropy layer, exactly what
  WP-C targets); hexp is retained only for the general arbitrary-Ic lemma. Gates green
  (build, 0 sorry, axioms, lean_dag_check, freeze 8/8). Report §WP-B; logs wpb_*.

- 2026-07-31 — **LEAN-2 WP-A LANDED, sorry-free and UNCONDITIONAL** (`pending-review:`
  R12): new module `WHGAP/Support/DefectChoi.lean` builds the 27×27 defect Choi from the
  Appendix A master formula and proves, for EVERY x ≠ 0: the annihilating identity
  C(C−λ₅)(C−λ₃) = 0, both trace identities, symmetry, AND the spectral decomposition
  **C = λ₅Q₅ + λ₃Q₃ with x-INDEPENDENT orthogonal projections** — plus the stretch
  (multiplicity solve; exact coincidence points λ₅=0 ⟺ x=1/2, λ₃=0 ⟺ x=1/3,
  λ₅=λ₃ ⟺ x=5/6; the three App C sample points instantiated). **Route deviation,
  reported not silent:** the frozen PIT route was abandoned after the commissioned pilot
  timing (one 27×27 kernel product = 6m25s ⟹ ≥14 products unaffordable); replaced by an
  x-independent spectral factorization C = (λ₅/12)W₅V₅ᵀ… with INTEGER x-free R₅, R₃
  certified by four SMALL decidable checks — a STRONGER result (all x ≠ 0, no
  interpolation, no hdeg). Inputs sympy-verified before any Lean (App A chart
  transcription; 729/729 agreement with the independent whgap_p2_exact construction; the
  paper's two closed-form traces). Honest non-coverage recorded (report items 7–10): the
  channel→defect construction bridge stays at sympy+R2-prose tier; spin reduction/Gram
  data/ZW factorization not formalized; the multiset conclusion rests on the textbook
  symmetric-diagonalizability step. Gates: build green, 0 sorry, axioms clean,
  lean_dag_check 0 FAIL, freeze-check 8/8. Report:
  [whgap_lean2_20260731.md](../../../../artifacts/whgap_lean2_20260731.md) §WP-A;
  logs `artifacts/logs_whgap_lean2_20260731/` (wpa_*).

- 2026-07-31 — **commission LEAN-2 dispatched** (rule 8a; lead directive of the same day
  authorizes the T3 entropy layer, quoted verbatim in the commission):
  [WHGAP_COMMISSION_LEAN2_20260731.md](../../notes/WHGAP_COMMISSION_LEAN2_20260731.md) —
  closing the two project-specific Lean gaps + the minimal entropy layer, three
  sequential Opus 5 work packages with checkpoint commits between: **WP-A** the spectrum
  theorem's basis-free core (annihilator + two trace identities) as a COMPLETE identity
  proof via polynomial identity testing (deg ≤ 6 entries, 7 rational evaluation points +
  the interpolation lemma — a proof for ALL x, not sampling); **WP-B** the expansion
  theorem for the §6 witness family as scalar real analysis over Real.negMulLog
  (replaces the abstract hexp for this family with a carried proof); **WP-C** the
  minimal vnEntropy layer (T3) discharging paper Lemma 7.1's Holevo collapse, reducing
  P14's hbridge to exactly the Devetak interface. R12 review to follow.

- 2026-07-30 — **M7 DELIVERED — the §7.6 anti-drift checker exists and its gates all
  PASS** (`pending-review:` executor-authored, NUMERICAL): `tools/lean_dag_check.py`
  implements all seven §7.6 checks at the commissioned severities, plus an extra WARN
  check 3b (docstring frozen-body vs node Claim body) closing the exact "edited body,
  intact hash line" hole R11 m7 named; hash normalization verified byte-identical to the
  freeze tool on all 8 nodes; a coverage block makes silent check-skips impossible.
  **G-M7a** selftest 4/4 (incl. the synthetic MAJOR-2 fixture); **G-M7b** real WHGAP tree
  exit 0 — 0 FAIL, 2 WARN (exactly the two DOCUMENTED scoped-input exceptions on P4/P6,
  their composition rel text printed), 1 INFO (goal's legitimate AND-style composition);
  **G-M7c** in-memory patched P9 copies reproduce the R11 MAJOR-2 detection against the
  REAL module in both readings, and real-tree mutation probes show checks 3 and 6 bite.
  Report: [whgap_m7_checker_20260730.md](../../../../artifacts/whgap_m7_checker_20260730.md);
  logs + LF SHA256SUMS (8/8) under `artifacts/logs_whgap_m7_20260730/`.
  **Decision-layer adjudication of finding M7-F1 (material commission-vs-disk conflict,
  honestly reported not resolved by the executor):** while M7 was in flight, a parallel
  session (commit b9fa96b) added a PARTIAL §7.6 `check_lean()` to the shared
  `tools/proof_dag_check.py` (existence as errors; hash/orphan/route/import as v1-rollout
  WARNINGS; **the MAJOR-2 state-vs-content class still uncaught there**). Authority is
  hereby declared rather than folded (the shared file is co-edited by live se/ksum
  sessions and out of this session's commit scope): **for werner-holevo-gap,
  `tools/lean_dag_check.py` is the AUTHORITATIVE §7.6 gate** (run it in every closeout
  alongside proof_dag_check); the shared tool's check_lean is advisory v1 for this
  problem. Registered cross-session coordination items (append-only, NOT actioned here
  per scope discipline): harmonize/fold the two implementations; fix the shared tool's
  `LEAN_NON_NODE_BASENAMES` omission of "Model" (M7-F2 — currently a spurious WARNING on
  every WHGAP run of the shared tool). Advisory F3 (checks 4/7b-empty-rel undecidable
  textually — every emitted line says so) and F4 (promote 3b rather than edit the
  single-writer freeze tool) recorded.

- 2026-07-30 — **commission M7 dispatched** (rule 8a, obligation registered in the
  LEAN-1.1 entry below; origin R11 m7):
  [WHGAP_COMMISSION_M7_20260730.md](../../notes/WHGAP_COMMISSION_M7_20260730.md) — the
  §7.6 Lean↔DAG anti-drift checker `tools/lean_dag_check.py` (seven checks at assigned
  severities; hash normalization byte-matching the freeze tool; `--selftest` regression
  fixtures incl. the MAJOR-2 class; gates G-M7a selftest / G-M7b real-tree green /
  G-M7c reproduce the MAJOR-2 detection on a patched in-memory copy). Scope discipline
  bound to WHGAP-only paths; shared `tools/proof_dag_check.py` untouched.

- 2026-07-30 — **LEAN-1.1 repair applied and R11's conditional license DISCHARGED.** The
  Opus 5 repair executor applied every R11 source-side item (MAJOR-1 theorem move with
  corrected Lemma 6.1 cross-reference; m2 honest shadow-justification; m4 honest bridge
  shape hbridge : Δ ≤ Pone + lsd_devetak — the interface field is now consumed by checked
  content; m5 citation fix; m10-m13, m15 hygiene; m14 R11's satisfiability model shipped
  in-tree as WHGAP/Model.lean, IMPROVED to discharge the P14 bridge concretely with
  Pone = Δ). Clean rebuild exit 0 (3052 jobs); **54/54 declarations on exactly the three
  standard axioms; 0 sorry**; ledger regenerated under the single LF convention, 28/28
  verified (R11's own raw-byte ledger untouched and still verifying). P13's Claim
  refrozen after the m3 reconciliation note (new hash e0fa50f4...c977d8c3bd; --check 8/8).
  Decision-layer metadata corrections (MAJOR-2, m3, m8, m9) were applied before the
  repair dispatch and are recorded on the affected nodes. **With both MAJORs corrected
  exactly as R11 prescribed, R11's conditional statement applies: the Lean development is
  a faithful machine-checked mirror at the stated tiers; the lean: states as now recorded
  are licensed.** Epistemic tier of the build evidence remains NUMERICAL (a green build
  is a run); the §7.10 review itself is COMPLETED and cited. Repo hygiene: .gitattributes
  now pins all proof-dag/lean sources to LF (the fresh-checkout CRLF risk the repair
  executor flagged). Residual registered obligations: BGSW25 literature ingestion
  (R11 m6); the §7.6 anti-drift checker implementation (R11 m7).

- 2026-07-30 — **LEAN-1 landed (Opus 5 executor; commission
  [WHGAP_COMMISSION_LEAN1_20260730.md](../../notes/WHGAP_COMMISSION_LEAN1_20260730.md)):**
  DAG-mirroring lake project `proof-dag/lean/` (package whgapDag, Lean v4.31.0 + Mathlib
  v4.31.0 via the shared prebuilt cache; 12 modules; module names = node ids via
  «guillemet» identifiers; frozen Claims + SHA-256 embedded, re-checkable by
  `tools/whgap_lean_freeze_claims.py --check`). **Gates: G-L1 build exit 0 (clean
  recompile); G-L2 zero sorry, 44/44 top declarations on exactly
  [propext, Classical.choice, Quot.sound]; G-L3 29 SelfTest examples closed; G-L4 import
  graph = the propagating skeleton; G-L5 fidelity self-table written (the fresh §7.10
  review is the completion gate, owed).** Both MUST-LAND items unconditional: the P14
  flagship scalar core and THIS node's union-assembly composition theorem (a complete
  Lean proof of {x ∈ (0,1) : Q x = 0} = [1/2,1) ∪ S from the three child Claims).
  Executor findings recorded append-only: the commissioned self-test point (2/5, 1/3,
  2/5) is DEGENERATE for both forcing identities (0 = 0 — decision-layer commission
  defect; non-degenerate points added); Delta_lower_bound left conditional on
  hsq : s² ≤ f s (the only conditional item; nothing depends on it); all eleven
  commissioned identities verified correct by independent sympy re-derivation before
  formalization. Report:
  [whgap_lean_t1t2_20260730.md](../../../../artifacts/whgap_lean_t1t2_20260730.md);
  run artifacts `artifacts/logs_whgap_lean_20260730/` (build transcript, print_axioms,
  forbidden-construct scan, SHA256SUMS). Evidence tier NUMERICAL (`pending-review:` the
  §7.10 statement-fidelity review). Per-node `lean:` metadata + index column filled this
  session (§7.6).

- 2026-07-30 — **post-normalization audit of the main conclusions (decision layer,
  recomputed bottom-up under the new edge semantics).** All four headline theorems
  SURVIVE the composition-proof discipline; no status changes:
  1. **Q = P = 0 on [1/2, 1)** — P4 PROVED: composition = the R3-reviewed assembly note;
     input = P2's R2-PROVED-scope region subclaim (the scoped-input display resolves the
     naive node-level min, see P4's composition block). Rels displayed: HRSF22-via-ZW
     provenance; the closed-interval corollary at CERTIFIED\* (RK24 cite-only endpoint).
  2. **x_B = 1/2 exactly (phase classification)** — P6 PROVED: composition = paper §5,
     R5b; same scoped P2 input for the holding side.
  3. **Q > 0 on (0, 2/5)** — P3's imported theorem PROVED: composition = Thm 8.1 (R5d,
     unconditional), consuming only the reviewed subset of P9; the P3 node stays
     CERTIFIED\* for its residual exact-onset scope. Consistency: 2/5 > x_1, subsumes the
     R4 package.
  4. **{x : P = 0} = [1/2, 1) exactly** — P14 PROVED (R8 §5), leaf with interface-only
     dependencies; closed interval CERTIFIED\*.
  Goal arithmetic: min over the assembly inputs = capped by P13 (CONJECTURED) ⟹ G = OPEN,
  "resolved except on [2/5, 1/2)". **One residual review item surfaced by the audit:**
  the paper's Lemma 4.1 (x = 1 self-complementarity), which carries the closed-interval
  endpoint in the manuscript, has a written proof + external-review + machine-check
  provenance but NO dedicated fresh-instance rule-7 review of its own; the endpoint is
  independently covered by RK24 antidegradability (cite-only), so nothing rests solely on
  it, but it is the right first target if the closed-interval corollary is ever to lose
  its star. Recorded here per rule 8c.

- 2026-07-29 - P5 paper-exposition package completed for child
  `WHGAP.signed-lift-extension`: [human derivation artifact](../../../../artifacts/whgap_p5_derivation_package_20260729.md),
  [machine JSON](../../../../artifacts/logs_whgap_p5_20260729/derivation_package.json), exact
  logs, scripts, and SHA-256 metadata. Gates V1-V5 PASS, including all 729 entrywise checks,
  explicit integer spin/Gram data, forced-point eigenvalue bookkeeping, and the three rational
  certificate congruences. Paper evidence only: no node status changed and this GOAL remains
  OPEN under the existing full-boundary adjudication.

- 2026-07-28 — node registered at problem-scaffold creation (rule 8); no work commissioned yet.
- 2026-07-28 — decision-layer adjudication of the propagation conflict reported by the run-2
  executor (see `tmp/codex_whgap_p1_20260728_run2.log`, closing summary): mechanical OR-max over
  children would lift this GOAL to NUMERICAL once P1 reached NUMERICAL, but the goal claim —
  determine the FULL set {x : Q(Lambda_x) = 0} — is not decided by either registered child alone.
  P1 (antidegradability boundary x*) settles only the antidegradable side; the Zhu–Wang point
  x = 1/2 already shows Q = 0 strictly below the antidegradable region, and the Q > 0 onset at
  small x is registered in no child at all. P2 alone certifies points without determining the
  boundary. The children are contributory sub-steps, not alternative complete routes, so the
  "proved if ANY ONE child" premise of OR propagation fails; this GOAL's aggregation is AND-like
  over a decomposition that is not yet fully registered. Status remains OPEN. The commission's
  closeout line "WHGAP.goal recomputes (stays OPEN)" is thereby ratified with the correct reason.

## Evidence

- 2026-07-28 — manuscript draft v1 (8 pp., compiles clean):
  [paper/main.tex](../../paper/main.tex) / `paper/main.pdf` — "Zero quantum and private
  capacities across the noisy Werner–Holevo family: the signed-lift certificate extends from a
  point to the interval [1/2,1]". Incorporates the four external-review revision requirements
  (unnormalized-Choi convention stated; uniqueness scoped to the five-real-parameter ansatz;
  x=1 via the minimal self-complementary representation, Lemma 4.2; novelty framed as
  zero-capacity gap closure with the antidegradability threshold kept numerical). Author list
  left for the lead to finalize; AI-use statement included (Zhu–Wang style).
- 2026-07-28 — external cross-vendor hostile review (ChatGPT Pro, via lead): PASS, no fatal
  flaw; archived at `artifacts/whgap_external_review_chatgpt_20260728.md` with decision-layer
  verification of its three new items (closed-form spectrum; forcing vectors; x=1
  self-complementarity).

## Open obligations

P1 executed (NUMERICAL, pending-review) — next: complete the paired R1 review commission, then
decide the P2 commission. The formerly missing third sub-step is now registered as
[`WHGAP.qpositive-onset`](WHGAP.qpositive-onset.md) (P3, OPEN; rule 8b).

- 2026-08-01 — **LEAN-5 WP-H commissioned** (lead directive 「先搞lean 然后你去做其他问题」):
  the complex-Hermitian entropy glue — the last named Lean residue (Trust residual (b),
  charpoly → `vnEntropy` over ℂ) — plus the `hach` reduction to the achievability
  interface. Commission:
  [WHGAP_COMMISSION_LEAN5_P15B_20260801.md](../../notes/WHGAP_COMMISSION_LEAN5_P15B_20260801.md)
  (Track H; R15 review chained). In flight; executor cap NUMERICAL `pending-review:`.
- 2026-08-01 — **LEAN-5 WP-H executed (executor-authored, NUMERICAL `pending-review:`
  R15 in flight):** report
  [whgap_lean5_20260801.md](../../../../artifacts/whgap_lean5_20260801.md), logs
  `artifacts/logs_whgap_lean5_20260801/` (LF manifest, 14 rows). 13 new declarations
  (232 → 245, all on the three standard axioms; 0 sorry; freeze 8/8 UNCHANGED; all seven
  closeout gates green). New module `Support/EntropyC.lean`: the entropy layer over ℂ
  (`vnEntropyC`, the eigenvalue-multiset bridge via `ofReal` injectivity, Fin-indexed +
  list workhorses) and the payoff `IcScalar_eq_vnEntropyC_diff` (for 0 ≤ x ≤ 1, β² =
  x(1−x)/2: `IcScalar x ε = vnEntropyC(Λ_x(ρ_ε)) − vnEntropyC(Λ^c_x(ρ_ε))` for the
  Kraus-built §6 witness outputs); node module additions `exists_eps_entropy_pos`
  (quantifier-congruent, GH3 freeze-diff PASS) and `Claim_of_entropy_witness`. Two
  reported deviations, both strengthenings: D1 the list-form length hypothesis is
  DERIVED, not assumed (`charpolyC_list_length`); **D2 `hach'` is EQUIVALENT to `hach`
  (proved: `entropy_witness_eq_IcScalar`), not weaker — the honest gain is that the
  charpoly→entropy identification LEAVES the trust boundary; `hach'` carries exactly
  (i) the Stinespring identification of `LamCK` as *the* complement and (ii) LSD/Devetak
  achievability.** Sympy gates GH0–GH3 all PASS (worst residual 7.8e-62; ε = 1/2
  degenerate point recorded, GH2c). Environment note on record: the clean rebuild took
  three invocations for non-mathematical reasons (foreground cap; a Windows DLL-init
  process failure); third run uninterrupted EXIT=0.
- 2026-08-01 — **R15 review COMPLETED (fresh Opus instance, rule-7 complete):
  FINDINGS — 1 MAJOR + 6 minors, ZERO soundness defects; "with MAJOR-1 corrected,
  menu (A) applies in full."** Report:
  [whgap_r15_review_20260801.md](../../../../artifacts/whgap_r15_review_20260801.md);
  r15_ logs + `SHA256SUMS_r15.txt` in `artifacts/logs_whgap_lean5_20260801/`. The WP-H
  mathematics verified by THREE reviewer routes (own symbolic sympy from the Kraus set;
  Faddeev–LeVerrier charpoly + polyroots; mp.eighe) at 8 rational points incl. exact
  degeneracy, near-degeneracy (gap 9.6e-13), endpoints, and an in-strip negative
  control; hypotheses shown LOAD-BEARING (dropping hβ falsifies the E-charpoly;
  discE < 0 reachable off [0,1]). D1 confirmed a strengthening; **D2 confirmed
  CORRECT — R15 proved `R15_hach_iff_hach'` in both directions out-of-tree; the
  commission's own "genuinely weaker" framing was the wrong text, disk wins.**
  Reviewer reproduced all §7.10 gates from scratch (uninterrupted rebuild, 20 Built /
  0 Replayed, superseding the executor's environment-interrupted transcript; 245
  declarations axioms-clean; freeze 8/8 unchanged). MAJOR-1 = stale under-claim in
  `Support/Channel.lean` item 4 (three sentences now FALSE in the honest-note
  direction — same defect class as R13 MAJOR-1, reversed); m1/m2/m4/m5 = adjacent
  stale-wording items; m3 = fold R15's satisfiability instances into `Model.lean`
  §3c; m6 = decision-layer metadata (applied same day: goal `lean.build` pointer,
  NODE_INDEX P9 Lean column). **LEAN-5.1 repair pass commissioned same day** (apply
  MAJOR-1 + m1–m5, rebuild, full gate chain; node files excluded — single-writer).
- 2026-08-01 — **LEAN-5.1 COMPLETED (all R15 findings applied, all gates green) ⟹ R15's
  conditional license is DISCHARGED: "with MAJOR-1 corrected, menu (A) applies in
  full."** MAJOR-1 + m1–m5 applied append-only (originals kept as history, dated
  amendments; Model.lean §3c carries R15's satisfiability instances WITH credit,
  transcribed from `r15_satisfiability.txt`, incl. the two-directional
  `R15_hach_iff_hach'` for an arbitrary interface). Totals: **248 declarations
  (245 → 248), 0 outside the three standard axioms; freeze 8/8 byte-identical;
  uninterrupted clean rebuild EXIT=0 (20 Built / 0 Replayed); lean_dag_check 0 FAIL.**
  Report section "LEAN-5.1" appended to
  [whgap_lean5_20260801.md](../../../../artifacts/whgap_lean5_20260801.md); wph51_ logs
  + `SHA256SUMS_lean51.txt` additive. **Trust residual (b) is now DISCHARGED in every
  place that displays it** (Trust, Channel item 4, EntropyC, IcScalar pointer, README).
  Paper Verification statement updated to match (trust boundary now: coding-theorem
  interfaces + ensemble-validity side conditions + the Stinespring identification of the
  complement; recompiles clean, 19pp). Commission-design lesson BANKED (R15/LEAN-5.1
  flag): a commission touching a residual display must enumerate EVERY file carrying
  that display, not just the trust file — added to the standing checklist for future
  Lean commissions.

## Status history

- 2026-07-28 — created OPEN (problem scaffold, lead directive; carried over from the same-day field-level scaffold).

## Lean

```yaml
lean:
  module: "WHGAP.goal"
  file: "channel-capacity/werner-holevo-gap/proof-dag/lean/WHGAP/goal.lean"
  claim: "Claim"
  composition: "composition"
  state: "composition-checked"
  tier: "T1"
  rel: ["P13 unresolved", "hS : S ⊆ [2/5,1/2)"]
  build: "artifacts/logs_whgap_lean5_20260801/"  # LEAN-5 batch (R15 m6); earlier evidence dirs retained
  claim_hash: "sha256:f3a95693d4b0de4409d1fe4267e436bf3fe419f84b8a5fc2ebc6e06d6939ce99"
  synced: "2026-08-01 (post LEAN-3.2, R13 m2)"
```

Mechanization notes (LEAN-1, 2026-07-30, NUMERICAL `pending-review:` — the §7.10
statement-fidelity review is the completion gate): the union-assembly composition theorem is a COMPLETE Lean proof from the three tier-1 child Claims; Q is an interface field; the x = 1 endpoint is deliberately excluded (CERTIFIED* on disk).
Report: [whgap_lean_t1t2_20260730.md](../../../../artifacts/whgap_lean_t1t2_20260730.md)
(G-L5 fidelity self-table row for this node; granularity losses stated there).

