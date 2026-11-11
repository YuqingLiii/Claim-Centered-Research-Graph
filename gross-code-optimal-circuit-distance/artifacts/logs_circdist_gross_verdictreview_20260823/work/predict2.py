"""Predict the cost of each OPEN sub-query from the decided sub-queries of its own cell.
Within a cell, cost falls steeply with orbit index; the ratio orbit_j / orbit_8 is fairly
stable across cells, so we fit a per-orbit multiplier and apply it to each open cell's own
decided orbits."""
import json,os,glob,sys,collections,statistics
sys.path.insert(0,"/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad/work2")
import cert4
SC="/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad"
R="<home>/Documents/Codex/2026-08-07/i-have-connected-an-old-windows/outputs/Windows-SSD-Recovery-2026-08-07/Research-Projects/discovery-new-algorithms/artifacts/logs_circdist_gross_drivers_20260823"
CAND={'Z':(1,2,62),'X':(14,0,2)}
lines={}
for D in (R, SC+"/work/logs", SC+"/work2/logs"):
    for L in sorted(glob.glob(os.path.join(D,'*.jsonl'))):
        for ln in open(L):
            ln=ln.strip()
            if ln: lines[(os.path.basename(L),ln)]=ln
u={}
for ln in lines.values():
    try: r=json.loads(ln)
    except: continue
    if r.get('verdict') not in ('SAT','UNSAT') or 'triple' not in r: continue
    if r.get('W')!=10 or tuple(r['triple'])!=CAND.get(r['sector']) or r.get('orbit',-1)<0: continue
    k=(r['sector'],r['K'],r['Ew'],r['orbit'])
    if k not in u or u[k]['seconds']>r['seconds']: u[k]=r
# per-orbit multiplier relative to the cell's orbit-2 time (orbit 2 is always decided)
ratios=collections.defaultdict(list)
cells=cert4.cells(10)
for sec in ('Z','X'):
    for (K,Ew) in cells:
        base=u.get((sec,K,Ew,2))
        if not base or base['seconds']<5: continue
        for o in range(9):
            r=u.get((sec,K,Ew,o))
            if r: ratios[o].append(r['seconds']/base['seconds'])
print("per-orbit cost multiplier, relative to the same cell's orbit-2 time")
print("(median over cells where orbit 2 took >5 s; n = number of cells)")
print()
mult={}
for o in range(9):
    if ratios[o]:
        mult[o]=statistics.median(ratios[o])
        print(f"   orbit {o}: median x{mult[o]:7.2f}   (n={len(ratios[o])})")
print()
# open list
op=[]
for sec in ('Z','X'):
    for (K,Ew) in cells:
        have={o for o in range(9) if (sec,K,Ew,o) in u}
        if Ew==12 and len(have)<9: continue
        for o in sorted(set(range(9))-have): op.append((sec,K,Ew,o))
print(f"predicted solver cost of each of the {len(op)} OPEN sub-queries")
print("(from its OWN cell's orbit-2 time x the multiplier above)")
print()
tot=0; rows=[]
for (sec,K,Ew,o) in op:
    b=u.get((sec,K,Ew,2))
    if not b: rows.append((sec,K,Ew,o,None)); continue
    est=b['seconds']*mult.get(o,1.0)
    tot+=est; rows.append((sec,K,Ew,o,est))
for sec,K,Ew,o,est in rows:
    b=u.get((sec,K,Ew,2))
    print(f"   {sec} ({K:2d},{Ew:2d}) orbit {o}   cell orbit-2 = {b['seconds']:8.1f} s"
          f"   -> predicted {est:9.1f} s" if est else f"   {sec} ({K},{Ew}) orbit {o}   no basis")
print()
print(f"predicted TOTAL solver time to finish the frontier: {tot:.0f} s  = {tot/3600:.1f} CPU-hours")
print(f"on 24 free cores that is ~{tot/3600/24*1.3:.1f} h wall (30% scheduling overhead);")
print(f"at the ~0.5 core a worker gets on the machine as it stands, ~{tot/3600/ (0.5*8):.1f} h with 8 workers.")
