# Ambainis--Balodis--Iraids 2021: small-range claw recurrence

- **Title:** A note about claw function with a small range
- **Authors:** Andris Ambainis, Kaspars Balodis, and Janis Iraids
- **Version checked:** arXiv:2103.16390v1
- **Source:** https://arxiv.org/abs/2103.16390v1

## Claim card: upper bound and recurrence

For two functions with domain size `n` and range size `k`, the paper states an
`O(n^(1/2+epsilon) k^(1/4))` quantum-query upper bound. Its recursive exponent
calculation is the external construction adapted and rechecked in the local
k-Sum upper-bound record.

**Locator in the checked source:** the upper-bound statement appears in
`claw.tex` lines 135--143, and the recurrence calculation appears in lines
240--286 of the arXiv v1 source.

## Used by

- [`KSUM.B4a`](../proof-dag/nodes/KSUM.B4a.yaml)
