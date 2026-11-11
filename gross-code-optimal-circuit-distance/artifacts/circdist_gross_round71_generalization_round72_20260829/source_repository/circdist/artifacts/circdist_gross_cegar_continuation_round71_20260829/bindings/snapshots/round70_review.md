# Round 70 independent exact review of the Gross block-minimization package

**Date:** 2026-08-29
**Reviewed package:** circdist/artifacts/circdist_gross_block_minimization_round69_20260829/
**Frozen node:** circdist/proof-dag/nodes/CIRCDIST.gross.yaml
**Single verdict:** **CLEAR-PROPOSER-LEVEL-CONTINUATION**

## Finding R70-VERDICT

The sealed round-69 package is clear to be linked as **proposer-level canonical
evidence**, and its sealed dynamic state is clear for a **strict continuation at
outer iteration 6 with exactly 6,212 installed sound blocks**. This clearance is
limited to the positive-witness facts proved below. It does not prove an absence
statement, enter arbitrary-round repair, exhaust the outer schedule space,
decide \(D^*_{\rm Gross}\), or license a node, route, or Gross-level change. The
exact interval remains

\[
                    D^*_{\rm Gross}\in\{11,12\}.
\]

No soundness, DIMACS-encoding, assignment, raw-physical-replay, manifest, or
proof-checker defect was found. Two non-defects must remain visible:

1. The author verifier with the live repository binding correctly rejects the
   later scheduler because it is byte-different from its sealed round-69
   snapshot. An independent 526-file binding audit shows that this is the only
   live drift and that it is exactly the round-69 settlement/round-70
   authorization.
2. A clean-room Z3 construction serializes equivalent assertions with different
   internal let-sharing names. The raw SMT-LIB bytes therefore differ, while
   all six parsed, ordered assertion lists are structurally identical. The
   schedules and every asserted constraint were also checked directly over
   integers, so this review makes no byte-equality claim for independently
   created SMT-LIB.

## 1. Review boundary and independence

I acted as a fresh, adversarial reviewer and did not contact the round-69
author, use a sub-agent, or import any proposer Python module into the
clean-room checker. I read DAG_PROTOCOL.md, FILE_PROTOCOL.md, the complete
current scheduler, the frozen Gross problem statement in
circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md, the complete current Gross
node, every source file in this package, and every physical/compressed member.
No AGENTS.md exists in this repository.

The real repository was read-only until this report was written. I did not edit
a canonical node, route, protocol, scheduler, generated view, existing review,
existing artifact, or the sealed package. I made no commit and no push. All
independent programs, virtual environments, candidate installations, logs,
decompressions, and solver outputs lived below
/tmp/circdist_round70_exact_review_20260829/ and are required to be deleted
after the final audit.

The trusted computational base is explicit: CPython 3.9.6, ordinary finite
integer/XOR/enumeration operations, SHA-256, PyYAML for repository validation,
Z3 5.1.0.0 for the outer-formula parse/structure check, the sealed CaDiCaL,
drat-trim, and lrat-check binaries for their named jobs, and the frozen Gross
incidences. This review is a finite computational certificate review, not a
Lean formalization of the enumerations and not a proof of the runtime or hash
function.

## 2. Package, compression, payload, and source seals

### 2.1 Every physical and compressed member

The package contains exactly 250 regular files occupying 19,557,352 physical
bytes. SHA256SUMS.txt contains 249 unique package-relative entries and its own
SHA-256 is

~~~text
aad4434050b1b64d3907b990e8279a2b25b2b4e29abcebf585fb885f3dbab647
~~~

Direct shasum checks passed:

| manifest | entries | result |
|---|---:|---|
| root SHA256SUMS.txt | 249 | PASS |
| PAYLOAD_SHA256SUMS.txt | 233 | PASS |
| tooling/SHA256SUMS.txt | 9 | PASS |

The 17 root-manifest files intentionally outside the payload manifest are the
final audit/process scans, root/payload manifests, repository inventory,
evidence-closure and proof-DAG logs/run records, final quick/full verification
logs/run records, and final seal/environment records. This exact set was
compared to the package inventory.

I read every byte of all 250 files. All JSON, JSONL, CSV, CNF, SMT-LIB,
Markdown, source, and text files were parsed or line-scanned as appropriate;
opaque executables were fully read and hashed. All 110 deterministic gzip
members were decompressed and read, representing 182,544,758 uncompressed
bytes, with gzip mtime zero and compressed/uncompressed sizes and hashes
matching COMPRESSED_INVENTORY.json.

The two source archives were independently traversed member by member:

| archive | members | regular members | regular bytes |
|---|---:|---:|---:|
| CaDiCaL 1.9.5 source | 438 | 427 | 2,690,784 |
| drat-trim source | 47 | 45 | 7,778,519 |

The all-file reader was 226 lines of independent code, SHA-256
3604990421e5039abdd74b8871ff45aac185dc3a7013701b9117f754b2bb661c.
Its result JSON has SHA-256
f8c34ef9564c0be31b7b8d0f91dc06ee606d7bb41be6d8e6c646dea629853093.
The physical-file, gzip-member, and tar-member record files had SHA-256 values
99010b33970d500537d318edcdaaeb159f1caa6b9a26b8c111df47cd8adfd53e,
8a56d5d5b2e48c329be937c286a00b37a7fc77d8f22d8f0babf0b52d6a43c11c,
and ac5a120ceb6fc5280d0297b01882e31bdafed242137efffe3dc4be359d10764b.

### 2.2 Source bindings and the one expected live drift

SOURCE_BINDINGS.json has 50 records expanding to 526 live files. I compared
each path directly and separately checked all five offline snapshots. The
frozen problem statement, current Gross node, both protocols, the complete
round-62/63/68 packages, and every mathematical source are byte-identical to
their sealed bindings. The sole live difference is:

| path | sealed | live |
|---|---|---|
| operations/circdist/SCHEDULER.yaml | 146,928 bytes; 6f3758de7781baa43d233b9c2009fb5c156bab289ae5853a92c902e205bf8530 | 150,126 bytes; 867a6765f6eb87dfb05caedec654d2ae1504496c5237ab061e0851bb042741d3 |

The complete 166-line unified diff, SHA-256
a3c5a67e2c81b7ec7550504213148f40e7c2dba8ac776ff5432672d884884187,
contains only expected bookkeeping and authorization:

- total sessions \(95\to96\), spent sessions \(94\to95\);
- settlement of round 69 as MATERIAL-CHECKED-PROGRESS-NOT-CLOSED, including
  the sealed counts and unchanged \(\{11,12\}\) interval;
- replacement of the finished authoring action by the round-70 independent
  review gate;
- insertion of the pending/unspent round-70 authorization and review
  requirements.

It changes no frozen mathematical object. The independent binding program has
SHA-256
020554e605ee2c7910141bd81fcdca71a8fb946a6af5817a0d0f11bfbf26cbf5;
its result has SHA-256
889a4b47ae805e2adefa07d48c2abdd8a5c7fdf9233baa80e6265f8922e4e3d5.

The sealed package's repository baseline excludes the future package and has
3,012 files, 88,762,997 bytes, and tree SHA-256
90845c573452f495d79e28d7748cb0fd0be01725542c2b7652cdf67aeffa96a7.
An independent present-tree recomputation, still excluding the package, has
the same 3,012 paths, no additions or removals, and exactly one changed file:
the scheduler above. Its current size is 88,766,195 bytes and tree SHA-256
f0db307779f908fb5d0a22face89de0faa24afee07278f9a4cda081606f496a1.

## 3. Author verifier: exact result

A clean virtual environment installed the package's exact requirements:
NumPy 2.0.2, python-sat 1.9.dev15, six 1.17.0, and z3-solver 5.1.0.0.
Every long-running command used a foreground process group with an external
hard limit; the wrapper has SHA-256
8bdf5c8a552f87d28441c0933cedbd8a0fce489b6f9bacc7fc51bd1025557b60.

The commissioned live-binding invocation was run exactly:

~~~text
<clean-python> verify.py --repo-root <repo>
~~~

It exited 1 after 0.624 seconds under a 360-second hard limit, at the explicit
assertion for operations/circdist/SCHEDULER.yaml. It did not time out. This is
the expected consequence of the post-seal scheduler transition just proved to
be the only drift; I do not relabel this invocation as a PASS.

The sealed/offline full invocation

~~~text
<clean-python> verify.py
~~~

exited 0 after 119.693 seconds under the same 360-second hard limit. It reported
status PASS, verdict MATERIAL-CHECKED-PROGRESS-NOT-CLOSED, 249 manifest entries,
110 gzip members, all classification/CEGAR checks, and valid/corrupt checker
controls. The independent work below, rather than that verdict text, is the
basis of this review.

## 4. Clean-room model reconstruction

The independent checker is 478 lines/36,796 bytes, imports no proposer module,
and has SHA-256
eb2e80f5d52d0d22aacf0dc2a8f42f863e281017855f5950bb14dcba2552a5be.
Its result JSON has SHA-256
e0c751e88fd0d0855ac6a3a91180cd0ea18edc76c003e8d014e331eb1f9a9ff6.
The passing run took 59.640 external seconds (56.957 seconds measured inside)
under a 480-second hard limit.

### 4.1 Incidence geometry and quotient

I rebuilt the checks from the finite group
\(G=\mathbb Z_{12}\times\mathbb Z_6\), with 72 coordinates in each of two
halves and \(n=144\). With

\[
A=((3,0),(0,1),(0,2)),\qquad
B=((0,3),(1,0),(2,0)),
\]

the X check at \(g\) is the sorted support
\((g+A)\cup(72+g+B)\), and the Z check is
\((g-B)\cup(72+g-A)\). This independently gives:

- 72 X checks and 72 Z checks, each of weight 6;
- 864 distinct check/data incidences;
- 648 nonempty X/Z check overlaps, every one of size 2;
- \(\operatorname{rank} H_X=\operatorname{rank} H_Z=66\);
- \(144-66-66=12\) encoded logical dimensions.

The weight-12 seeds were translated through all 72 group elements, deduplicated,
filtered against the same-sector row span, and checked against the opposite
syndrome. Both sectors independently contain exactly 1,884 nontrivial
weight-12 logical supports. Greedy quotient bases have 12 vectors, and their
cross-sector logical-pairing matrix has rank 12.

### 4.2 Candidate-specific direct columns

For a fixed schedule and sector, I regenerated all 360 direct columns:

- 144 singleton data columns;
- for each of 72 checks, three residual columns, hence \(72\cdot3=216\).

For an ordered check row \(o=(q_0,\ldots,q_5)\), the three canonical residual
index sets are

\[
R_0=\{0,1\},\quad R_1=\{3,4,5\},\quad R_2=\{4,5\},
\]

while the physical suffix sets are

\[
\widehat R_0=\{2,3,4,5\},\quad
\widehat R_1=\{3,4,5\},\quad
\widehat R_2=\{4,5\}.
\]

For every column the canonical and physical forms have the same opposite
syndrome and the same 12-bit logical quotient. For a selected set \(S\) of at
most ten columns I computed

\[
v=\bigtriangleup_{j\in S}c_j,\qquad
\widehat v=\bigtriangleup_{j\in S}\widehat c_j
\]

and required both syndromes to vanish, both supports to lie outside the
same-sector stabilizer span, at least one logical parity to be one, and the two
logical-parity vectors to agree.

## 5. Exhaustive local and pair classification

### 5.1 All 23 local catalogs

For every one of the 23 participating sector/check pairs, I generated all 720
permutations of the frozen six-qubit row in Python permutation order. I
recomputed the three residual supports, physical suffixes, opposite syndromes,
logical quotients, and unary completion status for every record: 16,560 local
records total.

Every catalog has exactly 360 unary-bad and 360 unary-good orders. For every
unary-bad record, the retained logical \(V\) and nine singleton columns \(D\)
satisfy

\[
R_1\triangle D=V,\quad |D|=9,\quad
\operatorname{syn}(V)=0,\quad [V]\ne0,
\]

and the physical suffix replay is likewise zero-syndrome and nontrivial. This
is 8,280 raw unary replays, not a sample.

I also rebuilt the inherited round-63 unary library from first principles. For
each of 144 checks and each of its ten bad three-subsets, an exhaustive search
over the nine exact suffix comparisons finds a five-atom antecedent that covers
all and only bad orders:

| property | exact count |
|---|---:|
| inherited unary clauses | 1,440 |
| local order cases checked | 103,680 |
| atom-deletion controls | 7,200 |
| bad/good orders per check | 360 / 360 |

The rebuilt sector-summary SHA-256 is
fa890f58f5fdf657b87bf75d0e2c12c45b41f943e8d2d1afa50f473dc2eb1f23,
equal to the sealed object.

### 5.2 All 15,552,000 pair cells and all physical configurations

The twelve round-68 source mechanisms induce 30 unique sector/check pairs. I
visited every cell in all \(30\cdot720^2=15,552,000\) pair matrices.

For a configuration
\((k_a,r_a,k_b,r_b,V,D)\), I required

\[
V=r_a\triangle r_b\triangle D,\qquad
|S_{\rm faults}|=2+|D|\le10,
\]

zero opposite syndrome, a nonzero 12-bit logical quotient, and equality of the
canonical and physical quotient. I independently rebuilt and raw-replayed all
3,368 retained configurations:

| source | configurations |
|---|---:|
| weight-12 logical pool | 3,347 |
| direct weight-14 completion | 21 |
| total | 3,368 |

For every unary-good/unary-good certified cell, the checker scans the two
ordered residual triples and assigns the first matching explicit configuration.
It assigns exactly 1,197,120 concrete tuple witnesses. The deterministic
tuple-selector stream has SHA-256

~~~text
bf023520379991fa597fba786d0505ccd71c85bd1f89f957298cefbbc65cdaed
~~~

matching the seal.

Define \(R_{a,b}\) to contain a tuple if the first order has a raw-verified
unary mechanism, the second order has one, or the pair has one of the
raw-verified two-residual configurations above. The sealed row bitsets equal
this independently constructed conservative positive relation. The historical
field name truth_rows_hex is safe only with this definition; it is not a
globally complete truth table for mechanism absence.

### 5.3 Every generalized antecedent and every covered tuple

A comparison atom is \(t(e_a(q))<t(e_a(r))\). A retained antecedent \(T\)
factors into order sets \(A_T\) and \(B_T\). The load-bearing condition is

\[
                         A_T\times B_T\subseteq R_{a,b}.             \tag{1}
\]

I regenerated the order masks for every atom, every term, and both checks. I
then iterated every tuple in every rectangle, not a sample, and checked (1)
against the independently built relation. There are 56,539,296
antecedent-tuple incidences. Each such tuple has either one of the 8,280
raw-replayed unary completions or one of the 1,197,120 explicit configuration
assignments whose underlying configuration was raw-replayed above.

The exact retained library is:

| atoms in antecedent | terms |
|---:|---:|
| 4 | 8 |
| 6 | 52 |
| 7 | 1,088 |
| 8 | 1,416 |
| 9 | 1,092 |
| 10 | 920 |
| 11 | 104 |
| 12 | 60 |
| **total** | **4,740** |

The atom total is 40,180. For each atom, the sealed deletion control supplies
an exact pair of order IDs. I removed the atom, checked that the exposed tuple
satisfies every remaining atom, and checked that it lies outside
\(R_{a,b}\). All 40,180 controls pass.

This proves **library-relative deletion minimality only**. It does not prove
that an exposed tuple has no other physical mechanism.

### 5.4 Public soundness derivation

If a legal schedule satisfies \(T\), its two local orders lie in
\(A_T\times B_T\). By (1), the tuple has a retained positive witness. The
witness's direct columns depend only on those local orders. The raw replay
supplies at most ten faults, zero syndrome, and a nontrivial logical quotient.
Hence that schedule has a direct-360 mechanism of weight at most ten. The outer
clause \(\neg T\) therefore excludes only schedules already known to fail the
distance-at-least-11 target. This proof uses no negative solver observation and
no assumption that the positive library is complete.

## 6. Adversarial attacks on overgeneralization

### 6.1 A concrete weight-12-only counterexample

I constructed a retained cell that would be lost if the library were described
as weight-12-only:

~~~text
sector       Xerr
checks       a=2, b=8
order ids    36, 180
a order      [3,20,80,4,77,86]
b order      [10,83,86,9,26,92]
~~~

Both local orders are unary-good, and none of their nine residual-pair choices
has a retained weight-12 pool completion. Configuration 33 is nevertheless a
valid direct weight-14 completion:

~~~text
a residual       {4,77,86}, kind 1
b residual       {9,26,92}, kind 1
singletons       {0,8,15,17,74,75,76,81}
logical support  {0,4,8,9,15,17,26,74,75,76,77,81,86,92}
fault count      10
logical parity   [0,1,1,0,1,1,0,0,0,0,1,1]
~~~

The canonical and physical nets are zero-syndrome and nontrivial. Across all
pair relations, 14,352 retained good-good cells rely exclusively on a
weight-14 configuration. The proposition “the generalized library is
weight-12-only” is false.

### 6.2 The 2,704 negative weight-14 observations

The X query ledger reports 1,800 candidates, 15 positive and 1,785 negative.
The Z ledger reports 925 candidates, 6 positive and 919 negative. Thus
\(1,785+919=2,704\) solver-negative observations. There is no corresponding
candidate-specific DRAT or LRAT set in the classification directory, and the
positive-library proof never consumes these observations.

They prove no absence, no completeness of the positive relation, and no right
to weaken a clause beyond its explicit rectangle proof. The 21 positive
weight-14 completions are load-bearing because their mechanisms are explicitly
replayed; the 2,704 negative observations are not.

### 6.3 Installed-library accounting

I rebuilt every retained family and checked every candidate's own block-count
dictionary:

\[
  1,440\ {\rm unary}
  +20\ {\rm round62}
  +4,740\ {\rm generalized}
  +12\ {\rm dynamic}
  =6,212.
\]

The round-62 package contributes 20 raw-replayed blocks and all
\(\binom{20}{2}=190\) prior-block exclusions replay. The round-63 validation
object records 15,874 exploratory pair-pattern clauses (8,159 X and 7,715 Z),
but every round-69 candidate installs exactly zero of them. No prose may turn
that exploratory count into a retained constraint family.

## 7. Six outer iterations

### 7.1 Formula and schedule legality

For each edge \(e\), the outer integer variable satisfies \(0\le t_e<864\).
The independently rebuilt constraints are:

1. six distinct times within each check;
2. six distinct incident times at every data qubit;
3. for every one of the 648 two-qubit X/Z overlaps \(\{q,r\}\),
   \[
   (t_{Z,b,q}<t_{X,a,q})\iff(t_{Z,b,r}<t_{X,a,r});
   \]
4. overlapping X and Z time ranges, ruling out a globally sector-serial
   schedule;
5. the negation of every installed positive-witness antecedent.

Six separate foreground Python processes independently reconstructed the outer
formulae. A direct integer replay checked that each stored model has all 864
required edges exactly once, integer times in range, a compressed layer set,
all check/data conflicts absent, all 648 measurement-consistency equalities,
true X/Z global interleaving, and every installed antecedent false:

| iter | blocks | assertions | layers | schedule SHA-256 |
|---:|---:|---:|---:|---|
| 0 | 6,200 | 10,598 | 125 | c8da557fa5f6470cb40fd0d0f48008a02add7b02f1e434b8d608fa64a69dd209 |
| 1 | 6,202 | 10,600 | 128 | 3de87c3ab911752591a51c9cb61c0ab3a472a2162470f8f248419881dde13d0d |
| 2 | 6,204 | 10,602 | 123 | 05131a24589c1ed96fbdb9455ff4f0e1ba2d9a6bc8ca13f40f3a6f76eac12446 |
| 3 | 6,206 | 10,604 | 131 | 3a1248b695865680e354f54a02c2ce49cfb5d9574875df099c99bb6e49178083 |
| 4 | 6,208 | 10,606 | 133 | c6fde2e505b528bc86deba59d9bad8a68a5e63a8c29cf469ba4bb35d62303dc4 |
| 5 | 6,210 | 10,608 | 118 | 81d6d668f8f1c0a56822402ddc7fff167df266babe220f448a31b87ee675fa6b |

### 7.2 Independent SMT serialization caveat

Raw independent/stored SMT-LIB hashes differ because Z3 chooses different
internal sharing names when the same ASTs are constructed in a different
process history. I parsed both serializations through Z3 and compared every
ordered assertion with structural AST equality. All six lists are identical:

| iter | stored SMT-LIB SHA-256 | normalized ordered assertions SHA-256 |
|---:|---|---|
| 0 | dc1a89f6f89ed62808d6486bc3c05a260ad610dc8d5f209ae2d014ff63bd25d4 | 6e620e0c04f4dd4dc68660fbe8f25c695186cec09e5e29aeecb3ba9db36c43cf |
| 1 | 3c284a78e5853ba351e0bd17d499dfefdcb6b0c768d0bf917f41377514e3f517 | 2ac3b067237c9019080227878a561693dadaa4a187b81ec69d1f26762f987ebf |
| 2 | 6d5b138a68e8265f6f7dc55153dadfcc3e5951b98477b6007766f17c9225fbfe | 5c67c6e3beebcd04c698f755d7929565c517cf20bbba3483e87a6efdf4d3cb6e |
| 3 | a6e14b4e2a48292ea32b433f8c92a2bb61e73670936cbe72b3e665f6eae49832 | 556a7e8766ab513ec0ed6002b8d660a103f6847774e1b8d6f3c9e52570372842 |
| 4 | 91f6388c957e728ef2f838796ae8291bdc592a1ca65cbfaa6cc1e61b378c2c8c | 25a0756bcb3b35a44016ff204cd5af146fcb8c4081f90b1589cf8a6fa2cd741a |
| 5 | 7a916516e566d6ed8058fd318a6fee1fdd99ef746a82ab7a59af6fb4ee85319c | 21c761515220642f7ca60d68b16285694c6bc623b000155bbfba405e399a762c |

The independently assembled block core has SHA-256
a6f610f6e7356b9959391041e427c9f368f194bf0a3ef54bddec3c3f4d5ae52b.

## 8. Twelve complete direct-360 formulae and SAT replays

### 8.1 Exact CNF construction

For each candidate and sector I rebuilt, without proposer code, all five
artifacts: DIMACS, variable dictionary, clause dictionary, column dictionary,
and formula summary. Every artifact is byte-identical to its sealed gzip
member.

The primary variables are exactly \(x_0,\ldots,x_{359}\), selecting any of the
360 candidate-specific columns. The formula imposes:

- 72 exact syndrome XOR equations, each terminal value zero;
- 12 exact logical-parity XOR outputs;
- one disjunction requiring at least one logical output;
- an exact prefix-threshold recurrence for
  \(\sum_{j=0}^{359}x_j\le10\).

Writing \(s_{i,j}\) for “the first \(i\) selections contain at least \(j\)
true variables”, the recurrence is

\[
s_{i,1}\leftrightarrow(s_{i-1,1}\lor x_i),\qquad
s_{i,j}\leftrightarrow(s_{i-1,j}\lor(s_{i-1,j-1}\land x_i)),
\]

with base/impossible-threshold clauses and
\(\neg s_{i-1,10}\lor\neg x_i\). An independent exhaustive control over all
64 assignments for \(n=6,k=3\) accepted exactly the 42 assignments of weight at
most 3 and rejected the other 22.

Both 1,884-word logical pools and their hashes are bound in each candidate, but
the CNF has **no pool-selection restriction**. It also has no
residual-pattern, check-count, or within-check order-family restriction. The
direct query is the complete 360-column query stated in the package.

### 8.2 Full assignments, every clause, and physical replay

All twelve solver runs exited 10 (SATISFIABLE) without timeout. I parsed every
literal of each complete assignment, required exactly one value for every CNF
variable, evaluated every clause, rebuilt the selected primary columns, and
replayed the canonical and physical mechanisms.

| iter | sector | variables | clauses checked | selected faults | DIMACS SHA-256 |
|---:|---|---:|---:|---:|---|
| 0 | Xerr | 5,953 | 22,392 | 10 | 5ecd22290e16e92bc6bf99496c6626a0f3ef93325f6999e47152167dad35b776 |
| 0 | Zerr | 5,973 | 22,472 | 10 | 46f1d78dcbe73e9a8c6cdf7b14bcab0e35cab840dd8c81b6cd3dd071b4ef1585 |
| 1 | Xerr | 5,962 | 22,428 | 10 | bdcb5c7deac2f52e1119e51ba3d900b068740056da4310900ffb549ec468a104 |
| 1 | Zerr | 5,965 | 22,440 | 10 | 917f8b456da62073fbdacd33ccdfb7c4fb30f30f6f2e2cfc2527106681b37c44 |
| 2 | Xerr | 5,964 | 22,436 | 10 | 2b6699d912dbf2e6b9d337a30e11f7600cb58993a4bfdcf7162f507467f2dde9 |
| 2 | Zerr | 5,975 | 22,480 | 10 | 65cb1ab65204662ee987bedaec42b3a5c380ba633b7fb18819bdf8e0e1b5c092 |
| 3 | Xerr | 5,958 | 22,412 | 7 | f5a6c3d3a4731152811b0431980b4254cf364165112369f885064977a8ef93b8 |
| 3 | Zerr | 5,947 | 22,368 | 10 | 356123aa27710c14cd6d057bfa51e9df9c40beb79ef38ef446b2744ac040f9d3 |
| 4 | Xerr | 5,991 | 22,544 | 10 | 7029a47bdcd2d727a74283574080bb414679980c98bfe1832be3c1ff0c5f1d1d |
| 4 | Zerr | 5,962 | 22,428 | 10 | aa1bf2590a591388f459f43fcd806e4fff483cc87ce4f84ba7ce8afe99841f5e |
| 5 | Xerr | 5,977 | 22,488 | 10 | 6df213aab2e724ca122737fa87cb6549f6ee29717b422861ba61ccc4567d329a |
| 5 | Zerr | 5,956 | 22,404 | 7 | c40a9cc2d86256c0ecc08604dd42110992d0ca7032b3554d867c68b5323f3958 |

This is 269,292 clause evaluations. Every selected mechanism has canonical and
physical zero syndrome, lies outside the stabilizer span, has a nonzero logical
parity vector, and reproduces the sealed exact comparison block. Each of the
twelve dynamic entries matches its candidate hash, sector, selected names,
fault count, mechanism hash, and antecedent. Thus all twelve new blocks are
sound by the same positive-witness theorem in section 5.4.

There are zero UNSAT sectors and zero candidate-specific absence proofs.
Arbitrary-round repair was correctly never entered.

### 8.3 Proof-checker controls

Using a fresh temporary LRAT output, I reran the four controls:

| control | exit | required marker | result |
|---|---:|---|---|
| valid DRAT | 0 | VERIFIED | PASS |
| truncated/corrupt DRAT | 1 | NOT VERIFIED | PASS |
| converted valid LRAT | 0 | VERIFIED | PASS |
| truncated/corrupt LRAT | 1 | NOT VERIFIED | PASS |

These controls validate the checker path. They do not create an absence proof
for any of the twelve SAT sectors. If a future sector is UNSAT, its exact CNF
must have an independently accepted candidate-specific DRAT and LRAT before any
absence language is allowed.

## 9. Claim boundary and rejected inferences

| proposed inference | adjudication |
|---|---|
| the 4,740 terms are sound positive-witness blocks | **accepted**, for their exact antecedents and frozen model |
| every atom is needed relative to the retained library | **accepted** |
| deletion controls prove global physical minimality | **rejected** |
| the library is weight-12-only | **rejected by the explicit \(a=2,b=8\) counterexample** |
| zeros in a pair row are proved mechanism-free | **rejected** |
| 2,704 negative weight-14 observations prove absence/completeness | **rejected** |
| the 15,874 exploratory round-63 pair clauses were installed | **rejected; installed count is exactly zero** |
| the six displayed outer candidates are legal SAT schedules | **accepted** |
| the six iterations exhaust the outer model | **rejected** |
| any direct sector is UNSAT | **rejected; all twelve are SAT** |
| the repair gate opens | **rejected** |
| \(D^*=11\) or \(D^*=12\) follows | **rejected** |
| Gross or a route level changes | **rejected** |

The package's strongest exact statement is
MATERIAL-CHECKED-PROGRESS-NOT-CLOSED.

## 10. Exact dispatcher installation and continuation license

### 10.1 Canonical evidence link

I tested this license in a disposable repository copy under /tmp. The candidate
kept the Gross claim, both routes, all prior events, and
assessment.level=CONJECTURED unchanged. It:

1. added the sealed package directory as kind run under the Gross assessment
   basis, with a note limiting it to positive-witness proposer-level progress;
2. added this report as kind review, locator Finding R70-VERDICT;
3. appended a summary sentence recording clearance for iteration 6/6,212 and
   explicitly denying absence, repair, exhaustion, \(D^*\) narrowing, and
   level change;
4. replaced only the stale dstar-residual frontier task text by the exact
   iteration-6 continuation boundary;
5. appended one review-completed event citing the package and this finding.

That disposable candidate passed prior-state retention, the 16-node circdist
validator, migration preservation, and evidence closure at 137 structured
paths. Running the generated-view refresh changed neither generated view
because graph topology, claim, and level did not change. Relative to the real
tree, the disposable installation differed only in the Gross node and the new
review path.

This is the complete substantive installation license. The dispatcher must not
change the claim, route premises/implications/proofs, assessment level, another
node, a protocol, the scheduler as part of this mathematical install, the
sealed package, or a prior artifact/review. No level-change event is licensed.

### 10.2 Strict continuation

The only licensed compute restart is:

~~~text
next outer iteration: 6
inherited unary blocks: 1,440
round-62 blocks: 20
round-69 generalized blocks: 4,740
sealed dynamic blocks: 12
total: 6,212
state: cegar/dynamic_blocks.json
~~~

Create all iteration-6 outputs outside the sealed package. Apply an external
foreground hard limit to the outer solve. If it is SAT, query both complete
direct-360 sectors even if the first is SAT, verify every assignment clause,
raw-replay each SAT mechanism, and only then append exact new blocks to a copied
dynamic state. If either sector is UNKNOWN, times out, or lacks an accepted
proof, stop without an absence verdict. If a sector is UNSAT, preserve its
complete formula and accept absence only after independent DRAT and LRAT
validation. Enter arbitrary-round repair only if both sectors of the same
candidate have accepted absence proofs. Do not mutate this package.

An outer UNSAT result would require a separate independently checked proof
appropriate to the complete SMT encoding before it could support outer
exhaustion or \(D^*=11\).

## 11. Repository validators and evidence closure

All commands below were read-only in the real repository and used
PYTHONDONTWRITEBYTECODE=1 where Python was involved:

| validation | result |
|---|---|
| proof_dag_check, circdist | PASS, 16/16 nodes |
| proof_dag_check, all | PASS, SE 85 + k-Sum 144 + circdist 16 = 245/245 |
| check_circdist_migration | PASS, 16 nodes / 143 original events / 728 byte-identical copies |
| duplicate-rejecting SafeLoader scan | PASS, 552/552 YAML files |
| release contract tests | PASS, 14/14 |
| DAG contract tests | PASS, 24/24 |
| Lean DAG selftest | PASS, 23/23 |
| append-only event check against HEAD | PASS |
| git diff --check | PASS |

Before this report existed, both circdist and all-project evidence-closure runs
exited 1 with exactly 249 errors. Every error was one physical file under the
unlinked round-69 directory except its specially ignored README.md. There was
no unrelated unlinked item. After this report is written but before dispatcher
installation, the exact expected real-tree result is those same 249 package
files plus this one intentionally unlinked review. Linking the package
directory and report as in section 10 makes closure pass, as the disposable
137-path check demonstrates.

The raw public-release audit was also run and exited 1. This is not an
installation validator for the present private working tree. Its 2,429
pre-existing findings were: 1 manifest digest mismatch, 2,040 unmanifested
files, 100 banned generated/session files, 149 machine-local paths, 104 private
identity matches, 30 session identifiers, and 5 credential-like strings. The
release-contract selftests above passed 14/14. No public-release waiver or
public-readiness claim is inferred, and this existing raw-tree condition is
not a defect of the round-69 package.

## 12. FIX-2 command, failure, timeout, and process ledger

All compute was serial and foreground. No detached job, worker pool, daemon, or
shell-background operator was used. The external wrapper started one process
group, waited in the foreground, and on a hard-limit breach would send SIGTERM
and then SIGKILL after five seconds. No command reached its hard limit, no
timeout kill occurred, and I manually interrupted no process.

The material command ledger is:

1. find and rg located policy, node, package, and validator inputs; chunked
   sed, cat, and Python reads covered the entire protocols, scheduler, problem
   statement, node, package documentation, code, and data.
2. Direct root, payload, and tooling shasum checks ran from their correct
   directories and exited 0.
3. The independent all-file/tar/gzip reader ran in /tmp. Two development runs
   exited 1 before the final pass: the first mistakenly excluded every basename
   SHA256SUMS.txt instead of only the root manifest; the second tried to parse
   an intentionally malformed CaDiCaL test CNF as a valid instance. Both were
   checker-construction errors, changed no package byte, and produced no
   mathematical verdict. The corrected run fully read and classified the
   fixtures and passed.
4. Python virtual-environment creation and clean requirements installation
   exited 0.
5. Full author live-binding verification ran with 360 seconds and exited 1 in
   0.624 seconds at the expected scheduler binding. Offline full verification
   ran with 360 seconds and exited 0 in 119.693 seconds.
6. The independent source-binding program compared 50 records/526 live files,
   five snapshots, and the scheduler unified diff; it exited 0 with exactly the
   one documented drift.
7. The first full clean-room run, under 480 seconds, exited 1 in 33.146 seconds
   because it demanded raw SMT-LIB byte equality. A diagnostic raw comparison
   also exited 1 and printed differing sizes/hashes. A first structural
   diagnostic exited 1 because it compared a solver assertion with a parsed
   stored wrapper equivalent to the assertion conjoined with true. Parsing both
   serializations before ordered structural comparison fixed the comparison.
   The diagnostic then passed, and the final full clean-room run exited 0 in
   59.640 seconds. These failed development assertions were not suppressed or
   counted as evidence.
8. The repository inventory, duplicate-key checker, DAG/evidence/migration,
   release/DAG/Lean selftests, append-only check, raw public-release audit, and
   whitespace check ran under 120- or 180-second limits with the exact outcomes
   in section 11.
9. A disposable copy under /tmp received the candidate Gross evidence links,
   review placeholder, summary/frontier text, and event. Its 120-second
   structural, previous-state, migration, evidence-closure, and generated-view
   commands all exited 0. No candidate byte was copied back.
10. Pre-report repository content was inventoried excluding this authorized
    path: 3,262 files, 108,323,547 bytes, aggregate SHA-256
    391f55867707b33e8dd2a018c5c05f1a70504a1a4f9d91ba6cff14d520cbcab3.
    A post-report comparison and final process/scratch scan are recorded below.

The independent helper hashes, sufficient to identify deleted scratch
programs, are:

| program | SHA-256 |
|---|---|
| hard-timeout runner | 8bdf5c8a552f87d28441c0933cedbd8a0fce489b6f9bacc7fc51bd1025557b60 |
| all-file reader | 3604990421e5039abdd74b8871ff45aac185dc3a7013701b9117f754b2bb661c |
| source-binding checker | 020554e605ee2c7910141bd81fcdca71a8fb946a6af5817a0d0f11bfbf26cbf5 |
| clean-room mathematical checker | eb2e80f5d52d0d22aacf0dc2a8f42f863e281017855f5950bb14dcba2552a5be |
| package-excluding inventory checker | c995b612486365207733978bfa14c59458172327462d1f5d9af92020ad764ccb |
| duplicate-YAML checker | 96c4e11569199f6372ef0ee130f52401677b1f4cf780e1c6f985db8afd461e2c |
| candidate-link installer | ac7c21620e81ee009c1be6702a2b811ce639b3a780762e7435131075465af22a |
| session inventory checker | 3b1003863b8c8ef192a638140fdc5ba512b0d6a72c28763a7192167b5d9e1425 |

## 13. Final boundary

**Verdict: CLEAR-PROPOSER-LEVEL-CONTINUATION.**

The exact licensed advancement is evidence linkage plus strict iteration-6
continuation from 6,212 blocks. The exact prohibited advancement is any
absence, repair, outer-exhaustion, \(D^*\), route-level, or Gross-level claim.

## 14. Post-write preservation and cleanup

After this report was present, I recomputed the repository inventory while
excluding only this authorized path. It is byte-for-byte equal to the
pre-report inventory: 3,262 files, 108,323,547 bytes, aggregate SHA-256
391f55867707b33e8dd2a018c5c05f1a70504a1a4f9d91ba6cff14d520cbcab3,
with zero added, removed, or changed paths. Thus the repository mutation made
by this reviewer is exactly this one new review.

The post-write all-project DAG check again passed 245/245, migration again
passed 16/143/728, duplicate-YAML again passed 552/552, release contracts
again passed 14/14, DAG contracts again passed 24/24, Lean selftest again
passed 23/23, and the whitespace command exited 0. Evidence closure produced
exactly 250 expected errors: 249 files in the still-unlinked package plus this
review, with zero unrelated items. The tested canonical link in section 10
removes precisely those expected items.

Before cleanup, an OS process scan found zero matching verifier, clean-room,
CaDiCaL, DRAT, LRAT, candidate-builder, classifier, or hard-timeout processes.
The complete scratch directory, virtual environment, candidate repository,
programs, logs, and temporary proof were then deleted. A final scan found the
scratch path absent, an empty matching /tmp glob, and zero matching OS
processes. No command timed out, no process was detached, and no compute
remains.
