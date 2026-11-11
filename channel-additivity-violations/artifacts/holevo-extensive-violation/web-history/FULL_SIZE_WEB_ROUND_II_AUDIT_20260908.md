# Full-size extensive Holevo/MOE web round II — public-result audit

Date: 2026-09-08

Conversation: <<private-chat-link-removed>>

Model shown in the browser: GPT-6 Astra Ultra.

Source artifact shown in the browser: `full_size_additivity_dossier_II.md`, dated 2026-09-08.

## Status boundary

The unrestricted target remains **OPEN**:

\[
\exists (N_r,M_r),\ c>0:\quad
\Delta_S(N_r,M_r)\ge c\,s(N_r,M_r),
\qquad s(N_r,M_r)\to\infty,
\]

and likewise after the finite MOE-to-Holevo and pair-to-self reductions.  The web report did not
produce a fixed finite channel pair with positive regularized cross defect

\[
\Gamma(N,M)=h(N)+h(M)-h(N\otimes M)>0,
\qquad
h(X)=\inf_{r\ge1}\frac{S_{\min}(X^{\otimes r})}{r}.
\]

Nothing in this record promotes `HEXT.goal` or any other canonical node.  Every statement below is
either an elementary identity checked in this audit or a proposer-side theorem requiring an
independent proof/source review under the repository protocol.

## Public result digest

### 1. Product-Haar architecture: stronger claimed obstruction

For a fixed number `m` of Haar unitaries per layer, the report claims a uniform entropy-rate theorem
for heterogeneous channel lists.  Its ingredients are:

1. Winter's conditional-entropy continuity modulus
   \[
   \omega_b(t)=2t\log_2 b+(1+t)h_2\!\left(\frac{t}{1+t}\right),
   \]
   yielding
   \[
   |H(X\otimes Z)-H(Y\otimes Z)|
   \le \omega_b\!\left(\tfrac12\|X-Y\|_\diamond\right)
   \]
   uniformly in the spectator channel `Z` and without restricting globally entangled inputs.
2. A finite-alphabet subadditive homogenization theorem with a uniform, generally non-effective,
   remainder `E_K(r)->0`.
3. A compact empirical-measure extension `f_K` that is continuous in Wasserstein distance and
   uniformly approximates the globally optimized minimum output entropy of every heterogeneous
   length-`r` list.
4. An eventual row tail
   \[
   \Pr\{\Delta_S(L_r,\overline L_r)\ge tr\}
   \le \exp\!\left[-\frac{t^2r}{128(\log_2 b)^2}\right].
   \]

From these ingredients the report claims one probability-one event on a countable product space
that controls **all** dimensions and any prescribed subexponential retry budget `M_J`:

\[
\lim_{J\to\infty}\sup_{D\ge1}\max_{k\le M_J}
\frac{\Delta_S(L_{J,D,k},\overline L_{J,D,k})}{s_{J,D,k}}=0.
\]

For large `D` this follows deterministically from

\[
0\le\Delta_S\le2J\log_2m,
\qquad s\ge4J\log_2D.
\]

For the finitely many remaining dimensions the report combines the row tail with a union bound and
Borel--Cantelli.  This is an obstruction only to the fixed-`m`, iid-within-row Haar architecture,
including subexponential retry-and-selection.  It does not cover growing `m`, exponentially many
retries, rare-event conditioning outside the declared sampling experiment, or a deliberately chosen
fixed reusable block.

### 2. Readable finite clocks and flags: claimed no-activation theorem

If a branch label is readable on the output or environment, the report derives the exact sector
minimum

\[
H(A\otimes Z)=\min_a H(X_a\otimes Z).
\]

For finitely many branches made from tensor words

\[
C_u=N^{\otimes p_u}\otimes M^{\otimes q_u}\otimes\tau_u,
\]

it claims the exact regularized variational formula

\[
h(A)=\min_{(x,y,c)\in K_A}[\mathcal H(x,y)+c]
\]

and the quantitative obstruction

\[
0\le\Gamma(A,B)\le K\,\Gamma(N,M).
\]

Thus readable finite tensor-word compilation cannot manufacture positive regularized defect from a
primitive pair with zero regularized defect.  A path-language extension is claimed with explicit
`o(r)` remainders.  Entropy penalties can suppress unwanted switching, but then they preserve the
primitive leakage and preserve `Gamma(N,M)` rather than improving it.

The report explicitly leaves coherent unreadable flags outside this theorem; branch channels alone
do not determine their cross maps.

### 3. Erasure and payload-retaining variants

For ordinary erasure it records the exact compatible-marginal formula

\[
H(E_p(X)^{\otimes r})=rh_2(p)+
\min_\psi\sum_{S\subseteq[r]}p^{|S|}(1-p)^{r-|S|}
S(X^{\otimes S}(\psi_S)).
\]

The minimization remains outside the subset sum.  Consequently independently optimizing each subset
would be invalid.  The ordinary dilution certificate cannot beat the original leakage certificate.

For the payload-retaining channel

\[
R_p(N)(\rho)=pN(\rho)\oplus(1-p)\rho,
\qquad R_p(N)^c=E_p(N^c),
\]

the singleton penalty no longer scales with the primitive input dimension.  This leads to the
weighted-subset gate in section 5 below.

The report also claims a separate one-shot theorem: at every fixed survival probability `p>0`,
finite channels with arbitrarily large two-copy self defects survive erasure dilution; for `p<=1/2`
they can be antidegradable, with degradable complements.  This statement is explicitly **not** a
full-size theorem.

### 4. Strong-additivity and transfer claims

The report correctly distinguishes strong additivity with every partner from merely having
`H(X^r)=rH(X)`.  It claims, by a swap-kernel derivation, exact heterogeneous additivity for any tensor
product of Werner--Holevo channels and/or their Stinespring complements:

\[
H\!\left(\bigotimes_j X_j\right)=\sum_j\log_2(d_j-1),
\qquad X_j\in\{W_{d_j},W_{d_j}^c\}.
\]

It also gives a direct derivation of the Weyl extension identities for arbitrary mixed words:

\[
H\!\left(\bigotimes_j\mathcal W(N_j)\right)
=H\!\left(\bigotimes_jN_j\right),
\]

\[
\chi\!\left(\bigotimes_j\mathcal W(N_j)\right)
=\sum_j\log_2b_j-H\!\left(\bigotimes_jN_j\right).
\]

Therefore the same fixed extensions preserve `h`, every mixed-word leakage term, and `Gamma`
exactly, with logarithmic size overhead bounded by a constant factor.

The report makes an important correction: for every fixed channel `T`,

\[
h(T^{\otimes k})=kh(T),\qquad C(T^{\otimes k})=kC(T),
\]

so `Gamma(T,T)=0` tautologically in the regularized sense.  Pair-to-self reduction can concern a
one-shot defect `chi(T^2)-2chi(T)` or `C(T)-chi(T)`; it cannot create a positive fixed-channel
regularized self defect.

### 5. Smallest surviving sufficient lemma

Fix the enormous constant

\[
m=\lceil e^{80}\rceil,
\qquad
B_m=\frac{\log_2m}{8m}-\frac1m>0,
\]

and a single finite random-unitary block

\[
Q(\rho)=\frac1m\sum_{i=1}^mU_i\rho U_i^*.
\]

For every `r` and input state `rho`, define

\[
\mathcal D_r(\rho)=2^{-r}\sum_{S\subseteq[r]}
D_{\rm rel}\!\left((Q^c)^{\otimes S}(\rho_S)
\middle\|\frac{I}{m^{|S|}}\right).
\]

The remaining gate is

\[
\tag{G}
\exists D<\infty,\ U_1,\ldots,U_m:\quad
\forall r\ge1\ \forall\rho:\quad \mathcal D_r(\rho)\le rB_m.
\]

The report checks only one-copy feasibility.  It does **not** give explicit unitaries or prove the
higher-copy inequalities.

Conditional on (G), with

\[
A=R_{1/2}(Q),\qquad B=\overline A,
\]

the dossier derives

\[
\Gamma(A,B)\ge\frac2m,
\qquad
\Delta_S(A^{\otimes r},B^{\otimes r})\ge\frac{2r}{m}
\quad\text{for all }r.
\]

Since `D` and `m` are fixed before `r` grows,

\[
\frac{\Delta_S(A^r,B^r)}{s(A^r,B^r)}
\ge\frac1{m\log_2(2D^2(m+1))}>0.
\]

Weyl extension and a balanced direct sum then conditionally give a family `T_r` with

\[
\Delta_\chi(T_r,T_r)\ge\frac{2r}{m}-1,
\qquad
C(T_r)-\chi(T_r)\ge\frac rm-\frac12,
\]

at full logarithmic size linear in `r`.

The proposed stronger induction certificate

\[
\mathcal D_{r+1}(\rho)-\mathcal D_r(\rho_{[r]})\le B_m
\]

has the diagnostic decomposition

\[
\frac12[\log_2m-S(\eta_{E_{r+1}})]
+\frac12\,2^{-r}\sum_{S\subseteq[r]}I(E_{r+1}:E_S)_\eta.
\]

The first term is controlled by the one-copy estimate; the averaged mutual-information term is the
new all-copy obstruction.  This is the sharpest explicit proof obligation produced by the round.

## Local algebra checks completed in this audit

The following checks use only the formulas displayed in the public dossier and do not certify the
deep analytic/source-dependent claims.

1. The large-`D` bound used in the all-dimension argument is dimensionally consistent:
   `Delta_S <= 2J log m` and the two channel inputs plus two outputs contribute at least
   `4J log D` to the declared size.
2. With `log_2 M_J=o(J)`, the displayed finite-dimension union bound is summable after halving the
   exponential rate, so the stated Borel--Cantelli step is formally sound once the row tail is
   accepted.
3. `Gamma(T,T)=0` follows exactly from `h(T tensor T)=2h(T)`; this is not a substantive positivity
   theorem.
4. Under (G), the two marginal lower bounds minus the displayed Bell-witness entropy equal
   `2r/m`; the constants in the conditional MOE defect close algebraically.
5. The displayed six-system size bound then gives the stated positive constant ratio because `D`
   and `m` are fixed independently of `r`.
6. The direct-sum Holevo calculation gives
   `log_2((1+2^{g_r})/2) >= g_r-1`, so the conditional pair-to-self and capacity lower bounds close
   algebraically.

## Independent-review obligations

Before any canonical promotion, a separate local reviewer must check at least:

1. the finite-alphabet homogenization theorem, especially uniqueness/convexity of the rate and the
   uniform remainder (P7);
2. the compact empirical-measure theorem (P12)--(P14) with unrestricted global input entanglement;
3. the exact constants and threshold in the concentration bound (P15), followed by the simultaneous
   quantifiers in (P20);
4. the regularized word-control formulas and both inequalities used to prove
   `Gamma(A,B)<=K Gamma(N,M)`;
5. the path-language `o(r)` estimate and its permitted cost/length dependence;
6. the erasure one-shot theorem, including complement/direct-sum witnesses and declared dimensions;
7. the Werner--Holevo/complement purity-kernel identity and purity attainment for every mixed
   orientation;
8. the exact hypotheses and cited locations of Winter, Shor, King, KMNR, Alicki--Fannes, Fukuda,
   and Fukuda--Wolf;
9. every equality in the compatible-marginal derivation of (G), including the global maximum over
   inputs and the mutual-information diagnostic.

## Repository decision

- Preserve all new statements as **proposer-side candidates**.
- Keep the full-size extensive target **OPEN**.
- Do not infer a fixed positive regularized defect from the unbounded one-shot construction.
- The next mathematical target is (G), or a counterexample to (G) for every candidate in the
  proposed class.  A finite-copy numerical pass can refute a fixed candidate but cannot prove (G).

