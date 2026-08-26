# Fresh rerun of two archived finite checks

Recorded on 2026-08-25. These are new runs of the restored checkers, not
recovered July outputs. Both processes exited with code 0. No node was promoted.
Runtime: Python 3.12.13, NumPy 2.3.5. The numerical construction in each archived
program is retained; headers are portable and failure now produces a nonzero
exit code. The matched-degree program additionally counts rows and violations.

Run from the repository root, in an environment with NumPy installed:

```bash
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 se/tools/se_bridge2_legal_rebuild_n3.py
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 se/tools/se_matched_degree_lemma_check.py
```

## Bridge-II output

Script SHA-256:
`647b6a9634fe9e5442d0b4a1ee7c8f99be9a368e5fc11028c7fb626581fbbc48`.

Output excerpt:

```text
k=0  ||R(Xbar_k)|| = 1.0000000000  <=? r_top=1.000000   PASS
     ||R(Ybar_k)|| = 0.0000000000  <=? r_top*ambY=0.000000   PASS
k=1  ||R(Xbar_k)|| = 1.2000000000  <=? r_top=1.200000   PASS
     ||R(Ybar_k)|| = 0.6324555320  <=? r_top*ambY=0.692820   PASS
k=2  ||R(Xbar_k)|| = 1.0954451150  <=? r_top=2.000000   PASS
     ||R(Ybar_k)|| = 1.3416407865  <=? r_top*ambY=1.632993   PASS
```

The printed values match the [archived July run](logs_se_bridge2_20260717/bridge2_n3.log).
Only k=0 is in the n=3 taper window. The Y comparison uses supplied rounded
ambient norms (0, 0.57735027, 0.81649658); this program does not recompute those
anchors. The comparison tolerance is 1e-9 and the legal norms use floating-point
SVD. This is a finite diagnostic, not an all-n proof or an exact norm certificate.

## Matched-degree output

Script SHA-256:
`0e1a9351477d0ad1e555299c187743f40b08b53bfb5d5505ea29b2971f291fc8`.

The run enumerates the program's retained shape filters for
(q,m)=(6,6),(6,3),(6,4),(5,5),(5,3),(7,3), giving respectively 8, 7, 8, 5, 5, 7 rows.
Its final output is:

```text
CHECKED ROWS: 40; VIOLATIONS: 0
DONE
```

All printed q=m rows have numerical equality (EQ). The remaining printed
norms and ratios agree to their displayed precision with the
[archived output](logs_se_carrier_steps35_20260716/se_matched_degree_lemma_check.log).
The tolerance is 1e-8. This supports only the 40 enumerated rows, not an
exhaustive scan of every partition or the general matched-degree lemma.
