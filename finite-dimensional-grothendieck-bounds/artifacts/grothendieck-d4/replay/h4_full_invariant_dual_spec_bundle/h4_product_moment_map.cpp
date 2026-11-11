#include <bits/stdc++.h>
using namespace std;
static const int N=300,G=14400,R=54;
static uint16_t* PERM; static int8_t* SGN; static long long Cb[301][5];
struct Rep{int len; uint16_t v[2];};
struct MapCat{int a,b; long long n; int32_t* data; long long offset; string path;};
vector<MapCat> cats;
long long crank(const vector<int>&s){long long r=0;for(int j=0;j<(int)s.size();++j)r+=Cb[s[j]][j+1];return r;}
long long C(int n,int k){if(k<0||k>n)return 0;return Cb[n][k];}
long long encAnch(const vector<int>&X,const vector<int>&Y,int a,int b){
 if(a>0){if(X.empty()||X[0]!=0){cerr<<"no anchor x\n";exit(2);}vector<int>xr;for(int j=1;j<a;++j)xr.push_back(X[j]-1);return crank(xr)*C(300,b)+crank(Y);} 
 else {if(Y.empty()||Y[0]!=0){cerr<<"no anchor y\n";exit(2);}vector<int>yr;for(int j=1;j<b;++j)yr.push_back(Y[j]-1);return crank(yr);} }
MapCat& getcat(int a,int b){for(auto&c:cats)if(c.a==a&&c.b==b)return c;cerr<<"cat missing "<<a<<","<<b<<"\n";exit(2);}

pair<int,int> momentLookup(vector<int> supp,const vector<int>&to0fixed){
 sort(supp.begin(),supp.end()); int k=supp.size();
 if(k==0)return {0,1};
 if(k&1)return {-1,0};
 vector<int>X,Y; for(int v:supp){if(v<N)X.push_back(v);else Y.push_back(v-N);} int a=X.size(),b=Y.size();
 int anchor=(a>0?X[0]:Y[0]); int g=to0fixed[anchor]; size_t base=(size_t)g*N; int sg=1;
 for(int&i:X){sg*=SGN[base+i];i=PERM[base+i];}
 for(int&i:Y){sg*=SGN[base+i];i=PERM[base+i];}
 sort(X.begin(),X.end());sort(Y.begin(),Y.end());
 MapCat&c=getcat(a,b); long long idx=encAnch(X,Y,a,b); if(idx<0||idx>=c.n){cerr<<"idx range\n";exit(2);} int32_t code=c.data[idx]; if(code==0)return {-1,0}; int o=(code>0?1:-1); int lid=abs(code)-1; return {(int)(c.offset+lid),sg*o};
}

int main(int argc,char**argv){
 if(argc!=6){cerr<<"usage perm sign reps mapdir outprefix\n";return 1;} string pp=argv[1],sp=argv[2],rp=argv[3],md=argv[4],op=argv[5];
 Cb[0][0]=1;for(int n=1;n<=300;++n){Cb[n][0]=1;for(int k=1;k<=4;++k)Cb[n][k]=Cb[n-1][k]+Cb[n-1][k-1];}
 size_t psz=(size_t)G*N; PERM=(uint16_t*)malloc(psz*2);SGN=(int8_t*)malloc(psz);{ifstream f(pp,ios::binary);f.read((char*)PERM,psz*2);if(!f){cerr<<"perm read\n";return 2;}}{ifstream f(sp,ios::binary);f.read((char*)SGN,psz);if(!f){cerr<<"sign read\n";return 2;}}
 vector<int>to0fixed(N,-1);for(int g=0;g<G;++g)for(int i=0;i<N;++i)if(PERM[(size_t)g*N+i]==0&&to0fixed[i]<0)to0fixed[i]=g;for(int i=0;i<N;++i)if(to0fixed[i]<0){cerr<<"no to0\n";return 2;}
 Rep reps[R];{ifstream f(rp,ios::binary);for(int i=0;i<R;++i){unsigned char l;uint16_t a,b;f.read((char*)&l,1);f.read((char*)&a,2);f.read((char*)&b,2);reps[i].len=l;reps[i].v[0]=a;reps[i].v[1]=b;}if(!f){cerr<<"reps read\n";return 2;}}
 auto loadcat=[&](int a,int b,long long off){long long n=(a>0?C(299,a-1)*C(300,b):C(299,b-1));string p=md+"/moment_map_"+to_string(a)+"_"+to_string(b)+".i32";int32_t*d=(int32_t*)malloc(n*4);ifstream f(p,ios::binary);f.read((char*)d,n*4);if(!f){cerr<<"map read "<<p<<"\n";exit(2);}cats.push_back({a,b,n,d,off,p});};
 loadcat(2,0,1);loadcat(1,1,17);loadcat(0,2,39);loadcat(4,0,55);loadcat(3,1,47212);loadcat(2,2,234908);loadcat(1,3,517768);loadcat(0,4,705464);
 int npair=R*(R+1)/2; size_t total=(size_t)npair*G; string idf=op+".id.i32",sf=op+".sgn.i8",pf=op+".pairs.txt"; int32_t* IDs=(int32_t*)malloc(total*4);int8_t* SS=(int8_t*)malloc(total);ofstream pairs(pf);int pidx=0; long long zero=0;
 for(int i=0;i<R;++i){for(int j=i;j<R;++j){pairs<<pidx<<" "<<i<<" "<<j<<"\n"; for(int g=0;g<G;++g){vector<int>s;for(int t=0;t<reps[i].len;++t)s.push_back(reps[i].v[t]);size_t base=(size_t)g*N;int ag=1;for(int t=0;t<reps[j].len;++t){int v=reps[j].v[t];int line=(v<N?v:v-N);int nv=(v<N?PERM[base+line]:N+PERM[base+line]);ag*=SGN[base+line];auto it=find(s.begin(),s.end(),nv);if(it==s.end())s.push_back(nv);else s.erase(it);}auto [id,o]=momentLookup(s,to0fixed);size_t z=(size_t)pidx*G+g;IDs[z]=id;SS[z]=(int8_t)(id<0?0:ag*o);if(id<0)zero++;}
 if((pidx+1)%100==0)cerr<<"pairs "<<(pidx+1)<<"/"<<npair<<"\n";pidx++;}}
 pairs.close();{ofstream f(idf,ios::binary);f.write((char*)IDs,total*4);} {ofstream f(sf,ios::binary);f.write((char*)SS,total);} cerr<<"done pair="<<npair<<" total="<<total<<" zero="<<zero<<"\n";
 for(auto&c:cats)free(c.data);free(IDs);free(SS);free(PERM);free(SGN);return 0;
}
