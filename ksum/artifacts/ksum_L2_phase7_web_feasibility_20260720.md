# KSUM L2 phase-7 web feasibility memo — canonical basis and two-ray profiles

Date: 2026-07-20
Source: ChatGPT web app, High reasoning, conversation “Quantum Query Complexity Literature”
Chat: https://chatgpt.com/c/6a5d9dd6-4950-83ea-b17d-02f21d5c2e61
Controlling node at commission time: `KSUM.B4b.L2.ALT.canonbasis`

## Status and scope

This is proposer-tier strategy evidence only. It has not received an independent rule-7 review and
licenses no completion-tier status. The web commission was restricted to the already registered
canonical-basis route. It generated one formula-defined two-ray support class and named one
unexamined escape, multi-pair global-profile cancellation; both were registered immediately after
the result was read and before further mathematical work.

The load-bearing literature identifiers reported by the web pass are Mathas–Soriano
`arXiv:math/0604108`, Bun–Thaler `arXiv:1503.07261`, and Bun–Kothari–Thaler
`arXiv:1710.09079`. They remain verify-before-cite for manuscript use.

## Decision

1. The final `S_N x C(sigma)`-invariant signed measure already has a canonical orbit basis, so a
   Wedderburn multiplicity basis is not needed merely to represent the witness.
2. The natural center/Jucys–Murphy proposal does not canonically fix the missing multiplicity
   coordinates. It fails separation at `N=1`, where the alphabet permutation module has two
   independent invariant lines with the same trivial endpoint-irrep label. The actual joint
   commutants also lack the obvious cross-`N` inclusion `T -> T tensor I`.
3. A direct Bun–Thaler-style cancellation can be written on two profile rays sharing one bad NO
   orbit. It yields exact zero mass, constant correlation, and an explicit `Theta(log N)` band.
4. More strongly, the entire two-ray support class has restricted approximate degree
   `O_tau(sqrt(N))`, uniformly in `q`. It therefore cannot supply the required `q^eta`
   enhancement and misses the `N^(2/3)` target at `q=N`.
5. Do not optimize the natural center/JM chain or the two-ray coefficient law further. The next
   registered escape is multi-pair global-profile cancellation.

## Canonical orbit coordinates

For odd `q=2m+1`, let `h=t/2` be the unique fixed point of `sigma(a)=t-a`. For each nonfixed
complementary pair `P={a,sigma(a)}`, sort its occupancies as `{u_P,v_P}` with `u_P<=v_P`.
The complete full-group orbit coordinate is

```text
omega = (c ; m_{r,s}),  c=n_h,
m_{r,s}=#{P : {u_P,v_P}={r,s}},
sum m_{r,s}=m,
c + sum_{r<=s}(r+s)m_{r,s}=N.
```

An invariant measure is specified by total orbit masses `w_omega`; then

```text
sum_x mu(x)       = sum_omega w_omega,
||mu||_1          = sum_omega |w_omega|,
<mu,f_t>          = sum_omega f_t(omega) w_omega.
```

This orbit coordinate is distinct from the `S_(N-1) x C(sigma)` stabilizer Wedderburn labels used
by L33. The latter label operator blocks and retain multiplicity-space gauge.

## Earliest canonical-basis gates

- `CB-1` — first-level separation: distinguish the invariant lines `C e_h` and
  `C e_nf` inside `W^{C(sigma)}`. Centers and endpoint-irrep labels fail.
- `CB-2` — commutant compatibility: every splitter at level `N` lies in
  `End_{S_N x C(sigma)}(W^{tensor N})`, not only in the larger `C(sigma)` commutant.
- `CB-3` — simple joint spectrum: the commuting family has one-dimensional joint eigenspaces in
  every multiplicity block.
- `CB-4` — cross-`N` compatibility: an explicit restriction or conditional-expectation identity
  connects the chosen family at `N+1` and `N`. The naive `T -> T tensor I` does not preserve the
  actual joint commutant.

The natural center/JM proposal fails `CB-1`; the obvious joint-commutant tower fails `CB-4`.
Choosing artificial Wedderburn matrix units would already choose the missing basis and is circular.

## Two-ray construction

Let `M=floor(N/2)`. The common bad NO profile `B` is a constant string on a nonfixed symbol.
For `0<=j<=M`:

- `Y_j` uses one complementary pair with occupancies `{j,N-j}`; `Y_0=B`, while `Y_j` is YES for
  `j>=1`.
- `Z_j` uses symbols from two different complementary pairs with occupancies `j` and `N-j`, with
  neither partner present; `Z_0=B`, while every `Z_j` is NO.

Choose nodes `0=s_0<s_1<...<s_L<=M` and barycentric coefficients

```text
b_i = 1 / product_{ell != i}(s_i-s_ell).
```

They annihilate every univariate polynomial of degree below `L`. Put

```text
alpha_i = -kappa b_i/b_0  on Y_{s_i},
beta_i  = +kappa b_i/b_0  on Z_{s_i}.
```

The masses at `B` cancel exactly. Both components separately have total mass zero. After the
pointwise cancellation, unit `l1` normalization gives correlation

```text
<psi,f_t> = 1/R_S,
R_S = sum_{i=1}^L |b_i/b_0|.
```

On either ray, every symmetrized factorial moment of order `k` is a polynomial in `j` of degree at
most `k`, so the witness has pure high degree at least `L`. Geometric nodes
`s_0=0`, `s_i=r^(i-1)` give constant `R_S` and hence constant correlation, but only
`L=Theta(log N)`.

## Scoped obstruction candidate

Let `W_2ray(N,q,t)` be the invariant signed measures supported on
`B union {Y_j,Z_j : 1<=j<=floor(N/2)}` with arbitrary signed coefficients.

For every fixed correlation threshold `tau>0`, the proposer claims that there is `C_tau` such that
every `mu in W_2ray(N,q,t)` with

```text
||mu||_1=1,  <mu,1>=0,  <mu,f_t>>=tau
```

has `phdeg(mu) <= C_tau sqrt(N)`, uniformly for odd `5<=q<=N`.

Reason: the degree-two target-pair count `C_t(x)` is zero on `B` and every `Z_j`, and equals
`j(N-j)` on `Y_j`. A Chebyshev polynomial of degree `O(sqrt(N))` separates `0` from
`[N-1,floor(N^2/4)]`, yielding a degree-`O(sqrt(N))` approximant to `f_t` on the entire support.
This is an unreviewed obstruction theorem candidate, not a completion result.

Hard boundary: the claim covers only support on `B,Y_j,Z_j`. It does not cover measures with
nonnegligible mass on profiles containing several simultaneously occupied complementary pairs,
fixed-point defects, or other global joint histograms.

## Cap sweep

- `q=5`: the two-ray class is not excluded from `Theta(sqrt(N))`, but the explicit geometric
  formula reaches only `Theta(log N)`.
- `q=N`: the canonical target is `Theta(N^(2/3))`, while the whole two-ray class is capped at
  `O(sqrt(N))`, a factor `N^(1/6)` too small.
- Intermediate growing `q`: the support-class ceiling is independent of `q`, so it cannot supply
  the required `q^eta` enhancement.

## Next action

Register and formulate `KSUM.B4b.L2.ALT.multipair` before any construction, computation, or review.
The first commission must define a genuinely global multi-pair support family and pass the same
mass, norm, correlation, factorial-moment, and endpoint-cap gates. No such formula is supplied here.
