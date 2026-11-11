---
id: "WHGAP.private-boundary"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.private-boundary.md"
aliases: ["P14"]
kind: LEAF
role: proof
status: PROVED
status_source: "R8 review 2026-07-30 (artifacts/whgap_r8_review_20260730.md §5 items 1-2, licensable-at-PROVED list) applied by the decision layer at the R8-corrected scope; execution note notes/WHGAP_P12A_PRIVATE_BOUNDARY_20260730.md"
disposition: null
parents: []
children: []
related: ["WHGAP.goal", "WHGAP.order-boundary", "WHGAP.restricted-order", "WHGAP.zero-capacity-application", "WHGAP.qpositive-onset"]
---

# WHGAP.private-boundary — The private-capacity boundary of the family is exactly 1/2

## Claim

**Theorem (PROVED).** For every x in (0, 1/2),

  P^{(1)}(Lambda_x) >= Delta(x) = [(1-2x)(1-x)/(2-3x)] * f( (1-2x)/(sqrt2 (1-x)) )
                    >= (1-2x)^3 / (2(1-x)(2-3x)) > 0   nats,

with f(s) = (1+s)log(1+s) + (1-s)log(1-s), attained by the symmetric two-point ensemble
{1/2 : rho_eps + tX, 1/2 : rho_eps - tX} at eps = t = eps_c(x)/2 = (1-2x)/(2-3x), where
(rho_eps, X) is the frozen necessity witness of paper §5. Hence P(Lambda_x) > 0 there.

**Corollary.** {x in (0,1) : P(Lambda_x) = 0} = [1/2, 1) EXACTLY at PROVED tier; the
closed interval [1/2, 1] holds at CERTIFIED\* (the x = 1 endpoint inherits P4's cite-only
RK24 dependency; the paper's Lemma 4.1 self-complementarity argument covers it at
written-proof/external-review tier). **[PROVED at the stated scope]**

## Role in DAG

Produced by the P12-A campaign (commissioned to decide the restricted-order question) as
its first and largest by-product. It settles the private-capacity half of the goal
question completely, and it is the unconditional engine of the P12 no-go map: any order
class whose conclusion is P^{(1)} = 0 is not merely unprovable below 1/2 — its conclusion
is FALSE there.

## Current status

PROVED at the R8-licensed scope. The mechanism: the reviewed necessity witness uses a
TRIVIAL reference, so it refutes plain relative-entropy domination, which by
HRSF22 Prop 2.3 (quantum Watanabe 2012 Prop 4) is equivalent to the less-noisy order,
which is equivalent to P^{(1)} = 0. The explicit ensemble makes this constructive and
elementary: both outputs COMMUTE with their base points, so both Holevo quantities
collapse to the same scalar function,
  chi_B = b f(u/b),  chi_E = e f(v/e),
  b = x/2 + (1-3x/2)eps, u = t(1-3x/2)/sqrt2, e = (x/2)(1-eps), v = t x/(2 sqrt2),
and at eps = t = eps_c/2 the two f-arguments COINCIDE exactly (executor's Lemma 3.2b), so
Delta = (b-e) f(s*) with b - e = eps(1-x) > 0 — no series bounds and no perturbation
theory anywhere. Delta_max(x) -> 0 like 4.740 (1-2x)^3 as x -> 1/2^-.

## Dependencies

Paper §5 necessity witness (R5b LICENSE A, frozen); P4 for the other side (PROVED on
[1/2,1), closed interval CERTIFIED\*); HRSF22 Prop 2.3 (order equivalence, local PDF);
Devetak's P^{(1)} formula as stated in ZW eq. (2.6)/(2.7) (verified verbatim by R8);
product-ensemble superadditivity of P^{(1)} (proved in the note, R8-audited).

## Work record

- 2026-07-30 — decision-layer design memo
  [WHGAP_DESIGN_MEMO_P12_20260730.md](../../notes/WHGAP_DESIGN_MEMO_P12_20260730.md)
  conjectured the chain; commission P12-A dispatched with the memo explicitly labelled
  untrustworthy input.
- 2026-07-30 — E-P12A executed all stages, outcome THEOREM, note
  [WHGAP_P12A_PRIVATE_BOUNDARY_20260730.md](../../notes/WHGAP_P12A_PRIVATE_BOUNDARY_20260730.md).
  Every closed form re-derived FROM THE KRAUS SET (43 symbolic gates, 0 fail); the
  eps = t = eps_c/2 coincidence is the executor's own improvement over the memo's
  series-bound route. Six exact rational certificates (2/5, 21/50, 9/20, 12/25, 49/100,
  499/1000) in exact arithmetic. Two of its own bugs caught by its own gates and logged
  append-only (a conjugate-transpose slip; an absolute-eps optimizer grid producing
  spurious negatives near 1/2).
- 2026-07-30 — **decision-layer memo defect recorded (executor + R8 both confirm):** the
  memo transcribed the paper's gap (5.3) in the OPPOSITE orientation (wrote
  2(1-x)(2x-1)/x where the leading factor must carry (1-2x)); with the memo's sign its own
  conclusion would not follow. Benign — the executor derived the correct orientation
  independently — but recorded as an authorship defect of the decision layer.

## Evidence

- 2026-07-30 — S0 literature check (executor, R8-confirmed by own extraction): RK24 and
  RK25 contain NO private-capacity statement about this family ("private" appears only in
  their bibliographies); ZW proves P = Q = 0 only at x = 1/2. **The theorem is new
  relative to the local library.** The order equivalence itself is NOT new
  (HRSF22 Prop 2.3 = quantum Watanabe 2012 Prop 4) and is cited, not claimed.
- 2026-07-30 — gates: G-cal run FIRST at x = 11/20 and 3/5 (max Delta over 1000 pairs
  each: -3.99e-8, -6.44e-8; R8's own 600-pair reruns: -1.10e-7, -1.77e-7) AND proved
  SYMBOLICALLY on all of [1/2,1] via the chain |u| <= v <= e <= b; G-ind against an
  independently coded Holevo computation at 5 triples, 55-59 digits (R8: 6 triples,
  55-60 digits, every printed digit reproduced); G-cont confirms the (1-2x)^3 vanishing.

## Adversarial reviews

- 2026-07-30 — **R8 (fresh Opus instance, rule-7 complete): FINDINGS — 3 MAJOR
  (all scope/quantifier, none arithmetic) + 9 minors; the mathematical core CONFIRMED IN
  FULL by an independent route** (own Levi-Civita Kraus set, own padded complement, own
  eigenvalues, Holevo assembled as S(avg) - mean S(components); the note's b/u/e/v/f are
  read only in a final comparison block). 60 gates across 7 scripts; 7 gate failures all
  resolved, 2 of them defects in the reviewer's OWN code, logged append-only. Confirmed:
  Kraus completeness; Lambda(X) = (1-3x/2)X; the a-block vanishing; both commutations;
  both spectra; chi_B, chi_E symbolically and at 60 dps; eps_c(x); Lemma 3.2b and the
  exact Delta at 5 x to residual < 8e-62; all six rational certificates in Q; the
  p -> 0 limit argument; the superadditivity lemma and the Devetak citation verified
  verbatim against the local ZW PDF. **MAJOR 2 (applied here):** the note wrote
  {x : P = 0} = [1/2,1] as PROVED, which overruns P4's disk scope — the licensed
  statement is [1/2,1) at PROVED with the closed interval at CERTIFIED\*. (MAJORs 1 and 3
  concern the S3 no-go map and are applied on [[WHGAP.restricted-order]].) Report:
  [whgap_r8_review_20260730.md](../../../../artifacts/whgap_r8_review_20260730.md) — its
  §5 lists exactly what is licensable, which is what this node writes.

## Open obligations

None for the theorem. Consequence to carry elsewhere: on the strip [2/5, 1/2) we now know
P > 0 while Q is unknown — if Q = 0 there, the family exhibits **P > 0 = Q**
(bound-entanglement-like regime; cf. HHHO 2008 in the local library). Paper: incorporated
as a numbered section in v5.

## Status history

- 2026-07-30 — created PROVED (decision layer, applying R8 §5 items 1-2 verbatim at the
  R8-corrected interval scope; the [1/2,1] closed form is recorded at CERTIFIED\* to match
  P4's disk scope, not promoted).

## Lean

```yaml
lean:
  module: "WHGAP.«private-boundary»"
  file: "channel-capacity/werner-holevo-gap/proof-dag/lean/WHGAP/private-boundary.lean"
  claim: "Claim"
  composition: ["Claim_of_delta_le", "Claim_of_devetak"]  # LEAN-2 WP-C added the reduced bridge
  state: "proved"
  tier: "T2 (scalar core) / T1 (Claim via Claim_of_delta_le)"
  rel: ["hdev (Devetak-interface reading of the ONE explicit ensemble — the REDUCED boundary after WP-C: the entropy collapse chi_B = b f(u/b), chi_E = e f(v/e) and Delta = chi_B - chi_E are PROVED for the displayed matrices; residual = the identification of outB/outE with the channel outputs, sympy-checked + R12 re-derived, outside Lean)", "hbridge retained as the general bridge (Claim_of_delta_le)", "hsq DISCHARGED by WP-F (f_ge_sq proved) — Delta_lower_bound is now unconditional; the outB/outE identification (old residual (c)) CLOSED by WP-D (outB_eq/outE_eq); hdev now carries Devetak's formula PLUS the ensemble-validity residual (PSD + |t| ≤ √2·ε, manuscript-discharged, R13 m5)"]
  build: "artifacts/logs_whgap_lean3_20260801/"  # LEAN-3/3.2 batch; earlier evidence dirs retained
  claim_hash: "sha256:415bdc11d2a60d65716e8b8c23f8eb4e87ba63a00f3e708e815164f172a30aa9"
  synced: "2026-08-01 (post LEAN-3.2, R13 m2)"
```

Mechanization notes (LEAN-1 + R11 corrections, 2026-07-30): FLAGSHIP: the scalar core is
PROVED UNCONDITIONALLY (f_pos; argument_coincidence — proved as a rational identity in r,
stronger than commissioned; prefactor_eq; Delta_eq_prefactor_mul; Delta_closed_form_pos).
**R11 MAJOR-1 correction:** blockA_trace_det was misfiled here under a wrong "Lemma 7.1"
cross-reference — it belongs to paper Lemma 6.1 (the positivity layer) and has been moved
to the P9 module; this node no longer claims it. R11 independently confirmed the flagship
chain is genuinely unconditional (from elaborated signatures, not source comments).
Report: [whgap_lean_t1t2_20260730.md](../../../../artifacts/whgap_lean_t1t2_20260730.md)
(G-L5 fidelity self-table row for this node; granularity losses stated there).

