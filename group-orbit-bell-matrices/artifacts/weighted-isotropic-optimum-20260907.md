# Exact vector optimum for two positive weighted isotropic frames

Date: 2026-09-07. Author proof for independent review.
Canonical owner: `GROTHORB.weighted-isotropic-optimum`.
Registration: `classical-family-registration-20260907.md`, C11.

This is a direct linear-algebra proof of the registered statement. It uses
no transitivity, group action, equality of setting counts, or imported
project theorem. Correctness and prior-art overlap are separate questions;
this artifact makes no originality claim.

## WI-1: statement, dimensions, and conventions

Let r,m,n be positive integers, let a_i (1<=i<=m) and b_j (1<=j<=n) be unit
vectors in R^r, and let u_i,v_j be positive real weights. Write

    S=sum_i u_i,    T=sum_j v_j,
    sum_i u_i a_i a_i^T=(S/r)I_r,
    sum_j v_j b_j b_j^T=(T/r)I_r.                  (WI.1)

Define the real m by n matrix

    M_ij=u_i v_j (a_i dot b_j).

Its real vector Bell value is the supremum of

    sum_(i,j) M_ij (x_i dot y_j)                   (WI.2)

over unit strategy vectors x_i,y_j in a common R^d, with any positive
integer d. Allowing an arbitrary real Hilbert space gives the same problem,
because finitely many strategy vectors span a finite-dimensional subspace.
The assertion is that this value is ST/r and is attained at d=r by
x_i=a_i, y_j=b_j.

The stated domain and positive weights give S,T>0. There is no requirement
that m=n. Under (WI.1), the frames necessarily span R^r and hence m,n>=r.

## WI-2: weighted spectral norm and the global upper bound

Form the matrices A in R^(m by r) and B in R^(n by r) whose rows are
sqrt(u_i) a_i^T and sqrt(v_j) b_j^T, respectively. Isotropy gives

    A^T A=(S/r)I_r,    B^T B=(T/r)I_r.

Consequently P=sqrt(r/S)A and Q=sqrt(r/T)B have orthonormal columns.
Put

    K=AB^T=(sqrt(ST)/r) P Q^T,
    K_ij=sqrt(u_i v_j)(a_i dot b_j).                (WI.3)

The rectangular operator P Q^T has norm one. Indeed, P is an isometry
on R^r, and Q^T is a contraction: QQ^T is an orthogonal projection
since Q^TQ=I_r. This proves the upper bound one. For any unit e in R^r,
the unit input Qe is sent to the unit vector Pe, giving equality. Thus

    ||K||_op=sqrt(ST)/r.                           (WI.4)

Now fix arbitrary unit strategy vectors in any common R^d. Let X and Y
have rows x_i^T and y_j^T. Define the weighted strategy matrices

    X~=diag(sqrt(u_i))X,    Y~=diag(sqrt(v_j))Y.

Their Frobenius norms, the Euclidean norms of their arrays of entries,
satisfy

    ||X~||_F^2=sum_i u_i ||x_i||_2^2=S,
    ||Y~||_F^2=sum_j v_j ||y_j||_2^2=T.             (WI.5)

The placement of both square-root factors is essential: by (WI.3),

    sum_(i,j) M_ij (x_i dot y_j)
       = tr(X~^T K Y~).

Apply Cauchy--Schwarz to all entries and the operator norm bound to
each column of Y~:

    tr(X~^T K Y~)
       <= |tr(X~^T K Y~)|
       <= ||X~||_F ||K Y~||_F
       <= ||X~||_F ||K||_op ||Y~||_F
       = sqrt(S) (sqrt(ST)/r) sqrt(T)
       = ST/r.                                    (WI.6)

This bounds every strategy dimension simultaneously. K is m by n,
X~ is m by d, and Y~ is n by d, so every product is defined even when
m!=n. This is a weighted norm bound; it does not assert that applying
the ordinary unweighted spectral bound directly to M must be tight.

## WI-3: matching strategy and the case r=1

Choose x_i=a_i and y_j=b_j in R^r. The resulting value is

    sum_(i,j) u_i v_j (a_i dot b_j)^2
       = tr[(sum_i u_i a_i a_i^T)(sum_j v_j b_j b_j^T)]
       = tr[((S/r)I_r)((T/r)I_r)]
       = ST/r.                                    (WI.7)

The first trace identity follows from
tr(a_i a_i^T b_j b_j^T)=(a_i dot b_j)^2 and linearity of trace.
Together (WI.6) and (WI.7) prove the asserted optimum and attainment.

Nothing in the proof requires r>1. At r=1 every unit a_i,b_j is a scalar
in {-1,+1}, isotropy (WI.1) is automatic, and the same strategy gives
sum_(i,j) u_i v_j=ST. The bound (WI.6) is ST as well. This also checks
the normalization at the smallest allowed dimension.

## WI-4: an equivalent diagonal quadratic upper certificate

For clarity about the weighted bound, define D_u=diag(u_i), D_v=diag(v_j)
and the symmetric (m+n) by (m+n) matrix

            [ (T/r)D_u       -M       ]
    L =     [    -M^T      (S/r)D_v   ].            (WI.8)

This matrix is positive semidefinite. To check it without importing an
SDP duality theorem, take p in R^m and q in R^n and write
p~=D_u^(1/2)p, q~=D_v^(1/2)q. Equations (WI.3)--(WI.4) give

    |p^T M q|=|p~^T K q~|
       <= (sqrt(ST)/r)||p~||_2||q~||_2.

Hence

    (p,q)^T L (p,q)
       >= (1/r)(sqrt(T)||p~||_2-sqrt(S)||q~||_2)^2
       >= 0.

For any unit vector strategy, apply this nonnegative quadratic form to
each coordinate column of (X,Y) and add. The result is

    0 <= 2ST/r - 2 sum_(i,j) M_ij(x_i dot y_j),

the same upper bound as (WI.6). This certificate is included only as an
equivalent expression of the registered claim's upper argument.

## WI-5: exact examples and review boundary

The companion standard-library checker
`grothendieck-group-orbit/tools/check_weighted_isotropic_optimum.py`
uses rational arithmetic in two finite cases:

- r=1, m=2, n=3, with unequal positive weights: S=3,T=6, optimum 18.
- r=2, m=3, n=4, with nonuniform positive rational weights. Alice's
  vectors are (1,0),(3/5,4/5),(3/5,-4/5) with weights
  7/8,25/16,25/16. Bob's vectors are (1,0),(0,1),(3/5,4/5),
  (-4/5,3/5) with weights 1,1,2,2. Here S=4,T=6, optimum 12.

For each example the checker verifies unit vectors, both isotropy
identities, the explicit matching value, and the positive semidefiniteness
of the rational matrix L in (WI.8) by exact elimination with nonnegative
pivots. The diagonal contribution tr(L)/2 is checked to equal ST/r.

Command from the candidate repository root:

    python3 grothendieck-group-orbit/tools/check_weighted_isotropic_optimum.py

Run record: `weighted-isotropic-exact-check-20260907.txt`.
These examples check normalization and a concrete upper certificate; the
universal result follows from WI-2 through WI-3. This author argument has
not by itself completed independent review or the separately requested
prior-art comparison, and does not license a completion-level promotion.
