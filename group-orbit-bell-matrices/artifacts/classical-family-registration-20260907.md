# Classical orbit-family registration, 2026-09-07

The user requested continuous research until explicitly stopped. This round
prioritizes the classical denominator for the already defined full D_r root
projection A_r=WW^T/[4(r-1)], n=2r(r-1).

## C1: base classical value

Register the candidate beta_cl(A_r)=2r(2r-1)/3, where
beta_cl(B)=max_{s,t in {+1,-1}^n} s^T B t. Prove both the global upper
bound and an explicit sign witness; do not infer the theorem from small r.

## C2: shifted family and a testable plateau proposal

Investigate B_r(lambda)=A_r-lambda I, 0<=lambda<=1/2. The spectral numerator
is already obtainable from the projection and transitive theorem. The
specific proposed classical formula beta_cl(B_r(lambda))=2r(2r-1)/3-n*lambda
for every r>=3 and the whole interval is a conjectured route, not an assumed
fact. Find exact counterexamples or a proof, preserving failures.

## C3: exact D3 envelope algorithm

Register an exact finite method for r=3: enumerate all Bob sign vectors t,
compute sum_i |(A_3 t)_i-lambda t_i| as rational piecewise-affine functions,
then compute their upper envelope on [0,1/2]. The algorithm must include all
signs (or a proved symmetry quotient), all breakpoints and matching witnesses.
The resulting formula is a new statement to freeze and review once computed.

## C4: literature boundary

Compare the full-root projection, antipodal duplication, shifts, and classical
certificate techniques to root-system Bell and zonotope literature. A correct
formula or a small-instance computation does not by itself establish novelty.

## C5: classical equality pattern

Register the all-r statement that every maximizing pair at lambda=0 is
diagonal s=t and is given by signs of w dot g rho, where rho=(r-1,...,0)
and g is a signed coordinate permutation. The proposed number of distinct
maximizers is 2^(r-1) r!. This must be established before using it to rule
out zero-length shift plateaus.

## C6: conservative uniform shift interval

Register beta_cl(A_r-lambda I)=2r(2r-1)/3-n lambda for
0<=lambda<=1/[2n(r-1)]. The intended route combines C1, C5 and the exact
classical value lattice at lambda=0. This much smaller interval is an
alternative to C2; a counterexample to C2 does not refute C6.
# C7. Exact D3 parameter envelope

Registered 2026-09-07 after the exploratory output of the previously registered
finite method C3, and before treating its formula as an established result.
Node GROTHORB.d3-shift-envelope claims beta(A3-lambda I)=10-12 lambda on
[0,1/4] and 8-4 lambda on [1/4,1/2].
The author reports all 4096 Bob signs enumerated with exact rational arithmetic.
This registration is not a proof or independent verification.
# C8. General antipodal duplication versus shift

Node GROTHORB.antipodal-shift-comparison registers the exact ternary identity
and the lower comparison beta(D(C)-lambda I)>=2 beta(C-lambda I), with
equality at lambda=0, for arbitrary real square C and lambda>=0.
The blueprint was first written during normalization checks in the source
note, L3; the substantive general statement is registered here before testing
or downstream reliance. No novelty is claimed.

# C9. Half-root D3 comparison point

Node GROTHORB.d3-half-shift-value registers beta(UU^T/4-I_6/3)=3 for the
six specified positive D3 roots. It is suggested by the checked literature
normalization and is not a novel prediction. The local exact upper bound and
explicit witness must be independently certified. Comparing it to the full-root
envelope will test whether shifted duplication is harmless in this instance.
# C10. A strict shifted-duplication gap

GROTHORB.shift-duplication-gap records the testable comparison at lambda=1/3:
full D3 beta=20/3 versus twice half D3 beta=6. Its exact-comparison route
depends on C7 and C9, with the simultaneous full-root ordering explicitly
verified. It does not refute any valid unshifted duplication identity.
# C11. Weighted isotropic orbit unions

GROTHORB.weighted-isotropic-optimum is a next-round candidate beyond a
single transitive orbit. It states the exact vector optimum S*T/r for
M_ij=u_i v_j a_i dot b_j when the two positive weighted unit frames are
isotropic. The aim is a usable rectangular/multi-orbit interface, not a
claim of novelty. A weighted Cauchy--Schwarz or diagonal SDP dual argument
must be supplied and compared with existing work before promotion.
# C12. Exact setting economy in the weighted isotropic framework

GROTHORB.minimum-settings-isotropic proposes minimum m+n=r(r+1)/2+1
for two positive weighted isotropic unit frames whose combined quadratic
map is injective on Sym_r. The explicit registered candidate uses Alice
coordinate vectors with unit weights, Bob normalized coordinate differences
with weight 2/r, and one normalized all-ones vector with weight 1.
The lower-count mechanism is the common weighted trace relation.
This is a framework-scoped setting-economy question, not a claim about
the smallest possible arbitrary Bell experiment or physical self-testing.
The construction, lower bound, and novelty must be checked separately.
# C13. Conditioning at a minimal setting budget

GROTHORB.minimal-setting-conditioning registers a quantitative next question
after the bare setting-count construction was found to have prior-art
counterparts. For normalized positive weighted frames with combined
injectivity and m+n=r(r+1)/2+1, the proposed upper bound on the smallest
traceless quadratic-measurement eigenvalue is
(r-1)/max(m-1,n-1). This eigenvalue controls an algebraic conditioning
question; no operational noise or self-testing statement follows merely
from this registration. A proof, sharpness study, and prior-art review
remain separate obligations. Register any stronger equality criterion
before attempting it.
# C14 — Equality in the minimal-setting conditioning bound

Registered 2026-09-07 before author assignment or testing of this claim.
Owner: `GROTHORB.minimal-conditioning-equality`.
Freeze the complete self-contained node claim: with m>=n and the C13
normalized positive-frame domain and minimum total setting budget,
attainment of c=(r-1)/(m-1) is proposed to be equivalent to equal Alice
weights r/m, Alice squared pair overlaps (m-r)/(r(m-1)), all cross squared
overlaps 1/r, and Bob's centered operator having eigenvalues at least c
on its range. Author must check both directions and all boundary cases.
This does not claim existence, a sharp optimum in every dimension, a
physical noise guarantee, or novelty relative to tight-frame literature.
# C15 and C16 — PSD antipodal linear window and its D_r consequence

Registered 2026-09-07. The general C15 candidate arose from exploratory
algebra in antipodal/symmetric coordinates; it is registered here before
separate checking, computational tests, or use as a proved premise. No
earlier registration or independently verified proof is claimed.

`GROTHORB.psd-antipodal-linear-window` proposes that for every real PSD
C and D(C)=(1/2)[C,-C;-C,C], the full classical value is
2 beta_cl(C)-2N lambda whenever 0<=lambda<=min diag(C)/2. The proposed
upper-bound route uses mean-sign random completion and PSD quadratic
forms; degeneracies and all factors require adversarial review.

`GROTHORB.root-extended-shift-window` registers the dependent consequence
for the full signed D_r roots: C=UU^T/[2(r-1)] has diagonal 1/(r-1),
so the putative new sufficient interval is [0,1/(2(r-1))]. Its route
explicitly requires C15 and the audited unshifted full-root formula.
Neither registration claims that the interval is always maximal, that
full/half duplication is harmless beyond it, or that this is original.
The earlier failed unrestricted linear extrapolation is not revived.
