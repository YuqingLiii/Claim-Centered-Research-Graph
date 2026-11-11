# The conjugate-edge adjacent SU(3) face pair has no Bell gap

Date: 2026-08-30

Status: proposer-side all-parameter theorem with an exact rational Bernstein/logarithm
certificate; independent review pending.

## 1. Orientation and convex reduction

Take the elementary faces based at `(p,q)` and `(p+2,q-1)`, with integers `p>=0,q>=3`. Their
shared incidence has the conjugate branch orientation. The union has environment offsets

\[
 (0,0),(1,-2),(2,-1),(3,-3),(4,-2)
\]

and input offsets

\[
 (0,-1),(1,0),(2,-2),(3,-1),(4,-3)
\]

from `(p,q)`.

Retain the binary weights `u,v` on input offsets `(1,0)` and `(3,-1)`. The shared three-edge input
and the two remaining binary inputs maximize at `3*2*2=12` endpoint patterns by the same
separate-convexity argument as in the middle-edge orientation. Thus the true Gram parameter is
bounded above by the largest of 12 rational functions `t_alpha(p,q,u,v)`.

## 2. Correlated side spectra

The retained highest-weight output probabilities are binary:

\[
 r_u=u+\frac{1-u}{p+3},\qquad
 r_v=v+\frac{1-v}{p+5}.
\tag{1}
\]

Therefore

\[
 S_{\min}(\Phi)\le\min\{h_2(r_u),h_2(r_v)\}.
\tag{2}
\]

The common worst-case Gram branch and these two entropies retain their shared `p,u,v` dependence;
no independent worst-case substitution is made.

## 3. Exact rational certificate

A positive common denominator for all 12 reduced branches is

\[
\begin{aligned}
D={}&8q(p+1)(p+2)(p+3)^2(p+4)(p+5)(q-2)(q-1)(q+1)\\
&\times(p+q+1)(p+q+2)(p+q+3)(p+q+4)\\
&\times(5pq-2p+5q^2+11q-10).
\end{aligned}
\tag{3}
\]

It is strictly positive on `p>=0,q>=3`. After clearing (3), the degree is at most 11 in `p`, 10
in `q`, and 2 in each retained weight. The standard-library checker evaluates the exact
representation formulas with `Fraction`, reconstructs every numerator by tensor Lagrange
interpolation, and verifies each identity at three extra rational points.

With

\[
 a=\frac{p}{p+1},\qquad b=\frac{q-3}{q-2},
\tag{4}
\]

the numerator and denominator are homogenized and converted to a common four-dimensional
Bernstein basis. Matched numerator/denominator zeros at projective boundaries are omitted before
taking the closure; every remaining denominator control is positive. Rational de Casteljau
subdivision gives a rigorous upper bound on all 12 Gram branches.

The probabilities in (1) are monotone in their compact variables. Their binary entropy maxima on
each box are therefore obtained at the endpoint nearest `1/2`, or at `ln 2` if the interval crosses
`1/2`. The Bell entropy is bounded below at the largest rational branch bound. Rational atanh-log
intervals certify 996 adaptive leaf boxes, with smallest natural-log margin greater than

\[
 3.113598803964\times10^{-4}.
\tag{5}
\]

Hence

\[
 S((\Phi\otimes\overline\Phi)(\Omega))
 >2S_{\min}(\Phi)\ge2\overline S_{\min}(\Phi)
\tag{6}
\]

throughout the conjugate-edge adjacent-face family.

## 4. Scope

Together with the middle-edge theorem, this closes two of the three unoriented shared-incidence
types. The distinct highest-edge orientation is now closed by a separate simplex-aware certificate
that retains the shared three-edge input. Three-face graphs, repeated vertices, multiplicities,
noncovariant factors, and non-Bell inputs remain open.

Reproduction:

```sh
python3 holevo-extensive-violation/tools/certify_su3_conjugate_edge_adjacent_faces.py
```
