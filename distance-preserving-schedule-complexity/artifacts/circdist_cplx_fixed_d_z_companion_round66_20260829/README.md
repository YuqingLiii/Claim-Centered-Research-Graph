# CIRCDIST round 66: the private-sentinel effective-Z theorem

## 0. Verdict, scope, and epistemic ceiling

**Final verdict: `FULL-FIXED-D-THEOREM-READY-FOR-FRESH-REVIEW`.**

This is a proposer-level package.  It changes no canonical claim, node, route, scheduler, protocol,
review, index, or earlier artifact.  It does not call itself an independent review.  Its positive
claim is licensed only for one fresh exact review under `DISPATCHER_LICENSE.txt`.

The package closes the exact no-inheritance boundary recorded by the round-65 review: it composes
the independently cleared restricted X-EFF3 reduction with a new **private-sentinel Z decoration**
whose emitted singleton Z orders have no nontrivial one- or two-fault Z mechanism.  The result is a
full fixed-`d` Eff-Preserve NP-completeness theorem at static distance exactly three.  This would
settle `CIRCDIST.cplx.fixed-d` if a fresh reviewer accepts it.  It does **not** settle
`CIRCDIST.cplx`, whose `CIRCDIST.cplx.sigma2` premise remains open.

The proposed automatic block-contiguous order lemma is false for the canonical increasing order.
The smallest nonempty source instance already supplies a raw counterexample.  A different random
block order happens to be safe on that finite instance, so this package does not misstate the
counterexample as an impossibility result for every block order.  Instead it proves an exact
block-order equivalence, identifies the old prefix-CSP obstruction, and bypasses it.

No private hidden chain of thought is offered or claimed.  The durable mathematical objects are the
definitions, identities, case splits, certificates, code, and logs below.

## 1. Exact theorem bindings

`THEOREM.txt`, after deleting its one terminal LF, contains exactly 999 characters and has SHA-256

```text
49cf956fe5afa49caa8707f15fd157ab27fedadc79c56bdec0a57c0a89a0e184
```

Its exact text is:

> Eff-Preserve in the frozen single-ancilla terminal-residual V1 model is the promise problem whose instance supplies a CSS pair (H_X,H_Z), explicit allowed local CNOT-order lists, the ordinary qubit-sharing conflict relation, no optional depth bound T, and promises full static distance exactly 3; it asks whether an allowed schedule M has d_eff(M)=3. This problem is NP-complete under total promise-preserving polynomial-time many-one reductions even when d_X=4, d_Z=3, every X generator has weight at most 4, every Z generator has weight at most 486, every qubit has CSS Tanner degree at most 20, the only nonsingleton order domains are the core-plane X checks inherited from the reviewed restricted X-EFF3 construction and each contains exactly three explicit orders, every other X-order domain is singleton, every Z-order domain is a singleton explicitly emitted private-sentinel order, and there are no artificial conflict edges; global serial execution realizes every allowed local-order tuple.

`LICENSED_X_THEOREM.txt`, under the same no-terminal-LF convention, contains exactly 883 characters
and has the independently cleared hash

```text
01cf8fd10f48db13e23a09f884eb24b0b17c860c121c336c324123ff222594c0.
```

The unchanged full fixed-`d` node claim has exact hash

```text
7adfe7c8356f6151e0da203826f9868cb414f193a4dfd5d63721b20e900e91cf.
```

The theorem above is stronger in constants and semantics than the node's qualitative restriction
clause.  The file hashes and exact dependencies read for this derivation are in
`SOURCE_BINDINGS.txt`.

## 2. Frozen model and algebraic notation

All vector spaces are over `F_2`.  A binary vector and its support are identified.  For a CSS pair
on `n` data qubits, put

```text
S_X = row(H_X),                N_X = ker(H_Z),
S_Z = row(H_Z),                N_Z = ker(H_X),
L_X = N_X \ S_X,               L_Z = N_Z \ S_Z.
```

The static sector distances are the minimum Hamming weights in `L_X` and `L_Z`; the full static
distance is their minimum.  `H_X H_Z^T=0` ensures `S_X subset N_X` and `S_Z subset N_Z`.

For a check with support order `(q_1,...,q_w)`, a single ancilla fault after CNOT `i` propagates to
the proper suffix

```text
T_i = e_{q_{i+1}} + ... + e_{q_w},       1 <= i <= w-1.
```

The preparation residual is the full support and is a stabilizer.  A data Pauli contributes a data
column `e_q`; a measurement flip contributes no terminal data residual.  At the CNOT with `q_i`, a
joint ancilla/data Pauli can contribute `T_i`, `e_{q_i}`, or
`T_i+e_{q_i}=T_{i-1}`.  Thus data columns and all proper suffixes exhaust the terminal columns in
that sector.  Because `T_i + P_i` is the check row, where

```text
P_i = e_{q_1} + ... + e_{q_i},
```

suffix and prefix represent the same class modulo the sector stabilizers.  The checker uses
prefixes to keep all calculations deterministic, while `COUNTEREXAMPLE.json` prints the physical
suffixes too.

A sector mechanism of size `t` is a multiset of `t` terminal columns whose sum is in `L_X` or
`L_Z`.  Repeated identical locations can be cancelled in a minimum.  The frozen terminal-residual
V1 bridge gives

```text
d_eff(M) = min(d_eff^X(M), d_eff^Z(M)).
```

At target `d=3`, safety therefore means absence of every nontrivial logical made by one or two
columns in both sectors.  Static distance three only excludes sums of one or two *data* columns; it
does not exclude two long hooks.

## 3. What is imported from the independently cleared X theorem

The proof takes the exact 883-character X theorem as a reviewed premise, with its binding
`F-NO-INHERITANCE` boundary.  The parts used here are the following.

1. There is a total promise-preserving Karp map `K_X` from Tovey `(3,4)-SAT`.  Malformed encodings
   map to a fixed `R_3(K4-NO) direct-sum G_neq3` NO object; a valid zero-clause encoding maps to the
   companion `G_neq3`; a valid nonempty formula `F` maps to
   `R_3(C_0(F)) direct-sum G_neq3`.
2. `C_0(F)` uses 16 private-base four-qubit planes per clause.  Core X checks select one of three
   pair classes.  Fixed connector checks implement the reviewed COPY/NEGATE formal-label
   partitions.  Deterministic basis tags give `64m` qubits, CSS commutation, a cap, and
   `d_X(C_0)=4`.
3. The repetition transform replaces old qubit `q` by `(q,0),(q,1),(q,2)`, puts each old X row on
   copy zero, adds `(q,0)+(q,1)` and `(q,0)+(q,2)`, and repeats every old Z row on all three copies.
   It preserves `d_X=4` and multiplies the main component's `d_Z` by three.
4. The fixed 12-qubit companion has exact `(d_X,d_Z,k)=(4,3,2)`.  Hence every branch of `K_X` has
   `d_X=4`, `d_Z=3`, and full static distance exactly three.
5. X-check weight is at most four, old Z-check weight at most 120, and total CSS Tanner degree at
   most 20.  Only the Boolean-carrying core checks have three orders; every other X order is fixed.
6. For an old weight-four X check, only its middle weight-two hook can participate in a two-fault
   X mechanism.  Equality of middle-hook syndromes together with inequality modulo `S_X` is the
   exact conflict.  The deterministic construction is X-safe exactly when the source formula is
   satisfiable.  There is no `T` and no artificial conflict edge.

For completeness, the repetition identities used later can be checked without the reviewed gadget
argument.  Let `pi:F_2^(3n)->F_2^n` take the parity of each three-copy block, and let `lift_0` put an
old vector on copy zero.  Direct substitution gives

```text
ker(H_Z^R) = pi^(-1)(ker H_Z),
S_X^R      = ker(pi) + lift_0(S_X),
ker(H_X^R) = {R(z): z in ker H_X},
S_Z^R      = {R(z): z in S_Z}.                     (3.1)
```

The first quotient has the same minimum weight as the old X quotient; the second has weights
multiplied by three.  The `2n` independent inner X rows meet `lift_0(S_X)` trivially, so

```text
rank(H_X^R)=rank(H_X)+2n,  rank(H_Z^R)=rank(H_Z),  k(R_3 C)=k(C).  (3.2)
```

The fixed companion is also completely explicit (digits denote qubit supports):

```text
X: 0123, 4567, 148(10), 068(11), 379(10)
Z: 12479, 0167(10), 012389, 0145(11), 02468(11), 4567(10)(11), 89(10)(11).
```

Its X and Z ranks are both five, so `k=12-5-5=2`; exact enumeration gives `d_X=4,d_Z=3`, with
representatives `[0,1,4,5]` and `[0,1,8]`.  Direct-sum normalizers and stabilizers split by
component, so direct-sum distances are the componentwise minima.

The review correctly refused to infer full Eff-Preserve hardness: no safe effective-Z order had
been proved for the main repeated Z rows.  Sections 4--11 supply exactly that missing theorem while
preserving every X object above.

## 4. Every hook of a block-contiguous lifted Z row

Let an old Z generator `z` have an explicit old-qubit order

```text
pi(z) = (q_1,...,q_W).
```

Write `R(v)` for the threefold repeat of an old vector and
`A_t=e_{q_1}+...+e_{q_t}`, with `A_0=0`.  The explicit block-contiguous lifted order is

```text
(q_1,0),(q_1,1),(q_1,2), (q_2,0),(q_2,1),(q_2,2), ...,
(q_W,0),(q_W,1),(q_W,2).                              (BC)
```

Every proper lifted prefix, and therefore every suffix-hook class, occurs at a unique cut
`k=3t+r`, where `0 <= t <= W-1` and `r in {0,1,2}` (with the obvious proper-cut endpoints).  Its
exact vector is

```text
r=0:  R(A_t),
r=1:  R(A_t) + e_(q_{t+1},0),
r=2:  R(A_t) + e_(q_{t+1},0) + e_(q_{t+1},1).         (4.1)
```

For a general fixed copy order inside a block, replace the final singleton/doubleton by the first
one/two elements of that copy order.  Thus (4.1) is a formula for every hook of every main lifted
row, not a sampling statement.

The two inner X checks of old qubit `q` measure the marker syndrome

```text
delta_q(x_0,x_1,x_2) = (x_0+x_1, x_0+x_2).           (4.2)
```

For (BC), the within-block terms in (4.1) have syndromes `(1,1)` and `(0,1)`; an exact block
boundary has syndrome zero.  More generally, `delta_q(J)=delta_q(J')` iff the copy subsets `J,J'`
are equal or complementary, because `ker(delta_q)=span{(1,1,1)}`.

Consequences:

* A single lifted hook can be undetected only at an exact block boundary.  It is then `R(A_t)`, and
  it is a nontrivial Z logical exactly when `A_t` is a nontrivial old Z logical.
* Two partial hooks can cancel inner syndromes only at the same old qubit.  Their within-block XOR
  is zero or `(1,1,1)`, so their total becomes the repeat of the XOR of two old boundary prefixes,
  with one boundary moved across that shared qubit in the complementary case.
* A hook plus the data column at its current CNOT is the adjacent hook, exactly as in Section 2.
* Two exact-boundary hooks are simply the repeat of the sum of their two old boundary prefixes.

Define `B(pi)` to contain all proper old boundary prefixes for every emitted old Z row, adjoining
`0`, the full row (a stabilizer), and data columns only to express adjacent boundaries.  The bullets
give both directions of the following statement.

**Block-contiguous equivalence lemma.**  A block-contiguous lifted tuple is Z-safe through two
faults iff `B(pi)` contains no one-column or two-column nontrivial old Z mechanism.  Every unsafe
lifted pair projects to such an old boundary pair; every unsafe old boundary pair lifts at exact
block cuts.  Partial cuts and hook-plus-data events add only adjacent boundaries.

This is the exact algebraic outcome of the proposed lemma attack.  Repetition does not create the
desired safety; it transports an old Z-prefix scheduling CSP.

## 5. Smallest source-family counterexample and exact obstruction

Take the one-clause positive formula

```text
(x_0 OR x_1 OR x_2).
```

It is the smallest valid nonempty source instance: `(3,4)-SAT` clauses have three distinct
variables, and the zero-clause branch emits only the fixed companion.  `C_0` has `n=64`, 37 X rows,
and 21 Z rows.  Under increasing old block order:

```text
Z row 0 = [5,7,9,11,13,15,17,19,21,23],  cut after 8 old blocks;
Z row 9 = [16,17,18,19],                    cut after 2 old blocks.
```

The two physical lifted suffix hooks are the threefold repeats of `[21,23]` and `[18,19]`.  Their
sum is

```text
R(v),  where v = [18,19,21,23].
```

Direct multiplication gives `H_X v=0`.  Row reduction of old `H_Z` has pivots

```text
[0,1,2,4,5,8,12,16,20,24,25,28,32,36,40,44,45,48,52,56,60],
```

and reduces `v` to the same nonzero support `[18,19,21,23]`.  Therefore `v` is a nontrivial old Z
logical and `R(v)` is a nontrivial lifted Z logical.  Two faults suffice.  In gate coordinates the
cuts are 24 and 6.  The checker logs a weight-24 prefix representative because it quotients each
physical suffix by its full lifted Z row; `COUNTEREXAMPLE.json` prints both physical suffixes, both
prefixes, their XORs, the complete 37-by-64 and 21-by-64 row supports, syndromes, pivots, and
remainders.

The obstruction is not visible inside one row support.  Exact restricted-normalizer linear algebra
on this instance gives:

```text
each of 21 single Z-row supports:  quotient dimension 0;
210 unordered unions of two row supports: 14 have positive quotient dimension.
```

For example, rows 0 and 3 have restricted-normalizer dimension 4, stabilizer-intersection dimension
2, and quotient dimension 2; `[5,7,9,10,14,15]` is one nontrivial witness.  Rows 0 and 9 have
quotient dimension 1 and contain the obstruction used above.  The exact algebraic failure of the
support-only argument is therefore

```text
ker(H_X restricted to supp(z_r) union supp(z_s))
    is strictly larger than
S_Z intersect F_2^(supp(z_r) union supp(z_s)).
```

As a guard against overclaiming, `random.Random(0)` produces a block-contiguous tuple that passes
the exact one/two-column audit on this one finite formula.  Thus the canonical increasing-order
lemma is refuted, and a universal support-local proof is refuted, but no all-orders counterexample
is claimed.  The existential block-order question is an old-prefix CSP and remains unproved.  The
positive theorem below does not depend on it.

## 6. The private-sentinel transform `D_Z`

Let `C=(H_X,H_Z)` be any emitted branch of the reviewed map, including its companion.  Apply the
following construction separately to **every emitted Z generator** `z_r`, including dependent rows
if an implementation emits any.  Put `W_r=wt(z_r)` and `L_r=W_r+2`.  Allocate `L_r` disjoint,
row-private triples

```text
B_(r,j) = (a_(r,j), b_(r,j), c_(r,j)),    0 <= j < L_r.
```

For each triple add the two X generators and one Z generator

```text
u_(r,j) = a_(r,j)+b_(r,j),
v_(r,j) = a_(r,j)+c_(r,j),
g_(r,j) = a_(r,j)+b_(r,j)+c_(r,j).       (6.1)
```

Replace the emitted row `z_r` by

```text
tilde(z_r) = z_r + sum_j g_(r,j),         (6.2)
```

and retain every `g_(r,j)` as a separate Z generator.  Old X generators and old qubits are
unchanged.  Marker families for different source rows are disjoint.  This is `D_Z(C)`.

### 6.1 CSS commutation

Old X rows commute with (6.2) because they commute with `z_r` and miss every marker.  Each of the
two marker X rows overlaps both its `g_(r,j)` and `tilde(z_r)` in exactly two qubits; it misses all
other Z rows.  Hence every new intersection is even and `D_Z(C)` is CSS.

### 6.2 Row spaces, ranks, dimension, and logical quotients

The row operation

```text
tilde(z_r) + sum_j g_(r,j) = z_r          (6.3)
```

shows that the new CSS pair is row-space equivalent to the old pair direct-summed with `L=sum L_r`
copies of the trivial `[[3,0]]` repetition block generated by `(ab,ac;abc)`.  If the old ranks are
`rho_X,rho_Z`, then

```text
n'     = n + 3L,
rho_X' = rho_X + 2L,
rho_Z' = rho_Z + L,
k'     = n' - rho_X' - rho_Z' = k.        (6.4)
```

These identities do not assume that the emitted old rows are independent.

On one marker triple,

```text
ker[abc] = span{ab,ac},       ker[ab;ac] = span{abc}.
```

Consequently the X normalizer/stabilizer quotient and the Z normalizer/stabilizer quotient of
`D_Z(C)` are canonically the corresponding old quotients: every marker normalizer component is a
marker stabilizer.  Stabilizer reduction removes markers without changing the old support.  Thus

```text
d_X(D_Z(C)) = d_X(C),          d_Z(D_Z(C)) = d_Z(C).  (6.5)
```

For every reviewed branch these are exactly 4 and 3, so the full static distance remains exactly
3.  The companion's old weight-three Z logical `[0,1,8]` persists and later supplies the upper
bound `d_eff <= 3` using three ordinary data faults.

## 7. Explicit singleton Z orders

Let the old data support of `z_r`, in increasing emitted-qubit order, be

```text
(d_0,...,d_(W-1)),            L=W+2.
```

The sole allowed order of the decorated row is

```text
a_0, a_1,
a_2,d_0, a_3,d_1, ..., a_(W+1),d_(W-1),
b_0,c_0, b_1,c_1, ..., b_(L-1),c_(L-1).  (7.1)
```

The sole order of each marker row is

```text
a_j,b_j,c_j.                                   (7.2)
```

Every support element occurs once.  The decorated row has weight and order length

```text
W+3(W+2)=4W+6,
```

and the marker row has weight three.  The lists are emitted literally; there is no oracle,
per-instance search, random seed, or existential choice in the Z sector.

## 8. Marker-path lemma

For a Z vector on one marker triple define its two-bit inner-X syndrome

```text
kappa(x) = (x_a+x_b, x_a+x_c).
```

Write `alpha=(1,1)`, `beta=(0,1)`, and `gamma=(1,0)`, the syndromes of `a`, `c`, and `b`.  Track the
full direct sum of these two-bit states along every proper prefix of (7.1).

* Opening `a_j` changes block `j` from zero to `alpha`.
* The immediately following old data gate changes no marker state.
* Closing `b_j` changes `alpha` to `beta`; closing `c_j` changes `beta` to zero.

The path first opens blocks 0 and 1, then opens one fresh block immediately before each old data
gate, and finally closes blocks in order.  Therefore:

**M1.** Every proper decorated prefix has nonzero marker syndrome.

**M2.** Two distinct proper prefixes of the same decorated row have equal marker syndrome iff they
are the two cuts immediately after `a_(i+2)` and after the following `d_i`.  Their old-data XOR is
the singleton `e_(d_i)`.

**M3.** A proper decorated prefix has marker syndrome supported in exactly one block only (i) just
after the first gate `a_0`, when its old projection is zero, or (ii) in the last block near the end
of closing, when its old projection is the full stabilizer `z_r`.  Its nonzero state is `alpha` or
`beta`, never `gamma`.

M1 follows because the last `c_(L-1)` is not a proper-prefix cut.  For M2, the set of open `alpha`
blocks grows strictly except across a data gate, then the ordered `alpha -> beta -> 0` closing path
changes at every gate and cannot equal an opening state.  For M3, after `a_1` at least two blocks
are nonzero until closing has reached the penultimate `c`; all old data gates have already occurred
in the latter phase.  This proves the lemma for all `W`, not just for tested row weights.

The two proper prefixes of a marker-row order (7.2) have states `alpha` and `beta`.  Marker data
columns have states `alpha`, `gamma`, and `beta`.  Two vectors on one marker block have equal
`kappa` iff their XOR is zero or `g_j`.

## 9. Exhaustive one- and two-fault Z classification

Work modulo the new Z stabilizer space.  Full-support preparation residuals are Z stabilizers and
may be deleted.  Measurement flips have zero data residual.  Section 2 shows that a joint CNOT
hook-plus-data residual is an adjacent prefix already included below.  The remaining terminal
columns fall into four types:

```text
D_o: old data singleton;
D_m: marker data singleton;
G:   a proper marker-row hook;
R:   a proper decorated-row hook.
```

### 9.1 One column

An `R` column is detected by M1.  A `D_m` or `G` column has nonzero marker syndrome unless it is a
full marker stabilizer.  An old data singleton cannot be a nontrivial Z logical because old
`d_Z=3`.  Hence there is no one-fault Z mechanism.

### 9.2 Two columns containing two decorated hooks

If the two `R` columns belong to different source rows, their nonzero marker syndromes lie in
disjoint private families and cannot cancel.  If they belong to the same row, cancellation requires
equal marker states.  By M2 their XOR has old projection exactly one data singleton and zero marker
projection.  It is detected or a stabilizer, but cannot be a nontrivial logical because `d_Z=3`.

### 9.3 One decorated hook and one old data column

The old data column has zero marker syndrome, while M1 gives the decorated hook nonzero marker
syndrome.  Their sum is detected.

### 9.4 One decorated hook and one marker-only column

A marker-only column is supported in one marker block.  Cancellation is possible only when the
decorated marker syndrome is confined to that same block.  M3 says the decorated old projection is
then either zero or the full old Z generator `z_r`.  Equal marker syndromes make the combined
marker vector a sum of `g_(r,j)` stabilizers, including already closed full triples.  The remaining
old vector is `0` or `z_r`, also a stabilizer by (6.3).  Thus every undetected pair of this type is
trivial.

### 9.5 No decorated hook

Two nonstabilizer marker-only columns from different blocks have disjoint nonzero syndromes.  In one
block, equal syndromes make their XOR `0` or `g_j`, a stabilizer.  A marker-only column cannot cancel
an old data column.  Two old data columns have physical weight at most two and cannot represent a
nontrivial logical at static `d_Z=3`.

The cases are exhaustive.  Therefore the fixed Z tuple (7.1)--(7.2) has

```text
d_eff^Z >= 3.                                    (9.1)
```

The preserved companion logical `[0,1,8]` is the sum of three `D_o` columns, so in fact

```text
d_eff^Z = 3.                                     (9.2)
```

This proof is uniform in the source formula, source-row overlap, row dependence, and old Z-row
order.  It uses only old static `d_Z=3`, private marker families, and the explicitly emitted path.

## 10. Preservation of the reviewed X theorem

For an old-qubit X residual `x`, its syndrome under a decorated Z row is exactly its old syndrome
under `z_r`; its syndrome under every marker Z row is zero.  Hence, on all old X terminal values,

```text
new-syndrome equality  iff  old-syndrome equality.   (10.1)
```

The X stabilizer quotient embeds unchanged because the new marker X stabilizers are disjoint from
old qubits.  Thus old quotient-class equality and inequality are also unchanged.  Every old core,
connector, repetition-inner, companion check, and every old allowed X order is emitted byte-for-byte
at the matrix/order level.

New marker X generators have weight two and singleton orders.  Modulo their full row, their only
proper hook is a singleton.  Any two-fault X candidate involving such a singleton and an old
reduced hook has an X representative of weight at most three.  Since (6.5) gives new `d_X=4`, it is
not a nontrivial X logical.  Candidates using two new singletons have weight at most two.  Therefore

```text
an old X-order tuple is X-safe in C
    iff its unique singleton extension is X-safe in D_Z(C).  (10.2)
```

This proves preservation, not inheritance by assertion.  The checker independently compares both
directions of the syndrome and quotient partitions for every old data value and every proper subset
of every old X row on the one-clause instance.

## 11. Static parameters and absolute structural constants

Before decoration the reviewed output has

```text
d_X=4, d_Z=3;  max X weight=4; max Z weight=120; max Tanner degree=20.
```

Equations (6.4)--(6.5) preserve `k,d_X,d_Z`.  A decorated Z row has weight at most
`4*120+6=486`; a marker Z row has weight three; a new X row has weight two.  Old-qubit incidences
are unchanged.  A marker `a` qubit meets two X rows and two Z rows, while `b` and `c` meet one X row
and two Z rows.  Their total degrees are at most four.  Therefore the global Tanner bound remains
20.

For a valid nonempty source with `m` clauses and `V<=3m` used variables, `C_0` has `64m` qubits and
`D=V+18m<=21m` emitted Z rows.  Each old column has Z incidence at most four, so after repetition
the main Z-incidence sum is at most `768m`.  The companion contributes 37 incidences and seven rows.
Thus

```text
L_total = sum_r(W_r+2) <= 768m+37 + 2(21m+7) = 810m+51.
```

At most `2430m+153` marker qubits are added.  The sparse matrix, generator list, and all local order
lists have linear total size; a dense encoding is still polynomial.  Every local order length is
at most 486, and every order domain has cardinality one or three exactly as stated in the theorem.
The malformed and empty branches are constant size.  Every loop has an explicit finite bound, so
the transform is total.

Only ordinary qubit-sharing conflicts are present.  For any allowed tuple, execute complete check
circuits one at a time in emitted order.  This is a legal global serial execution, so no optional
depth `T`, edge coloring, or artificial conflict edge is hidden in the local-order semantics.

## 12. Final total Karp reduction, both directions

Define the target map

```text
K(F) = D_Z(K_X(F)).                              (12.1)
```

The reviewed parser and all three branches of `K_X` are retained.  Section 11 makes `D_Z`
deterministic and polynomial.  Sections 6 and 11 prove that every output satisfies the promise
`d_X=4,d_Z=3`, hence full static distance exactly three, and satisfies every advertised structural
bound.

**Completeness.**  If a valid source formula is satisfiable, the reviewed theorem supplies an old
X-order tuple with `d_eff^X>=3`.  Extend it by all singleton marker-X orders and by the unique Z
tuple (7.1)--(7.2).  Equation (10.2) gives X safety and Section 9 gives Z safety.  Sector splitting
then gives `d_eff>=3`; the static weight-three companion logical, realized by three data faults,
gives `d_eff<=3`.  Hence the target answer is YES.  The valid empty formula uses the reviewed safe
companion tuple and the same argument.

**Soundness.**  If a valid nonempty formula is unsatisfiable, the reviewed theorem says no old
X-order tuple is safe.  Every target tuple restricts to one old X tuple, and (10.1)--(10.2) preserve
its nontrivial one/two-fault X mechanism.  Therefore no target tuple can have `d_eff=3`; the answer
is NO.  A malformed source maps to the reviewed fixed K4 NO branch, whose unsafe X mechanism is
preserved identically.  Thus all strings, including malformed encodings, are mapped in the correct
direction and into the promise.

NP-hardness follows.  NP membership is the fixed-`d` specialization of the current PROVED
`CIRCDIST.cplx.upper` certificate/fault-enumeration theorem, bound to exact 301-character claim hash

```text
1c2b9d0fed28591066e3fccba2578b00d179535a0aba048d1423b0397cee32b1.
```

Together these prove the exact 999-character theorem, at proposer level pending fresh review.

## 13. Reproducible checker and negative controls

All code is Python 3.9+ standard library only and imports no repository module.  `construction.py`
is the exact clean-room builder from the sealed round-64 package.  `z_companion.py` implements
`R_3`, `D_Z`, ranks, quotient canonicalization, emitted orders, the marker path audit, and an exact
one/two-column audit.  `make_counterexample.py` emits the raw JSON certificate.  `verify.py` rebuilds
and checks it.

From this directory run:

```text
PYTHONDONTWRITEBYTECODE=1 python3 make_counterexample.py > /tmp/counterexample.rebuilt.json
cmp COUNTEREXAMPLE.json /tmp/counterexample.rebuilt.json
PYTHONDONTWRITEBYTECODE=1 python3 verify.py > /tmp/verifier.replayed.json
cmp verifier_output.json /tmp/verifier.replayed.json
sha256sum -c SHA256SUMS.txt
```

The sealed author run uses Python 3.9.6 and records 20/20 PASS checks.  It includes:

* exact theorem and licensed-theorem length/hash checks;
* exact companion distances and logical witnesses;
* the one-clause increasing block-order failure and full raw certificate rebuild;
* the 21-single-row/210-pair restricted row-union audit with 14 obstructed pairs;
* a safe seed-0 block order, solely to prevent an all-orders overclaim;
* exact CSS/rank/`k` identities for one-clause, occurrence-four, and malformed branches;
* exact one/two-column Z audits over 5,218, 19,294, and 1,624 terminal columns;
* a one-clause old-X syndrome/quotient partition comparison over 582 values;
* the sharp 120-to-486 row-weight instance;
* the reviewed K4 `0/81` malformed-branch X negative control; and
* a real sentinel negative control: grouping all marker openings before companion-row-2 data gates
  makes two equal-marker hooks differ by the static logical `[0,1,8]`, and the audit rejects it.

Finite agreement corroborates the implementation.  It is not used to extrapolate M1--M3, the
fault case split, quotient preservation, or the Karp directions.

## 14. Limitations and review targets

1. The existential block-contiguous old-prefix CSP is not solved.  It is unnecessary because
   `D_Z` supplies fixed safe orders.
2. The constant 486 is deliberately loose and honest.  No weight-6 or weight-120 full theorem is
   claimed.
3. No theorem about `d_circ`, optional `T`, arbitrary conflict graphs, multi-round detector history,
   or a model other than the frozen terminal-residual V1 model is claimed.
4. The X theorem is used only at its exact independently reviewed hash.  If those bytes or the
   frozen model change, this composition must be reviewed again.
5. A fresh reviewer should attack M2/M3, the decorated-plus-marker case, joint CNOT hook/data
   coverage, old-X pair preservation, the total malformed branch, and the claim that the upper NP
   premise applies to these explicit lists.
6. No canonical promotion is authorized by this package.  Even a clean replay is not an
   independent proof review.

## 15. Package map and FIX-2

`MANIFEST.md` names every payload.  `ATTACK_LEDGER.md` records the public rejected-branch results.
`PROCESS_LEDGER.txt` declares the foreground process history and absence of detached compute.
`FINAL_AUDIT.txt` records the pre-seal repository/process/scratch audit.  `SHA256SUMS.txt` seals every
other payload; its own external digest is reported to the dispatcher.

This run used one mathematical worker and strict-serial verdict-bearing computation and mutation.
It spawned no subagent, background job, detached job, daemon, worker pool, or compute handoff.  Three
bounded tool batches ran independent read-only source-inspection shells concurrently; they were
awaited in the foreground, are disclosed in `PROCESS_LEDGER.txt`, and overlapped no computation or
write.  Every verdict-bearing output is preserved here.  Scratch was outside the repository and is
deleted after sealed replay.  The only repository write is this one package directory.
