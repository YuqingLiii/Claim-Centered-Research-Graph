# Public mathematical derivation and audit argument

This document gives the checkable derivation used by the package. It is an audit argument, not hidden reasoning. Machine objects named below are replayed by `verify.py`.

## 1. Frozen scheduling object

The Gross CSS instance has 144 data qubits, 72 X checks, and 72 Z checks. Every check has weight six, so the required named CNOT set has

\[72\cdot6+72\cdot6=864\]

edges. For every named edge `e`, the outer formula has an integer variable `t_e` with `0 <= t_e < 864`. For each check ancilla, its six incident edge times are pairwise distinct. For each data qubit, its three X-edge and three Z-edge times are pairwise distinct. These constraints enforce one two-qubit gate per participating qubit per time and exactly one occurrence of every required named edge.

There are 648 nonempty X/Z check overlaps, each of size two. For overlap `(a,b,{q0,q1})`, the MC constraint is

\[[t_{Z,b,q_0}<t_{X,a,q_0}]=[t_{Z,b,q_1}<t_{X,a,q_1}].\]

Global interleaving is the conjunction `xmax >= zmin` and `zmax >= xmin`, excluding both all-X-before-all-Z and all-Z-before-all-X. A SAT model is order-preservingly compressed onto consecutive used layers. The independent replay checks the resulting used set is exactly `0,...,L-1`, so idle layers are absent. In this batch `L` ranges from 128 to 170.

## 2. Sound outer exclusions

A mechanism fixes a finite conjunction of strict comparisons

\[A=\bigwedge_j(t_{e_j}<t_{f_j}).\]

If raw replay proves that every schedule retaining these comparisons retains a fault mechanism of weight at most ten, the outer search may add the sound block

\[\neg A=\bigvee_j\neg(t_{e_j}<t_{f_j}).\]

At iteration `i`, the exact outer database is 1,440 global unary blocks, 20 round-62 blocks, 4,740 round-69 generalized positive-witness blocks, and `2i` raw-replayed dynamic blocks. Thus iteration 6 starts with 6,212 blocks, and iteration 29 starts with 6,258. The 15,874 exploratory round-63 pair clauses occur zero times.

Each iteration is built in a fresh process. A second fresh process reconstructs every block and the complete SMT-LIB byte stream, fixes all 864 variables to the recorded compressed schedule, obtains SAT, and separately audits the named edge set, ancilla/data conflicts, 648 MC equations, compression, and global interleaving.

## 3. Complete direct-360 adversary

For either error sector there are exactly 360 primary selection variables:

- 144 data-singleton columns `D:q`;
- 3 residual columns for each of 72 same-sector checks, hence 216 residual columns.

For a check order `o=(o0,...,o5)`, the canonical residual position sets are

\[P_0=(0,1),\quad P_1=(3,4,5),\quad P_2=(4,5),\]

and the actual physical hook suffixes are

\[\widehat P_0=(2,3,4,5),\quad \widehat P_1=(3,4,5),\quad \widehat P_2=(4,5).\]

The kind-0 representatives differ by the full weight-six stabilizer, so syndrome and logical quotient agree; raw replay checks this on the candidate order.

Let `x_j` select column `j`. The CNF expresses all 72 opposite-check syndrome parities as zero, computes 12 logical parity outputs, requires their disjunction to be true, and adds an exact sequential-counter encoding of

\[\sum_{j=0}^{359}x_j\le 10.\]

The frozen 1,884-member logical pool in each sector is fully bound to the model metadata, but it is not a search restriction. There is no pool, residual-pattern, contributing-check-count, or within-check-order-family filter. `complete_query=true` and the four excluded restrictions are sealed in every formula summary.

## 4. SAT validation

CaDiCaL ran in the foreground with an internal 600-second limit and an external 660-second process-group limit. Both sectors ran before any state update. Exit code 10 denotes SAT. For each result the replay:

1. parses a truth value for every DIMACS variable;
2. evaluates every clause;
3. reads the selected primary columns;
4. reconstructs the canonical support `V`;
5. reconstructs the actual physical support `Vhat` from candidate edge order and hook suffix;
6. checks opposite-check syndrome zero;
7. checks the support is outside the stabilizer span and has nonzero logical quotient;
8. checks canonical and physical logical parity vectors agree; and
9. extracts only then the exact comparison antecedent used for the next outer block.

All 48 formulas passed. Xerr mechanisms have weights `{9:5, 10:19}`; Zerr mechanisms have `{9:3, 10:21}`. Exact antecedents range from 16 to 76 atoms in both sectors. These recurring weight classes are observations about positive witnesses, not a generalized coverage theorem. No additional generalized clause was emitted.

## 5. Negative controls

For every SAT assignment, flipping the first selected primary falsifies at least one clause. Removing the first selected physical fault destroys the verified logical mechanism. For every outer schedule, forcing two incident edges on data qubit zero to share a time creates a detected collision. A stored truncated iter6/Xerr assignment contains 5,995 of the required 5,996 variables and is rejected.

The DRAT/LRAT toolchain is also tested on a small known UNSAT pigeonhole formula: valid DRAT is accepted and translated to LRAT, valid LRAT is accepted, and corrupted/truncated DRAT and LRAT are rejected. These are checker controls only; no batch sector was UNSAT.

## 6. Why repair and root closure are unavailable

Arbitrary-round repair is gated on independently accepted direct absence proofs in both sectors of the same candidate. Every sector here is SAT, so the gate is false for all 24 candidates. There is no sector absence proof, no double-sector absence candidate, no repair certificate, and no outer UNSAT certificate. A Z3 result string alone would not have established exhaustion in any case.

Therefore the only licensed conclusion is positive CEGAR progress: 48 new exact sound blocks. The interval remains

\[D^*_{Gross}\in\{11,12\}.\]

## 7. Exact next state

After iteration 29, the dynamic file contains 60 blocks: 12 inherited from round 69 and 48 added here. The next exact query is iteration 30 with

\[1440+20+4740+60=6260\]

installed blocks and zero exploratory pair clauses.
