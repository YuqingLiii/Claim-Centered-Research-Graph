"""Apply the d_eff<=10 disqualifier to the stage-1 gap candidates + measure how many
legal+(MC) TI schedules survive it at all."""
import itertools, random, sys, json, time, collections
from lift import Schedule, Sector
import gross as G, hunt as H
NG = G.NG; CSSG = G.CSSG
rng = random.Random(20260823)
t0=time.time()
PX, PZ = H.pools()
pidxX = H.pair_index(PX); pidxZ = H.pair_index(PZ)
tidxX = H.triple_index(PX); tidxZ = H.triple_index(PZ)
print("index build %.0fs" % (time.time()-t0))

N = int(sys.argv[1]) if len(sys.argv)>1 else 2000
seen=set(); rows=[]; nti=0; draws=0
surv=0; gapc=[]
while nti < N and draws < N*200:
    draws+=1
    perm=list(range(12)); rng.shuffle(perm)
    key=(tuple(perm[0:3]),tuple(perm[3:6]),tuple(perm[6:9]),tuple(perm[9:12]))
    if key in seen or not H.ti_ok(*key): continue
    seen.add(key); nti+=1
    s=H.sched_TI(*key)
    rec={'key':key}
    alive=True
    for lab,mir,pidx,tidx in (('Z',False,pidxX,tidxX),('X',True,pidxZ,tidxZ)):
        sec=Sector(CSSG,s,mirror=mir)
        bad,why=H.dext_le10(sec,pidx,tidx)
        rec[lab+'_dext_le10']=bad
        if not bad:
            n0,nt,kinds=H.decide_rate(sec,pidx,[0])
            rec[lab+'_rate']=(n0,nt)
            rec[lab+'_kinds']={k:v for k,v in kinds.items() if v}
    if (not rec['Z_dext_le10']) or (not rec['X_dext_le10']):
        surv+=1
        if (('Z_rate' in rec and rec['Z_rate'][0]==0) or ('X_rate' in rec and rec['X_rate'][0]==0)):
            gapc.append(rec)
    rows.append(rec)
print("TI legal+(MC) sampled: %d (from %d draws)" % (nti,draws))
print("  sector-Z d_eff<=10 disqualified: %d ; sector-X: %d"
      % (sum(1 for r in rows if r['Z_dext_le10']), sum(1 for r in rows if r['X_dext_le10'])))
print("  schedules with at least one sector surviving the d_eff<=10 filter: %d" % surv)
print("  of those, sectors with repair-0 RATE 0 (STAGE-1 GAP CANDIDATES): %d" % len(gapc))
for r in gapc[:12]: print("   ",r)
json.dump([{k:(list(v) if isinstance(v,tuple) else v) for k,v in r.items()} for r in rows],
          open('filt_log.json','w'))
print("elapsed %.0fs" % (time.time()-t0))
