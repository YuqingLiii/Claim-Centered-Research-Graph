# The smallest reducible-input SU(3) branching cycle has no Bell gap

Date: 2026-08-30

Status: proposer-side finite-family theorem with certified rational interval proof; independent
review pending.

All entropy comparisons are base-independent. The certificate uses natural logarithms.

## 1. The first non-star branching graph

Consider the six-edge cycle with environment vertices

\[
 E_1=V_{(0,2)},
 \qquad E_2=V_{(2,1)},
 \qquad E_3=V_{(1,0)},
\tag{1}
\]

and input vertices

\[
 R_1=V_{(1,2)},
 \qquad R_2=V_{(2,0)},
 \qquad R_3=V_{(0,1)}.
\tag{2}
\]

The incidences are

\[
 R_1\sim(E_1,E_2),
 \qquad R_2\sim(E_2,E_3),
 \qquad R_3\sim(E_3,E_1).
\tag{3}
\]

The total input and environment dimensions are both 24. This is the smallest cycle in the
fundamental `SU(3)` Pieri branching graph; every proper connected subgraph is a previously
classified one-center star or a path.

Give the first incident edge of `R_1,R_2,R_3` squared amplitudes `x,y,z` respectively. The other
edge has squared amplitude `1-x`, `1-y`, or `1-z`. Arbitrary edge phases do not affect the Bell
Gram parameter: each pair of input vertices shares at most one environment, so every off-diagonal
Hilbert--Schmidt contribution contains only an absolute squared amplitude.

## 2. Exact Gram polynomial

Aligning the equivalent input representation bases and evaluating the six Clebsch--Gordan blocks
gives the depolarizing Gram parameter

\[
\begin{aligned}
 t(x,y,z)={}&\frac{41}{128}-\frac{15}{64}x-\frac3{16}y+\frac9{64}z
 +\frac{105}{128}x^2+\frac9{40}y^2+\frac9{128}z^2\\
 &-\frac3{16}xy-\frac3{16}yz-\frac{15}{64}zx.
\end{aligned}
\tag{4}
\]

The matrix reconstruction tool independently builds all six isometries and audits (4) through the
same Bell calculation used in the numerical scan.

## 3. Three explicit side inputs

Choosing a highest-weight state inside one input block gives the three output distributions

\[
 q_x=\left(\frac{1+2x}{3},\frac{2(1-x)}3,0\right),
\tag{5}
\]

\[
 q_y=\left(1-\frac{4y}{5},\frac{2y}{5},\frac{2y}{5}\right),
\tag{6}
\]

and

\[
 q_z=\left(\frac{1+z}{4},\frac{1+z}{4},\frac{1-z}{2}\right).
\tag{7}
\]

Therefore

\[
 S_{\min}(\Phi_{x,y,z})
 \le\min\{H(q_x),H(q_y),H(q_z)\}.
\tag{8}
\]

The Bell entropy is the isotropic entropy `B(t(x,y,z))`.

## 4. Certified box proof

Partition the unit cube into `16^3=4096` rational boxes. On each box:

1. Bound (4) above term-by-term, using the appropriate endpoint for the sign of every monomial.
2. Bound each entropy in (5)--(7) above by checking the two rational endpoints and its sole
   interior maximum (`x=1/4`, `y=5/6`, or `z=1/3`) when present.
3. Bound the decreasing Bell entropy below at the rational upper bound for `t`.
4. Evaluate every logarithm with the rational atanh series and its explicit positive remainder.

Every box satisfies

\[
 B(t)>2\min\{H(q_x),H(q_y),H(q_z)\}.
\tag{9}
\]

The smallest certified natural-log margin is greater than

\[
 1.242827406816\times10^{-2}.
\tag{10}
\]

Combining (8) and (9) proves

\[
 2\overline S_{\min}(\Phi_{x,y,z})
 \le2S_{\min}(\Phi_{x,y,z})
 <B(t(x,y,z))
\tag{11}
\]

for every point of the cycle family.

## 5. Scope

This closes the first genuinely cyclic reducible-input covariant family. It does not classify all
larger branching graphs, repeated cycles, arbitrary multiplicity subspaces on a cycle, or
noncovariant qutrit Gram factors.
