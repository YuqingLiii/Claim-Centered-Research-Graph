import re, sys, os, hashlib
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
got = {}
for md in sys.argv[2:]:
    txt = open(md).read()
    lines = txt.split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r'^#### `([A-Za-z0-9_]+\.py)`\s*$', lines[i])
        if m:
            name = m.group(1)
            j = i+1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            if j < len(lines) and lines[j].strip().startswith('```'):
                fence = lines[j].strip()
                k = j+1
                body = []
                while k < len(lines) and lines[k].strip() != '```':
                    body.append(lines[k]); k += 1
                src = "\n".join(body) + "\n"
                if name in got:
                    print(f"DUP {name} from {os.path.basename(md)}: identical={got[name]==src}")
                else:
                    got[name] = src
                    open(os.path.join(OUT, name), 'w').write(src)
                    print(f"{name:18s} {len(body):5d} lines  sha256={hashlib.sha256(src.encode()).hexdigest()[:16]}  <- {os.path.basename(md)}")
                i = k
        i += 1
print("total", len(got))
