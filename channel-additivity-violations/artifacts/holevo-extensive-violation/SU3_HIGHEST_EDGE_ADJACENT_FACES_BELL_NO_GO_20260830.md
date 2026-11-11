# The highest-edge adjacent SU(3) face pair has no Bell gap

Date: 2026-08-30

Status: proposer-side all-parameter theorem with an exact rational Bernstein/logarithm
certificate; independent review pending.

## 1. Orientation and convex reduction

Take the elementary faces based at `(p,q)` and `(p+1,q-2)`, with integers `p>=0,q>=4`. Their
shared incidence has the highest branch orientation. The union has environment offsets

\[
 (0,0),(1,-2),(2,-4),(2,-1),(3,-3)
\]

and input offsets

\[
 (0,-1),(1,-3),(1,0),(2,-2),(3,-4)
\]

from `(p,q)`.

Retain the shared three-edge input at offset `(2,-2)` and the binary input at offset `(1,0)`.
Write the shared-simplex weights as

\[
 \lambda_h=s,\qquad \lambda_c=(1-s)t,\qquad
 \lambda_m=(1-s)(1-t),
\]

and write the retained binary weight as `w`. Separate convexity reduces the other three binary
input blocks to `2^3=8` endpoint patterns. Thus the true Gram parameter is bounded above by the
largest of eight rational functions `t_alpha(p,q,s,t,w)`.

## 2. Correlated side spectra

For the shared input, put `r=p+2` and `u=q-2`. The three extreme highest-weight output rows are

\[
 K_h=(1,0,0),
\]

\[
 K_m=\left(\frac1{p+4},\frac{p+3}{p+4},0\right),
\]

and

\[
 K_c=\left(
 \frac1{p+q+3},
 \frac{p+q+2}{q(p+q+3)},
 \frac{(q-1)(p+q+2)}{q(p+q+3)}
 \right).
\]

Its explicit side distribution is therefore

\[
 r_{\rm sh}=sK_h+(1-s)tK_c+(1-s)(1-t)K_m.
\tag{1}
\]

For the retained binary input the nonzero probabilities are

\[
 r_w=w+\frac{1-w}{p+3},\qquad 1-r_w.
\tag{2}
\]

Consequently

\[
 S_{\min}(\Phi)\le
 \min\{H(r_{\rm sh}),h_2(r_w)\}.
\tag{3}
\]

The same `p,s,t,w` remain in the Gram and side bounds; no independent maximization discards their
correlation.

## 3. Exact rational certificate

A positive common denominator for all eight Gram branches is

\[
\begin{aligned}
D={}&8q(p+1)(p+2)(p+3)(p+4)(p+q)(q-3)(q-2)(q-1)^2(q+1)\\
&\times(p+q+1)(p+q+2)(p+q+3)\\
&\times(5p^2+5pq+19p+12q+12).
\end{aligned}
\tag{4}
\]

It is strictly positive on `p>=0,q>=4`. The standard-library checker evaluates the exact SU(3)
dimension-barycenter and cross-term formulas with `Fraction`, reconstructs all eight rational
branches by tensor Lagrange interpolation, and checks the reconstruction at three additional
rational points.

Compactify the unbounded labels by

\[
 a=\frac p{p+1},\qquad b=\frac{q-4}{q-3}.
\tag{5}
\]

After projective homogenization, every Gram numerator and denominator is converted to a common
five-dimensional Bernstein basis in `(a,b,s,t,w)`. Matched projective zeros are omitted before
taking control-point ratios; all remaining denominator controls are positive. Exact rational de
Casteljau subdivision bounds the maximum of the eight branches on each box.

The three rational probabilities in (1) are reconstructed over the positive denominator

\[
 (p+4)q(p+q+3).
\tag{6}
\]

Their Bernstein ratio intervals give an upper bound on the ternary entropy by rigorous rational
logarithm intervals. Formula (2) is monotone in `p,w`, so its binary entropy maximum is attained at
the endpoint nearest `1/2`, or is at most `ln 2` when its interval crosses `1/2`. The Bell entropy
is bounded below at the largest certified Gram parameter.

The checker certifies 4,216 adaptive compact leaf boxes. The smallest certified natural-log
margin is greater than

\[
 7.002783706262\times10^{-5}.
\tag{7}
\]

Hence throughout this highest-edge adjacent-face family,

\[
 S((\Phi\otimes\overline\Phi)(\Omega))
 >2S_{\min}(\Phi)\ge 2\overline S_{\min}(\Phi).
\tag{8}
\]

## 4. Scope

Together with the independently certified middle-edge and conjugate-edge orientations, this
closes all three unoriented ways for two elementary SU(3) Pieri faces to share an incidence edge.
This is a Bell-route obstruction only. Three-face graphs, repeated vertices, nontrivial
multiplicity spaces, noncovariant qutrit factors, and non-Bell inputs remain open.

Reproduction:

```sh
python3 holevo-extensive-violation/tools/certify_su3_highest_edge_adjacent_faces.py
```
