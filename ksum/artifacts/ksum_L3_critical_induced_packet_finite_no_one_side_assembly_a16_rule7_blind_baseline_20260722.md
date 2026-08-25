# Hostile blind baseline: finite NO one-side assembly at `a=16`

Seal time: `2026-07-22T12:15:54.3143083-04:00`  
Controlling node id supplied as Rule-8(a) commission metadata:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

## 1. Blindness and sealed inputs

This baseline was frozen before opening any file whose name contains
`first_target_no_physical_assembly`, and before reading the controlling occurrence node's newest
paragraphs.  It fixes no desired verdict.  It derives the expected finite assembly using only the
following already reviewed inputs and the proposer-tier planning interface.

| input | SHA-256 observed before the seal |
|---|---|
| reviewed `s=4` occurrence artifact | `5A3CEF4C3A26C59FC0EDA3BF6DB1F9490F0D22D5096F9564A5671E400A1D5A91` |
| occurrence Rule-7 review | `1741AD66F658E28BEC4EE7E606052EBE5F575FA35069BFA4C285B0364861AC12` |
| exact occurrence JSON | `BAA0501B082D8ACD20A280A363198F68A13B8CD3989F78E7E9BD9B225A52FF16` |
| finite NO alphabet artifact | `ECF051FEF929E8B461E05539F8E2D227766C7AE0650EB30A8D7A1AB628E7B6D5` |
| alphabet Rule-7 review | `4A8FEE28DFD4FC91EEB6E7B5F89BC8A0A3C26491895AC1AFE6889982E1560137` |
| exact alphabet JSON | `8281115792877C373B88C53601E34F99C1DDC72BBCA45048CB16258559100976` |
| corrected transported Pieri artifact | `07EF9D8E3BBC901B19E74D1F457C7E7BF0BD0607B14FF6B629A8EB60640012DC` |
| Pieri Rule-7 review | `DB65748CCE7C8F7E6541A203B9BEAE072DB479B58CBC090100156E9101A273CF` |
| exact Pieri JSON | `6C91B3C8D83EBFA0FF02DED17BE429DFB104CECA98C7A31DED685E257B544EBA` |
| one-point Gram-stack planning interface | `7EC0E42F84D08E0C8E53DE3AEF82F2C482ACD86722CD6134253EB4C024DDADFF` |

The blind exact model does not import an assembly proposer:

| blind evidence | SHA-256 at seal |
|---|---|
| `ksum/artifacts/logs_ksum_L3_finite_no_one_side_assembly_rule7_review_20260722/independent_model.py` | `D09C4D81F43C1AB74DF145E0FECC2ABCED7BB3B95806EC70D97FBF0F0A1BFC00` |
| `ksum/artifacts/logs_ksum_L3_finite_no_one_side_assembly_rule7_review_20260722/blind_model.json` | `1FB57BB03525AD4DB76C648DAD8A4B240B0B6041E10D1EE76F2C2A648BAC91BC` |
| `ksum/artifacts/logs_ksum_L3_finite_no_one_side_assembly_rule7_review_20260722/blind_model.log` | `CA9AFC80ADD0ACF8CB3B1FDA4154B1244C1CAE16600DBCDFAC552148AD6E5992` |

The exact result line is `ALL_BLIND_EXACT_MODEL_GATES_PASS`.  No floating-point value is used to
decide a rank, kernel, image, product, commutator, or algebra dimension.

## 2. Finite scope and spaces

Fix

\[
 (s,a,d,r,q,t,\tau)=(4,16,17,4,64,0,(61,2)),\qquad D=a-1=15,
\]

and one common raw marked letter.  The complete parent closure has multiplicities `1,3,6`, so its
packet multiplicity space `P` has dimension ten.  In the common marked Mackey gauge it has the
orthogonal resolution

\[
 I_P=P_A+P_B+P_{L,1}+P_{L,V}+P_{R,1}+P_{R,V},
\]

with ranks

\[
 (1,1,3,1,3,1).
\]

This is not an old-parent diagonalization.  In the parent gauge every one of the six projectors
has nonzero blocks across every pair of old parents.  The orthogonal resolution exists because
all six are conjugated by one common exact orthogonal matrix `E`.

Let `Z_L` and `Z_R` be the two four-dimensional occurrence spaces.  In the archived rational
occurrence basis their positive Gram is

\[
 G=\operatorname{diag}\left(
 {233245657600\over39},
 {37699701339916525\over14836},
 {252885664381001925\over1388384},
 {130423121542000\over93351}
 \right).
\]

The left active space and full source are

\[
 \mathcal H_{\rm act}=P\otimes Z_L,\quad \dim\mathcal H_{\rm act}=40,
 \qquad
 \mathcal H_{\rm full}=P\otimes Z_L\otimes Z_R,\quad
 \dim\mathcal H_{\rm full}=160.
\]

Their basis Grams are

\[
 \Gamma_{\rm act}=I_{10}\otimes G_L,
 \qquad
 \Gamma_{\rm full}=I_{10}\otimes G_L\otimes G_R.
\]

## 3. Form versus endomorphism convention

The occurrence JSON supplies symmetric bilinear-form matrices `H_(kappa,eta)`.  The corresponding
endomorphism in the rational basis is

\[
 O_{\kappa,\eta}=G^{-1}H_{\kappa,\eta},
 \qquad
 O_{\kappa,\eta}^{\dagger_G}
 =G^{-1}O_{\kappa,\eta}^{T}G=O_{\kappa,\eta}.
\]

For any assembled symmetric form `H`, the physical source effect is

\[
 \boxed{Q=\Gamma^{-1}H.}
\]

Consequently the correctly typed commutator form and effect are

\[
 K^{\rm form}_{ij}
 =H_i\Gamma^{-1}H_j-H_j\Gamma^{-1}H_i
 =\Gamma[Q_i,Q_j],
\]

\[
 [Q_i,Q_j]^{\dagger_\Gamma}=-[Q_i,Q_j].
\]

The commutator form is ordinary skew-symmetric.  It has the same rank and kernel as the effect
commutator, but

\[
 \operatorname{im}K^{\rm form}_{ij}
 =\Gamma\operatorname{im}[Q_i,Q_j],
\]

so their coordinate images must not be identified.

For a left effect the untouched right occurrence factor is

\[
 Q_{\rm full}=Q_{\rm act}\otimes I_{Z_R},
 \qquad
 H_{\rm full}=H_{\rm act}\otimes G_R.
\]

Thus `I_4` is correct at endomorphism level and `G_R` is correct at form level.  Omitting the
factor, or using `I_4` in the form, is a type error.

## 4. Correct finite NO assembly

The actual left statuses are rare `A` and heavy `H_L`; the actual right statuses are rare `B`
and heavy `H_R`.  The position children and transported heavy paths are exactly

| position child | legal `kappa` paths and corrected transported `p^2` |
|---|---|
| `beta_T=(282,4,1)` | `kappa_T:1`, `kappa_M:2/9275`, `kappa_B:4/19099` |
| `beta_M=(283,3,1)` | `kappa_M:9273/9275` |
| `beta_B=(283,4)` | `kappa_B:19095/19099` |

Rare `A/B` has only `beta_T` and `p^2=1`.  The heavy coefficients above are licensed by the
corrected identities containing `rho_lambda(g)`.  The uncorrected no-transport operator displays
do not produce these values and may not be cited as their derivation.

The status weights are

\[
 w_A=w_B={1\over18},\qquad w_H={17\over18}.
\]

The normalized coevaluation contributes `d_eta/D` in the Gram, with

\[
 (d_{\mathbf1},d_{V_{15}})=(1,14),
 \qquad
 (d_\eta/D)=(1/15,14/15).
\]

For `eta in {1,V15}` define

\[
 X^L_{\beta,\eta}
 ={17\over18}{d_\eta\over15}
 \sum_{\kappa\leadsto\beta}p_{\beta,\kappa}^{,2}O_{\kappa,\eta}.
\]

Then the complete left inventory at effect level is

\[
 Q_A^L={1\over18}P_A\otimes I_L\otimes I_R,
\]

\[
 \boxed{
 Q_\beta^L
 =P_{L,1}\otimes X^L_{\beta,1}\otimes I_R
 +P_{L,V}\otimes X^L_{\beta,V}\otimes I_R,
 \quad \beta\in\{T,M,B\}.}
\]

At form level the identical statement is

\[
 H_A^L={1\over18}P_A\otimes G_L\otimes G_R,
\]

\[
 H_\beta^L={17\over18}\sum_{\eta,\kappa}
 {d_\eta\over15}p_{\beta,\kappa}^{,2}
 P_{L,\eta}\otimes H_{\kappa,\eta}\otimes G_R.
\]

The right mirror exchanges `A,L,Z_L` with `B,R,Z_R` and has the same ranks.  No side or status is
added merely for symmetry.

The transported Pieri resolution and the occurrence resolution give

\[
 \sum_{\beta=T,M,B}Q_\beta^L
 ={17\over18}\left(
 {1\over15}P_{L,1}+{14\over15}P_{L,V}
 \right)\otimes I_L\otimes I_R.
\]

This is a fixed-child, fixed-mark sector identity, not a full raw-value/point-child query
resolution.

## 5. Predicted branch ranks, kernels, images, and supports

| branch | eta ranks on active `40` | active rank/kernel | full rank/kernel |
|---|---:|---:|---:|
| rare `A` | not applicable | `4 / 36` | `16 / 144` |
| `beta_T` | `12 + 4` | `16 / 24` | `64 / 96` |
| `beta_M` | `6 + 4` | `10 / 30` | `40 / 120` |
| `beta_B` | `12 + 4` | `16 / 24` | `64 / 96` |

The eta-sector full ranks are respectively `48+16`, `24+16`, and `48+16` for `T,M,B`.

Let

\[
 \mathcal S_A=\operatorname{im}P_A\otimes Z_L,
 \qquad
 \mathcal S_L=(\operatorname{im}P_{L,1}\oplus\operatorname{im}P_{L,V})\otimes Z_L.
\]

Then, on the active space,

\[
 \dim\mathcal S_A=4,\qquad \dim\mathcal S_L=16,
\]

\[
 \operatorname{supp}Q_T^L=\operatorname{supp}Q_B^L=\mathcal S_L,
 \qquad
 \operatorname{supp}Q_M^L\subsetneq\mathcal S_L,
\]

and rare/heavy products vanish in both orders.  The `eta=1` and `eta=V15` contributions also
annihilate each other in both orders.  Every full support is the stated active support tensored
with `Z_R`.

## 6. Predicted commutators

Put

\[
 \gamma={9273\over9275},\qquad
 \delta={19095\over19099},\qquad
 K=[O_{M,1},O_{B,1}].
\]

The occurrence input gives

\[
 \operatorname{rank}K=2,
 \qquad
 [O_{M,V},O_{B,V}]={1\over196}K.
\]

The three branch commutators are nonzero scalar multiples of the same blocks:

\[
 [X_T,X_M]=[X_M,X_B]=-[X_T,X_B]
\]

after suppressing the common positive eta-dependent scalar.  The `14/15` coevaluation factor
exactly cancels the `1/196` in the `V15` commutator at the squared commutator level, so the two eta
blocks have the same underlying `K` up to the same nonzero scalar.

In the archived rational occurrence coordinates,

\[
 \ker K=\operatorname{span}\left\{
 \begin{pmatrix}1\\1839664/39414687\\0\\0\end{pmatrix},
 \begin{pmatrix}1\\0\\248082006656/3823690659711\\-43039904/123251765\end{pmatrix}
 \right\},
\]

and one normalized image basis is

\[
 \operatorname{im}K=\operatorname{span}\left\{
 \begin{pmatrix}0\\0\\1\\134518791/5553536\end{pmatrix},
 \begin{pmatrix}1\\-474752/9414979\\0\\115412953/9414979\end{pmatrix}
 \right\}.
\]

For every unordered pair among `T,M,B`, the active effect commutator has

\[
 \operatorname{rank}=8,qquad \dim\ker=32,qquad\dim\operatorname{im}=8.
\]

More precisely, its eta ranks are `6` and `2`, and

\[
 \ker[Q_\beta,Q_{\beta'}]
 =\left(\operatorname{im}(P_A+P_B+P_{R,1}+P_{R,V})\otimes Z_L\right)
 \oplus\left(\operatorname{im}P_{L,1}\otimes\ker K\right)
 \oplus\left(\operatorname{im}P_{L,V}\otimes\ker K\right),
\]

\[
 \operatorname{im}[Q_\beta,Q_{\beta'}]
 =\left(\operatorname{im}P_{L,1}\otimes\operatorname{im}K\right)
 \oplus\left(\operatorname{im}P_{L,V}\otimes\operatorname{im}K\right).
\]

The full commutator tensors these spaces with `Z_R`, so its rank, kernel dimension, and image
dimension are `32,128,32`.

## 7. Predicted generated algebras and commutants

For either fixed eta, the three reduced heavy branch operators generate

\[
 M_1(\mathbb Q)\oplus M_3(\mathbb Q),
 \qquad \dim=10,
\]

with commutant dimension two.  The `eta=1` packet multiplicity is three and the `eta=V15` packet
multiplicity is one.  Their different aggregate eigenvalues `1/15` and `14/15` make the two eta
central sectors separately recoverable.  Adding the rare projector and the unobserved packet
complement gives the complete left unital algebra

\[
 \boxed{
 \mathcal A_L
 \cong
 \mathbb C\oplus\mathbb C\oplus\mathbb C\oplus M_3
 \oplus\mathbb C\oplus M_3,
 \qquad \dim\mathcal A_L=22.}
\]

On the active `40`-space its carrier-block dimensions are

\[
 20,4,3,9,1,3,
\]

and

\[
 \mathcal A_L'
 \cong M_{20}\oplus M_4\oplus M_3\oplus M_3\oplus M_1\oplus M_1,
 \qquad \dim\mathcal A_L'=436.
\]

On the full `160`-space the algebra still has dimension `22`, while the passive right factor
changes the carrier-block dimensions to

\[
 80,16,12,36,4,12
\]

and the commutant to

\[
 M_{80}\oplus M_{16}\oplus M_{12}\oplus M_{12}\oplus M_4\oplus M_4,
 \qquad \boxed{\dim\mathcal A_{L,\rm full}'=6976}.
\]

The right mirror has the identical classification.

## 8. Same-mark cross-side prediction

At one common fixed raw mark, the left packet supports are `A,L1,LV15`, while the right supports
are `B,R1,RV15`.  They are distinct projectors in the same six-term orthogonal resolution.
Therefore every one of the `4 x 4=16` products between the complete left inventory
`{rare A,T,M,B}` and the complete right inventory `{rare B,T,M,B}` is exactly zero in both
orders.  Hence every same-mark cross-side commutator vanishes.

This conclusion uses a common marked stabilizer.  It says nothing about two distinct raw marks,
whose point-stabilizer projectors are conjugate rather than one common orthogonal resolution.

## 9. Hostile attacks frozen before comparison

1. **Naive raw-form multiplication.**  Computing `[H_i,H_j]` is wrong in the nonorthonormal
   occurrence basis.  The blind model obtains naive ranks `10,16,10` for `TM,TB,MB`, rather than
   the correctly typed active rank `8` for all three.  The target must use a `Gamma^{-1}` between
   forms or convert every form to an endomorphism first.
2. **Omitted `rho_lambda(g)`.**  The heavy `p^2` table is the transported table.  The old
   no-transport display kills the middle/bottom path and fails its invariant-line resolution.
3. **Absorbed coevaluation/status/Pieri factors.**  `w`, `d_eta/D`, and `p^2` are three separate
   factors.  Each occurs exactly once.  In particular, `14/15` is not already hidden in the
   normalized `O_(kappa,V15)` or alphabet projector.
4. **Old-parent pinching.**  Parent multiplicities `1+3+6` remain one ten-dimensional row domain.
   Every same-mark alphabet projector has genuine old-parent off-diagonal blocks.  Pinching them
   changes the physical operator even though the unpinched six projectors commute.
5. **Missing untouched factor.**  Full left ranks are active ranks times four.  The untouched
   factor is `I_R` for effects and `G_R` for forms.
6. **Form-versus-effect commutators.**  Ranks and kernels agree only after the correct invertible
   Gram conversion; coordinate images are related by `Gamma` and are not literally the same.
7. **Type/dimension mismatch.**  All active maps are `40 -> 40`, all full maps are `160 -> 160`,
   and `Gamma` has the matching dimension.  Literal marked rows and their codomain images are not
   part of this source-effect calculation.
8. **Colored/fixed sector substituted for a full sum.**  This is one `tau`, one raw mark, and one
   answer.  Its beta/status resolution is not the full query normalization over all marks and
   point children.
9. **Values right while formula broken.**  Exact values cannot repair an omitted transporter,
   wrong form product, or missing Gram factor.  Formula identities and matrix values are separate
   gates.
10. **Numerical inference.**  Floating ranks or small residuals prove none of the exact claims.
    Exact rational/algebraic equality is required.

## 10. Rule-7 scope freeze

The positive quantifier is exactly: finite NO, `s=4,a=16,d=17,q=64,tau=(61,2)`, complete
`1+3+6` parent closure, all six same-mark alphabet sectors, all three NO position children, both
eta sectors, both four-dimensional occurrence factors, and one fixed common raw mark.

Explicitly withheld regardless of the comparison outcome: YES; two distinct raw marks; any other
`s`; a uniform-`s` statement; transfer/resolvent feasibility; query attenuation or query bound;
coefficient norm; numerator; lower bound; and exponent.

The exact checker reconstructs the same object from reviewed forms, a common alphabet gauge, and
corrected transported Pieri data.  A later rerun of a proposer would establish reproducibility
only, not independence.  Any target derivation that matches only numerical values but fails one of
the typed identities above must not receive a passing formula verdict.
