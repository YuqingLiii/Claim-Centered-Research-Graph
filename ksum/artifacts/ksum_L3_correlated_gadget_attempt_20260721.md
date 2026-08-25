# KSUM.B4b.L3 constructive attempt — a shared-address range-coupled claw gadget

Date: 2026-07-21

Controlling node: `KSUM.B4b.L3`

Scope: one explicit promised, range-coupled outer gadget; a fixed-query embedding into ordinary
two-list claw and cyclic 2-SUM; exact completeness, soundness, padding, and spurious-claw checks;
then an adversarial factorization audit.  Only the local corpus is used.  No DAG file is edited.

## Verdict

**The embedding lemma succeeds, but the gadget is killed as an L3 hardness candidate.**

The proposed gadget couples all pSearch buckets carrying the same range value through one shared
hidden address.  It has a one-query flattening into two-list claw with range `q+2`, and a
two-query-clean simulation into cyclic 2-SUM over `Z_(2q+5)`.  The two list-specific dummy values
make completeness and soundness exact even with arbitrary padding.

However, the same coupling creates a transposed search decomposition.  Equal real values must
occur in the same address column, so the gadget is exactly an OR over `m` ordinary `q`-by-`q`
column-claw predicates.  Grover search over columns and the standard `O(q^(2/3))` claw algorithm
give

```text
Q(RCClaw_(q,m))=O(sqrt(m) q^(2/3))
                =O(sqrt(n) q^(1/6)),       n=qm.        (L3.1)
```

This is the ABI exponent, strictly below the required
`sqrt(n) q^(1/4)` for growing `q`.  Thus the candidate does not literally have a Cartesian
independent-pSearch promise, but it computationally refactors after transposing rows and columns.
The required adversary or approximate-degree lower bound is impossible for this gadget because
of (L3.1).

No route outside the registered L3 claim is generated.

## 1. Parameters and oracle model

Fix integers

```text
q>=2,       m>=1.                                       (L3.2)
```

There are two arrays

```text
X^L,X^R in ({*} union [q])^([q] x [m]).                 (L3.3)
```

The oracle is the usual tagged cell oracle: a query specifies a side, row, and column and returns
the symbol in that cell.  Superpositions across sides and cells are allowed.

The promise has two parts.

### P1. One real symbol per row

For every side `sigma in {L,R}` and row `i in [q]`, exactly one entry of
`X^sigma_(i,*)` belongs to `[q]`; all other entries are `*`.  Let

```text
F_sigma(i) in [q]                                       (L3.4)
```

be that unique real symbol.

### P2. Shared hidden range address

There exists a map

```text
alpha:[q]->[m]                                          (L3.5)
```

such that

```text
X^sigma_(i,a)=v in [q]  implies  a=alpha(v).            (L3.6)
```

The map `alpha` is not supplied by a separate oracle.  It is visible only through the marked
cells.  It may be noninjective, and values unused by both sides impose no observable condition.
Thus all occurrences of one range value share an address, while different values may share an
address.

Define the promised Boolean gadget

```text
RCClaw_(q,m)(X^L,X^R)=1
iff exists i,j: F_L(i)=F_R(j).                          (L3.7)
```

This is a genuine range coupling: the allowed marked address in one row depends on its decoded
range value and must agree with every other occurrence of that value on both sides.

## 2. Exact embedding into two-list claw

Flatten each `q`-by-`m` array in row-major order.  Introduce two symbols outside the real range,

```text
d_L=q+1,       d_R=q+2.                                 (L3.8)
```

Define length-`qm` claw lists `A,B` by

```text
A_(i,a)= X^L_(i,a)  if real, and d_L if *,
B_(j,b)= X^R_(j,b)  if real, and d_R if *.              (L3.9)
```

Both lists use the common alphabet `[q+2]`.

### Completeness

If `RCClaw=1`, choose `i,j` with

```text
F_L(i)=F_R(j)=v.                                        (L3.10)
```

By the promise, the two real cells occur at address `alpha(v)`.  Therefore

```text
A_(i,alpha(v))=v=B_(j,alpha(v)),                         (L3.11)
```

so the flattened lists contain a claw.

### Soundness

Suppose `A_(i,a)=B_(j,b)`.  The common symbol cannot be a dummy:

```text
d_L!=d_R,
d_L,d_R notin [q].                                      (L3.12)
```

Hence both cells are real and equal to some `v in [q]`.  Their decoded row values satisfy

```text
F_L(i)=v=F_R(j),                                        (L3.13)
```

so `RCClaw=1`.  This direction does not rely on knowing `alpha`.

Thus

```text
RCClaw_(q,m)(X)=Claw_(qm -> q+2)(A,B)                  (L3.14)
```

exactly on every promised input.

### Query cost

A query to a real flattened coordinate makes one query to the corresponding gadget cell and
then applies the fixed replacement `*->d_sigma`.  Padding coordinates, introduced below, are
answered without a source query.  In a clean XOR-oracle simulation, querying and unquerying the
source work register costs at most two source queries.  The overhead is therefore an absolute
constant independent of `q,m,n`.

## 3. Arbitrary list lengths and padding

Let the desired ordinary claw lists have length `n>=q`, not necessarily divisible by `q`.  Put

```text
m=floor(n/q),       p=n-qm,       0<=p<q.               (L3.15)
```

Use the `qm` real gadget cells and append `p` copies of `d_L` to the left list and `p` copies of
`d_R` to the right list.

No padded cell creates a claw:

```text
- left padding has value d_L, absent from the entire right list;
- right padding has value d_R, absent from the entire left list;
- d_L and d_R are distinct.                              (L3.16)
```

Repeated padding inside one list is irrelevant because two-list claw tests one coordinate from
each list.  Consequently (L3.14) remains exact at length `n`, with range `q+2=O(q)`.

## 4. Exact embedding into cyclic 2-SUM

Set

```text
Q=2(q+2)+1=2q+5.                                       (L3.17)
```

For every left-list symbol `c` use the cyclic value `c in Z_Q`; for every right-list symbol `c`
use `Q-c`.  Concatenate the two lists into `2n` positions.

### Cross-list pairs

For `c,d in [q+2]`,

```text
c+(Q-d)=0 mod Q  iff  c=d,                              (L3.18)
```

because `|c-d|<Q`.  Therefore cross-list zero-sums are exactly the claws of (L3.14).

### Within-left pairs

The left list uses only

```text
[q] union {q+1}.                                        (L3.19)
```

For two left values, their integer sum is between `2` and `2q+2<Q`; it cannot vanish modulo
`Q`.

### Within-right pairs

The right symbol set before negation is

```text
[q] union {q+2}.                                        (L3.20)
```

For any two such symbols, `2<=c+d<=2q+4<Q`.  Hence

```text
(Q-c)+(Q-d)=-(c+d) !=0 mod Q.                           (L3.21)
```

### Dummy and padding cases

The left dummy represents symbol `q+1`, while the right dummy represents `q+2`.  Equation
(L3.18) shows that they do not form a cross zero-sum.  Neither dummy equals a real symbol.
Repeated padding therefore creates neither a cross-list nor a within-list zero-sum.

We have proved the exact identity

```text
RCClaw_(q,m)=Cyclic2SUM_(2n,Q,target=0)                 (L3.22)
```

on the encoded promise, with `Q=2q+5=O(q)` and constant query overhead.

If an odd total input length is desired, append one coordinate fixed to `0`.  All other encoded
values are nonzero and there is only one zero, so it creates no witness.  For arbitrary target
`t in Z_Q`, translate every coordinate by `t/2`; `Q` is odd, so `2` is invertible, and every pair
sum is shifted from `0` to `t` bijectively.  This also preserves the padding proof.

## 5. The intended hardness intuition

The ABI assembly uses `2q` Cartesian-independent pSearch buckets.  In contrast, P2 makes the
marked positions input-dependent across buckets:

```text
same decoded value  =>  same marked address.            (L3.23)
```

There is no fixed per-row permutation that makes the addresses independent, because the required
permutation depends on the unknown decoded value.  The promise domain is not a Cartesian product
of `2q` pSearch domains, so the Brassard pSearch composition theorem cannot simply be invoked in
either direction.

A hoped-for L3 theorem would be

```text
Adv^+-(RCClaw_(q,m))
 >= Omega(sqrt(qm) q^(1/4))
 =  Omega(sqrt(m) q^(3/4)).                             (L3.24)
```

Together with (L3.22), this would give the desired quarter-power cyclic 2-SUM lower bound at
alphabet `O(q)`.

The next section shows that (L3.24) is false.

## 6. Transposed factorization and upper algorithm

For each address `a in [m]`, define the column predicate

```text
C_a=1
iff exists i,j in [q], v in [q]:
    X^L_(i,a)=v=X^R_(j,a).                              (L3.25)
```

P2 gives both implications

```text
RCClaw_(q,m)=1  iff  exists a: C_a=1.                  (L3.26)
```

The forward implication is where the correlation is used: equal decoded value `v` forces both
occurrences into column `alpha(v)`.  The reverse implication is immediate.

For a fixed column, `C_a` is an ordinary two-list claw instance on two length-`q` lists; stars can
be mapped to the two distinct dummies exactly as in (L3.9).  The standard range-independent claw
algorithm evaluates it in

```text
O(q^(2/3))                                               (L3.27)
```

queries.  Bounded-error Grover search over the `m` columns then evaluates (L3.26) in

```text
O(sqrt(m) q^(2/3))                                      (L3.28)
```

queries, up to the standard constant-error composition overhead.  The promise coupling between
columns cannot invalidate this upper bound: the algorithm is correct on the larger domain where
the column predicates are arbitrary.

Writing `n=qm`, (L3.28) becomes

```text
O(sqrt(n) q^(1/6)).                                     (L3.29)
```

Since `q^(2/3)=o(q^(3/4))`, (L3.28) contradicts the hoped-for lower bound (L3.24) for unbounded
`q`.

## 7. Does the gadget secretly factor into independent pSearch?

There are two answers, and distinguishing them matters.

### Literal row-wise answer: no

Ignoring P2, the row representation is

```text
Claw_(q -> q) composed with 2q copies of pSearch_m.      (L3.30)
```

P2 restricts the joint domain non-Cartesianly, so the inner instances are not independent and
the BHK product theorem does not directly describe the promised function.

### Computational answer: yes, at the same exponent

After transposing the array, (L3.26) is search over address-indexed ordinary claws.  It is not
literally BHK's pSearch composition, but it restores the same multiplication

```text
sqrt(m) times q^(2/3),                                  (L3.31)
```

and hence the same `sqrt(n)q^(1/6)` ceiling.  The range coupling has only moved the independent
search coordinate from rows to columns; it has not produced the global extra `q^(1/12)` required
by L3.

Thus the kill criterion fires even more strongly than “secretly factors”: the gadget has an
explicit upper algorithm below the target.

## 8. What lower bound would still be required

For this candidate, no adversary or approximate-degree campaign remains: (L3.28) proves that the
required target is false.

For a different gadget still inside L3, the first genuinely new theorem would have to establish
all of the following simultaneously:

```text
1. Adv^+- or approximate degree Omega(sqrt(n) q^(1/4));
2. no searchable latent coordinate a whose conditioning leaves an ordinary q^(2/3) claw;
3. no Cartesian pSearch decomposition with a tight sqrt(m) inner factor;
4. constant-query embedding into range O(q) claw or cyclic 2-SUM;
5. total promise correctness, including padding and all spurious-claw cases.
```

Ordinary `q`-by-`q` claw cannot serve as a stronger outer donor: its `Theta(q^(2/3))` complexity
is tight.  Independent pSearch cannot supply the missing factor either: its `Theta(sqrt(m))`
complexity is tight.  The missing `q^(1/12)` must therefore come from a genuinely global assembly
whose correlations do not expose a Grover-searchable coordinate such as (L3.26).

Merely proving that a promise is non-Cartesian is insufficient.  One must rule out alternate
factorizations and upper algorithms, not only the ABI row-wise factorization.

## 9. Gate ledger

| obligation | result |
|:---|:---|
| explicit correlated range-coupled gadget | **PASS**: P1-P2 |
| fixed `O(1)`-query embedding into two-list claw | **PASS**: (L3.9)-(L3.14) |
| range `O(q)` | **PASS**: `q+2` for claw |
| exact completeness and soundness | **PASS** |
| arbitrary list padding | **PASS** with side-specific dummies |
| cyclic 2-SUM embedding | **PASS** over `Z_(2q+5)` |
| within-half spurious zero-sums | **NONE** by (L3.19)-(L3.21) |
| dummy/padding spurious claws | **NONE** by (L3.12), (L3.16) |
| odd-length padding / arbitrary target | **PASS** |
| literal independent-pSearch Cartesian product | **NO** |
| alternate low-cost factorization | **YES**: OR over address-column claws |
| required `sqrt(n)q^(1/4)` lower bound | **IMPOSSIBLE for this gadget** by (L3.28) |
| L3 node | remains **OPEN**; this is one failed candidate |
| route outside L3 | **NONE** |

## 10. Conclusion

The shared-address gadget is a clean example of why the first L3 lemma needs both an embedding
proof and an immediate upper-algorithm audit.  Its range coupling is real, the padding and cyclic
2-SUM maps are exact, and it is not a Cartesian product of pSearch promises.  Nevertheless the
coupling aligns every possible claw into one address column, exposing an OR-of-claws
factorization and reproducing the ABI `q^(1/6)` exponent.

Accordingly this candidate should be discarded.  It supplies no lower-bound progress beyond the
existing fixed-relabel claw reduction.  The registered L3 route remains open only for a more
global correlation pattern that cannot be localized by conditioning on a searchable address or
range coordinate.
