import numpy as np, os, json, sys
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import h
U='/mnt/user-data/uploads/'; PUB='/home/claude/silent_six/public/'
SH={'c':'0dc8a9cf','l':'955fb31c','t':'0a2f9c22','s':'14572901','x':'d231c52c'}
def key(im):
    a=np.asarray(im.convert('RGB')).astype(np.float32);r,g,b=a[...,0],a[...,1],a[...,2]
    k=np.minimum(r,b)-g; al=np.clip(1-(k-70)/90,0,1); e=(k>25)
    r=np.where(e,np.minimum(r,g+(r-g)*0.45),r); b=np.where(e,np.minimum(b,g+(b-g)*0.45),b)
    return Image.fromarray(np.dstack([r,g,b,al*255]).clip(0,255).astype(np.uint8),'RGBA')
def trim(im):
    a=np.asarray(im)[...,3]; ys,xs=np.where(a>24); return im.crop((xs.min(),ys.min(),xs.max()+1,ys.max()+1))
SP={}
for s,f in SH.items():
    im=key(Image.open(U+f+'-image.png'))
    for i in range(6): SP[s+str(i)]=trim(im.crop(((i%3)*512,(i//3)*512,(i%3)*512+512,(i//3)*512+512)))
W=30
def base():
    g=[['.']*W for _ in range(W)]
    def R(x0,x1,y0,y1,c):
        for y in range(y0,y1+1):
            for x in range(x0,x1+1): g[y][x]=c
    for i in range(W): g[0][i]=g[i][0]=g[W-1][i]=g[i][W-1]='#'
    for y0,y1,xs in [(23,24,[(9,13),(16,20),(25,28)]),(17,18,[(10,13),(16,19),(24,27)]),(10,11,[(10,13),(17,20),(23,26)])]:
        for a,b in xs: R(a,b,y0,y1,'B')
    R(1,4,9,12,'#'); R(2,3,10,11,'.'); g[11][4]='.'
    R(1,4,15,20,'#'); R(2,3,16,19,'.'); g[17][4]='.'
    R(3,4,5,6,'T'); R(27,28,3,4,'T')
    R(6,25,5,5,'C')
    for x in (7,8,22,23): g[5][x]='.'
    for x,y in [(7,24),(7,23),(7,21),(7,20),(7,18),(7,17),(7,16),(7,15),(6,13),(6,14),(6,11),(6,10),(6,8),(6,7)]: g[y][x]='C'
    return g
# 고정 소품: (스프라이트, x, y, w, h, 문자)
FIX=[('s2',21,23,3,2,'J'),('s0',20,17,2,2,'J'),('s1',15,10,2,2,'J'),('s4',9,20,4,1,'J'),('s5',22,20,2,2,'J'),('t1',25,26,2,2,'J'),
     ('t0',5,13,1,1,'J'),('t5',5,7,1,1,'J'),('t2',24,15,2,1,'J'),('t3',12,26,2,1,'J'),('t4',5,23,1,2,'J'),('s3',19,26,2,3,'J'),
     ('l0',14,21,1,1,'C'),('l0',9,15,1,1,'C'),('l0',26,21,1,1,'C'),('l1',17,21,1,1,'C'),('l1',21,16,1,1,'C'),('l1',5,8,1,1,'C'),
     ('l2',12,16,1,1,'C'),('l2',23,26,1,1,'C'),('l3',8,26,1,1,'C'),('l4',3,22,1,1,'C'),
     ('l0',16,27,1,1,'C'),
     ('l5',22,12,1,1,'W'),('l5',12,6,1,1,'W'),('x0',2,10,1,1,'X')]
ROW5=[('c0',8),('c1',13),('c2',18),('c3',23)]      # T5 움직이는 줄: 시작 x, 길이 5, y 13..14
ROW7=[('c3',9),('c4',15),('c2',21),('c5',26)]      # T7 목표 줄: y 7..8 (기관차는 길이 3)
def cars(state):
    out=[]
    for i,(sp,x) in enumerate(ROW5):
        if state&1 and i>0: x+=2
        w=5 if x+5<=29 else 29-x
        out.append((sp,x,13,5,2,'B',w))
    if not state&2:
        for sp,x in ROW7: out.append((sp,x,7,3 if sp=='c5' else 5,2,'B',3 if sp=='c5' else 5))
    return out
def place(basei,sp,x,y,w,hh,dark=0.84):
    sc=1.02
    if sp[0]=='c':
        y+= -0.6 if y==13 else 0.45; sc=0.86; x+=0.1
    L=h.P(x,y+hh);Rr=h.P(x+w,y);Bm=h.P(x+w,y+hh);T=h.P(x,y)
    fw=Rr[0]-L[0]; s=SP[sp]; k=fw/s.width*sc
    if sc<1:
        cxm=(L[0]+Rr[0])/2; Bm=(Bm[0],Bm[1]-(1-sc)*fw*0.14)
    im=s.resize((max(1,round(s.width*k)),max(1,round(s.height*k))),Image.LANCZOS)
    r,g,b,a=im.split(); rgb=Image.merge('RGB',(r,g,b)); rgb=ImageEnhance.Brightness(rgb).enhance(dark); rgb=ImageEnhance.Color(rgb).enhance(0.85)
    arr=np.asarray(rgb).astype(np.float32)*np.array([0.96,0.96,1.05]); im=Image.merge('RGBA',(*Image.fromarray(arr.clip(0,255).astype(np.uint8)).split(),a))
    sh=Image.new('RGBA',basei.size,(0,0,0,0)); d=ImageDraw.Draw(sh)
    d.polygon([(L[0]-3,L[1]),(T[0],T[1]-2),(Rr[0]+3,Rr[1]),(Bm[0],Bm[1]+3)],fill=(0,0,0,120)); basei.alpha_composite(sh.filter(ImageFilter.GaussianBlur(3)))
    basei.alpha_composite(im,(round((L[0]+Rr[0])/2-im.width/2),round(Bm[1]+2-im.height)))
def bake(state):
    b=Image.open('map.png').convert('RGBA'); items=[p[:5] for p in FIX]+[c[:5] for c in cars(state)]
    for p in sorted(items,key=lambda p:(p[1]+p[2]+(p[3]+p[4])/2)): place(b,*p)
    return b.convert('RGB')
def grid(state):
    g=base()
    for sp,x,y,w,hh,c in FIX:
        for j in range(hh):
            for i in range(w):
                assert g[y+j][x+i]=='.',(sp,x+i,y+j,g[y+j][x+i]); g[y+j][x+i]=c
    for sp,x,y,w,hh,c,wc in cars(state):
        for j in range(hh):
            for i in range(wc):
                assert g[y+j][x+i] in '.',(sp,x+i,y+j,g[y+j][x+i]); g[y+j][x+i]=c
    return [''.join(r) for r in g]
if __name__=='__main__':
    G=[grid(s) for s in range(4)]
    for s in range(4):
        im=bake(s); im.save(PUB+'bgw2_%d.jpg'%s,quality=88)
        if s==0: im.save('bake0.png')
        if s==1: im.save('bake1.png')
    def diff(a,b):
        op=[];sh=[]
        for y in range(W):
            for x in range(W):
                if a[y][x]!='.' and b[y][x]=='.': op.append([x,y])
                if a[y][x]=='.' and b[y][x]!='.': sh.append([x,y])
        return op,sh
    o1,s1=diff(G[0],G[1]); o2,s2=diff(G[0],G[2]); o1r,s1r=diff(G[1],G[0])
    json.dump({'MAP':G[0],'proj':[round(float(v),9) for v in h.H.flatten()],'sw1':{'clr':o1,'shut':s1},'sw2':{'clr':o2,'shut':s2}},open('map.json','w'))
    print('\n'.join('%2d %s'%(i,r) for i,r in enumerate(G[0]))); print('sw1',o1,s1); print('sw2 n',len(o2))
    os.makedirs('/home/claude/silent_six/tools/map/trace_winter_v3/s2/sprites',exist_ok=True)
    for k_,v_ in SP.items():
        v2=v_.copy(); v2.thumbnail((320,320),Image.LANCZOS); v2.save('/home/claude/silent_six/tools/map/trace_winter_v3/s2/sprites/%s.png'%k_,optimize=True)
    x1=SP['x1']; x1.resize((90,round(x1.height*90/x1.width)),Image.LANCZOS).save(PUB+'p_w2_charge.png',optimize=True)
