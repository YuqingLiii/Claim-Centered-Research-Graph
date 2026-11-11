"""Minimal independent PDF text extractor: xref-free brute scan of objects,
FlateDecode, ToUnicode CMap per font, Tj/TJ decoding."""
import re, zlib, sys, collections

data = open(sys.argv[1],'rb').read()

# ---- collect all indirect objects by brute scan
objs = {}
for m in re.finditer(rb'(\d+)\s+(\d+)\s+obj\b', data):
    num = int(m.group(1)); gen=int(m.group(2))
    start = m.end()
    e = data.find(b'endobj', start)
    objs[(num,gen)] = data[start:e]

def getstream(body):
    m = re.search(rb'stream\r?\n', body)
    if not m: return None
    s = m.end(); e = body.rfind(b'endstream')
    raw = body[s:e]
    if b'/FlateDecode' in body[:m.start()]:
        try: return zlib.decompress(raw)
        except Exception:
            try: return zlib.decompressobj().decompress(raw)
            except Exception: return None
    return raw

def resolve(ref):
    m = re.match(rb'(\d+)\s+(\d+)\s+R', ref.strip())
    if m: return objs.get((int(m.group(1)),int(m.group(2))))
    return None

# ---- ToUnicode maps
def parse_tounicode(s):
    mp={}
    for blk in re.findall(rb'beginbfchar(.*?)endbfchar', s, re.S):
        for a,b in re.findall(rb'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', blk):
            mp[int(a,16)] = ''.join(chr(int(b[i:i+4],16)) for i in range(0,len(b),4))
    for blk in re.findall(rb'beginbfrange(.*?)endbfrange', s, re.S):
        for a,b,c in re.findall(rb'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', blk):
            lo,hi,st=int(a,16),int(b,16),int(c,16)
            for i,cd in enumerate(range(lo,hi+1)): mp[cd]=chr(st+i)
    return mp

fontmaps={}
for k,body in objs.items():
    if b'/Type' in body and b'/Font' in body:
        m = re.search(rb'/ToUnicode\s+(\d+\s+\d+\s+R)', body)
        nm = re.search(rb'/BaseFont\s*/([^\s/\]>]+)', body)
        if m:
            tb = resolve(m.group(1))
            if tb is not None:
                st = getstream(tb)
                if st: fontmaps[k]=(nm.group(1).decode() if nm else '?', parse_tounicode(st))

# name->map per page resources is complex; build a global fallback keyed by font object
# Instead: for each page, map /F name -> font obj
pages=[]
for k,body in objs.items():
    if re.search(rb'/Type\s*/Page\b', body):
        pages.append((k,body))

def page_fonts(body):
    res = re.search(rb'/Resources\s+(\d+\s+\d+\s+R)', body)
    rbody = resolve(res.group(1)) if res else body
    if rbody is None: rbody=body
    fm={}
    fo = re.search(rb'/Font\s*<<(.*?)>>', rbody, re.S)
    if not fo:
        fr = re.search(rb'/Font\s+(\d+\s+\d+\s+R)', rbody)
        if fr:
            fb=resolve(fr.group(1))
            if fb: fo=re.search(rb'<<(.*?)>>', fb, re.S)
    if fo:
        for nm,ref in re.findall(rb'/([^\s/]+)\s+(\d+\s+\d+\s+R)', fo.group(1)):
            m2=re.match(rb'(\d+)\s+(\d+)\s+R',ref)
            fm[nm.decode()]=(int(m2.group(1)),int(m2.group(2)))
    return fm

def page_content(body):
    c = re.search(rb'/Contents\s+(\d+\s+\d+\s+R)', body)
    out=b''
    if c:
        cb=resolve(c.group(1))
        if cb is not None:
            st=getstream(cb)
            if st: out=st
            else:
                # array of refs
                pass
    else:
        c = re.search(rb'/Contents\s*\[(.*?)\]', body, re.S)
        if c:
            for ref in re.findall(rb'\d+\s+\d+\s+R', c.group(1)):
                cb=resolve(ref)
                if cb is not None:
                    st=getstream(cb)
                    if st: out+=st+b'\n'
    return out

def decode_text(content, fonts):
    cur=None; out=[]
    toks = re.finditer(rb'/([^\s/\[\]<>()]+)\s+[\d.]+\s+Tf|\((?:\\.|[^)\\])*\)\s*Tj|\[(?:[^\]\\]|\\.)*\]\s*TJ|<([0-9A-Fa-f\s]+)>\s*Tj|TD|Td|T\*|ET', content, re.S)
    def emit(s): out.append(s)
    for t in toks:
        s=t.group(0)
        if s.endswith(b'Tf'):
            nm=t.group(1).decode(); cur=fonts.get(nm)
        elif s.endswith(b'Tj') or s.endswith(b'TJ'):
            mp = fontmaps.get(cur,('',{}))[1] if cur else {}
            if s.startswith(b'<'):
                hx=re.sub(rb'\s',b'',t.group(2))
                codes=[int(hx[i:i+4],16) for i in range(0,len(hx),4)] if mp and max(mp)>255 else [int(hx[i:i+2],16) for i in range(0,len(hx),2)]
                emit(''.join(mp.get(c,'') for c in codes))
            else:
                for lit in re.findall(rb'\((?:\\.|[^)\\])*\)', s):
                    body2=lit[1:-1]
                    def _unesc(mm):
                        g=mm.group(1)
                        if g in b'()\\': return bytes([g[0]])
                        if g.isdigit(): return bytes([int(g,8)&0xFF])
                        return {b'n':b'\n',b'r':b'\r',b't':b'\t',b'b':b'\b',b'f':b'\f'}.get(g,g)
                    body2=re.sub(rb'\\([0-7]{1,3}|.)', _unesc, body2, flags=re.S)
                    if mp:
                        emit(''.join(mp.get(c,chr(c)) for c in body2))
                    else:
                        emit(body2.decode('latin-1'))
                if s.endswith(b'TJ'):
                    pass
        elif s in (b'TD',b'Td',b'T*'):
            emit(' ')
        elif s==b'ET': emit('\n')
    return ''.join(out)

allout=[]
for i,(k,body) in enumerate(pages):
    fonts=page_fonts(body)
    c=page_content(body)
    allout.append(decode_text(c,fonts))
sys.stdout.write('\n\n=== PAGEBREAK ===\n\n'.join(allout))
