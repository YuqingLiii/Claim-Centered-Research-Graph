# Exact affine-line L2 maximal inequality on F_3^2

Date: 2026-08-30

Status: proposer-side computer-assisted exact theorem; independent review pending.

## Statement

Let `p` be any probability distribution on the nine points of the affine plane `F_3^2`, and let

\[
 M=\max_{\ell}\sum_{x\in\ell}p_x,
\tag{1}
\]

where the maximum ranges over all 12 affine lines.  Then

\[
 \boxed{\sum_xp_x^2\le M^2.}
\tag{2}
\]

For the qutrit Weyl gate, `sum p_x^2` is the zero-shift autocorrelation `q_0`, hence the largest
entry of `p*tilde p`.  If `L_*` is a direction containing a line of mass `M`, then `M` is the
largest entry of the quotient distribution `r_{L_*}`.  Equation (2) is therefore exactly the
first cumulative-sum condition in

\[
 p*\widetilde p\prec r_{L_*}\otimes r_{L_*}.
\tag{3}
\]

It does not prove the other seven cumulative inequalities in (3).

## 1. Parametric polytope

For a parameter `M in [1/3,1]`, define

\[
 \mathcal P_M=\left\{p\ge0:\sum_xp_x=1,\quad
                 \sum_{x\in\ell}p_x\le M\text{ for all 12 lines }\ell\right\}.
\tag{4}
\]

The collision functional `sum_x p_x^2` is convex.  Its maximum on the compact polytope `P_M` is
therefore attained at a vertex: if a maximizing point is a nontrivial convex combination, at least
one endpoint has value no smaller, and iterating reaches a vertex.

Eliminate one probability using normalization.  The result is an eight-dimensional polytope with
21 affine inequalities: nine point nonnegativity constraints and 12 line-mass constraints.  Every
vertex has eight linearly independent active constraints.  Thus enumerating all

\[
 {21\choose8}=203{,}490
\tag{5}
\]

active sets is complete.

## 2. Exact rank and affine-vertex reconstruction

Every active coefficient matrix has integer entries in `{0,+/-1}`.  Its determinant has absolute
value at most

\[
 (\sqrt8)^8=8^4=4096
\tag{6}
\]

by Hadamard's inequality.  The checker first computes rank modulo the prime `1,000,003`; because
the prime exceeds (6), modular full rank is equivalent to rational full rank.  It then uses
fraction-free elimination to solve each nonsingular active system in the exact form

\[
 p_i(M)=u_i+v_iM,
 \qquad u_i,v_i\in\mathbb Q.
\tag{7}
\]

Intersecting all 21 exact affine inequalities with `[1/3,1]` gives the complete rational
feasibility interval of that vertex family.  Duplicate active bases leading to the same `(u,v)`
are merged only after their exact intervals agree.

The full enumeration contains 107,136 nonsingular active bases, 10,458 feasible active bases,
and 5,238 distinct affine vertex families.

## 3. Exact quadratic verification

For every affine vertex family, the desired gap is the rational quadratic

\[
 f(M)=M^2-\sum_{x=1}^9p_x(M)^2.
\tag{8}
\]

The checker evaluates (8) at both rational interval endpoints and, when the quadratic coefficient
is positive, at its exact rational stationary point if that point lies in the interval.  Every
minimum is nonnegative.  The smallest global value is exactly zero, as required by equality
families; no floating-point comparison participates in the certificate.

Convex vertex reduction and the complete active-set enumeration now prove (2) for every
`M in [1/3,1]`, hence for every probability distribution after choosing its actual maximum line
mass.

## Scope and reproduction

This theorem proves only the largest-entry condition in the selected-line majorization program.
It is independent of the open Shannon-entropy comparison and does not by itself close the qutrit
Weyl Bell route.

Run:

```text
python3 holevo-extensive-violation/tools/certify_f3_affine_line_l2_maximal.py \
  --progress-every 50000
```

Complete transcript:
`holevo-extensive-violation/artifacts/F3_AFFINE_LINE_L2_MAXIMAL_CERTIFICATE_20260830.txt`.

