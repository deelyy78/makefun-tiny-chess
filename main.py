import os,json,urllib.request as U
V=(0,100,320,330,500,900,0)
T=["kkkkuuuummoqllmpkkkoljiklmmgkkkk","aceecgkkekmnelnoeknoelmncgklacee","eccaeccaeccaeccageecigggookkoqmk"]
ND=(-33,-31,-18,-14,14,18,31,33);KD=(-17,-16,-15,-1,1,15,16,17);RD=(-16,-1,1,16);BD=(-17,-15,15,17);DS=(0,0,ND,BD,RD,KD,KD)
B=[0]*128;KG=[4,116];UN=[];TT={};NC=[0,0]
SV={p:[(V[abs(p)]+((ord(T[(abs(p)>1)+(abs(p)==6)][((s^112 if p>0 else s)>>4)*4+min(s&7,7-(s&7))])-107)*5 if abs(p)in(1,2,3,6)else 0))*((p>0)*2-1)if not s&0x88 else 0 for s in range(128)]for p in range(-6,7)if p}
def AP(p,s):
 global SC;B[s]=p;SC+=SV[p][s]
 if abs(p)==6:KG[p<0]=s
def DP(s):
 global SC;p=B[s];B[s]=0;SC-=SV[p][s];return p
def KY():return(tuple(B),W)
def FEN(f):
 global W,SC,CR
 B[:]=[0]*128;SC=0;ps=f.split();sq=112;fl=0
 for ch in ps[0]:
  if ch=='/':sq-=16;fl=0
  elif ch.isdigit():fl+=int(ch)
  else:v='pnbrqk'.find(ch.lower())+1;AP(v if ch.isupper()else -v,sq+fl);fl+=1
 W=0 if ps[1]=='b'else 1
 CR=('K' in ps[2])+2*('k' in ps[2])
def AT(sq,wt):
 s=2*wt-1
 for ds,pv in(((-15*s,-17*s),1),(ND,2),(KD,6)):
  for d in ds:
   t=sq+d
   if not t&0x88 and B[t]==pv*s:return 1
 for ds,p1 in((RD,4),(BD,3)):
  for d in ds:
   t=sq+d
   while not t&0x88:
    p=B[t]
    if p:
     if p*s in(p1,5):return 1
     break
    t+=d
 return 0
def GN(cap=0):
 ms=[];A=ms.append;s=2*W-1
 for sq,p in enumerate(B):
  if sq&0x88 or not p or p*s<0:continue
  a=abs(p);r=sq>>4
  if a==1:
   up=16*s;last=r==(1,6)[s>0]
   for d in(up,up-1,up+1):
    t=sq+d
    if t&0x88:continue
    if d==up:
     if B[t]or(cap and not last):continue
     if last:ms+=[(sq,t,x)for x in(5,2)]
     else:
      A((sq,t,0))
      if not cap and r==(6,1)[s>0]and not B[t+up]:A((sq,t+up,0))
    elif B[t]and(B[t]>0)!=(s>0):
     if last:ms+=[(sq,t,x)for x in(5,2)]
     else:A((sq,t,0))
  else:
   ds=DS[a];sl=3<=a<=5
   for d in ds:
    t=sq+d
    while not t&0x88:
     q=B[t]
     if q:
      if(q>0)!=(s>0):A((sq,t,0))
      break
     if not cap:A((sq,t,0))
     if not sl:break
     t+=d
 k=116-112*W;o=1-W
 if not cap and CR>>(1-W)&1 and B[k]==6*s and B[k+3]==4*s and B[k+1]==B[k+2]==0 and all(not AT(x,o)for x in(k,k+1,k+2)):A((k,k+2,0))
 return ms
def MK(m):
 global W
 fr,to,pr=m;p=B[fr];cap=B[to]
 if cap:DP(to)
 DP(fr);AP(p,to)
 if pr:DP(to);AP(((p>0)*2-1)*pr,to)
 if abs(p)==6 and to-fr==2:AP(DP(to+1),fr+1)
 UN.append((m,cap));W=1-W
def UM():
 global W
 m,cap=UN.pop();fr,to,pr=m;p=B[to]
 DP(to);AP((p>0)*2-1 if pr else p,fr)
 if abs(p)==6 and to-fr==2:AP(DP(fr+1),to+1)
 if cap:AP(cap,to)
 W=1-W
def OR(ms,tm):
 ms.sort(key=lambda m:1<<28 if m==tm else 100000+V[abs(B[m[1]])]*16-V[abs(B[m[0]])] if B[m[1]] else 0,reverse=True);return ms
def N(d,a,b):
 NC[0]+=1
 if NC[0]>1e5:NC[1]=1;return SC if W else-SC
 if d<=0:
  st=SC if W else-SC
  a=max(a,st)
  if a>=b:return b
  for m in OR(GN(1),None):
   MK(m)
   if AT(KG[W],W):UM();continue
   sc=-N(0,-b,-a);UM()
   if sc>=b:return b
   if sc>a:a=sc
  return a
 K=KY();e=TT.get(K);tm=None;ao=a
 if e:
  tm=e[2]
  if e[0]>=d and(e[1]>=b if e[3]==1 else e[1]<=a if e[3]==2 else 1):return e[1]
 best=-1e7;bm=None;lg=0
 for m in OR(GN(),tm):
  MK(m)
  if AT(KG[W],W):UM();continue
  lg+=1;sc=-N(d-1,-b,-a);UM()
  if sc>best:
   best=sc;bm=m
   if sc>a:a=sc
   if a>=b:break
 if not lg:return -10**5 if AT(KG[1-W],1-W)else 0
 TT[K]=(d,best,bm,(best>=b)+2*(best<=ao));return best
def BM(fen):
 FEN(fen);TT.clear()
 lg=[m for m in GN()if(MK(m),not AT(KG[W],W),UM())[1]]
 if not lg:return None
 rk=KY();best=lg[0]
 for d in range(9):
  NC[0]=0;NC[1]=0
  N(d,-1e7,1e7)
  if NC[1]:break
  e=TT.get(rk)
  if e and e[2]in lg:best=e[2]
 return best
def UC(m):
 fr,to,pr=m;return chr(97+(fr&7))+str((fr>>4)+1)+chr(97+(to&7))+str((to>>4)+1)+('nbrq'[pr-2]if pr else'')
url=os.getenv('MAKEFUN_ENV_URL')
def main():
 def post(p,bd):return json.load(U.urlopen(url+p,json.dumps(bd).encode()))
 st=post('/game',{})
 while(s:=st.get('status'))!='done':
  if s=='your_move':
   m=BM(st['fen']);st=post('/move',{'game':st['game'],'move':UC(m)})if m else post('/resign',{'game':st['game']})
  else:st=post('/game',{})
if url:main()
