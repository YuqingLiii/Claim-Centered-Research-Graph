# Scope review: Werner centered moment and downstream quantifiers

Date: 2026-08-30

Reviewer: independent Codex scope-audit context `/root/centered_scope_bridge`.

Independence declaration: this reviewer did not author either centered-moment assembly or any of
the canonical nodes inspected below. This report audits only DAG ownership, quantifiers, and
logical propagation. It assumes that the shortened master inequality and Markov argument in
`WERNER_CENTERED_MOMENT_ALL_GENUS_ASSEMBLY_20260830.md` receive a separate independent
mathematical review. It is therefore not itself a completion review of that inequality and does
not license any YAML promotion.

## 1. Executive verdict

The shortened assembly has a clean but strictly limited consequence:

> For every fixed integer `m>e^18` and every fixed `eta>=0`, the centered Werner spectral event
> holds with probability tending to one as `d` tends to infinity.

This is **not** the exact current claim of `HEXT.same-tuple-werner-centered-bound` if the phrase
“for fixed `m`” is read in its standard universal sense. The current claim has no lower bound on
`m`, does not bind the parameter `eta` inside the claim, and has exact claim hash
`sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5`.
The new route proves only the large-`m`, fixed-`eta` subclaim. Under the one-node/one-proposition
rule, it must not silently promote that broader node. A new large-`m` atomic node is the clean
protocol action.

No extra planar polynomial node is needed. The already `PROVED`
`HEXT.werner-two-boundary-constellation-count` supplies the connected `h=0` sector together with
every `h>=1`, using `D=32768` and `alpha=43`. In the moment sum this contributes

\[
 m^2\left(\frac{32768}{mH}\right)^N
 \sum_{h\ge0}\left(\frac{m^2N^{43}}{d^2}\right)^h,
\]

and `32768<sqrt(18m)<mH` for `m>e^18`. Thus the reviewed every-genus node directly replaces the
old proposer-side planar Input P. The separate candidate
`HEXT.werner-planar-two-boundary-polynomial-weighted-count` from the older assembly should not be
created merely for this route.

After the large-`m` centered node is independently proved, the already `PROVED` exact equivalence
`HEXT.same-tuple-werner-spectral-reduction` closes the **real two-dimensional Werner coefficient
sector** at the same `m,eta,d` quantifiers. It does not close the arbitrary-Hermitian same-tuple
lemma, global physical `n=2`, any `n>=3` or all-copy statement, the absolute-unbounded route, or
the Hayden--Penington full-size extensive target.

## 2. Inspected objects and byte hashes

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `artifacts/WERNER_CENTERED_MOMENT_FINAL_CONDITIONAL_ASSEMBLY_20260830.md` | `9a3a12d5b6bd99ecab8b435569f9cef91b49a1410ed2f5116ce00e9f5fb334f6` |
| `artifacts/WERNER_CENTERED_MOMENT_ALL_GENUS_ASSEMBLY_20260830.md` | `1a5979c3d9e341d9ba540110b11628fccd441bfc8ecf87901a04743d538c6c64` |
| `nodes/HEXT.same-tuple-werner-centered-bound.yaml` | `fd5829dd7ebe93aff95d45275580e471a84098c111d6c11b26c452441267f9c0` |
| `nodes/HEXT.same-tuple-werner-spectral-reduction.yaml` | `40521efd59f271785b2b09b31e13c649380866020dff4e079e2d6c8b15225a70` |
| `nodes/HEXT.same-tuple-two-leg-scalar-strong-norm.yaml` | `c8fbddb4b9f87d8f50da42e9c2c902309937a7190b3b5e1077dca57d5a734455` |
| `nodes/HEXT.complex-haar-global-n2-output-dual-gate.yaml` | `0e4c4ad2a46dbb3ca8c5cd8c66d960e16587290c53e925291ee0099e5e7a0a1c` |
| `nodes/HEXT.product-haar-physical-self-purity-multiplicativity.yaml` | `af5723703daba030fdb7700ea5d39975783862c6c066c1faa895011f046a2043` |
| `nodes/HEXT.finite-dimensional-unbounded-gap.yaml` | `35f7687e68c1ba4669ef4398b7090799e00f61616e499f989b479be66fb726a1` |
| `nodes/HEXT.goal.yaml` | `3c4a503fd2b5495ca26c5e244a980249f48458e695b880783cb10a540e8a1ab3` |
| `nodes/HEXT.werner-two-boundary-constellation-count.yaml` | `a99bd51193afcdcf3f531a6ce930bad359401f4458aa8b55a6f8cc98f6416df2` |

The shortened-assembly digest above includes the repaired plus sign in its displayed master
inequality. The earlier digest `f054b54c...` referred to a transient one-character display defect
and is not the inspected object.

## 3. Finding WCSB-01 — the existing centered node is too broad

The shortened assembly begins by fixing an integer `m>e^18` and `eta>=0` before taking
`d->infinity`. Both restrictions are used:

1. `m>e^18` supplies `32768<sqrt(18m)<mH`, hence the connected exponential base
   `b=32768/(mH)` is strictly below one.
2. `eta` is fixed before the limit. The logarithmic moment coefficient `gamma`, as well as `H`,
   may depend on the fixed pair `(m,eta)`; the proof does not give a statement uniform over an
   `eta=eta(d)` family.
3. The proof covers every fixed `eta>=0`; the endpoint `eta=0` is included. This is slightly wider
   than downstream project claims that deliberately ask for an `eta>0`, but it does not remove
   their additional small-`eta` rate inequalities.

By contrast, the existing canonical claim says only “for fixed `m`” and contains an unbound `A`.
Its caveat fixes `m` and `eta` before the limit but supplies neither `m>e^18` nor an `eta` range.
A caveat cannot turn a mathematically broader claim into the strict subclaim proved by one route.
Changing that node in place to `m>e^18` would materially weaken its proposition, contrary to the
file protocol. Therefore:

- keep `HEXT.same-tuple-werner-centered-bound` at its present level;
- create `HEXT.same-tuple-werner-centered-bound-large-m`; and
- link the new node from the broad node only as non-load-bearing partial progress. There is no
  valid route from the large-`m` node to the all-fixed-`m` claim.

## 4. Finding WCSB-02 — direct all-genus replacement of Input P

The six load-bearing canonical premises in the shortened assembly are:

1. `HEXT.werner-two-boundary-constellation-count`;
2. `HEXT.werner-admissible-equality-component-genus-bound`;
3. `HEXT.werner-two-component-low-genus-return-separation`;
4. `HEXT.werner-two-component-nonreturn-weighted-count`;
5. `HEXT.werner-monotone-weingarten-tail-summability`; and
6. `HEXT.werner-constellation-euler-deficit`.

For a connected genus-`h` nonreturn skeleton, these give

\[
 m^{-2N}m^{N+2+2h}32768^N N^{43h}d^{-2h}
 =m^2(32768/m)^N(m^2N^{43}/d^2)^h.
\]

This formula is valid starting at `h=0`. It is therefore stronger for DAG economy than keeping
the old positive-genus base `4096` plus a separate planar polynomial estimate. The residual
two-component `h>=2` branch keeps its sharper base `4096`; there is no reason to inflate it.

The exact centered forward/block-reversal expansion and return bound are internal steps of the
route proof. They were previously independently checked, but because they have no separate
canonical premise node, the final hash-bound reviewer must explicitly re-audit their use in the
assembled implication. The route must not cite the reversal-collision count as a substitute: that
claim bounds a different collision set and is not the return estimate used here.

## 5. Finding WCSB-03 — recommended large-`m` node

Suggested ID:

`HEXT.same-tuple-werner-centered-bound-large-m`

Suggested exact claim (one folded YAML scalar; hash uses `sha256(statement.strip())`):

> For every integer m>e^18 and every fixed eta>=0, let U_1^(d),...,U_m^(d) be independent Haar-distributed unitaries in U(d), define R_U=m^(-2)sum_(v,a=1)^m U_v^*U_a tensor U_a^*U_v, A=1+9(1+eta)^2/m, and H=sqrt((A^2-1)(1-m^(-2))). Then lim_(d->infinity) Pr{||R_U-I_(d^2)/m||_infinity>H}=0.

Claim hash:

`sha256:d882dca3c30783b1a7d9f6a6cec79a66317b23ea26800fe2a2306263d1eb6670`

Suggested route ID:

`reviewed-all-genus-log-moment`

Suggested premises: the six nodes listed in Finding WCSB-02.

Suggested exact route implication:

> The exact centered forward/block-reversal expansion and return estimate, combined with the listed proved connected every-genus weighted-count, equality-component, low-genus return-separation, residual two-component, monotone-tail, and Euler-deficit premises, imply, for every even N with x_43,x_24,theta<1, E Tr[(R_U-I_(d^2)/m)^N]/H^N <= 2d^2u^N + m^2(1-theta)^(-1)[b^N(1-x_43)^(-1)+a^N N^24 x_24(1-x_24)^(-1)], where u=(3m-4)/(m^2H), b=32768/(mH), a=4096/(mH), x_43=m^2N^43/d^2, x_24=m^2N^24/d^2, and theta=6(2N)^(7/2)/d^2. For m>e^18 and fixed eta>=0, 0<u<a<b<1. Choosing the even order N(d)=2ceil(gamma log(d)/2) with gamma>2/log(1/u) makes every term tend to zero, and even-moment domination plus Markov's inequality proves the node claim.

Route implication hash:

`sha256:e073d6e258a2e06b513bcd2c7a71c7bcf19023d14314ec469ef4b3065f83c319`

The route and node must begin at most `CONJECTURED`. Promotion to `PROVED` requires a fresh
independent review binding both exact hashes and explicitly checking the repaired shortened
assembly. No new planar premise should be added.

## 6. Finding WCSB-04 — exact real-Werner-sector consequence

`HEXT.same-tuple-werner-spectral-reduction` is already `PROVED` at exact claim hash
`sha256:241ced6a8c0a7c97de7cc172d9793bb96c032287da21ad5eb4a074dfb3004e67`.
Its deterministic “if and only if” turns the large-`m` centered event into a simultaneous estimate
for every coefficient in `span_R{I,F_m}`. Thus the real Werner coefficient sector is closed at
exactly the large-`m`, fixed-`eta`, high-probability scope after the centered node passes review.

If this downstream closure should itself be canonical rather than left as prose, atomicity calls
for a second, consequence node rather than changing the already proved equivalence node.

Suggested optional ID:

`HEXT.same-tuple-real-werner-sector-large-m`

Suggested exact claim:

> For every integer m>e^18 and every fixed eta>=0, with U_j^(d), R_U, and A as in HEXT.same-tuple-werner-centered-bound-large-m, the probability tends to one as d tends to infinity that ||M_U(Y)||_infinity<=(A/m)||Y||_2 holds simultaneously for every real Werner coefficient Y=alpha I_(m^2)+beta F_m with alpha,beta in R.

Claim hash:

`sha256:ad940ef6f776d5a94f7ecb3e679332863bdac1efde961c34ac3dc4ec855b0411`

Suggested premises:

- `HEXT.same-tuple-werner-centered-bound-large-m`;
- `HEXT.same-tuple-werner-spectral-reduction`.

Suggested exact route implication:

> On the event asserted by HEXT.same-tuple-werner-centered-bound-large-m, the proved equivalence in HEXT.same-tuple-werner-spectral-reduction identifies the centered spectral inequality exactly with the simultaneous coefficient inequality for all real alpha,beta. Since the event probability tends to one, the node claim follows.

Route implication hash:

`sha256:78bcb08e2f33b40bf8abd232ca2b51b4238da7abffd878bd7008cf9672141126`

## 7. Finding WCSB-05 — downstream non-consequences

| target | consequence of the large-`m` centered theorem? | exact reason |
|---|---|---|
| Real Werner coefficient sector | **Yes, at fixed `m>e^18`, fixed `eta>=0`, in probability as `d->infinity`** | The proved spectral-reduction node is an exact simultaneous equivalence on the two-dimensional real span of `I,F_m`. |
| `HEXT.same-tuple-two-leg-scalar-strong-norm` | **No** | That node quantifies over every fixed Hermitian `Y in M_(m^2)` and asserts convergence to the free scalar norm. The centered result gives a target inequality only on a two-real-dimensional subspace; it neither covers arbitrary `Y` nor proves the claimed limit equality. |
| `HEXT.complex-haar-global-n2-output-dual-gate` / global physical `n=2` target | **No** | Output duality requires uniform control of the entire Hermitian coefficient sphere of real dimension `m^4`, not only `span_R{I,F_m}`. Passing the Werner slice leaves generic entangled-input coefficients open. |
| `HEXT.product-haar-physical-self-purity-multiplicativity` | **No** | The physical node requires one fixed finite block and every copy number `n>=1`. A high-probability two-leg coefficient slice as `d->infinity` supplies neither global `n=2` nor any `n>=3` or all-copy bound. |
| `HEXT.finite-dimensional-unbounded-gap` and the absolute-unbounded subquestion | **No new implication and no dependency** | The absolute-unbounded proposer route uses independent Haar tuples on different tensor legs and fixed-depth tensor strong convergence. The centered same-tuple Werner result is neither a premise nor a review of that separate construction. |
| `HEXT.goal` full-size extensive target | **No** | Full-size extensivity needs a fixed block with positive regularized rate, such as all-copy physical self-purity or controlled self-leakage, plus dimension-cost bookkeeping. The order of limits here is fixed `m,eta`, then `d->infinity`, and controls only one two-leg coefficient slice. |

In particular, the centered theorem does not license promotion of the general same-tuple node, the
physical-purity node, the full-size root, or the already separate absolute-unbounded proposer
claim. Those objects may cite the large-`m` node only as scoped non-load-bearing progress unless a
new theorem supplies the missing quantifiers.

## 8. Protocol integration recommendation

After a separate independent mathematical review of the shortened assembly:

1. create the required large-`m` centered node with the exact claim and route above;
2. link the independent review at both the route implication and node claim hashes;
3. optionally create the real-Werner-sector consequence node with its two explicit premises;
4. add only non-load-bearing evidence links from the broader same-tuple and physical `n=2`
   frontiers;
5. do not change the broader existing centered claim, general same-tuple claim, physical-purity
   claim, absolute-unbounded claim, or full-size root level; and
6. regenerate the derived views and run the structural, evidence-closure, and scope checks.

This report is deliberately not linked into YAML by its author. Its findings are scope guidance;
mathematical completion still depends on the separate hash-bound review of the shortened master
inequality.
