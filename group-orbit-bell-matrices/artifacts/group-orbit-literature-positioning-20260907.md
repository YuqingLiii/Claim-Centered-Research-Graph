# Group-orbit Bell/XOR literature positioning

Date: 2026-09-07. Scope: bounded primary-source comparison of the staged
`complete-extremizer-classification-20260829.md` (GOC-T1--T8) and
`balanced-rank-theorem-draft-20260829.md` (GO-T1--T9).

This is a source note, not an independent mathematical review or a novelty
certificate. No claim node, assessment, or canonical artifact was changed.
The theorem locators below were checked in source text, except for the
explicitly identified Tsirelson-original access limitation.

## L1. The spectral bound and full weighted tightness criterion are prior results

[Epping, Kampermann, Bruß, *Designing Bell inequalities from a Tsirelson bound*,
PRL 111, 240404 (2013), arXiv:1306.3805](https://arxiv.org/pdf/1306.3805):

- Theorem 1, Eq. (5): the bound `sqrt(mn) ||A||_op`.
- Theorem 2, Eqs. (9)--(12), and Appendix A: necessary and sufficient
  normalization conditions on a shared factor in the paired top singular
  spaces, including dimension `d'`.
- Appendix B, Eqs. (B1)--(B4): the quadratic conditions are explicitly
  rewritten with the PSD variable `X=alpha alpha^T`.
- Corollary 1, Eqs. (13)--(14): constant squared row norms of both truncated
  singular bases suffice for tightness.

Exact translation to GOC notation: their `V^d=U`, `W^d=V`, `M1=m`, `M2=n`;
set `T=sqrt(n/m) alpha`, hence `H=(n/m) alpha alpha^T`. Their conditions
become precisely `H in S(A)`. The minimum-factor-rank interpretation and
complete factor parametrization therefore already follow from their theorem.
GO-T1--T2 and GOC-T1--T3 should be presented as a reformulation of this result.
GO-T3 supplies the elementary constant-diagonal argument, making GO-T4/GOC-T4
a direct transitive-symmetry corollary of Corollary 1. No priority claim for
that corollary follows from this bounded search.

## L2. Spectral modifications and dimension witnesses are also established

[Epping, Kampermann, Bruß, *Optimisation of Bell inequalities with invariant
Tsirelson bound* (2014), arXiv:1402.0378](https://arxiv.org/pdf/1402.0378):
Theorem 1, Eqs. (8)--(9), restates the factor criterion and its dimension
interpretation. Section 3, Corollary 1, Eqs. (10)--(12), gives admissible
singular-vector rotations and changes of singular values while retaining a
tight bound. Thus spectral design, dimension witnessing, or changing lower
singular values alone is not a new general mechanism. A project claim needs
a specific additional family, classification, algorithmic guarantee, or bound.

## L3. Vector rank is distinct from minimum physical resources

[Slofstra, *Lower bounds on the entanglement needed to play XOR non-local
games*, JMP 52 (2011), arXiv:1007.2248](https://arxiv.org/pdf/1007.2248):

- Theorem 2.5 restates Tsirelson's vector characterization; the adjacent
  Clifford construction realizes rank `s` using local dimension
  `2^floor(s/2)`.
- Theorem 2.3 characterizes optimal nondegenerate strategy marginals by
  representations of the solution algebra, assuming no zero rows/columns.
  Corollary 2.4 determines minimum entanglement from its smallest nonzero
  representation.
- Theorem 2.7 attributes to Tsirelson the Clifford structure and
  `floor(r/2)`-ebit lower bound for an **extreme** rank-`r` quantum correlation.
- Proposition 2.8 relates a unique optimal correlation to a Clifford solution
  algebra. Proposition 2.9 exhibits a gap between minimum entanglement and
  the best Clifford strategy; its following paragraph explicitly rejects
  determining minimum entanglement from optimal-correlation rank in general.
- Proposition 2.11, Theorem 2.12, and Corollary 2.13 already study stability,
  approximate representations, and robust dimension lower bounds.

GOC-T7 correctly states an explicit dimension upper bound, not physical
minimality. The wider optimal-quantum-strategy problem already has a general
algebraic framework; an orbit-specific result must add information to it.

Original attribution: [Tsirelson's author-hosted 1987 paper page](https://www.ma.huji.ac.il/~ohadfeld/Tsirelson/download/qbell87.html),
*Quantum analogues of the Bell inequalities. The case of two spatially
separated domains*, Journal of Soviet Mathematics 36, 557--570. The original
scan could not be reliably opened for theorem-number verification in this
pass; the exact verified locators used above are Slofstra's Theorems 2.5 and
2.7, not guessed locators in the original.

## L4. Existing self-testing and robustness results constrain positioning

[Miller and Shi, *Optimal Robust Self-Testing by Binary Nonlocal XOR Games*,
TQC 2013, pp. 254--262](https://drops.dagstuhl.de/storage/00lipics/lipics-vol022-tqc2013/LIPIcs.TQC.2013.254/LIPIcs.TQC.2013.254.pdf):
Propositions 2--3 characterize their self-testing condition and the
nonsingular-Hessian criterion for `O(sqrt(epsilon))` robustness; Proposition 4
extends the robustness conclusion to arbitrary finite-dimensional strategies.
Their binary-input model allows two measurements per party, so this is not
automatically an arbitrary-`m x n` theorem.

[Zhao, *Robust self-testing for nonlocal games with robust game algebras*,
arXiv:2411.03259v1 (2024)](https://arxiv.org/html/2411.03259v1):
Theorem 6.17 states that an XOR game self-tests its optimal quantum strategies
iff it has a unique optimal quantum correlation and its associated XOR
correlation has even rank. The definition is in Definition 3.4; retain this
physical equivalence convention, including its treatment of complex
conjugation, when applying the parity condition. Proposition 7.12(2) gives an
`O(epsilon^(1/4))` robust determining pair for XOR games; Theorem 7.14 gives
robust self-testing for extreme unbiased quantum correlations of even XOR
rank. Theorem 9.2 provides a quantitative algebraic route.

Consequently, Gram-factor uniqueness and physical self-testing must be
distinguished. Any quantitative orbit theorem needs a declared distance,
normalization of score error, constants, and comparison with these results.
A spectral-gap leakage estimate by itself does not establish physical
self-testing or a new robustness theorem.

## L5. Verified real Schur and symmetry-reduction references

[Rosenberg, *Structure and applications of real C*-algebras*,
arXiv:1505.04091](https://arxiv.org/pdf/1505.04091), Theorem 1.3 and Corollary
1.4, p. 2, provide a proof-bearing reference that the commutant of an
irreducible real representation is `R`, `C`, or `H`. Apply this to the real
*-algebra generated by the orthogonal group representation. Passing to
isotypic multiplicities then yields matrix algebras over those division
algebras; a compatible adjoint identifies self-adjoint positive elements
with Hermitian PSD blocks. This last multiplicity/adjoint step is a standard
deduction to write out, not the literal statement of Theorem 1.3.

[Gatermann and Parrilo, *Symmetry groups, semidefinite programs, and sums of
squares*, arXiv:math/0211450](https://arxiv.org/pdf/math/0211450), Theorem 3.3
and its Reynolds-operator proof, pp. 8--9 of this version, justify replacing
a group-invariant convex SDP by its fixed-point restriction without changing
the optimum. This is an existence/optimization reduction, not a description
of all feasible points, and does not preserve a nonconvex minimum-rank
objective. GOC-T5's counterexample and GOC-T6's invariant-only scope therefore
address a real distinction, but averaging itself is established machinery.

## L6. What would make a follow-up question substantive

Plausible investigation targets, without asserting that they are unsolved:

1. Exact unrestricted minimum vector rank for a specified nontrivial orbit
   family, with lower bounds matching constructions; compare it explicitly
   with the minimum among invariant weights.
2. A classification of the family-specific optimal correlations or solution
   algebra that yields physical dimension or rigidity statements unavailable
   from the singular-value multiplicity alone.
3. Quantitative stability to the entire optimizer set, or physical
   self-testing where appropriate, with explicit dependence on orbit
   parameters and a demonstrable improvement over applicable prior bounds.
4. A representation-based algorithm with stated input model, bit complexity,
   and a proved saving for a concrete family beyond generic block
   diagonalization and SDP feasibility.

The present general spectral and factor statements are useful organizing
lemmas. This comparison supplies substantial direct prior art against
presenting them as the main original theorem. It does not establish novelty
for any of the follow-up targets; each needs its own focused comparison.
