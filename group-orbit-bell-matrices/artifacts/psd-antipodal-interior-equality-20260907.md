# Ordered optimizers in the strict interior of the PSD antipodal window

Date: 2026-09-07. Author proof for independent adversarial review.
Canonical owner: `GROTHORB.psd-antipodal-interior-equality` (C18).
Route: `strict-gap-coefficients`.
Registration: `window-next-registration-20260907.md`, C18.

This artifact proves both directions of the exact registered optimizer
classification. The value premise is C15, whose author proof and
applicable independent review were read in full. The gap calculation
below is reconstructed from the original independent sign variables;
an equality conclusion is not inferred from a status label or from an
unexamined equation reference. No numerical experiment, external theorem,
new registered proposition, or endpoint classification is introduced.

## IE-1: statement, domain, and input bindings

Let `C` be a real symmetric PSD `N` by `N` matrix, `N>=1`. Write

```
d_i=C_ii,     d_min=min_i d_i>0,
0<lambda<d_min/2,
D(C)=(1/2)[C,-C;-C,C],     B=D(C)-lambda I_(2N).
```

Here `beta_cl(M)=max_{a,b in {+1,-1}^k} a^T M b` for a square
`k` by `k` real matrix. We prove that an ordered full sign pair `(a,b)`
attains `beta_cl(B)` if and only if

```
a=b=(z,-z),
z in {+1,-1}^N,     z^T C z=max_{w in {+1,-1}^N} w^T C w.
```

The statement hashes are SHA-256 of the parsed YAML string, stripped
at both ends and encoded in UTF-8:

| Statement | SHA-256 |
|---|---|
| C18 `claim` | `746e10d42ef48a0bfe93d2cb1d504271c4778806a582dc5ca3d18949e9e5a97d` |
| C18 `strict-gap-coefficients` implication | `efc78d327385e5bb26284efe100120667da70dc7b22540909eda65ce96e8669a` |
| C15 `GROTHORB.psd-antipodal-linear-window` claim | `98c4958c91dace11088aaff1ecc7b590bb982f84cc5d26c027bc8a2603beda38` |

Inspected input byte hashes, with project paths relative to
`grothendieck-group-orbit/`:

| Input | SHA-256 |
|---|---|
| `proof-dag/nodes/GROTHORB.psd-antipodal-interior-equality.yaml` | `2c05dd04eb30317d75281996de66bd1615aa03e532644cde8b5411c9feee604c` |
| `proof-dag/nodes/GROTHORB.psd-antipodal-linear-window.yaml` | `d49d9ea30af6722abde79d92acb2b7378626f6c7d0fe7a51534f206de984ffef` |
| `artifacts/window-next-registration-20260907.md` | `b77a1a721776e0f539e103c408a5bbfd3fa5d7a8295cd7a5ad878fb4ac3fe220` |
| `artifacts/psd-antipodal-linear-window-20260907.md`, PW-1--PW-6 | `281a14deb972523865c22c196b7972c4b3f704a541e7ddfa36ec3c68e7ab22f0` |
| `reviews/psd-antipodal-window-review-20260907.md`, applicable F1 | `fb1e4d331ba9c657d9cda1208cd51af6d836fd41afb79eb24ecb5e8072651c7d` |

The stage-root protocols were completely reread. Their byte hashes are
`d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095`
for `DAG_PROTOCOL.md` and
`6a2ea1af9bd14a4eaa8d158e304aee5e82cf907497addb17c2771782a4e6a329`
for `FILE_PROTOCOL.md`. The generated dependency view was inspected.
The existing C15 review's F1 binds the exact C15 claim hash above; it
reviews the value theorem, not this new all-optimizer statement.

## IE-2: the value premise and finite completion

Set

```
K=max_{z in {+1,-1}^N} z^T C z.
```

The maximum exists on a finite nonempty set. For arbitrary signs `s,t`,
symmetry and PSD give

```
0<=(s-t)^T C(s-t)=s^T Cs+t^T Ct-2s^T Ct,
s^T Ct<=(s^T Cs+t^T Ct)/2<=K.
```

Taking `s=t=z` at a maximizer shows `beta_cl(C)=K`. This PSD
reduction is applied to `C`, not to the shifted matrix `B`.
Our strict parameter range lies inside the closed interval of the
reviewed C15 premise. Consequently its optimum value is

```
beta_cl(B)=2K-2N lambda.                         (IE.1)
```

For later use, fix any `x in [-1,1]^N`. On the finite sign set give
each coordinate an independent distribution with probabilities
`Pr(Z_i=1)=(1+x_i)/2`, `Pr(Z_i=-1)=(1-x_i)/2`. Denote the expected
quadratic value by `E_x`. Since `E Z_i=x_i`, `Z_i^2=1`, and the
distinct-coordinate moments factor, direct expansion gives

```
E_x=sum_i d_i+sum_{i!=j} C_ij x_i x_j
   =x^T Cx+sum_i d_i(1-x_i^2) <= K.             (IE.2)
```

The inequality holds because every realization has value at most `K`.
This is a finite convex combination, not sampling or numerical evidence.
It includes deterministic coordinate distributions when `x_i=+1` or
`-1`, and the identity itself does not require positive definiteness.

## IE-3: exact coordinates for every ordered full sign pair

Start with arbitrary, independently chosen signs
`a=(a_+,a_-)`, `b=(b_+,b_-)` in `{+1,-1}^{2N}`. Define

```
p=(a_+-a_-)/2,     u=(a_++a_-)/2,
q=(b_+-b_-)/2,     v=(b_++b_-)/2.
```

At each coordinate exactly one of `p_i,u_i` is a sign and the other
is zero. The same assertion holds for `q_i,v_i`. In particular

```
p_i,u_i,q_i,v_i in {-1,0,1},
p_i^2+u_i^2=q_i^2+v_i^2=1.                     (IE.3)
```

No equality between Alice's and Bob's coordinates has been assumed.
The inverse formulas are
`a=(p+u,u-p)`, `b=(q+v,v-q)`, so no ordered full sign pairs are lost.

Expanding the two matrix terms separately gives

```
a^T D(C)b=(1/2)(a_+-a_-)^T C(b_+-b_-)=2p^T Cq,
a^T b=(p+u)^T(q+v)+(u-p)^T(v-q)
     =2(p dot q+u dot v).
```

Thus, writing `S=(1/2)a^T B b`,

```
S=p^T Cq-lambda(p dot q+u dot v).                (IE.4)
```

Now put `x=(p+q)/2`, `y=(p-q)/2`. Then `x in [-1,1]^N`,
`p=x+y`, `q=x-y`. Symmetry cancels the mixed terms in

```
p^T Cq=(x+y)^T C(x-y)=x^T Cx-y^T Cy.           (IE.5)
```

## IE-4: independent reconstruction of the full nonnegative gap

By (IE.1), the half-gap to the optimum is
`G=(beta_cl(B)-a^T B b)/2=K-N lambda-S`. Substitution of
(IE.2), (IE.4), and (IE.5) first yields

```
G=(K-E_x)+y^T Cy
  +sum_i [d_i(1-x_i^2)-lambda(1-p_i q_i-u_i v_i)].
                                                               (IE.6)
```

To expose the sign of each coordinate contribution, expand `x_i`:

```
2(1-x_i^2)-(1-p_i q_i-u_i v_i)
  =1-(p_i^2+q_i^2)/2+u_i v_i
  =(u_i^2+v_i^2)/2+u_i v_i
  =(u_i+v_i)^2/2.                              (IE.7)
```

The middle equality uses both relations in (IE.3). Hence the bracket
in (IE.6) equals
`(d_i-2lambda)(1-x_i^2)+(lambda/2)(u_i+v_i)^2` exactly. We obtain

```
G=(K-E_x)+y^T Cy
  +sum_i (d_i-2lambda)(1-x_i^2)
  +(lambda/2)||u+v||_2^2.                      (IE.8)
```

All terms are nonnegative, for separate explicit reasons:

- `K-E_x>=0` follows from the finite completion in (IE.2).
- `y^T Cy>=0` follows from PSD.
- `1-x_i^2>=0`, and `d_i-2lambda>=d_min-2lambda>0` for every `i`.
- The final coefficient is positive because `lambda>0`.

This reconstructs the complete gap for every original ordered sign
pair. No restriction to antipodal or synchronized signs was used to
derive it.

## IE-5: necessity and recovery of the actual signs

Suppose `(a,b)` is optimal. Then `G=0` by (IE.1). Every summand
on the right of (IE.8) is nonnegative, so in particular

```
(d_i-2lambda)(1-x_i^2)=0   for every i.
```

Strict positivity of `d_i-2lambda` forces `x_i^2=1`. Since
`x_i=(p_i+q_i)/2` and each of `p_i,q_i` belongs to `[-1,1]`, an
average equal to `+1` forces `p_i=q_i=+1`, and an average equal to
`-1` forces `p_i=q_i=-1`. Therefore

```
p=q=x=z in {+1,-1}^N.
```

The coordinate identities (IE.3) now force `u=v=0`; also `y=0`.
The inverse formulas from IE-3 give the literal equalities

```
a=b=(z,-z).                                   (IE.9)
```

Because all `x_i^2=1`, (IE.2) says `E_x=z^T C z`. In (IE.8)
every remaining term except `K-E_x` is now zero, so optimality also
forces `z^T C z=K`. This proves every part of the necessary condition,
including coincidence of the ordered signs, not merely their images
under `C`.

## IE-6: sufficiency and completeness of the ordered classification

Conversely, let `z` be any sign vector with `z^T C z=K` and set
`a=b=(z,-z)`. Then `p=q=z`, `u=v=0`, and (IE.4) gives

```
a^T B b=2z^T C z-2lambda ||z||_2^2
       =2K-2N lambda
       =beta_cl(B).
```

Thus every pair stated in the claim attains the optimum. Together
with IE-5, this proves the iff. The classification is of ordered pairs
themselves, not equivalence classes under switching, swapping, or global
sign. Distinct maximizing `z` give distinct pairs; the simultaneous
global negation is already represented by `-z`, whose quadratic value
equals that of `z`. No uniqueness of the maximizing `z` is asserted.

## IE-7: singular inputs, N=1, and strict-domain exclusions

Singular PSD matrices with positive diagonal are fully included. The
proof never divides by an eigenvalue or inverts `C`. In particular, it
does not infer `y=0` from `y^T Cy=0`, which would be invalid for
singular `C`. Instead the strictly positive coordinate coefficients
force `p=q=z`, hence `y=0`, independently of the kernel of `C`.

For `N=1`, write `C=[d]`, `d>0`, and `0<lambda<d/2`. The finite
maximum is `K=d`; the displayed optimum is `2d-2lambda`. Both
choices `z=+1,-1` maximize the scalar quadratic. The preceding
necessity gives exactly the two ordered pairs
`a=b=(1,-1)` and `a=b=(-1,1)`, and sufficiency verifies each.
No multi-coordinate argument or nonempty off-diagonal sum is required.

The registered claim excludes `lambda=0` and `lambda=d_min/2`.
At the upper endpoint, some coefficients `d_i-2lambda` may vanish,
so IE-5's forcing argument cannot be used at those coordinates. At
the lower endpoint, the last term of (IE.8) loses its positive
coefficient; this artifact makes no lower-endpoint classification.
In particular, exclusion of an endpoint from the statement is not an
assertion that the classification necessarily fails there: the decisive
forcing used in IE-5 is `d_i-2lambda>0`.

Inputs with `d_min=0` are outside C18, and there is then no `lambda`
satisfying its strict inequalities. The proof does not treat zero
diagonal entries as positive, infer a positive-width interval for them,
or classify their zero-shift optimizers. No assertion about parameters
outside the registered strict interval is made.

## IE-8: route assembly and status

The sole project premise is the exact C15 optimum value, applied in
IE-2 after explicitly reducing `beta_cl(C)` to `K`. IE-3--IE-4
reconstruct the full gap, IE-5 proves necessity by strict coefficients,
and IE-6 proves sufficiency. These steps establish the registered
`strict-gap-coefficients` implication and its exact parent claim.
The supporting coordinate and expectation calculations are included
here rather than assumed as unregistered lemmas.

This is a new author artifact, not an independent review of C18.
The author did not write the C15 proof; earlier work on C15 was limited
to literature positioning. The existing F1 review certifies the C15
premise only. C18 and its implication still require author-independent
adversarial review before any completion-level promotion. Integration
is left to the coordinator; no node, protocol, author input, or old
stage file was changed by this task.
