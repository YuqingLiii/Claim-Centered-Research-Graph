# CIRCDIST.gross Round 89 proof-producing outer exact review

Date: 2026-08-30
Reviewer role: sole fresh independent Round-89 reviewer
Reviewed proposer package: `circdist/artifacts/circdist_gross_proof_outer_round88_20260830`
Canonical node under protection: `circdist/proof-dag/nodes/CIRCDIST.gross.yaml`

## Disposition

**Verdict: `CLEAR-PROPOSER-LEVEL-CONTINUATION`.**

The sealed Round-88 package is internally complete for the continuation claim it actually makes. I independently reconstructed the frozen Gross geometry, the finite rank-compression theorem, every source family, every one of the four Tseitin encodings, every complete outer SAT assignment, every direct-360 formula and assignment, all six physical fault mechanisms, and the three atomic selector-state transitions. I found no scientific defect.

This verdict has deliberately narrow force. It licenses only:

1. linking the exact sealed Round-88 package and this review as evidence;
2. recording that iterations 109, 110, and 111 were positive SAT continuation steps;
3. recording the six exact EFSSC semantic cuts produced by those positive witnesses; and
4. continuing from the checked, fresh, unstarted, and **unsolved** iteration-112 frontier stated below.

It does **not** prove a Gross UNSAT, direct-sector absence, repair success, outer exhaustion, a distance-12 schedule, or a universal distance-11 ceiling. It does not narrow the exact residual, promote a route, or promote the root. `CIRCDIST.gross` and its live `gap-via-lift` route remain `CONJECTURED`; the exact residual remains

\[
D^*_{\mathrm{Gross}}\in\{11,12\}.
\]

The package has one non-scientific reproducibility limitation: its shell replay defaults to a system `python3` that need not contain Z3/PySAT, while the recorded successful environment is an absolute, host-local virtual-environment path. `REPORT.md` line 143 gives the working override explicitly and `ENVIRONMENT.json` records the executable and versions. That is adequate to interpret and reproduce the package on this host, but it is a portability defect and an environment requirement, not a mathematical defect.

## Independence, scope, and audit record

I did not contact, query, or rely on the Round-88 proposer. I did not import any Round-88 compiler, checker, geometry module, direct-formula builder, or state-transition checker into my scientific audit. My reviewer-written checker reconstructed those objects from the frozen mathematical data and serialized evidence. Z3 5.1.0 was used only to parse the already reviewed Round-86 SMT-LIB and compare its AST to an independently constructed AST. The proposer replay was run later as corroboration, not as the basis of this verdict.

No private hidden reasoning is claimed or exposed. The definitions, equations, counts, truth tables, state equations, commands, attacks, and limitations needed to audit the result are written here.

Authorization and protected inputs at start were:

| object | observed SHA-256 |
|---|---|
| `operations/circdist/SCHEDULER.yaml` | `b808ab44bb96b751359548e568469812d3136e10ef91dcb25315389a61eaf957` |
| `circdist/proof-dag/nodes/CIRCDIST.gross.yaml` | `f42dd0333a8faea3858cefcd859c0343ab33aedf2a6a1e663f2fa1625701288e` |
| Round-87 exact review | `c37912c5446819ed74e1636049d313c72601dd6a8b1543db01b6b22b51a2f25c` |
| Round-86 root manifest | `94322390a648262e8cc035f8e843617f134fe2d29ff36191720b646c021c89ff` |
| Round-86 payload manifest | `443b84ce18c568bdd6b88c4737d03b222b518897eecab787ffa1cc43718f182b` |

The current scheduler authorizes exactly one fresh Round-89 review at score 2.375 and leaves the package unlinked pending this review. The live repository was already broadly dirty/untracked before this work; notably the protected scheduler and node themselves appeared as pre-existing untracked files. I therefore used hashes, package-relative manifests, and disposable overlays rather than treating `git status` as a clean baseline.

The main independent command was:

```text
/private/tmp/circdist-r72-dispatcher-venv/bin/python \
  /tmp/circdist_round89_20260830/independent_audit.py
```

It exited 0 with `status: PASS`, an empty stderr, and checker SHA-256 `194b9bd954247c26c2e31451e2521017ca2dbece289094abb03d18efe826cd49`. The checker and its output were scratch instruments and are not licensed evidence; their complete mathematical content is summarized below, and they were removed under the final cleanup rule.

## 1. Package identity, inventory, and seals

I enumerated files from the filesystem rather than trusting `FILE_INVENTORY.jsonl`.

| measurement | independent result |
|---|---:|
| regular files | 257 |
| symlinks | 0 |
| total bytes | 103,600,176 |
| inventory rows | 254 |
| root-manifest rows | 256 |
| payload-manifest rows | 255 |

The inventory excludes exactly its own file and the two top-level manifests. The root manifest excludes only itself. The payload manifest excludes both top-level manifests. Every recorded byte count, LF count, path, and SHA-256 matched its actual file. Every path set was unique and lexicographically sorted.

| sealed object | SHA-256 |
|---|---|
| `SHA256SUMS.txt` | `c4061caff46b632b5c4beb7b6eb33281f3520d07c4dfaaa6eb7c6a33883c7e20` |
| `PAYLOAD_SHA256SUMS.txt` | `d2de2f014954070f20bbba0e55caf49aed93b26986a63fab77955a75f62c8157` |
| `REPORT.md` | `b1549f0a9f1fd707220aeb28bff17af2ea90d282fd0f9e0f9a2cee5cc7c31f0a` |

The first manifest command I issued was from the repository root, although the manifest paths are package-relative; it failed by invocation error. Repeating it from the package root checked 256/256 root rows and 255/255 payload rows successfully. This was a reviewer command error, not a seal failure.

The accepted manifest contains the five nested manifest rows that the disclosed defective basename filter omitted:

```text
bindings/initial_state/SHA256SUMS.txt
bindings/round80/PAYLOAD_SHA256SUMS.txt
bindings/round80/SHA256SUMS.txt
bindings/round86/PAYLOAD_SHA256SUMS.txt
bindings/round86/SHA256SUMS.txt
```

All 26 gzip members have header mtime zero. Deterministic replay regenerated every CNF, source map, and definition trace byte-for-byte. Of 254 UTF-8-decodable payloads, only three retained DRAT tool logs contain carriage-return progress output; this is literal tool output, not nondeterministic semantic serialization.

The prelink evidence-closure command exited 1 with exactly 256 errors. Every error was under the new package prefix. The package's 257th file, `bindings/initial_state/circdist/proof-dag/README.md`, is ignored by the closure check. There were no unrelated prelink errors. After the licensed overlay links the package directory and review path, evidence closure exits 0 with 156 structured paths.

## 2. Finite rank compression theorem

### 2.1 Frozen event set

The frozen Gross geometry has 72 X checks and 72 Z checks, each incident on six data qubits. Let

\[
E=E_X\sqcup E_Z,
\qquad |E_X|=72\cdot6=432,
\qquad |E_Z|=432,
\qquad |E|=864.
\]

A schedule assigns an integer timestamp `t(e)` to every interaction `e in E`. The frozen constructor also enforces `0 <= t(e) < 864`; conflicts and all retained cuts depend on equality or strict order.

For any integer schedule, let its distinct used timestamps be

\[
U_t=\{u_0<u_1<\cdots<u_{k-1}\},\qquad k=|U_t|\le |E|=864,
\]

and define the ranked schedule

\[
\rho_t(e)=j\quad\Longleftrightarrow\quad t(e)=u_j.
\]

Equivalently,

\[
\rho_t(e)=|\{u\in U_t:u<t(e)\}|.
\]

Then for every pair `e,f in E`:

\[
t(e)=t(f)\iff \rho_t(e)=\rho_t(f),
\]

and

\[
t(e)<t(f)\iff \rho_t(e)<\rho_t(f).
\]

The forward directions follow from applying the strictly increasing index map `u_j -> j`. For reflection, equal ranks name the same unique member of `U_t`, and ordered indices name ordered members of `U_t`. The image is exactly `0,1,...,k-1`, so every ranked time is in `0..863`. This proves the complete bound because no schedule on 864 events can use more than 864 distinct timestamps. A schedule using 864 distinct timestamps reaches rank 863, so nine bits are insufficient; ten unsigned bits represent `0..1023` and are sufficient. The root `time < 864` removes the unused `864..1023` words.

The reverse semantic inclusion is immediate: every ten-bit assignment whose roots enforce `<864` is already an integer schedule in the frozen domain. Thus the finite formula neither loses an admissible order type nor creates one.

### 2.2 Predicate-by-predicate preservation and reflection

I searched the frozen Round-86 SMT-LIB AST and the four semantic sources for every operation on times. The only integer numerals in the normalized AST were `0,1,3,4,5,864`. The only arithmetic addition was the finite sum of five Boolean indicators used to compute a within-check rank. There was no multiplication, division, modulus, absolute value, time difference, gap bound, duration, parity of an absolute time, negative-time permission, or other arithmetic predicate.

Rank compression therefore preserves and reflects every relevant family:

- **Nonnegativity and upper bound.** Ranking produces nonnegative values below 864. These two absolute predicates are not order invariants in general, but the canonical ranked representative always satisfies them. The finite-to-frozen direction enforces them directly.
- **Ancilla and data conflicts.** Six incident interactions conflict exactly when their times must be pairwise unequal. Equality is preserved and reflected.
- **MC0.** For each of 648 X/Z overlaps on two qubits `q0,q1`, the condition is `(t_Z(q0)<t_X(q0)) iff (t_Z(q1)<t_X(q1))`. Both strict comparisons are preserved and reflected.
- **Extrema.** `xmin,xmax,zmin,zmax` are bounded against all 432 words in their sector and each must equal at least one sector word. Attainment pins each auxiliary to the true minimum or maximum, so no unconstrained absolute auxiliary remains. The two global roots are the negations of `xmax<zmin` and `zmax<xmin`.
- **Local order and inherited blocks.** Every retained atom is `t(x)<t(y)`; a block excludes a conjunction of such atoms.
- **Ranks.** For a six-body check and qubit `q`, strict serialization makes
  \[
  r_c(q)=\sum_{p\ne q}[t(c,p)<t(c,q)]\in\{0,1,2,3,4,5\}.
  \]
  All five summands are preserved and reflected, so the rank is preserved exactly.
- **Membership and EFSSC validity.** Membership tests only whether `r_c(q)` belongs to one of the fixed residual-position sets. Detector and logical signature parities then depend only on those memberships and fixed data supports.

For each of the three accepted outer models I also tested all `864^2 = 746,496` ordered edge pairs, not merely pairs that appear syntactically. Both `<` and `=` agreed between raw and compressed schedules for every pair.

## 3. Independent semantic-source extraction

### 3.1 Gross geometry and linear algebra

I rebuilt the bivariate-bicycle incidence from

```text
A = ((3,0),(0,1),(0,2))
B = ((0,3),(1,0),(2,0))
L = 12, M = 6
```

with 72 group elements and 144 data qubits. This produced exactly 72 six-body X rows, 72 six-body Z rows, 864 uniquely named interactions, six interactions incident on each data qubit, and 648 X/Z check overlaps, each on two qubits. These arrays matched every iter109–112 semantic source exactly.

From the frozen weight-12 input seeds I independently expanded both translation orbits, removed stabilizers by GF(2) row reduction, and obtained 1,884 nonstabilizer logical words in each sector, all of weight 12 and zero opposite syndrome. The load-bearing ranks are:

| matrix | GF(2) rank |
|---|---:|
| `H_X` | 66 |
| `H_Z` | 66 |
| rows `H_Z union L_Z` | 78 |
| rows `H_X union L_X` | 78 |
| 12x12 X/Z logical pairing | 12 |

For X errors, `ker(H_Z)` has dimension 78. Adding the twelve `L_Z` parity equations leaves a 66-dimensional kernel, exactly the rank-66 span of `H_X`; the Z sector is symmetric. Consequently, zero detector syndrome plus a nonzero stored logical-parity vector is exactly nonstabilizer status in the frozen CSS semantics.

### 3.2 The 14,484 inherited blocks

I regenerated the 1,440 unary blocks without importing the proposer generator. For every check and each of ten bad three-qubit suffixes, I enumerated all `6! = 720` local orders, formed the nine possible cross-boundary strict atoms, and searched increasing atom-set size. The first sound separating set always had five atoms. Each chosen antecedent contained only bad suffix orders and excluded every good order.

The remaining serialized sources were independently normalized to their exact atom pairs:

| family | count |
|---|---:|
| unary Round-63 | 1,440 |
| Round-62 | 20 |
| generalized | 12,820 |
| dynamic | 204 |
| **total** | **14,484** |

Their semantic-base object hashes were `62cabe5f2925fc0caadd340848ea439219c13dc3d397c67762f852d36b6560e2` (dynamic), `4547a39d560358ce24c1615f5db99f17735c717a2b10d67ad2cfac515731acf3` (generalized), `fff897136200a97d12ae1756ca07a8aadd10e80cf11e4cce8e7ba30f8e428600` (raw), and `b9816477e347ed095e26fd4a521be8a951e92e1b3aa66c668cd2fa315d652604` (registry). Family, family index, source ID, trace hash where present, and every ordered atom matched each of the four sources.

### 3.3 Exact iter109 correspondence

The Round-86 starting state is fresh/unstarted iteration 109 with 134 selectors and selector-state hash

```text
9be75eba643ac167d5c51497ca8e5cd23eb1656f803a49cbd8e7f1285b004113
```

Two Round-86 state rows use `iteration` rather than `source_iteration`; the normalized source field is the same provenance value. After that documented normalization, all 134 compact selector rows matched iter109 source rows exactly.

I independently constructed the full iter109 Z3 AST in the frozen assertion order and compared it node-for-node with `bindings/round86/formulas/final_outer.smt2`. Result: 19,016 assertions, zero structural differences, normalized AST SHA-256 `6ac624f2acb35a6311034829970b4d2993fcdf208080898a8e1dbeff1dcb3c7d`. An initial comparison produced 288 differences because Z3 5.1.0 retains a harmless historical list-form wrapper `(and (distinct ...) true)` on each Distinct assertion. Reproducing that serialization wrapper reduced the difference count to zero; no predicate changed.

### 3.4 Complete assertion and root-clause enumeration

The following table is the iter109 source order. Later iterations change only the selector count.

| source family | assertion rows | root clauses |
|---|---:|---:|
| unsigned nonnegative | 864 | 0 |
| `< 864` | 864 | 864 |
| X-check Distinct | 72 | 1,080 |
| Z-check Distinct | 72 | 1,080 |
| data-incidence Distinct | 144 | 2,160 |
| MC equivalence | 648 | 1,296 |
| extrema inequalities | 1,728 | 1,728 |
| extrema attained | 4 | 4 |
| global interleaving | 2 | 2 |
| reviewed block | 14,484 | 14,484 |
| EFSSC exclusion | 134 | 134 |
| **total iter109** | **19,016** | **22,832** |

A six-word Distinct row expands to 15 roots of the form `lt(a,b) or lt(b,a)`. Each MC equivalence expands to two roots. Each selector adds one source assertion and one root clause, hence iter110/111/112 have 19,018/19,020/19,022 assertions and 22,834/22,836/22,838 roots.

### 3.5 Source and companion hashes

The semantic hashes, compressed-file hashes, maps, traces, and metadata all cross-bind:

| iter | selector count | semantic payload | source.gz | map.gz | trace.gz | metadata |
|---:|---:|---|---|---|---|---|
| 109 | 134 | `71e20fff97a08edfd096359297455d822357323037c473f834e9b2a32d263b3c` | `56797727a0a5dcf45190b335bacfbe264b1800eb026553e7882c2a2ae68b1a86` | `fce42796e43f47b7219aa4dfbae84e0b60280c871ea288fca18a5c08454d9b0c` | `1ea683fb7337b3bc21f4219c3fae4f3bd1c40193cf9b5b93368ad0c08324d5fa` | `07ec112f4d816c3d40c854b3c7564a1379c29c6d447381b5110e230f256dfcbc` |
| 110 | 136 | `6138239dcff590bf8a56b045739cd0cebd3306f0a0c982cf19520fbe61d57596` | `ae8c918e28a486a3656ddb3f4e3179b57a175db841b1edef7d7b295ecc7c4eb4` | `2734c1105e46cd9f39710457b7a78a6663713e8d2d20010085e9eb6a1ebbf805` | `eee9ba1fa334729880737fa7faece983fe6c63721ef74f9e9e306128c480cd20` | `bf0f775d4aca358195311986095ebbef72169666de582c4d690093ceac139d72` |
| 111 | 138 | `aec6eb553749233ef31eb57f131006c3778170064099d586e6109f54bb08f31d` | `1f08d8461f665844d899a8a26f60020ef6a408b996eac5d9ced890ffd677691c` | `ef93e9319841134a910141f4941da3a15151740d6f742378e0ffb2d4311fc790` | `b66b2ff20fef55515f7fcd552ba652150d77b7af25b5795ca04311d4b21448b0` | `605553ec8a230946d7136ee4c654e5c96e9d9bcdcbe32528e3f34d16956b6d97` |
| 112 | 140 | `a816fa6a7aec4eb3502f4b5c1a8c50dc8d958b383a003a84738fcb7e630e7c43` | `3a906e7abb020a6ea3bd108b9ad80ed8170439687c95830b21a7d9d283ecf5f8` | `2a25419bd8ddd7bcc1fbb9616b77c35adba02a5ff6544e9d30035c677b25a8cf` | `4113d7937a23f720eb70b0f137399b738e91ff1f546c396aaa6ec0bf964cfedf` | `4474f4af8da03b10f65419dea8ed93e8f2eb83494de913361b1a5af0e3b27323` |

## 4. Independent Tseitin and DIMACS audit

### 4.1 Variables and primitive gates

The primary-variable set is exactly 8,680 variables: 864 ten-bit time words and four ten-bit extrema words. Every other variable is defined exactly once, every definition uses only earlier variables, and the union of primary and defined variables is exactly `1..nvars`.

Let `v` be a defined variable and literals `a,b` its inputs. I reconstructed these clauses independently:

```text
v <-> (a AND b): (-v a), (-v b), (v -a -b)
v <-> (a OR  b): (v -a), (v -b), (-v a b)
v <-> (a XOR b): (-a -b -v), (a b -v), (a -b v), (-a b v)
constant true T: (T)
```

All 24 assignments across the three binary gates and output were tested. For each ten-bit pair `x,y`, all 1,048,576 pairs, I independently evaluated both the comparator and equality circuit.

Bits are processed least-significant to most-significant. With `r[-1]=false`,

\[
r_i=(\neg x_i\land y_i)\lor((x_i=y_i)\land r_{i-1}).
\]

When processing bit `i`, a strict difference at that more significant bit overrides the already computed lower-bit result; equality carries the lower result. Thus `r_9` is exactly unsigned `x<y`. The exhaustive test confirmed the direction on every pair. Equality is the conjunction of the ten bitwise equivalences and was also exhaustive on every pair.

For a six-check rank membership, the five comparator literals encode whether each other qubit precedes the target. A `rank_membership` definition has 32 clauses, one for each five-bit row; its output is true exactly when the row's Hamming weight belongs to the requested position set. I tested both output values for every row, 64 cases per membership definition.

### 4.2 EFSSC circuit

For each sector, define an 84-bit fixed signature for qubit `q`:

\[
\sigma(q)=(\langle e_q,h_0\rangle,\ldots,\langle e_q,h_{71}\rangle,
            \langle e_q,\ell_0\rangle,\ldots,\langle e_q,\ell_{11}\rangle).
\]

The first 72 bits are detector parities and the last 12 are logical-dual parities. For a selector `s`, its signature under schedule `t` is

\[
\Sigma_s(t)=
\bigoplus_{q\in D_s}\sigma(q)
\oplus
\bigoplus_{(c,K)\in G_s}
\bigoplus_{q\in c:\ r_c(q)\in P(K)}\sigma(q),
\]

where

\[
P(\{k_1,\ldots,k_m\})=P_{k_1}\triangle\cdots\triangle P_{k_m},
\]

and `P0={0,1}`, `P1={3,4,5}`, `P2={4,5}`. The validity literal is

\[
V_s(t)=\left(\bigwedge_{j<72}\neg\Sigma_{s,j}(t)\right)
\land
\left(\bigvee_{72\le j<84}\Sigma_{s,j}(t)\right).
\]

The formula installs the single exact root `not V_s`. I independently reconstructed every cached rank, membership, XOR fold, detector-zero conjunction, logical-nonzero disjunction, and selector root. No selector is replaced by its source atom cube.

### 4.3 Complete clause accounting

| iter | variables | definitions | definition clauses | root clauses | total clauses | memberships | uncompressed CNF SHA-256 | compressed CNF SHA-256 |
|---:|---:|---:|---:|---:|---:|---:|---|---|
| 109 | 397,902 | 389,222 | 1,303,764 | 22,832 | 1,326,596 | 2,274 | `536c348ede8409ca5d691091213acbada828934a6be641da0fd3a80a62c9292f` | `61e6f4d3b58bfe997803b86cbd40fd873c9f3b00173e15664fde0738c0546beb` |
| 110 | 398,070 | 389,390 | 1,304,714 | 22,834 | 1,327,548 | 2,286 | `932c4b0f31bb010950bc9999269983c79bba4c3941b883031ca3c14693f8946d` | `284f53d1c634351cca87c3e5ec51e1965f5d3bfb5346b9797b370fab0368b7a5` |
| 111 | 398,235 | 389,555 | 1,305,651 | 22,836 | 1,328,487 | 2,298 | `f0255ef2232c572ae6cc0aa3a50ec76a7b5bef4a13fbc42ad1f342ecf6e5a8f0` | `1e2c269b77f0791e7e28cb751bb5a5aaa93628aae718527ec2a90ad309663a09` |
| 112 | 398,488 | 389,808 | 1,307,266 | 22,838 | 1,330,104 | 2,322 | `a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594` | `889e3cb12d3ffdbcb5ea5da3cb769c552f5649bce763428ac43ea471d4f16dd4` |

Every formula has 11,234 distinct cached strict comparisons, 1,728 word equalities, and 852 within-check rank expressions. I reconstructed the exact root in assertion order and the exact definition clauses at the clause IDs recorded in the trace. A 32-byte digest per expected clause was placed in an `nclauses`-entry array; every slot was filled once, and the resulting array equaled the actual DIMACS clause array. Thus the check covers literal sign, literal order, clause order, clause-ID partition, header, maximum variable, and byte hash.

### 4.4 Missing pinned-true unit

The accepted trace's first definition is

```json
{"var":1,"op":"constant_true","inputs":[],"clause_ids":[1]}
```

and all four accepted CNFs begin with `1 0`. Removing exactly that line and decrementing only the iter109 header clause count reproduces the disclosed rejected artifact byte-for-byte:

```text
variables: 397,902
clauses:   1,326,595
SHA-256:  30da99d6fb47966fb01bc8e2b26e89144dd54307bebcf07140cf03c74d038e13
```

Without `(T)`, simplifications that emit `T` or `-T` are not tied to Boolean truth, so this is a genuine compiler soundness failure. It was caught before solving, appears in no accepted formula set, and supports no verdict. The repaired accepted iter109 hash is `536c348e...c9292f`, not the rejected hash.

### 4.5 Reviewer negative controls

I ran five controls through independently written ingress checks, not through the proposer checker:

| mutation | rejection condition | result |
|---|---|---|
| change one selector residual kind in source | semantic-payload hash mismatch | rejected |
| change frozen upper bound 864 to 865 | semantic-payload mismatch; witness 864 is accepted only by the wrong bound | rejected |
| reverse the first retained strict-order atom | semantic-payload mismatch; witness `17<19` changes truth under reversal | rejected |
| flip first unit `1 0` to `-1 0` | required unit and complete CNF SHA mismatch | rejected |
| remove the final CNF clause | header/actual clause count and complete SHA mismatch | rejected |

An additional first attempt to corrupt a DRAT proof by flipping an arbitrary middle byte was **not** a sound negative control: the byte landed in a non-load-bearing deletion line, drat-trim warned and still verified the proof. I rejected that test design and replaced it with a syntactically corrupt prefix plus a separate half-truncation. Both were rejected. This failed attack is evidence that corruption controls must target semantics or syntax, not evidence against the accepted tool chain.

## 5. Iter109–111 complete outer SAT models

I parsed each solver log and compressed assignment independently. Each assigns every variable exactly once, agrees literal-for-literal with the solver log, sets `T=true`, and satisfies every DIMACS clause. Across the three models, 1,194,207 variable values and 3,982,631 clauses were checked.

| iter | assigned vars | clauses checked | assignment.gz SHA-256 | raw schedule SHA-256 | compressed schedule SHA-256 | layers/max |
|---:|---:|---:|---|---|---|---|
| 109 | 397,902 | 1,326,596 | `0a1e7730bb7bca7b06194711422d3dbb3a91f624461800751816c73f42134d19` | `84e3fa5aea3700051a4b7badcc2c394c2ab2cbf80f79bd5404745852e8a7d016` | `773832f5d01143a26a41b03481c2c6a21524590191c76e8a4d80af208a6b2efe` | 129 / 128 |
| 110 | 398,070 | 1,327,548 | `d3506090ce3ad869b49dfa06ff81616dc65b683bb21076b4d85b5dbfdaaf4ab5` | `bf4f750aa6167d17c1333f0300d1851bc4ebd75a7593a6aee32385dec0f36714` | `3e51e30e33a32697af935908eaa368409366dcd4bb334c2290b85a2c7ac47d46` | 136 / 135 |
| 111 | 398,235 | 1,328,487 | `2a5d051e52dcf04d3d2d405548b5544c3638f06a39513b2873dcdecf8c05077f` | `de0dd3fd3ffdd9e9c3a104e8a91a20fa1b486eceac00c50ed93d130e8bca9819` | `4d6db429ad2759d87b6e4291885581c860df901186bf5eebbb0ab077a7ede0d2` | 384 / 383 |

For each reconstructed schedule I checked:

- all 72 X checks, 72 Z checks, and 144 data-qubit incidence sets are conflict-free;
- all 648 MC equivalences hold;
- extrema equal actual extrema and X/Z sectors are globally interleaved;
- none of 14,484 retained antecedents is fully true;
- none of the then-installed 134, 136, or 138 EFSSC validity domains is true;
- all 746,496 ordered edge-pair equality/order relations agree before and after compression.

The overlap-level/whole-check interleaving counts were 202/534, 190/580, and 105/376 for iterations 109, 110, and 111 respectively. These counts are descriptive; global interleaving and MC0 are the actual admissibility conditions. The three candidates are legal positive models, not closure evidence.

## 6. Six unrestricted direct-360 formulas and physical replay

### 6.1 Exact column semantics

Each sector has 360 distinct elementary-fault columns:

- 144 data singletons `D:q`;
- 216 ancilla residuals `R:c:k`, one for each of 72 checks and three residual kinds.

For a check ordered earliest to latest as `(q0,...,q5)`, the canonical residual position sets and physical propagated suffixes are

| kind | canonical positions | physical positions | difference |
|---:|---|---|---|
| 0 | `{0,1}` | `{2,3,4,5}` | full six-body check stabilizer |
| 1 | `{3,4,5}` | `{3,4,5}` | zero |
| 2 | `{4,5}` | `{4,5}` | zero |

Thus canonical and physical representatives have identical detector and logical parities for every residual column, for every schedule order. Multiple residual kinds on one check combine by symmetric difference, exactly as the selector uses `P(K)`.

I reconstructed all 360 columns in all six formulas, 2,160 columns total. For every residual I sorted the actual six CNOT interactions by the candidate schedule, regenerated the propagated physical suffix, regenerated the canonical support, checked their stabilizer relation, and recomputed its 72-bit syndrome and its stored hook-`U` option. For every data singleton I independently regenerated the singleton support and all schedule-ordered `U` choices.

Each direct CNF enforces:

1. all 72 detector parities are zero;
2. twelve output variables equal the logical-dual parities;
3. at least one logical output is true; and
4. at most ten of the 360 primary columns are selected, using a fully equivalent sequential counter.

I reconstructed every variable dictionary and clause dictionary, including every XOR link and cardinality recurrence, then verified each complete solver assignment against each clause.

### 6.2 Exact formulas and witnesses

| iter/sector | vars/clauses | DIMACS SHA-256 | physical weight | nonzero logical indices | source atoms |
|---|---:|---|---:|---|---:|
| 109 Xerr | 5,966 / 22,444 | `ae4e41414c428bc2ac495d5db197f368a34567d6397e8d4ae570df5d23e73fdf` | 12 | 1,3,4,8,9 | 16 |
| 109 Zerr | 5,934 / 22,316 | `793df3bdfb9ad48fd8b79040525aa5ce356297c97b6a648bb2255a29fed23fdc` | 20 | 0,2,3,4,5,8 | 50 |
| 110 Xerr | 5,980 / 22,500 | `d8a9c6add7afc43811aaee1bc87a20bfb57e6931d5266f5c718b3e2a19d2989f` | 12 | 0,2,9 | 16 |
| 110 Zerr | 5,946 / 22,364 | `8c9df8345f75b9dd72dc03bf8b8f7beecbc7ebc3c956ebab3354722479a82bf4` | 22 | 0,1,3,4,5 | 63 |
| 111 Xerr | 5,935 / 22,320 | `cedb2f5f3be7730a04a8cb12f08c5acc18154e1d3a43c4b9d40176f5027b6916` | 14 | 1,6 | 25 |
| 111 Zerr | 5,968 / 22,452 | `a1a24cfb2af4fe19675759ca4c97b79d3ab7fe841b64d4a61680a78795b79b30` | 20 | 0,1,2,4,5 | 80 |

Every assignment selects exactly ten distinct primary columns. The complete selected names are:

```text
109 Xerr: D:43 D:44 D:47 D:49 D:53 D:59 D:123 D:125 R:39:0 R:46:0
109 Zerr: D:70 D:71 D:124 D:139 R:26:1 R:42:2 R:43:1 R:54:0 R:57:0 R:60:0
110 Xerr: D:52 D:53 D:56 D:58 D:60 D:62 D:128 D:133 R:42:0 R:49:2
110 Zerr: D:39 R:35:0 R:38:0 R:38:2 R:40:0 R:40:1 R:48:0 R:49:2 R:52:0 R:58:0
111 Xerr: D:17 D:57 D:86 D:93 D:140 D:141 D:142 R:25:0 R:47:0 R:64:1
111 Zerr: R:41:0 R:42:2 R:46:0 R:47:0 R:51:0 R:52:2 R:53:2 R:55:2 R:60:2 R:61:0
```

The canonical net weights are 12,16,12,16,12,16 respectively. The physical net weights are the table's 12,20,12,22,14,20. In all six cases both net supports have zero detector syndrome, the displayed nonzero logical parity vector, and are outside the stabilizer span. Canonical and physical logical parities agree exactly. This is a gate-order physical replay: each ancilla Pauli propagates through the suffix of later CNOTs in that check, and selected supports combine by Pauli symmetric difference. It is not merely a lookup of the proposer's claimed support.

### 6.3 Why each new EFSSC is a globally sound exact cut

Fix one of the six ten-name selections. For any legal schedule `t`, its within-check ranks uniquely determine each residual column's canonical support. `V_s(t)` recomputes the full 84-bit detector/logical signature of that exact ten-fault selection. Therefore:

- if `V_s(t)` is false, the selector imposes no restriction on that schedule;
- if `V_s(t)` is true, the same ten elementary faults form a zero-syndrome nonstabilizer effective error under that schedule, so the candidate cannot have circuit distance at least 11;
- the physical suffix differs from the canonical representative only by selected check stabilizers, so the conclusion is unchanged by replacing all canonical residuals with the actual propagated suffixes.

Hence `not V_s` is necessary for every surviving Gross schedule throughout the selector's entire semantic domain. It is not limited to the source schedule and does not overreach to an approximate order cube. Conversely, its truth condition is exactly the signature criterion for the fixed ten-name selection, so the domain is not weakened. The stored source atoms only certify the concrete mechanism and its source antecedent; they are not substituted for the EFSSC circuit.

## 7. Atomic continuation and iteration 112

I recomputed the selector-state hash from the exact semantic key tuple

```text
(mechanism_id, sector, selected_names, data_support,
 group_kinds, selector_semantic_sha256)
```

at every prefix. The transition chain is:

| completed iter | before | before SHA-256 | added | after | after SHA-256 |
|---:|---:|---|---|---:|---|
| 109 | 134 | `9be75eba643ac167d5c51497ca8e5cd23eb1656f803a49cbd8e7f1285b004113` | `r88-i109-Xerr`, `r88-i109-Zerr` | 136 | `4cbdd9f9c588e643b92e890891ef60a632f996268375d1f825e0d8bad9ed2b6a` |
| 110 | 136 | `4cbdd9f9c588e643b92e890891ef60a632f996268375d1f825e0d8bad9ed2b6a` | `r88-i110-Xerr`, `r88-i110-Zerr` | 138 | `7066d3a5751eeb87af5e3a3423a98b7de71b5435923550633942b4d47d8083bd` |
| 111 | 138 | `7066d3a5751eeb87af5e3a3423a98b7de71b5435923550633942b4d47d8083bd` | `r88-i111-Xerr`, `r88-i111-Zerr` | 140 | `a0364547f846fd68ace7cdba85d89c0f8e6326145243fb0fea7ff543420994cb` |

For each step I checked that the source formula contains exactly the prior prefix, both direct sectors and outer model had already passed, exactly two new selector records match the physical mechanisms, `state_mutated_atomically` is true, `repair_entered` is false, and the next iteration is marked `started:false`.

`continuation/final_state.json` has SHA-256 `066538581a7c408827987a6b80d348655da3f41099000ca6f3fbc002e3c9aac`, `next_iteration:112`, `selector_count:140`, `started:false`, `stop:null`, and completed iterations `[109,110,111]`. The iter112 source contains exactly the compact form of those 140 selectors after the inherited `iteration`/`source_iteration` provenance normalization.

The only paths whose names contain iter112 are the six formula artifacts:

```text
formulas/iter112/source.json.gz
formulas/iter112/outer.cnf.gz
formulas/iter112/metadata.json
formulas/iter112/assertion_map.jsonl.gz
formulas/iter112/circuit_trace.json.gz
formulas/iter112/encoding_check.json
```

There is no `iterations/iter112` directory. A decompression-aware scan of every textual package payload found no iter112 solver log, assignment, model, SAT/UNSAT line, DRAT, LRAT, or proof disposition. `PROCESS_LEDGER.json` has no command containing 112. Iter112 is therefore **checked but unsolved**. Its `a8b917...6594` hash may be used as the next query binding; it may not be described as SAT, UNSAT, exhausted, or closed.

## 8. CaDiCaL, DRAT, and LRAT controls

The host is arm64 and all three bundled executables are Mach-O arm64:

| tool | bytes | SHA-256 |
|---|---:|---|
| CaDiCaL 1.9.5 | 967,144 | `fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9` |
| drat-trim | 70,120 | `f58f63b0f76945d4c4c9ff6e87afaf870f579e67c0f7cca589492df8fc7ebd47` |
| lrat-check | 36,552 | `bd7eb8052623525814a0a37502b47f05375d9d9dfaf96ddc2fcd858958517cea` |

I generated a fresh proof from the 30-variable, 141-clause PHP(6,5) fixture and ran fresh controls in the foreground:

```text
cadical --no-binary php6_5.cnf fresh.drat             -> exit 20, UNSATISFIABLE
drat-trim php6_5.cnf fresh.drat -t 170 -L fresh.lrat  -> exit 0, VERIFIED
lrat-check php6_5.cnf fresh.lrat                       -> exit 0, VERIFIED
drat-trim php6_5.cnf truncated.drat -t 170             -> exit 1, NOT VERIFIED
drat-trim php6_5.cnf corrupt.drat -t 170               -> exit 1, NOT VERIFIED
lrat-check php6_5.cnf truncated.lrat                    -> exit 1, NOT VERIFIED
lrat-check php6_5.cnf corrupt.lrat                      -> exit 1, NOT VERIFIED
```

The fixture hash is `b8d28f511bbc3bc5d67e0fcda748b6ad85d5e543c64bc91d09f34ecb10805efd`. The independently generated proof hashes are:

```text
fresh DRAT: b6c2e560bb08c84d583ca94799951a21c8cae5de35d6d04d77bc4842e9c18ecd (3,114 bytes)
fresh LRAT: cf32dfff36b24ba36c3504765f29ecf3d7a8abaa59956ade4d24a4062caa6431 (11,189 bytes)
```

They equal the package controls. This validates the executable chain on this host. It proves only PHP(6,5) UNSAT. No accepted Gross DRAT or LRAT exists, and no Gross UNSAT occurred.

## 9. Failure ledger, serialization, and FIX-2

All ten disclosed incidents were attacked separately:

| incident | independent disposition |
|---|---|
| extractor used `source_iteration` against rows carrying `iteration` | Round-86 has exactly two such rows; normalized values and all 134 selector semantics match; initial KeyError output has no evidentiary role |
| normalized-AST lookup used nonexistent key | accepted AST field exists and gives exact 0/19,016 comparison |
| Python 3.9 lacked `int.bit_count` | reproduced `AttributeError`; accepted code uses `bin(mask).count("1")`; exhaustive memberships pass |
| argparse namespace was shadowed | no rejected output appears in accepted manifests/formulas; accepted script parses and replays |
| missing true unit | byte-for-byte rejected hash reproduced; all accepted CNFs contain `(1)` and differ in count/hash |
| iter110 schema check hard-coded iter109 | accepted iter110–112 source schemas and exact expected counts all reconstruct |
| checker hard-coded 2,274 memberships | accepted counts are 2,274/2,286/2,298/2,322 and all four are exhaustively checked |
| continuation audit compared nonsemantic provenance field | exact semantic selector key projection reproduces all three state hashes |
| two continuation-checker formatting defects | accepted checker parses and full continuation independently reconstructs; failed syntax supports no result |
| manifest generator filtered by basename | exact five omitted rows identified; accepted sorted path sets include them and both manifests pass |

No rejected artifact is cited by `RESULT.json` as an accepted outcome. The rejected CNF hash occurs only in failure disclosure. The other nine failures stopped before a verdict-bearing output. The inherited 14.36 GB Round-86 failed DP path remains historical only.

`PROCESS_LEDGER.json` contains nine bounded foreground processes: three outer CaDiCaL SAT calls and six direct CaDiCaL SAT calls. All returned code 10, none timed out, and all are marked `exited_and_reaped`. Outer wall times were 3.916632, 4.336352, and 6.534544 seconds. Direct wall times were 122.184040, 49.359826, 90.957324, 40.480697, 21.134692, and 29.374692 seconds. No OS-level background or detached process was started. The requested SAT DRAT streams contain no empty-clause conclusion and are explicitly excluded as proof objects.

The sealed cleanup record removes `/tmp/circdist_round88_outer` and the preseal replay scratch, reports `science_scratch_exists_after:false`, and the preseal process scan reports zero matches. These claims agree with the inventory and process records.

## 10. Environment requirement and replay

`ENVIRONMENT.json` records:

```text
python executable: /private/tmp/circdist-r72-dispatcher-venv/bin/python
Python:            3.9.6
Z3:                5.1.0
PySAT:             1.9.dev15
platform:          macOS-26.6.2-arm64-arm-64bit
```

The current system interpreter is `/Library/Developer/CommandLineTools/usr/bin/python3`, also Python 3.9.6, but both `find_spec("z3")` and `find_spec("pysat")` return `None`. Importing `round68_build` under system Python reaches `round63_src/outer.py` and fails exactly with:

```text
ModuleNotFoundError: No module named 'z3'
```

The Z3 candidate corroboration likewise exits 1 under system Python and passes under the recorded interpreter with 19,016 assertions and both raw and compressed schedules SAT when fixed. This independently reproduces the dispatcher-observed dependency failure. It is not a failed mathematical model.

`replay.sh` sets `PY=${CIRCDIST_PYTHON:-python3}`, so its fallback is not portable. However, the documented command at `REPORT.md` line 143 does not ask the reader to use the fallback; it explicitly supplies the exact recorded interpreter, and `ENVIRONMENT.json` supplies executable and module versions. On a disposable overlay restoring the package's sealed protected scheduler snapshot, I ran exactly:

```text
CIRCDIST_PYTHON=/private/tmp/circdist-r72-dispatcher-venv/bin/python \
  ./circdist/artifacts/circdist_gross_proof_outer_round88_20260830/replay.sh
```

It exited 0 after rebuilding all four CNFs/maps/traces, replaying all three complete models and six direct mechanisms, checking continuation and proof fixtures, and ended with `ROUND88_PACKAGE_REPLAY_PASS`.

Running the same shell replay directly against today's live repository fails earlier, as it should, because `check_protected.py` sees scheduler SHA `b808ab...f957` rather than the sealed pre-dispatch SHA `fb1c4003...81b`. That is canonical scheduler drift after packaging, not package corruption. The disposable overlay changed no package byte and restored only the five protected inputs named by `INPUT_BINDINGS.json`.

Assessment: the documentation is adequate for this sealed host and review, but the absolute `/private/tmp` path may disappear and the fallback has no dependency probe. A future package should add a fail-fast import/version check or a portable environment lock. This improvement is not required to repair the scientific evidence accepted here.

## 11. Reviewer-side failed attacks and corrections

For completeness, these were my own non-evidentiary harness failures:

1. manifest verification from the wrong current directory;
2. an initial Python `nonlocal` declaration at module scope;
3. an inventory comparison that repeated the same defective basename idea being audited, then was corrected to package-relative paths;
4. the 288 harmless Z3 Distinct-wrapper serialization differences described above;
5. an incorrect expectation that numeral 2 must occur literally in the SMT AST, corrected after operator enumeration showed rank 2 need not be a literal;
6. an initial compact-final-state comparison that did not normalize inherited `iteration` to `source_iteration`;
7. an arbitrary-byte DRAT corruption that landed on a dispensable deletion line and therefore remained valid;
8. a proof-control harness assertion that searched only a truncated log tail for the CaDiCaL marker;
9. one Python 3.9 `Path.write_text(newline=...)` incompatibility while creating an overlay placeholder.

Every case stopped the reviewer harness or exposed an inadequate negative control. I corrected it, reran the complete affected check, and relied only on the final passing runs described above. None changed canonical or package data.

## 12. Licensed canonical replacement and validator overlay

Because the package is clear at proposer level, the following is the sole licensed replacement for `circdist/proof-dag/nodes/CIRCDIST.gross.yaml`. It is a complete byte-for-byte document, serialized by PyYAML with `sort_keys=False`, `allow_unicode=True`, and width 120. Those settings reserialize the unmodified current node byte-identically before the permitted mutations.

Licensed replacement identity:

```text
bytes:   61,309
LFs:     728
SHA-256: d3629fef2b325e3a41c39a2fea774391d99c9ff90ca9014f011a0bfa7a7118f5
```

The semantic diff is exactly:

- preserve `id`, `role`, aliases, claim, assessment level/caveats/summary/routes, every route, `task-003`, all 58 prior evidence rows, and all 14 prior events;
- append the Round-88 package and this Round-89 review as evidence;
- replace only `frontier.dstar-residual` with the fresh iteration-112 binding and limitations; and
- append one `review-completed` event.

No root or route label changes. In particular, `assessment.level` remains `CONJECTURED` and the exact residual remains `{11,12}`.

The disposable overlay results were:

| check | result |
|---|---|
| previous-state retention | exit 0; prior nodes, routes, and events retained; 16 nodes valid |
| proof DAG, circdist | exit 0; 16 nodes valid |
| proof DAG, all projects | exit 0; `se` 85, `ksum` 144, `circdist` 16, Holevo projects 7/8/86/20, Grothendieck projects 14/9/11 nodes valid |
| evidence closure | exit 0; 156 structured paths, all project-local and linked |
| migration | exit 0; 16 nodes, 143 original events, 728 byte-identical copies |
| release contracts | exit 0; 14/14 |
| DAG contracts | exit 0; 24/24 |
| Lean selftest | exit 0; 23/23 |
| duplicate YAML keys | exit 0; 758 files, 19,392 mappings, zero duplicates |
| `git diff --check` | exit 0 |

The overlay included a placeholder at the final review path only so evidence closure could test the exact link. The live node, scheduler, generated views, and package were never edited.

```yaml
id: CIRCDIST.gross
role: outcome
aliases:
- GROSS-DSTAR
claim: For the Gross code [[144,12,12]] with single-ancilla CNOT syndrome extraction (interleaving of X- and Z-check CNOTs
  allowed; each required CNOT exactly once; one two-qubit gate per qubit per time step; no flag ancillas, cat states, or generating-set
  changes; idle layers compressed), the optimum D*_Gross = max over legal schedules M of d_circ(C(M)) is determined with proof,
  as either an explicit interleaved schedule with certified d_circ = 12, or a proof that every legal schedule satisfies d_circ
  <= 11; and the published conjectured distance-11 circuit has a certified d_circ = 11.
assessment:
  level: CONJECTURED
  caveats:
  - Do not cite SBB26 Appendix H.2 as proving circuit distance 12 for the original Gross code. Shaw-Terhal Table I reports
    only tilde d_circ <= 12 for a different end-cycle “second gross” code; equality of n=144 and k=12 (or of the 288-qubit
    total hardware count) is not code identity or S_Gross membership.
  summary: 'The optimal circuit-distance question remains CONJECTURED, with D* in {11,12} unresolved. The universal d_ext
    <= 11 cap is PROVED; the candidate-certification route is CERTIFIED*. The latest completion-gap candidate was killed by
    the missed two-prefix shape. The three recorded no-go classes and search machinery are scoped by-products, not a universal
    proof of D*=11. A fresh primary-source scope audit closes the Shaw-Terhal morphing lead negatively: its distance-12-labeled
    endpoint is a different weight-9 [[144,12,12]] “second gross” code with alternating code frames, outside frozen S_Gross,
    and Table I gives only a BP-OSD circuit-distance upper bound <=12. It supplies neither a legal distance-12 witness nor
    a universal <=11 no-go. Round 61''s proposer-level clean-room audit refutes two further completion screens: absence of
    all four individually gain-positive shapes does not exclude cancelling multi-check weight-10 mechanisms, and even a clean
    |V|=12 / at-most-four-check stratum with diagonal short hooks does not exclude repair-zero minimum mechanisms. It also
    finds that hunt2''s j<=4 recursion did not enforce distinct contributing checks; the earlier candidate kill survives because
    its 144 decisive witnesses were separately rebuilt from raw schedules. These are filter no-go results, not a universal
    theorem, so D* remains in {11,12}. Round 62 installs a proposer-level unrestricted 864-edge/648-MC CEGAR package with
    direct-360 effective and arbitrary-round repair adversaries plus raw replay. Its first 20 exact outer schedules are all
    legal, MC-valid and interleaved, and all are killed in Xerr by verified weight-10 mechanisms; 20 sound order-region blocks
    and all 190 prior-block exclusions replay. This is quantitative search progress only: no effective-layer UNSAT, repair-layer
    UNSAT or outer exhaustion was obtained. Round 63 adds a proposer-level library of 1,440 globally valid deletion-minimal
    five-atom single-residual order clauses, exhaustively replayed over 103,680 local-order cases with 7,200 atom-deletion
    controls. A separate ten-step experiment generated 15,874 witness-checked pair-pattern clauses but did not retain the
    raw ledgers needed for absence use. No checked DRUP/DRAT/LRAT proof exists, so the exact residual is unchanged. Round
    68 emits complete direct-360 DIMACS for one unrestricted clause-saturated candidate, but both sectors are SAT and raw
    replay to weight-10 Xerr and weight-8 Zerr mechanisms. Five continuation candidates are likewise killed in both sectors.
    Twelve new sound blocks are retained, for 1,472 total; no direct absence, repair entry or outer exhaustion exists, so
    D* remains in {11,12}. Round 70''s fresh exact review clears the round-69 positive-witness block library as proposer-level
    evidence and licenses strict continuation at outer iteration 6 with 6,212 installed sound blocks. It licenses no absence,
    repair, outer exhaustion, D* narrowing, route change or level change. Round 71 continues through iterations 6--29: all
    24 outer candidates and all 48 complete direct sectors are SAT and raw-replayed, adding 48 candidate-exact blocks. The
    next reviewed-by-dispatcher frontier is iteration 30 with 6,260 blocks; no absence, repair, exhaustion or D* narrowing
    exists. Round 73''s fresh exact review clears the round-72 566-term conservative positive library and iterations 30--41
    as proposer-level evidence. The exact continuation frontier is iteration 42 with 6,850 installed blocks; no absence, repair,
    exhaustion, D* narrowing, route change or level change is licensed. Round 75''s fresh independent exact review clears
    the sealed round-74 online generalization package as proposer-level evidence. Iterations 42--53 add 134 sound generalized
    terms and 24 candidate-exact blocks after twelve legal outer SAT schedules and twenty-four complete direct-sector SAT/raw
    replays. The exact fresh-process continuation is iteration 54 with 7,008 installed blocks: 1,440 unary, 20 round-62, 4,740
    round-69 generalized, 566 round-72 generalized, 134 round-74 generalized and 108 dynamic exact. The review literally replays
    all 1,137,096 retained pair tuples and validates the factorized exhaustive proof for 2,985,984 retained multi tuples.
    Deletion controls establish only candidate-relation or fixed-selector atom minimality, not installed-union or global physical-mechanism
    minimality. No absence, repair, exhaustion, D* narrowing, route change or level change is licensed. Round 77''s fresh
    independent exact review clears the sealed round-76 package as proposer-level evidence. Iterations 54--77 add 303 sound
    generalized terms and 48 candidate-exact blocks after twenty-four legal outer SAT schedules and forty-eight complete direct-sector
    SAT/raw replays. The exact fresh-process continuation is unstarted iteration 78 with G=5,743 generalized, D=156 dynamic
    exact, registry=72 and 7,359 installed blocks. The review literally replays all 2,637,648 retained pair tuples and validates
    two factorized exhaustive multi-domain proofs totaling 55,037,740,032 tuples. It corrects one non-load-bearing provenance
    row: the final sealed compressor is 2,760 bytes with SHA-256 d4abdf75b066d8a2507d5c010f96c1c1760f36c6d1d242048fb45c5928cb8dde;
    the stale pre-adaptation row must not be cited as final inventory. Deletion controls still license only candidate-relation
    or fixed-selector atom minimality. No absence, repair, exhaustion, D* narrowing, route change or level change is licensed.
    Round 79''s fresh independent exact review clears the sealed round-78 cross-registry package as proposer-level evidence.
    Before iterations 78--89, synthesis across all 72 reviewed mechanisms retains 2,826 sound cross-registry terms; the twelve
    legal outer schedules and twenty-four complete direct sectors are all SAT and raw-replayed, adding 24 candidate-exact
    blocks, 62 online terms and 1,964 further cross-registry terms. The review''s non-importing checker actually visits all
    43,834,872 literal selector tuples and validates four factorized exhaustive domains totaling 15,485,313,024 tuples, including
    classification, dominance, union and zero-domain checks. The exact fresh-process continuation is unstarted iteration 90
    with G=10,595 generalized, D=180 dynamic exact, registry/raw=96 and 12,235 installed blocks. One non-load-bearing wording
    correction applies: the derivation''s word "permutation" denotes the encoded legal schedule with allowed parallel layers,
    not a strict total order. No absence, repair, exhaustion, D* narrowing, route change or level change is licensed. Round
    81''s fresh independent exact review clears the sealed round-80 whole-registry package as proposer-level evidence. Its
    exact star synthesis retains 24 strict installed-union expansions, with all 304,704 literal raw-selector pair cells replayed
    and 35,294,400 factorized tuples checked. Iterations 90--101 contain twelve legal outer SAT schedules and twenty-four
    complete direct-sector SAT/raw replays, adding 94 online terms, 2,107 cross-registry terms and 24 candidate-exact blocks.
    The review independently visits all 20,820,216 online/cross literal tuples and validates 55,037,740,032 factorized tuples,
    plus the eight reconstructed multi-selector terms and their exact GF(2) domains. The exact fresh-process continuation
    is unstarted iteration 102 with G=12,820 generalized, D=204 dynamic exact, registry/raw=120 and 14,484 installed blocks.
    No direct query is UNSAT and no accepted absence proof exists, so no repair, exhaustion, D* narrowing, route change or
    level change is licensed.'
  basis:
    routes:
    - candidate-certification
    evidence:
    - path: circdist/artifacts/circdist_gross_whole_registry_round80_20260830
      kind: run
      note: Sealed round-80 proposer package cleared by the fresh round-81 exact review. Whole-registry star synthesis retains
        24 strict installed-union expansions over 304,704 literal raw-selector pair cells and 35,294,400 factorized tuples.
        Iterations 90--101 contain twelve legal outer SAT schedules and twenty-four complete direct-sector SAT/raw replays,
        adding 94 online terms, 2,107 cross-registry terms and 24 candidate-exact blocks. The exact fresh-process restart
        is unstarted iteration 102 with G=12,820, D=204, registry/raw=120 and 14,484 installed blocks. The accepted root seal
        is sha256:e086a828391361620eabfbd31b544606f7817826af546fb8779a500f95ec0426. Positive SAT mechanisms, misses, zero
        domains and deletion controls remain non-absence evidence.
    - path: circdist/reviews/circdist_gross_round80_whole_registry_exact_review_20260830.md
      kind: review
      note: Fresh independent round-81 review with non-importing clean-room checkers. It reconstructs 96 source raw mechanisms,
        138 complete catalogs, all pair and star classifications, twelve outer formulas, twenty-four direct CNFs/assignments
        and 120 final raw mechanisms. It actually visits 304,704 whole-star and 20,820,216 online/cross literal cells; validates
        35,294,400 whole-star and 55,037,740,032 online/cross factorized tuples; and independently closes the eight multi-selector
        GF(2) terms, atomic state chain and exact iteration-102 semantic hashes. All ten FIX-2 incidents and rollback boundaries
        pass audit. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; claim, routes, D* interval and level remain unchanged. Review
        sha256:e0d6ad5b54768195516239f4d0a262135025a630ecd6292d91cb694baa51597e.
    - path: circdist/artifacts/circdist_gross_cross_registry_round78_20260829
      kind: run
      note: Sealed round-78 proposer package cleared by the fresh round-79 exact review. Cross-registry synthesis over all
        72 reviewed mechanisms retains 2,826 terms before the outer loop; iterations 78--89 contain twelve legal outer SAT
        schedules and twenty-four complete direct-sector SAT/raw replays, adding 24 candidate-exact blocks, 62 online terms
        and 1,964 further cross-registry terms. The exact fresh-process restart is unstarted iteration 90 with G=10,595, D=180,
        registry/raw=96 and 12,235 installed blocks. The accepted root seal is sha256:db82c387493285e56eeddcef6e7bafc3e48954c4034e6ec2fc699cea1699c987;
        both earlier defective seals remain forbidden. Positive SAT mechanisms and deletion controls remain non-absence evidence.
    - path: circdist/reviews/circdist_gross_round78_cross_registry_exact_review_20260830.md
      kind: review
      note: Fresh independent round-79 review with non-importing clean-room checkers. It reconstructs all twelve outer formulas
        and twenty-four direct CNFs/assignments plus 96 raw mechanisms, actually visits all 43,834,872 literal selector tuples
        and validates four factorized exhaustive domains totaling 15,485,313,024 tuples. It verifies classification, dominance,
        union, zero-domain handling, atomic state commits and the exact iteration-90 state and semantic hashes. All v1--v7
        failures, proof-control incident, rejected seals and rollback boundaries pass audit. It records only a non-load-bearing
        use of "permutation" for a schedule allowing parallel layers. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; claim, routes,
        D* interval and level remain unchanged. Review sha256:e90dc1a23c5c1740267c0ed21920ef4b4af05dab1aecd5eeef934c2a25d2a17a.
    - path: circdist/artifacts/circdist_gross_online_generalizing_round76_20260829
      kind: run
      note: Sealed round-76 proposer package cleared by the fresh round-77 exact review. Iterations 54--77 contain twenty-four
        legal outer SAT schedules and forty-eight complete direct-sector SAT/raw replays. Online generalization produces 420
        candidates and retains 303 sound terms after exact semantic filtering; forty-eight candidate-exact blocks freeze a
        fresh-process restart at iteration 78 with 7,359 installed blocks. The final compressor binding is the 2,760-byte
        sealed file, not the stale pre-adaptation provenance row. Positive misses, zero cells and deletion countertuples remain
        non-absence evidence.
    - path: circdist/reviews/circdist_gross_round76_online_generalizing_exact_review_20260829.md
      kind: review
      note: Fresh independent round-77 review with non-importing clean-room checkers. It reconstructs all twenty-four outer
        formulas and forty-eight direct CNFs/assignments/raw mechanisms, literally replays 2,637,648 retained pair tuples,
        validates two factorized exhaustive multi proofs totaling 55,037,740,032 tuples and the exact state chain G=5,743,
        D=156, registry=72, total=7,359. It records one non-load-bearing compressor provenance correction and limits deletion
        minimality to the candidate relation or fixed selector. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; claim, routes,
        D* interval and level remain unchanged.
    - path: circdist/artifacts/circdist_gross_online_generalizing_round74_20260829
      kind: run
      note: Sealed round-74 proposer package cleared by the fresh round-75 exact review. Iterations 42--53 contain twelve
        legal outer SAT schedules and twenty-four complete direct-sector SAT/raw replays. Online generalization produces 188
        candidates and retains 134 sound terms after exact semantic filtering; twenty-four candidate-exact blocks freeze a
        fresh-process restart at iteration 54 with 7,008 installed blocks. Positive misses, zero cells and deletion countertuples
        remain non-absence evidence.
    - path: circdist/reviews/circdist_gross_round74_online_generalizing_exact_review_20260829.md
      kind: review
      note: Fresh independent round-75 review with non-importing clean-room checkers. It reconstructs all twelve outer formulas
        and twenty-four direct CNFs/assignments/raw mechanisms, literally replays 1,137,096 retained pair tuples, validates
        the factorized exhaustive 2,985,984-tuple multi proof and exact state chain G=5,440, D=108, total=7,008. It records
        two non-load-bearing documentation corrections and limits deletion minimality to the candidate relation or fixed selector.
        Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; claim, routes, D* interval and level remain unchanged.
    - path: circdist/artifacts/circdist_gross_round71_generalization_round72_20260829
      kind: run
      note: Sealed round-72 proposer package cleared by the fresh round-73 exact review. It reconstructs all 48 round-71 mechanisms,
        113 local-order catalogs, 607 conservative pair relations and 48 multi-check GF(2) relations, retaining 566 new sound
        generalized terms after exact deduplication/dominance. Iterations 30--41 are twelve further dual-sector SAT/raw-replayed
        candidates. The package licenses continuation at iteration 42 / 6,850 blocks but no absence, repair, exhaustion, D*
        or level claim.
    - path: circdist/reviews/circdist_gross_round72_generalization_exact_review_20260829.md
      kind: review
      note: Fresh independent round-73 review with a non-importing 863-line clean-room checker. It validates 314,668,800 pair
        cells, 32,031,216 retained physical-selector tuples, all 48 source assignments, semantic deduplication from 696 candidates
        to 566 retained terms, twelve outer schedules and twenty-four complete direct SAT/raw replays; verdict CLEAR-PROPOSER-LEVEL-CONTINUATION,
        with claim, routes, D* interval and level unchanged.
    - path: circdist/artifacts/circdist_gross_cegar_continuation_round71_20260829
      kind: run
      note: Sealed round-71 proposer package independently replayed by the dispatcher. Iterations 6--29 contain 24 legal 864-edge/648-MC
        outer schedules; both complete unrestricted direct-360 sectors are SAT for every candidate, and all 48 assignments
        pass every DIMACS clause and raw physical replay. The 48 new exact blocks license strict continuation at iteration
        30 / 6,260 blocks but no absence, repair, exhaustion, D* or level claim.
    - path: circdist/artifacts/circdist_gross_block_minimization_round69_20260829
      kind: run
      note: Sealed round-69 proposer package cleared for positive-witness use by the fresh round-70 exact review. It contains
        4,740 conservative generalized sound blocks backed by 3,368 raw physical mechanisms and 1,197,120 explicit tuple witnesses,
        plus twelve raw-replayed dynamic blocks from six complete dual-sector SAT CEGAR candidates. The 2,704 negative weight-14
        solver observations are non-load-bearing. The package licenses continuation at iteration 6 / 6,212 blocks but no absence,
        repair, exhaustion, D* or level claim.
    - path: circdist/reviews/circdist_gross_block_minimization_exact_review_20260829.md
      kind: review
      note: Fresh independent round-70 review with a non-importing 478-line clean-room checker. It exhaustively validates
        all 15,552,000 pair cells, 56,539,296 antecedent-tuple incidences, 3,368 raw mechanisms, six outer schedules, twelve
        rebuilt direct-360 formulas and every SAT/raw replay; verdict CLEAR-PROPOSER-LEVEL-CONTINUATION, with claim, routes,
        D* interval and level unchanged.
    - path: circdist/artifacts/circdist_gross_direct360_proof_round68_20260829
      kind: run
      note: Sealed round-68 direct-360 package. Dispatcher independently verified the 101-entry manifest, 49 live bindings
        expanding to 424 files, full 864-edge/648-MC model, both 1884-word pools, complete DIMACS and raw SAT assignments,
        twelve new mechanisms/blocks, and DRAT/LRAT positive and corruption controls. Both primary sectors are SAT, so it
        licenses no absence or level claim.
    - path: circdist/artifacts/circdist_gross_pattern_cegar_round63_20260828
      kind: run
      note: Sealed round-63 proposer package. The independently replayed load-bearing output is a 1,440-clause single-residual
        order library with exhaustive 6! local-order soundness checks and atom-deletion controls. The 15,874-clause two-residual
        CEGAR output is explicitly exploratory because raw ledgers/exclusion replay were not retained. It contains zero checked
        proof objects and licenses no absence or level claim.
    - path: circdist/artifacts/circdist_gross_cegar_round62_20260828
      kind: run
      note: Sealed round-62 proposer package containing the unrestricted outer schedule model, direct-360 effective adversary,
        arbitrary-round repair adversary, raw replay validators, 20 sound CEGAR blocks, named/negative controls and SHA manifest.
        All 20 schedules are killed by positive Xerr witnesses; no absence-side UNSAT or outer exhaustion is claimed. Dispatcher
        independently replayed verify.py in a clean dependency environment before linking the directory.
    - path: circdist/artifacts/circdist_dstar_hunt3_20260828.md
      kind: run
      note: Round-61 proposer-level clean-room four-shape and bounded-stratum audit. Two explicit legal interleaved schedules
        refute those filters as sufficient closure criteria; the report also identifies a distinct-check defect in the old
        j<=4 recursion while preserving the raw-verified candidate kill. No exact D* branch closes, no solver UNSAT verdict
        is claimed, and the residual remains {11,12}.
    - path: circdist/artifacts/circdist_gross_morphing_scope_ruling_20260826.md
      kind: text
      note: Fresh primary-source Shaw-Terhal scope audit; the distance-12-labeled morphing endpoint is a different weight-9
        [[144,12,12]] “second gross” code derived from a [[288,12,18]] mid-cycle code; Table I reports only BP-OSD d_circ
        <= 12. The construction is outside frozen S_Gross, closes frontier task-002 negatively, and leaves D*_Gross in {11,12}.
    - path: circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.gross.yaml
      kind: text
      note: Immutable pre-migration record, including every original event, former summary and frontier; historical evidence,
        not an additional completion review.
    - path: circdist/artifacts/history/legacy_DAG_PROTOCOL.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_verdict_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/logs_circdist_gross_verdict_20260823/SHA256SUMS.txt
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_final_decision_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/logs_circdist_gross_final_20260823/SHA256SUMS.txt
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_candidate_decision_20260822.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/logs_circdist_gross_drivers_20260823/SHA256SUMS.txt
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_candidate_unsat_20260822.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_phicert_20260822.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/reviews/circdist_sbbcert_review_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_sbbcert_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_lift_iff_proof_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/reviews/circdist_numerical_review_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_lift_d3gate_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_g1_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_toolfeas_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_gross_recon_20260820.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/reviews/circdist_gross_verdict_review_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/reviews/circdist_gross_links_review_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_dstar_hunt1_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/circdist_dstar_hunt2_20260823.md
      kind: text
      note: Historical event source; see the unchanged pre-migration node for the exact event and its scope.
    - path: circdist/artifacts/logs_circdist_dstar_hunt1_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_dstar_hunt2_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_gross_drivers_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_gross_final_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_gross_harvest_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_gross_links_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_gross_verdict_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/logs_circdist_gross_verdictreview_20260823
      kind: text
      note: Byte-preserved historical computation package (sources, inputs, outputs and original checksums). No mathematical
        computation was rerun during migration.
    - path: circdist/artifacts/circdist_campaign4_closeout_20260823.md
      kind: text
      note: Preserved campaign context; not used as a new mathematical premise or completion review.
    - path: circdist/artifacts/history/legacy_FILE_PROTOCOL.md
      kind: text
      note: Preserved campaign context; not used as a new mathematical premise or completion review.
    - path: circdist/artifacts/history/notes/CAMPAIGN4_KICKOFF_20260822.md
      kind: text
      note: Preserved campaign context; not used as a new mathematical premise or completion review.
    - path: circdist/artifacts/history/notes/CAMPAIGN_CLOSEOUT_20260820.md
      kind: text
      note: Preserved campaign context; not used as a new mathematical premise or completion review.
    - path: circdist/artifacts/history/notes/HANDOFF_20260820.md
      kind: text
      note: Preserved campaign context; not used as a new mathematical premise or completion review.
    - path: circdist/artifacts/history/notes/HANDOFF_20260823.md
      kind: text
      note: Preserved campaign context; not used as a new mathematical premise or completion review.
    - path: circdist/artifacts/history/PATH_MAP.json
      kind: text
      note: Mechanical relocation map for immutable historical report references; not mathematical evidence.
    - path: circdist/artifacts/circdist_gross_efssc_round86_20260830
      kind: run
      note: Sealed Round-86 EFSSC proposer package, independently cleared at proposer level in Round 87; root seal sha256:94322390a648262e8cc035f8e843617f134fe2d29ff36191720b646c021c89ff.
        No distance-12 witness, universal distance-11 ceiling, UNSAT/exhaustion result, route promotion, or root promotion
        is inferred.
    - path: circdist/reviews/circdist_gross_efssc_exact_review_round87_20260830.md
      kind: review
      note: Fresh strict-serial Round-87 independent exact review licensing proposer-level continuation from iteration 109
        only, with CIRCDIST.gross and gap-via-lift remaining CONJECTURED and D*_Gross in {11,12}.
    - path: circdist/artifacts/circdist_gross_proof_outer_round88_20260830
      kind: run
      note: 'Sealed Round-88 proof-producing finite-outer continuation package independently cleared at proposer level in
        Round 89; root seal sha256:c4061caff46b632b5c4beb7b6eb33281f3520d07c4dfaaa6eb7c6a33883c7e20 and payload seal sha256:d2de2f014954070f20bbba0e55caf49aed93b26986a63fab77955a75f62c8157.
        Iterations 109--111 are complete outer SAT schedules with all six unrestricted direct-360 sectors SAT at weight 10
        and physically replayed, adding six exact EFSSC selectors atomically. The exact fresh/unstarted frontier is iteration
        112 with 14,484 inherited order blocks, 140 selectors, selector-state sha256:a0364547f846fd68ace7cdba85d89c0f8e6326145243fb0fea7ff543420994cb,
        and an independently checked but unsolved 398,488-variable/1,330,104-clause CNF sha256:a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594.
        This is positive continuation evidence only: no Gross UNSAT, direct absence, repair entry, outer exhaustion, D* narrowing,
        route promotion, or root promotion is licensed.'
    - path: circdist/reviews/circdist_gross_proof_outer_exact_review_round89_20260830.md
      kind: review
      note: Fresh independent Round-89 exact review. It re-derives the 864-event rank-compression theorem, reconstructs all
        19,016/19,018/19,020/19,022 source roots and 14,484 inherited order blocks, exhaustively audits all four deterministic
        Tseitin CNFs/source maps and complete iter109--111 SAT assignments, physically replays all six unrestricted direct-360
        weight-10 mechanisms, verifies exact EFSSC soundness and the atomic 134--136--138--140 selector chain, and confirms
        iteration 112 is fresh, checked, and unsolved. Verdict CLEAR-PROPOSER-LEVEL-CONTINUATION; CIRCDIST.gross and its live
        gap route remain CONJECTURED with D*_Gross in {11,12}.
routes:
  candidate-certification:
    premises:
    - CIRCDIST.gross.dext-cap
    assumptions:
      sbb-thm1:
        kind: external-theorem
        statement: 'SBB Thm 1 (arXiv:2603.05481, Theorem 1): d_circ of the candidate circuit equals the minimum distance of
          the associated extended code (two 360-column codes, one per sector) — the reduction this route''s entire certification
          rides on. PROOF VERIFIED 2026-08-23 (wave 36, artifacts/circdist_gross_links_review_20260823.md): re-derived against
          the frozen model, scoped to claim (11), R = E, NON-INTERLEAVED schedules, no 公共定义 mismatch; two published-proof
          defects found and closed (double Prop-2-for-Prop-3 mis-citation — typo, the needed statement is proved in the paper;
          the partition-by-idling step false as drawn for an LRC, closed by an order-preserving re-timing argument, 0/144
          qubits without a consistent order). UNUSABLE for interleaved schedules (only the paper''s claim (12) applies there).
          PDF on disk at <home>/Documents/ChatGPT/circcert/papers/.'
        source:
          note: arXiv:2603.05481 Theorem 1; local PDF under <home>/Documents/ChatGPT/circcert/papers/ (outside this
            repository).
    implication: Via SBB26 Thm 1 the statement d_circ = 11 for the candidate circuit reduces to an exact minimum-distance
      certification on a 360-column extended code (not a circuit-level DEM search); combined with the universal d_ext cap
      this certifies the first half of the claim and pins the achievable floor at 11.
    proof:
      sketch: Finite exact computation with a distance certificate; risk is solver scaling and recovering the actual published
        schedule. Recon P 0.60, D 2 sessions.
      sources:
      - path: circdist/artifacts/circdist_gross_recon_20260820.md
        kind: text
      - path: circdist/artifacts/circdist_gross_sbbcert_20260820.md
        kind: text
    assessment:
      level: CERTIFIED*
      caveats:
      - UNSAT verdicts are solver-grade certificates, not LRAT-checked (no DRAT toolchain on this machine).
      - 'Reconstruction, not authorship: the candidate schedule is the phicert reading of SBB Figure 12 (pixel-verified wave
        13; legality-filter uniqueness re-derived wave 36 over a LARGER space — 72 readings, one object), not a circuit published
        as machine-readable data by the authors.'
      - 'The shared colour-map constraint is LOAD-BEARING for uniqueness: with independent per-panel colour maps the reading
        space grows to 528 with 12 extra pairings (wave-36 finding); the frozen reading keeps the shared map, as the paper''s
        construction implies.'
      - SBB Thm 1 is VERIFIED (wave 36) scoped to claim (11), R = E, NON-INTERLEAVED schedules — it is unusable for interleaved
        schedules (only claim (12) applies there); the candidate is non-interleaved, so the route is unaffected, but no interleaved
        conclusion may cite it.
      - The implication text says "a 360-column extended code"; it is TWO 360-column codes, one per CSS sector (wave-36 precision
        note; rewording would rebind the implication hash and is left to a future fold).
      - 'Carried from wave 13: the verdict artifact''s cross-checking overstatement stands corrected (114 truly multiply-decided,
        not 860; 1026 records, not 3000; max 3 real decisions per sub-query); Figure-12 fill-convention conflict recorded
        and harmless.'
      summary: 'Promoted NUMERICAL -> CERTIFIED* 2026-08-23 (wave 36, artifacts/circdist_gross_links_review_20260823.md):
        the two inherited proposer-grade links are CLOSED — link 3 (phicert legality filter) CONFIRMED STRENGTHENED with the
        reviewer''s own EXHAUSTIVE weight-12 pool (meet-in-the-middle C, 1884/sector — the artifacts'' heuristic ISD pool
        shown exactly complete) and uniqueness re-derived over all 720 edge-maps per panel at t = 6,7,8 (72 readings, ONE
        object, pairing invariant, phi forced to a + b, no second reading; phicert §2.5''s "moderate" sublattice flag retires);
        link 4 (encoding fidelity) CONFIRMED as an exact reformulation of Def 2/3 (360 columns identical, 216/216 residual
        columns, 60/60 + 60/60 witness round-trips both sectors, 5/5 recorded CNF hashes rebuilt, W = 11 UNSAT / W = 12 SAT
        control); and SBB Thm 1''s PROOF IS VERIFIED against the frozen model (scoped: claim (11), R = E, non-interleaved;
        no 公共定义 mismatch) with two published-proof defects found and closed — a double Prop-2-for-Prop-3 mis-citation (needed
        statement proved in the paper), and the partition-by-idling step false as drawn for an LRC, closed by the reviewer''s
        own re-timing argument (0/144 qubits lack a consistent order). Verdict clauses (d) d_circ = 11 and (f) D* >= 11 are
        thereby lifted from PARTIAL. HISTORY: promoted CONJECTURED -> NUMERICAL 2026-08-23 by the wave-13 adversarial review
        (990/990 UNSAT reproduced; Figure-12 pixel-verified; d_ext = 11 both sectors).'
      basis:
        reviews:
        - path: circdist/reviews/circdist_gross_links_review_20260823.md
          kind: review
          scope: Wave-36 closure of the two inherited links (exhaustive-pool legality-filter uniqueness; encoding-fidelity
            round-trips and CNF hash rebuilds) plus verification of the SBB Thm 1 proof against the frozen model with two
            published-proof defects closed; licenses the route at CERTIFIED*.
          locator: Section 5
          reviewed_hash: sha256:4f40673227208c58d21650b3d685670019f5460b44ee52c0440b22293eec1598
        - path: circdist/reviews/circdist_gross_verdict_review_20260823.md
          kind: review
          scope: Independent adversarial review of the final compute verdict — analytic 990-slot completeness re-derived,
            orbit partition + equivariance closed, slot bookkeeping recomputed from SHA256-verified logs, 3+ adversarial spot
            re-decisions with a different solver, 50/50 witness re-verification, Figure-12 pixel verification at 900 dpi,
            inherited-links audit, per-clause verdicts with an honest downgrade of the verdict artifact's cross-checking claim.
          locator: Per-clause verdicts
          reviewed_hash: sha256:4f40673227208c58d21650b3d685670019f5460b44ee52c0440b22293eec1598
        runs:
        - path: circdist/artifacts/circdist_gross_sbbcert_20260820.md
          kind: run
          scope: Full certification sweep of the group-tiled representative class of the SBB candidate on the 360-column extended
            code, both sectors, symmetry-quotiented SAT decision queries; 10/10 eliminated-assignment witnesses audited end-to-end.
          result: d_ext <= 10 for all 8 survivors (hence all group-tiled assignments); d_ext(R) = 11 exactly for every <=
            2-check subset; gross code d = 12 reproduced as method validation; no 6-layer gross SEC is measurement-consistent
            (exact SAT, 55 s).
        evidence:
        - path: circdist/reviews/circdist_sbbcert_review_20260820.md
          kind: text
  gap-via-lift:
    premises:
    - CIRCDIST.gross.dext-cap
    - CIRCDIST.lift.iff
    implication: Given the universal d_ext <= 11 cap, D* = 12 holds iff some interleaved schedule has completion gap >= 1
      at weight 12; the closed-lift criterion turns this into a voltage/monodromy condition checkable per witness family,
      deciding the second half of the claim in either direction.
    proof:
      sketch: Cross-root import; inherits CIRCDIST.lift risk. Recon P 0.20, D 5 (about 2 sessions shared with the lift subtree).
      sources:
      - path: circdist/artifacts/circdist_gross_recon_20260820.md
        kind: text
    assessment:
      level: CONJECTURED
      summary: 'STAGE-2 VERDICT (wave 38): THE CANDIDATE IS DEAD IN BOTH SECTORS — d_eff <= 10, not 11 (Z: 72 configs at j
        <= 3, 180 at j <= 4; X: 72/84; zero at weights 8-9; all 144 witnesses re-verified from raw CNOT times and re-derived
        inside the campaign''s 360-column model), killed by the FOURTH gain-positive residual shape (the 2-prefix {i1,i2},
        = 4-suffix mod stabiliser) which wave 37''s d_eff filter missed (it tested 2 of 4 shapes); decisively, every X-memory
        weight-10 witness has exact repair = 1, so d_circ <= 11 for the candidate regardless. REPRICING: P(D* = 12) 0.30 ->
        0.10; P(D* = 11) 0.10 -> 0.15 — three no-go walls now stand at proposer level (check-serial class repair-0 PROVED;
        fully-TI cannot hold d_eff = 11 both sectors; all 297 interleaved re-timings of M_cand die on horizontal hooks, 100
        percent repair-0). NEW LEMMA D (proposer): d_eff depends only on within-check orders, so M_cand''s certification TRANSFERS
        to its interleaved re-timings (up to 504/648 interleaved) for free. D* remains OPEN in {11, 12}, evidence direction
        tilted toward 11. STAGE-1 HISTORY (candidate since killed): a 3-colour-tiled annealed schedule — legal, 0/648 MC violations,
        384/648 pairs interleaved, 72/72 hooks diagonal 0 vertical both sectors, no weight-<=10 configs — has repair-0 on
        0/144 (Z) and 0/360 (X) canonical minimum-weight gamma (same-round and 2-group multi-round), the exact gap signature
        the PROVED criterion demands. Schedule recorded in the hunt artifact. BINDING REMAINING CHECK (stage 2): SAT-certify
        d_eff = 11 for this schedule in both sectors and close the two uncovered |gamma| = 11 shapes (weight-13 provably empty
        — all gross logicals have even weight). Stage-1 no-go by-products: the whole CHECK-SERIAL (global-potential) class
        is PROVED repair-0 (226/226 + 170/170, with the two-line u(S) argument) so cannot gap; no fully-TI schedule keeps
        d_eff = 11 in both sectors (353/400 and 357/400 die on d_eff <= 10) — the binding constraint for a gap witness is
        keeping d_eff UP, not making repair positive. Stage-2 pricing: P(D* = 12 witness) 0.30, P(D* = 11 no-go) 0.10.'
      basis:
        runs:
        - path: circdist/artifacts/circdist_dstar_hunt2_20260823.md
          kind: run
          scope: 'Stage-2 certification attempt (logs: artifacts/logs_circdist_dstar_hunt2_20260823/, 45 SHA-summed entries;
            predecessor logs re-verified 23/23): no SAT solver on the machine, so an exact combinatorial exhaustion of the
            |V| = 12 stratum (complete 1884-logical pool per sector, j <= 4 contributing checks) on three proved reductions
            plus Bound 1; second-source validation — the same code returns 0 configurations for the published candidate M_cand
            (agreeing with its 990 all-UNSAT solver sub-queries) on both labelling readings, d = 12 on singleton-only columns,
            144/360 canonical family reproduction.'
          result: Candidate d_eff <= 10 both sectors (144 witnesses, 144/144 assertion checks); every X-memory weight-10 witness
            has exact repair = 1 hence candidate d_circ <= 11; 297/297 interleaved re-timings of M_cand repair-0 via horizontal
            hooks; Lemma D (d_eff order-only dependence) established at proposer level.
        - path: circdist/artifacts/circdist_dstar_hunt1_20260823.md
          kind: run
          scope: 'Stage-1 hunt (logs: artifacts/logs_circdist_dstar_hunt1_20260823/, 23 SHA-summed entries): LIFT-prime/repair
            decider built from scratch and validated on ground truth (Steane 21/21 criterion + 21/21 sandwich agreements vs
            brute-force multi-round DEM; independently reproduces the known Steane gap, 1/68 random schedules); gross rebuilt
            (overlaps {0:4536, 2:648}, k = 12, 1884 logicals/sector, 1080/1080 pair coverage); four families swept.'
          result: 'Non-interleaved 4/4 repair-0; check-serial 60 schedules repair-0 PROVED class-wide; TI legal+MC 400 sampled
            (1.15 percent acceptance), 0 gap survivors in both sectors; coset-TI 0/60000 pass MC; 3-colour-tiled annealed:
            ONE candidate with zero repair-0 canonical gamma in both sectors.'
frontier:
  task-003:
    task: 'Remaining after wave 36 closed links 3/4 and verified SBB Thm 1: (c) optionally LRAT-check a certificate sample
      (the sole remaining verification-depth item on the route); and fold the two-codes-one-per-sector precision into the
      implication text when next re-binding it.'
    kind: task
    since: '2026-08-20'
  dstar-residual:
    task: Continue only from the independently reviewed sealed fresh/unstarted iteration 112 state. The inherited sound order-block
      library remains exactly 14,484 predicates (1,440 unary, 20 round-62, 12,820 generalized, 204 dynamic), and the exact
      fixed-selector frontier is 140 EFSSCs (120 reviewed Round-80 selectors, fourteen Round-86 selectors from iterations
      102--108, and six Round-88 selectors from iterations 109--111). Bind selector-state sha256:a0364547f846fd68ace7cdba85d89c0f8e6326145243fb0fea7ff543420994cb
      and the iteration-112 semantic source sha256:a816fa6a7aec4eb3502f4b5c1a8c50dc8d958b383a003a84738fcb7e630e7c43 before
      use. Its deterministic 10-bit compressed finite-outer formula has 19,022 source assertions, 398,488 variables, 1,330,104
      clauses and CNF sha256:a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594; it was checked but deliberately
      not solved, and no solver/model/proof disposition is inherited. For a SAT result, retain the complete assignment, replay
      every DIMACS clause and frozen schedule condition, then rebuild and adjudicate both complete unrestricted direct-360
      sectors; a positive mechanism kills only that concrete candidate and proves no absence, and only exact source-schedule-valid
      EFSSC selectors may be added atomically. For an UNSAT result, retain a complete DRAT proof, independently accept it,
      generate LRAT, and independently accept the LRAT with valid/corrupt/truncated controls. Enter repair only after both
      direct sectors have independently checked absence. Preserve frozen S_Gross, strict serialization, MC0, terminal residual
      semantics, both CSS sectors, and every existing exclusion against morphing, Circ-Preserve substitutions, alternate conflict
      models, exploratory pair clauses, retroactive cuts and stale compressor provenance. Keep CIRCDIST.gross and gap-via-lift
      CONJECTURED and D*_Gross in {11,12}; this reviewed continuation supplies no Gross UNSAT, absence, exhaustion, distance-12
      witness, universal distance-11 ceiling, route promotion or root promotion.
    kind: task
    since: '2026-08-30'
events:
  gross-whole-registry-round81-review-2026-08-30:
    date: '2026-08-30'
    type: review-completed
    summary: Fresh independent exact review cleared the sealed round-80 whole-registry package as proposer-level evidence
      and licensed strict fresh-process continuation from unstarted iteration 102 with 14,484 blocks. Non-importing clean-room
      checkers rebuilt 96 source raw mechanisms, 138 complete catalogs, exact pair/star synthesis and classification, twelve
      legal outer SAT schedules, twenty-four complete direct SAT/raw replays and 120 final raw mechanisms. They actually visited
      304,704 whole-star and 20,820,216 online/cross literal cells; validated 35,294,400 whole-star and 55,037,740,032 online/cross
      factorized tuples; and independently closed the eight multi-selector GF(2) terms, atomic commits and the state chain
      G=12,820, D=204, registry/raw=120. All ten FIX-2 incidents and rollback boundaries pass audit. No absence, repair, exhaustion,
      D* narrowing, route change or level change is licensed. Gross remains CONJECTURED with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_whole_registry_round80_20260830
      kind: run
    - path: circdist/reviews/circdist_gross_round80_whole_registry_exact_review_20260830.md
      kind: review
  gross-cross-registry-round79-review-2026-08-30:
    date: '2026-08-30'
    type: review-completed
    summary: Fresh independent exact review cleared the sealed round-78 cross-registry package as proposer-level evidence
      and licensed strict fresh-process continuation from unstarted iteration 90 with 12,235 blocks. Non-importing clean-room
      checkers rebuilt twelve legal outer SAT schedules, twenty-four complete direct SAT/raw replays and 96 raw mechanisms;
      actually visited all 43,834,872 literal selector tuples; validated four factorized exhaustive domains totaling 15,485,313,024
      tuples; and verified classification, dominance, union, zero-domain handling, atomic commits and the state chain G=10,595,
      D=180, registry/raw=96. All synthesis v1--v7 failures, rollback boundaries, proof controls and both rejected seals pass
      audit. One non-load-bearing wording correction limits "permutation" to the encoded legal schedule with allowed parallel
      layers. No absence, repair, exhaustion, D* narrowing, route change or level change is licensed. Gross remains CONJECTURED
      with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_cross_registry_round78_20260829
      kind: run
    - path: circdist/reviews/circdist_gross_round78_cross_registry_exact_review_20260830.md
      kind: review
  gross-online-generalization-round77-review-2026-08-29:
    date: '2026-08-29'
    type: review-completed
    summary: Fresh independent exact review cleared the sealed round-76 positive online-generalization package as proposer-level
      evidence and licensed strict fresh-process continuation from unstarted iteration 78 with 7,359 blocks. Non-importing
      clean-room checkers rebuilt twenty-four legal outer SAT schedules, forty-eight complete direct SAT/raw replays, exact
      classification from 420 candidates to 303 retained terms, every one of 2,637,648 retained pair tuples, two factorized
      exhaustive proofs totaling 55,037,740,032 multi tuples and the state chain G=5,743, D=156, registry=72. One stale pre-adaptation
      compressor provenance row is corrected at review level; final sealed binding is 2,760 bytes / sha256:d4abdf75b066d8a2507d5c010f96c1c1760f36c6d1d242048fb45c5928cb8dde.
      Deletion minimality is limited to candidate relations or fixed selectors. No absence, repair, exhaustion, D* narrowing,
      route change or level change is licensed. Gross remains CONJECTURED with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_online_generalizing_round76_20260829
      kind: run
    - path: circdist/reviews/circdist_gross_round76_online_generalizing_exact_review_20260829.md
      kind: review
  gross-online-generalization-round75-review-2026-08-29:
    date: '2026-08-29'
    type: review-completed
    summary: Fresh independent exact review cleared the sealed round-74 positive online-generalization package as proposer-level
      evidence and licensed strict fresh-process continuation from iteration 54 with 7,008 blocks. Non-importing clean-room
      checkers rebuilt twelve legal outer SAT schedules, twenty-four complete direct SAT/raw replays, exact classification
      from 188 candidates to 134 retained terms, every one of 1,137,096 retained pair tuples, the factorized exhaustive proof
      for 2,985,984 retained multi tuples and the state chain G=5,440, D=108. Two documentation imprecisions are corrected
      at review level, and deletion minimality is limited to candidate relations or fixed selectors. No absence, repair, exhaustion,
      D* narrowing, route change or level change is licensed. Gross remains CONJECTURED with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_online_generalizing_round74_20260829
      kind: run
    - path: circdist/reviews/circdist_gross_round74_online_generalizing_exact_review_20260829.md
      kind: review
  gross-round72-generalization-round73-review-2026-08-29:
    date: '2026-08-29'
    type: review-completed
    summary: Fresh independent exact review cleared the sealed round-72 positive-witness generalization package as proposer-level
      evidence and licensed strict continuation from iteration 42 with 6,850 blocks. A non-importing clean-room checker validated
      314,668,800 pair cells, 32,031,216 retained physical-selector tuples, all 48 source assignments, exact semantic deduplication
      from 696 candidates to 566 retained terms, twelve legal outer schedules and twenty-four complete direct SAT/raw replays.
      Zero truth cells and failed positive completions remain non-load-bearing; no absence, repair, exhaustion, D* narrowing,
      route change or level change is licensed. Gross remains CONJECTURED with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_round71_generalization_round72_20260829
      kind: run
    - path: circdist/reviews/circdist_gross_round72_generalization_exact_review_20260829.md
      kind: review
  gross-cegar-continuation-round71-2026-08-29:
    date: '2026-08-29'
    type: repair-applied
    summary: Linked the sealed round-71 exact CEGAR continuation after dispatcher manifest and full verifier replay, without
      a level change. Iterations 6--29 give 24 legal outer schedules and 48 complete direct-sector SAT assignments, all clause-checked
      and raw-replayed, yielding 48 candidate-exact sound blocks. No sector is UNSAT, no repair is entered and no outer exhaustion
      exists. The exact restart is iteration 30 with 6,260 installed blocks. Gross remains CONJECTURED with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_cegar_continuation_round71_20260829
      kind: run
  gross-block-minimization-round70-review-2026-08-29:
    date: '2026-08-29'
    type: review-completed
    summary: Fresh independent exact review cleared the sealed round-69 positive-witness library as proposer-level evidence
      and licensed strict continuation from iteration 6 with 6,212 blocks. A non-importing clean-room checker validated all
      15,552,000 pair cells, 4,740 sound antecedents over 56,539,296 covered incidences, 3,368 raw mechanisms, six legal outer
      schedules and twelve complete direct-360 SAT/raw replays. The 2,704 negative weight-14 observations remain non-load-bearing;
      no absence, repair, outer exhaustion, D* narrowing, route change or level change is licensed. Gross remains CONJECTURED
      with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_block_minimization_round69_20260829
      kind: run
    - path: circdist/reviews/circdist_gross_block_minimization_exact_review_20260829.md
      kind: review
  gross-direct360-round68-2026-08-29:
    date: '2026-08-29'
    type: repair-applied
    summary: Linked the sealed round-68 complete direct-360 package after dispatcher manifest and full verifier replay, without
      a level change. One unrestricted clause-saturated candidate has SAT direct queries in both sectors and raw-verified
      weight-10 Xerr and weight-8 Zerr mechanisms; five further exact candidates are also killed in both sectors. Twelve new
      sound exact blocks raise the retained total to 1,472. The independent DRAT/LRAT toolchain accepts valid controls and
      rejects truncated proofs, but no candidate-specific UNSAT, repair result or outer exhaustion exists. Gross remains CONJECTURED
      with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_direct360_proof_round68_20260829
      kind: run
  gross-pattern-cegar-round63-2026-08-28:
    date: '2026-08-28'
    type: repair-applied
    summary: Linked the sealed round-63 pattern-CEGAR package after dispatcher replay, without a level change. The package
      proves 1,440 globally valid five-atom single-residual order clauses by exhaustive local-order checks and deletion controls.
      Its 15,874 pair-pattern clauses remain exploratory due to retention gaps, and it contains zero checked proof objects.
      Gross remains CONJECTURED with D*_Gross in {11,12}; the frontier now requires a proof-logged and independently checked
      direct-360 sector UNSAT on one exact outer candidate.
    sources:
    - path: circdist/artifacts/circdist_gross_pattern_cegar_round63_20260828
      kind: run
  gross-integrated-cegar-round62-2026-08-28:
    date: '2026-08-28'
    type: repair-applied
    summary: Linked the sealed round-62 integrated CEGAR package after independent manifest and replay verification, without
      a level change. The exact outer model produced 20 legal MC-valid interleaved schedules; each is killed by a raw-verified
      Xerr weight-10 mechanism, yielding 20 sound order-region blocks. No UNSAT or outer exhaustion exists, so Gross remains
      CONJECTURED with D*_Gross in {11,12}; the frontier now targets proof-producing residual-support-pattern clauses and
      an incremental checked backend.
    sources:
    - path: circdist/artifacts/circdist_gross_cegar_round62_20260828
      kind: run
  gross-dstar-hunt3-screen-repair-2026-08-28:
    date: '2026-08-28'
    type: repair-applied
    summary: Round-61 proposer audit linked without a level change. It refutes the four-positive-shape and bounded-|V|=12/at-most-four-check
      screens by explicit legal interleaved counterexamples, records the hunt2 distinct-check recursion defect, preserves
      the earlier candidate kill through separately raw-verified witnesses, and replaces the stale filter-based frontier with
      the exact integrated CEGAR residual. Gross remains CONJECTURED with D*_Gross in {11,12}; every new theorem in the report
      remains proposer-level.
    sources:
    - path: circdist/artifacts/circdist_dstar_hunt3_20260828.md
      kind: run
  gross-morphing-scope-ruling-2026-08-26:
    date: '2026-08-26'
    type: repair-applied
    summary: Fresh primary-source audit corrected the prior second-hand morphing gloss. Shaw-Terhal's original Gross [[144,12,12]]
      is only a mid-cycle input whose end-cycle code is [[72,12,6]]; their distance-12 endpoint is a different weight-9 [[144,12,12]]
      “second gross” code derived from [[288,12,18]], and its reported morphing circuit distance is only the BP-OSD upper
      bound <=12. The construction is outside frozen S_Gross. Frontier task-002 closes negative; the root stays CONJECTURED
      with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_morphing_scope_ruling_20260826.md
      kind: text
  gross-efssc-round87-review-2026-08-30:
    date: '2026-08-30'
    type: review-completed
    summary: Fresh independent Round-87 review cleared the sealed Round-86 exact fixed-selector semantic-cut package for proposer-level
      continuation only. It independently rederived the EFSSC iff theorem and canonical/physical stabilizer equivalence; checked
      134 source truths, fourteen selector domains (nine strict expansions, five equal, maximum factor 320), seven legal MC0
      globally interleaved schedules, fourteen unrestricted weight-10 mechanisms, atomic transitions, exact iteration-109
      state, and 0/19,016 structural formula differences. No UNSAT, exhaustion, distance-12 witness, universal distance-11
      ceiling, route change, inheritance, or level change is licensed. CIRCDIST.gross and gap-via-lift remain CONJECTURED
      with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_efssc_round86_20260830
      kind: run
    - path: circdist/reviews/circdist_gross_efssc_exact_review_round87_20260830.md
      kind: review
  gross-efssc-frontier-iteration109-2026-08-30:
    date: '2026-08-30'
    type: repair-applied
    summary: 'Canonical frontier bookkeeping synchronized to the reviewed fresh/unstarted iteration 109 state: 14,484 inherited
      sound order blocks, 134 EFSSC selectors, selector-state sha256:9be75eba643ac167d5c51497ca8e5cd23eb1656f803a49cbd8e7f1285b004113
      and preserved unsolved 19,016-assertion formula sha256:94d404da1777ef108a2a508dc55ca0f3fda68bc489482a00337d9acb7317ac4d.
      This records continuation state only and leaves root/route status and D* residual unchanged.'
    sources:
    - path: circdist/artifacts/circdist_gross_efssc_round86_20260830
      kind: run
    - path: circdist/reviews/circdist_gross_efssc_exact_review_round87_20260830.md
      kind: review
  gross-proof-outer-round89-review-2026-08-30:
    date: '2026-08-30'
    type: review-completed
    summary: 'Fresh independent Round-89 review clears the sealed Round-88 finite-outer package at proposer level and licenses
      continuation only from fresh/unstarted iteration 112: 14,484 inherited order blocks, 140 exact EFSSC selectors, selector-state
      sha256:a0364547f846fd68ace7cdba85d89c0f8e6326145243fb0fea7ff543420994cb, and checked-unsolved CNF sha256:a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594
      (398,488 variables; 1,330,104 clauses; 19,022 source assertions). Iterations 109--111 and all six unrestricted direct
      sectors are SAT; their exact physical mechanisms license only six candidate-domain cuts. No Gross UNSAT, direct absence,
      repair, exhaustion, D* narrowing, route change or level change is licensed; CIRCDIST.gross remains CONJECTURED with
      D*_Gross in {11,12}.'
    sources:
    - path: circdist/artifacts/circdist_gross_proof_outer_round88_20260830
      kind: run
    - path: circdist/reviews/circdist_gross_proof_outer_exact_review_round89_20260830.md
      kind: review
```

## 13. Final limitations and delivery state

The next authorized scientific action, if any, begins from the exact sealed iteration-112 CNF. A SAT result needs a complete assignment replay and both unrestricted direct-360 adjudications before any atomic selector transition. An UNSAT result needs a complete accepted DRAT-to-LRAT chain or an independently exhaustive certificate. Repair remains forbidden until both direct sectors have checked absence. Positive SAT evidence cannot be converted into absence or exhaustion.

Protected canonical hashes before and after this review are unchanged:

```text
operations/circdist/SCHEDULER.yaml
  b808ab44bb96b751359548e568469812d3136e10ef91dcb25315389a61eaf957
circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  f42dd0333a8faea3858cefcd859c0343ab33aedf2a6a1e663f2fa1625701288e
package SHA256SUMS.txt
  c4061caff46b632b5c4beb7b6eb33281f3520d07c4dfaaa6eb7c6a33883c7e20
package PAYLOAD_SHA256SUMS.txt
  d2de2f014954070f20bbba0e55caf49aed93b26986a63fab77955a75f62c8157
```

The only durable file written by this reviewer is:

```text
circdist/reviews/circdist_gross_proof_outer_exact_review_round89_20260830.md
```

All reviewer scratch trees and disposable overlays were removed after serialization. All reviewer-launched foreground processes exited and were reaped; no background process was started. No commit and no push were performed.

As with every ordinary content-addressed file, this review cannot contain its own final SHA-256 without changing the bytes being hashed. Its exact post-write byte count, LF-only status, and SHA-256 are computed after the single durable write and reported with delivery. The licensed YAML identity above is non-self-referential and fixed inside this review.
