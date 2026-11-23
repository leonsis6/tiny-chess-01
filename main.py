import json,os,urllib.request as u
L=os.getenv("MAKEFUN_ENV_URL")
H='kkkkuuuummoqllmpkkkoljiklmmgkkkkaceecgkkekmnelnoeknoelmncgklaceegiiiikkkiklmillmikmmimmmilkkgiiikkkklmmmjkkkjkkkjkkkjkkkjkkkkkkl'
V=(0,100,320,330,500,900,0)
N=(-33,-31,-18,-14,14,18,31,33)
B=(-17,-15,15,17)
R=(-16,-1,1,16)
G=B+R
Q=(0,0,N,B,R,B+R,G)
K={0:13,7:14,4:12,112:7,119:11,116:3}
T=[0]*896
for i,c in enumerate(H):
 a=i//32+1;j=i%32;r=j>>2;f=j&3;v=(ord(c)-107)*5
 for q in (f,7-f):T[a*128+(7-r)*16+q]=v
M=U=10**5
I=2*M
D=0
W=[0]*8
def F(f):
 b=[0]*128;p=f.split();i=112
 for c in p[0]:
  if c=='/':i-=24
  elif c.isdigit():i+=int(c)
  else:b[i]=('pnbrqk'.index(c.lower())+1)*(1 if c<'a' else -1);i+=1
 s=1-2*(p[1]=='b')
 a=sum(1<<'KQkq'.index(c) for c in p[2] if c!='-')
 e=(int(p[3][1])-1)*16+ord(p[3][0])-97 if p[3]!='-' else None
 return b,s,a,e,b.index(6),b.index(-6)
def A(b,q,y):
 for d in (15,17):
  t=q-d*y
  if not t&136 and b[t]==y:return 1
 for d in N+G:
  t=q+d
  if not t&136 and b[t]==y*(2 if d in N else 6):return 1
 for d in B+R:
  t=q+d
  while not t&136 and not b[t]:t+=d
  if not t&136 and b[t] in (y*(3+(d in R)),5*y):return 1
 return 0
def g(b,s,a,e):
 m=[]
 for f,p in enumerate(b):
  if not p or p*s<0:continue
  x=abs(p)
  if x==1:
   d=16*s
   w=7*(s>0)
   t=f+d
   if not t&136 and not b[t]:
    m.append((f,t,5*((t>>4)==w)))
    if (t>>4)==2+3*(s<0) and not b[f+2*d]:m.append((f,f+2*d,0))
   for z in (d-1,d+1):
    t=f+z
    if t&136:continue
    if b[t] and b[t]*s<0:m.append((f,t,5*((t>>4)==w)))
    elif t==e:m.append((f,t,0))
  else:
   for d in Q[x]:
    t=f+d
    while not t&136 and (not b[t] or b[t]*s<0):
     m.append((f,t,0))
     if x==2 or x==6 or b[t]:break
     t+=d
 for d in (1,-1):
  f=60-56*s
  o=f+2*d
  if a&1<<(2*(s<0)+(d<0)) and not b[f+d] and not b[f+2*d] and (d>0 or not b[f-3]) and b[o+1 if d>0 else o-2]==4*s and not any(A(b,f+i*d,-s) for i in (0,1,2)):m.append((f,o,0))
 return m
def Y(b,m,s,z):
 f,o,pr=m
 c=b[o];v=o
 w,x=z[0],z[1]
 j=k=-1
 if abs(b[f])==1 and o==x and not c:
  v=o-16*s;c=b[v];b[v]=0
 b[o]=pr*s if pr else b[f];b[f]=0
 if abs(b[o])==6:
  z[2+(s<0)]=o
  if abs(o-f)==2:
   j=o+1 if o%8==6 else o-2
   k=j-2 if j&1 else j+3
   b[k]=b[j];b[j]=0
 z[0]=w&K.get(f,15)&K.get(o,15)
 z[1]=f+16*s if b[o]==s and abs(o-f)==32 else None
 return (f,o,pr,c,v,w,x,j,k)
def Z(b,uu,s,z):
 f,o,pr,c,v,w,x,j,k=uu
 if abs(b[o])==6:z[2+(s<0)]=f
 b[f]=s if pr else b[o];b[o]=0
 if c:b[v]=c
 if j>=0:b[j]=b[k];b[k]=0
 z[0],z[1]=w,x
def E(b):
 v=0
 for q,p in enumerate(b):
  if p:
   a=abs(p)
   v+=(V[a]+T[a*128+q if p>0 else a*128+(q^112)])*(1 if p>0 else -1)
 return v
X=KeyError
def S(b,s,z,d,a,y,p):
 global D
 D+=1
 if D>U:raise X
 h=A(b,z[2+(s<0)],-s)
 q=not d and not h
 if q:
  t=s*E(b)
  if t>=y:return y
  if t>a:a=t
 m=g(b,s,z[0],z[1])
 if q:m=[mv for mv in m if b[mv[1]] or (abs(b[mv[0]])==1 and mv[1]==z[1])]
 m.sort(key=lambda mv:10000*(d and mv==W[p])+(10*V[abs(b[mv[1]])]-V[abs(b[mv[0]])] if b[mv[1]] else 0)+9000*(mv[2]>0),reverse=True)
 n=0
 for mv in m:
  uu=Y(b,mv,s,z)
  if A(b,z[2+(s<0)],-s):Z(b,uu,s,z);continue
  n+=1
  sc=-S(b,-s,z,max(d-1,0),-y,-a,p+1)
  Z(b,uu,s,z)
  if sc>a:a=sc
  if a>=y:
   if d and not b[mv[1]]:W[p]=mv
   break
 if not n:return -M+p if h else (a if not d else 0)
 return a
def C(b,s,z,mv):
 global D
 D=0
 w=mv[0];R={}
 for d in range(1,8):
  try:
   q=None;v=-I;a=-I
   mv.sort(key=lambda m:-R.get(m,0))
   for m in mv:
    uu=Y(b,m,s,z)
    sc=-S(b,-s,z,d-1,-I,-a,1)
    Z(b,uu,s,z)
    R[m]=sc
    if sc>v:v,q=sc,m
    if sc>a:a=sc
   w=q
  except X:break
 return w
def J(h,j):
 try:return json.load(u.urlopen(u.Request(L+h,data=json.dumps(j).encode())))
 except:return None
while (P:=J('/game',{})) and P['status']!='done':
 while P['status']=='your_move':
  b,s,a,e,w,k=F(P['fen'])
  z=[a,e,w,k]
  ms=[((int(t[1])-1)*16+ord(t[0])-97,(int(t[3])-1)*16+ord(t[2])-97,(5-'qrbn'.find(t[4:5] or 'x'))%6) for t in P['legal_moves']]
  mv=C(b,s,z,ms)
  h=J('/move',{'game':P['game'],'move':''.join(chr(97+(q&7))+str((q>>4)+1) for q in mv[:2])+'q'*(mv[2]>0)}) or J('/resign',{'game':P['game']})
  if not h:break
  P=h
