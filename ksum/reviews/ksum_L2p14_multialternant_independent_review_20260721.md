# Independent Rule-7 review of k-Sum L2 Phase 14

Date: 2026-07-21  
Reviewed node: `KSUM.B4b.L2.ALT.multipair.variable-pair-totals`  
Reviewed artifact: `ksum/artifacts/ksum_L2_phase14_multialternant_distributed_boundary_20260721.md`  
Reviewer: fresh independent reviewer; not an author of the Phase-14 mathematics  

## Verdict

**PARTIAL PASS with one exact counterexample to the memo's final hard-boundary wording.**

The following narrow results pass independent derivation and exact gates:

- the formulas for `A_11,A_12,A_22`;
- the two-component identities (14.1) and (14.2), including the zero-correlation conclusion after
  all three cross gates;
- the concrete `q=5` specialization and its normalization/tail arithmetic;
- the repeated-common-split injection formula (14.3), residual (14.4), moment system (14.5) after a
  necessary range correction, normalization bound (14.6), and consecutive alternant formula
  (14.7);
- the reduction of the repeated-common-split family to an OR dual in active-count level, and the
  `O(sqrt(K))` Chebyshev ceiling;
- the displayed `q=5` and large-`q` legality subsequences and the `Theta(N^(4/3))` large-endpoint
  target-pair count.

However, the final boxed claim says that **a bounded collection** of one-active-pair alternants
cannot survive degrees 2, 3, and 4.  The analysis preceding it treats only two components.  The
generalization is false.  At `N=10,q=5,K=2`, the four orbit weights

| orbit | label | weight |
|---|---|---:|
| `{(1,8),(0,1)}` | YES | `-3/10` |
| `{(2,7),(0,1)}` | YES | `3/7` |
| `{(3,6),(0,1)}` | YES | `-1/5` |
| `{(0,9),(0,1)}` | NO | `1/14` |

have zero total mass, unit `l1`, nonzero sign correlation `-1/7` (reverse the sign for `+1/7`),
and annihilate **every** `q=5` orbit moment of degree `<5`, including all pure-side rows as well as
`A_11,A_12,A_22`.  The exact full matrix has shape `17 x 4`, rank 3, and zero residual on this
vector.  Thus three one-active-pair components plus one boundary atom already survive all the cited
degree-2/3/4 gates.  This does not meet the project's `>2/3` correlation target and does not rescue
the asymptotic route, but it refutes the asserted bounded-collection hard boundary.

Consequently the Phase-14 artifact as a whole cannot receive a completion status without narrowing
its hard boundary.  The canonical construction node must remain **OPEN**.

### Highest allowed status recommendations

- If separately registered with the exact two-component scope and typed ranges in this report,
  the obstruction (14.1)-(14.2) is eligible for **PROVED**.
- If separately registered for the repeated-one-common-split active-count family, with (14.5)
  capped to legal `rho` and with the Chebyshev construction stated explicitly, (14.3)-(14.7) and
  its asymptotic correlation obstruction are eligible for **PROVED**.
- The quoted “bounded collection of one-active-pair alternants cannot survive degrees 2,3,4” claim
  is eligible for **REFUTED/PARKED** if registered verbatim; the counterexample above is an exact
  independent certificate.  It must not be used to kill bounded-rank three-or-more-component
  designs.
- The full `variable-pair-totals` node remains **OPEN**: arbitrary heterogeneous joint-histogram
  kernels are still untreated.

No DAG, node, status, index, or handoff file was edited in this review.

## Rule 7c: anchoring-ban record

I first read only the canonical node claim.  Before opening the Phase-14 artifact I independently
expanded the first three cross moments, derived the boundary/correlation identity, stated the
univariate approximation ceiling with its degree conversion, and audited endpoint legality.  That
frozen record is
[`pre_proposer_derivation.md`](logs_ksum_L2p14_multialternant_review_20260721/pre_proposer_derivation.md).

Only then was the proposer artifact opened.  The notation `A_11,A_12,A_22,s,p` coincides with the
proposer after disclosure; the frozen note records that the formulas themselves were obtained
before that notation was seen.  The three-component counterexample was generated independently in
response to the unsupported final generalization, not copied from proposer work.

## Rule 7a: formula-by-formula type and dimension audit

### Split features and NO boundary

An occupied split is `tau=(r,u) in Z_{>=0}^2`, canonically unordered, with scalar total
`s=r+u` and scalar product `p=ru`.  For nonnegative query multiplicities `alpha,beta`,

`A_{alpha,beta}:Z_{>=0}^2 -> Q`,

`A_{alpha,beta}(r,u)=((r)_alpha(u)_beta+(r)_beta(u)_alpha)/2`.

Direct expansion gives the scalar identities

- `A_11=p`;
- `A_12=p(s-2)/2`;
- `A_22=p(p-s+1)`.

Their query degrees are 2, 3, and 4.  On a NO split `(0,s)`, every
`A_{alpha,beta}` with `alpha,beta>=1` is zero.  A NO histogram `B_lambda` is indexed by a positive
integer partition `lambda` of `N` into exactly `K` occupied totals and lies in the same orbit space
as the YES profiles.  Every injection-row factor querying both sides of any selected pair is zero
on such a histogram.  Pure-side features need not vanish; the memo correctly does not use boundary
blindness for them.

### Two-component formula and (14.1)-(14.2)

`delta_Y` and `delta_B` are standard basis vectors of the real vector space over legal orbit
histograms.  Thus

`W_raw=c_1 delta_{Y_1}+c_2 delta_{Y_2}+sum_lambda b_lambda delta_{B_lambda}`

is a signed vector in that space.  Here `p_i>0`, so the one-row matrix `[p_1 p_2]` has a
one-dimensional nonzero kernel generated by `(p_2,-p_1)`.  Substitution gives exactly

`p_1p_2(s_1-s_2)/2` in (14.1).

When `s_1=s_2=s`, substitution into `A_22` gives exactly
`p_1p_2(p_1-p_2)` in (14.2).  Equal sum and product determine the same unordered integer pair as
the roots of `z^2-sz+p`.  The active split is therefore the same and
`c_1+c_2=p_2-p_1=0`.  Since all YES mass sums to zero, zero total mass also makes aggregate NO
mass zero, so the `{+1,-1}` correlation is zero.  The full profiles need not be identical in their
unsplit remainders; the correlation conclusion depends only on their common YES label.

### `q=5` specialization

The domain is integral `N>=4` and `2<=a<b<=N-1`; `K=m=2`.  Both displayed pairs are occupied and
sum to `N`.  Their `(s,p)` values are `(a,a-1)` and `(b,b-1)`.  Substitution gives the claimed cubic
residual `(a-1)(b-1)(a-b)/2`.

For coefficients `(b-1,-(a-1))`, aggregate YES mass is `b-a`.  Minimum possible boundary `l1` is
`b-a`, so total `l1=2(b-1)` and normalized correlation `(b-a)/(b-1)`.  At
`(a-1)/(b-1)=1/4`, the larger-`C_t` YES atom has normalized absolute mass `1/8` and correlation is
`3/4`.  These are exact value statements, not evidence that the cubic gate passes.

### Repeated-common-split family and (14.3)-(14.5)

Parameters are integers `1<=j<=K<=m`, a fixed mixed split `tau=(r,u)` with `r,u>=1`,
`s=r+u`, `p=ru`, and total occupancy `N`.  `H_j` contains `j` identical active slots and `K-j`
positive one-sided slots.  Such remainder slots exist iff
`N-js>=K-j` when `j<K`; for `j=K`, legality requires `N=Ks`.

For a query using `rho` distinct complementary pair labels and one position from each side of each
label, the injection sum has `(j)_rho` nonzero ordered choices and value `p^rho` per choice.  Hence

`F_rho(H_j)=(j)_rho p^rho/((m)_rho(N)_{2rho})`.

This is a scalar rational value.  The displayed fraction is defined only for
`rho<=m` and `2rho<=N`; it is zero when additionally `rho>j` by the numerator convention.  At
`rho=2`, weights `(b,-a)` give exactly `ab(a-b)` after the positive common denominator is removed.

Equation (14.5) needs the range correction

`1<=rho<=min(floor((D-1)/2),m,K,floor(N/2))`.

The memo writes only `rho<=R=floor((D-1)/2)`.  For example, at `q=5,m=2`, the displayed denominator
is zero for `rho>=3`; these are nonexistent query rows, not additional constraints.  This type error
does not affect the `q=5` failure at `rho=2` or the stated large-endpoint regime where the required
Chebyshev degree is much smaller than `K<=m`.

### Normalization, consecutive levels, and (14.6)-(14.7)

For `c in R^J`, let `S=sum_j c_j`.  The boundary coefficient vector `b` must have sum `-S`, hence
`||b||_1>=|S|`.  The signed target correlation before normalization is `2S`, so

`|corr(W)| <= 2|S|/(sum_j|c_j|+|S|)`.

This proves (14.6), with absolute correlation understood.

For `R+1<=K`, the `R x (R+1)` matrix `[(j)_rho]`, `rho=1,...,R`, `j=1,...,R+1`, has rank `R`.
Its kernel is generated by
`c_j=(-1)^(R+1-j) binom(R+1,j)`.  Omitting the `j=0` term from the order-`R+1` finite difference
does not affect positive-order falling factorials.  Exact binomial sums give
`|S|=1`, `sum|c_j|=2^(R+1)-1`, and optimal-boundary correlation `2^{-R}`.  Formula (14.7) is
therefore correct on its typed range.

### OR pushforward and Chebyshev ceiling

Aggregate all NO boundary mass at active-count level zero: `mu_0=-S`, `mu_j=c_j` for `j in J`.
Then (14.5) plus zero total mass says that `mu` annihilates all falling factorials, hence all
univariate polynomials, through degree `R` on `{0} union J`.  The aggregation can only decrease
`l1`, because `|sum b_lambda|<=sum|b_lambda|`, while preserving target correlation.  This is the
well-typed OR-dual reduction for the repeated-common-split family.

An explicit sign approximant on all of `{0,...,K}` is

`P_d(x)=1-2 T_d((K+1-2x)/(K-1))/T_d((K+1)/(K-1))`,

for `K>=2`.  It has `P_d(0)=-1`; on `1<=x<=K` its error from `+1` is at most
`2/T_d((K+1)/(K-1))`.  Choosing the least `d` with the denominator at least 3 gives error at most
`2/3` and `d=O(sqrt(K))`.  Restricting it to any `{0} union J` preserves the bound.  Therefore, if
`R>=d`, every unit-`l1` pushforward annihilator has absolute correlation at most `2/3`.  This proves
the claimed ceiling, with the phrase “once `R` exceeds a constant multiple of `sqrt(K)`” understood
as a sufficiently large lower bound on `R`, not as the upper-bound notation `R=O(sqrt(K))`.

## Rule 7b: regime-complete identity gates

The archived exact script exercises:

- 81 diagonal/non-diagonal/boundary split cases for all three `A` formulas;
- 384 NO histograms with unequal and equal boundary totals, and 3,456 cross-feature zero identities;
- 2,170 unequal-active-total and 231 equal-active-total Attempt-1 cases;
- 286 legal `q=5` `(N,a,b)` cases and the exact `3/4`, `1/8` normalization example;
- both `j<K` and `j=K`, `m=K` and `m>K`, minimum and nonminimum unsplit remainders, and 936 direct
  injection comparisons for (14.3);
- 455 two-level residual gates for (14.4);
- consecutive alternants for `R=1,...,8` and 787 nonconsecutive active-level pushforwards;
- explicit Chebyshev identity/error gates at `K=2,3,5,8,16,32,64,128`;
- odd large-`q` endpoint subsequences `N=q=n^3`, `K=n^2`, `n=3,5,7,9`, including exact
  `K<=m`, occupancy, near-balanced integer splits, and `C_t/N^(4/3)` ratios;
- `q=5` common-type all-active legality on `N=2s`;
- the full `17 x 4` degree-`<5` `W_2` moment identity for the three-component counterexample,
  including pure-side rows.

Untested as positive constructions are all-`N` unequal-total repairs, even-`q` complement fixed-point
structure, and genuinely heterogeneous growing-rank tensors.  The Phase-14 artifact itself admits
that it is not an all-`N` construction.  The sentence saying an unequal-total `j=K` repair “returns
to (14.1)-(14.2)” is not proved: (14.1)-(14.2) concern two profiles with one active pair each, not
one profile containing several unequal active splits.  That sentence receives no completion credit.

## Rule 7d: no frozen-input immunity

No Phase-12 formula or prior review was treated as frozen.  `A_11,A_12,A_22`, the injection count and
normalizations in (14.3), all residuals, the OR pushforward, the Chebyshev polynomial, and both
endpoint legality calculations were reopened and derived independently for this use.  The complete
`q=5` degree-`<5` orbit matrix for the counterexample was also reconstructed directly from the
`W_2` action rather than imported from a previous script.  Prior asymptotic endpoint claims were not
used as immune inputs.

## Rules 7e and 7f: standing failure modes and value/formula decoupling

- **Normalization factors:** the direct injection code includes `(m)_rho(N)_{2rho}`; the correlation
  code includes the minimum boundary `l1`.  The script checks values before and after normalization.
- **Types/dimensions:** all maps and ranges are above.  The missing `min(m,K,N/2)` in (14.5) is a real
  display-level type defect, though harmless to the two cited endpoint failures.
- **Undefined terms/ranges:** “bounded collection,” “smallest,” “cheapest,” “standard Chebyshev,”
  “constant multiple,” and “additional unequal-total repair” are not formal definitions.  The report
  replaces the Chebyshev reference with an explicit polynomial and rejects the bounded-collection
  generalization.  A general `q` claim must state the number of complement two-cycles/fixed points.
- **Orbit/full-central confusion:** direct (14.3) gates use the full injection and orientation feature.
  The counterexample is checked against every `W_2` query orbit through degree four, including
  pure-side rows; it is not merely a colored or cross-row aggregate.
- **Numerics versus printed formula:** symbolic code directly evaluates the printed A and (14.1),
  (14.2), (14.4) identities.  A separate direct injection enumeration is compared with the printed
  (14.3) value 936 times.  The Chebyshev ceiling uses an independently supplied explicit polynomial
  because the proposer printed none.  The endpoint gates verify values, while the asymptotic orders
  are established algebraically.  The counterexample is an independent construction, not a test of
  a proposer formula.
- **Hardcoded-output risk:** every residual, rank, correlation, and legality result in the final log
  is computed by exact SymPy/integer arithmetic.  Expected ranks or pass literals are not simply
  printed.

The first local run of the test harness reached all algebraic gates but stopped at a test-code type
error in constructing a symbolic rational Chebyshev argument.  The expression was corrected to a
rational coefficient times the symbol and the entire suite was rerun cleanly.  No mathematical
claim relies on the failed partial run.

## Rule 7g: quantifier hygiene

The proven Attempt-1 obstruction quantifies over exactly **two** legal YES profiles with exactly one
mixed split each and arbitrary NO boundary coefficients.  It does not quantify over three or more
YES components.

The proven Attempt-2 obstruction quantifies over profiles whose active splits are all copies of one
fixed mixed split, with active level `j in J subseteq {1,...,K}` and typed legal query range above.
It does not quantify over heterogeneous split multisets.

“Correlation” means absolute `{+1,-1}` correlation after unit-`l1` normalization.  “Boundary” means
the set of legal histograms in which every complementary split is one-sided.  “Degree below `D`” is
strict, so the largest required cross-injection order is the corrected floor/minimum in (14.5).
“Constant high-`C_t` mass” is not proved for a surviving annihilator here; the endpoint profiles only
show compatibility before the moment/correlation failure.

The large-endpoint legality statement is existential on divisibility-compatible odd subsequences,
not for every `N`.  At `q=5`, `m=2`; no growing number of complementary pair types is legal.

## Commands and SHA-256 provenance

Environment: Python 3.12.9, SymPy 1.14.0.

Command run from the repository root:

```powershell
python artifacts\logs_ksum_L2p14_multialternant_review_20260721\independent_phase14_identity_gates.py |
  Tee-Object -FilePath artifacts\logs_ksum_L2p14_multialternant_review_20260721\independent_phase14_identity_gates.log
```

| file | SHA-256 |
|---|---|
| `pre_proposer_derivation.md` | `83f67af11a232f54391130de383843642561dd261813e1135878d0f096135881` |
| `independent_phase14_identity_gates.py` | `768b5a1a1ee384b5a5ae6afcf63d54a7cd5258f18d2ecec9aa27927caf551627` |
| `independent_phase14_identity_gates.log` | `a85758aff3da1cd731672752d557d725e8c5375258eba907f5d48d80eb587fab` |

