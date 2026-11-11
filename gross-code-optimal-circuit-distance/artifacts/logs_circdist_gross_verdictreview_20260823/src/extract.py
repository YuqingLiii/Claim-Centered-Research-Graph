import re, sys, os, pathlib
md = pathlib.Path(sys.argv[1]).read_text()
outdir = pathlib.Path(sys.argv[2]); outdir.mkdir(parents=True, exist_ok=True)
lines = md.split('\n')
# find headings of form ####? `name.py` followed by a ```python block
cur = None; blocks = {}
i = 0
while i < len(lines):
    L = lines[i]
    m = re.match(r'^#{2,6}\s+.*?`([A-Za-z0-9_]+\.py)`', L)
    if m: cur = m.group(1)
    if L.strip().startswith('```python'):
        j = i+1; buf=[]
        while j < len(lines) and not lines[j].strip() == '```':
            buf.append(lines[j]); j += 1
        if cur and cur not in blocks:
            blocks[cur] = '\n'.join(buf)
        i = j
    i += 1
for k,v in blocks.items():
    (outdir/k).write_text(v+'\n')
    print(k, len(v.split('\n')))
