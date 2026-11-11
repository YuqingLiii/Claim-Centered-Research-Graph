# Independent review: product-Haar unbounded prevalence synthesis

Date: 2026-08-30

Reviewer: independent Codex review context `/root/q2_probability_review`.

## Independence and scope

I did not author
`artifacts/PRODUCT_HAAR_UNBOUNDED_PREVALENCE_PROOF_20260829.md`, either canonical node, or
either route reviewed here. I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full and made no
change to any proposer artifact or canonical mathematical node.

This review checks:

1. `HCPREV.product-haar-unbounded` and its exact direct-proof dossier;
2. route `product-haar-unbounded-route` in `HCPREV.random-models`;
3. Collins--Youn Theorem 3.3 and the entropy calculation in Theorems 3.4--3.5;
4. Bordenave--Collins Eq. (69), Theorem 9.2, and Lemmas 9.3--9.4;
5. finite-net uniformization over all traceless coefficient matrices;
6. the complementary-channel all-input entropy lower bound;
7. the probability intersection and the order of `m,J,D,eta`;
8. the conjugate-channel Bell witness; and
9. the asserted exact MOE-to-Holevo and quantitative pair-to-self transfers.

I do not review the unrelated whole-CPTP full-support probability result. I also do not use a
cross-project theorem as an undeclared premise: each current-layout project is required to expose
its own load-bearing interfaces.

## Executive verdict

The **product-Haar MOE core is mathematically correct**. For fixed `m>e^18` and fixed depth `J`,
Bordenave--Collins strong convergence can be uniformized over the entire traceless
Hilbert--Schmidt unit sphere because that coefficient space and the required net are fixed before
`D` grows. The resulting event is simultaneous over every coefficient matrix, so it can be
applied to the output-dependent matrix arising from every input state. Collins--Youn's exact norm
bound then gives the stated global side-entropy lower bound. The conjugate Bell input gives the
joint upper bound, and the probability and parameter order is

```text
fix m>e^18;
for every G choose fixed J;
choose fixed eta (equivalently an entropy error);
then let D tend to infinity.
```

No `J=J(D)` or full-size extensive conclusion is obtained.

Nevertheless, **the exact current claims and routes must remain `CONJECTURED`** for three
independent reasons:

1. The two canonical external assumptions are summaries rather than the exact theorem statements
   and regimes required by `DAG_PROTOCOL.md`. The Collins--Youn assumption omits the trace-zero
   coefficient space, constant, norms, and direct-product representation. The
   Bordenave--Collins assumption omits the precise independent-Haar tensor-leg tuple and the
   polynomial/norm meaning of strong convergence.
2. The exact `HCPREV.product-haar-unbounded` claim also asserts finite-dimensional exact
   MOE-to-Holevo transfer and a same-channel loss of at most one bit. The Q2 artifact gives only
   two assertions and a final formula for those steps. It contains neither the dephasing Weyl
   channel definition/global minimum-output-entropy proof nor the flagged-direct-sum Holevo
   calculation, and the node registers no load-bearing assumption or premise for either result.
   Those reductions are mathematically plausible and the displayed one-bit arithmetic is correct,
   but they are not established by this Q2 dossier.
3. The sole route in `HCPREV.random-models` proves only the final product-Haar clause of its parent
   claim. The parent claim additionally asserts positive-probability, probability-tending-to-one,
   and almost-sure-eventual results in several earlier named models. Generic evidence links to a
   source audit are non-load-bearing under the DAG protocol. A route that establishes one conjunct
   does not imply the whole compound claim.

Accordingly:

- the scoped product-Haar **MOE subtheorem** passes mathematical review but is not a separately
  registered canonical claim;
- `HCPREV.product-haar-unbounded` at its current broader hash is **BLOCKED** from `PROVED`;
- `HCPREV.random-models.routes.product-haar-unbounded-route` is **BLOCKED** as an implication of
  the whole parent claim; and
- `HCPREV.random-models` is not eligible for promotion from this route.

## Immutable inputs and exact hashes

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| product-Haar proposer artifact | `8589c42191b6379028d869f528dceaa377d3569d1fa4d789ed294b9c12083889` |
| product-Haar node YAML | `2456b3b163443ca51f5f1c8f86ee448f7b24fae12def6ce68191386973b87f07` |
| random-models node YAML | `14c1c05ef5e67e2e4e51c807c73d8e51f93e92ea125c7c3ae8a82db2ac64c297` |
| Collins--Youn PDF | `70c97a9e4c17218e17f159e00f3bc554011fa6f87b8966be494c97af0d726714` |
| Bordenave--Collins PDF | `59e14a3334b24f5683d8a0a8919d6cf266cb587f9dbae8d78e8213ca3fe2d8ac` |

Exact canonical statement hashes:

| object | exact statement hash |
|---|---|
| `HCPREV.product-haar-unbounded` claim | `sha256:e50f0b1cf0c3a7640ca404b494d7a0f8a3d1a8cdcbaf9e7ee6cb9967097a78a9` |
| `HCPREV.random-models.routes.product-haar-unbounded-route` implication | `sha256:b1418ad7bdb5616942a0cff29ac6e6a8c918477b72eeffc2dd11cf0b1cdd9f58` |
| `HCPREV.random-models` claim | `sha256:7f7f0e6d089f1eaef97075cbfb37654ecaa7b0852a90e68df3ba6827e5a5a611` |

## Finding HCP-PH-IR-01 -- PASS: primary-theorem match for the MOE core

Collins--Youn Theorem 3.3 states that for the regular representation of the direct product
`F_m^J`, every scalar matrix `a=(a_vw)` on `[m]^J` with `tr(a)=0` satisfies

```text
|| sum_(v,w) a_vw u_v^*u_w ||
 <= m^(J/2) sqrt((1+9/m)^J-1) ||a||_2.
```

The index set, direct-product word, trace-zero condition, operator norm, Hilbert--Schmidt norm, and
constant all match the proposer calculation. Theorems 3.4--3.5 in the same source contain the
corresponding complementary-output Hilbert--Schmidt and entropy argument in the free model.

Bordenave--Collins Eq. (69) places independent Haar `U_{i,j}` on separate tensor legs exactly as
the proposer does. Theorem 9.2 states that for fixed generator count `m` and fixed leg count `J`,
the tuple converges strongly in probability to the regular representation of `F_m^J`. The word

```text
W_v^*W_w = product over tensor legs of U_(v_j,j)^* U_(w_j,j)
```

is a fixed star-polynomial once `m,J` are fixed, so it lies in the theorem's scope.

**Verdict:** PASS for the two primary inputs as actually used in the MOE proof. This finding does
not cure the underspecified canonical assumption text; see Finding HCP-PH-IR-07.

## Finding HCP-PH-IR-02 -- PASS: finite-net uniformization controls all coefficients

Put `q=m^J`. On the traceless Hilbert--Schmidt unit sphere in `M_q`, define

```text
T_D(a)   = sum_(v,w) a_vw W_v^*W_w,
T_inf(a) = sum_(v,w) a_vw u_v^*u_w.
```

For both maps,

```text
| ||T(a)||-||T(b)|| |
 <= sum_(v,w)|a_vw-b_vw|
 <= q ||a-b||_2,
```

because the `q^2` operator coefficients are unitary. Fix `eta>0`. Choose a finite net whose
radius, together with the pointwise norm-convergence tolerance, contributes at most
`eta K_(m,J)`, where

```text
K_(m,J)=m^(J/2)sqrt((1+9/m)^J-1)>0.
```

For each net point, Theorem 9.2 gives convergence in probability of the required polynomial norm.
The net is finite after `m,J,eta` are fixed, so a finite union of failure events still has
probability tending to zero. Lipschitz extension from the net gives

```text
||T_D(a)|| <= (1+eta)K_(m,J)||a||_2
```

simultaneously for every traceless `a`.

The event is chosen before any input state. Therefore it applies even when the coefficient matrix
`a` is subsequently selected as a function of the sampled unitaries and an optimizing input. There
is no invalid interchange of a pointwise probability limit with an uncountable input supremum.

**Verdict:** PASS. The enormous net size affects the uncontrolled threshold in `D`, not the
fixed-parameter probability limit.

## Finding HCP-PH-IR-03 -- PASS: the event yields a global all-input entropy lower bound

For `q=m^J`, a complementary channel is

```text
L^c(S)_(v,w)=q^(-1)Tr(W_v S W_w^*).
```

Its diagonal is `1/q`. Set `X=L^c(S)-I_q/q`. Then `X` is Hermitian and traceless, and

```text
||X||_2^2
 = Tr(L^c(S)X)
 = Tr(S (L^c)^*(X))
 <= ||(L^c)^*(X)||_infinity
 <= q^(-1)(1+eta)K_(m,J)||X||_2.
```

The simultaneous event from Finding HCP-PH-IR-02 permits applying the coefficient estimate to
this `X` for every `S`; a transpose of coefficient indices under an alternate Choi convention is
harmless. Dividing by `||X||_2` when nonzero, with the zero case immediate, gives the claimed
Hilbert--Schmidt bound.

Since `Tr X=0`,

```text
Tr(L^c(S)^2)
 <= m^(-J)[1+(1+eta)^2((1+9/m)^J-1)].
```

Von Neumann entropy is at least Renyi-2 entropy. Minimum output entropy is attained on a pure input,
and for a pure input a channel and its complement have the same nonzero output spectrum. Hence the
bound is global for `S_min(L)`, not merely a selected-input or complementary-channel statement.
Complex conjugation gives `S_min(bar L)=S_min(L)` deterministically, so no second random event is
needed.

**Verdict:** PASS.

## Finding HCP-PH-IR-04 -- PASS: conjugate Bell upper bound

For one leg, each of the `m^2` equal-weight Kraus outcomes on a normalized Bell input is pure.
The `m` equal-index outcomes all equal the same Bell vector because

```text
(U tensor conjugate(U))|Omega_D> = |Omega_D>.
```

After merging them, a realizing pure-state ensemble has one probability `1/m` and
`m^2-m` probabilities `1/m^2`. Entropy of a pure-state mixture is at most the Shannon entropy of
any realizing ensemble, even if additional collisions occur. The bound is therefore

```text
2 log_2(m) - log_2(m)/m.
```

The tensor product of `J` Bell inputs produces the tensor product of the `J` layer outputs, so the
upper bound adds exactly. This yields the proposer's joint `J`-layer upper bound.

**Verdict:** PASS. The witness is specifically the conjugate partner and matched product Bell
input; no independent-partner or arbitrary-input upper bound is claimed.

## Finding HCP-PH-IR-05 -- PASS: probability intersection and quantifier order

On the single simultaneous coefficient event, both side lower bounds hold--the conjugate side by
deterministic spectral equality--while the Bell upper bound is deterministic. Thus there is no
intersection of `J` separate asymptotic events and no product-of-probabilities assumption.

For fixed `m,J`, choose `eta` sufficiently small so the side-entropy correction is at most a chosen
fixed `epsilon`. Then

```text
gap >= J c_m - 2 epsilon,
c_m = log_2(m)/m - 2log_2(1+9/m).
```

For `m>e^18`, `ln(1+9/m)<9/m` gives `c_m>0`. Given `G>0`, first choose the fixed integer
`J>2G/c_m`, then set `epsilon=Jc_m/4` and choose fixed `eta`, and only then let `D` grow. The event
probability tends to one and its gap is strictly greater than `G` because the choice of `J` is
strict.

The correct statement is

```text
for every G>0, there exists fixed J such that
lim_(D->infinity) Pr[gap_(J,D)>G]=1.
```

The artifact's informal line containing both "for all sufficiently large D" and an arrow to one
should be read as this limit, which is stated correctly in its theorem and canonical claim.

**Verdict:** PASS. No conclusion about a growing `J(D)`, a practical threshold `D(J)`, or gap per
full logarithmic dimension follows.

## Finding HCP-PH-IR-06 -- BLOCK: Holevo and pair-to-self transfers are not in the Q2 dossier

The current product-Haar canonical claim includes two deterministic conclusions beyond the MOE
theorem:

1. exact numerical transfer to a finite-dimensional Holevo pair; and
2. conversion to a same-channel Holevo defect with at most one bit loss for the symmetric
   conjugate family.

The proposer artifact states these conclusions in two paragraphs but does not define the Weyl
extension or prove its global one-channel and product minimum-output-entropy identities. It also
does not define the flagged direct-sum channel or prove the one-channel and four-block
log-sum-exp formulas. The canonical node has no assumptions or premises for either step.

The displayed one-bit arithmetic is correct **conditional on** those missing interfaces. If the
transferred conjugate pair has equal Holevo quantities `x`, the direct-sum law gives

```text
chi(A direct-sum B)=x+1,
```

and product-ensemble lower bounds in the four tensor-square blocks give

```text
chi(T tensor T)-2chi(T)
 >= log_2[1+(1/2)(2^g-1)]
 >= g-1.
```

Equal balance follows from an exact Weyl identity of the form
`chi(N_tilde)=log d-S_min(N)` applied to conjugate channels with equal minimum output entropy.
But this conditional arithmetic is not a substitute for a registered proof of the two
interfaces.

Other projects currently contain related nodes and artifacts, but they are not declared premises
of this Q2 node, and one of the quantitative pair-to-self nodes remains `CONJECTURED`. Generic
cross-project awareness cannot silently become load-bearing evidence.

**Verdict:** exact claim hash
`sha256:e50f0b1cf0c3a7640ca404b494d7a0f8a3d1a8cdcbaf9e7ee6cb9967097a78a9`
is BLOCKED from `PROVED`. The MOE portion should be split into a separately reviewable node, or the
two finite-dimensional transfer proofs should be reproduced/registered locally as explicit
premises before re-review.

## Finding HCP-PH-IR-07 -- BLOCK: canonical source assumptions are underspecified

The current assumption
`product-free-group-haagerup-bound` says only that Collins--Youn gives "the required
all-coefficient norm bound." The exact imported statement must expose:

- fixed integers `m,J` and the regular representation of `F_m^J`;
- scalar `a in M_(m^J)(C)` with `tr(a)=0`;
- operator norm on the sum and Hilbert--Schmidt norm on `a`; and
- the constant `m^(J/2)sqrt((1+9/m)^J-1)`.

The current assumption `tensor-strong-convergence` says only that Theorem 9.2 gives strong
convergence for fixed counts. It must expose the independent Haar `U_(i,j) in U(D)`, their placement
on the `j`th tensor leg as Eq. (69), convergence in probability as `D->infinity`, and the
norm-convergence interface for each fixed matrix-valued star-polynomial. Its current locator is
adequate, but its statement is not the exact theorem interface required by the protocol.

**Verdict:** even a narrowed MOE-only canonical node is not eligible for `PROVED` until these
assumption statements are repaired. No mathematical defect in the cited theorems was found.

## Finding HCP-PH-IR-08 -- BLOCK: the random-models route does not imply its parent claim

The exact parent claim at
`sha256:7f7f0e6d089f1eaef97075cbfb37654ecaa7b0852a90e68df3ba6827e5a5a611`
contains at least two logically independent conjuncts:

1. positive probability, probability tending to one, or almost-sure eventual MOE violation in
   several earlier named Haar models; and
2. arbitrarily large high-probability gaps in the new fixed-depth product-Haar model.

The route implication at
`sha256:b1418ad7bdb5616942a0cff29ac6e6a8c918477b72eeffc2dd11cf0b1cdd9f58`
says only that the product-Haar premise supplies the second clause. That is true but does not imply
the whole parent claim. The primary-source audit links under `basis.evidence` are non-load-bearing
and cannot supply the missing first conjunct.

**Verdict:** route implication BLOCKED as a route to this parent, independently of the status of
`HCPREV.product-haar-unbounded`. Repair by splitting the parent into atomic named-model and
product-Haar claims, or by adding all load-bearing named-model premises to an assembled route whose
implication covers the full compound statement.

## Promotion disposition and minimal repair

No reviewed canonical object should be promoted on this dossier.

A protocol-safe repair is:

1. register a new atomic claim containing only the product-Haar MOE high-probability theorem;
2. give it the exact Collins--Youn and Bordenave--Collins assumption statements specified in
   Finding HCP-PH-IR-07;
3. separately register local exact Weyl-transfer and symmetric pair-to-self premises, or narrow the
   present claim to MOE only;
4. split the compound `random-models` classification into atomic clauses or assemble a route with
   every named-model premise; and
5. obtain new hash-bound review of the repaired claims/routes. Findings HCP-PH-IR-01--05 may be
   cited as mathematical review of an unchanged MOE substatement, but they are not a hash-bound
   completion review of any new claim until its exact statement exists.

## Scope limitations

Even after repair, the result gives absolute gaps unbounded along a sequence selected in the order
`J` then `D(J)`. It gives no bound on `D(J)`, no dimension-uniform probability rate, no density or
full-support conclusion in the whole CPTP body, no explicit deterministic unitary tuple, and no
Hayden--Penington full-size extensive violation.
