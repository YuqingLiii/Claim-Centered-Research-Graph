# k-Sum L2 phase-8 web feasibility — one-defect multi-pair support

Date: 2026-07-20  
Controlling node: `KSUM.B4b.L2.ALT.multipair`  
Executor: ChatGPT web, High mode  
Conversation: https://chatgpt.com/c/6a5d9dd6-4950-83ea-b17d-02f21d5c2e61  
Tier: proposer only; independent review not performed

## Strategic commission

Test a genuinely two-parameter global profile family:

- `K`: number of simultaneously active complementary value pairs;
- `S`: occupancy scale within active pairs.

The candidate had to remain nontrivial at `q=5`, use growing pair count at `q=N`, attempt a
nonseparable signed kernel, and run low-degree primal-obstruction tests before any exponent claim.

## Formula returned

The smallest family uses a one-sided carrier of size

`R_{k,s}=N-k(s+1)`

and replaces, on each of `k` active complementary pairs,

- NO: `{0,s+1}`;
- YES: `{1,s}`.

The web proposer supplied the non-rank-one coefficient rule

`w_{k,s}=(-1)^(k+s) binom(r,k) binom(u,s) (1+ks)`.

The common boundaries `k=0` and `s=0` cancel termwise. Formal finite-difference moments give a
band of `floor((r+u-3)/2)`. However, the normalized correlation is the alternating interior sum
divided by an `l1` quantity exponential in `r+u`; constant correlation forces `r,u=O(1)`.

## Decisive support-level obstruction candidate

Define the degree-two target-pair statistic

`C_t(x)=sum_{i<j} 1[x_i+x_j=t]`.

On the proposed family,

- `C_t(X_{k,s})=0`;
- `C_t(Y_{k,s})=ks`;
- legality implies `1 <= ks <= N-1` on interior YES profiles.

Thus the target restricted to the whole support is the univariate threshold
`C_t=0` versus `1<=C_t<=N-1`. A Chebyshev approximant to this threshold, composed with the
degree-two polynomial `C_t`, has constant-error query degree `O_tau(sqrt(N))`.

More generally, the proposer states the scoped candidate:

> If every orbit in a support family satisfies `C_t <= M`, then every unit-`l1`, zero-mass,
> correlation-at-least-`tau` invariant dual supported there has pure high degree at most
> `O_tau(sqrt(M))`.

This is coefficient-independent and requires independent review.

## Cap sweep and decision

- `q=5`: the `O(sqrt(N))` support ceiling matches the desired order, but the displayed joint
  kernel itself loses correlation when the occupancy range grows.
- `q=N`: the ceiling misses the `N^(2/3)` target by `N^(1/6)`.
- `q=N^(1/(6 eta))`: the same `N^(1/6)` gap remains.

Decision: **B — precise scoped obstruction theorem candidate.** Stop coefficient tuning on the
one-defect `C_t=O(N)` family. The next registered direction is
`KSUM.B4b.L2.ALT.multipair.highCt-balanced`, requiring nonnegligible mass on profiles with
`C_t=omega(N)`.
