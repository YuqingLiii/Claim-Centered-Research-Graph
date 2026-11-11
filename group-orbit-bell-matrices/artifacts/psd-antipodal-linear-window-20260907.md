# A sufficient linear-shift window for PSD antipodal duplication

Date: 2026-09-07. Author proof for independent review.
Canonical owner: `GROTHORB.psd-antipodal-linear-window`.
Registration: `classical-family-registration-20260907.md`, C15.

This direct elementary proof establishes the registered sufficient interval.
It uses no other project theorem or external result, does not assert a
maximal interval, and makes no novelty claim. No numerical testing is used.

## PW-1: statement and the PSD classical value

Let N>=1 and let C be a real symmetric positive-semidefinite N by N
matrix. For a real square k by k matrix M, write

    beta_cl(M)=max_{s,t in {-1,+1}^k} s^T M t.

Define

    D(C)=(1/2)[ C -C; -C C ],
    B_lambda=D(C)-lambda I_(2N),
    d_i=C_ii,
    0<=lambda<=(1/2)min_i d_i.                    (PW.1)

All d_i are nonnegative by PSD. Let

    K=max_{z in {-1,+1}^N} z^T C z.

The maximum exists because the sign set is finite. For arbitrary signs
s,t, PSD and symmetry give

    0<=(s-t)^T C(s-t)
      =s^T Cs+t^T Ct-2s^T Ct.

Hence s^T Ct<=(s^T Cs+t^T Ct)/2<=K. A sign z attaining K gives
the matching pair s=t=z, so

    beta_cl(C)=K.                                 (PW.2)

This reduction is only applied to the PSD matrix C. It is not assumed
for B_lambda, which may be indefinite.

We prove

    beta_cl(B_lambda)=2K-2N lambda
                    =2 beta_cl(C)-2N lambda.       (PW.3)

## PW-2: independent sign completion at a prescribed mean

For any x in [-1,1]^N, choose independent signs Z_i with

    Pr(Z_i=1)=(1+x_i)/2,
    Pr(Z_i=-1)=(1-x_i)/2.

These are valid probabilities even when x_i is an endpoint. Then
E[Z_i]=x_i, E[Z_i^2]=1, and for i!=j, independence gives
E[Z_i Z_j]=x_i x_j. Expanding the finite quadratic sum yields

    E_x:=E[Z^T C Z]
        =x^T Cx+sum_i d_i(1-x_i^2).               (PW.4)

Every sign realization has quadratic value at most K, so E_x<=K.
This is a finite convex-combination argument, with no sampling error or
probabilistic asymptotic step. The expectation identity itself does not
require PSD; PSD will be used separately in the upper certificate.

## PW-3: exact antipodal coordinates for an arbitrary sign pair

Write arbitrary Alice and Bob signs as

    a=(a_+,a_-),    b=(b_+,b_-),

where each component is in {-1,+1}^N. Set

    p=(a_+-a_-)/2,    u=(a_++a_-)/2,
    q=(b_+-b_-)/2,    v=(b_++b_-)/2.

For each coordinate, exactly one member of (p_i,u_i) is a sign and the
other is zero; the same holds for (q_i,v_i). In particular,

    p_i^2+u_i^2=q_i^2+v_i^2=1,
    p_i,u_i,q_i,v_i in {-1,0,1}.                   (PW.5)

Conversely a_+=p+u, a_-=u-p, b_+=q+v, b_-=v-q, so these coordinates
lose no sign pairs. Direct block multiplication gives

    a^T D(C)b=2p^T Cq,
    a^T b=2(p dot q+u dot v).

Therefore the exact half-score is

    S(a,b):=(1/2)a^T B_lambda b
           =p^T Cq-lambda(p dot q+u dot v).        (PW.6)

Put x=(p+q)/2 and y=(p-q)/2. Then x lies in [-1,1]^N. Because C is
symmetric, the cross terms cancel in the identity

    p^T Cq=x^T Cx-y^T Cy.                         (PW.7)

There is also the following exact scalar identity at every coordinate:

    2(1-x_i^2)-(1-p_i q_i-u_i v_i)
       =1-(p_i^2+q_i^2)/2+u_i v_i
       =(u_i+v_i)^2/2 >=0.                        (PW.8)

The second equality uses both relations in (PW.5); no relation between
Alice's and Bob's sign choices is imposed.

## PW-4: the global upper bound as a nonnegative gap

Use E_x from (PW.4) at x=(p+q)/2. Substituting (PW.6)--(PW.8) gives
the exact gap identity

    K-N lambda-S(a,b)
      =(K-E_x)+y^T Cy
        +sum_i (d_i-2lambda)(1-x_i^2)
        +(lambda/2)||u+v||_2^2.                  (PW.9)

To check the coefficient of lambda explicitly, the terms for coordinate i
before using (PW.8) are

    d_i(1-x_i^2)-lambda(1-p_i q_i-u_i v_i),

which equal

    (d_i-2lambda)(1-x_i^2)+(lambda/2)(u_i+v_i)^2.

This verifies both factors of two in the window and in the final score.

Every term on the right of (PW.9) is nonnegative:

- K-E_x>=0 by the finite sign completion;
- y^T Cy>=0 by PSD;
- d_i-2lambda>=0 by the registered window, and 1-x_i^2>=0; and
- lambda>=0.

It follows that S(a,b)<=K-N lambda for every original pair of full
sign vectors, hence

    beta_cl(B_lambda)<=2K-2N lambda.              (PW.10)

This upper bound covers all sign pairs, including pairs whose antipodal
coordinates have zeros. It does not replace their feasible set by only
fully antisymmetric signs.

## PW-5: matching signs and all stated boundary cases

Choose z_* in {-1,+1}^N with z_*^T Cz_*=K, and use

    a=b=(z_*,-z_*).

For this pair p=q=z_*, u=v=0, so

    a^T B_lambda a=2K-2N lambda.                  (PW.11)

This matches (PW.10) and proves (PW.3).

The proof includes the following cases without division by any matrix
entry, eigenvalue, or weight:

- Singular C: only symmetry and nonnegativity of its quadratic form are
  used, so no positive-definiteness or inverse is required.
- A zero diagonal entry: the registered interval is then just lambda=0.
  The argument proves beta_cl(D(C))=2 beta_cl(C) at that point. It makes
  no positive-width assertion in this case.
- C=0: this is the preceding case, with K=0 and value zero.
- N=1: for C=[d], d>=0, the proof gives 2d-2lambda for
  0<=lambda<=d/2; the pair a=b=(1,-1) attains it. All coordinate
  identities and the independent-sign construction remain defined.
- Both parameter endpoints: at lambda=0, terms proportional to lambda
  vanish; at lambda=min_i d_i/2, some d_i-2lambda may vanish. All
  inequalities are non-strict, so both endpoints are included.

## PW-6: status and scope

The registered universal assertion follows from the explicit finite
completion and gap identity, with matching signs. This author artifact
does not identify the largest interval for a given C or make any claim
about lambda outside (PW.1). Independent adversarial review must check
the exact canonical statement and this argument before promotion.
