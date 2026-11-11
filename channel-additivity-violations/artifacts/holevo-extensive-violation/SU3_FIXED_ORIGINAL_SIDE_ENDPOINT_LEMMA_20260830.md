# Fixed-original-side endpoint reduction lemma

Date: 2026-08-30

Status: proposer-side exact argument; independent review pending.

## Statement

Fix one labelled finite union of elementary `SU(3)` Pieri face channels in which every pair of
distinct input blocks shares at most one environment block.  (The exact incidence audit verifies
this condition for all 11 connected three-distinct-face classes.)  Write the channel's direct-sum
input-block simplex weights as `lambda=(lambda_i)_i`, and let `R` be a nonempty set of blocks whose
weights remain continuous.  For each block outside `R`, independently replace its simplex weight
by a vertex, producing an endpoint pattern `e` while keeping all weights in `R` unchanged.

Let `t(lambda)` be the conjugate-Bell isotropic Gram parameter and let `q_r(lambda_r)` be an
explicit output distribution obtained by feeding the registered block-highest input into retained
block `r`.  If, for every allowed representation label and retained weight tuple, the endpoint
calculation certifies `0<=T:=max_e t_e<1` and

`B(max_e t_e) > 2 min_(r in R) H(q_r)`, 

then the original channel obeys

`S((Phi tensor barPhi)(Omega)) > 2 S_min(Phi)`

for all weights in every block.  Here `B(t)` is the entropy of the qutrit isotropic spectrum
`((1+8t)/9,(1-t)/9,...,(1-t)/9)`.

## Proof

Because two distinct inputs share at most one environment, each off-diagonal Hilbert--Schmidt
term contains an absolute squared edge amplitude.  Arbitrary edge phases therefore disappear.

Each diagonal block is a chi-square form and each shared-environment coefficient is the squared
Hilbert--Schmidt overlap of the corresponding Clebsch--Gordan blocks.  Hence `t(lambda)>=0`.

For one eliminated block with all other weights fixed, the Gram parameter is a positive diagonal
quadratic form in that block's simplex weights plus an affine term.  It is therefore convex on the
simplex.  Its maximum is attained at a vertex.  Repeating this one block at a time gives

`t(lambda) <= max_e t_e`

without breaking any shared-environment cross terms: the *same endpoint pattern* is used in the
complete Gram expression.

The endpoint certificate supplies `t(lambda)<=T<1`.  Direct differentiation gives

`B'(t)=-(8/9) log((1+8t)/(1-t)) <= 0`.

Consequently `B(t(lambda)) >= B(max_e t_e)`.

For each retained block, `q_r(lambda_r)` is the output of the **original channel with its original
weights** on a legal block-highest input.  Hence

`S_min(Phi) <= H(q_r(lambda_r))`

for every retained `r`, and therefore `S_min(Phi) <= min_r H(q_r)`.  Combining the three
inequalities proves the claim.

## Quantifier warning

Endpoint patterns are replacement channels used only to upper-bound the original Gram parameter.
Their side outputs are not, in general, outputs of the original channel.  Thus an
endpoint-pattern-dependent side entropy cannot replace `H(q_r(lambda_r))` above.  The exact
large-label failure in
`SU3_INPUT_CENTERED_TRIANGLE_FIXED_THREE_COVER_FAILURE_20260830.md` records why that invalid repair
reverses the necessary quantifier order.

The phase-incidence condition is reproduced by
`holevo-extensive-violation/tools/audit_su3_three_face_phase_independence.py`.
Exact nonnegativity of the three elementary shared-environment coefficients is reproduced by
`holevo-extensive-violation/tools/audit_su3_cross_coefficient_positivity.py`: after multiplication
by the positive common denominator `8 dim(E)`, every coefficient of each sparse `p,q` polynomial
is nonnegative.
