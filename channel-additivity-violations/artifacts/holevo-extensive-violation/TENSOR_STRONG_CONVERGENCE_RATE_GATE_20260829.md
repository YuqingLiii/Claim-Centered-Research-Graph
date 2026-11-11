# Quantitative rate gate for the tensor-strong-convergence construction

Date: 2026-08-29

Status: proposer-side proof-method audit.

## Question

Can the finite-dimensional unbounded-gap construction in
`FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md` already be promoted to a
Hayden--Penington full-size extensive construction by invoking the quantitative estimate behind
Bordenave--Collins Theorem 9.2?

The answer for the **published estimate as currently used** is no. Its tensor-leg and Schatten-
moment losses force the per-leg matrix dimension to grow with hierarchy depth before one even pays
the additional cost of linearizing the degree-`2J` polynomial needed by the entropy proof. This is
a limitation of the available certificate, not a theorem that the true channels lack an extensive
gap.

## The explicit factor

Use `m` for the fixed number of Haar generators per leg, `J` for the number of tensor legs, `D`
for the matrix dimension on each leg, `n` for the coefficient-matrix dimension, and `p` for the
even Schatten moment. Bordenave--Collins Lemma 9.3 gives, for a linear pencil on `J` tensor legs,
an upper factor of the form

\[
 F(D,J,n,p)=
 (2n)^{(J+1)/p}
 D^{J(J+1)/(2p)}
 p^{3J(J+1)/(2p)}
 (1+c/\sqrt D)^J,
\tag{1}
\]

subject to

\[
 2\le p\le D^{\alpha_m},\qquad
 \alpha_m=\frac1{16m+80},
\tag{2}
\]

and `m^70<=D`. Polynomial linearization can only add losses to (1), so it is enough to inspect
the optimistic linear, scalar-coefficient case `n=1`.

## Necessary growth inside this certificate

The entropy construction uses an operator-norm bound `K_D<=F K_free`. In the purity estimate this
costs `F^2`; because there are two side channels, the defect rate loses `4 log_2 F/J`. To retain a
fixed positive fraction of the free coefficient

\[
 c_m=\frac{\log_2m}{m}-2\log_2(1+9/m)>0,
\]

one needs, in particular,

\[
 \frac{\log F}{J}=O(1).
\tag{3}
\]

But the `D` and `p` factors in (1) alone give

\[
 \frac{\log F}{J}
 \ge \frac{J+1}{2p}\log D.
\tag{4}
\]

Thus (3) requires at least

\[
 p=\Omega(J\log D).
\tag{5}
\]

Together with (2), this forces `D^{alpha_m}=Omega(J log D)`, and hence `D=D(J)` must be
unbounded; in particular

\[
 \log D(J)=\Omega(\log J)
\tag{6}
\]

up to the fixed exponent `1/alpha_m=16m+80`. The omitted `p` factor, coefficient uniformization,
and degree-`2J` linearization can only strengthen the required growth.

## Dimension consequence

At depth `J`, each side of the constructed primitive pair acts on dimension `D(J)^J`; therefore
its logarithmic input/output cost contains

\[
 M_J=J\log_2D(J).
\]

The certified defect is `Theta(J)`. Equation (6) means that this proof route, under the published
quantitative factor, can at best have

\[
 \frac{\text{gap}_J}{M_J}=O\!\left(\frac1{\log J}\right)\longrightarrow0.
\]

So Lemma 9.3 does not close the Hayden--Penington full-size extensive target.

## Joint scaling of generator count and depth does not rescue the certificate

The preceding calculation fixed `m`. One might instead try to choose `m=m(J)` so that the
free-model defect grows fast enough to pay for the increasing matrix dimension. The actual
coefficient rules this out for the published certificate.

For every `m`, the certified free defect per tensor leg satisfies

\[
 0<c_m
 =\frac{\log_2m}{m}-2\log_2(1+9/m)
 \le\frac{\log_2m}{m}.
\tag{7}
\]

Lemma 9.3 also assumes `D>=m^70`. Even before the Holevo transfer, the primitive channel has
logarithmic input/output cost at least `J log_2 D`, so the ratio of the certified free lower bound
`Jc_m` to this cost obeys

\[
 \frac{Jc_m}{J\log_2D}
 \le\frac{\log_2m/m}{70\log_2m}
 =\frac1{70m}.
\tag{8}
\]

Therefore every subsequence on which `m(J)->infinity` has certified full-size ratio tending to
zero, even if all convergence and linearization losses are optimistically discarded.

On the complementary case, `m(J)` has an infinite bounded subsequence. Restrict to a fixed value
of `m` occurring infinitely often; if its `c_m` is nonpositive it supplies no gap, while if it is
positive the fixed-`m` argument (4)--(6) forces `log D(J)=Omega(log J)` and again makes the
certified ratio tend to zero.

Hence, for every joint parameter sequence `(m(J),D(J))` admitted by the published estimate,

\[
 \frac{\text{certified defect lower bound}}
 {\text{full primitive logarithmic dimension cost}}
 \longrightarrow0
\tag{9}
\]

along some unbounded-depth subsequence. In particular no uniform positive extensive constant can
be certified. Complementation retains the primitive input dimension `D(J)^J`, even though it can
decrease the output dimension from `D(J)^J` to `m(J)^J`. The subsequent Weyl-label and pair-to-self
reductions add finite dimensional overhead and constant gap losses. Consequently none of these
reductions removes the input cost `J log D(J)` responsible for (9), so they cannot reverse this
certificate obstruction.

This remains a proof-certificate obstruction. Equations (7)--(9) do not upper-bound the true gap
of the realized channels.

## Exact frontier exposed by the audit

One of the following genuinely stronger inputs would be needed:

1. a fixed finite-dimensional base pair with positive **regularized** cross defect, so ordinary
   tensor powers work at bounded per-layer cost;
2. a tensor strong-convergence/operator-space estimate uniform in arbitrarily many tensor legs at
   one fixed finite `D`, with sufficiently small per-leg entropy loss; or
3. a different finite-dimensional family whose per-layer gap grows proportionally to the added
   logarithmic dimension cost.

The current Bordenave--Collins estimate supplies none of these. Conversely, this calculation does
not rule out a better theorem or a different argument for the same random channels.

## Primary source

Charles Bordenave and Benoit Collins, *Norm of matrix-valued polynomials in random unitaries and
permutations*, arXiv:2304.05714v2, Lemma 9.3 and Theorem 9.2, PDF pp. 62--65. Local SHA-256:
`59e14a3334b24f5683d8a0a8919d6cf266cb587f9dbae8d78e8213ca3fe2d8ac`.
