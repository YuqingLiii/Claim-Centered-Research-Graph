# Antipodal duplication and a subsequent diagonal shift

Date: 2026-09-07. Author proof for independent review.
Canonical owner: `GROTHORB.antipodal-shift-comparison`.
Registration: `classical-family-registration-20260907.md`, C8.

This is a direct elementary proof of the registered statement. It imports
no literature note or project theorem and makes no novelty claim.

## AD-1: statement and reduction to Bob signs

Let C be any real m by m matrix, lambda>=0, and

    D(C) = (1/2) [ C  -C ] ,    B=D(C)-lambda I_(2m).
                 [-C   C ]

For every real square matrix M, independently maximizing the Alice signs
in each coordinate gives

    beta_cl(M) := max_{s,t in {-1,+1}^dim(M)} s^T M t
               = max_{t in {-1,+1}^dim(M)} ||Mt||_1. (AD.1)

No symmetry or positivity of M is required.

We prove

    beta_cl(B)/2 = max_{z in {-1,0,1}^m} F_lambda(z),

where

    F_lambda(z)
      = sum_{i:z_i!=0} |(Cz)_i-lambda z_i|
        + sum_{i:z_i=0} max(|(Cz)_i|,lambda).        (AD.2)

## AD-2: exact sign-to-ternary correspondence

Write a Bob sign vector as t=(a,b), with a,b in {-1,+1}^m, and set

    z=(a-b)/2,    q=(a+b)/2.

At each coordinate, (z_i,q_i) is one of

    (1,0), (-1,0), (0,1), (0,-1).

Conversely these coordinatewise choices give a unique sign pair by

    a=z+q,    b=q-z.                               (AD.3)

Thus this is a bijection between Bob sign pairs and admissible (z,q).
Every z in {-1,0,1}^m is realized: q_i=0 when z_i!=0, and q_i may be
either sign when z_i=0. The number of q choices is immaterial below.

Put v=Cz-lambda z. Block multiplication using (AD.3) gives

    Bt = (Cz-lambda(z+q), -Cz-lambda(q-z))
       = (v-lambda q, -v-lambda q).

For real u,h,

    |u-h|+|u+h|=2 max(|u|,|h|).

For example, if |u|>=|h|, both u-h and u+h have the sign of u (allowing
zero), and their absolute values sum to 2|u|; the other case follows by
interchanging the roles. Therefore

    ||Bt||_1 = 2 sum_i max(|v_i|,lambda |q_i|).

If z_i!=0 then q_i=0, giving the first type of summand in (AD.2).
If z_i=0 then |q_i|=1 and v_i=(Cz)_i, giving the second type. Hence

    ||Bt||_1=2F_lambda(z).

This expression is independent of all choices of q. Every ternary z is
attained, so maximizing (AD.1) proves the exact identity (AD.2).

## AD-3: lower comparison and equality at zero shift

Restrict the maximum in (AD.2) to z in {-1,+1}^m. There are then no zero
coordinates and

    F_lambda(z)=||(C-lambda I_m)z||_1.

Using (AD.1),

    beta_cl(D(C)-lambda I_(2m))
       >= 2 beta_cl(C-lambda I_m).                 (AD.4)

At lambda=0, F_0(z)=||Cz||_1. This function is convex because C is linear
and the triangle inequality makes the norm convex. If a ternary vector z
has a zero coordinate i, both z+e_i and z-e_i remain ternary and

    ||Cz||_1
       <= (||C(z+e_i)||_1+||C(z-e_i)||_1)/2.

At least one of these two vectors has value at least that of z. Repeating
at the remaining zero coordinates produces a sign vector of no smaller
value. Thus

    max_{z in {-1,0,1}^m} ||Cz||_1
       = max_{z in {-1,+1}^m} ||Cz||_1
       = beta_cl(C).

Combining this with (AD.2) proves

    beta_cl(D(C))=2 beta_cl(C),                     (AD.5)

which is the claimed equality case of (AD.4).

## AD-4: scope

The theorem applies to arbitrary real square C, including nonsymmetric or
indefinite matrices. It does not assert equality in (AD.4) for positive
lambda. The ternary choices with zero coordinates are precisely the extra
possibilities the exact shifted formula must retain. Correctness of these
identities and their novelty are separate questions. This author argument
requires independent adversarial review before completion-level promotion.
