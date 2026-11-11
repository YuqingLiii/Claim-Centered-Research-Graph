# EFSSC soundness and atomic continuation

## Definition

Fix a sector and a named selection `s` consisting of distinct data columns `D:q` and residual columns `R:c:k`, with total count at most ten. For a schedule `t`, let `o_c(t)=(q_0,...,q_5)` be check `c`'s qubits sorted by the six strict CNOT times. Define canonical position sets

`A_0={0,1}`, `A_1={3,4,5}`, `A_2={4,5}`.

If several residual kinds of the same check are selected, their aggregate support is indexed by the symmetric difference

`A(K_c) = XOR_(k in K_c) A_k`.

Let `sigma(q) in F_2^84` be the frozen qubit signature whose low 72 bits are detector incidences and whose high twelve bits are logical-dual parities. The selector signature is

`Sigma_s(t) = XOR_(D:q in s) sigma(q) XOR XOR_c XOR_(p in A(K_c)) sigma(o_c(t)[p])`.

Define

`V_s(t) := [low_72(Sigma_s(t))=0] AND [high_12(Sigma_s(t)) != 0]`.

The installed EFSSC is the source root `NOT V_s(t)`.

## Exact-validity theorem

**Theorem.** For every legal frozen schedule `t`, `V_s(t)` is true if and only if the fixed named selection `s` is a terminal effective logical of weight `|s|<=10` in its declared sector.

**Proof.** Each data singleton contributes exactly `sigma(q)`. A residual `R:c:k` contributes the XOR of `sigma(q)` over the qubits occupying `A_k` in the schedule's strict local order. XORing all selected columns commutes and cancels duplicates, so grouping residuals by check yields exactly the symmetric-difference position set `A(K_c)`. The low 72 coordinates of the total signature are therefore exactly the detector syndrome of the selected canonical net support; the high twelve coordinates are exactly its logical-dual coordinates. Zero low coordinates and at least one high coordinate are precisely zero syndrome and nontrivial logical class. The weight is fixed by the number of distinct names and is independent of the schedule. ∎

## Physical soundness

The physical position sets are `P_0={2,3,4,5}`, `P_1=A_1`, and `P_2=A_2`. Since `P_0 XOR A_0` is the complete six-qubit stabilizer row, replacing canonical supports by physical supports changes the aggregate only by stabilizers. It leaves detector syndrome and logical coordinates unchanged. Thus the theorem also certifies that every true EFSSC corresponds to the same named physical terminal mechanism under the frozen elementary-fault convention.

## CNF realization

For each participating check and qubit, five strict comparisons identify the qubit's rank among six. A complete 32-row truth table binds whether that rank lies in `A(K_c)`. The compiler XORs the selected qubit signatures, forms all 84 parity coordinates, and defines `V_s` by a full conjunction/disjunction circuit. A root unit clause forces `NOT V_s`. The independent checker reconstructs all membership truth tables and every defining clause from the semantic source.

No source atom cube is substituted for `V_s`; the exact Boolean domain may be disconnected and may include cross-check cancellations. The old `source_atoms` are retained only as provenance and physical replay evidence.

## Atomic transition protocol

Let `P_i` be the selector prefix before iteration `i`. The transition is:

1. solve exactly `Outer_(P_i)` in a fresh bounded process;
2. retain and clause-check a complete assignment;
3. decode and audit the schedule against all 864 interactions, 648 MC relations, endpoint conflicts, global interleaving, 14,484 blocks, and all selectors in `P_i`;
4. build both complete unrestricted direct-360 formulas;
5. require SAT and complete clause/physical replay for Xerr and Zerr;
6. form selectors `s_i^X,s_i^Z` from those exact named selections;
7. independently verify `V_(s_i^X)(t_i)=V_(s_i^Z)(t_i)=True` and verify every old selector is false;
8. append both selectors together, compute the canonical selector-state hash, emit the fresh unstarted source for `i+1`, and only then publish the record.

If either direct query had been UNSAT, UNKNOWN, timed out, or verifier rejected, no pair would have been committed under this transition. Later selectors are absent from the source used to solve earlier candidates; therefore no retroactive cut is used.

## Round90 transition ledger

| iteration | prefix | added selectors | weights X/Z | source schedule SHA-256 | state-after SHA-256 |
|---:|---:|---|---|---|---|
| 112 | 140 | `r90-i112-Xerr`, `r90-i112-Zerr` | 10/10 | `bbcce5e137626ac9fb9600ac093c46789ae2b8ddb13531078b5c06371e574e5e` | `f3c7f81bf7b0d81af3ed254054cd29338c173d2da7f8837be18abcf8306feeee` |
| 113 | 142 | `r90-i113-Xerr`, `r90-i113-Zerr` | 10/10 | `69db40d0326eb03ddf32e92880f446471cc06f409d802547516d6315687c5cd7` | `0f61bd1f7ddc52a6bfdcfff3d198774ac99d3558931737b9f72b9149311a954b` |
| 114 | 144 | `r90-i114-Xerr`, `r90-i114-Zerr` | 10/10 | `0fd9611076774d9359d473303269ad801a7b911b6db1a319ee8cd86dc1928fb7` | `0b269f3609e81928bf3e79bc2d1dda1f53f23e800da1c51f2ff1e4a7a1738708` |
| 115 | 146 | `r90-i115-Xerr`, `r90-i115-Zerr` | 10/9 | `5dac0dbc23c28a3b58e1affbaf7df67270c9364d1a9646792c1403858a29571e` | `7896e13abd03b0665852112f97417e7ec42d838c076b3563bc01c08d59f961b4` |
| 116 | 148 | `r90-i116-Xerr`, `r90-i116-Zerr` | 10/10 | `6c1f5efcf2ec11e980c3fa6f79b7aba380187abc922687695fd70607b475e26f` | `a16ac76ea004b02d2df4cd3ef6e2787d0de18273a0fa55c0ba8873b1a03df03d` |
| 117 | 150 | `r90-i117-Xerr`, `r90-i117-Zerr` | 10/10 | `b6de1a0ba69a87841ffc17f8db691d85c85ad29bb245f3b40abbb72fc7099291` | `0392d24445dfc276715ec3eb4ad73e851bac1ad0d58b7463bffac2ad5e78bb55` |
| 118 | 152 | `r90-i118-Xerr`, `r90-i118-Zerr` | 10/10 | `956618afb0325fa69adecaf994dbcabbd9fb744882552fb8620f1f72070e8b21` | `53e01b89f5b1772a4e6109ce454a5351077ca2092a9f5e3e39a1ebf2c91f4d5e` |
| 119 | 154 | `r90-i119-Xerr`, `r90-i119-Zerr` | 9/10 | `2efd95f27430f1b8a4d8cef8c86c15ef2247eda26bbe55959f355e60c3410c49` | `e7278568a1e38939969bde2da6b60e950e5be2f8fadd70c58b74e3d807e01faf` |
| 120 | 156 | `r90-i120-Xerr`, `r90-i120-Zerr` | 10/10 | `a7c52588b152724dce6e822910bbed4ebe37df1aacbbe06ba1459b1ae2688210` | `c96a2e01c5579c28ab048b4101182fea54bec26b9e9e5f70aabde75c72bcd506` |
| 121 | 158 | `r90-i121-Xerr`, `r90-i121-Zerr` | 10/10 | `4db4b8641df1ae4709f1467177ee0397d5b2cd384ec8c1e7b9f0ca81ea01b643` | `e00d6529570b2e69dbd6da75fa7cc707de354b81b86a2630d2b8bbd0d6bd0b05` |
| 122 | 160 | `r90-i122-Xerr`, `r90-i122-Zerr` | 10/10 | `91db319cc429009edcf5c856efd24317498e04875c28cf7a9655b225025974be` | `14e551af5ea909e1e88f02def5bfaaf61df3d0557e48c9544546389db1acbf99` |
| 123 | 162 | `r90-i123-Xerr`, `r90-i123-Zerr` | 10/10 | `9fd434dbd60840b4da5ad4954e655af11468d3643a0fbc1197c89329908ae5f6` | `854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3` |

The state chain begins at the independently reviewed Round88 hash `a0364547f846fd68ace7cdba85d89c0f8e6326145243fb0fea7ff543420994cb` and ends at `854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3`. The sealed final state contains exactly 164 unique selector semantic hashes and exactly completed iterations 112–123.

`source/check_continuation.py` rebuilds all selector objects from the stored schedules and direct replays. Package `replay.sh` independently reruns the transition writer and requires byte equality for every record, every next source, and the final state.

## Scope limitation

An EFSSC excludes only schedules on which its fixed named selection remains valid. It is not a universal pattern absence theorem, a direct-sector UNSAT result, a full-circuit repair theorem, or an exhaustion certificate. Twelve successful transitions do not imply that the next outer formula is UNSAT; iteration 124 is deliberately unsolved.
