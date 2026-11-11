# Selected-line majorization for qutrit Weyl autocorrelations

Date: 2026-08-30

Status: proposer-side computer-assisted exact theorem; independent review pending.

## Statement

Let `p` be a probability distribution on `F_3^2`, let

\[
 q=p*\widetilde p,
\]

and choose a direction containing a maximum-mass affine line.  If `r=(a,b,c)` is the vector of
the three parallel-line masses in decreasing order, then

\[
 \boxed{q\prec r\otimes r.}
\tag{1}
\]

Consequently

\[
 H(p*\widetilde p)\ge 2H(r)
 \ge 2\min_L H(p\bmod L).
\tag{2}
\]

This closes the classical Shannon gate for the fixed-qutrit Weyl random-unitary conjugate-Bell
route.  It does not settle the full-size extensive Holevo/MOE question.

## 1. Paired form and the odd-index reduction

Use an affine symmetry to make the selected parallel class the three rows and write

\[
 a\ge b\ge c,\qquad a+b+c=1.
\tag{3}
\]

The autocorrelation has the paired form

\[
 q=(q_0,x_1,x_1,x_2,x_2,x_3,x_3,x_4,x_4)
\tag{4}
\]

before sorting, with `q_0` its largest entry.  If `Q_k` and `R_k` are the sorted cumulative sums
of `q` and `r tensor r`, the equal pairs in (4) imply

\[
 Q_{2j}={Q_{2j-1}+Q_{2j+1}\over2},\qquad j=1,2,3,4,
\tag{5}
\]

where `Q_9=1`.  Sortedness of `r tensor r` gives

\[
 R_{2j}\ge {R_{2j-1}+R_{2j+1}\over2}.
\tag{6}
\]

Thus it suffices to prove cumulative indices `k=1,3,5,7`.  The exact affine-line and
parametric-vertex certificates already establish `k=1,3`, and `k=2` follows from (5)-(6).

## 2. The stronger k=5 inequality

For the four projective directions let

\[
 C_i=\sum_t r_i(t)^2=q_0+2x_i
\tag{7}
\]

be the collision probability of the corresponding three-line quotient.  Then

\[
 Q_5=\max_{i<j}(C_i+C_j-q_0).
\tag{8}
\]

The five largest entries of `r tensor r` have sum

\[
 R_5=a^2+2ab+ac+\max\{b^2,ac\}
 \ge a^2+2ab+2ac=2a-a^2.
\tag{9}
\]

The exact checker proves the stronger six inequalities

\[
 C_i+C_j-q_0\le2a-a^2\qquad(i<j).
\tag{10}
\]

Equations (8)-(10) give `Q_5<=R_5`.

## 3. The k=7 inequality

Let `y_4=min_i x_i`.  The two smallest entries of `q` are both `y_4`, whereas the two smallest
entries of `r tensor r` are `c^2` and one copy of `bc`.  Hence

\[
 Q_7=1-2y_4,
 \qquad
 R_7=1-c^2-bc.
\tag{11}
\]

The exact checker proves, for all four projective directions,

\[
 2x_i\ge c(b+c).
\tag{12}
\]

Taking the minimum over `i` in (12) proves `Q_7<=R_7`.

## 4. Exact polytope and KKT completeness

Eliminate the ninth point probability using normalization.  The remaining eight variables obey
twenty affine inequalities:

- nine point nonnegativity inequalities;
- `a-b>=0` and `b-c>=0`;
- the nine bounds saying that every affine line outside the selected parallel class has mass at
  most `a`.

This compact rational polytope represents every distribution after the affine normalization in
(3).  Both (10) and (12) are quadratic inequalities on it.

For each quadratic, the checker enumerates every linearly independent active set of size at most
eight.  At a minimum, the gradient belongs to the polyhedral normal cone, so a nonnegative KKT
representation exists on an independent active subset.  Complete enumeration therefore contains
the minimizer's KKT system.  If that system is singular after a basis for the full active-normal
span is chosen, its null vector is tangent to the face and the quadratic is constant along that
direction; the same minimum is attained on a proper subface.  Choosing a global minimizer on a
face of minimal dimension rules this out.  It is consequently sufficient to retain the exact
nonsingular KKT solutions and test primal feasibility, nonnegative multipliers, and the rational
objective value.

Modular elimination certifies the common nonsingular cases.  A zero modular determinant is never
discarded: the fraction-free rational solver decides it exactly.  The complete counts are:

| condition | active sets | independent sets | nonsingular KKT systems | feasible | dual feasible | minimum |
|---|---:|---:|---:|---:|---:|---:|
| stronger `k=5` | 263,950 | 232,006 | 1,327,083 | 49,683 | 12,777 | 0 |
| `k=7` | 263,950 | 232,006 | 881,269 | 38,367 | 17,773 | 0 |

No exact candidate has negative gap.  This proves (10) and (12).

## 5. Completion of majorization

The exact results at `k=1,3,5,7`, followed by (5)-(6), prove all eight nontrivial cumulative
inequalities.  Equality of the ninth cumulative sum is normalization.  Equation (1) follows, and
Shannon's Schur concavity gives (2).

## Reproduction and scope

Run:

```text
python3 holevo-extensive-violation/tools/certify_f3_weyl_majorization_k5.py --progress-every 25000
python3 holevo-extensive-violation/tools/certify_f3_weyl_majorization_k7.py --progress-every 25000
```

The earlier `k=1,2,3` certificates are linked from their atomic nodes.  New terminal transcripts:

- `holevo-extensive-violation/artifacts/F3_WEYL_MAJOR_K5_CERTIFICATE_20260830.txt`
- `holevo-extensive-violation/artifacts/F3_WEYL_MAJOR_K7_CERTIFICATE_20260830.txt`

The theorem is exact but computer-assisted and proposer-side.  Independent review must audit the
affine normalization, the odd-index interpolation, both quadratic objectives, the polyhedral KKT
completeness argument, the exact solvers, and the recorded counts before any completion-level
promotion.
