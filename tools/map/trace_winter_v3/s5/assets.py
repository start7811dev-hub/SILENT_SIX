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
SH={'x':'68e29b2d','t':'eb133f86','l':'b5856723','v':'746f8543'}
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
    R(2,6,2,6,'J')
    R(8,20,4,4,'#'); R(8,8,4,11,'#'); g[10][8]='.'; g[11][9]='#'; R(20,20,4,11,'#'); g[10][20]='.'
    R(22,26,3,8,'H'); R(27,28,6,8,'H'); R(1,1,22,25,'T'); R(25,26,26,27,'T')
    for x0 in (4,8,12,16,20): R(x0,x0+2,24,26,'J')
    return g
FIX=[('v0',10,15,4,2,'J'),('v1',19,15,2,4,'J'),('v2',22,20,4,2,'J'),('v4',13,20,5,2,'J'),('v5',17,12,2,3,'J'),
     ('t0',22,17,5,2,'J'),('t1',8,17,2,5,'J'),('t2',15,17,2,2,'J'),('t3',22,12,2,1,'J'),('t4',7,21,1,2,'J'),('t5',3,9,3,2,'J'),
     ('l0',14,14,1,1,'C'),('l0',24,14,1,1,'C'),('l1',19,21,1,1,'C'),('l2',7,3,1,1,'C'),('l2',12,18,1,1,'C'),('l3',9,14,1,1,'C'),('l3',26,12,1,1,'C'),
     ('l4',17,10,1,1,'C'),('l5',18,6,1,1,'C'),('l2',17,28,1,1,'C'),('l0',22,28,1,1,'C'),('l1',6,22,1,1,'C'),('l1',10,6,1,1,'C'),('l3',21,10,1,1,'C'),('l0',5,12,1,1,'C')]
JET0=('x1',10,4,7,7); JET1=('x0',0,12,7,7)
BODY=[[x,y] for y in range(6,10) for x in range(12,16)]; TAXI=[[x,y] for y in range(14,18) for x in range(2,6)]
SC={'l3':.8,'t4':.9}
def place(basei,sp,x,y,w,hh,dark=0.86):
    L=h.P(x,y+hh);Rr=h.P(x+w,y);Bm=h.P(x+w,y+hh);T=h.P(x,y)
    fw=Rr[0]-L[0]; s=SP[sp]; k=fw/s.width*1.02*SC.get(sp,1)
    im=s.resize((max(1,round(s.width*k)),max(1,round(s.height*k))),Image.LANCZOS)
    r,g,b,a=im.split(); rgb=Image.merge('RGB',(r,g,b)); rgb=ImageEnhance.Brightness(rgb).enhance(dark); rgb=ImageEnhance.Color(rgb).enhance(0.82)
    arr=np.asarray(rgb).astype(np.float32)*np.array([0.94,0.97,1.08]); im=Image.merge('RGBA',(*Image.fromarray(arr.clip(0,255).astype(np.uint8)).split(),a))
    if sp[0]!='x':
        sh=Image.new('RGBA',basei.size,(0,0,0,0)); d=ImageDraw.Draw(sh)
        d.polygon([(L[0]-3,L[1]),(T[0],T[1]-2),(Rr[0]+3,Rr[1]),(Bm[0],Bm[1]+3)],fill=(0,5,20,110)); basei.alpha_composite(sh.filter(ImageFilter.GaussianBlur(3)))
    basei.alpha_composite(im,(round((L[0]+Rr[0])/2-im.width/2),round(Bm[1]+2-im.height-(20 if sp=='x0' else -14 if sp=='x1' else 0))))
if __name__=='__main__':
    g=base()
    for sp,x,y,w,hh,c in FIX:
        for j in range(hh):
            for i in range(w):
                assert g[y+j][x+i]=='.',(sp,x+i,y+j,g[y+j][x+i]); g[y+j][x+i]=c
    for x,y in BODY: assert g[y][x]=='.',(x,y); g[y][x]='B'
    for x,y in TAXI: assert g[y][x]=='.',(x,y)
    g[10][13]='X'
    for st in (0,1):
        b=Image.open('map.png').convert('RGBA'); items=[p[:5] for p in FIX]+[JET1 if st else JET0]
        for p in sorted(items,key=lambda p:(p[1]+p[2]+(p[3]+p[4])/2)): place(b,*p)
        b.convert('RGB').save(PUB+'bgw5_%d.jpg'%st,quality=88); b.convert('RGB').save('bake%d.png'%st)
    MAP=[''.join(r) for r in g]; json.dump({'MAP':MAP,'proj':[round(float(v),9) for v in h.H.flatten()],'body':BODY,'taxi':TAXI},open('map.json','w'))
    print('\n'.join('%2d %s'%(i,r) for i,r in enumerate(MAP)))
    os.makedirs('/home/claude/silent_six/tools/map/trace_winter_v3/s5/sprites',exist_ok=True)
    for k_,v_ in SP.items():
        v2=v_.copy(); v2.thumbnail((320,320),Image.LANCZOS); v2.save('/home/claude/silent_six/tools/map/trace_winter_v3/s5/sprites/%s.png'%k_,optimize=True)
    for n,f in [('a','b293a959'),('b','efba1368')]: Image.open(U+f+'-image.png').convert('RGB').resize((768,1152),Image.LANCZOS).save(PUB+'w5_end_%s.jpg'%n,quality=86)
