---
id: "WHGAP.onset-two-fifths"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.onset-two-fifths.md"
aliases: ["P13"]
kind: LEAF
role: proof
status: CONJECTURED
status_source: "onset identification CONJECTURED; P13-A stratum-exhaustion PROVED (R6, LICENSE A); P13-B n=2 exact package CERTIFIED* per R7's repaired wording (FINDINGS, 2 interpretive MAJORs corrected on-node; artifacts/whgap_r7_review_20260730.md §7), sweep NUMERICAL"
disposition: null
parents: ["WHGAP.goal"]
children: []
related: ["WHGAP.qpositive-onset", "WHGAP.no-ascent-hierarchy", "WHGAP.order-boundary"]
---

# WHGAP.onset-two-fifths — Is x_D = 2/5 the exact single-letter onset of Q > 0?

## Claim

**Conjecture:** the onset of positive (single-letter) quantum capacity in the noisy
Werner–Holevo family is exactly x_D = 2/5: Q^{(1)}(Lambda_x) > 0 for x < 2/5 (PROVED) and
Q^{(1)}(Lambda_x) = 0 for x in [2/5, 1) (OPEN); ideally also Q = 0 there (which would close
the entire strip [2/5, 1/2) and, with P4, give {x : Q = 0} = [2/5, 1]).
**[CONJECTURED]**

Reconciliation note (2026-07-30, applying R11 m3): what the parent goal's composition
consumes from this node is the **Q-determination in set form** — the set
S = {x in [2/5, 1/2) : Q(Lambda_x) = 0} — i.e. the "ideally also Q = 0" clause, NOT the
Q^{(1)} statements (which are this node's mechanism layer). A future proof of the
Q^{(1)}-only conjecture would NOT by itself discharge the goal assembly (Q^{(1)} = 0 at
one blocklength does not give Q = 0); the Lean module mirrors the Q-set form for exactly
this reason.

## Role in DAG

Registered 2026-07-30 per rule 8b, at the explicit joint request of the E-N1 lemma note
(§13 item 4) and the R5d review, so that "2/5" is never read off the expansion-lemma note
as a proven onset. What IS proved (R5c + R5d, cited on [[WHGAP.no-ascent-hierarchy]] and
[[WHGAP.qpositive-onset]]): the first-order isotropic ascent mechanism has EXACT threshold
2/5 — max over states of (w_B − w_E) equals max(d_1, 0) with d_1 = (1−x)(2−5x)/(2−x), so
the mechanism yields Q > 0 on (0, 2/5) and NOTHING at or above 2/5 (at x = 2/5 the witness
family is strictly unhelpful: Ic = c_1(2/5)·eps + o(eps) < 0). Whether Q (or Q^{(1)})
actually vanishes on [2/5, 1/2) is this node's open content.

## Current status

CONJECTURED. Structural evidence for: P3's S1 full-input scans found no positive Ic above
x_1 (but Prop 9.1's crossover eps* collapse means those scans were blind below eps ~ 1e-5 —
weakening them as evidence near 2/5); the P10 distillation probes found no strip rate above
1e-10; the balanced/higher-order layers gave nothing at 9/20. Structural evidence against:
none known. Named obligations (from the E-N1 note §10 item 3, all open):
(a) optimality of phi = P_psibar among all states — DONE in effect via the R5c closed form
    (max_phi (w_B − w_E) = max(d_1, 0)) for the FIRST-ORDER isotropic mechanism; what
    remains is (b)–(d);
(b) non-isotropic strata: no tau ≠ 0 pure psi supports any ascent for x in [2/5, 1/2);
(c) the balanced layer (N1'-b) and all higher-order terms give nothing on [2/5, 1/2)
    (note: for x < 2/5 the balanced set is a nontrivial face — R5c m4 — but that region is
    already decided; the question is at and above 2/5);
(d) every blocklength n >= 2 (the superactivation directions; entangled isotropic psi_n).

## Dependencies

[[WHGAP.no-ascent-hierarchy]] (the PROVED n = 1 isotropic layer and the R5c closed form);
[[WHGAP.qpositive-onset]] (Q > 0 on (0, 2/5) PROVED — the lower side of the conjectured
onset); [[WHGAP.order-boundary]] / P4 (Q = 0 on [1/2, 1) — the upper side); the E-N1 note
[WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md](../../notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md)
(Prop 9.1's two-term expansion — the tool for scanning candidate mechanisms near 2/5).

## Work record

- 2026-07-30 — node registered (rule 8b, decision layer) while applying the R5 batch; no
  commission authored yet. Numerical-search caveat carried from Prop 9.1: any Ic search
  near 2/5 must reach eps below exp(c_1/d_1) (doubly-exponentially small in 2/5 − x) or it
  will report the wrong sign.
- 2026-07-30 — commission P13-A authored (rule 8a, this node cited):
  [WHGAP_COMMISSION_P13A_20260730.md](../../notes/WHGAP_COMMISSION_P13A_20260730.md) —
  stratum exhaustion of the first-order mechanism (gates G0-G5; executor + paired fresh
  R6 review; decision-layer pre-derivation det = x(1-x)tau^2/2 given to verify, not
  trust). Dispatched as a two-agent pipeline.
- 2026-07-30 — commission P13-B authored (rule 8a, this node cited, obligation (d) n=2
  instance): [WHGAP_COMMISSION_P13B_20260730.md](../../notes/WHGAP_COMMISSION_P13B_20260730.md)
  — the n=2 entangled first-order layer: exact structured families (product iso⊗iso with
  the inclusion-exclusion D⁽²⁾ = D⊗1 + 1⊗D − (M_B⊗M_B − M_E⊗M_E); maximally entangled;
  global-isotropic Tr(MMᵀ)=0 families), degeneracy-variety derivation, numeric sweep on
  the variety with pre-registered rank discipline; calibration gates G-cal1 (embedded n=1
  witness at 7/20 must be found) and G-cal2 (hard: nothing positive at 11/20); decision
  gates G+ (strip witness ⟹ Q>0 there, NUMERICAL cap + immediate follow-up) / G0
  (bounded null). Paired review deferred until outcome. Dispatched.
- 2026-07-30 — E-P13A executed, all gates passed, no partial delivery. One commission
  repair reported honestly: "the 2x2 block in span{psi, psibar}" is ill-typed at tau = 1
  (span is 1-dim); restated in characteristic-polynomial form covering tau in (0,1]
  uniformly and proved for ARBITRARY psi. Two standing sympy failure modes hit and
  documented (odd-monomial radical substitution — fixed by a radical-free rational chart;
  Matrix.charpoly Relational error — fixed by Berkowitz det). Sanity: 56 gates PASS
  (`tools/whgap_p13a_sanity.py`; logs + SHA256SUMS_p13a.txt under
  `artifacts/logs_whgap_p13a_20260730/`).

## Evidence

- 2026-07-30 — **the P13-A stratum-exhaustion Theorem, PROVED** (decision layer applying
  the completed R6 review verbatim; note
  [WHGAP_P13A_STRATUM_EXHAUSTION_20260730.md](../../notes/WHGAP_P13A_STRATUM_EXHAUSTION_20260730.md)):
  for every x in (0,1), every pure psi with tau(psi) > 0, and every state phi,
  Ic((1-eps)P_psi + eps phi) = -w_E * eps log(1/eps) + O(eps) with
  **w_E = (x/2)(1 - <psi|phi|psi>) > 0 strictly for phi != P_psi** (explicit remainder
  C(x,tau), window eps <= g/4, g = mu_-(x,tau) >= x(1-x)tau^2/(2-x)). Supporting exact
  facts, all independently re-derived by R6: the B-side 2x2-block determinant
  x(1-x)tau^2/2 (full rank iff tau > 0); ker Lambda^c(P_psi) = span{(0, conj psi)};
  K(k) = -sqrt(x/2)[psi]_x purely skew with K^dag K = (x/2)(1 - P_psi) exactly, so the
  **exceptional set is EMPTY** (rank 2 even on the nilpotent psi^T psi = 0 bilinear
  branch) and the kernel-avoiding set is exactly {P_psi} (trivial: rho_eps = P_psi, Ic
  identically 0). **Licensed consequence (R6 wording): at n = 1 the pure-base FIRST-ORDER
  mechanism yields positive-capacity witnesses exactly for x < 2/5, and only on the
  isotropic stratum.** Nothing here establishes Q^(1) = 0 or Q = 0 on [2/5, 1/2).

## Work record (continued — P13-B, the n=2 layer)

- 2026-07-30 — E-P13B executed (fresh Opus executor): **G0 BOUNDED NULL at the n=2
  first-order layer** (`pending-review:` unreviewed executor evidence, NUMERICAL cap).
  Calibration first: G-cal1 PASS (x=7/20: family (a) recovers lambda_max = d_1(7/20)
  = 13/132 EXACTLY via the psibar tensor slot; inclusion-exclusion
  D^(2) = D⊗1 + 1⊗D − (M_B⊗M_B − M_E⊗M_E) re-derived from first principles);
  G-cal2 PASS (x=11/20: nothing above 1e-9 over 70 states; exact NSD certificates for
  all 13 families). One S3 false positive (0.0200 at x=2/5) REFUTED three ways
  (conditioning boundary; negative measured eps-log slope; rationalized exact test gives
  r=9, lambda_max=0) — the compute overran to ~150 min on this refutation (honest
  report). Two sympy failure modes hit and documented (nsimplify corrupting exact
  rationals; Relational truth-value on mismatched Symbol); an index slip was caught by
  the three-way construction-agreement gate. Artifact:
  [whgap_p13b_n2_layer_20260730.md](../../../../artifacts/whgap_p13b_n2_layer_20260730.md);
  24 files hashed (SHA256SUMS_p13b.txt, LF, verified) under
  `artifacts/logs_whgap_p13b_20260730/`.

## Evidence (continued — P13-B, all `pending-review:`)

- 2026-07-30 — **exact strip nulls:** at x in {2/5, 21/50, 9/20, 12/25} EVERY
  commissioned family has D_Psi <= 0 EXACTLY (exact LDL/charpoly certificates), hence
  lambda_max = 0 exactly; **interval certificate: lambda_max(D_Psi(x)) = 0 for ALL
  x in [2/5, 1)** for the isotropic-product and type-E base points (exact root
  isolation; the top charpoly coefficients carry (5x−2) factors — **the 2/5 threshold
  reappears at n=2**). Best accepted numerical strip value: 2.3e-15 (round-off).
- 2026-07-30 — **S2 structural identity (executor-symbolic, unreviewed):**
  <conj(Psi)|(Lambda⊗Lambda)(P_Psi)|conj(Psi)> = (1−x)^2 |Tr(M M^T)|^2
  + x^2 ||adj M||_F^2 (via Tr(M^T A_i M A_j) = −2 adj(M)_{ji}) — so conj(Psi) lies in
  the B-kernel ONLY for products with an isotropic factor: the n=1 witness direction
  does NOT generalize. Also: m_B is x-INDEPENDENT (kernel = (span{Ahat_a M Ahat_b^T})^perp);
  the variety P3 = {v a^T + y u^T : u^T u = v^T v = 0} has m_B >= 1 and contains all
  commissioned degenerate families (r = 4/6/7/8 strata), while maximally entangled and
  diag(1, i, 0) are NON-degenerate (r = 9, structural null); **{m_B >= 1} = P3 is
  CONJECTURED** (60/60 unconstrained hunts land in P3). Stretch determinant
  factorization not forced (documented).
- 2026-07-30 — **below-onset enhancement (noteworthy):** at x = 7/20 the type-E
  entangled base point gives exactly 1102933/9570000 = 0.11524900... > d_1(7/20) =
  13/132 = 0.09848... — the n=2 first-order layer is ~17% STRONGER than n=1 below the
  onset, yet dies at the same 2/5. Structured evidence that the 2/5 threshold is
  blocklength-robust at the first-order layer.
- Coverage honesty: NOT covered — the n=2 balanced layer (now generic on the strip),
  higher orders, mixed base points, n >= 3, and any component of {m_B >= 1} outside P3.
  Nothing establishes Q^(1) = 0 or Q = 0 on [2/5, 1/2).

## Adversarial reviews

- 2026-07-30 — **R7 (fresh Opus instance, rule-7 complete) on P13-B: FINDINGS — 2 MAJOR
  (both INTERPRETIVE; every exact number confirmed) + 6 minors.** The reviewer
  independently re-derived the entire exact package (own E-side range-route projector;
  M_B twice — operator-sum AND direct channel formula; Newton-identity charpoly on
  denominator-cleared integer matrices): S2 identity PROVED symbolically in 18 free
  symbols and x; m_B x-independence PROVED; six strip (family,x) pairs exactly NSD;
  BOTH interval-certificate base points re-derived symbolically; 13/132 and
  1102933/9570000 reproduced exactly and corroborated at 60 dps as true eps-log slopes;
  the x=2/5 false positive genuinely refuted (stratum-drift diagnosis confirmed).
  **MAJOR 1 (headline inversion):** "n=2 beats n=1 by ~17%, dies at same 2/5" is false
  in both halves — per channel use the type-E coefficient is lambda_max/2 = 0.0576 <
  d_1(7/20) = 0.0985 (strictly SUBADDITIVE: 0.11525 < 2 d_1 = 0.19697), and the type-E
  point's exact threshold is **x*_E = 0.391297769484659... (unique (0,1)-root of
  19x^4 − 21x^3 − 14x^2 + 28x − 8), STRICTLY BELOW 2/5** (advantage reverses from
  x = 0.38 up); the (5x−2) charpoly signature belongs to the isotropic PRODUCT family —
  whose lambda_max = d_1(x) identically, i.e. the embedded n=1 witness — NOT to the
  entangled layer. **MAJOR 2 (coverage):** lambda_max is discontinuous across strata, so
  the generic F1 sweep never probes m_B >= 2; the m_B = 2 stratum (positive-dimensional
  mod the real symmetry) is exactly covered only at TWO isolated inequivalent orbits;
  the "13 structured families" collapse to ~7 O(3)xO(3) orbits of which 3 are
  structurally trivial (m_B = 0 gives D = −M_E <= 0). The bounded NULL itself is
  UNTOUCHED and reinforced (entangled base points die EARLIER than 2/5). Report (with
  the repaired licensable wording in §7):
  [whgap_r7_review_20260730.md](../../../../artifacts/whgap_r7_review_20260730.md);
  reviewer scripts `tools/whgap_r7_*.py`; logs + SHA256SUMS_r7.txt (30/30 verified) in
  `artifacts/logs_whgap_p13b_20260730/`.

## Post-R7 corrections and licensing (decision layer, 2026-07-30 — append-only)

- **CORRECTION of the "below-onset enhancement" Evidence bullet above (R7 MAJOR 1):**
  the exact values stand; the interpretation is withdrawn. Correct reading: the 2-copy
  first-order coefficient is strictly subadditive (per-use 41% WEAKER than n=1 at 7/20);
  the type-E entangled threshold x*_E < 2/5 — entangled base points die EARLIER than the
  product witness; "the 2/5 threshold reappears at n=2" holds only via the embedded n=1
  product witness and is NOT independent blocklength evidence. The same correction
  applies to the P13-B artifact's one-line outcome and §8.3, to the NODE_INDEX
  narrative, and to the DAG header (all corrected this session, citing R7).
- **CORRECTION of the coverage statement (R7 MAJOR 2):** the null's honest scope is:
  exact zero at ~7 distinct orbits (3 structurally trivial) + a sound NUMERICAL bounded
  null on the generic m_B = 1 stratum and the product stratum; m_B >= 2 covered only at
  two isolated exact orbits (type-E diag(1,1,0) and P3s u0 e3^T + e3 u0^T, inequivalent
  by Tr(MM^T)/||M||_F^2 = 1 vs 0); the F2 chart is numerically unfaithful; the
  positive-dimensional remainder of the m_B = 2 stratum is UNSEARCHED.
- **CERTIFIED\* opened for the P13-B exact package** (decision layer applying R7's
  repaired licensing wording, report §7, verbatim scope): (1) the S2 identity + its
  corollary — PROVED; (2) x-independence of (r, m_B, m_E) with the kernel formula —
  PROVED; (3) exact lambda_max(D_Psi) = 0 at the tabulated rows (~7 orbits) — PROVED at
  those orbits; (4) lambda_max ≡ 0 on [2/5,1) for the isotropic product AND on
  [x*_E, 1) for type-E — PROVED; (5) G-cal1 exact, product family lambda_max ≡ d_1(x),
  false positive correctly refuted by legs (i)-(ii) (the rationalisation leg is VOID —
  R7 m2: ambient rationalisation leaves every positive-codimension variety; future G+
  gates must use CHART-AWARE rationalisation); (6) the exact type-E value with the
  corrected framing. The S3 sweep stays NUMERICAL. Nothing establishes Q^(1) = 0 on
  [2/5, 1/2); this node stays CONJECTURED.
- **R7 m4 (reviewer-authored observation, NUMERICAL):** dim ker D_Psi = 1 at every strip
  point tested (iso-product at 9/20, 12/25; type-E at 2/5, 9/20; P3g r=8 at 9/20; P3s at
  9/20) ⟹ ker D_Psi = span{Psi}, the only balanced state is P_Psi, so **the n=2 balanced
  layer appears EMPTY on the open strip** (sole exception: iso-product exactly at
  x = 2/5, where dim ker D_Psi = 4) — mirroring the P9b n=1 emptiness. This narrows
  obligation (d): the named remaining n=2 gaps are the unsearched m_B >= 2 stratum
  remainder and the exactly-2/5 exceptional kernel, not a generic balanced layer.
- **R7 m6 ruling (commission cap):** the 150-vs-120-min overrun was spent refuting the
  false positive — the honesty rule governs; overrun RATIFIED. Tooling additions from
  m5 adopted into the standing list: Symbol('x') needs a reality assumption or
  rational-x settlement for Hermiticity gates; Newton-identity charpolys on integer
  matrices beat symbolic Berkowitz at r = 8.
  minors.** Independent routes throughout: arbitrary-psi Berkowitz charpoly (6 free real
  symbols, no normal form) reproduces the factorization with the slip-prone a(p+q) term
  intact; kernel found by own nullspace route and pinned by exact rank count; rank
  K(k) = 2 established twice (principal 2x2 minors — no case split — and
  spec K^dag K = {0, x/2, x/2}); G2 assembly audited line by line against the
  R5d-reviewed machinery (m = 1 instantiation confirmed in scope); own-code numerics
  21/21 PASS (log-slope = -w_E to 1e-12 at 9/9 pairs; two high-precision certificate
  points, dps 202/891; 256-point own grid rank histogram {2: 256}; tau -> 0 crosscheck
  mu_-/tau^2 -> mu_A/4; independent corroboration of the frozen R5c isotropic layer).
  Minors: m1 licensing wording must say "first-order layer" (adopted verbatim here);
  m2 the executor's non-commissioned moderate-eps probe included the tau = 0 endpoint
  (reviewer's tau>0-only probe: maxima -1.44e-7 at 9/20, -1.61e-7 at 49/100 — negative);
  m3 gate count is 55 assertions + 1 completion marker; m4 a remark's normal-form-only
  phrasing; m5 deliberate slack in C(x,tau) (valid). Report:
  [whgap_r6_review_20260730.md](../../../../artifacts/whgap_r6_review_20260730.md).

## Decision-layer adjudication of the executor's two suggested nodes (rule 8b, 2026-07-30)

E-P13A suggested registering (a) a finite-mixing landscape node (Ic > 0 at moderate eps
from tau != 0 base points — exhibited at x = 1/5, which lies in the PROVED Q > 0 region)
and (b) a no-uniform-window obstruction node (the eps-window collapses like tau^2, so no
compactness route from the stratum theorem). Adjudication: (a) as an approach is the
full-input single-letter search already executed and reviewed under P3-S1 (bounded null
in the strip; 200 restarts/point), now sharpened by the Prop 9.1 blindness caveat — it is
recorded HERE as obligation context, not duplicated as a node; (b) is a methodological
obstruction (a reason the stratum theorem cannot decide the strip), recorded here
append-only, not an approach. Both candidates thereby terminate in explicit states.

## Open obligations

- (b) FIRST-ORDER LAYER CLOSED (P13-A + R6). The literal "no ANY ascent" reading stays
  open only in the sense that moderate-eps mixed states are not constrained by the
  first-order theorem — in the strip the evidence is the P3-S1 bounded null plus R6's
  tau>0 probe (negative at 9/20, 49/100); no witness is known.
- (c) at and above 2/5 on the isotropic stratum: higher-order/balanced layers — OPEN
  (off the isotropic stratum, first-order (c) is closed: every phi != P_psi has
  w_E > 0, so there is no balanced layer to enter).
- (d) n >= 2 entangled layers — n = 2 FIRST-ORDER layer: reviewed (R7). Exact package
  CERTIFIED\*; sweep NUMERICAL. Remaining n = 2 gaps (per R7): the UNSEARCHED
  positive-dimensional remainder of the m_B >= 2 stratum (chart F2 unfaithful; only two
  isolated exact orbits covered); the iso-product exactly-2/5 exceptional kernel
  (dim ker D_Psi = 4 there); higher orders; {m_B >= 1} = P3 completeness (CONJECTURED);
  n >= 3. The generic n = 2 balanced layer appears EMPTY (R7 m4, NUMERICAL).

## Status history

- 2026-07-30 — created CONJECTURED (rule 8b registration; the E-N1 note and R5d review
  jointly requested the separate node).
- 2026-07-30 — status unchanged CONJECTURED; PROVED-tier sub-result recorded (decision
  layer applying the completed R6 review verbatim): the stratum-exhaustion Theorem —
  first-order layer of obligation (b) closed, first-order (c) closed off the isotropic
  stratum. The onset identification itself remains the node's open content.

## Lean

```yaml
lean:
  module: "WHGAP.«onset-two-fifths»"
  file: "channel-capacity/werner-holevo-gap/proof-dag/lean/WHGAP/onset-two-fifths.lean"
  claim: "Claim"
  composition: null  # conjecture
  state: "stated"
  tier: "T1 (stated only)"
  rel: []
  build: "artifacts/logs_whgap_lean_20260730/"
  claim_hash: "sha256:e0fa50f46c12fb8f58b7d187cda62c5a478d1c73edbc94ac7f7167c977d8c3bd"  # refrozen after the R11-m3 reconciliation note (LEAN-1.1)
  synced: "2026-07-30 (refrozen post R11 m3)"
```

Mechanization notes (LEAN-1, 2026-07-30, NUMERICAL `pending-review:` — the §7.10
statement-fidelity review is the completion gate): Claim stated in the set form the goal assembly consumes; conjecturedS := Ico (2/5) (1/2) is defined but ASSERTED NOWHERE; no theorem in this module, deliberately (the node is CONJECTURED).
Report: [whgap_lean_t1t2_20260730.md](../../../../artifacts/whgap_lean_t1t2_20260730.md)
(G-L5 fidelity self-table row for this node; granularity losses stated there).

