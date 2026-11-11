#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
using U=uint64_t;
struct Row{U gi;std::array<U,6> n;std::array<U,3> c,p;std::array<U,2> cs,ps;U cl,pl;};
struct Key{std::array<U,6>w;bool operator==(Key const&o)const{return w==o.w;}bool operator<(Key const&o)const{return w<o.w;}};
struct KH{size_t operator()(Key const&k)const noexcept{U h=0x9e3779b97f4a7c15ULL;for(U x:k.w){h^=x+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);}return (size_t)h;}};
struct Ent{std::array<U,3>c,p;std::array<U,2>cs,ps;U cl,pl,m=0;std::array<U,5>idx{};};
static U C(U n,U k){if(k>n)return 0;if(k>n-k)k=n-k;__uint128_t r=1;for(U i=1;i<=k;i++)r=r*(n-k+i)/i;return(U)r;}
static int pc(U x){return __builtin_popcountll(x);}
template<size_t N>static int pc(const std::array<U,N>&a){int s=0;for(U x:a)s+=pc(x);return s;}
template<size_t N>static std::array<U,N> x5(const std::array<U,N>&a,const std::array<U,N>&b,const std::array<U,N>&c,const std::array<U,N>&d,const std::array<U,N>&e){std::array<U,N>r;for(size_t i=0;i<N;i++)r[i]=a[i]^b[i]^c[i]^d[i]^e[i];return r;}
static void add256(std::array<U,4>&a,U x,int limb){__uint128_t z=(__uint128_t)a[limb]+x;a[limb]=(U)z;U carry=(U)(z>>64);for(int i=limb+1;carry&&i<4;i++){z=(__uint128_t)a[i]+carry;a[i]=(U)z;carry=(U)(z>>64);}}
template<class T>static void rd(std::ifstream&f,T&x){f.read((char*)&x,sizeof(x));if(!f)throw std::runtime_error("truncated input");}
static std::string arr(const std::vector<U>&v){std::ostringstream o;o<<'[';for(size_t i=0;i<v.size();i++){if(i)o<<',';o<<v[i];}o<<']';return o.str();}
static std::string hex256(const std::array<U,4>&x){std::ostringstream o;o<<std::hex<<std::setfill('0');for(int i=3;i>=0;i--)o<<std::setw(16)<<x[i];return o.str();}
int main(int ac,char**av){
 if(ac!=5){std::cerr<<"usage: enum input eligible summary sector\n";return 2;}
 std::string in=av[1],elig=av[2],summary=av[3],sector=av[4];
 std::ifstream f(in,std::ios::binary);if(!f){std::cerr<<"open input\n";return 2;}
 char magic[16];f.read(magic,16);std::string want("CDR98O5V1\0\0\0\0\0\0",16);if(std::string(magic,16)!=want)throw std::runtime_error("magic");
 U n;rd(f,n);std::vector<Row>r(n);
 for(auto&x:r){rd(f,x.gi);for(auto&z:x.n)rd(f,z);for(auto&z:x.c)rd(f,z);for(auto&z:x.p)rd(f,z);for(auto&z:x.cs)rd(f,z);for(auto&z:x.ps)rd(f,z);rd(f,x.cl);rd(f,x.pl);}
 char extra;if(f.read(&extra,1))throw std::runtime_error("trailing input");
 std::vector<U>wh(51),ch(145),ph(145),csh(73),psh(73),clh(4096),plh(4096);
 U seen=0,zname=0,zcan=0,zphys=0,cs0=0,ps0=0,cl0=0,pl0=0,cv=0,pv=0,cons=0,eligocc=0;std::array<U,4>check{};
 std::unordered_map<Key,Ent,KH> em;em.reserve(262144);
 for(U a=0;a+4<n;a++)for(U b=a+1;b+3<n;b++)for(U c=b+1;c+2<n;c++)for(U d=c+1;d+1<n;d++)for(U e=d+1;e<n;e++){
  const Row&A=r[a],&B=r[b],&C_=r[c],&D=r[d],&E=r[e];
  Key k{x5(A.n,B.n,C_.n,D.n,E.n)};
  auto ca=x5(A.c,B.c,C_.c,D.c,E.c);
  auto pa=x5(A.p,B.p,C_.p,D.p,E.p);
  auto csa=x5(A.cs,B.cs,C_.cs,D.cs,E.cs);
  auto psa=x5(A.ps,B.ps,C_.ps,D.ps,E.ps);
  U cla=A.cl^B.cl^C_.cl^D.cl^E.cl,pla=A.pl^B.pl^C_.pl^D.pl^E.pl;
  int w=pc(k.w),cw=pc(ca),pw=pc(pa),csw=pc(csa),psw=pc(psa);assert(w<=50&&cw<=144&&pw<=144&&csw<=72&&psw<=72&&cla<4096&&pla<4096);
  seen++;wh[w]++;ch[cw]++;ph[pw]++;csh[csw]++;psh[psw]++;clh[cla]++;plh[pla]++;zname+=(w==0);zcan+=(cw==0);zphys+=(pw==0);cs0+=(csw==0);ps0+=(psw==0);cl0+=(cla==0);pl0+=(pla==0);
  bool cvalid=w>=1&&w<=10&&csw==0&&cla!=0,pvalid=w>=1&&w<=10&&psw==0&&pla!=0,conservative=cvalid&&pvalid&&cla==pla;cv+=cvalid;pv+=pvalid;cons+=conservative;
  U q=(a+1)*3+(b+1)*5+(c+1)*7+(d+1)*11+(e+1)*13;add256(check,q,0);for(size_t j=0;j<6;j++)add256(check,k.w[j],j&3);for(size_t j=0;j<3;j++){add256(check,ca[j],(j+1)&3);add256(check,pa[j],(j+2)&3);}for(size_t j=0;j<2;j++){add256(check,csa[j],(j+1)&3);add256(check,psa[j],(j+2)&3);}add256(check,cla,2);add256(check,pla,3);
  if(w>=1&&w<=10){eligocc++;auto it=em.find(k);if(it==em.end()){Ent x;x.c=ca;x.p=pa;x.cs=csa;x.ps=psa;x.cl=cla;x.pl=pla;x.m=1;x.idx={a,b,c,d,e};em.emplace(k,x);}else{Ent&x=it->second;if(x.c!=ca||x.p!=pa||x.cs!=csa||x.ps!=psa||x.cl!=cla||x.pl!=pla)throw std::runtime_error("same named set unequal linear effect");x.m++;}}
 }
 U expect=C(n,5);if(seen!=expect)throw std::runtime_error("domain count");
 for(auto const&h:{wh,ch,ph,csh,psh,clh,plh}){U s=0;for(U x:h)s+=x;if(s!=seen)throw std::runtime_error("hist sum");}
 std::vector<std::pair<Key,Ent>> es;es.reserve(em.size());for(auto const&x:em)es.push_back(x);std::sort(es.begin(),es.end(),[](auto const&a,auto const&b){return a.first<b.first;});
 std::ofstream ef(elig,std::ios::binary);ef.write("CDR98E5V1\0\0\0\0\0\0",16);U ec=es.size();ef.write((char*)&ec,8);
 for(auto const&kv:es){auto const&k=kv.first;auto const&x=kv.second;for(U z:k.w)ef.write((char*)&z,8);for(U z:x.c)ef.write((char*)&z,8);for(U z:x.p)ef.write((char*)&z,8);for(U z:x.cs)ef.write((char*)&z,8);for(U z:x.ps)ef.write((char*)&z,8);ef.write((char*)&x.cl,8);ef.write((char*)&x.pl,8);ef.write((char*)&x.m,8);for(U z:x.idx)ef.write((char*)&z,8);}ef.close();
 std::map<U,U>mh;U mm=0;for(auto const&x:es){mh[x.second.m]++;mm=std::max(mm,x.second.m);}std::vector<U>mflat;for(auto x:mh){mflat.push_back(x.first);mflat.push_back(x.second);}
 std::ofstream o(summary);o<<"{\n  \"schema\": \"circdist-round98-order5-cpp-census-v1\",\n  \"status\": \"PASS\",\n  \"sector\": \""<<sector<<"\",\n  \"selector_count\": "<<n<<",\n  \"domain_expected\": "<<expect<<",\n  \"domain_enumerated\": "<<seen<<",\n  \"location_weight_histogram\": "<<arr(wh)<<",\n  \"canonical_support_weight_histogram\": "<<arr(ch)<<",\n  \"physical_support_weight_histogram\": "<<arr(ph)<<",\n  \"canonical_syndrome_weight_histogram\": "<<arr(csh)<<",\n  \"physical_syndrome_weight_histogram\": "<<arr(psh)<<",\n  \"canonical_logical_action_histogram\": "<<arr(clh)<<",\n  \"physical_logical_action_histogram\": "<<arr(plh)<<",\n  \"zero_named_support\": "<<zname<<",\n  \"zero_canonical_support\": "<<zcan<<",\n  \"zero_physical_support\": "<<zphys<<",\n  \"canonical_syndrome_zero\": "<<cs0<<",\n  \"physical_syndrome_zero\": "<<ps0<<",\n  \"canonical_logical_trivial\": "<<cl0<<",\n  \"physical_logical_trivial\": "<<pl0<<",\n  \"canonical_source_valid_occurrences\": "<<cv<<",\n  \"physical_source_valid_occurrences\": "<<pv<<",\n  \"conservative_source_valid_occurrences\": "<<cons<<",\n  \"eligible_weight_1_to_10_occurrences\": "<<eligocc<<",\n  \"unique_eligible_named_results\": "<<ec<<",\n  \"multiplicity_histogram_flat_pairs\": "<<arr(mflat)<<",\n  \"maximum_eligible_multiplicity\": "<<mm<<",\n  \"enumeration_checksum_mod_2_256\": \""<<hex256(check)<<"\",\n  \"unordered_indexing\": \"strict nested a<b<c<d<e; every tuple once\",\n  \"hash_table_semantics\": \"full 384-bit key equality; hash collisions do not merge unequal keys\"\n}\n";o.close();
 std::cout<<"ORDER5_ENUM_PASS "<<sector<<" "<<n<<" "<<seen<<" "<<eligocc<<" "<<ec<<" "<<cons<<"\n";
}
