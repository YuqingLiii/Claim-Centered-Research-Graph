"""Every TIMEOUT the inherited drivers recorded, against what is now known about that sub-query."""
import json,glob,os,re,ast,statistics,sys
SC="/private/tmp/claude-508/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad"
R="<home>/Documents/Codex/2026-08-07/i-have-connected-an-old-windows/outputs/Windows-SSD-Recovery-2026-08-07/Research-Projects/discovery-new-algorithms/artifacts/logs_circdist_gross_drivers_20260823"
CAND={'Z':(1,2,62),'X':(14,0,2)}
tmo=[]
for f in glob.glob(os.path.join(SC,"work","logs","*.out")):
    for ln in open(f, errors='ignore'):
        m=re.search(r"\[\s*\d+/\d+\]\s*(\[[^\]]*\])\s*->\s*TIMEOUT\s*([\d.]+)s", ln)
        if m:
            a=ast.literal_eval(m.group(1))
            tmo.append(((a[0],a[3],a[4],a[5]), float(m.group(2)), os.path.basename(f)))
u={}
for D in (R,SC+"/work/logs",SC+"/work2/logs"):
    for L in glob.glob(os.path.join(D,'*.jsonl')):
        for ln in open(L):
            try: r=json.loads(ln)
            except: continue
            if r.get('verdict') not in ('SAT','UNSAT') or 'triple' not in r: continue
            if r.get('W')!=10 or tuple(r['triple'])!=CAND.get(r['sector']): continue
            k=(r['sector'],r['K'],r['Ew'],r.get('orbit'))
            if k not in u or u[k]['seconds']>r['seconds']: u[k]=r
seen=set(); rows=[]
for k,w,src in sorted(tmo):
    if k in seen: continue
    seen.add(k)
    r=u.get(k)
    rows.append((k,w,r))
print("| sub-query | recorded by the inherited driver | actually |")
print("|---|---|---|")
solved=0
for (sec,K,Ew,o),w,r in rows:
    if r:
        solved+=1
        note=f"**UNSAT in {r['seconds']} s** ({r.get('solver','cd15')}) — **{w/r['seconds']:.0f}× less than the wall it was given**"
    else:
        note="still open"
    print(f"| `{sec} ({K},{Ew}) orbit {o}` | TIMEOUT after {w:.0f} s wall | {note} |")
print()
print(f"{len(rows)} distinct sub-queries carry a TIMEOUT record; {solved} of them have since been decided.")
