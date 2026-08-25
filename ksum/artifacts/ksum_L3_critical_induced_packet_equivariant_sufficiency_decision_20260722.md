# Proposer decision: induced-packet equivariant sufficiency

Date: 2026-07-22  
Controlling node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-rectangular-transfer-resolvent-law`

## Decision

**PARTIAL THEOREM / STRONG GATE BLOCKED BY TWO MISSING FROZEN INTERFACES.**

There is an exact positive theorem: the raw-value-summed alphabet equality transfers preserve
`Hom_(S_q)(E_0,E_1)`.  Their formal defects, their commuting restrictions, and every explicitly
defined polynomial, defined resolvent, or joint spectral taper of those restrictions remain in the
same space.  Consequently, a construction formulated entirely in this restricted effect algebra
does not require the spectrum of the nontrivial `S_q`-carrier/Wigner sectors of the full
Hilbert--Schmidt space.

That theorem does **not** complete the proposed adversary construction.  Two required physical
interfaces are absent from the frozen record.

1. `B-E_s(B)` is an effect-compressed defect.  The reviewed occurrence typing explicitly says
   that polar partial isometries are needed to return to the literal marked codomains.  No frozen
   range/polar identity identifies its operator norm with the norm of the literal physical query
   mask.
2. No frozen outer incidence/numerator map for this induced-packet multiplier has been defined.
   Alphabet symmetry does not determine such a map.

There is also a separate carrier warning.  The reviewed `19456`-dimensional common-child reducer
has suppressed the two position Specht carriers.  Alphabet equivariance does not make that
suppression norm preserving.  A fixed-coordinate row branches the active position carrier through
`beta_T,beta_M,beta_B`; only the opposite position carrier is passive in the reviewed untouched-
factor theorem.  Thus `19456` is not a norm-complete substitute for the full
`Hom_(S_q)(E_0,E_1)` restriction.

The strong yes/no sufficiency question is therefore not decidable from the frozen inputs.  This is
not a refutation of the candidate and not a proof that a nontrivial alphabet-carrier spectrum is
needed.  It identifies the two minimal missing physical interfaces and proves everything that can
be proved before they are supplied.

## 1. Exact spaces and the meaning of “equivariant”

Put `Q=S_q`.  Retain every non-alphabet factor inside the multiplicity space and write

\[
 \mathbf E_t=\bigoplus_{\nu\vdash q} S^\nu\otimes K_{t,\nu}.
 \tag{1.1}
\]

Then Schur's lemma gives

\[
 \operatorname{Hom}_Q(\mathbf E_0,\mathbf E_1)
 =\bigoplus_\nu I_{S^\nu}\otimes
   \operatorname{Hom}(K_{0,\nu},K_{1,\nu}).
 \tag{1.2}
\]

Thus the allowed alphabet-equivariant multiplier has exactly the advertised form

\[
 B=\bigoplus_\nu I_{S^\nu}\otimes B_\nu.
 \tag{1.3}
\]

Crucially, `B_nu` in (1.3) still acts on the position carriers and all occurrence/multiplicity
coordinates.  The stronger full-product-invariant ansatz used in the unmarked packet is

\[
 B_\nu=I_P\otimes b_\nu,
 \qquad P=S^\lambda_L\otimes S^\lambda_R.
 \tag{1.4}
\]

Equations (1.3) and (1.4) are different spaces.  Suppressing `P` in (1.4) produces the reviewed
`19456` coefficient count; it does not give the dimension of (1.2).

At the finite target `lambda=(283,4,1)`, the exact hook dimension is

\[
 f^\lambda=62{,}660{,}742{,}144,
 \qquad p=\dim P=(f^\lambda)^2
 =3{,}926{,}368{,}606{,}036{,}857{,}716{,}736.
 \tag{1.5}
\]

For the three reviewed alphabet parents,

\[
 (f^{(62,2)},f^{(61,3)},f^{(61,2,1)})=(1952,39648,79360),
 \tag{1.6}
\]

\[
 (m_{0,\nu})=(16,48,96),\qquad
 (m_{1,\nu})=(16,80,160).
 \tag{1.7}
\]

Therefore

\[
 D:=\sum_\nu m_{0,\nu}m_{1,\nu}=19456,
 \tag{1.8}
\]

while the three-parent alphabet-equivariant space retaining both position carriers has dimension

\[
 \dim\operatorname{Hom}_Q=p^2D
 =299940903095259675438598672952304469069189349376.
 \tag{1.9}
\]

The two alphabet-module dimensions are

\[
 d_0=9{,}552{,}896,\qquad d_1=15{,}900{,}672,
 \tag{1.10}
\]

so the corresponding unsuppressed full Hilbert--Schmidt dimension is

\[
 p^2d_0d_1
 =2341707602475240847302026296380683718340432648807699709952.
 \tag{1.11}
\]

The strict hierarchy is therefore

\[
 D < p^2D < p^2d_0d_1.
 \tag{1.12}
\]

## 2. Alphabet-equivariant closure theorem

For a fixed query side `s`, let the reviewed source effects obey the raw-value covariance law

\[
 F^s_{t,gz}=\rho_t(g)F^s_{t,z}\rho_t(g)^*,
 \qquad g\in Q,
 \tag{2.1}
\]

and define

\[
 \mathcal E_s(B)=\sum_zF^s_{1,z}BF^s_{0,z}.
 \tag{2.2}
\]

If `B` is a `Q`-intertwiner, then

\[
\begin{aligned}
 \rho_1(g)\mathcal E_s(B)\rho_0(g)^*
 &=\sum_z
   \bigl(\rho_1(g)F^s_{1,z}\rho_1(g)^*\bigr)
   \bigl(\rho_1(g)B\rho_0(g)^*\bigr)
   \bigl(\rho_0(g)F^s_{0,z}\rho_0(g)^*\bigr)\\
 &=\sum_zF^s_{1,gz}BF^s_{0,gz}
 =\mathcal E_s(B).
\end{aligned}
\tag{2.3}
\]

The last equality is only a relabelling of the complete raw-value sum.  It would not hold for one
colored term in isolation.  Equation (2.3) proves

\[
 \mathcal E_s\bigl(\operatorname{Hom}_Q\bigr)
 \subseteq\operatorname{Hom}_Q.
 \tag{2.4}
\]

Consequently the formal equality-query defect

\[
 D_s(B):=B-\mathcal E_s(B)
 \tag{2.5}
\]

also lies in `Hom_Q`.  By (1.2), both outputs remain identity on every alphabet Specht carrier
`S^nu`; no off-diagonal map between inequivalent `nu` can appear.

The occurrence review proves that each `E_s` is positive self-adjoint on the rectangular
Hilbert--Schmidt space.  Since (2.4) makes `Hom_Q` invariant, self-adjointness makes it reducing:
for `X` orthogonal to `Hom_Q` and `Y` in `Hom_Q`,

\[
 \langle\mathcal E_sX,Y\rangle_{HS}
 =\langle X,\mathcal E_sY\rangle_{HS}=0.
 \tag{2.6}
\]

The separately reviewed direct-coset theorem gives
`[E_L,E_R]=0` on the full rectangular space.  Their restrictions therefore commute and remain
self-adjoint.  It follows that all of the following are endomorphisms of `Hom_Q`:

* every noncommutative polynomial in the restrictions (which becomes an ordinary joint
  polynomial because they commute);
* every inverse or resolvent whose denominator is invertible on the restricted space;
* every explicitly declared joint spectral taper of the two restricted commuting self-adjoint
  operators.

Only the joint spectrum on `Hom_Q` is relevant to that restricted functional calculus.  The
nontrivial `Q`-isotypic complement of the full Hilbert--Schmidt space is a reducing complement and
need not be diagonalized for this formal restricted calculation.

This statement concerns the specified multiplier architecture only.  It neither twirls nor
optimizes an arbitrary adversary and makes no claim that arbitrary adversaries can be symmetrized
without loss.

## 3. Norms before and after carrier suppression

For

\[
 C=\bigoplus_\nu I_{S^\nu}\otimes C_\nu
 \in\operatorname{Hom}_Q(\mathbf E_0,\mathbf E_1),
 \tag{3.1}
\]

the exact operator and Hilbert--Schmidt norms are

\[
 \|C\|=\max_\nu\|C_\nu\|,
 \qquad
 \|C\|_{HS}^2=\sum_\nu f^\nu\|C_\nu\|_{HS}^2.
 \tag{3.2}
\]

No full-Hilbert--Schmidt complement is needed to evaluate (3.2).  If in addition
`C_nu=I_P tensor c_nu`, then

\[
 \|C\|=\max_\nu\|c_\nu\|,
 \qquad
 \|C\|_{HS}^2=p\sum_\nu f^\nu\|c_\nu\|_{HS}^2.
 \tag{3.3}
\]

The operator-norm equality in (3.3) is valid only while the factor is literally `I_P`.  A
normalized partial trace or a scalar coefficient extracted from `P` is not an isometry for the
operator norm once a fixed-coordinate query has produced non-scalar position blocks.

The exact guard uses a two-dimensional position carrier.  With

\[
 U=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 B=I_2,\quad P_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},
 \tag{3.4}
\]

the fixed-coordinate effect is `P_0BP_0=P_0` and `[U,P_0]` has rank two.  The true defect has norm
one.  Replacing `P_0` by its normalized carrier trace `(1/2)I_2` gives defect norm `1/2`.  Thus
carrier suppression changes the operator norm even though the multiplier was identity on the
carrier before the query.

This toy is not substituted for the physical position table.  It proves the logical point that
alphabet covariance alone cannot justify the suppression.  The reviewed physical Pieri data show
why the issue is real rather than decorative.  At `lambda=(283,4,1)`, restriction at the marked
position has three distinct branches with dimensions

\[
 f^{\beta_T}=61{,}569{,}010{,}503,\quad
 f^{\beta_M}=818{,}808{,}991,\quad
 f^{\beta_B}=272{,}922{,}650,
 \tag{3.5}
\]

and the transported NO resolutions include

\[
 \frac2{9275}+\frac{9273}{9275}=1,
 \qquad
 \frac4{19099}+\frac{19095}{19099}=1.
 \tag{3.6}
\]

The corrected physical identities require the transporter `rho_lambda(g)`.  Hence the active
queried position carrier is not a passive identity at the row level.  For a left query the reviewed
untouched-factor theorem leaves the right position/occurrence factor passive; for a right query the
roles reverse.  No frozen theorem recombines the active `beta` blocks into `I_P` for the physical
cross-answer defect.  The position-carrier-suppressed `19456` reducer is therefore a coefficient
diagnostic, not a licensed operator-norm model.

## 4. Effect defect versus literal physical query defect

Let `W_t` denote unmarked embeddings and `Q_z` raw-value projections.  In the simplest typed model,
the literal equality-retained map and its defect are

\[
 \Lambda(B)=\sum_zQ_zW_1BW_0^*Q_z,
 \qquad
 \Delta(B)=W_1BW_0^*-\Lambda(B).
 \tag{4.1}
\]

The effect transfer is only the unmarked compression:

\[
 W_1^*\Lambda(B)W_0=\mathcal E(B),
 \qquad
 W_1^*\Delta(B)W_0=B-\mathcal E(B).
 \tag{4.2}
\]

Compression gives

\[
 \|B-\mathcal E(B)\|\le \|\Delta(B)\|,
 \tag{4.3}
\]

and equality need not hold.  The exact guard takes

\[
 W_0=\binom10,\qquad
 W_1=\frac1{\sqrt2}\binom11,\qquad
 Q_0=\operatorname{diag}(1,0),\quad Q_1=\operatorname{diag}(0,1),
 \tag{4.4}
\]

with scalar `B=1`.  It obtains

\[
 \|\Delta(B)\|^2=\frac12,
 \qquad
 \|B-\mathcal E(B)\|^2=\frac14.
 \tag{4.5}
\]

The reviewed occurrence proof makes precisely this type distinction: the effect sandwich is a
full-source compression, while polar partial isometries are needed to return to literal marked
codomains.  Therefore the algebraic closure theorem proves that the **compressed** defect norm is
computable on `Hom_Q`; it does not yet prove that this is the physical equality-query norm required
by the adversary bound.

The minimal missing input is one of the following, with all physical ranges typed:

1. a frozen polar/range-reducing identity proving equality in the required norm; or
2. the complete literal marked row formula and a direct norm theorem for its defect.

## 5. Numerator/incidence is independent data

No reviewed source defines the outer numerator map for the induced-packet coefficient `B`.  The
reviewed first packet gate explicitly states that it proves neither the two required query bounds
nor the growing three-row numerator.  The later occurrence review likewise withholds incidence
normalization and a numerator.

Equivariance cannot fill this gap.  On a two-dimensional trivial multiplicity space, the two linear
readouts

\[
 N_1(B)=e_1^*Be_1,
 \qquad N_2(B)=e_1^*Be_2
 \tag{5.1}
\]

are equally group invariant, yet for `B=I_2` they give `1` and `0`.  This is an underdetermination
guard, not a proposed numerator.  It shows that representation type alone cannot decide numerator
survival or whether additional coefficient blocks are needed.

The minimal missing frozen input is an exact outer incidence map (or numerator functional), its
domain and codomain, and the identity connecting it to the physical adversary built from `B`.
Only after that map is supplied can one prove whether it preserves `Hom_Q`, vanishes on the
restricted construction, or requires additional components.  At present there is no license to
claim either requirement or nonrequirement of nonequivariant numerator components.

## 6. Decision ledger

| question | exact decision | reason |
|---|---|---|
| Does `E_s` preserve `Hom_(S_q)`? | **YES** | covariance plus relabelling of the complete raw-value sum, (2.3) |
| Does `B-E_s(B)` remain an `S_q` intertwiner? | **YES** | linearity, (2.5) |
| Do restricted `E_L,E_R` commute and remain self-adjoint? | **YES** | reviewed full-space commutation plus reducing-subspace lemma |
| Do explicit polynomial/resolvent/joint tapers close there? | **YES, when the displayed inverse/function is defined on the restriction** | restricted joint functional calculus |
| Are their block operator norms computable without the nonequivariant `S_q` complement? | **YES** | Schur block norm (3.2) |
| Does the `19456` position-suppressed slice suffice for those norms? | **NO LICENSE** | active position branches remain and suppression can change norm |
| Is `B-E_s(B)` already the literal physical query defect with the same norm? | **BLOCKED** | missing polar/range identity; exact strict-gap guard (4.5) |
| Does the outer numerator close on the restricted coefficient? | **BLOCKED** | numerator/incidence map is absent |
| Is the full strong sufficiency gate passed? | **NO: PARTIAL ONLY** | the two preceding physical interfaces are load-bearing |
| Is a nontrivial alphabet-carrier/Wigner spectrum proved necessary? | **NO** | no such obstruction is derived |
| May an arbitrary adversary be symmetrized without loss? | **NOT CLAIMED** | outside this fixed architecture and would require a separate SDP theorem |

## 7. Exact guards and reproducibility

Checker:
`ksum/tools/ksum_l3_equivariant_sufficiency_decision_check.py`

Run command:

```text
python ksum/tools/ksum_l3_equivariant_sufficiency_decision_check.py \
  --output ksum/artifacts/logs_ksum_L3_equivariant_sufficiency_decision_20260722/run.json \
  --log ksum/artifacts/logs_ksum_L3_equivariant_sufficiency_decision_20260722/run.log
```

The checker performs five independent exact gates.

1. It recomputes all hook dimensions and the three distinct ambient dimensions (1.8)--(1.11), and
   verifies all four reviewed transported position-branch resolutions.
2. In an exact `C_2` model with source isotypic multiplicities `(1,2)` and target multiplicities
   `(2,1)`, it constructs a covariant two-value positive effect family.  The transfer and defect
   have zero intertwiner residual; the restricted transfer is symmetric positive semidefinite; a
   commuting partner, polynomial, resolvent, and rational taper all remain equivariant.  The
   restricted commutator has rank zero and the exact resolvent denominator determinant is
   `300969285`.
3. It proves the position-carrier norm loss (3.4): the fixed-coordinate commutator has rank two and
   the true/suppressed defect norm squares are `1` and `1/4`.
4. It proves the literal/effect strict gap (4.5) exactly.
5. It proves numerator underdetermination (5.1) and pins every load-bearing reviewed source hash.

The executable status is
`ALL_EQUIVARIANT_SUFFICIENCY_DECISION_GUARDS_PASS`; this means the decision boundaries and
counterguards pass, not that the strong physical sufficiency gate passes.

## 8. Frozen sources and scope lock

Load-bearing reviewed inputs:

* occurrence-pencil Rule-7 review, SHA-256
  `000E1E77B1C7A2F6A8E06EBC91EF527173568EAE0D1A36ADB3D2DBAB6676D6A4`;
* direct-coset cross-side Rule-7 review, SHA-256
  `C3A7DFD24286F6C74A111DD01981D284E9A17F08B10E007766AC22AF0DDDECEB`;
* equivariant Schur--coset reducer Rule-7 review, SHA-256
  `E062009CA2BBD47A2EE0DB8BA5D667D2793430E55CBC587A9F7388DB65A0B6D6`;
* first-target Pieri Rule-7 review, SHA-256
  `DB65748CCE7C8F7E6541A203B9BEAE072DB479B58CBC090100156E9101A273CF`;
* induced bicovariant packet first-gate Rule-7 review, SHA-256
  `CF1E853AE7BEBC689963409A03D19BBA96684AF0C4BBAF4ED59155E2F64741F2`.

No unreviewed position-incidence proposal is load bearing.  This artifact does not compute a
private-child effect, a complete spectrum, a taper parameter, a small singular value, query
attenuation, a numerator, or an exponent.  It does not edit or change the status of the canonical
node.

## 9. Minimal continuation

The next admissible work is exactly:

1. freeze the literal marked-query/polar norm interface, retaining the active position `beta`
   blocks and all physical ranges; and
2. freeze the outer incidence/numerator map for the induced-packet multiplier.

If both maps preserve the alphabet-equivariant restriction and the required physical norms agree,
then the nontrivial `S_q`-carrier/Wigner spectrum can be removed from this candidate's
prerequisites.  If either map exposes a nontrivial `S_q` sector, that exact map supplies the first
valid obstruction.  Until then, choosing either conclusion would be a guess.
