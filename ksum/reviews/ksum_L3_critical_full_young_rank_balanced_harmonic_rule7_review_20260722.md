# Rule-7 review: full Young-rank balanced-harmonic feasibility audit

Date: 2026-07-22  
Canonical node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.full-young-rank-balanced-harmonic-kernel`  
Reviewed proposer artifact:
`ksum/artifacts/ksum_L3_critical_full_young_rank_balanced_harmonic_feasibility_20260722.md`  
Reviewed proposer SHA-256:
`A2ECCB1B0A8EE49B0D58B61FEC75400A40FC54FAFF00B6AD5326BD6CA465B9DD`

## 1. Verdict

**PARTIAL.**  The formula-level obstruction is independently correct in the following exact
scope:

* on the complete `S_q`-trivial alphabet sector of either frozen answer space, for every left or
  right coordinate and every rectangular operator `Gamma=P_1 Gamma P_0`,
  \[
    P_1(\Gamma\circ\Delta_i^s)P_0=(1-q^{-1})\Gamma,
    \qquad
    \|\Gamma\circ\Delta_i^s\|\ge (1-q^{-1})\|\Gamma\|;
    \tag{R1}
  \]
* literal `S_n` restriction keeps different full-group parent origins in orthogonal summands, so
  the scalar Young-down map obtains its cancellations only after an extra, nonphysical
  codiagonal;
* both statements are insensitive to occurrence multiplicity and to amplification by a genuinely
  independent common auxiliary space.

This rules out the **scalar Young-harmonic / alphabet-trivial mechanism** as the missing
`m^(1/6)` selector.  It does not refute the canonical existential node: nontrivial alphabet
types, pair-dependent full-position coefficients, and formula-defined raw/status recouplings are
outside the reviewed no-go.

The review is not a full PASS because the proposer's displayed “infinite legal endpoint”

\[
 a=k^2,\qquad d=k,\qquad n=a(d+1),\qquad q=4a
 \tag{P2.1}
\]

is not in the frozen range for any `k>=2`.  With even total length `N=2n`, legality
`q<=N^(2/3)` is equivalent to

\[
 d+1\ge 4\sqrt a.
 \tag{R2}
\]

The printed choice has `k+1<4k`.  A correct exact cap sequence is

\[
 a=k^2,\qquad d=4k-1,\qquad m=4k,\qquad
 n=4k^3,\qquad N=8k^3,\qquad q=4k^2=N^{2/3}.
 \tag{R3}
\]

The obstruction itself is uniform in `a,d,q` and therefore survives this correction.  Two minor
printed typing qualifications are also required: proposer (8.7) assumes that each `J_t` is an
isometry, and proposer (6.4) assumes that the displayed predecessor set is nonempty.

## 2. Independent reconstruction from the promise

I reconstructed the reviewed interfaces from the raw joint histograms in
`ksum/artifacts/ksum_L3_hidden_frequency_promise_20260721.md`, rather than treating the earlier Young
audits as frozen.  Only after fixing the stabilizers, marked maps, and equality channel did I
compare them with the proposer's formulas.  The standard symbols `Z_lambda`, `D_(t,z)`, and `P_t`
coincide because they are the canonical invariant, raw-value, and trivial-isotypic objects; no
proposer-specific transport map was imported.

Work on `p=0`, so one list has `a` singleton labels and `a` heavy labels of multiplicity `d`, and

\[
 n=a(d+1),\qquad q\ge4a.
 \tag{R4}
\]

After quotienting a NO input by common alphabet relabeling, the left and right supports are
disjoint and leave no cross-side matching datum.  One side is an `S_n`-set of an unlabeled
`a`-subset together with an unordered family of `a` heavy `d`-blocks.  Its stabilizer and module
are

\[
 H=S_a\times(S_d\wr S_a),\qquad
 M=\operatorname{Ind}_{H}^{S_n}{\bf1},\qquad
 \operatorname{ch}M=h_a h_a[h_d].
 \tag{R5}
\]

If the coordinate labels are instead fixed, the position stabilizer is `(S_d)^a` and the
character is `h_1^a h_d^a`; hence the two modules must not be identified.

Fixing a coordinate partitions the quotient basis into singleton and heavy orbits.  Their exact
stabilizers are

\[
 H_S=S_{a-1}\times(S_d\wr S_a),\qquad
 H_H=S_a\times S_{d-1}\times(S_d\wr S_{a-1}).
 \tag{R6}
\]

Their dimensions are respectively `a/n` and `ad/n` times `dim M`, and therefore exhaust the
restriction.  This independently gives

\[
 M\downarrow S_{n-1}
 =\operatorname{Ind}_{H_S}^{S_{n-1}}{\bf1}
  \oplus
  \operatorname{Ind}_{H_H}^{S_{n-1}}{\bf1}.
 \tag{R7}
\]

Now decompose `M=direct_sum_lambda S^lambda tensor Z_lambda`, with
`Z_lambda=(S^lambda)^H`.  Multiplicity-free one-box branching gives, for every
`beta partition of n-1`,

\[
 R_\beta=\bigoplus_{\lambda:\,\beta\nearrow\lambda}
          B_{\beta\lambda}\otimes Z_\lambda,
 \qquad \dim B_{\beta\lambda}=1.
 \tag{R8}
\]

The sum in (R8) is orthogonal because it is obtained by restricting the orthogonal full-group
isotypic decomposition before regrouping equal lower irreps.  A full-group multiplier restricts
as the block direct sum of its parent blocks.  It does not add the parent-origin copies.  In
contrast, the scalar Young row

\[
 c\longmapsto
 \sum_{\lambda:\,\beta\nearrow\lambda}
 \sqrt{f^\beta/f^\lambda}\,c_\lambda
 \tag{R9}
\]

first forgets `Z_lambda` and the parent tag and then applies a codiagonal.  Thus a kernel of (R9)
is not a kernel of literal restriction.

For the physical channel, let `V_t=C[X_t]` and let `D^s_(t,z)` project onto inputs whose marked
coordinate on side `s` has raw value `z`.  Let `P_t` project to the `S_q`-fixed subspace.  Alphabet
covariance and transitivity imply that `P_t D^s_(t,z)P_t` is independent of `z`.  Summing over
`z` gives, without a dimension or multiplicity assumption,

\[
 P_tD^s_{t,z}P_t=q^{-1}P_t.
 \tag{R10}
\]

For `Gamma=P_1 Gamma P_0`, insert `P_1` and `P_0` next to the two raw projections in the equality
pinching:

\[
 \begin{aligned}
 P_1\left(\sum_zD^s_{1,z}\Gamma D^s_{0,z}\right)P_0
 &=\sum_z(P_1D^s_{1,z}P_1)\Gamma(P_0D^s_{0,z}P_0)\\
 &=q(q^{-1})^2\Gamma=q^{-1}\Gamma.
 \end{aligned}
 \tag{R11}
\]

Subtracting (R11) proves (R1), and compression contractivity gives its norm inequality.  The
argument applies separately to NO and YES spaces, to left and right marks, and after tensoring
with any identity auxiliary factor.

## 3. Rule 7(a): type and dimension audit

Write `f^lambda=dim S^lambda`, `z_lambda=dim Z_lambda`,
`z^S_beta=dim Z^S_beta`, and `z^H_beta=dim Z^H_beta`.  Let `p(r)` denote the number of partitions
of `r`.  All Hilbert spaces are finite-dimensional complex spaces with their permutation-module
inner products.

### 3.1 Modules and quotient dimensions

For `p=0`, the exact raw orbit dimensions are

\[
 \dim V_0={q!\over(q-4a)!(a!)^4}
              \left({n!\over(d!)^a}\right)^2,
 \tag{T1}
\]

\[
 \dim V_1={q!\over(q-4a+1)!((a-1)!)^2(a!)^2}
              \left({n!\over(d!)^a}\right)^2.
 \tag{T2}
\]

The `S_q`-fixed ranks are

\[
 r_0:=\operatorname{rank}P_0
   =\left({n!\over(a!)^2(d!)^a}\right)^2,
 \qquad
 r_1:=\operatorname{rank}P_1
   =\left({n!\over(a!(a-1)!(d!)^a}\right)^2=a^2r_0.
 \tag{T3}
\]

These agree with the exact quotient modules
`P_0V_0 isomorphic to M_L box-times M_R` and
`P_1V_1 isomorphic to Mtilde_L box-times Mtilde_R`, where

\[
 \dim M={n!\over(a!)^2(d!)^a},\qquad
 \dim\widetilde M={n!\over a!(a-1)!(d!)^a}=a\dim M.
 \tag{T4}
\]

Thus proposer (1.1), (2.3), (2.6)--(2.9), (3.1)--(3.7), and (7.1)--(7.3) have the asserted
module domains and dimensions.  The NO/YES quotient factorization in proposer (7.7)--(7.8) is
also correct; it is special to the disjoint-support NO orbit and the unique distinguished
singleton pair in the YES orbit.

### 3.2 Occurrence and restriction maps

The following table audits every operator-valued display in proposer Sections 4--6.

| proposer tags | domain | codomain | dimensions | audit |
|---|---|---|---|---|
| (4.1) | `S^alpha box-times S^theta` | `S^lambda` restricted to `S_|alpha| x S_|theta|` | `f^alpha f^theta` to `f^lambda`; Hom dimension `c^lambda_(alpha,theta)` | typed |
| (4.2)--(4.7) | invariant/intertwiner spaces | finite direct sums of LR spaces tensor Foulkes invariant spaces | `z_lambda`, `z^S_beta`, `z^H_beta` equal the displayed LR-weighted sums | typed; no multiplicity-one assumption |
| (4.8) | `S^beta` | `S^lambda downarrow S_(n-1)` | `f^beta` to `f^lambda`; Hom dimension `1` iff `beta nearrow lambda` | typed |
| (4.9) | `direct_sum_beta S^beta tensor R_beta` | `M downarrow S_(n-1)` | `dim R_beta=sum_(lambda:beta nearrow lambda) z_lambda` | unitary isomorphism |
| (4.10)--(4.12) | `R_beta` | `Z^S_beta direct-sum Z^H_beta` | both dimension `z^S_beta+z^H_beta=sum z_lambda` | a unitary exists; no canonical parent identification follows |
| (5.1) | `S^beta` | the `beta` branch inside `S^lambda downarrow S_(n-1)` | isometry from `f^beta` into `f^lambda` | typed |
| (5.2) | `R_beta` | `Z^sigma_beta` | `(z^S_beta+z^H_beta)` to `z^sigma_beta` | coisometry |
| (5.3) | `R_beta` | `R_beta` | square of size `sum z_lambda`; effects sum to identity | typed |
| (5.4)--(5.5) | selected `E` | `Z^sigma_beta`, then effect on `E` | `dim E` to `z^sigma_beta`; `Q` is `dim E` square | typed if `J:E->R_beta` is isometric |
| (5.6)--(5.7) | `R_(0,beta)` | `R_(1,beta)` | direct sum of `B_lambda:Z_(0,lambda)->Z_(1,lambda)` | parent diagonal, including arbitrary occurrence dimensions |
| (5.8) | `Z^(sigma0)_(0,beta)` | `Z^(sigma1)_(1,beta)` | `z^(sigma0)_(0,beta)` to `z^(sigma1)_(1,beta)` | composition order and answer indices correct |
| (6.0a)--(6.0c) | `C^(p(n))` | `direct_sum_beta C^{deg(beta)}` and then `C^(p(n-1))` | column normalization uses `sum_(beta nearrow lambda)f^beta=f^lambda` | `R_n` is isometric; `Sigma` is the extra codiagonal |
| (6.1)--(6.3) | scalar coefficient space | parent-tagged lower copies | squared norm is the sum of squares, with no cross term | typed |
| (6.4) | nonempty direct sum of parent blocks | same lower-parent direct sum | operator norm is the maximum block norm | correct with the stated nonempty-set qualification |
| (6.5)--(6.8) | marked full-product multiplicity spaces | direct sums over left or right Young parents | dimensions are sums of `dim M_t(lambda,mu,nu)` | typed for arbitrary multiplicity |

Here proposer (5.2) writes `P_sigma U_beta`; `P_sigma` is the coordinate projection from
`Z^S_beta direct-sum Z^H_beta`, not a projector acting on `R_beta`.  With that reading the formula
and its coisometry claim are correct.

### 3.3 NO/YES incidence and raw query maps

The quotient incidence in proposer (7.4) has type

\[
 J:M\longrightarrow\widetilde M,qquad
 \dim\widetilde M=a\dim M,qquad J^*J=I_M.
 \tag{T5}
\]

Its restrictions `j_lambda:Z_lambda->Ztilde_lambda` are isometries, and the two-sided map has
domain rank `r_0` and codomain rank `r_1`.  The status identities (7.5) are identities in
`Hom(M,Mtilde)` and are correct on every quotient basis vector.

For proposer (8.1)--(8.8), the complete type ledger is:

| proposer tags | domain | codomain | dimensions | audit |
|---|---|---|---|---|
| (8.1) | `V_t` | `V_t` | square `dim V_t`; orthogonal projection | typed; `sum_z D_(t,z)=I` |
| (8.2)--(8.3) | `Hom(V_0,V_1)` | `Hom(V_0,V_1)` | vector-space dimension `(dim V_1)(dim V_0)` | equality pinching and off-equality Schur channel correct |
| (8.4) | `E_t` | `D_(t,z)V_t`; effect on `E_t` | `rank D_(t,z)` by `dim E_t`; effect is `dim E_t` square | typed |
| (8.5) | `E_t` | `D_(t,z)V_t` | polar partial isometry has initial support `supp F_(t,z)` | typed |
| (8.6) | `D_(0,z)V_0` | `D_(1,z)V_1` | rectangular `rank D_(1,z)` by `rank D_(0,z)` | typed after zero extension |
| (8.7) | `E_0` | `E_1` | rectangular `dim E_1` by `dim E_0` | exact provided `J_0,J_1` are isometries; this hypothesis is implicit in the proposer |
| (8.8) | raw-refined multiplicity space | direct sum over position and alphabet parents | dimension `sum_(lambda,nu) dim M_t(lambda,mu,nu)` because both branching lines are 1D | typed; left/right variants are distinct |

Finally, proposer (9.1) is an identity in `End(V_t)` with rank-`r_t` support; (9.2) and (1.6)
are identities in `Hom(P_0V_0,P_1V_1)`, of matrix size `r_1` by `r_0`; and (9.3) is the induced
operator-norm inequality in `Hom(V_0,V_1)`.  Proposer (9.4) is correct for a full-group
intertwiner decomposed into inequivalent `(lambda,mu,(q))` carriers: its norm is the maximum norm
of its multiplicity blocks.

## 4. Rule 7(b): regime-complete exact identity gates

No numerical exponent or floating-point experiment is used.  The gates below are exact algebraic
constructions of the reviewed maps, so they test the printed formulas rather than merely matching
aggregate values.

### Gate A: one parent, multiplicity one

For `R_beta=C`, literal restriction sends the unique parent occurrence to its tagged lower copy
isometrically.  A scalar coefficient `c` has restricted norm `|c|`; the normalized Young weight
can change the coordinate convention but cannot cancel it.  This exercises `c=1` at identity
level.

### Gate B: two parents and multiplicity greater than one

Take the abstract parent-origin space

\[
 R_\beta=(B_{\beta\lambda_1}\otimes\mathbb C)
          \oplus
          (B_{\beta\lambda_2}\otimes\mathbb C^2)
       \cong\mathbb C\oplus\mathbb C^2.
 \tag{G1}
\]

For arbitrary `b in C` and `C in End(C^2)`, literal restriction of the parent multiplier is
exactly `diag(b,C)`, with norm `max{|b|,||C||}`.  No map from the second two-dimensional occurrence
space to the first scalar occurrence is supplied.  Any scalar row which adds the parent entries
must choose an extra functional on `C^2`, and therefore is not the displayed restriction.  This
exercises both multiple parent origins and `c>1` at the operator-identity level.

### Gate C: rectangular NO/YES spaces and arbitrary multiplicity

Let `E_0,E_1` have arbitrary dimensions `r_0,r_1`, including the separate cases `1` and `>=2`.
In the standard transitive-label model, put

\[
 P_t={1\over q}{\bf1}{\bf1}^*\otimes I_{E_t},
 \qquad D_{t,z}=|z\rangle\langle z|\otimes I_{E_t}.
 \tag{G2}
\]

Direct multiplication gives `P_tD_(t,z)P_t=P_t/q`.  For every rectangular
`B:E_0->E_1`, summing the `q` equality terms gives `B/q`.  This separately exercises unequal
NO/YES dimensions, arbitrary occurrence multiplicity, and the exact formula rather than only its
trace.

The actual answer modules need not literally factor as the model (G2): covariance proves (R10)
on them.  Gate C is an identity-level normal form for the invariant subspace, not a numerical
substitute for that proof.

### Gate D: left/right and status regimes

The raw histograms are symmetric under exchanging the two position factors.  Repeating (R10)--(R11)
with `D^L_(t,z)` and `D^R_(t,z)` gives the same identity without identifying their marked
multiplicity spaces.  Singleton, exclusive/common-singleton, and heavy status pieces may have
different ranks, but their direct sum is contained in `P_tV_t`; (R10) is imposed before any
status refinement and therefore covers every such piece jointly.  No frozen status branch is
left untested.

### Gate E: endpoint and outer amplification

On the corrected exact sequence (R3), `q>=4a`, `p=0`, `d>=3`, and the retained ratio is
`1-1/(4k^2)=1-O(m^-2)`.  Tensoring (G2) and an arbitrary rectangular `B` with `I_c` for any
`c>=1` leaves all residuals exactly zero and leaves the norm ratio unchanged.  A payload carrying
the same diagonal `S_q` action is not covered by this gate and is correctly left open.

## 5. Rules 7(c)--7(g)

### 7(c): anchoring control

The review re-derived the quotient stabilizers from the raw promise, then derived the marked
orbits and raw-label channel before comparing formulas.  The only notational coincidences are
standard representation-theoretic notation and the proposer's equation tags used for audit
traceability.  In particular, the decisive proof (R10)--(R11) does not use the proposer's Young
decomposition at all.

### 7(d): no frozen-input immunity

The prior promise and Young-lattice reviews were not accepted as black boxes for the new use.  The
joint-histogram range, the one- and two-sided quotient modules, parent-tag orthogonality, and the
same-raw-label Schur channel were reopened above.  This reopening exposed the illegal printed
sequence (P2.1), even though earlier local artifacts had used the same scaling.

### 7(e): standing failure-mode audit

* **Dropped/extra normalization:** the `1/sqrt(a)` incidence normalization and the two factors
  `1/q` in each equality summand are correct; summing over `q` labels gives exactly `1/q`.
* **Type/dimension mismatch:** all occurrence, restriction, status, polar, effect, and rectangular
  query maps are typed in Section 3.  The implicit isometry hypothesis in proposer (8.7) is noted.
* **Undefined terms/ranges:** “legal endpoint” is false for the printed sequence and is repaired
  by (R3).  “Common auxiliary” is valid only when every raw/status map acts as identity on it.
* **Colored versus full central sums:** the equality channel sums over all raw labels
  `z in [q]`; no selected palette or colored-orbit sum replaces it.
* **Values versus printed derivation:** no numerical value is used to rescue a broken formula.
  The operator identity itself is derived in (R10)--(R11).

### 7(f): value/formula decoupling

There is no verification code and no empirical exponent fit.  The verdict verifies the printed
physical value by an independent formula-level construction.  It also verifies the literal
restriction/direct-sum formula, while rejecting the printed claim that the chosen parameter
sequence is legal.

### 7(g): quantifier hygiene

The reviewed no-go quantifies over all integers `a,d>=1`, `q>=4a` for which the two frozen orbits
exist, both answers `t in {0,1}`, both sides `s in {L,R}`, every coordinate, every
`Gamma=P_1Gamma P_0`, and every independent identity auxiliary factor.  For the original frozen
endpoint it is enough to impose `d+1>=4sqrt(a)`, with (R3) an exact infinite subsequence.

“Scalar Young harmonic” here means a coefficient law whose claimed attenuation comes from the
partition-label map (R9), without formula-defined raw/status maps that physically combine parent
occurrences.  “Alphabet-trivial sector” means `P_tV_t=(V_t)^{S_q}`.  “Independent common
auxiliary” means a tensor factor on which all position restrictions and raw-label projections act
as the identity.  Nontrivial diagonal-alphabet coupling does not satisfy that definition and is
not adjudicated.

## 6. Gate ledger and exact scope

| obligation | result |
|---|---|
| proposer SHA | **MATCH**, `A2ECC...B9DD` |
| raw NO quotient module | **PASS**, formula-level |
| raw YES quotient module | **PASS**, formula-level |
| singleton/heavy and C/X/H restrictions | **PASS**, formula-level |
| LR/Foulkes occurrence spaces | **PASS**, typed for arbitrary multiplicity |
| parent-origin orthogonality | **PASS**, formula-level |
| scalar Young codiagonal is nonphysical | **PASS**, formula-level |
| `c=1` and `c>1` identity regimes | **PASS**, exact Gates A--B |
| raw effects, polar maps, rectangular query | **PASS**, with `J_t` explicitly isometric |
| trivial-alphabet compression `1/q` | **PASS**, formula-level |
| left and right physical norm lower bound | **PASS**, formula-level |
| independent outer tensor | **PASS**, exact amplification scope |
| shared-alphabet outer payload | **OUT OF SCOPE**, remains open |
| printed `a=k^2,d=k` legal endpoint | **FAIL**, violates `d+1>=4sqrt(a)` |
| corrected legal endpoint | **PASS**, (R3) |
| broad canonical existential claim | **NOT ADJUDICATED** |

## 7. DAG consequence

The canonical node must remain **OPEN**.  The pending-review marker can be replaced by this
completed PARTIAL review.  The node may record as reviewed fact that the entire
alphabet-trivial/scalar-Young mechanism retains `1-1/q` under every physical query, provided it
also records the frozen-sequence correction and does not extend the no-go to nontrivial alphabet
or pair-dependent occurrence couplings.

