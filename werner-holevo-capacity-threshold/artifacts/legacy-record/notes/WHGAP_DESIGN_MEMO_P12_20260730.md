# WHGAP P12 design memo — decision layer, 2026-07-30

Node: `WHGAP.restricted-order` (P12). This memo discharges that node's standing open
obligation ("decision-layer design memo: candidate order + tensorization sketch +
falsification anchors, THEN a bounded feasibility commission"). It is decision-layer
authorship: it licenses NOTHING. Its claims are commissioned for verification in
[WHGAP_COMMISSION_P12A_20260730.md](WHGAP_COMMISSION_P12A_20260730.md) and are to be
reviewed before any status write.

## 1. The observation that reframes P12

The reviewed necessity witness (paper §5, R5b LICENSE A) uses a **trivial reference**.
So what it refutes below x = 1/2 is not merely the *complete* relative-entropy order but
the **plain** RE domination
  D(Λ^c(ρ) ‖ Λ^c(σ)) ≥ D(Λ(ρ) ‖ Λ(σ)) for all admissible (ρ, σ).

Plain RE domination is equivalent to the **less-noisy** order (⟸ is trivial; ⟹ follows by
the two-point limit: for the ensemble {p, ρ; 1−p, σ}, χ/p → D(·(ρ)‖·(σ)) as p → 0⁺). And
less-noisy is exactly P^{(1)} = 0. Therefore, below 1/2, **P^{(1)} > 0** — and since
P^{(1)} is superadditive under tensor powers, **P(Λ_x) > 0 for every x < 1/2**.

## 2. The elementary closed form (no perturbation theory needed)

Take the SYMMETRIC two-point ensemble
  E(ε,t) = { ½ : ρ_ε + tX , ½ : ρ_ε − tX },  average ρ̄ = ρ_ε,
with the frozen witness ρ_ε = diag(1−2ε, ε, ε), X = (E_{12}+E_{21})/√2 (0-based).
Both states are PSD for |t| ≤ √2 ε.

- Receiver: Λ(X) = (1−3x/2)X, and Λ(ρ_ε) has the degenerate pair
  b = x/2 + (1−3x/2)ε on the {1,2} block, so Λ(ρ_ε ± tX) COMMUTES with Λ(ρ_ε) and has
  eigenvalues {α, b ± u}, u = t(1−3x/2)/√2.
- Environment: Λ^c(X) = 0 ⊕ (−x/2)X, and Λ^c(ρ_ε) = diag(1−x, xε, e, e) with
  e = (x/2)(1−ε); again commuting, eigenvalues {1−x, xε, e ± v}, v = tx/(2√2).

With f(s) := (1+s)log(1+s) + (1−s)log(1−s) = Σ_{k≥1} s^{2k}/(k(2k−1)) ≥ 0:

  **χ_B = b·f(u/b),  χ_E = e·f(v/e),  Δ(x,ε,t) := χ_B − χ_E = b f(u/b) − e f(v/e).**

Leading order: b(u/b)² − e(v/e)² = u²/b − v²/e = (t²/2)[g_B − g_E] = (t²/2)·2(1−x)(2x−1)/x
at ε → 0 — the paper's gap (5.3). Since f(s) ≥ s² and
f(s) ≤ s² + s⁴/(6(1−s²)) for |s| < 1, positivity of Δ for explicit rational (ε,t) is an
elementary inequality. Hence P^{(1)}(Λ_x) ≥ Δ(x,ε,t) > 0 for x < 1/2.

**Consequence (target theorem): {x : P(Λ_x) = 0} = [1/2, 1] EXACTLY.** The private-capacity
boundary of the family is completely determined, and it coincides with the cRE/cBKM order
boundary — the necessity theorem is not just an obstruction to a proof technique, it is
the true private-capacity phase boundary.

## 3. Why this decides P12

Write the order class by the ENSEMBLE CLASS it controls (the "purity knob"):

- **All ensembles** ⟺ less noisy ⟺ P^{(1)} = 0. Dead below 1/2 by §1–§2 —
  UNCONDITIONALLY (the conclusion itself is false there, not merely unprovable).
- **Pure-state ensembles** ⟺ Q^{(1)} = 0: for pure ψ_u the outputs Λ(ψ_u), Λ^c(ψ_u) are
  isospectral, so the conditional entropies cancel and
  χ_B − χ_E = S(Λ(ρ̄)) − S(Λ^c(ρ̄)) = I_c(ρ̄). Maximizing gives exactly Q^{(1)}.
  This is the more-capable order; for complement pairs it equals its own complete version
  (HRSF22 Prop 3.3) and its tensorization IS the additivity problem ([[WHGAP.more-capable-route]],
  PARKED with that reason).
- **Anything in between:** the P12 node's own first candidate ("anchored less-noisy",
  anchors σ = ψ_R ⊗ ρ_A) CONTAINS the ensemble pairs — take R trivial, σ = ρ̄ — so it
  implies P^{(1)} = 0 and is dead below 1/2 by §2. More sharply: the witness states
  ρ_ε ± tX are within O(ε) trace distance of the pure state |0⟩⟨0|, and ε may be taken
  arbitrarily small (any ε < ε_c(x) = 2(1−2x)/(2−3x) works). So **every ensemble class
  with any thickness around the pure states fails below 1/2**; the only surviving class is
  the exactly-pure one, i.e. Q^{(1)} = 0 itself.

**P12 no-go (the memo's main structural claim, to be verified):** on this family, the
restricted-order program has no room. Any order defined by relative-entropy domination
over an ensemble class either (a) contains a non-pure neighbourhood and is FALSE below
1/2, or (b) is the pure class, which is exactly Q^{(1)} = 0 and whose tensorization is
the coherent-information additivity problem. The frontier therefore relocates entirely to
[[WHGAP.order-converse]] (P11: does O(3)-covariance collapse regularized-more-capable to
its complete version?) and to genuine additivity technology — not to a new intermediate
order.

## 4. What this does NOT say

Nothing about Q on [2/5, 1/2). If Q = 0 there, those channels have **P > 0 = Q** — the
bound-entanglement-like regime (cf. HHHO 2008, secure key from bound entanglement, in the
local library); that is a *feature* of the result, and a strong hint about which
mechanisms could possibly certify Q = 0 there (they must be Q-specific).

## 5. Falsification anchors (binding on the commission)

- Hard calibration: at x = 11/20 and x = 3/5, Δ(x,ε,t) ≤ 0 for every tested (ε,t) —
  P = 0 is PROVED there (P4), so any positive value means the closed forms are wrong.
- Consistency: at x < 2/5 the conclusion P > 0 is already implied by Q > 0 (P3+R5d), so
  the genuinely new content is exactly the strip [2/5, 1/2).
- Degeneration: Δ → 0 as x → 1/2⁻ (since ε_c(x) → 0) — the lower bound must vanish
  continuously at the boundary, not jump.

