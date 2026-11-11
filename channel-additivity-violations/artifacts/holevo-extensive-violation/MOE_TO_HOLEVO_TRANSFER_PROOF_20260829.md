# Exact minimum-output-entropy to Holevo gap transfer

Date: 2026-08-29

Status: proposer-side specialization of Fukuda Lemma 6.2.

## Statement

Let

`Phi: L(C^l) -> L(C^k)` and `Omega: L(C^{l'}) -> L(C^{k'})`

be finite-dimensional channels. Fukuda Lemma 6.2 constructs channels `tilde(Phi)` and
`tilde(Omega)` satisfying, for every `m,n >= 0`,

`chi(tilde(Phi)^m tensor tilde(Omega)^n)`

`= log_2(k^m (k')^n)-S_min(Phi^m tensor Omega^n)`.                 (1)

Here tensor powers are understood and exponent zero means the absent factor.

## Pair-gap identity

Use (1) at `(m,n)=(1,1),(1,0),(0,1)`. Then

`chi(tilde(Phi) tensor tilde(Omega))-chi(tilde(Phi))-chi(tilde(Omega))`

`= [log_2(kk')-S_min(Phi tensor Omega)]`

`  -[log_2 k-S_min(Phi)]-[log_2 k'-S_min(Omega)]`

`= S_min(Phi)+S_min(Omega)-S_min(Phi tensor Omega)`.              (2)

Thus the numerical pair gap is preserved exactly. The construction changes both channels and
their input spaces; this is stronger quantitatively but narrower pointwise than merely invoking
Shor's universal equivalence.

## Dimension budget

Fukuda's displayed construction maps

`tilde(Phi): L(C^{k^2} tensor C^l) -> L(C^k)`.

It therefore adds `2 log_2 k` input qubits and no output qubits beyond the original `k`-dimensional
output. The same holds for `Omega`. If every original logarithmic input/output dimension is `O(m)`,
the extended dimensions remain `O(m)`. Consequently an `Omega(m)` MOE pair gap transfers to an
`Omega(m)` Holevo pair gap.

## Source

`primary-sources/fukuda-1307.0707.pdf`, Lemma 6.2 and Eqs. (6.9)--(6.17), PDF pp. 11-12.
