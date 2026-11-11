"""Render the per-cell result table from ALL sweep logs (predecessor's + this session's)."""
import json, collections, sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cert4
HERE=os.path.dirname(os.path.abspath(__file__))
ENC={'full.jsonl':'cert4','t2.jsonl':'cert4','b6.jsonl':'cert6','bench.jsonl':'cert4',
     'full7.jsonl':'cert7','full7b.jsonl':'cert7','final.jsonl':'cert7','mine.jsonl':'cert7'}
CAND=[('Z',(1,2,62)),('X',(14,0,2))]
rs=[]
for L in sorted(glob.glob(os.path.join(HERE,'logs','*.jsonl'))):
    b=os.path.basename(L)
    if b not in ENC: continue
    for l in open(L):
        try: r=json.loads(l)
        except: continue
        if (r.get('verdict') in ('SAT','UNSAT') and r.get('orbit',-1)>=0
                and (r.get('sector'),tuple(r.get('triple',[]))) in CAND):
            r['enc']=ENC[b]; r['src']=b; rs.append(r)
cells=cert4.cells(10)
by=collections.defaultdict(dict)
for r in rs:
    key=(r['sector'],tuple(r['triple'])); k=(r['K'],r['Ew'],r['orbit'])
    if k in by[key] and by[key][k]['seconds']<=r['seconds']: continue
    by[key][k]=r
summary={}
for key in CAND:
    sec,tr=key; tab=by.get(key,{})
    print(f"\n**sector {sec}, triple {tr}** — `U` = UNSAT, `S` = SAT, `.` = not decided\n")
    print("| `K` | `\\|E\\|` | orbit 0..8 | cell verdict | encoding | cell CPU s | slowest orbit s |")
    print("|---|---|---|---|---|---|---|")
    tot=0.0; ndone=0; nsat=0; newly=0
    for (K,Ew) in cells:
        row=[];sats=[];times=[];encs=set();srcs=set()
        for j in range(9):
            r=tab.get((K,Ew,j))
            if r is None: row.append('.')
            else:
                row.append('U' if r['verdict']=='UNSAT' else 'S')
                times.append(r['seconds']); encs.add(r['enc']); srcs.add(r['src'])
                if r['verdict']=='SAT': sats.append(j)
        done=all(x!='.' for x in row)
        if Ew==12:
            v='SAT' if sats else '**UNSAT** (enum12)'; done=True
        else:
            v='SAT' if sats else ('**UNSAT**' if done else 'incomplete')
        mark=' †' if (done and Ew!=12 and ({'final.jsonl','mine.jsonl'} & srcs)) else ''
        if mark: newly+=1
        ndone+=int(done); nsat+=int(bool(sats)); tot+=sum(times)
        print(f"| {K} | {Ew} | `{''.join(row)}` | {v}{mark} | {'+'.join(sorted(encs)) or '-'} | "
              f"{sum(times):.0f} | {max(times) if times else 0:.0f} |")
    print(f"\n`{ndone}` of `{len(cells)}` cells decided; SAT cells: `{nsat}`; "
          f"CPU for this sector: `{tot:.0f}` s; cells closed after the predecessor's artifact (†): `{newly}`")
    summary[sec]=(ndone,nsat,tot,newly)
print("\nTOTAL:",summary," grand CPU",round(sum(v[2] for v in summary.values())))
print("decided cells overall:", sum(v[0] for v in summary.values()), "/ 110; SAT cells:", sum(v[1] for v in summary.values()))
