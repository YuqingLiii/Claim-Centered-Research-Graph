# The first three cumulative inequalities in the selected-line F_3^2 Weyl majorization

Date: 2026-08-30

Status: proposer-side computer-assisted exact theorem; independent review pending.

## Statement

Let `p` be a probability distribution on `F_3^2`.  Choose an affine line of maximum mass and use
an affine symmetry to make its direction the row direction.  Let the three parallel-line masses be

\[
 a\ge b\ge c,\qquad a+b+c=1.
\tag{1}
\]

Set

\[
 q=p*\widetilde p,
 \qquad r=(a,b,c).
\tag{2}
\]

Then the first three cumulative majorization inequalities hold:

\[
 \sum_{j=1}^k q_j^\downarrow
 \le
 \sum_{j=1}^k(r\otimes r)_j^\downarrow,
 \qquad k=1,2,3.
\tag{3}
\]

The result at `k=1` is the exact affine-line `L2` maximal theorem.  The new certificate proves
`k=3`; the middle case follows by averaging those two inequalities.

## 1. Reduction of k=3 to four collision bounds

Write the nonzero autocorrelation coefficients in the four projective directions as

\[
 q_{g_i}=q_{-g_i}=x_i,qquad i=1,\ldots,4.
\tag{4}
\]

The zero coefficient `q_0=sum_xp_x^2` is the largest by Cauchy--Schwarz.  Therefore

\[
 \sum_{j=1}^3q_j^\downarrow=q_0+2\max_i x_i.
\tag{5}
\]

For the line direction `L_i`, let `r_i=p mod L_i` be its three affine-line masses.  Two independent
samples have the same quotient exactly when their difference lies in `L_i`, so

\[
 C_i:=\sum_t r_i(t)^2=q_0+2x_i.
\tag{6}
\]

Hence the left side of (3) at `k=3` is `max_i C_i`.  On the product side, (1) makes the three
largest entries of `r tensor r` equal to `a^2,ab,ab`.  It remains to prove, for every direction,

\[
 C_i\le a^2+2ab.
\tag{7}
\]

## 2. Six-dimensional parametric polytope

Fix `(a,b)` and put `c=1-a-b`.  Eliminate one probability from each row:

\[
 p_{02}=a-p_{00}-p_{01},\quad
 p_{12}=b-p_{10}-p_{11},\quad
 p_{22}=c-p_{20}-p_{21}.
\tag{8}
\]

The six remaining point probabilities are constrained by nine nonnegativity inequalities and the
nine nonparallel affine-line bounds `mass<=a`.  The parameter domain is

\[
 1/3\le a\le1,qquad a\ge b\ge1-a-b\ge0.
\tag{9}
\]

For fixed parameters, every `C_i` is a convex quadratic in the six free point probabilities.
Consequently its maximum is attained at a polytope vertex.  Every vertex has six independent
active constraints, so all

\[
 {18\choose6}=18{,}564
\tag{10}
\]

active sets suffice.

## 3. Exact affine families and polygon minima

The checker uses modular rank followed by fraction-free elimination to reconstruct each vertex as

\[
 p_j(a,b)=u_j+v_ja+w_jb
\tag{11}
\]

over the rationals.  The six-row determinant bound is at most `(sqrt(6))^6=216`, below the rank
prime `1,000,003`, so the modular rank gate is exact.  Intersecting every original inequality with
(9) gives an exact rational polygon in the `(a,b)` plane.

The enumeration contains 11,934 nonsingular active bases, 3,123 feasible active bases, and 2,367
distinct affine vertex families.  For each family and all four directions, the gap

\[
 a^2+2ab-C_i(p(a,b))
\tag{12}
\]

is a rational quadratic on its parameter polygon.  The checker evaluates every polygon vertex,
every exact stationary point on every vertex-pair segment (thereby including all edges), and every
interior stationary point.  Singular stationary sets meet the polygon boundary, already included
in the segment checks.  All exact minima are nonnegative; the global minimum is zero.

This proves (7) and hence `k=3`.

## 4. The k=2 interpolation

Let `Q_k` and `R_k` denote the top-`k` cumulative sums of `q` and `r tensor r`.  The paired form
(4) gives

\[
 Q_2={Q_1+Q_3\over2}.
\tag{13}
\]

Likewise the three largest product entries `a^2,ab,ab` give

\[
 R_2={R_1+R_3\over2}.
\tag{14}
\]

The exact inequalities at `k=1` and `k=3` therefore imply `Q_2<=R_2`.  Equations (3) follow.

## Scope and reproduction

The theorem leaves cumulative indices `k=4,...,8` open and therefore does not yet prove the full
majorization or the Shannon Weyl no-go.

Run:

```text
python3 holevo-extensive-violation/tools/certify_f3_weyl_majorization_first_three.py \
  --progress-every 5000
```

Complete transcript:
`holevo-extensive-violation/artifacts/F3_WEYL_MAJOR_FIRST_THREE_CERTIFICATE_20260830.txt`.

