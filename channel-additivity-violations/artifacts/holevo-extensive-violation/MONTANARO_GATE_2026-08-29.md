# Montanaro weak-multiplicativity gate — quantitative scope check

Date: 2026-08-29  
Node: `ADDGAP.montanaro-gate`  
Status: negative scope result, not independently reviewed

## Question

Can Ashley Montanaro's weak multiplicativity theorem supply the sublinear single-side leakage

\[
\alpha_s+\beta_s=o(s)
\]

needed to turn `s` matched random-channel/conjugate-channel defects into an extensive
von-Neumann minimum-output-entropy defect?

## Exact theorem data recovered from the arXiv source

Primary source: Ashley Montanaro, *Weak Multiplicativity for Random Quantum Channels*,
[arXiv:1112.5271](https://arxiv.org/abs/1112.5271).

The channel is represented by a Haar-random `r`-dimensional subspace of
`C^(d_A) tensor C^(d_B)`, with `d_A <= d_B`. Put `m=min(d_A,r)`. Under

\[
m\ge 2(\log_2 d_B)^{3/2},
\]

Theorem 3 gives, except with probability at most
`C m^(16/3) 2^(-(m/2)^(2/3))`, weak infinity-norm multiplicativity with exponent

\[
\frac12-\frac{9}{\log_2(d_A d_B/r)}
\quad (r\ge d_B/d_A),
\]

or

\[
1-\frac{9}{\log_2 d_A}
\quad (r\le d_B/d_A).
\]

The paper's von-Neumann corollary is correspondingly

\[
\frac1s H_{\min}(N^{\otimes s})\ge
\frac12(\log d_A+\log d_B-\log r)-C
\]

in the first regime, and

\[
\frac1s H_{\min}(N^{\otimes s})\ge \log d_A-C
\ge H_{\min}(N)-C
\]

in the second. Here `C` is a universal, unoptimised constant. The fixed-channel result is uniform
over every tensor power `s`. The paper separately remarks that the independently sampled
`N_1 tensor ... tensor N_s` version applies when `s` is fixed; it does not state a growing-`s`
probability theorem in that sentence.

## Comparison with the almost-one-bit BCN ensemble

Primary source: Belinschi--Collins--Nechita, *Almost one bit violation for the additivity of the
minimum output entropy*, [arXiv:1305.1567](https://arxiv.org/abs/1305.1567).

Their channels have

\[
\Phi_n:M_{d_n}\to M_k,\qquad d_n\sim tkn,
\]

with output dimension `k`, environment dimension `n`, and Haar-random Stinespring image subspace
of dimension `d_n`. In Montanaro's notation this is

\[
d_A=k,\qquad d_B=n,\qquad r=d_n\sim tkn.
\]

Therefore the almost-one-bit choice `t=1/2`, and more generally every fixed `t>0` at large `k`,
lies in Montanaro's first regime because `tkn >= n/k` is equivalent to `t k^2>=1`.
The resulting lower bound is only

\[
\frac1sH_{\min}(\Phi_n^{\otimes s})
\ge \frac12\log(1/t)-C,
\]

whereas the one-copy minimum output entropy is of order `log k`. Thus the theorem allows a
single-side leakage of order `s log k`; it is much too coarse to protect a matched cross gain of at
most about one bit per factor.

The second Montanaro regime would require `t<=1/k^2`. Even there the displayed theorem gives only
`alpha_s<=Cs`, not `o(s)`. Moreover it does not overlap the BCN near-one-bit choice. A direct
evaluation of BCN's exact entropy vectors gives positive Bell entropy difference at `t=1/k^2` for
`k=183,276,432,1000,10000` (respectively approximately `1.598e-4`, `6.993e-5`, `2.842e-5`,
`5.274e-6`, `5.233e-8` bits), so that boundary does not expose a Bell-state violation in those
checks. This numerical sentence is diagnostic only, not a global theorem.

## Gate verdict

**PARK this route as a consequence of the cited theorem.** Montanaro proves a valuable constant-
fraction/constant-additive weak additivity statement, but it does not imply the required
`alpha_s+beta_s=o(s)`. In the known near-one-bit BCN parameter regime the mismatch is stronger:
the permitted leakage is of order `s log k`.

The route can restart if one proves either:

1. a dimension-dependent per-factor loss `epsilon_k` with `epsilon_k=o(g_k)`, uniformly in all
   tensor powers, where `g_k` is the matched `p=1` gap; or
2. a base pair gap larger than twice the available constant per-factor loss.

The second restart condition is close to the original large-gap problem and therefore is not an
independent solution.

## Public reasoning summary

The key bookkeeping is

\[
\operatorname{gap}(A_s,B_s)
\ge \sum_{i=1}^s g_i-\alpha_s-\beta_s.
\]

A theorem that loses a fixed positive amount per factor gives `alpha_s+beta_s=O(s)`, not `o(s)`.
It can amplify only when its explicit loss coefficient is strictly smaller than the base cross-gap
coefficient. Montanaro's stated constants and the BCN dimension regime do not meet that inequality.

