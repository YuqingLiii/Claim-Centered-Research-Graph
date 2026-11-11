# Boss question 3: can the violation be large or extensive?

Date: 2026-08-30

## Frozen question

Keep three scales separate:

1. greater than one bit;
2. unbounded absolute finite-dimensional gap; and
3. `Omega(full logarithmic input/output size)` in the Hayden--Penington sense. Counting a minimal
   Stinespring environment is an equivalent constant-factor convention; padded environments do
   not count.

In the third item, the family label is not a tensor-power exponent. Repeating a fixed one-shot
counterexample gives cumulative coding gain relative to its single-copy quantity, but it does not
automatically give a positive additivity defect between two growing primitive block channels;
their two side quantities may self-regularize at the same linear scale.

## Current verdict

- A single channel/conjugate-channel Bell certificate whose output is isotropic is at most one bit.
  This new proposer-side theorem is uniform in the LLW parameters and closes every LLW boundary
  scaling `t=t_k` in the iterated auxiliary-dimension limit.
- The one-bit cap is mechanism-specific. A product of nonidentical layers is not one isotropic
  state.
- A Collins--Youn plus Bordenave--Collins synthesis independently proves finite-dimensional pair
  gaps that exceed one bit and are unbounded in absolute size. Independently reviewed exact
  Weyl-flag and pair-to-self reductions transfer this to Holevo pair and same-channel gaps with
  constant loss.
- This does not yet prove full-size extensivity: the finite matrix dimension required at hierarchy
  depth `J` is not controlled well enough relative to the complete logarithmic cost.
- An independently proved proof-method rate gate shows that jointly increasing the free-generator
  count does not repair the published certificate: its
  per-layer coefficient is at most `log(m)/m` while the theorem requires `D>=m^70`. Thus unbounded
  `m` has vanishing certified gap/cost ratio, and bounded `m` falls back to the
  `log D=Omega(log J)` obstruction.
- Fixed-dimensional heterogeneity is no escape. For any compact continuous layer family, an
  arbitrary heterogeneous product has side entropy rate no larger than the best fixed-channel
  regularized rate. If the product of layerwise Bell inputs did certify a positive asymptotic gap
  rate, one fixed finite layer would already have positive Bell-certified regularized defect.
- A non-isotropic data-hiding Bell route is now more constrained than the correlation test alone
  suggests. Every conjugate-Bell output has positive realignment
  `R(Z)=L_Phi L_Phi^dagger/d`; under maximally mixed marginals it is the Choi state of the Gram
  channel `(k/d)Phi Phi^*`. This excludes all nontrivial Werner `aI+bF` states. A surviving
  candidate must be non-Werner, realignment-positive, admit the required rectangular CP
  factorization, and still have a global one-channel minimum-entropy bound.
- For the surviving Gram-channel candidates the required hidden-correlation surplus is exactly
  `2E_F(B:E)-S(E)` on the maximally mixed Stinespring state. This supplies a precise candidate
  screening functional but not the missing extensive construction.
- After tensor regularization, a positive fixed-channel Bell rate requires the sharper necessary
  condition `E_C(B:E)>S(E)/2`. Passing it is still insufficient without an all-copy global side
  entropy lower bound.
- That remaining physical all-copy bound now has an exact independently reviewed subset
  decomposition: for `C=D_0+E`, its purity is the sum of centered correlations over all input
  marginals. A new fully centered term appears at every copy count, so summing the lower-copy
  marginal inequalities does not close an induction. This is a reduction, not a proof of the
  all-copy bound.
- At two copies the Bell-collision obstruction extends from real tuples to every complex Kraus
  tuple closed under conjugation up to permutation and phases, with purity at least
  `2/q^2-1/q^3`. Exact conjugation closure is a dependent measure-zero subclass and therefore does
  not refute the generic complex-Haar existential route.
- The newly exact flower-state entanglement costs do not fill this gap. The high-cost Fourier
  flower states fail the necessary positive-realignment test as Bell outputs; as Stinespring
  candidates they have the wrong rank, and their canonical rank completion only saturates
  `2E_C-S(E)=0`.
- The state threshold is nevertheless attainable: the normalized qutrit antisymmetric projector
  has strict surplus `2E_C-S(E)=2-log(3)>0`. It still cannot solve the channel problem because a
  polar-decomposition argument excludes every Hilbert-Schmidt-positive input/output orientation
  of its support channel.
- The full normalized antisymmetric-projector family is consequently closed: a one-ebit Slater
  decomposition gives `E_C<=1`, so every `d>=4` member fails `E_C>S(E)/2`; `d=2` is a constant
  rank-one-input channel, and the exceptional `d=3` member is the polar-sign near-miss above.
- The first proper antisymmetric square-support case is closed too: every rank-four support in
  `wedge^2 C^4` with maximally mixed marginals has a four-state Slater ensemble, so
  `E_C<=1=S(E)/2`. Any such proper-support search must start at `d>=5`.
- In every dimension `d>=4`, Slater-convex antisymmetric states fail for the same one-ebit reason.
  Thus any higher-dimensional proper-support survivor must be fermionically entangled and still
  needs an independent tensor-stable lower bound on `E_C`.
- The first natural fermionically entangled square support is another exact near-miss.  The
  seven-dimensional `G2` cross-product subspace has maximally mixed marginals and one-shot
  `E_F=log(3)+1/3>log(7)/2`, but its polar sign has 34 negative directions; an inner involution on
  `M_7` has at most 24.  No local orientation is Gram-positive.  This does not determine its
  regularized `E_C` or exclude other higher-dimensional supports.
- A coherent scalar-plus-antisymmetric construction also fails exactly.  The rank-eight
  octonionic Hurwitz support has one-shot `E_F=2>log(8)/2`, but its singular polar sign is the
  spinorial `Spin(7)` split.  The positive 21-space has no common axis, while every inner
  orthogonal involution with the required seven negative skew directions is reflection type and
  fixes one.  The new kernel-compatible polar criterion excludes every local Gram orientation.
- More generally, for an invertible square support channel `T=Q|T|`, such a positive orientation
  exists exactly when `Q` is an inner automorphism. This is now a mechanically testable candidate
  gate before the stronger rectangular CP-square condition.
- For singular self-adjoint square supports, the exact replacement is that the polar sign on
  `(ker T)^perp` extend to a support-preserving inner automorphism.
- A qubit Pauli Gram channel can pass both the exact entanglement-cost and rectangular CP-factor
  gates, so neither is vacuous. Yet a dimension-uniform norm argument forces every one of its
  rectangular factors to have too-low side entropy for a Bell defect. The missing construction
  must pass all three gates simultaneously.
- The preceding obstruction is now universal for qubit output. A full CP-polytope calculation
  proves `2 barS_min(Phi)<=S((Phi tensor barPhi)(Omega))` for every
  maximally-mixed-preserving `Phi:M_d->M_2`, regardless of input dimension. Any surviving Bell
  candidate must have output dimension at least three.
- On the depolarizing Gram subbranch, an exact Haar-purity theorem gives an additional cutoff:
  every `Phi:M_d->M_k` with `d<=k` fails the Bell inequality. Thus a depolarizing qutrit candidate
  must have `d>=4`; general qutrit Gram channels are not excluded.
- For qutrit Weyl random-unitary factors, the Bell route reduces exactly to the classical gate
  `H(p*tilde p)>=2 min_L H(p mod L)` on `F_3^2`.  The stronger selected-line majorization is now
  certified exactly proposer-side: `k=1,3,5,7` come from complete rational active-face
  enumerations, and paired-spectrum interpolation gives `k=2,4,6,8`.  This closes the regularized
  qutrit Weyl conjugate-Bell route, but not non-Weyl qutrit Gram factors or non-Bell joint inputs.
- The natural oversized `SU(3)` family from the lower summands in `3 tensor Sym^n(3)` also fails
  exactly for every `n`; this includes the first `M_8->M_3` factor. Other qutrit couplings remain
  open.
- The next nonsymmetric coupling `3 tensor 8` is fully closed as well. Its `bar6` channel has
  exact `S_min=1` and Bell entropy `h_2(1/4)+9/4`, while the other two summands are excluded by a
  product vector or the small-input theorem.
- The conjugate-symmetric tower `3 tensor Sym^n(bar3)` is also classified: the first lower summand
  saturates and every nontrivial lower summand has a strict negative Bell defect.
- These calculations extend to all mixed highest weights. An exact Pieri theorem excludes every
  qutrit channel obtained from a single irreducible summand in `3 tensor V_(p,q)`.
- The classification now also covers every invariant direct sum inside the same product. The only
  new two-lower-sector subspace has an exact Gram formula and a strict explicit-input entropy
  no-go.
- Arbitrary equivalent-copy multiplicity `V_(p,q) tensor C^m` is closed by an exact convex Gram
  reduction.
- Mixtures of inequivalent environments are also closed on the two boundary input towers
  `V_(r,0)` and `V_(0,r)`.
- For interior `V_(r,s)`, the last irreducible-input covariant Bell gate reduces to the explicit
  classical inequality `B((1/8)chi^2(lambda||mu))>=2H(lambda K_(r,s))`, and that inequality is now
  proved with certified rational-log endpoints. Thus every irreducible-input `SU(3)`-covariant
  qutrit channel is excluded; only reducible-input cross-irrep coherence remains within covariance.
- The smallest reducible-input cross-irrep coherence pattern, a 24-dimensional six-edge branching
  cycle, is also excluded by a certified 4096-box rational entropy proof.
- More strongly, every translation of that elementary Pieri hexagon is excluded for all integer
  representation labels and all continuous edge weights by a 204-leaf compact rational
  Bernstein/logarithm certificate.
- Every adjacent elementary two-face family is now excluded. The three unoriented shared-edge
  types are covered separately: middle edge by a 12-branch, 1,098-leaf certificate; conjugate edge
  by a 12-branch, 996-leaf certificate; and highest edge by an eight-branch, 4,216-leaf
  simplex-aware certificate. A covariant survivor must therefore use at least three faces,
  repeated vertices, cycle multiplicity, or another larger-graph effect.
- Connected triples of distinct elementary faces are classified into three straight, six bent,
  and two triangular orientations. Six of the 11 atomic directions now have exact certificates:
  three are independently `PROVED` and three remain proposer-side `CONJECTURED`. The bent-right
  ternary result is a 24-branch, 13,744-box six-dimensional certificate with strictly positive
  exact margin displayed approximately as `4.870629792869e-05`. The other five orientations retain
  positive full-incidence numerical filters but are not exact results. Straight-reduced-coordinate
  is precisely blocked at a full-depth width-`1/1024` box after a depth-10 exact replay; the
  negative lower-enclosure diagnostic is not a mathematical counterexample. Bent-central's
  depth-10 replay was user-stopped at `10000/4992/15` and produced no terminal verdict.
  None of the three orientation-conjunction parents is upgraded.
- Noncovariant qutrit factors and non-Bell inputs remain outside this classification.

So the rigorous project boundary is:

\[
 \text{absolute-unbounded: PROVED},\qquad
 \text{full-size extensive: still open}.
\]

## Exact remaining target

Prove or refute positive regularized MOE defect for one fixed finite channel and its conjugate, or
find a genuinely collective non-Bell construction whose gap pays for every introduced dimension.

Canonical nodes: `HEXT.absolute-unbounded-finite-dimensional-defects`,
`HEXT.finite-dimensional-unbounded-gap`,
`HEXT.isotropic-bell-one-bit-cap`, `HEXT.fixed-d-heterogeneous-selection`,
`HEXT.conjugate-bell-realignment-constraint`, `HEXT.gram-channel-correlation-identities`,
`HEXT.gram-channel-entanglement-cost-gate`, `HEXT.flower-state-gram-gate`,
`HEXT.support-channel-polar-orientation-criterion`,
`HEXT.partial-support-polar-orientation-criterion`,
`HEXT.qutrit-antisymmetric-gram-obstruction`, `HEXT.g2-antisymmetric-square-support-no-go`,
`HEXT.octonionic-hurwitz-support-no-go`,
`HEXT.pauli-gram-high-cost-side-obstruction`,
`HEXT.qubit-output-gram-bell-no-go`, `HEXT.depolarizing-gram-small-input-no-go`,
`HEXT.su3-symmetric-complement-bell-no-go`, `HEXT.su3-adjoint-environment-bell-no-go`,
`HEXT.su3-conjugate-symmetric-complement-no-go`,
`HEXT.su3-irreducible-covariant-bell-no-go`,
`HEXT.su3-reducible-pieri-subspace-bell-no-go`,
`HEXT.su3-equivalent-environment-multiplicity-no-go`,
`HEXT.su3-boundary-environment-mixture-bell-no-go`,
`HEXT.su3-inequivalent-environment-mixture-reduction`,
`HEXT.su3-interior-environment-mixture-bell-no-go`,
`HEXT.su3-minimal-covariant-cycle-bell-no-go`,
`HEXT.su3-all-elementary-cycles-bell-no-go`,
`HEXT.su3-adjacent-elementary-faces-bell-no-go`,
`HEXT.su3-conjugate-edge-adjacent-faces-bell-no-go`,
`HEXT.su3-highest-edge-adjacent-faces-bell-no-go`,
`HEXT.su3-all-adjacent-elementary-face-pairs-bell-no-go`,
`HEXT.unbounded-family-self-leakage`, and `HEXT.goal`.

This folder is unrelated to the completed WHGAP capacity-threshold project.
