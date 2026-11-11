# Weighted orbit frames: prior-art mapping and remaining research choices

Date: 2026-09-07. Scope: bounded primary-source positioning of
`GROTHORB.weighted-isotropic-optimum` (registration C11), with a priority
follow-up on `GROTHORB.minimum-settings-isotropic` (registration C12).
This document is a literature/mapping note, not an independent mathematical
review of C11 or C12, a proof of a new statement, or a novelty certificate. No node,
author proof, earlier manuscript, or other project was modified. Source
statements below were checked in the linked original papers; mappings and
research choices are explicitly identified as local interpretation.

The assessed C11 claim uses positive integer r,m,n, unit vectors a_i,b_j,
positive weights u_i,v_j, S=sum u_i, T=sum v_j, weighted frame operators
(S/r)I and (T/r)I, and M_ij=u_i v_j(a_i dot b_j). It proposes
beta_vec(M)=ST/r. The inspected claim SHA-256 is
`efc68dff78220733c250b60537c17019339c6229129c7cd7235e033a06f83490`.

The positioning judgment is that C11 should be presented as a useful
weighted diagonal-SDP-dual certificate. Its unweighted rectangular case has
an explicit prior counterpart, while arbitrary positive weights fit an
established diagonal-dual interface. I did not verify that the exact wording
of C11 already appears as a separately named theorem. The distinction does
not support presenting its vector-value mechanism as new.

## WL-1: explicit rectangular frame and orbit precedents

[Pál and Vértesi, *Platonic Bell inequalities for all dimensions*,
Quantum 6, 733 (2022), arXiv:2112.03887](https://arxiv.org/pdf/2112.03887),
Section 4, Observation and Eqs. (3)--(7), PDF pp. 5--6: the constraint is
sum_i V_ij V_ik=(m/d)delta_jk. Their coefficients are
M_ij=A_i dot B_j. Eq. (5) gives the construction-strategy value m_A m_B/d;
the singular-value argument in Eqs. (6)--(7) proves optimality when both
sides satisfy the constraint. The paragraph between Eqs. (5) and (6)
explicitly allows different groups on the two sides. Mapping:
`d=r, m_A=m, m_B=n, A_i=a_i, B_j=b_j, u_i=v_j=1`.
Rectangularity and absence of a common transitive group are already covered.

[Bolonek-Lasoń and Kosiński, *Groups, Platonic solids and Bell inequalities*,
Quantum 5, 593 (2021), arXiv:2009.04347](https://arxiv.org/pdf/2009.04347),
Section 2: Eq. (12) gives N_A N_B/3 for the orbit construction; Eqs.
(15)--(18) express its isotropic second moments. Eqs. (21)--(23) formulate
the classical problem through signed orbit sums. Table 1, PDF p. 7,
already compares unequal orbit pairs such as cuboctahedron/tetrahedron.
Their Bell-sign convention is absorbed by reversing all Alice signs.
These are direct precedents for different finite orbit sets, not just a
single square root Gram matrix. The weighted all-r wording of C11 is not
the literal scope of these three-dimensional formulas.

## WL-2: Epping's exact overlap and its boundary

[Epping, Kampermann and Bruß, *Designing Bell inequalities from a Tsirelson
bound*, PRL 111, 240404 (2013), arXiv:1306.3805](https://arxiv.org/html/1306.3805),
Theorem 1/Eq. (5), gives sqrt(M_1 M_2)||g||_2. Theorem 2/Eqs. (9)--(12)
characterize tightness through a shared factor alpha and normalized rows;
Corollary 1/Eqs. (13)--(14) supplies the constant-row-norm case. Appendix A
relates factor rank to real vector dimension; Appendix B rewrites the
normalizations with X=alpha alpha^T.

For C11 with unit weights and row matrices A,B, the source substitution is

```
g=AB^T, M_1=m, M_2=n, d=r,
V^d=sqrt(r/m) A, W^d=sqrt(r/n) B,
||g||_2=sqrt(mn)/r, alpha=sqrt(m/r) I_r.
```

Thus the unweighted claim is already a spectral-tightness instance. For
unequal positive weights, applying that unweighted spectral bound directly
to the raw M does not automatically give ST/r: weighted isotropy is not
constant row normalization of M's ordinary singular bases. The appropriate
general prior interface is the diagonal dual below, rather than an
unexplained invocation of Corollary 1.

## WL-3: arbitrary positive weights fit the established diagonal dual

[Wehner, *Tsirelson bounds for generalized Clauser-Horne-Shimony-Holt
inequalities*, PRA 73, 022110 (2006), arXiv:quant-ph/0510076](https://arxiv.org/pdf/quant-ph/0510076),
Section 2, PDF pp. 4--5, explicitly writes the Gram SDP and its diagonal
dual `min Tr diag(lambda)` subject to `diag(lambda)-W/2 >= 0`.
Her lambda is a dual vector, not this project's shift parameter.

For a directly rectangular formulation, see
[Slofstra, *Lower bounds on the entanglement needed to play XOR non-local
games*, JMP 52, 102202 (2011), arXiv:1007.2248](https://arxiv.org/pdf/1007.2248),
Section 3, PDF p. 9, displayed primal (P) and dual (D) preceding the proof
of Theorem 3.1. In the present unnormalized notation the dual is

```
min 1/2 (sum_i c_i + sum_j d_j),
subject to [Diag(c), -M; -M^T, Diag(d)] >= 0.
```

The source uses normalized game coefficients G. Set
`Z=sum_ij |M_ij|`, `G=M/Z`, and divide c,d and the objective by Z to
match that convention. The model is already m by n.

The following is the **local variable mapping** of C11 into this known
certificate interface; it is not a separate correctness review:

```
c_i=(T/r)u_i,                       d_j=(S/r)v_j,
P_(i,*)=sqrt(r u_i/S) a_i^T,         Q_(j,*)=sqrt(r v_j/T) b_j^T,
P^T P=Q^T Q=I_r,
Diag(c)^(-1/2) M Diag(d)^(-1/2)=P Q^T,
1/2 (sum c_i + sum d_j)=ST/r.
```

This identifies the standard dual candidate and its normalized cross block.
The author's C11 proof and a different reviewer must check feasibility and
the matching strategy in their own assembled dossier. Establishing them
is an application of the existing dual framework, not a new optimization
principle. Positive real weights cause no rational-replication restriction:
the displayed source interface accepts real diagonal entries.

## WL-4: the generic classical and rank machinery is also prior art

For the classical side, [Pál--Vértesi, Section 5, Eqs. (9)--(11) and the
geometrical-strategy construction, PDF pp. 8--10](https://arxiv.org/pdf/2112.03887),
allow nonunit construction vectors. Set their A_i=u_i a_i and
B_j=v_j b_j. Their fixed-rank hyperplane-arrangement method therefore
already applies to weighted rectangular M. This note does not claim that
merely replacing 2^n enumeration by geometric sign patterns is a new
algorithm, nor convert their arithmetic-operation discussion into an
unverified bit-complexity guarantee.

For dimension, [Epping et al. (2013), Example 4, Eq. (30) in the checked
HTML version](https://arxiv.org/html/1306.3805), already constructs a
rectangular matrix by stacking orthogonal bases and discusses full vector
dimension via independent ellipsoid constraints. Random basis unions and
quadratic-span uniqueness alone are therefore poor novelty targets.

[Epping et al., *Optimisation of Bell inequalities with invariant Tsirelson
bound* (2014), arXiv:1402.0378](https://arxiv.org/pdf/1402.0378),
Theorem 1/Eqs. (8)--(9), restates the factor criterion. Section 3,
Corollary 1/Eqs. (10)--(12), already varies singular vectors/values while
retaining a tight quantum bound; Section 4.3 studies bounded vector
dimension. A relative rotation or preserved quantum numerator is not by
itself a new optimization method.

[Gatermann and Parrilo, *Symmetry groups, semidefinite programs, and sums
of squares*, arXiv:math/0211450](https://arxiv.org/pdf/math/0211450),
Theorem 3.3, PDF pp. 8--9, preserves an invariant convex SDP's optimum under
fixed-point restriction. It is not a theorem preserving minimum matrix
rank. Any proposed orbit-rank computation must handle unrestricted
optimizers, not only invariant matrices.

Finally, [Slofstra (2011), Proposition 2.9 and its following paragraph,
PDF p. 6](https://arxiv.org/pdf/1007.2248), explicitly separate minimum
entanglement from optimal-correlation rank. A real-vector-rank result must
not be advertised as minimum physical Hilbert-space dimension without
additional hypotheses and an appropriate theorem.

## WL-5: potential frontiers that require a concrete family

The checked general results determine the numerator or provide methods;
they do not supply every family-specific classical value or rank minimum.
The following are **research questions to register and scope**, not claims
that the literature has left them open. No new experiment or proof was
started in this positioning task.

1. **An exact classical parameter diagram for specified orbit unions.**
   Fix a finite group representation, explicit seed vectors on each side,
   a rectangular pair of orbit unions, and an exact one- or two-parameter
   weight domain. Seek the complete maximum, every transition locus,
   matching signs, and an independently checkable upper certificate.
   Choosing two orbit unions whose relevant signed-sum geometry is not
   identical is a more demanding target than reusing one common root
   chamber. The deliverable must identify the particular family and compare
   its formulas with existing orbit tables. A numerical weight sweep or the
   observation that finitely many scores have an upper envelope does not
   meet this target.

2. **Certified optimization of the classical denominator under a fixed
   vector numerator.** Normalize S and T and specify allowable relative
   rotations or orbit weights. Determine the global infimum of beta_cl and
   all parameters attaining it, with a proof across the whole domain.
   The substance would be a global certificate and an exact new family
   value, not preserving ST/r or running local optimization. The search
   must also rule out row/column relabelings, sign changes, antipodal
   duplication, or scaling of an already treated matrix before making a
   construction claim.

3. **Exact unrestricted minimum vector rank for a deterministic family
   with nonunique feasible factors.** Select a concrete multi-orbit or
   rectangular construction whose optimal-factor constraints are not
   already forced to a unique full-rank matrix by quadratic spanning.
   The target should be an explicit minimum-rank formula, a lower
   certificate, and matching strategies, including singular parameter
   values. First register and establish the correct factor-space
   equivalence for that weighted family; C11 alone gives an attaining
   r-dimensional strategy, not a minimum. Do not assume that changing only
   positive weights while keeping all directions fixed supplies rank
   control. Any invariant/unrestricted difference must be proved directly.

4. **A demonstrated improvement over fixed-rank sign enumeration.**
   For one of those registered families, specify rational/algebraic input
   encoding, treatment of coincident hyperplanes and ties, certificate
   size, and total bit complexity. A useful result would exploit orbit
   structure to give a proved improvement over the existing general
   geometric method or a uniform all-r formula. No claim of improved
   complexity follows from symmetry or small numerical runtimes alone.

Of these, the first is the most concrete continuation: the vector value
can serve as established setup once C11 passes its separate review, while
the exact classical diagram supplies a falsifiable deliverable. The third
is appropriate only after a nontrivial deterministic factor-feasibility
family is actually specified. At present this note certifies neither a
novel example nor an open problem.

## WL-6: search and scope limitations

This bounded pass checked original texts for diagonal SDP duality,
singular-value tightness, rectangular frame constructions, orbit classical
sums, fixed-rank classical computation, symmetry reduction, and vector-rank
versus physical-resource boundaries. It did not exhaust databases or
reproduce external software. Primary papers were read online; theorem
locators refer to the linked versions, whose printed/HTML equation
numbering can differ.

The phrase "two orbits" alone is not a model match. For example,
[Bolonek-Lasoń--Kosiński, *Bell inequalities for S4 group: classical and
quantum bounds for two orbits case*, arXiv:1907.10437v2](https://arxiv.org/pdf/1907.10437),
Section II, Eqs. (2)--(9), encodes basis outcomes and sums joint
probabilities. It must not be treated as the same weighted dichotomic
cross-Gram problem merely from its title. It is adjacent prior art requiring
a separate observable/outcome mapping for any claimed comparison.

The absence of a selected concrete family's formula from the inspected
sections is not evidence that no paper contains it. Each chosen next family
requires a focused follow-up search before any novelty wording.

## WL-7: C12's optimal setting count and explicit construction are prior art

The inspected C12 claim has SHA-256
`dc1b7a167caab8ad27dc638a70586b4bc98bd3f56fc3b4b66a2854e2e9a35aef`.
It asks for the minimum m+n among nonempty positive isotropic unit-frame
pairs with injective combined quadratic measurements, and proposes
`m+n=r(r+1)/2+1` with Alice the standard basis and Bob the normalized
pairwise differences plus normalized all-ones vector. This follow-up read
the registered statement, not the author's proof, and supplies no review
verdict for that proof.

[Gribling, de Laat and Laurent, *Matrices with high completely positive
semidefinite rank*, arXiv:1605.00988](https://arxiv.org/pdf/1605.00988):
Theorem 3.5/Eq. (4) is the outer-product spanning criterion; Theorem
3.9(ii)/Eq. (7) uses positive balancing coefficients. C12 maps to these
with `x_i=a_i, y_j=b_j, lambda_i=u_i/S, mu_j=v_j/T`.
Corollary 3.10/Eq. (8), PDF p. 12, gives
`r(r+1)/2 <= m+n-1`. Section 3.3's first construction and Theorem
3.11(i), PDF pp. 12--14, attain it with exactly C12's directions and
`m=r, n=binom(r,2)+1`. Their matrix `B=[(e_i-e_j)_{i<j}, e]` satisfies
`BB^T=rI`; column normalization of `B/sqrt(r)` gives precisely Bob's
weights `2/r` and `1`. Their positive-direction theorem statement is
unambiguous; intermediate cross-block sign conventions do not change
outer products. This is direct overlap, not merely a similar cardinality.

An independently accessible repetition is [Gribling's thesis, Section
6.2.3](https://ir.cwi.nl/pub/28887/Thesis_S_Gribling.pdf), printed pp.
111--113: Corollary 6.11/Eq. (6.6), the first construction, and Theorem
6.12(i). It attributes the rank bound to Tsirelson and points to
Vértesi--Pál [VP09] for the same family through optimization. This note
checked the displayed bound in Gribling--de Laat--Laurent, not Tsirelson's
1993 original; it does not upgrade that attribution into an independent
reading of the earlier paper.

The earlier optimization match is also explicit. [Vértesi and Pál,
*Bounding the dimension of bipartite quantum systems*, PRA 79, 042106
(2009), arXiv:0812.1572](https://arxiv.org/pdf/0812.1572), Section III.B,
PDF p. 5, Eq. (19), uses pair-difference coefficients and a gamma-weighted
all-ones term. Eq. (22) and the paragraph following Eq. (24) identify
`gamma=sqrt(m_B/2)` as the orthogonal-vector case. Swap parties, put
`m_B=r`, `gamma=sqrt(r/2)`, and scale their coefficient matrix by
`sqrt(2)/r`. Its columns become

```
(sqrt(2)/r)(e_i-e_j),      e/sqrt(r),
```

which are exactly C12's weighted directions when inserted into C11's
`M_ij=u_i v_j(a_i dot b_j)`. Eq. (25) and its following paragraph already
give the full classical maximum
`max_{0<=k<=r} [2k(r-k)+gamma*abs(r-2k)]`; multiply by `sqrt(2)/r`
for this project's normalization. Thus the exact classical denominator
of this particular C12 matrix is not a remaining frontier either.

The Slofstra comparison is distinct: Gribling--de Laat--Laurent Section
3.3's second construction, Theorem 3.11(ii), explicitly relates to
Slofstra Section 7.2 and has rank r-1, rather than C12's first family.
Wehner's diagonal dual and Epping's factor constraints remain relevant
general mechanisms (WL-2--4), but the direct construction references above
are much sharper for this candidate.

Positioning conclusion: C12 can be retained as an audited framework
corollary and explicit prior-art example; neither the optimal total count
nor its proposed directions/weights should be presented as a new setting-
economy construction. This is a definite overlap finding, not a claim
that the bounded search failed to find novelty. It does not assert a
minimum over all Bell scenarios, a physical self-testing result, or a new
Hilbert-space dimension theorem. The potential questions in WL-5 require
a genuinely different, precisely specified family; this C12 construction
does not furnish one.
