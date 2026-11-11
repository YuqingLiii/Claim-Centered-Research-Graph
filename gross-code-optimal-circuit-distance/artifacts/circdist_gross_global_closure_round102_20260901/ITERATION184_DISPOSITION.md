# Mandatory iteration-184 disposition

## Exact starting bind

The unstarted reviewed frontier was used before any global experiment:

* 14,484 inherited sound order predicates;
* 328 exact EFSSC selectors;
* state SHA-256 `3b128ef192074a3bc0c163502e97eff99ab9d15c546381e98e1e178471552d7b`;
* selector-state SHA-256 `7296aa70690e01852519b78826b173af35998cec0e9c124c46ea30101dd0777d`;
* source-file SHA-256 `5eb1607bebea7bfc44b693a4a3a9ae19f2ab5ae498407290863b34d6eb9b66b0`;
* semantic-source SHA-256 `d601f297e8b2a1b7d6179d19452da8b0abca2e4f16d7404b6395a8254e949268`;
* CNF SHA-256 `2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62`;
* 19,210 assertions, 415,793 variables, and 1,416,404 clauses.

The package snapshots and live bindings independently reproduce those values.
Proof output was named on the CaDiCaL command line before each solve started.

## Outer result

CaDiCaL PID 41074 returned SAT (rc 10) in 3.195227 seconds.  The complete
assignment satisfied all 1,416,404 clauses.  Decoding and replay proved:

* a bijective assignment of all 864 edge times;
* all frozen conflict, MC0, precedence, extrema, and interleaving predicates;
* 123 compressed layers, times 0 through 122;
* zero inherited block hits and zero installed selector hits;
* compressed-schedule SHA-256
  `5c13a6ef32fec263f6cdc5d10db1da30d6758a79f089194814fe99e360d55c23`.

The SAT-side output stream is retained losslessly: raw SHA-256
`8e0d0549a78a735da03f8d2633e9fd154d4c08d19af7e92bd748358b8e7ec877`,
98,909,039 bytes / 3,425,586 LF; deterministic-gzip SHA-256
`64db96f8bd0f9d5f75838babd09526724ebbd1b1502e547eb2ff97dedd68fd5c`,
16,725,168 bytes.  This SAT stream is not an UNSAT certificate.

## Complete unrestricted direct-360 results

Both rebuilt queries used all 360 named columns with exact
`sum(select) <= 10`, all 72 detector rows, all 12 logical rows, and no pool,
residual-pattern, check-count, or within-check-order restriction.

### Xerr

Formula SHA-256
`40bcf7fc4e701d496c03d521324c5b7d88e094b5a350dbfb1f25468e1bea0b63`,
5,935 variables / 22,320 clauses.  PID 41183 returned SAT in 7.355678 seconds.
The complete assignment passed every clause.  The named-weight-10 mechanism is

```text
D:129 R:1:0 R:2:0 R:3:2 R:9:1 R:18:2 R:44:2 R:53:2 R:55:0 R:61:0
```

Its canonical support is
`[1,2,5,27,36,45,48,63,71,78,85,86,87,102,128,129,130,139]`; its physical
support is
`[4,5,7,19,20,27,36,45,48,56,57,62,71,73,76,77,78,79,80,87,102,128,129,133,136,139]`.
Both detector syndromes are zero and both logical vectors equal
`[1,0,0,0,0,0,0,1,1,1,1,1]`.  Its exact source-schedule-valid exclusion has
73 order atoms.

The SAT-side stream has raw SHA-256
`c7b16f50def540eb654021183736057d6a335a8ab877c5b0bcdb16c72ba720bf`,
82,029,613 bytes / 452,102 LF, stored in 16,540,307 deterministic-gzip bytes.

### Zerr

Formula SHA-256
`539289f9eccfd06d9c71e046fd62b2ec7140c09f5250f5761d9d5c55698b1f49`,
5,904 variables / 22,196 clauses.  PID 41190 returned SAT in 32.101532 seconds.
The complete assignment passed every clause.  The named-weight-10 mechanism is

```text
D:47 D:90 D:113 D:143 R:3:2 R:13:0 R:17:2 R:37:0 R:38:0 R:45:0
```

Its canonical support is `[7,14,31,32,39,47,63,74,89,90,113,115]`; its
physical support is
`[1,14,16,25,26,33,40,41,42,47,63,74,84,90,91,92,99,109,116,139]`.
Both detector syndromes are zero and both logical vectors equal
`[1,1,1,1,1,0,1,1,1,1,1,1]`.  Its exact source-schedule-valid exclusion has
48 order atoms.

The SAT-side stream has raw SHA-256
`125e861bc3e4f72321d9d322879db2f468436f5e681f3174afbf02c0092d7061`,
350,661,070 bytes / 1,487,763 LF, stored in 71,140,712 deterministic-gzip bytes.

## Atomic transition

Only after both complete sectors were SAT, the two exact selectors were staged,
compiled, independently encoding-checked, and atomically promoted inside this
proposal package.  The fresh iteration-185 base has 330 selectors, selector
state SHA-256
`efcfc98b44e4d5abea00b3618c8828e65971bea46dc9b9eea081fde89df42004`,
source SHA-256
`1c42610cbb692000204d26967c668173b551d3a187249e67a4b569f5c3465b41`,
semantic SHA-256
`f1593c4f09c197d38e44f3631d0565081e382294786a3cf5dd49ec16901501c5`,
and CNF SHA-256
`ddd40740b42854b74de7d64e3899f017a58a56223b3fa560d15845a9f7cae6c9`
(19,212 assertions, 416,062 variables, 1,417,374 clauses).  Repair was
forbidden and was not entered.

