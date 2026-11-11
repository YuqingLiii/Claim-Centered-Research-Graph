# Bounded literature positioning of the minimum-budget equality criterion

Date: 2026-09-07. Scope: source comparison for C14, not a correctness
review, new proof, numerical experiment, or originality certificate.
Four primary papers were selected; locators below refer to the specified
arXiv versions, not automatically to the journal pagination. No claim,
author artifact, previous note, or dimension-specific construction was
changed.

## EL-1: exact target and input binding

Target: `GROTHORB.minimal-conditioning-equality`, route-free.
SHA-256 of the decoded YAML `claim.strip()` in UTF-8:

`1808e5956926e46c72702359a6273694b3c8bfbbc3389693fd67ce358b6660e1`.

The complete node and author artifact were read for scope. Input byte
hashes, relative to `grothendieck-group-orbit/`, were:

| Input | SHA-256 |
|---|---|
| `proof-dag/nodes/GROTHORB.minimal-conditioning-equality.yaml` | `f35746c6bdf82ef1135a955ff24f3ac643eb8c01f4a1846f2d0c942ab5967216` |
| `artifacts/minimal-conditioning-equality-20260907.md` | `f6e1d7d3498abbfb1722bbd45bcaedc5f4ec2c0654a90f9eec86ebe613cd93e4` |
| Existing independent review, `reviews/minimal-conditioning-equality-review-20260907.md` | `75e96a14db3adc9c47ced118226827de45bd0569b7eccc5b145b9aa9f861444b` |

The third hash records the existing review artifact's identity; this note
does not replace or repeat that correctness review.

With `R=r(r+1)/2`, C14 assumes two positive real isotropic unit frames,
`m>=n`, `m+n=R+1`, and joint quadratic-measurement injectivity on
`Sym_r`. For their centered frame operators, it characterizes
`lambda_min(F_A+F_B)=c=(r-1)/(m-1)` by: equal Alice weights `r/m`,
Alice ETF squared overlaps `(m-r)/(r(m-1))`, all cross squared overlaps
`1/r`, and `F_B|span{g_j} >= c I`. The last condition is a spectral
floor, not an assertion that Bob is an ETF.

## EL-2: the generic spectral mechanism is not a new principle

Author sections CE-3--5 organize equality in the PSD compression bound
already positioned in `weighted-orbit-literature-correction-20260907.md`,
WC-3. That frozen supplement has SHA-256
`cbb7ef1f419bbbf3e49d9fa8ea6ffb6d9f5e3527832c65fa17c6acf4fd5dc29c`.
No fifth primary paper is introduced here.

The pertinent generic equality data are support orthogonality, a scalar
operator on the compressed block, and a lower spectral bound on the
complementary block. CE-3 then translates these into centered-projector
orthogonality and CE-4 uses the one-dimensional synthesis kernel to
recover weights and overlaps. This identifies C14 as an elementary
specialization of standard PSD/Gram-matrix equality reasoning. It does
not identify a published theorem asserting the complete same-domain
four-condition iff. Those are different prior-art questions.

## EL-3: direct real MUETF overlap, including the balanced case

Matthew Fickus and Benjamin R. Mayo, *Mutually Unbiased Equiangular Tight
Frames*, IEEE Transactions on Information Theory 67(3), 1656--1667
(2021); [author-institution publication record](https://scholar.afit.edu/facpub/844/).
In [arXiv:2001.02055v1](https://arxiv.org/pdf/2001.02055v1), Section III,
Definition 3, Eq. (15), printed p. 4, the within-frame and cross-frame
squared overlaps are exactly

```
(N-D)/(D(N-1)),      1/D.
```

The rank-one-projector Gram calculation immediately following gives
rank `M(N-1)+1`; Eq. (16) and Theorem 1 bound this by `D(D+1)/2` over
the reals. Map `D=r`, `N=m`, and `M=2` when C14 has `m=n`. In that
balanced case, CE-6's trace constraint makes Bob's spectral floor scalar,
and the same weight/Gram characterization applies to Bob. Thus the
equality geometry is a pair of real MUETFs saturating that published
dimension bound. This is a direct structural precedent, not a new name
or geometry. The paper's equal-cardinality ETF premise does not state
C14's general asymmetric weighted conditioning iff.

## EL-4: unbiased frames need not both be equiangular

F. Caro Perez, V. Gonzalez Avella and D. Goyeneche, *Mutually unbiased
frames*, Quantum 6, 851 (2022),
[arXiv:2110.08293v2](https://arxiv.org/pdf/2110.08293v2), Section 3,
Definition 4/Eq. (3), printed p. 4, defines constant cross squared
overlaps for frames with possibly different sizes `n1,n2`. This directly
names C14's cross condition under `d=r,n1=m,n2=n,c_overlap=1/r`.
Proposition 1 and Corollary 1, p. 5, relate overlap to ordinary frame
bounds, with overlap `1/d` if one frame is tight in the stated
equal-cardinality corollary. They do not provide C14's centered-operator
spectral floor or minimal total budget. A positively weighted isotropic
frame must not silently be treated as an unweighted unit-norm tight
frame.

## EL-5: equal-weight ETF and real projective-design precedents

Christine Bachoc and Martin Ehler, *Tight p-fusion frames*,
[arXiv:1201.1798v2](https://arxiv.org/pdf/1201.1798v2), Section 3.2,
Theorem 3.4/Eqs. (10)--(11), printed pp. 5--6, characterizes equality
in weighted fusion-potential/simplex bounds. Corollary 3.5, p. 6,
characterizes equiangular tight fusion frames of equal subspace dimension
by constant weights and projector overlap `k(nk-d)/((n-1)d)`.
Substitute `k=1,d=r,n=m`, `V_i=span(a_i)` and weights `u_i`:
the overlap becomes exactly C14's Alice formula. Its isotropic
normalization fixes the common weight at `r/m`.

For design comparison, Section 5.3, Definition 5.5/Eq. (24), p. 13,
and Theorem 5.7/Eq. (26), p. 14, characterize positive cubature and
fusion-potential equality on real Grassmannians. For rank-one lines,
their strength-four convention corresponds to degree-two projective
moments. These are full moment identities, not a floor on one residual
block. Their objective is potential/coherence, not C14's smallest
eigenvalue. In particular, C14's asymmetric conclusion does not license
calling the whole union a real projective 2-design. The rank-one fusion
frames in this mapping are the original lines; C14's centered ranges
instead live in traceless `Sym_r`.

## EL-6: a particularly close grouped-operator iff, with essential differences

Katarzyna Siudzińska, *Equivalence relations between conical 2-designs
and mutually unbiased generalized equiangular tight frames*, Mathematics
14, 128 (2026), [arXiv:2509.17261v2](https://arxiv.org/pdf/2509.17261v2).
Section 5, Definition 3/Eqs. (43)--(46), printed pp. 7--8, allows
unequal group sizes and obtains normalized cross overlap `1/d`.
Section 6, Theorem 3, p. 14, assumes `N` GETFs spanning `B(C^d)` with
`|R|=d^2+N-1`; their union is a conical 2-design iff the GETFs are
equidistant and mutually unbiased. Definition 4/Eq. (58), p. 9,
specifies equidistance through `S_alpha=a_alpha^2(b_alpha-c_alpha)`.

The analogous two-group count is `d^2+1`, but C14 spans real `Sym_r`,
not all complex Hermitian operators. This theorem also presupposes a
GETF in every group and characterizes globally flat traceless spectrum
(Definition 1/Eq. (2)), unlike C14's one-sided scalar block plus Bob
floor. Finally, using POVM elements `u_i a_i a_i^T` in its quadratic
operator sum produces `u_i^2`, not C14's `u_i`; square-root rescaling
matches the latter but need not preserve GETF group normalization.
Consequently the theorem is close prior art, not a verbatim C14 theorem.

## EL-7: bounded conclusion

There is positive evidence for substantial known structure: the ETF
overlap/equal-weight condition, unbiased cross geometry, balanced
saturated real MUETFs, and closely related grouped-operator design iff
theorems. These should be credited rather than presented as discoveries.
The general spectral compression mechanism likewise has no novelty
content by itself.

No statement of the complete C14 iff under its same two-positive-real-
isotropy, `R+1` setting budget, and asymmetric residual spectral-floor
hypotheses was located in the inspected passages of these four papers.
This is a bounded retrieval result, not a claim that no paper contains
it, and not an originality certificate. Nor does the presence of a
nearby conical-design iff establish identical coverage without the
missing domain and weighting translations.

Defensible positioning: an already correctness-reviewed framework
equality lemma with explicitly documented standard ingredients and
structural predecessors; originality remains unestablished. This note
does not investigate attainability in any dimension, define a new
frontier, or imply physical self-testing, a minimum physical dimension,
or a noise-stability guarantee.
