# Independent correctness review of the minimum isotropic-frame count

Date: 2026-09-07. Reviewer: Codex agent `/root/orbit_root_prior_art`.
Reviewed root: `/private/tmp/grothorb-classical-20260907-R0Shtu`.

Verdict: **PASS** for the exact current C12 claim in F1. The trace relation
proves the universal lower count, and the stated construction attains it
for every integer `r>=1`. No mathematical repair was needed.

## Independence, scope, and inputs

The reviewer did not author or advise on the C12 node, proof, construction,
or checker before this review. Earlier work by this reviewer concerned
literature, D3 comparisons, and C11; it did not supply the C12 argument.
This is separate author/reviewer responsibility in the same model family
and shared task context, not fresh-context or cross-model independence.
No author file, node, or earlier frozen report was modified.

The complete current node, proof MS-1--MS-6, checker source, and author run
record were read. The repository protocols were already read completely.
The current claim explicitly restricts to **nonempty finite** frames; this
review binds that version. Correctness is assessed only inside the stated
positive weighted isotropic-frame framework, with injectivity on the full
space `Sym_r`. No novelty, priority, arbitrary-Bell-setting minimum,
physical dimension, or self-testing conclusion is reviewed or implied.

Paths below are relative to `grothendieck-group-orbit/`.

| Frozen input | SHA-256 |
|---|---|
| `proof-dag/nodes/GROTHORB.minimum-settings-isotropic.yaml` | `cace3e18258f0c97f099960d598b524ea32ee2e5c92dda8c981e1944f2c6ce1c` |
| `artifacts/minimum-settings-isotropic-20260907.md` | `455e003a93386bdaa7a9a98e7d6ee4be2ebe655ae257757386e1776508735575` |
| `tools/check_minimum_settings_isotropic.py` | `4d1e89152a577eb586fb31db9a694b10355de4eaf44f69ce1a1db5f34497ca3e` |
| `artifacts/minimum-settings-isotropic-exact-check-20260907.txt` | `d02dd1cc45da3e9cd46aad71197be678d828933a98cd47af8d3e5170c0907816` |

The fresh command and complete output are frozen in
[minimum-settings-review-rerun-20260907.txt](../artifacts/minimum-settings-review-rerun-20260907.txt),
SHA-256 `9edd68f6f673932dd63e07002b69f07da7a077e2c11f5820b3a3ce3b4162a935`.
Run MS-R1 exited 0 and checked `r=1,...,10`. All four mathematical inputs
were hashed again before closeout and remained unchanged.

## F1. GROTHORB.minimum-settings-isotropic — PASS

Target: the route-free node claim.

`reviewed_hash: sha256:dc1b7a167caab8ad27dc638a70586b4bc98bd3f56fc3b4b66a2854e2e9a35aef`

Exact parsed `claim.strip()` reviewed:

> Fix an integer r>=1. Among pairs of nonempty finite positive weighted isotropic unit frames in R^r for which the map H -> ((a_i^T H a_i)_i,(b_j^T H b_j)_j) is injective on Sym_r, the minimum total number of frame vectors m+n is r(r+1)/2+1. It is attained with Alice vectors e_1,...,e_r of weight 1, Bob vectors (e_i-e_j)/sqrt(2) for i<j of weight 2/r, and (1,...,1)/sqrt(r) of weight 1.

**Universal lower bound.** The frame domain supplies positive finite
totals `S,T`, so normalizing weights by S and T is legitimate. Isotropy
and the identity `tr(aa^T H)=a^T H a` give normalized weighted output
sums `tr(H)/r` separately on each side. Subtracting yields the linear
relation with coefficients `(u/S,-v/T)` in MS.3. It is nonzero because
the sides are nonempty and the weights positive; in particular, the
Alice-block coefficients sum to 1. Outputs are unweighted evaluations,
so these coefficients are inserted in the relation rather than silently
absorbed into the definition of the measurement map.

The image of the linear map on `Sym_r` therefore has dimension at most
`m+n-1`. Injectivity on that entire space requires rank
`d=dim(Sym_r)=r(r+1)/2`, giving `m+n>=d+1`. This argument applies to
every admissible pair of frames, not just the proposed construction.
It neither restricts H to trace zero nor assumes the isotropy relation
is the only dependence; one nonzero dependence suffices for the bound.

**Construction for every positive r.** Alice's basis vectors are unit,
have positive weight 1, total `S=r`, and moment `I_r`. Bob's difference
vectors are unit because `||e_i-e_j||^2=2`; their weights `2/r` are
positive. The all-ones vector divided by `sqrt(r)` is also unit and has
positive weight 1. Bob's total is `(2/r)*r(r-1)/2+1=r`, so no empty
Bob side occurs even when the difference-vector list is empty.

Entrywise, `sum_{i<j}(e_i-e_j)(e_i-e_j)^T` has diagonal entries `r-1`
and off-diagonal entries `-1`, hence equals `rI-J`. The squared norm
normalization contributes `1/2`, canceling the 2 in Bob's weights. Its
weighted difference contribution is therefore `I-J/r`; the all-ones
vector contributes exactly `J/r`. The total moment is `I=(T/r)I`.
This checks both the signs and the square-root normalizations in MS.6.
Counts are `m=r` and `n=r(r-1)/2+1`, totaling `d+1`.

**Injectivity.** Alice's evaluations determine every `H_ii`. Once these
are zero in a kernel element, a Bob difference evaluation is
`(H_ii+H_jj-2H_ij)/2=-H_ij`, so every off-diagonal entry must vanish.
As a separate general rank check, order the independent coordinates of H
as its r diagonal entries followed by its `k=binom(r,2)` upper off-diagonal
entries. The d rows corresponding to Alice and Bob's difference vectors
form the block matrix

```text
[ I_r   0  ]
[  E   -I_k],
```

where each row of E has 1/2 in its two endpoint columns. Its determinant
is `(-1)^k`, including the empty `k=0` case. Thus those d rows alone
already have full rank for every r. Bob's additional all-ones row is
needed to complete isotropy, not for this rank argument. The universal
lower bound and the admissible construction together establish a minimum,
not merely a sufficient count.

**Smallest cases.** At `r=1`, the pair list is empty, `rI-J=0`, and
each side consists of one copy of `e_1` with weight 1. The map is
`h -> (h,h)`, has rank one, and uses two vectors as the formula requires.
At `r=2`, Bob's two vectors are the normalized difference and sum of the
two basis vectors, both with weight 1; the total count is four and the
rank is three. Neither case needs an exception or an altered domain.

**Implementation and replay.** The checker forms exact rational outer
products for the displayed vectors. Trace one, symmetry, and idempotence
correctly verify unit rank-one projectors. Positive weights and all
entries of the weighted moments are checked separately. Its measurement
matrix assigns coefficient `2P_ij` to the independent variable `H_ij`,
which is required when evaluating `tr(PH)` for symmetric H. The code
checks the nonzero trace-relation vector and all of its coordinate sums,
then uses rational forward elimination to verify rank d. Pivot selection,
row swaps, normalization, and trailing row elimination are consistent;
all entries are `Fraction` values, so division does not introduce floats.

The fresh replay with Python optimization flag 0 reproduced the author
record for every `r=1,...,10`, with total counts
`2,4,7,11,16,22,29,37,46,56` and ranks
`1,3,6,10,15,21,28,36,45,55`. Assertions were enabled. These finite
checks validate the implementation and examples; the universal conclusion
rests on the all-r trace, moment, and injectivity arguments above.

No missing load-bearing project premise, rank defect, boundary failure,
or normalization error was found. The node is route-free, so there is no
additional route implication to assess in this report.

## Closeout

The statement hash is SHA-256 of UTF-8 after `yaml.safe_load` followed by
`claim.strip()`; the file digests are separate. PyYAML 6.0.3 was used only
to extract the statement, while the mathematical run used the standard
library. F1 concerns the exact nonempty-frame version quoted above.

This is a same-model, shared-context, non-formal review. Mathematical
correctness does not settle originality, and the separate literature
work is not part of this verdict. The report and reviewer rerun record
are frozen on completion. Earlier frozen reports remain unchanged;
node promotion and integration are left to the coordinator. No further
research scope is opened by this review.
