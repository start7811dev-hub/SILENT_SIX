import numpy as np, os, json
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import h, mk
U='/mnt/user-data/uploads/'
SH={'a':'dc99a5be','b':'1dce8635','c':'1bac1a11','d':'02e97d83'}
PUB='/home/claude/silent_six/public/'
def key(im,mode):
    a=np.asarray(im.convert('RGB')).astype(np.float32);r,g,b=a[...,0],a[...,1],a[...,2]
    if mode=='m':
        k=np.minimum(r,b)-g; al=np.clip(1-(k-70)/90,0,1)
        sp=np.clip(k,0,None)*(al<1)*0.0
        m=np.maximum(g,np.minimum(r,b)*0.55); e=(k>25)
        r=np.where(e,np.minimum(r,g+ (r-g)*0.45),r); b=np.where(e,np.minimum(b,g+(b-g)*0.45),b)
    else:
        k=g-np.maximum(r,b); al=np.clip(1-(k-45)/70,0,1)
        g=np.where(k>8,np.maximum(r,b)+np.minimum(k,8),g)
    out=np.dstack([r,g,b,al*255]).clip(0,255).astype(np.uint8)
    return Image.fromarray(out,'RGBA')
def trim(im):
    a=np.asarray(im)[...,3]; ys,xs=np.where(a>24); return im.crop((xs.min(),ys.min(),xs.max()+1,ys.max()+1))
SP={}
for s,f in SH.items():
    im=key(Image.open(U+f+'-image.png'),'m')
    for i in range(6):
        c=im.crop(((i%3)*512,(i//3)*512,(i%3)*512+512,(i//3)*512+512)); SP[s+str(i)]=trim(c)
# 배치: (스프라이트, x, y, w, h, 칸 문자)
PR=[('a0',8,12,1,1,'C'),('a0',19,10,1,1,'C'),('a0',10,22,1,1,'C'),('a0',28,8,1,1,'C'),
    ('a1',12,8,1,1,'C'),('a1',22,12,1,1,'C'),('a1',8,19,1,1,'C'),
    ('a2',18,18,1,1,'C'),
    
    ('a4',22,17,1,1,'C'),('a4',14,22,1,1,'C'),('a4',19,12,1,1,'C'),
    ('a5',8,8,1,1,'C'),('a5',22,22,1,1,'C'),('a5',8,22,1,1,'C'),
    ('b1',11,17,1,2,'C'),('b2',18,8,2,1,'C'),('b5',20,18,1,2,'C'),('b4',16,19,2,1,'C'),
    ('c0',21,8,2,2,'J'),('c1',8,13,1,1,'J'),('c1',16,7,1,1,'J'),('c1',12,23,1,1,'J'),('c1',15,23,1,1,'J'),
    ('c2',22,14,1,1,'J'),('c5',17,21,4,2,'J')]
def place(base,sp,x,y,w,hh,dark=0.82):
    L=h.P(x,y+hh);Rr=h.P(x+w,y);Bm=h.P(x+w,y+hh);T=h.P(x,y)
    fw=Rr[0]-L[0]; s=SP[sp]; k=fw/s.width*1.02
    im=s.resize((max(1,round(s.width*k)),max(1,round(s.height*k))),Image.LANCZOS)
    r,g,b,a=im.split(); rgb=Image.merge('RGB',(r,g,b)); rgb=ImageEnhance.Brightness(rgb).enhance(dark); rgb=ImageEnhance.Color(rgb).enhance(0.85)
    arr=np.asarray(rgb).astype(np.float32)*np.array([0.95,0.96,1.06]); rgb=Image.fromarray(arr.clip(0,255).astype(np.uint8))
    im=Image.merge('RGBA',(*rgb.split(),a))
    sh=Image.new('RGBA',base.size,(0,0,0,0)); d=ImageDraw.Draw(sh); cx=(L[0]+Rr[0])/2; cy=(T[1]+Bm[1])/2
    d.polygon([(L[0]-3,L[1]),(T[0],T[1]-2),(Rr[0]+3,Rr[1]),(Bm[0],Bm[1]+3)],fill=(0,0,0,120)); sh=sh.filter(ImageFilter.GaussianBlur(3))
    base.alpha_composite(sh)
    base.alpha_composite(im,(round(cx-im.width/2),round(Bm[1]+2-im.height)))
if __name__=='__main__':
    base=Image.open('map.png').convert('RGBA')
    for p in sorted(PR,key=lambda p:(p[1]+p[2]+(p[3]+p[4])/2)): place(base,*p[:5])
    import os
    os.makedirs('/home/claude/silent_six/tools/map/trace_winter_v3/sprites',exist_ok=True)
    for k_,v_ in SP.items():
        v2=v_.copy(); v2.thumbnail((256,256),Image.LANCZOS); v2.save('/home/claude/silent_six/tools/map/trace_winter_v3/sprites/%s.png'%k_,optimize=True)
    base.convert('RGB').save('bg_baked.png'); base.convert('RGB').save(PUB+'bgw1.jpg',quality=90)
    g=[list(r) for r in mk.MAP]
    for a,b,c in [(2,10,'.'),(3,10,'.'),(3,11,'.'),(2,17,'.'),(3,17,'.'),(3,18,'.'),(10,2,'.'),(10,3,'.'),(11,3,'.'),(27,18,'.'),(27,19,'.'),(26,18,'.')]: g[b][a]=c
    for sp,x,y,w,hh,c in PR:
        for j in range(hh):
            for i in range(w):
                assert g[y+j][x+i]=='.',(sp,x+i,y+j,g[y+j][x+i]); g[y+j][x+i]=c
    for i in range(2,7): g[28][i]='H'
    g[13][16]='X'
    MAP=[''.join(r) for r in g]; json.dump({'MAP':MAP,'proj':[round(float(v),9) for v in h.H.flatten()]},open('map.json','w'))
    print('\n'.join('%2d %s'%(i,r) for i,r in enumerate(MAP)))
    # 런타임 스프라이트
    for n,sp,wd in [('p_w1_bar_x.png','d0',150),('p_w1_bar_y.png','d1',150),('p_w1_gate_x.png','d2',150),('p_w1_gate_y.png','d3',150),('p_w1_beacon.png','d4',70)]:
        s=SP[sp]; s.resize((wd,round(s.height*wd/s.width)),Image.LANCZOS).save(PUB+n,optimize=True)
    sm=trim(key(Image.open(U+'121162cc-image.png'),'m')); sm.resize((round(sm.width*150/sm.height),150),Image.LANCZOS).save(PUB+'p_w_santa.png',optimize=True)
    for i,f in enumerate(['c2a2ec60','5e5c104c','c6be7150','d18a7138','89a6bf92']):
        p=key(Image.open(U+f+'-image.png'),'g').resize((640,960),Image.LANCZOS); p.save(PUB+'d_w_santa_%d.webp'%(i+1),quality=86,method=6)
    p=key(Image.open(U+'ccd40032-image.png'),'g').resize((640,960),Image.LANCZOS); p.save(PUB+'d_w1_mirage.webp',quality=86,method=6)
    Image.open(U+'6af6d4c1-image.png').convert('RGB').save('/home/claude/silent_six/tools/charsheet/out/sheet_santa.jpg',quality=88)
    for f in sorted(os.listdir(PUB)):
        if f.startswith(('p_w','d_w','bgw1')): print(f,os.path.getsize(PUB+f)//1024,'KB')
