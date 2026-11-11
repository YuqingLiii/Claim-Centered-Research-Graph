# Pair-to-self Holevo reduction

Date: 2026-08-29

## Statement

Let `N` and `M` be finite-dimensional channels and suppose

`chi(N tensor M) = chi(N) + chi(M) + delta`

for some `delta > 0`. Define the classical-flag direct-sum channel

`T = N direct_sum M`.

Then `chi(T tensor T) > 2 chi(T)`.

## Inputs

Fukuda-Wolf Proposition 1(4) gives, for finite direct sums,

`chi(direct_sum_i T_i) = log_2(sum_i 2^{chi(T_i)})`.

We also use product-ensemble superadditivity

`chi(A tensor B) >= chi(A) + chi(B)`

and invariance of `chi` under input/output swap unitaries, so
`chi(M tensor N) = chi(N tensor M)`.

## Proof

Write `a = chi(N)` and `b = chi(M)`. The direct-sum identity gives

`chi(T) = log_2(2^a + 2^b)`.

The tensor square is a four-block flagged channel:

`T tensor T = (N tensor N) direct_sum (N tensor M)`
`              direct_sum (M tensor N) direct_sum (M tensor M)`.

Consequently,

`2^{chi(T tensor T)}`
` = 2^{chi(N tensor N)} + 2^{chi(N tensor M)}`
`   + 2^{chi(M tensor N)} + 2^{chi(M tensor M)}`
` >= 2^{2a} + 2 * 2^{a+b+delta} + 2^{2b}`
` > 2^{2a} + 2 * 2^{a+b} + 2^{2b}`
` = (2^a + 2^b)^2`
` = 2^{2 chi(T)}.`

The base-2 logarithm is strictly increasing, hence

`chi(T tensor T) > 2 chi(T)`.

All spaces are finite because direct sums and tensor products of the original finite-dimensional
spaces remain finite-dimensional. No balancing side channel and no assumption about
`chi(N tensor N)` or `chi(M tensor M)` beyond ordinary product-ensemble superadditivity is needed.

## Consequence for classical capacity

The regularized unassisted classical capacity satisfies

`C(T) = sup_{n >= 1} chi(T tensor n)/n`.

Therefore

`C(T) >= chi(T tensor T)/2 > chi(T)`.

## Dependencies and review gate

- Primary identity: Fukuda-Wolf, arXiv:0704.1092v2, Proposition 1(4), statement on PDF p. 1 and proof on PDF p. 2.
- Same-vs-pair formulation: ibid., Proposition 2(2) and proof, PDF p. 3.
- Local source: `primary-sources/fukuda-wolf-0704.1092.pdf`, SHA-256
  `1a8890f8484d450894545190d306efd67b57ee7f646fc45be1e4a26fe6b653b7`.

This proof is proposer-authored. Promotion to a completion tier requires independent review of the
frozen statement and algebra.
