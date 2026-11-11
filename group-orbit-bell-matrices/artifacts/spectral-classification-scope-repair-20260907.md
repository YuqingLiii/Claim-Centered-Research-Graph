# Boundary wording repairs, 2026-09-07

This addendum preserves the historical 2026-08-29 proof artifacts and makes
their scope explicit following independent findings F4 and F5/F5R in
`reviews/spectral-classification-review-20260907.md`.

## SC1: zero matrices

For nonzero transitive equivariant A the largest singular value is positive, and its paired left
and right singular spaces have the same dimension. Their normalized rows
give the strategy constructed in GO-T2 and GOC-T4. For A=0 all strategies
have zero objective, proving beta_vec(A)=sqrt(mn)||A||op without a singular
basis construction. The construction is therefore asserted only for A!=0.
For m!=n the full zero singular spaces do not admit paired orthonormal bases
of the same width, so the earlier unconditional wording was too broad.

## SC2: minima over feasible strategies

GOC-T2's equivalence is valid whether or not S(A) is empty. The dimension
minimum in GOC-T3 is asserted when S(A) is nonempty, as that section states
in its preceding sentence. The revised canonical claim carries this
qualification explicitly. No minimum over an empty set is used. In the
transitive nonzero setting H=(n/r)I is feasible, so all uses in the complete
extremizer classification remain valid.
