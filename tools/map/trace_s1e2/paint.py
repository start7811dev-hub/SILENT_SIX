import sys
import json,sys
class G:
    def __init__(s,n=31):
        s.n=n; s.g=[['.']*n for _ in range(n)]
        for i in range(n):
            for (x,y) in [(i,0),(i,n-1),(0,i),(n-1,i)]: s.g[y][x]='#'
    def c(s,ch,*pts):
        for x,y in pts:
            if 0<=x<s.n and 0<=y<s.n: s.g[y][x]=ch
    def r(s,ch,x0,y0,x1,y1):
        for y in range(min(y0,y1),max(y0,y1)+1):
            for x in range(min(x0,x1),max(x0,x1)+1): s.c(ch,(x,y))
    def hx(s,y,x0,x1,ch='#'): s.r(ch,x0,y,x1,y)   # wall row y
    def vy(s,x,y0,y1,ch='#'): s.r(ch,x,y0,x,y1)   # wall col x
    def o(s,*pts): s.c('.',*pts)
    def save(s,path):
        M=[''.join(r) for r in s.g]; json.dump({'MAP':M},open(path,'w')); print('\n'.join('%2d %s'%(i,r) for i,r in enumerate(M)))

import numpy as np, math
sys.path.insert(0,'/home/claude/tools')
import ov
def to_grid(n,pts,plane='t'):
    H=ov.H_of(n, 0 if plane=='t' else None); Hi=np.linalg.inv(H); out=[]
    for x,y in pts:
        p=Hi@np.array([x,y,1.0]); out.append((p[0]/p[2],p[1]/p[2]))
    return out
def _seg(g,ch,a,b,skip=()):
    (x0,y0),(x1,y1)=a,b; d=math.hypot(x1-x0,y1-y0); n=max(2,int(d*12))
    prev=None
    for i in range(n+1):
        t=i/n; x=x0+(x1-x0)*t; y=y0+(y1-y0)*t; c=(int(math.floor(x)),int(math.floor(y)))
        if prev and c[0]!=prev[0] and c[1]!=prev[1]:
            # 대각선으로 건너뛰면 사이 칸 하나를 채워 새는 틈을 막는다
            mid=(c[0],prev[1]); 
            if mid not in skip: g.c(ch,mid)
        if c not in skip: g.c(ch,c)
        prev=c
def poly_px(g,n,pts,ch='#',plane='t',closed=False,skip=()):
    G_=to_grid(n,pts,plane)
    for i in range(len(G_)-1): _seg(g,ch,G_[i],G_[i+1],skip)
    if closed: _seg(g,ch,G_[-1],G_[0],skip)
    return G_
def poly_g(g,pts,ch='#',closed=False,skip=()):
    for i in range(len(pts)-1): _seg(g,ch,pts[i],pts[i+1],skip)
    if closed: _seg(g,ch,pts[-1],pts[0],skip)
