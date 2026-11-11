# CIRCDIST.gross — D* hunt 3 (round 61): corrected four-shape audit and the residual after two counterexample attacks

**Date:** 2026-08-28  
**Commission:** strict-serial round 61, one worker, no sub-agents  
**Target:** `CIRCDIST.gross#gap-via-lift`  
**Authorship status:** proposer-level. This report does not promote a node and does not license promotion. Any exact-root result still requires a fresh independent adversarial review.  
**Public reasoning note:** this document gives the definitions, reductions, equations, case boundaries, certificates, commands, outputs, failures, and decision criteria used in the round. It does not claim to disclose private hidden chain-of-thought.

## 0. Verdict

# **3) NOT CLOSED**

The exact root residual remains

\[
D^*_{\mathrm{Gross}}\in\{11,12\}.
\]

Neither integer has been eliminated.

The strongest new result is a pair of explicit, independently rebuilt counterexample attacks on tempting but invalid completion screens:

1. **Four-positive-shape cleanliness is not sufficient for `d_eff >= 11`.** I give a legal, measurement-consistent, interleaved three-colour-tiled schedule for which all four individually gain-positive `|V|=12` shapes are absent in both CSS sectors and every length-2, length-3, and length-4 hook is diagonal, yet an explicit five-hook plus five-singleton configuration has weight 10 and nontrivial logical residual. The missed mechanism uses all seven reduced per-check options, including individually zero/negative-gain options whose outside support cancels across checks.
2. **All-diagonal hooks plus a clean bounded `|V|=12` stratum is not sufficient for a completion gap.** I give a second legal, measurement-consistent, interleaved schedule with all 432 audited length-2/3/4 hooks diagonal and no weight-`<=10` configuration in the complete `|V|=12`, at-most-four-contributing-check stratum in either sector, but with same-round `repair=0` certificates in both sectors for canonical weight-11 effective logicals. On the three colour representatives the census is 22/40 repair-zero in the X-error/Z-memory sector and 18/30 in the Z-error/X-memory sector.

These are no-go results for two **filters**, not a universal no-go over `S_Gross`. They do not narrow `{11,12}`.

My updated, explicitly heuristic prices for one further comparable round are:

| branch | probability of closing in one comparable round | reason |
|---|---:|---|
| explicit reviewed-ready `D*=12` witness | **0.05** (from 0.10) | corrected necessary order screens can be met, but the first bounded-stratum survivor had repair zero in 40/70 representative canonical mechanisms; higher-logical strata and complete repair-zero exclusion remain untouched |
| reviewed-ready universal `D*=11` proof | **0.20** (from 0.15) | the new separations strengthen the structural tension, but no lossless partition of all `S_Gross` has been found |
| neither | **0.75** | exact quantification remains the dominant obstacle |

These are planning estimates, not mathematical probabilities.

## 1. Disk state, scope, and hash bindings

Disk agreed with the commission on the mathematical state. The current canonical root is `CONJECTURED`; its summary says that the wave-37 candidate was killed by the missed fourth shape and that the three no-go classes are scoped by-products rather than a universal proof. The scheduler authorizes round 61 on the corrected residual. One operational discrepancy was found: the scheduler's FIX-2 registry still lists historical PIDs `43443` (`drive10.py`) and `5675` (`drive7.py`), but neither process existed when checked. I treated the live process table as authoritative and did not touch unrelated processes.

The exact statement hashes, using `SHA256(claim.replace("\r\n","\n").strip().encode("utf-8"))`, are:

| object | characters | exact SHA-256 |
|---|---:|---|
| `CIRCDIST.gross` claim | 586 | `fc22f602b9bfd9e38fa69d7fc1d00b973c7a634e6c400662eaccd38c8ec0f180` |
| route `candidate-certification` implication | 300 | `4f40673227208c58d21650b3d685670019f5460b44ee52c0440b22293eec1598` |
| route `gap-via-lift` implication | 279 | `915109fe708c63ce138b11d07aa87c3048d676c87d9d6b7a80d68c0e2025c5d1` |
| `CIRCDIST.gross.dext-cap` claim | 148 | `4bc0b5eb3b74b174e60f641357f5bea5b9e6a4240c390ced1bf8fd17746bff42` |
| `CIRCDIST.lift.iff` claim | 544 | `0c4c466b895d938d2028140967d87974ee2216b3cebcc48967804f530e227240` |

The current governing/source file hashes read at the start were:

```text
DAG_PROTOCOL.md                                      d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095
FILE_PROTOCOL.md                                     d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595
operations/circdist/SCHEDULER.yaml                    786d06d74ec29359d000bd3b91071c6788cddbfd889bd57c2b1d2b9d4bc21a87
circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md   5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64
circdist/proof-dag/nodes/CIRCDIST.gross.yaml          dd8a9b94d674951f0cc24ac8ad235888bd086e1ffe3bc3364b34fd1bb9292d32
circdist/proof-dag/nodes/CIRCDIST.gross.dext-cap.yaml a2c89dac0a66bee9f4055fece6d7d4e032203ca2ad38d8a70c071ff7afc16f0d
circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml        7b7929628c48e7c75997d33661989ed61e7bf83ca775802d807f211a224b3a68
circdist/artifacts/circdist_dstar_hunt1_20260823.md    d6d104c20d28c3fe29a3dd2cf53cfe50f3cc3cadc852e46c6ea00fc5ff4f4671
circdist/artifacts/circdist_dstar_hunt2_20260823.md    01f9e79226495ad837ecb8fa08066b4d96a2d7078e385d5831d827ddb6ba82da
hunt1 preserved SHA256SUMS.txt                         733fe555ff885b105c09625594079430b8dc80a8e3d49dd0836dffb3c8b14c9b
hunt2 preserved SHA256SUMS.txt                         862974e15286113a5ed58e76e6ff31d9717e8d2e221bb1e052381d0ac4b5086d
```

The two imported exhaustive weight-12 seed files were re-expanded and every resulting word was checked for weight, zero syndrome, and non-stabilizer status:

```text
w12X.txt  1460a15c2ae372fa602fca810aa05bf9fb62426aba121b84931d8fec5c3d6697
w12.txt   981be6c7aa8a42ab00a8925007a4a0567724ab7b46bd157383087f18b0af8125
expanded pool: 1884 nontrivial weight-12 logicals per sector
```

Pool **completeness** is inherited from the independently reviewed wave-36 meet-in-the-middle enumeration. This round revalidated all members but did not independently re-prove completeness from no imported data.

## 2. Exact quantified schedule space

Let `G = Z_12 x Z_6`, `|G|=72`, with

\[
A=x^3+y+y^2,\qquad B=y^3+x+x^2,
\]
\[
H_X=[A\mid B],\qquad H_Z=[B^T\mid A^T].
\]

There are 144 data qubits, 72 X ancillas, 72 Z ancillas, and 864 required CNOT edges. Every vertex in the combined data-check incidence graph has degree six.

A raw schedule is a surjective time map

\[
t:E_{\rm CNOT}\to\{0,\ldots,T-1\}
\]

such that incident edges have distinct times. Surjectivity is idle-layer compression. It executes every one of the 864 named CNOTs exactly once and gives one two-qubit gate per qubit per time. The remaining frozen conditions exclude flags, cats, and generator changes. X/Z interleaving is allowed.

For the standard repeated-check detector model, a physically valid schedule must also be measurement-consistent. Every nonempty X-check/Z-check overlap has exactly two data qubits. If X check `a` and Z check `b` overlap on `{q1,q2}`, the condition used throughout the reviewed lift dossier and all Gross computations is

\[
[t_Z(q_1,b)<t_X(a,q_1)]\oplus[t_Z(q_2,b)<t_X(a,q_2)]=0. \tag{MC}
\]

The frozen six-bullet list does not spell out `(MC)` as a lexical subclause of “legal”, but the current campaign treats non-MC schedules as invalid syndrome-extraction circuits because their nominal repeated-round detectors are non-deterministic. A universal theorem must state this convention explicitly rather than silently switching it.

### 2.1 Lossless and non-lossless normal forms

The following reductions are lossless for the full quantifier:

- relabel used times increasingly to `0,...,T-1` (idle compression);
- translate all group labels by a fixed element of `G` (a code automorphism);
- apply a proved CSS mirror only while swapping the two memory sectors and all corresponding definitions.

The following are **not** lossless normal forms for all `S_Gross`:

- minimum depth or six CNOT layers;
- translation-invariant schedules;
- three-colour-tiled schedules;
- left-right circuits;
- check-serial/global-potential schedules;
- fixed within-check order classes such as `M_cand`;
- any bounded number of contributing hook checks;
- any bounded logical residual weight such as `|V|=12`.

Therefore no result below is called universal unless it quantifies over the raw schedule space above.

## 3. Reconstructed prior state and review status

### 3.1 What is proved/reviewed

1. **Universal extended-distance cap.** `CIRCDIST.gross.dext-cap` is `PROVED`: every schedule has a physical 2-suffix hook; every two-subset of every check lies in an explicit weight-12 logical; the hook plus ten singleton columns gives `d_ext<=11`. The proof is schedule-independent and applies to interleaved schedules.
2. **Closed-lift criterion.** `CIRCDIST.lift.iff` is `PROVED` at the exact current hash. For `R>=d_sec`,
   \[
   d_{\rm circ}=d_{\rm eff}\iff
   \exists\gamma\in L_{\rm eff},\ |\gamma|=d_{\rm eff},\ \operatorname{repair}(\gamma)=0.
   \]
   Thus, with the spatial ceiling 12, a schedule with `d_eff=11` and no repair-zero minimum effective logical has `d_circ=12`.
3. **Published candidate.** The reconstructed noninterleaved `M_cand` has `d_ext=11` in both sectors at `CERTIFIED*`, and SBB Theorem 1 was independently verified only in its noninterleaved scope. It gives the achieved floor `D*>=11`.
4. **SBB scope.** SBB Theorem 1 is not used anywhere below for an interleaved schedule. Its equality statement is unavailable there.
5. **Shaw-Terhal.** The “second gross” morphing construction is outside frozen `S_Gross` and supplies no in-scope evidence for either exact branch.

### 3.2 Hunts 1 and 2

Hunt 1 built a repair decider and found a legal MC-clean tiled schedule with no repair-zero member of its **canonical** minimum family under a two-shape `d_eff<=10` filter. Hunt 2 found that the filter omitted two of the four individually positive shapes and killed the candidate in both sectors with raw-verified weight-10 configurations. It also recorded:

- **Lemma D (proposer):** `d_eff` depends only on within-check orders, not absolute times;
- 297 sampled interleaved retimings of `M_cand` orders, all killed by horizontal hooks;
- a warning that a pair-only implementation of the corrected filter remained insufficient.

The stage-2 kill is secure because its 144 displayed configurations were independently rebuilt from raw CNOT times and translated into the campaign's 360-column model. The absence-side bounded enumerations remain proposer computations.

### 3.3 The three existing no-go walls and Lemma D

| item | exact scope | status this round | does it cover all `S_Gross`? |
|---|---|---|---|
| check-serial/global-potential Theorem B | schedules whose pair orientation comes from one global check potential | short algebraic derivation is persuasive, but artifact and current root leave it proposer-level; no fresh independent review | **no** |
| “fully TI cannot keep `d_eff=11` both sectors” | hunt-1 sample of 400 legal+MC TI schedules; the old 25,920 minimum-depth TI class is entirely non-MC | numerical sample, not an exhaustive theorem over all TI depths, much less all schedules | **no** |
| 297 `M_cand` retimings | sampled linear extensions preserving one certified order class | sampled no-go only; it does not quantify over every retiming or other orders | **no** |
| Lemma D | every retiming preserving all within-check orders | follows directly from the definition of residual columns; strong proposer lemma, not independently reviewed as a standalone claim | transfers `d_eff`, but says nothing universal about repair or timing feasibility |

Their union is not a partition. A schedule can be non-check-serial, non-TI, outside the `M_cand` order class, and still belong to `S_Gross`. No missing lossless case split was found. Consequently these walls cannot be assembled into a universal `D*=11` proof.

## 4. Re-derivation of the extended-code search and all four positive shapes

Fix one sector. Let a within-check order be `i1,...,i6`, earliest to latest. The physical suffix of length `l` is `S_l={i_{7-l},...,i6}`. Modulo the check stabilizer and singleton domination, the 360-column model has 144 singleton columns and three residual representatives per check:

\[
\{i_1,i_2\},\quad \{i_4,i_5,i_6\},\quad \{i_5,i_6\}.
\]

For exact physical repair data, the first representative is realized by the physical 4-suffix, not by a fictional prefix fault.

For a fixed nontrivial logical `V`, let `K_a subset {2,3,4,5}` be the set of suffix lengths selected on check `a`, `n_a=|K_a|`, and `C_a` their XOR. Let `D=xor_a C_a`. The remaining singleton set is `T=V xor D`, so

\[
\operatorname{cost}=\sum_a n_a+|V\oplus D|. \tag{4.1}
\]

Length 6 can be deleted modulo the check stabilizer and length 1 is dominated by a singleton. If `|C_a|-n_a<=0`, dropping that check does not raise the cost. The seven surviving per-check options are:

| `K_a` | positions in `C_a`, counted from the end | `n_a` | `|C_a|` |
|---|---|---:|---:|
| `{2}` | `{1,2}` | 1 | 2 |
| `{3}` | `{1,2,3}` | 1 | 3 |
| `{4}` | `{1,2,3,4}` | 1 | 4 |
| `{5}` | `{1,2,3,4,5}` | 1 | 5 |
| `{2,5}` | `{3,4,5}` = `{i2,i3,i4}` | 2 | 3 |
| `{2,3,5}` | `{1,2,4,5}` | 3 | 4 |
| `{3,4,5}` | `{1,2,3,5}` | 3 | 4 |

At `|V|=12`, the bound

\[
|V\cap\operatorname{supp}(a)|\le 3
\]

follows because `V xor supp(a)` is in the same logical class and must have weight at least 12. For a single option, its improvement over twelve singleton faults is

\[
g_a=2|C_a\cap V|-|C_a|-n_a. \tag{4.2}
\]

The complete list with `g_a>0` has **four** shapes:

| physical/reduced shape | gain |
|---|---:|
| 3-suffix `{i4,i5,i6} subset V` | 2 |
| 2-suffix `{i5,i6} subset V` | 1 |
| physical 4-suffix with exactly three entries in `V`, equivalently the two-prefix `{i1,i2}` in the stabilizer-shifted weight-12 logical | 1 |
| `{i2,i3,i4}=S_2 xor S_5 subset V` | 1 |

The third row is the historically missed “two-prefix = four-suffix modulo stabilizer” case. Every filter used this round includes all four rows.

However, equations (4.1)-(4.2) also show why the four rows are not sufficient. If several options overlap outside `V`, individually nonpositive options can cancel their outside support and have positive **combined** gain. The seven-option exhaustion is therefore the required bounded-stratum check.

## 5. Independent formulations and controls

### 5.1 Clean-room 360-column SAT formulation

I independently formulated `d_ext<=W` as follows. For one sector let `c_j` be the 360 singleton/residual data masks, and select Boolean variables `x_j` with `sum x_j<=W`. Set

\[
e=\bigoplus_j x_jc_j.
\]

Require the opposite-check syndrome to vanish and require at least one of twelve independently rebuilt logical dual parities to be one:

\[
H_{\rm det}e=0,\qquad \bigvee_{r=1}^{12}\langle \ell_r,e\rangle=1. \tag{5.1}
\]

XOR chains were Tseitin-encoded, and a sequential counter encoded the cardinality. A second version introduced 144 explicit `e_q` variables, the sound cut `|e|>=12`, and the exact dominance clauses forbidding simultaneous 3-suffix and 2-suffix columns of one check. This is independent of the campaign's cell/orbit/lex-minimal encoding.

Structural controls completed:

```text
rank(HX)=66, rank(HZ)=66, k=12
logical complement dimensions: 12 and 12
X/Z logical pairing rank: 12
extended columns: 360 per sector
```

The hard known-candidate `W=10` UNSAT control did **not** complete in the timebox. It was interrupted after approximately four foreground minutes with no verdict. Shorter W37 and z-cut trials were also interrupted without verdict. No solver summary from those stopped runs is used as evidence.

Environment created only in external scratch:

```text
python-sat 1.9.dev15
z3-solver 5.1.0.0
solver called: CaDiCaL 1.9.5 through python-sat
```

### 5.2 Independent bounded combinatorial checker

A separate standard-library checker rebuilt the code and schedule without importing hunt1/hunt2 modules. It enumerated the seven options above, used (4.1) as the final test, and enforced distinct contributing checks in its bounded decomposition. It reduced the complete reviewed 1884-word pool by the colour-preserving translation subgroup only after explicitly checking each orbit; there are 88 orbits per sector, with orbit sizes summing to 1884.

Negative control on the wave-37 schedule:

```text
legal True; MC violations 0
all length-2/3/4 hooks diagonal in both sectors
four-positive-shape bad logicals: 48 X-error, 48 Z-error
complete |V|=12, <=4-check bad logicals (orbit-weighted): 96 X-error, 60 Z-error
first witnesses agree in shape with hunt2: 4-suffix + 2-suffix
```

The counts are bad **logical words**, not hunt2's configuration counts, so equality to hunt2's 72/72 is neither expected nor claimed. The decisive mechanism agrees.

A code-reading precision note: hunt2's recursive implementation describes depth as “distinct contributing checks” but does not explicitly reject selecting two pre-combined options from the same check. Such selections can be normalized by symmetric-differencing their suffix-length sets and deleting duplicate fault locations, so this creates duplication/looser bookkeeping rather than invalidating the separately raw-verified 144 kill witnesses. This round's checker enforced distinct checks directly.

## 6. Counterexample C1: the four-shape screen is insufficient

This is a diagnostic counterexample, **not** a proposed distance-12 candidate.

### 6.1 Complete raw schedule definition

Use colour `phi(i,j)=(i+j) mod 3`. The 36 integers are ordered as

```text
[XL[c][0..2] for c=0..2,
 XR[c][0..2] for c=0..2,
 ZL[c][0..2] for c=0..2,
 ZR[c][0..2] for c=0..2].
```

For X check `g` of colour `c`, assign its three left edges `g+A_r` times `XL[c][r]` and its three right edges `72+g+B_s` times `XR[c][s]`. For Z check `g`, assign left edges `g-B_s` times `ZL[c][s]` and right edges `72+g-A_r` times `ZR[c][r]`. This formula names every required CNOT exactly once.

The schedule vector is

```text
T_C1 = [19,14,10, 6,13,7, 11,8,3,
        24,35,5, 18,30,16, 12,31,4,
        20,0,21, 9,2,17, 25,1,23,
        28,27,32, 33,22,15, 29,34,26]
```

Within-check slot orders, earliest first, are:

```text
X colours 0,1,2:
  (5,2,1,0,3,4)  (0,2,1,5,3,4)  (2,5,1,0,3,4)
Z colours 0,1,2:
  (1,0,2,4,3,5)  (1,0,5,2,4,3)  (1,2,0,5,3,4)
```

### 6.2 Raw audit

| condition | result |
|---|---:|
| X CNOTs / Z CNOTs | 432 / 432 |
| required CNOTs exactly once | yes |
| incident-gate time conflicts | 0 |
| used layers | exactly `0..35` (36/36; no empty layer) |
| MC violations | 0 / 648 overlapping check pairs |
| overlap-interleaved pairs | 312 / 648 |
| whole-check-interleaved pairs | 648 / 648 |
| globally X/Z interleaved | yes |
| length-2/3/4 hooks, X-error sector | 216 diagonal, 0 horizontal, 0 vertical/trivial |
| length-2/3/4 hooks, Z-error sector | 216 diagonal, 0 horizontal, 0 vertical/trivial |
| four-positive-shape bad logicals | 0 in each sector |

### 6.3 Explicit weight-10 certificate

The failing sector is the Z-error/X-memory sector. Take

```text
V = {10,18,19,26,34,50,66,67,76,78,100,102}.
```

The checker verifies `|V|=12`, `H_X V=0`, and `V` is outside `rowspace(H_Z)`.

Use five physical hook faults:

| Z check | selected suffix lengths `K` | XOR residual `C_a` | raw CNOT order `(qubit,time)` |
|---:|---|---|---|
| 7 | `{5}` | `{10,67,78,83,133}` | `(1,1),(67,23),(10,25),(83,26),(133,29),(78,34)` |
| 31 | `{2,5}` | `{19,34,102}` | `(25,0),(34,20),(19,21),(102,27),(85,28),(107,32)` |
| 6 | `{3}` | `{66,83,132}` | `(0,2),(9,9),(82,15),(66,17),(83,22),(132,33)` |
| 62 | `{4}` | `{50,116,132,133}` | `(56,0),(65,20),(50,21),(133,27),(116,28),(132,32)` |

Their XOR is

```text
D = {10,19,34,50,66,67,78,102,116}.
```

Add the five singleton faults

```text
V xor D = {18,26,76,100,116}.
```

Therefore the total fault count is `5 hooks + 5 singletons = 10`, and the net extended residual is exactly `V`. Every check equation and logical-class test was recomputed from the polynomials. This is a checkable upper-bound certificate `d_eff<=10` in that sector.

The individual gains reveal why the four-shape filter misses it:

```text
check 7,  K={5}:   individual gain  0
check 31, K={2,5}: individual gain +1
check 6,  K={3}:   individual gain -2
check 62, K={4}:   individual gain -3
combined gain: +2
```

The negative individual options cancel qubits 83, 132, and 133 outside `V`. Thus:

> **Proposer Theorem C1.** In the frozen Gross geometry, absence of all four individually gain-positive `|V|=12` shapes, even together with legality, `(MC)`, full X/Z interleaving, and diagonality of every length-2/3/4 hook in both sectors, does not imply `d_eff>=11`.

The theorem is existential and its certificate is above. It says nothing universal about `S_Gross`.

## 7. Counterexample C2: bounded `d_eff` cleanliness and all-diagonal hooks do not imply a gap

This is also diagnostic, not an exact-root candidate.

### 7.1 Schedule and audit

```text
T_C2 = [16,10,14, 6,1,8, 13,9,5,
        23,35,12, 17,32,11, 18,34,4,
        20,0,22, 7,2,15, 26,3,24,
        30,25,27, 33,21,19, 29,31,28]
```

Within-check slot orders:

```text
X colours 0,1,2:
  (1,5,2,0,3,4)  (1,0,2,5,3,4)  (5,2,1,0,3,4)
Z colours 0,1,2:
  (1,0,2,4,5,3)  (1,0,2,5,4,3)  (1,2,0,5,3,4)
```

The raw audit is identical in its geometry counts to C1:

```text
864/864 named CNOTs; 0 conflicts; layers exactly 0..35;
MC 0/648; overlap-interleaved 312/648; whole-check-interleaved 648/648;
216/216 length-2/3/4 hooks diagonal in each sector; no horizontal/vertical/trivial hook.
```

All four positive shapes are absent in both sectors. More strongly, the seven-option checker found **no** weight-`<=10` configuration in either complete bounded stratum

```text
|V| = 12, V in the complete 1884-word pool,
at most four distinct contributing hook checks,
all seven reduced per-check options,
both CSS sectors.
```

This is a complete finite statement only for the displayed stratum. It excludes neither `|V|>=14` nor configurations needing five or more contributing checks.

### 7.2 Same-round repair-zero census

Despite all hooks being diagonal, canonical weight-11 mechanisms have repair zero:

| sector | representative canonical mechanisms tested | same-round `repair=0` |
|---|---:|---:|
| X errors / Z memory | 40 | 22 |
| Z errors / X memory | 30 | 18 |

The representatives consist of the physical 2-suffix and physical 4-suffix/two-prefix families on one check of each colour, with every reviewed weight-12 logical containing the corresponding pair. Colour-preserving translations transport the certificates to the other checks.

Two explicit certificates follow. For a singleton qubit `q`, `k in {0,1,2,3}` selects the `k`-element suffix of its three detector-gate order; the listed `u` masks XOR with the hook `u` to zero. All faults are in one round, so cumulative syndrome `C=0` and this equality is exactly `repair=0`.

**X-error/Z-memory certificate.** X check 0 has order

```text
(1,10),(84,12),(2,14),(18,16),(75,23),(78,35).
```

Use its physical 2-suffix `{75,78}` and singleton set

```text
{1,5,9,11,12,16,72,76,77,82}.
```

The hook voltage is `{5,21}`. Singleton suffix choices in the displayed singleton order are

```text
k = (1,0,1,0,0,3,0,2,0,1).
```

Their nonzero `u` masks are

```text
q=1  -> {13}
q=9  -> {21}
q=16 -> {13,22,28}
q=76 -> {5,22}
q=82 -> {28}
```

whose XOR is `{5,21}`, canceling the hook.

**Z-error/X-memory certificate.** Z check 0 has order

```text
(66,0),(3,20),(60,22),(77,25),(76,27),(126,30).
```

Use its physical 2-suffix `{76,126}` and singleton set

```text
{2,10,26,42,43,58,66,67,78,124}.
```

The hook voltage is `{48,70}`. All singleton choices are `k=0` except `q=66`, for which the X-detector gate order is

```text
(71,1),(48,13),(70,14)
```

and `k=2` gives `u={48,70}`, canceling the hook.

Therefore:

> **Proposer Theorem C2.** Legality, `(MC)`, full interleaving, all-diagonal length-2/3/4 hooks, absence of all four positive shapes, and even exact cleanliness of the complete `|V|=12`, at-most-four-check stratum do not imply absence of `repair=0` among canonical weight-11 effective logicals.

Again this is a theorem about the insufficiency of a screen, not the value of `D*`.

## 8. Why neither exact branch closes

### 8.1 Distance-12 branch

An exact interleaved witness needs all of the following in both sectors:

1. raw schedule legality, idle compression, and `(MC)`;
2. `d_eff=11`, meaning **every** effective logical of weight at most 10 is absent, across all logical residual weights and all hook counts;
3. every minimum-weight effective logical has nonzero repair, with arbitrary round-group assignments covered, not just same-round or two-group tests;
4. the reviewed lift criterion then gives `d_circ>11`, and the sector spatial ceiling gives `d_circ=12`;
5. whole-circuit distance is the minimum of the two sector distances, so both sectors are load-bearing.

C1 fails item 2 by certificate. C2 passes only a bounded part of item 2 and fails item 3 in both sectors. No exact candidate survives this report.

### 8.2 Universal distance-11 branch

A universal proof must show for every compressed, conflict-free, MC-valid time map on all 864 edges that at least one sector has either

\[
d_{\rm eff}\le10,
\]

or, if `d_eff=11`, a minimum-weight `gamma` with `repair(gamma)=0`. The check-serial, sampled-TI, and sampled-`M_cand` walls do not form a lossless partition. C1 and C2 also show that several natural local case labels do not decide the alternatives. No universal decomposition or checkable exhaustive certificate was produced.

## 9. Smallest exact residual and concrete next action

The exact residual cannot honestly be made smaller than the two-point set `{11,12}`. Its sharpest structural form is:

\[
\boxed{\exists M\in S_{\rm Gross}^{\rm MC}:\ d_{\rm eff}^X(M)=d_{\rm eff}^Z(M)=11
\ \text{and every minimum effective logical in both sectors has repair}>0?}
\]

A “yes” gives `D*=12`; a “no”, proved over the full schedule space, gives `D*=11`.

The next action should be one integrated **schedule/mechanism CEGAR certificate**, not another heuristic filter:

1. schedule variables encode all 864 edge times (or a proved lossless order/orientation quotient), conflict constraints, compression, and `(MC)`;
2. an adversary query uses the direct 360-column formulation to return any weight-`<=10` effective logical in either sector;
3. if none exists, a second adversary query returns any weight-11 effective logical with exact arbitrary-round `repair=0`;
4. every returned mechanism becomes a checked blocking clause on schedule/order variables;
5. a surviving schedule is then certified by proof-producing UNSAT for both adversaries; exhaustion of the outer schedule formula would instead be a universal no-go certificate.

A three-colour-tiled implementation is useful for development but must remain labelled a subclass. It cannot close the universal branch.

## 10. Reproduction fragments and decisive outputs

The following fragments contain the load-bearing conventions. They are sufficient to regenerate every raw CNOT time from either `T_C1` or `T_C2`, audit conflicts/MC, and verify the C1 cost certificate. The complete scratch programs were exploratory and were deleted at close; no claim depends on an unavailable solver verdict.

```python
L, M, G, N = 12, 6, 72, 144
A = ((3,0),(0,1),(0,2))
B = ((0,3),(1,0),(2,0))

def gi(i,j): return (i % L)*M + (j % M)
def add(g,u):
    i,j = divmod(g,M)
    return gi(i+u[0],j+u[1])
def colour(g):
    i,j = divmod(g,M)
    return (i+j) % 3

Xslot = [[add(g,a) for a in A] + [G+add(g,b) for b in B] for g in range(G)]
Zslot = [[add(g,(-b[0],-b[1])) for b in B]
         + [G+add(g,(-a[0],-a[1])) for a in A] for g in range(G)]

def build(T):
    XL=[T[3*c:3*c+3] for c in range(3)]
    XR=[T[9+3*c:12+3*c] for c in range(3)]
    ZL=[T[18+3*c:21+3*c] for c in range(3)]
    ZR=[T[27+3*c:30+3*c] for c in range(3)]
    tX,tZ={},{}
    for g in range(G):
        c=colour(g)
        for i,q in enumerate(Xslot[g][:3]): tX[g,q]=XL[c][i]
        for j,q in enumerate(Xslot[g][3:]): tX[g,q]=XR[c][j]
        for j,q in enumerate(Zslot[g][:3]): tZ[q,g]=ZL[c][j]
        for i,q in enumerate(Zslot[g][3:]): tZ[q,g]=ZR[c][i]
    assert len(tX)==len(tZ)==432
    return tX,tZ

# MC on every nonempty two-qubit overlap.
def mc_violations(tX,tZ):
    bad=[]
    for a,Arow in enumerate(Xslot):
        for b,Brow in enumerate(Zslot):
            sh=sorted(set(Arow)&set(Brow))
            if sh:
                assert len(sh)==2
                if ((tZ[sh[0],b] < tX[a,sh[0]]) !=
                    (tZ[sh[1],b] < tX[a,sh[1]])):
                    bad.append((a,b))
    return bad

# Exact seven per-check options after the length-6 and length-1 reductions.
def position_set(K):
    return tuple(p for p in range(1,6)
                 if sum(l >= p for l in K) % 2)
KSETS=[]
for r in range(1,5):
    for K in itertools.combinations((2,3,4,5),r):
        P=position_set(K)
        if len(P)-len(K)>=1:
            KSETS.append((K,P))
assert len(KSETS)==7

# Exact cost of a proposed bounded-stratum configuration.
def configuration_cost(V, order, chosen):
    D=0; hooks=0
    for a,K in chosen:
        P=position_set(K)
        C=mask(order[a][6-p] for p in P)
        D ^= C
        hooks += len(K)
    return hooks + popcount(V ^ D)
```

Search/control command record, all foreground:

```text
python3 -m venv /tmp/circdist_gross_hunt3_20260828_r61/venv
.../python -m pip install --disable-pip-version-check python-sat z3-solver
.../python independent_sat.py controls                    # stopped; no verdict
.../python search_tiled.py                               # W37 control completed
.../python search_tiled.py anneal 61 3000 w37            # C1 found
.../python cegar.py                                      # C2 found after two cuts
.../python audit_candidate.py                            # C2 repair census completed
.../python search_repair.py                              # stopped at iteration 342
```

Decisive output excerpts:

```text
C1:
edges 864 legal True MC 0 pair_interleaved 312 whole_interleaved 648 layers 36 0 35
hooks X {diagonal:216,horizontal:0,vertical:0,trivial:0}
hooks Z {diagonal:216,horizontal:0,vertical:0,trivial:0}
four_bad_X 0 four_bad_Z 0
full_j4_Z first: cost 10, [(7,{5}),(31,{2,5}),(6,{3}),(62,{4})]

C2:
edges 864 legal True MC 0 pair_interleaved 312 whole_interleaved 648 layers 36 0 35
full_j4_X none; full_j4_Z none
CANON X total_reps 40 repair0 22
CANON Z total_reps 30 repair0 18

stopped final exploratory repair anneal:
BEST seed 7001 iteration 342 score 11500, representative repair0 23,
cut penalty 0, base four-shape/hook/MC score 0; interrupted, no schedule serialized,
no mathematical verdict attached.
```

## 11. Assumptions and limitations

- The frozen Gross code and circuit fault inventory are the shared model. This round independently rebuilt the algebra but shares the same model interpretation as prior work.
- Completeness of the 1884-word weight-12 pools is imported from the reviewed wave-36 exhaustive enumeration; members were revalidated here.
- The seven-option `|V|=12`, at-most-four-check results are exact only in that finite stratum.
- Same-round repair-zero certificates are sound existence witnesses. Their absence would not exclude multi-round repair zero; this report uses only positive certificates.
- No completed SAT UNSAT verdict, LRAT/DRAT object, or universal schedule enumeration was obtained.
- No result from SBB Theorem 1 is applied to an interleaved schedule.
- Nothing from the out-of-scope Shaw-Terhal second-gross morphing construction is used.

## 12. Read-only validation and sealing

After writing the report and without regenerating views, I ran:

```text
$ python3 tools/proof_dag_check.py --problem circdist
circdist: 16 node files structurally valid
exit 0

$ python3 tools/evidence_closure_check.py --problem circdist
ERROR: circdist: unlinked evidence: circdist/artifacts/circdist_dstar_hunt3_20260828.md
exit 1
```

The first result validates the extant canonical CIRCDIST node graph. The second is a precise, expected scope failure: this new proposer report is unlinked because the commission forbids editing the canonical Gross node or any other repository file. It is not evidence-closure clean until a later authorized process links or adjudicates it; this round does not do so.

The scratch tree was then deleted with `shutil.rmtree`; an independent `Path.exists()` check printed `scratch_exists False`. A process-table search for the scratch path and every round-61 executable name returned no match (exit 1 from `rg`), so no declared or undeclared round-61 computation remained alive at sealing.

## 13. FIX-2 file and process accounting

- **Repository writes:** exactly one new durable file, this report: `circdist/artifacts/circdist_dstar_hunt3_20260828.md`.
- **Canonical state:** no node, route, scheduler, protocol, prior artifact/review, generated view, or tool was edited.
- **Pre-existing worktree state:** the repository was already dirty/untracked because of the current migration and unrelated edits. Those objects were not modified by this round.
- **Sub-agents/delegation:** none.
- **Background/detached work:** none. Every process was attached to a foreground tool session.
- **Completed foreground work:** virtual-environment creation/install, code/pool rebuilds, bounded enumerations, schedule anneals, CEGAR steps, and audits.
- **Stopped foreground work:** the hard known-candidate SAT control (about four minutes, no verdict), shorter W37/z-cut SAT controls (no verdict), and the final repair anneal at iteration 342. Each was stopped with keyboard interrupt and is non-evidential except for its recorded frontier.
- **Inherited scheduler processes:** PIDs 43443 and 5675 were absent; no inherited process was killed or modified.
- **Scratch:** `/tmp/circdist_gross_hunt3_20260828_r61/` contained the only temporary code, logs, virtual environment, and exploratory JSON. It was deleted before handoff and independently verified absent.
- **Handoff compute:** none.

## 14. Required final line

# **3) NOT CLOSED, with exact residual `D*_Gross in {11,12}`.**
