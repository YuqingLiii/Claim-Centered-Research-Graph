# Round 64: deterministic X-sector reduction after the Proposition-5 refutation

**Verdict: MATERIAL X-REDUCTION PREMISE READY FOR FRESH REVIEW, with remaining Z/other premise exact.**

Date: 2026-08-28.  Target: `CIRCDIST.cplx.fixed-d@task-004`.  This package does not edit or
promote a DAG node.  The theorem below is narrower than the fixed-d claim: it proves the hard
X-sector gate and the full static-distance/structure promises, but it does not prove that the
constructed main block has a distance-preserving **Z-sector schedule**.

## 1. Exact theorem offered for review

Let **X-EFF3** be the following promise problem in the frozen single-ancilla terminal-residual
model.  The input is a CSS pair `(H_X,H_Z)`, allowed local CNOT-order lists, the ordinary
qubit-sharing conflict model, no depth bound `T`, and the promise that the full CSS static distance
is exactly 3.  The question is whether the X-check orders can be chosen so that
`d_eff^X >= 3`.

**Theorem R64-X.** X-EFF3 is NP-complete even on the family below:

* `d_X=4`, `d_Z=3`, hence full static distance exactly `3`;
* X-check weight at most `4`, Z-check weight at most `120`;
* qubit Tanner degree at most `20`;
* every X-order list has size at most `3`, every Boolean-carrying core check has exactly three
  orders (one per 2|2 split), and all other X-order lists are singleton;
* every Z-order list is the singleton increasing-support order;
* there is no optional depth bound and no artificial conflict edge: sequential execution realizes
  every local-order tuple.

Thus the construction is on the honest `d=3` / active domain-3 side of the boundary.  It does not
contradict the PROVED island where **all** order domains have size at most two and the CSP is 2-SAT.
The large constant `120` is honest; this is not a weight-4-or-6 theorem.

NP membership is bound directly to the current PROVED premise
`CIRCDIST.cplx.upper`, exact 301-character claim hash
`1c2b9d0fed28591066e3fccba2578b00d179535a0aba048d1423b0397cee32b1`.
Its fixed-`d` schedule-certificate/fault-enumeration proof applies verbatim after deleting the
Z-sector tests.  This is a direct use of that premise, not inheritance through the root or the
classification route.

## 2. Total source language and Karp map

The source is Tovey's `(3,4)-SAT`: every clause has exactly three distinct variables, no variable
is repeated in a clause, and every variable occurs in at most four clauses.  It is NP-complete
[Tovey, *Discrete Applied Mathematics* 8 (1984), 85-89,
doi:10.1016/0166-218X(84)90081-7](https://doi.org/10.1016/0166-218X(84)90081-7).
The paper explicitly defines `(r,s)-SAT` and assumes no repeated variable in a clause.

For totality, fix the encoding `p n m` followed by exactly `3m` nonzero signed decimal variable
indices.  A parser accepts only if `n,m` are nonnegative canonical integers, every absolute index
is in `1..n`, each clause has three distinct absolute indices, occurrence counts are at most four,
and no token remains.  A valid string is in the source language iff its formula is satisfiable;
malformed strings are outside it.

The deterministic map `K` is:

1. Malformed input: output the fixed domain-3 K4-NO block of Section 10, apply the three-copy
   transform, and direct-sum the fixed companion.  This is a promised X-EFF3 NO instance.
2. Valid input with zero clauses: output only the fixed companion with the explicit safe X schedule
   in Section 8.  This is a promised YES instance, matching the empty CNF.
3. Valid input with at least one clause: discard unused variables and renumber used variables by
   first occurrence; construct `C_0(F)` in Sections 3-5, apply `R_3`, and output
   `K(F)=R_3(C_0(F)) direct-sum G_neq3`.

Every branch halts.  The malformed and empty branches also cover negative integers, bad UTF-8,
integer overflow in a bounded implementation, truncated files, repeated variables, and edge cases.
On a valid formula, the construction uses only fixed loops and XORs; its output size is linear.

## 3. Entire main CSS construction

Write `V` for the number of used variables and `m>=1` for the number of clauses.  Use a point space
`P=F_2^(V+2m)` with basis points

```
p_v                         for every used variable v,
q_t,1 and q_t,2             for clause t,
q_t,3 = q_t,1 + q_t,2.
```

For literal position `r` in clause `t`, the routing line is
`{p_v,q_t,r,p_v+q_t,r}`.  The last point is gadget-private.  Basis-support comparison proves that
all private points are distinct, that none is a named point, and that the only repeated named
points are the intended occurrences of a variable and the intended clause/gadget use of `q_t,r`.

There are 16 four-qubit **planes** per clause: one clause plane and five for each of three literal
gadgets.  Enumerate them deterministically and give plane `i` a fresh private base coordinate `b_i`.
For a plane on line `{u,v,u+v}`, its four H_Z columns are

```
b_i,  b_i+u,  b_i+v,  b_i+u+v.                       (1)
```

The four qubits form a weight-4 X-check.  A connector at point `u` between planes `i,j` is the
weight-4 X-check consisting of their two canonical u-pairs:

```
{b_i,b_i+u,b_j,b_j+u}.                               (2)
```

Duplicate `(i,j,u)` connectors are deterministically suppressed.  `H_Z` is the coordinate matrix
of all columns (1); its rows are the base and point coordinates.  Equations (1)-(2) have zero
column sum, so every X row is orthogonal to every H_Z row.  This specifies all of `C_0(F)`.

The core-check order domain consists of the three permutations whose middle split is respectively
`{b_i,b_i+u}`, `{b_i,b_i+v}`, or `{b_i,b_i+u+v}`.  A connector has the singleton order whose middle
split is `{b_i,b_j+u}`.  Its selected syndrome is

```
a(i,j,u) = b_i+b_j+u.                                (3)
```

Every H_Z check gets the singleton increasing-qubit order.  The optional depth bound is absent.
The only gate conflicts are shared-qubit conflicts, and executing all checks sequentially realizes
any selected tuple.

## 4. Deterministic total placement and cap proof

This replaces Island V's fixed-dimensional random rejection sampler.

```
PLACE(F):
  parse and validate F; otherwise return FIXED_NO
  allocate V+2m point basis coordinates in the order above
  derive q_t,3 and every private point by XOR
  enumerate the 16m planes and allocate a new base coordinate to each
  emit the four columns (1) for every plane
  run the explicit nonzero/distinct/cap and point-collision audits
  if an audit fails, return FIXED_NO             # unreachable by the lemmas below
```

The ambient dimension is
`D=(V+2m)+16m=V+18m <=21m`; the number of old qubits is `N_0=64m`.
Each emitted column has exactly one base coordinate.  Therefore it is nonzero.  Two columns with
different base coordinates differ; two with the same base coordinate belong to one plane and their
four point parts are distinct.  Finally, the XOR of two columns has base weight zero (same plane)
or two (different planes), whereas a column has base weight one.  Hence no two distinct columns
XOR to a third.  The columns are a cap, and `ker H_Z` has no nonzero word of weight 1, 2, or 3.

The optional audit uses a hash set for zero/distinct and checks every unordered pair XOR against
the column set: `O(N_0^2 D)=O(m^3)` bit operations (or `O(m^2)` word-XOR operations).  All other
loops are linear in the output.  There is no search, randomness, retry bound, assertion-dependent
partiality, or fixed ambient dimension.  The proved tag invariant makes the fallback unreachable;
including it makes an implementation total even under malformed internal data.

## 5. COPY/NEGATE and the schedule semantics

Let `h` be one global nonzero formal label, and let every literal gadget `g` have a fresh independent
label `r_g`.  Interpret Island V's `0,1,2,3` as `0,h,r_g,h+r_g`.  Its five label triples are

```
COPY:    (0,h,h) (0,r,r) (h,0,h) (h,h,0) (r,0,r)
NEGATE:  (0,0,0) (0,h,h) (h,h,0) (h,h+r,r) (r,0,r).
```

For every point and every repeated label, connectors (2) join consecutive planes.  At the first two
points, occurrences of `0` and `h` are additionally joined to the global name registry.  A clause
plane has labels `(0,0,0)` and is joined to the `0` class at each routed clause point.

The gadget relation has a short exhaustive *case proof*, not an empirical assumption.  A selected
class not printed at a point is denoted `*`; it serves no row there.  Checking the five displayed
disjunctions gives exactly

```
COPY:    (external u, external v, private witness) = (0,0,0), (h,h,r)
NEGATE:                                           = (0,h,r), (h,0,h).
```

For example, in COPY with the first selection `0`, the last three rows force the second and third
selections to `0`; with first selection `h`, the first, second and fifth rows force second `h` and
private `r`; first selection `r` or `*` makes two required private values inconsistent.  The four
NEGATE cases are identical substitutions in the second table.  Thus COPY pins both external points
to `{0,h}` and equates them; NEGATE pins and negates them.  `verify.py` repeats all `5^3` cases as
corroboration.

At `d_X>=4`, a weight-4 check's one-fault suffixes reduce modulo its stabilizer to weights 1,2,1.
At fault budget two, any mechanism involving a reduced singleton has a representative of weight at
most 3 and cannot be an X logical.  Two middle, weight-2 hooks conflict exactly when their H_Z
syndromes agree but their classes modulo `S_X` differ.  Consequently an X-safe schedule is exactly
a choice of one of the three pair classes per core check such that checks choosing the same syndrome
choose the same class.  This is the reviewed weight-4/d_X>=4 hook-value lemma, and the preceding
weight split also proves the specialization directly.

## 6. Replacement for Proposition 5: the no-unintended-pair-relations lemma

The refuted assertion said that pairwise equalities were the **only** relations a CSS family could
create.  This package does not say that.  It proves the following weaker statement, which is exactly
what completeness and soundness use.

**Lemma (formal-label separation).** In `C_0(F)`, for every pair value used by a core plane, two
values with the same syndrome are equal modulo `S_X` iff their displayed formal labels are equal.
Every connector's selected value is free.  These statements remain true after `R_3`, after adding
the inner checks, and after direct sum with the companion.

**Proof.** Define a linear map `A:F_2^N -> W`, where
`W=span{h} direct-sum span{r_g:g a literal gadget}`.  On the four qubits of a plane labelled
`(x,y,x+y)` set

```
A(e_b)=0, A(e_b+u)=x, A(e_b+v)=y, A(e_b+u+v)=x+y.    (4)
```

Every core row maps to zero.  Every connector joins two equal-labelled pairs, so it also maps to
zero.  Hence `S_X subset ker A`.  If equal-syndrome pairs with distinct formal labels differed by
an X stabilizer, applying A would say their nonzero label difference was zero, a contradiction.
Conversely, every intended equal-label pair is joined by a connector chain (including the name
registry), or is the complementary pair inside one core row, so its difference is in `S_X`.

It remains to classify syndrome collisions.  Core values have base-tag weight zero.  The selected
connector value (3) has base-tag weight two and is unique: equality forces the same unordered base
pair and the same point, hence the same deduplicated connector.  Repetition inner checks have
base-tag weight one; inner checks over copies of the same old qubit have equal classes because their
difference is an inner stabilizer.  The point-basis support classification in Section 3 shows that
core point equality is exactly an intended shared variable, clause point, or one gadget line point.
The fixed companion uses a disjoint syndrome-coordinate block, so no nonzero cross-component
syndrome equality exists.  This exhausts core/core, core/connector, connector/connector,
inner/old, inner/inner, and cross-component pairs.  QED.

This is also a classification of every relation relevant at fault budget two.  It does **not** claim
`ker A=S_X`; higher-arity kernel relations are allowed.

## 7. Completeness and soundness

Given a satisfying assignment, select class `h` at `p_v` for TRUE and `0` for FALSE.  For a positive
literal use NEGATE; for a negative literal use COPY.  The routed `q_t,r` class is therefore `0`
exactly when that literal is true.  Use the private witness listed in Section 5.  Each satisfied
clause has a `q_t,r` in class 0, serving its `(0,0,0)` clause plane.  Choose the corresponding core
orders, the fixed connector/inner orders, and the companion witness.  The separation lemma excludes
every cross-check X mechanism of size below three, proving completeness.

Conversely, an X-safe schedule defines a partial section: checks selecting the same syndrome must
select the same actual class.  The separation lemma says every gadget sees exactly its displayed
partition.  The five-row case proof pins every occurrence of `p_v` and `q_t,r` to `0` or `h` and
enforces COPY/NEGATE.  The name connectors make all occurrences of a variable use one class.  Read
`v=TRUE` iff `p_v=h`.  A clause plane must select one of its three points, and its label there is
0, so some routed literal is true.  The read assignment satisfies every source clause.  Extra
higher-arity stabilizer relations cannot enlarge a gadget relation; the formal map specifically
prevents the only dangerous event, a designed unequal pair-class merge.  This proves soundness.

## 8. CSS parameters, both static sectors, and exact distance 3

For a nonempty formula, `C_0(F)` has `64m` qubits, `16m` core X rows and at most
`27m-2V` connectors, hence at most `43m-2V` X rows.  It has at most `21m` H_Z rows.
CSS commutation was proved from zero column sums.  The cap gives `d_X(C_0)>=4`.  Every literal
gadget contains, at its first point, a formal-0 pair and a formal-h pair.  Their four-qubit XOR has
zero syndrome but nonzero A-image, so it is outside `S_X`; therefore `d_X(C_0)=4` exactly.

Apply the three-copy transform `R_3`: replace every old qubit q by `(q,0),(q,1),(q,2)`; put every
old X row on copy 0; add X rows `(q,0)+(q,1)` and `(q,0)+(q,2)`; repeat every old H_Z row on all
three copies.  Let `pi` take block parity.  Then

```
ker H_Z' = pi^{-1}(ker H_Z),
S_X'     = ker pi + lift_0(S_X),
ker H_X' = {repeat(z): z in ker H_X},
S_Z'     = {repeat(z): z in S_Z}.
```

The first two identities give `d_X(R_3 C_0)=d_X(C_0)=4`; the last two give
`d_Z(R_3 C_0)=3 d_Z(C_0)>=3`.  They also preserve k.  This addresses both static CSS sectors
without assuming anything about a Z schedule.

Finally direct-sum the printed `G_neq3` companion:

```
X: 0123 4567 148(10) 068(11) 379(10)
Z: 12479 0167(10) 012389 0145(11) 02468(11) 4567(10)(11) 89(10)(11).
```

Complete enumeration gives `(d_X,d_Z,k)=(4,3,2)`; `verify.py` independently reproduces it.  Its X
split witness is `(0,1,0,0,0)` in the row order above.  Direct-sum distances are minima, so every
nonempty output has `d_X=4`, `d_Z=3`, and static distance exactly 3.  The fixed empty and malformed
branches use the same companion and hence have the same promise.

Old H_Z weights are: private-base rows 4; clause-basis rows 22; variable rows `10 occ(v)<=40`.
After repetition they are at most 120.  X weights are 4 or 2.  A plane meets at most six local
connectors and a constant number of name connectors; `occ(v)<=4`.  Adding two inner rows and at most
four H_Z coordinate incidences gives qubit Tanner degree at most 20 (a deliberately loose bound).
All sizes and degrees are therefore polynomial/bounded as stated.

## 9. What the Proposition-5 and K4 attacks now say

The reviewer's `n=16` construction has four L-cosets plus two transverse V-cosets.  The sum of the
four u-pairs is in `S_X` although no pairwise equality holds.  `verify.py` reconstructs it, checks
CSS, cap, `d_X=4`, the four-term membership, and all six pairwise nonmemberships.  This relation is
fully admitted: it corresponds to a vector in `ker A` and does not contradict formal pair
separation.  The proof never invokes Proposition 5(2)'s “only” or Proposition 5(3)'s “exactly”.

The old K4/transitive-clique branch is also not reused as the SAT mechanism.  A fixed four-plane
rank-metric K4 is included only as the malformed-input NO object; exhaustive `3^4` checking finds
zero schedules.  The SAT reduction instead uses named pair partitions plus the formal quotient.
Thus the K4 obstruction is attacked, retained where true, and bypassed rather than silently recycled.

## 10. Exact residual blocking the full fixed-d claim

No lemma here proves that the singleton increasing-support orders of the **main H_Z checks** have
`d_eff^Z>=3`, nor that any other bounded list of their orders does.  Static `d_Z>=3` is insufficient:
two Z-hook columns can still sum to a nontrivial Z logical.  The old proposed shortcut
`W=6,d_Z>=7` is unavailable; the reviewed pair count forces weight at least 10 in the original
COPY/NEGATE layout, and this package's honest bound after repetition is 120.

Therefore Theorem R64-X cannot be promoted to Eff-Preserve NP-hardness.  The exact remaining premise
is:

> For every constructed `R_3(C_0(F))`, exhibit from a uniformly bounded per-H_Z-check order list a
> Z-order tuple with no one- or two-fault nontrivial Z mechanism, independent of F; or replace
> `R_3` by a different inert-sector transform with the same X quotient, static distance at least 3,
> bounded generators/degrees, and a proved Z schedule.

The one concrete different next action is to formulate the repetition block's Z hooks under the
block-constant quotient and test/prove a **block-contiguous lifted-row order lemma**.  If its two-hook
images do not remain threefold repeats, abandon COPY/NEGATE sparsification and seek a chain-complex
inert-sector product; do not return to random cap placement or Proposition 5.

Pending fresh review, estimated survival probability of Theorem R64-X is `0.75`; estimated probability
that the full fixed-d claim closes via the remaining Z premise is `0.25` (scheduler prior was `0.20`).
These are planning estimates, not evidence.

## 11. Verification and limits

Run:

```
python3 verify.py
```

The sealed run used Python 3.9.6 and passed 164 assertions.  It independently checks the two gadget
relations, deterministic dimensions, CSS commutation, cap, every actual/formal pair partition in a
one-clause reduction, connector auxiliary uniqueness, repetition commutation, exact companion
distances and schedule, the Proposition-5 counterexample, and the K4 NO control.  These finite checks
corroborate the lemmas; no universal proof above depends on brute-force agreement.

Known limitations: no Stim compiler cross-check; no effective-Z theorem; no claim about `d_circ`;
no optional T; no arbitrary conflict graph; no weight-6 result; no promotion license.

## 12. Disk bindings, stale conflicts, and FIX-2

Repository HEAD at sealing: `e40a7ac40972ad5186018797efa390a8e3f784f0`.  Current canonical node
file hashes: fixed-d `40544563337197c618722f882ac2427db46065f84bf491bcda728533711481ac`;
upper `47260df53e4491c86e10f6ccdebadf47b1161d2533339fd9c499f389a8eb2321`;
root `e5fa3667bd9dec3b36f808f927156bd060a8ffcc35ea918ff5e1d353cf558b6a`;
islands `25196ae04048e64f5db785c06ebaee8768704c6b60de6aa5ae17dc57b436396a`.
Exact claim hashes are fixed-d `7adfe7c8356f6151e0da203826f9868cb414f193a4dfd5d63721b20e900e91cf`,
upper `1c2b9d0fed28591066e3fccba2578b00d179535a0aba048d1423b0397cee32b1`,
and root `0d9572ec3c4b58be6c824c1445c8bb6c3db76736a73aea9111d5c39586984c60`.
`SOURCE_BINDINGS.txt` lists every other bound byte hash.

The duplicate current artifacts under top-level `artifacts/` agree byte-for-byte with the canonical
`circdist/artifacts/` / `circdist/reviews/` copies checked here.  In contrast, all four corresponding
`research/circdist/proof-dag/nodes/` files differ from the current canonical nodes; they are stale
legacy conflicts and were not used.  Disk-current canonical `circdist/` wins.

FIX-2 accounting: work was strict serial; no subagent, detached job, background process, compute
handoff, or repository-external worker was used.  One foreground exploratory exhaustive scan was
interrupted cleanly with Ctrl-C before packaging.  A final process probe found no round-64 worker
after excluding the probe shell itself.  The repository was already dirty on entry; its status-list
hash was `c4152c4df421abc0728ce2b2892c1262a704c71d272e8685080a2e0eb8f6a918`.
This task wrote only this one sealed package directory inside the repository and did not edit any
canonical node, scheduler, protocol, prior artifact, tool, or generated view.
