# L3 critical endpoint: non-sampling upper attacks

Date: 2026-07-21  
Scope: the exact hidden-frequency promise at `q=Theta(N^(2/3))`  
Method: local corpus only; no web; **no DAG or status file edited**

## 1. Outcome

None of the three registered non-sampling attacks gives an `o(N^(2/3))` algorithm on the
frozen endpoint promise.  The optimized ledgers are:

| registered node | best fully costed construction in scope | endpoint cost | verdict |
|:---|:---|:---|:---|
| `...ALT.duplicate-classification` | indexed duplicate-role test followed by cross-list search, with ideal variable-time composition | `O-tilde(sqrt(Nq))=O-tilde(N^(5/6))` | worse than the cap; exact singleton generation followed by a walk is `O-tilde(N^(17/18))` |
| `...ALT.frequency-aware-joint-walk` | soft duplicate filter plus weighted distinct-label down-up walk | minimum `Theta(N^(2/3))`, attained by applying no filter | matches ordinary Johnson; every nontrivial filtering regime tested is worse |
| `...ALT.joint-statistic-estimation` | support-intersection or missing-label search with ideal variable-time role synthesis | `O-tilde(sqrt(Nq))=O-tilde(N^(5/6))` | worse than the cap; the collision and dense-cell estimators are still slower |

Thus the best algorithm found after cross-comparing the three families remains the ordinary
two-list Johnson/MNRS walk,

\[
 Q=\Theta(N^{2/3})=\Theta(q).
 \tag{NS.1}
\]

This is an upper-attack audit, not a query lower bound.  The negative statements below are exact
only for the explicitly parameterized constructions and oracle-synthesis methods.  In particular,
they do not exclude a different coherent joint transform.

The exact orbit and its lossless 2-SUM embedding are in
[the frozen-promise memo](ksum_L3_hidden_frequency_promise_20260721.md).  The earlier sampling
attack is in [the endpoint upper audit](ksum_L3_hidden_frequency_upper_attack_20260721.md), and the
best current adversary calculation is in
[the critical adversary attempt](ksum_L3_hidden_frequency_critical_adversary_attempt_20260721.md).

## 2. Endpoint normalization

Write `n=floor(N/2)` for each list length, `a=floor(q/4)` for the number of singleton labels and
also the number of heavy labels on each side, and use `h` for either legal heavy multiplicity
`d` or `d+1`.  Constants and rounding do not affect the following ledgers.  At the endpoint,

\[
 a=\Theta(q),\qquad h=\Theta(N/q),\qquad
 q=\Theta(N^{2/3}),
 \tag{NS.2}
\]

and it is useful to remember the equivalent scale identities

\[
 q=\Theta(h^2),\qquad N=\Theta(h^3).
 \tag{NS.3}
\]

Each side contains `Theta(q)` singleton positions and `Theta(N)` heavy positions.  NO has
disjoint supports.  YES changes only the following four low-frequency histogram cells:

\[
 \Delta H_{1,1}=+1,
 \quad \Delta H_{1,0}=-1,
 \quad \Delta H_{0,1}=-1,
 \quad \Delta H_{0,0}=+1.
 \tag{NS.4}
\]

The `(1,1)` label is the unique cross-list match.  All heavy labels are side-exclusive.

## 3. Verdict for `...ALT.duplicate-classification`

### 3.1 Correct coherent cost of the same-side role test

Suppose an occurrence `i` and its queried value `v=x_i` are already stored.  Search the other
`n-1` positions of that same list for `v`.  The promise is

\[
 K_v=0\quad\hbox{or}\quad K_v\in\{h-1,h\}.
 \tag{NS.5}
\]

A promise-calibrated bounded-error Grover test therefore costs

\[
 C_{\rm role}=\widetilde\Theta\!\left(\sqrt{n/h}\right)
              =\widetilde\Theta(\sqrt q)
              =\widetilde\Theta(N^{1/3}).
 \tag{NS.6}
\]

This cost applies on **both** branches.  In particular, a singleton does not require a
`sqrt(N)` exhaustive certification: the algorithm only has to distinguish zero duplicates from
at least `h-1` duplicates.  A one-sided search leaves the singleton flag negative; standard
error reduction, copying the decision bit, and uncomputing the search workspace add only
polylogarithmic and constant factors.  This corrects the tempting but inaccurate branch ledger
in which the same-side singleton test itself was charged `sqrt(N)`.

The long negative branch occurs one level later.  Once `i` is certified singleton, deciding
whether the opposite list contains `v` is a zero-versus-one search and costs

\[
 C_{\rm cross}=\Theta(\sqrt n)=\Theta(\sqrt N)
 \tag{NS.7}
\]

on every nonshared singleton and also on the unique accepting singleton.  The YES branch is not
allowed to stop after role classification: its same-side duplicate flag is negative, and the
full cross search must run before it can accept.

### 3.2 Indexed variable-time attack

Use a left position as the outer search index.  Its branch algorithm is:

1. query and store its value;
2. run the coherent role test (NS.6);
3. stop and reject if heavy;
4. if singleton, run the opposite-list search (NS.7), verify equality, and uncompute.

There are `Theta(N)` heavy branches of time
`T_H=O-tilde(sqrt(q))` and `Theta(q)` singleton branches of time
`T_S=O-tilde(sqrt(N))`.  Even granting the most favorable root-sum-square variable-time search
composition (and suppressing its logarithms), the outer cost is

\[
 \begin{aligned}
 C_{\rm VT}
 &\;=\widetilde O\!\left(
       \sqrt{\Theta(N)T_H^2+\Theta(q)T_S^2}\right)\\
 &\;=\widetilde O(\sqrt{Nq})
  =\widetilde O(N^{5/6}).
 \end{aligned}
 \tag{NS.8}
\]

The additive maximum branch time `sqrt(N)` is smaller.  Equation (NS.8) includes all
`Theta(q)` negative singleton branches and the accepting branch.  A uniform fixed-time
composition can only be worse.

### 3.3 Trying to manufacture singleton access

A uniformly random position is singleton with probability

\[
 p_S=\Theta(q/N)=\Theta(1/h).
 \tag{NS.9}
\]

Combining the role test with amplitude amplification prepares one uniformly random singleton
occurrence at cost

\[
 A_S=\widetilde\Theta(\sqrt q/\sqrt{p_S})
    =\widetilde\Theta(\sqrt N).
 \tag{NS.10}
\]

This already prevents cheap random access to the virtual singleton lists.  For completeness,
give that access mechanism to a product Johnson walk on `r` singleton positions per side.  Its
state stores both `r`-subsets and their queried values; setup is `S=Theta(r A_S)`, update is
`U=Theta(A_S)`, checking stored cross equality is free, the gap is `delta=Theta(1/r)`, and the
YES marked fraction is

\[
 \varepsilon=\Theta((r/q)^2).
 \tag{NS.11}
\]

The MNRS ledger becomes

\[
 C_S(r)=\widetilde\Theta\!\left[
 A_S\left(r+{q\over\sqrt r}\right)\right].
 \tag{NS.12}
\]

It is minimized at `r=Theta(q^(2/3))`, giving

\[
 \min_r C_S(r)
 =\widetilde\Theta(\sqrt N\,q^{2/3})
 =\widetilde\Theta(N^{17/18}).
 \tag{NS.13}
\]

### 3.4 Duplicate-classification verdict

The corrected role oracle is cheaper than previously feared, but it does not expose the answer.
The unavoidable zero-versus-one cross check remains long on a `Theta(q/N)` fraction of position
branches.  The best direct variable-time construction is (NS.8), and explicitly generating the
singleton domain is worse by (NS.13).  Therefore this tested duplicate-classification family
does not beat the cap.  This is not a lower bound against a global coherent classifier that is
not decomposable into these indexed branches.

## 4. Verdict for `...ALT.frequency-aware-joint-walk`

### 4.1 Baseline that must be beaten

The ordinary state space is `J(n,r) x J(n,r)`.  A state stores the queried values in one
`r`-subset from each list.  Its complete ledger is

\[
 S=\Theta(r),\quad U=\Theta(1),\quad C=0,
 \quad\delta=\Theta(1/r),\quad
 \varepsilon=\Theta((r/n)^2)
 \tag{NS.14}
\]

on YES with its unique marked pair.  Hence

\[
 C_J(r)=\Theta\!\left(r+{N\over\sqrt r}\right),
 \qquad
 \min_r C_J(r)=\Theta(N^{2/3})
 \tag{NS.15}
\]

at `r=Theta(N^(2/3))=Theta(q)`.

Simply conditioning on labels that look distinct inside the current subset does not change this.
For a sampled occurrence of a heavy label, the chance that another one of its `h-1` copies lies
in an `r`-subset is `Theta(rh/N)=Theta(r/q)`.  Thus at `r=o(q)`, a `1-o(1)` fraction of sampled
heavy occurrences still look locally unique; at `r=Theta(q)`, setup has already reached the cap.

### 4.2 A nontrivial soft-filtered weighted walk

Here is an explicit frequency-aware construction.  On each side, let a `t`-query one-sided
duplicate detector accept all singleton occurrences and accept a heavy occurrence with
probability `alpha=alpha_t`.  Starting from a uniform position, its total acceptance probability
and accepted label weight are

\[
 P=\Theta\!\left({1+\alpha h\over h}\right),
 \qquad
 W=\Theta\!\left(q(1+\alpha h)\right).
 \tag{NS.16}
\]

One singleton label has weight `1`; one heavy label has weight `alpha h`.  A coherent accepted
representative can be proposed, including value query, filter, amplification, error reduction,
and uncomputation, at cost

\[
 A=\widetilde\Theta\!\left(
       (t+1)\sqrt{h\over1+\alpha h}\right).
 \tag{NS.17}
\]

For each side, take the heat-bath/down-up chain on `r` distinct labels with stationary weight

\[
 \pi(S)\ \propto\ \prod_{v\in S}w_v,
 \tag{NS.18}
\]

and store one accepted representative occurrence per label.  An update deletes a uniform stored
label and proposes a filtered occurrence whose label is not among the retained labels.  For
`r<=c q` with a sufficiently small fixed `c`, the exclusion rejection probability is bounded
away from one because `max_v w_v/W=O(1/q)`.  The two-list walk uses the product of the left and
right chains and marks a state iff the two stored label sets intersect.

The resulting explicit cost ledger is

\[
 S=\widetilde\Theta(rA),\qquad
 U=\widetilde\Theta(A),\qquad C=0.
 \tag{NS.19}
\]

Give the attack the favorable standard down-up gap `delta=Theta(1/r)`; any smaller gap only
increases the cost.  For `r<=c q`, the unique shared singleton has marginal inclusion probability
`Theta(r/W)` on each side, so

\[
 \varepsilon=\Theta((r/W)^2).
 \tag{NS.20}
\]

The full MNRS expression is therefore

\[
 C_{\rm fw}(r,t)
 =\widetilde\Theta\!\left[
 A\left(r+{W\over\sqrt r}\right)\right].
 \tag{NS.21}
\]

If the formal optimizer `r=Theta(W^(2/3))` reaches `Theta(q)`, setup alone is already the cap;
otherwise substituting it gives

\[
 \min_r C_{\rm fw}(r,t)
 =\widetilde\Theta(AW^{2/3}).
 \tag{NS.22}
\]

### 4.3 Optimizing the filter strength

A heavy duplicate occupies a `Theta(1/q)` fraction of the same-side search domain.  With
`t=o(sqrt(q))=o(h)` duplicate queries, the probability of finding it is `O(t^2/q)=o(1)`.
Consequently

\[
 \alpha=1-o(1),\qquad W=\Theta(qh)=\Theta(N),
 \tag{NS.23}
\]

and (NS.21)--(NS.22) cost at least the ordinary `Theta(N^(2/3))` scale.  The minimum in this
regime is attained at `t=0`: do not filter.

Conversely, lowering heavy acceptance by a constant amount distinguishes zero duplicates from
`Theta(h)` duplicates among `Theta(N)` positions, so it requires
`t=Omega(sqrt(N/h))=Omega(sqrt(q))=Omega(h)`.  Combining (NS.16)--(NS.17) gives the useful exact
product

\[
 AW^{2/3}
 =\widetilde\Theta\!\left(
 (t+1)h^{1/2}q^{2/3}(1+\alpha h)^{1/6}
 \right).
 \tag{NS.24}
\]

For `t=Omega(h)`, this is at least

\[
 \widetilde\Omega(h^{3/2}q^{2/3})
 =\widetilde\Omega(N^{17/18}),
 \tag{NS.25}
\]

even under the favorable gap.  Exact singleton filtering is the extreme `alpha=0` case and
reproduces the cost (NS.13).

### 4.4 Frequency-aware-walk verdict

The soft-filter family has a sharp dichotomy: a sub-`sqrt(q)` filter leaves essentially all heavy
weight and reduces to the ordinary `N^(2/3)` balance, while a filter strong enough to alter the
stationary measure costs too much to prepare and update.  Optimizing `t`, `alpha`, and `r` gives
`Theta(N^(2/3))`, attained by `t=0`.  This closes the explicit weighted-representative walk tested
here, not every conceivable frequency-aware walk.

## 5. Verdict for `...ALT.joint-statistic-estimation`

### 5.1 A promise-aware joint-role oracle

For a known label `v`, a staged search over the two lists can stop early if `v` is heavy.  After
finding one occurrence, the same-side duplicate test confirms the role.  Singleton and unused
labels require the full zero-versus-one search.  Thus a coherent role unitary outputting one of
`H_L,H_R,10,01,11,00` has branch costs

\[
 T_H=\widetilde\Theta(\sqrt q),
 \qquad
 T_{10}=T_{01}=T_{11}=T_{00}
       =\widetilde\Theta(\sqrt N).
 \tag{NS.26}
\]

There are `Theta(q)` heavy labels and `Theta(q)` singleton labels; there are only `O(1)` unused
labels.  Hence

\[
 \sum_{v\in[q]}T_v^2=\widetilde\Theta(qN).
 \tag{NS.27}
\]

As in Section 3, all estimates below grant ideal variable-time root-sum-square composition.  This
is favorable to the attack and retains the long low-frequency branches.

### 5.2 Support intersection and union

The exact signals are

\[
 |\operatorname{supp}x\cap\operatorname{supp}y|=0\ \hbox{or}\ 1,
 \qquad
 |\operatorname{supp}x\cup\operatorname{supp}y|=4a\ \hbox{or}\ 4a-1.
 \tag{NS.28}
\]

Equivalently, the number of unused labels is `q-4a` or `q-4a+1`, both `O(1)`.  Searching the
label universe for the sparse `11` cell, or for the sparse `00` complement, uses (NS.27) and
costs

\[
 C_{\rm support}
 =\widetilde O\!\left(\sqrt{\sum_vT_v^2}\right)
 =\widetilde O(\sqrt{qN})
 =\widetilde O(N^{5/6}).
 \tag{NS.29}
\]

If support membership were a unit-cost oracle, sparse-complement search would use `Theta(sqrt q)`
calls.  Equation (NS.29) is the required oracle-synthesis charge; assuming direct support access
would hide the main cost.

### 5.3 Cross and combined collision counts

The cross-collision statistic is

\[
 C_\times=\sum_v r_vs_v
          =\sum_{i,j}{\bf1}[x_i=y_j]
          =0\ \hbox{or}\ 1.
 \tag{NS.30}
\]

Its natural oracle is equality on one of `n^2=Theta(N^2)` cross pairs and takes two input-value
queries up to uncomputation constants.  The signal probability is `0` versus `Theta(N^(-2))`;
Grover search or amplitude detection therefore costs

\[
 C_\times=\Theta(N).
 \tag{NS.31}
\]

The combined unordered collision count is

\[
 C_{\rm all}=\sum_v {r_v+s_v\choose2}=B_0\ \hbox{or}\ B_0+1,
 \tag{NS.32}
\]

where the same-side heavy baseline is

\[
 B_0=2\left[(a-p){d\choose2}+p{d+1\choose2}\right]
    =\Theta(qh^2)=\Theta(N^2/q)=\Theta(N^{4/3}).
 \tag{NS.33}
\]

Among `L=Theta(N^2)` unordered pairs, the background probability is `Theta(1/q)` and the YES/NO
gap is `Theta(1/N^2)`.  The corresponding amplitude-angle gap is

\[
 \Delta\theta
 =\Theta\!\left({1\over\sqrt{B_0L}}\right)
 =\Theta(N^{-5/3}),
 \tag{NS.34}
\]

so resolving the unit increment by counting costs

\[
 C_{\rm all}=\Theta(\sqrt{B_0L})=\Theta(N^{5/3})
 \tag{NS.35}
\]

pair-oracle calls.  Restricting to cross-colored pairs removes `B_0` but merely returns the
`Theta(N)` unique-pair search (NS.31).

### 5.4 Four-cell switch

The sparse cells `H_11` and `H_00` give (NS.29).  The dense cells `H_10,H_01=Theta(q)` differ by
one.  A uniformly random label therefore supplies a bounded variable with constant variance and
mean gap `Theta(1/q)`.  Quantum mean/count estimation needs `Theta(q)` role-oracle uses.  The RMS
role cost under a uniform label is

\[
 T_{\rm rms}
 =\sqrt{{1\over q}\sum_vT_v^2}
 =\widetilde\Theta(\sqrt N),
 \tag{NS.36}
\]

so a dense-cell or constant-coefficient four-cell contrast costs

\[
 C_{\rm four,dense}
 =\widetilde\Theta(q\sqrt N)
 =\widetilde\Theta(N^{7/6}).
 \tag{NS.37}
\]

Using the sparse cell is better, but still gives `N^(5/6)`, not a subcap algorithm.

### 5.5 Sketch variance

Random-sign sketches do not turn the unit cross signal into a low-variance observable.  For a
four-wise independent sign function `chi`, put

\[
 X=\sum_i\chi(x_i),\qquad Y=\sum_j\chi(y_j),\qquad Z=XY.
 \tag{NS.38}
\]

Then \(\mathbb E[Z]=C_\times\).  In NO the two supports are disjoint, so `X` and `Y` depend on disjoint
sign sets; in YES their only shared sign is the unique singleton and does not alter the leading
scale.  Thus each marginal second moment has scale

\[
 \sum_vr_v^2=\Theta(qh^2)=\Theta(N^{4/3}),
 \qquad
 \sum_vs_v^2=\Theta(N^{4/3}).
 \tag{NS.39}
\]

Accordingly `Z` has standard deviation `Theta(N^(4/3))` against a unit signal.  This
rules out a constant-sample AMS-style shortcut, even before charging the queries needed to
synthesize `X` and `Y`.  Direct pair access, which is the cleanest synthesis, already has the
costs (NS.31) and (NS.35).

### 5.6 Statistic-estimation verdict

The best audited joint-statistic implementation is sparse support/union/four-cell search at
`O-tilde(N^(5/6))`.  Cross collision costs `Theta(N)`, the dense four-cell contrast costs
`O-tilde(N^(7/6))`, and combined collision counting costs `Theta(N^(5/3))`.  Every statistic has
an exact unit signal, but none comes with a cheap statistic oracle.  Treating the histogram or
support as directly queryable would be circular.

## 6. Hybrid optimization

The main hybrids do not alter the verdict.

### 6.1 Partial sample/delete followed by a walk

For comparison with the earlier sampling architecture, sample `ell=xq` raw positions per side
and delete labels exposed by the sample after the required sample-incident claw check.  Up to
constants, the residual size is

\[
 B(x)=\Theta(q+Ne^{-cx}).
 \tag{NS.40}
\]

The reviewed virtual-residual access cost is `O-tilde(sqrt(N/B))`.  A Johnson child therefore has

\[
 C_{\rm sample+walk}(x)
 =\Theta(qx)+\widetilde O(\sqrt N\,B(x)^{1/6}).
 \tag{NS.41}
\]

If `x=o(1)`, then `B=(1-o(1))N` and the child remains `Theta(q)`.  If `x=Theta(1)`, setup itself
is `Theta(q)`.  If `x` grows, setup is supercap.  Hence the optimized scale is still `Theta(q)`.

### 6.2 Partial sample/delete followed by a pair statistic

Unique-pair search on two virtual residual lists of length `B` makes `Theta(B)` virtual queries,
so

\[
 C_{\rm sample+pair}(x)
 =\Theta(qx)+\widetilde O(\sqrt{NB(x)}).
 \tag{NS.42}
\]

Reducing `B` to its singleton floor `Theta(q)` requires `x=Theta(log h)` and leaves pair cost

\[
 \widetilde\Theta(\sqrt{Nq})=\widetilde\Theta(N^{5/6}),
 \tag{NS.43}
\]

already worse than the cap.  Stopping earlier is no better.

### 6.3 Cross-family comparison

| hybrid or primitive | optimized endpoint scale |
|:---|:---|
| ordinary Johnson | `N^(2/3)` |
| partial sample/delete + Johnson | `N^(2/3)` |
| duplicate soft filter + weighted walk | `N^(2/3)` at zero filtering |
| direct indexed variable-time classification | `N^(5/6)` |
| support/union sparse statistic | `N^(5/6)` |
| exact singleton access + Johnson | `N^(17/18)` |
| partial sample/delete + cross-pair statistic | `N^(5/6)` |
| raw cross-pair search | `N` |

The only cap-matching rows are Johnson balances; every mechanism that actually tries to expose
the hidden singleton roles is slower.

## 7. Gate ledger and remaining scope

The calculations above explicitly charge:

- value queries used to synthesize duplicate, role, equality, and support predicates;
- zero-mark duplicate and cross-list branches;
- the unique accepting branch and its final equality verification;
- coherent error reduction and uncomputation, hidden only in `O-tilde` notation;
- setup, update, check, spectral gap, and marked fraction for both walk constructions;
- precision/background and variance for each statistic;
- the true residual-coordinate cost in the two hybrids.

No result in this memo promotes, refutes, or closes a DAG node.  The three registered leaves now
have concrete tested architectures and separate verdicts, but a global `Omega(N^(2/3))` lower
bound for the frozen promise remains unproved.

## 8. Distinct routes generated outside the registered nodes

**None.**  Every tested construction is an instance or hybrid of duplicate classification,
frequency-aware joint walking, joint-statistic estimation, or the already registered
sample/delete/residual architecture.  No mathematically distinct outside-node algorithm was
generated for Rule-8 registration.
