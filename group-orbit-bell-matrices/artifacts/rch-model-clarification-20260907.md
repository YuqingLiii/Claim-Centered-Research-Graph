# R/C/H reduction: explicit model clarification

Date: 2026-09-07. Owner: `GROTHORB.rch-reduction`.
This records a statement repair before independent review. It is not an
independent correctness verdict or a new originality claim.

## RM-1: preserved previous claim and its source convention

The preceding canonical claim was:

> Group averaging maps every feasible top-singular-space balance weight to an invariant feasible weight, and every invariant positive-semidefinite weight on a real isotypic component is represented by Hermitian positive-semidefinite multiplicity blocks over the division algebras R, C, and H.

The old `complete-extremizer-classification-20260829.md`, GOC-T1/T6,
defined a nonzero Bell matrix, paired top singular bases, and feasibility
by two constant-diagonal conditions. GOC-T6 justified averaging because
the corresponding diagonal vectors are **permuted**. The shorthand node
did not state these group-action hypotheses in its own claim. The repaired
statement makes finite row/column permutation representations and their
equivariance explicit. It does not assert preservation under arbitrary
orthogonal mixing of settings. Old artifacts and this previous statement
are retained rather than rewritten.

## RM-2: why arbitrary orthogonal setting actions cannot be substituted

The author identified the following exact diagnostic for the broader
orthogonal-action interpretation (not a refutation of GOC-T6's permutation
model). Set A=I_2, U=V=I_2, and let the nonidentity element of C_2 act
on both sides by

    R=(1/sqrt(2)) [[1,1],[1,-1]].

Then R^2=I and RA=AR, but R is not a permutation matrix. The positive
definite weight H=[[1,1/2],[1/2,1]] has unit diagonal and is feasible.
Direct multiplication gives RHR^T=diag(3/2,1/2). Hence the average
(H+RHR^T)/2 has diagonal (5/4,3/4), and is not feasible.
This exhibits the missing model boundary; it must not be hidden by saying
that general orthogonal equivariance alone permutes the diagonal.

## RM-3: new review scope

The repaired node spells out finite G, nonzero real A, permutation P_g,Q_g,
P_g A=A Q_g, the paired top-space matrices, and the balance constraints.
The invariant block statement is made relative to an orthogonal isotypic
decomposition of the induced top-space representation. Real Schur's
division-algebra theorem is registered as an external assumption, with
the adjoint, multiplicity, and PSD correspondence left to the new proof.

This is a clarification of the cited permutation setting and a necessary
restriction if the earlier shorthand was read as allowing arbitrary
orthogonal row/column actions. It is not a silent scope change to obtain a
PASS. The node remains CONJECTURED until independent review of the complete
repaired statement. No minimum-rank preservation or all-extremizer
commutant classification is asserted.
