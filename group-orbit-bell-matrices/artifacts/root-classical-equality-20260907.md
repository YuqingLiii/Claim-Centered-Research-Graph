# Equality cases for the full D_r root classical value

Date: 2026-09-07. Author proof for independent review.
Canonical owner: `GROTHORB.root-classical-equality`.
Route: `support-equality`.
Registration: `classical-family-registration-20260907.md`, C5.
Load-bearing premise: `GROTHORB.root-classical`, whose author proof is
`root-classical-value-20260907.md`, RC-1 through RC-4.

This artifact proves the registered equality implication and records its
complete assembly conditional on the base-value premise. It does not assign
a completion level or establish the separate shifted-family theorem.

## RE-1: conventions and statement

Fix r>=3. The row set of W is the full set

    R_r = {alpha e_i + beta e_j: i<j, alpha,beta in {-1,+1}}.

Each root, including its antipode, occurs once. Set

    n=2r(r-1),    c=4(r-1),    A_r=WW^T/c,
    rho=(r-1,r-2,...,1,0),    Q=||rho||_2^2,
    L=4 sqrt(Q).

The base-value premise states

    beta_cl(A_r) = max_{s,t in {-1,+1}^{R_r}} s^T A_r t
                = 2r(2r-1)/3 = L^2/c.               (RE.1)

A signed coordinate permutation g is an orthogonal r by r matrix having
exactly one entry in {-1,+1} per row and per column, with all other entries
zero. Such matrices permute R_r. The assertion is that the maximizing
ordered pairs are exactly

    (s(y),s(y)),  where y=g rho and s(y)_w=sign(w dot y),

and their number is 2^(r-1) r!. We will prove that all inner products used
in this sign expression are nonzero.

## RE-2: bilinear equality gives a common maximal image

For a sign vector u define z_u=W^T u. Since (u,u) is an allowed pair,
(RE.1) implies

    ||z_u||_2^2/c = u^T A_r u <= L^2/c.

Thus ||z_u||_2<=L for every u. If (s,t) attains the bilinear maximum,

    L^2 = z_s dot z_t <= ||z_s||_2 ||z_t||_2 <= L^2.  (RE.2)

Both norms therefore equal L: each is at most L, their product equals
L^2, and L>0. Equality in Cauchy--Schwarz with positive inner product
then gives z_s=z_t=z, with ||z||_2=L. Equivalently, one can calculate
||z_s-z_t||_2^2=L^2+L^2-2L^2=0.

The identity W^T s=W^T t alone is not an injectivity statement about W^T.
The remaining steps use maximality to recover every sign individually.

## RE-3: the common image has a signed-permutation direction

Put x=z/L, so ||x||_2=1. For u=s and also for u=t,

    sum_{w in R_r} u_w (w dot x) = x dot z_u = L.     (RE.3)

Let a_1>=...>=a_r>=0 be the decreasing rearrangement of the absolute
coordinates of x. The support identity follows by grouping the four roots
over each coordinate pair:

    F(x) := sum_{w in R_r} |w dot x|
          = 4 sum_{i<j} max(|x_i|,|x_j|)
          = 4 sum_{i=1}^r (r-i)a_i.                 (RE.4)

For the first equality after the definition, use
|a+b|+|a-b|=2 max(|a|,|b|); the four signed roots supply twice the left
side. For the next equality, sorted coordinate a_i is the larger member
in precisely r-i coordinate pairs, with ties giving the same value.

Since sum_i a_i^2=1, Cauchy--Schwarz gives

    F(x)=4 rho dot a <= 4||rho||_2 ||a||_2=L.

On the other hand each term u_w(w dot x)<=|w dot x|, so (RE.3) gives
L<=F(x). Hence equality holds. Equality in the last Cauchy--Schwarz
inequality requires a to be a positive scalar multiple of rho, because
rho is nonzero and rho dot a=||rho||_2||a||_2>0. Its norm fixes the scalar:

    a=rho/sqrt(Q).

Consequently

    x=g rho/sqrt(Q),   and z=Lx=4g rho,              (RE.5)

for some signed coordinate permutation g. In particular, the absolute
coordinates of x are pairwise distinct, and exactly one coordinate is zero.

For a root w=alpha e_i+beta e_j, the equation w dot x=0 would imply
|x_i|=|x_j|. This is impossible for i<j. Thus

    w dot x != 0 for every w in R_r.                (RE.6)

This is the strictness needed to recover the signs; the one zero coordinate
of x creates no root orthogonal to x because roots use two distinct
coordinates whose absolute values are different.

## RE-4: support equality recovers every sign on both sides

For u=s or u=t, subtract (RE.3) from F(x)=L:

    sum_{w in R_r} (|w dot x|-u_w(w dot x))=0.

Each summand is nonnegative. A finite sum of nonnegative numbers is zero
only when every summand is zero. By (RE.6), this happens precisely when

    u_w=sign(w dot x)=sign(w dot g rho)              (RE.7)

for every root w. Applying this to both s and t proves

    s=t=s(g rho).

Thus equality of the images does imply equality of the sign vectors at the
optimum, through termwise strictness of the support maximum. The argument
does not presume that W^T is injective on arbitrary sign vectors.

## RE-5: converse and injectivity of the direction-to-sign map

For y=rho, a root w=alpha e_i+beta e_j with i<j satisfies
rho_i>rho_j>=0, so sign(w dot rho)=alpha. Summing the corresponding
signed roots over alpha,beta gives 4e_i for each pair i<j. Therefore

    sum_{w in R_r} sign(w dot rho) w=4rho.           (RE.8)

Now let y=g rho. Since g is orthogonal and permutes the full root set,
write w=g v in the sum to obtain

    W^T s(y)
       = sum_{w in R_r} sign(w dot g rho)w
       = g sum_{v in R_r} sign(v dot rho)v
       = 4g rho = 4y.                              (RE.9)

The root inner products are nonzero as in (RE.6). In particular,

    s(y)^T A_r s(y)=16||y||_2^2/c=L^2/c,

which equals the base-value maximum. This proves the converse.

Moreover (RE.9) proves that different orbit vectors produce different sign
vectors: if s(y)=s(y'), then applying W^T yields 4y=4y', so y=y'. No
extra identifications of sign patterns are hidden by the group action.

## RE-6: exact count and the zero-coordinate stabilizer

The coordinates of rho have the distinct absolute values 0,1,...,r-1.
An orbit vector y=g rho is therefore determined uniquely by:

1. a placement of these r distinct absolute values in r coordinate slots,
   giving r! possibilities; and
2. a sign for each of the r-1 nonzero coordinates, giving 2^(r-1)
   possibilities.

The sign at the zero coordinate has no effect on the vector. Equivalently,
the full signed permutation group has order 2^r r!. A group element fixing
rho must preserve every absolute coordinate value, so its permutation is
the identity. It must have positive signs at all nonzero coordinates, and
may choose either sign at the sole zero coordinate. The stabilizer has
exactly two elements, explaining exactly a factor of two duplication in
the parameter g and no more.

Thus the orbit has 2^(r-1)r! vectors. By RE-5 its map to sign vectors is
injective, and by RE-2 through RE-4 every maximizing ordered pair is the
corresponding diagonal pair. The number of maximizing pairs is therefore

    2^(r-1) r!.

This counts ordinary ordered sign pairs, with no quotient by global sign,
coordinate permutation, or interchange of the two sides.

## RE-7: exact finite replay and its limits

The standard-library checker
`grothendieck-group-orbit/tools/check_root_classical_equality.py` performs
two distinct checks:

- For r=3,4,5, enumerate every signed coordinate permutation, verify exactly
  two group elements per orbit vector, construct every predicted sign
  pattern, and check nonvanishing root products, W^T s(y)=4y, the exact
  classical value and injectivity of the direction-to-sign map.
- For r=3, enumerate all 4096 Bob sign vectors t. For each t, maximize
  Alice's signs term by term using sum_w |(WW^T t)_w|. The maximizing
  Bob vectors are checked to be exactly the 24 predicted patterns. Each
  has no zero Alice coefficient and has the unique Alice maximizer s=t.
  Hence this checks all bilinear maximizers at r=3 without omitting any
  pair: the optimization over Alice is exact and the uniqueness check
  excludes unenumerated tied Alice choices.

Command from the candidate repository root:

    python3 grothendieck-group-orbit/tools/check_root_classical_equality.py

The run is recorded in `root-classical-equality-exact-check-20260907.txt`.
These finite checks do not establish the universal classification; that
argument is RE-2 through RE-6 and depends on the base-value claim (RE.1).
Neither checker success nor this author artifact licenses completion-level
promotion without independent adversarial review of the exact claim and
the registered route implication with its supporting premise.
