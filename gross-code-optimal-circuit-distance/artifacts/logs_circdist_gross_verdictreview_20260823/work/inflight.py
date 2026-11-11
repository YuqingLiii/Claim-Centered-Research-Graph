import subprocess, json, os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
def inflight():
    out = subprocess.run(['ps','-eo','args'], capture_output=True, text=True).stdout
    jobs=set()
    for line in out.split("\n"):
        if 'job7.py' in line or 'job4.py' in line:
            parts=line.split()
            try:
                i=[k for k,p in enumerate(parts) if p.endswith('job7.py') or p.endswith('job4.py')][0]
                sec=parts[i+1]; tri=parts[i+2]; W=int(parts[i+3]); K=int(parts[i+4]); Ew=int(parts[i+5]); orb=int(parts[i+6])
                jobs.add((sec,tri,K,Ew,orb))
            except Exception: pass
    return jobs
if __name__=='__main__':
    j=inflight()
    print(len(j),"in flight")
    for x in sorted(j): print(x)
