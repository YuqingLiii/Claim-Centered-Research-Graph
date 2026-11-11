"""Minimal PDF content-stream parser: filled/stroked path bounding boxes with fill colour,
in the form XObject's own coordinate system."""
import re

def parse(stream):
    toks = re.findall(r"\[[^\]]*\]|\((?:\\.|[^)\\])*\)|/[^\s/\[\]()<>]+|<<|>>|[^\s\[\]<>]+", stream)
    ctm = [1,0,0,1,0,0]; stack=[]
    fill=(0,0,0); strk=(0,0,0)
    args=[]; pts=[]; out=[]
    def ap(m,x,y): return (m[0]*x+m[2]*y+m[4], m[1]*x+m[3]*y+m[5])
    def num(t):
        try: return float(t)
        except: return None
    for t in toks:
        v=num(t)
        if v is not None:
            args.append(v); continue
        if t=='q': stack.append((ctm[:],fill,strk))
        elif t=='Q':
            if stack: ctm,fill,strk = stack.pop(); ctm=ctm[:]
        elif t=='cm' and len(args)>=6:
            a,b,c,d,e,f=args[-6:]
            m=ctm
            ctm=[a*m[0]+b*m[2], a*m[1]+b*m[3], c*m[0]+d*m[2], c*m[1]+d*m[3],
                 e*m[0]+f*m[2]+m[4], e*m[1]+f*m[3]+m[5]]
        elif t=='sc' or t=='scn':
            if len(args)>=3: fill=tuple(args[-3:])
            elif len(args)>=1: fill=(args[-1],)*3
        elif t=='SC' or t=='SCN':
            if len(args)>=3: strk=tuple(args[-3:])
            elif len(args)>=1: strk=(args[-1],)*3
        elif t=='g': fill=(args[-1],)*3 if args else fill
        elif t=='rg' and len(args)>=3: fill=tuple(args[-3:])
        elif t in ('m','l') and len(args)>=2:
            pts.append(ap(ctm,args[-2],args[-1]))
        elif t=='c' and len(args)>=6:
            for i in (0,2,4): pts.append(ap(ctm,args[-6+i],args[-6+i+1]))
        elif t=='v' or t=='y':
            if len(args)>=4:
                for i in (0,2): pts.append(ap(ctm,args[-4+i],args[-4+i+1]))
        elif t=='re' and len(args)>=4:
            x,y,w,h=args[-4:]
            for (a,b) in ((x,y),(x+w,y),(x+w,y+h),(x,y+h)): pts.append(ap(ctm,a,b))
        elif t in ('f','f*','F','B','B*','b','b*','S','s','n'):
            if pts:
                xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
                out.append(dict(op=t, fill=fill, stroke=strk,
                                cx=(min(xs)+max(xs))/2, cy=(min(ys)+max(ys))/2,
                                w=max(xs)-min(xs), h=max(ys)-min(ys), n=len(pts),
                                pts=pts if t in ('S','s') else None))
            pts=[]
        if t not in (): args=[]
    return out
