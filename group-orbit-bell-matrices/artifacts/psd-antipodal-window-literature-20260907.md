# Bounded prior-art positioning of the PSD antipodal shift window

Date: 2026-09-07. This is a literature/model comparison for C15 and C16,
not a correctness review, new proof, numerical experiment, or novelty
certificate. Three primary sources were selected. The third was
accessible only at abstract level; that limitation is material.
No node, author proof, or previous artifact was edited.

## PL-1: exact registered targets

`GROTHORB.psd-antipodal-linear-window` (C15) asserts, for every real
symmetric PSD `N` by `N` matrix `C`, `N>=1`,

```
D(C) = (1/2)[C,-C;-C,C],
beta_cl(M) = max_{s,t in {+1,-1}^k} s^T M t,
beta_cl(D(C)-lambda I_(2N)) = 2 beta_cl(C)-2N lambda
    for 0 <= lambda <= (1/2) min_i C_ii.
```

Its decoded YAML `claim.strip()` SHA-256 is
`98c4958c91dace11088aaff1ecc7b590bb982f84cc5d26c027bc8a2603beda38`.
The inspected node byte hash is
`8958abb99db80f8c5aa8375cb470be757aa59144aabac9de2622f37679e4bcd3`.

`GROTHORB.root-extended-shift-window` (C16) asserts, for all `r>=3`,
the full-root matrix `A_r=WW^T/[4(r-1)]`, `n=2r(r-1)`, satisfies

```
beta_cl(A_r-lambda I_n) = 2r(2r-1)/3-n lambda
    for 0 <= lambda <= 1/[2(r-1)].
```

Its claim hash is
`df62de9a7c9c2c2dd4e5512ea89a3374d63f3c3bbb6e6d41f4eff509732f05db`;
the inspected node byte hash is
`904c12b4313e0d7ee8db0ad1f6617872d8f3c518d30fce8b1a32fb884c1dcf9a`.
The exact `psd-duplication-window` route `implication.strip()` hash is
`81735fbe09238f4c5e32f9448ef5d0e01af445de76cb04e4d7df5421e20545ca`.
These are statement bindings, not PASS verdicts or status promotions.

## PL-2: directly checked root benchmark

S. Designolle, T. Vértesi and S. Pokutta, *Better bounds on finite-order
Grothendieck constants*, [arXiv:2409.03739v3](https://arxiv.org/pdf/2409.03739v3),
Section II/Eq. (1), printed p. 2, defines `SDP_1` as exactly the
bilinear sign maximum here. Section III.B, pp. 4--5, and Table I use
unit-root Gram matrices `P` of size `r(r-1)` for `D_r`, i.e. one root
per antipodal pair. They study `P-mu I`; the displayed root benchmark
uses `mu=2/3`. Table I reports the shifted ratios
`4/3,7/5,10/7,13/9,16/11,19/13` for `r=3,...,8` without heuristic
asterisks. Section III.B attributes the first three cases and the base
family to Fishburn--Reeds and states its extension to `r=6,7,8`.
Section III.C/Eq. (9), p. 6, also explicitly eliminates one side of
the signs to obtain an absolute-row-sum maximum.

Thus the objective, root family, and half-root diagonal modification
have concrete prior counterparts. These passages do not state the
general-PSD antipodal theorem or an all-`r` full-root linear interval.
The distinction is the matrix and admissible signs, not a change of
notation for the same benchmark.

## PL-3: diagonal modifications preserve a quantum certificate, not a classical formula

M. Epping, H. Kampermann and D. Bruß, *Optimisation of Bell inequalities
with invariant Tsirelson bound*, J. Phys. A 47, 424015 (2014),
[arXiv:1402.0378v1](https://arxiv.org/pdf/1402.0378v1), Section 2/Eq. (2),
pp. 2--3, again uses independent deterministic signs for the classical
bound. Corollary 1(ii)/Eqs. (11)--(12), pp. 4--5, modifies singular
values while maintaining attainability of the specified quantum bound,
subject to its maximal-singular-space conditions. The paragraph after
the proof identifies `g'=g+delta I` when the singular bases coincide
as an earlier special case. It does not assert a universal affine
classical response to that modification.

Example 3/Eq. (22), p. 9, makes the root normalization explicit:
`g=V^d(V^d)^T-(4/3)I`, with `d(d-1)` rows of length `sqrt(2)`.
Under `V^d=U`, this is `2(P-(2/3)I)`, still the half-root matrix.
The subsequent optimization and Table 1 concern that family, not
`D(C)-lambda I_(2N)`. Consequently neither Corollary 1 nor the example
supplies C15's minimum-diagonal endpoint or its classical upper bound.

## PL-4: original root paper and the access boundary

P. C. Fishburn and J. A. Reeds, *Bell Inequalities, Grothendieck's
Constant, and Root Two*, SIAM J. Discrete Math. 7(1), 48--56 (1994),
[publisher record](https://epubs.siam.org/doi/abs/10.1137/S0895480191219350?journalCode=sjdmec),
DOI `10.1137/S0895480191219350`. The abstract directly confirms a
size-`k(k-1)` family approaching ratio `3/2` and a uniform diagonal
change yielding the size-20 ratio `10/7`.

The publisher PDF URL redirected to this abstract in the current pass;
the full original theorem statements were not read. Therefore no lemma
number from this paper is supplied as a directly checked C15/C16
precedent. Its specific root/shift attribution in PL-2 is explicitly
attribution by the later primary paper. Inaccessibility cannot establish
that the original paper lacks a general lemma applicable here.

## PL-5: exact normalization and the model boundary

The following is a source-variable mapping, not a proof of the proposed
window. It agrees with the already frozen normalization note
`classical-root-literature-20260907.md`, L2--L3, SHA-256
`70de5d428959171fcfdbf1f6d4f158ce741d8248301f9f1949d5818639d2002a`.
Let `U` contain one positive representative per `D_r` root pair and
write `W=[U;-U]` after permutation. Then

```
N = r(r-1),     P = UU^T/2,     C = P/(r-1),
A_r = D(C),    mu = (r-1)lambda,
A_r-lambda I_(2N) = [D(P)-mu I_(2N)]/(r-1).
```

C16's proposed interval corresponds to `0<=mu<=1/2`, not the tabulated
half-root point `mu=2/3`. Restricting both full sign vectors to the
antipodal form yields the objective `2 a^T(C-lambda I_N)b`. This is
only a restricted optimization unless additional reasoning controls
all other signs. The decisive noncommutation is

```
[D(C)-lambda I_(2N)] - D(C-lambda I_N)
    = -(lambda/2)[I,I;I,I].
```

Thus `D(C-lambda I)` is not C15's model. The difference acts on the
symmetric block even though it vanishes on the antipodal block.

Likewise, standard PSD reduction to a synchronized sign quadratic form
and the constant diagonal shift in such a quadratic objective cannot
alone be imported as a theorem about the shifted bilinear maximum.
In `s^T(M-lambda I)t` the correction is `-lambda s^T t`, not a
constant unless the signs are synchronized. Moreover, for positive
`lambda`, `D(C)-lambda I` is negative on the symmetric block and is
not PSD. None of these observations verifies or refutes C15; they
identify precisely what a directly applicable precedent must control.

## PL-6: bounded conclusion

The selected primary sources positively establish prior root families,
the bilinear objective, sign elimination, and diagonal-modification
techniques. They do not, in the inspected material, provide a located
theorem with C15's full duplicated matrix, arbitrary real PSD input,
and endpoint `(1/2)min C_ii`, nor C16's all-`r` sufficient full-root
interval. Targeted searches combining PSD sign/bilinear optimization,
antipodal duplication, minimum diagonal, and diagonal perturbation did
not produce a directly matching theorem to add within this three-source
pass. Search-title or keyword matches were not treated as model matches.

This limited retrieval result, especially with the original 1994 paper
not fully accessible, establishes neither absence of prior art nor
originality. The source comparison also establishes no maximal-window
claim, new Grothendieck bound, or correctness verdict. Those questions
remain separate from this note; no further research direction is opened
or pursued here.
