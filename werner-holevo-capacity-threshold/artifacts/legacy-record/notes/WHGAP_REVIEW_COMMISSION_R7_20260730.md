# WHGAP review commission R7 — rule-7 review of P13-B (frozen 2026-07-30)

Commissioner: decision layer. Reviewer: ONE fresh Opus instance (did not author P13-B,
no desired outcome given). NODE_ID = `WHGAP.onset-two-fifths`, ROLE = reviewer.
Interpreter: `C:<home>/cpython3119/python.exe`. Reviewer scripts
`tools/whgap_r7_*.py`; logs into `artifacts/logs_whgap_p13b_20260730/` with
`SHA256SUMS_r7.txt` (LF). Pre-task reload mandatory; single-writer deviation binding.

**Inherited:** §1–§3 of [WHGAP_REVIEW_COMMISSION_R5_20260729.md](WHGAP_REVIEW_COMMISSION_R5_20260729.md)
+ P13-A/P13-B tooling notes (radical-free charts; Berkowitz det; nsimplify ban on exact
rationals). Frozen inputs (7d): R5/R6-reviewed package (expansion machinery, n=1 closed
form, stratum exhaustion, P2/P4, Q>0 on (0,2/5)).

**Reviewed inputs (frozen):** `artifacts/whgap_p13b_n2_layer_20260730.md`; commission
[WHGAP_COMMISSION_P13B_20260730.md](WHGAP_COMMISSION_P13B_20260730.md); scripts
`tools/whgap_p13b_*.py` (read only); logs/JSON under
`artifacts/logs_whgap_p13b_20260730/` (verify SHA256SUMS_p13b.txt first).

## Claims under review

1. **S2 identity:** <conj(Psi)|(Lambda⊗Lambda)(P_Psi)|conj(Psi)> =
   (1−x)^2 |Tr(M M^T)|^2 + x^2 ||adj M||_F^2, via Tr(M^T A_i M A_j) = −2 adj(M)_{ji}.
   Re-derive INDEPENDENTLY (own route — e.g. direct index contraction or your own
   symbolic assembly on a general 9-parameter complex M), symbolically or at c >= 3
   generic exact M and 2 rational x.
2. **m_B x-independence:** ker (Lambda⊗Lambda)(P_Psi) = (span{Ahat_a M Ahat_b^T})^perp
   with the executor's normalization — audit the derivation and verify at >= 2 exact
   Psi with different ranks r.
3. **Exact strip nulls:** D_Psi <= 0 exactly for the 13 families at
   x in {2/5, 21/50, 9/20, 12/25} — re-verify at least 4 (family, x) pairs INCLUDING
   one type-E entangled point and one r=8 generic-entangled point, by your own exact
   construction of D_Psi (own kernel computation, own duality derivation).
4. **Interval certificate:** lambda_max(D_Psi(x)) = 0 identically on [2/5, 1) for the
   isotropic-product and type-E base points; the (5x−2) factor structure. Re-derive the
   symbolic-in-x charpoly for ONE of the two base points by your own route.
5. **Calibrations + false-positive refutation:** G-cal1 (13/132 at 7/20), G-cal2, and
   the three-way refutation of the 0.0200 incumbent at x=2/5 — audit the logic and
   reproduce the exact re-test of the rationalized point.
6. **Below-onset enhancement:** the exact value 1102933/9570000 at x=7/20 for the
   type-E point — re-verify exactly; audit the "~17% stronger, dies at same 2/5"
   framing for over-claim.
7. **Variety conjecture hygiene:** {m_B >= 1} = P3 is CONJECTURED on 60/60 hunts —
   audit that no reviewed-tier claim leans on it; check the coverage statement of the
   bounded null (families, restarts, rank-ambiguous exclusions) for honesty.

## Licensing menu

- (A) License: "the P13-B exact package (claims 1–4, 6) is CERTIFIED\* [state exact
  scopes]; the S3 sweep + calibrations are a sound NUMERICAL bounded null; the n=2
  first-order layer yields no witness in [2/5, 1/2) within the searched families, with
  the P3-variety completeness explicitly CONJECTURED."
- (B) FINDINGS (itemized MAJOR/minor).

Report: `artifacts/whgap_r7_review_20260730.md` (immutable). Return
{verdict, summary, majors[], minors[], report_path}.

