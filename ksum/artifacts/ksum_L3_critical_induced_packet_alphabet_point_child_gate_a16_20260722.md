# L3 induced packet: exact first-target alphabet point-child gate

Date: 2026-07-22  
Controlling node (not edited by this calculation):
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

Scope: only `a=16`, `q=64`, answer `t=0`, and the common point child
`tau_*=(61,2)`.  This is a proposer-side finite exact calculation.  It is not a Rule-7 review,
does not prove a statement for all `s>=4`, and makes no occurrence, position-Pieri, query,
numerator, attenuation, or exponent claim.

## 1. Result

The complete one-box parent closure of `tau_*` is

\[
 \{(62,2),(61,3),(61,2,1)\}.
\tag{1.1}
\]

Their complete NO packet multiplicities are, in that order,

\[
 \boxed{1,\ 3,\ 6}.
\tag{1.2}
\]

The corresponding all-parent column space therefore has dimension ten.  For one fixed marked raw
letter, its exact pointed Mackey resolution is

\[
 \underbrace{1}_{A\ {m rare}}+
 \underbrace{1}_{B\ {m rare}}+
 \underbrace{3}_{L,\eta=\mathbf1}+
 \underbrace{1}_{L,\eta=V_{15}}+
 \underbrace{3}_{R,\eta=\mathbf1}+
 \underbrace{1}_{R,\eta=V_{15}}=10.
\tag{1.3}
\]

This dimension identity is checked independently of the matrix construction below.  By itself it
does **not** determine any cross-Gram or commutator.

The calculation then constructs the actual ten-dimensional last Jucys--Murphy matrix in a stated
marked Mackey gauge.  Its exact characteristic polynomial is

\[
 \boxed{(x-61)(x-1)^3(x+2)^6}.
\tag{1.4}
\]

The three eigenspaces are exactly the ordered parent spaces in (1.1).  Exact spectral projection
and a deterministic positive-leading Gram--Schmidt rule give a common orthonormal all-parent
gauge.  In that gauge the full `10 by 10` tables

\[
 \mathsf C^{0,L}_{\tau_*,\mathbf1},\quad
 \mathsf C^{0,L}_{\tau_*,V_{15}},\quad
 \mathsf C^{0,R}_{\tau_*,\mathbf1},\quad
 \mathsf C^{0,R}_{\tau_*,V_{15}}
\tag{1.5}
\]

are evaluated exactly and archived in the raw JSON.  They are orthogonal projectors of ranks
`3,1,3,1`, respectively.  The two rare rank-one tables are also archived, and all six tables sum
exactly to `I_10`.  Thus no parent and no multiplicity line has been selected away.

## 2. Reproducible Frobenius-character derivation

For the NO alphabet packet,

\[
 \operatorname{ch}M_0
 =h_{16}^2s_{(15,1)}^2
 =h_{16}^2(h_{15}h_1-h_{16})^2.
\tag{2.1}
\]

The checker evaluates every coefficient of a product of complete functions by the exact Pieri
recurrence

\[
 [s_\lambda]\prod_{i=1}^k h_{r_i}
 =\sum_{\mu:\lambda/\mu\ {m horizontal}\ r_k\text{-strip}}
 [s_\mu]\prod_{i=1}^{k-1}h_{r_i}.
\tag{2.2}
\]

Writing the three terms from (2.1) as `A-2B+C`, the exact rows are

| parent `nu` | `A=[s_nu]h16^2 h15^2 h1^2` | `B=[s_nu]h16^3 h15 h1` | `C=[s_nu]h16^4` | `m_(0,nu)` |
|---|---:|---:|---:|---:|
| `(62,2)` | 13 | 9 | 6 | 1 |
| `(61,3)` | 25 | 16 | 10 | 3 |
| `(61,2,1)` | 32 | 17 | 8 | 6 |

There are no other one-box parents: the only addable boxes of `(61,2)` are at `(1,62)`, `(2,3)`,
and `(3,1)`.  Hence (1.1)--(1.2) are the complete active closure, not a chosen low-tail subset.

For a left-heavy mark, Frobenius reciprocity gives the pointed characteristics

\[
 \begin{aligned}
 F_{L,\mathbf1}&=h_{16}^2h_{15}s_{(15,1)},\\
 F_{L,V_{15}}&=h_{16}^2s_{(14,1)}s_{(15,1)}.
 \end{aligned}
\tag{2.3}
\]

At `tau_*`, the first multiplicity is `9-6=3`.  Using
`s_(14,1)=h14 h1-h15`, the second is

\[
 13-9-9+6=1.
\tag{2.4}
\]

The right-heavy values are the same by swapping the two heavy cells.  Marking either trivial cell
has characteristic `h16 h15 s_(15,1)^2` and multiplicity `13-2*9+6=1`.  These calculations give
the independent Mackey count (1.3).

## 3. Exact sparse realization and canonical gauge

The point-child carrier is not built by enumerating 1,890 Young tableaux.  It is realized as the
harmonic edge representation

\[
 S^{(61,2)}
 \cong\left\{x\in\mathbb R^{\binom{[63]}2}:
       \sum_{j\ne i}x_{\{i,j\}}=0\quad(1\le i\le63)\right\}.
\tag{3.1}
\]

Its dimension is `binom(63,2)-63=1890`, and alphabet permutations merely relabel edges.  The six
pointed types in (1.3) have explicit isometric embeddings into (3.1):

* the rare and `V15 tensor V16` sectors use the cross-edge tensor `x_(ij)=u_i v_j` between the
  two heavy cells;
* an `eta=1` heavy sector uses the four copies of the opposite heavy standard representation
  carried by its internal edges and by its cross edges to the other three cells, subject to the
  one row-sum constraint.

For the latter three-dimensional space, the checker fixes the following positive-leading,
weighted-orthonormal coefficient vectors.  Coordinates mean `(internal, cross A, cross B,
cross marked-heavy)` and the edge-norm weights are `(14,16,16,15)`:

\[
 { (0,1,-1,0)\over\sqrt{32}},\qquad
 { (16,-7,-7,0)\over\sqrt{5152}},\qquad
 { (15,15,15,-46)\over\sqrt{42090}}.
\tag{3.2}
\]

The marked Mackey basis order is

\[
 A_{\rm rare},B_{\rm rare},L_{\mathbf1,0},L_{\mathbf1,1},L_{\mathbf1,2},
 L_{V_{15}},R_{\mathbf1,0},R_{\mathbf1,1},R_{\mathbf1,2},R_{V_{15}}.
\tag{3.3}
\]

For each destination cell `d` and each `i<64`, the program factors exactly

\[
 (i,64)r_d=l\,r_c h,
 \qquad l\in S_{63},\quad h\in S_{16}^4,
\tag{3.4}
\]

and contracts the explicit sector embeddings.  This constructs
`X_64=sum_(i<64)(i,64)` directly on the ten-dimensional multiplicity space.  Two different unit
vectors in every local irreducible give the identical exact matrix, checking that the contraction
is the required Schur scalar rather than a favorable matrix coefficient.

The contents of the added boxes are

\[
 c_{(62,2)}=61,\qquad c_{(61,3)}=1,\qquad c_{(61,2,1)}=-2,
\tag{3.5}
\]

which agrees with (1.4).  Let `P_61,P_1,P_-2` be the exact Lagrange spectral projectors of this
matrix.  Within each eigenspace, the checker projects the ordered coordinate vectors from (3.3),
discards exact dependencies, performs exact Gram--Schmidt, and chooses the positive first nonzero
entry.  The resulting orthogonal matrix `E` has columns ordered

\[
 (62,2)\#0\mid (61,3)\#0,1,2\mid(61,2,1)\#0,1,2,3,4,5.
\tag{3.6}
\]

This is the canonical gauge used by the archived tables.  A different orthonormal basis inside a
parent block conjugates all tables by the same block-diagonal orthogonal matrix and changes no
rank, projector, normalization, or physical conclusion.

## 4. Exact point-child tables

In the marked gauge (3.3), let

\[
 \begin{aligned}
 D_{L,\mathbf1}&=\operatorname{diag}(0,0,1,1,1,0,0,0,0,0),\\
 D_{L,V_{15}}&=\operatorname{diag}(0,0,0,0,0,1,0,0,0,0),\\
 D_{R,\mathbf1}&=\operatorname{diag}(0,0,0,0,0,0,1,1,1,0),\\
 D_{R,V_{15}}&=\operatorname{diag}(0,0,0,0,0,0,0,0,0,1).
 \end{aligned}
\tag{4.1}
\]

Because the sector embeddings are isometries, Frobenius reciprocity identifies the normalized
Hilbert--Schmidt Gram in the planning artifact's equation (6.7) with

\[
 \boxed{\mathsf C_{s,\eta}=E^T D_{s,\eta}E.}
\tag{4.2}
\]

Thus (4.2) includes exactly the factor `1/(d_eta*15)` from the normalized trace; no dimension
factor is omitted.  The raw JSON prints every entry of all four `10 by 10` matrices as an exact
rational/radical expression.  For example, using the parent column order (3.6),

\[
 \begin{aligned}
 [\mathsf C_{L,\mathbf1}]_{0,1}
   &={\sqrt{14091}\over22275},\\
 [\mathsf C_{L,V_{15}}]_{0,1}
   &=-{16\sqrt{14091}\over22275},\\
 [\mathsf C_{R,\mathbf1}]_{0,3}
   &={\sqrt{305}\over1350},\\
 [\mathsf C_{R,V_{15}}]_{0,3}
   &=-{8\sqrt{305}\over675}.
 \end{aligned}
\tag{4.3}
\]

These entries join different old parents and therefore explicitly verify that the physical point
child is codiagonal in the all-parent source.  Replacing it by old-parent superselection would
delete genuine nonzero entries.

The exact checks are

\[
 \mathsf C_{s,\eta}^2=\mathsf C_{s,\eta},\qquad
 \operatorname{Tr}(\mathsf C_{L,\mathbf1},
 \mathsf C_{L,V_{15}},\mathsf C_{R,\mathbf1},
 \mathsf C_{R,V_{15}})=(3,1,3,1),
\tag{4.4}
\]

and, after including the two rare tables,

\[
 \boxed{
 C_A+C_B+C_{L,\mathbf1}+C_{L,V_{15}}
       +C_{R,\mathbf1}+C_{R,V_{15}}=I_{10}.}
\tag{4.5}
\]

Equation (4.5) is the requested all-parent normalization.  It is stronger than the dimension sum
(1.3), because it is checked entrywise on the actual exact matrices.

The checker also evaluates the algebra of all six tables in this common parent gauge.  Every one
of the fifteen unordered pairs has exact product rank zero and hence exact commutator rank zero:

\[
 \operatorname{rank}(C_\chi C_{\chi'})
 =\operatorname{rank}[C_\chi,C_{\chi'}]=0
 \qquad(\chi\ne\chi').
\tag{4.6}
\]

This includes separately:

* the left/right pairs `L1--R1`, `L1--RV15`, `LV15--R1`, and `LV15--RV15`;
* the same-side status pairs `L1--LV15` and `R1--RV15`;
* `A--B` and every rare/heavy pair.

The exact simultaneous block ranks, in the table order
`A,B,L1,LV15,R1,RV15`, are `(1,1,3,1,3,1)`.  Therefore the generated unital
star algebra and its commutant are

\[
 \mathcal A\cong\mathbb C^6,\qquad \dim\mathcal A=6,
\tag{4.7}
\]

\[
 \mathcal A'
 \cong M_1\oplus M_1\oplus M_3\oplus M_1\oplus M_3\oplus M_1,
 \qquad \boxed{\dim\mathcal A'=22}.
\tag{4.8}
\]

Equations (4.6)--(4.8) are derived from the explicitly constructed square orthogonal matrix `E`,
the six disjoint marked projectors `D_chi`, and the exact identity (4.5).  The reviewed same-raw-
mark cross-side commutation theorem is therefore a consistency check on this finite alphabet
calculation, not an assumption used to make the matrices commute.  The exact cross-parent entries
in (4.3) simultaneously show why this commuting resolution is not an old-parent diagonal pinch.

## 5. Scope boundary

The four tables use one common fixed marked raw letter and the common `S_63` point-child carrier.
In this same-mark decomposition the six Mackey projectors are mutually orthogonal, with the exact
algebra in (4.6)--(4.8).  This does not
evaluate point-child refinements for two different raw marks, whose point-stabilizer projectors
are conjugate rather than common.  It therefore gives no arbitrary-`z,w` refined commutator
verdict.

This gate also does not evaluate the occurrence Grams `O_(kappa,eta)` or the position Pieri
scalars.  Consequently it does not assemble a physical one-side occurrence pencil.  The only
claim is that the first-target **alphabet** factor and its complete parent codiagonal are now exact.

Finally, all displayed values are at `a=16,q=64`.  They are finite evidence only and cannot prove
uniform noncommutation, simultaneous diagonalization, query attenuation, or a critical exponent.

## 6. Evidence

* Exact checker: `ksum/tools/ksum_l3_alphabet_point_child_gate.py`.
* Raw exact JSON: `ksum/artifacts/logs_ksum_L3_alphabet_point_child_gate_20260722/run.json`.
* The JSON contains the complete JM matrix, its three spectral projectors, the canonical parent
  basis, all six exact point-child cross-Gram tables, the two independent-vector identity check,
  and every Pieri integer used above.
