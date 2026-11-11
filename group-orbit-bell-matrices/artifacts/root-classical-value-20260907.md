# Exact classical value of the full D_r root projection

Date: 2026-09-07. Author proof for independent review.
Canonical claim owner: `GROTHORB.root-classical`.
Registration: `classical-family-registration-20260907.md`, C1.

This artifact proves the registered base-value formula. It does not assign a
completion level, establish a shifted-family formula, or make a novelty claim.
All linear-algebra identities needed below are proved here; no root-system
classification or other project theorem is a load-bearing premise.

## RC-1: statement and exact conventions

Fix an integer r >= 3. Index the rows of W by

    I_r = {(i,j,alpha,beta): 1 <= i < j <= r,
                              alpha,beta in {-1,+1}}.

The row indexed by (i,j,alpha,beta) is the transpose of

    w_(i,j,alpha,beta) = alpha e_i + beta e_j in R^r.

Thus every signed root is included exactly once, including its antipode, and
n = |I_r| = 4 binom(r,2) = 2r(r-1). Put

    c = 4(r-1),    A_r = W W^T / c,
    beta_cl(A_r) = max_{s,t in {-1,+1}^{I_r}} s^T A_r t.

The assertion is

    beta_cl(A_r) = 2r(2r-1)/3.                         (RC.1)

A matching pair is s=t=s*, where

    s*_(i,j,alpha,beta) = alpha.                      (RC.2)

The maximum here is the signed bilinear maximum. If one instead inserts an
absolute value in its definition, the value is identical because replacing s
by -s negates the objective.

## RC-2: exact reduction from two sign vectors to one

For any sign vector s write z_s = W^T s, and let

    M = max_{s in {-1,+1}^{I_r}} ||z_s||_2.

For every pair (s,t), the Euclidean Cauchy--Schwarz inequality gives

    s^T A_r t = (z_s dot z_t)/c
              <= ||z_s||_2 ||z_t||_2/c <= M^2/c.

The finite sign set contains an s_0 with ||z_(s_0)||_2=M. Choosing
s=t=s_0 gives s_0^T A_r s_0=M^2/c. Therefore

    beta_cl(A_r) = max_s s^T A_r s = M^2/c.           (RC.3)

In particular this step uses the positive Gram representation of A_r; it is
not asserted for a shifted matrix A_r-lambda I.

## RC-3: support-function identity and a global upper bound

For z in R^r one has ||z||_2=max_{||x||_2=1} x dot z: the upper bound
is Cauchy--Schwarz, with equality at x=z/||z||_2 when z is nonzero, and
both sides are zero when z=0. Consequently

    M = max_s max_{||x||_2=1} sum_{w in I_r} s_w (w dot x)
      = max_{||x||_2=1} max_s sum_{w in I_r} s_w (w dot x)
      = max_{||x||_2=1} sum_{w in I_r} |w dot x|.      (RC.4)

The maxima can be interchanged because they are maxima of the same
continuous function on the product of a finite set and the compact unit
sphere. For fixed x the signs are chosen independently, so the last
equality also holds if some w dot x vanishes.

For real a,b,

    |a+b| + |a-b| = 2 max(|a|,|b|).

Indeed, assume |a|>=|b|, replace both a,b by their negatives if necessary
to take a>=0, and observe that a+b and a-b are nonnegative. The other
case follows by interchanging a and b. Hence for each i<j,

    sum_{alpha,beta in {-1,+1}} |alpha x_i + beta x_j|
        = 2(|x_i+x_j|+|x_i-x_j|)
        = 4 max(|x_i|,|x_j|).

Write a_1 >= a_2 >= ... >= a_r >= 0 for the decreasing rearrangement
of (|x_1|,...,|x_r|). Sorting merely permutes the unordered coordinate
pairs, so

    sum_{w in I_r} |w dot x|
      = 4 sum_{i<j} max(|x_i|,|x_j|)
      = 4 sum_{i=1}^r (r-i) a_i.                    (RC.5)

This identity includes ties: the pair in sorted positions i<j contributes
a_i even when a_i=a_j. Since sum_i a_i^2=||x||_2^2=1, a second
Cauchy--Schwarz inequality yields

    sum_{w in I_r} |w dot x|
       <= 4 sqrt(sum_{i=1}^r (r-i)^2).

Let rho=(r-1,r-2,...,1,0), and Q=||rho||_2^2. For r>=3, Q>0,
and x=rho/sqrt(Q) has decreasing nonnegative coordinates and unit norm.
It attains equality above. We have therefore proved the exact identity

    M = 4 sqrt(Q),    M^2 = 16Q,
    Q = sum_{k=0}^{r-1} k^2 = (r-1)r(2r-1)/6.        (RC.6)

This is a global bound over all sign vectors, not an inference from a
finite-r computation.

## RC-4: explicit attaining signs and the value

For each i<j, rho_i>rho_j>=0, so

    sign(alpha rho_i + beta rho_j) = alpha.

In particular none of these root inner products vanishes, and (RC.2) is
also the support-maximizing sign choice at x=rho/sqrt(Q). More directly,
the four roots associated with a fixed pair i<j give

    sum_{alpha,beta} alpha (alpha e_i + beta e_j) = 4e_i.

After summing over all coordinate pairs this gives the exact vector witness

    W^T s* = 4 sum_{i=1}^r (r-i)e_i = 4rho.          (RC.7)

Thus the explicit pair (s*,s*) has value

    (s*)^T A_r s* = 16Q/[4(r-1)]
                  = 4Q/(r-1) = 2r(2r-1)/3.

Equation (RC.3) together with (RC.6) gives the same expression as an
upper bound for every pair (s,t), completing the proof of (RC.1).

## RC-5: computational checks and review boundary

The companion standard-library checker is
`grothendieck-group-orbit/tools/check_root_classical_value.py`.
It constructs the full signed root set, checks the witness (RC.7) using
integer arithmetic for r=3,...,12, and computes the full classical value
at r=3 by enumerating all 2^12 Bob sign vectors and maximizing Alice's
signs exactly. The checker is a normalization and small-instance audit;
the all-r theorem is proved by RC-2 through RC-4.

Reproduction command from the candidate repository root:

    python3 grothendieck-group-orbit/tools/check_root_classical_value.py

No conclusion about shifted classical values or a complete classification
of maximizing sign pairs is needed by this proof. Those would be separate
registered claims. A completion-level assessment of this base theorem
requires an independent review of the exact canonical claim and this
assembled argument.
