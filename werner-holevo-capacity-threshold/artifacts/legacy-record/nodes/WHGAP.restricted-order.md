---
id: "WHGAP.restricted-order"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.restricted-order.md"
aliases: ["P12"]
kind: LEAF
role: proof
status: OPEN
status_source: "registered-2026-07-29 (lead directive: the genuinely-new-mechanism target)"
disposition: null
parents: []
children: []
related: ["WHGAP.goal", "WHGAP.order-boundary", "WHGAP.relaxed-lift", "WHGAP.order-converse", "WHGAP.more-capable-route"]
---

# WHGAP.restricted-order — A tensorizing RESTRICTED less-noisy order: the new-mechanism target

## Claim

Construct a partial order strictly weaker than complete relative-entropy domination that
(i) still tensorizes (or self-tensorizes along the diagonal N vs N^c), and (ii) controls
ONLY the input pairs the capacity proofs actually consume — for Q the purification pairs
(psi_RA, psi_R ⊗ rho_A); for P the ensemble pairs (rho_u, rho_bar) — and determine whether
it holds for Lambda_x at some x < 1/2. **[OPEN]**

## Role in DAG

Registered 2026-07-29 on the lead's directive after the analytic necessity result closed
every cRE-implying route below 1/2 (see [[WHGAP.order-boundary]], [[WHGAP.relaxed-lift]]).
This is tier-3 originality territory (a NEW zero-capacity mechanism, not an application of
Zhu–Wang's): the ZW hierarchy complete-less-noisy ⟹ all-block domination ⟹ P=Q=0 uses only
one-way implications; the last two steps need far less than the full cRE quantifier. The
research object: identify the minimal tensor-stable quantifier class.

## Current status

OPEN. Design considerations recorded at registration (decision layer):
- The purification pairs (psi_RA, psi_R ⊗ rho_A) are NOT closed under tensoring with an
  arbitrary second admissible pair — the tensor of two purification pairs is again a
  purification pair for the product input, which is promising for a SELF-tensorization
  lemma along the HRSF22 hybrid proof line (their Lemma 3.1's two-pair specialization);
  the danger is regularized-order territory (see [[WHGAP.more-capable-route]] — for
  complement pairs the fully-restricted "coherent-information order" IS Q^{(1)}=0 and its
  tensorization is the regularization problem). The candidate must sit STRICTLY between:
  restricted enough to survive below 1/2, structured enough that the hybrid tensorization
  induction closes. First concrete candidate to test: domination restricted to pairs
  (rho, sigma) with sigma = psi_R ⊗ rho_A ranging over PRODUCT-marginal anchors only
  ("anchored less-noisy"), which contains all pairs the coherent-information step uses and
  is closed under products of anchors.
- Falsification target for any candidate order O: it must FAIL at x where Q > 0 is proved
  (x < x_1), else it cannot imply Q = 0.
- Cross-check resource: the P6 witness family shows WHICH (rho, X) pairs break full cBKM
  below 1/2 (spin-2 directions at near-pure REAL-stratum anchors); a viable restricted
  order must EXCLUDE those pairs while keeping the purification pairs.

## Dependencies

HRSF22 (hybrid tensorization proof line); ZW (capacity-consequence corollaries);
P6/P6b (which pairs break below 1/2); P3/P9b (strip single-letter landscape).

## Work record

- 2026-07-29 — node registered (rule 8b) on lead directive; no commission yet (theory-first:
  the decision layer must formalize the candidate order and its tensorization lemma sketch
  before any executor scan).
- 2026-07-30 — **decision-layer design memo written** (discharging this node's standing
  theory-first obligation):
  [WHGAP_DESIGN_MEMO_P12_20260730.md](../../notes/WHGAP_DESIGN_MEMO_P12_20260730.md).
  Its three claims (ALL decision-layer authorship — they license nothing and are
  commissioned for independent verification or refutation):
  1. the reviewed necessity witness uses a TRIVIAL reference, so it refutes plain
     relative-entropy domination, which equals the less-noisy order (two-point ensemble
     limit) — hence P^{(1)}(Lambda_x) > 0 for x < 1/2 and, by superadditivity,
     **P(Lambda_x) > 0**, giving {x : P = 0} = [1/2, 1] EXACTLY;
  2. an ELEMENTARY closed form makes this perturbation-theory-free: for the symmetric
     ensemble {1/2 : rho_eps ± tX} both outputs commute with the base and
     chi_B = b f(u/b), chi_E = e f(v/e) with f(s) = (1+s)log(1+s) + (1−s)log(1−s),
     b = x/2 + (1−3x/2)eps, u = t(1−3x/2)/sqrt2, e = (x/2)(1−eps), v = tx/(2 sqrt2);
  3. the **purity knob** decides P12: pure-state ensembles give
     chi_B − chi_E = Ic(rho_bar) (isospectral pure outputs) so the pure class IS
     Q^{(1)} = 0 = more capable, while ANY class with thickness around the pure states
     contains the witness ensembles (rho_eps ± tX lies within O(eps) of |0><0|, and every
     eps < eps_c(x) works) and is therefore FALSE below 1/2. In particular this node's own
     first candidate ("anchored less-noisy") is dead: its trivial-reference specialization
     contains the ensemble pairs. **Consequence if verified: the restricted-order program
     has no room on this family** — the frontier relocates to [[WHGAP.order-converse]]
     (covariance collapse) and to genuine additivity technology.
- 2026-07-30 — commission P12-A authored (rule 8a, this node cited) and dispatched as an
  executor -> fresh-reviewer pipeline:
  [WHGAP_COMMISSION_P12A_20260730.md](../../notes/WHGAP_COMMISSION_P12A_20260730.md).
  S0 literature check (is the P-boundary result new for this family? is the
  less-noisy/RE equivalence in HRSF22/Watanabe?); S1 the theorem with exact rational
  certificates and an explicit (eps,t) threshold; S2 the purity-knob hierarchy; S3 the
  no-go map over candidate order classes. HARD calibration gate first: Delta <= 0 at
  x in {11/20, 3/5} where P = 0 is PROVED. The memo is explicitly labelled
  NOT-TO-BE-TRUSTED input; refuting it is a first-class outcome.

## Evidence

- 2026-07-30 — **P12-A executed (outcome THEOREM) + R8 review (FINDINGS: 3 MAJOR, all
  scope/quantifier; the mathematical core CONFIRMED IN FULL by an independent route).**
  Note [WHGAP_P12A_PRIVATE_BOUNDARY_20260730.md](../../notes/WHGAP_P12A_PRIVATE_BOUNDARY_20260730.md);
  review [whgap_r8_review_20260730.md](../../../../artifacts/whgap_r8_review_20260730.md);
  logs `artifacts/logs_whgap_p12a_20260730/` (SHA256SUMS verified 15/15).

  **(1) The unconditional engine, now PROVED and carried on its own node
  [[WHGAP.private-boundary]]:** P^{(1)}(Lambda_x) > 0 for every x < 1/2 with an exact
  closed-form value. Consequence for this node: **any order class whose conclusion is
  P^{(1)} = 0 is not merely unprovable below 1/2 — its conclusion is FALSE there.**
  DEAD by this argument (executor's table, R8-verified rows a1-a4, a6, b1, c, d): less
  noisy; complete less noisy; cRE; cBKM; any signed-lift CP-defect certificate;
  alpha >= 1 sandwiched-Rényi orders (R8 recomputed these from matrix powers, independent
  of the note's closed-form route, 40 cases); and **this node's own first candidate,
  "anchored less-noisy"** — its trivial-reference specialization contains the ensemble
  pairs, exactly as the design memo predicted.

  **(2) The purity-knob hierarchy, PROVED (R8 §5 item 3):** for PURE-state ensembles
  chi_B - chi_E = Ic(rho_bar) exactly (isospectral pure outputs), so the pure class IS
  Q^{(1)} = 0 = more capable; for all ensembles the sup is P^{(1)}. The knob therefore
  interpolates exactly between [[WHGAP.more-capable-route]] and [[WHGAP.private-boundary]].

  **(3) The decision layer's "no room" DICHOTOMY IS REFUTED as non-exhaustive** — by the
  executor (who found a surviving class) and independently by R8 (MAJOR 1, who found a
  second one). The memo's argument was that thickness around the pure states forces the
  class to contain the witness; that inference is invalid, because the witness is ONE
  specific family of pairs, not all nearby pairs. Two survivors, both now registered:
   - [[WHGAP.pure-anchor-order]] (P15) — pure FIRST argument, arbitrary second: contains
     mixed states yet not the witness (whose both members are mixed); implies Q^{(1)} = 0;
     dead on (0,2/5) as required; survives a bounded search at 9/20 and 49/100;
   - [[WHGAP.direction-restricted-order]] (P16) — exclude the spin-2 breaking directions
     (this node's OWN second candidate): R8 MAJOR 1 shows the no-go quantifier never
     reaches it; it was wrongly declared dead by the note's §8 headline.

## Decision-layer adjudication (2026-07-30, applying R8)

- **The no-go stands only at the row-(d) quantifier**, i.e. for classes containing ALL
  pairs of states within trace distance delta of a pure state (any delta > 0), and for the
  explicitly tabulated classes. The note's §8 headline ("every class containing A PAIR of
  mixed states arbitrarily close to a pure state") is **over-claimed and is not adopted**
  (R8 MAJOR 1). Direction-restricted classes are UNDECIDED, not dead.
- **No Q-consequence may be drawn from a P_b2 violation** (R8 MAJOR 3): "P_b2 is strictly
  stronger than Q^{(1)} = 0" is unproven and load-bearing; R8's first-order law shows the
  two conditions coincide at first order, so no separation is in evidence. Wording fixed
  on [[WHGAP.pure-anchor-order]].
- **Interval scope** (R8 MAJOR 2): {x : P = 0} = [1/2,1) at PROVED, closed interval at
  CERTIFIED\*, matching P4's disk scope. Applied on [[WHGAP.private-boundary]].
- **Decision-layer authorship defect recorded:** the design memo transcribed the paper's
  gap (5.3) with the wrong orientation (leading factor must carry (1-2x)); benign because
  the executor re-derived it, but it is exactly why the memo was dispatched as
  untrustworthy input.

## Adversarial reviews

None yet.

## Open obligations

The design-memo and first-feasibility obligations are DISCHARGED. This node's remaining
content is now split:
1. the **no-go half is settled** at the corrected scope (see Evidence + adjudication);
2. the **construction half stays OPEN**, and its live candidates are exactly the two
   registered children-in-spirit [[WHGAP.pure-anchor-order]] (P15, the more promising —
   it has data) and [[WHGAP.direction-restricted-order]] (P16, needs a theory decision
   first). Both must FAIL on (0, 2/5) to be viable, and both stand or fall on
   TENSORIZATION, which nothing here addresses.
Adjacent live frontier unchanged: [[WHGAP.order-converse]] (P11, covariance collapse) and
genuine Ic-additivity technology ([[WHGAP.more-capable-route]], PARKED).

## Status history

- 2026-07-29 — created OPEN (lead-directed registration).
- 2026-07-30 — status stays OPEN (the construction question is neither achieved nor
  refuted), but the node's content is now largely settled: the unconditional no-go is
  PROVED for every P^{(1)}-implying class, the purity-knob hierarchy is PROVED, the
  node's own first candidate is DEAD, its second candidate is registered as P16, and a
  new surviving candidate P15 was discovered. Cite:
  `artifacts/whgap_r8_review_20260730.md` §5.

## Lean

`lean: none` — its proved content (no-go engine) is mechanized on WHGAP.private-boundary; the construction half is OPEN. (Recorded per DAG_PROTOCOL §7.4: silence is invalid; added 2026-07-30 applying R11 m9.)

