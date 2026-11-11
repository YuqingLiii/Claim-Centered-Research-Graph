# Secondary adversarial review: exact physical self-purity atoms

Date: 2026-08-31

Reviewer: Codex context `/root/q2_probability_review`, independent of both the proposer and the
first reviewer.

## Scope and disposition

This is a fresh line-by-line audit of exactly these two atomic claims:

- `HEXT.physical-purity-centered-subset-expansion`;
- `HEXT.conjugation-closed-self-purity-n2-obstruction`.

It also audits the earlier review
`PRODUCT_HAAR_PHYSICAL_SELF_PURITY_EXACT_ATOMS_INDEPENDENT_REVIEW_20260831.md`. It does not review,
prove, or promote `HEXT.product-haar-physical-self-purity-multiplicativity`, any generic-Haar
all-copy statement, or `HEXT.goal`.

**Final verdict:** both atomic claims **PASS** at the exact claim hashes below. The earlier review
has one narrow endpoint omission: its residual-rank quotient is undefined at `q=1`. The project
artifact works in the regime `q=m^J>=2`; the standalone canonical wording does not say this. The
claim is nevertheless also true at `q=1`, and Finding `HEXT-PP-SAR-04` supplies the missing direct
branch. This secondary review should be linked from the canonical dossiers if the unrestricted
positive-integer wording is retained. No mathematical downgrade is needed after that link is made.

## Immutable inputs and exact bindings

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| derivation artifact | `40b52957a0a5c87ed98f0e3736fd727afee5456755b8d30c6da56ab7dd2d162f` |
| current centered-subset YAML | `9e8f9fd29731040e03357ce06a90abb57731d006dbb7355b171b01e46ce1778a` |
| current conjugation-closed YAML | `87bfc4f185d05ef3455a9bb441b273d8d21eaa82cb9c1a580a85add51dc1ac04` |
| earlier independent review | `9bccb3e53833e886cc6f66e5bfc1bf287888325a44fc6267a9fc4bf01e921282` |
| derivation Section 2, heading included and next heading excluded | `6ac437cc6a625b278ca81c26097e3bc3e16eff61b5a8a22faf8008a2a73822c8` |
| derivation Section 3, heading included and next heading excluded | `b390c088821ffd345607649ddf32893f29b4f2ec497297bb3a13d262c7ff66e5` |
| derivation Section 7, heading included and next heading excluded | `b4883f6359df0263e874286dc245e676b04e7336fe6f6248a19e61c972eb5584` |

The raw YAML hashes changed from the values recorded in the earlier review only because the nodes
were promoted and their review/event records were added. The claim strings did not change. Their
repository-normalized exact hashes, computed as `sha256(claim.strip())`, are:

| node | exact claim hash | verdict |
|---|---|---|
| `HEXT.physical-purity-centered-subset-expansion` | `sha256:475cfa24817b886754b899ce5a8d1caea6d1ccfc5728e24ecaac33ba87a1a0e7` | PASS |
| `HEXT.conjugation-closed-self-purity-n2-obstruction` | `sha256:6eae14abe6af4beb91e413ec834b99ad9f155a270899757d2dc34fe7e7cc6b7e` | PASS, with the explicit `q=1` branch below |

Neither atomic node has a route implication, so there is no route hash to authorize.

## Finding HEXT-PP-SAR-01 — PASS: the marginal formula and every cross-term cancellation

Let

\[
 T_S=(I_q/q)^{\otimes S^c}\otimes E^{\otimes S}(\rho_S),
\]

with tensor factors restored to their original positions. Applying `D_0` on one input leg traces
that leg and inserts `I_q/q`; doing this on every leg of `S^c`, while applying `E` on `S`, gives
exactly `T_S`. Thus

\[
 C^{\otimes r}(\rho)=\sum_{S\subseteq[r]}T_S.
\]

This remains true for correlated `rho`: the object entering the surviving `E` factors is precisely
the physical marginal `rho_S`, not a product of one-body marginals.

For `S!=T`, choose `i` in their symmetric difference and, without loss of generality, take
`i in S\T`. On output factor `i`, the `T`-summand has an identity factor. More invariantly,

\[
 \operatorname{Tr}_i T_S=0,
\]

because `Tr o E=0` as a linear functional, even when the input to the `E` leg is correlated with
all other legs. Therefore

\[
 \langle T_S,T_T\rangle_{HS}=0.
\]

No unjustified product decomposition of `rho` is used here. Finally,

\[
 \|T_S\|_2^2
 =\operatorname{Tr}[(I_q/q)^2]^{r-|S|}
   \|E^{\otimes |S|}(\rho_S)\|_2^2
 =q^{-(r-|S|)}\|E^{\otimes |S|}(\rho_S)\|_2^2.
\]

For `S=emptyset`, use `rho_emptyset=1` and `E^(tensor 0)=id` on the scalar field; the term is
`q^(-r)`. Summing squared norms proves the exact subset formula. Multiplication by `q^r` proves the
stated iff with the centered budget; it is not merely a sufficient implication.

**Verdict:** exact claim hash `475cfa24...` passes.

## Finding HEXT-PP-SAR-02 — PASS: the `r=3` statement has the correct limited quantifiers

For the three pair marginals, every available `r<=2` subset budget contains only empty-, one-, and
two-body centered terms. Their direct sum contains no occurrence, and hence no coefficient, of

\[
 q^3\|E^{\otimes3}(\rho)\|_2^2.
\]

The canonical claim concludes only that *naive marginal-summation induction* does not bound this
term. It does not assert that the term is independent of the proper marginals, that no additional
structural inequality can control it, or that the all-copy target fails. Those stronger
quantifiers would be unsupported, but they are absent. The phrase “at `r=3`” is also relative to
the assumed `r<=2` proper-marginal inequalities; it does not deny that a new fully centered term
already appears at `r=2` relative to `r=1`.

The derivation artifact has a harmless duplicated display lead-in `q^3||E^(tensor3)(rho)||_2^2`
immediately before equation (16). The displayed inequality and the canonical claim are
unambiguous; this typographical duplication is not used in the proof.

**Verdict:** no quantifier enlargement and no propagation to the all-copy parent.

## Finding HEXT-PP-SAR-03 — PASS: conjugation closure yields exactly `q` matched ordered pairs

Write the closure condition in its precise standard form: there are a permutation `pi` of `[q]`
and phases `z_v` such that

\[
 W_{\pi(v)}=z_v\overline{W_v}.
\]

For the normalized Bell vector `Omega=d^(-1/2) sum_i |i,i>`,

\[
 (W_v\otimes W_{\pi(v)})\Omega
 =z_v(W_v\otimes\overline{W_v})\Omega=z_v\Omega.
\]

The ordered pairs `(v,pi(v))` are distinct because their first coordinates are distinct. Hence
there are exactly `q` selected ordered pairs among the `q^2` equally weighted Kraus pairs. The
argument needs only “at least these `q` pairs hit the Bell ray”: if additional remaining pairs hit
the same ray, retaining them in the positive remainder only strengthens the later estimate.

For `q>=2`, write

\[
 (L\otimes L)(|\Omega\rangle\langle\Omega|)=q^{-1}P_\Omega+R.
\]

Every omitted Kraus-pair contribution is a normalized rank-one projector of weight `q^(-2)`, so
`R>=0`, `Tr R=1-1/q`, and `rank R<=q^2-q`. Consequently

\[
 \operatorname{Tr}R^2\ge
 \frac{(\operatorname{Tr}R)^2}{\operatorname{rank}R}
 \ge\frac{(1-1/q)^2}{q^2-q}
 =\frac1{q^2}-\frac1{q^3}.
\]

The cross term `2q^(-1)Tr(P_Omega R)` is nonnegative because both operands are positive. Thus

\[
 \operatorname{Tr}[(L\otimes L)(\Omega)^2]
 \ge\frac2{q^2}-\frac1{q^3}.
\]

The rank substitution has the correct direction: a lower actual residual rank only increases the
purity lower bound.

**Verdict:** the ordered-pair count, residual trace, residual rank, cross-term sign, and arithmetic
all pass.

## Finding HEXT-PP-SAR-04 — PASS WITH AN EXPLICIT ENDPOINT REPAIR: `q=1`

The earlier review divides by `q^2-q` without first stating `q>=2`. In the main derivation this is
implicitly harmless because its frozen setup has `m>=2`, `J>=1`, and `q=m^J`. The standalone
canonical claim, however, merely says “`q`-Kraus,” so its public wording also admits the unitary
case `q=1` under the usual convention.

At `q=1`, `L` is a unitary channel and a complementary channel is a one-dimensional constant pure
output, up to an output isometry. Hence

\[
 \mu_2(C\otimes C)=1=2/q^2-1/q^3.
\]

The proposed target is `mu_2(C tensor C)<=A^2`, and it fails whenever `A^2<1=2-1/q`, exactly as
claimed. Thus the theorem itself has no false endpoint; only the earlier review's displayed proof
omitted this separate branch.

**Disposition:** link this secondary finding to the canonical node, or equivalently narrow the
canonical hypothesis to `q>=2`. With this finding present, the exact current claim passes without a
rewrite.

## Finding HEXT-PP-SAR-05 — PASS: complementarity transfers the physical witness

Use the equal-weight Stinespring isometry

\[
 V=q^{-1/2}\sum_v W_v\otimes|v\rangle_E.
\]

After the harmless tensor-factor regrouping, `V tensor V` is a Stinespring isometry for
`L tensor L`, and its environment output is `C tensor C`. On the pure physical input `Omega`, the
joint system-environment output is pure. Its system and environment reductions have identical
nonzero eigenvalues, including when the displayed `q`-label complement is nonminimal. Therefore

\[
 \operatorname{Tr}[(C\otimes C)(\Omega)^2]
 =\operatorname{Tr}[(L\otimes L)(\Omega)^2].
\]

Convexity of output purity permits the maximum defining `mu_2` to be taken on pure inputs, but only
the lower bound from this one pure input is needed. Comparing

\[
 (2-1/q)/q^2>(A/q)^2
\]

is exactly equivalent to `A^2<2-1/q`. All inequalities have the required strictness.

**Verdict:** complementarity and the failure threshold pass.

## Finding HEXT-PP-SAR-06 — PASS: the “genuinely complex” clause is realizable, not a generic-Haar claim

The qualitative last clause means that conjugation closure does not force a common real
orientation. Under the already registered project meaning

\[
 W_v=e^{i\theta_v}UO_vV_0
\]

for fixed unitaries `U,V_0` and real orthogonal `O_v`, an explicit two-word example exists in
dimension three. Let

\[
 W_1=\operatorname{diag}(1,e^{-i\pi/10},e^{-i\pi/4}),
 \qquad W_2=\overline{W_1}.
\]

The tuple is conjugation-closed by the transposition of its two labels. If it had a common real
orientation, the relative unitary `W_1^*W_2` would, after multiplication by one scalar phase, be
unitarily similar to a real orthogonal matrix. Its eigenphases are

\[
 \{0,\pi/5,\pi/2\}.
\]

A three-dimensional real orthogonal spectrum, after one scalar phase, consists of one real
eigenvalue and one conjugate pair. Equivalently, one of the three phases must be the midpoint of
the other two modulo `pi`. Here the three tests compare `0` with `7pi/20`, `pi/5` with `pi/4`, and
`pi/2` with `pi/10`, respectively; none holds modulo `pi`. Thus this tuple has no common real
orientation.

This example establishes only that the exact special subclass includes genuinely complex tuples.
It supplies no positive-measure statement. Exact conjugation closure remains a dependent,
measure-zero condition in the independent complex-Haar product model.

**Verdict:** the last clause is valid under the project's existing definition and does not reach
the generic-Haar gate.

## Final authorization and strict boundary

After linking this review's `q=1` endpoint finding, the following exact claims remain licensed at
`PROVED`:

- `HEXT.physical-purity-centered-subset-expansion`, exact hash
  `sha256:475cfa24817b886754b899ce5a8d1caea6d1ccfc5728e24ecaac33ba87a1a0e7`;
- `HEXT.conjugation-closed-self-purity-n2-obstruction`, exact hash
  `sha256:6eae14abe6af4beb91e413ec834b99ad9f155a270899757d2dc34fe7e7cc6b7e`.

This authorization is atomic. It does **not** authorize any level change to
`HEXT.product-haar-physical-self-purity-multiplicativity`, any generic-Haar `r=2` or all-copy gate,
or `HEXT.goal`. The first atom is an exact reformulation plus a limited induction obstruction; the
second is a two-copy counterexample subclass of measure zero under the independent complex-Haar
model.
