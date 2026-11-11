"""Figure-12 label data (pixel-verified in wave 13; taken as given) + check geometry."""
from gr import *
E=['e1','e2','e3','e4','e5','e6']
TYPE={'e1':'D','e6':'D','e2':'V','e5':'V','e3':'H','e4':'H'}
# labels[panel][colour][edge] = drawn time label ; blocks = the two contiguous 3-blocks
LAB={
 'upper':{'blue':{'e6':2,'e2':3,'e5':4,'e3':5,'e1':6,'e4':7},
          'red' :{'e5':1,'e6':2,'e2':3,'e1':4,'e4':5,'e3':6},
          'green':{'e5':1,'e6':2,'e2':3,'e3':4,'e1':5,'e4':6}},
 'lower':{'blue':{'e2':2,'e1':3,'e5':4,'e6':5,'e3':6,'e4':7},
          'red' :{'e5':1,'e2':2,'e1':3,'e6':4,'e3':5,'e4':6},
          'green':{'e5':1,'e2':2,'e1':3,'e3':4,'e4':5,'e6':6}},
}
def blocks(panel,colour):
    d=LAB[panel][colour]; o=sorted(d,key=lambda e:d[e]); return o[:3],o[3:]
# check-support geometry
def xslots(g): return [gadd(g,m) for m in Amon]+[NG+gadd(g,m) for m in Bmon]
def zslots(g): return [gadd(g,(-m[0],-m[1])) for m in Bmon]+[NG+gadd(g,(-m[0],-m[1])) for m in Amon]
# overlapping X/Z check pairs, with the shared (slotX,slotZ) coordinates
def overlaps():
    zof={}
    for g in range(NG):
        for s,q in enumerate(zslots(g)): zof.setdefault(q,[]).append((g,s))
    out=[]
    for gx in range(NG):
        acc={}
        for sx,q in enumerate(xslots(gx)):
            for (gz,sz) in zof.get(q,[]): acc.setdefault(gz,[]).append((sx,sz))
        for gz,lst in acc.items(): out.append((gx,gz,lst))
    return out
if __name__=='__main__':
    for p in ('upper','lower'):
        for c in ('blue','red','green'):
            b1,b2=blocks(p,c)
            print(p,c,'block1',[ (e,TYPE[e]) for e in b1],'block2',[(e,TYPE[e]) for e in b2])
    ov=overlaps()
    from collections import Counter
    print('X/Z pairs by overlap size:',Counter(len(l) for _,_,l in ov),
          ' non-overlapping pairs:',NG*NG-len(ov))
