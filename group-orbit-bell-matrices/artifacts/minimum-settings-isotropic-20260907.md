# Minimum total setting count in the positive isotropic-frame framework

Date: 2026-09-07. Author proof for independent review.
Canonical owner: `GROTHORB.minimum-settings-isotropic`.
Registration: `classical-family-registration-20260907.md`, C12.

This direct elementary argument proves the registered minimum within its
specified frame class. It does not assert a minimum for arbitrary Bell
experiments, a physical dimension bound, self-testing, or originality.
No other project theorem or literature result is a load-bearing input.

## MS-1: domain and the injective map

Fix an integer r>=1 and let d=r(r+1)/2, the dimension of the real vector
space Sym_r of symmetric r by r matrices. For a pair of finite nonempty
positive weighted unit frames, write

    a_1,...,a_m in R^r,    b_1,...,b_n in R^r,
    u_i>0, v_j>0,    S=sum_i u_i>0, T=sum_j v_j>0.

The isotropy conditions are

    sum_i u_i a_i a_i^T=(S/r)I_r,
    sum_j v_j b_j b_j^T=(T/r)I_r.                  (MS.1)

The map to be made injective is the linear map

    Phi: Sym_r -> R^(m+n),
    Phi(H)=((a_i^T H a_i)_i,(b_j^T H b_j)_j).       (MS.2)

The output coordinates in (MS.2) are unweighted; the weights enter the
isotropy conditions and the linear dependence used below.

## MS-2: a universal trace relation gives the lower bound

For every H in Sym_r, taking trace against (MS.1) gives

    sum_i (u_i/S) a_i^T H a_i=tr(H)/r,
    sum_j (v_j/T) b_j^T H b_j=tr(H)/r.

Their difference is the output relation

    sum_i (u_i/S) Phi(H)_i
       -sum_j (v_j/T) Phi(H)_(m+j)=0.              (MS.3)

The coefficient vector (u_1/S,...,u_m/S,-v_1/T,...,-v_n/T) is
nonzero. Consequently the image of Phi lies in a hyperplane of R^(m+n)
and rank(Phi)<=m+n-1. If Phi is injective on Sym_r, its rank is d.
Therefore every admissible pair satisfies

    m+n >= d+1 = r(r+1)/2+1.                       (MS.4)

This additional one is forced by the relation between the two isotropic
frames, not merely by counting the coordinates of H.

## MS-3: the registered construction and exact isotropy

For Alice take a_i=e_i (1<=i<=r), with all u_i=1. Then S=r and

    sum_i u_i a_i a_i^T=I_r=(S/r)I_r.

For Bob take one vector

    b_ij=(e_i-e_j)/sqrt(2),    v_ij=2/r

for each i<j, and one additional vector

    b_0=(1,...,1)^T/sqrt(r),    v_0=1.

These are unit vectors and all their weights are positive. Bob's total
weight is

    T=(2/r) binom(r,2)+1=r.

Let J be the all-ones r by r matrix. The elementary matrix identity

    sum_{i<j}(e_i-e_j)(e_i-e_j)^T=rI_r-J           (MS.5)

holds because each diagonal entry of the sum is r-1 and each off-diagonal
entry is -1. At r=1 the sum is empty and both sides are the zero matrix.
Therefore Bob's weighted moment is

    sum_{i<j} (2/r)b_ij b_ij^T+b_0 b_0^T
       = (1/r)(rI_r-J)+J/r
       = I_r=(T/r)I_r.                            (MS.6)

Thus both sides satisfy the required isotropy with S=T=r. The counts are

    m=r,    n=binom(r,2)+1,
    m+n=r+binom(r,2)+1=d+1.                       (MS.7)

## MS-4: injectivity and attainment of the minimum

Suppose H in Sym_r lies in the kernel of Phi for this construction.
Alice's outputs give H_ii=e_i^T H e_i=0 for every i. Each difference
vector on Bob's side then gives

    0=b_ij^T H b_ij
      =(H_ii+H_jj-2H_ij)/2=-H_ij.

All off-diagonal entries are zero as well, so H=0 and Phi is injective.
The additional all-ones vector is not needed for this kernel argument;
it supplies the term J/r that completes Bob's isotropy in (MS.6).

The lower bound (MS.4) and the admissible injective construction with count
(MS.7) prove that the minimum total number is exactly r(r+1)/2+1.

## MS-5: the cases r=1 and r=2

For r=1, Alice and Bob each have the single vector e_1 with weight one.
There are no difference vectors. The map sends the one scalar entry h
to (h,h), so it is injective with total count two, equal to d+1.

For r=2, Alice has e_1,e_2 and Bob has
(e_1-e_2)/sqrt(2),(e_1+e_2)/sqrt(2), all with weight one. Both moment
matrices are I_2. Alice's two outputs fix the diagonal entries and Bob's
difference output fixes the off-diagonal entry, so the map is injective.
The total is four, equal to dim(Sym_2)+1. These cases use the exact same
construction and proof; neither is an exception to the formula.

## MS-6: exact rational outer-product replay and scope

The standard-library checker
`grothendieck-group-orbit/tools/check_minimum_settings_isotropic.py`
uses only rational outer products, never numerical square roots:

    a_i a_i^T=e_i e_i^T,
    b_ij b_ij^T=(e_i-e_j)(e_i-e_j)^T/2,
    b_0 b_0^T=J/r.

For r=1,...,10 it checks positive weights, unit rank-one projectors,
both exact isotropy identities, the output trace relation, and the rank
d of the full quadratic measurement matrix by rational elimination. In
that matrix the coefficient of the independent off-diagonal variable
H_ij is twice the (i,j) entry of the corresponding outer product.
It also checks the precise side counts and total d+1.

Command from the candidate repository root:

    python3 grothendieck-group-orbit/tools/check_minimum_settings_isotropic.py

Run record: `minimum-settings-isotropic-exact-check-20260907.txt`.
This finite replay checks the construction and normalizations; the all-r
minimum is established by MS-2 through MS-4. Independent review must
check both the universal lower bound and the construction. Prior-art
positioning remains separate from mathematical correctness.
