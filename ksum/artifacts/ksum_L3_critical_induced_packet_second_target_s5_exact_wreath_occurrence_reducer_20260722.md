# L3 induced packet: exact second-target `s=5` wreath occurrence reducer

Date: 2026-07-22  
Controlling node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

Tier: proposer-side exact calculation, pending fresh Rule-7 review.  This calculation remains
inside the already registered occurrence-pencil classification node.  It creates no new route and
changes no canonical/shared DAG file.  The reviewed `s=4` tool, artifact, and logs were not edited.

## 1. Exact finite-target verdict

At the second critical target

\[
 (s,a,d,r)=(5,25,21,5),\qquad
 \theta=(519,5,1),
\tag{1.1}
\]

the exact reduced calculation constructs all six occurrence matrices

\[
 \mathsf O_{\kappa,\eta}\in\operatorname{End}(\mathbb Q^7),
 \qquad
 \begin{aligned}
 \kappa&\in\{(518,5,1),(519,4,1),(519,5)\},\\
 \eta&\in\{\mathbf1,V_{24}\}.
 \end{aligned}
\tag{1.2}
\]

The expected occurrence multiplicity is confirmed exactly:

\[
 C_5=7.
\tag{1.3}
\]

The proposed extrapolation from `s=4`, however, fails at this finite point.  The common exact
operator algebra is not `M_1(Q) direct_sum M_6(Q)`.  Instead,

\[
 \boxed{
 \mathcal A_{s=5}
 \cong M_1(\mathbb Q)\oplus M_1(\mathbb Q)\oplus M_5(\mathbb Q).}
\tag{1.4}
\]

Thus two common invariant lines survive.  In the rational algebra basis used in the JSON, they are

\[
 \begin{aligned}
 L_-&=\operatorname{span}\left(
 1,-{10197\over23035},-{3700\over677229},{1330086\over115175},
 {45880\over677229},0,0\right),\\
 L_+&=\operatorname{span}\left(
 1,1,{236\over9261},0,0,0,0\right).
 \end{aligned}
\tag{1.5}
\]

Every pair with distinct `kappa` has exact commutator rank `2`; each same-`kappa` pair has rank
`0`.  This remains an occurrence-only, finite-`s` statement.  It is not an assembled physical
query-pencil result and supplies no asymptotic inference.

## 2. Reduced construction and the avoided scale

Put `H=S_21^25`.  As at `s=4`, use the tabloid model

\[
 S^{(519,5,1)}
 =\bigcap_{i,v}\ker\psi_{i,v}
 \subset M^{(519,5,1)}
\tag{2.1}
\]

and take block invariants before solving the James kernels.  A labelled `H`-orbit is specified by
a five-point row-two occupancy and the block containing the row-three singleton.  There are

\[
 25{29\choose5}=2,968,875
\tag{2.2}
\]

such labelled keys.  The new tool does **not** enumerate them.  It constructs occupancy multisets
directly from integer partitions of a tail of size at most five.

After fixing block zero and quotienting the remaining twenty-four block labels, the James domain
has dimension `64`.  Quotienting all twenty-five block labels gives dimension `19`.  The exact
stacked James ranks are

\[
 56\text{ in dimension }64,
 \qquad
 18\text{ in dimension }19.
\tag{2.3}
\]

Consequently,

\[
 \dim(S^\theta)^{H\rtimes S_{24}}=8,
 \qquad
 \dim(S^\theta)^{H\rtimes S_{25}}=1,
\tag{2.4}
\]

and the standard-isotypic fixed-line difference is

\[
 8-1=7.
\tag{2.5}
\]

The complete exact horizontal-strip recurrence independently returns

\[
 \begin{aligned}
 [s_{(519,5,1)}]h_{21}^{25}&=1,883,700,\\
 [s_{(518,5,1)}]h_{20}h_{21}^{24}&=1,883,700,\\
 [s_{(519,4,1)}]h_{20}h_{21}^{24}&=322,920,\\
 [s_{(519,5)}]h_{20}h_{21}^{24}&=98,280.
 \end{aligned}
\tag{2.6}
\]

No dense Specht carrier and no dense matrix on any space in (2.6) is built.

## 3. Exact 21-point block swaps

On a labelled occupancy key, the adjacent swap `s_i` exchanges the two occupancy pairs at blocks
`i,i+1` and sends the row-three block label `j` to `s_i(j)`.  This gives all twenty-four physical
adjacent 21-point block swaps.  The tool verifies exactly

\[
 s_i^2=1,
 \qquad
 s_is_{i+1}s_i=s_{i+1}s_is_{i+1},
 \qquad
 s_is_j=s_js_i\quad(|i-j|>1).
\tag{3.1}
\]

There is no need to check nearly three million keys individually.  The unnormalised orbit weight
is a product of local factors

\[
 {21\choose c_i}{21-c_i\choose b_i},
 \qquad c_i\in\{0,1\},
\tag{3.2}
\]

and swapping two blocks simply exchanges two factors.  The tool exhausts the `63` possible local
tail cases and checks (3.2) exactly.  Since the James maps are symmetric-group equivariant, their
kernels inherit this normalizer action.

## 4. Marked relative-JM branch projectors

Mark one point in block zero, changing its internal block size from `21` to `20`.  The direct
marked orbit quotient has dimension `121`.  On it construct

\[
 J_x=\sum_{y\ne x}(x\ y).
\tag{4.1}
\]

The three removable-corner contents of `theta` are

\[
 c_T=518,\qquad c_M=3,\qquad c_B=-2.
\tag{4.2}
\]

Thus the exact branch projectors on the source Specht columns are

\[
 \begin{aligned}
 P_T&={(J_x-3I)(J_x+2I)\over267800},\\
 P_M&={(J_x-518I)(J_x+2I)\over-2575},\\
 P_B&={(J_x-518I)(J_x-3I)\over2600}.
 \end{aligned}
\tag{4.3}
\]

Rather than form dense projectors, the tool applies the degree-two polynomials in (4.3) directly
to the seven source columns.  It verifies the exact cubic corner polynomial, eigenvalue equations,
mutual Gram orthogonality, and

\[
 P_T+P_M+P_B=I
\tag{4.4}
\]

on those columns.  The marked `J_x` matrix is exactly self-adjoint for the invariant orbit Gram.

## 5. The six exact `7 x 7` occurrence matrices

The deterministic rational Gram-orthogonal source basis `v_1,...,v_7` has squared norms

\[
 \begin{aligned}
 n_1&={19152478455818400\over323},\\
 n_2&={192491066722685068800\over3081553},\\
 n_3&={577481028782666676921428868\over13549812817},\\
 n_4&={68372398054832720688000\over167451457799},\\
 n_5&={6643039682072109119463891\over6865552807},\\
 n_6&={5474196098371353647448\over198050201},\\
 n_7&={14116835563919550\over214079}.
 \end{aligned}
\tag{5.1}
\]

Let `G=diag(n_1,...,n_7)` and

\[
 H^\mathbf1_\kappa[i,j]
 =\langle P_\kappa v_i,P_\kappa v_j\rangle.
\tag{5.2}
\]

The exact orthonormal occurrence entries are encoded in `run.json` as

\[
 \mathsf O_{\kappa,\mathbf1}[i,j]
 ={H^\mathbf1_\kappa[i,j]\over\sqrt{n_in_j}}.
\tag{5.3}
\]

No decimal approximation or hidden radical simplification is used.  The `V_24` table follows from

\[
 V_{25}\downarrow S_{24}=\mathbf1\oplus V_{24},
 \qquad \dim V_{25}=24,\quad\dim V_{24}=23,
\tag{5.4}
\]

and the exact trace identity

\[
 \boxed{
 H^\mathbf1_\kappa+23H^{V_{24}}_\kappa
 =24{f^\kappa\over f^\theta}G.}
\tag{5.5}
\]

The hook dimensions are

\[
 \begin{array}{c|r}
 \theta=(519,5,1)&139672485907500\\
 \kappa_T=(518,5,1)&138073135358211\\
 \kappa_M=(519,4,1)&1279485207936\\
 \kappa_B=(519,5)&319865341353.
 \end{array}
\tag{5.6}
\]

They sum exactly as required by Young branching.  The six matrix ranks are

| `kappa` | `eta=1` | `eta=V24` |
|---|---:|---:|
| `T` | 7 | 7 |
| `M` | 5 | 7 |
| `B` | 6 | 7 |

All six exact characteristic-polynomial sign gates certify positive semidefiniteness.  Both
resolutions hold:

\[
 \sum_\kappa H^\mathbf1_\kappa=G,
 \qquad
 \sum_\kappa H^{V_{24}}_\kappa=G.
\tag{5.7}
\]

The complete six rational `7 x 7` `H` matrices and their normalization data are stored in the JSON.

## 6. Pairwise commutators and generated algebra

For exact rational algebra gates the tool uses a smaller pre-Gram--Schmidt fixed-line basis.  If
`G_0` and `H_0` are its exact rational Gram and occurrence forms, put

\[
 A_{\kappa,\eta}=G_0^{-1}H_{0,\kappa}^{\eta}.
\tag{6.1}
\]

This is rationally similar to the orthonormal matrices in (5.3), so commutator ranks, commutant
dimension, generated-algebra dimension, and invariant-block sizes are unchanged.

The exact pairwise commutator ranks are

| left/right | `T,1` | `T,V24` | `M,1` | `M,V24` | `B,1` | `B,V24` |
|---|---:|---:|---:|---:|---:|---:|
| `T,1` | - | 0 | 2 | 2 | 2 | 2 |
| `T,V24` |  | - | 2 | 2 | 2 | 2 |
| `M,1` |  |  | - | 0 | 2 | 2 |
| `M,V24` |  |  |  | - | 2 | 2 |
| `B,1` |  |  |  |  | - | 0 |
| `B,V24` |  |  |  |  |  | - |

Each rank-2 entry includes an exact nonzero `2 x 2` minor witness after one harmless global
rational scaling.  The same-`kappa` zeros also follow from (5.5), but are checked directly.

Because `B,1=I-T,1-M,1` and each `eta=V24` operator is affine in its `eta=1` partner, the common
commutant can be solved from `T,1` and `M,1`.  Exact `QQ` nullspace gives

\[
 \dim\mathcal A'=3.
\tag{6.2}
\]

A deterministic self-adjoint element of this commutant has characteristic polynomial

\[
 {(lambda-3)^5(5605\lambda-21039647)
 (52725\lambda+1179431509)\over295523625}.
\tag{6.3}
\]

Its exact rational eigenspaces have dimensions `5,1,1`, are pairwise `G_0`-orthogonal, and the two
one-dimensional spaces are precisely (1.5).  Exact word closure from `T,1,M,1` has dimension

\[
 \dim\mathcal A=27=5^2+1^2+1^2.
\tag{6.4}
\]

The dimension reaches the full block-diagonal maximum on the three rational eigenspaces, proving
(1.4).  Therefore the proposed `M_1 direct_sum M_6` finite-target pattern is false at `s=5` at
proposer tier.  A completion-tier refutation or any uniform statement still requires fresh review
and appropriate quantifiers.

## 7. Exact gates and scope controls

The run checks, without floating point:

1. the four horizontal-strip-chain counts (2.6);
2. reduced block-swap Coxeter and local Gram formulas;
3. all James maps, kernel residuals, and `C_5=7`;
4. marked/unmarked Gram compatibility and `J_x` self-adjointness;
5. the corner minimal polynomial, exact eigencolumns, and branch resolution;
6. all six matrix ranks, PSD characteristic-polynomial gates, trace identities, and eta
   resolutions;
7. all fifteen commutator ranks and twelve nonzero-minor witnesses;
8. commutant dimension `3`, rational `1+1+5` eigenspaces, their Gram orthogonality, and generated
   algebra dimension `27`.

The new tool imports reusable combinatorics from the frozen reviewed `s=4` reducer only after
checking its SHA-256 equals
`06B842F0475B85691A76128864BE22D6996BBECDC7A9981FE6111929CA28F371`.
No SE-specific array or physical coefficient is imported.

This artifact contains no alphabet point-child table, Pieri scalar, assembled left/right Gram,
NO/YES transfer, query attenuation, numerator, or exponent conclusion.

## 8. Provenance

Command:

```powershell
python ksum/tools/ksum_l3_wreath_occurrence_reducer_s5.py `
  --json ksum/artifacts/logs_ksum_L3_wreath_occurrence_reducer_s5_20260722/run.json `
  --log ksum/artifacts/logs_ksum_L3_wreath_occurrence_reducer_s5_20260722/run.log
```

Files:

* new tool: `ksum/tools/ksum_l3_wreath_occurrence_reducer_s5.py`, SHA-256
  `C086195BCB3AF0976CAD84B35750B3B89A4D4D50729B40374816618B2820BAE1`;
* complete exact JSON:
  `ksum/artifacts/logs_ksum_L3_wreath_occurrence_reducer_s5_20260722/run.json`, SHA-256
  `11B7C2EF09D38B171C4721452CE4D0D4A4F07C4711282D30A1429CEB95B88933`;
* human-readable exact log:
  `ksum/artifacts/logs_ksum_L3_wreath_occurrence_reducer_s5_20260722/run.log`, SHA-256
  `06916370884E1AD3F94899DAFD91124F898C4D87792E92ED1A6D022ABDA90583`.

## 9. Stopping point

This second target materially changes the occurrence-side pattern: the finite algebra gains a
second scalar block rather than extending the `s=4` scalar-plus-active decomposition from `1+3`
to `1+6`.  No asymptotic decomposition law should be inferred from two points.  The controlling
node remains OPEN, this artifact is pending fresh Rule-7 review, and the physical classification
still needs the alphabet/Pieri assembly required by the one-point Gram-stack specification.
