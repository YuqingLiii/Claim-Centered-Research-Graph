# L3 multiscale-frequency-mask: optimized sampling upper envelope

Date: 2026-07-21  
Canonical scope: `KSUM.B4b.L3.ALT.multiscale-frequency-mask`  
Status of this memo: upper-algorithm/ceiling audit only; **no lower bound or DAG status change is
claimed**  
Method: local corpus only; no web; no DAG-file edits

## 1. Verdict

For every permutation-invariant rare-candidate promise of the form specified below, the optimized
one-stage sample/delete/compress/Johnson attack is controlled by one explicit one-dimensional
variational quantity, and a stronger finite stratified-cutoff envelope is given in Theorem 2.  If
`R` is the total unresolved candidate mass per side and the side-exclusive decoys have frequency
spectrum

```text
{(h_j,M_j)}_j,       sum_j h_j M_j = Theta(N),
sum_j h_j=O(q),      R=O(q),
```

then, up to the already-reviewed coherent-compression polylogarithms,

\[
 Q_{\rm SC}(N,q)
 \;\le\;
 \widetilde O\!\left(
 \min\left\{N^{2/3},
 \inf_{0\le \ell\le N}
 \left[
   \ell+\sqrt N\,
   \left(R+\sum_jh_jM_j e^{-\ell M_j/N}\right)^{1/6}
 \right]\right\}\right).
 \tag{ME.1}
\]

Here `ell` is the number of uniformly sampled positions on **each** side.  Formula (ME.1) does not
assume that a value carries a public frequency-band tag.  The algorithm stores only the raw values
it actually samples and removes every occurrence of those values after a safe sample-incident claw
check.

Below the cap, put

\[
 T:=\sqrt Nq^{1/4},\qquad b_*:=q^{3/2},\qquad
 m_*:={N\over T}=\sqrt Nq^{-1/4}.
 \tag{ME.2}
\]

Then a spectrum is killed by this attack whenever some `ell=o(T)` makes

\[
 R+\sum_jh_jM_j e^{-\ell M_j/N}=o(q^{3/2})
 \tag{ME.3}
\]

with enough slack to absorb the sixth power of the compression polylogarithm.  Section 6 gives the
exact log-aware form.

There is **no universal subtarget theorem for all such spectra within this attack class**.  A legal
two-scale spectrum already saturates (ME.1): use one side-exclusive label of multiplicity
`Theta(N)` and `Theta(q)` side-exclusive labels of multiplicity `Theta(sqrt(q))`, plus `Theta(q)`
singleton candidates.  Sampling `O(log N)` positions removes the macroscopic label, but the
remaining decoy mass is `Theta(q^(3/2))`, so the compressed Johnson child costs exactly
`Theta(sqrt(N)q^(1/4))`.  Conversely, any sample of size `o(T)` removes only an asymptotically
negligible fraction of that critical shelf.  Thus the analytic envelope is `Theta(T)` on this
family (polylogarithmic overhead aside).

This does **not** prove the two-scale promise hard.  It proves only that the palette-exposure attack
which killed the balanced single-scale profile no longer gives a little-oh algorithm.  A different
algorithm might exploit duplicate testing, a joint walk, or another statistic.

## 2. Model and scope

Use `N` for the length of either claw list; replacing it by `floor(N_total/2)` changes only absolute
constants in a length-`N_total` 2-SUM reduction.  Each answer class has identical one-side frequency
spectra.  On each side there are:

1. candidate labels whose total occurrence mass is at most `R`; in the intended application these
   are `R=O(q)` distinct singleton labels, with zero common labels in NO and exactly one common
   singleton label in YES;
2. for every `j`, exactly `h_j` decoy labels of multiplicity `M_j`; and
3. no decoy label occurring on the opposite side.

The domain positions are independently permuted and the common alphabet is relabelled.  The total
number of labels over both sides is `O(q)`, and the alphabet has size `O(q)`.  The algorithm is
allowed to know the global promised spectrum, as is standard for promise query complexity, but it
is not told which raw value belongs to which scale.  Even knowledge of the spectrum is unnecessary
for correctness after an `ell` has been selected.

The proof below only uses the following weaker facts:

```text
- every actual claw touches the candidate part;
- the unresolved candidate mass per side is at most R;
- every decoy value is side-exclusive;
- a decoy value of multiplicity M survives deletion iff an ell-sample misses all M copies.
```

Thus (ME.1) also applies to variants with a more complicated rare part after replacing `R` by a
valid deterministic upper bound on its total residual mass.

## 3. The sample/delete/compress theorem

Define

\[
 D(\ell):=R+\sum_jh_jM_j e^{-\ell M_j/N}.
 \tag{ME.4}
\]

### Theorem 1 (Laplace-envelope upper bound)

For every integer `0<=ell<=N`, the promise above has a bounded-error quantum query algorithm of
cost

\[
 \widetilde O\!\left(\ell+\sqrt N\,D(\ell)^{1/6}\right).
 \tag{ME.5}
\]

Taking the best `ell` and the ordinary Johnson/MNRS `O(N^(2/3))` algorithm gives (ME.1).

### Proof

**Sampling and the safe deletion rule.**  Uniformly sample `ell` positions without replacement
from each side and query their values.  Check cross-equalities between the two stored samples
classically.  Then Grover-search the entire right list for membership in the sampled-left value
set, and symmetrically search the left list against the sampled-right value set.  These two
searches cost `O(sqrt(N))` queries, with constant-error amplification, and every returned pair is
verified.

After correctly negative incident checks, it is safe to delete on each side every position whose
same-side value occurred in that side's sample.  Indeed, any claw using a deleted value would have
been incident to a sampled occurrence and hence found by one of the two searches.  In particular,
this deletion rule does not classify sampled values as rare or heavy and never needs a public
scale label.

**Expected residual mass.**  A fixed decoy value of multiplicity `M` is missed with probability

\[
 {\binom{N-M}{\ell}\over\binom N\ell}
 \le (1-M/N)^\ell
 \le e^{-\ell M/N}.
 \tag{ME.6}
\]

Let `B_L,B_R` be the two residual position sets.  We conservatively retain all candidate mass,
even though sampled candidates are also safely deleted.  Therefore

\[
 \mathbb E|B_L|,\ \mathbb E|B_R|\le D(\ell).
 \tag{ME.7}
\]

Markov's inequality and a union bound give, with an absolute positive constant probability,

\[
 |B_L|,|B_R|\le 6D(\ell).
 \tag{ME.8}
\]

No independence between different missed labels is assumed.  Constant repetition suffices to
turn this good-sample probability into bounded error.

**Count, gate, and compress.**  Membership in either residual is testable with one input query and
a coherent lookup in the stored sample-value table.  Run the capped residual count used in the
reviewed ABI compression construction and reject this branch if its verified upper estimate
exceeds a deterministic constant multiple of `D(ell)`.  On (ME.8) and the good-count event this
gate continues.  Its `O-tilde(sqrt(N))` cost is absorbed by (ME.5), since a nontrivial YES promise
has `D(ell)>=1`.

For a residual size ceiling `b=O(D(ell))`, the random-permutation first-member construction makes a
virtual residual list of length `O-tilde(b)`.  One virtual coordinate costs

\[
 \widetilde O(\sqrt{N/b})
 \tag{ME.9}
\]

original queries, and logarithmic duplication covers every residual position with high
probability.  Run the ordinary `O(b^(2/3))` two-list claw/Johnson child on the virtual lists.  Its
original-query cost is

\[
 \widetilde O\!\left(\sqrt{N/b}\,b^{2/3}\right)
 =\widetilde O\!\left(\sqrt N\,b^{1/6}\right)
 =\widetilde O\!\left(\sqrt N\,D(\ell)^{1/6}\right).
 \tag{ME.10}
\]

Unequal left/right residual sizes can be rounded to the larger ceiling with internal tagged
dummies that never compare equal.  Every reported pair is unwrapped and checked on the original
input, so bad sampling, counting, coverage, or nested-oracle events can cause a false negative but
not an accepted false positive.  All branches have the deterministic gate and query caps required
by the local reviewed construction.  Adding the samples and incident checks proves (ME.5).  Taking
the best `ell` and the ordinary Johnson cap proves (ME.1).  QED.

### Continuous optimizer

Ignoring integer rounding and polylogarithms, put

\[
 G(\ell):=\sum_jh_jM_j^2e^{-\ell M_j/N}.
 \tag{ME.11}
\]

At any interior stationary point of
`ell+sqrt(N)D(ell)^(1/6)`, one has

\[
 G(\ell)=6\sqrt N\,D(\ell)^{5/6}.
 \tag{ME.12}
\]

Thus an arbitrary finite spectrum requires only a one-dimensional optimization; endpoints and all
solutions of (ME.12) can be compared.  No convexity claim is needed.

## 4. Frequency-cutoff forms

Define the cumulative low-frequency mass

\[
 S(\tau):=R+\sum_{j:M_j<\tau}h_jM_j.
 \tag{ME.13}
\]

For any `tau>=1` and `lambda>=0`, take

\[
 \ell=\left\lceil {\lambda N\over\tau}\right\rceil.
 \tag{ME.14}
\]

Every band with `M_j>=tau` contributes at most an `e^(-lambda)` fraction of its mass to (ME.4),
so

\[
 D(\ell)\le S(\tau)+Ne^{-\lambda}.
 \tag{ME.15}
\]

The expectation-based cutoff envelope is therefore

\[
 Q_{\rm SC}le
 \widetilde O\!\left(
 {\lambda N\over\tau}
 +\sqrt N\,[S(\tau)+Ne^{-\lambda}]^{1/6}
 \right).
 \tag{ME.16}
\]

This is usually stronger than demanding coupon collection.  If one specifically wants every
label of multiplicity at least `tau` to be sampled, a union bound over at most `Cq` labels permits

\[
 \lambda=\log(Cq/\delta),
 \tag{ME.17}
\]

and yields, with probability at least `1-delta`, the deterministic residual bound `|B|<=S(tau)`.
Consequently

\[
 Q_{\rm full\ cover}\le
 \widetilde O\!\left(
 {N\over\tau}\log(q/\delta)
 +\sqrt N\,S(\tau)^{1/6}
 \right).
 \tag{ME.18}
\]

The `log q` in (ME.18) is a full-palette-coverage charge, not an inherent sampling charge in
(ME.1).  Markov control of total residual mass is why (ME.1) and (ME.16) avoid it.

### Theorem 2 (stratified cutoff envelope)

Multiple cutoffs can be stronger than one original-list sample, because after a high-frequency
band is deleted one can sample uniformly from the smaller residual.  This possibility is also
captured without public scale labels.

Choose decreasing thresholds

\[
 \infty=\tau_0>\tau_1>\cdots>\tau_k\ge2,
 \qquad
 B_0:=N,\quad B_i:=S(\tau_i).
 \tag{ME.S1}
\]

At stage `i`, capped-count the current residual, use independent random-permutation first members
to sample it uniformly, and take enough residual samples to cover every still-present value of
multiplicity at least `tau_i`.  One residual sample costs
`O-tilde(sqrt(N/B_(i-1)))` original queries, while coupon coverage needs
`O((B_(i-1)/tau_i) log(qk/delta))` samples.  Raw sampled values are added to one cumulative deletion
set.  The two sample-incident searches may be postponed until all stages finish, because every
deleted candidate value remains stored and is then searched against the complete opposite list.

Let `Lambda=Theta(log(Nqk/delta))` include coupon coverage, truncated first-member sampling,
counting, and constant-error allocation, and let `L_res=polylog(Nqk/delta)` be the terminal coherent
compression factor.  A worst-case capped implementation gives

\[
 Q_{\rm strat}\le
 O\!\left(
 \Lambda\left[(k+1)\sqrt N+
 \sum_{i=1}^k{\sqrt{NB_{i-1}}\over\tau_i}\right]
 +L_{\rm res}\sqrt N\,B_k^{1/6}
 \right).
 \tag{ME.S2}
\]

To justify the stage invariant, condition on all earlier coverage events, so the current residual
has size at most `B_(i-1)`.  Counting supplies its actual size `b`.  Sampling
`Theta((b/tau_i)log(qk/delta))` uniform residual coordinates misses a fixed remaining value of
multiplicity `M>=tau_i` with probability at most `exp(-Theta(log(qk/delta)))`; a union bound over
`O(q)` raw values proves that the next residual is at most `B_i`.  The original-query sampling cost
is

\[
 \widetilde O\!\left(
 {b\over\tau_i}\sqrt{N/b}\right)
 \le \widetilde O\!\left({\sqrt{NB_{i-1}}\over\tau_i}\right).
 \tag{ME.S3}
\]

Bad counts or coverage events meet deterministic gates and can only create false negatives; final
original-input verification prevents false positives.  Taking the infimum of (ME.S2) over all
finite threshold sequences, together with (ME.1) and Johnson, is the strongest generic ceiling
obtained here from the commissioned primitives.

## 5. Target normalization

For `5<=q<=N^(2/3)`, the desired uncapped scale is

\[
 T=\sqrt Nq^{1/4}.
 \tag{ME.19}
\]

Using (ME.2), write `ell=xT`.  Then

\[
 {\ell M_j\over N}=x{M_j\over m_*}
 \tag{ME.20}
\]

and define the normalized Laplace residual

\[
 \Psi(x):={1\over q^{3/2}}
 \left[
 R+\sum_jh_jM_j e^{-xM_j/m_*}
 \right].
 \tag{ME.21}
\]

If `L(N,q)` denotes the polylogarithmic factor in coherent residual access and amplification, then
(ME.1) implies the explicit ratio bound

\[
 {Q_{\rm SC}\over T}
 \le O\!\left(
 \inf_{x\ge0}\{x+L(N,q)\Psi(x)^{1/6}\}
 \right),
 \tag{ME.22}
\]

together with the Johnson ratio

\[
 {N^{2/3}\over T}
 =\left({N^{2/3}\over q}\right)^{1/4}\ge1.
 \tag{ME.23}
\]

Equation (ME.21), rather than the number of declared scales, is the invariant seen by this entire
attack family.

## 6. Explicit necessary inequalities for a survivor

The following are necessary only for surviving the algorithm above; they are not sufficient for a
lower bound.

### 6.1 Exact Laplace condition

If along any claimed asymptotic regime there is a choice `x=x(N,q)` such that

\[
 x=o(1),\qquad
 \Psi(x)=o(L(N,q)^{-6}),
 \tag{ME.24}
\]

then (ME.22) gives `Q_SC=o(T)` and refutes a uniform `Omega(T)` claim for that promise.  Therefore
every survivor must obey

\[
 \text{there is no sequence }x=o(1)\text{ for which }
 R+\sum_jh_jM_j e^{-xM_j/m_*}
 =o(q^{3/2}/L^6).
 \tag{ME.25}
\]

This is the strongest concise necessary inequality produced by the audit.

### 6.2 Cutoff condition

By (ME.16), a spectrum is also killed whenever some pair `(tau,lambda)` satisfies all three
conditions

\[
 {\lambda m_*\over\tau}=o(1),
 \qquad
 S(\tau)=o(q^{3/2}/L^6),
 \qquad
 Ne^{-\lambda}=o(q^{3/2}/L^6).
 \tag{ME.26}
\]

Thus a survivor must violate at least one inequality in (ME.26) for **every** cutoff pair.  For a
convenient log-audited specialization, take

\[
 \lambda\ge
 \log\!\left({NL^6\over q^{3/2}}\right)+\omega(1).
 \tag{ME.27}
\]

For every `tau` with `tau/(lambda m_*) -> infinity`, survival requires

\[
 R+\sum_{j:M_j<\tau}h_jM_j
 =\Omega(q^{3/2}/L^6).
 \tag{ME.28}
\]

When `q->infinity`, the intended singleton part has `R=O(q)=o(q^(3/2))`, so decoys themselves
must supply the mass in (ME.28).

### 6.3 Consequence of the `O(q)` label budget

Because `sum_j h_j<=Cq`, any cumulative decoy mass of order `q^(3/2)/L^6` forces an average
multiplicity at least

\[
 \Omega(\sqrt q/L^6).
 \tag{ME.29}
\]

Dyadic pigeonholing refines this: up to one additional `O(log N)` factor, a survivor must contain
some frequency band `[m,2m)` with

\[
 \sum_{j:m\le M_j<2m}h_jM_j
 =\Omega\!\left({q^{3/2}\over L^6\log N}\right),
 \qquad
 m=\Omega\!\left({\sqrt q\over L^6\log N}\right),
 \tag{ME.30}
\]

and, by choosing the cutoff in (ME.28), this mass-bearing band cannot all escape above every
subtarget-exposure scale.  Informally, the spectrum needs a `q^(3/2)`-mass shelf carried by at most
`O(q)` hidden values, beginning around multiplicity `sqrt(q)` (up to logs).  Merely adding many
named scales without satisfying (ME.25) does nothing.

### 6.4 Stratified condition

The stronger multistage theorem supplies one more mandatory test.  For every decreasing threshold
sequence in (ME.S1), a survivor must prevent the three quantities

\[
 {\Lambda(k+1)\over q^{1/4}},
 \qquad
 {\Lambda\over q^{1/4}}
 \sum_{i=1}^k{\sqrt{B_{i-1}}\over\tau_i},
 \qquad
 L_{\rm res}\left({B_k\over q^{3/2}}\right)^{1/6}
 \tag{ME.S4}
\]

from tending to zero simultaneously.  If some sequence makes all three `o(1)`, (ME.S2) is an
`o(T)` algorithm.  This condition catches a nominally multiscale law whose bands can be peeled in
cheap succession even when no single original-list cutoff is optimal.

## 7. A legal spectrum that saturates the envelope

This section demonstrates why the audit cannot prove that every spectrum is subtarget.

For growing `q`, take on each side

```text
r=floor(q/8) candidate singleton labels;
h=floor(q/8) critical decoy labels, each of multiplicity m=max{2,floor(sqrt(q))};
one macroscopic decoy label of multiplicity M_0=N-r-hm.
```

Choose constants slightly smaller if needed for finitely many rounded parameters.  For
`q<=N^(2/3)`,

\[
 hm=\Theta(q^{3/2})\le\Theta(N),
 \qquad M_0=\Theta(N).
 \tag{ME.31}
\]

Use disjoint decoy palettes on the two sides.  In NO use disjoint singleton palettes; in YES
identify exactly one singleton across the sides.  The marginal spectra remain identical.  The NO
union uses

```text
2r+2h+2 <= q/2+2 <= q
```

for all sufficiently large `q`, so even an exact `q`-element range suffices; certainly the range
is `O(q)`.  All label identities and positions may be uniformly permuted.  No scale tag is public.

For this spectrum,

\[
 D(\ell)
 =r+hm e^{-\ell m/N}+M_0e^{-\ell M_0/N}.
 \tag{ME.32}
\]

**Upper side.**  With `ell=C log N`, the macroscopic term is negligible and

\[
 D(\ell)=O(q^{3/2}).
 \tag{ME.33}
\]

Since `log N=o(T)`, (ME.5) gives `Q_SC=O-tilde(T)`.

**Lower side of this particular envelope.**  If `ell>=cT`, the sampling term itself is
`Omega(T)`.  If `ell<cT`, then

\[
 {\ell m\over N}
 =O\!\left({T\sqrt q\over N}\right)
 =O\!\left({q^{3/4}\over\sqrt N}\right)
 =O(1)
 \tag{ME.34}
\]

uniformly for `q<=N^(2/3)`.  Hence a constant fraction of the critical `hm=Theta(q^(3/2))` mass
remains and the child term in (ME.5) is `Omega(T)`.  Therefore

\[
 \inf_\ell\left\{\ell+\sqrt N D(\ell)^{1/6}\right\}
 =\Theta(T).
 \tag{ME.35}
\]

For the finitely many bounded values including `q=5`, use one singleton candidate and one
macroscopic side-exclusive decoy per side.  Four raw labels suffice in NO, and after the
macroscopic labels are sampled the residual has constant size.  This gives `Theta(sqrt(N))`, which
is exactly `Theta(sqrt(N)q^(1/4))` for fixed `q`.

The important diagnostic is that a growing ladder is **not necessary merely to defeat the
sample/delete/compress ceiling**.  One macroscopic cleanup scale plus one critical shelf already
does so.  Whether this simpler promise survives algorithms outside (ME.1) is wholly open.

It also saturates the stratified envelope.  After the macroscopic value is removed, the residual
has size `b=Theta(q^(3/2))`, and the critical values have multiplicity `m=Theta(sqrt(q))`.  Removing
a constant fraction of that shelf requires `Theta(b/m)=Theta(q)` uniform residual samples.  Each
such sample costs `Theta(sqrt(N/b))` original queries, so the exposure cost is

\[
 \Theta(q)\sqrt{N/q^{3/2}}
 =\Theta(\sqrt Nq^{1/4})=\Theta(T).
 \tag{ME.S5}
\]

With `o(q)` total residual samples, a `1-o(1)` fraction of the shelf survives and the terminal
Johnson term remains `Theta(T)`.  Splitting those samples among arbitrarily many rounds does not
change this dichotomy.  Thus neither one-stage nor stratified use of the commissioned primitives
gives a little-oh algorithm on the critical-shelf law.

## 8. Endpoint audit

### `q=5`

Here `T=Theta(sqrt(N))` and `b_*=Theta(1)`.  The singleton candidate mass alone is already a
constant residual after the macroscopic decoys are sampled.  The compression child costs
`Theta(sqrt(N))`; no little-oh conclusion is expected or obtained.  The construction above uses
at most four labels in NO and is legal.

### `q=N^kappa`, `0<kappa<2/3`

Now

\[
 T=N^{1/2+\kappa/4},\qquad
 b_*=N^{3\kappa/2},\qquad
 m_*=N^{1/2-\kappa/4}.
 \tag{ME.36}
\]

The balanced single-scale promise had all decoys at multiplicity `N/q`, so `O(q log q)=o(T)`
samples exposed them and left only `O(q)=o(b_*)` residual mass.  It violates (ME.25).

The saturating spectrum instead leaves `Theta(b_*)` mass at multiplicity `sqrt(q)`.  Since

\[
 {\sqrt q\over m_*}
 ={q^{3/4}\over\sqrt N}=o(1),
 \tag{ME.37}
\]

every `o(T)` sample has vanishing exposure exponent on this shelf.  It satisfies the necessary
Laplace condition for this attack throughout every strictly subcritical polynomial regime.

### `q=Theta(N^(2/3))`

At the crossover,

\[
 T=N^{2/3},\qquad b_*=N,
 \qquad m_*=N^{1/3}=\sqrt q.
 \tag{ME.38}
\]

Thus an endpoint survivor needs linear residual mass at the critical frequency scale, up to the
logarithmic slack quantified in (ME.25)-(ME.30).  The saturating shelf has exactly that form and
ordinary Johnson matches the cap.  By contrast, a spectrum whose entire linear mass lives on a
few `omega(sqrt(q))`-frequency labels is vulnerable if those labels can all be exposed by an
`o(N^(2/3))` sample; (ME.25) makes the required quantifier precise.

## 9. Logarithm and information audit

| issue | exact treatment |
|:---|:---|
| sample size | `2ell` total queries; the factor two is absolute |
| miss probability | exact hypergeometric bound (ME.6) |
| controlling total residual | Markov, constant probability; **no coupon log** |
| exposing every value above a cutoff | requires `log(q/delta)`, (ME.17)-(ME.18) |
| sample-incident claws | two `O(sqrt(N))` membership Grover searches plus verification |
| residual count/gate | capped worst-case query schedule; `O-tilde(sqrt(N))` |
| virtual coverage | `O(log N)` duplicates |
| coherent nested access | polylogarithmic amplification factor `L(N,q)` |
| Johnson/MNRS child | `O(b^(2/3))` virtual queries |
| bad branches | deterministic gate and final original-input verification prevent false positives |
| public scale labels | **never used**; deletion is by sampled raw-value equality only |
| knowing the global spectrum | promise advice only; selects `ell`, not value roles |

If even the global spectrum is not supplied, one may run geometrically spaced sample budgets and
residual ceilings, paying another polylogarithmic factor.  In promise query complexity this is not
needed, but it confirms that no per-value band oracle is hidden in (ME.1).

## 10. What remains open inside the node

The upper audit leaves a sharply narrower feasibility target:

1. freeze an exact YES/NO orbit whose Laplace residual satisfies (ME.25) in every claimed regime;
2. preferably begin with the simpler critical-shelf spectrum of Section 7, since a long frequency
   ladder is not needed against the registered sampling attack;
3. attack that orbit with duplicate classification, support/collision estimation, frequency-aware
   Johnson states, and genuinely joint walks before attempting a dual;
4. only if all such algorithms fail, seek an adversary lower bound and the exact cyclic 2-SUM
   embedding.

No query lower bound follows from (ME.25), and no exponent claim should be advanced from this memo
alone.

## 11. Distinct routes generated outside this node

**None tested.**  The critical-shelf specialization in Section 7 is a frequency law within the
registered `multiscale-frequency-mask` node, not a new proof technology.  The following possible
attacks are named only as untested obligations already implicit in this node: coherent duplicate
classification, a frequency-aware joint walk, and estimation of a joint support/collision
statistic.  If any of these is promoted into a mathematically distinct construction or lower-bound
route, it must receive its own canonical node before work under Rule 8.
