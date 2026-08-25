# KSUM.B4b.L2 phase 6 — non-composition spine+satellite transfer

Date: 2026-07-19  
Status: **BLOCKED for the optimizer-faithful, irrep-label-only spine+satellite transfer class;
new obstruction candidate pending independent rule-7 review.**  
Scope: cyclic 2-Sum. No exponent claim is made from finite instances (G11).

## Decision

The representation labels can be recovered and align exactly as predicted, but they do not supply
the missing internal coordinates needed to turn the L33 optimizer into an L2 signed measure.
There are two separate representation-theoretic obstructions:

1. L33 decomposes a stabilizer-commutant **PSD operator** into irreps of
   `H=S_(N-1) x C(sigma)`. Its multiplicity basis has an independent orthogonal gauge in every
   sector. Irrep labels align sectors across `N`; they do not align multiplicity coordinates or the
   observed top eigenvector.
2. A direct vector transfer of a nontrivial satellite is killed by invariant averaging. The
   canonical positive operator transfer, `mu=Reynolds(diag(A))/trace(A)`, is nonnegative and has
   constant factorial moment one, hence annihilation band zero.

This meets the frozen **BLOCKED** condition as a new scoped obstruction to the requested
non-composition spine+satellite form. It does not refute L2. A signed recombination built in a new
canonical multiplicity basis remains open.

Combined with reviewed M2 (pair-product independence), phase-4 T1 (unaveraged sign-bit
composition), phase-4 T2 (whole-pair value budget), and phase-5 T2 (equal-total orientation
coherence), L2P6-G gives a **candidate paradigm-level obstruction map**: the standard independent
composition architectures are blocked on their hard classes, while the most literal
optimizer-guided non-composition transfer fails at the operator/vector boundary. The reviewed M1
slice calculus and phase-5 band-multiplication lemma remain positive tools, not kills. The map's
surviving region is genuinely signed, canonically multiplicity-labeled, non-product coupling.

Preregistration: [predictions.txt](logs_ksum_L2p6_20260719/predictions.txt).  
Commands: [COMMANDS.txt](logs_ksum_L2p6_20260719/COMMANDS.txt).  
Hashes: [SHA256SUMS.txt](logs_ksum_L2p6_20260719/SHA256SUMS.txt).

## 1. Inherited reviewed scope

The phase did not reopen the completed components outside these uses:

- **M1:** exact factorial cancellation on every fixed-total slice for the explicit pair kernel.
- **M2:** the five-condition locally zero-balanced, sign-separated pair-product class and its
  sign-aligned positive mixtures, only as stated for odd `q>=5`.
- **L2P3:** band `2(1+floor(log_5((q-1)/2)))` and correlation at least
  `437/581`; no `N`-growth.
- **Phase-4 T1/D10:** the correlation product applies before norm-changing averaging in the
  fixed-allocation sign-bit class; D10 leaves the general averaging escape open.
- **Phase-4 T2:** only whole-pair/value-disjoint allocation.
- **Phase-5 T1:** the positive general occupancy-convolution band-multiplication lemma.
- **Phase-5 T2:** only identical phase-3 blocks, one common exact pair total, and a raw product
  coupling before averaging. Unequal totals, nonidentical blocks, non-product couplings,
  alternative inners, and non-composition shapes were expressly outside that review.

## 2. Exact L33 representation labels

### Type correction

The reviewed L33 reduction fixes a query position. Its Wedderburn labels are therefore irreps of

`H=S_(N-1) x C(sigma)`,

not irreps of the full `S_N x C(sigma)` acting on a signed-measure vector. Full `S_N` invariance is
recovered in L33 by transporting the stabilizer block among query positions. This distinction is
load-bearing below.

The fresh labeler rebuilds the deterministic reviewed decomposition read-only. It identifies the
`S_(N-1)` partition from the normalized transposition character and the alphabet irrep from exact
small-centralizer character types. Character residuals are at floating roundoff scale; the labels
are discrete exact representation names. Full output is in
[labels.json](logs_ksum_L2p6_20260719/labels.json), with raw
[log](logs_ksum_L2p6_20260719/labels.log).

| point | dominant spine | leading satellites by trace | key shares |
|---|---|---|---|
| `(5,4,0)`, `tau=2` | `[4] x (+pair,+fixed)` | `[3,1] x (+,+)`, `[3,1] x (+,-)`, `[3,1] x (-,+)` | spine 41.06% trace, 93.35% Frobenius |
| `(5,4,1)`, `tau=0` | `[4] x ((2),empty)` | `[4] x ((1),(1))`; `[3,1] x ((1),(1))`; `[3,1] x ((1,1),empty)` | spine 39.98% trace, 85.33% Frobenius; repetition-two satellite 22.33% trace, 12.17% Frobenius |
| `(6,3,0)` | `[5] x C2-triv` | `[4,1] x C2-triv`; `[4,1] x C2-sign`; `[5] x C2-sign` | spine 42.80% trace, 96.57% Frobenius |
| `(7,3,0)` | `[6] x C2-triv` | `[5,1] x C2-triv`; `[5,1] x C2-sign`; `[4,2] x C2-triv` | spine 35.82% trace, 97.88% Frobenius |

Here `((alpha),(beta))` is the bipartition label for `C2 wr S_2=B_2`; `((1),(1))`
is its unique two-dimensional irrep. The frozen label predictions all pass, including the
repetition-two prediction.

## 3. The attempted ansatz and its type

For an L33 sector `lambda`, let `Q_(lambda,j): R^(m_lambda)->V` be its aligned multiplicity frames,
`j=1,...,d_lambda`. The optimizer-shaped operator ansatz is

`A = sum_lambda sum_a w_(lambda,a) sum_(j=1)^(d_lambda)
     Q_(lambda,j) v_(lambda,a) v_(lambda,a)^T Q_(lambda,j)^T`,

with the spine the rank-one term in `lambda=([N-1],triv_C)` and `O(1)` satellite terms in the
labels in the table. This is not factorized over value pairs or position blocks.

As an operator formula it is well typed: `A in End(R^X)^H`, and nonnegative `w` make it PSD. It is
not yet an L2 witness, which must be a vector `mu in R^X` fixed by the full group and equipped with
factorial moments, `l1`, and correlation. The two natural transfers are:

- **vector transfer:** lift `v_(lambda,a)` through one frame and average it;
- **positive diagonal transfer:** set
  `mu_A=R_(S_N x C(sigma))(diag A)/trace(A)`.

The first loses every nontrivial satellite. The second keeps sector-diagonal information but has no
positive annihilation band.

## 4. Candidate obstruction theorem

### L2P6-G — gauge/type/constant-moment obstruction (candidate; pending review)

Let the only cross-parameter labels of a spine+satellite construction be the L33 irrep pairs, and
let its internal directions be coordinates in the reviewed solver's multiplicity blocks.

1. **Gauge:** replacing every frame by `Q_(lambda,j) O_lambda` and the block by
   `O_lambda^T B_lambda O_lambda`, for arbitrary orthogonal `O_lambda`, leaves the natural operator
   unchanged. Thus an internal coordinate profile is not an invariant of the archived optimizer.
   Irrep labels alone cannot define or fit it across `N`.
2. **Vector branch:** the Reynolds projection of a vector in a nontrivial irrep is zero. Hence a
   direct invariant signed-measure vector cannot retain the named nontrivial satellites.
3. **Positive-projector branch:** for every nonzero PSD `A`, `diag(A)>=0` and
   `sum_x diag(A)_x=trace(A)>0`. Reynolds averaging preserves these facts. After `l1`
   normalization, the degree-zero factorial moment is exactly one, so the annihilation band is
   zero.

Therefore an optimizer-faithful construction using only irrep labels and nonnegative PSD
spine/satellite weights cannot produce the required L2 dual polynomial. An escape must add a
canonical multiplicity label and a genuinely signed transfer/recombination; that new signed object
is not determined by the current optimizer decomposition.

The exact gauge gate uses the rational orthogonal matrix
`[[3/5,-4/5],[4/5,3/5]]`: the same natural operator has internal top-coordinate squares `(1,0)`
or `(9/25,16/25)`. The exact `S_3` standard-vector gate averages `(1,-1,0)` to zero. See
[obstruction.json](logs_ksum_L2p6_20260719/obstruction.json).

### Hard boundary

L2P6-G does **not** cover signed coefficients across canonical multiplicity projectors, nonlinear
off-diagonal extractions, a new joint-histogram/branching basis, or arbitrary non-composition
signed measures. It is a candidate theorem about the optimizer-faithful, irrep-label-only class,
not a refutation of the canonical L2 obligation.

## 5. Fit and held-out gate

The four training points confirm a stable exact spine label and the predicted satellite labels.
They do not define a cross-`N` internal profile: even the spine multiplicity dimensions are
`44,22,33,44`, and the solver bases in those spaces are independently gauge-rotatable.

The frozen held-outs were nevertheless solved with the reviewed pipeline:

| point | Adv+/- | leading label | spine Frobenius | held-out-refit rank-one oracle |
|---|---:|---|---:|---:|
| `(4,4,0)` | 3.00121227470243 | `[3] x (+pair,+fixed)` | 91.20% | 91.01% |
| `(4,5,0)` | 3.07786754591669 | `[3] x ((2),empty) x S1-triv` | 92.01% | 91.78% |

The label predictions pass and both oracle diagnostics exceed the frozen 75% threshold. The actual
no-refit closed-family capture is **not defined**: using each held-out eigenvector is a held-out
refit, while no gauge-invariant fitted profile exists. The gate therefore is not counted as
passed. The audit also records that the frozen phase-6 Frobenius metric is not numerically
interchangeable with L1's objective ratio `optimum/T`; no claim of beating L1's 38.90--62.83%
objective capture is made. See [fit_audit.json](logs_ksum_L2p6_20260719/fit_audit.json).

## 6. Exact finite closed-form gates

The canonical label-only positive fallback was instantiated exactly:

`mu = Reynolds(diag(P_([N-1],triv_C)+P_([N-2,1],triv_C))) / trace`.

Characters and group averages were evaluated with `fractions.Fraction`; no optimizer decimals were
used.

| point | invariance | `l1` | constant moment | correlation | band |
|---|---|---:|---:|---:|---:|
| `(4,5,0)` | exact | 1 | 1 | `49/95` | 0 |
| `(5,5,0)` | exact | 1 | 1 | `5/7` | 0 |

The second correlation exceeds `2/3`, but the constant moment already fails, so it is not a dual
polynomial of positive pure high degree. These are finite formula checks, not an asymptotic trend.

## 7. Escape ledger

- **Outside M2 (`q>=5`):** the operator ansatz is a global direct sum of stabilizer sectors, not a
  five-condition positive mixture of locally zero-balanced pair products. Its positive diagonal
  transfer is outside M2 because it is not locally or globally zero-balanced. No successful
  signed-measure escape is claimed.
- **Outside phase-4 T2:** no whole complementary-pair allocation or value-disjoint positional
  blocks occur.
- **Outside phase-5 T2:** there are no repeated identical phase-3 blocks, common exact pair total,
  or raw product outer tensor.
- **Outside phase-4 T1/D10:** it is not fixed-allocation absolute-value sign-bit composition and is
  invariant by a direct Reynolds transfer, not by normalizing that composition.

Thus none of the five old obstructions causes this failure. L2P6-G is a distinct operator/vector
and multiplicity-gauge obstruction.

## 8. Band, caps, and G11

No `omega(log q)` fixed-`q` band was obtained. The only well-defined positive label-only transfer
has band zero for every `N,q`; it fails the canonical target already at the constant row. The cap
sweep is therefore trivial at both `q=5` and `q=N`: zero is below the Johnson and B4a caps but also
strictly below `c0 min{sqrt(N)q^eta,N^(2/3)}` for every `c0>0`.

The phase-5 band-multiplication lemma is not applicable because this is not a convolution of
positional block measures. M1's slice cancellation cannot enter until a signed transfer with zero
constant moment is defined.

G11 is enforced: the four training labels, two held-out optimizers, oracle captures, and two exact
projector instances are structural evidence only. The general obstruction is analytic; no exponent
is inferred from finite values.

## 9. Outcome and next obligation

**Outcome: BLOCKED for the optimizer-faithful, irrep-label-only spine+satellite transfer class.**

The next viable redesign must first give an exact, cross-`N` label for multiplicity coordinates—for
example a branching/Gelfand--Tsetlin or joint-histogram harmonic basis—and then define a genuinely
signed operator-to-measure map in that basis. It must verify zero constant moment before fitting,
retain strict correlation `>2/3`, and prove `N`-growing band at fixed odd `q>=5`. Merely naming the
irrep pairs or copying positive optimizer block weights is now stopped.

The new theorem and all phase-6 mathematics are **CONJECTURED / pending independent rule-7 review**.
The route leaf remains CONJECTURED and the canonical cap-scale obligation is unchanged.

## 10. What was not checked

- No canonical multiplicity/branching basis was constructed, so no signed spine+satellite witness
  or no-refit internal profile was produced.
- No `N`-growing band, cap-scale witness, or exponent consequence was proved.
- No obstruction was proved for signed sector coefficients, nonlinear extractions, or arbitrary
  joint-histogram witnesses.
- The held-out optimizer values and label assignments are numerical; no rational SDP certificate
  or optimizer uniqueness theorem was produced.
- Even-`q` held-out `(4,4,0)` is structure evidence only and is not part of the canonical odd-`q`
  obligation.
- No independent rule-7 review was performed, no network was used, and no git commit was made.
