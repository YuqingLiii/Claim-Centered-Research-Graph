# Exact finite replay, 2026-09-07

Command from repository root:

    python3 grothendieck-group-orbit/tools/check_spectral_stability.py

Dependencies: Python 3 standard library (`fractions`, `itertools`). This is a
fresh run, not a recovered historical log. Output:

```text
P3 signs: nonnegative_pairs=46, best_relative_score=8/9, dimension_gap_threshold=95/96, PASS
P3 rational planar strategies: nonnegative_pairs=2440, best_relative_score=8/9, PASS
diag(2,1) imbalanced strategies: nonnegative_pairs=128, best_relative_score=3/4, PASS
1x4 rectangular strategies: nonnegative_pairs=584, best_relative_score=1, PASS
All checks use exact Fraction arithmetic. This finite run is not a universal proof.
```

## P3 conditioning calculation

For P3=I3-J3/3 use the orthonormal basis U displayed in BR-5 of
`balance-rigidity-20260907.md`, and V=U. In the Frobenius-orthonormal
basis of Sym_2 consisting of I/sqrt(2), diag(1,-1)/sqrt(2), and
[[0,1],[1,0]]/sqrt(2), the three columns of L are mutually orthogonal.
Their squared lengths are 4/3, 2/3, 2/3. Hence s^2=2/3; with r=2,
sigma=1, tau=0 the general dimension-gap threshold is 95/96 of optimum.
The exhaustive scalar strategy check gives 8/9, consistent with a conservative
bound. The planar strategies tested are only a finite set, not all planar
strategies (which attain optimum 1 by BR-5).

## Scope

This checks exact rational examples with and without top-projector balance,
a nontrivial singular gap, rectangular dimensions, and scalar dimension loss.
The all-matrix proof is ST1-ST5 of
`spectral-stability-dimension-gap-20260907.md`, separately reviewed.
