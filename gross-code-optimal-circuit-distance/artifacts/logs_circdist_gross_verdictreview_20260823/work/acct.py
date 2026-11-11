import json, collections, os, sys, glob
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import cert4
HERE=os.path.dirname(os.path.abspath(__file__))
LOGS=sorted(glob.glob(os.path.join(HERE,'logs','*.jsonl')))
CAND={('Z',(1,2,62)),('X',(14,0,2))}
rec={}   # (sec,K,Ew,orb) -> record
nsat=[]
for L in LOGS:
    for l in open(L):
        try: r=json.loads(l)
        except: continue
        if r.get('verdict') not in ('SAT','UNSAT'): continue
        if r.get('orbit',-1)<0: continue
        key=(r['sector'],tuple(r['triple']))
        if key not in CAND: continue
        k=(r['sector'],r['K'],r['Ew'],r['orbit'])
        if r['verdict']=='SAT': nsat.append((k,L,r))
        if k not in rec or rec[k]['seconds']>r['seconds']: rec[k]=r
cells=cert4.cells(10)
print("logs:", [os.path.basename(x) for x in LOGS])
print("total decided orbit sub-queries on candidate:", len(rec), " SAT:", len(nsat))
tot=0
for sec in ('Z','X'):
    op=[];nj=0;ndone=0
    for (K,Ew) in cells:
        if Ew==12:   # decided completely by enum12
            ndone+=1; continue
        have={o for o in range(9) if (sec,K,Ew,o) in rec}
        if len(have)==9: ndone+=1
        else:
            m=9-len(have); op.append(f"({K},{Ew})x{m}"); nj+=m
    print(f"\n{sec}: {ndone}/{len(cells)} cells decided; {len(op)} cells open, {nj} orbit sub-queries open")
    print("   " + " ".join(op))
    tot+=nj
print("\nTOTAL open orbit sub-queries:", tot)
