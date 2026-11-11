# Invariant top-space balance weights and real R/C/H blocks

Date: 2026-09-07. Author argument for independent review.
Canonical owner: `GROTHORB.rch-reduction`.
Starting records: `complete-extremizer-classification-20260829.md`,
GOC-T1 and GOC-T6; `balanced-rank-theorem-draft-20260829.md`, GO-T6;
`group-orbit-literature-positioning-20260907.md`, L5.

## RCH-0: exact model boundary and statement to review

This proof is bound to the repaired canonical node statement, re-read after
the `explicit-permutation-model-20260907` event. The earlier shorthand
omitted the group action, matrix equivariance, and nonzero-matrix convention.
That previous wording and the scope diagnostic are preserved in
`rch-model-clarification-20260907.md`, RM-1 through RM-3. The repaired node
now explicitly registers the following model already used in the GOC setup:

1. A is a nonzero real m by n matrix, with m,n>=1;
2. a finite group G acts by row and column permutation representations
   P_g in O(m), Q_g in O(n), with P_g A Q_g^T=A for every g; and
3. U,V are paired orthonormal bases of the top left/right singular spaces,
   with the balance constraints in RCH-1 below.

Transitivity is not needed for this conditional averaging result. The
abstract commutant result in RCH-3 through RCH-7 applies to any finite
dimensional real orthogonal representation, independently of A.

The repair is a clarification of the documented GOC model, and a necessary
restriction of any broader reading that allowed arbitrary orthogonal
row/column actions. That broader reading is false, as the exact diagnostic
in RCH-2 shows. The current claim and its external assumption record have
been checked against these inputs. This artifact neither silently narrows
the repaired claim nor marks the intended permutation model refuted.

The theorem proved here is: under inputs 1--3, every feasible weight has
an invariant feasible group average. In orthogonal isotypic coordinates,
every invariant symmetric PSD weight is represented by one Hermitian PSD
multiplicity matrix over R, C, or H per real irreducible type. The original
balance equations remain as affine constraints on those blocks. This
classifies the invariant feasible subset, not all individual extremizers.

## RCH-1: the common induced top-space representation

Let sigma=||A||_op>0 and let its singular multiplicity be t. Choose
U in R^(m by t), V in R^(n by t) satisfying

    U^T U=V^T V=I_t,
    AV=sigma U,    A^T U=sigma V.

The balance set, with the existing GOC normalization, is

    S(A)={H in Sym_t:
           H>=0,
           diag(VHV^T)=1_n,
           diag(UHU^T)=(n/m)1_m}.                 (RCH.1)

Equivariance gives AQ_g=P_g A and A^T P_g=Q_g A^T. Hence Q_g
commutes with A^T A and preserves its sigma^2 eigenspace. Define

    R_g=V^T Q_g V.

Invariance of that space gives Q_g V=V R_g. Since Q_g and V are
isometries on their domains, R_g is orthogonal. Also

    P_g U=P_g AV/sigma=AQ_g V/sigma=U R_g.

The same R_g therefore acts on both paired top spaces. From Q_(gh)V
=Q_g Q_h V one obtains R_(gh)=R_g R_h, so this is an orthogonal
representation of G on R^t. This argument uses the full top eigenspace
and does not choose a preferred vector inside a degenerate singular block.

For H in S(A), put H_g=R_g H R_g^T. It is symmetric PSD, and

    U H_g U^T=P_g(UHU^T)P_g^T,
    V H_g V^T=Q_g(VHV^T)Q_g^T.                    (RCH.2)

Conjugating by a permutation matrix permutes diagonal entries. Both
prescribed diagonal vectors in (RCH.1) are constant, so each constraint
is preserved, with its own normalization n/m or 1. Thus H_g is feasible.
In particular,

    H_bar=(1/|G|) sum_(g in G) R_g H R_g^T         (RCH.3)

is PSD and satisfies both full families of affine balance constraints.
For h in G, conjugation by R_h permutes the summands by g -> hg; hence
R_h H_bar R_h^T=H_bar. Since R_h is orthogonal, this is equivalent to
H_bar commuting with every R_h. Averaging an already invariant weight
leaves it fixed. No transitivity or general SDP duality result was used.

## RCH-2: why arbitrary orthogonal row actions are insufficient

This diagnoses a possible overbroad reading of the node, not its inherited
permutation model. Let A=I_2, U=V=I_2, and let G have two elements with
the nonidentity row and column action

    P=Q=R=(1/sqrt(2)) [1  1; 1 -1].

The matrix R is orthogonal, R^2=I_2, and P A Q^T=A. The weight

    H=[1 1/2; 1/2 1]

is positive definite, with eigenvalues 3/2 and 1/2, and has the required
unit diagonal on both sides. Direct multiplication gives

    RHR^T=diag(3/2,1/2),
    diag((H+RHR^T)/2)=(5/4,3/4).

Even the group average therefore fails the balance constraints. General
orthogonality of row and column actions cannot replace permutation
invariance of the coordinate balance equations without another explicit
constraint-invariance hypothesis. Nonzero A is also an explicit convention
of the paired setup: the proof does not divide by sigma when A=0 or claim
to select a canonical common paired top representation in that case.

## RCH-3: external input and elementary representation preliminaries

The only non-elementary external theorem imported is the following real
Schur statement.

**RS (exact imported statement).** If a real C*-algebra is represented
irreducibly by bounded real operators on a real Hilbert space as a
*-representation, its commutant is isomorphic, as a real division algebra,
to R, C, or the quaternions H.

Source: Jonathan Rosenberg, *Structure and applications of real C*-algebras*,
[arXiv:1505.04091v1](https://arxiv.org/pdf/1505.04091), Theorem 1.3,
PDF page 2; Corollary 1.4 names the three representation types. The theorem
and proof were rechecked for this artifact. Only the division-algebra
classification is imported. The compatible adjoint, multiplicity formula,
PSD correspondence, and real-rank conversion are proved below, rather than
attributed to the literal statement of that theorem.

Here is the precise applicability check. For an irreducible real orthogonal
G-module W, the real linear span of its representation matrices is a
finite-dimensional norm-closed unital *-algebra: multiplication follows from
the group law, and adjoints from rho(g)^*=rho(g^(-1)). With the inherited
operator norm it is a real C*-algebra, in the concrete sense of Rosenberg's
Definition 1.1. A subspace invariant under this algebra is exactly a
G-invariant subspace. Its commutant is End_G(W), so RS applies.

The additional finite-dimensional facts needed here have short direct
proofs:

- An orthogonal representation is an orthogonal direct sum of irreducibles.
  The orthogonal complement of any invariant subspace is invariant, since
  the group operators and their inverses are orthogonal. Successively take
  a nonzero invariant subspace of least positive dimension and its
  complement; dimension decreases until the decomposition is complete.
- A self-adjoint element T of End_G(W), with W irreducible, is a real
  scalar. A real self-adjoint finite-dimensional operator has an eigenvector
  (for example, maximize its Rayleigh quotient on the unit sphere). Its
  corresponding eigenspace is nonzero and G-invariant, hence all of W.
- An intertwiner between inequivalent irreducibles is zero: a nonzero
  intertwiner has invariant kernel and image, so irreducibility would make
  it an isomorphism. If L is an invertible intertwiner between equivalent
  orthogonal irreducibles, L^*L is positive, self-adjoint, and commutes with
  G. Thus L^*L=aI with a>0, and L/sqrt(a) is an isometric intertwiner.

These arguments supply orthogonal isotypic coordinates and isometric
identifications of equivalent copies. No separate complete-reducibility,
polar-decomposition, or quaternionic spectral theorem is imported.

## RCH-4: a star-compatible division-algebra action in real coordinates

Fix an irreducible real orthogonal module W, write d=dim_R(W), and choose
a unital real-algebra isomorphism

    phi:D -> End_G(W),    D in {R,C,H},

provided by RS. For D=R its adjoint is already ordinary real conjugation.
Adjoints stay in the commutant: transpose a commutation relation and use
rho(g)^*=rho(g^(-1)), with g^(-1) again ranging over G.
For each standard imaginary generator of C or H, its image J satisfies
J^2=-I. Both J+J^* and J^*J are self-adjoint commutant elements, so the
preceding scalar fact gives

    J+J^*=aI,    J^*J=bI.

Using J^*=aI-J and J^2=-I gives aJ=(b-1)I. J is not a real scalar
operator, because a real scalar cannot square to -I. Hence a=0 and b=1,
so J^*=-J. Apply this to i in C, and to i,j,k in H. Real linearity yields

    phi(q)^*=phi(conj(q))  for every q in D,
    phi(q)^*phi(q)=|q|^2 I.                       (RCH.4)

Thus the chosen algebra identification is compatible with the original
real inner product. In particular imaginary elements are skew-adjoint,
and phi(q) is orthogonal whenever |q|=1.

There is also an explicit orthonormal real coordinate model. Let
delta=dim_R(D), equal to 1,2,4. For any unit w in W, the map

    q -> phi(q)w

is a real isometry from D, with inner product Re(conj(p)q), to W. Indeed,

    <phi(p)w,phi(q)w>
       =<w,phi(conj(p)q)w>=Re(conj(p)q),

because the imaginary part acts skew-adjointly. The image phi(D)w is a
D-invariant subspace of real dimension delta. Its orthogonal complement
is also D-invariant by (RCH.4). Repeat there to obtain an orthogonal
decomposition into such subspaces. It follows that delta divides d and,
with ell=d/delta,

    W is isometric to D^ell as a real inner-product space,
    phi(q)(z_1,...,z_ell)=(qz_1,...,qz_ell).       (RCH.5)

The real coordinates are those of 1,i in the complex case and 1,i,j,k in
the quaternionic case, on each cyclic subspace. This auxiliary
D-module decomposition need not be G-invariant; its purpose is to give
an orthonormal real model of the commuting algebra action.

## RCH-5: exact isotypic multiplicity blocks and the adjoint

Decompose the real top-space representation orthogonally as

    R^t = orthogonal-sum_(alpha) W_alpha^(k_alpha),

where the W_alpha are pairwise inequivalent real irreducibles, and the
copies of each type are identified isometrically as in RCH-3. Write

    d_alpha=dim_R(W_alpha),
    D_alpha=End_G(W_alpha) identified with R,C,or H.

Any commuting operator is zero between different isotypic types: its
irreducible-to-irreducible components would otherwise be nonzero
intertwiners between inequivalent modules. On one isotypic component
W^k, every commuting operator has a unique block description

    Psi(B)(w_1,...,w_k)_a=sum_(b=1)^k phi(B_ab)w_b,
    B=(B_ab) in M_k(D).                           (RCH.6)

Conversely every such operator commutes with G. Composition uses the
ordinary ordered matrix product over D, because phi is an algebra
homomorphism and the entries act on the left. This fixes the convention
explicitly, avoiding an unstated opposite-algebra choice in the
quaternionic case.

In the orthonormal real direct-sum coordinates, the adjoint has (a,b)
block phi(B_ba)^*=phi(conj(B_ba)). Therefore

    Psi(B)^*=Psi(B^*),    (B^*)_ab=conj(B_ba).      (RCH.7)

Faithfulness of phi implies that Psi(B) is real self-adjoint exactly when
B=B^*: real symmetric for D=R, complex Hermitian for D=C, and quaternionic
Hermitian for D=H. No nonorthogonal similarity is used for this assertion.

## RCH-6: PSD correspondence without a quaternionic spectral theorem

For a Hermitian B in M_k(D), use the following PSD convention:

    B>=0 over D iff z^* B z>=0 for every z in D^k. (RCH.8)

Hermiticity makes z^*Bz real, including when D=H. Let L_D(q) be the
delta by delta real matrix of left multiplication by q on D in its
orthonormal real basis. Define the realification

    Real_D(B)=(L_D(B_ab))_(a,b),

a real delta*k by delta*k matrix. Equation (RCH.7), or the standard real
inner product Re(z^*w), gives

    Real_D(B)^T=Real_D(B^*),
    <z,Real_D(B)z>_R=Re(z^*Bz).                   (RCH.9)

Consequently Hermitian B is PSD over D exactly when Real_D(B) is PSD
as a real symmetric matrix.

Now apply the explicit coordinate model (RCH.5) in each copy of W. The
operator Psi(B) acts by left multiplication with B on each of the ell
coordinate collections in D^k. Regrouping real orthonormal coordinates
therefore gives

    Psi(B) orthogonally equivalent to
       Real_D(B) direct-sum ... direct-sum Real_D(B),
       with ell=d/delta copies.                  (RCH.10)

This proves, in both directions,

    Psi(B) is real symmetric PSD
       iff B is Hermitian PSD over D.             (RCH.11)

Thus the correspondence includes the boundary of the PSD cone and zero
blocks. It uses neither a quaternionic eigenvalue theorem nor an informal
identification of complex or quaternionic PSD with an arbitrary real block.

## RCH-7: real-rank conversion

Let rank_D(B) mean the dimension over D of the image of the right-D-linear
map z -> Bz on column vectors D^k. It is right linear even for H, because
matrix entries act on the left and multiplication is associative. An image
basis over D with s elements gives real dimension delta*s, by expanding
each coefficient in the real basis of D. Such a basis can be obtained by
successively choosing vectors outside the right span of the preceding
ones; finite-dimensional elimination over a division algebra terminates.
Hence

    rank_R(Real_D(B))=delta rank_D(B).

Together with (RCH.10),

    rank_R(Psi(B))=d rank_D(B).                    (RCH.12)

For the whole invariant top weight the formula is therefore

    rank_R(H)=sum_alpha d_alpha rank_(D_alpha)(B_alpha).
                                                       (RCH.13)

The factor is the real dimension d_alpha of the irreducible G-module,
not merely 1,2,4. Equivalently it is d_alpha/delta_alpha times the rank
of the corresponding realified multiplicity matrix. This distinction
matters when the irreducible real module contains several D-cyclic
coordinate copies in (RCH.5).

## RCH-8: all balance constraints after block reduction

Let O be the real orthogonal change from the isotypic coordinates to the
original paired top-space coordinates, and put

    K(B)=direct-sum_alpha Psi_alpha(B_alpha),
    H=O K(B) O^T,
    U_tilde=UO,    V_tilde=VO.

Every invariant symmetric PSD H is uniquely of this form with Hermitian
PSD B_alpha, once the coordinate choices have been fixed. It is feasible
precisely when the original equations are imposed:

    diag(V_tilde K(B) V_tilde^T)=1_n,
    diag(U_tilde K(B) U_tilde^T)=(n/m)1_m.          (RCH.14)

These are real affine constraints on the real coordinates of the Hermitian
blocks. PSD blocks alone do not imply balance, and the two families in
(RCH.14) must not be replaced by a trace condition alone. This is the
complete invariant feasible-set reduction within the stated model.

By RCH-1, nonemptiness of S(A) implies nonemptiness of this invariant
slice, and the reverse implication is immediate. Equation (RCH.13)
computes the rank of a particular invariant weight. It does not identify
that rank, or a minimum restricted to invariant weights, with the minimum
over all of S(A). Group averaging is a convex feasibility operation, not
a rank-preserving equivalence of individual solutions. No assertion about
all noninvariant extremizers is made here.

## RCH-9: audit checklist and remaining protocol work

The mathematical argument supplies: the paired induced action; exact
preservation of both balance normalizations; invariant averaging; the
orthogonal real isotypic description; the conjugate-transpose adjoint;
the equivalence of real PSD and Hermitian PSD blocks; and the precise
real-rank conversion. RS is the only imported representation-theoretic
theorem, with its full scope and locatable source in RCH-3.

The owner has registered the model inputs in the repaired claim, preserved
the distinction exposed by RCH-2 in a separate clarification record, and
registered RS as an external assumption. An independent adversarial review
must now bind that exact scoped node statement and this assembled proof
before a completion-level assessment. This author artifact does not modify
the node or supply an independent review. It also makes no novelty claim
for group averaging or real representation-theoretic block reduction.
