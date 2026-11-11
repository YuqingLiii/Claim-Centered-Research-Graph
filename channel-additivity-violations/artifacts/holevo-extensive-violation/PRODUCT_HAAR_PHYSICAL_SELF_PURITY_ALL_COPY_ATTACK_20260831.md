# Product-Haar physical self-purity: all-copy attack and the first irreducible correlation terms

Date: 2026-08-31

Status: proposer-side derivation and route audit. The all-copy claim remains OPEN.

All entropy logarithms are base two.

## Executive conclusion

The all-copy physical-purity node has not been proved or refuted for a generic selected complex
product-Haar block. This attack produces four strict advances.

1. It freezes the quantifiers and gives an exact subset expansion for every outer copy number `r`.
   The node is equivalent to one hierarchy of centered physical-correlation inequalities, not to
   unrestricted complete boundedness.
2. At `r=3`, a genuinely new three-body centered term appears. Directly summing the global `r=2`
   inequalities for the three pair marginals produces no bound on that term. Therefore the naive
   induction that uses only those one- and two-copy marginal inequalities does not close.
3. The same-tuple Haar moment expansion at `r=2` and `r=3` contains connected Weingarten wirings
   absent from the independently sampled tensor-leg theorem. Kadison, scalar Haagerup, a generic
   `2->2` spectral estimate, and frame-potential tests do not control all these physical terms with
   the required constant.
4. There is a genuine complex, not necessarily simultaneously real, physical failure subclass:
   any Kraus tuple closed under entrywise conjugation up to a permutation and phases violates the
   `r=2` target whenever `A^2<2-1/q`. This does not refute the existential generic-complex node,
   because conjugation closure is a measure-zero dependency under independent complex Haar.

The narrowest missing lemma is now:

> control every connected centered physical correlation
> `E^(tensor |S|)(rho_S)` uniformly in `|S|` for one fixed selected tuple, with the exact binomial
> budget below, or exhibit one finite `r` and one physical pure state that exceeds that budget.

## 1. Frozen claim and quantifiers

Fix integers

\[
 m\ge2,\qquad J\ge1,\qquad D\ge1,
\]

and one **deterministic selected realization**

\[
 U_{i,j}\in U(D),
 \qquad i\in[m],\quad j\in[J],
\tag{1}
\]

from the independent complex-Haar product ensemble. Randomness is used only to find the tuple. Once
the tuple is selected, no probability quantifier remains in the all-copy assertion.

Put

\[
 \mathcal H=(\mathbb C^D)^{\otimes J},\qquad
 d=\dim\mathcal H=D^J,\qquad q=m^J,
\]

and, for `v=(v_1,...,v_J) in [m]^J`,

\[
 W_v=\bigotimes_{j=1}^J U_{v_j,j}.
\tag{2}
\]

The random-unitary channel and its chosen complement are

\[
 L_J(X)=\frac1q\sum_{v=1}^qW_vXW_v^*,
 \qquad
 C_J(X)_{v,w}=\frac1q\operatorname{Tr}(XW_w^*W_v).
\tag{3}
\]

Fix `eta>0` and set

\[
 A=A_{J,\eta}
 =1+(1+\eta)^2\big((1+9/m)^J-1\big),
 \qquad p=\frac Aq.
\tag{4}
\]

The load-bearing assertion is

\[
 \boxed{
 \forall r\ge1\ \forall\rho\in\mathcal D(\mathcal H^{\otimes r}):
 \quad
 \operatorname{Tr}[C_J^{\otimes r}(\rho)^2]\le p^r.}
\tag{5}
\]

The existential parent additionally requires

\[
 \ln m>18,
 \qquad
 \frac{J\log m}{m}>2\log A.
\tag{6}
\]

The order of quantifiers is therefore

\[
 \exists(m,J,D,\eta,U)\ \forall r\ \forall\rho.
\tag{7}
\]

It is not `forall r, choose a new D(r)` and not an assertion in probability after the block has
been fixed.

## 2. Exact all-copy centered subset expansion

Write

\[
 D_0(X)=\operatorname{Tr}(X)\frac{I_q}{q},
 \qquad E=C_J-D_0.
\tag{8}
\]

Every `E(X)` has zero diagonal and hence zero trace. For a subset `S subseteq [r]`, let `rho_S`
be the corresponding input marginal and let `E^(tensor S)(rho_S)` occupy the output tensor factors
in `S`. Expanding `(D_0+E)^(tensor r)` gives

\[
 C_J^{\otimes r}(\rho)
 =\sum_{S\subseteq[r]}
 \left(\frac{I_q}{q}\right)^{\otimes S^c}
 \otimes E^{\otimes |S|}(\rho_S),
\tag{9}
\]

with the tensor factors restored to their original order.

The summands for distinct subsets are Hilbert--Schmidt orthogonal: choose a factor in the
symmetric difference of the two subsets and use `Tr E(X)=0`. Consequently

\[
 \boxed{
 \operatorname{Tr}[C_J^{\otimes r}(\rho)^2]
 =\sum_{S\subseteq[r]}
 q^{-(r-|S|)}
 \|E^{\otimes |S|}(\rho_S)\|_2^2.}
\tag{10}
\]

The empty-set term is `q^(-r)`. Multiplying by `q^r`, (5) is exactly equivalent to

\[
 \boxed{
 \sum_{S\subseteq[r]}q^{|S|}
 \|E^{\otimes |S|}(\rho_S)\|_2^2\le A^r.}
\tag{11}
\]

This formula retains every physical marginal-consistency constraint. Replacing the physical
family by an arbitrary coefficient ball or arbitrary replica vector is a strict relaxation.

If `a=A-1`, the stronger termwise estimates

\[
 q^k\|E^{\otimes k}(\sigma)\|_2^2\le a^k
 \quad(k\ge1)
\tag{12}
\]

would prove (11) by the binomial theorem. They are sufficient, not necessary: physical marginal
slack can be transferred to higher-body correlations.

## 3. The exact `r=2` and `r=3` budgets

For `r=2`, (10) is

\[
 \operatorname{Tr}[C_J^{\otimes2}(\rho)^2]
 =\frac1{q^2}
 +\frac1q\sum_{i=1}^2\|E(\rho_i)\|_2^2
 +\|(E\otimes E)(\rho)\|_2^2.
\tag{13}
\]

Thus the exact two-body budget is

\[
 q^2\|(E\otimes E)(\rho)\|_2^2
 \le A^2-1-q\sum_i\|E(\rho_i)\|_2^2.
\tag{14}
\]

For `r=3`, one obtains the new identity

\[
\begin{aligned}
 \operatorname{Tr}[C_J^{\otimes3}(\rho)^2]
 ={}&\frac1{q^3}
 +\frac1{q^2}\sum_i\|E(\rho_i)\|_2^2\\
 &+\frac1q\sum_{i<j}\|(E\otimes E)(\rho_{ij})\|_2^2
 +\|E^{\otimes3}(\rho)\|_2^2.
\end{aligned}
\tag{15}
\]

The exact three-body budget is

\[
 q^3\|E^{\otimes3}(\rho)\|_2^2
 \le A^3-1
 -q\sum_i\|E(\rho_i)\|_2^2
 -q^2\sum_{i<j}\|(E\otimes E)(\rho_{ij})\|_2^2.
\tag{16}
\]

Suppose, optimistically, that the global `r=2` target has already been proved for every pair
marginal. Summing its three inequalities gives

\[
 3+2q\sum_i\|E(\rho_i)\|_2^2
 +q^2\sum_{i<j}\|(E\otimes E)(\rho_{ij})\|_2^2
 \le3A^2.
\tag{17}
\]

Equation (17) contains no upper bound on the last term in (15). Therefore direct summation of the
`r<=2` marginal inequalities does not induct to `r=3`; an additional structural estimate could in
principle do so. The fully centered three-body correlation is the first new term in this subset
expansion. At general `r`, one new `r`-body term appears at every level.

## 4. Exact Gram and replica-operator structures

For a multi-index `alpha=(alpha_1,...,alpha_r) in [q]^r`, put

\[
 K_\alpha=\bigotimes_{t=1}^r W_{\alpha_t}.
\]

For an input state `rho`, define the physical Gram matrix

\[
 G_\rho[\alpha,\beta]
 =\operatorname{Tr}(\rho K_\beta^*K_\alpha).
\tag{18}
\]

Then

\[
 C_J^{\otimes r}(\rho)=q^{-r}G_\rho,
 \qquad
 \operatorname{Tr}[C_J^{\otimes r}(\rho)^2]
 =q^{-2r}\|G_\rho\|_2^2.
\tag{19}
\]

Hence (5) is also equivalent to

\[
 \|G_\rho\|_2^2\le A^r q^r
 \quad\text{for every physical Gram matrix.}
\tag{20}
\]

For a pure input, the same objective is the expectation of the two-replica operator

\[
 Q_{J,r}=q^{-2r}\sum_{\alpha,\beta}
 K_\beta^*K_\alpha\otimes
 \overline{K_\beta^*K_\alpha}
\tag{21}
\]

on the restricted vectors `psi tensor bar(psi)`. Because the `J` hierarchy legs are sampled
independently, regrouping tensor factors gives the exact factorization

\[
 Q_{J,r}\simeq\bigotimes_{j=1}^JQ_{1,r}(U_{1,j},...,U_{m,j}).
\tag{22}
\]

This does not license the unrestricted operator-norm bound
`||Q_(J,r)||<=p^r`: the operator norm optimizes over arbitrary two-replica vectors, whereas the
physical problem uses only `psi tensor bar(psi)`. The known replica-operator relaxation loses the
needed constant already at low copy number.

## 5. Same-tuple Weingarten structure at `r=2` and `r=3`

At one hierarchy leg, for `alpha,beta in [m]^r`, define

\[
 X_{\alpha,\beta}
 =\bigotimes_{t=1}^r U_{\beta_t}^*U_{\alpha_t}.
\tag{23}
\]

Every matrix element of the Haar expectation of (21) is a sum of monomials

\[
 \mathbb E\big[X_{\alpha,\beta}\otimes
 \overline{X_{\alpha,\beta}}\big].
\tag{24}
\]

For a fixed generator label `i`, let

\[
 k_i=|\{t:\alpha_t=i\}|+|\{t:\beta_t=i\}|.
\tag{25}
\]

After the immediate cancellations at positions where `alpha_t=beta_t`, the remaining integral for
label `i` is an ordinary balanced unitary moment of degree at most `k_i<=2r`. In index notation its
exact expansion is

\[
 \sum_{\sigma_i,\tau_i\in S_{k_i}}
 \operatorname{Wg}_D(\sigma_i^{-1}\tau_i)
 \prod_s\delta_{a_s,a'_{\sigma_i(s)}}
 \prod_s\delta_{b_s,b'_{\tau_i(s)}}.
\tag{26}
\]

Independence over generator labels makes the full term the product of (26) over `i`.

- At `r=2`, the unreduced degrees satisfy `k_i<=4`; nonidentity permutations can connect the two
  outer copies and the two replicas. These are precisely the same-tuple exchange terms that do not
  occur when the tuple on the second tensor leg is sampled independently.
- At `r=3`, one has `k_i<=6`; besides pair exchanges, permutation wirings can connect all three
  outer copies. Their physical contraction is the last term of (15). It is not determined by the
  `r=2` moment or by its marginals.

For example, at degree two the source coefficients are

\[
 \operatorname{Wg}_D(e)=\frac1{D^2-1},
 \qquad
 \operatorname{Wg}_D((12))=-\frac1{D(D^2-1)}.
\tag{27}
\]

At degrees four and six the additional conjugacy classes generate connected corrections of higher
order in `1/D`, but a bound for a fixed input does not control the supremum over a
`D^(Jr)`-dimensional physical input space. Discarding these terms merely because each coefficient is
small is therefore an invalid uniform argument.

Bordenave--Collins Theorem 9.2 uses independent Haar tuples on distinct tensor legs. It does not
identify (24) for a tuple reused on every outer copy, and Collins--Youn controls the corresponding
free/commuting model rather than these finite same-tuple connected wirings.

## 6. Why the standard analytic routes do not close (11)

### 6.1 Scalar `1->2` control does not tensorize on entangled states

The one-copy event gives

\[
 \|E(X)\|_2\le\kappa\|X\|_1,
 \qquad \kappa^2=\frac{A-1}{q}.
\tag{28}
\]

For a Schmidt decomposition this gives the projective-norm estimate

\[
 \|(E\otimes E)(\rho)\|_2
 \le\kappa^2\|\rho\|_{S_1\widehat\otimes_\pi S_1}.
\tag{29}
\]

The projective factor equals `(sum_s sqrt(lambda_s))^2` for a pure state's Schmidt probabilities
and can grow like the Schmidt rank. Thus (29) loses exactly on the entangled inputs that must be
controlled. Repeating it at `r=3` introduces the corresponding tensor nuclear sum and is worse.

### 6.2 A Hilbert--Schmidt spectral gap is false at the target scale

The tempting sufficient estimate

\[
 \|E\|_{2\to2}^2\le\frac{A-1}{q}
\tag{30}
\]

would tensorize. It is generally false for these complements. For any two distinct word labels
`v!=w`, take

\[
 X=\frac{(W_w^*W_v)^*}{\sqrt d},
 \qquad \|X\|_2=1.
\]

One off-diagonal entry of `E(X)` has modulus `sqrt(d)/q`, so

\[
 \boxed{\ \|E\|_{2\to2}^2\ge\frac d{q^2}.\ }
\tag{31}
\]

Therefore (30) would require `d<=(A-1)q`. The strong-convergence construction normally takes `d`
far larger. The witness `X` is not a density matrix, so (31) is a method obstruction and not a
physical counterexample to (5).

### 6.3 Kadison plus Haagerup keeps the nuclear-sum loss

Kadison's inequality can control square functions after one decomposes a coefficient into simple
operator-Schmidt terms. Scalar or operator Haagerup estimates control each term, but summing them
retains the projective/nuclear norm seen in (29). The repository already has explicit maximal
operator-Schmidt-rank coefficients for which that ratio is order `sqrt(r)` or order one after the
normalization needed here. No cancellation theorem valid on all physical Gram matrices is supplied
by Kadison.

### 6.4 A Bell frame potential is only one input

At `r=2`, the Bell input gives the exact finite frame potential

\[
 \frac1{q^4}\sum_{v,a,w,b}
 \left|\frac1d\operatorname{Tr}
 [(W_vW_a^T)^*(W_wW_b^T)]\right|^2.
\tag{32}
\]

The project proves that a generic complex-Haar tuple passes this test with high probability at
fixed `m,J` and large `D`. That is necessary evidence but not a supremum theorem. At `r=3`, no
single canonical maximally entangled input detects the fully centered term in (15) for all states.

### 6.5 Matrix concentration and finite nets do not give all copy numbers

For every fixed `r`, output duality reduces the coefficient space to dimension `q^(2r)`, which is
finite independently of `D`. A same-tuple fixed-coefficient theorem plus a finite net could in
principle prove that one `r`. But the net dimension grows exponentially with `r`, the tuple is held
fixed, and pointwise convergence permits a new auxiliary dimension threshold for each `r`.
Intersecting all fixed-`r` asymptotic events after fixing `D` is the same invalid quantifier swap as
before.

## 7. A genuine complex physical obstruction subclass at `r=2`

The earlier real/orthogonal obstruction has a wider exact form. Suppose the word tuple is closed
under conjugation up to phases: there are a permutation `pi` of `[q]` and phases `z_v` such that

\[
 W_{\pi(v)}=z_v\overline{W_v}
 \qquad(v\in[q]).
\tag{33}
\]

The tuple need not be simultaneously real. On the normalized Bell state,

\[
 (W_v\otimes W_{\pi(v)})\Omega=z_v\Omega.
\tag{34}
\]

Thus `q` of the `q^2` equally weighted Kraus pairs produce the same output ray. Writing the
remaining positive output as `R`, its trace is `1-1/q` and its rank is at most `q^2-q`. Therefore

\[
 \operatorname{Tr}[L_J^{\otimes2}(\Omega)^2]
 \ge\frac1{q^2}+\frac{(1-1/q)^2}{q^2-q}
 =\frac2{q^2}-\frac1{q^3}.
\tag{35}
\]

Complementarity transfers (35) to `C_J tensor C_J` on a suitable pure input. Hence the physical
target fails whenever

\[
 A^2<2-\frac1q.
\tag{36}
\]

For example, choose a genuinely complex set `V_1,...,V_(q/2)` and take the tuple consisting of
the `V_i` and their entrywise conjugates. This is conjugation-closed but generically has no common
real orientation.

This is a route boundary, not a refutation of the existential node. Exact conjugation closure has
probability zero under the independent complex-Haar product ensemble, and (35) says nothing about
tuples outside its neighborhood. It does show that avoiding simultaneous reality is not enough;
the selected tuple must also avoid approximate conjugation closure at the target margin.

## 8. What would constitute a proof or a refutation

### Proof atom

It would suffice to establish, for one selected tuple, the exact physical hierarchy

\[
 \sum_{S\subseteq[r]}q^{|S|}
 \|E^{\otimes |S|}(\rho_S)\|_2^2\le A^r
 \quad\text{for all }r,\rho.
\tag{37}
\]

A viable inductive theorem must control the new connected `r`-body term conditional on all lower
marginals; a theorem that only repeats the `r=2` inequality cannot work.

### Refutation atom

One finite tuple satisfying the one-copy event and (6), together with one finite `r` and pure
physical input for which the left side of (37) exceeds `A^r`, refutes that tuple. To refute the
existential node itself one must rule out **every** eligible selected tuple, not merely a positive-
measure or symmetric subclass.

The smallest presently explicit physical counterterm is (35) on the conjugation-closed subclass.
For generic complex tuples the first unresolved case remains `r=2`; if it passes, (16) is the first
new `r=3` obstruction.

## 9. Status boundary and next action

| Item | Status |
|---|---|
| Exact all-copy subset expansion (10)--(11) | proposer-side proved algebraically |
| Exact `r=3` irreducible correlation budget (15)--(16) | proposer-side proved algebraically |
| `r=2` for separable inputs | proved in prior artifact |
| `r=2` for generic complex-Haar entangled inputs | OPEN |
| conjugation-closed complex tuples | physical failure at `r=2` under (36) |
| scalar `1->2`, unrestricted `2->2`, Kadison/Haagerup | insufficient proof routes |
| all `r` for one fixed generic complex tuple | OPEN |
| `HEXT.goal` | OPEN |

The most economical next computation is not a new all-input net. It is to select a small explicit
complex tuple that passes the one-copy coefficient certificate and then optimize the exact
`r=2` physical Gram objective, with a certified upper/lower method. A violation would be final for
that tuple; a global pass would create an `r=2` lemma and expose (16) as the next atom.

## Primary/local interfaces

1. Benoit Collins and Sang-Gyun Youn, *Additivity Violation of the Regularized Minimum Output
   Entropy*, arXiv:1907.07856v2, Theorems 3.3--3.5. Used for the free-model coefficient and purity
   bounds. Local SHA-256:
   `70c97a9e4c17218e17f159e00f3bc554011fa6f87b8966be494c97af0d726714`.
2. Charles Bordenave and Benoit Collins, *Norm of matrix-valued polynomials in random unitaries
   and permutations*, arXiv:2304.05714v2, Theorem 9.2 and the unitary Weingarten framework used in
   its proof. Local SHA-256:
   `59e14a3334b24f5683d8a0a8919d6cf266cb587f9dbae8d78e8213ca3fe2d8ac`.
3. `PRODUCT_HAAR_PHYSICAL_SELF_PURITY_N2_ANALYSIS_20260830.md` for the exact two-copy physical
   reduction and the simultaneously-real obstruction.
4. `COMPLEX_HAAR_N2_BELL_FRAME_POTENTIAL_ANALYSIS_20260830.md` for the generic complex Bell test.
5. `SAME_TUPLE_HIGH_SCHMIDT_SPECTRAL_FLAT_EXTENSION_20260830.md` for the exact scope of the
   Kadison/Haagerup and projective-norm obstruction.

Nothing here promotes the all-copy node, propagates to `HEXT.goal`, or converts the
absolute-unbounded theorem into a full-size result.
