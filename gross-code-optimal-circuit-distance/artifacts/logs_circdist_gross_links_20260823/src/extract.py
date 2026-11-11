import re,sys,os
ART='<repo>/artifacts/'
SRC={'circdist_gross_sbbcert_20260820.md':['gross.py','sched.py','cascade.py','pool.py','dext.py','dext2.py','cert.py'],
     'circdist_gross_candidate_unsat_20260822.md':['cert4.py','cert6.py','cert7.py'],
     'circdist_gross_verdict_20260823.md':['rebuild.py','w11.py']}
for md,names in SRC.items():
    t=open(ART+md).read().split('\n')
    i=0
    while i<len(t):
        m=re.match(r'^#### `([a-z0-9_]+\.py)`',t[i])
        if m and m.group(1) in names:
            j=i+1
            while j<len(t) and not t[j].startswith('```'): j+=1
            k=j+1; buf=[]
            while k<len(t) and not t[k].startswith('```'): buf.append(t[k]); k+=1
            open('gen/'+m.group(1),'w').write('\n'.join(buf)+'\n')
            print("extracted",m.group(1),len(buf),"lines")
            i=k
        i+=1
