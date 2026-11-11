# Independent review: product-Haar tensor-strong-convergence quantitative rate gate

Date: 2026-08-30

Reviewer: independent Codex review context `/root/q1_weyl_transfer_review`.

## Independence and scope

I did not author `HEXT.tensor-strong-convergence-rate-gate`,
`PRODUCT_HAAR_DEPTH_DIMENSION_QUANTITATIVE_AUDIT_20260830.md`, or the earlier rate-gate note. I
read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full and inspected the cited local
Bordenave--Collins PDF directly.

This review asks only what the published tensor-strong-convergence certificate can establish for
the present Collins--Youn/Bell lower-bound mechanism. It does not upper-bound the true channel
defect, rule out a sharper theorem, or review a different construction.

## Executive verdict

The exact claim at
`sha256:4dadeb060c65e6b31e4db969da267e732d758d5f609ae0914d2bcb3c4ec7f37d`
**PASSes mathematically**.

For bounded generator count, the `D^{J(J+1)/(2p)}` factor in Bordenave--Collins Lemma 9.3 and its
constraint `p<=D^{1/(16m+80)}` force `ln D(J)=Omega_m(ln J)` if the multiplicative norm loss is
small enough to preserve a linear-in-`J` entropy certificate. The primitive full logarithmic cost
is at least `J log D(J)`, whereas this proof mechanism supplies only `O_m(J)` certified defect, so
the certified ratio tends to zero. For unbounded `m`, the source condition `D>=m^70` together with
`c_m<=log_2(m)/m` bounds that ratio by `1/(70m)` before any convergence loss.

The audit also correctly labels `ln D_suff=O_m(J ln J)` only as a candidate upper-scale blueprint:
Bordenave--Collins Theorem 8.3 and Lemma 7.4 are ingredients, not a published theorem assembling
the tensor-leg tail, coefficient-dependent linearization, algebraic kernel, and uniform net.

However, the current completion dossier is **BLOCKED from `PROVED`** because this route-free node
uses external theorems but has no machine-visible `assumptions` block. The source paths in generic
`basis.evidence` do not satisfy `DAG_PROTOCOL.md` Sections 2 and 6. After the exact theorem
interfaces listed in Finding HEXT-RG-IR-07 are registered, the unchanged claim is eligible for a
short amendment review and proposer-side promotion. No mathematical repair to the claim is needed.

## Immutable inputs and exact claim hash

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| rate-gate node YAML | `f2accc92105b6106f0a9520327fee6648e0e8d9511b6a38d9280246cad3669b6` |
| new quantitative audit | `6d0fe12f2e9ae37a00215cecae5edeb426322dc91d1b7c15166745b2a9384549` |
| earlier rate-gate audit | `153c41a97bedf9b608f61233525106e4d8a526ac7d0e6c2a765cd0809b284d6d` |
| finite-unitary distortion obstruction | `af0f972e45d72f904d02767e7908d8250f3e2ea8360220cb46aa933fb8d277a1` |
| Bordenave--Collins PDF | `59e14a3334b24f5683d8a0a8919d6cf266cb587f9dbae8d78e8213ca3fe2d8ac` |

The repository-normalized exact claim digest independently recomputes to
`sha256:4dadeb060c65e6b31e4db969da267e732d758d5f609ae0914d2bcb3c4ec7f37d`.

## Finding HEXT-RG-IR-01 -- PASS: exact fixed-depth and linear-pencil source interfaces

Bordenave--Collins Theorem 9.2, PDF pp. 62--63, fixes the positive generator count `d>=2` and
tensor-leg count `k>=1` before sending `N -> infinity`. It proves strong convergence in probability
for the independent Haar tensor-leg tuple toward the regular representation of `F_d^k`. It states
no growing-`k` threshold `N_0(d,k)` and no coefficient-uniform growing-depth event.

Under the audit substitution

```text
source d=m, source k=J, source N=D,
```

Lemma 9.3, PDF pp. 63--65, assumes `m^70<=D` and an even integer
`2<=p<=D^(1/(16m+80))`. For one matrix-valued linear pencil with coefficient size `n`, its upper
expectation factor is exactly

```text
(2n)^((J+1)/p)
D^(J(J+1)/(2p))
p^(3J(J+1)/(2p))
(1+c/sqrt(D))^J.
```

This is an expectation estimate for one fixed linear pencil, not the simultaneous coefficient
sphere required by the entropy proof.

**Verdict:** PASS. The audit preserves all fixed-parameter, even-moment, and dimension conditions.

## Finding HEXT-RG-IR-02 -- PASS: bounded-`m` necessary dimension growth

The entropy proof can tolerate a norm factor `F_J` with `ln F_J=O_m(J)`; it does not need
`F_J=1+o(1)`. Even after optimistically setting `n=1` and discarding every other factor, the `D`
factor alone contributes

```text
[J(J+1)/(2p)] ln D.
```

For that contribution to be `O_m(J)`, necessarily

```text
p=Omega_m(J ln D).
```

Combining this with `p<=D^alpha_m`, `alpha_m=1/(16m+80)`, yields

```text
D^alpha_m=Omega_m(J ln D),
ln D(J)=Omega_m(ln J).
```

This is a necessary condition within the displayed published factor. It is not a universal lower
bound on dimensions of all successful channel realizations.

**Verdict:** PASS.

## Finding HEXT-RG-IR-03 -- PASS: full-cost ratio is subextensive for this certificate

At depth `J`, each primitive side acts on a space containing dimension `D(J)^J`, so any natural
full logarithmic input/output/environment cost `M_J` used by the project obeys

```text
M_J>=J log_2 D(J).
```

The Collins--Youn/Bell lower-bound mechanism contributes at most `O_m(J)` as a certified positive
quantity; linearization and uniformization only subtract from it. Finding HEXT-RG-IR-02 therefore
gives

```text
certified gap / M_J = O_m(1/log J) -> 0.
```

The statement is about what this lower-bound certificate proves. It does not say the true defect
of those finite channels is `O(J)` or `o(M_J)`.

**Verdict:** PASS.

## Finding HEXT-RG-IR-04 -- PASS: Theorem 8.3 and Lemma 7.4 are not a completed uniform theorem

Bordenave--Collins Corollary 8.2 and Theorem 8.3, PDF pp. 58--59, give effective degree
linearization. For polynomial degree `l` in `s` positive generators, the displayed bookkeeping used
by the audit is

```text
n_lin <= 2^l(2s)^(2l),
C_lin = 4l^2(2s)^(2l),
```

with the theorem's upper-bound hypothesis
`epsilon<=(2s)^(-l)l^(-2)`. For the entropy polynomial, taking `l=2J` and `s=mJ` gives the audit's
worst-case formulas.

Lemma 7.4, PDF pp. 52--53, is a concentration result for one Haar linear pencil in `d` independent
unitaries. With the source's normalized Schatten norm it states, for `t>0` and `2<=p<=infinity`,

```text
Pr{| ||A_N||_p-E||A_N||_p | >= t||A_F||}
 <=2 exp[-c N^(1+2/p)t^2/d].
```

It does not directly state the needed tail after tensor-leg embedding and coefficient-dependent
linearization, nor a simultaneous bound over the traceless coefficient sphere. The audit therefore
correctly leaves the tail normalization, algebraic-kernel handling, finite net, hidden constants,
and even-`p` selection unassembled.

**Verdict:** PASS. The proposed scale `ln D_suff=O_m(J ln J)` is explicitly conditional
bookkeeping, not a theorem or a premise of the strict obstruction claim.

## Finding HEXT-RG-IR-05 -- PASS: unbounded generator count does not rescue this certificate

For the audited free defect coefficient,

```text
0<c_m=log_2(m)/m-2log_2(1+9/m)<=log_2(m)/m.
```

Lemma 9.3 requires `D>=m^70`, so even before convergence, linearization, or transfer losses,

```text
Jc_m/[J log_2 D]
 <=[log_2(m)/m]/[70log_2(m)]
 =1/(70m).
```

Hence every subsequence with `m(J)->infinity` has vanishing certified ratio. If the integer
sequence `m(J)` is bounded, it has an infinite constant subsequence. A value with nonpositive
`c_m` supplies no positive certificate; a value with positive `c_m` falls under the fixed-`m`
argument and again has vanishing ratio. Thus no joint `m(J),D(J)` sequence yields a uniform
positive full-size constant through this published certificate.

**Verdict:** PASS. This does not rule out a different lower-bound mechanism for the same channels.

## Finding HEXT-RG-IR-06 -- PASS: strict scope boundary

The exact node claim is framed as a limitation of the published quantitative estimate “by itself.”
Its caveats explicitly say it obstructs the present proof certificate rather than the true channel
family or stronger estimates. The audit separately labels:

- fixed-depth strong convergence and absolute-unbounded existence as proved;
- the candidate effective upper scale as conditional and unassembled;
- the naive tail-plus-net method as a failed proof route, not a probability lower bound; and
- fixed-block positive regularized cross defect and full-size extensivity as open.

Therefore the result may be promoted only as `HEXT.tensor-strong-convergence-rate-gate`. It supplies
no channel impossibility theorem and no completing route for `HEXT.goal`.

**Verdict:** PASS.

## Finding HEXT-RG-IR-07 -- BLOCKER: external interfaces are not machine-visible

`HEXT.tensor-strong-convergence-rate-gate` is a route-free proof-method obstruction that depends on
external source statements but currently has no node-level `assumptions` block. Before `PROVED`, a
proposer must register at least:

1. **Fixed-depth strong convergence:** Theorem 9.2 with fixed `m>=2`, fixed `J>=1`, independent
   Haar tensor-leg tuple, convergence in probability as `D->infinity`, and no growing-depth
   threshold. Locator: Bordenave--Collins PDF pp. 62--63.
2. **Quantitative linear-pencil upper estimate:** Lemma 9.3 with coefficient size `n`,
   `m^70<=D`, even `2<=p<=D^(1/(16m+80))`, and the full four-factor expectation bound written in
   Finding HEXT-RG-IR-01. Locator: PDF pp. 63--65.
3. **Effective polynomial linearization interface:** Corollary 8.2 and Theorem 8.3, including
   degree/generator meanings, coefficient dimension bound, relative-error amplification, and
   epsilon restriction. Locator: PDF pp. 58--59. This interface supports only the candidate
   blueprint, not a completed uniform theorem.
4. **Single-pencil concentration interface:** Lemma 7.4 with its one-pencil Haar model,
   normalized Schatten/operator norm, `2<=p<=infinity`, and exact tail dependence. Locator: PDF
   pp. 52--53. It must be explicitly scoped as not yet assembled for the tensor coefficient event.

After those exact assumptions are added without changing the claim, a short amendment may authorize
promotion at
`sha256:4dadeb060c65e6b31e4db969da267e732d758d5f609ae0914d2bcb3c4ec7f37d`.

## Final disposition

- exact mathematical claim: **PASS**;
- current completion dossier: **BLOCK** pending exact node-level assumptions;
- authorized eventual promotion scope: this proof-method obstruction only;
- `HEXT.goal`: remain `OPEN`.

