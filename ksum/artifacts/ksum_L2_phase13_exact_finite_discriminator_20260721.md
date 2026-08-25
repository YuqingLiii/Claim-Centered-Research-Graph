# k-Sum L2 phase-13 web exact finite discriminator

Date: 2026-07-21  
Node: `KSUM.B4b.L2.ALT.multipair.variable-pair-totals`  
Tier: proposer computation; independent reproduction pending

At `N=8,q=5,m=K=2`, exact enumeration gives 24 legal histograms (orbit-list SHA-256
`ca2bd2d9f1539078f43cd96ee0ce0ad70ba1cb5be473040e54c43aebe1bae50a`).

| cutoff | raw rows | exact rank | nullity | modular ranks |
|---|---:|---:|---:|---|
| `D=2` | 2 | 1 | 23 | 1,1,1 |
| `D=8` | 63 | 20 | 4 | 20,20,20 |
| `D=9` | 92 | 24 | 0 | 24,24,24 |

The `D=2` positive control has unit-`l1` correlation 1. At `D=8`, the exact optimum is `1/32`
without a tail constraint and with at least `1/4` absolute mass on `C_t>=4,6,8`. Exact primal
witnesses attain it; an 18-term rational degree-`<8` polynomial has uniform error `1/32` on all 24
orbits. `D=9` zero nullity is the negative control.

Deleting the `(1,1)` row changes nothing because it is exactly redundant, correcting the
preregistration. Perturbing one `C_t` label creates primal residual `1/896` and changes the local
dual error from `1/32` to `19/32`.

Decision B: finite obstruction certificate ready for independent reproduction. This is only the
over-demanding cutoff `D=8`, not asymptotic evidence; the next audit must use cutoffs proportional
to the actual `q=5` target `sqrt(N)`.
