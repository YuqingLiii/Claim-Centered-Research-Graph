# Childs--Eisenberg 2005: quantum subset finding

- **Title:** Quantum Algorithms for Subset Finding
- **Authors:** Andrew M. Childs and Jason M. Eisenberg
- **Version checked:** arXiv:quant-ph/0311038v2
- **Source:** https://arxiv.org/abs/quant-ph/0311038v2
- **Journal:** Quantum Information and Computation 5 (2005), 593
- **DOI:** https://doi.org/10.26421/QIC5.7

## Claim card: general fixed-size subset upper bound

For fixed `L`, finding an `L`-subset satisfying a property that can be checked
without further input queries uses `O(N^(L/(L+1)))` quantum queries. At `L=2`,
this gives the range-independent `O(N^(2/3))` upper bound used by the k-Sum
nodes that link this record.

**Locator in the checked source:** Section 2 of arXiv:quant-ph/0311038v2; the
theorem begins at source lines 276--285.

## Used by

- [`KSUM.B4a`](../proof-dag/nodes/KSUM.B4a.yaml)
- [`KSUM.k2.threshold`](../proof-dag/nodes/KSUM.k2.threshold.yaml)
- [`KSUM.B4b.U1`](../proof-dag/nodes/KSUM.B4b.U1.yaml)
