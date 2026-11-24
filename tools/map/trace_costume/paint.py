import json
class G:
    def __init__(s,n=33):
        s.n=n; s.g=[['.']*n for _ in range(n)]
        for i in range(n):
            for (x,y) in [(i,0),(i,n-1),(0,i),(n-1,i)]: s.g[y][x]='#'
    def c(s,ch,*pts):
        for x,y in pts:
            if 0<=x<s.n and 0<=y<s.n: s.g[y][x]=ch
    def r(s,ch,x0,y0,x1,y1):
        for y in range(min(y0,y1),max(y0,y1)+1):
            for x in range(min(x0,x1),max(x0,x1)+1): s.c(ch,(x,y))
    def hx(s,y,x0,x1,ch='#'): s.r(ch,x0,y,x1,y)
    def vy(s,x,y0,y1,ch='#'): s.r(ch,x,y0,x,y1)
    def o(s,*pts): s.c('.',*pts)
    def diag(s,k,x0,x1,ch='#'):
        for x in range(x0,x1+1): s.c(ch,(x,k-x))
    def M(s): return [''.join(r) for r in s.g]
    def save(s,path):
        M=s.M(); json.dump({'MAP':M},open(path,'w')); print('\n'.join('%2d %s'%(i,r) for i,r in enumerate(M)))
