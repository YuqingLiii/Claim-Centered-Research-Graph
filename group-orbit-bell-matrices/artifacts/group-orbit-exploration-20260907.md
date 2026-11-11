# Group-orbit exploration: scope, results, and next questions

Date: 2026-09-07. This note is an explanatory view; canonical node YAMLs own
claims, assessments, dependencies, and unfinished actions.

## E1: source-verified positioning

The old spectral bound, factor tightness criterion, and minimum-factor-rank
interpretation are already covered by Epping--Kampermann--Bruss (2013),
Theorems 1--2 and Appendices A--B. Transitive symmetry supplies constant
projector diagonals, giving an immediate corollary. See the primary-source
translation in `group-orbit-literature-positioning-20260907.md`, L1--L2.
The previous draft's suggestion of a publishable-looking general theorem
therefore needs this qualification. An independently correct proof does not
establish an original result.

## E2: results pursued in this round

- `GROTHORB.balance-rigidity`: L's injectivity is exactly uniqueness of the
  feasible balance weight. Injectivity forces the full top-space dimension r;
  a nonzero kernel explicitly produces a lower-rank optimum.
- `GROTHORB.root-frame-dimension`: for every r>=3, the full D_r root frame
  gives a rational, ordinary-transitive projection matrix with n=2r(r-1)
  settings on each side, optimum n and minimum optimal vector dimension r.
- `GROTHORB.near-saturation`: a relative score deficit epsilon controls the
  mass outside the top singular space and the Alice/Bob alignment error.
- `GROTHORB.robust-dimension-gap`: with injective balance map L, least
  singular value s in Frobenius coordinates, and spectral gap
  delta=1-tau/sigma, dimension d<r forces relative score at most
  1-delta*s^2/(16r^2).

Proofs are `balance-rigidity-20260907.md`, `root-frame-dimension-20260907.md`,
and `spectral-stability-dimension-gap-20260907.md`. Exact finite replays are
linked from their canonical nodes. These are universal author arguments
with separate independent reviews, not universal conclusions inferred from
the tested small cases. Current final levels are in the generated index.

## E3: repaired defects and preserved limits

The fresh review found two wording defects in the older exact claims:
the normalized paired-basis construction needed A!=0, and the minimum-vector-
dimension statement needed a nonempty feasible set. Both are explicitly
qualified, with original adverse findings preserved and repaired statements
re-reviewed. They do not change the nonzero transitive theorem's value.

The former commutant-only classification route remains refuted and retained.
The new rigidity argument does not average weights, since averaging may
increase rank. Clifford construction still supplies a physical realization
upper bound; this round does not prove minimum quantum Hilbert dimension or
physical self-testing. The R/C/H full multiplicity formula and wreath-specific
reduction have unfinished work recorded in their own nodes.

## E4: next research priorities

1. **Classical certification for a parameterized orbit family.** For the
   root-frame projection A_r, study the shifted matrices A_r-lambda I for a
   specified rational lambda regime. Seek exact classical upper certificates
   and matching sign witnesses, then compare ratios with the existing root
   literature. No formula or hardness improvement is assumed here. This
   targets the denominator that the general spectral theorem does not solve.
2. **Quantitative dimension tradeoffs.** Compute the balance-map conditioning
   for explicit families, sharpen the conservative gap, and compare the
   setting count and robustness to prior dimension witnesses. A useful
   contribution needs an actual proved improvement or a new classification.
3. **Physical rigidity where the model permits it.** Compare the unique Gram
   cases with Slofstra's solution algebra and Zhao's XOR self-testing results,
   retaining their extremality, parity, and equivalence conventions. Do not
   infer physical uniqueness directly from vector rank.

These are concrete project questions, not assertions that the literature has
left them open. Each proposed substantive formula or route must be registered
before testing under DAG_PROTOCOL.md. This round does not restart the old
H4 search or establish an optimal Grothendieck constant.
