# The G* monotonicity lemma — decision-layer proof (2026-08-01)

**Author:** decision layer (Fable). **Status: derived, `pending-review:`** — rule 6: the
author may not stamp this PROVED; review obligation registered on
[WHGAP.pure-anchor-order](../proof-dag/nodes/WHGAP.pure-anchor-order.md). Cap NUMERICAL/
derived until a fresh reviewer completes the rule-7 check (it is four lines of calculus;
fold into the next review batch).

**Context.** P15-B (R16 LICENSE A) established, at reviewer-verified FORMULA level (R16
item 2: independent symbolic derivation, residual exactly 0), that on the orthocomplement
stratum (ψ real, σ = (1−P_ψ)/2) the pure-anchor functional takes the value

G*(x) = (1−2x)·ln x + x·ln(2−x) − (1−x)·ln(1−x) − (1−x)·ln 2,  x ∈ (0, 1/2).

R16 upgrade U2 observed numerically that G* < 0 throughout (0, x_d) and > 0 throughout
(x_d, 1/2) with G*′ > 0, and stated that only "an elementary monotonicity lemma" separates
"P_b2 fails at every x < x_d" from theorem status. This note supplies that lemma.

## Lemma (monotonicity and unique zero)

On (0, 1/2]: G* is strictly increasing, with G*(0⁺) = −∞ and G*(1/2) = (1/2)·ln(3/2) > 0.
Consequently G* has a UNIQUE zero x_d ∈ (0, 1/2), the zero is simple, G* < 0 on (0, x_d),
and G* > 0 on (x_d, 1/2].

## Proof

Differentiate term by term:

G*′(x) = −2 ln x + (1−2x)/x + ln(2−x) − x/(2−x) + ln(1−x) + 1 + ln 2.

Group as G*′(x) = L(x) + R(x) with

- L(x) = −2 ln x + ln(2−x) + ln(1−x) + ln 2 = ln( 2(2−x)(1−x) / x² ),
- R(x) = (1−2x)/x − x/(2−x) + 1.

**L ≥ ln 6 on (0, 1/2].** The ratio h(x) = 2(2−x)(1−x)/x² has a positive strictly
decreasing numerator and a positive strictly increasing denominator on (0, 1/2], hence is
strictly decreasing; its minimum is h(1/2) = 2·(3/2)·(1/2)/(1/4) = 6. So L(x) ≥ ln 6.

**R ≥ 2/3 on (0, 1/2].** The first term (1−2x)/x is ≥ 0 on (0, 1/2]. The middle term
x/(2−x) is strictly increasing (derivative 2/(2−x)² > 0), so x/(2−x) ≤ (1/2)/(3/2) = 1/3.
Hence R(x) ≥ 0 − 1/3 + 1 = 2/3.

Therefore G*′(x) ≥ ln 6 + 2/3 > 2.45 on (0, 1/2]: G* is strictly increasing there.

Boundary values: as x → 0⁺, (1−2x)·ln x → −∞ while the other three terms stay bounded, so
G*(0⁺) = −∞. At x = 1/2 the first term vanishes and
G*(1/2) = (1/2)ln(3/2) − (1/2)ln(1/2) − (1/2)ln 2 = (1/2)ln(3/2) ≈ 0.2027 > 0.

Strict monotonicity + the two boundary signs give a unique zero x_d; simplicity is
G*′(x_d) ≥ ln 6 + 2/3 > 0 (R16's independent value: G*′(x_d) = 3.326, consistent — the
bound is not tight and need not be). ∎

**Consistency checks (value-vs-formula):** G*(1/2) = (1/2)ln(3/2) = 0.20273… matches R16's
+0.2027; the lower bound 2.45 < 3.326 = G*′(x_d) as required; the sign pattern matches
R16's 50-dps grid (negative at all 1718 grid points below x_d, positive at all 281 above).

## Corollary (unconditional violation below x_d)

For every x ∈ (0, x_d): the orthocomplement pair (any real unit ψ, σ = (1−P_ψ)/2) has
G(ψ, σ) = G*(x) < 0, hence **P_b2 fails at every x < x_d** — analytically, with an
explicit exact witness pair (R16 U3 exhibits the rational instance ψ = e₁,
σ = diag(0, 1/2, 1/2)); no optimizer and no sampling enter. Consequently the death point
x_death := sup{ x : P_b2 fails at x } satisfies **x_death ≥ x_d**, where x_d is the root
of G*(x) = 0, x_d = 0.42966287456589232412… (two independent root-finders, 40 digits,
R16 item 2).

**What this does NOT give.** The upper side stays numerical: x_death = x_d (i.e., no
violation ABOVE x_d) is exactly the F1 stratum-global-minimality question, supported by
R16's U4 tracking (global minimum agrees with G* to 5 digits at 4.6·10⁻⁹ below x_d) but
not proved. And per the standing R8 MAJOR-3 wording, no Q-consequence follows from any
P_b2 statement.

## Dependencies

- The stratum-value identity G|_{orthocomplement} = G* — executor-derived (P15-B §4),
  independently re-derived symbolically by R16 (residual exactly 0). This lemma consumes
  the identity as reviewed input; nothing here re-proves it.
- Elementary real analysis only; no numerics load-bearing (the numeric lines above are
  consistency checks, not evidence).

## Review obligation

One fresh-instance rule-7 review of THIS note (type audit trivially: all scalars;
c ≥ 2: the derivative can be checked symbolically and the two bracket bounds are
one-line monotonicity facts; value-vs-formula stated above). Until then this note is
`pending-review:` and the node records the corollary at derived/pending tier.

