"""Why do all interleaved re-timings of M_cand's certified orders fail the repair test?
Diagnostic on a sample: hook classification and the repair-0 RATE over the minimum-weight family.
A schedule survives only if that rate is 0."""
import collections, itertools, random, sys, time
import core2 as C
from orderlib import OrderSector
_argv = sys.argv; sys.argv = ['v3_retime', '1,62,2', '14,2,0']
from v3_retime import mc_ok, build, random_linext, oZ, oX
sys.argv = _argv
from v4_newcand import FAMZ, FAMX

NS = int(sys.argv[1]) if len(sys.argv) > 1 else 8
rng = random.Random(4242)
sched = []
while len(sched) < NS:
    t = random_linext(rng)
    if not mc_ok(t):
        continue
    tX, tZ = build(t)
    if not C.interleave_stats(tX, tZ)[2]:
        continue
    sched.append((t, tX, tZ))

print("sample of %d legal+(MC)+interleaved re-timings of M_cand's orders" % NS)
print("family sizes: Z-memory %d, X-memory %d minimum-weight (11) gammas" % (len(FAMZ), len(FAMX)))
t0 = time.time()
for si, (t, tX, tZ) in enumerate(sched):
    pi, siv, _ = C.interleave_stats(tX, tZ)
    row = []
    for lab, mir, fam in (('Z', False, FAMZ), ('X', True, FAMX)):
        sec = C.Sector(tX, tZ, mirror=mir)
        kinds2 = collections.Counter(sec.classify(a, sec.suffix(a, 2)) for a in range(C.NG))
        kinds4 = collections.Counter(sec.classify(a, sec.suffix(a, 4)) for a in range(C.NG))
        n0 = 0
        for (V, ch) in fam:
            hooks, D = [], 0
            for (a, K) in ch:
                for l in K:
                    S = sec.suffix(a, l)
                    hooks.append((a, S))
                    D ^= C.msk(S)
            if C.sameround_repair0(sec, hooks, C.bits(V ^ D)) is not None:
                n0 += 1
        row.append("%s: repair-0 %4d/%4d (%.1f%%)  2-suffix hooks %s  4-suffix hooks %s"
                   % (lab, n0, len(fam), 100.0 * n0 / len(fam),
                      dict(kinds2), dict(kinds4)))
    print("  #%d  overlap-int %3d/648 | %s | %s" % (si, pi, row[0], row[1]))
    sys.stdout.flush()
print("(%.0fs)" % (time.time() - t0))
