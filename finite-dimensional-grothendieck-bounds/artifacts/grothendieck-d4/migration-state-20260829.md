# Dimension-four migration ledger

## D4-M1: precise target

Let `A` denote the archived symmetric `300 x 300` Bell matrix whose canonical
integer serialization has SHA-256
`5fc272a61a97c0aa9f42ef86266756500401c701a6f33a3b30bde4dbe6f113e5`.
The candidate values recovered from the prior work are

```text
C = 2081044153087351400
N = 1539823299061914600 + 706968072319078800 sqrt(5)
N/C = 1.499560671050487541027064009096710890591...
```

The mathematical target is to establish both `omega_4(A) = N` (or at least
`omega_4(A) >= N`) and `omega_1(A) = C`.  Only then does the candidate give the
claimed explicit dimension-four Grothendieck lower bound.

## D4-M2: exact materials imported

Three byte-preserved bundles were imported with hashes recorded in
`source-manifest-20260829.yaml`:

1. the full invariant degree-four dual specification;
2. the canonical twenty-block `K`-compressed pencil/operator layer; and
3. the equality-rank, party-swap, matrix-free rank, and one-step PDHG frontier.

The canonical block sizes are

```text
582, 465, 611, 211, 611, 822, 235, 162, 107, 397,
504, 43, 17, 107, 166, 235, 162, 504, 384, 286.
```

The invariant moment domain has 746825 effective coordinates.  The canonical
operator data are exact over the recorded number field/finite-field recipes;
the exports explicitly state that construction of the operator does not decide
full degree-four feasibility.

## D4-M3: exact negative results

The archived exact-output records give two properly scoped negative results.

* The `alpha = 2/3` candidate has a negative `K`-block witness in irrep 13.
* Every member of the specified one-parameter affine Wick/SOS-dual family is
  covered by one of two exact negative-witness regions.

These results refute only that affine family.  They neither prove nor refute
`omega_1(A) = C` and do not decide arbitrary degree-four pseudoexpectations.
They are kept at repository level `NUMERICAL` until an independent adversarial
review checks the exact programs, inputs, and scope.

## D4-M4: equality-face and swap reductions

The preserved exact run records report:

* invariant degree-at-most-four equality restriction rank exactly 28;
* hence kernel dimension at least 28 and canonical operator rank at most
  746797;
* a lossless party-swap decomposition with even dimension 374414 and odd
  dimension 372411;
* the known equality kernel splitting as 14 even plus 14 odd directions.

The earlier rank-12-only hypothesis is therefore refuted.  The remaining exact
algebraic lemma is whether the known equality-supported kernel is the complete
kernel, equivalently whether the canonical rank is 746797.

## D4-M5: unrestricted numerical frontier

The imported one-step preconditioned PDHG record is discovery evidence only.
At its normalized initial point it reports global minimum eigenvalue
`-7117729.311658967`, negative-part Frobenius norm `7117853.580674244`, and
dual stationarity relative residual `0.9257945343812308`.  This is far from a
primal PSD certificate or a dual/SOS stationarity certificate.  The scalar
Wiedemann backend passed small block tests but a full scalar run was assessed
as computationally infeasible with the current matvec.

No convergence trend, feasibility conclusion, or classical upper bound is
inferred from these numbers.

## D4-M6: reproduction gaps

The local migration did not locate `d4_n1_300x300.mat`, its exact-system JSON,
or the full moment-map binary directory from which the preserved bundles were
built.  Instance-dependent scripts therefore remain archived but have not been
freshly rerun in this repository.  Restoring an input with merely the same
filename is insufficient: it must match the recorded MD5/SHA-256 identities.

## D4-M7: local continuation frontier

The highest-value local actions are:

1. recover and hash-verify the missing matrix and generated exact system;
2. independently replay the rank-28 and swap-even certificates;
3. give a deterministic exact rank certificate at 746797 or exhibit a further
   kernel direction;
4. run a resumable, stability-certified full twenty-block feasibility method;
5. if feasibility is found, rational/algebraic reconstruction plus independent
   review is required before using it as `omega_1(A) <= C`.

## D4-M8: 2026-08-29 direction correction

The last sentence of D4-M7 inherited a logical error.  The full
746825-coordinate system searches for a positive functional on squares in
the equality-vanishing module with `L(C-x^T A y)<0`.  If feasible, this is a
separating pseudoexpectation and therefore refutes the degree-four SOS route;
it does not prove `omega_1(A)<=C`.  The correctly oriented upper-bound route
is an exact PSD Gram/SOS representation of `C-x^T A y`, or an independent
combinatorial/exhaustive proof.  See
`d4-duality-direction-audit-20260829.md`.
