# SU(3) chain three-face fixed-cover complexity audit

Date: 2026-08-30

This audit counts the independent simplex coordinates in each selected fixed-three original-side
cover and the correlated Gram endpoints left after convexifying all other input blocks.  The two
compactified Dynkin labels are included in `NVAR`.

| shape/cluster | retained branch sets | NVAR | Gram endpoints |
|---|---|---:|---:|
| straight `((-4,2),(-2,1),(0,0))` | `hm, hm, hm` | 5 | 36 |
| bent `((-3,0),(-2,1),(0,0))` | `hc, hm, hm` | 5 | 36 |
| bent `((-3,0),(-1,-1),(0,0))` | `hm, hm, hc` | 5 | 36 |
| bent `((-3,3),(-2,1),(0,0))` | `hm, hcm, hm` | 6 | 24 |
| bent `((-3,3),(-1,2),(0,0))` | `hm, hm, hcm` | 6 | 24 |
| straight `((-2,-2),(-1,-1),(0,0))` | `hcm, hm, hc` | 6 | 24 |
| straight `((-2,4),(-1,2),(0,0))` | `hm, hcm, hcm` | 7 | 16 |
| bent `((-1,-1),(-1,2),(0,0))` | `hm, hcm, hc` | 6 | 24 |
| bent `((-1,-1),(0,-3),(0,0))` | `cm, hm, hc` | 5 | 36 |

The finite-scan-optimal cover for straight `((-2,4),(-1,2),(0,0))` uses two ternary blocks and is
seven-dimensional.  A subsequent coordinate-constrained search found the alternative
`((-1,4),(0,2),(2,-2))`, with branch sets `hm,hcm,hc`: it is six-dimensional with 24 endpoints
and retained a positive `0.084088268623` bit margin in a 120,000-sample million-label stress test.
This is the preferred exact route; the table preserves the originally selected cover for audit
history.

This is a combinatorial audit, not an entropy certificate.  In particular, a ternary retained
block contributes two stick-breaking coordinates and must not be represented by one variable.

Reproduce with
`holevo-extensive-violation/tools/audit_su3_chain_three_face_cover_complexity.py`.
