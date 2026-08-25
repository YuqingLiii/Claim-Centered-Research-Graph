# k-Sum L2 phase-9 web feasibility — high-Ct balanced splits

Date: 2026-07-21  
Controlling node: `KSUM.B4b.L2.ALT.multipair.highCt-balanced`  
Executor: ChatGPT web, High mode  
Conversation: https://chatgpt.com/c/6a5d9dd6-4950-83ea-b17d-02f21d5c2e61  
Tier: proposer only; independent review not performed

## Commission

Test the support geometry before optimizing coefficients. The target band was

`D_*(N,q)=min{sqrt(N) q^eta, N^(2/3)}` for fixed `eta>1/6`.

The seed family assigned each active complementary pair a total occupancy `S` and split
`(z_i,S-z_i)`, with a one-sided carrier enforcing total occupancy `N`.

## Quantitative tail correction

For a unit-`l1` signed measure `mu`, let `delta_mu(M)` be the absolute mass on `C_t>M`. A
Chebyshev approximant that works on `0<=C_t<=M` can grow rapidly above `M`. The proposer derived
the conditional inequality

`tau <= epsilon_(M,d)(1-delta_mu(M)) + B_(M,d)(Z_N) delta_mu(M)`,

where `Z_N=binom(N,2)` and `B` is the worst tail amplification. At `M=Theta(D^2)` the resulting
general lower bound on `delta_mu(M)` can be exponentially small in
`D log(1+N^2/D^2)`. Therefore pure high degree and constant correlation alone do not imply
constant high-`C_t` absolute mass.

This tail statement is proposer-tier and its displayed normalization requires independent review.

## Explicit single-scale family

The proposer used `K` active complementary pairs with common total occupancy `S`, arbitrary
splits `(z_i,S-z_i)`, and one additional one-sided carrier of size `R=N-KS`. Under
`K_1<=2K_0`, `S_1<=2S_0`, and `K_1S_1<=N/4`, all profiles are legal and the carrier is distinct.
All labeled cube corners collapse to a common NO orbit; interior splits are YES.

The family contains:

- at `q=5`, profiles with `C_t=Theta(N)` under the displayed choice;
- at `q=N`, profiles with `C_t=Theta(N^(4/3))` using
  `K=Theta(N^(2/3))`, `S=Theta(N^(1/3))`;
- analogous capped-endpoint profiles when the pair budget permits.

## Decisive obstruction candidate

Let

- `g_F=min{C_t(omega)>0: omega in F}`;
- `M_F=max{C_t(omega): omega in F}`.

On a single dyadic occupancy scale, every positive pair contribution is at least `S_0-1`, while
the maximum is at most `K_1 S_1^2/4`. The legality window gives

`M_F/g_F=O(N)`.

A gap-sensitive Chebyshev polynomial approximates the threshold on
`{0} union [g_F,M_F]` with query degree `O_tau(sqrt(M_F/g_F))`. Thus the entire single-scale
balanced support class has a proposer ceiling `O_tau(sqrt(N))`, regardless of:

- the signed coefficient law or nonseparability;
- exact cancellation on cube faces;
- the distribution of absolute mass inside the high-`C_t` region;
- constant mass on profiles with `C_t=Theta(N^(4/3))`.

## Strategist audit caveats

The web answer is not ready for completion-tier use:

1. Its displayed `q=5` choice `S=Theta(sqrt(N))`, `K=1` actually gives
   `M/g=Theta(sqrt(N))`, hence the same gate yields `O(N^(1/4))`, not an order-matching
   `O(sqrt(N))` ceiling. The broader class still has the valid loose ceiling `O(sqrt(N))`.
2. Its crossover construction explicitly assumes `eta<=1/4`, although the commission stated
   only `eta>1/6`. The parameter choice must be repaired or the scope narrowed.
3. Several displayed formulas were rendered incompletely in the web transcript. Independent
   review must reconstruct them rather than treat the transcript as a proof.

## Decision

Decision: **B — scoped support-class obstruction candidate.** Stop coefficient work on the
single-dyadic-scale balanced family. Register, but do not yet analyze,
`KSUM.B4b.L2.ALT.multipair.multiscale-splits`: mix parametrically different pair-total scales so
that the support retains `g=O(1)` while reaching `M=Theta(N^(4/3))`.
