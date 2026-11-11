# Exact cut route audit for the dimension-four candidate

Date: 2026-08-30  
Status: the reduction lemmas below are exact; the global cut inequality remains open.

## D4-CUT1: switching identity

Let `A` be the frozen 300 by 300 integer matrix, let `(a,b)` be the archived
sign strategy, and put

\[
 B_{ij}=a_iA_{ij}b_j,\qquad C=\sum_{ij}B_{ij}
   =2081044153087351400.
\]

For left and right flip sets `S,T`, define

\[
 W(S,T)=\sum_{s_i\mathbin{\mathsf{xor}}t_j=1}B_{ij}.
\]

Termwise comparison before and after the flips gives the integer identity

\[
 \sum_{ij}B_{ij}(-1)^{s_i+t_j}=C-2W(S,T).
\]

Consequently `C` is a global classical upper bound if and only if
`W(S,T)>=0` for every pair of subsets.

## D4-CUT2: exact elimination of the right variables

For fixed `S`, write

\[
 r_i=\sum_jB_{ij},\quad c_j=\sum_iB_{ij},\quad
 q_j(S)=\sum_{i\in S}B_{ij}.
\]

Each right decision is independent after `S` is fixed, hence

\[
 \min_T W(S,T)=
 \sum_{i\in S}r_i+\sum_j\min(0,c_j-2q_j(S)).
\]

This is an exact 600-bit-to-300-bit reduction and supplies an integer leaf
evaluator for a finite proof transcript.

## D4-CUT3: audited failed low-order certificates

The current branch/min-cut verifier is a sound proof system: when every
negative edge has a fixed endpoint its residual min-cut is exact, while at
interior nodes replacing each negative free--free edge by its constant
minimum is a valid lower bound. Independent exhaustive tests on 500 random
bipartite integer instances with at most five vertices on each shore agreed
with brute force on every instance.

For the frozen instance, however, the root lower bounds are far below zero.
The negative-edge relaxation starts at
`-3131353829703088100`; an integer QPBO double-cover leaves 599 variables
unlabelled and gives the same scaled weakness. A cardinality-conditioned
integer lower bound is nonnegative only for cardinalities 0 and 300 and has
minimum

```text
L_165 = -7659798777104361864.
```

The replay program
`artifacts/drafts/d4_cardinality_bound_probe.py` checks the last statement.
These are failures of particular relaxations, not counterexamples to the
global cut inequality.

## D4-CUT4: refutation of the simple positive-path certificate class

Let

```text
N = 3131353829703088100
P = 5212397982790439500
```

be respectively total negative demand and total positive capacity. A
positive-edge path joining the endpoints of a negative edge in the bipartite
graph has odd length and cannot have length one, hence has length at least
three. Any capacity-feasible multicommodity routing of all negative demand
would therefore consume at least

```text
3N = 9394061489109264300 > P,
```

which is impossible. Thus the entire certificate class based on routing
each negative edge through capacity-bounded positive paths is refuted,
including certificates allowing arbitrary path splitting.

## D4-CUT5: exact H4 orbit data and equality faces

The replay program `artifacts/drafts/d4_h4_orbit_support_probe.py` verifies:

- the signed H4 action has order 14400;
- the archived strategy orbit has 2400 distinct pairs and stabilizer order 6;
- the closest nonidentity group image flips 46 left and 40 right signs;
- 18 group elements attain this support 86 minimum;
- party swap has support `(83,83)`.

The six zero right fields are at indices `46,56,85,99,131,148`. They give a
Boolean six-face of equality strategies already at the base witness. The
support-86 result therefore describes the orbit of the selected strategy; it
does not classify every equality strategy.

## D4-CUT6: remaining certificate obligation

A viable finite certificate can use the exact left-only evaluator, a
canonical H4 coverage DAG, equality-face terminals, and exact rational duals
for higher-order local cut inequalities. What has not been established is:

- `W(S,T)>=0` for all cuts;
- completeness of the known equality-face orbits;
- a high-order rational dual closing all non-equality branch regions.

The full implementation audit and proposed transcript format are recorded in
`artifacts/drafts/d4-exact-cut-20260830-agent.md`.
