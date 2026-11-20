import numpy as np, os, json, sys
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import h
U='/mnt/user-data/uploads/'; PUB='/home/claude/silent_six/public/'
SH={'i':'d75f975f','w':'50081e0a','t':'5a855d3c','x':'9cab4b71'}
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
    R(2,6,2,6,'#'); R(3,5,3,5,'.')
    for x,y in [(6,5),(6,6),(5,6),(2,5)]: g[y][x]='.'
    g[3][4]='X'
    R(2,5,9,12,'J'); R(2,5,15,19,'J'); R(1,5,23,27,'H'); R(3,5,21,22,'H')
    R(9,13,24,27,'J'); R(15,19,24,27,'J'); R(24,27,15,19,'J'); R(24,27,9,13,'J')
    R(23,25,2,4,'H'); R(26,27,2,3,'J'); g[4][22]='T'
    R(15,19,2,5,'J'); R(10,13,2,4,'H')
    return g
FIX=[('i2',18,18,2,2,'#'),('i1',14,15,2,2,'#'),('i0',10,12,2,2,'#'),('i2',12,8,2,2,'#'),('i1',17,11,2,2,'#'),
     ('w0',20,15,1,1,'C'),('w0',9,17,1,1,'C'),('w0',16,8,1,1,'C'),('w0',8,10,1,1,'C'),('w0',21,20,1,1,'C'),
     ('w1',12,18,2,1,'C'),('w1',19,13,2,1,'C'),('i3',15,20,2,1,'C'),('i4',21,10,1,2,'C'),('i5',8,20,3,1,'C'),
     ('w3',11,15,1,1,'C'),('w4',17,15,1,1,'C'),('w4',14,11,1,1,'C'),('t2',19,8,2,1,'J'),('t3',7,14,1,2,'J'),('t2',15,13,2,1,'J'),
     ('w2',7,4,1,1,'C'),('w5',14,5,1,1,'C'),('w4',20,3,1,1,'C'),('t5',21,22,1,1,'J'),('w2',6,22,1,1,'C'),('t4',9,22,3,1,'J'),
     ('w5',22,24,1,1,'C'),('w4',25,23,1,1,'C'),('t1',26,25,2,2,'J'),('w2',28,14,1,1,'C'),('t5',23,14,1,1,'J'),('w5',1,14,1,1,'C'),('w3',7,25,1,1,'C'),
     ('t0',20,26,2,2,'J'),('w1',15,22,2,1,'C')]
def place(basei,sp,x,y,w,hh,dark=0.82):
    L=h.P(x,y+hh);Rr=h.P(x+w,y);Bm=h.P(x+w,y+hh);T=h.P(x,y)
    fw=Rr[0]-L[0]; s=SP[sp]; k=fw/s.width*1.02
    im=s.resize((max(1,round(s.width*k)),max(1,round(s.height*k))),Image.LANCZOS)
    r,g,b,a=im.split(); rgb=Image.merge('RGB',(r,g,b)); rgb=ImageEnhance.Brightness(rgb).enhance(dark); rgb=ImageEnhance.Color(rgb).enhance(0.8)
    arr=np.asarray(rgb).astype(np.float32)*np.array([0.92,0.96,1.10]); im=Image.merge('RGBA',(*Image.fromarray(arr.clip(0,255).astype(np.uint8)).split(),a))
    sh=Image.new('RGBA',basei.size,(0,0,0,0)); d=ImageDraw.Draw(sh)
    d.polygon([(L[0]-3,L[1]),(T[0],T[1]-2),(Rr[0]+3,Rr[1]),(Bm[0],Bm[1]+3)],fill=(0,10,30,110)); basei.alpha_composite(sh.filter(ImageFilter.GaussianBlur(3)))
    basei.alpha_composite(im,(round((L[0]+Rr[0])/2-im.width/2),round(Bm[1]+2-im.height)))
if __name__=='__main__':
    b=Image.open('map.png').convert('RGBA')
    for p in sorted(FIX,key=lambda p:(p[1]+p[2]+(p[3]+p[4])/2)): place(b,*p[:5])
    b.convert('RGB').save('bake.png'); b.convert('RGB').save(PUB+'bgw3.jpg',quality=88)
    g=base()
    for sp,x,y,w,hh,c in FIX:
        for j in range(hh):
            for i in range(w):
                assert g[y+j][x+i]=='.',(sp,x+i,y+j,g[y+j][x+i]); g[y+j][x+i]=c
    MAP=[''.join(r) for r in g]; json.dump({'MAP':MAP,'proj':[round(float(v),9) for v in h.H.flatten()]},open('map.json','w'))
    print('\n'.join('%2d %s'%(i,r) for i,r in enumerate(MAP)))
    os.makedirs('/home/claude/silent_six/tools/map/trace_winter_v3/s3/sprites',exist_ok=True)
    for k_,v_ in SP.items():
        v2=v_.copy(); v2.thumbnail((320,320),Image.LANCZOS); v2.save('/home/claude/silent_six/tools/map/trace_winter_v3/s3/sprites/%s.png'%k_,optimize=True)
    wsp=SP['x0']; wsp.resize((round(wsp.width*150/wsp.height),150),Image.LANCZOS).save(PUB+'p_w3_witness.png',optimize=True)
    for n,f in [(0,'eb7d72ba'),(1,'c91ea020')]:
        key(Image.open(U+f+'-image.png'),'g').resize((640,960),Image.LANCZOS).save(PUB+'d_w3_witness_%d.webp'%n,quality=86,method=6)
