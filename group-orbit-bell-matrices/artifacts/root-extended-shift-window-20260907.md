# The full D_r root linear-shift window from PSD duplication

Date: 2026-09-07. Author route assembly for independent review.
Canonical owner: `GROTHORB.root-extended-shift-window`.
Route: `psd-duplication-window`.
Registration: `classical-family-registration-20260907.md`, C16.

## RW-1: registered premises and review status

The assembled implication uses exactly the two registered premises:

1. `GROTHORB.psd-antipodal-linear-window`: for a real symmetric PSD
   N by N matrix C and D(C)=(1/2)[C,-C;-C,C],
   beta_cl(D(C)-lambda I_(2N))=2 beta_cl(C)-2N lambda whenever
   0<=lambda<=min_i C_ii/2. Its author proof is
   `psd-antipodal-linear-window-20260907.md`, PW-1 through PW-5.
2. `GROTHORB.root-classical`: for the full D_r signed roots and
   A_r=WW^T/[4(r-1)], beta_cl(A_r)=2r(2r-1)/3. Its proof is
   `root-classical-value-20260907.md`, RC-1 through RC-4.

The generic window premise is unreviewed at authoring. The algebra below
establishes the registered implication conditional on that premise; it
does not promote the parent or treat an unreviewed premise as reviewed.
No extra duplication theorem or dimension-specific computation is used.

## RW-2: positive half-roots and the exact block normalization

Fix r>=3 and put N=r(r-1), n=2N. Let U be the N by r matrix with
the two rows e_i-e_j and e_i+e_j for every 1<=i<j<=r. Define

    W_hat=[U;-U],
    C=UU^T/[2(r-1)].                              (RW.1)

Every full signed root epsilon e_i+eta e_j occurs exactly once among
these rows: the roots with epsilon=+1 occur in U, and those with
epsilon=-1 occur in -U. Thus for W in the canonical claim there is a
permutation matrix P with W=P W_hat. Consequently

    A_r=P A_hat P^T,
    A_hat=W_hat W_hat^T/[4(r-1)]
         =(1/2)[ C -C; -C C ]=D(C).              (RW.2)

The matrix C is symmetric PSD because it is a positive scalar multiple
of a real Gram matrix. Every U row has squared norm two, so

    C_ii=2/[2(r-1)]=1/(r-1) for all i.            (RW.3)

In particular the generic premise applies on exactly the sufficient
interval

    0<=lambda<=1/[2(r-1)].                        (RW.4)

Simultaneous permutation does not change a classical value: as s,t range
over signs, P^T s,P^T t range over the same full sign sets. Also
P I_n P^T=I_n. Thus for every real lambda,

    beta_cl(A_r-lambda I_n)
       =beta_cl(D(C)-lambda I_(2N)).              (RW.5)

## RW-3: assemble the two premises

Applying the generic premise at lambda=0 and then the base root premise
gives

    2 beta_cl(C)=beta_cl(D(C))=beta_cl(A_r)
               =2r(2r-1)/3.                     (RW.6)

For lambda in (RW.4), apply the same generic premise, (RW.5), and
2N=n to obtain

    beta_cl(A_r-lambda I_n)
       =2 beta_cl(C)-2N lambda
       =2r(2r-1)/3-n lambda.                      (RW.7)

This proves the registered route implication, including both endpoints,
with the exact positive-half/full-root scaling.

## RW-4: an explicit witness and scope

The matching signs can also be written without finding an optimizer of C.
In the order W_hat=[U;-U], use s=t=(1_N,-1_N). For
rho=(r-1,r-2,...,0), summing the two U rows over each coordinate pair
gives U^T1_N=2rho. Therefore

    W_hat^T s=4rho,
    s^T A_hat s=16||rho||_2^2/[4(r-1)]
               =2r(2r-1)/3,
    s^T(A_hat-lambda I_n)s=2r(2r-1)/3-n lambda.

Here ||rho||_2^2=(r-1)r(2r-1)/6. For the arbitrary row order of W,
use the simultaneously permuted pair Ps,Ps. Equivalently, the sign
assigned to the root epsilon e_i+eta e_j with i<j is epsilon. The
generic theorem supplies the global upper bound over all competing pairs.

This artifact asserts a sufficient all-r interval, not that its endpoint
is maximal for each r. It neither revives the refuted whole-interval
extrapolation nor makes a novelty claim. Independent review must check
the generic premise and this exact normalization assembly before a
completion-level assessment of the parent.
