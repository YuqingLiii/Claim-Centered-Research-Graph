"""Re-derive Figure 12's edge labels from the PDF vector coordinates, rigorously:
match each drawn digit to the nearest incident edge of its cell's check."""
import re, math
import pdfparse
MAP={'!':2,'"':3,'#':4,'$':1,'%':5,'&':6,"'":7}
s=open("xobj_Im12.txt",encoding="latin-1").read()
pat=re.compile(r"q ([\d.eE+-]+) 0 0 ([\d.eE+-]+) ([\d.eE+-]+) ([\d.eE+-]+)\s*\n?cm\s*\n?BT [\d.eE+-]+ 0 0 [\d.eE+-]+ 0 ([\d.eE+-]+) Tm /TT\d 1 Tf \((.*?)\) Tj ET Q", re.S)
labels=[]
for m in pat.finditer(s):
    sx,sy,tx,ty,tmy,ch=m.groups()
    if ch in MAP:
        labels.append((float(tx), float(ty)+float(sy)*float(tmy), MAP[ch]))
o=pdfparse.parse(s)
small=[r for r in o if r['op'] in ('f','f*') and 5<r['w']<12 and 5<r['h']<12]
checks=[r for r in small if r['n']<=5]
circles=[r for r in small if r['n']>5]
print("checks:",len(checks)," circles:",len(circles)," labels:",len(labels))
EDGE=[('e1',33.5,47.9),('e2',0.0,21.4),('e3',-27.3,0.0),('e4',26.7,0.0),
      ('e5',0.0,-26.6),('e6',-48.0,-27.3)]
for chk in sorted(checks,key=lambda c:(-c['cy'],c['cx'])):
    cx,cy=chk['cx'],chk['cy']
    panel = 'UPPER' if cy>130 else 'LOWER'
    col = tuple(round(v,2) for v in chk['fill'])
    # its 6 incident data qubits (nearest circle to each ideal edge endpoint)
    nb={}
    for (e,dx,dy) in EDGE:
        best=min(circles,key=lambda r:(r['cx']-(cx+dx))**2+(r['cy']-(cy+dy))**2)
        d=math.hypot(best['cx']-(cx+dx),best['cy']-(cy+dy))
        nb[e]=(best,d)
    # each label -> nearest qubit of this cell (only labels within the cell's x-window)
    res={}
    for (lx,ly,val) in labels:
        cand=[(math.hypot(lx-nb[e][0]['cx'], ly-nb[e][0]['cy']),e) for (e,_,_) in EDGE]
        d,e=min(cand)
        if d<20 and abs(lx-cx)<80 and ((ly>130)==(cy>130)):
            res.setdefault(e,[]).append((round(d,1),val))
    print(f"check ({cx:6.1f},{cy:6.1f}) {panel} fill={col}")
    for (e,_,_) in EDGE:
        q,dq=nb[e]
        half='white' if q['fill'][0]>0.5 else 'black'
        print(f"    {e}: qubit ({q['cx']:6.1f},{q['cy']:6.1f}) {half} fit={dq:4.1f}  label(s) {res.get(e)}")
