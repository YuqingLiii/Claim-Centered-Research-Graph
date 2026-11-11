# Explicit Clifford state and measurements

This note gives a completely explicit physical realization of any real unit-
vector Bell strategy. It is specialized in the claim graph to the extremizers
coming from the balance spectrahedron.

## CL-T1: Pauli data

Use the Hermitian Pauli matrices

```text
I = [1 0; 0 1],
X = [0 1; 1 0],
Y = [0 -i; i 0],
Z = [1 0; 0 -1].
```

They square to the identity, distinct nonidentity Paulis anticommute, and every
nonidentity Pauli has trace zero.

## CL-T2: explicit generators in vector dimension s

Let `q=floor(s/2)` and `D=2^q`. For `1 <= j <= q`, define

```text
Gamma_(2j-1) = Z^(tensor (j-1)) tensor X tensor I^(tensor (q-j)),
Gamma_(2j)   = Z^(tensor (j-1)) tensor Y tensor I^(tensor (q-j)).
```

If `s=2q+1`, add

```text
Gamma_(2q+1) = Z^(tensor q).
```

For the edge case `s=1`, this last formula is the `1 x 1` matrix `[1]`.

Every `Gamma_a` is a `D x D` Hermitian involution. Two different generators
anticommute: at the first tensor position where one generator has `X` or `Y`,
the later generator has `Z`, producing exactly one anticommuting tensor factor.
Consequently

```text
Gamma_a Gamma_b + Gamma_b Gamma_a = 2 delta_ab I_D.
```

If `a != b`, the product is a nonidentity Pauli string and is traceless. Hence

```text
Tr(Gamma_a Gamma_b)/D = delta_ab.
```

## CL-T3: observables associated with real unit vectors

For `v in R^s`, put

```text
Gamma(v) = sum_a v_a Gamma_a.
```

The anticommutation relations give

```text
Gamma(v)^2 = ||v||_2^2 I_D.
```

Thus, for a real unit vector, `Gamma(v)` is Hermitian with eigenvalues in
`{-1,+1}` and is a valid dichotomic observable.

## CL-T4: state and correlator identity

Let

```text
|Phi_D> = (1/sqrt(D)) sum_(k=1)^D |k> tensor |k>
```

be the maximally entangled state. Direct expansion in the computational basis
gives, for arbitrary `D x D` matrices `M,N`,

```text
<Phi_D| M tensor N |Phi_D> = Tr(M N^T)/D.
```

For real unit-vector families `x_i,y_j in R^s`, choose

```text
Alice: A_i = Gamma(x_i),
Bob:   B_j = Gamma(y_j)^T.
```

Transposition preserves Hermiticity and the involution property. Applying the
maximally entangled identity and CL-T2 gives

```text
<Phi_D| A_i tensor B_j |Phi_D>
  = Tr(Gamma(x_i) Gamma(y_j))/D
  = <x_i,y_j>.
```

Therefore every real unit-vector strategy in dimension `s` has an explicit
quantum realization with

```text
local Hilbert-space dimension D = 2^floor(s/2).
```

No minimality claim is needed for this construction.

## CL-T5: application to the balance spectrahedron

If `H` is a feasible balance weight of rank `s`, factor it as `H=T T^T` with
`T` of width `s`. The formulas

```text
Y = V T,
X = sqrt(m/n) U T
```

give real unit vectors realizing the spectral optimum. CL-T4 converts them to
a maximally entangled state and explicit local observables of dimension
`2^floor(s/2)` without changing any Bell correlator.

In particular, minimizing `rank(H)` over the balance spectrahedron gives the
best local-dimension bound furnished by this construction.

## CL-T6: status boundary

CL-T1 through CL-T5 are complete author-level algebraic derivations. An
independent reviewer still needs to inspect the tensor order, the odd-`s` edge
case, the transpose convention, and the connection to the unchanged claim
before the protocol permits a `PROVED` label.

