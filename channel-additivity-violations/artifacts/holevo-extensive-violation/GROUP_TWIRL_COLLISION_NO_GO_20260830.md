# Uniform finite-group twirls: maximal label collisions but exact MOE additivity

Date: 2026-08-30

Status: proposer-side exact derivation; independent review pending.

All logarithms are base two.

## Candidate mechanism

The conjugate Bell witness for `q` unrelated random-unitary Kraus operators merges only the `q`
diagonal labels among `q^2` pairs, producing a collision entropy saving of order `(log q)/q`.
A natural attempt to obtain a saving of order `log q` is to make the Kraus set closed under
multiplication.  If `U_g` is a finite-group representation, then

\[
 (U_g\otimes\overline{U_h})\Omega
 =\operatorname{vec}(U_gU_h^*)/\sqrt D
\]

depends only on the group difference `gh^{-1}`.  Thus `|G|^2` Kraus labels collapse onto at most
`|G|` vectors.

The calculation below shows why this does not create a minimum-output-entropy violation: the
uniform group average is a conditional expectation, and its minimum output entropy is exactly
additive with that of every other uniform group twirl.

## Twirl decomposition

Let `G` be a finite group and let `U:G->U(H)` be a finite-dimensional unitary representation.
Write its isotypic decomposition as

\[
 H=\bigoplus_{\alpha} V_\alpha\otimes M_\alpha,
 \qquad
 U_g=\bigoplus_\alpha U_g^{(\alpha)}\otimes I_{M_\alpha},
\]

where the `V_alpha` are inequivalent irreducible representations of dimensions `d_alpha` and the
`M_alpha` are multiplicity spaces.  Define the uniform twirl

\[
 \mathcal E_G(\rho)=\frac1{|G|}\sum_{g\in G}U_g\rho U_g^*.
\]

Schur orthogonality gives the exact conditional-expectation formula

\[
 \mathcal E_G(\rho)
 =\bigoplus_\alpha
   \frac{I_{V_\alpha}}{d_\alpha}\otimes
   \operatorname{Tr}_{V_\alpha}(P_\alpha\rho P_\alpha).
\tag{1}
\]

Let

\[
 p_\alpha=\operatorname{Tr}(P_\alpha\rho),
 \qquad
 \sigma_\alpha=p_\alpha^{-1}
 \operatorname{Tr}_{V_\alpha}(P_\alpha\rho P_\alpha)
\]

for nonzero blocks.  The entropy of (1) is

\[
 S(\mathcal E_G(\rho))
 =H(p)+\sum_\alpha p_\alpha
   \bigl(\log d_\alpha+S(\sigma_\alpha)\bigr)
 \ge\min_\alpha\log d_\alpha.
\tag{2}
\]

Equality is achieved by a product vector `v tensor m` in an isotypic block having minimal irrep
dimension.  Therefore

\[
 \boxed{S_{\min}(\mathcal E_G)=\log d_{\min}(G,U),}
\tag{3}
\]

where `d_min(G,U)` is the smallest irreducible dimension occurring in `U`.

## Exact strong additivity inside the twirl class

Let `V:H'->U(K)` be a representation of another finite group `H`, with twirl `E_H` and smallest
occurring irrep dimension `e_min`.  The product channel `E_G tensor E_H` is exactly the uniform
twirl of the product-group representation of `G times H` on `H tensor K`.  Its occurring
irreducibles are the external tensor products `V_alpha tensor W_beta`, of dimension
`d_alpha e_beta`.  Applying (3) to the product group gives

\[
 S_{\min}(\mathcal E_G\otimes\mathcal E_H)
 =\log(d_{\min}e_{\min})
 =S_{\min}(\mathcal E_G)+S_{\min}(\mathcal E_H).
\tag{4}
\]

In particular, for the conjugate representation,

\[
 S_{\min}(\mathcal E_G\otimes\overline{\mathcal E_G})
 =2S_{\min}(\mathcal E_G).
\tag{5}
\]

This is exact for every finite dimension and every multiplicity pattern.

## Why the apparent Bell saving disappears

For an irreducible representation, (1) says that `E_G` is the completely depolarizing channel and
`S_min(E_G)=log D`.  Although the `|G|^2` Bell-ensemble labels depend only on `gh^{-1}`, Schur
orthogonality makes the resulting `|G|` vectors a tight operator frame.  Their uniform mixture is
maximally mixed on the full `D^2` joint output, with entropy `2 log D`; there is no MOE defect.

For a reducible representation the multiplicity blocks lower the one-side entropy by exactly the
amount needed for the product-group formula (4) to remain additive.  Thus algebraically increasing
the collision multiplicity by closing the Kraus set into a uniformly weighted group cannot create
the desired `Omega(log D)` one-layer gap.

## Gate verdict

The most direct high-collision construction is a no-go:

- uniform group closure does turn diagonal collisions into full multiplication-table collisions;
- but it simultaneously turns each side into a conditional expectation;
- the minimum output entropy is then exactly additive for every pair of such twirls.

This does not rule out nonuniform group weights, approximate designs that are not conditional
expectations, or non-group collision structures.  Any such replacement must quantify how much of
the `log q` collision saving survives without reintroducing an equally large one-side entropy
loss.

## External input

The only imported representation-theoretic fact is the standard finite-group isotypic
decomposition and Schur orthogonality formula used in (1).  All entropy conclusions are derived
above.
