# Isolation seal: YES alphabet point-child gate at `a=16`

Date: 2026-07-22  
Role: pre-proposer expectations for a fresh independent Rule-7 checker  
Target node (not opened before this seal):
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

## Isolation boundary

Before writing this file I read the two repository protocols in full, then only the already
reviewed NO (`t=0`) alphabet gate and the reviewed induced-packet definitions/reviews.  I did not
open or grep the YES proposer artifact, YES proposer tool, YES proposer JSON/output, the existing
YES blind/contaminated baseline, or the target canonical node.  No candidate YES numerical result
was supplied by another agent.

This seal records independently derived expectations.  It is not a verdict and it is not evidence
for a completion status.

## Frozen exact expectations

Put `q=64`, `a=16`, `tau=(61,2)`, and

\[
 \operatorname{ch}M_1=h_1^2h_{15}^2s_{(15,1)}^2
 =h_{15}^4h_1^4-2h_{16}h_{15}^3h_1^3+h_{16}^2h_{15}^2h_1^2.
\]

The complete one-box parent closure is

\[
 (62,2),\qquad(61,3),\qquad(61,2,1).
\]

An independently written predecessor-horizontal-strip recurrence gives the three raw Pieri rows
and YES multiplicities

| parent | first term | middle coefficient before `-2` | last term | multiplicity |
|---|---:|---:|---:|---:|
| `(62,2)` | 24 | 18 | 13 | 1 |
| `(61,3)` | 56 | 38 | 25 | 5 |
| `(61,2,1)` | 88 | 55 | 32 | 10 |

Thus the all-parent point-child multiplicity space is `C^16`, with parent blocks `1+5+10`.

For one fixed raw mark, the complete Mackey-sector ledger is

| marked cell/sector | characteristic at size 63 (abbreviated) | raw coefficient tuple | rank |
|---|---|---|---:|
| `U` | `h1 h15^2 s15,1^2` | `(18,13,9)` with signs `(+,-2,+)` | 1 |
| `C` | same | `(18,13,9)` | 1 |
| `L` | `h1^2 h14 h15 s15,1^2` | `(24,18,13)` | 1 |
| `R` | same | `(24,18,13)` | 1 |
| `H_L, eta=1` | `h1^2 h15^3 s15,1` | `(18,13)` with signs `(+,-)` | 5 |
| `H_L, eta=V15` | `h1^2 h15^2 s15,1 s14,1` | `(24,18,18,13)` with signs `(+,-,-,+)` | 1 |
| `H_R, eta=1` | mirror | `(18,13)` | 5 |
| `H_R, eta=V15` | mirror | `(24,18,18,13)` | 1 |

The ranks are `(1,1,1,1,5,1,5,1)` and sum to all 16 raw multiplicity lines.  No singleton,
residual, heavy-trivial, or heavy-standard sector may be dropped.

## Unequal-cell Mackey normalization

If a marked sector `c` comes from a cell of size `n_c` and has local irreducible carrier dimension
`d_c`, then its normalized Frobenius evaluation constant is

\[
 \alpha_c=\sqrt{\frac{\dim S^{(61,2)}}{[S_{63}:L_c]d_c}},
 \qquad [S_{63}:L_c]=n_c\frac{63!}{\prod_j n_j!}.
\]

Therefore a transition from source sector `d` to target sector `c` carries

\[
 \boxed{\frac{\alpha_d}{\alpha_c}
 =\sqrt{\frac{n_c d_c}{n_d d_d}}}.
\]

This is the unequal-cell correction; the equal-cell NO formula is its `n_c=n_d` specialization.
For `(U,C,L,R,H_L1,H_LV,H_R1,H_RV)`, the triples `(n_c,d_c,n_cd_c)` are

\[
 (1,225,225),(1,225,225),(15,225,3375),(15,225,3375),
 (16,15,240),(16,210,3360),(16,15,240),(16,210,3360).
\]

## JM, projector, table, and algebra gates

The addable-box contents are `61,1,-2`.  Hence an exact independently constructed last-JM matrix
`X` must satisfy

\[
 \chi_X(x)=(x-61)(x-1)^5(x+2)^{10},\qquad
 \mu_X(x)=(x-61)(x-1)(x+2),
\]

with symmetric spectral projectors

\[
 P_{61}=\frac{(X-I)(X+2I)}{3780},\quad
 P_1=-\frac{(X-61I)(X+2I)}{180},\quad
 P_{-2}=\frac{(X-61I)(X-I)}{189},
\]

of ranks `1,5,10`, pairwise orthogonal and summing to `I_16`.

In any one common orthonormal parent gauge `E`, the eight physical same-mark tables must be
`C_chi=E^*D_chi E`, where the `D_chi` are the eight disjoint raw-sector coordinate projectors.
Consequently their ranks must be `(1,1,1,1,5,1,5,1)`, their sum must be `I_16`, and every one of
the 28 unordered distinct products and commutators must vanish exactly.  The generated unital
star algebra and commutant must have

\[
 \mathcal A\cong\mathbb C^8,\quad\dim\mathcal A=8,
 \qquad
 \mathcal A'\cong M_1^{\oplus6}\oplus M_5^{\oplus2},
 \quad\dim\mathcal A'=6+25+25=56.
\]

All of these are statements in `End(C^16)`.  Cross-parent table blocks are legal after restriction
to the common `S_63` child and must be tested, not erased by retaining the old parent as an output
superselection tag.

## Physical orientation typing

For each `o in {L,R}`, the fixed-child physical orientation is an isometry

\[
 j_o:\mathbb C^{10}\hookrightarrow\mathbb C^{16},
 \qquad j_o^*j_o=I_{10},
\]

block diagonal in the unmarked parents with exact block types

\[
 \mathbb C^1\to\mathbb C^1,\qquad
 \mathbb C^3\to\mathbb C^5,\qquad
 \mathbb C^6\to\mathbb C^{10}.
\]

Thus each orientation has an explicitly constructed six-column unmatched complement, parent
block dimensions `0+2+4=6`; it may not be represented by zero padding.  `j_L` and `j_R` are two
physical embeddings, not two gauges.  A common change of NO/YES parent bases must transform both
coherently and preserve these types, ranks, and complement dimensions.

## Pre-audit NO hash seal

The reviewed `t=0` inputs had the following SHA-256 values before any YES proposer file was opened:

| file | SHA-256 |
|---|---|
| `ksum/artifacts/ksum_L3_critical_induced_packet_alphabet_point_child_gate_a16_20260722.md` | `ECF051FEF929E8B461E05539F8E2D227766C7AE0650EB30A8D7A1AB628E7B6D5` |
| `ksum/tools/ksum_l3_alphabet_point_child_gate.py` | `A247A6DB9EEDE94EBB83626ED3F41EB3047A99B2487901597A0D7EF5BBDA010F` |
| `ksum/artifacts/logs_ksum_L3_alphabet_point_child_gate_20260722/run.json` | `8281115792877C373B88C53601E34F99C1DDC72BBCA45048CB16258559100976` |

## Scope and formula/value boundary

The intended checker will construct the exact finite object independently at only
`a=16,q=64,t=1,tau=(61,2)` and one fixed common raw mark.  Agreement of its values with a proposer
will corroborate the finite object but will not by itself verify the proposer's printed derivation.
The later audit must separately check every displayed proposer formula and its quantifiers.  This
seal licenses no statement for another `a`, all critical `s`, distinct raw marks, occurrence or
position-Pieri factors, a physical occurrence pencil, query attenuation, a numerator, or an
endpoint exponent.
