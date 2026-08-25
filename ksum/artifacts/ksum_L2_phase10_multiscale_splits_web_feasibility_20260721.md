# k-Sum L2 phase-10 web feasibility memo — fixed multiscale splits

Date: 2026-07-21  
Controlling node: `KSUM.B4b.L2.ALT.multipair.multiscale-splits`  
Tier: proposer only; no independent review

## Decision

**B — precise scoped obstruction candidate.** A support using a fixed low-complexity list of
complementary-pair total occupancies is still too easy, even when its positive `C_t` support begins
at `1`, has no single large global gap, and reaches `Theta(N^(4/3))`.

No signed coefficient law was attempted because the support failed the primal gate first.

## Minimal legal two-scale family

Use one micro pair of total occupancy `2`, `K` macro pairs of common total occupancy `S`, and an
optional one-sided carrier of occupancy

`R = N - 2 - K S`.

Legality requires `S>=3`, `K>=1`, `R>=0`, `R=0` or `R>S`, and

`K + 1 + 1[R>0] <= (q-1)/2`.

For the micro pair let `e=0` denote split `{0,2}` and `e=1` denote `{1,1}`. For each macro pair
write the unordered split coordinate as `j_i=min(z_i,S-z_i)`. With

`Q_S = {j(S-j): 0<=j<=floor(S/2)}`,

the exact positive target-pair set is

`A_{K,S} = ({0,1} + K Q_S) \ {0}`,

where `K Q_S` is the `K`-fold Minkowski sum. The unique NO boundary orbit for fixed `(K,S)` has
`e=0` and every macro split on a boundary side.

At `q=5`, only two nonfixed complementary-pair types exist. Thus the legal endpoint specialization
must have no carrier: one micro pair, one macro pair, `S=N-2`. The previously contemplated third
carrier pair is illegal.

## Two-scale obstruction

Because the only pair totals are `2`, `S`, and optionally `R`, constant-degree interpolation in
`n_a+n_{t-a}` isolates the micro and macro scales. This gives an exact constant-degree micro
detector and a macro threshold approximant of degree `O(sqrt(KS))`. Since `KS<=N`, the restricted
target has degree `O(sqrt N)`.

This matches the required order at `q=5`, but is `o(N^(2/3))` at `q=N` and at
`q=N^(1/(6 eta))` for every fixed `eta in (1/6,1/4]`.

## Fixed scale-ladder obstruction

For distinct fixed pair totals `2=S_0<S_1<...<S_L`, fixed counts `K_l`, and optional carrier
`R=N-sum_l K_l S_l`, exact interpolation constructs a selector for scale `l` of degree at most
`L+2`. Composing per-scale target-pair counts with threshold approximants and OR-ing the scales gives

`deg_epsilon(f_t | F) <= C_epsilon (L+4) log(L+1) sum_l sqrt(K_l S_l)`.

By Cauchy-Schwarz and total occupancy at most `N`, this is at most

`C_epsilon sqrt(N) (L+4) sqrt(L+1) log(L+1)`.

For a geometric ladder with `L=O(log N)` the displayed bound is `o(N^(2/3))`; for the explicit
geometric allocation in the web derivation, `sum_l sqrt(K_l S_l)=O(sqrt N)` and the bound becomes
`O(sqrt(N) log(N) log log(N))`.

The hard boundary is: **fixed, low-complexity pair-total scales can be isolated by low-degree
interpolation, reducing 2-Sum to an OR of easy per-scale thresholds.** The conclusion is claimed
for arbitrary split histograms and fully nonseparable signed coefficient laws on that support.

## Tail necessity retained from the derivation

The web derivation also sharpened the phase-9 tail warning. Pure high degree `D` and constant
correlation alone force only exponentially small absolute mass above `C_t=Theta(D^2)` in general;
they do not yield constant high-`C_t` mass. Any eventual dual formula must therefore prove its own
constant high-`C_t` mass gate.

## Caveats

- All claims are new proposer-tier derivations, not source-verified facts.
- The selector/OR bound has not received an independent Rule-7 audit.
- The response's heading called itself a “Phase-9 memo”; this artifact records it as phase 10, the
  actual commission sequence.
- The obstruction does not cover supports in which pair totals themselves vary over a large,
  jointly coupled set, so that isolating one total costs degree comparable to the target band.

## Rule-8 escape named by the web result

Registered before further work:

`KSUM.B4b.L2.ALT.multipair.variable-pair-totals`.

