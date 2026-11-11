# Bent-central ternary three-face certificate: stopped depth-10 replay

Date: 2026-08-31

Status: the registered depth-6 certificate failed at a precisely recorded full-depth box; a
runtime-only depth-10 replay was later stopped at user request after the `10000/4992/15`
checkpoint. The atomic node remains `NUMERICAL`.

## Exact depth-6 failure

For the bent cluster `((-1,-1),(-1,2),(0,0))`, exact reconstruction succeeded for 24 Gram
endpoints of degree tuple `(12,14,2,2,2,2)` and three retained-side distributions of degree tuple
`(6,6,1,1,1,1)`. The registered run exhausted depth 6 at

```text
((63/64,1), (45/64,23/32), (1/2,33/64),
 (49/64,25/32), (51/64,13/16), (1/32,3/64))
```

with printed lower-enclosure diagnostic `-0.00026545496304754106`. Every interval has width
`1/64`. This is a certificate-resolution failure, not a negative evaluation of the true margin
and not a mathematical counterexample.

## Stopped depth-10 replay

Without changing the public driver or shared core, a runtime override set the maximum per-axis
depth to 10. It passed the original depth-6 failure region and reached:

```text
bent-central-ternary-fixed-three: processed=10000, certified=4992, pending=15
```

The user then requested that this session stop. A keyboard interrupt was delivered only to this
session's depth-10 process, while it was computing an exact rational range. No depth-10
uncertified box and no exit-zero final verdict were printed. The checkpoint therefore cannot be
used as a certificate and does not justify any evidence-level promotion.

The complete recorded output for both attempts is in
`SU3_BENT_CENTRAL_TERNARY_THREE_FACE_CERTIFICATE_STOPPED_20260831.txt`. A future continuation may
resume with a fresh source-bound depth-10 run or first sharpen the enclosure around the recorded
depth-6 box; it must not treat the interrupted prefix as reusable terminal evidence.
