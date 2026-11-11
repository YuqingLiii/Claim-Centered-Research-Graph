# Product-Haar depth versus matrix dimension: quantitative full-size audit

Date: 2026-08-30

Status: proposer-side theoretical audit. No canonical completion level is changed by this note.

All logarithms in entropy formulas are base two. Natural logarithms are written `ln`.

## Executive verdict

The finite-dimensional product-Haar construction has two very different conclusions.

1. For every fixed generator count `m` and depth `J`, Bordenave--Collins Theorem 9.2 supplies
   strong convergence in probability as the per-leg matrix dimension `D` tends to infinity. This
   is enough to select one finite successful realization and therefore proves the already separated
   **absolute-unbounded** theorem.
2. The local source does **not** state a growing-depth theorem with a displayed threshold `D(J)`
   for the coefficient-uniform entropy event. Lemma 9.3 is an expectation estimate for one linear
   pencil; the entropy proof needs a simultaneous estimate over a Hilbert--Schmidt coefficient
   sphere for a degree-`2J` polynomial. Theorem 8.3 and Lemma 7.4 indicate how an effective
   linearization/concentration proof could be assembled, but that uniform assembly and all of its
   constants are not a theorem presently registered in the project.

More importantly, no such assembly based on the published factor can establish the
Hayden--Penington full-size conclusion. The optimistic linear-pencil estimate already forces
`D(J)` to be unbounded, with `ln D(J)=Omega_m(ln J)`. The certified gap is only `Theta(J)`, while
the primitive input cost contains `J log D(J)`. Consequently the certified gap divided by full
logarithmic size tends to zero. Effective polynomial linearization and a direct epsilon-net only
make the dimension requirement worse.

Thus the sharp conclusion is a **proof-certificate obstruction**, not a channel impossibility:

> the local tensor-strong-convergence theorem proves fixed-depth existence and absolute
> unboundedness, but neither states nor can its published quantitative factor certify a
> full-size-extensive product-Haar family.

## 1. The event actually needed by the entropy argument

Fix `m>e^18`, depth `J`, and set

\[
 q=m^J,
 \qquad
 W_v^{(D)}=\bigotimes_{j=1}^J U_{v_j,j}^{(D)},
 \qquad v\in[m]^J.
\]

For a traceless Hermitian coefficient matrix `a in M_q`, define

\[
 P_{J,D}(a)=\sum_{v,w}a_{v,w}W_v^{(D)*}W_w^{(D)}.
\tag{1}
\]

The Collins--Youn free-group estimate is

\[
 \|P_{J,\mathrm{free}}(a)\|
 \le K_{m,J}\|a\|_2,
 \qquad
 K_{m,J}=m^{J/2}\sqrt{(1+9/m)^J-1}.
\tag{2}
\]

The finite-dimensional entropy proof needs a single random tuple for which

\[
 \sup_{\substack{a=a^*,\ \operatorname{Tr}a=0\\ \|a\|_2=1}}
 \|P_{J,D}(a)\|
 \le F_JK_{m,J}
\tag{3}
\]

holds. Pointwise convergence for one fixed `a` is insufficient; (3) is a simultaneous event on a
real sphere of dimension `q^2-2`.

The factor `F_J` need not tend to one. Repeating the purity argument with (3) gives

\[
 S_{\min}(L_{J,D})
 \ge J\log m-
 \log\!\left[1+F_J^2\big((1+9/m)^J-1\big)\right].
\tag{4}
\]

The product Bell witness therefore gives

\[
 \Delta_{J,D}
 \ge Jc_m-4\log F_J,
 \qquad
 c_m=\frac{\log m}{m}-2\log(1+9/m)>0,
\tag{5}
\]

where we used `1+F_J^2(B-1)<=F_J^2B` for `F_J>=1`. Thus it would be enough to have, for example,

\[
 \log F_J\le \frac{c_mJ}{8},
\tag{6}
\]

which retains the linear certificate `Delta_(J,D)>=Jc_m/2`.

Equation (6) is the correct tolerance when auditing dimension rates. Requiring `F_J=1+o(1)` is
unnecessarily strong; allowing the full exponential tolerance in (6) still does not rescue
full-size extensivity.

## 2. What the Bordenave--Collins source states

Use the source's notation `d=m`, `k=J`, and `N=D`.

### 2.1 Theorem 9.2: fixed parameters, no growing-depth threshold

Theorem 9.2 states that for every **fixed** pair of integers `m>=2`, `J>=1`, the independent-leg
tuple converges strongly in probability to the regular representation of `F_m^J` as `D->infinity`.
For a fixed coefficient net this proves

\[
 \forall m,J,F>1:\quad
 \Pr[(3)]\longrightarrow1
 \quad(D\to\infty),
\tag{7}
\]

after choosing `F` above the free bound and interpolating the finite net. It does not exchange the
quantifiers to `J->infinity`, does not display a threshold `D_0(m,J,F)`, and does not control one
tuple at all coefficient levels.

### 2.2 Lemma 9.3: a quantitative linear-pencil expectation bound

For a coefficient matrix algebra `M_n`, even `p`, and a linear pencil in the `mJ` generators,
Lemma 9.3 gives

\[
 \mathbb E\|A_D\|
 \le \|A_{F_m^J}\|
 (2n)^{(J+1)/p}
 D^{J(J+1)/(2p)}
 p^{3J(J+1)/(2p)}
 (1+c/\sqrt D)^J,
\tag{8}
\]

subject to

\[
 m^{70}\le D,
 \qquad
 2\le p\le D^{\alpha_m},
 \qquad
 \alpha_m=\frac1{16m+80}.
\tag{9}
\]

This is not (3): it is an expectation bound for one linear pencil. In particular, expectation
alone cannot be union-bounded over a coefficient net by Markov's inequality at a near-mean
threshold. If `E X<=(1+delta/2)K`, Markov only gives

\[
 \Pr[X>(1+\delta)K]
 \le\frac{1+\delta/2}{1+\delta},
\tag{10}
\]

which stays close to one as `delta->0`.

### 2.3 The other local quantitative interfaces

The same paper contains two additional ingredients, but does not package their growing-`J`,
coefficient-uniform combination as a theorem.

- Theorem 8.3 is an effective polynomial linearization. A degree-`l` polynomial in `s` positive
  generators is reduced to a linear pencil with coefficient size at most

  \[
   n_{\mathrm{lin}}\le2^l(2s)^{2l},
  \tag{11}
  \]

  and a linear relative error `epsilon` is amplified by at most

  \[
   C_{\mathrm{lin}}=4l^2(2s)^{2l}.
  \tag{12}
  \]

- Lemma 7.4 proves a Gaussian concentration inequality for the Schatten/operator norm of one
  Haar linear pencil. Its proof is a Lipschitz argument on a product of unitary groups. Applying
  that argument to the tensor pencil requires recording the dependence on all `mJ` independent
  variables and on the coefficient normalization after the `a`-dependent linearization.

For (1), `l=2J` and one may take `s=mJ`, so the displayed worst-case bookkeeping is

\[
 n_{\mathrm{lin}}\le2^{2J}(2mJ)^{4J},
 \qquad
 C_{\mathrm{lin}}=16J^2(2mJ)^{4J}.
\tag{13}
\]

These estimates are effective, but they show that polynomialization is not a harmless constant
when depth grows.

## 3. Necessary dimension growth from the optimistic linear estimate

Ignore coefficient uniformization and polynomial linearization and optimistically set `n=1` in
(8). Every displayed factor is at least one. If its contribution is to satisfy the entropy
tolerance `ln F_J=O(J)`, then the `D` factor alone requires

\[
 \frac{J(J+1)}{2p}\ln D=O(J),
 \qquad\text{hence}\qquad
 p=\Omega(J\ln D).
\tag{14}
\]

Together with `p<=D^alpha_m`,

\[
 D^{\alpha_m}=\Omega(J\ln D).
\tag{15}
\]

In particular,

\[
 \ln D(J)=\Omega_m(\ln J).
\tag{16}
\]

This is only a necessary condition inside the published certificate; it is not a lower bound on
the matrix dimension of every possible realization of (3). It is already enough for the
full-size conclusion below.

## 4. Why an explicit upper threshold would still not prove full size

The original side channel acts on input/output dimension `D(J)^J`. Passing to its complement and
performing the Weyl transfer does not remove the input cost: the transferred primitive input has
dimension `m^(2J)D(J)^J`. In either presentation the full logarithmic size `M_J` obeys

\[
 M_J\ge J\log D(J).
\tag{17}
\]

The present certificate is at most of order `Jc_m` as a lower-bound mechanism. To infer a fixed
positive inequality `Delta_J>=C M_J` from this certificate, one would need `log D(J)=O(1)`.
But (16) forces `D(J)` to be unbounded, and yields at best

\[
 \frac{\text{certified gap}}{M_J}
 =O_m\!\left(\frac1{\log J}\right)\longrightarrow0.
\tag{18}
\]

This is exactly the distinction in Hayden--Penington equation (11): both primitive input and output
spaces must grow linearly in the external parameter in qubit terms, while the defect is linear in
that same parameter. Reparametrizing by `M_J` does not help here because the defect then becomes
`o(M_J)`.

The conclusion is one-sided and certificate-scoped. It does not upper-bound the true additivity
defect of the sampled channels.

## 5. Can Section 8 be used to write any asymptotic `D(J)` upper scale?

There is an effective **blueprint**, but not a complete local theorem with a numeric threshold.
This distinction matters.

Fix

\[
 \kappa=\frac{c_m}{8},
 \qquad F_J=2^{\kappa J}.
\]

To make Theorem 8.3 return a polynomial factor at most `F_J`, its linear-pencil error must be of
order

\[
 \varepsilon_J
 \lesssim\frac{F_J}{C_{\mathrm{lin}}}
 =\exp[-4J\ln J+O_m(J)].
\tag{19}
\]

Taking `p` near `D^alpha_m` in (8), the logarithm of its multiplicative factor has the schematic
upper bound

\[
 O_m\!\left(
 \frac{J^2\ln D+J\ln n_{\mathrm{lin}}+J^2\ln p}{D^{\alpha_m}}
 +\frac{J}{\sqrt D}
 \right).
\tag{20}
\]

Equations (13), (19), and (20) suggest that, after all normalization and tail steps are supplied,
one can force the pointwise polynomial error below (19) at a scale of the form

\[
 \ln D_{\mathrm{suff}}(J)
 \le C_m J\ln(J+1)
\tag{21}
\]

for a sufficiently large constant `C_m` depending on the fixed generator count and on the
unspecified numerical constants in the source. This is an asymptotic candidate upper scale, not a
printable finite threshold.

Three interfaces still have to be made explicit before (21) becomes a proved node:

1. a tensor-product version of the Lemma 7.4 tail, with its `m,J,n_lin` normalization written after
   the coefficient-dependent linearization;
2. a simultaneous finite-net argument that handles the algebraic kernel of
   `a -> P_(J,free)(a)` rather than dividing by an arbitrarily small free norm; and
3. explicit choices of every hidden numerical constant and the even integer `p`.

Even granting all three and granting (21), the resulting cost is
`J log D_suff=O_m(J^2 log J)`, whereas the gap remains `Theta(J)`. Thus this possible effective
upper bound would prove only a quantitatively explicit **subextensive** absolute-unbounded family.
It cannot close the full-size node.

## 6. Direct epsilon-net plus generic Haar concentration is worse

The coefficient-uniform event also exposes why a naive concentration argument is not a hidden
full-size shortcut.

For `||a||_2=1`, changing one generator `U_(i,j)` changes (1) with a crude operator-norm
Lipschitz constant at most `q sqrt(2/m)`. Combining the `mJ` independent coordinates gives

\[
 \operatorname{Lip}(a)\le q\sqrt{2J}.
\tag{22}
\]

The same unitary-group concentration mechanism used in Lemma 7.4 therefore has a fixed-`a` tail
no better, at this crude level, than

\[
 \Pr\{|f_a-\mathbb Ef_a|>t\}
 \le2\exp\!\left[-c\frac{Dt^2}{Jq^2}\right].
\tag{23}
\]

An interpolation net for the Hermitian traceless unit sphere has

\[
 \ln |\mathcal N|
 =O\!\left(q^2\ln\frac{Cq}{t}\right).
\tag{24}
\]

At the natural slack `t` comparable to `F_JK_(m,J)`, the union-bound condition from (23)--(24)
has the optimistic form

\[
 D
 \gtrsim
 \frac{Jq^4}{F_J^2K_{m,J}^2}
 \ln\frac{Cq}{F_JK_{m,J}}
 =\frac{Jm^{3J}}{F_J^2((1+9/m)^J-1)}
 \ln\frac{Cq}{F_JK_{m,J}}.
\tag{25}
\]

For the admissible `F_J` in (6), the right side is still exponential in `J`; hence this standard
net route forces `ln D=Omega_m(J)` and is even less compatible with full-size scaling. Equation
(25) is a failure statement about this generic Lipschitz/union-bound method, not a lower bound on
the probability of (3) under a sharper, structure-sensitive theorem.

No local matrix-concentration theorem was found that directly controls the supremum in (3) with a
tail strong enough to overturn this metric-entropy cost.

## 7. Fixed `D`, fixed partner, and hierarchical alternatives

### 7.1 Fixed iid `D` is not merely unproved

The project-local conjugate-collision argument proves that at every fixed finite `D`, an iid
conjugation-invariant sequence of Haar layers contains an asymptotically perfect matching of
approximate conjugates. The one-side entropy rate then falls below the Collins--Youn rate needed
for (5). Thus the target side certificate itself fails almost surely at large depth for that fixed-`D`
iid ensemble.

This is model-specific and does not upper-bound the true defect of every deterministic sequence.

### 7.2 Heterogeneous fixed-dimensional layers reduce to one regularized block

For any compact fixed-dimensional continuous family, the project-local heterogeneous selection
theorem shows that a positive asymptotic product-Bell certificate rate selects one fixed tuple with
a positive regularized channel/conjugate-channel defect. Hence adaptive or oriented selection at
bounded `D` does not avoid the fixed-partner problem; it repackages it.

### 7.3 Fixed-partner and hierarchy routes remain conditional

A single finite pair with positive regularized cross defect would bypass `D(J)` completely: keep
that block fixed and tensor it. All primitive logarithmic dimensions and the defect would then grow
linearly in the outer copy number. The exact currently registered sufficient atom is the physical
self-purity multiplicativity estimate for all copies of one selected block. It is OPEN.

The hierarchical fixed-partner proposal is weaker. Pointwise convergence after each finite history
allows the next auxiliary dimension to depend arbitrarily badly on that history. Without a theorem
of the form

\[
 \sum_{j\le J}(g_j-2\ell_j)
 \ge c\sum_{j\le J}\text{(full qubit cost of layer `j`)}-O(1),
\tag{26}
\]

it can at most support the already separated absolute-unbounded conclusion. No local primary
theorem supplies (26).

## 8. Status table

| Statement | Status after this audit |
|---|---|
| Fixed `m,J`, `D->infinity` strong convergence in probability | THEOREM (Bordenave--Collins 9.2) |
| Fixed `m,J` existence of a finite successful coefficient-uniform realization | PROVED in the separately reviewed absolute-unbounded chain |
| Lemma 9.3 linear-pencil expectation factor (8) | THEOREM |
| Generic linear-pencil concentration, fixed coefficient data | THEOREM interface (Bordenave--Collins Lemma 7.4) |
| One displayed numeric threshold for the global entropy event (3) | NOT PROVIDED |
| Effective uniform assembly with candidate `ln D_suff=O_m(J ln J)` | CONDITIONAL BOOKKEEPING LEMMA; not registered as proved |
| Naive direct coefficient net plus generic Lipschitz tail | FAILED FULL-SIZE ROUTE; (25) is exponentially costly |
| Published certificate with bounded or growing `m` proves full size | NO; existing rate gate remains |
| Fixed finite block with positive regularized cross defect | OPEN |
| Hayden--Penington full-size extensive violation | OPEN |

## 9. Strongest strict conclusion and next atom

The strongest strict conclusion is:

> Within the existing Collins--Youn/Bell lower-bound mechanism and the published
> Bordenave--Collins quantitative factor, any certified growing-depth product-Haar construction has
> vanishing defect divided by full primitive logarithmic size. The theorem still proves
> finite-dimensional absolute unboundedness because it may choose a new, uncontrolled finite `D`
> after each fixed depth.

The next locally meaningful quantitative atom is narrow and testable:

> For fixed `m>e^18`, prove or refute a completely explicit, high-probability version of (3), with
> every dependence on `J,D`, the coefficient-net radius, the effective-linearization dimension,
> and the algebraic kernel recorded.

That atom would quantify the already proved absolute-unbounded construction, but by Sections 3--5
it would not close full size unless it also discovered a new gap term proportional to `J log D`.
The next **full-size-relevant** atom remains instead one fixed finite pair with positive regularized
cross defect, for example the registered physical self-purity multiplicativity statement.

## Primary sources and scope

1. Charles Bordenave and Benoit Collins, *Norm of matrix-valued polynomials in random unitaries
   and permutations*, arXiv:2304.05714v2. Used: Theorem 1.1, Lemma 7.4, Theorem 8.3,
   Theorem 9.2, and Lemma 9.3. Local SHA-256:
   `59e14a3334b24f5683d8a0a8919d6cf266cb587f9dbae8d78e8213ca3fe2d8ac`.
2. Benoit Collins and Sang-Gyun Youn, *Additivity Violation of the Regularized Minimum Output
   Entropy*, arXiv:1907.07856v2. Used: Theorem 3.3 for (2) and the associated entropy mechanism.
   Local SHA-256:
   `70c97a9e4c17218e17f159e00f3bc554011fa6f87b8966be494c97af0d726714`.
3. Patrick Hayden and Geoff Penington, *Black hole microstates vs the additivity conjectures*,
   arXiv:2012.07861v1. Used: Section 2, especially equations (9)--(11), for the full-size target.
   Local SHA-256:
   `e461f61e89bed46791974a6b2334e3aefb09d7824849b0f615744c1108397b21`.

No statement in this note upgrades `HEXT.goal`, turns absolute-unboundedness into full-size
extensivity, or upper-bounds the true defect of the finite-dimensional channel family.
