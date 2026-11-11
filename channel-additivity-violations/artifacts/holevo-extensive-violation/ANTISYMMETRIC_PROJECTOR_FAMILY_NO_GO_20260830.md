# The full antisymmetric-projector family fails the fixed-channel Bell gate

Date: 2026-08-30

Status: proposer-side finite-dimensional obstruction; independent review pending.

All logarithms are base two.  This note concerns only the fixed-channel conjugate-Bell route to
the third Holevo/minimum-output-entropy additivity question.

## Statement

For every integer `d>=2`, let

\[
 P_-^{(d)}=\frac{I-F}{2},\qquad
 r_d=\operatorname{rank}P_-^{(d)}=\frac{d(d-1)}2,
 \qquad
 \alpha_d=\frac{P_-^{(d)}}{r_d}.
\tag{1}
\]

No member of this normalized antisymmetric-projector family supplies the maximally mixed
Stinespring state required by a positive-rate fixed-channel conjugate-Bell certificate:

1. `d=2` is a rank-one, one-dimensional-input constant channel and has zero pair defect;
2. `d=3` has positive entanglement-cost surplus but fails every Gram-positive square-channel
   orientation by the existing polar-sign obstruction; and
3. every `d>=4` fails the necessary entanglement-cost inequality
   `E_C(alpha_d)>S(E)_{alpha_d}/2`.

This is a route obstruction, not a claim that all antisymmetric-state constructions or all
non-Bell inputs are impossible.

## 1. Marginal entropy

The antisymmetric projector is invariant under `U tensor U`.  Its two marginals are therefore
scalar, and the trace fixes

\[
 (\alpha_d)_B=(\alpha_d)_E=\frac{I_d}{d},
 \qquad
 S(E)_{\alpha_d}=\log d.
\tag{2}
\]

## 2. A dimension-independent one-ebit upper bound on entanglement cost

For `1<=i<j<=d`, define the normalized Slater vectors

\[
 |i\wedge j\rangle
 =\frac{|i\rangle|j\rangle-|j\rangle|i\rangle}{\sqrt2}.
\tag{3}
\]

They form an orthonormal basis of the antisymmetric subspace, so

\[
 \alpha_d=\frac1{r_d}\sum_{i<j}|i\wedge j\rangle\!\langle i\wedge j|.
\tag{4}
\]

Every vector in this displayed ensemble has Schmidt spectrum `(1/2,1/2)` and hence exactly one
ebit of entanglement.  By the convex-roof definition,

\[
 E_F(\alpha_d)\le1.
\tag{5}
\]

Entanglement cost is the regularized entanglement of formation.  Subadditivity of `E_F` gives

\[
 E_C(\alpha_d)
 =\lim_{n\to\infty}\frac1nE_F(\alpha_d^{\otimes n})
 \le E_F(\alpha_d)\le1.
\tag{6}
\]

For every `d>=4`, equations (2) and (6) imply

\[
 2E_C(\alpha_d)-S(E)_{\alpha_d}
 \le 2-\log d\le0.
\tag{7}
\]

The strict necessary condition from
`GRAM_CHANNEL_ENTANGLEMENT_COST_GATE_20260830.md` therefore fails before any rectangular
CP-factor or all-copy side-entropy test is attempted.  At `d=4` the upper bound merely saturates
zero, which is still insufficient because the required inequality is strict.

## 3. The two exceptional small dimensions

For `d=2`, `r_2=1` and `alpha_2` is the pure singlet.  An isometry onto its support has a
one-dimensional input.  Tracing either half produces the fixed state `I_2/2`; tensoring two such
constant channels adds their output entropies exactly, so the MOE pair defect is zero.

For `d=3`, `r_3=3` and the cost upper bound does not exclude a strict surplus.  In fact Yura's
exact result gives `E_C(alpha_3)=1`, so `2-log 3>0`.  This is precisely the exceptional square
support case treated in `QUTRIT_ANTISYMMETRIC_GRAM_OBSTRUCTION_20260830.md`: its support channel
has polar sign that is not an inner automorphism, and hence no input/output unitary orientation is
Hilbert-Schmidt positive.  It cannot be a Gram channel.

## Verdict and scope

The dimension split is exhaustive:

\[
 \boxed{\text{Every normalized antisymmetric projector }\alpha_d, d\ge2,
 \text{ fails the fixed-channel conjugate-Bell candidate route.}}
\tag{8}
\]

The proof deliberately uses different obstructions in the three regimes.  The qutrit polar-sign
argument must not be extrapolated to `d>3`, where `r_d!=d` and the support channel is rectangular;
the cost bound (7) is what excludes those dimensions.  No assertion is made about arbitrary
states supported on a proper antisymmetric subspace, coherent mixtures with other supports, or
collective witnesses that are not conjugate Bell inputs.

## Sources

- The necessary cost gate is proved in
  `holevo-extensive-violation/artifacts/GRAM_CHANNEL_ENTANGLEMENT_COST_GATE_20260830.md`.
- The exceptional qutrit orientation obstruction and Yura citation are recorded in
  `holevo-extensive-violation/artifacts/QUTRIT_ANTISYMMETRIC_GRAM_OBSTRUCTION_20260830.md`.
