# Hidden-frequency critical endpoint: adversary and algorithm attempt

Date: 2026-07-21  
Canonical node: `KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint`  
Scope: the exact two-orbit promise in
`ksum/artifacts/ksum_L3_hidden_frequency_promise_20260721.md`, only at
`q=Theta(N^(2/3))`  
Method: local corpus and first-principles reductions; no web; no DAG edits

## 1. Verdict

The endpoint remains **OPEN**.

I did not obtain either an explicit `Omega(N^(2/3))` adversary/dual or an
`o(N^(2/3))` algorithm.  I did obtain a theorem-backed adversary lower bound for the **exact frozen
promise**, rather than for unrestricted claw:

\[
 \operatorname{Adv}^{\pm}(\mathrm{HF}_{N,q})
 =\Omega\!\left(a^{2/3}\sqrt{d+1}\right)
 =\Omega\!\left(\sqrt N\,q^{1/6}\right),
 \tag{1.1}
\]

where

\[
 n=\lfloor N/2\rfloor,\qquad
 a=\lfloor q/4\rfloor,\qquad
 d=\left\lfloor\frac{n-a}{a}\right\rfloor.
 \tag{1.2}
\]

At `q=Theta(N^(2/3))`, (1.1) is

\[
 \operatorname{Adv}^{\pm}(\mathrm{HF}_{N,q})
 =\Omega(N^{11/18}).
 \tag{1.3}
\]

The ordinary claw walk gives the matching cap-side upper bound

\[
 Q(\mathrm{HF}_{N,q})=O(N^{2/3}),
 \tag{1.4}
\]

so the rigorous endpoint bracket established here is

\[
 \boxed{\Omega(N^{11/18})\ \le\ Q(\mathrm{HF}_{N,q})\ \le\ O(N^{2/3}).}
 \tag{1.5}
\]

The remaining exponent gap is exactly `N^(1/18)`.  In the natural block notation

\[
 a=\Theta(N^{2/3}),\qquad m=d+1=\Theta(N^{1/3}),\qquad N=\Theta(am),
 \tag{1.6}
\]

the proved addressed composition has scale

\[
 a^{2/3}m^{1/2}=N^{11/18},
 \tag{1.7}
\]

whereas the endpoint requires

\[
 a^{2/3}m^{2/3}=N^{2/3}.
 \tag{1.8}
\]

Thus an independent `pSearch` product cannot finish the endpoint: `pSearch_m` itself has tight
complexity `Theta(sqrt(m))`.  The missing gain must come from the global erasure of the block
address / private-heavy-label structure, not from retuning the existing product.

## 2. Exact promise notation

Write `HF_(N,q)` for the frozen partial Boolean function.  Each side has length `n` and contains

* `a` singleton labels;
* `a-p` private heavy labels of frequency `d`;
* `p` private heavy labels of frequency `d+1`,

where

\[
 p=(n-a)-ad,\qquad 0\le p<a.
 \tag{2.1}
\]

The left and right heavy palettes are disjoint.  In a NO input all singleton labels are also
cross-disjoint.  In a YES input exactly one singleton label occurs once on each side and all other
supports are cross-disjoint.  The two answer classes are single orbits under

\[
 S_n^{(L)}\times S_n^{(R)}\times S_q.
 \tag{2.2}
\]

Let `X_0` and `X_1` denote the NO and YES orbits, respectively.

## 3. A theorem-backed lower bound on this restriction

This section proves (1.1).  It does not appeal to hardness of unrestricted small-range claw.

### 3.1 Outer problem: injective unique claw

Define `UIC_a` on two lists `u,v in [2a]^a` with the promise that both lists are injective and

\[
 |\operatorname{im}(u)\cap\operatorname{im}(v)|
 \in\{0,1\}.
 \tag{3.1}
\]

The output is the intersection bit.  Then

\[
 Q(\mathrm{UIC}_a)=\Omega(a^{2/3})
 \quad\text{and hence}\quad
 \operatorname{Adv}^{\pm}(\mathrm{UIC}_a)=\Omega(a^{2/3}).
 \tag{3.2}
\]

Here is an exact reduction supporting (3.2).  Start from unique-collision Element Distinctness on
`2a` positions over alphabet `[2a]`: the input is promised either injective or to have exactly one
colliding pair and no other collision.  Rosmanis's locally stored small-alphabet paper explicitly
uses this at-most-one-collision promise and proves the tight lower bound at alphabet size equal to
the domain size (`rosmanis_small_range_ed.txt`, lines 139--145 and its Section 6).

Choose a uniformly random balanced split of the `2a` positions into two sides of size `a`.  On an
injective input every split is a valid UIC NO instance.  On a unique-collision input, the two
colliding positions land on opposite sides with probability

\[
 \frac{a}{2a-1}>\frac12.
 \tag{3.3}
\]

Conditioned on this event, both sides are injective and their images intersect exactly once, so the
input is a valid UIC YES instance.  If the pair lands on one side, the UIC promise is violated, but
this does not invalidate the reduction: after first reducing the UIC solver's error to a small
constant, an invalid branch can only add a nonnegative amount to the YES acceptance probability.
The NO acceptance probability remains small on every split.  Therefore a constant number of
repetitions gives a bounded-error unique-ED solver.  Each simulated UIC query is one ED query.

This is a promise-respecting lower reduction, not the invalid inference that a hard full function
makes every restriction hard.

### 3.2 Common-length `pSearch` blocks, including all rounding cases

Put

\[
 m:=d+1.
 \tag{3.4}
\]

For each side create `a` public blocks, one per private heavy label.  Every block contains one
instance of `pSearch_m`: it has exactly one non-star symbol from `[2a]` and `d` stars.

Map the unique non-star symbol to a singleton label and map every star in block `k` on side
`sigma in {L,R}` to a private heavy label `H_(sigma,k)`.

The `a-p` frequency-`d` blocks need no other coordinate.  Each of the `p` frequency-`d+1` blocks
gets one additional **public fixed** coordinate equal to the same private heavy label.  Consequently

\[
 (a-p)(d+1)+p(d+2)=a+ad+p=n,
 \tag{3.5}
\]

so each side has exactly the frozen length, and its heavy frequencies are exactly the required
`d/(d+1)` split.  This handles every remainder `p`; no subsequence or divisibility assumption is
being hidden.

Allocate disjoint target-label pools as follows:

\[
 \underbrace{[2a]}_{\text{outer singleton labels}}
 \ \dot\cup\
 \underbrace{\{H_{L,1},\ldots,H_{L,a},H_{R,1},\ldots,H_{R,a}\}}_{\text{private heavy labels}}.
 \tag{3.6}
\]

This uses `4a<=q` labels; any of the remaining `q-4a` labels are unused.  Restrict the outer inputs
to `UIC_a`.  In an outer NO input its two injective supports use all `2a` singleton labels and are
disjoint.  In an outer YES input their union has size `2a-1`, leaving exactly one more unused label.
Thus the mapped joint histograms are exactly (HF.8) and (HF.9) from the frozen construction.

### 3.3 Query simulation and composition

Let

\[
 H:=\mathrm{UIC}_a\circ(\mathrm{pSearch}_m)^{2a}.
 \tag{3.7}
\]

The mapping above makes `H` a literal subfunction of `HF_(N,q)`.  A target query to a variable
block coordinate makes one source query and applies the fixed map

\[
 *\mapsto H_{\sigma,k},\qquad z\mapsto z.
 \tag{3.8}
\]

A query to one of the `2p` extra coordinates is answered publicly.  Hence the value-oracle
simulation uses at most one source query, and the standard coherent XOR simulation uses at most
two.  The reducer never has to discover a palette, a block, or a frequency.

The locally stored `pSearch` composition theorem gives the product lower bound.  Tani states the
adversary form

\[
 \operatorname{Adv}^{\pm}(f\circ\mathrm{pSearch}_m)
 \ge \frac{2}{\pi}\operatorname{Adv}^{\pm}(f)
       \operatorname{Adv}^{\pm}(\mathrm{pSearch}_m)
 \tag{3.9}
\]

at `tani_2410.02243_src/main.tex`, lines 1447--1466.  The local GWWZ source explicitly records that
the lower composition argument also holds for a partial outer `f`, such as unique-ED
(`gilani_wang_wu_zhou_2412.17786_eprint_src/main.tex`, line 511 and its footnote).  That statement
is written at the query-complexity level; general-adversary optimality converts it back to the same
asymptotic `Adv+/-` lower bound for this finite partial function.  Since

\[
 \operatorname{Adv}^{\pm}(\mathrm{pSearch}_m)=\Theta(\sqrt m),
 \tag{3.10}
\]

(3.2), (3.7)--(3.10), and monotonicity under restriction give

\[
 \operatorname{Adv}^{\pm}(\mathrm{HF}_{N,q})
 \ge \operatorname{Adv}^{\pm}(H)
 =\Omega(a^{2/3}\sqrt{d+1}),
 \tag{3.11}
\]

which is (1.1).

### 3.4 Boolean-versus-`q`-ary interface audit

There is no interface sleight of hand in (3.11):

* the outer `UIC_a` is Boolean;
* each outer input coordinate expects a label in `[2a]`;
* `pSearch_m` returns exactly such a non-Boolean label;
* the outer function compares those returned labels for equality.

This is precisely the interface covered by the special `pSearch` composition theorem.  In
contrast, an element-distinctness or Collision inner gadget returns one Boolean collision bit.  It
cannot replace (3.10) by `m^(2/3)` because that bit does not provide the label required by the
outer equality test.

## 4. Why the proof stops at `N^(11/18)`

The addressed subfunction exposes the partition into blocks through target coordinates.  Its
inner problem is exactly `pSearch_m`, so the factor `sqrt(m)` in (3.10) is tight even algorithmically.
No coefficient choice in an independent product of these same blocks can produce `m^(2/3)`.

The full hidden-frequency orbit removes all block addresses: domain positions are globally
permuted, and the private heavy labels only reveal a block after repeated occurrences have been
found.  At the endpoint, the desired adversary would therefore have to exploit **coherent
interference among many possible block decompositions**.  Algebraically the missing improvement is

\[
 \sqrt m\longrightarrow m^{2/3},
 \qquad\text{an extra factor }m^{1/6}=N^{1/18}.
 \tag{4.1}
\]

Neither the ABI/Tani adversary nor the partial-hiding theorem contains such an address-erasure
gain.  GWWZ in fact proves that ordinary recognizable-star hiding of element distinctness remains
at the `sqrt(m)d^(1/6)` scale, up to logarithms.  Therefore (4.1) cannot be credited merely because
the relevant positions are shuffled.

## 5. Exact missing adversary object

Let `Delta_i` be the zero-one matrix on `X_1 x X_0` whose `(x,y)` entry is one iff the two inputs
differ at target coordinate `i`.  A complete endpoint proof is now reduced to the following single
finite statement.

> **Critical hidden-merger adversary lemma.**  There is an absolute `c>0` and, for every endpoint
> parameter pair, a real matrix
> `Gamma_(N,q) in R^(X_1 x X_0)` such that
> \[
>   \|\Gamma_{N,q}\|\ge cN^{2/3},
>   \qquad
>   \max_{i\in[2n]}\|\Gamma_{N,q}\circ\Delta_i\|\le 1.
>   \tag{5.1}
> \]

Equation (5.1) is the smallest exact missing formula.  It is already the correct Boolean
adversary, is supported only on the two legal frozen orbits, and has no alphabet-transfer or
query-simulation issue.  The construction in Section 3 gives a valid matrix with the first norm
only `Omega(N^(11/18))`; no explicit coefficient correction giving the extra `N^(1/18)` was found.

Because (2.2) acts transitively on each answer class, a symmetry-resolved attack can look for
`Gamma_(N,q)` in the intertwiner space between the two orbit modules.  Concretely, after choosing
representatives with stabilizers `K_0,K_1`, an invariant candidate has the orbital expansion

\[
 \Gamma=\sum_{\omega\in K_1\backslash G/K_0}c_\omega A_\omega,
 \qquad G=S_n^{(L)}\times S_n^{(R)}\times S_q.
 \tag{5.2}
\]

What is missing is not the statement of the SDP but either

1. coefficients `c_omega` and a block diagonalization proving (5.1), or
2. an equivalent strict-orbit recording-query estimate.

The most concrete recording-query substitute for (5.1) would be a strict-type analogue of the
element-distinctness progress estimate

\[
 \|\Upsilon^+_{\mathrm{merge}}\psi_T\|
 \le O(T^{3/2}/N)
 \quad\text{for }T\le cN^{2/3},
 \tag{5.3}
\]

together with constant anti-concentration of the complementary (no-known-cross-pair) subspace
between the two answer types.  Equation (5.3) would force `T=Omega(N^(2/3))`.

Belovs proves the analogous `O(T^(3/2)/n)` query-gain estimate for ordinary element distinctness
(`new-adversary_v6.tex`, lines 2547--2607).  The combinatorial numerator is promising here because
the highlighted cross-pair endpoints range over all `Theta(N^2)` cross-position pairs even though
only `Theta(N^(2/3))` positions are singletons in any one input.  But his proved strict/relaxed
transfer requires alphabet `Omega(N^2)`, and his general anti-concentration theorem assumes a
linear number of singleton blocks and bounded largest block.  Here the alphabet and singleton
count are only `Theta(N^(2/3))`, and the largest blocks have size `Theta(N^(1/3))`.

This is not a cosmetic hypothesis failure.  The exact input distribution assigns **distinct**
labels to `Theta(q)` blocks using an alphabet of size `Theta(q)`, essentially a random injection.
The relaxed independent-label distribution has `Theta(q)` accidental block-label collisions and
is not a small perturbation.  The needed extension is therefore a strict random-injection / random-
partition progress lemma, not the already-proved relaxed theorem.

The Jeffery--Zur local source explicitly describes extension of compressed-oracle reasoning to
non-product distributions as an open methodological direction
(`compressed_oracle_adversary_2509.07876_eprint_src/arxiv_v1-new.tex`, lines 195 and 239).  Random
permutation inversion is handled there via separate representation-theoretic projectors, but no
theorem in that source covers the present merge of two singleton blocks amid growing heavy blocks.

## 6. Upper-algorithm attacks at the endpoint

No `o(N^(2/3))` algorithm survived the following checks.

### 6.1 Generic walk and palette exposure

The ordinary two-list Johnson/MNRS claw walk costs `Theta(N^(2/3))`, proving (1.4).  The previously
audited heavy-palette algorithm costs

\[
 \widetilde O(q+\sqrt Nq^{1/6}).
 \tag{6.1}
\]

At `q=Theta(N^(2/3))`, its palette term already costs the cap.  Sampling `o(q)` positions leaves a
constant fraction of the `Theta(q)` heavy labels and hence `Theta(N)` heavy positions; sampling
`omega(q)` is supercap.  This is an exact obstruction to that architecture, not a general lower
bound.

### 6.2 A role oracle is too expensive

Suppose one occurrence of a label is known.  Determining whether that label is a singleton or has
frequency at least `d` requires distinguishing zero from `d-1` marked items among the remaining
`n-1` positions.  By the tight Grover/search bound this costs

\[
 \Theta\!\left(\sqrt{n/d}\right)
 =\Theta(\sqrt q)
 =\Theta(N^{1/3})
 \tag{6.2}
\]

queries at the endpoint.  Thus a coherent filter that explicitly classifies every loaded label
does not provide the cheap singleton-residual oracle that the compressed claw child needs.  This
does not rule out an algorithm that never performs explicit role classification.

### 6.3 Small stored subsets do not reveal the mask locally

For a uniformly sampled stored subset of `r` positions, a fixed heavy label has expected occupancy

\[
 \Theta(r/q).
 \tag{6.3}
\]

If `r=o(q)`, most sampled heavy occurrences appear only once inside the stored data and are locally
indistinguishable from true singleton occurrences.  Taking `r=Theta(q)` reaches
`Theta(N^(2/3))` setup.  This explains why frequency-conditioned Johnson walks audited so far hit
the cap, but (6.3) is not a lower bound against arbitrary quantum states.

### 6.4 Histogram and support-size reformulations

The cross moment

\[
 \sum_z r_zs_z
 \tag{6.4}
\]

is zero versus one, and the union support size differs by one.  When `q` is divisible by four, the
NO input globally uses all `q` labels while the YES input misses exactly one, so the problem is
also a very narrow, colored, fixed-histogram surjectivity restriction.  Neither observation gives
an algorithm: estimating either statistic to additive error below one is the original decision
problem.  Conversely, a lower bound for unrestricted surjectivity does not pass to this two-orbit
restriction without a dual supported on these exact histograms.

### 6.5 Frequency flattening / state preparation

Preparing a position-weighted label state is easy, but flattening it to a uniform state over
distinct labels requires suppressing Schmidt weights differing by `sqrt(d)`.  More importantly,
the black-box operation that decides which weight applies contains the singleton-versus-heavy
search problem (6.2).  No locally verified state-conversion or variable-time theorem turns this
into `o(N^(2/3))` total claw detection.  Treating the condition number `sqrt(d)` alone as the query
cost would ignore the absolute small singular value and would not be a valid algorithm.

## 7. Cap sweep and cyclic 2-SUM transfer

At the endpoint,

\[
 q=\Theta(N^{2/3}),\qquad
 \sqrt Nq^{1/4}=\Theta(N^{2/3}).
 \tag{7.1}
\]

Thus (5.1) asks exactly for the standard walk cap and never for a super-cap lower bound.

The frozen embedding uses modulus `Q=2q+1`, arbitrary target `t`, and the maps

\[
 x_i\mapsto c+x_i,\qquad y_j\mapsto c-y_j,
 \qquad 2c=t\pmod Q.
 \tag{7.2}
\]

It is exact on all claw inputs, has no within-half or padding witness, and uses one source query per
live coordinate (at most two in coherent XOR convention).  Therefore both the proved
`Omega(N^(11/18))` lower bound and any future (5.1) witness transfer losslessly to the corresponding
cyclic 2-SUM restriction.  The alphabet changes only by an absolute factor.

## 8. Conditional scaling consequence

This endpoint is potentially more valuable than a single cap point.  Suppose an endpoint family
of total length `B`, alphabet `r=Theta(B^(2/3))`, satisfied

\[
 \operatorname{Adv}^{\pm}(\mathrm{HF}_{B,r})=\Omega(B^{2/3}).
 \tag{8.1}
\]

Take `B=Theta(q^(3/2))` and compose each `r=Theta(q)`-valued input coordinate with
`pSearch_m`, where `m=Theta(N/B)`.  The interface is valid because `pSearch_m` returns the actual
`r`-ary label expected by the endpoint function.  The adversary product would be

\[
 B^{2/3}\sqrt m
 =\Theta(q)\sqrt{N/q^{3/2}}
 =\Theta(\sqrt Nq^{1/4}).
 \tag{8.2}
\]

This calculation is only a conditional adversary scaling statement.  Legality of a particular
full-curve target encoding belongs to its already registered bridge node; it is not proved or
tested here.  It does show why an actual endpoint witness (5.1), rather than another parameter
analogy, is the decisive missing object.

## 9. Source ledger

| Local source | Fact used | Result here |
|---|---|---|
| `ksum/artifacts/references/rosmanis_small_range_ed.txt`, lines 139--145 and Section 6 | ED over alphabet equal to domain remains `Omega(n^(2/3))` under the at-most-one-collision promise | outer `UIC_a` lower bound |
| `ksum/artifacts/references/tani_2410.02243_src/main.tex`, lines 1423--1466 | general adversary definition and `pSearch` product | exact addressed lower construction |
| `ksum/artifacts/references/ksum_W_walkopt/gilani_wang_wu_zhou_2412.17786_eprint_src/main.tex`, line 511 footnote | lower `pSearch`/hiding composition extends to partial outer functions | promise-interface audit |
| `ksum/artifacts/references/abi_2103.16390_src/claw.tex`, lines 291--344 | baseline `sqrt(N)q^(1/6)` construction and the same critical hard profile posed as open | provenance and exponent comparison |
| `ksum/artifacts/references/bel2026/new-adversary_v6.tex`, lines 2547--2609 | ED query gain `O(T^(3/2)/n)` | precise desired strict-type analogue |
| same, lines 1427--1494 and 1964--1976 | strict/relaxed alphabet requirement; linear singleton and bounded-block hypotheses | theorem does not apply |
| `ksum/artifacts/references/ksum_W_walkopt/compressed_oracle_adversary_2509.07876_eprint_src/arxiv_v1-new.tex`, lines 195, 239, 1189--1241 | non-product-distribution limitation; separate permutation projectors | method boundary, not a donor |

## 10. Gate ledger

| Obligation | Outcome |
|---|---|
| exact frozen two-orbit promise | preserved |
| all integer remainders `p` | handled by one public heavy coordinate in each long block |
| theorem-backed restriction lower bound | `Omega(a^(2/3)sqrt(d+1))` |
| endpoint value | `Omega(N^(11/18))` |
| explicit `Omega(N^(2/3))` adversary/dual | **not found** |
| smallest exact missing formula | (5.1) |
| Boolean versus non-Boolean interface | audited; `pSearch` passes labels, Collision does not |
| concrete `o(N^(2/3))` algorithm | **not found** |
| generic upper cap | `O(N^(2/3))` |
| cyclic 2-SUM simulation | one query; exact; `Q=2q+1` |
| cap sweep | target equals, never exceeds, `N^(2/3)` |
| numerical evidence | none used |
| DAG/status edit | none |

## 11. Out-of-node approaches generated

None.  The conditional endpoint-to-full-curve scaling bridge was already registered before this
commission, and the surjectivity view was already included in the local donor audit.  No distinct
unregistered route was tested.

## 12. Bottom line

The exact hidden-frequency endpoint is not merely known to be a restriction of claw: it contains a
fully legal addressed subproblem whose negative-weight adversary is
`Omega(N^(11/18))`, with all rounding and oracle interfaces closed.  That is the strongest rigorous
partial result obtained here.

Reaching the cap requires a new address-erasure adversary: a matrix supported on the exact YES/NO
orbits satisfying (5.1), or an equivalent strict random-injection progress theorem yielding
(5.3) plus anti-concentration.  Existing independent `pSearch`, recognizable-star hiding,
relaxed arbitrary-type, Collision, and ordinary Johnson machinery cannot supply the missing
`m^(1/6)=N^(1/18)` factor.  No endpoint-killing algorithm was found.
