# Strict shifted-duplication comparison

Date: 2026-09-07. Author: parent research agent /root.
Claim owner: GROTHORB.shift-duplication-gap.
The calculation below awaits independent review of both premises and this
route implication. It is a normalization obstruction, not a new bound record.

## GAP-1. Exact matrix identification

Let U contain once each e_i-e_j and e_i+e_j for 1<=i<j<=3.
The twelve rows of W'=[U;-U] are exactly all the signed D3 roots.
They differ from the W in the D3-envelope dossier by a row permutation R.
Since the full normalization denominator is 4(r-1)=8,

  W'W'^T/8 = (1/2)[C,-C;-C,C] = D(C),  C=UU^T/4.

Hence D(C)=R A3 R^T and D(C)-lambda I=R(A3-lambda I)R^T.
Mapping both signs by R is a bijection, so it preserves beta_cl.

## GAP-2. Value comparison

Premise GROTHORB.d3-shift-envelope yields

  beta_cl(D(C)-I_12/3)=8-4/3=20/3,

because 1/3 belongs to [1/4,1/2].
Premise GROTHORB.d3-half-shift-value yields

  2 beta_cl(C-I_6/3)=2*3=6.

Their difference is 2/3>0. Therefore a proof for the half-root shifted
matrix cannot be transferred as an equality by doubling alone. This does
not contradict the unshifted equality or the valid antipodal-strategy lower
bound for shifted matrices.
