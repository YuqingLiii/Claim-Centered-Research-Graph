# Exact D3 classical envelope dossier, 2026-09-07

Canonical formula owner: `GROTHORB.d3-shift-envelope`, route `exact-envelope`.
Canonical method owner: `GROTHORB.d3-envelope-method`. The registered proposed
all-r linear extension is `GROTHORB.shift-linear-candidate`. This dossier
records author computation and an assembled exact argument; independent
adversarial review is required before any completion-level assessment.
The resulting formula was sent for separate canonical registration immediately
after the exploratory run and before relying on it as a theorem.

## D3-1: exact input and row convention

Let W have these rows, in this order:

```
(-1,-1, 0), (-1, 1, 0), ( 1,-1, 0), ( 1, 1, 0),
(-1, 0,-1), (-1, 0, 1), ( 1, 0,-1), ( 1, 0, 1),
( 0,-1,-1), ( 0,-1, 1), ( 0, 1,-1), ( 0, 1, 1).
```

These are all D3 roots, including both members of every antipodal pair.
Set A=WW^T/8, B(lambda)=A-lambda I_12, and
beta_cl(B)=max_{s,t in {+1,-1}^12} s^T B t. All intervals below are closed
and confined to 0<=lambda<=1/2. The checker reconstructs A entry by entry
using Fraction(dot(root_i,root_j),8) and verifies W^T W=8 I_3.

## D3-2: exhaustive reduction and continuum coverage

For every fixed t, independent coordinate choices of s give

```
max_s s^T B(lambda)t = f_t(lambda)
                       = sum_i |(At)_i - lambda*t_i|.
```

If a coordinate is zero, either sign is maximizing. Thus enumerating all
2^12=4096 Bob sign vectors suffices; no symmetry quotient is used.

For a fixed t and row i, the sole possible absolute-value kink is
lambda=(At)_i/t_i. The checker collects every such rational in [0,1/2]
across every enumerated t, together with both domain endpoints. The resulting
partition is {0,1/4,1/2}. On each open base interval, every f_t is affine:
b_t+m_t lambda, with s_i selected from the sign at its rational midpoint,
b_t=s^T At, and m_t=-s^T t. The same affine representation extends to both
endpoints by continuity. The implementation keeps every line, deduplicating
only equal coefficient pairs and preserving their exact multiplicities.

The first base interval has 18 distinct lines with total multiplicity 4096;
the second has 17, also with total multiplicity 4096. The full coefficient
and multiplicity lists are frozen in
`d3-classical-envelope-certificate-20260907.json` at `base_intervals[].lines`.

Within each base interval, the checker includes every intersection
(b_2-b_1)/(m_1-m_2) of two lines with distinct slopes, when the intersection
lies strictly inside the interval. It includes intersections of nonmaximal
lines as well. The first interval's interior crossing set is

```
1/10, 1/8, 1/6, 3/16, 1/5, 3/14.
```

The second interval's interior crossing set is

```
5/16, 1/3, 7/20, 5/14, 3/8, 7/18, 11/28, 2/5,
5/12, 3/7, 7/16, 9/20, 5/11, 11/24, 13/28.
```

Together these create 23 elementary closed cells. No ordering of distinct
affine functions can change inside such a cell. The checker selects a
maximizing line at the exact midpoint and then verifies that this line
dominates **every** distinct line at **both** cell endpoints. The latter
check alone implies dominance on the whole cell, since each difference is
affine. It also directly checks the retained (s,t) witness at both endpoints.
Hence neither narrow interior changes nor endpoint ties are omitted.
Adjacent cells are merged only if their affine coefficients and both sign
witnesses agree. Finally the checker directly reevaluates every original
absolute-value function at each merged boundary. This establishes full
coverage of the real parameter interval, rather than rational-grid sampling.

## D3-3: computed envelope and matching witnesses

The exhaustive computation returns

```
beta_cl(A-lambda I) = 10-12 lambda,  0 <= lambda <= 1/4;
                    =  8- 4 lambda,  1/4 <= lambda <= 1/2.
```

Both pieces give 7 at their common boundary. Equivalently the envelope on
the stated domain is max(10-12 lambda, 8-4 lambda).

For the first piece take

```
s=t=(-1,-1,1,1, -1,-1,1,1, -1,-1,1,1).
```

Then W^T t=(8,4,0), s^T At=10 and s^T t=12, giving the first line.
For the second piece take

```
s=( 1, 1, 1, 1, -1,1,-1,1, -1,1,-1,1),
t=(-1,-1,-1,-1, -1,1,-1,1, -1,1,-1,1).
```

Here W^T t=(0,0,8) and

```
At=(0,0,0,0, -1,1,-1,1, -1,1,-1,1).
```

Consequently s^T At=8 and s^T t=4, giving the second line. These two
fixed sign pairs actually give their respective affine bilinear values
throughout [0,1/2]; the global maximizer changes at lambda=1/4.

The finite computation supplies the upper bound by D3-2; the explicit sign
pairs supply matching lower bounds. No unproved all-r classical formula or
vector-optimum theorem is used in this argument.

## D3-4: scoped refutation of the full-interval linear proposal

For r=3, the registered proposed expression is 10-12 lambda. At lambda=1/2,
the second sign pair in D3-3 gives

```
s^T(A-(1/2)I)t = 8-(1/2)*4 = 6 > 4 = 10-12*(1/2).
```

This exact witness refutes the universal equality in
`GROTHORB.shift-linear-candidate`, already for r=3. The contrary witness does
not require believing the computed upper envelope. It does not refute the
base value at lambda=0, the D3 equality on [0,1/4], or any untested replacement
formula for larger r. Failed full-interval extrapolation must remain recorded.

## D3-5: frozen certificate and reproducibility

All arithmetic uses Python's standard-library fractions.Fraction. The checker
uses only argparse, fractions, itertools, json, and pathlib. It makes no
network calls and needs no solver, numerical library, tolerance, or random
seed. It enumerates all signs directly and constructs both row kinks and
pairwise affine crossings before selecting an envelope.

From the repository root:

```sh
python3 grothendieck-group-orbit/tools/check_d3_classical_envelope.py --check grothendieck-group-orbit/artifacts/d3-classical-envelope-certificate-20260907.json
```

Omit `--check` to print the independently reconstructed deterministic JSON.
The frozen certificate includes the complete root order, domain, enumeration
count, all row breakpoints, full affine-line inventory and multiplicities,
all pairwise crossings, envelope pieces with witnesses, exact endpoint
values, and the scoped counterexample. The `--check` mode requires full
object equality with the reconstructed certificate and raises an error on
any mismatch. Use ordinary Python execution, without optimization flags
that disable assertions.

The exact run is evidence for these scoped finite statements. Protocol
promotion depends separately on an independent reviewer checking the argument,
implementation, run, and exact registered statements. This is not a proof
assistant formalization and makes no novelty claim.
