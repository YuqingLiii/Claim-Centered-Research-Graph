# A smallest-eigenvalue bound at the minimum setting budget

Date: 2026-09-07. Author proof for independent review.
Canonical owner: `GROTHORB.minimal-setting-conditioning`.
Registration: `classical-family-registration-20260907.md`, C13.

This direct finite-dimensional argument proves the registered bound and
positive definiteness. It imports no project theorem or external result
beyond elementary inner-product-space linear algebra. It does not assert
sharpness, an equality classification, an operational noise guarantee,
self-testing, or originality.

## MC-1: hypotheses and notation

Let r>=2 and m,n>=1 be integers. Let a_i,b_j be unit vectors in R^r,
with positive weights u_i,v_j, such that

    sum_i u_i a_i a_i^T=I_r,
    sum_j v_j b_j b_j^T=I_r.                      (MC.1)

Assume

    m+n=r(r+1)/2+1                               (MC.2)

and assume the combined map

    H -> ((a_i^T H a_i)_i,(b_j^T H b_j)_j)

is injective on Sym_r. Equip Sym_r with the Frobenius inner product
<H,K>_F=tr(HK). Let

    V={H in Sym_r: tr(H)=0},
    q=dim(V)=r(r+1)/2-1=m+n-2,
    f_i=a_i a_i^T-I_r/r,    g_j=b_j b_j^T-I_r/r.

The vectors f_i,g_j belong to V. Define self-adjoint positive
semidefinite operators on V by

    F_A(H)=sum_i u_i <f_i,H>_F f_i,
    F_B(H)=sum_j v_j <g_j,H>_F g_j,
    F=F_A+F_B.                                    (MC.3)

We will prove that F is positive definite and

    lambda_min(F) <= (r-1)/max(m-1,n-1).            (MC.4)

Taking the matrix trace in (MC.1), and using that the frame vectors are
unit, gives sum_i u_i=sum_j v_j=r. Also (MC.1) forces each frame to
span R^r: a vector orthogonal to a whole frame would be killed by I_r.
Thus m,n>=r>=2. In particular both denominators m-1,n-1 used below
are positive.

## MC-2: positive definiteness and exact single-side ranks

For H in V,

    <H,F(H)>_F
       = sum_i u_i <f_i,H>_F^2+sum_j v_j <g_j,H>_F^2.

Every term is nonnegative. If the sum vanishes, positivity of the weights
forces every inner product to vanish. Since H is traceless,

    <f_i,H>_F=a_i^T H a_i,
    <g_j,H>_F=b_j^T H b_j.

Combined injectivity therefore gives H=0. This proves that F is positive
definite and rank(F)=q.

For either single-side operator, the same sum-of-squares calculation
shows that its kernel is the orthogonal complement of its vector span:

    ker(F_A)=span{f_i}^perp,
    ker(F_B)=span{g_j}^perp,

where orthogonal complements are taken in V. Consequently

    rank(F_A)=dim span{f_i},
    rank(F_B)=dim span{g_j}.                        (MC.5)

Centering the moment identities in (MC.1), using the weight sums r,
gives nontrivial linear dependences

    sum_i u_i f_i=0,    sum_j v_j g_j=0.

The coefficient vectors are nonzero, so

    rank(F_A)<=m-1,    rank(F_B)<=n-1.              (MC.6)

On the other hand, the image of F=F_A+F_B is contained in the sum of
the two images. Therefore

    q=rank(F) <= rank(F_A)+rank(F_B)
      <= (m-1)+(n-1)=q.

Both inequalities are equalities. Each bound in (MC.6) must therefore
be attained, because their two upper bounds already sum to q. Thus

    rank(F_A)=m-1,    rank(F_B)=n-1,
    dim ker(F_A)=n-1,    dim ker(F_B)=m-1.          (MC.7)

These ranks use the exact setting budget (MC.2), not merely injectivity.
They make no assertion that the two ranges are orthogonal.

## MC-3: the two operator traces

For a unit vector a, its rank-one matrix P=aa^T satisfies P^2=P and
tr(P)=1. Therefore its centered matrix has squared Frobenius norm

    ||P-I_r/r||_F^2
       = tr(P^2)-(2/r)tr(P)+tr(I_r)/r^2
       = 1-2/r+1/r=(r-1)/r.

The same formula holds for every f_i and g_j. For a vector f in the
inner-product space V, the rank-one operator H -> <f,H>_F f has operator
trace ||f||_F^2: sum its diagonal entries in an orthonormal basis and
apply the Pythagorean identity. Consequently (MC.3) and the weight sums
give

    tr_V(F_A)=sum_i u_i ||f_i||_F^2=r-1,
    tr_V(F_B)=sum_j v_j ||g_j||_F^2=r-1.           (MC.8)

Here tr_V is the trace of an operator on V; it is distinct from the
r by r matrix trace used in the definition of V.

## MC-4: compress to the opposite kernel

Let mu=lambda_min(F), which is positive by MC-2. Let

    E=ker(F_B),    k=dim(E)=m-1>0.

Choose an orthonormal basis H_1,...,H_k of E and extend it to an
orthonormal basis of V. For each H_ell, the Rayleigh bound and the
identity F_B(H_ell)=0 give

    mu <= <H_ell,F(H_ell)>_F
        = <H_ell,F_A(H_ell)>_F.

Adding these k inequalities, and then using positivity of F_A for the
remaining basis vectors, gives

    k mu
       <= sum_(ell=1)^k <H_ell,F_A(H_ell)>_F
       <= tr_V(F_A)=r-1.                          (MC.9)

The middle sum is the trace of the compression of F_A to E. Its trace
cannot exceed the full trace because all omitted diagonal contributions
of a positive semidefinite operator are nonnegative. No invariance of E
under F_A is needed. Thus

    mu <= (r-1)/(m-1).

Interchanging A and B and using dim ker(F_A)=n-1 yields

    mu <= (r-1)/(n-1).

Taking the smaller of these two upper bounds proves (MC.4), since r-1
and both denominators are positive.

## MC-5: scope and review boundary

The proof is universal for the normalized positive frames and exact total
count stated in MC-1. It uses combined injectivity only to establish
positive definiteness and, together with the budget, the exact ranks.
It uses isotropy to obtain the centering relations and the trace values.

No computation is needed for the proof. This artifact does not establish
that the bound is attainable for any specified setting split, characterize
equality, or derive a condition-number or experimental perturbation
guarantee. Those are separate research questions requiring registration
before investigation. The author proof remains subject to independent
adversarial review and separate prior-art comparison.
