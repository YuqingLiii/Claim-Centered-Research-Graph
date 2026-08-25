# First-target exact NO same-mark physical assembly at `a=16`

Date: 2026-07-22

Controlling canonical node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

Tier: **proposer-side exact finite result, pending fresh independent Rule-7 review**.  Nothing in
this artifact changes a DAG status.  The scope is only

\[
 (s,a,d,r,q,n,N)=(4,16,17,4,64,288,576),\qquad
 t=0\ ({\rm NO}),\qquad \tau=(61,2),
\]

for one fixed raw mark.  The calculation assembles the complete left branch stack, its right
mirror, and their same-mark direct sum.  It makes no YES, distinct-mark, uniform-`s`, asymptotic,
query-lower-bound, numerator, or exponent claim.

## 1. Reviewed inputs and frozen scope

Only the following three finite tables are used.

1. The reviewed `s=4` occurrence table:
   `ksum/artifacts/logs_ksum_L3_wreath_occurrence_reducer_20260722/run.json`, SHA-256
   `BAA0501B082D8ACD20A280A363198F68A13B8CD3989F78E7E9BD9B225A52FF16`.
   Its fresh Rule-7 review is
   `ksum/artifacts/ksum_L3_critical_induced_packet_first_target_exact_wreath_occurrence_reducer_rule7_review_20260722.md`,
   SHA-256 `1741AD66F658E28BEC4EE7E606052EBE5F575FA35069BFA4C285B0364861AC12`.
2. The reviewed NO alphabet point-child table at `a=16,q=64,tau=(61,2)`:
   `ksum/artifacts/logs_ksum_L3_alphabet_point_child_gate_20260722/run.json`, SHA-256
   `8281115792877C373B88C53601E34F99C1DDC72BBCA45048CB16258559100976`.
   Its fresh Rule-7 review is
   `ksum/artifacts/ksum_L3_critical_induced_packet_alphabet_point_child_gate_a16_rule7_review_20260722.md`,
   SHA-256 `4A8FEE28DFD4FC91EEB6E7B5F89BC8A0A3C26491895AC1AFE6889982E1560137`.
3. The reviewed corrected transported Pieri table:
   `ksum/artifacts/logs_ksum_L3_first_target_pieri_scalars_a16_20260722.json`, SHA-256
   `6C91B3C8D83EBFA0FF02DED17BE429DFB104CECA98C7A31DED685E257B544EBA`.
   Its fresh Rule-7 review is
   `ksum/artifacts/ksum_L3_critical_induced_packet_first_target_pieri_recoupling_scalars_a16_rule7_review_20260722.md`,
   SHA-256 `DB65748CCE7C8F7E6541A203B9BEAE072DB479B58CBC090100156E9101A273CF`.

The checker pins all six hashes before reading any value.  In particular, the occurrence review
licenses the finite forms and their source Gram, the alphabet review licenses exactly the one-mark
NO point-child resolution, and the Pieri review licenses the finite table only after inserting
the physical move-to-last transporter.  None of those reviews licenses the present assembly; that
is why this result remains pending review.

## 2. Domain, gauge, form, and effect

The all-parent alphabet multiplicity at `tau=(61,2)` has dimension ten.  Each occurrence
multiplicity has dimension `C_4=4`.  Thus the active left source, after suppressing the untouched
right occurrence factor, is

\[
 \mathcal S_L^{\rm act}=Y_{0,\tau}\otimes Z_L,
 \qquad \dim\mathcal S_L^{\rm act}=10\cdot4=40.
\]

Restoring the untouched factor gives

\[
 \mathcal S=Y_{0,\tau}\otimes Z_L\otimes Z_R,
 \qquad \dim\mathcal S=10\cdot4\cdot4=160.
\]

### 2.1 Alphabet gauge

The reviewed orthogonal matrix `E` has marked-Mackey rows and canonical all-parent columns.  The
checker parses every radical exactly, verifies `E^T E=I_10`, and independently verifies all six
archived identities

\[
 \mathsf C_\chi=E^T D_\chi E.
\]

It then conjugates the source by `E`.  In this common orthonormal marked-Mackey gauge the alphabet
matrices are the six pairwise orthogonal coordinate projectors

\[
 D_A,D_B,D_{L,1},D_{L,V},D_{R,1},D_{R,V}
\]

of ranks `1,1,3,1,3,1`, and their sum is exactly `I_10`.  This is a simultaneous gauge change on
all physical effects, not a parent pinch: the archived parent-gauge matrices retain their reviewed
nonzero cross-parent entries.

### 2.2 Occurrence gauge and the required `G^{-1}H`

The occurrence source basis consists of the reviewed rational Gram-orthogonal vectors `v_h`; it is
not normalized.  Its exact source Gram is

\[
 G_{\rm occ}=\operatorname{diag}\left(
 {233245657600\over39},
 {37699701339916525\over14836},
 {252885664381001925\over1388384},
 {130423121542000\over93351}
 \right).
\]

For every `kappa in {T,M,B}` and `eta in {1,V15}`, the occurrence JSON supplies a symmetric
bilinear **form** `H_(kappa,eta)`.  The physical endomorphism is instead

\[
 A_{\kappa,\eta}=G_{\rm occ}^{-1}H_{\kappa,\eta}.
\]

The checker reconstructs all six `A` matrices this way, entrywise matches them against the
reviewed `operator_algebra` convention, and checks

\[
 G_{\rm occ}A_{\kappa,\eta}
 =A_{\kappa,\eta}^{T}G_{\rm occ}.
\]

No product of raw forms is used anywhere.  On the active source the Gram is

\[
 \Gamma_{40}=I_{10}\otimes G_{\rm occ},
\]

so every assembled form `H_beta` is converted to the effect
`F_beta=Gamma_40^{-1}H_beta`.  On the full source the Gram is

\[
 \Gamma_{160}=I_{10}\otimes G_{{\rm occ},L}\otimes G_{{\rm occ},R}.
\]

The untouched factor in a form is therefore its Gram, while the untouched factor in the
corresponding effect is the identity.

## 3. Transported Pieri data and exact assembly

The coefficients below come from the corrected table with
`rho_lambda(g_(272->288))` inserted.  The archived representative is the order-preserving
move-to-last cycle

\[
 1\mapsto17,\qquad j\mapsto j-1\quad(2\le j\le17).
\]

The review also shows that the endpoint transposition is an equivalent representative for this
finite scalar table.  The literal no-transport version of planning equations (5.4)/(5.6) is not
used.  The required NO squares are

\[
 p^2_{T,T}=1,quad p^2_{T,M}={2\over9275},quad
 p^2_{M,M}={9273\over9275},quad
 p^2_{T,B}={4\over19099},quad
 p^2_{B,B}={19095\over19099}.
\]

Put `w_H=17/18`.  In the marked alphabet gauge the left-heavy assembled **forms** are

\[
\begin{aligned}
 H_M={}&{17\over18}{9273\over9275}
 \left({1\over15}D_{L,1}\otimes H_{M,1}
       +{14\over15}D_{L,V}\otimes H_{M,V}\right),\\
 H_B={}&{17\over18}{19095\over19099}
 \left({1\over15}D_{L,1}\otimes H_{B,1}
       +{14\over15}D_{L,V}\otimes H_{B,V}\right),\\
 H_T={}&{17\over18}\sum_{\eta\in\{1,V\}}{d_\eta\over15}D_{L,\eta}\otimes
 \left(H_{T,\eta}+{2\over9275}H_{M,\eta}
                    +{4\over19099}H_{B,\eta}\right),
\end{aligned}
\]

where `(d_1,d_V)=(1,14)`.  The rare form and effect are

\[
 H_{\rm rare}={1\over18}D_A\otimes G_{\rm occ},
 \qquad
 F_{\rm rare}={1\over18}D_A\otimes I_4.
\]

Each displayed form was converted entrywise by `Gamma_40^{-1}`.  The right formulas are identical
after replacing `(D_A,D_L1,D_LV)` by `(D_B,D_R1,D_RV)` and making the right occurrence factor
active.

## 4. Correct endomorphism commutator

For the two non-top branches,

\[
 [F_M,F_B]
 =\alpha_1D_{L,1}\otimes[A_{M,1},A_{B,1}]
  +\alpha_VD_{L,V}\otimes[A_{M,V},A_{B,V}],
\]

where

\[
 \alpha_1=\left({17\over18}\right)^2{9273\over9275}{19095\over19099}{1\over15^2},
 \qquad
 \alpha_V=\left({17\over18}\right)^2{9273\over9275}{19095\over19099}
 {14^2\over15^2}.
\]

Both scalars are nonzero.  Exact rational elimination gives

\[
 \operatorname{rank}[A_{M,1},A_{B,1}]=2,
 \qquad
 \operatorname{rank}[A_{M,V},A_{B,V}]=2.
\]

In the rational occurrence coordinates, both kernels have the same exact basis

\[
 k_1=\left({39414687\over1839664},1,0,0\right),
 \qquad
 k_2=\left(-{123251765\over43039904},0,-{3833060\over20630571},1\right).
\]

One exact image basis for the `eta=1` commutator is

\[
\begin{aligned}
 u_{1,1}&=\left(0,0,{6724985\over954389258064},{20305\over118966272}\right),\\
 u_{1,2}&=\left(-{2614234805\over12181847670784},
 {12047165\over1113284040704},0,
 -{374871633305\over142500357210112}\right),
\end{aligned}
\]

and one exact image basis for the `eta=V15` commutator is

\[
\begin{aligned}
 u_{V,1}&=\left(0,0,{6724985\over187060294580544},{20305\over23317389312}\right),\\
 u_{V,2}&=\left(-{373462115\over341091734781952},
 {12047165\over218203671977984},0,
 -{374871633305\over27930070013181952}\right).
\end{aligned}
\]

Since `rank(D_L1)=3` and `rank(D_LV)=1`, the correctly typed active commutator has

\[
 \boxed{\operatorname{rank}[F_M,F_B]=3\cdot2+1\cdot2=8.}
\]

Its kernel and image are exactly

\[
\begin{aligned}
 \ker[F_M,F_B]
 ={}&\bigl(\operatorname{im}(D_A+D_B+D_{R,1}+D_{R,V})\otimes\mathbb Q^4\bigr)\\
 &\oplus\bigl(\operatorname{im}D_{L,1}\otimes\ker[A_{M,1},A_{B,1}]\bigr)\\
 &\oplus\bigl(\operatorname{im}D_{L,V}\otimes\ker[A_{M,V},A_{B,V}]\bigr),\\
 \operatorname{im}[F_M,F_B]
 ={}&\bigl(\operatorname{im}D_{L,1}\otimes\operatorname{im}[A_{M,1},A_{B,1}]\bigr)\\
 &\oplus\bigl(\operatorname{im}D_{L,V}\otimes\operatorname{im}[A_{M,V},A_{B,V}]\bigr).
\end{aligned}
\]

Thus the active kernel and image dimensions are `32` and `8`.  The checker also verifies the
required metric skew-adjointness

\[
 \Gamma_{40}[F_M,F_B]+[F_M,F_B]^T\Gamma_{40}=0.
\]

Restoring the untouched right occurrence factor tensors the commutator with `I_4`, so its exact
rank on the 160-dimensional source is

\[
 \boxed{8\cdot4=32.}
\]

The same conclusions hold for the right mirror.

## 5. Complete finite branch resolution and ranks

The occurrence effects obey, separately for both eta sectors,

\[
 A_{T,\eta}+A_{M,\eta}+A_{B,\eta}=I_4.
\]

Combining this with the transported Pieri square resolutions gives

\[
 F_T+F_M+F_B
 ={17\over18}\left({1\over15}D_{L,1}+{14\over15}D_{L,V}\right)\otimes I_4.
\]

This is the exact heavy-position resolution.  It is not a claim that a single fixed-mark effect is
the identity.  On the active 40-dimensional source, exact ranks and kernel dimensions are

| branch | rank | kernel dimension |
|---|---:|---:|
| `beta_T` heavy | 16 | 24 |
| `beta_M` heavy | 10 | 30 |
| `beta_B` heavy | 16 | 24 |
| rare `A` | 4 | 36 |
| rare plus all left-heavy branches | 20 | 20 |

The right mirror has the same ranks, with rare `B`.  On the 160-dimensional full source the
three heavy ranks become `64,40,64`, each rare rank becomes `16`, and each one-side total rank is
`80`.

At the same raw mark, every left alphabet projector is orthogonal to every right alphabet
projector.  Consequently every left branch times every right branch is exactly zero in both
orders.  The left-plus-right total has rank 160 because the six alphabet sectors resolve `I_10`
and every displayed weight is positive.  This is a finite same-mark resolution only; it says
nothing about two distinct raw marks.

## 6. Generated algebras and survival of the occurrence core

Exact unital algebra closure is performed over `Q` using multiplication in the physical
endomorphism algebra.  Because each generator is self-adjoint for the source metric, this is also
the physical star algebra.  In each eta sector, `A_M` and `A_B` generate a ten-dimensional algebra
with two-dimensional commutant and common invariant line

\[
 \operatorname{span}\left(1,{1839664\over39414687},0,0\right).
\]

Hence each eta-sector algebra is exactly

\[
 M_1(\mathbb Q)\oplus M_3(\mathbb Q).
\]

The full tuple closures are:

1. `beta_M,beta_B` plus the identity on the active 40-dimensional source:

   \[
   \mathbb Q_{\rm zero}\oplus
   (M_1\oplus M_3)_{L,1}\oplus
   (M_1\oplus M_3)_{L,V},
   \]

   of dimension `1+10+10=21`.  Its commutant dimension on the represented
   40-dimensional space is `596`.
2. Rare plus all three left-heavy branches plus the identity:

   \[
   \mathbb Q_{\rm inactive}\oplus\mathbb Q_A\oplus
   (M_1\oplus M_3)_{L,1}\oplus
   (M_1\oplus M_3)_{L,V},
   \]

   of dimension `22`.  Its represented commutant dimension is `436`.
3. The complete left/right NO same-mark branch stack on the 160-dimensional source:

   \[
   \mathbb Q_A\oplus\mathbb Q_B\oplus
   \bigoplus_{X\in\{L1,LV,R1,RV\}}(M_1\oplus M_3)_X,
   \]

   of dimension `42`.  Its represented commutant dimension is `1152`.

After complexification these are respectively
`C^3 direct_sum M_3(C)^2`, `C^4 direct_sum M_3(C)^2`, and
`C^6 direct_sum M_3(C)^4`.

Therefore the finite reviewed occurrence `M_1 direct_sum M_3` core **does survive** this physical
NO/same-mark assembly: the alphabet resolution produces separately isolatable copies rather than
averaging the noncommutative block away.  This statement is finite and proposer-tier.  It is not a
uniform critical-family theorem.

## 7. Reproduction and exact certificate

Tool:
`ksum/tools/ksum_l3_first_target_no_physical_assembly.py`, SHA-256
`B31EE99618772CC38DB8FDD705002C31370C52F63A490F70DF7A8F7A7699D770`.

Machine-readable exact output:
`ksum/artifacts/logs_ksum_L3_first_target_no_physical_assembly_20260722/run.json`, SHA-256
`428F8D33A60563A1F99787C98A78C5833CD2275A1C41975598284B553B17E009`.

Concise run log:
`ksum/artifacts/logs_ksum_L3_first_target_no_physical_assembly_20260722/run.log`, SHA-256
`4CA8972B9841A424FA3D376B861A618FBE441814187DA982A4A750BD7A42C5E9`.

Commands:

```text
python ksum/tools/ksum_l3_first_target_no_physical_assembly.py \
  --output-json ksum/artifacts/logs_ksum_L3_first_target_no_physical_assembly_20260722/run.json \
  --output-log ksum/artifacts/logs_ksum_L3_first_target_no_physical_assembly_20260722/run.log

python ksum/tools/ksum_l3_first_target_no_physical_assembly.py \
  --verify-log ksum/artifacts/logs_ksum_L3_first_target_no_physical_assembly_20260722/run.json
```

The fresh run begins `ALL_EXACT_FIRST_TARGET_NO_PHYSICAL_ASSEMBLY_GATES_PASS`; the verification
command returns `ARCHIVED_NO_PHYSICAL_ASSEMBLY_RESULT_VERIFIED`.  The JSON contains the exact
occurrence kernel/image bases, all form/effect matrix digests, the active kernel/image digests,
every algebra closure dimension, all frozen-input hashes, and 26 exact gates.

## 8. Review boundary

This artifact is an exact proposer work product, not an independent review.  Under DAG Rules 6--8,
its result must first be appended to the canonical node with an explicit pending-review marker;
only then may a fresh Rule-7 reviewer be commissioned.  A favorable review could bank only the
finite NO/same-mark assembly above.  It could not by itself license YES transfer, distinct-mark
commutation, a formula for arbitrary `s`, asymptotic attenuation, a numerator bound, a query lower
bound, or an exponent improvement.
