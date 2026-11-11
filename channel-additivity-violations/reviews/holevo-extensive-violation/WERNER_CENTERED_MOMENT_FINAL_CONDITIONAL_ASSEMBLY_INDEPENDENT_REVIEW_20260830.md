# Independent review: Werner centered moment all-genus final assembly

Date: 2026-08-30

Reviewer: independent Codex review context `/root/centered_assembly_audit`.

## Independence and scope

I did not author
`artifacts/WERNER_CENTERED_MOMENT_ALL_GENUS_ASSEMBLY_20260830.md`, its predecessor
`artifacts/WERNER_CENTERED_MOMENT_FINAL_CONDITIONAL_ASSEMBLY_20260830.md`, or any of their
load-bearing combinatorial inputs. I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full,
reconstructed the term partition, every `m,N,d,H` factor, the geometric sums and the even-moment
Markov step, and checked the current canonical status of every cited premise. I used no Chrome,
webpage ChatGPT, large certificate run, or subagent. I used one bibliographic web lookup only to
cross-check the Akemann--Ostrand DOI; no mathematical step depends on that lookup. I made no
canonical YAML change. This review file is the only repository mutation made by the audit.

This review checks:

1. whether the return/nonreturn and `c,h,g` partition exhausts the exact Haar expansion;
2. the connected all-genus mass, including its planar endpoint;
3. the two-component low-genus separation and residual mass;
4. the skeletonwise monotone-Weingarten multiplier;
5. every constant and quantifier in the choice `N(d)=Theta(log d)`;
6. the Markov implication;
7. the current planar, equality-component and two-component premise statuses; and
8. the exact canonical scope that may, and may not, be promoted.

It does not re-prove the Collins--Matsumoto path theorem, the rooted-map deletion theorem, or the
equality-component theorem from first principles. Those are used only through their current
independently reviewed `PROVED` nodes. It does independently check that their exact statements are
sufficient for this assembly.

## 1. Executive verdict

The shortened all-genus master inequality and logarithmic-moment argument **PASS** in the exact
large-`m` scope

```text
fixed integer m>e^18, fixed eta>=0, then d->infinity.
```

The new all-genus route is strictly preferable to the predecessor: it uses the now-`PROVED`
`HEXT.werner-two-boundary-constellation-count` directly for every connected genus, so it needs no
new planar Input P and no literal `h=0` specialization of a positive-genus tree--cotree code.

The expansion is exhaustive. After the return sequences are removed, every nonzero Haar term has
`c=1` or `c=2`; the connected sector splits into `h=0` and `h>=1`; the two-component sector with
`h<=1` is already in the return union; its nonreturn remainder starts at `h=2`; and for every
fixed minimal skeleton the `g>=1` monotone excess is included by the single factor
`1/(1-theta)`. No Weingarten family is omitted and no cancellation is needed after the safe return
sector is separated.

The constants in equation (4), the two handle ratios, the even rounding of `N(d)`, and the Markov
step are correct. An earlier byte version omitted the `+` between the return term and the
nonreturn bracket; the proposer repaired it before this verdict. The current inspected artifact at
`sha256:1a5979c3d9e341d9ba540110b11628fccd441bfc8ecf87901a04743d538c6c64`
contains the correct addition and is the only version approved here.

For fixed `m>e^18` and `eta>=0`, all three bases satisfy

```text
u=(3m-4)/(m^2 H)<1,   a=4096/(mH)<b=32768/(mH)<1,
```

and every polynomial/logarithmic remainder vanishes.

However, the current canonical claim
`HEXT.same-tuple-werner-centered-bound` at
`sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5`
is not eligible for `PROVED` from this route as written. It says only “For fixed m” and does not
define `A` or restrict `m>e^18`, whereas the proof uses `4096<mH` through the much stronger project
regime. That is a material quantifier mismatch, not a failure of the moment argument.

The protocol-safe outcome is therefore:

- **mathematical and protocol PASS** for the registered scoped centered claim at `d882...` and its
  repaired route implication at `0c09...`;
- **FAIL for promotion of the current broad/underspecified centered claim hash**;
- use the newly registered exact reversal/return atom as a seventh final-route premise; its
  machine-visible Akemann--Ostrand assumption, exact claim hash, and source note pass this review;
  that atom is eligible for `PROVED` once this finding is linked; and
- after promoting that atom and binding this review to `0c09...` and `d882...`, the scoped centered
  Werner route and node are eligible for `PROVED`.

The artifact's statements that Inputs E and D are still proposer-side are stale historical status
descriptions. Both are now independently `PROVED`. The planar repair is also now independently
`PROVED`. The proposer also applied the existential `D,alpha` interface repair during this audit.
Thus no mathematical or dependency interface remains; only review linkage and level promotion
remain.

This result does **not** prove `HEXT.same-tuple-two-leg-scalar-strong-norm`, the all-copy physical
self-purity node, or `HEXT.goal`. It closes only the large-`m` real-Werner coefficient sector after
combining the scoped centered theorem with the already-`PROVED` exact Werner spectral reduction.

## 2. Immutable inputs

The following are SHA-256 digests of the exact bytes inspected for this review.

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| primary reviewed all-genus assembly | `1a5979c3d9e341d9ba540110b11628fccd441bfc8ecf87901a04743d538c6c64` |
| superseded conditional assembly | `9a3a12d5b6bd99ecab8b435569f9cef91b49a1410ed2f5116ce00e9f5fb334f6` |
| exact reversal/return artifact | `6f0d52b4d48433c9f16d8ded4440469268b336df3af8f23f4a8b798ac15752ce` |
| reversal/return independent review | `d0bc4279e0507979f2d3b994bc620f1ec918c1ff6149e40b7515c209d9f5887e` |
| registered reversal/return node YAML | `8f0bdb644e210e9441fa204752d408a61f8e73141b3a9c28f42e4ea29030a52f` |
| Akemann--Ostrand source note | `90697add96836d6faf1f44fbcf5ad6ad46128d3b0c557ec89feb8e858f5264a1` |
| registered large-`m` centered node YAML | `139940e947d9e76acd0c67894ac491b614358aa7577b8d581539fffc055e4d0b` |
| registered large-`m` real-Werner node YAML | `787307f6b8e0b03674727fe6fb693e3368fa7b13547571cecfc930a489ff2548` |
| exact constellation artifact | `c52f59c7e301a154925149689b13897a54cf462bf9674ef16105f9a2dd3d1a88` |
| constellation independent review | `b033b088c557bd0aee8c281013d6da542e475557f68f3e172dd94852638a3fc0` |
| finite-`d` Weingarten artifact | `0b44d44bae7438e08a5d865f5c01076d5175271eb1f6697e91fc6456640d1280` |
| Weingarten independent review | `282c480439f213183038e4ce0ee5cc3a9ccebff5ffaf15437f4f3064c9018281` |
| weighted connected-count artifact | `f4d0b8b92366c0aa353b3f7794c9a0b1a5326aa0602ecc9323f6f9a9e51a8bab` |
| weighted-count independent review | `ce0f613f8b3f3377a0c2c02357b9fe7423939746d624386078fc32a01da8f8ba` |
| equality/two-component artifact | `1aac1c071b61dc3809a3bcf28339263508e301062eba8980e8b287a64ef92be7` |
| equality/two-component independent review | `2aa54c84031ea8dee9bd79463b93417cd63e061b7e222fd9d15742ff900f194a` |
| planar repair artifact | `f4cd879af9d05ec88b2e94ab6e0c8d183b1248bd483d11d916b101189297ef73` |

The planar repair review and canonical planar nodes were integrated while this independent review
was in progress. The review finding is bound to the unchanged planar claim hash
`sha256:0f07c313c810842eb7e0eb912962eea4b0895adedaa10ba4cac9dea0aaaf42c8`,
and the repaired all-genus route is bound to
`sha256:64b8e9fb8161425c5f94b416af059f8e5ce623c14bc58f3fa7137198a5f1bc99`.
At final audit time both corresponding canonical nodes are `PROVED`.

The load-bearing existing claim hashes are:

| node | exact claim hash | status |
|---|---|---|
| `HEXT.werner-contraction-skeleton-ribbon-injection` | `sha256:288e0f5df3ca6a53915325c487648184b9be0ff950c1e52c5db7689468c730f7` | `PROVED` |
| `HEXT.werner-constellation-euler-deficit` | `sha256:c1c37d08c4f0cf37cb698b26a03d48cef0dd668686b71ed3a8391fed63c1d62a` | `PROVED` |
| `HEXT.werner-planar-two-boundary-rooted-map-count` | `sha256:0f07c313c810842eb7e0eb912962eea4b0895adedaa10ba4cac9dea0aaaf42c8` | `PROVED` |
| `HEXT.werner-minimal-catalan-weight` | `sha256:82a54db26f9887fab15962f597b42c9d9b7c5a50b2dc86c713e0b066cc51cf54` | `PROVED` |
| `HEXT.werner-positive-genus-two-boundary-weighted-count` | `sha256:300c642a7cab1717445a387e793666fa416ead65bd0731f9be684701d8f30cf6` | `PROVED` |
| `HEXT.werner-two-boundary-constellation-count` | `sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603` | `PROVED` |
| `HEXT.werner-admissible-equality-component-genus-bound` | `sha256:443c7023066be044f8795ef5d036a159f652ccb78bb6b51d15d0a95904791651` | `PROVED` |
| `HEXT.werner-two-component-low-genus-return-separation` | `sha256:c523f97093f9490b81572424cc273a25e9224cdbff285506d7a376dc304e9724` | `PROVED` |
| `HEXT.werner-two-component-nonreturn-weighted-count` | `sha256:16edb16e7ddcce4a044c0fe7608bc73bfe530a0fad52e02fc9f1a05fe7488c32` | `PROVED` |
| `HEXT.werner-monotone-weingarten-tail-summability` | `sha256:e47cd4541145cc59fcd04cf217f738d0ceb6c126508210d4c169af7fc0c8c0e4` | `PROVED` |
| `HEXT.werner-centered-reversal-return-bound` | `sha256:a8936d811867eacbe9a4b2d13a61063479d3558ce15174c6d0dc2e035198bc3a` | `CONJECTURED`, eligible for `PROVED` by Finding WCMF-IR-08 |
| `HEXT.same-tuple-werner-spectral-reduction` | `sha256:241ced6a8c0a7c97de7cc172d9793bb96c032287da21ad5eb4a074dfb3004e67` | `PROVED` downstream reduction only |

The `PROVED` route implication inside `HEXT.werner-two-boundary-constellation-count` establishes
the exact values `D=32768` and `alpha=43`, but the node's public claim is only existential in
`D,alpha`. The exact numerical master is mathematically established by the reviewed route proof,
yet a downstream route that lists only the node ID formally receives only its public claim. Finding
WCMF-IR-10 records the minimal interface repair.

## 3. Exact reviewed statements and hashes

Hashes use `sha256(statement.strip())` after the same folded-scalar normalization used by the
repository.

### 3.1 Scoped centered Werner claim — PASS

> For every integer m>e^18 and every fixed eta>=0, let U_1^(d),...,U_m^(d) be independent
> Haar-distributed unitaries in U(d), define R_U=m^(-2)sum_(v,a=1)^m U_v^*U_a tensor
> U_a^*U_v, A=1+9(1+eta)^2/m, and H=sqrt((A^2-1)(1-m^(-2))). Then
> lim_(d->infinity) Pr{||R_U-I_(d^2)/m||_infinity>H}=0.

Exact claim hash:
`sha256:d882dca3c30783b1a7d9f6a6cec79a66317b23ea26800fe2a2306263d1eb6670`.

This is the exact current claim of `HEXT.same-tuple-werner-centered-bound-large-m`. It is
mathematically equivalent to the initially reviewed prose formulation but makes the varying
dimension and identity operator explicit.

### 3.2 Master moment inequality — PASS

> For every fixed integer m>e^18 and fixed eta>=0, define A=1+9(1+eta)^2/m,
> H=sqrt((A^2-1)(1-m^(-2))), S_U=R_U-I/m, u=(3m-4)/(m^2 H),
> b=32768/(mH), a=4096/(mH),
> x_43=m^2 N^43/d^2, x_24=m^2 N^24/d^2, and theta=6(2N)^(7/2)/d^2. For every even
> integer N>=2 such that theta,x_43,x_24<1,
> E Tr(S_U^N)/H^N <= 2d^2 u^N + m^2/(1-theta)
> [b^N/(1-x_43) + a^N N^24 x_24/(1-x_24)].

Exact claim hash:
`sha256:fa2f08914a889a7dcdd41768fff616da4e058c802858567f3af332cc90b250dd`.

### 3.3 Registered exact reversal/return atom — PASS

This atom is now registered canonically as
`HEXT.werner-centered-reversal-return-bound`. Its exact YAML claim folds to the statement below.

> For every integer m>=2 and independent complex Haar U_1,...,U_m in U(d), set
> A_(v,a)=U_v^*U_a and S_U=m^(-2)sum_(v!=a) A_(v,a) tensor A_(v,a)^*. For every integer
> N>=1, Tr(S_U^N)=m^(-2N)sum_e Tr(W_U(e)) overline(Tr(check W_U(e))), where W_U is the
> forward product and check W_U reverses its N edge blocks. For every even N, the total absolute
> contribution of all edge sequences whose forward or block-reversed free word is the identity is
> at most 2d^2((3m-4)/m^2)^N.

Exact registered claim hash:
`sha256:a8936d811867eacbe9a4b2d13a61063479d3558ce15174c6d0dc2e035198bc3a`.

The node records the external free-group norm identity
`||sum_v lambda(g_v)||=2sqrt(m-1)` as a node-level `external-theorem` assumption. Its source points
to `AKEMANN_OSTRAND_FREE_GENERATOR_NORM_SOURCE_NOTE_20260830.md`, which gives the exact imported
statement, the full journal citation (Akemann--Ostrand, *American Journal of Mathematics* 98(4)
(1976), 1015--1047), and its only local use. The bibliographic identity is additionally consistent
with DOI `10.2307/2374039`. The algebraic implication
`T_m=X_m^*X_m-mI`, hence `||T_m||<=3m-4`, and the return-union bound are independently checked here
and in Finding STPW-IR-05.

The assumption scope is exact (`m>=2`, left-regular representation of `F_m`), its source is
locatable, and no unresolved conjecture is hidden as an assumption. The registered atom therefore
passes mathematically and is eligible for `PROVED` when this finding is linked at its exact claim
hash.

### 3.4 Current final route implication — PASS

During this audit the proposer replaced the earlier exact-numerical implication at `e073...` by
the following statement, which uses exactly the public existential connected-count interface while
keeping the same seven premises.

> The exact centered forward/block-reversal expansion and return estimate, combined with the
> listed proved connected every-genus weighted-count, equality-component, low-genus
> return-separation, residual two-component, monotone-tail, and Euler-deficit premises, imply the
> following. Let D,alpha be witnesses for HEXT.werner-two-boundary-constellation-count, and set
> u=(3m-4)/(m^2H), b_D=D/(mH), a=4096/(mH), x_alpha=m^2N^alpha/d^2,
> x_24=m^2N^24/d^2, and theta=6(2N)^(7/2)/d^2. For every even N with
> x_alpha,x_24,theta<1, E Tr[(R_U-I_(d^2)/m)^N]/H^N <= 2d^2u^N +
> m^2(1-theta)^(-1)[b_D^N(1-x_alpha)^(-1)+a^N N^24
> x_24(1-x_24)^(-1)]. For m>e^18 and fixed eta>=0, 0<u<1, 0<a<1, and
> 0<b_D<1. Choosing the even order N(d)=2ceil(gamma log(d)/2) with
> gamma>2/log(1/u) makes every term tend to zero, and even-moment domination plus Markov's
> inequality proves the node claim.

Exact current implication hash:
`sha256:0c09e4e2f6afb70b6364c7e69b7e1892fa113826a91dc1474ceaa824bb58a937`.

This current implication **PASSes** this review. Once the return atom is promoted, all seven
premises are `PROVED`, so this route and the scoped node claim at `d882...` are eligible for
`PROVED`.

## 4. Findings

### Finding WCMF-IR-01 — PASS: the Haar-term partition is exhaustive

Centering removes exactly the `v=a` terms and leaves

```text
S_U=m^(-2) sum_(v!=a) A_(v,a) tensor A_(v,a)^*.
```

Direct multiplication gives the forward/block-reversal formula in Section 3.3. An unbalanced
generator multiplicity has zero Haar expectation. Every balanced term is indexed by its physical
edge sequence and its global row/column pairing permutations. The lossless constellation map
recovers those pairings, while a compatible labeling of its equality components recovers every
possible edge sequence without a factorial multiplicity.

Because `rho` has two cycles, every constellation has exactly `c=1` or `c=2` topological
components. Therefore, after first partitioning edge sequences into the return union and its
complement, the nonreturn skeletons split exhaustively into:

```text
c=1,h=0;  c=1,h>=1;  c=2,h<=1;  c=2,h>=2.
```

The `c=2,h<=1` nonreturn class is empty by the independently proved low-genus return separation.
For every remaining fixed skeleton, minimal monotone length is `g=0`, while all allocations with
total excess `g>=1` have the same contraction skeleton and are bounded absolutely by the
single geometric multiplier `1/(1-theta)`. Hence the sector accounting in artifact Section 3 covers every
nonzero term exactly once after overcounting compatible labels and structural maps in the safe
direction.

The earlier cyclic-reversal collision-count node is not load-bearing in this final absolute
assembly. It was useful for finding the route, but it should not be listed as a premise of the
final implication.

**Verdict:** PASS.

### Finding WCMF-IR-02 — PASS: one reviewed connected all-genus mass

For connected `c=1`, the Euler node gives `d^(-2h)` at minimal path length, and the equality node
gives `kappa<=N+2+2h` for even `N`. Thus every genus-`h` structural weighted sum is multiplied by
at most

```text
m^(-2N) m^(N+2+2h) d^(-2h).
```

The newly `PROVED` every-genus node supplies one uniform structural bound

```text
S_(N,h)<=32768^N N^(43h)    for every h>=0.
```

Therefore the entire connected minimal mass at genus `h` is at most

```text
m^2(32768/m)^N (m^2 N^43/d^2)^h.
```

Summing from `h=0` gives

```text
m^2(32768/m)^N/(1-x_43).
```

This directly includes the planar term and is precisely the first bracketed term of the shortened
master inequality after division by `H^N`. No separate planar node, minimal-Catalan node,
positive-genus node, or `h=0` tree--cotree specialization is a direct premise of the final route;
they are already assembled and independently reviewed inside
`HEXT.werner-two-boundary-constellation-count`.

**Verdict:** PASS. This is the smallest and cleanest connected dependency.

### Finding WCMF-IR-03 — PASS: the disconnected sector and all powers

For `c=2`, the minimal Euler power is `d^(2-2h)`. The proved low-genus theorem moves all `h<=1`
edge sequences into the already bounded return union before any skeleton absolute sum. For the
remaining nonreturn sector, `h>=2`, the proved structural bound and equality bound are

```text
S_(N,h)^(c=2)<=4096^N N^(24h),   kappa<=N+2h.
```

After `m^(-2N)` normalization the genus-`h` mass is exactly bounded by

```text
(4096/m)^N m^(2h) N^(24h) d^(2-2h).
```

Writing `x_24=m^2N^24/d^2` and summing `h>=2` gives

```text
m^2(4096/m)^N N^24 x_24/(1-x_24),
```

so both the outside `m^2`, the extra `N^24`, and the starting genus are correct. There is no
uncontrolled `d^2` or `d^0` disconnected term left outside the return estimate.

**Verdict:** PASS.

### Finding WCMF-IR-04 — PASS: monotone excess and genus sums

For each fixed skeleton, the current monotone-tail node proves

```text
sum_(g>=0) absolute excess weight <= minimal weight/(1-theta),
theta=6(2N)^(7/2)/d^2.
```

It already convolves all generator-label allocations, so the assembly correctly adds neither a
factorial nor an active-label composition factor. Because it is skeletonwise, it can be applied
after restricting to nonreturn sequences and then summed over any `c,h` family.

The connected all-genus sum starts at `h=0` and is
`1/(1-x_43)`. The disconnected sum starts at `h=2` and becomes
`N^24 x_24/(1-x_24)` after the common `m^2(4096/m)^N` factor is extracted. Extending the finite
genus ranges to infinity enlarges positive sums and is safe.

**Verdict:** PASS.

### Finding WCMF-IR-05 — PASS: constants and fixed-parameter quantifiers

With `b=(1+eta)^2>=1`,

```text
(mH)^2=[18mb+81b^2](1-m^(-2)).
```

For every `m>=2` this is strictly larger than `18m`; its minimum in `b` occurs at `b=1`, where the
difference is `81-18/m-81/m^2>0`. Also

```text
log(32768^2/18)=30 log 2-log 18=17.9040436589...<18.
```

Thus every integer `m>e^18` satisfies

```text
4096<32768<sqrt(18m)<mH.
```

Therefore `0<a<b<1`; moreover

```text
u<(3m)/(m sqrt(18m))=1/sqrt(2m)<1.
```

Fix `m,eta` first. Choose any `gamma>2/log(1/u)` and set
`N(d)=2ceil(gamma log(d)/2)`. Then `N(d)` is even, at least two eventually, and
`N(d)=gamma log d+O(1)`. The return term is

```text
2d^2u^N=exp([2-gamma log(1/u)]log d+O(1)) -> 0.
```

The connected term is `b^N/(1-x_43)` and tends to zero. The disconnected term contains
`a^N N^24x_24/(1-x_24)` and also tends to zero. Moreover `theta,x_43,x_24` and
`N^24x_24=m^2N^48/d^2` tend to zero. There is no upper restriction on the
fixed `gamma`: the Collins--Matsumoto condition follows from `theta<1`, and every fixed
`N=O(log d)` satisfies it eventually.

**Verdict:** PASS.

### Finding WCMF-IR-06 — PASS: even-moment Markov

`S_U` is Hermitian. For even `N`, every eigenvalue satisfies
`|lambda|^N=lambda^N>=0`, so

```text
||S_U||_infinity^N <= Tr(S_U^N).
```

The exact trace is pointwise nonnegative even though its forward/reversal expansion is signed.
The sectorwise absolute bounds therefore imply the displayed upper bound on its expectation.
Markov gives

```text
Pr{||S_U||_infinity>H}
 <= E Tr(S_U^N)/H^N -> 0.
```

No concentration theorem, median estimate, or uniform fixed-order second-order-freeness theorem
is needed.

**Verdict:** PASS.

### Finding WCMF-IR-07 — PASS: large-`m` scope is now separated from the broad claim

The reviewed proof uses `m>e^18` to ensure a strict exponential margin. The current canonical
claim says only “For fixed m” and its caveat says merely that `m,eta` are fixed before `d` tends
to infinity. Nothing in `PROJECT.yaml` supplies a global `m>e^18` assumption. The same claim also
uses `A` without defining it.

Consequently this review cannot bind a completion verdict to the broad hash
`sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5`.
The newly registered
`HEXT.same-tuple-werner-centered-bound-large-m` has the exact scoped hash
`sha256:d882dca3c30783b1a7d9f6a6cec79a66317b23ea26800fe2a2306263d1eb6670`,
defines `A,H,R_U`, makes the dimension sequence explicit, and is exactly what passed.

Leave the old broader node `CONJECTURED` unless it receives a proof valid for every fixed `m`.
The new node is eligible for `PROVED` through the now-repaired completion route approved in
Finding WCMF-IR-10.

**Verdict:** new large-`m` claim PASS; old broad node promotion FAIL.

### Finding WCMF-IR-08 — PASS: exact return input is now machine-visible

The exact reversal formula and return estimate are registered as
`HEXT.werner-centered-reversal-return-bound` at exact claim hash
`sha256:a8936d811867eacbe9a4b2d13a61063479d3558ce15174c6d0dc2e035198bc3a`.
The node-level assumption states the Akemann--Ostrand theorem exactly and links the locatable
source note reviewed in Section 3.3. The finite trace expansion, forward/reverse return union,
constant `3m-4`, and factor `2d^2` all pass.

The smallest route now lists exactly the following seven canonical premises:

1. `HEXT.werner-centered-reversal-return-bound`;
2. `HEXT.werner-two-boundary-constellation-count`;
3. `HEXT.werner-admissible-equality-component-genus-bound`;
4. `HEXT.werner-constellation-euler-deficit`;
5. `HEXT.werner-two-component-low-genus-return-separation`;
6. `HEXT.werner-two-component-nonreturn-weighted-count`; and
7. `HEXT.werner-monotone-weingarten-tail-summability`.

The individual planar, minimal-Catalan, positive-genus, ribbon-injection and internal
two-component premises are already machine-visible below the aggregate atoms and should not be
duplicated in the final route. The
`HEXT.werner-reversal-cyclic-collision-count`, surgery nodes, and exact Werner spectral reduction
are also not premises of the centered probability statement. The spectral reduction is a separate
downstream implication from the centered theorem to the real Werner coefficient sector.

**Verdict:** exact return atom PASS and eligible for `PROVED` when this finding is hash-bound.

### Finding WCMF-IR-09 — STRICT SCOPE: no full-size propagation

The scoped theorem controls one fixed real-Werner coefficient sector for one two-leg reuse of a
fixed Haar tuple. By the already-proved spectral reduction it yields the corresponding uniform
real-Werner coefficient norm bound with high probability in the same fixed-`m` large-`d` regime.

It does not prove:

- convergence for arbitrary fixed Hermitian coefficients in
  `HEXT.same-tuple-two-leg-scalar-strong-norm`;
- any all-copy (`n>=1`) physical self-purity multiplicativity theorem;
- a fixed-channel positive regularized leakage rate;
- an `Omega` bound in full logarithmic input/output/environment cost; or
- `HEXT.goal`.

Therefore neither the existing absolute-unbounded result nor this centered Werner subtheorem may
be relabeled Hayden--Penington full-size extensive. Those remain logically independent.

The newly registered `HEXT.same-tuple-real-werner-sector-large-m` is scoped correctly. Its route
implication at
`sha256:78bcb08e2f33b40bf8abd232ca2b51b4238da7abffd878bd7008cf9672141126`
and its claim at
`sha256:ad940ef6f776d5a94f7ecb3e679332863bdac1efde961c34ac3dc4ec855b0411`
may propagate to `PROVED` after the large-`m` centered premise is `PROVED`; no broader node follows.

**Verdict:** promote only the scoped centered and real-Werner atoms after the reviewed return atom
and route are promoted; no arbitrary-coefficient, all-copy, or full-size node changes level.

### Finding WCMF-IR-10 — PASS: exact connected-count interface repair applied

The superseded centered route implication at
`sha256:e073d6e258a2e06b513bcd2c7a71c7bcf19023d14314ec469ef4b3065f83c319`
used `32768` and `43`. Those constants are proved in the completion route of
`HEXT.werner-two-boundary-constellation-count`, but that node's public claim exposes only the
existence of `D,alpha` with `D<sqrt(18m)`. Under the DAG protocol, a premise edge imports its node
claim, not a stronger sentence internal to its proof dossier.

The proposer applied the minimal repair during this audit: the current route is exactly the
existential-interface statement in Section 3.4 at
`sha256:0c09e4e2f6afb70b6364c7e69b7e1892fa113826a91dc1474ceaa824bb58a937`.
It defines `b_D,x_alpha`, uses only the public premise, preserves every bound, and has the same
logarithmic-moment conclusion.

**Verdict:** current `0c09...` route PASS and eligible for `PROVED` once its return premise is
promoted. The historical `e073...` text is not the current route and must not be used as its
reviewed hash.

## 5. Minimal integration instructions

No instruction below was applied by this reviewer.

1. Promote `HEXT.werner-centered-reversal-return-bound` at exact claim hash
   `sha256:a8936d811867eacbe9a4b2d13a61063479d3558ce15174c6d0dc2e035198bc3a`
   after linking Finding WCMF-IR-08.
2. Promote the current route `reviewed-all-genus-log-moment` at exact implication hash
   `sha256:0c09e4e2f6afb70b6364c7e69b7e1892fa113826a91dc1474ceaa824bb58a937`,
   retaining these seven premises:
   - `HEXT.werner-centered-reversal-return-bound`;
   - `HEXT.werner-two-boundary-constellation-count`;
   - `HEXT.werner-admissible-equality-component-genus-bound`;
   - `HEXT.werner-constellation-euler-deficit`;
   - `HEXT.werner-two-component-low-genus-return-separation`;
   - `HEXT.werner-two-component-nonreturn-weighted-count`; and
   - `HEXT.werner-monotone-weingarten-tail-summability`.
3. Link Findings WCMF-IR-01--WCMF-IR-10 as appropriate to the replacement route and to centered
   claim hash
   `sha256:d882dca3c30783b1a7d9f6a6cec79a66317b23ea26800fe2a2306263d1eb6670`.
   The review scope must retain fixed integer `m>e^18`, fixed `eta>=0`, then `d->infinity`.
4. Promote only the reviewed route and scoped centered node to `PROVED`. Remove no historical
   failed route or negative review.
5. The already reviewed downstream real-Werner node may then promote through its two proved
   premises. Do not use it as a route to arbitrary-Hermitian or full-size goals.
6. Regenerate generated views and run the project, all-project, and evidence-closure checks.

## 6. Limitations

The proof is an absolute-moment upper bound, not a sharp limiting spectral law. The exponential
bases `32768,4096` and threshold `m>e^18` are very nonoptimal. This review does not say whether the
broad centered claim holds for smaller fixed `m`; it says only that the audited route does not prove it.
The review also does not independently re-prove the external free-group norm or unitary
Weingarten path theorem, and therefore requires those assumptions to remain exactly sourced in
the DAG.
