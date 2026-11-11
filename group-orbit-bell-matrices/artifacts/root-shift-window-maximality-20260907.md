# Exact maximal linear-shift window for the full D_r roots

Date: 2026-09-07. Author proof for independent review.
Canonical owner: `GROTHORB.root-shift-window-maximality`.
Route: `height-one-competitor`.
Registration: `window-next-registration-20260907.md`, C17.

This artifact proves the registered iff and evaluates its explicit
competing ordered sign pair. It does not determine the full classical
envelope beyond the window, classify all endpoint optimizers, or claim
originality. No numerical tests are used.

## WM-1: exact scope and the sole registered premise

Fix an integer r>=3. Index rows by the full signed roots

    R_r={epsilon e_i+eta e_j: 1<=i<j<=r,
                             epsilon,eta in {-1,+1}},

each occurring once, in any order. Let W be their row matrix and set

    n=2r(r-1),    A_r=WW^T/[4(r-1)],
    B_r=2r(2r-1)/3,    lambda_*=1/[2(r-1)].

For any square real matrix M, beta_cl(M)=max_(a,b) a^T M b over
ordered sign pairs of the matching size.

The sole project-theorem premise is `GROTHORB.root-extended-shift-window`:

    beta_cl(A_r-lambda I_n)=B_r-n lambda
    for every 0<=lambda<=lambda_*.                 (WM.1)

Its complete proof is `root-extended-shift-window-20260907.md`, RW-1
through RW-4. Its applicable independent report is
`../reviews/psd-antipodal-window-review-20260907.md`, F2 for that precise
claim and F3 for its separately checked assembly. The current premise
node records PROVED, with claim reviewed hash
`sha256:df62de9a7c9c2c2dd4e5512ea89a3374d63f3c3bbb6e6d41f4eff509732f05db`.
The proof and applicable report were read in full for this author task;
the review discloses author/reviewer role separation within the same model
family and shared context, not fresh-context or cross-model independence.

The premise supplies only (WM.1). The strict obstruction for every
lambda>lambda_* is proved directly below, not inferred from a previous
finite-dimensional envelope or from the sufficient-window status.

## WM-2: a baseline sign pattern and an explicit height-one root

Let

    rho=(r-1,r-2,...,1,0),
    Q=||rho||_2^2=(r-1)r(2r-1)/6,

and define the baseline sign s^0 on a row w=epsilon e_i+eta e_j,
i<j, by s^0_w=epsilon. For a fixed pair i<j,

    sum_(epsilon,eta) epsilon(epsilon e_i+eta e_j)=4e_i.

Summing over coordinate pairs gives, independently of their row order,

    W^T s^0=4rho,
    (s^0)^T A_r s^0=16Q/[4(r-1)]=B_r.             (WM.2)

Choose the particular positive root

    h=e_(r-1)-e_r.

Both h and -h occur exactly once among the full roots. Since the last
two coordinates of rho are 1 and 0,

    rho dot h=1,    ||h||_2^2=2.                  (WM.3)

Thus the required height-one property is verified explicitly for every
r>=3, without presuming a root-system classification result.

## WM-3: the ordered competitor and its exact full score

Define Alice's sign a and Bob's sign b as follows:

    a_w=s^0_w for w!=-h,    a_(-h)=+1;
    b_w=s^0_w for w!= h,    b_h=-1.                (WM.4)

At these two roots the values are

| Root row | Baseline s^0 | Alice a | Bob b |
|---|---:|---:|---:|
| h | +1 | +1 | -1 |
| -h | -1 | +1 | -1 |

At every other row a_w=b_w=s^0_w. These definitions are unambiguous
sign vectors in every row order. Relative to the baseline, Alice flips
only the -h row and Bob flips only the h row. Consequently

    W^T a=4rho+2(-h)=4rho-2h,
    W^T b=4rho-2h.                                (WM.5)

The two sign vectors agree on n-2 coordinates and have opposite signs
on the two displayed rows, so

    a dot b=(n-2)-2=n-4.                          (WM.6)

Using the Gram normalization, (WM.3), and (WM.5),

    a^T A_r b
       =||4rho-2h||_2^2/[4(r-1)]
       =[16Q-16(rho dot h)+4||h||_2^2]/[4(r-1)]
       =(16Q-8)/[4(r-1)]
       =B_r-2/(r-1).                             (WM.7)

Together with (WM.6), this gives the exact score, for every lambda>=0,

    a^T(A_r-lambda I_n)b
       =B_r-2/(r-1)-lambda(n-4)
       =B_r-n lambda+4lambda-2/(r-1).             (WM.8)

This is a score of one feasible ordered pair, not an asserted value of
the full optimum beyond the window.

## WM-4: check against the registered antipodal coordinates

To make the route's coordinate prescription explicit, put N=r(r-1).
Take U to list e_i-e_j and e_i+e_j for i<j, and order the full roots
temporarily as W_hat=[U;-U]. Let k denote the U row containing h, and
let E_k be the kth standard coordinate vector in R^N. In this order,
(WM.4) is

    a_+=1_N,          a_-=-1_N+2E_k,
    b_+=1_N-2E_k,     b_-=-1_N.

Its antisymmetric and symmetric coordinates are therefore exactly

    p=(a_+-a_-)/2=1_N-E_k,
    u=(a_++a_-)/2=E_k,
    q=(b_+-b_-)/2=1_N-E_k,
    v=(b_++b_-)/2=-E_k.                           (WM.9)

Thus both antisymmetric coordinates vanish at k, and the symmetric signs
there are opposite, as proposed in the registered route. All other
coordinates have the original fully antisymmetric positive pattern.

For an additional direct normalization identity, set C=UU^T/[2(r-1)]
and A_hat=W_hat W_hat^T/[4(r-1)]=(1/2)[C,-C;-C,C]. Summing the two U
rows over each pair gives U^T1_N=2rho; hence

    U^T p=2rho-h,
    p^T Cp=||2rho-h||_2^2/[2(r-1)]
           =B_r/2-1/(r-1),
    p dot q+u dot v=(N-1)-1=N-2.

Direct block multiplication consequently gives

    a^T(A_hat-lambda I_n)b
       =2[p^T Cq-lambda(p dot q+u dot v)],

which is precisely (WM.8). These identities are derived here and do
not use a separate generic duplication theorem as an undeclared premise.

For an arbitrary original row order, W=P W_hat for a permutation matrix
P. Applying P simultaneously to both sign vectors preserves their score
because A_r=P A_hat P^T and P I_n P^T=I_n. This agrees with the
row-label definition (WM.4).

## WM-5: all parameters, the endpoint, and the iff

Subtracting the affine value from (WM.8) gives

    a^T(A_r-lambda I_n)b-(B_r-n lambda)
       =4lambda-2/(r-1)=4(lambda-lambda_*).        (WM.10)

For every lambda>lambda_* this difference is strictly positive. Since
the classical optimum is at least the score of any feasible pair,

    beta_cl(A_r-lambda I_n)>B_r-n lambda
    for every lambda>lambda_*.                    (WM.11)

There is no upper restriction on lambda in this argument. In particular,
the witness excludes a later return to the affine formula, even where
the witness itself may no longer be an optimal pair.

For 0<=lambda<=lambda_*, the unique registered premise (WM.1) gives
the equality. Combining (WM.1) and (WM.11) proves the exact assertion
among lambda>=0:

    beta_cl(A_r-lambda I_n)=B_r-n lambda
       if and only if lambda<=1/[2(r-1)].         (WM.12)

At lambda=lambda_* the gap (WM.10) is zero and the sufficient-window
premise includes that endpoint. The explicit competitor also attains the
known endpoint value, but no classification of all endpoint pairs is
claimed here.

For r=3 all indices remain distinct and the chosen root is h=e_2-e_3.
Here n=12, B_r=10, lambda_*=1/4, and the competitor score (WM.8)
is 9-8lambda. Its difference from 10-12lambda is 4lambda-1, strictly
positive exactly above 1/4. This is a substitution into the all-r proof,
not a numerical test or an appeal to the separately known D3 envelope.

## WM-6: evidence and scope boundary

The argument establishes both the full C17 claim and its registered
`height-one-competitor` implication, using only the reviewed sufficient
window and the explicit computations above. It does not compute
beta_cl(A_r-lambda I_n) for lambda beyond the endpoint; there it supplies
only a strict competing lower bound sufficient to disprove the affine
formula. It adds no external theorem or unregistered premise.

This is an author proof, not its own independent correctness verdict.
The exact new claim and route implication require an author-independent
review before promotion. Existing nodes, proofs, and reviews are unchanged.
