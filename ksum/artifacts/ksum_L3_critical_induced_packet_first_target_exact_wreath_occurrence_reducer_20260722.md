# L3 induced packet: exact first-target wreath occurrence reducer

Date: 2026-07-22  
Controlling node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

Tier: proposer-side exact calculation, pending fresh Rule-7 review.  This artifact was produced
inside the already registered occurrence-pencil node.  It registers no new route and changes no
canonical/shared DAG file.

## 1. Outcome and exact scope

For the first selected target

\[
 (s,a,d,r)=(4,16,17,4),\qquad
 \theta=(267,4,1),
\]

the occurrence/Pieri part of the one-point Gram stack has now been evaluated exactly.
The calculation constructs the physical action of the fifteen adjacent swaps of the sixteen
17-point blocks, extracts the four copies of

\[
 V_{16}=S^{(15,1)},
\]

marks one point in the distinguished block, and returns all six rationally encoded
`4 x 4` occurrence Grams

\[
 \mathsf O_{\kappa,\eta},\qquad
 \kappa\in\{(266,4,1),(267,3,1),(267,4)\},\quad
 \eta\in\{\mathbf 1,V_{15}\}.
\]

The six operators are noncommutative but reducible.  In one common exact rational basis:

* the two operators with the same `kappa` commute;
* every pair with different `kappa` has commutator rank exactly `2`;
* the common commutant has dimension `2`;
* the generated unital algebra has dimension `10` and is exactly
  `M_1(Q) direct_sum M_3(Q)`;
* the common invariant line is

  \[
  \operatorname{span}\left(1,{1839664\over39414687},0,0\right).
  \]

This is a finite `s=4` occurrence-side result only.  It does **not** construct the alphabet
point-child tables `C`, the Pieri scalars `p`, an assembled physical Gram stack, a NO/YES or L/R
commutator, an attenuating coefficient, a numerator, or an asymptotic theorem.

## 2. Why no dense Specht or dense 34272-space is needed

Let `H=S_17^16`.  The horizontal-strip-chain carrier is

\[
 U_\theta=(S^\theta)^H.
\]

Instead of expanding either the `f^theta=46,937,442,816` Young carrier or a dense matrix on
`U_theta`, use the tabloid realization

\[
 S^{(267,4,1)}
 =\bigcap_{i,v}\ker\psi_{i,v}
 \subset M^{(267,4,1)}
\tag{2.1}
\]

from the characteristic-zero James kernel-intersection theorem.  A tabloid is determined by a
four-set `B` in row two and a disjoint singleton `C` in row three.  An `H`-orbit is therefore
specified by

\[
 (b_0,\ldots,b_{15};j),\qquad
 \sum_i b_i=4,
\tag{2.2}
\]

where `b_i` is the number of elements of `B` in block `i` and `j` is the block containing `C`.
The labelled `H`-orbit basis has

\[
 16{19\choose4}=62016
\tag{2.3}
\]

elements, but fixing block zero and quotienting the other fifteen block labels leaves only
`38` unnormalised orbit sums.  Quotienting all sixteen block labels leaves `12`.

The exact James maps used in (2.1) are

\[
 \psi_{1,v}:B\longmapsto\sum_{B'\subseteq B,\ |B'|=v}B',
 \quad 0\le v<4,
 \qquad
 \psi_{2,0}:(B,C)\longmapsto B\cup C.
\tag{2.4}
\]

Their stacked ranks on the two quotients are respectively `33` in dimension `38` and `11` in
dimension `12`.  Hence

\[
 \dim (S^\theta)^{H\rtimes S_{15}}=5,
 \qquad
 \dim (S^\theta)^{H\rtimes S_{16}}=1.
\tag{2.5}
\]

Only the trivial and standard `S_16` irreducibles can contain an `S_15`-fixed vector.  Therefore

\[
 \dim\operatorname{Hom}_{S_{17}\wr S_{16}}(V_{16},S^\theta)=5-1=4.
\tag{2.6}
\]

This extracts the required `C_4=4` without choosing a favourable copy.

As a separate exact size gate, the horizontal-strip recurrence regenerates

\[
 [s_\theta]h_{17}^{16}=34272
\tag{2.7}
\]

and, after replacing one block size `17` by `16`, gives

\[
 [s_{(266,4,1)}]h_{16}h_{17}^{15}=34272,
 \quad
 [s_{(267,3,1)}]h_{16}h_{17}^{15}=7140,
 \quad
 [s_{(267,4)}]h_{16}h_{17}^{15}=3060.
\tag{2.8}
\]

Thus the earlier unarchived planning counts are independently regenerated here as exact logged
outputs.

## 3. Exact adjacent 17-point block swaps

Before the `S_15` orbit compression, the adjacent swap of blocks `i` and `i+1` is the exact
permutation

\[
 s_i:(b_0,\ldots,b_i,b_{i+1},\ldots,b_{15};j)
 \longmapsto
 (b_0,\ldots,b_{i+1},b_i,\ldots,b_{15};s_i(j)).
\tag{3.1}
\]

The unnormalised orbit Gram weight is

\[
 17{16\choose b_j}\prod_{i\ne j}{17\choose b_i},
\tag{3.2}
\]

so (3.1) preserves it exactly.  The tool checks (3.2) on all `62016` labelled orbit keys and
checks at the index-permutation level

\[
 s_i^2=1,\qquad
 s_is_{i+1}s_i=s_{i+1}s_is_{i+1},\qquad
 s_is_j=s_js_i\ (|i-j|>1).
\tag{3.3}
\]

Because every James map in (2.4) is `S_272`-equivariant, these swaps preserve the kernel (2.1).
This is the physical `S_16` wreath action on `U_theta`, represented without a dense
horizontal-strip-chain matrix.

## 4. Marked point and the three exact branching projectors

Fix a point `x` in block zero.  After reducing the internal group of that block from `S_17` to
`S_16`, the marked tabloid orbit quotient has dimension `71`.  In it the exact relative
Jucys--Murphy operator is

\[
 J_x=\sum_{y\ne x}(x\ y).
\tag{4.1}
\]

The orbit action of (4.1) is computed by moving `x` between the top, middle, and bottom rows and
updating the occupancy of the block containing `y`.  Its matrix is integer in unnormalised orbit
coordinates and is exactly self-adjoint for the diagonal orbit Gram.

On `S^(267,4,1)`, the three removable-corner contents are

\[
 c_T=266,\qquad c_M=2,\qquad c_B=-2.
\tag{4.2}
\]

Therefore the Young-branch projectors are the following exact degree-two polynomials:

\[
 \begin{aligned}
 P_T&={(J_x-2I)(J_x+2I)\over70752},\\
 P_M&={(J_x-266I)(J_x+2I)\over-1056},\\
 P_B&={(J_x-266I)(J_x-2I)\over1072}.
 \end{aligned}
\tag{4.3}
\]

On all four extracted source columns the tool verifies exactly

\[
 P_T+P_M+P_B=I,\qquad P_\kappa^2=P_\kappa,
 \qquad P_\kappa P_{\kappa'}=0\quad(\kappa\ne\kappa').
\tag{4.4}
\]

No floating eigenvalue threshold enters (4.2)--(4.4).

## 5. Basis, normalization, and the six matrices

Let `v_1,...,v_4` be the deterministic rational Gram-orthogonal basis returned by exact nullspace
and Gram--Schmidt operations.  Its squared norms are

\[
 \begin{aligned}
 n_1&={233245657600\over39},\\
 n_2&={37699701339916525\over14836},\\
 n_3&={252885664381001925\over1388384},\\
 n_4&={130423121542000\over93351}.
 \end{aligned}
\tag{5.1}
\]

Put `G=diag(n_1,n_2,n_3,n_4)` and

\[
 H^{\mathbf1}_\kappa[i,j]=\langle v_i,P_\kappa v_j\rangle.
\tag{5.2}
\]

The orthonormal occurrence matrix in the basis `v_i/sqrt(n_i)` is encoded without any numerical
radical by

\[
 \mathsf O_{\kappa,\mathbf1}[i,j]
 ={H^{\mathbf1}_\kappa[i,j]\over\sqrt{n_in_j}}.
\tag{5.3}
\]

The exact `H` matrices, every normalized expression in (5.3), and every principal minor are in
`run.json`.  One especially informative branch is

\[
 H^{\mathbf1}_M=
 \begin{pmatrix}
 0&0&0&0\\
 0&0&0&0\\
 0&0&\frac{199986205635125}{16896}&-\frac{28081728357011875}{394314624}\\
 0&0&-\frac{28081728357011875}{394314624}&
 \frac{1668696602695264165625}{9202416116256}
 \end{pmatrix},
\tag{5.4}
\]

which has rank exactly `2`.  The `T` and `B` trivial-child matrices have rank `4`.

To obtain the `V_15` child, use

\[
 V_{16}\downarrow S_{15}=\mathbf1\oplus V_{15},
 \qquad \dim V_{16}=15,\quad \dim V_{15}=14.
\tag{5.5}
\]

For each fixed point, wreath conjugacy and
`sum_x P_(kappa,x)=(272 f^kappa/f^theta)I` give

\[
 \boxed{
 H^{\mathbf1}_\kappa+14H^{V_{15}}_\kappa
 =15{f^\kappa\over f^\theta}G.}
\tag{5.6}
\]

The exact dimensions used in (5.6) are

\[
 \begin{array}{c|r}
 \theta=(267,4,1)&46937442816\\
 \kappa_T=(266,4,1)&46071366111\\
 \kappa_M=(267,3,1)&649566675\\
 \kappa_B=(267,4)&216510030.
 \end{array}
\tag{5.7}
\]

All three `V_15` matrices have rank `4`.  Exact principal-minor gates show that all six forms are
positive semidefinite.  The two independent resolutions are

\[
 \sum_\kappa H^{\mathbf1}_\kappa=G,
 \qquad
 \sum_\kappa H^{V_{15}}_\kappa=G.
\tag{5.8}
\]

Equations (5.1)--(5.8), together with the exact JSON matrices, completely specify all six
`O_(kappa,eta)` with no phase or floating-point ambiguity.

## 6. Exact same-side occurrence algebra

For commutators, radicals are unnecessary.  In the common rational basis use the operator
matrices

\[
 A_{\kappa,\eta}=G^{-1}H^\eta_\kappa.
\tag{6.1}
\]

Conjugating (6.1) by `G^(1/2)` gives the orthonormal matrices, so ranks and polynomial identities
are unchanged.  The exact pairwise ranks are

| left/right | `T,1` | `T,V15` | `M,1` | `M,V15` | `B,1` | `B,V15` |
|---|---:|---:|---:|---:|---:|---:|
| `T,1` | - | 0 | 2 | 2 | 2 | 2 |
| `T,V15` |  | - | 2 | 2 | 2 | 2 |
| `M,1` |  |  | - | 0 | 2 | 2 |
| `M,V15` |  |  |  | - | 2 | 2 |
| `B,1` |  |  |  |  | - | 0 |
| `B,V15` |  |  |  |  |  | - |

The same-`kappa` zeros also follow from (5.6), but the tool checks the matrices directly.  Every
rank-2 entry is obtained by exact rational RREF; the complete exact commutator matrices are stored
in the JSON.

Solving

\[
 XA_{\kappa,\eta}=A_{\kappa,\eta}X
\tag{6.2}
\]

for all six operators gives an exact linear system of rank `14`, hence common commutant dimension
`2`.  Exact product closure of the unital algebra gives dimension `10`.  A `G`-self-adjoint
rank-one central projector is

\[
 P_{1}=
 \begin{pmatrix}
 \frac{315317496}{607181845}&
 \frac{371088450396573}{36032599409680}&0&0\\
 \frac{3968}{163705}&
 \frac{291864349}{607181845}&0&0\\
 0&0&0&0\\
 0&0&0&0
 \end{pmatrix}.
\tag{6.3}
\]

The checker verifies `P_1^2=P_1`, `rank(P_1)=1`, and `P_1^T G=G P_1`.  Its image is the line
stated in Section 1.  The complementary central block has rank `3`, and

\[
 1^2+3^2=10.
\tag{6.4}
\]

Since the generated rational algebra reaches the full maximum dimension on these two central
blocks, it is exactly

\[
 M_1(\mathbb Q)\oplus M_3(\mathbb Q).
\tag{6.5}
\]

Thus the occurrence tables do contain genuine noncommutation, but one common scalar line survives.
This finite structural fact is not an assembled physical query-pencil verdict.

## 7. Exact gates and failure-mode audit

The run passes all of the following with integer or rational equality:

1. horizontal-strip-chain counts (2.7)--(2.8);
2. all adjacent block-swap Coxeter identities and all `62016` orbit-weight checks;
3. every James-kernel residual and the `5-1=4` standard multiplicity extraction;
4. marked/unmarked Gram embedding;
5. self-adjointness of `J_x`;
6. branch-projector resolution, idempotence, and mutual orthogonality on all four source columns;
7. hook-dimension branching resolution;
8. exact symmetry, rank, and principal-minor positivity of all six occurrence forms;
9. both eta resolutions (5.8) and all three trace identities (5.6);
10. all fifteen pairwise commutator ranks;
11. common-commutant dimension, generated-algebra dimension, and the rank-one `G`-orthogonal
    central projector.

The computation uses Python integers and SymPy rationals.  Floating point is not used in any
mathematical gate.  The stored SE scripts and arrays identified in the planning artifact are not
imported and do not supply any coefficient here.

The reduction is value-and-formula coupled: the program implements (2.4), (3.1), (4.1), (4.3),
(5.2), (5.6), and (6.1) directly.  It does not merely hardcode the six output matrices.

## 8. Provenance

Command:

```powershell
python ksum/tools/ksum_l3_wreath_occurrence_reducer.py `
  --json ksum/artifacts/logs_ksum_L3_wreath_occurrence_reducer_20260722/run.json `
  --log ksum/artifacts/logs_ksum_L3_wreath_occurrence_reducer_20260722/run.log
```

Files:

* tool: `ksum/tools/ksum_l3_wreath_occurrence_reducer.py`, SHA-256
  `06B842F0475B85691A76128864BE22D6996BBECDC7A9981FE6111929CA28F371`;
* complete exact JSON: `ksum/artifacts/logs_ksum_L3_wreath_occurrence_reducer_20260722/run.json`,
  SHA-256 `BAA0501B082D8ACD20A280A363198F68A13B8CD3989F78E7E9BD9B225A52FF16`;
* human-readable raw log: `ksum/artifacts/logs_ksum_L3_wreath_occurrence_reducer_20260722/run.log`,
  SHA-256 `323AEBA68F87E24FB40EA51F78DD1304264B2B5E1BA86B0F503666DB061D1C76`.

## 9. Stopping point

This calculation discharges the first-target **occurrence table** requested by Section 11.3 of the
one-point Gram-stack specification and adds the exact same-side occurrence-algebra classification.
It does not discharge Sections 11.4--11.5 of that specification.  In particular, the next physical
calculation still needs the complete all-parent alphabet matrices and every required Pieri scalar
before forming `Q_L(z)` or `Q_R(w)`.  Until fresh Rule-7 review and that remaining assembly land,
the controlling node must stay OPEN and no successor law is activated by this artifact alone.
