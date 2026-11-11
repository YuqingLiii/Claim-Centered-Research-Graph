# Independent correctness review of the repaired invariant R/C/H reduction

Date: 2026-09-07. Reviewer: Codex agent `/root/orbit_root_prior_art`.
Reviewed root: `/private/tmp/grothorb-classical-20260907-R0Shtu`.

Verdict: **PASS** for the exact repaired `GROTHORB.rch-reduction` claim
in F1, with its registered real-Schur external input. The finite
permutation model preserves both balance families, and the proof supplies
the adjoint-compatible Hermitian PSD block correspondence in both
directions. No mathematical repair is required for this statement.

## Independence, scope, and frozen inputs

The reviewer did not write this RCH proof or the node repair. This agent
previously performed literature work and independent reviews of other
claims in this task. This is author/reviewer role separation within a
shared context and the same model family, **not fresh-context or
cross-model independence**. Familiarity with earlier scope diagnostics is
disclosed, not treated as a source of additional independent evidence.

The complete current YAML claim, assumptions, and events were read,
together with the complete author proof RCH-0--RCH-9, the complete model
clarification RM-1--RM-3, L5 of the source note, and the earlier GOC
classification record. The repository protocols had already been read
completely. The primary real-Schur source was checked directly, including
its definition, theorem, full theorem proof, and corollary at the locators
below. This is a correctness review, not a novelty assessment or an
all-extremizer classification.

| Frozen local input | SHA-256 |
|---|---|
| `grothendieck-group-orbit/proof-dag/nodes/GROTHORB.rch-reduction.yaml` | `4fab3af0bdee3c7d267d0286b9214dc0bd12b861f06fea8b6dbb31177b439130` |
| `grothendieck-group-orbit/artifacts/rch-invariant-blocks-20260907.md` | `04c7f06deb15b366e104984e5164bb26398697b3f9edf5ebd2488436e79673e9` |
| `grothendieck-group-orbit/artifacts/rch-model-clarification-20260907.md` | `7a53235e296c1918e06b21bf0b8e9e83f201686d3bb652fcc80d66f790d4be37` |
| `grothendieck-group-orbit/artifacts/group-orbit-literature-positioning-20260907.md` | `310ed176e035bba8c0b57d90680656a6a50b3b3e1ab8b83d1448468ae2a93473` |
| `grothendieck-group-orbit/artifacts/complete-extremizer-classification-20260829.md` | `44ac28ada792471f5ff014f763a94da16929ac2f6d99df01b2a056f52a47cd99` |

The author proof digest matches the supplied frozen digest. These five
digests and the exact parsed statement digest were recomputed at closeout
and remained unchanged. Only this new review was written; no author
artifact, node, or earlier frozen report was modified. The proof is
analytic, with no numerical sampling or finite-example inference used
as a substitute for any general step.

## F1. GROTHORB.rch-reduction — PASS

Target: the current route-free node claim, after the explicit permutation
model repair. No separate route implication is registered.

`reviewed_hash: sha256:152252d578bb0e893995f4a940a9ebe99124b3dc8cc6f5325076c6ebd41ed2f4`

Exact parsed `claim.strip()` reviewed:

> Let a finite group G act by permutation matrices P_g on R^m and Q_g on R^n, and let A be a nonzero real m by n matrix with P_g A=A Q_g. Let sigma=||A||_op, and let U,V have orthonormal columns spanning its paired top singular spaces, with AV=sigma U and A^T U=sigma V. Then R_g=V^T Q_g V is an orthogonal representation with P_g U=U R_g. Every H>=0 satisfying diag(VHV^T)=1_n and diag(UHU^T)=(n/m)1_m has an invariant feasible average |G|^(-1) sum_g R_g H R_g^T. Relative to an orthogonal real isotypic decomposition of this representation into W_alpha^{oplus t_alpha}, every invariant PSD weight, and only such a weight, is represented by Hermitian PSD multiplicity matrices B_alpha in M_{t_alpha}(D_alpha), where D_alpha=End_G(W_alpha) is R, C, or H, with compatible real adjoint corresponding to conjugate transpose on each multiplicity matrix. The two original balance equations remain additional constraints on these invariant PSD blocks.

### Registered external assumption and its application

The node registers `real-schur-division-algebras` as an external theorem,
with L5 and Rosenberg Theorem 1.3/Corollary 1.4, page 2, as its source.
Theorem 1.3 supplies the R/C/H division-algebra alternatives for the
commutant of an irreducible real C*-representation; the corollary labels
the three types. Definition 1.1, page 1, gives the concrete operator
algebra definition used here. These locators, including the theorem's
proof, were checked in the primary version:
[Rosenberg, *Structure and applications of real C*-algebras*, arXiv:1505.04091v1](https://arxiv.org/pdf/1505.04091v1).

In the actual application there is no unverified extension to an
arbitrary non-star algebra representation. On an irreducible orthogonal
G-module W, the real span of the group operators contains the identity,
is closed under products and adjoints, and is finite-dimensional, hence
norm-closed. With its inherited operator norm and the inclusion
*-representation it meets the cited concrete definition. Its invariant
subspaces and commutant are exactly those for G. The registered theorem
therefore applies to `End_G(W)`.

Only this division-algebra classification is imported. The author does
not attribute the full multiplicity, compatible-adjoint, or PSD formula
to the literal theorem statement. Those additional steps are checked
below. No Gatermann--Parrilo optimization theorem is needed as a hidden
premise for the elementary finite average.

### Common top-space action and preservation of every balance equation

Since A is nonzero, `sigma>0`. Applying the transpose equivariance
identity to the inverse group element gives `A^T P_g=Q_g A^T`.
Together with `A Q_g=P_g A`, this makes Q_g commute with `A^T A`.
Consequently Q_g preserves its entire top eigenspace. The use of the
full top singular space, rather than an arbitrary selection of vectors
inside a degenerate singular space, is essential and is explicit.

For the orthonormal basis V, invariance gives `Q_g V=V R_g`, where
`R_g=V^T Q_g V`. This restriction is orthogonal and obeys the group law.
The pairing and nonzero sigma give
`P_g U=P_g A V/sigma=A Q_g V/sigma=U R_g`. Thus there really is one
common representation on both paired top spaces; unrelated left/right
coordinate choices have not been assumed to agree.

Conjugating H by R_g preserves symmetry and PSD. The two lifted
matrices are respectively conjugated by P_g and Q_g. These are
permutations, so their diagonal entries are permuted. This preserves
every entry of both required constant vectors, including the distinct
normalizations `1_n` and `(n/m)1_m`. It does not merely preserve their
traces. Convexity and affinity give feasibility of the average, and
left multiplication permutes its finite group summands, proving
invariance. For orthogonal R_g, invariance by conjugation is equivalent
to commutation. An already invariant H is fixed by the average.
No transitivity, nonempty feasibility assumption, or rank argument is
required for this conditional assertion.

### Orthogonal multiplicities and the real adjoint

Orthogonal complements of invariant subspaces remain invariant, so
successive irreducible decomposition can be made orthogonally. A
self-adjoint commuting operator on an irreducible W is scalar: it has
a real eigenvalue and a nonzero invariant eigenspace, which must be all
of W. A nonzero intertwiner between irreducibles is an isomorphism;
for equivalent orthogonal copies, `L^*L=aI` with `a>0`, so normalizing
by `sqrt(a)` gives an isometric identification. These facts justify
orthogonal isotypic coordinates and the adjoint calculation, not just
an abstract nonorthogonal similarity.

Starting with a real-algebra isomorphism phi from D to `End_G(W)`,
closure under real adjoints is proved from the inverse group elements.
For the image J of each standard imaginary generator, `J^2=-I`, and
both `J+J^*` and `J^*J` are self-adjoint commutant elements. Writing
them as `aI` and `bI` yields `aJ=(b-1)I`. Since J cannot be a real
scalar, `a=0,b=1`; thus `J^*=-J`. Applying this to i, and also j,k
for H, gives `phi(q)^*=phi(conj(q))` by real linearity. Therefore the
algebra identification is star-compatible with the actual real inner
product, rather than being assumed star-compatible without proof.

Off-type components of a commutant operator vanish by the intertwiner
argument. On k isometrically identified copies of W, every component
has a unique coefficient in D. Hence all, and only, commuting operators
are `Psi(B)` with `(Psi(B)w)_a=sum_b phi(B_ab)w_b`. Composition keeps
the displayed coefficient order. The adjoint's (a,b) block is
`phi(conj(B_ba))`, proving `Psi(B)^*=Psi(B^*)`. Faithfulness gives
real self-adjointness if and only if B is Hermitian, including in the
noncommutative quaternionic case. Once the orthogonal identifications
and phi are fixed, the parametrization is unique; a canonical choice
of those coordinates is not claimed or needed.

### Realification, PSD in both directions, and quaternionic order

For a unit vector w, the map `q -> phi(q)w` is a real isometry: the
inner product is `Re(conj(p)q)` because imaginary elements act
skew-adjointly. Its image and orthogonal complement are D-invariant.
Iterating yields an orthonormal real model `W = D^ell`, with
`ell=dim_R(W)/dim_R(D)`, where phi(q) acts by left multiplication
on each coordinate. This auxiliary decomposition is not asserted to
be G-invariant; that distinction causes no problem for expressing
the commuting operators.

Use real matrices for left multiplication by each B_ab. Their block
matrix satisfies `Real_D(B)^T=Real_D(B^*)`. For a Hermitian B, the
scalar `z^*Bz` is real even over H: conjugating it reverses products
and exchanges the two matrix indices, giving the same scalar.
Its real quadratic form is exactly `Re(z^*Bz)`. Thus Hermitian PSD
over D, in the stated quadratic-form convention, is equivalent to
PSD of this real symmetric matrix. No quaternionic spectral theorem
is silently required.

Regrouping the orthonormal coordinates of the k copies of `D^ell`
makes Psi(B) an orthogonal direct sum of ell identical realifications.
Since `ell>=1`, PSD of Psi(B) implies PSD of each realification by
testing one summand, and the reverse follows by summing their
nonnegative quadratic forms. The zero matrix and singular PSD boundary
are included. This establishes the claimed equivalence in both
directions, not merely a sufficient block construction.

The quaternionic conventions are consistent throughout: phi is a
homomorphism whose coefficients act on the **left**; ordinary matrix
composition has order `B_ab C_bc`; conjugate transpose reverses the
order where required; and the auxiliary column map `z -> Bz` is
**right**-D-linear because `B(zq)=(Bz)q`. The latter statement does
not identify the G-action with scalar right multiplication or claim
that Psi(B) is left-D-linear. There is no unannounced switch to an
opposite algebra.

RCH-7's auxiliary real-rank conversion is consistent with these
coordinates: a right-D image of dimension s has real dimension
`dim_R(D)*s`, and ell repeated realifications supply the factor
`dim_R(W)`. This was checked only as an ancillary consistency step.
The rank formula is not in the reviewed node claim and is not promoted
by this report into a separately registered theorem or an optimization
over all feasible weights.

### Remaining constraints and preserved diagnostic boundaries

After the orthogonal change O, the full invariant PSD cone is given
by `H=O K(B) O^T`. Feasibility still requires both displayed affine
families in RCH.14 with `U_tilde=UO` and `V_tilde=VO`. Block PSD alone
does not impose these equations, and neither does a total trace
condition. Conversely, imposing them on the invariant PSD blocks
produces precisely an invariant feasible H. The proof therefore
gives the claimed invariant feasible-set reduction, and no larger
classification.

The old shorthand claim, preserved in RM-1, did not list the setting
actions explicitly. GOC-T6 used permutation of the diagonal vectors.
The present statement makes that model explicit; relative to an
arbitrary-orthogonal-action reading, this is a necessary restriction,
not a retrospective PASS for the broader wording. The diagnostic
in RM-2/RCH-2 is exact: for the two-element Hadamard reflection action,
`A=I_2` and `H=[[1,1/2],[1/2,1]]`, one has
`RHR^T=diag(3/2,1/2)`, so the averaged diagonal is `(5/4,3/4)`.
H is positive definite and initially has unit diagonal, but that
average fails balance. This refutes the broader orthogonal-action
substitution, not the repaired permutation claim. The nonzero A
hypothesis also keeps division by sigma and the common pairing valid.

The earlier GOC-T5 noninvariant feasible weight for `A=I_3` and
simultaneous S3 permutations remains a separate counterexample to
placing every individual extremizer in the commutant. Neither that
diagnostic nor the new orthogonal-action diagnostic is erased by F1.
Average feasibility proves existence of an invariant feasible point
whenever a feasible point exists; it does not equate individual
solutions, preserve rank, or equate unrestricted and invariant-only
minimum ranks. The repaired claim and RCH-8 retain these boundaries.

## Closeout

No missing common-action hypothesis, dropped balance family, unjustified
star identification, multiplicity error, one-way PSD implication, or
quaternionic order reversal was found in the repaired claim's proof.
The `reviewed_hash` is SHA-256 of the UTF-8 encoding of
`yaml.safe_load(node_text)['claim'].strip()`, distinct from all file
digests. F1 binds exactly the quoted statement, the registered external
input as applied above, and the frozen proof listed here.

This is a non-formalized, same-model correctness review, not a novelty
assessment, proof-assistant certificate, all-extremizer result, or
rank-preservation theorem. The old diagnostic limitations remain
part of the audit history. This report is frozen on completion;
canonical integration is left to the coordinator, and no further
research scope is opened.
