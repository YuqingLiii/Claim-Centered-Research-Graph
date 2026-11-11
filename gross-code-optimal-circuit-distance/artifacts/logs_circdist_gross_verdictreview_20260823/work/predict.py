"""Empirical hardness model for an open (sector,K,Ew,orbit) sub-query, fitted on the
718 already-decided sub-queries of this sweep.  Features: the slack s = (W + 2K) - Ew
(s = 0 collapses to unit propagation via cut (c6)) and the residual-orbit index."""
import json, glob, os, collections, statistics, sys
HERE=os.path.dirname(os.path.abspath(__file__))
CAND={('Z',(1,2,62)),('X',(14,0,2))}
def load():
    rec={}
    for L in sorted(glob.glob(os.path.join(HERE,'logs','*.jsonl'))):
        for l in open(L):
            try: r=json.loads(l)
            except: continue
            if r.get('verdict') not in ('SAT','UNSAT') or r.get('orbit',-1)<0: continue
            if (r['sector'],tuple(r['triple'])) not in CAND: continue
            k=(r['sector'],r['K'],r['Ew'],r['orbit'])
            if k not in rec or rec[k]['seconds']>r['seconds']: rec[k]=r
    return rec
def model(rec):
    by=collections.defaultdict(list)
    for (sec,K,Ew,orb),r in rec.items():
        by[((10+2*K)-Ew, orb)].append(r['seconds'])
    return {k: statistics.median(v) for k,v in by.items()}, by
def predict(m, K, Ew, orb):
    s=(10+2*K)-Ew
    if (s,orb) in m: return m[(s,orb)]
    cand=[v for (s2,o2),v in m.items() if o2==orb]
    if cand: return statistics.median(cand)*2
    return 3000.0
if __name__=='__main__':
    rec=load(); m,by=model(rec)
    print("fitted cells (slack,orbit) -> median seconds, n:")
    for k in sorted(m): print(f"  slack={k[0]:2d} orbit={k[1]} -> {m[k]:8.1f}s  (n={len(by[k])})")
