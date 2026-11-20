import numpy as np, os, json, sys
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import h
U='/mnt/user-data/uploads/'; PUB='/home/claude/silent_six/public/'
SH={'p':'3e325e3b','t':'5bd3d824','w':'afab5501','x':'d0a8efd5'}
def key(im,m='m'):
    a=np.asarray(im.convert('RGB')).astype(np.float32);r,g,b=a[...,0],a[...,1],a[...,2]
    if m=='m':
        k=np.minimum(r,b)-g; al=np.clip(1-(k-70)/90,0,1); e=(k>25)
        r=np.where(e,np.minimum(r,g+(r-g)*0.45),r); b=np.where(e,np.minimum(b,g+(b-g)*0.45),b)
    else:
        k=g-np.maximum(r,b); al=np.clip(1-(k-90)/80,0,1); g=np.where((al<1)|(k>60),np.minimum(g,np.maximum(r,b)+np.clip(k,0,60)*0.5),g)
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
    R(1,7,6,6,'#'); g[6][6]='.'; R(8,8,1,6,'#'); g[5][8]='.'
    for y in (12,18,26): R(1,5,y,y,'#')
    for x,y in [(9,9),(8,12),(8,15),(8,18),(9,21),(9,24),(21,8),(22,11),(22,14),(23,16),(23,19),(23,21)]: g[y][x]='#'
    for y,(a,b) in zip([10,13,15,17,19,21,23],[(9,13),(9,13),(10,13),(10,14),(10,14),(11,14),(11,14)]): R(a,b,y,y,'P')
    for y,(a,b) in zip([9,11,13,15,18,20,22],[(16,20),(17,20),(17,21),(17,21),(18,21),(18,21),(19,22)]): R(a,b,y,y,'P')
    R(10,10,3,6,'B'); R(19,19,2,4,'B'); R(13,15,3,4,'C'); g[3][16]='X'
    R(21,26,3,3,'#'); g[3][22]='.'; R(21,21,1,2,'#'); g[1][23]='R'
    R(26,26,1,10,'#'); g[4][26]='.'; R(25,25,11,24,'#'); R(25,28,25,25,'#'); g[25][27]='.'
    for x in range(10,25): g[28 if x<12 else 27 if x<18 else 26][x]='#'
    for x,y in [(12,27),(16,27),(17,27),(21,26)]: g[y][x]='.'
    R(6,8,24,24,'B')
    return g
FIX=[('t0',2,8,1,1,'J'),('t0',2,14,1,1,'J'),('t0',2,21,1,1,'J'),('t2',6,15,2,2,'J'),('t3',24,7,1,2,'J'),('t5',24,5,2,1,'J'),('t1',11,2,1,1,'J'),
     ('p4',12,6,3,1,'J'),('w0',3,9,1,1,'C'),('w0',3,15,1,1,'C'),('w0',3,22,1,1,'C'),('w1',18,6,1,1,'C'),('w1',4,10,1,1,'C'),('w2',12,2,1,1,'C'),('w2',17,2,1,1,'C'),
     ('w3',14,25,1,1,'C'),('w4',5,20,1,1,'C'),('w4',24,23,1,1,'C'),('w5',3,27,1,1,'C'),('w4',28,15,1,1,'C'),('w3',27,20,1,1,'C'),('w2',6,9,1,1,'C'),('t1',4,3,1,1,'J'),('w3',2,2,1,1,'C')]
CROWD=[]
SC={'t0':.5,'t1':.55,'w1':.55,'w4':.55,'w2':.6,'w5':.7,'w3':.7,'w0':.8,'p2':.85,'p3':.85,'p5':.55,'p4':.62,'t2':.8,'t5':.8,'t3':.9}
def place(basei,sp,x,y,w,hh,dark=0.86):
    L=h.P(x,y+hh);Rr=h.P(x+w,y);Bm=h.P(x+w,y+hh);T=h.P(x,y)
    fw=Rr[0]-L[0]; s=SP[sp]; k=fw/s.width*1.02*SC.get(sp,1)
    im=s.resize((max(1,round(s.width*k)),max(1,round(s.height*k))),Image.LANCZOS)
    r,g,b,a=im.split(); rgb=Image.merge('RGB',(r,g,b)); rgb=ImageEnhance.Brightness(rgb).enhance(dark); rgb=ImageEnhance.Color(rgb).enhance(0.85)
    im=Image.merge('RGBA',(*rgb.split(),a))
    sh=Image.new('RGBA',basei.size,(0,0,0,0)); d=ImageDraw.Draw(sh)
    d.polygon([(L[0]-3,L[1]),(T[0],T[1]-2),(Rr[0]+3,Rr[1]),(Bm[0],Bm[1]+3)],fill=(20,0,0,110)); basei.alpha_composite(sh.filter(ImageFilter.GaussianBlur(3)))
    basei.alpha_composite(im,(round((L[0]+Rr[0])/2-im.width/2),round(Bm[1]+2-im.height)))
if __name__=='__main__':
    g=base(); shut=[]
    for sp,x,y,w,hh,c in FIX:
        for j in range(hh):
            for i in range(w):
                assert g[y+j][x+i]=='.',(sp,x+i,y+j,g[y+j][x+i]); g[y+j][x+i]=c
    for y in (11,12,15,16,19,20,22,23):
        for x in (14,15,16):
            if g[y][x]=='.': shut.append([x,y])
    for n,(x,y) in enumerate(shut):
        if (x+y)%2==0 or x==15: CROWD.append((('p2','p3','p5')[n%3],x,y,1,1))
    for st in (0,1):
        b=Image.open('map.png').convert('RGBA'); items=[p[:5] for p in FIX]+(CROWD if st else [])
        for p in sorted(items,key=lambda p:(p[1]+p[2]+(p[3]+p[4])/2)): place(b,*p)
        b.convert('RGB').save(PUB+'bgw4_%d.jpg'%st,quality=88); b.convert('RGB').save('bake%d.png'%st)
    MAP=[''.join(r) for r in g]; json.dump({'MAP':MAP,'proj':[round(float(v),9) for v in h.H.flatten()],'shut':shut},open('map.json','w'))
    print('\n'.join('%2d %s'%(i,r) for i,r in enumerate(MAP)))
    os.makedirs('/home/claude/silent_six/tools/map/trace_winter_v3/s4/sprites',exist_ok=True)
    for k_,v_ in SP.items():
        v2=v_.copy(); v2.thumbnail((320,320),Image.LANCZOS); v2.save('/home/claude/silent_six/tools/map/trace_winter_v3/s4/sprites/%s.png'%k_,optimize=True)
    key(Image.open(U+'ec3b38a3-image.png'),'g').resize((640,960),Image.LANCZOS).save(PUB+'d_w4_mirage.webp',quality=86,method=6)
