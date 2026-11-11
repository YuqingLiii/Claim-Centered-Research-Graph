# Quantitative Holevo pair-to-self reduction — 2026-08-29

Canonical node: `HEXT.pair-to-self`.

This note gives the full proposer-side derivation. It is not a completion-tier proof until an
independent rule-6/7 review has been archived.

All logarithms are base two. For a finite-dimensional channel `Phi`, write `chi(Phi)` for its
one-shot Holevo quantity and `C(Phi)=sup_n chi(Phi^tensor-n)/n` for its unassisted classical
capacity.

## 1. Flagged direct sums

For channels `A:B(H_A)->B(K_A)` and `B:B(H_B)->B(K_B)`, define the flagged direct sum

`T=A direct-sum B`

on `H_A direct-sum H_B` by deleting the off-diagonal input blocks and applying the corresponding
channel to each diagonal block. Its output lies in `K_A direct-sum K_B`, so the branch is perfectly
distinguishable.

Let `x=chi(A)` and `y=chi(B)`. Then

`chi(A direct-sum B)=log(2^x+2^y)`.                                           (1)

More generally, the identical branch-entropy argument for any finite family
`T_1,...,T_K` gives the finite-`K` form

`chi(direct-sum_(i=1)^K T_i)=log(sum_(i=1)^K 2^chi(T_i))`.                    (1a)

Indeed, for branch weights `q_i` the Holevo quantity is at most
`H(q)+sum_i q_i chi(T_i)`, and the Gibbs variational identity maximizes this at
`q_i=2^chi(T_i)/sum_j 2^chi(T_j)`. Mixing near-optimal within-branch ensembles
approaches equality. Thus the later use of `K` identical summands is not an induction from the
binary formula; it is the same finite-family identity.

### Upper bound in (1)

For any ensemble `{p_i,rho_i}`, let `q_i` be the trace of the `A` input block and let `qbar` be its
average. Conditional on a nonzero branch weight, normalize the two diagonal input blocks. The
output entropy of state `i` is

`h(q_i)+q_i S(A(rho_i^A))+(1-q_i)S(B(rho_i^B))`.

Applying the same block-entropy formula to the average output and subtracting gives

`Holevo(output ensemble)`

`= h(qbar)-sum_i p_i h(q_i) + qbar chi(E_A)+(1-qbar)chi(E_B)`

`<= h(qbar)+qbar x+(1-qbar)y`.

The last expression is maximized at `qbar=2^x/(2^x+2^y)` and its maximum is
`log(2^x+2^y)`.

### Achievability in (1)

Use near-optimal ensembles supported entirely in one input branch, mixing the `A` ensemble with
probability `q` and the `B` ensemble with probability `1-q`. Then every `q_i` is zero or one, so
the negative binary-entropy term vanishes. Optimizing `q` and taking the near-optimal limit reaches
the upper bound. This also handles channels whose Holevo suprema are expressed as suprema rather
than preselected maximizers.

## 2. Exact balancing by a classical side channel

Let `Delta_K` be the noiseless `K`-symbol classical channel, represented as complete dephasing in
a fixed basis. Because `A tensor Delta_K` is a flagged direct sum of `K` copies of `A`, (1a) gives

`chi(A tensor Delta_K)=chi(A)+log K`.                                         (2)

Suppose initially `x=chi(N)<=y=chi(M)` and put

`K=ceil(2^(y-x))`, `N'=N tensor Delta_K`, `x'=chi(N')`.

Then `y<=x'<y+1`. If `y<x`, apply the same construction to `M` instead. Moreover (2), now applied
to the whole pair, shows that the cross defect is unchanged:

`chi(N' tensor M)-chi(N')-chi(M)`

`=chi(N tensor M)+log K-[chi(N)+log K]-chi(M)`

`=g`.                                                                         (3)

Thus after relabelling we may assume `|x'-y|<1` without changing `g`.

## 3. The two-copy same-channel defect

Set `T=N' direct-sum M`, `a=2^x'`, and `b=2^y`. Applying (1) gives

`2^(2chi(T))=(a+b)^2`.                                                        (4)

The channel `T tensor T` is the flagged direct sum of the four channels

`N' tensor N'`, `N' tensor M`, `M tensor N'`, `M tensor M`.

Ordinary product ensembles give

`chi(N' tensor N')>=2x'`, `chi(M tensor M)>=2y`,                              (5)

and (3), together with swap symmetry, gives

`chi(N' tensor M)=chi(M tensor N')=x'+y+g`.                                  (6)

Using (1) on the four branches and then (5)-(6),

`2^chi(T tensor T) >= a^2+2ab 2^g+b^2`.                                      (7)

Divide (7) by (4) and define

`w=2ab/(a+b)^2`.

Then

`chi(T tensor T)-2chi(T) >= log[1+w(2^g-1)]`.                                (8)

The balancing step ensures `a/b` lies between `1/2` and `2`. The minimum of
`2r/(1+r)^2` on that interval is `4/9`, so

`w>=4/9`.                                                                     (9)

Equations (8)-(9) imply both

`chi(T tensor T)-2chi(T) >= log[1+(4/9)(2^g-1)] > 0` for every `g>0`,          (10)

and the simpler extensive-scale estimate

`chi(T tensor T)-2chi(T) >= g-log(9/4)`.                                     (11)

The latter follows from `1+w(2^g-1)>=w2^g>=4*2^g/9`.

### Symmetric-pair corollary

If the original pair already satisfies `chi(N)=chi(M)`, no classical balancing channel is needed.
Taking `T=N direct-sum M` gives `a=b` and hence `w=1/2` exactly. Equation (8) becomes

`chi(T tensor T)-2chi(T) >= log[1+(1/2)(2^g-1)] >= g-1`.                 (11a)

The conjugate pair produced by the product-Haar construction and the Weyl-flag transfer has equal
one-shot Holevo quantities, so (11a), rather than the weaker general bound (11), is the applicable
constant-loss estimate for that family.

## 4. Capacity consequence

By the regularized definition and superadditivity of the Holevo sequence,

`C(T)>=chi(T tensor T)/2`.

Therefore

`C(T)-chi(T) >= (1/2)log[1+w(2^g-1)]`

`>= (1/2)[g-log(9/4)]`.                                                       (12)

The exact first expression in (12) is strictly positive for every positive pair defect, even when
the coarser second expression is negative.

In the symmetric case, the corresponding simpler estimate is

`C(T)-chi(T) >= (1/2)(g-1)`.                                               (12a)

## 5. Dimension bookkeeping

The classical balancing factor obeys

`log K < |chi(N)-chi(M)|+1`.

Since `chi(Phi)<=log(dim output(Phi))`, its extra input and output qubit cost is at most linear in
the original logarithmic dimensions. The final direct sum adds at most one further qubit beyond
the larger balanced branch, up to the usual ceiling convention. Hence a family with pair defect
`g_m=Omega(m)` and all original logarithmic dimensions `O(m)` becomes a family with
`C(T_m)-chi(T_m)=Omega(m)` and logarithmic dimensions still `O(m)`.

## 6. Scope and remaining obstruction

This reduction is purely about the Holevo quantity. It does not identify a large pair defect and it
does not authorize replacing a minimum-output-entropy witness by a pointwise Holevo witness without
the separate quantitative extension used in the literature. Its value is to show that the
same-channel requirement costs only `O(1)` bits once an extensive Holevo pair defect is available.

The live obstruction is therefore the construction of an extensive finite-dimensional `p=1` pair
defect, not the pair-to-self conversion.
