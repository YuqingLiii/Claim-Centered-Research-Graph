"""Does the translation-invariant minimum-depth class contain ANY measurement-consistent
schedule?  Brute force over (6!)^2 = 518400 candidate (X-order, Z-order) pairs."""
import numpy as np, itertools, time
from gross import NG
from sched import make_phi, expand, check_legal, mc_violations, sbb_noninterleaved

phi0 = np.zeros(NG, int)          # single colour = fully translation invariant

t0 = time.time()
legal = 0; mcok = 0; examples = []
for px in itertools.permutations(range(1, 7)):
    LX = np.zeros((3, 2, 3), int)
    for c in range(3):
        LX[c, 0, :] = px[:3]; LX[c, 1, :] = px[3:]
    for pz in itertools.permutations(range(1, 7)):
        LZ = np.zeros((3, 2, 3), int)
        for c in range(3):
            LZ[c, 0, :] = pz[:3]; LZ[c, 1, :] = pz[3:]
        tX, tZ = expand(phi0, LX, LZ)
        if not check_legal(tX, tZ, 6):
            continue
        legal += 1
        bad, tot = mc_violations(tX, tZ)
        if bad == 0:
            mcok += 1
            if len(examples) < 3:
                examples.append((px, pz))
print("legal TI min-depth schedules      :", legal)
print("of which measurement-consistent   :", mcok)
print("examples:", examples)
print("elapsed %.1f s" % (time.time() - t0))
