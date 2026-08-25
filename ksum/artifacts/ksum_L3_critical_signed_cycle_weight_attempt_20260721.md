# L3 critical signed cycle-weight law: exact tests and a constant ceiling

Date: 2026-07-22  
Canonical scope:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.orbit-intertwiner-adversary.ALT.signed-cycle-weight-law`  
Verdict: **FAIL for the registered standalone cycle-kernel separation; PARTIAL for the full
critical endpoint**  
Status discipline: proposer-tier result only; **no DAG/status edit**

## 1. Executive verdict

The requested `Omega(m^(1/6))` separation does not occur in the declared address-cycle operator
by itself.  There are two possible precise readings of a "one-point-marked address operator," and
both give an exact obstruction.

1. If marking means restricting the address symmetry group to the stabilizer of the marked point,
   then the underlying matrix is unchanged.  A unitary marked Fourier decomposition therefore
   gives

   \[
   \|K_w\|=\max_\psi\|K^\bullet_{w,\psi}\|.
   \tag{1.1}
   \]

   The unmarked/marked ratio is exactly one for **every** signed colored-cycle weight, including
   nonseparable dependence on long-heavy exclusion mismatches.
2. If "marked operators" means the local status pieces exposed by the mark, then those pieces
   partition the unmarked matrix.  A marked singleton or short-heavy point gives two pieces and

   \[
   \|K_w\|\le2\max_\zeta\|K^\bullet_{w,\zeta}\|.
   \tag{1.2}
   \]

   A long-heavy occurrence gives at most ten pairing/exclusion pieces and hence another absolute
   constant ceiling.  For the Krawtchouk/Hamming exclusion laws the sharper ceiling is three.

These identities already apply on the infinite legal critical subsequence with remainder `p=0`.
On that subsequence `m` tends to infinity, while (1.1) or (1.2) remains `O(1)`, so it is
`o(m^(1/6))`.

The sign character, arbitrary irreducible characters, the cycle-number law `z^(#cycles)`, general
product-over-cycle laws, and Krawtchouk exclusion-mismatch laws were all tested analytically below.
No numerical spectrum is used.

This does **not** refute the full endpoint adversary.  It exposes a type gap in the previous
separated ansatz: an address-cycle kernel is a square operator on one address fiber, whereas the
real adversary is a rectangular map from addressed NO inputs to addressed YES inputs.  A
nonseparable coupling between the outer `UIC` adversary and relative addresses might evade the
ceiling, but that is a new ansatz outside this registered standalone family.  It was registered
separately under Rule 8 and was not tested in this memo.

## 2. Exact address module and types

Fix one side of a full-orbit input.  Let

* `S` be its `a` singleton labels;
* `H_0` be its `a-p` frequency-`d` heavy labels;
* `H_1` be its `p` frequency-`d+1` heavy labels;
* `m=d+1`.

An address is a pair

\[
 \alpha=(\phi,e),
 \qquad
 \phi:S\overset{\sim}{\longrightarrow}H_0\sqcup H_1,
 \qquad
 e=(e_h)_{h\in H_1}\in[m]^p,
 \tag{2.1}
\]

where `e_h` selects the public excluded occurrence of a long heavy label.  Hence the address set is

\[
 \Omega_{a,p,m}=\{(\phi,e)\},
 \qquad
 |\Omega_{a,p,m}|=a!m^p,
 \tag{2.2}
\]

and a standalone address kernel has the exact type

\[
 K_w:\ell_2(\Omega_{a,p,m})\longrightarrow
       \ell_2(\Omega_{a,p,m}),
 \qquad
 K_w\in\mathbb C^{a!m^p\times a!m^p}.
 \tag{2.3}
\]

The address automorphism group permutes `S`, short heavy labels, long heavy labels, and the `m`
occurrences within each long label.  Pair orbits are the colored alternating matching cycles,
together with the equality/difference flag for the two exclusions at each long vertex.  Thus any
weight `w_theta` declared in the registered node gives

\[
 K_w(\alpha,\beta)=w_{\theta(\alpha,\beta)}.
 \tag{2.4}
\]

Formula (2.4) includes weights by cycle length, number of cycles, sign, representation character,
products over cycles, and arbitrary coupling to the long-exclusion mismatch flags.

## 3. The exact one-point restriction identity

Let `G_addr` be the address automorphism group and let `H_zeta` be the stabilizer after marking one
singleton coordinate, one short-heavy occurrence, or one long-heavy occurrence.  Since `K_w` is
`G_addr`-invariant, it is also `H_zeta`-invariant.  Choose a unitary isotypic decomposition

\[
 U_\zeta:\ell_2(\Omega_{a,p,m})
 \overset{\sim}{\longrightarrow}
 \bigoplus_{\psi\in\widehat H_\zeta}
 \mathbb C^{d_\psi}\otimes\mathbb C^{r_{\zeta,\psi}}.
 \tag{3.1}
\]

The same matrix (2.3) has the exact block identity

\[
 U_\zeta K_wU_\zeta^*
 =\bigoplus_{\psi\in\widehat H_\zeta}
 I_{d_\psi}\otimes K^\bullet_{w,\zeta,\psi}.
 \tag{3.2}
\]

Therefore

\[
 \boxed{
 \|K_w\|
 =\max_{\psi\in\widehat H_\zeta}
   \|K^\bullet_{w,\zeta,\psi}\|
 }
 \tag{3.3}
\]

for every marked point type `zeta`.  This is just unitary invariance of operator norm, but it is the
essential type check: a one-point extension refines the orbital and Fourier labels; it does not
change a matrix.

The same fact can be written entrywise.  Let `T_eta` be the one-point-marked orbitals and let
`F(eta)` forget the mark.  Every ordered pair of addresses belongs to exactly one marked orbit, so

\[
 K_w
 =\sum_\eta w_{F(\eta)}T_\eta.
 \tag{3.4}
\]

Equation (3.4) is the exact finite marked-operator identity missing from the earlier informal
system.  Fourier transforming its right-hand side gives (3.2), not a smaller-norm operator.

It follows immediately that the ratio requested in the registered node, when "marked block" has
its standard representation-theoretic meaning, is

\[
 {\|K_w\|\over\max_\psi\|K^\bullet_{w,\zeta,\psi}\|}=1.
 \tag{3.5}
\]

This conclusion is independent of signs, colors, `a,p,m`, and the formula used for `w`.

## 4. Local-status reading: a constant partition ceiling

Perhaps the intended marked operator was not the restriction (3.2), but one of the entrywise
pieces revealed by a mark.  That reading still gives a constant ceiling.

### 4.1 Marked singleton or short-heavy vertex

Identify two matching addresses `phi,psi` by their relative permutation

\[
 \pi=\phi^{-1}\psi\in S_a.
 \tag{4.1}
\]

For a marked singleton `s`, let

\[
 P_s^=(\phi,\psi)={\bf1}[\phi(s)=\psi(s)]
                 =\mathbf 1[\pi(s)=s],
 \qquad
 P_s^\ne=1-P_s^=.
 \tag{4.2}
\]

Define `K_w^= = K_w circ P_s^=` and `K_w^ne = K_w circ P_s^ne`.  These are the two aggregate
one-point status operators.  Entrywise,

\[
 K_w=K_w^=+K_w^\ne.
 \tag{4.3}
\]

Thus

\[
 \boxed{
 \|K_w\|\le\|K_w^=\|+\|K_w^\ne\|
 \le2\max\{\|K_w^=\|,\|K_w^\ne\|\}.
 }
 \tag{4.4}
\]

Marking a short-heavy vertex gives the identical same-partner/different-partner partition.
Consequently any requirement that controls every local marked status has ratio at most two.

### 4.2 Marked long-heavy occurrence

Fix a long heavy label `h` and one of its physical occurrences `v in [m]`.  For a pair of addresses,
the two matching partners of `h` are equal or different.  Independently, the two exclusions
`e_h,e'_h` occupy exactly one of the five states

\[
\begin{array}{lll}
(1)&e_h=v,       &e'_h=v,\\
(2)&e_h=v,       &e'_h\ne v,\\
(3)&e_h\ne v,   &e'_h=v,\\
(4)&e_h=e'_h\ne v,\\
(5)&e_h\ne e'_h,&e_h,e'_h\ne v.
\end{array}
 \tag{4.5}
\]

Hence at most ten pairing/exclusion status matrices `K_(b,r)`, with `b in {=,ne}` and
`r in {1,...,5}`, have disjoint entry supports and satisfy

\[
 K_w=\sum_{b,r}K_{w,b,r}.
 \tag{4.6}
\]

The triangle inequality yields the universal bound

\[
 \|K_w\|\le10\max_{b,r}\|K_{w,b,r}\|.
 \tag{4.7}
\]

The number ten is not important; its independence from `m` is.  Equations (4.4) and (4.7) apply
even when cycle weights and exclusion flags are coupled nonseparably.

## 5. Uncolored matching algebra and exact Fourier formula

The legal case `p=0` is especially decisive.  Choose reference orderings of `S` and the heavy
labels.  An address is a permutation `sigma in S_a`, and

\[
 \ell_2(\Omega_{a,0,m})=\ell_2(S_a),
 \qquad \dim\ell_2(S_a)=a!.
 \tag{5.1}
\]

Every cycle-structure law is a class function `w:S_a -> C`.  Its kernel is right convolution,

\[
 (K_wf)(\sigma)
 =\sum_{\tau\in S_a}w(\sigma^{-1}\tau)f(\tau)
 =\sum_{\pi\in S_a}w(\pi)f(\sigma\pi).
 \tag{5.2}
\]

Let `f^lambda=dim S^lambda` and `chi^lambda` be the irreducible character.  The regular Fourier
decomposition gives the exact eigenvalue

\[
 \kappa_\lambda(w)
 ={1\over f^\lambda}\sum_{\pi\in S_a}w(\pi)\chi^\lambda(\pi),
 \tag{5.3}
\]

and therefore

\[
 \boxed{
 \|K_w\|=\max_{\lambda\vdash a}|\kappa_\lambda(w)|.
 }
 \tag{5.4}
\]

This is the exact finite operator system for every uncolored cycle-length/number, sign-character,
and representation-character law.

## 6. Cycle-number weights: Jucys--Murphy diagonalization

Test the formula family

\[
 w_z(\pi)=z^{c(\pi)},
 \tag{6.1}
\]

where `c(pi)` is the number of permutation cycles and `z` may depend on the parameters.  Let

\[
 J_1=0,\qquad J_k=\sum_{i<k}(i\ k).
 \tag{6.2}
\]

The Jucys identity is

\[
 Z_a(z):=\sum_{\pi\in S_a}z^{c(\pi)}\pi
 =\prod_{k=1}^a(z+J_k).
 \tag{6.3}
\]

On the Specht module `S^lambda`, this central element is the scalar

\[
 P_\lambda(z)=\prod_{b\in\lambda}(z+\operatorname{ct}(b)),
 \qquad
 \operatorname{ct}(i,j)=j-i.
 \tag{6.4}
\]

Thus

\[
 \|K_{w_z}\|=\max_{\lambda\vdash a}|P_\lambda(z)|.
 \tag{6.5}
\]

Mark the point `a`.  The fixed-point and moved-point group-algebra pieces are

\[
 Z_a^=(z)=z\,\iota(Z_{a-1}(z)),
 \qquad
 Z_a^\ne(z)=Z_a(z)-Z_a^=(z),
 \tag{6.6}
\]

where `iota` embeds `S_(a-1)` as the stabilizer of `a`.  Under the multiplicity-free branching
`mu nearrow lambda`, let `b=lambda\setminus mu` be the removed box.  The exact two marked
eigenvalues on that branch are

\[
 zP_\mu(z),
 \qquad
 P_\lambda(z)-zP_\mu(z)
 =\operatorname{ct}(b)P_\mu(z).
 \tag{6.7}
\]

Since

\[
 P_\lambda(z)=(z+\operatorname{ct}(b))P_\mu(z),
 \tag{6.8}
\]

(6.7) gives the exact uniform ceiling

\[
 \|K_{w_z}\|
 \le2\max\{\|K_{w_z}^=\|,\|K_{w_z}^\ne\|\}.
 \tag{6.9}
\]

This holds for every real or complex `z`, including `z=z(a,m)`.  Taking very large `z` can make the
moved piece alone look small, but it simply concentrates the law on the identity/same-address
relation; the fixed piece in (6.7) is then large.  It is the already eliminated diagonal kernel,
not an address-erasure gain.

## 7. Sign and representation-character laws

### 7.1 Sign character

The sign law is contained in (6.1) up to a global sign because

\[
 (-1)^{c(\pi)}=(-1)^a\operatorname{sgn}(\pi).
 \tag{7.1}
\]

It is also useful to see its matrices directly.  Let `b=(a-1)!`.  Conjugating rows and columns by
the diagonal sign matrix turns the unmarked sign kernel into `J_(a!)`.  The fixed-point part is `a`
diagonal blocks `J_b`, while the moved part is the complete `a`-partite block matrix.  Hence

\[
 \|K_{\rm sgn}\|=a!,
 \qquad
 \|K_{\rm sgn}^=\|=(a-1)!,
 \qquad
 \|K_{\rm sgn}^\ne\|=(a-1)(a-1)!.
 \tag{7.2}
\]

Therefore

\[
 {\|K_{\rm sgn}\|
  \over\max\{\|K_{\rm sgn}^=\|,\|K_{\rm sgn}^\ne\|\}}
 ={a\over a-1}=1+O(a^{-1}).
 \tag{7.3}
\]

The most obvious signed law has asymptotic ratio one.

### 7.2 Irreducible-character weights

For any partition `eta |- a`, take

\[
 w_\eta(\pi)=\chi^\eta(\pi).
 \tag{7.4}
\]

Character orthogonality in (5.3) gives

\[
 \kappa_\lambda(w_\eta)
 ={a!\over f^\eta}{\bf1}[\lambda=\eta],
 \qquad
 \|K_{w_\eta}\|={a!\over f^\eta}.
 \tag{7.5}
\]

Under a one-point restriction this is still the same matrix, so (3.3) gives ratio exactly one.  If
the fixed/moved status pieces are used instead, (4.4) gives ratio at most two.  Thus no choice of
Young diagram, including parameter-dependent diagrams, yields `m^(1/6)`.

### 7.3 General product-over-cycle laws

A law

\[
 w(\pi)=\prod_{\ell\ge1}t_\ell^{c_\ell(\pi)}
 \tag{7.6}
\]

is again a class function and can be signed or complex before taking a Hermitian real part.  It may
not have the one-parameter product formula (6.3), but the exact identities (3.3) and (4.4) do not
use that formula.  They cover all weights (7.6), and indeed every linear combination of
representation characters.

## 8. Long-heavy exclusion mismatches and Krawtchouk laws

To test the part of the registered family depending explicitly on exclusion mismatches, first
separate the exclusion-choice space `[m]^p`.  Let `A_r^(p,m)` be the adjacency matrix of the Hamming
relation `d_H(e,e')=r`.  A radial signed law is

\[
 L_w=\sum_{r=0}^p w_r A_r^{(p,m)}.
 \tag{8.1}
\]

Its exact eigenvalues are

\[
 \Lambda_j(w)=\sum_{r=0}^p w_rK_r^{(p,m)}(j),
 \qquad 0\le j\le p,
 \tag{8.2}
\]

where

\[
 K_r^{(p,m)}(j)
 =\sum_{\ell=0}^r(-1)^\ell(m-1)^{r-\ell}
   {j\choose\ell}{p-j\choose r-\ell}.
 \tag{8.3}
\]

Thus

\[
 \|L_w\|=\max_{0\le j\le p}|\Lambda_j(w)|.
 \tag{8.4}
\]

Now isolate one long label.  The Hamming recurrence is the exact matrix identity

\[
 A_r^{(p,m)}
 =I_m\otimes A_r^{(p-1,m)}
 +(J_m-I_m)\otimes A_{r-1}^{(p-1,m)},
 \tag{8.5}
\]

with `A_(-1)=0`.  Put

\[
 B_0=\sum_{r=0}^{p-1}w_rA_r^{(p-1,m)},
 \qquad
 B_1=\sum_{r=0}^{p-1}w_{r+1}A_r^{(p-1,m)}.
 \tag{8.6}
\]

Then

\[
 L_w=I_m\otimes B_0+(J_m-I_m)\otimes B_1.
 \tag{8.7}
\]

Fix the marked physical occurrence `v`, set `E=|v><v|`, `Q=I-E`, and
`u=Q 1`.  The five exclusion statuses (4.5) give

\[
\begin{aligned}
 L_w={}&E\otimes B_0+Q\otimes B_0
 +|v\rangle\langle u|\otimes B_1
 +|u\rangle\langle v|\otimes B_1\\
 &+(|u\rangle\langle u|-Q)\otimes B_1.
\end{aligned}
 \tag{8.8}
\]

This is the exact long-exclusion one-point identity.  For `m>=3`, the component norms are

\[
 \|B_0\|,\quad \|B_0\|,\quad
 \sqrt{m-1}\|B_1\|,\quad\sqrt{m-1}\|B_1\|,\quad
 (m-2)\|B_1\|.
 \tag{8.9}
\]

On the other hand, (8.7) gives

\[
 \|L_w\|\le\|B_0\|+(m-1)\|B_1\|.
 \tag{8.10}
\]

Let `D_mark` be the maximum in (8.9).  For every `m>=3`,

\[
 {\|L_w\|\over D_{\rm mark}}
 \le1+{m-1\over m-2}\le3.
 \tag{8.11}
\]

The case `m=2` is bounded by two using the two cross pieces.  Hence every signed Krawtchouk/Hamming
law has an absolute marked/unmarked ceiling.  A tensor product with a matching-cycle law cannot
help: a marked singleton still invokes (4.4), so the whole product ratio is at most two.

For nonseparable colored laws that couple the cycle word and exclusion flags, (8.11) need not
factor, but the general same-matrix identity (3.3) and the ten-piece bound (4.7) still apply.

## 9. Infinite legal `p=0` critical subsequence

Uniformity over all legal integer remainders is decisive.  For every integer `k>=2`, take

\[
 a=k^2,\qquad q=4k^2,\qquad d=k,\qquad p=0,
 \qquad n=a(d+1)=k^2(k+1),\qquad m=k+1.
 \tag{9.1}
\]

Then (2.1) of the endpoint promise holds exactly:

\[
 \left\lfloor{n-a\over a}\right\rfloor=k=d,
 \qquad (n-a)-ad=0=p.
 \tag{9.2}
\]

Moreover

\[
 a=\Theta(n^{2/3}),\qquad m=\Theta(n^{1/3}),
 \qquad m\longrightarrow\infty.
 \tag{9.3}
\]

There are no long-exclusion flags on this subsequence, so every registered formula collapses to a
signed cycle-structure law on `S_a`.  Equations (3.5) and (4.4) give, respectively,

\[
 \mathcal R_{\rm addr}=1
 \quad\text{or}\quad
 \mathcal R_{\rm addr}\le2.
 \tag{9.4}
\]

Therefore

\[
 \mathcal R_{\rm addr}=O(1)=o(m^{1/6}).
 \tag{9.5}
\]

No exclusion-mismatch weighting can repair a uniform theorem because those variables do not exist
on the legal sequence (9.1).

## 10. Type audit of the proposed lift

The preceding ceiling also reveals why the earlier separated inequality was not yet a valid
endpoint construction.  The typed spaces are different.

The standalone address kernel is the square map (2.3).  The actual lifted adversary would have to
be a rectangular map

\[
 \widetilde\Gamma:
 \ell_2\{(y,\beta):y\in X_0,\ \beta\in\mathcal Z_0(y)\}
 \longrightarrow
 \ell_2\{(x,\alpha):x\in X_1,\ \alpha\in\mathcal Z_1(x)\},
 \tag{10.1}
\]

followed by normalized incidence maps to

\[
 \Gamma:\ell_2(X_0)\longrightarrow\ell_2(X_1).
 \tag{10.2}
\]

The two address sets in (10.1) belong to different inputs and answer classes.  A relative-address
kernel on one fixed input does not canonically identify their outer `UIC` coordinates.  No formula
for `widetilde Gamma`, no domains/codomains for its proposed tensor factors, and no identity for
`widetilde Gamma circ Delta_i` were supplied in the previous reduction.

This distinction matters because a query mask changes the YES/NO input-pair matrix; merely marking
an address point does not, as (3.2) shows.  If one instead keeps only the moved-address piece in
(4.3), a diagonal address kernel can have a zero denominator, contradicting the already established
fact that the same-address lifted BHK witness has ratio one.  The missing outer/input action is
exactly what resolves that contradiction.

Consequently one cannot multiply the addressed `N^(11/18)` ratio by a standalone address ratio
from (3.5).  A valid continuation would first need a formula-defined, type-correct coupling in
(10.1), then derive its full query-mask blocks.  That coupled outer-address construction is not the
registered standalone signed-cycle family and was not tested here.

## 11. Coverage and gate ledger

| Registered obligation or candidate | Exact outcome |
|---|---|
| cycle-length/number weights | covered by central convolution (5.2)--(5.4) and ceiling (3.3)/(4.4) |
| `z^(#cycles)` family | exact Jucys spectrum (6.3)--(6.7); ratio at most two |
| sign character | exact ratio `a/(a-1)=1+O(1/a)` |
| arbitrary irreducible character | exact unmarked norm `a!/f^eta`; marked restriction ratio one |
| general product-over-cycles law | universal restriction identity; no growing ratio |
| Krawtchouk exclusion mismatches | exact Hamming spectrum and one-point recurrence; ratio at most three |
| nonseparable colored mismatch dependence | same-matrix ratio one; status-piece ceiling at most ten |
| every legal remainder | killed by the infinite `p=0` sequence (9.1) |
| `Omega(m^(1/6))` standalone address ratio | **FAIL** |
| typed lift to full YES/NO adversary | **not defined by this family** |
| endpoint `Omega(N^(2/3))` witness | **not obtained and not refuted** |
| numerical spectra | none used |
| DAG/status edit | none |

## 12. Scope boundary and untested outside-node idea

The analysis generated one possible escape: replace the square address kernel by a genuinely
nonseparable rectangular kernel that couples the outer `UIC` adversary, YES/NO address fibers, and
the cycle data before incidence compression.  This is materially different from multiplying an
address-cycle norm ratio into the addressed witness.  Before any calculation it was registered as
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.orbit-intertwiner-adversary.ALT.coupled-uic-address-cycle-kernel`.
**No calculation on that successor is part of this memo.**

No other new ansatz was generated or tested.

## 13. Bottom line

Signed cycles do not erase addresses merely by changing the Fourier basis.  A one-point extension
of a square invariant address kernel is the same matrix and has the same norm.  If one interprets
the mark as a local status split, the pieces reconstruct the unmarked matrix and impose an absolute
constant ceiling.  Sign, Jucys cycle-number, representation-character, and Krawtchouk mismatch
weights all realize this obstruction explicitly.

On an infinite exact critical sequence with `p=0`, the best possible ratio in the registered
standalone formulation is `O(1)=o(m^(1/6))`.  Therefore this coefficient family cannot provide the
missing `N^(1/18)` factor as presently formulated.  The full critical endpoint remains open because
a different, type-correct outer/address coupling could behave differently; that would require its
own registered node and a fresh analysis.
