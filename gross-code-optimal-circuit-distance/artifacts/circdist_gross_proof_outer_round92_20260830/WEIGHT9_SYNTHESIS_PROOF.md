# Public proof of the Round92 weight-9 synthesis step

## Frozen objects

For a CSS sector, every direct-360 elementary column has an 84-bit signature
`sigma = detector_72 || logical_12`.  A named data column `D:q` has the frozen qubit
signature.  For a residual name `R:c:k`, its canonical support is determined by the
within-check rank positions `P_k`: `P_0={0,1}`, `P_1={3,4,5}`, and `P_2={4,5}`.
The six qubits of check `c` are permuted by the frozen schedule's strict local order.

A fixed named selector is valid exactly when the XOR of its signatures has zero low
72 bits and nonzero high 12 bits.  Its weight is the number of distinct named columns,
not the weight of its final data support.

## Factorized universal domain proof

For every participating check `c`, XOR the residual position sets of all residual names
from that check to obtain `P_c`.  Across all six-element local permutations, every
`|P_c|`-subset of the check row occurs as the selected qubit support, each with exactly
`|P_c|! (6-|P_c|)!` permutations.  Therefore it is sufficient and complete to enumerate
the subset options for each check.

Split the participating checks into left and right products.  Let `L(v)` and `R(v)` count
factor choices yielding full 84-bit signature `v`, including the fixed data-column XOR
on the left.  Let `L_72(s)` and `R_72(s)` be the corresponding counts after projection to
the detector bits.  The exact number of support tuples with zero detector and nonzero
logical signature is

`sum_s L_72(s) R_72(s) - sum_v L(v) R(v)`.

The first term counts every pair with equal detector projection; the second removes
exactly those whose full signatures are equal, which are precisely the pairs with zero
logical part as well.  Multiplication by the local permutation factors gives the exact
number of local-order tuples.  This is a complete finite proof over every local-order
tuple, including empty domains.  Each retained selector also stores a constructive
support choice and local permutation witness.

## Physical residual theorem

The actual physical suffix supports are `Q_0={2,3,4,5}`, `Q_1={3,4,5}`, and
`Q_2={4,5}`.  Thus `Q_1=P_1`, `Q_2=P_2`, and

`Q_0 XOR P_0 = {0,1,2,3,4,5}`.

The last set is the entire frozen generating row of the same-sector check.  Replacing a
canonical kind-0 residual by its physical suffix therefore adds one stabilizer row;
kinds 1 and 2 are unchanged.  Detector syndrome and all logical-dual parities are
invariant.  Consequently every tuple accepted by the exact signature calculation has an
explicit physical terminal mechanism of the same named fault count.

## Reconstructed nine-column bases

The i115 Zerr base is

`D:111, D:114, R:38:0, R:41:0, R:41:2, R:43:2, R:47:2, R:48:0, R:50:2`.

Its syndrome is zero and its logical vector in LSB-first order is `001101000000`.

The i119 Xerr base is

`D:55, D:63, D:129, R:53:0, R:55:0, R:56:2, R:62:2, R:65:0, R:71:1`.

Its syndrome is zero and its logical vector is `101100000001`.  Both were reconstructed
from the reviewed Round90 schedule, direct proof object, local orders, canonical support,
physical support, and frozen model rather than trusted as opaque inputs.

## Complete tested families

For each base, all 351 possible extra elementary columns were tested.  The i115 base had
11 nonempty residual completions and 340 zero domains; all 144 data completions were among
the zero domains.  The i119 base had 29 nonempty residual completions and 322 zero domains;
all 144 data completions were again zero.  Across all nonempty proper subsets of each
nine-column base, 2 of 510 i115 minors and 1 of 510 i119 minors were nonempty.

Among the prior 164 selectors, no same-sector pair had a compatible union of at most ten
columns.  Among all 6,642 same-sector pairs, six symmetric differences had weight 1–10;
exactly one had a nonempty domain.  The resulting novel ordinary terms, after semantic
deduplication against the prior registry and against each other, total 44.

For source-cube relaxation, each of 101 individual order atoms was deleted in turn.
Every local permutation satisfying the remaining atoms was enumerated at the affected
check.  The base selector and the complete same-coordinate one-residual completion family
were tested on every such tuple.  Ninety-seven deletions strictly broadened the local cube,
but every one had an explicit uncovered tuple; four did not broaden it.  Hence no relaxed
cube was retained.

## Strict expansion and scope

Local-domain nonemptiness alone need not extend to a globally legal schedule.  The separate
frozen-CNF query retained all base constraints and all 164 old negative selector clauses,
removed only the 44 new negative roots, kept their defining circuits, and added one clause
requiring at least one new validity variable.  Its checked SAT model has all old validities
false and exactly `r92-r90-i119-Xerr-plus-R_61_2` true.  The mapped frozen schedule passes
all 864 interaction, conflict, 648 MC-overlap, local-order, whole-check, global-interleaving,
and MC0 checks.  This is an exact witness that the new union strictly contains the old union.

The theorem is limited to the declared selector families and their exact domains.  It does
not claim that no other generalization exists, that any zero domain is global absence, or
that the 44-term union covers all frozen schedules.

