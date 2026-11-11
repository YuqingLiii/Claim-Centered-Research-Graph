# Remaining full-size frontier after the 2026-08-30 reductions

Date: 2026-08-30

Status: research routing note; not a mathematical completion claim.

## What is now closed as a route

1. **Single LLW/BCN-style isotropic Bell layer with a growing output spike.** The Bell certificate
   is uniformly at most one bit for every isotropic parameter. The special `t=c/k^2` calculation
   gives the sharper cap `h_2(1/c)`.
2. **Uniform finite-group twirl label collisions.** The side channel is a conditional expectation
   and MOE is exactly additive.
3. **Fixed-dimension iid Haar layers.** Approximate conjugate matching creates within-side Bell
   leakage that defeats the Collins--Youn side rate.
4. **Changing iid to an oriented, adaptive, or deterministic fixed-dimensional layer sequence.**
   Arbitrary heterogeneity is bounded by fixed-channel regularization; a positive product-Bell
   rate selects one fixed finite regularized counterexample.
5. **Using the published fixed-depth tensor strong-convergence rate as a full-size certificate.**
   Its matrix-dimension cost makes the current lower bound subextensive.
6. **Simple visible erasure, finite-subspace truncation, uniform additive bounds, and the checked
   Temperley--Lieb candidate.** Each has an explicit obstruction or an unproved global-minimum gate
   recorded in its own node.

“Closed” here means the named proof strategy does not establish full-size extensivity under its
current hypotheses. It is not an impossibility theorem for all channels.

## Ranked live targets

### 1. One fixed finite regularized pair

Find a finite channel `Phi` such that

\[
 \overline S_{\min}(\Phi)+\overline S_{\min}(\bar\Phi)
 >\overline S_{\min}(\Phi\otimes\bar\Phi).
\]

The stronger Bell-certified sufficient condition is

\[
 2\overline S_{\min}(\Phi)
 >S((\Phi\otimes\bar\Phi)(\Omega)).
\]

This is the highest-leverage target: tensor powers immediately give a full-size extensive family,
and every compact fixed-dimensional heterogeneous product-Bell route now reduces to it.

It now has a state-level necessary pre-screen. For the Gram channel
`Theta=(k/d)Phi Phi^*`, let `sigma_BE` be its maximally mixed Stinespring output. Tensorizing the
hidden-correlation identity gives
`2 barS_min(Phi)-S(Z) <= 2E_C(sigma_BE)-S(E)`. Hence a candidate cannot work through the Bell
certificate unless `E_C(sigma_BE)>S(E)/2`. Passing this entanglement-cost gate is not sufficient;
the global all-copy side entropy bound remains necessary.

### 2. Physical-output-specific all-copy inequality

For one successful finite product-Haar block, control all tensor powers of its complementary
channel on the restricted coefficient matrices that actually arise from density operators. The
general completely bounded approximation shortcut is impossible, but the physical subset may be
smaller than the adversarial matrix-coefficient ball.

The target has now been sharpened. For a fixed successful block, write `C_J=L_J^c`, `q=m^J`, and

\[
 A_{J,\eta}=1+(1+\eta)^2((1+9/m)^J-1).
\]

It suffices to prove, for every `n>=1`,

\[
 \sup_\rho \operatorname{Tr}[C_J^{\otimes n}(\rho)^2]
 \le (A_{J,\eta}/q)^n.
\]

This gives regularized pair defect at least
`J log_2(m)/m-2 log_2(A_{J,eta})`, which is positive for `ln(m)>18` and sufficiently small `eta`.
The claim is only about physical outputs of one selected finite tuple, not arbitrary matrix-level
coefficients. It is therefore narrower than the already-refuted uniform completely bounded
shortcut. It remains OPEN in node `HEXT.product-haar-physical-self-purity-multiplicativity`.

Montanaro's Haar-random-subspace theorem cannot supply this estimate: the product-random-unitary
Stinespring projectors form a singular ensemble with exactly maximally mixed partial trace. Even a
fictitious application gives only half the needed entropy rate, and its deterministic PPT
relaxation obeys the exact floor `||P_J^Gamma||_infty>=m^(-J/2)`.

At the first nontrivial copy number, every input separable across the two repeated uses already
satisfies the target. Simultaneously real/orthogonal tuples are independently proved to fail by a
Bell collision. The same exact lower bound `2/q^2-1/q^3` now independently covers every complex
tuple closed under entrywise conjugation up to a permutation and phases. Exact conjugation closure
is a special dependent, measure-zero subclass and does not refute the generic independent-Haar
existential route. Generic complex-Haar tuples behave differently: their one-layer Bell frame
potential has exact mean
`m^2+(m^4-m^2)/d^2+2m(m-1)/(d(d+1))`, giving Bell-failure probability `O(m^3/d^2)` at fixed `m`.
The live `n=2` target is therefore the full pure-entangled-input physical Gram supremum, not the
Bell vector alone; passing that case would still leave every `n>=3`.

Three elementary global routes are now quantitatively blocked. A pure-state epsilon net costs
`exp(Theta(d^2 log m))` against only `exp(-Theta(d/m^5))` standard Haar tails; the unrestricted
replica operator norm is deterministically at least `(2-1/m)/m^2`, above the target in the intended
small-eta regime; and the sharper symmetric-bosonic DPS/de Finetti control still needs extension
level much larger than `m^3 d^2` (the older ordinary permutation-invariant estimate gives the
valid but non-sharp `m^3 d^4`). Exact output duality avoids all three: it replaces the input sphere
by a Hermitian
coefficient sphere of real dimension `m^4`. The precise remaining n=2 lemma is
`HEXT.same-tuple-two-leg-scalar-strong-norm`; it is OPEN and is not the independent-leg tensor
strong-convergence theorem already in the project.

For arbitrary copy number the physical target has an independently proved exact reformulation.
With `C_J=D_0+E`, trace-annihilation of `E` makes the subset terms Hilbert--Schmidt orthogonal and
gives

`Tr[C_J^(tensor n)(rho)^2]=sum_S q^(-(n-|S|))||E^(tensor |S|)(rho_S)||_2^2`.

At `n=3`, direct summation of all one- and two-copy marginal inequalities contains no coefficient
for the new fully centered three-body term. Thus the naive marginal induction does not close; the
remaining theorem must control connected physical correlations uniformly at every order. This
exact reduction does not prove the target budget or promote the full-size root.

The output-dual reduction, the first strict coefficient base cases, the exact rank-one Gram
contraction, and its near-diagonal-Gram neighborhood have now passed independent review and are
`PROVED`, without promoting that OPEN boundary.  In particular, diagonal row or column Gram
matrices—including every dense maximally entangled coefficient—obey the sharp deterministic `1/m`
bound.

The unresolved flip/Werner slice is also isolated more sharply.  Independently reviewed exact
reduction turns the whole real Werner sector into the centered spectral inequality
`||R_U-I/m||<=sqrt((A^2-1)(1-m^-2))`.  Expectation and fixed bulk moments are safe but do not
exclude adaptive extreme-eigenvalue outliers; the standard quantum-expander estimate is before a
partial transpose that may lose a factor `d`, and this interface obstruction is now `PROVED`.
A growing-moment analysis further shows that return words are safely below threshold, while the
positive modulus-square majorant is too lossy.  The latter obstruction is independently `PROVED`.
Independently reviewed circular cancellation combinatorics now bounds the full fixed-word
reduction-plus-reversal collision set exponentially. Independently reviewed finite-`d` analysis
shows that the excess monotone-Weingarten paths above any fixed skeleton form a uniformly
vanishing geometric tail through logarithmic order. A repeated-edge example also rules out the
overstrong target of a genus-independent coefficientwise `C^N` bound without producing a bad
exact moment. The live trace gate is therefore the minimal-length nonplanar contraction-skeleton
entropy. Independent review proved the multi-boundary paired-stack label and Catalan-weight
bounds and verified the internal rooted-map count; the latter remains `CONJECTURED` only because
its exact unicellular-trisection input lacks an archived primary source. Subsequent proposer-side
permutation algebra settles the factorial and Euler questions more precisely: every contraction
skeleton is losslessly encoded by `ABC=rho`, and a connected genus-`h` minimal term carries exactly
`d^(-2h)`. Independent review has promoted both statements to `PROVED`. It also confirms the
topological correction—the canonical incidence constellation has 4N ordinary
edges, not the provisional 2N. Therefore the favorable `4096/m` generic-map instantiation is
retired; the naive 4N-edge application has unusable base `1048576^N`. A support-two common-cycle
surgery and its genuine recursive subclass bound with per-handle cost `2m^4N^2/d^2` are now
independently `PROVED`; an independently proved odd repeated-edge family stalls that induction
with positive genus. The live choices are now a
sharp weighted count for the structured two-face constellation or a boundary-preserving surgery
of support at least five. Independent review now proves this support floor for the fixed-rho
one-step normal form using an actual admissible `N=4` genus-one skeleton; the same skeleton admits
a support-five structural reduction, but that singleton base case is not universal and does not
preserve its original coloring. A separate independently reviewed tree--cotree code now proves the
entire positive-genus structural weighted count
`S_(N,h)<=4096^N N^(43h)` for `N>=2,h>=1`. The earlier printed planar coefficient is false at
`e=2`, but a self-contained unicyclic deletion-code repair has now passed independent review.
Together with the lossless injection and Catalan bound, it promotes the every-genus structural
count to `PROVED` with `D=32768` and `alpha=43`; the defective historical route remains visible.
Independently reviewed algebra also proves the sharp
admissible equality-component bound `kappa<=N+2+2h`, separates `c=2,h<=1` into the safe return
union, and bounds the residual `c=2,h>=2` sector by `4096^N N^(24h)` with its exact normalized
mass. The identity-pairing even-moment family proves that a
genus-independent `kappa<=N+O(1)` bound is impossible and forces any linear-genus version to have
`L>=2`; its own normalized mass decays and does not refute the centered target. The final signed-
moment assembly now combines these pieces into an explicit logarithmic-order master bound and exact
Markov step. Independent review first proved the high-probability centered statement and real
two-dimensional Werner coefficient sector for every fixed integer `m>e^18`. A later independently
reviewed refinement keeps the planar factor `16N^2 4096^N` explicit instead of absorbing its
polynomial into `32768^N`; the centered statement is now `PROVED` under the exact condition
`mH>4096`, uniformly including every integer `m>=932064` for `eta>=0`. Propagation of this stronger
threshold through the exact spectral equivalence has now passed fresh independent review: the
separately registered real-Werner two-dimensional coefficient-sector node is `PROVED` under the
same condition, including the `m>=932064` corollary.
The broader all-fixed-`m` centered claim, arbitrary-Hermitian coefficient sphere, physical `n=2`,
all-copy and every full-size conclusion remain unpromoted.

Positive-coefficient Loewner contraction through both coefficient partial traces, near-diagonal
positive and polarized spectral nuclear-norm subclasses, the `sqrt(r)` loss for unrefined
positive summation, the broader rook-support class, and the nonpositivity of rook
inclusion--exclusion truncation have all passed independent review and are `PROVED`. The reviewed
rook class reaches positive full-rank, high operator-Schmidt-rank examples with trace above `A`.
Independently reviewed double-off analysis extends this to a separately positive rook
core plus one Hermitian double-off simple-tensor direction and to explicit full-rank diagonal-core
neighborhoods of operator-Schmidt rank `Theta(m)`. Its exact projective/Frobenius ratio `sqrt(r)`
also shows why projective triangle summation alone cannot cover the full double-off sphere. The
next independently reviewed extension uses unital complete positivity to control every positive
spectral-flat coefficient with effective rank at least `m^2/A^2`, independently of
support or operator-Schmidt rank. It includes an explicit maximal-OSR complement projector and an
amplitude-restricted positive double-off family of OSR `1+m(m-1)`. This does not control arbitrary
positive coefficients with large coefficient operator norm; an unrefined Haagerup--Kadison route
retains an order-one nuclear-sum loss at rank `Theta(m^2)`. The high-probability Werner centered
bound, full Hermitian coefficient sphere, global physical `n=2`, and every `n>=3` case remain OPEN.

### 3. A genuinely collective non-Bell witness

The isotropic one-bit cap and fixed-dimensional selection theorem both use layerwise maximally
entangled witnesses. A construction whose optimized joint input is not a tensor product of those
witnesses could evade both reductions. It must still include a global all-input lower bound for
each side and full dimension-cost bookkeeping.

For a non-isotropic Bell witness of a channel with maximally mixed output marginal, the new
necessary condition is `I(A:B)-2J_{A->B}=Omega(full logarithmic size)`. This points specifically to
data-hiding or locking Bell outputs, but the same channel must also satisfy the global side bound.

There is now an additional channel-realization constraint: the realignment of every
`(Phi tensor bar(Phi))(Omega)` is `L_Phi L_Phi^dagger/d` and hence positive semidefinite. With
maximally mixed marginals the state is equivalently the normalized Choi state of the bistochastic,
self-adjoint, superoperator-positive Gram channel `(k/d)Phi Phi^*`. This excludes the entire
nontrivial affine Werner family `aI+bF`, including its symmetric and antisymmetric endpoints. The
surviving candidates must be non-Werner, realignment-positive hiding or locking states whose Choi
map admits the required rectangular CP factorization.

For such a Gram-channel Choi state the screening functional has an exact second form. If
`sigma_BE` is the Gram channel's maximally mixed Stinespring output, then
`I(A:B)-2J_{A->B}=2E_F(B:E)-S(E)`. Candidate searches can therefore work directly with this signed
entanglement-of-formation surplus, but must still solve the CP-square and global-side-entropy gates.

The exact 2026 flower-state entanglement-cost formula gives a sharp near-miss rather than a
candidate. Nontrivial Fourier/generalized flower states fail positive realignment when used as the
Bell output. When used as the Stinespring state they have only half the required rank, and the
canonical environment-local rank completion exactly saturates `2E_C-S(E)=0`. The search should
therefore move to non-maximally-correlated locking projectors rather than further flower variants.

The qutrit antisymmetric projector shows that the strict cost surplus is feasible in the correct
rank class: it has `E_C=1` and `S(E)=log(3)`. However, the polar sign of every square channel
orientation of its support is not an inner automorphism, so no orientation is
Hilbert-Schmidt-positive. Candidate searches must now impose an inner-compatible polar sign before
attempting the still stronger rectangular CP-square and all-copy side-entropy tests.

There is no higher-dimensional escape inside the normalized full antisymmetric-projector family.
The uniform Slater-basis decomposition gives `E_C(alpha_d)<=1`, whereas `S(E)=log d`, so every
`d>=4` member fails the strict necessary cost surplus.  The `d=2` member induces a constant
channel with zero defect, leaving the already-excluded qutrit member as the sole nontrivial
dimension that passes the cost screen.  Searches must move to proper supports or coherent
multi-sector states rather than larger full antisymmetric projectors.

The first proper-support escape is also unavailable.  A Pfaffian-pencil and skew-Takagi
classification shows that every rank-four subspace of `wedge^2 C^4` with maximally mixed
four-dimensional marginals has a four-element orthonormal Slater basis.  Its maximally mixed
support state therefore obeys `E_C<=1=S(E)/2` and fails the strict gate.  Proper antisymmetric
square supports need only be searched from `d>=5` onward.

Even there, Slater-convex supports are unavailable: any antisymmetric state with maximally mixed
`d`-dimensional marginal and a Slater ensemble has `E_C<=1`, below the strict `log(d)/2` threshold
for every `d>=4`.  The higher-dimensional search must begin with fermionically entangled support
states outside that convex hull, and must still prove a tensor-stable cost lower bound.

The canonical first example outside that screen is also a near-miss.  The rank-seven `G2`
cross-product subspace of `wedge^2 C^7` has maximally mixed marginals and exact one-shot
`E_F=log(3)+1/3>log(7)/2`; nevertheless, its square support channel has polar-sign negative
multiplicity 34, impossible for an inner involution on `M_7`, whose negative multiplicity is at
most 24.  Hence no local orientation is Gram-positive.  The regularized `E_C` of this state is not
claimed, and other fermionically entangled rank-`d` supports remain open.

Coherently adjoining the scalar Hurwitz direction does not repair the polar gate.  The rank-eight
octonionic left-multiplication support has maximally mixed marginals and exact one-shot `E_F=2`,
but its singular support channel has sign `+` on an irreducible 21-dimensional spinorial
`Spin(7)` algebra and `-` on a seven-dimensional complement.  The kernel-compatible polar
criterion would require an inner extension.  Any inner orthogonal involution with seven negative
skew directions is reflection type and fixes a common axis; the exact positive eigenspace has
common kernel zero.  This coherent multi-sector support is therefore another Gram near-miss.

More generally, an invertible square support channel `T=Q|T|` has some Hilbert-Schmidt-positive
input/output unitary orientation exactly when `Q` is an inner automorphism. This gives a
necessary-and-sufficient algebraic pre-screen for the first Gram-positivity stage. The
noninvertible self-adjoint extension is now also exact: the sign on `(ker T)^perp` must extend to a
support-preserving inner automorphism.  The CP-square test for survivors remains open.

The first exact qubit survivor of those pre-screens has also been closed. The positive Pauli Gram
channel with spectrum `(1,0,1/2,1/2)` has strict regularized entanglement-cost surplus and an
explicit rectangular CP factor, but every possible rectangular factor has a pure output with
Bloch length at least `1/sqrt(2)`. Its side entropy is therefore too small relative to the
`3/2`-bit Bell output.

The factor-norm argument now extends to the entire qubit-output Gram class. At fixed largest Bloch
eigenvalue `t`, concavity reduces the Choi-entropy lower bound to the vertices of the nonnegative
unital-qubit CP polytope. Strong additivity, majorization, and two scalar binary-entropy lemmas give
`S(J(T))>=2h_2((1+sqrt(t))/2)`, matching the universal factor upper bound. Thus every
qubit-output conjugate-Bell route is closed, for arbitrary finite input dimension. The Bell search
must move to output dimension at least three.

Within the first surviving output dimension, the depolarizing branch has a further exact cutoff.
For a depolarizing `k`-output Gram channel, every factor with input dimension `d<=k` has a pure
output whose purity reaches the depolarizing-square-root benchmark. The sharp maximum-entropy
curve at fixed purity, together with arbitrary-dimensional depolarizing strong additivity, rules
out a positive Bell defect. Hence a depolarizing qutrit candidate must have `d>=4`. The immediate
finite-dimensional target is to decide those oversized rectangular factors, or move to a
nondepolarizing qutrit Gram channel.

The qutrit Weyl random-unitary branch is now closed for the conjugate-Bell witness.  Its Bell output
has autocorrelation law `p*tilde p`, and four stabilizer inputs bound the regularized side by the
least line-quotient entropy.  The selected-line majorization
`p*tilde p prec (p mod L_*) tensor (p mod L_*)`, with `L_*` containing a maximum-mass affine line,
is now exact and independently reviewed. Earlier certificates give `k=1,3`; new complete KKT-face
enumerations give `k=5,7`; paired spectra interpolate `k=2,4,6,8`.  Shannon Schur concavity proves
`H(p*tilde p)>=2 min_L H(p mod L)`, excluding the regularized qutrit Weyl conjugate-Bell route.
The active construction frontier therefore moves to non-Weyl qutrit Gram channels or non-Bell
joint inputs.

The first structured oversized family does not survive. For the lower irreducible summand in
`3 tensor Sym^n(3)`, an occupation-number calculation gives the exact Gram contraction
`(5n-1)/[8(n+1)]`, while a product-overlap calculation gives exact minimum output entropy
`h_2(1/(n+1))`. Its Bell entropy is strictly more than twice that side entropy for every `n`.
The next representation-theoretic search must therefore use a nonsymmetric environment irrep or
a nondepolarizing qutrit Gram channel.

The first nonsymmetric choice, the adjoint environment `8`, is now also closed. In
`3 tensor 8=15 direct-sum bar6 direct-sum 3`, the sole new oversized channel is the `bar6`
summand. Its exact Gram contraction is `5/32`, its exact minimum output entropy is one bit, and its
Bell entropy is `h_2(1/4)+9/4`. The next covariant candidates must therefore come from other
environment irreps, beginning with the remaining small multiplicity-free tensor products.

The complete conjugate-symmetric tower is also unavailable. The lower summand in
`3 tensor Sym^n(bar3)` has exact Gram contraction `(n-1)/[4(n+2)]` and exact minimum output
spectrum `(n/(n+2),1/(n+2),1/(n+2))`; only the trivial first member saturates, while all `n>=2`
have negative Bell defect. The representation-theoretic frontier is now genuinely mixed highest
weights `(p,q)` with `p,q>0` beyond the adjoint.

That mixed-weight frontier is now closed for every single-irrep Stinespring channel. Exact Pieri
formulas show that one lower branch reduces monotonically to the symmetric tower and the other has
a Bell-minus-twice-side margin that can only improve away from the conjugate-symmetric tower.
Together with the product highest summand, this excludes all irreducible summands in
`3 tensor V_(p,q)`.

Taking a reducible invariant input subspace inside that same product does not reopen the route.
Every subspace containing the highest sector contains a product-output vector, while the only new
two-lower-sector direct sum has exact Gram contraction
`((5p+2)q+5p^2+9p-2)/(8(p+1)(p+q+2))`; an embedded middle-sector input gives a strict no-go for all
`p,q>=1`.

Repeating one environment irrep with arbitrary multiplicity is also insufficient. The overlap of
the middle- and third-sector multiplicity subspaces turns the total Gram contraction into a convex
combination of the two single-sector values and the completely coherent lower-sum value; the last
is the largest and is already excluded. The covariant qutrit frontier is therefore a coherent
mixture of *inequivalent* environment irreps sharing a common input irrep, or else a genuinely
noncovariant/nondepolarizing Gram channel.

The inequivalent-environment boundary towers are now closed. For inputs `V_(r,0)` and `V_(0,r)`,
every two-extreme mixture is parameterized by a qutrit depolarizing output spectrum `H_3(z)` and a
Bell Gram parameter no larger than `z^2`; depolarizing strong additivity gives the no-go.

For an interior input `V_(r,s)`, the three-extreme mixture becomes an explicit classical problem.
Writing `mu_i=e_i/(3 dim V_(r,s))`, its Gram parameter is exactly
`(1/8)chi^2(lambda||mu)`, and one highest-weight input gives an explicit triangular distribution
`q=lambda K_(r,s)`. The uniform scalar inequality
`B((1/8)chi^2(lambda||mu))>=2H(q)` is now proved. The proof combines the sharp qutrit bound
`D(q||u_3)>=(2 ln 2/3)chi^2(q||u_3)`, the exact contraction `chi^2(q||u_3)>=(8/5)t`, and certified
rational-log endpoint comparisons above `t=2/3`. Hence every irreducible-input covariant qutrit
channel is excluded. More than 3.21 million grid points remain as an independent audit. The only
covariant qutrit frontier is a reducible input with genuine cross-irrep channel coherence.

The smallest such cross-irrep graph is now closed. Its six-edge cycle connects three input and
three environment irreps, with both total dimensions equal to 24. The Gram parameter is an exact
quadratic in three edge weights, and a certified `16^3` rational box proof compares it against
three explicit block-highest side spectra with a strictly positive margin. The covariant frontier
does not begin merely at another translation of the same loop. An exact compact rational
Bernstein/logarithm certificate now covers every translated elementary hexagon with integer
`p>=0,q>=2` and all continuous edge weights. Separate convexity reduces two weights to four
corners; 204 adaptive compact boxes certify a global natural-log margin greater than `0.00180`.
This supersedes the earlier 1,225-cycle finite scan.

The complete elementary two-face target is now closed. Up to reversing the unordered pair, the
shared incidence edge has three branch types, and all three required distinct arguments. The
middle-type pair has a 12-branch, 1,098-leaf four-dimensional certificate. The conjugate-type pair
uses different binary side blocks and has a 12-branch, 996-leaf certificate. The highest-type pair
cannot be controlled by two ordinary binary blocks; retaining its shared three-edge simplex and
one binary block gives an eight-branch, 4,216-leaf five-dimensional certificate. All three leave
strict natural-log margins over every allowed integer label and continuous weight.

The connected three-face case is exactly classified into 11 translation classes while preserving
all `h/m/c` incidence labels: three straight chains, six bent chains, and two triangular clusters.
A full-incidence finite scan found no Bell candidate, and each of the nine chains has a
fixed-three original-side cover that survived ordinary, corner-biased, and million-label stress
tests. Six atomic directions now have exact certificates. Bent-left ternary, bent
`c/m,h/m,h/c`, and bent-right ternary are independently `PROVED`; the environment-centered
triangle, bent `h/m,h/m,h/c`, and straight all-`h/m` remain proposer-side `CONJECTURED`.
The bent-right run certifies 24 endpoint branches over 13,744 adaptive six-dimensional boxes
with a strictly positive exact margin displayed approximately as `4.870629792869e-05`. Five
directions remain `NUMERICAL`. The straight-reduced-coordinate run is now precisely blocked at a
width-`1/1024` depth-10 box whose lower-enclosure diagnostic is
`-9.173335876151267e-06`; this failed certificate is not a counterexample. Other selected
directions remain under exact computation. The immediate covariant tasks are to sharpen that
boundary enclosure, finish the remaining exact certificates, and independently review every
proposer-side result, not to repeat the classification. None of the straight, bent, or triangular
conjunction parents is upgraded. Repeated vertices, nontrivial multiplicity spaces, noncovariant
qutrit factors, and non-Bell inputs remain outside this three-distinct-face analysis.

The bent-central depth-10 replay was stopped at user request after the complete progress checkpoint
`processed=10000, certified=4992, pending=15`. It printed neither an uncertified depth-10 box nor
an exit-zero verdict, so the direction remains `NUMERICAL` and the interrupted prefix is not a
certificate.

### 4. A cost-paying finite approximation theorem

Improve the representation/strong-convergence realization so the certified gap and the complete
input/output/environment logarithmic cost have the same order. A fixed-depth existence theorem or
an uncontrolled `D(J)` is insufficient. The current published-estimate obstruction is now
independently `PROVED`; overcoming it requires a genuinely stronger uniform theorem or a different
gap mechanism, not a reinterpretation of the existing rate bound.

## Status boundary

The project now independently proves absolute-unbounded finite-dimensional `p=1` MOE pair,
Holevo pair, and same-channel two-copy gaps. No live route currently proves the Hayden--Penington
full-size statement. The first
target above is not a cosmetic strengthening; it is the finite-dimensional regularized-MOE
additivity problem that the checked literature continues to leave open.
