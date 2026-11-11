# Independent review: Werner two-boundary planar rooted-map repair

Date: 2026-08-30

Reviewer: independent Codex review context `/root/planar_repair_audit`.

Independence declaration: this reviewer did not author
`WERNER_TWO_BOUNDARY_PLANAR_ROOTED_MAP_REPAIR_20260830.md`. The review reconstructed the deletion
code from the halfedge-permutation model, checked the bridge, loop, parallel-edge, coincident-corner,
root, and automorphism cases, and audited the assembled Werner route against its current canonical
premises. It used no web access, no external enumeration formula, no large computation, and made no
canonical YAML change.

## 1. Executive verdict

The self-contained planar deletion code **PASSES**. It proves the exact current claim of
`HEXT.werner-planar-two-boundary-rooted-map-count` at
`sha256:0f07c313c810842eb7e0eb912962eea4b0895adedaa10ba4cac9dea0aaaf42c8`.
The proof covers the unique-cycle loop, a two-edge parallel core, longer cores, a root bridge at any
depth, coincident deletion corners, and the zero-edge intermediate tree. There is no missing
automorphism divisor or root multiplier.

The repaired four-premise implication in
`HEXT.werner-two-boundary-constellation-count` also **PASSES** at its exact route hash
`sha256:64b8e9fb8161425c5f94b416af059f8e5ce623c14bc58f3fa7137198a5f1bc99`.
Together with the current `PROVED` premises, it proves the unchanged structural target claim at
`sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603`, with the explicit
choice `D=32768` and `alpha=43` for every fixed integer `m>e^18`.

Accordingly, protocol-complete integration may promote:

1. `HEXT.werner-planar-two-boundary-rooted-map-count` to `PROVED`;
2. only the route `repaired-rooted-two-face-map-code` to `PROVED`; and
3. `HEXT.werner-two-boundary-constellation-count` to `PROVED`, supported only by that repaired
   route.

The earlier route `rooted-two-face-map-code` must remain `CONJECTURED` with its false planar
coefficient and negative review preserved. This finding does **not** promote
`HEXT.same-tuple-werner-centered-bound`, any equality-component result, the two-component sector,
or any centered or full-size extensive-violation result.

The malformed display near equation (19) in the repair artifact is presentation-only: the raw text
omits the TeX commands before `le` and `qquad`. Its intended inequality is explicit from the two
neighboring sentences, equation (20), the already reviewed positive-genus premise, and the exact
route implication. No canonical statement or hash contains the malformed display.

## 2. Inspected objects and immutable hash lock

The file digests below are SHA-256 of the exact inspected bytes.

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `artifacts/WERNER_TWO_BOUNDARY_PLANAR_ROOTED_MAP_REPAIR_20260830.md` | `f4cd879af9d05ec88b2e94ab6e0c8d183b1248bd483d11d916b101189297ef73` |
| `artifacts/WERNER_TWO_BOUNDARY_CONSTELLATION_WEIGHTED_COUNT_20260830.md` | `f4d0b8b92366c0aa353b3f7794c9a0b1a5326aa0602ecc9323f6f9a9e51a8bab` |
| `reviews/WERNER_TWO_BOUNDARY_CONSTELLATION_WEIGHTED_COUNT_INDEPENDENT_REVIEW_20260830.md` | `ce0f613f8b3f3377a0c2c02357b9fe7423939746d624386078fc32a01da8f8ba` |
| `nodes/HEXT.werner-planar-two-boundary-rooted-map-count.yaml` | `d5090b532aa36a6324f7255f410b1e364cd13741b7e842554215c80df80bfa59` |
| `nodes/HEXT.werner-two-boundary-constellation-count.yaml` | `6abd8ab1acf090bc178c2d593c1c72370cf3919591782c8d2d77a79cb0b13c01` |
| `nodes/HEXT.werner-positive-genus-two-boundary-weighted-count.yaml` | `359840c8a2cb6aa5578845a7de449c4eff011816c8a32337b2d85afe76362260` |
| `nodes/HEXT.werner-contraction-skeleton-ribbon-injection.yaml` | `b6f5c1c9b2ae73901cec858f1883fa2e455fbad1c7ae3ee302395133079cbf0a` |
| `nodes/HEXT.werner-minimal-catalan-weight.yaml` | `b04ed45a51a164e343e54fa2e616bf971a12fc852bf689ca3aa46e4e4e7af57e` |
| generated `proof-dag/NODE_INDEX.md` | `6a295c0052930e8808a97393b429b1cc3b86469c22309c65cace7eda5b5b1511` |
| generated `proof-dag/GRAPH.mmd` | `e8867607facaceffff9c0a7cee172d371385de478ad7cdad30c55fd5219adfa7` |

Statement hashes use the repository rule `sha256(statement.strip())` after YAML folding and CRLF
normalization.

| statement | exact hash | verdict |
|---|---|---|
| singly rooted lemma quoted in repair Section 11.1 | `sha256:99b4fc8a1b6c08ed9a36942e4f9012a7dc1e42b5820c14a926b83de65cd09ce6` | PASS |
| `HEXT.werner-planar-two-boundary-rooted-map-count` claim | `sha256:0f07c313c810842eb7e0eb912962eea4b0895adedaa10ba4cac9dea0aaaf42c8` | PASS; may promote |
| `HEXT.werner-positive-genus-two-boundary-weighted-count` claim and `rooted-tree-cotree-code` implication | `sha256:300c642a7cab1717445a387e793666fa416ead65bd0731f9be684701d8f30cf6` | unchanged `PROVED` premise |
| `HEXT.werner-contraction-skeleton-ribbon-injection` claim | `sha256:288e0f5df3ca6a53915325c487648184b9be0ff950c1e52c5db7689468c730f7` | unchanged `PROVED` premise |
| `HEXT.werner-minimal-catalan-weight` claim | `sha256:82a54db26f9887fab15962f597b42c9d9b7c5a50b2dc86c713e0b066cc51cf54` | unchanged `PROVED` premise |
| repaired route `repaired-rooted-two-face-map-code` implication | `sha256:64b8e9fb8161425c5f94b416af059f8e5ce623c14bc58f3fa7137198a5f1bc99` | PASS; may promote |
| `HEXT.werner-two-boundary-constellation-count` claim | `sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603` | PASS through the repaired route; may promote |
| old route `rooted-two-face-map-code` implication | `sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603` | remains `CONJECTURED`; its proof artifact is defective |

The repository structural checker independently recomputed these YAML statement bindings and
reported all 138 project nodes structurally valid at the final audit check.

## 3. Findings

### Finding WTPR-IR-01 — PASS: unicyclic structure and canonical selected edge

**Applies to:** singly rooted lemma hash
`sha256:99b4fc8a1b6c08ed9a36942e4f9012a7dc1e42b5820c14a926b83de65cd09ce6`
and planar node claim hash
`sha256:0f07c313c810842eb7e0eb912962eea4b0895adedaa10ba4cac9dea0aaaf42c8`.

For a connected planar map with `e` edges and two faces, Euler gives `V=e`, so the underlying
connected multigraph has cyclomatic number `e-V+1=1`. In a connected pseudograph this means that
the non-bridge edges form exactly one circuit: a loop, a two-edge parallel circuit, or a simple
cycle of length at least three. Every other edge lies in a tree attached to a core vertex. Deleting
one core edge therefore leaves a connected graph with `e` vertices and `e-1` edges, hence a tree.
This argument does not assume simplicity.

The selector in repair Section 5 is total and invariant.

- If the root edge is a bridge, its endpoint depths from the core differ by one. The nearer
  endpoint and its unique path determine the incoming halfedge at the first core vertex. Positive
  rotation then determines the first core halfedge. If the bridge is incident directly to the
  core, its core-side root-edge halfedge is exactly that incoming halfedge. If the core is a loop,
  either encountered loop halfedge names the same edge.
- If the root lies on a core of length at least two, its directed head vertex has exactly one other
  incident core edge. This edge differs from the root even for a two-edge parallel core.
- If the root is the one-edge core loop, the selector necessarily chooses the root edge itself.

Graph distance, the named directed root, and the positive rotations are all preserved by rooted
orientation-preserving isomorphisms. Thus two isomorphic inputs cannot select different edge
orbits. The selected edge equals the root precisely in the rooted one-loop-core case, so Classes I
and II are disjoint and exhaustive.

**Verdict:** PASS.

### Finding WTPR-IR-02 — PASS: both deletion decoders, Catalan convention, and automorphisms

**Applies to:** the same singly rooted and planar statement hashes as Finding WTPR-IR-01.

In Class I, deleting the non-root selected edge leaves a directed-halfedge-rooted plane tree with
`n=e-1` edges. The two deleted positions are an unordered multiset of its `2n` corners. This covers
different vertices, different corners at one vertex, and a repeated corner. For distinct corners,
exchanging the two temporary halfedge names intertwines both the rotations and the edge
involution. At a repeated corner, the two consecutive orders are likewise interchanged by this
renaming because neither new halfedge is rooted. Hence one unordered corner pair with repetition
determines at most one rooted-map isomorphism class, and there are
`binom(2n+1,2)=n(2n+1)` such records.

In Class II, root orientation orders the deleted loop sites. Rooting the tree at the site of `r`
leaves `2n-1` choices for a different mate site. If both sites coalesce, the two orders of the named
halfedges `r,alpha(r)` in the common gap must be retained: unlike Class I, swapping them would move
the root. Thus at most `(2n-1)+2=2n+1` records occur for `n>=1`. When `n=0`, the unique cyclic order
on the two halfedges gives exactly one record, again `2n+1`.

Both decoders produce a connected orientable rotation system with `V=e` and `E=e`. If it has genus
`g` and `F>=1` faces, Euler gives `F=2-2g`; hence necessarily `g=0,F=2`. On encoder-produced records
the decoder restores the deleted rotations and root exactly. Codes whose decoded map would choose
a different canonical edge merely overcount and do not impair injectivity.

A plane tree with `n` edges has `2n` corner occurrences. The equivariant bijection between a root
corner and the next directed contour halfedge identifies corner-rooted and directed-halfedge-rooted
trees, including the single conventional object at `n=0`. The standard contour/Dyck-word decoder
therefore gives exactly `Cat_n` isomorphism classes under either convention.

No automorphism factor is missing. In a connected map, a root-preserving automorphism commuting
with `alpha` and `sigma` fixes the full orbit of the root under those permutations, hence every
halfedge. The explicit decoders give the same conclusion without orbit-stabilizer counting.

Adding the class bounds gives

\[
 \operatorname{Cat}_{e-1}(e-1)(2e-1)
 +\operatorname{Cat}_{e-1}(2e-1)
 =(2e-1)\binom{2e-2}{e-1}
 =\frac e2\binom{2e}{e}.
\]

**Verdict:** PASS.

### Finding WTPR-IR-03 — PASS: two directed face roots, the `e=1` endpoint, and the planar claim

**Applies to:** exact planar node claim hash
`sha256:0f07c313c810842eb7e0eb912962eea4b0895adedaa10ba4cac9dea0aaaf42c8`.

A directed halfedge belongs to one face-permutation cycle, so the first root names and roots the
first face. With exactly two faces, the remaining face is uniquely second. Its boundary contains
at most all `2e` halfedges. A bridge contributes its two distinct halfedges to the same face when
appropriate; it creates no occurrence beyond this `2e` total. Forgetting the second root therefore
has fiber at most `2e`. Because the singly rooted map has trivial root-preserving automorphism,
passing to isomorphism classes creates no larger fiber. Consequently

\[
 R_{e,0}^{(2)}\le 2eT_e\le e^2\binom{2e}{e}.
\]

At `e=1`, the unique connected two-face map is one vertex with one loop. Deleting the rooted loop
is exactly the Class II `n=0` case: `T_1=1`, and both sides of the singly rooted inequality equal
one. The second face has the mate halfedge as its only possible directed root, so
`R_(1,0)^(2)=1<=2`; the artifact does not claim equality in this latter bound.

As a non-load-bearing sanity check, a fresh exhaustive orbit enumeration with fixed edge
involution and root dart, restricted to at most eight halfedges, gave
`T_e=1,5,22,93` and `R_(e,0)^(2)=1,8,48,256` for `e=1,2,3,4`. These values satisfy the proved
bounds and reproduce the earlier review's `e=2` value without being used as a premise.

**Verdict:** the complete planar claim PASSES and may promote to `PROVED` at the locked hash.

### Finding WTPR-IR-04 — PASS: assembled route, constants, and exact implication hash

**Applies to:** repaired route implication hash
`sha256:64b8e9fb8161425c5f94b416af059f8e5ce623c14bc58f3fa7137198a5f1bc99`
and target claim hash
`sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603`.

All four listed route premises are load-bearing and sufficient:

1. `HEXT.werner-contraction-skeleton-ribbon-injection`, currently `PROVED`, injects connected
   Werner constellations with `E=2N` darts into maps with `e=2E=4N` ordinary edges and both ordered
   directed face roots, without a factorial or color multiplier.
2. The planar node proved in Findings WTPR-IR-01--03 bounds the `h=0` map count.
3. `HEXT.werner-positive-genus-two-boundary-weighted-count`, currently `PROVED`, supplies
   `4096^N N^(43h)` for `N>=2,h>=1`; at `N=1` positive genus is empty because
   `#A+#B+#C>=3` but the genus identity would require `#A+#B+#C=4-2h<=2`.
4. `HEXT.werner-minimal-catalan-weight`, currently `PROVED`, gives the per-triple factor
   `16^N=4^E=2^e` used in the planar branch.

For `h=0`, multiplication of the planar count by `2^e`, followed by
`binom(2e,e)<=4^e`, gives

\[
 S_{N,0}\le e^2 8^e=16N^2\,4096^N.
\]

For `N>=2`, `16N^2<=8^N`, with equality at `N=2` and a strictly increasing margin under the ratio
step. Hence `S_(N,0)<=32768^N`. For `N=1`, the direct bound of at most four choices for `A,B`, with
`C` forced and minimal weight one, is more than sufficient. For `h>=1`, the independently proved
premise gives the stronger base `4096<=32768` and the same factor `N^(43h)`. Thus the explicit
constants are `D=32768` and `alpha=43` for every `N>=1,h>=0`.

Finally,

\[
 \log(32768^2/18)=30\log 2-\log 18=17.9040436589\ldots<18.
\]

Therefore every fixed integer `m>e^18` satisfies `32768<sqrt(18m)`. This proves the route
implication exactly as currently written and implies the target's existential claim.

The equation-(19) string
`4096^N N^(43h)le32768^N N^(43h)qquad(h>=1)` is missing two TeX backslashes. The preceding sentence
identifies the positive-genus premise, equation (20) states the assembled conclusion correctly,
and Section 11.3 plus the canonical route contain the correctly normalized words. This is a
typographical presentation defect only and is not a mathematical or hash defect.

**Verdict:** the repaired route and exact target claim PASS and may promote to `PROVED` after the
review links and research events are added.

### Finding WTPR-IR-05 — PASS WITH STRICT SCOPE: no centered or full-size propagation

**Applies to:** promotion scope only; it does not review a centered or full-size claim.

The route counts structural connected triples with minimal Catalan weight. It does not count
compatible physical tuple labelings, prove an equality-component estimate, treat the two-component
sector, assemble a centered logarithmic moment, or prove a high-probability spectral statement.
The ordinary-map deletion is a counting code, not a label-compatible Werner surgery. Promotion of
the structural target therefore does not propagate to a centered node under the DAG protocol.

**Verdict:** preserve the artifact's stated boundary. No centered or full-size result may promote
from this review.

## 4. Exact integration instructions

No instruction below was applied by this reviewer.

### 4.1 Planar node

In `HEXT.werner-planar-two-boundary-rooted-map-count`:

1. Change the node assessment `CONJECTURED -> PROVED` without changing the claim.
2. Link this review at `Finding WTPR-IR-03` (scope should state that Findings WTPR-IR-01--03 checked
   the unicyclic selector, all loop/parallel/bridge and repeated-corner decoders, Catalan convention,
   automorphisms, both directed face roots, and `e=1`) with
   `reviewed_hash: sha256:0f07c313c810842eb7e0eb912962eea4b0895adedaa10ba4cac9dea0aaaf42c8`.
3. Remove the now-discharged review caveat and `independent-planar-deletion-code-review` frontier
   item. Preserve the ordinary-map/not-physical-surgery scope caveat if desired.
4. Append a dated `level-change` event sourced to this finding. Do not rewrite the creation event.

### 4.2 Repaired route

In route `repaired-rooted-two-face-map-code` of
`HEXT.werner-two-boundary-constellation-count`:

1. Keep its four premises and implication text byte-for-byte unchanged.
2. Change the route assessment `CONJECTURED -> PROVED`.
3. Link this review at `Finding WTPR-IR-04`, with scope covering the complete four-premise assembly,
   `N=1`, the constants, and the large-`m` comparison, and bind
   `reviewed_hash: sha256:64b8e9fb8161425c5f94b416af059f8e5ce623c14bc58f3fa7137198a5f1bc99`.
4. Remove the discharged review caveat and append a route-scoped `level-change` event.

### 4.3 Every-genus structural node

In `HEXT.werner-two-boundary-constellation-count`:

1. Change the node assessment `CONJECTURED -> PROVED` without changing its claim.
2. Set `assessment.basis.routes` to only `repaired-rooted-two-face-map-code`. A completion assessment
   must not cite the still-`CONJECTURED` old route as completed support.
3. Link this review at `Finding WTPR-IR-04` with
   `reviewed_hash: sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603`.
4. Remove the now-discharged planar-repair caveat and review frontier. Retain a caveat stating that
   the theorem is structural and does not control equality-graph labels or the two-component sector.
5. Append a node `level-change` event sourced to this finding.

Keep `rooted-two-face-map-code` at `CONJECTURED`, including its caveat and Finding WTBC-IR-04. Keep
the earlier weighted-count artifact, its independent review, and the repair event. The false
coefficient is historical evidence about that old route, not a reason to weaken the repaired one.

### 4.4 Unchanged boundaries and closeout

Leave `HEXT.werner-positive-genus-two-boundary-weighted-count` at its present `PROVED` level and do
not change its exact claim. Do not promote any centered or full-size node.

After canonical integration, regenerate `NODE_INDEX.md` and `GRAPH.mmd`, run

```text
python3 tools/proof_dag_check.py --problem holevo-extensive-violation --write-generated
python3 tools/proof_dag_check.py --problem all
python3 tools/evidence_closure_check.py --problem holevo-extensive-violation
```

and confirm that all new review links resolve to this immutable report and carry the applicable
exact statement hash.

## 5. Limitations

This review proves a finite combinatorial counting statement and audits its already registered
structural assembly. The small orbit enumeration in Finding WTPR-IR-03 was only a sanity check; the
verdict rests on the deletion decoders. The review does not establish a physical genus-lowering
surgery, a label-compatible count, a centered spectral bound, or a full-size extensive theorem.
