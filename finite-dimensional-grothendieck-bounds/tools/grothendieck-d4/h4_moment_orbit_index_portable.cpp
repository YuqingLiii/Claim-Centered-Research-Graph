#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <filesystem>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;
static const int N=300,G=14400;
static uint16_t *PERM;
static int8_t *SGN;
static long long Cbin[301][5];

long long crank(const vector<int>& s){ long long r=0; for(int j=0;j<(int)s.size();++j) r+=Cbin[s[j]][j+1]; return r; }
long long count_comb(int n,int k){ if(k<0||k>n) return 0; return Cbin[n][k]; }

struct State { vector<int> X,Y; };

long long encode(const State& S,int a,int b){
    if(a>0){
        if(S.X.empty()||S.X[0]!=0) { cerr<<"encode no x anchor\n"; exit(2);} 
        vector<int> xr; for(int j=1;j<a;++j) xr.push_back(S.X[j]-1); // 0..298
        long long rx=crank(xr); long long ry=crank(S.Y); return rx*count_comb(300,b)+ry;
    } else {
        if(S.Y.empty()||S.Y[0]!=0){ cerr<<"encode no y anchor\n"; exit(2);} 
        vector<int> yr; for(int j=1;j<b;++j) yr.push_back(S.Y[j]-1);
        return crank(yr);
    }
}

pair<State,int> act(const State&S,int g){
    State T; T.X.reserve(S.X.size()); T.Y.reserve(S.Y.size()); int sg=1;
    size_t base=(size_t)g*N;
    for(int i:S.X){ T.X.push_back(PERM[base+i]); sg*=SGN[base+i]; }
    for(int i:S.Y){ T.Y.push_back(PERM[base+i]); sg*=SGN[base+i]; }
    sort(T.X.begin(),T.X.end()); sort(T.Y.begin(),T.Y.end());
    return {T,sg};
}

void genCombRec(int start,int need,int maxv,vector<int>&cur,const function<void(const vector<int>&)>&fn){
    if(need==0){fn(cur);return;}
    for(int v=start; v<=maxv-need+1; ++v){cur.push_back(v);genCombRec(v+1,need-1,maxv,cur,fn);cur.pop_back();}
}
void genComb(int lo,int hi,int k,const function<void(const vector<int>&)>&fn){ vector<int>cur; if(k==0){fn(cur);return;} genCombRec(lo,k,hi,cur,fn); }

string supportStr(const State&S){ string z="X:"; for(int x:S.X)z+=to_string(x)+","; z+=" Y:";for(int y:S.Y)z+=to_string(y)+",";return z; }

struct CatSummary{int a,b; long long anchored,raw,ori,nonori; string mapfile, repfile, mapsha, repsha;};

string sha256_file(const string&path){ string cmd="sha256sum '"+path+"'"; FILE*f=popen(cmd.c_str(),"r"); char buf[256]; if(!f||!fgets(buf,sizeof(buf),f)){cerr<<"sha fail\n";exit(2);} pclose(f); string s(buf); return s.substr(0,64); }

CatSummary processCat(int a,int b,const vector<vector<int>>&to0,const string&outdir,long long expRaw,long long expOri){
    long long cnt;
    if(a>0) cnt=count_comb(299,a-1)*count_comb(300,b); else cnt=count_comb(299,b-1);
    cerr<<"category "<<a<<","<<b<<" anchored="<<cnt<<"\n";
    vector<int32_t> oid(cnt,-1);
    vector<int8_t> ori(cnt,0);
    vector<State> reps; vector<char> orientable;

    auto handle=[&](const State&S){
        long long idx=encode(S,a,b); if(oid[idx]!=-1) return;
        int id=(int)reps.size(); reps.push_back(S); orientable.push_back(1);
        // Entire G-orbit intersection with anchor: choose any variable in anchor party to map to line 0.
        const vector<int>& anchors=(a>0?S.X:S.Y);
        for(int line:anchors){
            for(int g:to0[line]){
                auto [T,sg]=act(S,g);
                if(a>0){ if(T.X.empty()||T.X[0]!=0){cerr<<"bad x anchor transform\n";exit(2);} }
                else { if(T.Y.empty()||T.Y[0]!=0){cerr<<"bad y anchor transform\n";exit(2);} }
                long long j=encode(T,a,b);
                if(oid[j]==-1){ oid[j]=id; ori[j]=(int8_t)sg; }
                else if(oid[j]==id){ if((int)ori[j]!=sg) orientable[id]=0; }
                else { cerr<<"orbit collision id "<<id<<" prior "<<oid[j]<<" state "<<supportStr(T)<<"\n"; exit(2); }
            }
        }
        // rep itself should be marked +; central stabilizer conflict may mark nonorientable but sign at identity is +.
        if(oid[idx]!=id){cerr<<"rep not marked\n";exit(2);} 
        if(ori[idx]!=1){ // opposite path to same rep means nonorientable; keep stored first identity? identity should be among to0 only if anchor line=0, yes.
            // If first assignment wasn't identity, this can be - while conflict detected later. force + for stable canonical orientation.
            orientable[id]=0;
        }
        ori[idx]=1;
    };

    if(a>0){
        genComb(1,299,a-1,[&](const vector<int>&xr){
            State S; S.X.push_back(0); S.X.insert(S.X.end(),xr.begin(),xr.end());
            genComb(0,299,b,[&](const vector<int>&yy){ S.Y=yy; handle(S); });
        });
    } else {
        genComb(1,299,b-1,[&](const vector<int>&yr){ State S; S.Y.push_back(0); S.Y.insert(S.Y.end(),yr.begin(),yr.end()); handle(S); });
    }

    long long raw=reps.size(), oc=0; vector<int> lid(raw,-1);
    for(int i=0;i<(int)raw;++i) if(orientable[i]) lid[i]=oc++;
    long long non=raw-oc;
    cerr<<"  raw="<<raw<<" orientable="<<oc<<" non="<<non<<"\n";
    if(raw!=expRaw||oc!=expOri){cerr<<"EXPECTED mismatch raw/orient "<<expRaw<<" "<<expOri<<"\n";exit(3);} 

    // overwrite oid with signed local moment id+1, zero for nonorientable.
    for(long long j=0;j<cnt;++j){ int id=oid[j]; if(id<0){cerr<<"unassigned anchored state "<<j<<"\n";exit(2);} if(!orientable[id]) oid[j]=0; else oid[j]=(int32_t)(ori[j]*(lid[id]+1)); }
    string mf=outdir+"/moment_map_"+to_string(a)+"_"+to_string(b)+".i32";
    { ofstream f(mf,ios::binary); f.write((char*)oid.data(),oid.size()*sizeof(int32_t)); }
    string rf=outdir+"/moment_reps_"+to_string(a)+"_"+to_string(b)+".txt";
    { ofstream f(rf); for(int id=0;id<(int)raw;++id) if(orientable[id]) f<<lid[id]<<" "<<supportStr(reps[id])<<"\n"; }
    return {a,b,cnt,raw,oc,non,mf,rf,sha256_file(mf),sha256_file(rf)};
}

int main(int argc,char**argv){
    if(argc!=4){cerr<<"usage: orbit_index perm.bin sign.bin outdir\n";return 1;}
    string pp=argv[1],sp=argv[2],od=argv[3]; filesystem::create_directories(od);
    Cbin[0][0]=1; for(int n=1;n<=300;++n){Cbin[n][0]=1;for(int k=1;k<=4;++k)Cbin[n][k]=Cbin[n-1][k]+Cbin[n-1][k-1];}
    size_t psz=(size_t)G*N;
    PERM=(uint16_t*)malloc(psz*sizeof(uint16_t)); SGN=(int8_t*)malloc(psz);
    {ifstream f(pp,ios::binary);f.read((char*)PERM,psz*sizeof(uint16_t));if(!f){cerr<<"perm read fail\n";return 2;}}
    {ifstream f(sp,ios::binary);f.read((char*)SGN,psz);if(!f){cerr<<"sign read fail\n";return 2;}}
    vector<vector<int>>to0(N);
    for(int g=0;g<G;++g)for(int i=0;i<N;++i)if(PERM[(size_t)g*N+i]==0)to0[i].push_back(g);
    for(int i=0;i<N;++i)if(to0[i].size()!=48){cerr<<"to0 size line "<<i<<"="<<to0[i].size()<<"\n";return 2;}

    // Expected raw/orientable counts from an independent signed Burnside calculation.
    map<pair<int,int>,pair<long long,long long>> ex={
      {{4,0},{47194,47157}}, {{3,1},{187771,187696}}, {{2,2},{282935,282860}}, {{1,3},{187771,187696}}, {{0,4},{47194,47157}}
    };
    vector<CatSummary> ss;
    for(auto ab: vector<pair<int,int>>{{4,0},{3,1},{2,2},{1,3},{0,4}}){ auto e=ex[ab]; ss.push_back(processCat(ab.first,ab.second,to0,od,e.first,e.second)); }
    ofstream js(od+"/moment_orbit_index_summary.json");
    js<<"{\n  \"degree4_orientable_total\":752566,\n  \"degree4_raw_total\":752865,\n  \"categories\":[\n";
    for(size_t i=0;i<ss.size();++i){auto&s=ss[i];js<<"    {\"a\":"<<s.a<<",\"b\":"<<s.b<<",\"anchored_states\":"<<s.anchored<<",\"raw_orbits\":"<<s.raw<<",\"orientable_orbits\":"<<s.ori<<",\"nonorientable_orbits\":"<<s.nonori<<",\"map_file\":\""<<filesystem::path(s.mapfile).filename().string()<<"\",\"map_sha256\":\""<<s.mapsha<<"\",\"reps_file\":\""<<filesystem::path(s.repfile).filename().string()<<"\",\"reps_sha256\":\""<<s.repsha<<"\"}"<<(i+1<ss.size()?",":"")<<"\n";}
    js<<"  ]\n}\n";
    js.close();
    cerr<<"summary sha "<<sha256_file(od+"/moment_orbit_index_summary.json")<<"\n";
    free(PERM);free(SGN); return 0;
}
