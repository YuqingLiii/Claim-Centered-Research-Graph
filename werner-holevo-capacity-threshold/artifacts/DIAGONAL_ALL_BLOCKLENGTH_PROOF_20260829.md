# Diagonal inputs at every blocklength

Date: 2026-08-29  
Status: proposer-side analytic proof; independent review pending.

## Statement

Let

\[
\frac25\le x\le\frac12.
\]

For every blocklength `n` and every state diagonal in a real product basis,

\[
\rho^{(n)}=\sum_{j^n}P(j^n)|j^n\rangle\langle j^n|,
\]

with an arbitrary correlated distribution `P`,

\[
\boxed{I_c(\rho^{(n)},\Lambda_x^{\otimes n})\le0.}
\]

The basis may be rotated independently on each qutrit by real orthogonal matrices, by local
`O(3)` covariance.

## The two induced classical channels

Put

\[
p=1-x,\qquad q=x/2.
\]

On a computational-basis input symbol `j in {1,2,3}`, the receiver output is the ternary
symmetric channel `W_B`:

\[
W_B(y|j)=
\begin{cases}
p,&y=j,\\
q,&y\ne j.
\end{cases}
\]

The padded complementary output is the four-output channel `W_E`:

\[
W_E(0|j)=p,
\qquad
W_E(i|j)=
\begin{cases}
0,&i=j,\\
q,&i\ne j.
\end{cases}
\]

For every input symbol the two conditional output distributions have the same nonzero multiset
`{p,q,q}`. Therefore

\[
H(B|J)=H(E|J).
\tag{1}
\]

## Single-letter theorem is a classical more-capable order

For an arbitrary input distribution `r`, the all-real one-copy theorem gives

\[
H(E)-H(B)\ge0.
\]

Using (1), this is equivalent to

\[
I(J;E)-I(J;B)\ge0
\quad\text{for every distribution of }J.
\tag{2}
\]

Thus `W_E` is more capable than `W_B` in the classical sense on this parameter interval.

## Tensorization by a hybrid identity

Let `J^n` have an arbitrary correlated distribution and pass its coordinates through the memoryless
product pair `(W_B^tensor n,W_E^tensor n)`. Define

\[
U_i=(E^{i-1},B_{i+1}^n).
\]

Replacing the receiver coordinates by environment coordinates one at a time gives the exact
telescoping identity

\[
\begin{aligned}
I(J^n;E^n)-I(J^n;B^n)
=\sum_{i=1}^n\bigl[
&I(J^n;E_i|U_i)\\
&-I(J^n;B_i|U_i)
\bigr].
\end{aligned}
\tag{3}
\]

Memorylessness implies

\[
I(J^n;E_i|U_i)=I(J_i;E_i|U_i),
\qquad
I(J^n;B_i|U_i)=I(J_i;B_i|U_i).
\]

Condition on `U_i=u`. This merely selects some distribution for the single input symbol `J_i`, so
the single-letter more-capable inequality (2) applies. Averaging over `u` makes every summand in
(3) nonnegative. Hence

\[
I(J^n;E^n)\ge I(J^n;B^n).
\tag{4}
\]

For a fixed input string, both product channels again have the same conditional entropy, now
`n H(p,q,q)`. Therefore

\[
I(J^n;E^n)-I(J^n;B^n)=H(E^n)-H(B^n),
\]

and (4) is precisely

\[
I_c(\rho^{(n)},\Lambda_x^{\otimes n})=H(B^n)-H(E^n)\le0.
\]

## Scope and obstruction to a stronger shortcut

This theorem permits arbitrary classical correlations across copies, but not off-diagonal quantum
coherences or entangled superpositions.

The stronger classical **less-noisy** order fails throughout `2/5 <= x < 1/2`. Indeed, at

\[
r=(\varepsilon,1-2\varepsilon,\varepsilon),
\qquad v=(1,0,-1),
\]

the receiver-minus-environment relative-entropy Hessian in direction `v` equals

\[
2\left[
\frac{(p-q)^2}{q+(p-q)\varepsilon}
-\frac{q}{1-\varepsilon}
\right],
\]

which is positive whenever

\[
0<\varepsilon<1-\frac{q}{p-q}.
\]

Such an epsilon exists exactly when `x<1/2`. Thus the tensorization above genuinely uses the
more-capable hybrid argument for the conveyed variable `J^n`; it cannot be upgraded to a general
auxiliary-variable/quantum-coherence order below `1/2`.
