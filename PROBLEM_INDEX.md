# Problem index

Each research problem with a recorded proof-DAG has its own self-contained project directory. Node IDs, claims, routes, assessment levels and research events are those of the original records.

| ID | Problem | Project | Node files | Entry / root nodes |
|---|---|---|---:|---|
| P01 | Channel additivity violations | [`channel-additivity-violations/`](channel-additivity-violations/README.md) | 174 | `HAEQ.goal`, `HCPREV.goal`, `HEXT.goal` |
| P02 | Werner–Holevo zero-capacity boundary | [`werner-holevo-capacity-threshold/`](werner-holevo-capacity-threshold/README.md) | 20 | `WHGAP.goal` |
| P03 | Quantum-capacity superactivation | — | — | No DAG project for this problem was found; none is included. |
| P04 | Bound entanglement with negative partial transpose | — | — | No DAG project for this problem was found; none is included. |
| P05 | Circuit-distance stabilization | [`circuit-distance-stabilization/`](circuit-distance-stabilization/README.md) | 4 | `CIRCDIST.sat` |
| P06 | Circuit versus effective distance | [`circuit-versus-effective-distance/`](circuit-versus-effective-distance/README.md) | 4 | `CIRCDIST.lift` |
| P07 | Optimal circuit distance of the Gross code | [`gross-code-optimal-circuit-distance/`](gross-code-optimal-circuit-distance/README.md) | 4 (1 copied dependency) | `CIRCDIST.gross` |
| P08 | Complexity of distance-preserving schedules | [`distance-preserving-schedule-complexity/`](distance-preserving-schedule-complexity/README.md) | 5 | `CIRCDIST.cplx` |
| P09 | Quantum k-sum with small alphabets | [`ksum/`](ksum/README.md) | 144 | `KSUM.goal`, `KSUM.k2.lower`, `KSUM.k2.threshold` … |
| P10 | Set equality and collision | [`se/`](se/README.md) | 85 | `SE.goal`, `SE.br.cor16`, `SE.goal.conditional-optimal` |
| P11 | Finite-dimensional Grothendieck bounds | [`finite-dimensional-grothendieck-bounds/`](finite-dimensional-grothendieck-bounds/README.md) | 55 | `GROTHD4.goal`, `GROTHD4.fixed-support.upper`, `GROTHD4.cut.affine-equality-terminals` … |
| P12 | Group-orbit Bell matrices | [`group-orbit-bell-matrices/`](group-orbit-bell-matrices/README.md) | 32 | `GROTHORB.transitive-optimum`, `GROTHORB.extremizer-classification`, `GROTHORB.measurements` … |

Node files across projects: 527. One node (`CIRCDIST.lift.iff`) appears in two circuit-distance projects as a recorded dependency copy, so the number of distinct claims is one less.

Linked evidence that is not present in this repository is listed in [`EVIDENCE_GAPS.yaml`](EVIDENCE_GAPS.yaml).
