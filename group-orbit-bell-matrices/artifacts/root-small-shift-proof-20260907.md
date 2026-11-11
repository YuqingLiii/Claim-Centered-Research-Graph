# Conservative exact small-shift interval for full D_r roots

Date: 2026-09-07. Author: parent research agent /root.
Target: GROTHORB.root-small-shift, route discrete-gap.
This is an author proof awaiting an independent review of the assembled argument.
It claims a sufficient interval only, not the maximal interval of this formula.

## S1. Objects and dependency boundary

Let r>=3, n=2r(r-1), and let W contain once each of the full roots
alpha e_i+beta e_j, i<j, alpha,beta in {-1,1}. Put
A=WW^T/[4(r-1)], C=2r(2r-1)/3, and let s,t be sign vectors of length n.
We use exactly the following separately registered premises:

1. GROTHORB.root-classical: s^T A t<=C and some pair s=t attains C.
2. GROTHORB.root-classical-equality: every pair attaining C has s=t.

The stronger orbit classification and count in premise 2 are not needed for this
implication, but that full stated premise must be proved before node promotion.
No claim about minimum physical Hilbert-space dimension or improved record
Grothendieck bounds is made here.

## S2. Exact score lattice

For each coordinate k, precisely 4(r-1) roots have nonzero kth coordinate,
which is +1 or -1. Thus (W^T s)_k is a sum of an even number of signs and
is an even integer. The same holds for W^T t. Consequently

  s^T A t = ((W^T s) dot (W^T t))/[4(r-1)] belongs to (1/(r-1)) Z.

The number C also lies in this lattice: C(r-1)=2r(r-1)(2r-1)/3 is an
integer, since one of r, r-1, or 2r-1 is divisible by 3.
Alternatively its membership follows from any exact attaining sign pair.
If s!=t, premise 2 excludes equality at C. Premise 1 and the lattice then give

  s^T A t <= C - 1/(r-1).                                      (S2.1)

## S3. Uniform comparison of all pairs

If s=t, then

  s^T (A-lambda I) s <= C-n lambda.

For s!=t and lambda>=0, use s dot t>=-n and (S2.1):

  s^T (A-lambda I) t <= C-1/(r-1)+n lambda.

Whenever 2n lambda<=1/(r-1), the latter is also at most C-n lambda.
A diagonal sign pair attaining C at lambda=0 still attains C-n lambda.
Maximizing over all pairs therefore proves

  beta_cl(A-lambda I)=C-n lambda
  for 0<=lambda<=1/[2n(r-1)]=1/[4r(r-1)^2].

This argument includes both endpoints and permits extra tying pairs at the
right endpoint. It does not identify all shifted equality pairs or imply the
formula outside this interval.

## S4. Audit and reproduction

The all-r argument above is finite algebra, not inferred from sampled ranks.
The root-classical checker supplies reproducible exact attaining signs, while
the equality proof is a separate load-bearing premise.
For r=3 the sufficient interval ends at 1/48. The independently registered
full D3 envelope may yield a longer interval; that does not strengthen the
general statement without a separate argument.
