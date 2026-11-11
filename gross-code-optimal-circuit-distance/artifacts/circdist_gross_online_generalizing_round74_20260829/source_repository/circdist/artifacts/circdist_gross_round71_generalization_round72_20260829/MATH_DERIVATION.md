# Public mathematical derivation

## 1. Schedule and direct mechanism

There are 864 named check-data edges, 72 X checks, 72 Z checks, and 648 measurement-collision constraints. A candidate assigns an integer time `t_e` to every edge. Each six-edge check is a strict local order; incident edges cannot collide; the outer encoding is global and interleaved. Idle compression only renames used time layers and does not change an order atom `t_e < t_f`.

For a sector let `H_D` be its detecting matrix, `H_S` its stabilizer span, and `L_0,...,L_11` a quotient-dual logical basis derived from the complete 1,884-member logical pool. The direct formula has 360 elementary selection variables `x_j`. Column `j` has a canonical support `c_j` and a physical support `p_j`. A selected set `S` is a failure mechanism exactly when

```text
|S| <= 10,
H_D (XOR_{j in S} c_j) = 0,
(<XOR c_j,L_0>,...,<XOR c_j,L_11>) != 0.
```

For the frozen hook model the three residual-position sets are

```text
R_0=(0,1), R_1=(3,4,5), R_2=(4,5),
```

and the physical suffix sets are

```text
P_0=(2,3,4,5), P_1=(3,4,5), P_2=(4,5).
```

Round 72 does not assume canonical replay implies physical replay. For every selected hook and its sealed local order it independently rebuilds both masks, XORs them with all selected data singletons, and checks

```text
H_D c = H_D p = 0,
logical(c) = logical(p) != 0,
c,p are outside span(H_S),
|S| <= 10.
```

All 48 round-71 mechanisms pass. Forty have 10 faults and eight have 9. Their canonical net weights range from 12 to 20 and physical net weights from 12 to 22; the bound is on elementary fault count, not net support weight.

## 2. Exhaustive local catalogs

Exactly 113 sector/check pairs occur in the 48 mechanisms. For each check, the code enumerates all `6! = 720` permutations. Each order record contains the ordered qubits; all three canonical residual supports; all three physical suffix supports; the combined 72 syndrome bits and 12 logical quotient bits; and an explicit unary completion when present.

For every catalog, 360 orders have the positive unary completion and 360 do not. The completion uses one selected hook of kind 1 and nine data singletons from a bound weight-12 logical pool member, so the elementary weight is 10. This is a constructive positive witness for each marked order.

## 3. Exact selected-mechanism multi-check relation

Fix one of the 48 selected mechanisms. Its data singletons give a constant signature `d`. For a participating check `c` and local order `o`, XOR the canonical contributions of every selected hook at `c` and define

```text
sigma_c(o) = syndrome_bits || logical_bits.
```

The physical contribution is computed in parallel and has the same signature. If a comparison antecedent permits the local-order domain `A_c`, all reachable global signatures are exactly

```text
R = { d XOR sigma_c1(o1) XOR ... XOR sigma_ck(ok) : oi in A_ci }.
```

This is not a skipped Cartesian product. The generator groups each 720-order domain by equal signature and performs an exact memoized GF(2) transition. Equal signatures are interchangeable for the final syndrome/logical test, so the transition preserves the full truth relation. A term is sound precisely when every element of `R` has zero syndrome and a nonzero logical quotient. Every permitted tuple maps to the explicit fixed selector and to physical suffixes rebuilt from that tuple's local orders.

The 48 mechanisms involve from 2 to 9 checks. Thus the potentially nonfactorizable greater-than-two-check coupling is represented exactly by the signature DP; no independent-pair assumption is used. Two deterministic atom-deletion orders produce 96 raw multi-check terms.

## 4. Conservative pair truth relations

The participating check sets induce 607 structural pairs. For each pair `(a,b)` and order indices `(i,j)`, the positive truth relation is

```text
T(i,j) = U_a(i)
      OR U_b(j)
      OR E(i,j),
```

where `U_a,U_b` are the constructive unary witnesses and `E` is a union of explicit two-hook configurations. Every `E` cell stores the residual kinds/supports, logical completion, data-singleton completion, fault weight, and source round-71 mechanism. If both orders are non-unary, a cell is marked only when one of those physical configurations matches both local orders.

The full 607 by 720 by 720 relation is stored factorwise as 607 arrays of 720 exact 720-bit rows: 314,668,800 represented cells. There are 272 relations with an explicit pair configuration and 335 whose positive content is unary only. The 300 configurations comprise 299 weight-12 completions and one necessary weight-14 completion. That weight-14 witness is the positive transform of weight-12 pool index 566 by stabilizer check 57 for Xerr checks 51 and 57, with logical support

```text
{3,42,47,49,53,57,58,60,115,120,123,125,135,141}.
```

The weight-14 pools contain 9,438 Xerr and 9,435 Zerr constructive positives. No failed search in those pools is used as a negative fact.

## 5. Rectangle extraction and deletion minimality

A conjunction of order comparisons on checks `a,b` defines a rectangle `A x B`. It is accepted only if

```text
for every i in A: B subseteq T(i,*).
```

For every covered tuple, witness selection is deterministic: use the `a` unary witness if available, otherwise the `b` unary witness, otherwise the first stored explicit pair configuration. Atom minimization deletes one comparison at a time only when the rectangle remains within `T`. For every retained atom, deleting it must expose a concrete order tuple outside this positive relation. The stored exposed tuple is a control relative to the selected-mechanism/positive library and never a global absence claim.

The same deletion rule is applied to exact multi-check terms using the GF(2) relation. In total the 566 retained terms carry 5,705 per-atom deletion controls.

## 6. Semantic deduplication and dominance

Each term is represented semantically by its sector and the 720-bit permitted-order mask for every constrained check. Two terms are duplicates when these finite relations are equal. Term `U` dominates `V` exactly when every local tuple allowed by `V` is allowed by `U`; missing check masks mean all 720 orders.

Starting from the reviewed 4,740 round-69 terms and 696 new candidates:

```text
new pair candidates                  600
new exact multi-check candidates       96
duplicate of old                       0
duplicate within new                  85
dominated by old                       0
dominated within new                  45
retained new                          566
merged generalized library          5,306
```

The retained set is 563 pair rectangles and three exact multi-check terms. The three pair-library misses are `iter11-Xerr`, `iter17-Xerr`, and `iter19-Xerr`; they are honestly retained through exact multi-check terms covering respectively 23,887,872, 2,985,984, and 82,944 order tuples. All 48 source mechanisms have at least one retained generalized cover, and all 48 candidate-exact blocks remain in the dynamic state.

These counts describe a conservative positive library. Completeness would require a negative-side proof for every unmarked physical tuple; this package supplies no such proof and makes no completeness claim.

## 7. Exact CEGAR continuation

The licensed iteration-30 state has 6,260 blocks. Adding 566 proved-positive generalized blocks gives 6,826 blocks before candidate 30. Each iteration rebuilds the complete outer model in a fresh Python process, independently reproduces its 864-edge/648-MC SMT formula, runs both unrestricted direct sectors, replays complete assignments clause-by-clause and physically, then appends two exact blocks.

Iterations 30 through 41 are all outer SAT and dual-sector SAT. Twenty-four exact blocks are added. The next state is iteration 42 with 6,850 blocks. Because neither sector of any candidate has accepted absence, repair is never licensed; because the outer remains SAT, no exhaustion claim is available.
