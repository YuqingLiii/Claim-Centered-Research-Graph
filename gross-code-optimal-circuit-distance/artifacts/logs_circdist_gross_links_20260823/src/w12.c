/* Independent enumeration of all weight-12 vectors in ker(H_X) of the gross code.
   (u,v) in F2^72 x F2^72 with A u = B v.  Two branches + two degenerate branches. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned __int128 u128;
#define NG 72
static u128 Acol[NG],Bcol[NG],solA[NG],solB[NG];
static u128 kerA[12],kerB[12];
static unsigned short sigA[NG],sigB[NG];   /* 12-bit im-membership signature */
static u128 lnA[12],lnB[12];
static u128 cosA[4096],cosB[4096];
static FILE*out;
static int pc(u128 x){ return __builtin_popcountll((unsigned long long)x)+
                              __builtin_popcountll((unsigned long long)(x>>64)); }
static u128 ap(const u128*cols,u128 u){ u128 r=0; while(u){ int p=__builtin_ctzll((unsigned long long)u)
     ; if(!(unsigned long long)u){ p=64+__builtin_ctzll((unsigned long long)(u>>64)); }
     r^=cols[p]; u&= u-1; } return r; }
static u128 rinv(const u128*sol,u128 s){ u128 r=0; while(s){ int p;
     unsigned long long lo=(unsigned long long)s;
     if(lo) p=__builtin_ctzll(lo); else p=64+__builtin_ctzll((unsigned long long)(s>>64));
     r^=sol[p]; s&= s-1; } return r; }
static unsigned sigof(const unsigned short*sg,u128 u){ unsigned r=0; while(u){ int p;
     unsigned long long lo=(unsigned long long)u;
     if(lo) p=__builtin_ctzll(lo); else p=64+__builtin_ctzll((unsigned long long)(u>>64));
     r^=sg[p]; u&= u-1;} return r; }
static long long nfound=0;
static void emit(u128 u,u128 v){
  fprintf(out,"%llx %llx %llx %llx\n",(unsigned long long)u,(unsigned long long)(u>>64),
          (unsigned long long)v,(unsigned long long)(v>>64)); nfound++;
}
/* enumerate first-half vectors of weight a with lex-min support = 0 */
static int WA;                    /* weight of first half */
static const u128 *C1,*S2; static const unsigned short *SG1; static const u128 *COS2;
static int flip;                  /* 0: (u,v) 1: (v,u) */
static int pos[8];
static void rec(int depth,int start,u128 uacc,unsigned sacc){
  if(depth==WA){
    if(sacc) return;
    u128 s=uacc? ap(C1,uacc):0;
    u128 v0=rinv(S2,s);
    int need=12-WA;
    for(int i=0;i<4096;i++){ u128 v=v0^COS2[i]; if(pc(v)==need){ if(!flip) emit(uacc,v); else emit(v,uacc);} }
    return;
  }
  for(int p=start;p<NG;p++){
    rec(depth+1,p+1,uacc|((u128)1<<p),sacc^SG1[p]);
  }
}
int main(int argc,char**argv){
  FILE*f=fopen(argv[1],"r"); char tag[32]; unsigned long long lo,hi; int i;
  #define RD(arr,n) for(i=0;i<n;i++){ if(fscanf(f,"%llx %llx",&lo,&hi)!=2){fprintf(stderr,"read err\n");return 1;} arr[i]=((u128)hi<<64)|lo; }
  RD(Acol,NG) RD(Bcol,NG) RD(solA,NG) RD(solB,NG) RD(kerA,12) RD(kerB,12) RD(lnA,12) RD(lnB,12)
  fclose(f);
  (void)tag;
  /* signatures: sigA[p] = 12 bits <lnB_j , Acol[p]> ; membership of A u in im(B) */
  for(int p=0;p<NG;p++){ unsigned s=0; for(int j=0;j<12;j++) if(pc(lnB[j]&Acol[p])&1) s|=1u<<j; sigA[p]=s; }
  for(int p=0;p<NG;p++){ unsigned s=0; for(int j=0;j<12;j++) if(pc(lnA[j]&Bcol[p])&1) s|=1u<<j; sigB[p]=s; }
  for(int m=0;m<4096;m++){ u128 a=0,b=0; for(int j=0;j<12;j++) if(m>>j&1){a^=kerA[j];b^=kerB[j];} cosA[m]=a;cosB[m]=b; }
  out=fopen(argv[2],"w");
  /* degenerate: u=0 -> v in ker(B), |v|=12 ; v=0 -> u in ker(A), |u|=12 */
  for(int m=1;m<4096;m++){ if(pc(cosB[m])==12) emit(0,cosB[m]); }
  for(int m=1;m<4096;m++){ if(pc(cosA[m])==12) emit(cosA[m],0); }
  /* branch 1: |u|=1..6, lexmin(u)=0 */
  flip=0; C1=Acol; S2=solB; SG1=sigA; COS2=cosB;
  for(WA=1;WA<=6;WA++){ rec(1,1,(u128)1,sigA[0]); fprintf(stderr,"branch1 w=%d cum=%lld\n",WA,nfound); }
  /* branch 2: |v|=1..5, lexmin(v)=0 */
  flip=1; C1=Bcol; S2=solA; SG1=sigB; COS2=cosA;
  for(WA=1;WA<=5;WA++){ rec(1,1,(u128)1,sigB[0]); fprintf(stderr,"branch2 w=%d cum=%lld\n",WA,nfound); }
  fclose(out); fprintf(stderr,"raw emitted %lld\n",nfound); return 0;
}
