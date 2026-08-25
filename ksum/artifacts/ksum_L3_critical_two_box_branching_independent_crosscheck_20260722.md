# L3 critical endpoint: independent two-box alphabet branching cross-check

Date: 2026-07-22  
Canonical scope:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.three-row-bicovariant-two-cell-alphabet-kernel`  
Evidence tier: independent formula scout, not a Rule-7 completion review

## Result

The first representation-theoretic gate passes on the high-alphabet critical family. Let

\[
 V_C=\{x\in\mathbb C^<machine-local-path-redacted> C}x_i=0\}.
\]

For a cell of size `a>=2`, this is `S^(a-1,1)`. Put `u=q-4a+1`. The exact alphabet type-cell
stabilizers are

\[
 A_0=S_{u-1}\times S_a^{S_L}\times S_a^{S_R}
       \times S_a^{H_L}\times S_a^{H_R},
\]

\[
 A_1=S_u\times S_1\times S_{a-1}^{S_L}\times S_{a-1}^{S_R}
       \times S_a^{H_L}\times S_a^{H_R}.
\]

On either answer define

\[
 \tau_t=V_{H_L}\boxtimes V_{H_R}\boxtimes\mathbf1_{\rm other\ cells}.
\]

For `a>=2` and `t=0,1`, direct two-point-module decomposition gives

\[
 \dim\operatorname{Hom}_{A_t}
 \left(\tau_t,\operatorname{Res}_{A_t}^{S_q}S^{(q-2,2)}\right)=1,
\]

\[
 \dim\operatorname{Hom}_{A_t}
 \left(\tau_t,\operatorname{Res}_{A_t}^{S_q}S^{(q-2,1,1)}\right)=1.
\]

Thus each candidate contains one normalized common NO/YES tensor component.

## Explicit isometries and uniqueness

The ordered distinct-pair module decomposes as

\[
 \mathbb C\{(i,j):i\ne j\}
 =\mathbf1\oplus2S^{(q-1,1)}
  \oplus S^{(q-2,2)}\oplus S^{(q-2,1,1)}.
\]

For `x in V_(H_L)` and `y in V_(H_R)`, set

\[
 \Phi_\pm(x\otimes y)
 ={1\over\sqrt2}\sum_{\ell\in H_L,r\in H_R}
 x_\ell y_r(e_{\ell r}\pm e_{r\ell}).
\]

The plus map is an isometry into `S^(q-2,2)` and the minus map is an isometry into
`S^(q-2,1,1)`. The zero-sum conditions put the plus image in the kernel of the unsigned incidence
map and the minus image in the kernel of the oriented boundary map. Those kernels are precisely
the two displayed Specht modules. Among type-cell pair orbits, only `H_L x H_R` carries both
nontrivial cell standards, so the occurrence is unique.

An independent character check uses

\[
 \chi_{(q-2,2)}={X_1\choose2}+X_2-X_1,
 \qquad
 \chi_{(q-2,1,1)}={X_1-1\choose2}-X_2.
\]

Averaging either character against
`(X_1(g_L)-1)(X_1(g_R)-1)` over `A_t` gives exactly one.

## It is not the dead one-cell direct sum

At the unmarked level,

\[
 V_{H_L}\boxtimes V_{H_R}
\]

is an irreducible outer tensor product for `S_a x S_a`; it is not

\[
 (V_{H_L}\boxtimes\mathbf1)\oplus
 (\mathbf1\boxtimes V_{H_R}).
\]

Fixing one left-heavy label restricts

\[
 V_{H_L}\downarrow S_{a-1}=\mathbf1\oplus V_{a-1},
\]

so the selected tensor becomes

\[
 (\mathbf1\boxtimes V_{H_R})\oplus
 (V_{a-1}\boxtimes V_{H_R}).
\]

For `a>=3` the second summand is a genuine two-cell tensor of dimension `(a-2)(a-1)`. On the exact
high-end `u=1` family, this genuine branch has multiplicity one under NO and YES in each two-box
irrep. The opposite-cell-standard marked type has total multiplicity four in NO and six in YES,
so a raw marked calculation must resolve nontrivial recoupling; the old block-diagonal theorem
cannot simply be imported.

## Boundary cases and scope

- At `a=2`, the unmarked tensor is still not a one-cell direct sum, but after fixing one side
  `V_1=0`, so the selected local component degenerates to an opposite-side single standard.
- At `q=5`, the project parameters have `a=1`, hence `V_(H_L)=V_(H_R)=0`. The required carrier is
  absent. This is not a failure of the critical-endpoint route, whose task is
  `q=Theta(N^(2/3))`; the fixed-`q` endpoint must be supplied by the existing square-root branch.
- If each position side supplies a three-row covariant occurrence space of dimension
  `C=S_(r-2)`, the unique alphabet tensor gives a natural `C^2` common channel in each answer.
  This is only an occurrence gate. No physical query attenuation follows from it.

## Decision

The exact branching/common-channel gate is **PASS at proposer/scout tier** for `a>=2`, and the
carrier is genuinely outside the dead unmarked one-cell direct sum. The next gate is the literal
raw-label effect and equality sandwich for each single global alphabet type. No completion status
is licensed by this cross-check.
