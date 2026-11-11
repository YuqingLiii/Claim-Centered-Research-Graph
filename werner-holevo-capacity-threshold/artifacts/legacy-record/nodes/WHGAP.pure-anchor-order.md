---
id: "WHGAP.pure-anchor-order"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.pure-anchor-order.md"
aliases: ["P15"]
kind: LEAF
role: proof
status: OPEN
status_source: "registered 2026-07-30 (rule 8b) as the first SURVIVING restricted-order candidate found by P12-A; both the executor and R8 recommend the node"
disposition: null
parents: []
children: []
related: ["WHGAP.goal", "WHGAP.restricted-order", "WHGAP.more-capable-route", "WHGAP.no-ascent-hierarchy", "WHGAP.private-boundary"]
---

# WHGAP.pure-anchor-order — Pure-first-argument domination P_b2: does it hold on the strip, and does it tensorize?

## Claim

Define the **pure-anchor order** P_b2: relative-entropy domination restricted to pairs
(P_psi, sigma) whose FIRST argument is a pure state (sigma arbitrary):

  G(psi, sigma) := D( Lambda^c(P_psi) || Lambda^c(sigma) ) - D( Lambda(P_psi) || Lambda(sigma) ) >= 0
  for all pure psi and all states sigma  (plus references, for the complete version).

Two open questions: **(i)** does P_b2 hold for Lambda_x at some x in [2/5, 1/2)?
**(ii)** does P_b2 tensorize? A YES to both would give Q(Lambda_x) = 0 there by a
genuinely new mechanism. **[OPEN]**

## Role in DAG

P12-A's most interesting outcome: it **refutes the decision layer's "no room" dichotomy**
(design memo §3). The memo argued that every ensemble class either has thickness around
the pure states — and is then FALSE below 1/2 because it implies P^{(1)} = 0
([[WHGAP.private-boundary]]) — or is the exactly-pure class, which is
Q^{(1)} = 0 = the additivity problem ([[WHGAP.more-capable-route]]). P_b2 escapes the
dichotomy: its SECOND argument ranges over mixed states (so it is strictly more than the
pure class in content), yet it does NOT contain the private-capacity witness pair, whose
BOTH members are mixed. It therefore survives the unconditional no-go.

## Current status

OPEN. Known so far (all executor-authored, `pending-review:` except where noted):
- P_b2 IMPLIES Q^{(1)} = 0 (take sigma = the purification anchor);
- P_b2 is DEAD on (0, 2/5) — it must be, since Q > 0 is PROVED there;
- P_b2 is numerically VIOLATED at x = 2/5 itself (R8 reproduced this with an independent
  optimizer at 50 dps: G = -0.1224208841, min spec Lambda(sigma) = 2.95e-2, so it is NOT
  a support-threshold artifact) — and the violation is NON-PERTURBATIVE;
- P_b2 SURVIVES a bounded search at x = 9/20 and 49/100 (strip points). R8 m1: the
  reported positive minima are optimizer stalls; the honest reading is "no negative value
  found; inf G = 0, approached at sigma -> P_psi".
- 2026-08-01 (P15-B, NUMERICAL `pending-review:` R16): the death point is BRACKETED —
  x_d ∈ [687/1600, 43/100] (width 6.25e-4) — with an EXACT-FORM CANDIDATE: near x_d the
  global minimizer is the orthocomplement pair (ψ real, σ = (1−P_ψ)/2), on whose stratum
  G*(x) = (1−2x)ln x + x ln(2−x) − (1−x)ln(1−x) − (1−x)ln 2, simple root
  x_d = 0.42966287456589232412… inside the search bracket (a candidate THIRD exact
  threshold besides 2/5 and 1/2; stratum global-optimality checked at 5 points only).
  Candidate domain sharpens to (x_d, 1/2). First tensorization test: BOUNDED NULL —
  2-copy P_b2 survives at three surviving-side points, and the product-σ case is
  EXACTLY equivalent to 1-copy (W₂ additivity), so only correlated σ can ever break it.
- 2026-08-01 (R16 applied — LICENSE A): the previous bullet is REVIEWED standing
  knowledge with these upgrades: **G* is a reviewer-verified identity (U1)**; bracket
  tightened to **[0.42966287, 0.4297]** (width 3.7e-6, U4); exact rational endpoint
  certificate on the violation side (U3); the 41/100 2-copy minimum is a bound
  (≤ −0.1363906031, m5). **Violation side now ANALYTIC pending ONE review:** the
  decision-layer monotonicity lemma
  ([WHGAP_P15B_MONOTONICITY_LEMMA_20260801.md](../../notes/WHGAP_P15B_MONOTONICITY_LEMMA_20260801.md),
  G*′ ≥ ln 6 + 2/3 on (0,1/2], unique simple zero) gives, with the U1 identity:
  **P_b2 fails at EVERY x < x_d** (derived, `pending-review:`). Upper side stays
  numerical: x_death = x_d ⟺ F1 (stratum global minimality above x_d) — the remaining
  proof obligation for exact-threshold status. No Q-consequence (R8 MAJOR-3 standing).

## Dependencies

[[WHGAP.private-boundary]] (why the other classes die); [[WHGAP.no-ascent-hierarchy]] (P13
weight operator — R8's first-order law below); [[WHGAP.qpositive-onset]] (Q > 0 on
(0,2/5) forces P_b2 to fail there); HRSF22 (tensorization technology).

## Work record

- 2026-07-30 — node registered (rule 8b) by the decision layer while applying the R8
  review, on the joint recommendation of the P12-A executor (which discovered the class
  while building the S3 no-go table) and R8 (which independently endorsed registering it
  and supplied the first-order law below). No commission yet: obligation 1 (strictness)
  should be settled before spending compute on obligation 2 or 3.
- 2026-07-30 — commission P15-A authored and dispatched (Track A of
  [WHGAP_COMMISSION_P15A_P16A_20260730.md](../../notes/WHGAP_COMMISSION_P15A_P16A_20260730.md))
  — the decomposition identity Σ_u p_u G(ψ_u, σ) = −I_c(σ), the decisive x = 2/5 test, and
  the strip re-scan. The agent died on the session usage limit AT CLOSEOUT — the
  structured return and the SHA manifest are missing, **but the note and all run logs are
  complete on disk** (initial "nothing was learned" record CORRECTED 2026-07-30 same day,
  after the commit surfaced the orphaned files; decision layer generated the post-hoc
  manifest `artifacts/logs_whgap_p15a_20260730/SHA256SUMS_posthoc_decision_layer.txt`
  over the untouched outputs, 24 entries — closeout-discipline defect of the run,
  flagged for R9).
- 2026-07-30 — **P15-A headline (executor-authored, `pending-review:` — NUMERICAL cap,
  R9 NOT yet run):** note
  [WHGAP_P15A_STRICTNESS_20260730.md](../../notes/WHGAP_P15A_STRICTNESS_20260730.md)
  (638 lines, all gates executed). **Gate G-A0: strictness demonstrated at x = 2/5** —
  at the violating pair, G(ψ*, σ*) = −0.12242088416... (60 dps; not a support artifact:
  min spec Λ(σ*) = 2.95e-2, min spec Λ^c(σ*) = 2.15e-2) while
  **I_c(σ*) = −0.023524168... < 0** and the local max of I_c near σ* over 120 restarts is
  0 (7.66e-15). **G-A+ NOT triggered**: no new Q witness at any probed x ≥ 2/5 — the
  onset conjecture [[WHGAP.onset-two-fifths]] SURVIVES this designed falsification
  attempt. If R9 licenses: P_b2 is strictly stronger than Q^(1) = 0 at 2/5 (the R8
  MAJOR-3 gap closes in the strict direction), upgrading this node to a genuine
  new-mechanism candidate. Lead directive 2026-07-30 stopped the line before R9;
  **review debt: R9 on the complete P15-A package** when/if resumed.
- 2026-08-01 — **P15-B executed (executor-authored, `pending-review:` — NUMERICAL cap,
  R16 commissioned):** note
  [WHGAP_P15B_DEATHPOINT_20260801.md](../../notes/WHGAP_P15B_DEATHPOINT_20260801.md),
  logs `artifacts/logs_whgap_p15b_20260801/` (LF manifest, 19/19 verified), tools
  `tools/whgap_p15b_{core,phase0,phase1,stratum,fullrank,phase2,phase2b}.py`. All three
  pre-registered gates PASS; local compute only; commission Track P15B of
  [WHGAP_COMMISSION_LEAN5_P15B_20260801.md](../../notes/WHGAP_COMMISSION_LEAN5_P15B_20260801.md).
  Headlines (all NUMERICAL): (i) **instrument reduction** — for pure anchors
  G(ψ,σ) = ⟨ψ|W(σ)|ψ⟩ is a quadratic form in the anchor, so min over ALL pure ψ =
  λ_min(W(σ)) exactly (anchor solved, not searched; every value cross-checked against the
  definitional 4-term G, worst diff 4.8e-15); (ii) **death point bracketed**
  [687/1600, 43/100], 7 mpmath-60dps violation certificates up to 687/1600, calibrated
  bounded null at 43/100 (0/200 restarts, power statement in the note); Phase-0
  reproduced R9's 41/100 violation to every printed digit; (iii) **exact-form candidate**
  x_d = root of the orthocomplement-stratum value G*(x) (see Current status; checked to
  7.8e-62 against the definition on-stratum); (iv) **tensorization: bounded null + the
  structural fact W₂(σ₁⊗σ₂) = W(σ₁)⊗1 + 1⊗W(σ₂)** (product-σ case ⟺ 1-copy; violations
  require correlated σ); unexpected: violation DEPTH is superadditive at 41/100
  (min G₂ = −0.13639 < 2·min G₁ = −0.13607) — the functional is non-additive even where
  the property tensorized. Honest coverage limits recorded: 2-copy null = 80/32 restarts
  in 162 real dims; the 1-copy lesson (violations near x_d live on the RANK-2 boundary)
  means the boundary-restricted 2-copy search (follow-up F2) is the most likely hiding
  place and was NOT run (batch 1 of ≤ 2). Follow-ups F1–F5 registered in the note. No
  Q-consequence claimed (R8 MAJOR-3 wording respected). One unresolved wrinkle recorded:
  at 41/100 the global min sits 2.4e-5 below the stratum value at a complex anchor
  (τ = 0.918); below 0.415 only, does not affect x_d.

## Evidence

- 2026-07-30 — **R8 reviewer-authored theorem (NUMERICAL/derived, own verification 6/6
  points):** the first-order law
    G((1-s) P_chi + s phi) = s ( w_E - w_B )(chi, phi) + o(s),
  i.e. **P_b2's first-order content is exactly the P13 weight operator**
  ([[WHGAP.no-ascent-hierarchy]], R5c/R6-PROVED closed forms). Two consequences recorded:
  (a) the strip null of P_b2 at first order is now explained by a REVIEWED theorem rather
  than by an optimizer; (b) the x = 2/5 violation is non-perturbative, since at first
  order nothing happens there.
- 2026-07-30 — executor probe data and R8's independent reruns:
  [WHGAP_P12A_PRIVATE_BOUNDARY_20260730.md](../../notes/WHGAP_P12A_PRIVATE_BOUNDARY_20260730.md)
  §7.2-7.3, [whgap_r8_review_20260730.md](../../../../artifacts/whgap_r8_review_20260730.md)
  §3; logs `artifacts/logs_whgap_p12a_20260730/`.

## Adversarial reviews

- 2026-08-01 — **R16 (fresh Opus instance, rule-7 complete, review of P15-B):
  LICENSE A — 0 MAJOR, 6 minors (all applied in the note's dated R16-application
  section + the DAG-doc outline fix), 4 reviewer upgrades.** Report:
  [whgap_r16_review_20260801.md](../../../../artifacts/whgap_r16_review_20260801.md);
  r16_ logs + `SHA256SUMS_r16.txt` in `artifacts/logs_whgap_p15b_20260801/`. Anchoring
  ban honored (quadratic-form reduction re-derived from the claim alone before opening
  the executor's code; own optimizer, own 2-copy code, own root-finders). Verified:
  the reduction W = Λ†(log Λ(σ)) − (Λ^c)†(log Λ^c(σ)) (definitional-vs-reduced G to
  6.6e-61); **G* at FORMULA level (symbolic residual exactly 0)** + O(3)-covariance
  check; x_d to 40 digits by two root-finders; both bracket endpoints reproduced with
  own protocol + independent hit-rate scan (power claim does NOT outrun the
  instrument); 5/7 certificates recomputed (no support artifact); W₂ additivity proved
  by own route; superadditivity reproduced (deeper: min G₂ ≤ −0.1363906031).
  Upgrades: **U1** G* = reviewer-verified identity; **U2** violation side ANALYTIC
  modulo a monotonicity lemma (supplied same day by the decision layer, pending-review);
  **U3** exact rational endpoint certificate (ψ = e₁, σ = diag(0,1/2,1/2),
  x = 687/1600); **U4** tightened bracket **[0.42966287, 0.4297]** (width 3.7e-6),
  global minimum tracking G* to 5 digits at 4.6e-9 below x_d. The P15-B
  `pending-review:` markers are DISCHARGED at the reviewed scope.
- 2026-08-01 — **R9 (fresh Opus 5 instance, rule-7 complete, the owed review of P15-A):
  FINDINGS — 2 MAJOR + 6 minors; the core results CONFIRMED, the strip claim
  CORRECTED.** Anchoring ban honored (own derivation of the decomposition identity;
  own 200-restart optimizer at x = 2/5 run to completion before reading the note).
  **CONFIRMED:** the decomposition identity Σ p_u G(ψ_u,σ) = −I_c(σ) is correct and
  independently re-derived (R9's route needs NO faithfulness hypothesis — support
  inclusion is automatic; 60-dps residual 6.6e-61 across multiple decompositions of the
  SAME σ — the decomposition-independence sharp part verified); the x = 2/5 violating
  pair reproduced from scratch (G = −0.12242088..., not a support artifact, ψ* 99.6% in
  ker σ*); **G-A0 CONFIRMED: I_c(σ*) = −0.023524... < 0 with global I_c max at 2/5
  attained only on pure states — strictness of P_b2 over {Q^(1)=0} is DEMONSTRATED at
  x = 2/5, reviewed** (the R8 MAJOR-3 gap closes in the strict direction, pointwise);
  G-A+ NOT triggered (no new Q witness — [[WHGAP.onset-two-fifths]] survives); G-Acal
  clean; A2.5's five non-claims accurate.
  **MAJOR 1:** A3.3's "strictness CRITERION (proved)" is FALSE as stated (the
  spread-vs-δ clause is a non-sequitur; the note's own probe log is a counterexample) —
  the '(proved)' label is struck and the criterion must NOT be registered as a node;
  R9 supplies the correct replacement (if some p_v G_v > δ then some term is negative).
  **MAJOR 2 (decision-relevant):** the note's §A4.3 strip "bounded null" is CONTRADICTED
  by its own archived data — **P_b2 is VIOLATED at x = 41/100 INSIDE the strip**
  (note's own log: inf G = −6.803e-2, 97.1% of restarts negative; R9's independent scan
  agrees to 9 digits, plus interior full-rank violators with G < 0 while −I_c(σ) > 0).
  The genuine nulls at 9/20 and 49/100 are confirmed (corner stalls at fidelity 1).
  Consequence: **P_b2 is numerically DEAD at and below ≈ 0.41; the candidate's possible
  domain narrows to roughly (0.41, 1/2), and the new frontier question is where in
  (0.41, 0.45) it dies.** Minors: value-vs-search routing (m1, with the missing value
  supplied), an overstated "far from pure" description (m2), optimizer-stall caveat
  placement (m3), the note's FALSE claim of a manifest verification that never happened
  (m4 — struck under rule 1; integrity itself fine, 24/24 post-hoc), missing JSONs from
  the early termination (m5), commission filename conflict resolved to the later one
  (m6). Report:
  [whgap_r9_review_20260801.md](../../../../artifacts/whgap_r9_review_20260801.md).

## Post-R9 status application (decision layer, 2026-08-01)

- The pending-review markers on the P15-A results are DISCHARGED at the reviewed scope:
  the decomposition identity and the x = 2/5 strictness demonstration are now
  review-backed (CERTIFIED\*-grade content on this node; the node itself stays OPEN —
  its two questions are unresolved).
- The Current-status bullet "P_b2 SURVIVES a bounded search at x = 9/20 and 49/100" is
  RETAINED but the implied strip-wide reading is WITHDRAWN: P_b2 fails at 2/5 AND at
  41/100 (reviewed). Open question (ii) sharpens to: does P_b2 hold on (≈0.41, 1/2),
  and where exactly does it die in (0.41, 0.45)?
- A3.3's criterion is NOT registered (R9 MAJOR 1); the note's §5 recommendation to
  register it is dead.

- 2026-07-30 — R8 **MAJOR 3 applies to this node's framing:** the executor's claim that
  "P_b2 is STRICTLY STRONGER than Q^{(1)} = 0" is **asserted without proof**, and it is
  load-bearing — if P_b2 were EQUIVALENT to Q^{(1)} = 0, the reproduced x = 2/5 violation
  would be a statement that Q^{(1)}(Lambda_{2/5}) > 0. R8's first-order law sharpens the
  concern: at first order the P_b2-violation condition and the Q^{(1)}-ascent condition
  are literally the same function w_B - w_E, so **no separation is in evidence**; the only
  witnessed gap is the single non-perturbative x = 2/5 point. Adopted wording (decision
  layer): *the converse implication (Q^{(1)} = 0 => P_b2) is NOT established, hence a
  violation of P_b2 carries NO Q-consequence*; "sits strictly between more capable and
  less noisy" is downgraded to "implies Q^{(1)} = 0; strictness OPEN"; "dead at 2/5" is
  NUMERICAL (below 2/5 it rests on the PROVED Q > 0).

## Open obligations

1. **Strictness** (the R8 MAJOR-3 item): prove or refute P_b2 =/= {Q^{(1)} = 0}. If they
   coincide, this node collapses into [[WHGAP.more-capable-route]] and the x = 2/5 datum
   becomes a Q-statement that must be reconciled with the PROVED Q > 0 on (0,2/5) and the
   PROVED first-order exhaustion at 2/5 — a strong consistency test in its own right.
2. **Does it hold on the strip?** The current evidence is a bounded search at two points
   with inf G = 0 approached degenerately. Needs a structured search (the P13 stratum
   machinery applies: R8's first-order law reduces the first-order layer to the already
   PROVED weight operator, so any violation must be non-perturbative — search accordingly).
3. **Tensorization** — the decisive question. The pure-first-argument class is closed
   under tensor products of its own members (P_psi ⊗ P_chi is pure), which is exactly the
   structure the HRSF22 hybrid induction consumes; whether the induction closes with the
   SECOND arguments unrestricted is the technical crux.
4. **P15-B commissioned (2026-08-01, decision layer; lead frontier directive):**
   death-point localization — bracket x_d in (0.41, 0.45) to width ≤ 5e-3 with a
   calibrated optimizer (Phase-0 gate = reproduce the R9 x = 41/100 violation) — plus a
   2-copy tensorization probe at two surviving-side points (the first numerical test of
   obligation 3). Commission:
   [WHGAP_COMMISSION_LEAN5_P15B_20260801.md](../../notes/WHGAP_COMMISSION_LEAN5_P15B_20260801.md)
   (Track P15B). — **EXECUTED same day, all gates PASS** (see Work record); R16 review
   commissioned ([WHGAP_COMMISSION_R16_20260801.md](../../notes/WHGAP_COMMISSION_R16_20260801.md));
   registered follow-ups live in the note (F2 boundary-restricted 2-copy search =
   highest-value next test; F1 stratum-minimality proof would make x_d an EXACT analytic
   threshold — a proof task for the decision layer). — **R16 COMPLETED same day:
   LICENSE A** (see Adversarial reviews; minors applied in the note's dated section).
5. **Review the monotonicity-lemma note** (decision-layer authored 2026-08-01,
   `pending-review:` — rule 6): one fresh-instance rule-7 review of
   [WHGAP_P15B_MONOTONICITY_LEMMA_20260801.md](../../notes/WHGAP_P15B_MONOTONICITY_LEMMA_20260801.md).
   If licensed, "P_b2 fails at every x < x_d" becomes reviewed-analytic and obligation 2
   collapses to the interval [x_d, 1/2).

## Status history

- 2026-07-30 — created OPEN (rule 8b; registered by the decision layer on the joint
  recommendation of the P12-A executor and the R8 review).

## Lean

`lean: none` — OPEN candidate; P15-A pending review (R9) before any mechanization. (Recorded per DAG_PROTOCOL §7.4: silence is invalid; added 2026-07-30 applying R11 m9.)

