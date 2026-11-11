# Bibliographic correction and bounded conditioning follow-up

Date: 2026-09-07. This supplement preserves without alteration
`weighted-orbit-literature-20260907.md`, whose frozen SHA-256 is
`68bb8d969cf4eecb367d9716e547956d6583aa4d9144b94dd1ece1513a18e378`.
It corrects a bibliographic error and records a bounded C13 prior-art
comparison. It is not a correctness review of C13 or an originality
certificate. No node or author proof is edited.

## WC-1: publication number correction

In WL-1 of the frozen note, the publication entry for Károly F. Pál and
Tamás Vértesi, *Platonic Bell inequalities for all dimensions*, incorrectly
reads **Quantum 6, 733 (2022)**. It must read **Quantum 6, 756 (2022)**,
published 7 July 2022, DOI **10.22331/q-2022-07-07-756**. These details were
verified against the [official Quantum publication page and its BibTeX
entry](https://quantum-journal.org/papers/q-2022-07-07-756/).
The linked arXiv identifier `2112.03887` and the intended paper are
unchanged. This bibliographic correction does not change the mathematical
comparison or promote any claim's evidence level.

## WC-2: C13 scope and inspected inputs

The follow-up concerns `GROTHORB.minimal-setting-conditioning` (C13),
claim SHA-256
`b2c7293343b8537e0ff7e26fe74d6ec1c6fe43fc7c6cb30e28fb4fb70309aa98`.
The inspected author file is `minimum-setting-conditioning-20260907.md`,
SHA-256
`9e8d2c030ff30e921de56897dd238d6dabc4dcc658a5157360b72569f4e2442a`.
Its Sections MC-1--4 define centered, positive semidefinite frame operators
F_A,F_B on traceless Sym_r, with q=r(r+1)/2-1, and propose

```
lambda_min(F_A+F_B) <= (r-1)/max(m-1,n-1).
```

This is an upper limit on a lower frame bound, not by itself a condition-
number estimate or a guaranteed tolerance to measurement noise. This
supplement checks source correspondence only: it does not independently
certify the author's rank computation, hypotheses, or proof conclusion.

## WC-3: the rank/trace mechanism is standard

[Liang, Wang, Zhang and Li, *On Generalizing Trace Minimization*,
arXiv:2104.00257v1](https://arxiv.org/pdf/2104.00257), Section 1,
Eq. (1.1), PDF pp. 1--2, recalls Ky Fan's trace-minimum principle
`min_(X*X=I_k) tr(X* A X)=sum_(i=1)^k lambda_i(A)`, with eigenvalues
ascending. This is a checked, explicit source for the compression
variational principle, not a claim that the 2021 paper originated it.

The generic consequence relevant to C13 is, for PSD operators A,B on a
q-dimensional space and k=dim ker(B)>0,

```
lambda_min(A+B) <= tr(P_ker(B) A)/k <= tr(A)/k.
```

The two inequalities are the Rayleigh/trace-compression average and
positivity of the omitted trace, respectively. This displayed consequence
is a local source mapping, not a verbatim theorem attributed to Liang
et al. MC-4 uses exactly this mechanism. Taking MC.7--8 as the author's
inputs, its substitutions are `A=F_A, B=F_B, k=m-1, tr(A)=r-1`, then
the exchanged pair. The formula's m,n dependence comes from the asserted
single-side ranks; the eigenvalue step is not a new spectral principle.

[Balan, Begué, Clark and Okoudjou, *Optimization methods for frame
conditioning and application to graph Laplacian scaling*,
arXiv:1609.02233](https://arxiv.org/pdf/1609.02233), Section 1, PDF
pp. 1--4, identifies optimal frame bounds with the extremal eigenvalues
of the frame operator and formulates scaling/conditioning optimization.
Map its frame vectors to `sqrt(u_i) f_i` and `sqrt(v_j) g_j` in the
q-dimensional Frobenius space. Its general conditioning framework is
prior art; the inspected section does not state C13's two-isotropy,
minimal-budget bound.

## WC-4: informational completeness and stability are related, not identical

[Scott, *Tight informationally complete quantum measurements*,
arXiv:quant-ph/0604049](https://arxiv.org/pdf/quant-ph/0604049),
Eq. (45), Definition 11/Eqs. (47)--(49), PDF pp. 8--9, uses centered
projectors P-I/d and their frame operator on traceless Hermitian
matrices. Eq. (54) gives the tight rank-one frame constant 1/(d+1).
Proposition 13 and the following paragraph, PDF p. 10, relate tight
rank-one IC measurements to weighted complex projective 2-designs and
minimal d^2-outcome SIC measurements. Lemma 17/Eqs. (94)--(97), PDF
p. 14, minimizes inverse-frame trace by flattening the nonidentity
spectrum, with a stated linear-tomography interpretation. Thus centered
operator frames, trace constraints, and spectral uniformity as a
reconstruction criterion are explicit precedents.

The domain distinction matters. C13 uses real symmetric matrices:
`dim V=r(r+1)/2-1`, not Scott's `d^2-1`. Its two separately normalized
families impose two centered dependencies, and its budget is `q+2`,
not the `q+1` outcome count of an ordinary minimally spanning normalized
operator frame. Under the formal POVM mapping

```
E_i=(u_i/2) a_i a_i^T,      E_(m+j)=(v_j/2) b_j b_j^T,
```

the combined centered frame operator is `F/2` on the real-symmetric
subspace. These real projectors do not span all complex Hermitian
matrices for r>=2. Scott's full complex IC theorem therefore cannot be
invoked unchanged to obtain C13's denominator `max(m-1,n-1)`, its exact
count, or a physical stability assertion.

## WC-5: evidence boundary and positioning

This bounded pass checked the above original texts and targeted queries
for minimal informational completeness, frame conditioning, and PSD
rank/trace smallest-eigenvalue bounds. No exact statement with C13's
two real isotropic frames, total count r(r+1)/2+1, and denominator
max(m-1,n-1) was located in the inspected passages. This is a limited
retrieval result, not evidence that no such publication exists.

Conversely, the standard spectral mechanism and established centered-
frame stability program are positively documented. The defensible
positioning is a scoped elementary framework consequence, with no
novelty claim based merely on the absence of the exact formula from this
search. A sharper attainable constant, equality classification, or
quantitative reconstruction guarantee would be separate questions; this
supplement neither investigates nor labels them open. No claim about
quantum self-testing or minimum physical dimension is made.
