# Equality in the minimum-budget conditioning bound

Date: 2026-09-07. Author proof for independent review.
Canonical owner: `GROTHORB.minimal-conditioning-equality`.
Registration: `classical-family-registration-20260907.md`, C14.

This artifact proves both directions of the registered equivalence. All
load-bearing rank, trace, and equality steps are included here. It does not
assume that the two centered ranges are orthogonal, assert existence in any
dimension, or make a novelty or physical-dimension claim.

## CE-1: exact domain and the four conditions

Let r>=2 and m>=n>=1 be integers. Let a_i,b_j be unit vectors in R^r,
with weights u_i,v_j>0, such that

    sum_i u_i a_i a_i^T=sum_j v_j b_j b_j^T=I_r,
    m+n=r(r+1)/2+1.                               (CE.1)

Assume H -> ((a_i^T H a_i)_i,(b_j^T H b_j)_j) is injective on Sym_r.
On the Frobenius inner-product space

    V={H in Sym_r: tr(H)=0},
    q=dim(V)=r(r+1)/2-1=m+n-2,

put

    f_i=a_i a_i^T-I_r/r,    g_j=b_j b_j^T-I_r/r,
    F_A(H)=sum_i u_i <f_i,H>_F f_i,
    F_B(H)=sum_j v_j <g_j,H>_F g_j,
    F=F_A+F_B,    c=(r-1)/(m-1).

The claim is lambda_min(F)=c if and only if all four conditions hold:

1. u_i=r/m for every i;
2. (a_i^T a_k)^2=(m-r)/(r(m-1)) for every i!=k;
3. (a_i^T b_j)^2=1/r for every i,j; and
4. the restriction of F_B to span{g_j} has smallest eigenvalue at least c.

Each moment identity in (CE.1) has rank r, so its frame spans R^r and
has at least r vectors. Thus m,n>=r>=2. In particular c>0, m-1,n-1
are positive, and the subspaces used below will be nonzero. Taking
matrix traces in (CE.1) gives sum_i u_i=sum_j v_j=r.

## CE-2: positivity, exact ranks, and traces

For H in V, the quadratic forms are sums of nonnegative squares:

    <H,F(H)>_F
       =sum_i u_i <f_i,H>_F^2+sum_j v_j <g_j,H>_F^2.

If this is zero, all inner products vanish because the weights are
positive. Since H is traceless, these inner products are the original
quadratic evaluations a_i^T H a_i,b_j^T H b_j. Injectivity gives H=0.
Thus F is positive definite and rank(F)=q.

Write E_A=span{f_i}, E_B=span{g_j}. Applying the same sum-of-squares
argument to one side gives

    ker(F_A)=E_A^perp,    ker(F_B)=E_B^perp,
    rank(F_A)=dim(E_A),   rank(F_B)=dim(E_B).        (CE.2)

The centered moment identities are

    sum_i u_i f_i=0,    sum_j v_j g_j=0.

They are nontrivial dependences, so rank(F_A)<=m-1 and
rank(F_B)<=n-1. The image of F is contained in E_A+E_B, and therefore

    q=rank(F)<=rank(F_A)+rank(F_B)<=m+n-2=q.

Both rank bounds must be attained. In particular,

    dim(E_A)=m-1,    dim(E_B)=n-1,
    E_A+E_B=V,
    dim ker(F_B)=m-1.                              (CE.3)

At this point orthogonality of E_A and E_B has not been assumed or proved.

For a unit a, the projector aa^T has squared centered Frobenius norm

    ||aa^T-I_r/r||_F^2
       =tr((aa^T)^2)-(2/r)tr(aa^T)+tr(I_r)/r^2
       =(r-1)/r.

The trace on V of the rank-one operator |f><f| is ||f||_F^2. Hence

    tr_V(F_A)=tr_V(F_B)=r-1.                       (CE.4)

Here operator traces on V are distinct from the r by r matrix trace.

## CE-3: necessity of scalar Alice range and cross orthogonality

Assume lambda_min(F)=c. Set E=ker(F_B) and k=m-1. By (CE.3),
dim(E)=k. Choose an orthonormal basis H_1,...,H_k of E and extend it
to an orthonormal basis of V. Since F>=cI_V and F_B vanishes on E,

    kc <= sum_(ell=1)^k <H_ell,F_A(H_ell)>_F
       <= tr_V(F_A)=r-1=kc.                       (CE.5)

The second inequality omits only nonnegative diagonal contributions of
F_A. Thus both inequalities are equalities, and the contribution from
every remaining basis vector K in E^perp is zero:

    0=<K,F_A(K)>_F=sum_i u_i <f_i,K>_F^2.

Positivity of the weights implies that every f_i is orthogonal to every
such K. Therefore E_A is contained in E. Since both have dimension k,

    E_A=E=ker(F_B)=E_B^perp.                       (CE.6)

This is the point at which orthogonality is proved. It follows that F_A
is zero on E^perp and preserves E. On E it is at least cI_E, because
F_B vanishes there. Its trace on E is kc by (CE.5), so
F_A|E-cI_E is positive semidefinite with zero trace. Its eigenvalues
are nonnegative and sum to zero, forcing that operator to be zero.
Consequently

    F_A=cP_E,                                     (CE.7)

where P_E is the orthogonal projection onto E.

For any two unit vectors a,b,

    <aa^T-I_r/r,bb^T-I_r/r>_F=(a^T b)^2-1/r.

By (CE.6), all centered cross inner products vanish, proving condition 3.
On E_B=E^perp, F_A is zero and F agrees with F_B. The bound F>=cI_V
therefore proves condition 4. The restriction is well defined: F_B is
self-adjoint with range E_B and kernel E_B^perp by (CE.2).

## CE-4: recovering equal weights from the weighted Gram matrix

Define L:R^m -> V by its columns

    L e_i=sqrt(u_i) f_i,

and put s=(sqrt(u_1),...,sqrt(u_m))^T. Then

    LL^*=F_A=cP_E,
    Ls=sum_i u_i f_i=0,
    ||s||_2^2=r.

By (CE.3), L has rank m-1, so its kernel is exactly span{s}.
Its Gram matrix G=L^*L is positive semidefinite, has the same kernel,
and satisfies

    G^2=L^*(LL^*)L=cL^*P_E L=cG,

because range(L)=E. Thus the only eigenvalues of G are zero and c,
with the zero eigenspace exactly span{s}. Equivalently,

    G=c(I_m-ss^T/r).                              (CE.8)

Comparing the diagonal entries gives

    u_i(r-1)/r=G_ii=c(1-u_i/r),
    u_i=cr/(r-1+c)=r/m.                           (CE.9)

All divisions are valid because r>=2 and c>0. This proves condition 1;
equal weights were not assumed in obtaining the Gram kernel or (CE.8).

For i!=k, compare the off-diagonal entries of (CE.8):

    sqrt(u_i u_k)<f_i,f_k>_F
       =-(c/r)sqrt(u_i u_k).

The weights are positive, so cancellation gives <f_i,f_k>_F=-c/r.
Expanding the centered inner product now yields

    (a_i^T a_k)^2=1/r-c/r
       =(m-r)/(r(m-1)),                           (CE.10)

which is condition 2. This completes necessity of all four conditions.

## CE-5: sufficiency

Assume conditions 1--4. Keep the notation and rank facts of CE-2.
For the same weighted column map L, conditions 1 and 2 give

    G_ii=(r/m)(r-1)/r=(r-1)/m,
    G_ik=(r/m)(-c/r)=-c/m  for i!=k.

Since c(m-1)=r-1, this is exactly

    G=c(I_m-J_m/m),                               (CE.11)

where J_m is the all-ones matrix. The centered moment relation and equal
weights imply sum_i f_i=0, so L1=0. If Z=Lx is any vector in E_A,

    F_A Z=LL^*Lx=LGx
         =cLx-(c/m)L1(1^T x)=cZ.

Also F_A is zero on E_A^perp by (CE.2). Thus

    F_A=cP_(E_A).                                 (CE.12)

Condition 3 says <f_i,g_j>_F=0 for every cross pair. Therefore E_A and
E_B are orthogonal. Their sum is V by (CE.3), so V=E_A orthogonal-sum
E_B. The two operators consequently act in separate blocks:

    F=cI_(E_A) orthogonal-sum (F_B|E_B).

Condition 4 makes the second block at least cI_(E_B). The first block
has the eigenvalue c and has positive dimension m-1. Hence

    lambda_min(F)=c,

which proves sufficiency and the full registered equivalence.

## CE-6: balanced sides and the smallest dimension

When m=n, the proof of necessity still uses the same E=ker(F_B), and
does not need m>n. For consistency, condition 4 is then imposed on a
space of dimension n-1=m-1 with trace r-1=c(m-1). Thus all eigenvalues
of that restricted operator must equal c if they are at least c. No
step of either direction changes or assumes this fact in advance.

When r=2, the moment identities force m,n>=2, while the total budget
is four. Hence m=n=2 and c=1. The four conditions have well-defined
values: Alice weights one, distinct Alice squared overlap zero, cross
squared overlaps 1/2, and the one-dimensional Bob restriction at least
one. Both centered spans have dimension one, and every rank, trace,
Gram-kernel, and compression step above remains valid. There is no
zero-dimensional restriction or vanishing denominator in this case.

## CE-7: review and scope

This equivalence is conditional on the complete hypotheses in CE-1.
It does not decide whether the four conditions are jointly realizable in
any given dimension or setting split, prove optimality below the bound
when they fail, or derive a noise or self-testing theorem. No numerical
experiment is needed for the argument. The author proof remains subject
to independent adversarial review; prior-art comparison is separate.
