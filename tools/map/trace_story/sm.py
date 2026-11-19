import st,json
from PIL import Image
def blank(n):
    c,r=st.CFG[n][:2];M=[['.']*c for _ in range(r)]
    return M
def put(M,cells,ch):
    for (x,y) in cells:
        if 0<=y<len(M) and 0<=x<len(M[0]):M[y][x]=ch
def R(x0,y0,x1,y1):return [(x,y) for y in range(min(y0,y1),max(y0,y1)+1) for x in range(min(x0,x1),max(x0,x1)+1)]
def border(M):
    c,r=len(M[0]),len(M);put(M,R(0,0,c-1,0)+R(0,r-1,c-1,r-1)+R(0,0,0,r-1)+R(c-1,0,c-1,r-1),'#')
def notch(M,k=35,door=((17,18),(18,17)),apron=((18,18),(18,19),(19,18),(19,19))):
    c,r=len(M[0]),len(M)
    for y in range(r):
        for x in range(c):
            if x+y>=k:M[y][x]='#'
    put(M,door,'.');put(M,apron,'.')
OUT={}
def check(n):
    o=OUT[n];M=o['MAP'];c,r=len(M[0]),len(M);seen=set();s=[o['start'][0]]
    while s:
        x,y=s.pop()
        if (x,y) in seen or not(0<=x<c and 0<=y<r) or M[y][x] not in '.W':continue
        seen.add((x,y));s+=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    un=[(x,y) for y in range(r) for x in range(c) if M[y][x]=='.' and (x,y) not in seen]
    return tuple(o['use']) in seen,len(seen),un
def show(n,S=2,half=None):
    M=[''.join(r) for r in OUT[n]['MAP']];print('\n'.join(M));print(check(n))
    st.grid(n,'v%d'%n,S=S,MAP=M,lab=True)
    im=Image.open('v%d.jpg'%n);W,H=im.size
    im.crop((0,0,W,H//2+60)).save('v%d_a.jpg'%n,quality=80);im.crop((0,H//2-60,W,H)).save('v%d_b.jpg'%n,quality=80)
# ---------- 1 warehouse
M=blank(1);border(M);notch(M)
put(M,R(1,4,4,4)+R(4,4,4,7)+R(4,9,4,14)+R(1,10,3,10)+R(1,14,3,14)+R(1,16,6,16)+R(6,16,6,19)+R(6,1,6,4)+R(6,4,8,4)+R(10,1,10,4)+R(10,4,15,4)+R(16,1,16,7)+R(18,7,19,7),'#')
put(M,[(2,10),(2,14),(6,18),(12,4)],'.')
put(M,R(7,10,8,14)+R(8,6,9,8)+R(11,6,12,8)+[(13,6),(13,7)]+R(11,9,12,12)+[(10,14),(11,14),(9,18),(9,19),(10,19)]+R(12,18,13,19)+R(16,9,17,11)+[(18,9),(18,10),(15,11),(17,14),(18,13),(18,14),(18,3),(19,3)],'C')
put(M,[(1,18),(1,19),(3,19),(4,19),(1,17),(2,17),(4,17),(1,12),(1,5),(1,6),(1,7),(1,8),(2,5),(3,5),(2,8),(1,1),(1,2),(2,1),(3,1),(4,1),(5,1),(7,1),(7,2),(9,1)],'C')
OUT[1]=dict(MAP=M,start=[(18,18)],use=(13,2),hostage=(13,1))
# ---------- 3 office
M=blank(3);border(M);notch(M)
put(M,R(1,4,4,4)+R(4,4,4,6)+R(4,8,4,15)+R(1,10,3,10)+R(1,16,6,16)+R(6,16,6,19)+R(6,1,6,4)+R(6,4,15,4)+R(15,1,15,4)+R(16,1,16,7)+R(18,7,19,7),'#')
put(M,[(4,13),(6,18),(10,4)],'.')
put(M,[(8,8),(8,9),(9,8)]+R(8,12,10,13)+R(11,7,12,9)+R(12,11,13,12)+R(9,16,10,17)+R(15,9,17,10)+[(12,17),(13,16),(13,17),(17,13),(18,13),(2,19),(3,19),(4,19),(2,12),(2,13),(1,6),(1,7),(1,8),(3,6),(2,8),(1,1),(1,2),(2,1),(4,1),(1,3),(18,2),(18,3),(18,4),(18,6),(19,6)],'C')
put(M,[(8,1),(9,1),(10,1),(12,1),(13,1),(14,1),(14,2)],'C');M[1][11]='X'
OUT[3]=dict(MAP=M,start=[(18,18),(19,18)],use=(11,2),obj=(11,1))
if __name__=='__main__':
    import sys
    for n in map(int,sys.argv[1:]):show(n)
