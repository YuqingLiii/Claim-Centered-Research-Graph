# Round-66 attack and rejected-branch ledger

This ledger records inspectable claims, calculations, and branch dispositions.  It is not a record
of private reasoning.

## A. Repetition/block-contiguous route

| ID | proposed premise or attack | exact result | disposition |
|---|---|---|---|
| B1 | Static `d_Z=3` should exclude effective-Z faults of size `<3`. | False. Static distance controls sums of data columns. Two long Z hooks can sum to a logical. | Rejected; never used. |
| B2 | The old `W=6,d_Z>=7` COPY/NEGATE shortcut can be restored. | It was refuted before this round; the licensed construction has old Z weight up to 120 after repetition. | Forbidden and not reused. |
| B3 | Threefold repetition should force every hook pair to have a threefold-repeat image. | False at partial block cuts. Inner X checks attach a two-bit copy marker. Exact formulas are README (4.1)--(4.2). | Replaced by exact cut classification. |
| B4 | Increasing block-contiguous order is automatically safe. | False on the one-positive-clause source instance. Rows 0 and 9 at lifted cuts 24 and 6 yield `R([18,19,21,23])`, a nontrivial Z logical. | Refuted by `COUNTEREXAMPLE.json`. |
| B5 | Each single source-row support contains no logical, so any two hooks are safe. | Premise holds on all 21 rows of the counterexample, but conclusion fails: 14 of 210 two-row unions have a nontrivial restricted quotient. | Exact algebraic obstruction identified. |
| B6 | The one-clause witness refutes every block order. | False as a claimed inference. `random.Random(0)` gives a safe block tuple on this finite instance. | Explicitly not claimed. |
| B7 | Random search over block orders could prove the universal existential lemma. | Finite success cannot establish existence uniformly for all formulas, and no polynomial emitter/proof followed. | Corroboration only; route not used. |

### Exact block-route residual

For chosen old row permutations, block-contiguous Z safety is equivalent to absence of one/two
nontrivial mechanisms among old boundary-prefix columns.  Partial hooks only move one prefix across
its current old qubit; exact cuts lift old prefixes.  The existential block route is therefore an
old Z-prefix scheduling CSP.  This package neither proves nor refutes that CSP for every source
instance.

## B. Private-sentinel construction attacks

| ID | attack | exact result | proof/check location |
|---|---|---|---|
| S1 | A decorated hook may be undetected by all marker checks. | No proper prefix of the emitted order has zero marker syndrome. | README M1; `sentinel_state_audit`. |
| S2 | Two hooks of different decorated rows may cancel. | Their nonzero syndromes occupy disjoint row-private marker families. | README 9.2. |
| S3 | Two hooks of one decorated row may revisit a marker state after a long old-data interval. | Equal states occur only across one immediately adjacent old data gate. | README M2; exhaustive path checks. |
| S4 | A marker-row hook may cancel a decorated hook while leaving a logical old prefix. | A decorated state confined to one block occurs only with old projection `0` or the full source stabilizer `z_r`. | README M3 and 9.4. |
| S5 | Closing full marker triples may hide residual marker support. | Every completed triple is exactly `g_(r,j)` and is a retained Z stabilizer. | README 6 and 9.4. |
| S6 | A joint CNOT hook-plus-data Pauli is absent from the column audit. | It equals the adjacent suffix/prefix; data columns and every proper hook prefix are enumerated. | README 2 and 9; `terminal_columns`. |
| S7 | Marker-only faults create a new logical. | On each triple `ker[ab;ac]=span{abc}=S_Z`; different blocks have disjoint syndrome. | README 6.2 and 9.5. |
| S8 | New marker X checks alter the reviewed old X pair CSP. | Old syndromes are embedded by decorated rows and old quotient classes are unchanged. New weight-two X hooks are reduced singletons, harmless at `d_X=4`. | README 10; partition check over 582 values. |
| S9 | The transformation changes `k,d_X`, or `d_Z`. | Row operations expose a direct sum with `L` trivial `[[3,0]]` blocks; ranks change by `(2L,L)` and both logical quotients are canonical copies of the old quotients. | README 6.2; three branch rank checks. |
| S10 | The advertised Z weight bound is missed on an occurrence-four variable. | Old weight 40 becomes 120 under `R_3`, then exactly 486 under `D_Z`. | `verifier_output.json`. |
| S11 | The sentinel proof is insensitive to order. | False, as desired: grouping all openings before companion-row-2 data gates creates two equal-marker hooks differing by logical `[0,1,8]`; the exact audit rejects it. | Final negative control. |
| S12 | Local choices may lack a compatible global schedule. | All check circuits can be executed serially; only shared-qubit conflicts exist and no `T` is supplied. | README 11. |

## C. Construction alternatives not promoted

* A shared sentinel family would lose the disjoint-syndrome argument across decorated rows.  No
  safe shared-family theorem was found or asserted.
* Grouping all marker openings, even with private families, is unsafe by S11.
* The package does not claim `W+2` triples are minimal.  They give a short universal invariant and
  absolute constants; optimizing the additive guards is outside the claim.
* Chain-complex products and COPY/NEGATE sparsification were not needed once the private-sentinel
  transform preserved both logical quotients exactly.

## D. Remaining review risk

The result remains proposer-level.  The highest-value independent attacks are: rederive the
terminal column classification from the frozen circuit; test M2/M3 symbolically; check every case
of decorated-plus-marker cancellation modulo the full new Z row space; independently prove the X
iff preservation; and replay total malformed/empty/nonempty branches without importing package
assertions as premises.
