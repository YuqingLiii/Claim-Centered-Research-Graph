# L3 structural audit: fixed relabel / disjoint-bucket claw embeddings

Date: 2026-07-21  
Canonical node: `KSUM.B4b.L3`  
Scope: cyclic `2-SUM`; local corpus only; no DAG edit

## Decision

There is a clean ceiling, but it applies to a narrower and more precise class than “all fixed
per-position relabel embeddings.”

**Proved algebraic ceiling.** Every pairwise-faithful cyclic embedding whose lower-bound source is
assembled from an equal-range claw core of size `r`, with each outer input hidden independently in
a disjoint unique-live/pSearch bucket, has ABI-product certificate scale at most

\[
  O\!\left(\sqrt N\,\min\{q,N\}^{1/6}\right).
\tag{L3.1}
\]

For `q<=N` this is `O(sqrt(N) q^(1/6))`; for `q>=N` it is the usual `O(N^(2/3))` plateau. The
ceiling is unchanged by position-dependent injective relabels, unequal bucket sizes, padding, or a
partition into independent palettes.

**Not proved, and false as an encoding-only assertion.** Fixed injective relabeling into cyclic
`2-SUM` does **not** itself cap the transferred lower bound at exponent `1/6`. The standard direct
encoding is an exact, query-for-query restriction of `2-SUM` to the entire small-range claw
function. It transfers whatever lower bound claw actually has. Locally the known claw window is

\[
 \Omega(\sqrt n\,\kappa^{1/6})
 \ \le Q(\operatorname{Claw}_{n\to\kappa})\le\
 O_\varepsilon(n^{1/2+\varepsilon}\kappa^{1/4}).
\tag{L3.2}
\]

Thus no structural argument based only on fixed relabels and alphabet capacity can rule out
`sqrt(N)q^(1/4)`. The `1/6` appears exactly when one additionally factors the donor into an
equal-range `r^(2/3)` claw core and independent `sqrt(bucket size)` selectors. A genuine L3 advance
must break that factorization, improve the small-range claw donor itself, or prove a new correlated
composition theorem. This is precisely the already registered L3 direction, not a new escape.

## 1. Local inputs and definitions

The local sources used are:

* `ksum/proof-dag/nodes/KSUM.B4b.L3.yaml`;
* the claw definition, cyclic encoding, and imported ABI/Tani bounds in
  `ksum/paper/ksum_small_alphabet.tex`, especially the local lines containing
  Theorems `thm:abi`, `thm:tani`, and Lemma `lem:encode`;
* the on-disk ABI source `ksum/artifacts/references/abi_2103.16390_src/claw.tex`, lines 291--330, which
  explicitly factors the lower bound as an equal-range claw core composed with pSearch.

No other agent's L3 artifact was read.

Fix integers `N>=2`, `q>=3`, and a target `t in Z_q`. Let

\[
 \sigma_t(x)=t-x,
 \qquad
 \tau_t=|\{x\in\mathbb Z_q:2x=t\}|.
\tag{L3.3}
\]

For odd `q`, `tau_t=1` for every target.

### Pairwise-faithful fixed-relabel embedding

Choose `r_L,r_R>=1` virtual claw coordinates. Each virtual coordinate `u` has a nonempty physical
bucket `B_u`; all buckets are pairwise disjoint subsets of `[N]`. A promised bucket input contains
exactly one live symbol `a in [kappa]` at an arbitrary site and a dummy symbol `*` at every other
site. The recovered virtual value is that unique live symbol.

Each physical site `p` has a fixed injective relabel map

\[
 e_p:\{*\}\mathbin{\dot\cup}[\kappa]\longrightarrow\mathbb Z_q.
\tag{L3.4}
\]

The maps can vary arbitrarily with `p`, but not with other input positions. Call the embedding
**pairwise faithful** if, for every left live site `p`, right live site `v`, and labels `a,b`,

\[
 e_p(a)+e_v(b)=t\pmod q\quad\Longleftrightarrow\quad a=b,
\tag{L3.5}
\]

and no pair involving a dummy or two sites on the same side sums to `t`. These clauses imply exact
completeness, exact soundness, and absence of padding-induced false claws. They are the local
pairwise condition used by the standard claw-to-`2-SUM` encoding.

Pairwise faithfulness is deliberately explicit. Mere equality of the two **decision functions**
does not imply (L3.5): a globally coded reduction could allow a matching virtual pair to be
witnessed by a different physical pair. Such a construction is range-coupled rather than an
independent fixed-relabel claw embedding and is outside the theorem below.

### ABI-composable subclass

An embedding is **ABI-composable** when, in addition:

1. `r_L=r_R=r` and the outer donor is the equal-domain, equal-range core
   `Claw_{r->r}` (changing `r` by an absolute additive constant is allowed);
2. every one of its `2r` virtual inputs is independently hidden in its own unique-live bucket;
3. the only inner hardness used is the pSearch/unique-live factor `Theta(sqrt(ell))`, where `ell`
   is a bucket size; and
4. the certificate is obtained by the ABI product rule: equal-range claw strength
   `Theta(r^(2/3))` times the common pSearch strength. For unequal buckets one may restrict every
   bucket to `ell_min`, the minimum size, before applying the uniform composition theorem.

This definition captures the complete algebra behind ABI's on-disk display

\[
 r^{2/3}\sqrt{n/r}=\sqrt n\,r^{1/6}.
\tag{L3.6}
\]

It does not assume that every conceivable adversary or approximate-degree proof must factor this
way.

## 2. Relabel rigidity and alphabet capacity

### Lemma 1 (position dependence collapses)

For every pairwise-faithful embedding with `kappa>=1`, there is an injective map
`c:[kappa]->Z_q` such that every left live map equals `c` and every right live map equals
`sigma_t circ c`:

\[
 e_p(a)=c(a),\qquad e_v(a)=t-c(a)
\tag{L3.7}
\]

for every left live site `p`, right live site `v`, and label `a`.

**Proof.** Fix one right live site `v_0`. By (L3.5), for every left live site `p`,
`e_p(a)+e_{v_0}(a)=t`; hence `e_p(a)=t-e_{v_0}(a)` is independent of `p`. Call this common value
`c(a)`. Fixing a left site gives `e_v(a)=t-c(a)` for every right site. If `c(a)=c(b)` for `a!=b`,
then `c(a)+e_v(b)=t`, contradicting the reverse implication in (L3.5). Thus `c` is injective. ∎

So arbitrary fixed per-position live relabels buy no extra cyclic capacity. Their only remaining
freedom is in dummy values, which soundness can only constrain further.

### Lemma 2 (complement-orbit capacity)

Every pairwise-faithful embedding satisfies

\[
 \kappa\le {q-\tau_t\over2}.
\tag{L3.8}
\]

In particular, for odd cyclic `q`, `kappa<=(q-1)/2`.

**Proof.** Let `S=c([kappa])`. The same-side soundness clause says
`x+y!=t` for every `x,y in S`. Equivalently `S` is disjoint from `sigma_t(S)`. Fixed points of
`sigma_t` cannot belong to `S`, and every remaining orbit has size two, of which `S` contains at
most one element. There are `(q-tau_t)/2` such orbits. ∎

The standard encoding attains this capacity up to dummy/frozen values by choosing one representative
from each non-fixed complement pair and using its complement on the other side. Thus (L3.8) is the
exact alphabet bottleneck for this class, not merely a loose counting argument.

## 3. The ABI-product ceiling

### Theorem 3 (single-core algebraic ceiling)

For all `N>=2`, `q>=3`, targets `t`, and ABI-composable pairwise-faithful embeddings using at most
`N` physical positions, let `ell_min` be the minimum of the `2r` bucket sizes. The magnitude exposed
by the equal-range-claw/pSearch product certificate satisfies

\[
 \begin{aligned}
 C_{\rm ABI}
   &=O\!\left(r^{2/3}\sqrt{\ell_{\min}}\right)\\
   &\le O\!\left(\sqrt N\,r^{1/6}\right)\\
   &\le O\!\left(\sqrt N\,
      \min\left\{{q-\tau_t\over2},{N\over2}\right\}^{1/6}\right).
 \end{aligned}
\tag{L3.9}
\]

All constants are absolute and independent of `N,q,t,r`, bucket sizes, and relabel maps.

**Proof.** Disjointness and nonempty buckets give

\[
 2r\ell_{\min}\le\sum_u|B_u|\le N.
\tag{L3.10}
\]

The ABI core contributes `Theta(r^(2/3))` and pSearch on the common restricted bucket contributes
`Theta(sqrt(ell_min))`. Therefore

\[
 r^{2/3}\sqrt{\ell_{\min}}
 \le r^{2/3}\sqrt{N/(2r)}
 =2^{-1/2}\sqrt N\,r^{1/6}.
\]

The core uses `r` different live labels, so Lemma 2 gives `r<=(q-tau_t)/2`; nonempty disjoint
buckets give `r<=N/2`. Substitution proves (L3.9). ∎

For odd `q<=N`, (L3.9) is `O(sqrt(N)q^(1/6))`. For `q>=N`, it is `O(N^(2/3))`. Equal bucket sizes,
`r=Theta(min{q,N})`, and a capacity-saturating complement palette meet this algebraic scale, so no
choice of fixed relabel or bucket schedule improves its exponent.

### Unequal and multiple independent blocks

Unequal buckets cannot help because the uniform product theorem can use only the smallest bucket
without an additional variable-cost composition theorem. A claim that larger buckets add their
hardness while the smallest bucket does not limit the product is new composition mathematics, not
an optimization of the ABI construction.

For completeness, suppose independent palette blocks `j` use equal-range cores `r_j`, minimum
bucket sizes `ell_j`, disjoint physical coordinates, and disjoint complement-orbit palettes. If the
block certificates are combined by the standard Euclidean/OR accounting

\[
 C^2\le C_0^2\sum_j r_j^{4/3}\ell_j,
\tag{L3.11}
\]

then `2 sum_j r_j ell_j<=N` and `max_j r_j<=min{(q-tau_t)/2,N/2}` give

\[
 C^2
 \le {C_0^2N\over2}\max_j r_j^{1/3}
 =O\!\left(N\min\{q,N\}^{1/3}\right),
\tag{L3.12}
\]

again yielding (L3.1). Equation (L3.12) is a proved algebraic implication of the explicitly stated
aggregation rule. This memo does not silently assume that every correlated adversary must obey
(L3.11).

## 4. Why this is not a ceiling for all fixed relabel reductions

Take `n=floor(N/2)` and `kappa<=(q-1)/2` for odd `q`. The direct map

\[
 f(i)\mapsto f(i),\qquad g(j)\mapsto-g(j)\pmod q
\tag{L3.13}
\]

is a pairwise-faithful fixed injective relabel with buckets of size one. On its image,

\[
 \operatorname{2SUM}_{\mathbb Z_q,0,2n}
 =\operatorname{Claw}_{n\to\kappa}
\tag{L3.14}
\]

exactly. Therefore

\[
 Q(\operatorname{2SUM}_{\mathbb Z_q,0,2n})
 \ge Q(\operatorname{Claw}_{n\to\kappa}).
\tag{L3.15}
\]

No `1/6` appears in (L3.13)--(L3.15). It enters only when the currently known ABI/Tani lower bound
for the donor is substituted, or when the donor itself is re-derived from the equal-range core and
pSearch.

Consequently, the broad statement

> every fixed per-position injective claw embedding into cyclic `2-SUM` is capped at
> `sqrt(N)q^(1/6)`

is unsupported and cannot be proved by palette counting. The same standard embedding would
immediately transfer a future `Omega(sqrt(n)kappa^(1/4))` claw lower bound. The local corpus's
`q^(1/4)` claw expression is presently an **upper bound**, not a lower bound, so this is not a new
complexity result or a counterexample attaining the larger exponent. It is a counterexample to an
encoding-only no-go argument.

## 5. Proved facts versus composition heuristics

### Proved here

1. Pairwise faithfulness forces all live per-position relabels to collapse to one global left code
   and its target complement on the right, (L3.7).
2. Such a code has at most `(q-tau_t)/2` live labels, (L3.8).
3. Disjoint unique-live buckets obey `2r ell_min<=N`.
4. The ABI product expression, and every multi-block expression explicitly satisfying (L3.11), is
   bounded by (L3.1).
5. Direct fixed relabeling preserves the full small-range claw function, so fixed relabeling alone
   has no proved `1/6` ceiling.

### Not promoted to a theorem here

It is tempting to say that the **actual quantum query complexity** of every independent-inner
composition is `Theta(r^(2/3)sqrt(ell))`, invoking exact general-adversary composition and robust
upper composition. The local ABI source explicitly supplies the needed pSearch **lower-product**
rule, but this commission did not re-audit a matching theorem for arbitrary multi-output partial
inners, unequal bucket sizes, or multiple blocks. Accordingly:

* (L3.9) is a ceiling on the precisely defined ABI-derived certificate magnitude;
* it is not asserted as an information-theoretic upper bound on every promise function expressible
  with disjoint buckets;
* any claim that correlation among buckets still obeys the product/minimum rule needs a separate
  operator-level adversary-composition proof;
* conversely, merely observing joint structure numerically does not establish a super-product
  lower bound.

This separation prevents the algebraic parameter optimization from being mistaken for a universal
adversary impossibility theorem.

## 6. Quantifier ledger and kill criterion

The ceiling theorem quantifies over every `N>=2`, `q>=3`, target `t in Z_q`, core size `r>=2`, all
families of nonempty disjoint buckets using at most `N` coordinates, all bucket sizes, and all fixed
sitewise injective maps satisfying the explicit pairwise-faithfulness and no-padding-hit clauses.
For odd `q`, `tau_t=1`; no translation-to-zero assumption is needed for the capacity proof.

The theorem is endpoint-uniform in `q`: it gives `sqrt(N)q^(1/6)` below the alphabet/position
crossover and `N^(2/3)` above it. It makes no claim for a globally coded decision reduction that
fails pairwise faithfulness, a non-unique-live inner gadget, overlapping buckets, a correlated
range-coupled donor, or a new composition rule. Those cases are exactly where L3 could differ from
ABI's architecture.

Hence the L3 kill criterion is now precise:

* a proposal that reduces, after typing, to an equal-range `r^(2/3)` core with independent
  unique-live buckets cannot improve the existing exponent, regardless of relabel details;
* a proposal is not killed merely because its final map into `Z_q` is fixed and injective;
* to remain live it must exhibit a formula-defined correlation or donor lower bound outside the
  ABI-product hypotheses and prove exact completeness, soundness, `O(1)` query simulation, and
  range `O(q)`.

No distinct escape outside the registered L3 direction was generated in this audit.

## Conclusion

The fixed-relabel layer is rigid but lossless: it consumes one complement orbit per claw label and
otherwise preserves the donor. The disjoint-bucket layer creates the `1/6` exponent only when it is
paired with the equal-range `r^(2/3)` claw core:

\[
 \underbrace{r^{2/3}}_{\text{equal-range claw}}
 \times
 \underbrace{\sqrt{N/r}}_{\text{independent pSearch}}
 =\sqrt N\,r^{1/6}
 \le\sqrt N\,q^{1/6}.
\]

That is the exact structural ceiling justified by the local corpus. A stronger no-go for correlated
range-coupled L3 gadgets would require new adversary-composition mathematics; the present algebra
does not supply one.

