"""The phi = a+b tiled family: survivor lists, LRC-compatible classes, colour-rotation orbits."""
import numpy as np, itertools, json
from gross import NG
from sched import make_phi, colour_valid
from cascade import REPS, CLS_OF, survivors, collect_rules, NCLS

def lrc_classes():
    """classes containing an order that is one contiguous L block (slots 0,1,2) then one
    contiguous R block (slots 3,4,5), or the reverse."""
    out=set()
    for Lp in itertools.permutations(range(3)):
        for Rp in itertools.permutations(range(3,6)):
            out.add(CLS_OF[tuple(Lp)+tuple(Rp)])
            out.add(CLS_OF[tuple(Rp)+tuple(Lp)])
    return sorted(out)

LRC = lrc_classes()

def surv(sector, s, t):
    phi = make_phi(s, t); assert colour_valid(phi)
    r1, r2 = collect_rules(sector, phi)
    alive, stage1, after1 = survivors(r1, r2)
    return [tuple(int(x) for x in v) for v in np.argwhere(alive)]

def rot_orbit(tr):
    return sorted({tr, (tr[1],tr[2],tr[0]), (tr[2],tr[0],tr[1])})

if __name__ == "__main__":
    print("LRC-compatible order classes (of 90):", LRC)
    out={}
    for sector in ('Z','X'):
        S = surv(sector, 1, 1)
        classes = sorted({c for t in S for c in t})
        reps=[]; seen=set()
        for t in S:
            if t in seen: continue
            o=rot_orbit(t); seen|=set(o); reps.append(t)
        print(f"\n=== sector {sector}, phi=a+b: {len(S)} survivors, classes used {classes}")
        print("   orbit reps under cyclic colour rotation:", len(reps))
        for t in S:
            print("   ", t, "orders", [REPS[c] for c in t],
                  "LRC" if all(c in LRC for c in t) else "",
                  "uniform" if len(set(t))==1 else "")
        out[sector]=dict(survivors=S, classes=classes, reps=reps,
                         lrc_survivors=[t for t in S if all(c in LRC for c in t)],
                         lrc_nonuniform=[t for t in S if all(c in LRC for c in t) and len(set(t))>1])
        print("   LRC-compatible survivors:", len(out[sector]['lrc_survivors']),
              " non-uniform:", len(out[sector]['lrc_nonuniform']))
        print("   ", out[sector]['lrc_nonuniform'])
    json.dump(out, open("fam.json","w"))
