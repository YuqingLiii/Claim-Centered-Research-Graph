# Every translated elementary SU(3) branching cycle has no Bell gap

Date: 2026-08-30

Status: proposer-side all-parameter theorem with an exact rational Bernstein/logarithm
certificate; independent review pending.

All entropy comparisons are base-independent. The executable certificate uses natural
logarithms.

## 1. Infinite translated family

For integers `p>=0` and `q>=2`, take the environment vertices

\[
 E_0=V_{(p,q)},\qquad E_1=V_{(p+2,q-1)},\qquad E_2=V_{(p+1,q-2)}
\tag{1}
\]

and the input vertices

\[
 R_1=V_{(p+1,q)},\qquad R_2=V_{(p+2,q-2)},\qquad R_3=V_{(p,q-1)}.
\tag{2}
\]

Their incidences form the elementary six-edge hexagon

\[
 R_1\sim(E_0,E_1),\qquad
 R_2\sim(E_1,E_2),\qquad
 R_3\sim(E_2,E_0).
\tag{3}
\]

Let `x,y,z` be the squared edge amplitudes in the three input blocks. Each pair of input
vertices shares at most one environment irrep. Consequently every off-diagonal contribution to
the Hilbert--Schmidt Gram norm contains one absolute squared amplitude, and arbitrary edge phases
do not change the Bell Gram parameter.

The case `(p,q)=(0,2)` is the previously certified 24-dimensional minimal cycle. The theorem here
covers every translation of that combinatorial hexagon, with unbounded representation dimensions.

## 2. Exact Gram reduction

For an input irrep `V_(r,s)`, write

\[
 \mu_i=\frac{\dim E_i}{3\dim V_{(r,s)}}.
\tag{4}
\]

If its incident edge weights are `lambda_i`, its diagonal Gram contribution is

\[
 t_{r,s}(\lambda)=\frac18\left(\sum_i\frac{\lambda_i^2}{\mu_i}-1\right).
\tag{5}
\]

The shared-environment calculation adds three bilinear terms. Their mixed coefficients in the
total Gram parameter are

\[
 c_{xy}=-\frac{(q-1)(q+1)}{4q^2},\qquad
 c_{yz}=-\frac{(p+1)(p+3)}{4(p+2)^2},\qquad
 c_{zx}=-\frac{(p+q+1)(p+q+3)}{4(p+q+2)^2}.
\tag{6}
\]

The coefficients of `y^2` and `z^2` come from (5), multiplied by positive dimension ratios, and
are strictly positive. All other dependence on either variable is affine. Thus `t` is separately
convex in `y` and `z`, and

\[
 t(p,q,x,y,z)\le
 \max_{(\epsilon,\delta)\in\{0,1\}^2}
 t(p,q,x,\epsilon,\delta).
\tag{7}
\]

It is therefore enough to certify four rational corner functions.

## 3. One correlated side bound

In the first input block, a highest-weight state has output distribution

\[
 q_x(p)=
 \left(
 x+\frac{1-x}{p+3},
 \frac{(1-x)(p+2)}{p+3},
 0
 \right).
\tag{8}
\]

Therefore

\[
 S_{\min}(\Phi_{p,q,x,y,z})\le H(q_x(p)).
\tag{9}
\]

It is essential that (8) and the Gram parameter retain their common `p,x` dependence. Taking an
independent worst-case Gram bound and an independent worst-case side-entropy bound creates a false
corner which is not realized by any one channel.

## 4. Compact exact certificate

Compactify the two unbounded labels by

\[
 a=\frac{p}{p+1},\qquad b=\frac{q-2}{q-1}.
\tag{10}
\]

Both lie in `[0,1)`, and closure at `a=1` or `b=1` supplies the corresponding limits. After a
positive common denominator is cleared, each corner of (7) is quadratic in `x`, of degree at most
six in `q-2`, and of degree at most seven in `p` (five for the two unequal corners). The exact
denominators before compactification are:

\[
\begin{array}{c|l}
(y,z)&D_{yz}/8\\ \hline
(0,0)&q^2(p+1)(p+2)^2(p+3)(q+1)(p+q+1)(p+q+2)^2\\
(0,1)&q^2(p+1)(p+3)(q-1)(p+q+1)(p+q+2)^2\\
(1,0)&q^2(p+1)(p+3)(q+1)(p+q+2)^2(p+q+3)\\
(1,1)&q^2(p+1)(p+2)^2(p+3)(q-1)(p+q+2)^2(p+q+3).
\end{array}
\tag{11}
\]

The checker evaluates the representation-theoretic formulas using `Fraction`, reconstructs the
unique numerator polynomial on a full tensor interpolation grid, and verifies it at three extra
rational points per corner. It then homogenizes (11) under (10) and converts numerator and
denominator to the same tensor Bernstein basis.

When the denominator control points are positive, the rational function is a convex combination
of the control-point ratios. At the double projective corner, every zero denominator control is
paired with a zero numerator control and is omitted before taking the closure. Dyadic de Casteljau
subdivision therefore gives an exact rational upper bound on `t` in each compact box.

For the side probability

\[
 r(a,x)=x+(1-x)\frac{1-a}{3-2a},
\tag{12}
\]

monotonicity in `a` and `x` gives exact box endpoints. The binary entropy maximum is at the endpoint
nearest `1/2`, or exactly `ln 2` when the interval crosses `1/2`. The decreasing isotropic Bell
entropy

\[
 B(t)=H\left(\frac{1+8t}{9},\frac{1-t}{9},\ldots,\frac{1-t}{9}\right)
\tag{13}
\]

is bounded below at the Bernstein upper bound for `t`. Every logarithm is enclosed by 24 terms of
the rational atanh series plus its explicit positive remainder.

Adaptive subdivision, with depth at most six in each of `a,b,x`, certifies:

\[
\begin{array}{c|c|c}
(y,z)&\text{certified leaf boxes}&\text{smallest natural-log margin}\\ \hline
(0,0)&83&1.875882234131\times10^{-3}\\
(0,1)&96&1.809460759066\times10^{-3}\\
(1,0)&18&2.682824560027\times10^{-2}\\
(1,1)&7&6.534872538794\times10^{-3}.
\end{array}
\tag{14}
\]

Hence for every allowed parameter,

\[
 B(t(p,q,x,y,z))>2H(q_x(p))\ge2S_{\min}(\Phi_{p,q,x,y,z})
 \ge2\overline S_{\min}(\Phi_{p,q,x,y,z}).
\tag{15}
\]

Every translated elementary Pieri hexagon therefore fails the conjugate-Bell route.

## 5. Scope

This is a uniform theorem over infinitely many representation labels and all edge weights; it
supersedes the earlier scan through total base weight 50. It does not classify graphs with two or
more adjacent elementary faces, repeated environment/input vertices, nontrivial cycle
multiplicity, general reducible invariant subspaces on a larger graph, noncovariant qutrit Gram
factors, or non-Bell collective inputs. In particular it does not settle the full-size extensive
question.

Reproduction:

```sh
python3 holevo-extensive-violation/tools/certify_su3_all_elementary_cycles.py
```

