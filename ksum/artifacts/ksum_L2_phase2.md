# KSUM.B4b.L2 phase 2 — first asymptotic-kernel assault

Date: 2026-07-19  
Node status after implementing the completed repair review's D7 condition: **CONJECTURED · pending-review**.  
Phase-2 outcome: **BLOCKED for the coefficientwise sign-separated tensor ansatz**.  
Scope: canonical odd-`q` route only; no even-`q` strengthening and no exponent inference from numerics (G11).

## Outcome against the preregistration

The run proves an explicit general odd-`q` kernel and its conditioning-preserved annihilation band,
but the same product structure forces correlation `2^(1-(q-1)/2)`.  It is already `1/2` at `q=5`
and therefore cannot meet the required strict `>2/3` threshold for any canonical `q>=5`.

This matches the preregistered **BLOCKED** outcome, not PROGRESS or PARTIAL.  The obstruction is a
theorem for the tested pure sign-separated tensor subclass and a candidate lemma-for-the-kill for
any attempted construction that independently balances every complementary pair.  It does **not**
kill the full joint-histogram route: a correlated outer kernel can escape the factorized correlation
calculation.

## 1. Explicit coefficientwise-conditioned kernel

Fix odd `q`, `N>=q`, and target `t`.  The involution `sigma(a)=t-a` has one fixed point `f` and
`r=(q-1)/2` two-cycles.  Choose an orientation `(a_c,b_c)` of each cycle.  Put exactly one item at
`f`.  Choose a permutation-invariant distribution `lambda` on integer vectors

```text
(s_1,...,s_r),    each s_c >= 2,    sum_c s_c = N-1.
```

The concrete family uses the orbit of the balanced vector: its entries differ by at most one.

For `s>=2`, define probability measures on the pair-count slice `i+j=s` by

```text
A_s = (delta_(s,0) + delta_(0,s))/2,
I_s = delta_(s/2,s/2)                                      if s is even,
I_s = (delta_((s-1)/2,(s+1)/2)+delta_((s+1)/2,(s-1)/2))/2 if s is odd,
kappa_s = (I_s-A_s)/2.
```

Thus `A_s` is entirely on the local NO axes and `I_s` is entirely in the local YES interior.  Set

```text
mu = (-1)^(r+1) E_(s_1,...,s_r)~lambda [ tensor_c kappa_(s_c) ] tensor delta_(n_f=1).
```

Finally lift an occupancy weight uniformly to all strings in its `S_N` orbit.  Pair-swap symmetry
of `kappa_s` and permutation invariance of `lambda` make the lift `S_N x C(sigma)` invariant.  This
is genuinely conditioned on total occupancy `N`: every tensor summand already lies on that exact
slice, rather than being normalized after a Poisson approximation.

## 2. Lemmas

### Lemma 2.1 — local moments (PROVED here; pending independent review)

For every `s>=2`,

```text
sum kappa_s = 0,
sum kappa_s(i,j) i = 0,
sum kappa_s(i,j) j = 0,
||kappa_s||_1 = 1.
```

Proof.  Both `A_s` and `I_s` have total mass one and coordinate means `(s/2,s/2)`.  Their supports
are disjoint, so `(I_s-A_s)/2` has zero total and first moments and l1 norm
`(1+1)/2=1`.  These are exactly the falling-factorial moment conditions of pair-degree below two.

### Lemma 2.2 — conditioning-preserved annihilation (PROVED here; pending independent review)

The lifted `mu` annihilates every query polynomial of degree below `2r=q-1`.

Proof.  Fix a size vector before averaging over `lambda`.  An occupancy factorial monomial factors
over the `r` pairs as

```text
product_c (n_(a_c))_(u_c) (n_(b_c))_(v_c),
```

times a fixed-point factor.  If its total degree is below `2r`, then some pair has
`u_c+v_c<2`.  The corresponding local expectation is zero by Lemma 2.1, so the whole tensor
expectation is zero.  This holds separately on every exact-total size vector, hence averaging over
`lambda` cannot reintroduce leakage.  The independently reviewed phase-1 moment map establishes
that these factorial rows span all symmetrized one-hot query monomials without degree loss
([phase-1 report, §2](ksum_L2_phase1.md); [phase-1 review, S2](ksum_L2p1_review.md)).  Invariance then
lifts the cancellation to every query polynomial of degree below `q-1`.

### Lemma 2.3 — l1 normalization (PROVED here; pending independent review)

`||mu||_1=1`.

Proof.  A fixed-size tensor has l1 equal to the product of the local l1 norms, hence one.  Distinct
labeled size vectors have disjoint support because the pair totals recover the vector.  Within a
support point the sign depends only on which pairs are on axes versus interiors, not on the sizes,
so the permutation average introduces no cancellation.  The `lambda` mixture and uniform lift
therefore preserve l1 exactly.

### Lemma 2.4 — tensor-correlation obstruction (PROVED for this subclass; pending independent review)

For the above family,

```text
<mu,F> = 2^(1-r) = 2^(1-(q-1)/2).
```

In particular, it equals `1/2` at `q=5` and is at most `1/2` for every odd `q>=5`, so no fixed
positive margin above `2/3` is possible.

Proof.  The fixed point has occupancy one and never supplies a solution.  A global input is NO
exactly when every pair lies on an axis.  Each local signed axis mass is `-1/2`.  The global sign was
chosen so that the total NO mass is `-2^(-r)`.  Because every local kernel has total signed mass
zero, `mu` has total mass zero.  With `F=-1` on NO and `+1` on YES,

```text
<mu,F> = sum mu - 2 sum_NO mu = 0 - 2(-2^(-r)) = 2^(1-r).
```

The same calculation applies to any pure product of l1-normalized, sign-separated local kernels
whose zero constant moment balances an interior probability against an axis probability: zero
total forces absolute local YES and NO masses to be `1/2`.  Consequently the obstruction already
appears while annihilating the per-pair constant moment; adding the first moments `{1,i,j}` supplies
the proved `q-1` band but cannot repair correlation.

### Required asymptotic band and correlation (BLOCKED in this ansatz)

The annihilation machinery is exact but does not prove the requested lemma for any
`eta0>1/6`, because correlation fails uniformly on the canonical `q>=5` domain.  At `q=3` the
correlation is one, but the proved degree is only two and cannot reach `c0 sqrt(N) 3^eta0` for a
fixed positive `c0` as `N` grows.  No exponent claim follows.

The precise escape obligation is therefore:

> Construct a non-product outer signed kernel over the number and locations of interior pairs that
> preserves the coefficientwise total-`N` cancellations while keeping more than `2/3` normalized
> signed separation between the all-axis boundary and its complement.

This is the named candidate lemma-for-the-kill for the next assault: prove that a wider specified
class of independently balanced pair kernels also obeys a correlation bound at most `2/3`, or give
an explicit correlated outer kernel that violates it.

## 3. Exact finite instantiations

All arithmetic uses `fractions.Fraction`; the second script independently reconstructs the JSON
weights, all falling-factorial rows, the function labels, and the full centralizer action.

| case | claimed pure high degree | exact rows checked | exact l1 | exact correlation | `>2/3` |
|---|---:|---:|---:|---:|---|
| `(N,q,t)=(5,5,0)` | `4` | `56` (degrees `0..3`) | `1` | `1/2` | no |
| `(N,q,t)=(7,3,0)` | `2` | `4` (degrees `0..1`) | `1` | `1` | yes |

Every moment residual is exactly zero.  The verifier also checks invariance under centralizers of
orders `8` and `2`, respectively.  Odd-`q` target translation makes the chosen `t=0` representatives
equivalent to all targets; the proof itself was written for arbitrary `t`.

### Command, log, and SHA-256 triplets

| purpose | command | raw log | script SHA-256 |
|---|---|---|---|
| construct/check | `python ksum/tools/ksum_l2p2_pair_kernel.py --output ksum/artifacts/logs_ksum_L2p2_20260719/pair_kernel_results.json` | [pair_kernel.log](logs_ksum_L2p2_20260719/pair_kernel.log) | `5ce6e86c378b243e0d001fcb6f8665795477386e561d71326beda93df6d4f9ed` |
| independent reconstruction | `python ksum/tools/ksum_l2p2_exact_verify.py --input ksum/artifacts/logs_ksum_L2p2_20260719/pair_kernel_results.json` | [exact_verify.log](logs_ksum_L2p2_20260719/exact_verify.log) | `9943a5eac1cf29c1df4057c5bbe70b653bf8376783ea725a2451a326bae37b23` |

Machine-readable output SHA-256: `7e0cd489239b6793c4b4e1eed4d6bc901972f98ca0da120adfded7834a35c1f1`.
The preregistration SHA-256 is `dda78ed0b2999c8f9a988ba9ea68c36eaa94ec903c7557614a7daeda423cd2da`.
Commands and all hashes are archived in [the run directory](logs_ksum_L2p2_20260719/).

## 4. Literature boundary

The local BKT claim card verifies an explicit-dual-polynomial k-distinctness theorem and gives the
exact source locus (arXiv 1710.09079v3, Section 6, theorem source lines 2103–2113; informal theorem
lines 588–600), but the local page does not expose a block-composition lemma that can simply be
ported here ([BKT literature page, lines 10–16](../ksum/literature/bun-kothari-thaler-2018-dual-polynomials/README.md)).
No BKT lemma is imported into the proof above.

Ambainis's locally verified range-transfer theorem requires full `S_N x S_M` symmetry (source lines
299–323), explicitly not the present centralizer symmetry
([Ambainis literature page, lines 10–17](../ksum/literature/ambainis-2005-small-range-symmetric/README.md)).
It is not imported.  Kutin is only background in the local intake and has no verified local theorem
locus ([Aaronson–Shi page, line 24](../ksum/literature/aaronson-shi-2004-collision-lower/README.md)); nothing is attributed to it.  The only imported mathematical mechanism is the reviewed
occupancy/falling-factorial query-degree map cited in Lemma 2.2.

## 5. What was not checked

- No correlated outer dual, Christoffel estimate, or BKT-style dual block composition was constructed.
- No `eta0>1/6` asymptotic witness theorem, cap plateau, or exponent lower bound was proved.
- No even-`q` target or cycle type was attempted.
- No additional `(N,q,t)` point, optimizer extraction, or one-input held-out discriminator was run.
- The phase-2 lemmas have not received an independent rule-6 review; they remain pending-review.
- No network was used.
