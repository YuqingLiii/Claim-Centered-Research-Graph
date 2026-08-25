# Critical hidden-frequency endpoint: strict-injection recording-query attempt

Date: 2026-07-21  
Canonical node: `KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.strict-injection-recording-query`  
Scope: the exact frozen hidden-frequency promise at `q=Theta(N^(2/3))`  
Method: exact random partitions and random injections only; no relaxed-label transfer; no DAG edits

## 1. Verdict

The declared strict Belovs-style recording/projector architecture **fails**.

The strict injection counts are clean: after splitting one endpoint from the unique cross pair,
the unused-label normalization cancels exactly.  The associated completion map has norm one only
after the Fourier polynomial has already been restricted to the query-boundary sector.  It does
**not** imply the generic fixed-partition comparison with `Upsilon_1^+`, nor the tempting orbit
factor

\[
 \sqrt{|M_1|/|M_2|}=a^{-1/2},
 \tag{1.1}
\]

as a full-space operator bound.  A degree-two local witness has merged boundary norm one but
split plus norm strictly below one, and a degree-six aggregate witness directly reverses the
putative orbit inequality.  Even earlier in a recurrence, the usual bottom support-counting
estimate also fails because of a strict promise kernel.  Therefore this hierarchy supplies no
generic progress inequality and no new lower-bound exponent.  In particular, the previously
considered `Omega(N^(4/9))` consequence is **withdrawn**.  The independently proved
`Omega(N^(11/18))` exact-promise lower bound is external to this route and is unaffected.

This loss cannot be repaired by claiming that an unqueried coordinate is a singleton only with
probability `a/n`.  There is an exact degree-at-most-four polynomial, using no occurrence of that
coordinate, which recognizes whether it is a singleton.  A degree-at-most-nine vector then
realizes `Omega(1/a)` boundary norm and rules out the desired `O(sqrt(t)/n)` operator bound by the
growing factor `n/a=Theta(N^(1/3))`.

The second required ingredient, constant operator anti-concentration of the no-known-pair sector,
is not merely unproved.  It is false with norm ratio exactly one.  The correct degree-two witness
for a proposed pair `rho=(i,j)` is

\[
 \phi_\rho(x,y)={\bf 1}[x_i=y_j].
 \tag{1.5}
\]

Its minus projection under the strict YES orbit is nonzero and supported only on types whose
unique pair is `rho`.

These are failures of the full low-Fourier-degree knowledge projector used in this node.  They do
not give an upper algorithm, do not refute a different adversary or a reachability-sensitive
recording filtration, and do not change the status of the parent critical endpoint.

## 2. Exact strict distributions

Use the frozen parameters

\[
 n=\lfloor N/2\rfloor,\qquad a=\lfloor q/4\rfloor,
 \qquad d=\left\lfloor{n-a\over a}\right\rfloor,
 \qquad p=(n-a)-ad.
 \tag{2.1}
\]

Each side has `a` singleton blocks, `a-p` blocks of size `d`, and `p` blocks of size `d+1`.
At the critical endpoint,

\[
 a=\Theta(N^{2/3}),\qquad d=\Theta(N^{1/3}),\qquad n=\Theta(N).
 \tag{2.2}
\]

Let `M_0` be the orbit of NO partitions.  Every `mu_0 in M_0` has `4a` blocks: the left and
right singleton blocks and the two side-exclusive heavy palettes.

For one query orientation, let `M_1^R` be the same NO orbit with one right singleton highlighted;
define `M_1^L` symmetrically.  Highlighting changes no input values.  We write `M_1` when either
fixed orientation is understood.

Let `M_2` be the YES orbit, with its unique cross-side two-block highlighted.  All other blocks
have the same sizes as in `M_0`.  Thus every member of `M_2` has `4a-1` blocks.

Conditioned on a partition `mu`, assign values by a uniformly random injection

\[
 \lambda:\operatorname{blocks}(\mu)\hookrightarrow[q],
 \tag{2.3}
\]

and put the value `lambda(B)` at every coordinate in block `B`.  Finally choose `mu` uniformly
from its orbit.  Because assignments are injective, this is exactly the strict frozen orbit and
not the independent-label relaxation.

Merging any chosen left singleton with any chosen right singleton is a bijection between

\[
 (\mu_0,B_L,B_R),\qquad
 \mu_0\in M_0,\quad B_L\in S_L(\mu_0),\quad B_R\in S_R(\mu_0),
 \tag{2.4}
\]

and `M_2`.  Highlighting one singleton is likewise a bijection from
`(mu_0,B_R)` to `M_1^R`.  Consequently,

\[
 |M_1|=a|M_0|,\qquad |M_2|=a^2|M_0|,
 \qquad {|M_1|\over |M_2|}={1\over a}.
 \tag{2.5}
\]

## 3. Strict splitting count and failure of the operator comparison

Fix `mu_2 in M_2`, write its highlighted pair as `B={i,h}`, and suppose that the next query is
to `i`.  Splitting off `i` leaves `{h}` highlighted and produces a member `mu_1 in M_1`.

There are

\[
 (q)_{4a-1}
 \tag{3.1}
\]

strict assignments for `mu_2`.  Given one of them, the new singleton `{i}` can receive any label
not already used by the other `4a-1` blocks.  The exact number of extensions is

\[
 u=q-(4a-1)=q-4a+1\in\{1,2,3,4\},
 \tag{3.2}
\]

and hence

\[
 (q)_{4a}=u(q)_{4a-1}.
 \tag{3.3}
\]

The normalized completion map

\[
 |\lambda_2\rangle\longmapsto
 {1\over\sqrt u}\sum_{z\notin\operatorname{im}(\lambda_2)}
 |\lambda_2\cup\{\{i\}\mapsto z\}\rangle
 \tag{3.4}
\]

is an isometry.  Let `B_i` denote the Fourier projector onto supports that contain `h` and omit
`i`.  Because `B_i phi` does not depend on the fresh value at `i`, forgetting that value sends the
uniform split injection exactly to the uniform merged injection.  The valid conclusion is only

\[
 \|\Upsilon_{\mu_2}^{\partial i}\phi\|
 =\|\Upsilon_{\mu_1}B_i\phi\|.
 \tag{3.5}
\]

It is not legitimate to replace the right side of (3.5) by
`||Upsilon^+_{mu_1} phi||`.  The latter also contains Fourier terms supported on both `i` and `h`,
and strict transfer need not make those terms orthogonal to the boundary part.

### 3.1 Exact local counterexample

Fix a nonzero alphabet character `chi_c` and define

\[
 G_{ih}={1\over2}\bigl(\chi_c(y_h)-\chi_c(x_i)\bigr)
 +{q\over2}{\bf1}[x_i=y_h]\chi_c(y_h).
 \tag{3.6}
\]

Expanding the equality predicate gives

\[
 G_{ih}=\chi_c(y_h)
 +{1\over2}\sum_{r\ne0,c}\chi_r(x_i)\chi_{c-r}(y_h).
 \tag{3.7}
\]

Thus its `i`-query boundary part is exactly `B_iG_ih=chi_c(y_h)`, whose squared norm on the merged
type is one.  On the strict split type, every term in (3.7) belongs to the highlighted-singleton
plus sector.  Since `x_i != y_h` there, (3.6) reduces to

\[
 {1\over2}\bigl(\chi_c(y_h)-\chi_c(x_i)\bigr).
\]

For two uniformly distinct injected labels, nontrivial-character orthogonality yields

\[
 \|\Upsilon^+_{\mu_1}G_{ih}\|^2
 ={q\over2(q-1)}=: \eta<1,
 \qquad
 \|\Upsilon^{\partial i}_{\mu_2}G_{ih}\|^2=1.
 \tag{3.8}
\]

Therefore the generic fixed-partition inequality

\[
 \|\Upsilon^{\partial i}_{\mu_2}\phi\|
 \le \|\Upsilon^+_{\mu_1}\phi\|
 \tag{3.9}
\]

is false already at degree two.  Equation (3.4) remains an isometry, but it applies to
`B_i phi`; the additional plus terms in (3.7) destructively interfere after strict transfer.

The failure persists after orbit averaging.  Let `S_i^L:=R_i^{L,-}` be the exact
degree-at-most-four left singleton indicator from (4.4), and set

\[
 F_i={1\over\sqrt n}\sum_{h\in R}
 S_i^L G_{ih}|h\rangle|i\rangle_I.
 \tag{3.10}
\]

This vector has degree at most six.  In `M_2`, only types whose pair has left endpoint `i`
contribute, and only the workspace component indexed by the actual right endpoint is on the
`i`-query boundary.  In `M_1^R`, the vector vanishes unless `i` is a left singleton, and only the
component indexed by the highlighted right singleton is in the plus sector.  Consequently,

\[
 \|\Psi_2^\partial F_i\|^2={1\over n^2},
 \qquad
 \|\Upsilon_1^+F_i\|^2={\eta a\over n^2}.
 \tag{3.11}
\]

Since `eta<1`, this gives the direct reversal

\[
 \|\Psi_2^\partial F_i\|^2
 ={1\over n^2}
 >{1\over a}\|\Upsilon_1^+F_i\|^2
 ={\eta\over n^2}.
 \tag{3.12}
\]

Thus neither the former generic fixed-partition comparison nor the former
`|M_1|/|M_2|=1/a` full-space operator estimate survives review.

### 3.2 Promise-kernel failure at the bottom level

Independently, the usual relaxed-partition bottom lemma also fails.  Fix a left coordinate `i`
and a right coordinate `j`, and define the degree-two cross-equality polynomial

\[
 E_{ij}(x,y)={\bf1}[x_i=y_j]
 ={1\over q}\sum_{c\in\mathbb Z_q}
 \chi_c(x_i)\overline{\chi_c(y_j)}.
 \tag{3.13}
\]

Every strict NO assignment gives distinct labels to the blocks containing `i` and `j`.  Hence

\[
 \Upsilon_0E_{ij}=0.
 \tag{3.14}
\]

Now use `M_1^R`.  If its highlighted right singleton is `h=j`, the plus projector keeps exactly
the nonconstant terms in (3.13).  Strict injection still gives `x_i != y_j`, and character
orthogonality gives

\[
 {1\over q}\sum_{c\ne0}
 \chi_c(x_i)\overline{\chi_c(y_j)}=-{1\over q}.
 \tag{3.15}
\]

Thus, for every such highlighted type,

\[
 \Upsilon^+_{\mu_1}E_{ij}
 =-{1\over q}|\operatorname{Comp}(\mu_1)\rangle\ne0.
 \tag{3.16}
\]

If `h != j`, no Fourier support of (3.13) contains `h`, so the plus projection is zero.  The
highlighted singleton position is uniform over the `n` right coordinates, and therefore

\[
 \|\Upsilon_1^+E_{ij}\|^2={1\over nq^2}>0.
 \tag{3.17}
\]

Equations (3.14) and (3.17) directly refute every bottom inequality of the form

\[
 \|\Upsilon_1^+\phi\|
 \le C_t\|\Upsilon_0\phi\|.
 \tag{3.18}
\]

The relaxed support-counting proof relies on a transfer representation in which the relevant
components are orthogonal.  Strict injection introduces a promise kernel: cancellation makes the
full transfer zero, while highlighting removes part of the cancellation.

The only surviving statements in this section are the injection counts (3.1)--(3.3) and the
completion isometry (3.4)--(3.5) after explicit boundary restriction.  There is no generic
full-low-degree progress inequality and no lower-bound exponent.

## 4. Exact singleton-role leakage

A separate hoped repair was to claim that the split image, in which the queried position `i` is a
singleton, occupies only an `a/n` fraction of `M_1`.  This is false on the full low-degree space.

Work on either side.  Its total same-side collision count is the promise constant

\[
 K_0=(a-p){d\choose2}+p{d+1\choose2}.
 \tag{4.1}
\]

For a fixed coordinate `i`, define

\[
 K_{-i}=\sum_{\substack{j<k\\j,k\ne i}}\mathbf 1[x_j=x_k].
 \tag{4.2}
\]

If `f_i` is the multiplicity of the value at `i`, then on every legal input

\[
 K_0-K_{-i}=f_i-1\in\{0,d-1,d\}.
 \tag{4.3}
\]

Therefore

\[
 R_i^-=
 {\bigl(K_0-K_{-i}-(d-1)\bigr)
  \bigl(K_0-K_{-i}-d\bigr)\over d(d-1)}
 \tag{4.4}
\]

is exactly one when `i` is a singleton and exactly zero when `i` belongs to a heavy block.

Each equality predicate in (4.2) has Fourier degree two.  Thus `R_i^-` has degree at most four,
and every Fourier term omits coordinate `i`.  This is an exact algebraic role test available even
when `i` itself is unqueried.

For any nonzero alphabet character `chi_c`, put

\[
 R_i^+=\chi_c(x_i)R_i^-.
 \tag{4.5}
\]

It has degree at most five, every Fourier support contains `i`, and
`|R_i^+|=R_i^-` on legal inputs.  The orthogonal-workspace vector

\[
 \Phi={1\over\sqrt a}\sum_i R_i^+|i\rangle
 \tag{4.6}
\]

has pointwise norm one because exactly `a` positions on the chosen side are singletons.  If `h`
is the highlighted singleton, the `i=h` component is wholly in the knowledge sector and has
squared norm `1/a`.  Hence

\[
 {\|\Upsilon_1^+\Phi\|\over\|\Upsilon_0\Phi\|}
 \ge {1\over\sqrt a},
 \tag{4.7}
\]

already at degree five.  A bound `O(sqrt(t/n))` would give `O(n^(-1/2))` here and is false by the
factor `sqrt(n/a)=Theta(sqrt d)`.

Independently, the hoped `n`-denominator target has another explicit obstruction.  Fix a left
query position `i_0` and define, with right-side role polynomials,

\[
 \Phi_{i_0}={1\over\sqrt a}
 \sum_{h\in R} R_{i_0}^{L,-}R_h^{R,+}|h\rangle|i_0\rangle_I.
 \tag{4.8}
\]

This vector has degree at most nine.  It vanishes unless `i_0` is a left singleton, so its
`M_1` mass is entirely in the split image.  When the highlighted right singleton is `h`, the
workspace component `|h>` contains `h` in every Fourier support and omits `i_0`, so it is exactly
a boundary component for querying `i_0`.  After normalizing by its `Upsilon_0` norm,

\[
 \|\Psi_2^\partial\Phi_{i_0}\|=\Omega(1/a).
 \tag{4.9}
\]

Thus a claimed `O(sqrt(t)/n)` bound is false at constant `t`, by the full factor

\[
 {n\over a}=\Theta(d)=\Theta(N^{1/3}).
 \tag{4.10}
\]

The earlier possible intermediate estimate obtained by multiplying by an `a/n` image-rarity
factor is therefore invalid.  Section 3.1 already refutes the generic split comparison, and
Section 3.2 separately refutes the bottom transfer comparison.  Hence neither an `N^(5/9)` nor an
`N^(4/9)` consequence is licensed by this hierarchy.

## 5. Anti-concentration: classical posterior passes, operator statement fails

### 5.1 Classical conditioning

Fix a classical query database `D` of at most `T` coordinates and their values, and condition on
seeing no queried equal cross pair.  Under the uniform strict YES distribution, at least one
endpoint of the unique pair is unqueried.  Permutations of unqueried coordinates on each side fix
`D` and preserve the conditional distribution.  Consequently:

* if both endpoints of a proposed `rho` are queried, its conditional probability is zero;
* if exactly one is queried, the other is uniform over the compatible unqueried coordinates on
  its side, giving probability at most `1/(n-T)`;
* if both are unqueried, their ordered cross position is uniform over the compatible unqueried
  cross pairs, giving probability at most `1/(n-T)^2`.

Equivalently, one may alter any completion by splitting its current pair and merging any chosen
unqueried left/right singleton blocks.  For `T<=ca`, this supplies `Omega(a^2)` alternatives while
preserving the database; the relabeling can be chosen bijectively because at most one old pair
endpoint was recorded.  Thus ordinary posterior anti-concentration is not the obstacle.

### 5.2 Exact degree-two operator counterexample

The required Belovs operator statement is stronger than the preceding classical fact and is
false.  Fix `rho=(i,j)` and let

\[
 \phi_\rho(x,y)={\bf1}[x_i=y_j]
 ={1\over q}\sum_{c\in\mathbb Z_q}
 \chi_c(x_i)\overline{\chi_c(y_j)}.
 \tag{5.1}
\]

This lies in `X_{<=2}`.  Let a YES type have actual highlighted pair `B`.

If `B=rho`, the nonconstant terms in (5.1) have support containing both endpoints and are removed
by `Upsilon^-`; the constant term remains.  Therefore

\[
 \Upsilon^-_{\mu_B}\phi_\rho={1\over q}\,|\operatorname{Comp}(\mu_B)\rangle\ne0.
 \tag{5.2}
\]

If `B != rho`, neither the empty support nor the support `rho` contains `B`, so the whole
polynomial belongs to the minus sector.  Strict injection makes the two blocks containing `i`
and `j` carry distinct labels, and hence

\[
 \Upsilon^-_{\mu_B}\phi_\rho
 =\Upsilon_{\mu_B}\phi_\rho=0.
 \tag{5.3}
\]

It follows exactly that

\[
 M_\rho\Upsilon^-\phi_\rho=\Upsilon^-\phi_\rho\ne0,
 \qquad
 {\|M_\rho\Upsilon^-\phi_\rho\|
  \over\|\Upsilon^-\phi_\rho\|}=1.
 \tag{5.4}
\]

Thus every proposed anti-concentration constant `gamma<1` fails already at degree two.

For clarity, an earlier candidate expression

\[
 1-\sum_{(u,v)\ne(i,j)}\mathbf 1[x_u=y_v]
 \tag{5.5}
\]

equals (5.1) after restriction to legal YES strings, but it is **not** interchangeable with
(5.1) before the plus/minus Fourier projection: the transfer has a nontrivial promise kernel.
The exact witness for (5.4) is (5.1).

The relaxed independent-label model avoids (5.3), because two distinct blocks can accidentally
receive the same label.  This is precisely why a relaxed anti-concentration theorem cannot be
imported into the strict orbit here.

## 6. Why a classical recording proof does not lift

For a database touching `k` latent blocks, a strict completion state has the schematic form

\[
 |\operatorname{Comp}(\mu,D)\rangle=
 {1\over\sqrt{(q-k)_{b-k}}}
 \sum_{\lambda\text{ injective},\ \lambda\supset D}|\lambda\rangle.
 \tag{6.1}
\]

Classical databases are orthogonal events, but Fourier-recording components transferred to the
strict injection distribution are coordinated through the same low-degree control vector and can
interfere.  Equation (5.4) is an explicit instance: destructive cancellation makes
`phi_rho` vanish on every wrong strict type, while the knowledge projection removes exactly the
term needed for cancellation on the right type.

Permutation/completion database spaces are also not a product tensor decomposition.  The local
Jeffery--Zur source treats permutation distributions with separate representation-theoretic
projectors and identifies non-product compressed-oracle extensions as a methodological boundary;
it supplies no theorem for the present random injection plus random heavy partition.  More
importantly, even a perfect orthogonalization of classical completions would not validate the
specific full-low-degree minus space, because (5.4) directly refutes its desired norm inequality.

## 7. First failed inequalities and exponent status

The exact failures are:

1. **Generic fixed-partition split comparison, false at degree two.**  The witness `G_ih`
   satisfies
   \[
    \|\Upsilon_{\mu_2}^{\partial i}G_{ih}\|^2=1,
    \qquad
    \|\Upsilon_{\mu_1}^{+}G_{ih}\|^2=\eta<1.
   \]
   The completion map is isometric only after applying the boundary projector `B_i`.
2. **Orbit-averaged split comparison, false at degree six.**  The witness `F_i` gives
   \[
    \|\Psi_2^\partial F_i\|^2={1\over n^2}
    >{1\over a}\|\Upsilon_1^+F_i\|^2={\eta\over n^2}.
   \]
3. **Bottom transfer comparison, false at degree two.**  The strict promise-kernel witness
   `E_ij` satisfies
   \[
    \|\Upsilon_0E_{ij}\|=0,
    \qquad
    \|\Upsilon_1^+E_{ij}\|^2={1\over nq^2}>0.
   \]
   Hence not even an `a`-denominator bottom estimate follows from support counting.
4. **Split-image rarity, false at degree four.**  For the image `I_i subset M_1` in which an
   unqueried coordinate `i` is a singleton, no uniform inequality of the form
   \[
    \sum_{\mu\in I_i}\|\Upsilon_\mu\phi\|^2
    \le C{a\over n}\sum_{\mu\in M_1}\|\Upsilon_\mu\phi\|^2
   \]
   can hold.  `R_i^-` is supported exactly on `I_i`.
5. **Summed singleton-role bound, false at degree five.**
   \[
    \|\Upsilon_1^+\phi\|
    \le C\sqrt{t/n}\,\|\Upsilon_0\phi\|
   \]
   is contradicted by (4.6)--(4.7).
6. **Target query gain, false at degree nine.**
   \[
    \|\Psi_2^\partial\phi\|
    \le C\sqrt t/n\,\|\Upsilon_0\phi\|
   \]
   is contradicted by (4.8)--(4.10).
7. **Constant anti-concentration, false at degree two.**
   \[
    \|M_\rho\Upsilon^-\phi\|\le\gamma\|\Upsilon^-\phi\|,
    \qquad \gamma<1,
   \]
   is contradicted with equality ratio one by (5.1)--(5.4).

No generic progress estimate survives.  Only the block/injection counts and the completion
isometry for an explicitly boundary-restricted polynomial remain valid.  Therefore this hierarchy
gives no new lower-bound exponent.  The existing `Omega(N^(11/18))` exact-promise lower bound comes
from a separate addressed-composition argument and remains intact.

## 8. Gate ledger

| Obligation | Outcome |
|---|---|
| exact YES/NO random-partition distributions | **PASS**, Section 2 |
| strict random injection, no relaxed transfer | **PASS**, (2.3) |
| exact block-orbit counts | **PASS**, (2.5) |
| boundary-restricted completion isometry | **PASS only after `B_i`**, (3.2)--(3.5) |
| generic fixed-partition split comparison | **FAIL**, degree-two `G_ih`, (3.6)--(3.9) |
| generic orbit-averaged split comparison | **FAIL**, degree-six `F_i`, (3.10)--(3.12) |
| heavy-size loss in a generic transition | **NOT REACHED**; comparison already fails |
| strict bottom support-counting | **FAIL**, promise-kernel witness (3.13)--(3.18) |
| desired `O(T^(3/2)/N)` progress | **FAIL**, multiple explicit constant-degree leakages |
| generic accumulated-progress theorem | **NONE obtained** |
| new lower-bound exponent from this hierarchy | **NONE** |
| classical posterior anti-concentration | **PASS** for a fixed orthogonal database |
| required operator anti-concentration | **FAIL**, exact ratio one at degree two |
| endpoint `Omega(N^(2/3))` | **NOT PROVED** |
| improvement over `Omega(N^(11/18))` | **NONE** |
| relaxed strict-transfer hypothesis used | **NO** |
| DAG/status edit | **NONE** |

## 9. Outside-node untested ideas

The counterexamples use the full low-degree space `X_{<=t}` and the certificate-support knowledge
projector.  A materially different route would have to remove the promise-kernel witnesses or
prove that algorithm-reachable states cannot exploit them.  Two examples are:

1. a representation-theoretic strict-injection adversary/projector on the two exact orbit modules,
   quotienting the strict promise ideal before defining knowledge;
2. a reachability-sensitive recording filtration that is strictly smaller than the full
   `X_{<=t}` image and remains invariant under every query.

Neither idea was tested here.  They are outside the registered node's declared projector
architecture and require Rule-8 registration before work begins.

## 10. Source boundary

* Exact promise: `ksum/artifacts/ksum_L3_hidden_frequency_promise_20260721.md`.
* Existing endpoint bracket: `ksum/artifacts/ksum_L3_hidden_frequency_critical_adversary_attempt_20260721.md`.
* Belovs framework, splitting hierarchy, relaxed-partition bottom norm, and ED query gain:
  `ksum/artifacts/references/bel2026/new-adversary_v6.tex`, especially lines 2182--2604.
* Non-product/permutation recording boundary:
  `ksum/artifacts/references/ksum_W_walkopt/compressed_oracle_adversary_2509.07876_eprint_src/arxiv_v1-new.tex`.

## 11. Bottom line

Strict injection counting was not the obstruction: the unused-label factor cancels exactly.
The obstruction is algebraic leakage caused by the exact frozen promise.  Constant Fourier degree
already breaks the generic split comparison and the bottom transfer comparison, identifies
singleton roles without querying the tested coordinate, and makes the no-known-pair operator
concentrate perfectly on one output type.
Therefore the standard Belovs recording-query route cannot deliver the critical
`Omega(N^(2/3))` endpoint.  Any continuation must use a genuinely different projector/adversary,
not another estimate inside this hierarchy.
