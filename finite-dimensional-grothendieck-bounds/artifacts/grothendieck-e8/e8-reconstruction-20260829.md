# E8 candidate reconstruction

## E8-R1: imported checker scope

The imported checker constructs eight simple roots over exact rationals,
verifies their Gram matrix and determinant one, constructs all 240 norm-two E8
roots, changes them to integral simple-root coordinates, selects the 120
positive roots, and enumerates all 25080 filters of the resulting root poset.
It verifies the full stored table `F_k` and in particular

```text
F_98 = 2366
F_104 = 2420.
```

All arithmetic in these checks is integral or rational.

## E8-R2: fresh local replay

On 2026-08-29 the checker completed locally with exit status zero and the
three-line output stored in `e8-checker-run-20260829.txt`.  Its source SHA-256
at import was
`9b7345153bcc10623f2b573d4b2f654706b8f4309b410eb0de3bff0541356f0e`.

## E8-R3: reported Bell values

The prior research state reported

```text
omega_8 = 9240
omega_1 = 6104
omega_8 / omega_1 = 9240 / 6104 = 165 / 109.
```

The ratio arithmetic is immediate.  The current local checker, however, does
not itself define the Bell matrix or derive either 9240 or 6104 from its
`F_k` table.  Those bridges must be reconstructed as explicit lemmas rather
than inferred from the checker's filename or from a former conversation.

## E8-R4: missing proof interfaces

The local record still needs:

1. a canonical integer/rational definition and hash of the Bell matrix;
2. an exact derivation of the dimension-eight vector value 9240;
3. the reduction of every classical sign strategy to the enumerated E8-poset
   optimization and the exact derivation of 6104;
4. explicit unit vectors, a bipartite quantum state, and dichotomic observables
   attaining the vector correlations;
5. an independent adversarial review binding the unchanged claims and the
   complete derivations.

## E8-R5: status boundary

The root construction and filter census are reproducible exact computations,
so their repository level is `NUMERICAL`.  The reported Bell values have a
substantive reconstruction target but incomplete local derivations, so they
remain `CONJECTURED`.  The physical state/measurement claim remains `OPEN`.

