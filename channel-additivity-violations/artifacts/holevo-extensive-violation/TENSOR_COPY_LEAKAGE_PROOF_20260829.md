# Tensor-copy leakage and regularized-gap identities

Date: 2026-08-29

Status: proposer-side elementary proof.

## Holevo leakage inequality

For a fixed finite-dimensional pair `N,M`, define

`delta = chi(N tensor M)-chi(N)-chi(M)`,

`a_r = chi(N^r)-r chi(N) >= 0`,

`b_r = chi(M^r)-r chi(M) >= 0`.

Reordering tensor factors and using the product of `r` near-optimal ensembles for `N tensor M`
gives

`chi(N^r tensor M^r) >= r chi(N tensor M)`.

Therefore

`chi(N^r tensor M^r)-chi(N^r)-chi(M^r)`

`>= r delta-a_r-b_r`.                                                        (1)

The self-regularization terms can consume the entire apparent linear gain. A one-copy pair
counterexample alone does not imply a linearly amplified block-pair counterexample.

## Minimum-output-entropy leakage inequality

Define

`Delta = S_min(N)+S_min(M)-S_min(N tensor M)`,

`alpha_r = r S_min(N)-S_min(N^r) >= 0`,

`beta_r = r S_min(M)-S_min(M^r) >= 0`.

A product of `r` near-minimizing inputs for `N tensor M` gives

`S_min(N^r tensor M^r) <= r S_min(N tensor M)`.

Hence

`S_min(N^r)+S_min(M^r)-S_min(N^r tensor M^r)`

`>= r Delta-alpha_r-beta_r`.                                                (2)

Equations (1)--(2) show that sublinear total self-leakage is sufficient for linear amplification,
but they do not establish that hypothesis for any known `p=1` random counterexample pair.

## Exact regularized limits

Let

`C(N)=lim_r chi(N^r)/r`

and

`Sbar_min(N)=lim_r S_min(N^r)/r`.

The first limit follows from superadditivity and the second from subadditivity. Dividing the exact
block-pair defects by `r` gives

`lim_r [chi(N^r tensor M^r)-chi(N^r)-chi(M^r)]/r`

`= C(N tensor M)-C(N)-C(M)`,                                                (3)

and

`lim_r [S_min(N^r)+S_min(M^r)-S_min(N^r tensor M^r)]/r`

`= Sbar_min(N)+Sbar_min(M)-Sbar_min(N tensor M)`.                            (4)

Thus asymptotically linear amplification of a fixed pair is exactly a regularized nonadditivity
question, not a consequence of one-shot nonadditivity.

## Large-gap versus absolute self-leakage bootstrap

For a fixed MOE pair define the absolute regularization losses

`ell_N=S_min(N)-Sbar_min(N)` and `ell_M=S_min(M)-Sbar_min(M)`.

Since `Sbar_min(N tensor M)<=S_min(N tensor M)`, the regularized pair defect obeys the elementary
one-copy lower bound

`Sbar_min(N)+Sbar_min(M)-Sbar_min(N tensor M)`

`>= Delta-ell_N-ell_M`.                                                   (5)

Consequently, an unbounded family of one-shot gaps would solve the fixed-pair regularized problem,
and hence the full-size extensive problem by taking tensor powers of one selected member, if its
two absolute self-leakages were uniformly bounded or merely `o(Delta)`.

The Holevo analogue is

`C(N tensor M)-C(N)-C(M)`

`>= delta-[C(N)-chi(N)]-[C(M)-chi(M)]`.                                   (6)

Equations (5)--(6) expose a stronger use for a large one-shot gap than the copy inequality alone:
the gap can overwhelm a **dimension-independent absolute leakage allowance**. No such allowance is
currently proved for the product-Haar blocks constructed in this project. Montanaro's constant-
loss theorem applies to its own Haar-random subspace ensemble, not automatically to a tensor
product of random-unitary channels, so it cannot be transplanted without a new theorem.

## Fixed-channel cumulative defect is a different quantity

If one fixed channel satisfies `C(N)>chi(N)`, then

`chi(N^n)-n chi(N) = n[C(N)-chi(N)]+o(n)`.

But when `N^n` itself is regarded as a primitive block channel,

`C(N^n)-chi(N^n)=n C(N)-chi(N^n)=o(n)`.

The equality `C(N^n)=nC(N)` follows by taking the regularized Holevo limit along the subsequence of
multiples of `n`. Therefore cumulative coding gain for repeated use of a fixed primitive channel
must not be confused with a family whose *one-shot primitive-size* gap is `Omega(log dimension)`.

## Dimension interpretation

If `N,M` are fixed and (1) or (2) has a positive limiting coefficient, the block dimensions grow
exponentially in `r`, so linear-in-`r` is `Omega(log d_block)`. For a hierarchical construction
whose factor dimensions also grow with the level, the correct cost is the sum of all introduced
input/output logarithmic dimensions; depth alone is not a size certificate. One may equivalently
include the minimal Stinespring environment because its log dimension is at most the sum of the
input and output log dimensions. A nonminimal padded environment is not a legitimate extra cost.
