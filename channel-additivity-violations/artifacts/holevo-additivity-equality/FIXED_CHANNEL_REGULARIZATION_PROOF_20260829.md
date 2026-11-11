# Fixed-channel regularization equivalence

Date: 2026-08-29

## Statement

For a fixed finite-dimensional channel `N`, let

`a_n = chi(N tensor n)`.

Then `C(N) = chi(N)` if and only if `a_n = n a_1` for every positive integer `n`.

## Proof

Product ensembles give

`a_{m+n} >= a_m + a_n`.

Thus `(a_n)` is superadditive. Fekete's lemma and the HSW regularization theorem give

`C(N) = lim_{n to infinity} a_n/n = sup_{n >= 1} a_n/n`.

The same product-ensemble argument also gives `a_n >= n a_1` for every `n`.

If `C(N) = a_1`, then for every `n`,

`a_1 <= a_n/n <= sup_k a_k/k = C(N) = a_1`,

so `a_n = n a_1`.

Conversely, if `a_n = n a_1` for every positive integer `n`, then the regularized formula directly
gives `C(N) = a_1 = chi(N)`.

In particular, a single strict inequality `chi(N tensor n) > n chi(N)` is already sufficient to
prove `C(N) > chi(N)`.

## Source and review gate

Shor writes the finite-dimensional regularized Holevo capacity formula on PDF p. 3 of
`primary-sources/shor-quant-ph-0305035.pdf`, SHA-256
`300a97664fe8d05531230cd6f3a812b23e2c2cbf22c429436e50442993f415d6`.

This sentence records the pre-review state of the proposer-authored proof. The exact claim was
subsequently independently reviewed and promoted to `PROVED`; the canonical
`HAEQ.fixed-channel-regularization` YAML is authoritative for its current status.
