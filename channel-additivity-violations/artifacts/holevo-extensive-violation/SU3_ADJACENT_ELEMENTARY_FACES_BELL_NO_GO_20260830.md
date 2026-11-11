# A canonical adjacent pair of elementary SU(3) faces has no Bell gap

Date: 2026-08-30

Status: proposer-side all-parameter theorem with an exact rational Bernstein/logarithm
certificate; independent review pending.

All entropy comparisons are base-independent. The executable certificate uses natural
logarithms.

## 1. Graph and exact convex reduction

Join the elementary Pieri face based at `(p,q)` to the face based at `(p+1,q+1)`, for integers
`p>=0,q>=2`. The two faces share one input vertex, one environment vertex, and their incidence
edge. Their union has five input blocks and five environment blocks. The shared input has three
incident environments; the four outer inputs have two each.

For one input block with edge-weight vector `lambda`, its diagonal Gram contribution is

\[
 \frac{\dim R}{8}\left(\sum_i\frac{\lambda_i^2}{\mu_i}-1\right),
 \qquad
 \mu_i=\frac{\dim E_i}{3\dim R}.
\tag{1}
\]

Every off-diagonal shared-environment term is bilinear in weights from two different input blocks.
The total Gram parameter is therefore convex in each input block separately. Arbitrary edge
phases again disappear because any two input vertices share at most one environment.

Retain the weights `u,v` on the two outer inputs of the added face. Maximizing over the other
three blocks reduces exactly to 12 patterns: three vertices of the shared-input simplex and two
endpoints for each of the other two binary blocks. Hence

\[
 t(p,q,\text{all weights})
 \le \max_{\alpha=1}^{12}t_\alpha(p,q,u,v).
\tag{2}
\]

Each branch is quadratic in `u,v`, with one `uv` term.

## 2. Two explicit side blocks

Highest-weight inputs in the retained blocks give

\[
 q_u=\left(u+\frac{1-u}{p+4},\frac{(1-u)(p+3)}{p+4},0\right)
\tag{3}
\]

and

\[
 q_v=(1-v)e_1+v\left(
 \frac1{p+q+5},
 \frac{p+q+4}{(q+1)(p+q+5)},
 \frac{q(p+q+4)}{(q+1)(p+q+5)}
 \right).
\tag{4}
\]

Therefore

\[
 S_{\min}(\Phi)\le\min\{H(q_u),H(q_v)\}.
\tag{5}
\]

Combining (2) and the monotonic decrease of the isotropic Bell entropy reduces the theorem to

\[
 B\left(\max_\alpha t_\alpha(p,q,u,v)\right)
 >2\min\{H(q_u),H(q_v)\}.
\tag{6}
\]

## 3. Exact rational reconstruction

A positive common multiple of the 12 reduced branch denominators is

\[
\begin{aligned}
 D={}&8q(p+1)(p+2)(p+3)(p+4)(q-1)(q+1)(q+2)\\
 &\times(p+q+1)(p+q+2)(p+q+3)^2(p+q+4)(p+q+5)\\
 &\times(5pq+2p+13q+10).
\end{aligned}
\tag{7}
\]

The reduced numerators have degree at most 11 in `p`, 9 in `q`, and 2 in each of `u,v`. The
checker evaluates the exact representation-theoretic formulas with `Fraction`, reconstructs the
unique numerator of every branch on a full tensor interpolation grid, and verifies each identity
at three additional rational points outside the interpolation grid.

Compactify

\[
 a=\frac{p}{p+1},\qquad b=\frac{q-2}{q-1}.
\tag{8}
\]

After homogenization, each branch numerator and denominator is converted to the same tensor
Bernstein basis in `(a,b,u,v)`. Positive denominator controls make the rational value a convex
combination of control-point ratios. At a projective boundary, a zero denominator control is used
only when its numerator control is also zero; the closure is then bounded by all remaining ratios.

## 4. Certified side entropies and result

The binary probability in (3) is monotone in `a,u`, so its entropy maximum on a box is obtained at
the endpoint nearest `1/2`, or at `ln 2` if the interval crosses `1/2`.

For (4), its `c`-row components satisfy:

- the first decreases in both `p,q`;
- the second increases in `p` and decreases in `q`; and
- the third increases in both `p,q`.

Together with linear monotonicity in `v`, this gives exact rational probability intervals. For
`f(r)=-r ln r`, the checker uses endpoint monotonicity outside `[1/3,3/8]` and the rigorous bound
`f(r)<3/8` inside it. The comparisons `1/3<1/e<3/8` are themselves certified by rational-log
intervals. The sum is also capped by a certified upper bound on `ln 3`.

Every Bell entropy is bounded below at the largest of the 12 rational Bernstein branch bounds.
Every logarithm uses the rational atanh series and its explicit positive remainder. Adaptive
dyadic subdivision to depth at most six per coordinate certifies 1,098 leaf boxes. The smallest
natural-log margin is greater than

\[
 1.738276558105\times10^{-5}.
\tag{9}
\]

Consequently

\[
 S((\Phi\otimes\overline\Phi)(\Omega))
 >2S_{\min}(\Phi)\ge2\overline S_{\min}(\Phi)
\tag{10}
\]

for every parameter in this canonical adjacent-face family.

## 5. Scope

This closes the middle-edge orientation obtained from base faces `(p,q)` and `(p+1,q+1)`. The
conjugate- and highest-edge orientations are not assumed equivalent; they are now closed by
separate exact certificates. Graphs with three or more faces, repeated vertices, cycle
multiplicity, noncovariant qutrit factors, and non-Bell inputs remain outside the theorem.

Reproduction:

```sh
python3 holevo-extensive-violation/tools/certify_su3_adjacent_elementary_faces.py
```
