# Independent review: dephasing Weyl extension and exact MOE-to-Holevo transfer

Date: 2026-08-30

Reviewer: independent Codex review context `/root/q1_weyl_transfer_review`.

## Independence and scope

I did not author either canonical node or either proposer artifact reviewed here. I read
`DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full, reconstructed the channel maps and entropy
arguments independently, and inspected the cited local primary PDFs. I used no web source and made
no appeal to Q2, Q3, WHGAP, or an unreviewed result elsewhere in the repository.

This review covers exactly:

1. `HAEQ.weyl-extension-moe-preservation`;
2. the `explicit-weyl-extension` implication in `HAEQ.direct-moe-to-holevo-transfer`;
3. the claim of `HAEQ.direct-moe-to-holevo-transfer`;
4. the proposer derivations in
   `WEYL_EXTENSION_GLOBAL_MOE_PRESERVATION_20260830.md` and, only where needed to inspect the
   assembled route, `DIRECT_MOE_TO_HOLEVO_TRANSFER_20260830.md`;
5. Shor, Section 9, local PDF pages 18--19; and
6. Fukuda--Wolf, Propositions 1 and 2, local PDF pages 1--3, solely to determine whether any direct
   sum result is hidden inside the two reviewed claims.

It does not review the Hastings existence input, any pair-to-self reduction, fixed-channel
regularization, the Q1 root assembly, or any statement about classical capacity beyond the
one-shot Holevo quantity appearing in the reviewed claim.

## Executive verdict

**PASS.** The completely dephasing classical-label Weyl extension is a finite-dimensional CPTP
map with output dimension `d`. Its action on arbitrary inputs, including inputs coherent in the
label basis and inputs entangled across two extended channels, is exactly the convex-mixture formula
used by the proposer. Entropy concavity and fixed-label achievability prove both the one-channel and
product-channel global minimum-output-entropy identities. The universal Holevo upper bound and the
uniform Weyl orbits attain the corresponding one-channel and product identities. Subtraction has
the correct sign and preserves the numerical pair defect for every finite-dimensional channel pair.

The following exact objects are therefore eligible for `PROVED` once this review is linked:

- `HAEQ.weyl-extension-moe-preservation` at
  `sha256:d6001ff040d7a0282b64842132b530f2f4b181e5cfbde87ac9a82f9f5c034e53`;
- route `HAEQ.direct-moe-to-holevo-transfer.routes.explicit-weyl-extension` at
  `sha256:f68eee218351e32e87ea69e57de9806d6fe84791b4f253afb46759d805ac6f51`;
  and
- `HAEQ.direct-moe-to-holevo-transfer` at
  `sha256:0a165d2114f2c448697a4ec9d71063260da689a00571772202b8b84b48289e3d`.

The verdict is for the explicit **dephasing** extension. It does not apply to an arbitrary coherent
controlled-unitary extension that retains label coherences.

## Immutable inputs

The exact byte digests inspected were:

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| Weyl preservation artifact | `f8c277677b7711aa30446142c8970c93282ff08c4f59507c11e27d9fe74f069e` |
| assembled direct-transfer artifact | `9b14b2f0a5b695c79e6fba5ac6ad6715bd93bab7a19f375c450483fb335259e3` |
| preservation node YAML | `db655be7c12ec30c3a1287099c6f181aaba0ccc68c5bf4a088a70dde62193d98` |
| direct-transfer node YAML | `a34afd9f4daaa8ec43a70f71dcfef1d2be35218f2ae0b5ad0611719cde99a83f` |
| Shor local PDF | `300a97664fe8d05531230cd6f3a812b23e2c2cbf22c429436e50442993f415d6` |
| Fukuda--Wolf local PDF | `1a8890f8484d450894545190d306efd67b57ee7f646fc45be1e4a26fe6b653b7` |

The statement hashes below use the repository rule
`sha256(statement.replace("\\r\\n", "\\n").strip())`.

## Exact reviewed statements

### Preservation claim -- PASS

> Let N1 and N2 be finite-dimensional channels whose outputs are isometrically embedded in a
> common d-dimensional space, and let N1' and N2' be their completely dephasing classical
> Weyl-label extensions. Then Smin(Ni') = Smin(Ni) for i=1,2 and
> Smin(N1' tensor N2') = Smin(N1 tensor N2), where every minimum is over all input states,
> including label-input-correlated states and states entangled across the two extended channels.

Exact claim hash:
`sha256:d6001ff040d7a0282b64842132b530f2f4b181e5cfbde87ac9a82f9f5c034e53`.

### Direct-transfer route implication -- PASS

> The premise identifies the exact one-channel and product minimum output entropies of the
> dephasing Weyl extensions. The output-dimension Holevo upper bound and Shor's uniform Weyl
> ensembles attain log d minus those minima singly and 2 log d minus the product minimum;
> subtracting the identities preserves the original numerical MOE pair defect exactly.

Exact route-implication hash:
`sha256:f68eee218351e32e87ea69e57de9806d6fe84791b4f253afb46759d805ac6f51`.

### Direct-transfer claim -- PASS

> Every finite-dimensional p=1 minimum-output-entropy pair defect can be transferred by Shor's
> finite Weyl-labelled extension to an exactly equal numerical Holevo pair defect; the extension
> changes the channels but remains finite dimensional.

Exact claim hash:
`sha256:0a165d2114f2c448697a4ec9d71063260da689a00571772202b8b84b48289e3d`.

## Findings

### Finding Q1WR-01 -- PASS: the dephasing extension is CPTP with the stated dimensions

Write `N(X)=sum_alpha K_alpha X K_alpha^*`. For each Weyl label `z`, define

```text
L_(alpha,z) = W_z K_alpha (I_A tensor <z|).
```

Then the proposer map is

```text
N_tilde(omega) = sum_(alpha,z) L_(alpha,z) omega L_(alpha,z)^*,
```

so it is completely positive, and

```text
sum_(alpha,z) L_(alpha,z)^* L_(alpha,z)
  = I_A tensor sum_z |z><z|
  = I_(A tensor Z),
```

so it is trace preserving. The input dimension is `dim(A)d^2`; the output dimension remains `d`.
An isometric padding of an original output into the common `d`-dimensional space only adds zero
eigenvalues and therefore preserves all single and product output entropies used here.

Shor's Section 9 defines the action on an original input together with a *classical* integer label
and gives `N'(rho tensor |i><i|)=X_i N(rho)X_i^*`. The local formula is the canonical
measurement/dephasing CPTP completion of that classical-input definition. This finding does not
reinterpret Shor's construction as a coherence-preserving controlled channel.

### Finding Q1WR-02 -- PASS: arbitrary label coherences and cross-channel entanglement are covered

For a state `omega` on `A tensor Z`, each diagonal compression

```text
omega_z = (I_A tensor <z|) omega (I_A tensor |z>)
```

is positive and subnormalized, and the off-diagonal label blocks vanish by the Kraus formula above.
Thus the output is a convex mixture of the normalized states
`W_z N(omega_z/Tr(omega_z)) W_z^*`.

For an arbitrary state on `(A1 tensor Z1) tensor (A2 tensor Z2)`, including one entangled across
the two extended-channel inputs, the same calculation produces positive joint diagonal blocks
`omega_(z1,z2)` on `A1 tensor A2`. Their normalized versions need not be separable; applying
`N1 tensor N2` to them is exactly the global minimization regime required by the claim. Therefore
the product formula is a convex mixture of local-Weyl conjugates of original product-channel
outputs, with no separability assumption and no omitted coherent-label contribution.

### Finding Q1WR-03 -- PASS: the global minimum-output-entropy equalities are exact

Entropy concavity and unitary invariance give, for every extended-channel input,

```text
S(N_tilde_i(omega)) >= sum_z p_z S(N_i(rho_z)) >= Smin(N_i).
```

A finite-dimensional entropy minimum exists. A fixed label attached to an original minimizing
input attains the opposite inequality. Hence `Smin(N_tilde_i)=Smin(N_i)`.

The identical argument for joint diagonal blocks gives the product lower bound against the global
minimum of `N1 tensor N2`; a fixed label pair attached to a joint product-channel minimizer attains
it. Hence

```text
Smin(N_tilde_1 tensor N_tilde_2) = Smin(N1 tensor N2).
```

No MOE additivity hypothesis is used. If one insists that signal ensembles contain pure inputs,
concavity of output entropy lets the finite-dimensional minima be attained on pure states; this is
also the convention stated by Shor before Section 9.

### Finding Q1WR-04 -- PASS: the Holevo upper bounds are attained singly and jointly

For any channel with output dimension `D`, every signal output entropy is at least `Smin` and the
average output entropy is at most `log D`, so

```text
chi(Phi) <= log D - Smin(Phi).
```

The `d^2` discrete Weyl conjugations satisfy the exact twirl

```text
(1/d^2) sum_z W_z sigma W_z^* = I_d/d.
```

For completeness, this is not left as an imported slogan. With `W_(a,b)=T^a R^b`, averaging a
matrix unit `|j><k|` over `b` gives zero unless `j=k`; for `j=k`, the remaining average over `a`
is `I_d/d`. Linearity gives `Tr(sigma)I_d/d`, hence `I_d/d` for every density matrix. The same
calculation in each output tensor factor gives the local product twirl used below.

Using one original-channel minimizer with all labels uniformly therefore attains
`log d-Smin(N_i)`. Using one joint minimizer with all `d^4` label pairs uniformly applies the two
local twirls to the joint output, giving `I_d/d tensor I_d/d`, while every signal entropy equals
`Smin(N1 tensor N2)`. The product output dimension is `d^2`, so the attained value is
`2 log d-Smin(N1 tensor N2)`. Together with Findings Q1WR-02 and Q1WR-03 these are global identities,
not merely ensemble lower bounds.

### Finding Q1WR-05 -- PASS: the defect sign and quantifiers are correct

Subtracting the two one-channel identities from the product identity gives

```text
chi(N_tilde_1 tensor N_tilde_2) - chi(N_tilde_1) - chi(N_tilde_2)
 = Smin(N1) + Smin(N2) - Smin(N1 tensor N2).
```

Thus the Holevo superadditivity defect has exactly the same sign and numerical magnitude as the
`p=1` MOE subadditivity defect. The construction works for every pair of finite-dimensional
channels after common-output padding, with no random-channel or positive-gap assumption required.
When the right side is positive it transfers a violation; when it is zero it transfers zero.

### Finding Q1WR-06 -- PASS with source-scope clarification

Shor Section 9, PDF pages 18--19, supports the common output padding, the `d^2` generalized Pauli
labels, the labelled extension on classical inputs, the one-channel uniform orbit of a minimum
output input, and the product uniform orbit of a joint lower-entropy input. Shor uses these facts to
prove the relevant universal implication by contradiction. The paper does not separately state the
stronger arbitrary-input equality in Finding Q1WR-03; that equality is the local completion reviewed
here, not a theorem silently imported from Shor.

Fukuda--Wolf Proposition 1(4), PDF pages 1--2, gives the Holevo formula for a direct sum, and
Proposition 2(2), PDF page 3, gives the arbitrary-pair/equal-pair reduction. Neither theorem is a
load-bearing input to the two claims reviewed here. The reference to a later Fukuda--Wolf direct-sum
step in the assembled proposer note is downstream context only and is not used to license this
verdict.

### Finding Q1WR-07 -- PASS: protocol and scope boundaries

The preservation node is a direct proof with no unresolved load-bearing external theorem: the
finite Weyl operators and their twirl are defined and proved at the level needed in the proposer
derivation, while Shor supplies a locatable primary-source match for the construction. The transfer
route lists the preservation lemma as its only unresolved premise and records Shor's exact finite
construction/ensemble interface as an external theorem. The route implication proves the precise
parent claim and introduces no hidden premise.

Promotion must retain the existing caveat that the extension changes the channels. This review
does not prove that the original Hastings pair itself violates Holevo additivity, does not perform
the pair-to-self step, and does not establish the regularized classical capacity separation by
itself.

## Promotion recommendation

Subject to exact-hash linkage under the DAG protocol, promote in dependency order:

1. `HAEQ.weyl-extension-moe-preservation` to `PROVED`, binding Finding Q1WR-01 through
   Finding Q1WR-03 to claim hash `d600...`;
2. route `explicit-weyl-extension` to `PROVED`, binding Finding Q1WR-04 through Finding Q1WR-06 to
   implication hash `f68e...`; and
3. `HAEQ.direct-moe-to-holevo-transfer` to `PROVED`, binding Finding Q1WR-04 through Finding Q1WR-07
   to claim hash `0a16...`, once its premise and route are both `PROVED`.

No broader node is reviewed or eligible for promotion from this report.
