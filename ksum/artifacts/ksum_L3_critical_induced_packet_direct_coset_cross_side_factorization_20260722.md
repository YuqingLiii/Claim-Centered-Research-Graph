# L3 critical endpoint: direct-coset cross-side factorization of the complete induced packet

Date: 2026-07-22  
Canonical owner:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`  
Status of this artifact: **proposer-tier exact structural derivation; fresh Rule-7 review pending**  
Scope: the complete `p=0,u=1,q=4a` induced packet, every legal occurrence parameter, and the
native positive raw-value effects and rectangular transfers.  No coefficient, attenuation,
numerator, or exponent claim is made.

## 1. Result and scope boundary

The complete induced packet has a physical cell-basis realization in which the selected source is
an orthogonal direct sum over complete palette-cell partitions `xi`, and every `xi` summand is a
tensor product of a selected left marginal and a selected right marginal.  This is stronger than
the previously recorded Fourier-coordinate identities

\[
 G^L=\widehat G^L\otimes I_{Z_R},\qquad
 G^R=I_{Z_L}\otimes\widehat G^R,
\tag{1.1}
\]

because (1.1) alone leaves a shared packet coordinate in both hatted factors and therefore does
not imply commutation.  The new input is the complete induced-module reconstruction, not a formal
manipulation of (1.1).

For every answer `t in {0,1}`, every left position `i`, every right position `j`, and every raw
values `z,w`, the full positive source effects satisfy

\[
 \boxed{[F^L_{t,i,z},F^R_{t,j,w}]=0.}
\tag{1.2}
\]

Consequently the two native rectangular transfer superoperators

\[
 \mathcal E_s(B)=\sum_z F^s_{1,z}B F^s_{0,z},\qquad
 \mathcal E_s:\operatorname{Hom}(\mathbf E_0,\mathbf E_1)
 \longrightarrow\operatorname{Hom}(\mathbf E_0,\mathbf E_1),
\tag{1.3}
\]

commute exactly:

\[
 \boxed{[\mathcal E_L,\mathcal E_R]=0.}
\tag{1.4}
\]

This theorem includes the full YES packet, including the orthogonal complement of either
orientation image `J_o M_0`.  It does not pull YES back through `J_L` or `J_R`, and it does not
assert commutation between orientation-dependent pulled-back NO/YES effects.  It also does not
assert that all same-side status/path effects commute.

## 2. Fixed-palette marginal product

Put

\[
 q=4a,\qquad n=a(d+1),\qquad V_a=S^{(a-1,1)},\qquad D=a-1.
\tag{2.1}
\]

For a NO palette partition write

\[
 \xi=(A,B,H_L,H_R),\qquad |A|=|B|=|H_L|=|H_R|=a,
\tag{2.2}
\]

and for a YES palette partition write

\[
 \xi=(U,C,L,R,H_L,H_R),
 \quad |U|=|C|=1,\quad |L|=|R|=a-1,\quad |H_L|=|H_R|=a.
\tag{2.3}
\]

Define the marginal rare palettes

\[
 R_{0,L}=A,\quad R_{0,R}=B,\qquad
 R_{1,L}=C\sqcup L,\quad R_{1,R}=C\sqcup R.
\tag{2.4}
\]

Every one of these sets has size `a`.  For a fixed `xi`, let `Omega_(t,s)(xi)` be the set of
length-`n` words on side `s` in which every value in `R_(t,s)` occurs once and every value in
`H_s` occurs `d` times.  Then the complete raw input fiber over `xi` is exactly

\[
 \boxed{\Omega_t(\xi)=\Omega_{t,L}(\xi)\times\Omega_{t,R}(\xi).}
\tag{2.5}
\]

For YES, the fact that `C` is used once on both sides imposes no relation between its two position
locations.  After the raw value `C` is fixed, its left and right singleton positions are chosen
independently.  The unused value `U` occurs on neither side.  Thus (2.5) is valid for both answers,
including the common-singleton status.

The whole orbit Hilbert space therefore has the physical orthogonal decomposition

\[
 \mathbb C[X_t]
 =\bigoplus_{\xi}\mathbb C[\Omega_{t,L}(\xi)]
       \otimes\mathbb C[\Omega_{t,R}(\xi)].
\tag{2.6}
\]

The common alphabet action permutes the summands in (2.6).  It does not identify distinct
summands inside the Hilbert space.

## 3. The complete selected projection is a product on every cell fiber

Fix `xi` and a side `s`.  Position permutations `S_n` and the actual within-cell label
permutations act on `C[Omega_(t,s)(xi)]`.  Let

* `P_lambda^s` be the central position projector onto `S^lambda`, where
  `lambda=(n-r-1,r,1)`;
* `P_V^(H_s)` be the projector onto the standard representation `V(H_s)` of permutations of the
  `a` heavy labels;
* `P_(theta_r nearrow lambda)^(t,s,xi)` be the deterministic multiplicity-channel projector which
  retains the specified intermediate heavy-position type `theta_r=(ad-r-1,r,1)` and the actual
  coefficient-one rare attachment path to `lambda`.

For NO that path attaches the `a` singleton positions at once.  For YES it is the ordered path

\[
 S^{\theta_r}\boxtimes S^{(a-1)}\longrightarrow S^\zeta,
 \qquad S^\zeta\boxtimes S^{(1)}\longrightarrow S^\lambda,
 \qquad \zeta=(n-r-2,r,1),
\tag{3.0}
\]

corresponding to the residual cell and the common singleton.  It would be wrong to insert an
`S_a` symmetry swapping `C` with `L` or `R` inside one fixed YES cell partition: that is not a
within-cell symmetry.  The ordered map (3.0), not such an extra symmetry, defines the YES local
channel.

The last projector is necessary: `P_lambda P_V` alone may contain other intermediate heavy
types and would select a larger space than the node owns.  Define the local selected projector by

\[
 P_{t,s}(\xi):=P_{(\theta_r\nearrow\lambda)}^{t,s,\xi},
 \qquad
 P_{t,s}(\xi)\preceq
 P_\lambda^s P_V^{H_s}.
\tag{3.1}
\]

where equivalently `P_(t,s)(xi)` is the range projector of the deterministic local Fourier
isometry built from the fixed Pieri map and all `T_h`.  This equivalent definition avoids any
claim that the intermediate-channel projector is central.  The coefficient-one rare-singleton
attachment and Frobenius reciprocity identify its range as

\[
 \mathcal L_{t,s}(\xi):=\operatorname{im}P_{t,s}(\xi)
 \cong S^\lambda_s\otimes V(H_s)\otimes Z_s,
\qquad
 Z_s=\operatorname{Hom}_{S_d\wr S_a}(V_a,S^{\theta_r}),
\tag{3.2}
\]

with `theta_r=(ad-r-1,r,1)`.  The deterministic intertwiners `T_h` give the stated copy of `Z_s`.
If `f_1,...,f_D` is the fixed orthonormal basis of `V_a`, the local invariant tensor is

\[
 \eta_{t,s,h}(\xi)
 ={1\over\sqrt D}\sum_{i=1}^D
  \iota_{t,s}(T_hf_i)\otimes\phi_{t,s,\xi}(f_i),
\tag{3.3}
\]

where `phi_(t,s,xi):V_a -> V(H_s)` is the order-fixed cell isometry.  Since
`T_h^*T_k=delta_(hk)I`, these local tensors are orthonormal in the occurrence label.

The previously used double coevaluation is exactly the tensor product of (3.3) on the two sides:

\[
 \eta_{t,L,h}(\xi)\otimes\eta_{t,R,k}(\xi)
 ={1\over D}\sum_{i,j=1}^D
 \iota_{t,L}(T_hf_i)\otimes\iota_{t,R}(T_kf_j)
 \otimes\phi_{t,L,\xi}(f_i)\otimes\phi_{t,R,\xi}(f_j).
\tag{3.4}
\]

Thus the factor `1/D` is not an entangled compression between the two position sides; it is the
product of the two local factors `1/sqrt(D)`.

The local rank is

\[
 \dim\mathcal L_{t,s}(\xi)=f^\lambda D C_r.
\tag{3.4a}
\]

The numbers of complete palette partitions are

\[
 |\Xi_0|={q!\over(a!)^4},\qquad
 |\Xi_1|={q!\over((a-1)!)^2(a!)^2}=a^2|\Xi_0|,
\tag{3.4b}
\]

and `dim M_t=|Xi_t|D^2`.  Transporting (3.3) with the position groups and transporting `xi` and
the two heavy fibers with `S_q` defines an equivariant isometry from the right-hand side of (3.5)
into the selected raw orbit.  On the reference fiber its invariant tensor is exactly (3.4), hence
it is the deterministic selected Fourier embedding already fixed by the occurrence construction.
Its rank is

\[
 |\Xi_t|(f^\lambda D C_r)^2
 =(f^\lambda)^2\dim(M_t)C_r^2,
\tag{3.4c}
\]

which is the complete selected Fourier rank.  Thus the map is onto that selected space; there is
no additional entangled compression or omitted multiplicity sector.

Let `P_t` be the projection onto the complete selected packet in `C[X_t]`.  Equations
(2.6)--(3.4) give the physical projection identity

\[
 \boxed{
 P_t=\bigoplus_\xi P_{t,L}(\xi)\otimes P_{t,R}(\xi),
 \qquad
 \operatorname{im}P_t
 =\bigoplus_\xi\mathcal L_{t,L}(\xi)\otimes\mathcal L_{t,R}(\xi).}
\tag{3.5}
\]

This is a reducing/product compression, not a dimension count.  In abstract Fourier notation,
the right-hand side is

\[
 S^\lambda_L\otimes S^\lambda_R\otimes
 \operatorname{Ind}_{H_t}^{S_q}\tau_t\otimes Z_L\otimes Z_R
 =S^\lambda_L\otimes S^\lambda_R\otimes M_t\otimes Z_L\otimes Z_R.
\tag{3.6}
\]

Because every cell coset and every vector in the heavy fiber
`V(H_L) tensor V(H_R)` occurs in (3.5), this is the complete `M_t`, not a chosen list of full
types.  For `t=1`, it includes all of

\[
 M_1\cong M_0\oplus2\operatorname{Ind}_{S_a^4}^{S_{4a}}
   (V_a\boxtimes\mathbf1\boxtimes V_a\boxtimes V_a)
 \oplus\operatorname{Ind}_{S_a^4}^{S_{4a}}(V_a^{\boxtimes4}),
\tag{3.7}
\]

so no unmatched YES complement has been discarded.

Conversely, if one pinches to selected `S_q` parents before the raw query, (3.5) is generally
destroyed.  Completeness of the induced packet is load-bearing.

## 4. Raw queries preserve `xi` and act on one marginal only

Fix a left coordinate `i`, a right coordinate `j`, and raw values `z,w`.  On the fiber over `xi`,
let `M^L_(i,z)(xi)` and `M^R_(j,w)(xi)` be multiplication by the corresponding value predicates.
They are zero when the value is absent from that marginal.  On (2.6),

\[
 \begin{aligned}
 M^L_{i,z}|_\xi&=M^L_{i,z}(\xi)\otimes I_{\Omega_{t,R}(\xi)},\\
 M^R_{j,w}|_\xi&=I_{\Omega_{t,L}(\xi)}\otimes M^R_{j,w}(\xi).
 \end{aligned}
\tag{4.1}
\]

A raw query only reads an existing coordinate.  It neither changes a palette cell nor moves a
value between cells.  Hence both operators in (4.1) preserve the same `xi` summand.

The normalized marked refinement satisfies

\[
 (\operatorname{Ref}_t^s)^*D^s_{t,z}\operatorname{Ref}_t^s=M^s_{i,z}
\tag{4.2}
\]

for the fixed queried coordinate, with the usual carrier normalization included in `Ref`.  Thus
the full positive selected effect is simply the product compression of (4.1):

\[
 \begin{aligned}
 F^L_{t,i,z}
 &=P_tM^L_{i,z}P_t|_{\operatorname{im}P_t}\\
 &=\bigoplus_\xi
   \left(P_{t,L}(\xi)M^L_{i,z}(\xi)P_{t,L}(\xi)ight)
   \otimes I_{\mathcal L_{t,R}(\xi)},\\
 F^R_{t,j,w}
 &=\bigoplus_\xi I_{\mathcal L_{t,L}(\xi)}\otimes
   \left(P_{t,R}(\xi)M^R_{j,w}(\xi)P_{t,R}(\xi)\right).
 \end{aligned}
\tag{4.3}
\]

No invariance of a local selected range under `M_(i,z)` is assumed: the two local `P` factors in
(4.3) are retained.  The conclusion uses only that the opposite marginal is a reducing identity
factor and that the complete packet retains the orthogonal direct sum over `xi`.

Multiplying the two displays fiber by fiber gives

\[
 F^L_{t,i,z}F^R_{t,j,w}
 =\bigoplus_\xi A^L_{t,i,z}(\xi)\otimes A^R_{t,j,w}(\xi)
 =F^R_{t,j,w}F^L_{t,i,z},
\tag{4.4}
\]

which proves (1.2) for both answers and all raw values, including values whose effect is zero.

## 5. Complete actual-status and branch audit

For fixed `xi,z`, cell status is a scalar condition on the direct-sum label `xi`; it does not
alter the marginal product.  The nonzero statuses are exactly

| answer | left query | right query |
|---|---|---|
| NO | `A`, `H_L` | `B`, `H_R` |
| YES | `C`, `L`, `H_L` | `C`, `R`, `H_R` |

The YES unused cell `U` is never an input status.  Opposite-side cells give the zero local
operator.  In particular, the common `C` status still gives a left-local and a right-local
compression on the product fiber (2.5).

The following refinements preserve the cross-side product conclusion.

1. **Singleton/residual/heavy status.**  These are `xi`-diagonal masks.  They preserve (4.3).
2. **Ordered position predecessor.**  Each of `beta_T,beta_M,beta_B` is a projector in the marked
   representation of one position group only.  A left predecessor is local to
   `L_(t,L)(xi)` and a right predecessor is local to `L_(t,R)(xi)`.
3. **Internal heavy path.**  A heavy restriction path is contained in the pointed wreath-product
   restriction on the queried marginal.  Keeping every compatible path, or summing them, leaves
   the opposite marginal equal to the identity.
4. **Alphabet point child at the same marked raw value.**  For fixed `z`, the literal marked map is
   `S_(q-1)^(z)`-equivariant.  The projector `Pi_tau^(z)` onto a point child is central in the
   group algebra of that marked alphabet stabilizer.  With separate source and codomain
   projectors, equivariance gives

   \[
    \Pi_{\tau,\mathrm{out}}^{(z)}\ell^s_{t,z}
      =\ell^s_{t,z}\Pi_{\tau,\mathrm{in}}^{(z)},\qquad
    Q^s_{t,z;\tau}
      =\Pi_{\tau,\mathrm{in}}^{(z)}F^s_{t,z}
      =F^s_{t,z}\Pi_{\tau,\mathrm{in}}^{(z)}.
   \tag{5.1}
   \]

   All full parents `nu` sharing `tau` are automatically assembled in (5.1).  A private child is
   the same formula with only one nonzero parent column.  Hence common and private children are
   both included, without an old-parent pinch.

For one common raw mark `z`, the central point-child projectors commute with both left and right
fixed-`z` effects.  Combining (4.4) and (5.1), all cross-side refinements built from actual status,
ordered position child, compatible local heavy path, and point children of this same marked
stabilizer commute.

The theorem does **not** license the following stronger statements.

* Point-child projectors for two different raw marks `z != w` belong to two conjugate, not common,
  point stabilizers.  Those refined projectors need not commute.  Only the aggregate raw effects
  in (4.4) commute for arbitrary `z,w`.
* Same-side compressed effects can be noncommuting.  Compression by `P_(t,s)(xi)` is not a
  homomorphism, and the growing occurrence multiplicity is active on that side.
* Artificially retaining the old full parent `nu` as a post-query superselection label is not
  physical.  It deletes the required codiagonal entries and can change commutators.
* Literal rectangular rows do not have ordinary commutators.  The statements above concern their
  positive source effects.
* Pulling YES effects back with `J_L` or `J_R` is another compression.  It need not preserve
  commutation, and this artifact gives no cross-answer pulled-back verdict.

The physical marked codiagonal does not change `xi`: it is the Fourier description, under the
marked subgroup, of the same `xi`-preserving raw map.  It joins different unmarked `S_q` parent
coordinates after a basis change, rather than moving a physical input between palette partitions.

## 6. Native rectangular transfer commutation

Suppress the fixed position coordinates, as symmetry makes their choices unitarily equivalent.
The operators have the types

\[
 F^s_{0,z}\in\operatorname{End}(\mathbf E_0),\qquad
 F^s_{1,z}\in\operatorname{End}(\mathbf E_1),
\tag{6.1}
\]

and therefore (1.3) is an endomorphism of the rectangular Hilbert--Schmidt space even when the
NO and YES ranks differ.  For `B in Hom(E_0,E_1)`, direct composition gives

\[
 \begin{aligned}
 \mathcal E_L\mathcal E_R(B)
 &=\sum_{z,w}F^L_{1,z}F^R_{1,w}\,B\,F^R_{0,w}F^L_{0,z},\\
 \mathcal E_R\mathcal E_L(B)
 &=\sum_{z,w}F^R_{1,w}F^L_{1,z}\,B\,F^L_{0,z}F^R_{0,w}.
 \end{aligned}
\tag{6.2}
\]

Equation (4.4) applies separately in `E_1` and `E_0`.  Commuting the two left factors on the
target and the two right factors on the source turns the first line of (6.2) into the second,
proving (1.4).  No NO-to-YES identification, padding, polar transport, or orientation choice is
used.

Each `E_s` is already positive self-adjoint in the Hilbert--Schmidt inner product.  Hence (1.4)
implies that the pair is simultaneously unitarily diagonalizable on
`Hom(E_0,E_1)`.  This is only an algebraic classification.  It does not show that a favorable
joint eigenspace exists, that the joint spectrum reduces to one scalar total-energy statistic, or
that any resolvent has an admissible norm or surviving numerator.

## 7. What direct cosets do not close: the one-side pointed occurrence algebra

The alphabet side is explicit in the complete cell basis, and the three position predecessors
can be projected without a full subduction table.  If `X_i` denotes the Jucys--Murphy element
conjugated to the fixed queried coordinate, its three eigenvalues on
`lambda=(n-r-1,r,1)` are the removable-box contents

\[
 c_T=n-r-2,\qquad c_M=r-2,\qquad c_B=-2.
\tag{7.1}
\]

Thus

\[
 \Pi_\beta^{(i)}
 =\prod_{\beta'\ne\beta}{X_i-c_{\beta'}\over c_\beta-c_{\beta'}}
\tag{7.2}
\]

is an exact formula for every ordered position branch.

The remaining non-scalar object occurs when the queried position lies inside a heavy block.  Put

\[
 W=S_d\wr S_a,\qquad Z=\operatorname{Hom}_W(V_a,S^{\theta_r}),
\tag{7.3}
\]

and define the isometry

\[
 C:V_a\otimes Z\longrightarrow S^\lambda,qquad
 C(f\otimes e_h)=\iota(T_hf).
\tag{7.4}
\]

For a distinguished heavy label, restriction of `V_a` to `S_(a-1)` is
`1 direct-sum V_(a-1)`.  Let `P_0,P_1` be those two projectors.  The aggregate heavy marked
position matrices are the basis-free compressions

\[
 C^*\Pi_\beta^{(i)}C
 =P_0\otimes R_{\beta,0}+P_1\otimes R_{\beta,1},
 \qquad R_{\beta,\epsilon}\in\operatorname{End}(Z).
\tag{7.5}
\]

Individual internal paths are obtained by inserting their pointed-subgroup projectors before the
compression in (7.5).  Equations (7.2)--(7.5) avoid constructing a marked codomain, but they do
not evaluate the `C_r by C_r` matrices.

The natural finite algebra is the one-point extension of the matrix-valued wreath-product Hecke
algebra

\[
 \mathcal H(S_{ad},W,V_a)
 =\operatorname{End}_{S_{ad}}\!\left(\operatorname{Ind}_W^{S_{ad}}V_a\right).
\tag{7.6}
\]

Unpointed double cosets are block-overlap transportation matrices, modulo the row/column block
symmetries; a heavy mark distinguishes one block and one incident position.  Because the
`theta_r` block has multiplicity

\[
 C_r=\sum_{j=0}^{r-2}p(j),
\tag{7.7}
\]

its centralizer block is `End(Z)`, not a scalar Johnson algebra.  Algebraic noncommutativity of
this ambient block does not prove that the particular six matrices in (7.5) fail to commute.
Computing their ranks, spectra, and same-side commutators is the precise remaining obstruction.

## 8. Matrix-free Gram-stack route and smallest next calculation

The existing exact Young machinery can be reused at the level of source Grams:

1. `mdh_d4c_branching.py` supplies exact fix-first branch adjoints and normalized branch
   projectors.
2. `mdh_standard_query_tensor.py` demonstrates the needed pattern: apply branch adjoints to
   deterministic unmarked invariant vectors, then take ambient Gram contractions.  This computes
   `A^*A` and cross-Gram stacks without constructing any marked codomain basis.
3. The SE trace-t5 scripts demonstrate matrix-free Casimir projection on a fixed low-defect
   induced carrier.  The same idea can replace full Young-tableau enumeration for a fixed `r`,
   using (7.2) and a colored low-defect carrier.

These tools are not plug-compatible with (7.3): their present cosets, stabilizers, and invariant
types are different.  Full Young-seminormal enumeration is already impractical at the first
critical parameters, while the trace-t5 formulas cover fixed small defect and do not provide a
uniform growing-`r` wreath-covariant theorem.

The smallest physically relevant symbolic calculation is therefore:

* take `r=4`, for which `C_4=4`, with symbolic stable `a>=5,d>=4` (and separately substitute the
  first legal critical choice);
* realize the four deterministic covariants in a low-defect/transportation basis;
* compute the six aggregate `4 by 4` matrices
  `R_(beta,epsilon)`, `beta in {T,M,B}`, `epsilon in {0,1}`, solely from source Gram contractions;
* verify the exact resolution identity and evaluate the gauge-invariant quantities

  \[
   \operatorname{Tr}\!left([R_{\beta,\epsilon},R_{\beta',\epsilon'}]^*
                    [R_{\beta,\epsilon},R_{\beta',\epsilon'}]\right).
  \tag{8.1}
  \]

A nonzero rational function in (8.1) would prove only a one-side physical commutator in its stated
uniform range; it would not overturn the cross-side and transfer commutation theorems (1.2)--(1.4).
Finite substitutions can debug the formula but cannot prove the critical asymptotic family.

## 9. Relation to the previous stopping statement

The earlier statement that a shared packet factor in (1.1) does not **automatically** imply
commutation remains logically correct.  Synthetic matrices of the forms
`X_(packet,L) tensor I_R` and `I_L tensor Y_(packet,R)` can fail to commute through their shared
packet coordinate.

The present theorem adds physical information absent from (1.1): for the complete induced packet,
the packet coordinate is the section space over actual palette partitions, and the selected
projection itself decomposes as the product (3.5) on every physical cell fiber.  Raw queries
preserve that fiber.  Thus commutation follows from the physical induced-coset realization, not
from the abstract untouched-factor identities.

This proposer-tier result should be entered into the canonical occurrence-pencil node before any
downstream use and independently reviewed.  Even if it passes, the endpoint bracket and every
attenuation/numerator obligation remain unchanged.
