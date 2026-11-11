# Holevo / minimum-output-entropy extensive violation

This folder owns the third question: can finite-dimensional p=1 additivity violations exceed the
current constant scale, become unbounded, or grow linearly with the natural logarithmic size of a
primitive channel family?

- [`proof-dag/NODE_INDEX.md`](../../proof-dag/NODE_INDEX.md) is the generated claim index.
- [`proof-dag/GRAPH.mmd`](../../proof-dag/GRAPH.mmd) is the generated graph view.
- [`proof-dag/nodes/`](../../proof-dag/nodes) contains the canonical node records.
- [`reviews/`](../../reviews/holevo-extensive-violation) contains project-level independent reviews.
- [`artifacts/`](.) contains the linked proofs, exact certificates, source audits, and runs.
- [`tools/`](../../tools/holevo-extensive-violation) contains the project-specific exact certificate programs.

Begin with node `HEXT.goal`, then follow its structured route, evidence, and review links. This
directory is self-contained; repository-level `tools/` contains only shared structural validators.

Boss-facing frozen verdict: `artifacts/BOSS_QUESTION_3_VERDICT_20260830.md`. This project is not
the completed WHGAP capacity-threshold project.

The project separates three statements that must not be conflated:

1. a fixed positive one-shot pair gap;
2. an absolute gap unbounded with hierarchy depth; and
3. a Hayden--Penington-style gap extensive in full input/output/environment qubit cost.

Canonical claims live in `proof-dag/nodes/*.yaml`. Historical webpages and the previous Markdown
DAG are preserved under `artifacts/legacy-*`; they are evidence, not active task surfaces.

Current answer: a new proposer-side synthesis proves that finite-dimensional `p=1`
minimum-output-entropy pair gaps are unbounded in absolute size. It combines Collins--Youn's
product-free-group Haagerup bound with Bordenave--Collins tensor strong convergence, then uses a
product Bell witness. The Weyl-flag extension transfers the numerical pair gap exactly to Holevo
`chi`, and the balanced direct-sum reduction gives an unbounded same-channel Holevo gap with only
constant loss. This proof still awaits independent review.

A second proposer-side adversarial pass has now checked the direct-product representation,
finite-net uniformization, complementary-channel duality, global entropy bound, Bell witness,
probability order, Weyl transfer and pair-to-self constant against the local primary PDFs. It found
no failure and repaired a stale evidence locator, but it does not count as the independent review
required for promotion to `PROVED`.

The stronger Hayden--Penington full-size extensive question remains open. Strong convergence is
available after fixing the hierarchy depth, but the proof does not control how the required finite
matrix dimension grows with depth. Thus an `Omega(depth)` gap has been established without an
`Omega(full logarithmic dimension cost)` conclusion. Ordinary tensor-copy amplification remains
blocked by the two single-channel self-regularization defects.

The quantitative estimate behind the strong-convergence theorem has also been audited. Its
Schatten-moment factor already forces the per-leg dimension to grow at least polynomially with
depth in the regime where it preserves a positive entropy-defect rate. Consequently the published
bound certifies at most a subextensive ratio against the full `depth * log(per-leg dimension)` cost.
This is a proof-method obstruction, not an impossibility result for the channels.

Allowing the number of free generators to grow with depth does not rescue that certificate. The
free per-layer coefficient is at most `log(m)/m`, while the quantitative theorem requires
`D>=m^70`; thus an unbounded `m` gives certified gap/cost ratio at most `1/(70m)`. If `m` stays
bounded, the original `log D=Omega(log depth)` obstruction applies on a fixed-`m` subsequence.
Hence no joint `m(depth)` scaling within the published estimate certifies a positive full-size
constant, although the true random channels could still behave better than this proof bound.

There is now also a model-specific reason that the per-leg dimension cannot simply be frozen in
the iid Haar realization. At fixed dimension, conjugation invariance and empirical matching pair
almost all sufficiently many layers with approximate conjugates inside the same side. Bell inputs
on those pairs force a side entropy rate below the Collins--Youn rate used by the construction.
Thus fixed-dimension iid Haar layers fail mathematically, not merely because the available
convergence theorem lacks a rate. An oriented or non-iid ensemble could evade this exact matching
argument, but then repeated-channel leakage becomes the replacement gate.

That replacement gate no longer needs an iid assumption. In a compact fixed-dimensional
continuous channel family, every deterministic or random long sequence can be grouped into
arbitrarily large blocks of near-repeated channels. If its empirical measures converge, the
heterogeneous product's per-layer minimum output entropy is at most the corresponding average of
the individual regularized entropies; in complete generality it is at most the best fixed-channel
regularized rate in the family. Avoiding conjugate collisions by orientation or adaptive layer
selection therefore does not bypass self-regularization.

There is also an exact selection principle for the remaining fixed-dimensional Bell route. If a
heterogeneous product and its conjugate had a positive asymptotic defect rate certified by the
product of its layerwise Bell inputs, an empirical-measure subsequence would select one layer whose
fixed channel/conjugate pair already has positive regularized MOE defect. Conversely, repeating
such a layer gives the rate. Hence adaptive or deterministic layer diversity is equivalent here to
the core fixed-finite-channel regularization problem, not a weaker surrogate for it.

A separate attempt to make the single-layer gain pay for dimension was evaluated exactly. Closing
the random-unitary Kraus set into a uniformly weighted finite group makes `q^2` Bell labels collapse
through the group multiplication table, apparently offering a `log q` saving. But the same group
average is a conditional expectation. Its minimum output entropy is the logarithm of the smallest
occurring irrep dimension and is exactly additive with every other uniform group twirl. The large
label collision is therefore cancelled by the side structure; only nonuniform or genuinely
non-group collision mechanisms remain open.

The newest projection-induced construction also has a tempting dimension-paying boundary that
must not be analyzed with its published fixed-parameter expansion. If the projection ratio is
scaled as `t=c/k^2`, its conjugate Bell output has a constant exceptional eigenvalue and an apparent
`Theta(log k)` entropy saving. Direct use of the exact LLW output body produces a feasible
one-channel output with the same spike. The logarithmic terms cancel, and the limiting Bell
certificate is at most `h_2(1/c)<=1` bit, maximized at `c=2`. This closes that critical-scaling
loophole but is not a universal one-bit upper bound.

The remaining LLW boundary scalings are now closed by a stronger elementary theorem. Whenever a
channel/conjugate-channel Bell output is isotropic, measuring one output leg steers the other
channel to a legal one-channel output with a related spike spectrum. A scalar entropy inequality
then caps that Bell certificate by one bit for every finite `k` and every isotropic parameter.
Applied after LLW's fixed-`k,t` output-set limit, the cap is uniform over all admissible `t=t_k`.
This is universal for the isotropic Bell mechanism, not for arbitrary channel pairs, optimized
joint inputs, or products of heterogeneous isotropic layers.

For general non-isotropic Bell outputs there is now a quantitative replacement. If the channel
maps maximally mixed input to maximally mixed output, the Bell-certified defect is at most
`I(A:B)-2J_{A->B}`, where `J` is the largest classical correlation extractable by measuring one
side. Thus an extensive Bell route needs an extensive data-hiding/locking-like correlation surplus
and a global one-channel entropy bound. Product isotropic layers obey the sum of their individual
one-bit caps even though their total state is not isotropic.

Bell outputs also satisfy a sharp channel-realization constraint that arbitrary data-hiding states
do not: after realignment, `(Phi tensor bar(Phi))(Omega)` is exactly the positive Gram matrix
`L_Phi L_Phi^dagger/d` of the channel's Liouville superoperator. Equivalently, under maximally
mixed marginals the state is the normalized Choi state of the bistochastic, self-adjoint,
superoperator-positive Gram channel `(k/d)Phi Phi^*`. This rules out every nontrivial
`U tensor U` Werner state, including the symmetric and antisymmetric endpoints, as a conjugate-Bell
output. Any surviving hiding/locking candidate must be non-Werner, realignment-positive, admit the
required rectangular CP factorization, and still support the global side entropy bound.

For the same Gram-channel Choi state, the one-way classical correlation is exactly the channel's
Holevo quantity constrained to maximally mixed average input. A Stinespring decomposition then
gives the identity `I-2J=2E_F(B:E)-S(E)`. The surviving Bell route is therefore an exact signed
entanglement-of-formation-surplus problem with two additional channel constraints: the Choi map
must admit the rectangular CP square root, and that square root must keep its entire output set
high-entropy.

The same bridge now survives tensor regularization. For one fixed candidate, the Bell-certified
regularized defect is at most `2E_C(sigma_BE)-S(E)`, where `E_C` is the entanglement cost of the
Gram channel's maximally mixed Stinespring state. Therefore a fixed finite channel cannot bootstrap
to a positive Bell rate unless `E_C>S(E)/2`. This is a necessary pre-screen, not a construction:
even a positive state-level surplus must still be converted into a global all-copy minimum-output-
entropy lower bound for the rectangular factor.

The August 2026 exact entanglement-cost formula for flower states has now been screened against
this pipeline. It does not provide the missing candidate. A maximally correlated state
`M(rho)=sum rho_ij |ii><jj|` has diagonal realignment with entries `rho_ij`; hence a generalized
flower state is realignment-positive only when its defining unitary is a permutation. In
particular the high-cost Fourier flower state cannot be a conjugate-Bell output. It also has rank
only half its local dimension as a Stinespring candidate. Appending the minimal environment-local
mixed qubit repairs that rank but gives exactly `2E_C-S(E)=0`, not a strict surplus. This rules out
the natural flower-state route while leaving non-maximally-correlated locking states open.

The entanglement-cost threshold itself is not vacuous. The normalized qutrit antisymmetric
projector has rank three, maximally mixed qutrit marginals, exact `E_C=1`, and therefore strict
surplus `2E_C-S(E)=2-log(3)>0`. But its support channel has polar sign
`Sigma(X)=2Tr(X)I/3-X^T`, which is not a unitary conjugation. Uniqueness of the polar decomposition
then proves that no input/output unitary orientation can make that square channel
Hilbert-Schmidt-positive. This near-miss passes the state gate and fails the independent
Gram/CP-square realization gate.

The entire normalized antisymmetric-projector family is now excluded, not just this qutrit
member.  A uniform Slater-basis ensemble gives `E_C(alpha_d)<=1`, while the maximally mixed
environment marginal has entropy `log d`; hence every `d>=4` member fails the strict cost gate.
The `d=2` member is a rank-one constant channel with zero defect, and `d=3` is the exceptional
rank coincidence handled by the polar-sign argument above.  This family theorem does not exclude
proper antisymmetric supports or coherent mixtures with other sectors.

The first proper-support extension is closed as well.  In `wedge^2 C^4`, every rank-four support
with maximally mixed four-dimensional marginals has a two-dimensional complement unitarily
congruent to `span{e_1 wedge e_2,e_3 wedge e_4}`.  The original support consequently has four
orthonormal Slater determinants and again satisfies `E_C<=1=S(E)/2`.  Thus a proper
antisymmetric square-support candidate, if one exists, must begin at `d>=5`.

There is also a dimension-uniform convex-hull pre-screen.  Any maximally-mixed-marginal
antisymmetric state admitting a Slater-determinant ensemble has `E_C<=1`, and hence fails the
strict gate for every `d>=4`.  A `d>=5` proper-support survivor must therefore be fermionically
entangled--outside the Slater convex hull--before polar orientation, CP factorability, or all-copy
side entropy are worth testing.

The first natural support beyond that convex hull is now screened too.  The seven-dimensional
`G2` cross-product subspace of `wedge^2 C^7` has rank seven, maximally mixed marginals, and exact
one-shot `E_F=log(3)+1/3>log(7)/2`.  However, its support channel has Hilbert--Schmidt eigenvalue
multiplicities `1,-1/2,1/2,-1/6` with multiplicities `1,7,14,27`; its polar sign consequently has
a 34-dimensional negative space.  An inner involution on `M_7` has negative dimension at most 24,
so no local orientation is Gram-positive.  This is an exact polar near-miss, not an
entanglement-cost result: `E_C` of the support state remains unproved.

A coherent multi-sector variant reaches the same boundary and also fails.  The rank-eight
octonionic left-multiplication support has exact one-shot `E_F=2>log(8)/2`; its support channel is
singular with spectrum `1^1,(-1/2)^7,(1/2)^21,0^35`.  A new kernel-compatible polar theorem says
that its sign must extend to a support-preserving inner automorphism.  Exact rational ranks show
that the positive 21-space is the irreducible spinorial `Spin(7)` algebra with no common axis,
whereas any orthogonal inner involution with seven negative skew directions fixes a standard
`so(7)` and a common axis.  Hence this support too has no Gram-positive local orientation.  Again,
the statement is about exact one-shot `E_F`; no value of its regularized `E_C` is asserted.

This obstruction is now abstracted into an exact orientation theorem. For any invertible square
support channel `T=Q|T|`, input/output unitary conjugations can make `T` Hilbert-Schmidt-positive
if and only if the polar unitary `Q` is itself an inner automorphism `Ad_R`. Candidates failing
this test can be rejected before attempting the harder CP-square and tensor-entropy analysis.
For a self-adjoint support channel with a kernel, the exact replacement requires the polar sign on
`(ker T)^perp` to extend to an inner automorphism that preserves that support; this partial-polar
version is what closes the octonionic candidate.

An exact qubit Pauli near-miss now shows that even passing both of those state/channel gates is not
enough. The Hilbert-Schmidt-positive channel with transfer spectrum `(1,0,1/2,1/2)` has exact
Stinespring-state surplus `2h_2(3/4)-3/2>0` and an explicit rectangular `M_4->M_2` CP factor.
However, for every rectangular factor the Gram identity forces one adjoint Pauli observable to
have operator norm at least `1/sqrt(2)`. Some pure input therefore has output entropy at most
`h_2((1+1/sqrt(2))/2)`, making twice the side entropy strictly smaller than the `3/2`-bit Bell
entropy. This candidate passes cost and CP factorability but fails the global side-entropy gate.

That single example has now been upgraded to a complete qubit-output no-go theorem for the Bell
route. Every positive qubit Gram channel has nonnegative Bloch eigenvalues `lambda_i`. If
`t=max lambda_i`, every rectangular factor has
`S_min(Phi)<=h_2((1+sqrt(t))/2)`, while a CP-polytope vertex argument proves that the Bell-diagonal
Choi entropy is at least twice this quantity. Therefore
`2 barS_min(Phi)<=S((Phi tensor barPhi)(Omega))` for every finite input dimension. Any surviving
fixed-channel conjugate-Bell candidate must have output dimension at least three.

The first qutrit subfamily is now also sharply reduced. If the Gram channel is the `k`-dimensional
depolarizing channel and the factor has input dimension `d<=k`, an exact Haar-average purity
identity forces some factor output to be at least as pure as an output of the depolarizing square
root. The sharp entropy bound at fixed purity and King's arbitrary-dimensional depolarizing strong
additivity then give `2 barS_min(Phi)<=S((Phi tensor barPhi)(Omega))`. Thus a surviving
depolarizing qutrit factor must be genuinely rectangular with `d>=4`; general nondepolarizing
qutrit Gram channels remain open.

One nondepolarizing CP-square family is now excluded from the conjugate-Bell route.  For a qutrit Weyl
random-unitary factor `Phi_p`, the conjugate-Bell entropy is exactly `H(p*tilde p)`, while the four
stabilizer directions give the regularized side bound `barS_min<=min_L H(p mod L)`.  Thus the
uniform inequality `H(p*tilde p)>=2 min_L H(p mod L)` excludes this entire Bell route.  It is now
proved by the stronger selected-line majorization
`p*tilde p prec r_L tensor r_L`, where `L` contains a maximum-mass affine line.  Exact certificates
give `k=1,3,5,7`; paired autocorrelation values and sorted product entries interpolate all even
indices.  The two new eight-dimensional KKT-face enumerations cover all 263,950 active sets and
have exact minimum zero.  The earlier 200,000-point scan and global collision-entropy identity are
retained as route-selection and independent-shadow evidence, not as the proof.  The complete
chain has now passed an independent adversarial review with fresh reproduction of all four exact
certificate stages.  The proved scope still does not exclude non-Weyl qutrit Gram factors or
non-Bell joint inputs.

The most natural oversized `SU(3)` covariant continuation has also been classified exactly. For
the lower summand in `3 tensor Sym^n(3)`, the input dimension is `n(n+2)`, the Gram contraction is
`(5n-1)/[8(n+1)]`, and the minimum output entropy is `h_2(1/(n+1))`. Direct comparison with the
isotropic Bell spectrum is strict in the wrong direction for every `n`. In particular the first
`M_8->M_3` candidate from `3 tensor 6=10 direct-sum 8` misses the Bell threshold by about `0.821`
bits. Other `SU(3)` couplings and nondepolarizing qutrit Gram channels remain live.

The first nonsymmetric environment has now been closed too. In
`3 tensor 8=15 direct-sum bar6 direct-sum 3`, the `15` contains a product vector and the `3` is
covered by the `d<=k` theorem. For the new `M_6->M_3` channel from `bar6`, a Casimir calculation
gives Gram contraction `5/32`, while the exact product-overlap block forces and attains
`S_min=1`. Its Bell entropy is `h_2(1/4)+9/4>3`, so the whole coupling fails the Bell route.

The conjugate-bosonic tower is closed as well. For the lower `Sym^{n-1}(bar3)` summand in
`3 tensor Sym^n(bar3)`, a creation-operator isometry gives Gram contraction
`(n-1)/[4(n+2)]` and exact minimum output spectrum
`(n/(n+2),1/(n+2),1/(n+2))`. The first member merely saturates the Bell inequality and every
`n>=2` member fails it strictly. The covariant qutrit search is therefore narrowed to genuinely
mixed highest weights beyond the adjoint, or to nondepolarizing Gram channels.

The mixed highest weights are now closed too. The general Pieri decomposition
`3 tensor V_(p,q)` has one product-containing highest summand and two lower summands. Exact
Casimir/Gelfand--Tsetlin formulas give both lower Gram contractions and their minimum output
spectra. The first lower branch reduces monotonically to the already excluded symmetric boundary;
the second branch has a Bell-minus-twice-side margin that improves monotonically away from the
already excluded conjugate-symmetric boundary. Hence every single-irrep `SU(3)`-covariant qutrit
channel fails the Bell route.

Allowing several Pieri sectors inside the same irreducible-environment product does not help. Any
invariant subspace containing the highest sector still contains a product-output vector. The only
new case is the direct sum of the two lower sectors; its exact Gram contraction is
`((5p+2)q+5p^2+9p-2)/(8(p+1)(p+q+2))`, and an embedded middle-sector input already makes twice the
side entropy strictly smaller than the Bell entropy. Thus every invariant subspace of
`3 tensor V_(p,q)` is excluded.

Equivalent environment multiplicities are excluded as well. For
`V_(p,q) tensor C^m`, arbitrary middle/third multiplicity subspaces contribute only through their
principal-angle overlap, and the resulting Gram contraction is a convex combination of the two
single-sector contractions and the already excluded fully coherent lower-sum contraction. The
remaining covariant case must mix inequivalent environment irreps that share a common input irrep;
noncovariant qutrit Gram factors also remain open.

The inequivalent-environment problem is now solved on both boundary input towers. For input
`V_(r,0)` or `V_(0,r)`, the two-extreme mixture has a highest-weight output spectrum `H_3(z)` and
Gram parameter `t=((r+3)/(4r))z^2<=z^2`; depolarizing strong additivity excludes a Bell gap.

For an interior input `V_(r,s)`, the last irreducible-input covariant case reduces exactly to a
classical two-variable inequality. With dimension barycenter `mu_i=e_i/(3 dim V_(r,s))`, a mixture
`lambda` has `t=(1/8)chi^2(lambda||mu)` and an explicit triangular highest-weight output
distribution `q=lambda K_(r,s)`. That inequality is now proved: a sharp qutrit
relative-entropy/collision bound and an exact `chi^2(q||u_3)>=(8/5)t` contraction close `t<=2/3`;
dimension weights plus five certified rational-log intervals close `t>2/3`. Thus every
irreducible-input `SU(3)`-covariant qutrit channel fails the Bell route. Reducible inputs with
cross-irrep coherences remain open. The earlier 3,210,735-point scan is retained only as an audit.

The first reducible-input cross-irrep cycle is closed too. The smallest six-edge Pieri cycle has
total input and environment dimension 24, an exact three-variable quadratic Gram parameter, and
three explicit block-highest side spectra. A `16^3` rational box proof gives a strictly positive
Bell-minus-twice-side margin on every box; the smallest certified natural-log margin exceeds
`0.0124`.

This is now upgraded from one loop and a finite translation scan to the entire translated
elementary-cycle family. For every integer `p>=0,q>=2`, separate convexity reduces the Gram
parameter to four edge-weight corners. Compactifying both unbounded labels and using exact
rational Bernstein control-point ratios gives a 204-leaf certificate over all labels and all
continuous weights; its smallest natural-log margin exceeds `0.00180`. The subsequent two-face
analysis closes every way for two elementary faces to share an incidence edge. Thus a covariant
survivor must use at least three faces, repeated vertices, nontrivial cycle multiplicity, or
another larger-graph effect. Noncovariant qutrit factors and non-Bell inputs remain open.

All elementary two-face families are now closed. Up to reversing the unordered pair, the shared
incidence edge has three genuinely different branch types. The middle-edge and conjugate-edge
orientations reduce to 12 endpoint branches and are certified by 1,098- and 996-leaf
four-dimensional rational Bernstein/logarithm proofs. The highest-edge orientation requires
retaining a shared three-edge simplex together with one binary block; its eight branches are
certified over five variables by 4,216 compact boxes. The cover uses three separate proofs rather
than an unjustified channel-level Weyl equivalence.

The connected three-face frontier is now classified rather than merely proposed. Quotienting only
by translation gives exactly 11 labelled orientation classes: three straight chains, six bent
chains, and two triangles. A full-incidence random/corner scan found no Bell candidate in any
class. Six atomic directions now have exact certificates: bent-left ternary, bent
`c/m,h/m,h/c`, and bent-right ternary are independently `PROVED`, while the
environment-centered triangle, bent `h/m,h/m,h/c`, and straight all-`h/m` are proposer-side
`CONJECTURED`. The bent-right certificate covers 24 endpoint branches and 13,744 six-dimensional
compact boxes, with strictly positive exact margin displayed approximately as
`4.870629792869e-05`. Five directions remain `NUMERICAL`. In particular,
straight-reduced-coordinate reached an exactly recorded full-depth box at runtime depth 10 with
lower-enclosure diagnostic `-9.173335876151267e-06`; this certificate-resolution failure is not a
mathematical counterexample. The bent-central depth-10 replay was stopped at user request after
`processed=10000, certified=4992, pending=15`; it produced no terminal verdict and remains
`NUMERICAL`. Other selected directions may remain under exact computation. All fixed-cover
selectors for the nine chains survived million-label stress, but those scans are not exact
certificates. No straight, bent, or triangular conjunction parent is upgraded by these atomic
results. Repeated vertices and cycle multiplicity remain outside this classification.

The most direct remaining bootstrap is now sharper than the old fixed-depth route. If one selected
large-gap product-Haar block has two absolute self-regularization losses whose sum is smaller than
its one-shot pair gap, then that fixed finite pair already has positive regularized MOE defect;
ordinary tensor powers would immediately give full-size extensivity. Because the one-shot gaps are
unbounded, any uniform `O(1)` self-leakage theorem for this family would suffice. No such theorem is
currently available, and ensemble-specific weak-multiplicativity bounds cannot be imported without
proving that they cover these blocks.

That bootstrap has now been narrowed to one explicit OPEN lemma. For the complement `C_J` of one
fixed successful product-Haar block, with `q=m^J`, it is enough to prove physical-output purity
multiplicativity
`sup_rho Tr[C_J^(tensor n)(rho)^2] <= (A_{J,eta}/q)^n` for every `n`, where
`A_{J,eta}=1+(1+eta)^2((1+9/m)^J-1)`. It would give regularized pair defect at least
`J log_2(m)/m-2 log_2(A_{J,eta})`, positive for `ln(m)>18` and small enough `eta`. This does not ask
for arbitrary matrix-level completely bounded control. Montanaro's random-subspace theorem does
not apply to the singular product-random-unitary ensemble, and its PPT relaxation is capped at half
the needed entropy rate. The canonical gate is
`HEXT.product-haar-physical-self-purity-multiplicativity`; full-size extensivity remains OPEN.

The first repeated-use case is now reduced exactly. At `n=2`, every input separable across the two
uses satisfies the purity target, so only pure entangled inputs remain. Their exact missing
condition is a centered two-body correlation inequality, equivalently a physical Gram-cone bound;
PPT/DPS gives relaxations but not an automatic proof. Simultaneously real/orthogonal tuples are
ruled out by an independently reviewed maximally entangled collision with purity at least
`2/q^2-1/q^3`; the same independently reviewed obstruction now covers every complex tuple closed
under entrywise conjugation up to permutation and phases. This remains a special dependent,
measure-zero subclass and is not a generic-Haar refutation. For a generic complex-Haar one-layer
tuple, the Bell frame potential instead has
exact mean `m^2+(m^4-m^2)/d^2+2m(m-1)/(d(d+1))`; at fixed `m` its Bell-failure probability is
`O(m^3/d^2)`. Thus the Bell input is high-probability safe as `d` grows, but the supremum over all
entangled inputs—and therefore even the global `n=2` case—remains open. Direct pure-state nets
lose because their metric entropy is quadratic in `d`, and unrestricted replica/PPT relaxations
erase load-bearing physical geometry. Exact output duality instead reduces global `n=2` to an
`m^4`-dimensional scalar coefficient net. The remaining lemma is same-tuple two-leg scalar strong
convergence, which is not supplied by the independent-leg Bordenave--Collins theorem.

The all-copy physical purity itself now has an exact independently reviewed centered-subset
expansion. Writing `C_J=D_0+E`, one has
`Tr[C_J^(tensor n)(rho)^2]=sum_S q^(-(n-|S|))||E^(tensor |S|)(rho_S)||_2^2`.
At `n=3` a new fully centered three-body term appears; summing the one- and two-copy marginal
inequalities gives no bound on it. This closes an exact reduction, not the inequality: a new
connected physical-correlation estimate is still required at every copy number.

A second shortcut is now ruled out exactly: no fixed finite unitary tuple can approximate the free
length-two operator system with small distortion at every matrix level. A Bell-vector coefficient
witness forces completely bounded distortion at least `(m-1)/5`. Thus fixed-depth scalar strong
convergence cannot simply be promoted to all-depth control by abstract operator-space
tensorization. The remaining question is narrower and more physical: can the coefficients that
actually arise as complementary-channel outputs obey a better all-copy bound than arbitrary matrix
coefficients?

The post-2024 literature does not silently close that remaining gate. Kalantar--Shobeiri's 2025
extension remains infinite-dimensional and commuting-operator. Magee--de la Salle's stronger
finite-matrix theorem is uniform only over representation degrees up to `n^A` while `n` tends to
infinity, and it controls a diagonal representation rather than the full independently indexed
coefficient system of a repeated channel. It therefore cannot exchange `for every copy count,
choose a dimension` with `choose one finite dimension that works for every copy count`.

Simply restricting the infinite commuting-operator construction to a finite input does not evade
this distinction. Such a restriction does inherit the all-copy side lower bound. However, for the
natural finite-set subspace and maximally correlated tensor witness, the matched joint sector and
a one-channel translate test state have exactly the same Gram matrix. The spatial joint collision
is therefore accompanied by the same one-side entropy loss. A successful restriction argument
would need a genuinely different spatialization that breaks this Gram-spectrum identity.

Temperley--Lieb quantum channels were also checked as a structured finite-dimensional candidate.
Their one-shot minimum output entropy is asymptotically sharp as the ambient quantum-group
parameter grows, and selected two-channel covariant outputs have exact spectra. But the source
does not control every tensor power of one fixed finite channel or identify the global minimum for
the product. Its own numerical tests point against strict subadditivity in the tested covariant
family. Thus this is another useful source-scope gate, not the missing regularized construction.

The fixed-partner hierarchy has now been sharpened in two directions. Isometric and
entanglement-breaking fixed partners have exactly zero defect with every other channel, but the
general non-EB FCEA support-function inequality remains open. Separately, an elementary output-
entropy bound proves that the proposed fixed-output BCN hierarchy cannot be full-size extensive if
its fresh environment dimensions tend to infinity; that route can at most target an absolute-
unbounded gap unless it is replaced by bounded-cost reusable layers or a gap that grows with cost.
The Fukuda--Nechita additivity-rate bounds also cannot supply the missing tensor-copy
amplification for a conjugate pair: each underlying entropy bound is tensor-multiplicative, so the
same bound automatically forces every matched joint witness entropy to be at least the sum of the
two side bounds. This is a proof-method obstruction, not a no-go theorem for extensive gaps.

The simplest visible-erasure wrapper has now been evaluated exactly. Its cross defect is at most
`p*q` times the original gap, and its regularized side loss is an explicit variational entropy over
binomially surviving subsets. Generic bounds on that functional are only linear in the survival
probability and cannot improve a failed bootstrap certificate. The route is not logically dead,
but it now has a precise revival condition: prove a channel-specific strict thinning bound for the
product-Haar blocks, or use a wrapper with genuinely different cross/self scaling.

The post-reduction live targets are ranked in
`artifacts/REMAINING_FRONTIER_20260830.md`; the first target is one fixed finite channel with
positive regularized channel/conjugate-channel defect.

## Validation

```sh
python3 tools/proof_dag_check.py --problem holevo-extensive-violation --write-generated
python3 tools/evidence_closure_check.py --problem holevo-extensive-violation
```
