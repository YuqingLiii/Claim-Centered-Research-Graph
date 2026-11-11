"""[SBB26] Prop. 6's own second step, reproduced: 'we tile ALL RED CHECKS with a residual set, and
upper bound the resulting extended-code distances.  Scanning through the 45 residual sets, we find
all but 4 have extended-code distance of 10 or below.'

R = the residual errors of the 24 checks of ONE colour class only.  A class is eliminated when some
weight-12 logical L contains either a covered triple in the last three CNOT positions of one check
of that colour (gain 2 -> weight 10) or two DISJOINT weight-2 residuals of two checks of that
colour (gain 1+1 -> weight 10).  Every elimination exhibits a weight-10 extended codeword, so the
filter is one-sided sound, exactly as the paper's upper-bound search is."""
import itertools
import numpy as np
from gross import NG
from sched import make_phi, colour_valid
from cascade import (REPS, NCLS, ACT2, ACT3, PAIRS, TRIPS, PIDX, TIDX, sector_data, collect_rules,
                     survivors)

def stage1(sector, phi):
    """the 90 -> 45 filter (single isolated check), colour-independent"""
    slots, Pl, Hstab, Hdet = sector_data(sector)
    kill = set()
    for L in Pl:
        for c in range(NG):
            S = [k for k in range(6) if L[slots[c][k]]]
            if len(S) == 3:
                kill.add(TIDX[tuple(S)])
    ok = np.ones(NCLS, bool)
    for ti in kill:
        ok &= ~ACT3[:, ti]
    return ok

def tile_one_colour(sector, phi, colour, alive45):
    """which of the 45 survive when that residual class is tiled on ONE colour class"""
    slots, Pl, Hstab, Hdet = sector_data(sector)
    dead = np.zeros(NCLS, bool)
    for L in Pl:
        hits = []
        for c in range(NG):
            if int(phi[c]) != colour:
                continue
            S = [k for k in range(6) if L[slots[c][k]]]
            if len(S) < 2:
                continue
            for Pr in itertools.combinations(S, 2):
                hits.append((PIDX[Pr], frozenset(slots[c][k] for k in Pr)))
        for i in range(len(hits)):
            for j in range(i + 1, len(hits)):
                if hits[i][1] & hits[j][1]:
                    continue
                dead |= (ACT2[:, hits[i][0]] & ACT2[:, hits[j][0]])
    return alive45 & ~dead

for sector in ('Z', 'X'):
    a45 = stage1(sector, None)
    print(f"=== sector {sector}:  90 -> {int(a45.sum())} after the single-check filter")
    for (s, t) in [(1, 1), (1, 2), (2, 1), (2, 2)]:
        phi = make_phi(s, t); assert colour_valid(phi)
        res = []
        for colour in range(3):
            surv = tile_one_colour(sector, phi, colour, a45)
            res.append(sorted(int(i) for i in np.nonzero(surv)[0]))
        same = all(r == res[0] for r in res)
        print(f"   phi={s}a+{t}b : 45 -> {len(res[0])} per colour  {res[0]}"
              f"   (identical for all three colours: {same})")
