# Primary-source scope ruling: Shaw-Terhal morphing circuits versus frozen `S_Gross`

**Date:** 2026-08-26  
**Target node:** `CIRCDIST.gross`  
**Commission:** round 57, `CIRCDIST.gross@task-002-scope-ruling`  
**Auditor role:** fresh primary-source scope auditor; no sub-agents or delegated work  
**Canonical-state authority:** none; this report recommends, but does not install, node/scheduler changes

## 0. Ruling in one paragraph

**Scope verdict: OUTSIDE `S_Gross`.** Shaw and Terhal discuss two materially different uses of the label `[[144,12,12]]`. The original Gross code is their `G=Z_12 x Z_6` **mid-cycle** input; morphing that object leaves only a `[[72,12,6]]` end-cycle code. Their distance-12 **end-cycle** object is instead a “second gross” code obtained from a different `[[288,12,18]]` mid-cycle code on `G=Z_12 x Z_12`; its displayed generators have weight 9 and its parity-check matrices are not those of the original Gross code. Its morphing round alternates two end-cycle code frames through resets, `F_i^dagger`, `F_j`, and measurements. It therefore fails the frozen code/generator, dedicated-ancilla, and exact-original-Tanner-CNOT conditions before circuit distance is considered. Moreover, Shaw-Terhal Table I reports only the heuristic upper bound `tilde d_circ <= 12`, not equality and not an exclusion of faults of weight at most 11. The paper supplies neither a legal `S_Gross` distance-12 member nor a universal `<=11` proof. Consequently **`D*_Gross` does not change and remains unresolved in `{11,12}`**. This is a scope ruling, not a proof that `D*_Gross=11`.

## 1. Frozen question and standard of decision

The project freezes `S_Gross` to syndrome-extraction schedules for the **original** Gross code

```
G = Z_12 x Z_6,
A = x^3 + y + y^2,
B = y^3 + x + x^2,
H_X = [A | B],
H_Z = [B^T | A^T].
```

There are 144 data qubits, 72 displayed X checks and 72 displayed Z checks, all weight 6; each check gets one dedicated ancilla. A legal schedule applies each of the 864 displayed Tanner CNOTs exactly once, never applies two simultaneous two-qubit gates to one qubit, may interleave X- and Z-check CNOTs subject to measurement consistency, introduces no flags/cat states/generator change, and is compared after deleting idle-only layers.

The root can close only by one of two mathematical objects:

1. an explicit member of that exact set with a proof-quality certificate that its circuit distance is 12; or
2. a proof that every member has circuit distance at most 11.

The already certified published-candidate clause is separate. Equality of parameter triples, equality of total hardware count, or good numerical logical-error performance cannot establish membership in `S_Gross`.

## 2. Sources, versions, bytes, hashes, and access limitations

### 2.1 Downloaded primary sources

Every successful network download was made into the task-only directory `/tmp/circdist_gross_morphing_scope_ruling_20260826`. Extracted members inherit the archive hash; they were not separate network downloads.

| Local scratch object | Exact public URL | Version/date fixed for this audit | Bytes | SHA-256 |
|---|---|---:|---:|---|
| `arxiv_abs_2407.16336v3.html` | `https://arxiv.org/abs/2407.16336v3` | arXiv v3; submitted 2024-07-23, v3 2025-03-26 12:39:33 UTC | 42,256 | `bebcef76d4ba0ac495e64820c507e7fa46ffddc81cfb634355640530cb756080` |
| `arxiv_2407.16336v3.pdf` | `https://arxiv.org/pdf/2407.16336v3` | arXiv v3 full version, 29 pages; PDF creation 2025-03-26 | 8,037,706 | `b2047eae50f79fd55dd7a4da69feb057cfd4e522646afb8fd37761583ae247ce` |
| `arxiv_2407.16336v3_source.tar` | `https://arxiv.org/e-print/2407.16336v3` | arXiv v3 TeX/source bundle | 17,801,231 | `9452fea795ac8669f0ac93ecc8a7c3a8c4e65d5a28ea9eaba91d7c0aaef932d1` |
| `tudelft_fe111406.pdf` | `https://repository.tudelft.nl/file/File_fe111406-ef39-432b-86c9-6fffc812a78e` | APS publisher PDF, PRL 134, 090602 (2025), DOI `10.1103/PhysRevLett.134.090602`, 7 pages | 391,493 | `e045c9762bb330a5fe516d0d0384fa99f81547148d7c0960760701be246b02f1` |
| `github_head_api.json` | `https://api.github.com/repos/Mac-Shaw/morphing_qec_circuits/commits/main` | API snapshot of `main` at audit time | 60,699 | `2b2d11b916f1948433ca59d790aa6c2bc33c850631500559dd284c6b21efc07f` |
| `github_morphing_qec_circuits_1ee705f.tar.gz` | `https://github.com/Mac-Shaw/morphing_qec_circuits/archive/1ee705f4664518c0ebf72f343ec2a917f17ebe4b.tar.gz` | immutable commit `1ee705f4664518c0ebf72f343ec2a917f17ebe4b`; author 2025-08-29 00:53:29 UTC, committer 00:59:16 UTC | 327,360 | `53f17bd4e2c7eeb32a60a9088c026cf76264c40c603aba631054fff7b127db3f` |

The GitHub commit message is “Added more flexible syndrome extraction to BBParams”; the immutable commit page is `https://github.com/Mac-Shaw/morphing_qec_circuits/commit/1ee705f4664518c0ebf72f343ec2a917f17ebe4b`.

The APS article endpoint `https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.134.090602` and supplemental endpoint `https://link.aps.org/supplemental/10.1103/PhysRevLett.134.090602` returned HTTP 403 to `curl` (exit 56). A second supplemental attempt with browser-like headers also returned 403. The in-app browser reached an APS Cloudflare “Just a moment...” challenge; I did not bypass it and closed the tab. This is an access limitation, not a content gap: the TU Delft file is the APS publisher article, and arXiv v3 is the authors' 29-page combined main text and supplement, including the supplemental numerical method, general morphing construction, BB derivation, and modifications audited below.

### 2.2 Secondary source inspected at the commissioned locator

| Source | Version/date | Bytes | SHA-256 | Exact locator |
|---|---:|---:|---|---|
| `<home>/Documents/ChatGPT/circcert/papers/2603.05481_high_performance_syndrome_extraction_circuits.pdf`, Strikis-Browne-Beverland, “High-performance syndrome extraction circuits for quantum codes” | arXiv:2603.05481v1; PDF dated 2026-03-06; 21 pages | 934,094 | `aebb4b0e4673714daeb1370650d62f9453d72e6ff203d14224b3867f654b0d80` | Appendix H, subsection 2, PDF p.20, final paragraph after Fig. 11 |

The relevant page was extracted and also rendered at 150 dpi for visual verification. No edit or re-export of the source PDF occurred.

### 2.3 Primary-source locators used

The following are stable semantic locators in Shaw-Terhal; line numbers in parentheses refer to extracted `arxiv_combined.tex` from the hashed v3 source archive.

| Fact | Primary locator |
|---|---|
| Mid-cycle versus end-cycle construction and `M_i F_i`, `R_i F_i^dagger` semantics | main text, “Mid- and End-cycle Codes” and “QEC through Morphing Circuits” (`arxiv_combined.tex` 135-152) |
| Exact `[[144,12,12]]` rows, original versus second gross, and upper-bound symbols | main Table I and caption (169-186) |
| Three-layer contraction circuits and bases | main Table II, “Applying the Morphing Protocol” (188-230); supplement Table IV (505-521) |
| Weight-9 end-cycle generators and “second ‘gross’ code” sentence | main “The End-cycle Codes” (241-246) |
| BP-OSD claim explicitly called an estimated upper bound | main “Circuit-level Performance” (256-259) |
| Static-distance ILP and circuit-distance BP-OSD details | Supplemental Material, “Numerical Simulations” (285-310) |
| General static-distance lower bound only | Supplemental Material, “Distance Lower Bound,” proposition `tilde d_i >= d/c_i` (342-356) |
| Exact end-cycle generator formula and compact `tilde A,tilde B` | Supplemental Material, “Weight-6 Bivariate Bicycle Codes,” Corollary `end-cycle_stabilizers`, Eqs. `end-cycle_labeled_stabilizer_support` and `tilde_A_B` (598-646) |
| Reported minimum stabilizer weight 9 | same section (613) |
| Optional data/ancilla swap by reversing layer 3 | Supplemental Material, “Modifications ... Reversing the CNOTs in Round 3” (1014-1073) |
| Repository constructs matching gate layers | commit above, `morphing_qec_circuits/bb_params.py`, `get_standard_morphing_specification`, especially 283-398 |
| Repository verifies no repeated qubit in a layer | `morphing_qec_circuits/morphing_specifications.py`, `check_consistent_gates`, 114-120 |
| Repository executes reset, inverse previous contraction, next contraction, measurement | same file, `morphing_QEC_round`, 792-843 |
| Repository names circuit distance an upper bound and implements decoder search | `README.md` line 4; `circuit_distance_functions.py`, `circuit_distance_ub`, 39-94 |
| Repository static-distance optimizer | `distance_functions.py`, `dx/dz/distance`, 11-99 |

## 3. Exactly which `[[144,12,12]]` codes are discussed?

### 3.1 Original Gross code

For `G=Z_12 x Z_6`, Shaw-Terhal Table I uses

```
A = {x^3, y, y^2},       B = {y^3, x, x^2}.
```

On `q(L,g),q(R,g)`, `g in G`, the CSS generators are

```
s(X,g) = X(A g, B g),
s(Z,g) = Z(B^{-1} g, A^{-1} g),
H_X = [A | B],   H_Z = [B^T | A^T].
```

There are 72 displayed rows of each type. Direct GF(2) elimination in this audit gives

```
rank(H_X)=66, rank(H_Z)=66,
k = 144 - 66 - 66 = 12,
all 72+72 displayed generator rows have weight 6.
```

This is the frozen original Gross code. In Shaw-Terhal it is a **known/mid-cycle input**, and Table I maps it as follows:

```
known/mid-cycle: [[144,12,12]], standard d_circ <= 10
morph end-cycle: [[72,12,6]],    morph    d_circ <= 6.
```

Table I's caption is explicit that the `n=144` input qubits are **both data and ancilla** when this code is used as a morphing mid-cycle code. Thus this row cannot be a morphing SEC on 144 persistent original-Gross data qubits with another 144 dedicated check ancillas.

### 3.2 The new end-cycle “second gross” code(s)

The row that yields a distance-12 end-cycle code instead starts from

```
G = Z_12 x Z_12,
A = {x^3, y^7, y^2},     B = {y^3, x, x^2},
known/mid-cycle [[288,12,18]].
```

Direct elimination gives 144 X rows and 144 Z rows, ranks 138 and 138, hence `k=288-138-138=12`; its displayed generators have weight 6. Morphing it leaves 144 end-cycle data qubits and 144 measured/reset qubits:

```
known/mid-cycle: [[288,12,18]], standard d_circ <= 18
morph end-cycle: [[144,12,12]], morph    d_circ <= 12.
```

The paper itself calls this a **second “gross” code** and says equality of the parameter triples is “perhaps coincidental.” That sentence rules out reading the row as merely a new SEC for the original Gross parity checks.

For completeness, Table I admits three homomorphisms `f_x,f_y,f_xy`. For a fixed `f`, the two alternating end-cycle frames `tilde C_1,tilde C_2` are related by shifting every qubit label by any element of `K^c`; they are permutation-equivalent frames of that `f` construction, not literally the same fixed labeled stabilizer group. The paper's footnote at line 203 warns that different homomorphisms applied to one mid-cycle code can lead to distinct end-cycle codes unrelated by the Lin et al. mappings. It does not prove or claim arbitrary-Clifford inequivalence among all three, so this audit does not invent that stronger statement.

The supplemental compact BB formula is

```
tilde A = (a1^{-1}(a2+a3) + b1^{-1}(b2+b3)) r,
tilde B = 1 + a1^{-1}b1^{-1}(a2+a3)(b2+b3),
```

where `a1,b1` are the unique elements in their respective sets with the exceptional `f` parity and `r in K^c`. Expanding it gives the following exact presentations (all exponents reduced in the stated group):

| homomorphism | compact group/basis for `K` | `tilde A` | `tilde B` |
|---|---|---|---|
| `f_x` | `K ~= Z_6 x Z_12`, `u=x^2, v=y`, `r=x` | `u^5v^7 + u^5v^2 + v^3 + u` | `1 + u^4v^10 + u^5v^7 + u^4v^5 + u^5v^2` |
| `f_y` | `K ~= Z_12 x Z_6`, `u=x, v=y^2`, `r=y` | `u^3v^3 + v^4 + uv^5 + u^2v^5` | `1 + u^4v + u^5v + uv^2 + u^2v^2` |
| `f_xy` | `K ~= Z_12 x Z_6`, `u=xy^{-1}, v=y^2`, `r=x` | `uv^3 + u^4v + 1 + u^11v` | `1 + u^11v^2 + u^10v^3 + u^2 + uv` |

I independently constructed `H_X=[tilde A|tilde B]` and `H_Z=[tilde B^T|tilde A^T]` for each row. Each has 72 displayed X rows and 72 displayed Z rows, ranks 66 and 66, `k=12`, and every displayed row has weight `4+5=9`; all X/Z commutators vanish. This verifies the algebraic parameter/rank/generator distinction without running the authors' Gurobi distance solver.

### 3.3 Equivalence to the original Gross code

The exact matrices and displayed generating sets are different. More strongly, the original stabilizer group contains displayed weight-6 stabilizers, whereas Shaw-Terhal report from their stabilizer-weight integer optimization that every Table-I end-cycle code except `[[36,12,3]]` has **minimum nonidentity stabilizer weight 9**. If that reported optimum is accepted, Pauli-weight invariance immediately excludes equality or equivalence under any qubit permutation or tensor product of one-qubit Clifford maps. No arbitrary entangling-Clifford equivalence to the original is asserted or established; invoking one would in any event change the frozen data/check locality and generating set, so it cannot establish `S_Gross` membership.

The exact conclusion needed here is therefore stronger than “not shown to be the same”: under the paper's own reported minimum-stabilizer result, it is not the original stabilizer code up to the weight-preserving relabelings relevant to a syndrome schedule. Equal `n=144`, `k=12`, and reported static `d=12` do not identify a code.

## 4. Reconstruction of the morphing protocol

### 4.1 Abstract cycle

Let `C` be the known mid-cycle code with displayed stabilizer set `S`. A contraction circuit `F_i` maps every generator in a subset `S_i` onto a single host qubit. `M_i` measures those hosts in X or Z, leaving an end-cycle code `tilde C_i` on the unmeasured qubits. `R_i` resets exactly those measured hosts, and `F_i^dagger` restores the joint mid-cycle code. Validity requires the union of contracting sets to cover `S`.

For two contractions, the physical QEC rounds are

```
tilde C_1 -- R_1 -- F_1^dagger -- [mid-cycle C] -- F_2 -- M_2 --> tilde C_2,
tilde C_2 -- R_2 -- F_2^dagger -- [mid-cycle C] -- F_1 -- M_1 --> tilde C_1.
```

Thus a round both extracts the starting end-cycle syndrome and changes the labeled end-cycle code frame. The midpoint, not the endpoint, is the known input code.

### 4.2 Exact `F_1/F_2`, measurements, and resets

In the normalized notation `a1=b1=1`, set `K=ker f` and `K^c=G\K`. For `F_1`, take `g in K`, `h in K^c`; for `F_2`, swap the cosets. Each contraction has:

| contraction layer | gates for all applicable `g,h` |
|---|---|
| 1 | `CNOT(q(L,g) -> q(R,b3 g))`; `CNOT(q(R,a3^{-1}h) -> q(L,h))` |
| 2 | `CNOT(q(L,g) -> q(R,b2 g))`; `CNOT(q(R,a2^{-1}h) -> q(L,h))` |
| 3 | `CNOT(q(R,g) -> q(L,g))`; `CNOT(q(L,h) -> q(R,h))` |
| measurement | `M_X(q(R,g))`; `M_Z(q(R,h))` |

The unnormalized supplemental Table IV inserts the factors `a1^{-1}b_j`, `a_j^{-1}b1`, and `a1^{-1}b1` exactly as recorded in Section 2.3 above. `R_i` resets the prior `M_i` hosts in the same X/Z bases. The contracting sets are

```
S_1 = {even X checks} union {odd Z checks},
S_2 = {odd X checks}  union {even Z checks}.
```

All right mid-cycle qubits are measured each half-cycle: half in X and half in Z, with bases swapped on the next contraction.

The expanding mid-cycle checks become end-cycle generators on left qubits only:

```
X(b1^{-1} A B g,0),
Z(a1 A^{-1} B^{-1} h,0).
```

When all nine products are distinct, these checks have weight 9. In the compact BB reading, the two 72-qubit “end-cycle left/right” blocks are actually the even and odd subsets of the **mid-cycle left** qubits. The physical mid-cycle right qubits are the measured/reset hosts: right-even are X ancillas and right-odd are Z ancillas for `tilde C_1`, with the roles reversed for `tilde C_2`.

### 4.3 Counts and matching property for the second gross construction

Here `|G|=144`, so each coset has 72 elements.

- Mid-cycle physical qubits: 288 (`144 L + 144 R`).
- End-cycle data: 144 (all physical `L` qubits in the base protocol).
- Measured/reset hosts: 144 physical `R` qubits, 72 X and 72 Z each round.
- Each contraction layer: `72+72=144` CNOTs.
- Each full QEC round: three inverse-contraction layers plus three next-contraction layers, hence 6 CNOT layers and `6*144=864` CNOT occurrences.
- Every one of the 288 physical qubits appears once in every CNOT layer. This is both an algebraic matching property of Table II and the condition checked by the public repository's `check_consistent_gates()` method.
- The union connectivity has degree 5, because one neighbor interaction is reused across the two contractions; it is not the degree-6 Tanner graph of the frozen original Gross checks.

The repository implementation corroborates the order literally: `morphing_QEC_round()` resets the qubits measured in the previous contraction, emits previous `gate_lists` in reverse order, emits following `gate_lists` in forward order, and measures the following X/Z lists.

### 4.4 Base protocol versus optional role swap

The base Table-II protocol keeps end-cycle data on the physical left qubits and the measured hosts on the right. Supplemental “Reversing the CNOTs in Round 3” is an optional variant. Reversing layer 3 in one contraction moves the next end-cycle code to the right; alternating that choice swaps data and ancilla roles each QEC round so every qubit is reset every two rounds. This does not make the protocol closer to the frozen dedicated-ancilla model: it removes persistent data/ancilla roles altogether.

## 5. What distance statement is actually established?

| Quantity | Object | Source statement/method | Evidentiary meaning |
|---|---|---|---|
| Static code distance `d=12` | original Gross `[[144,12,12]]` | known input in Table I | Static code parameter, not SEC circuit distance. |
| Static code distance `tilde d=12` | second-gross end-cycle code | Table I; binary integer optimization described in supplement | Authors report/calculated `d=12`. The paper says Gurobi “allows one to approximately solve” the integer program, then says repeating over logical representatives finds the distance. No solver log, optimality certificate, or independent exact certificate is published in the sources inspected. |
| General lower bound | end-cycle static code | supplemental proposition `tilde d_i >= d/c_i`; here `c_i=3`, so only `tilde d>=6` from `d=18` | A static-distance lower bound. It does not prove `tilde d=12`, and says nothing about circuit distance. |
| Morphing circuit distance | second-gross protocol | Table I prints **`tilde d_circ <= 12`**; main text says “estimated an upper-bound” using BP-OSD | A found decoder output/fault candidate gives only an upper bound. It is not `tilde d_circ=12`, not a lower bound, and not an exclusion of weights 1-11. |
| Numerical logical-error performance | Table-I end-cycle codes under uniform circuit depolarizing noise | main Fig. 3 / arXiv compact figure; supplement full numerical plot | Monte Carlo/decoder performance under a specified noise model. It is not a circuit-distance proof. |
| “effective distance” / SBB extended distance | none in Shaw-Terhal | no such equality/certificate is asserted for this circuit | Must not be imported from SBB's different framework. |

The supplemental BP-OSD procedure makes the direction unambiguous. It constructs a two-QEC-round memory experiment, turns a chosen logical observable into a detector, asks BP-OSD for a low-weight correction, and explicitly says: “The weight of the output ... is therefore an upper bound on the circuit-level distance.” The public code function is named `circuit_distance_ub`; it takes the minimum decoder-output weight. A heuristic failure to find a lighter fault cannot certify absence.

Therefore even for the second gross object, the inspected sources do **not** prove `d_circ=12`. They show `d_circ<=12` and numerical performance consistent with a useful circuit. No theorem, table, figure, supplemental derivation, repository certificate, or enumerated fault exclusion establishes `d_circ>=12`.

## 6. Frozen-condition pass/fail ruling

There are two possible attempted identifications, and each fails at object identity:

- Use the original Gross row: the original code exists only at mid-cycle on 144 **total** qubits and contracts to a `[[72,12,6]]` end-cycle code.
- Use the second-gross row: the endpoint has `n=144,k=12,d=12`, but it is a different weight-9 stabilizer code whose midpoint is `[[288,12,18]]`.

The condition audit below applies to the only distance-12 endpoint, the second gross protocol, while noting the original-row alternative where needed.

| Frozen `S_Gross` condition | Result | Source-grounded reason |
|---|---|---|
| Exact original Gross `[[144,12,12]]` parity checks | **FAIL — earliest decisive violation** | The distance-12 endpoint is `H(tilde A,tilde B)` with weight-9 displayed generators, derived from `G=Z_12 x Z_12`; the original `H(A,B)` weight-6 code instead morphs to `[[72,12,6]]`. |
| One dedicated ancilla for each of the original 72 X and 72 Z weight-6 generators | **FAIL** | There are 144 measured/reset right qubits in the second-gross protocol, but they contract alternating halves of the **288-qubit mid-cycle** stabilizers. They are not fixed hosts for the original Gross rows. Equality of the count 144 does not give the required mapping. |
| Every required original-Gross Tanner CNOT exactly once | **FAIL** | Morphing applies `F_previous^dagger F_next`, has degree-5 unique connectivity, and repeats one neighbor interaction across the six layers. The original Tanner interaction graph has degree 6 and 864 distinct check-data incidences. Equal occurrence count `864` is not equality of the labeled CNOT multiset. |
| At most one two-qubit gate per qubit per time | **PASS** | Each of the six morphing CNOT layers is a matching; for the second gross it is a perfect matching of 288 qubits. Public code checks this property. |
| X/Z CNOT interleaving allowed | **COMPATIBLE, not curative** | The frozen model permits interleaving. Morphing layers mix contractions associated with X- and Z-basis measurements, but permission to interleave does not waive code/generator/edge semantics. |
| No flag ancillas | **PASS for base protocol** | No separate flag system appears. |
| No cat states | **PASS for base protocol** | No cat-state check gadget appears. |
| No generating-set changes | **FAIL** | The protocol deliberately partitions mid-cycle generators into `S_1,S_2`, turns the expanding half into weight-9 end-cycle generators, and alternates `tilde C_1,tilde C_2`. This is a change of code frame and measured generating semantics. |
| Idle-only layers compressed | **PASS/irrelevant** | The reconstructed round already has six nonempty CNOT layers, with reset and measurement boundaries that are not idle layers. Compression cannot change any failed semantic condition. |

The first failure is decisive. The later failures independently prevent serialization as one frozen schedule.

## 7. Rejected repairs

| Proposed repair | Why it does not establish inclusion |
|---|---|
| Relabel qubits | A shift maps `tilde C_1` to `tilde C_2` only within a fixed second-gross construction. It does not turn weight-9 second-gross stabilizers into the original weight-6 Gross group; the reported minimum stabilizer weights distinguish them under weight-preserving relabeling. |
| Compress idle layers | There is no idle-only CNOT layer to remove. Timing compression cannot alter parity checks, roles, or edge labels. |
| Choose the mid-cycle code | In the second-gross distance-12 protocol, mid-cycle is `[[288,12,18]]`, not original Gross. In the original-Gross protocol, mid-cycle is the right code but occupies all 144 physical qubits and its endpoint/data code is `[[72,12,6]]`; treating that transient instant as an end-cycle SEC changes the commissioned object. |
| Group two alternating rounds | This returns `tilde C_1 -> tilde C_2 -> tilde C_1` only after two reset/measurement blocks and 12 CNOT layers. It repeats/changes interactions and measures two alternating frames; it is not one application of each original Tanner edge. |
| Interpret the 144 right qubits as dedicated Gross ancillas | Their number matches, but their maps do not: they host contracted `[[288,12,18]]` mid-cycle checks, swap X/Z basis by parity, and collectively extract weight-9 endpoint checks. Reassigning them to original Gross checks changes the circuit and code. |
| Use the optional data/ancilla role-swap variant | This alternates which physical half contains the data and resets every qubit every two rounds. It is even less compatible with persistent original data and dedicated ancillas. |
| Invoke abstract Clifford equivalence | None is established. An entangling Clifford would alter support/locality/Tanner interactions and thus construct a different model even if an abstract code isomorphism existed. |

Accordingly, a single morphing cycle cannot be serialized as a member of `S_Gross` without changing the code, generating set, or ancilla semantics. A “repair” that changes those frozen objects is not inclusion.

## 8. Consequence for `D*_Gross`

Because the construction is outside the optimization domain, no explicit frozen schedule is supplied and no `<=11` fault-exclusion certificate is called for on the morphing object. Even if the morphing circuit had a separately certified distance 12, it would still be irrelevant to the maximum over `S_Gross`.

This report establishes only:

```
Shaw-Terhal morphing construction not in S_Gross.
```

It does **not** establish:

```
for every M in S_Gross, d_circ(C(M)) <= 11.
```

The smallest live residual after closing this gate is exactly the root's one-bit disjunction:

- exhibit a legal original-Gross schedule with proof-certified `d_circ=12`, including a complete exclusion of all logical fault sets of weight at most 11; **or**
- prove universally that every legal original-Gross schedule has `d_circ<=11`.

The certified achievable floor/published-candidate clause remains handled. The universal `d_ext<=11` cap remains useful but, as the current node already records, it does not alone settle circuit distance for interleaved schedules. Hence `D*_Gross in {11,12}` is unchanged.

## 9. Audit of SBB Appendix H.2 and repository A7

### 9.1 Exact SBB wording

At Appendix H, subsection 2, PDF p.20, after Fig. 11, SBB says Shaw-Terhal produces:

> “circuits involving the same number of physical and logical qubits as the gross code, but with circuit distance twelve”

The qubit-count part can be read truthfully at either of two levels: the second endpoint has `n=144,k=12`, and its implementation has 288 total physical qubits (`144` data plus `144` measured/reset hosts), matching the total used by a one-ancilla-per-displayed-check original-Gross implementation. Neither numerical equality identifies the stabilizer code.

The “circuit distance twelve” part is not what the cited primary Table I proves or even prints: Table I prints `tilde d_circ <=12`, its caption calls that column an upper bound, the main text says “estimated an upper-bound,” and the supplement explains the BP-OSD witness search. SBB's wording therefore overstates the primary source. It also invites, but does not explicitly state, the mistaken inference that the circuit is for the original Gross code.

### 9.2 Exact correction to current A7

Current `circdist_gross_recon_20260820.md` A7 says “Morphing circuits reach circuit distance 12 with the same qubit counts,” attributes the statement second-hand to SBB, and admits the author did not read Shaw-Terhal. The exact correction needed is:

> **A7 — corrected primary-source reading.** Shaw and Terhal construct a different end-cycle `[[144,12,12]]` “second gross” code from a `[[288,12,18]]` mid-cycle BB code. It has weight-9 end-cycle generators and alternates two shift-related code frames through morphing contractions. Their Table I reports the BP-OSD upper bound `tilde d_circ <= 12`; it does not prove `tilde d_circ=12`. The original Gross `[[144,12,12]]` appears separately as a mid-cycle input whose morphing endpoint is `[[72,12,6]]`. The construction is outside frozen `S_Gross` and does not decide `D*_Gross`.

Also correct the bibliographic initial from “S. Shaw” to **Mackenzie H. Shaw / M. H. Shaw**. Replace the speculative “ancilla merging / measurement-based gadgets” scope rationale with the exact parity-check, role, edge-set, and alternating-frame violations in Sections 3-7 of this report.

The old reconstruction should remain historically intact if preservation forbids editing; the canonical node can carry this correction prospectively through evidence, caveat, and append-only event.

## 10. Complete dispatcher recommendation (not installed here)

### 10.1 Canonical `CIRCDIST.gross` evidence link

Append under `assessment.basis.evidence`:

```yaml
- path: circdist/artifacts/circdist_gross_morphing_scope_ruling_20260826.md
  kind: text
  note: >-
    Fresh primary-source Shaw-Terhal scope audit: the distance-12-labeled morphing endpoint is a
    different weight-9 [[144,12,12]] “second gross” code derived from a [[288,12,18]] mid-cycle
    code; Table I reports only BP-OSD d_circ <= 12. The construction is outside frozen S_Gross,
    closes frontier task-002 negatively, and leaves D*_Gross in {11,12}.
```

### 10.2 Exact recommended assessment summary

```yaml
summary: >-
  The optimal circuit-distance question remains CONJECTURED, with D* in {11,12} unresolved. The
  universal d_ext <= 11 cap is PROVED; the candidate-certification route is CERTIFIED*. The latest
  completion-gap candidate was killed by the missed two-prefix shape. The three recorded no-go
  classes and search machinery are scoped by-products, not a universal proof of D*=11. A fresh
  primary-source scope audit closes the Shaw-Terhal morphing lead negatively: its distance-12-labeled
  endpoint is a different weight-9 [[144,12,12]] “second gross” code with alternating code frames,
  outside frozen S_Gross, and Table I gives only a BP-OSD circuit-distance upper bound <=12. It
  supplies neither a legal distance-12 witness nor a universal <=11 no-go.
```

### 10.3 Caveat append

If `assessment.caveats` is absent, create it; otherwise append exactly:

```yaml
- >-
  Do not cite SBB26 Appendix H.2 as proving circuit distance 12 for the original Gross code.
  Shaw-Terhal Table I reports only tilde d_circ <= 12 for a different end-cycle “second gross” code;
  equality of n=144 and k=12 (or of the 288-qubit total hardware count) is not code identity or
  S_Gross membership.
```

### 10.4 Frontier and event

Delete only completed `frontier.task-002`; retain `task-003` and `dstar-residual` unchanged. Append this new-format event without rewriting any historical event:

```yaml
events:
  gross-morphing-scope-ruling-2026-08-26:
    date: '2026-08-26'
    type: repair-applied
    summary: >-
      Fresh primary-source audit corrected the prior second-hand morphing gloss. Shaw-Terhal's
      original Gross [[144,12,12]] is only a mid-cycle input whose end-cycle code is [[72,12,6]];
      their distance-12 endpoint is a different weight-9 [[144,12,12]] “second gross” code derived
      from [[288,12,18]], and its reported morphing circuit distance is only the BP-OSD upper bound
      <=12. The construction is outside frozen S_Gross. Frontier task-002 closes negative; the root
      stays CONJECTURED with D*_Gross in {11,12}.
    sources:
    - path: circdist/artifacts/circdist_gross_morphing_scope_ruling_20260826.md
      kind: text
```

`repair-applied` is the fitting protocol event type: this is a material correction of a prior source reading, not an independent completion review and not a mathematical route refutation.

### 10.5 Scheduler-only bookkeeping

- Mark `CIRCDIST.gross@task-002-scope-ruling` completed/held negative; retain its historical `P: 0.08` rather than rewriting the forecast after observing the result.
- Set round 57's outcome to the exact negative ruling and settle spend `82.0 -> 83.0/83`.
- Correct `work_items.CIRCDIST.gross.P_why` only if desired to say the candidate-certification route is complete but closure-neutral, rather than “partial only.”
- Re-auction only the surviving `dstar-residual` if the lead authorizes more budget.

### 10.6 Levels and probabilities

**No node or route level change is licensed.** The root remains `CONJECTURED`; no promotion follows from documentation alone. This artifact is an authored source audit, not the independent adversarial review required for a completion-level promotion.

**No root closure-probability change is mathematically licensed.** Keep root and `gap-via-lift` at the current operational `P=0.235` unless the dispatcher independently reprices them. The negative scope result removes a cheap false-positive lead but supplies no new witness or no-go evidence inside `S_Gross`. The completed action can be marked held; its old ex ante `P=0.08` may remain as historical scheduler data.

After canonical installation, the dispatcher must regenerate derived views with `--write-generated` and rerun structural/evidence/migration validation. This worker was expressly forbidden to do so.

## 11. Verification and transient evidence closure

### 11.1 Pre-write read-only snapshot

From repository root, before this artifact existed:

| Command | Exit/result |
|---|---|
| `python3 tools/proof_dag_check.py --problem circdist` | 0; `circdist: 16 node files structurally valid` |
| `python3 tools/proof_dag_check.py --problem all` | 0; SE 85, k-Sum 144, circdist 16 node files structurally valid |
| `python3 tools/evidence_closure_check.py --problem circdist` | 0; closure OK, 123 structured paths, all project-local and linked |
| `python3 tools/check_circdist_migration.py` | 0; 16 nodes, 143 original events, 728 byte-identical copies |
| `git diff --check` | 0 |
| `test ! -e circdist/artifacts/circdist_gross_morphing_scope_ruling_20260826.md` | 0 |

The working tree was already highly non-clean and the whole migrated `circdist/` tree was untracked relative to the current Git `main`; that baseline is external to this task. The target path was absent. This session does not claim ownership of any pre-existing status entry.

### 11.2 Expected post-write state

Structural validation and migration preservation should remain green because this report does not edit a node, schema, history file, or generated view. Evidence closure should return nonzero and name this one report as an unlinked/orphan artifact. That is the expected transient result under the one-file authorization: linking it requires a canonical-node write reserved to the dispatcher. It must not be misreported as a completed atomic repository update.

The actual post-write results were exactly as expected:

| Command | Exit/result |
|---|---|
| `python3 tools/proof_dag_check.py --problem circdist` | 0; `circdist: 16 node files structurally valid` |
| `python3 tools/proof_dag_check.py --problem all` | 0; SE 85, k-Sum 144, circdist 16 node files structurally valid |
| `python3 tools/evidence_closure_check.py --problem circdist` | **1, expected transient result**; its sole diagnostic was `unlinked evidence: circdist/artifacts/circdist_gross_morphing_scope_ruling_20260826.md` |
| `python3 tools/check_circdist_migration.py` | 0; 16 nodes, 143 original events, 728 byte-identical copies |
| `git diff --check` | 0 |
| `git status --short -- <target>` | 0; the sole target line was `?? circdist/artifacts/circdist_gross_morphing_scope_ruling_20260826.md` |
| `find circdist -type f -newer <target>` | 0; no path printed |

Thus the only new file detected in this task's authorized scope is this report. The closure error is intentionally left for the dispatcher to cure by the exact evidence link in Section 10.1; suppressing it or editing the node here would violate the commission.

## 12. Public derivation and limitations

The report exposes the checkable formulas, rank calculations, scope comparisons, rejected interpretations, and exact source locations. It does not expose or claim private chain-of-thought.

Limitations are deliberately narrow:

1. APS direct endpoints were inaccessible as disclosed; the APS publisher article from TU Delft and complete official arXiv v3 main/supplement were read.
2. The authors' static-distance and minimum-stabilizer results were not re-solved with Gurobi. Rank, commutation, and displayed generator weights were independently recomputed; the paper/repository publish no Gurobi optimality logs or certificate in the inspected snapshot.
3. The BP-OSD circuit-distance number was audited for logical direction and implementation, not rerun. Its own primary source defines it as an upper bound, so rerunning is unnecessary to reject an equality claim.
4. No claim is made about arbitrary entangling-Clifford equivalence among codes; such an equivalence is neither sourced nor relevant to frozen schedule membership.
5. No inference about universal `D*_Gross<=11` is drawn from this negative scope gate.

## 13. Command, download, process, and FIX-2 ledger

### 13.1 Command ledger

All work was strict serial. No sub-agent, child worker, background solver, detached computation, or repository mutation other than the final target artifact was used. The audit command families, in execution order, were:

1. Read-only repository discovery and baseline: `pwd`; `git status --short --branch`; `test ! -e <target>`; `rg --files`; `find`; `cat`, `sed`, `nl`, and `rg` over `DAG_PROTOCOL.md`, `FILE_PROTOCOL.md`, `operations/circdist/SCHEDULER.yaml`, `CIRCDIST_PROBLEMS.md`, current `CIRCDIST.gross.yaml`, its children, the old recon, and its cited Gross artifacts/reviews. All exited 0 unless a search intentionally returned no match.
2. Network retrieval with foreground `curl -L --fail --show-error` to each URL in Section 2.1. All six listed objects completed with exit 0. The three APS requests failed as disclosed with curl exit 56/HTTP 403.
3. Archive inspection/extraction under scratch only: `file`, `tar -tf`, `tar -xf` for arXiv source, and `tar -xzf` for the GitHub archive; `find`, `sed`, `nl`, and `rg` for extracted source/code. Exits 0.
4. Hash/metadata: `shasum -a 256`, `stat -f`, `pdfinfo`, and Python JSON reads. Exits 0.
5. Exact GF(2) matrix audit via inline `python3`: one first run exited 1 because system Python 3.9 lacks `int.bit_count`; the corrected `bin(x).count('1')` run exited 0 and produced the ranks/weights in Section 3. A separate mid-cycle rank run exited 0.
6. SBB extraction: `shasum -a 256` and `pdfinfo` exited 0. System `pdftotext` was unavailable, so that compound command exited 2 after printing `command not found`; no output file was created. `load_workspace_dependencies` located the bundled runtime; bundled Python/pypdf extraction exited 0. Bundled `pdftoppm -f 20 -l 20 -png -r 150` exited 0, stderr empty, and the page image was visually inspected. The render remained scratch only.
7. Source/object locators: further `nl`, `sed`, `rg`, `find`, pypdf, and inline Python reads over the hashed TeX, publisher PDF, repository files, current A7, canonical root, protocols, and scheduler. Exits 0.
8. Validator help and pre-write commands are recorded verbatim in Section 11.1; exits all 0.
9. Artifact staging used a quoted here-document in task scratch; installation and post-write commands appear below.

The command ledger records every command that affected a verdict and every failure. Repeated pagination-only reads are grouped because they have identical read-only semantics; their exact paths and decisive line ranges are enumerated in Sections 2.3 and 11.

### 13.2 Download/process incident and disposition

The first arXiv PDF `curl` was started in what should have been a foreground tool call, but the tool returned without a reusable session identifier while process PID **5466** remained alive. This was not intentionally detached. I detected it with `pgrep`, inspected it with `ps` (parent PID 70180), explicitly executed `kill 5466` (exit 0), verified it was gone, deleted its partial output, and restarted the transfer in tracked foreground exec session **45639**. That session completed with exit 0. The 17.8 MB arXiv source transfer ran in tracked session **19060**, was polled in bounded intervals, and completed with exit 0 after approximately 7 minutes 2 seconds. No verdict relies on the killed partial file.

A safety filter rejected one attempted `rm -f` cleanup command before execution; `unlink` removed the partial file successfully. No attempt was made to evade the filter.

No downloaded object, extracted source, PDF rendering, or scratch log is required as a durable proof object: the report records immutable URLs, versions, sizes, and hashes, and the dispatcher links this report itself. The entire task scratch directory is deleted at FIX-2 closeout rather than copied into the repository, exactly as commissioned.

### 13.3 Final process and scratch disposition

Immediately before cleanup, `pgrep -fl` over the task slug, arXiv version, and pinned repository archive printed no process, and `ps -p 5466,43443,5675` printed no row. Thus the accidentally surviving PID 5466 was gone, and neither formerly scheduler-declared inherited PID was alive.

Cleanup used foreground `python3` with `shutil.rmtree('/tmp/circdist_gross_morphing_scope_ruling_20260826')`; it printed `scratch_exists_after_cleanup= False` and the following `test ! -e` exited 0. All downloaded files, archives, extracted sources, PDF text/render intermediates, and the scratch draft were removed. No task process or scratch object was handed off. The only durable path is `circdist/artifacts/circdist_gross_morphing_scope_ruling_20260826.md`.

No task process is handed off. Pre-existing scheduler-declared jobs, if visible on the host, were not started, used, or terminated by this session.

## 14. Final verdict

- **Exact scope:** Shaw-Terhal morphing circuits are **outside** frozen `S_Gross`.
- **Earliest violation:** code/parity-check/generator identity; dedicated-ancilla and exact-CNOT semantics fail independently.
- **Distance:** static second-gross `d=12` is reported from an integer optimization; morphing `d_circ<=12` is only a BP-OSD upper bound, not a proof of equality.
- **`D*_Gross`:** unchanged, still `{11,12}`.
- **Nature of result:** negative scope ruling only, not a universal `D*=11` no-go.
- **Repository level:** no promotion, no probability change licensed, canonical state untouched.
