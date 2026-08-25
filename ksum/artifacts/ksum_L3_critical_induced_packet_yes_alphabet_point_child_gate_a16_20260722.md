# L3 induced packet: exact YES first-target alphabet point-child gate

Date: 2026-07-22  
Controlling node (not edited by this calculation):
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

Tier: proposer-side finite exact calculation, pending fresh Rule-7 review.  Scope is only
`a=16`, `q=64`, answer `t=1`, one fixed raw mark, and `tau_*=(61,2)`.  No canonical/shared DAG
file was edited.  This artifact makes no uniform, occurrence, position-Pieri, transfer, query,
attenuation, numerator, feasibility, or exponent claim.

## 1. Complete YES result

Use the full physical YES palette

\[
 |U|=|C|=1,\qquad |L|=|R|=15,\qquad |H_L|=|H_R|=16.
\tag{1.1}
\]

Here `U` is unused by the input and hence query-inactive, but it remains a physical alphabet cell
and is retained in the marked restriction.  The complete one-box parent closure of
`tau_*=(61,2)` is

\[
 \{(62,2),(61,3),(61,2,1)\},
\tag{1.2}
\]

with full `M_1` multiplicities

\[
 \boxed{1,\ 5,\ 10}.
\tag{1.3}
\]

The complete pointed Mackey resolution, in physical status order, is

\[
 \underbrace1_U+
 \underbrace1_C+
 \underbrace1_L+
 \underbrace1_R+
 \underbrace5_{H_L,\eta=\mathbf1}+
 \underbrace1_{H_L,\eta=V_{15}}+
 \underbrace5_{H_R,\eta=\mathbf1}+
 \underbrace1_{H_R,\eta=V_{15}}
 =16.
\tag{1.4}
\]

The actual last Jucys--Murphy matrix is constructed exactly on this full sixteen-dimensional
space.  Its characteristic polynomial is

\[
 \boxed{(x-61)(x-1)^5(x+2)^{10}},
\tag{1.5}
\]

so its three eigenspaces have exactly the parent dimensions in (1.3).

## 2. Exhaustive Frobenius-character calculation

The complete induced YES character is

\[
 \operatorname{ch}M_1
 =h_1^2h_{15}^2s_{(15,1)}^2
 =h_1^2h_{15}^2(h_{15}h_1-h_{16})^2.
\tag{2.1}
\]

The exact checker evaluates complete-function coefficients by the horizontal-strip Pieri
recurrence, with no character values supplied as constants.  If the three terms in (2.1) are
written as `A-2B+C`, the complete parent table is

| parent `nu` | `A=[s_nu]h15^4 h1^4` | `B=[s_nu]h15^3 h16 h1^3` | `C=[s_nu]h15^2 h16^2 h1^2` | `m_(1,nu)` |
|---|---:|---:|---:|---:|
| `(62,2)` | 24 | 18 | 13 | 1 |
| `(61,3)` | 56 | 38 | 25 | 5 |
| `(61,2,1)` | 88 | 55 | 32 | 10 |

There are no other parents because `(61,2)` has exactly the three addable cells `(1,62)`,
`(2,3)`, and `(3,1)`.

The marked-sector characters and exact coefficients are

| marked status | Frobenius characteristic at size 63 | exact Pieri combination | rank |
|---|---|---:|---:|
| unused `U` | `h1 h15^2 s_(15,1)^2` | `18-2*13+9` | 1 |
| common `C` | `h1 h15^2 s_(15,1)^2` | `18-2*13+9` | 1 |
| residual `L` | `h1^2 h14 h15 s_(15,1)^2` | `24-2*18+13` | 1 |
| residual `R` | same | `24-2*18+13` | 1 |
| `H_L`, `eta=1` | `h1^2 h15^3 s_(15,1)` | `18-13` | 5 |
| `H_L`, `eta=V15` | `h1^2 h15^2 s_(14,1)s_(15,1)` | `24-18-18+13` | 1 |
| `H_R`, `eta=1` | left/right swap | `18-13` | 5 |
| `H_R`, `eta=V15` | left/right swap | `24-18-18+13` | 1 |

This independently proves the dimension resolution (1.4).  It does not determine the matrices;
those are constructed separately below.

## 3. Full unmatched-packet accounting

The earlier NO gate has parent multiplicities `(1,3,6)`, totaling ten.  Either physical
orientation isometry embeds those ten columns into `M_1`, but the complete YES packet has the
sixteen columns (1.3).  Parent by parent, the complement of one orientation image has dimensions

\[
 (1,5,10)-(1,3,6)=\boxed{(0,2,4)},
\tag{3.1}
\]

totaling six.  The present JM matrix, parent basis, and all marked tables use all sixteen columns.
They are not a ten-column orientation pullback and do not zero-pad or discard the unmatched
complement.  The choice of which six-dimensional complement is orthogonal is orientation
dependent; only the full-space dimension statement (3.1) is used here.

## 4. Sparse exact JM construction

As in the NO finite gate, the point child is realized without a dense Specht construction:

\[
 S^{(61,2)}
 \cong\left\{x\in\mathbb R^{\binom{[63]}2}:
       \sum_{j\ne i}x_{\{i,j\}}=0\quad(1\le i\le63)\right\}.
\tag{4.1}
\]

Permutation action is exact edge relabeling.  The passive `U,C,L,R` sectors and the heavy
`V15 tensor V16` sectors use the cross-edge tensor between `H_L` and `H_R`.  For an `eta=1`
heavy sector, the opposite heavy standard occurs on its internal edges and on its cross edges to
the other five cells.  The coefficient metric and row-sum constraint have weights

\[
 (14,1,1,15,15,15).
\tag{4.2}
\]

The tool constructs a deterministic positive-leading weighted-orthonormal basis of the
five-dimensional constraint kernel by exact Gram--Schmidt.

### Unequal-cell Mackey normalization

This is the load-bearing difference from the four equal NO cells.  If the marked cell is `c` of
size `m_c`, then

\[
 |K_c|={|H_1|\over m_c},\qquad
 |S_{63}:K_c|\ \text{is proportional to }m_c.
\tag{4.3}
\]

For a pointed irreducible of dimension `d_c`, the normalized Fourier embedding therefore has
scale `alpha_c proportional to (m_c d_c)^(-1/2)`.  In the block from source `c` to destination
`d`, the exact scale is

\[
 \boxed{{\alpha_c\over\alpha_d}
 =\sqrt{{m_d d_d\over m_c d_c}}.}
\tag{4.4}
\]

Using the equal-cell factor from the NO calculation would make the YES JM matrix nonsymmetric;
the missing ratios are exactly the cell-size ratios.  Equation (4.4) restores exact symmetry
entry by entry and is used in the archived calculation.

For each destination status `d` and each `i<64`, the program factors

\[
 (i,64)r_d=l r_c h,
 \qquad l\in S_{63},\quad h\in H_1,
\tag{4.5}
\]

and contracts the explicit sector embeddings.  Two different unit vectors in every local
irreducible produce the identical exact sixteen-dimensional matrix.  Its exact spectrum is
(1.5), with added-box contents `61,1,-2`.

## 5. Deterministic all-parent columns and exact status tables

Let the marked Mackey basis be ordered

\[
 U,C,L,R,
 H_{L,\mathbf1,0},\ldots,H_{L,\mathbf1,4},H_{L,V_{15}},
 H_{R,\mathbf1,0},\ldots,H_{R,\mathbf1,4},H_{R,V_{15}}.
\tag{5.1}
\]

Exact Lagrange projectors at `61,1,-2`, followed by projected-coordinate Gram--Schmidt with
positive first nonzero entry, give a square orthogonal matrix `E`.  Its parent columns are ordered

\[
 (62,2)\#0\mid(61,3)\#0,\ldots,4
 \mid(61,2,1)\#0,\ldots,9.
\tag{5.2}
\]

For each physical marked status `chi`, let `D_chi` be its coordinate projector in (5.1).  The
actual normalized point-child table in the common all-parent gauge is

\[
 \boxed{C_\chi=E^T D_\chi E.}
\tag{5.3}
\]

The normalized Hilbert--Schmidt factors `1/(d_eta*15)` are already included by the isometric
sector construction.  The raw JSON contains every entry of all eight `16 by 16` tables, the full
JM matrix, all three parent projectors, and `E`.

Every status table has a nonzero block between every distinct pair of parents.  The following
entries give one exact witness in each such block; indices use (5.2).

| status table | `[0,1]`: `(62,2)--(61,3)` | `[0,6]`: `(62,2)--(61,2,1)` | `[1,6]`: `(61,3)--(61,2,1)` |
|---|---|---|---|
| `U` | `sqrt(75579)/3780` | `sqrt(9455)/945` | `sqrt(192045)/945` |
| `C` | `-sqrt(75579)/223020` | `-sqrt(9455)/58590` | `sqrt(192045)/3456810` |
| `L` | `-sqrt(75579)/14868` | `-sqrt(9455)/3906` | `sqrt(192045)/230454` |
| `R` | `-sqrt(75579)/14868` | `-sqrt(9455)/3906` | `sqrt(192045)/230454` |
| `H_L,eta=1` | `sqrt(75579)/238950` | `-17 sqrt(9455)/1757700` | `-7969 sqrt(192045)/14814900` |
| `H_L,eta=V15` | `-8 sqrt(75579)/119475` | `-16 sqrt(9455)/62775` | `16 sqrt(192045)/3703725` |
| `H_R,eta=1` | `sqrt(75579)/238950` | `-17 sqrt(9455)/1757700` | `-7969 sqrt(192045)/14814900` |
| `H_R,eta=V15` | `-8 sqrt(75579)/119475` | `-16 sqrt(9455)/62775` | `16 sqrt(192045)/3703725` |

Thus every physical status has genuine old-parent codiagonal support.  None of the tables is an
old-parent superselection or a favorable parent truncation.

## 6. Exact resolution and same-mark algebra

The exact table ranks, in physical order
`U,C,L,R,HL1,HLV15,HR1,HRV15`, are

\[
 (1,1,1,1,5,1,5,1),
\tag{6.1}
\]

and entrywise exact arithmetic gives

\[
 \boxed{C_U+C_C+C_L+C_R+C_{HL,1}+C_{HL,V15}
             +C_{HR,1}+C_{HR,V15}=I_{16}.}
\tag{6.2}
\]

All eight tables are idempotent.  For all 28 unordered distinct pairs,

\[
 \operatorname{rank}(C_\chi C_{\chi'})
 =\operatorname{rank}[C_\chi,C_{\chi'}]=0.
\tag{6.3}
\]

This includes unused/common/private pairs, same-heavy-side `eta=1` versus `V15`, all left/right
heavy pairs, and every passive/heavy pair.  The generated star algebra and its commutant are

\[
 \mathcal A\cong\mathbb C^8,
 \qquad\boxed{\dim\mathcal A=8},
\tag{6.4}
\]

\[
 \mathcal A'
 \cong M_1^{\oplus4}\oplus M_5\oplus M_1\oplus M_5\oplus M_1,
 \qquad\boxed{\dim\mathcal A'=56}.
\tag{6.5}
\]

These conclusions are derived from the explicitly constructed orthogonal `E`, the eight physical
coordinate projectors, and (6.2).  The reviewed same-fixed-mark cross-side theorem is a
consistency check, not an assumption used to force commutation.  The nonzero codiagonal entries
in Section 5 show simultaneously that this commuting algebra is not produced by pinching old
parents.

## 7. Scope boundary

This is a same-fixed-raw-mark alphabet result.  Point-child projectors for distinct raw marks
belong to conjugate point stabilizers, so (6.3) gives no distinct-mark refined commutator.  It also
does not evaluate the occurrence tables `O_(kappa,eta)`, position Pieri scalars, a complete
one-side occurrence pencil, an orientation-pulled cross-answer map, or the native rectangular
transfer.  The query-inactive `U` status is included for representation completeness but is not
silently promoted to a queried branch.

All numbers are for the single finite first target `a=16,q=64`.  They do not prove a formula or
quantifier for the target family and cannot support an asymptotic feasibility or exponent claim.

## 8. Evidence

* Exact YES checker: `ksum/tools/ksum_l3_yes_alphabet_point_child_gate.py`, SHA-256
  `3DE2DD5E77CBAB60D1C5CA30CDB12EEC1B96C481BC4408AC6257630AC3E2903C`.
* Raw exact JSON: `ksum/artifacts/logs_ksum_L3_yes_alphabet_point_child_gate_20260722/run.json`,
  SHA-256 `05C07213ECB406D0F61118BCF214D551F59170074CC5E2399EB1A5F6AEAAB333`.
* The new checker reuses only generic exact Pieri/permutation/edge helpers from the preserved NO
  checker `ksum/tools/ksum_l3_alphabet_point_child_gate.py`, SHA-256
  `A247A6DB9EEDE94EBB83626ED3F41EB3047A99B2487901597A0D7EF5BBDA010F`.

