# KSUM.B4b.L3.ALT.hidden-frequency-mask — upper-algorithm attack

Date: 2026-07-21

Controlling node: `KSUM.B4b.L3.ALT.hidden-frequency-mask`

Scope: adversarial upper-algorithm analysis of the rare-singleton/heavy-decoy profile motivated
by ABI lines 333--344.  Only local sources are used.  The analysis covers sampling and frequency
classification, Grover search, residual compression, Johnson/MNRS walks, variable-time
heuristics available locally, and conditioning on histogram statistics.  No DAG file is edited.

## Verdict

**The promise is algorithmically easier than the quarter-power target throughout every strictly
subcritical polynomial range, but no `o(N^(2/3))` algorithm is obtained in the critical window
`q=Theta(N^(2/3))`.**

For the balanced hidden-frequency profile frozen below, sampling enough positions to expose every
heavy label and then running the reviewed residual-claw walk gives

```text
Q_hidden(N,q)
 = O-tilde(q + sqrt(N) q^(1/6)).                         (HF.1)
```

More explicitly, the sampling term is `O(q log(q/delta))`; the tilde hides the reviewed virtual
residual-oracle amplification and coverage logarithms.

Consequently, for

```text
q=N^kappa,       0<kappa<2/3,                            (HF.2)
```

both terms in (HF.1) are little-oh of

```text
sqrt(N) q^(1/4).                                        (HF.3)
```

The same conclusion, including logarithms, holds whenever

```text
q log q=o(sqrt(N)q^(1/4)),
equivalently q=o(N^(2/3)/(log q)^(4/3)).                 (HF.4)
```

Thus this profile cannot support the proposed quarter-power lower bound uniformly below the
critical endpoint.

At `q=Theta(N^(2/3))`, however, the heavy-palette setup itself costs `Theta(N^(2/3))` before
logarithms.  Sampling `o(q)` positions leaves `Theta(N)` heavy-decoy positions with constant
probability, and the residual Johnson/MNRS child then costs `Theta(N^(2/3))`.  Sampling
`omega(q)` positions makes setup supercritical.  Frequency-aware Grover, direct Johnson walks,
and the locally available variable-time heuristics do not break this balance.

For `q>N^(2/3)`, the generic Johnson walk matches the capped target `N^(2/3)` and palette exposure
costs at least the cap; no little-oh algorithm is found there either.  The ABI endpoint is the
first unresolved window and already prevents a uniform upper refutation of the node.

The exact unresolved subproblem is therefore:

> At `q=Theta(N^(2/3))`, construct a coherent singleton-residual access mechanism, or a direct
> claw walk, that avoids explicitly learning `Theta(q)` hidden heavy labels and costs
> `o(N^(2/3))`; alternatively prove that no such mechanism exists.

This is essentially ABI's stated hard profile, now isolated from the already-easy subcritical
regimes.  No distinct route outside the registered node emerges.

## 1. A precise balanced profile for the attack

The node has not yet frozen exact counts.  To make the upper attack checkable, take one canonical
balanced version.  Assume initially that `q` is divisible by four and put

```text
h=q/4,       r=q/4.                                     (HF.5)
```

Each of the two length-`N` lists has:

```text
- h heavy labels, each of multiplicity floor/ceil((N-r)/h)=Theta(N/q);
- r singleton labels, each occurring once.              (HF.6)
```

The left and right heavy palettes are disjoint and absent from the opposite side.  Singleton
labels are disjoint from every heavy palette and distinct within each side.  The promise bit is

```text
NO: left and right singleton palettes are disjoint;
YES: their intersection consists of exactly one label.  (HF.7)
```

All domain positions and all alphabet labels are hidden by independent domain permutations and a
common range permutation.  The per-side frequency histograms are therefore identical in YES and
NO.  A claw exists exactly in the YES case and is the unique cross-list singleton pair.

The NO union uses exactly

```text
2h+2r=q                                                   (HF.8)
```

labels; YES uses one fewer, leaving an unused alphabet label.  Floor/ceiling multiplicities and
`q mod 4` change only constants.  Every upper bound below is robust under fixed positive constant
fractions in place of (HF.5).

The target envelope is

```text
T(N,q)=min{sqrt(N)q^(1/4), N^(2/3)}.                    (HF.9)
```

The critical point is `q=Theta(N^(2/3))`, exactly the profile named in ABI.

## 2. Heavy-palette exposure algorithm

Fix failure probability `delta<1/20`.  Independently on each side, query a uniformly random
sample without replacement of size

```text
ell=C q log(q/delta),                                   (HF.10)
```

capped at `N`, for a sufficiently large absolute constant `C`.  Store the sampled labels in a
classical lookup table.

### Sample-incident claw check

Check cross-equalities between the two stored samples classically.  Then Grover-search every
unsampled position on the right for membership in the sampled left-label set, and symmetrically
search the left list against the sampled right-label set.  This costs

```text
O(sqrt(N))                                               (HF.11)
```

queries, up to constant-error amplification.

If the unique singleton claw is incident to a sampled position, (HF.11) finds it.  Therefore,
after a correctly negative check it is safe to delete *every* position whose label appeared in
the same-side sample.  No frequency classification of sampled singleton labels is needed.

### Heavy coverage

Every heavy label has multiplicity at least `cN/q` for a fixed `c>0`.  Its probability of being
missed by a uniform `ell`-sample is at most

```text
exp(-c ell/q).                                           (HF.12)
```

A union bound over `Theta(q)` heavy labels on both sides makes the probability that any heavy
label is missed at most `delta` for the constant in (HF.10).

Condition on this good event and on a negative sample-incident search.  Every surviving position
is a singleton, there are at most `r=Theta(q)` survivors per side, and any genuine claw survives.

## 3. Residual claw cost

Let `b=Theta(q)` be the number of surviving indices on each side.  Membership in the residual set
is testable with one input query and a lookup in the stored sample-label table.

The reviewed ABI residual construction uses random permutations and minimum finding to expose a
virtual residual coordinate at cost

```text
O-tilde(sqrt(N/b))                                       (HF.13)
```

original queries.  Coverage requires only logarithmically many virtual duplicates.  Running the
standard `O(b^(2/3))` two-list claw/Johnson child on the virtual residual lists therefore costs

```text
O-tilde(sqrt(N/b) b^(2/3))
 =O-tilde(sqrt(N)b^(1/6))
 =O-tilde(sqrt(N)q^(1/6)).                              (HF.14)
```

The equivalent MNRS accounting from the local U1 audit is

```text
sqrt(N/b) (u + b/sqrt(u)),                              (HF.15)
```

minimized at `u=b^(2/3)` and giving (HF.14).  Thus (HF.1) follows from (HF.10), (HF.11), and
(HF.14).

## 4. Regime comparison

Below the cap crossover, divide the two main terms in (HF.1) by the target (HF.3):

```text
q log q /(sqrt(N)q^(1/4)) = q^(3/4)log q/sqrt(N),

sqrt(N)q^(1/6)/(sqrt(N)q^(1/4)) = q^(-1/12).            (HF.16)
```

For every fixed `0<kappa<2/3`, substituting `q=N^kappa` makes both ratios tend to zero.  At fixed
`q`, the second ratio is a constant, so this attack matches the expected `Theta(sqrt(N))` scale
but does not give little-oh.

At the critical point `q=Theta(N^(2/3))`, the residual term after complete palette exposure is
only

```text
sqrt(N)q^(1/6)=Theta(N^(11/18)),                         (HF.17)
```

but learning the hidden palette by (HF.10) costs `Theta(N^(2/3)log N)`.  Dropping the union-bound
logarithm can bring setup to `Theta(q)`, but not to `o(q)=o(N^(2/3))`.

## 5. Partial sampling cannot break the endpoint within this framework

Let

```text
ell=xq.                                                   (HF.18)
```

A heavy label is unseen with probability `exp(-Theta(x))`.  Since unseen heavy labels retain all
`Theta(N/q)` of their positions, the residual size has the scale

```text
b(x)=Theta(q+N exp(-Theta(x))).                          (HF.19)
```

The sample/compress/Johnson strategy therefore has cost

```text
A(x)=Theta(qx)
     +O-tilde(sqrt(N)[q+N exp(-Theta(x))]^(1/6)).        (HF.20)
```

At `q=Theta(N^(2/3))`:

- If `x=o(1)`, almost every heavy label remains and `b=(1-o(1))N`; the child costs
  `Theta(N^(2/3))`.
- If `x=Theta(1)`, a constant fraction of heavy labels and positions remains; both setup and the
  child are `Theta(N^(2/3))`.
- If `x->infinity`, then setup is `omega(q)=omega(N^(2/3))`, even if the residual becomes small.

Hence no choice of sample size makes (HF.20) little-oh of the cap.  This is not a lower bound
against arbitrary quantum algorithms; it is an exact obstruction to the strongest locally
reviewed sample/compress/residual-child factorization on this profile.

## 6. Frequency classification and Grover attacks

### 6.1 Classifying one queried position

Given a position of value `v`, search the same list for a second occurrence.

```text
heavy v:     Theta(sqrt(N/(N/q)))=Theta(sqrt(q)) queries;
singleton v: Theta(sqrt(N)) queries to certify absence. (HF.21)
```

The long branch is exactly the branch containing the possible claw.  A fixed-time coherent
singleton predicate therefore costs `Theta(sqrt(N))`, too much to use inside an outer search or
walk.

Truncating the duplicate search at `Theta(sqrt(q))` rejects a heavy position only with constant
error.  Repetition can reduce the false-singleton rate, but with a constant number of repetitions
a constant fraction of the `Theta(N)` heavy positions enters the residual.  Driving the residual
to `o(N)` needs a growing number of repetitions and reintroduces the endpoint cost in coherent
residual access.

### 6.2 Searching positions

There are `Theta(q)` singleton positions per side but only one matching singleton position in the
YES case.  Finding an arbitrary singleton does not solve the problem: its probability of being
the matching one is `Theta(1/q)`.  Repeating singleton search with amplitude amplification loses
the hoped-for gain.

A direct Grover search over left positions using the predicate

```text
"this position is a singleton and its value occurs on the right"                  (HF.22)
```

has only one marked index and invokes the `sqrt(N)` negative searches in (HF.21).  It is worse
than the Johnson bound.  Pair-Grover over `N^2` cross pairs costs `Theta(N)`.

### 6.3 Searching labels

Searching the `q` possible labels does not help.  Testing whether one label occurs on both sides
requires certifying nonoccurrence on at least one side for every NO label.  Heavy labels are
side-exclusive and singleton labels are usually side-exclusive, so the expensive negative branch
is typical, not exceptional.

## 7. Johnson/MNRS walk attacks

The ordinary Johnson walk on subsets of `u` positions has

```text
setup =Theta(u),
spectral gap =Theta(1/u),
marked fraction =Theta((u/N)^2)                         (HF.23)
```

for the unique cross-list claw.  With query-free checking of stored values, MNRS gives

```text
Theta(u+N/sqrt(u)),                                     (HF.24)
```

minimized at `u=Theta(N^(2/3))`.  The promise does not create additional marked cross pairs;
heavy collisions occur only within one side and hence do not improve (HF.23).

Could a walk recognize and discard heavy values from its stored subset?  A fixed heavy label has
expected subset occupancy

```text
Theta(u/q).                                              (HF.25)
```

If `u=o(q)`, almost every sampled heavy occurrence looks locally like a singleton, so the walk
cannot expose the hidden mask.  At the critical point, taking `u=Theta(q)` is already
`Theta(N^(2/3))` setup; taking `u>>q` is supercritical.  Thus frequency-conditioned Johnson states
do not give little-oh within the standard stored-subset architecture.

Walking on subsets of value labels instead shifts the cost into finding an occurrence of each
selected label in the length-`N` lists.  No local data structure makes those occurrence queries
free, and the side-exclusive heavy palette forces negative searches.

## 8. Variable-time and nested-walk audit

No variable-time composition theorem suitable for this worst-case claw promise is present in the
local literature catalog; the U1 audit explicitly records that fact.  Even granting the usual RMS
heuristic does not yield a complete algorithm.

For duplicate testing of a uniformly random position, the rough squared-time average is

```text
(1-q/N)Theta(q) + (q/N)Theta(N)=Theta(q),               (HF.26)
```

so its RMS is `Theta(sqrt(q))`.  But every accepting path must process the exceptional singleton
branches, and the unique matching pair supplies only one marked left and one marked right index.
A naive application of a variable-time OR bound based on the sum of squared branch times charges
the scale

```text
sqrt(Nq),                                                (HF.27)
```

which is worse than `N^(2/3)` at the critical `q=N^(2/3)`.

The useful but unproved possibility would be a *joint* variable-time claw walk that amortizes the
long singleton-certification branches across both lists without first materializing a singleton
oracle.  Neither the local MNRS formula nor the locally cited chained-walk source provides such a
theorem for a worst-case unique pair.  Standard nesting reproduces (HF.14) after the palette is
known and (HF.24) before it is known.

Thus variable time is an exact unresolved technique boundary, not evidence of hardness.

## 9. Conditioning on histogram statistics

The separate frequency histograms of the two lists are identical in YES and NO by construction.
They reveal only

```text
{Theta(q) entries of frequency 1,
 Theta(q) entries of frequency Theta(N/q)}              (HF.28)
```

on each side, not which labels occupy which class.

The first joint statistic that distinguishes the promise is

```text
J=sum_v freq_L(v)freq_R(v).                              (HF.29)
```

Side-exclusive heavy palettes give no contribution, so `J=0` in NO and `J=1` in YES.  But
(HF.29) is exactly the number of cross-list claw pairs.  Conditioning on it assumes the answer.

The combined distinct-label count also differs by one between YES and NO, but resolving that one
unit among `Theta(q)` labels is another formulation of the same unique cross-collision problem.
Low-order moments of either side alone are identical.  Internal heavy collision counts are large
but equal across the promise classes and carry no location information about the rare mask.

Conditioning on the *complete heavy palettes* does help: it reduces the input to two
`Theta(q)`-element singleton lists and yields (HF.14).  Producing that conditioning coherently in
`o(q)` setup at the critical endpoint is precisely what is not known.

## 10. Exact unresolved subproblem

After the attacks above, the surviving task can be stated without reference to the broad L3
program.

### Hidden-palette residual access problem

At

```text
q=Theta(N^(2/3)),       M=Theta(N/q)=Theta(N^(1/3)),     (HF.30)
```

each side has `Theta(q)` singleton positions and `Theta(q)` hidden heavy labels of multiplicity
`Theta(M)`.  Heavy palettes are cross-disjoint; exactly zero or one singleton label is shared.

Construct, with total bounded-error cost `o(N^(2/3))`, either:

```text
(a) a coherent oracle/list for the singleton residual positions with enough coverage to run a
    subcritical claw child; or

(b) a direct joint walk/search that detects the unique common singleton without explicitly
    learning the heavy palettes.                         (HF.31)
```

The mechanism must not:

```text
- query/store Theta(q) heavy labels;
- leave Theta(N) false-singleton decoy positions;
- charge sqrt(N) separately to certify each true singleton;
- reduce to the ordinary unique-pair Johnson walk.       (HF.32)
```

No locally available sampling, Grover, Johnson/MNRS, frequency-counting, or variable-time theorem
satisfies (HF.31)-(HF.32).  Conversely, this audit does not prove an `Omega(N^(2/3))` lower bound
for the hidden-palette problem.

## 11. Gate ledger

| attack | result |
|:---|:---|
| exact balanced rare/heavy promise | frozen for analysis in (HF.5)-(HF.8) |
| expose all heavy labels by sampling | `O(q log q)` queries |
| sample-incident claw handling | `O(sqrt(N))`, exact on good search event |
| conditioned residual claw | `O-tilde(sqrt(N)q^(1/6))` |
| total conditioned algorithm | `O-tilde(q+sqrt(N)q^(1/6))` |
| `q=N^kappa`, `0<kappa<2/3` | **little-oh of quarter-power target** |
| fixed `q` | `Theta(sqrt(N))`, not little-oh |
| `q=Theta(N^(2/3))` | no `o(N^(2/3))` algorithm found |
| `q>N^(2/3)` | generic Johnson matches the cap; no little-oh improvement found |
| partial sampling optimization | cannot beat endpoint within sample/compress framework |
| direct Grover / pair-Grover | worse than Johnson |
| ordinary Johnson/MNRS | `Theta(N^(2/3))` |
| frequency-conditioned Johnson | setup reaches `Theta(q)=Theta(N^(2/3))` |
| variable-time idea | no applicable local theorem; RMS heuristic does not close |
| separate histogram conditioning | no information |
| joint statistic conditioning | exactly restates claw count |
| distinct outside-node route | **NONE** |

## 12. Conclusion

The rare-singleton/heavy-decoy promise is not uniformly quarter-power hard.  Once the heavy
palettes can be exposed below the target budget, the instance collapses to a compressed
`Theta(q)`-by-`Theta(q)` claw and the ABI `q^(1/6)` factor returns.  This gives a strict upper
improvement for every polynomial `q=N^kappa` with `0<kappa<2/3`.

The first serious surviving regime is the ABI endpoint `q=Theta(N^(2/3))`.  There, the number of
hidden heavy labels equals the entire `N^(2/3)` budget, while leaving a constant fraction
unlearned leaves a linear-size residual.  Standard Johnson/MNRS then exactly meets the cap.  Above
that endpoint the target stays capped and this audit also finds no little-oh algorithm, but the
critical window already contains the essential hidden-palette obstruction.

Accordingly the node should not claim a uniform quarter-power lower bound from this broad profile.
If it continues, it should be narrowed to the critical hidden-palette residual-access problem
(HF.30)-(HF.32).  This audit neither supplies a subcap endpoint algorithm nor confirms endpoint
hardness, and it generates no new route outside the registered node.
