import sys,json,importlib.util,numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
sys.path.insert(0,'/home/claude/tools'); import ov
W='/home/claude/work/'; PUB='/home/claude/repo/public/'
def key(im):
    a=np.asarray(im.convert('RGB')).astype(np.float32);r,g,b=a[...,0],a[...,1],a[...,2]
    k=np.minimum(r,b)-g; al=np.clip(1-(k-70)/90,0,1)
    e=(k>25); r=np.where(e,np.minimum(r,g+(r-g)*0.45),r); b=np.where(e,np.minimum(b,g+(b-g)*0.45),b)
    return Image.fromarray(np.dstack([r,g,b,al*255]).clip(0,255).astype(np.uint8),'RGBA')
def trim(im):
    a=np.asarray(im)[...,3]; ys,xs=np.where(a>24); return im.crop((xs.min(),ys.min(),xs.max()+1,ys.max()+1))
def sprites(n):
    SP={}
    for s in 'ab':
        im=key(Image.open(W+'p%s%s.png'%(s,n)))
        for i in range(6):
            c=im.crop(((i%3)*512,(i//3)*512,(i%3)*512+512,(i//3)*512+512)); SP[s+str(i)]=trim(c)
    return SP
def place(base,H,sp,x,y,w,hh,dark=0.9,sc=1.0):
    P=lambda a,b: ov.P(H,a,b)
    L=P(x,y+hh);Rr=P(x+w,y);Bm=P(x+w,y+hh);T=P(x,y)
    fw=(Rr[0]-L[0])*sc; k=fw/sp.width*1.02
    im=sp.resize((max(1,round(sp.width*k)),max(1,round(sp.height*k))),Image.LANCZOS)
    r,g,b,a=im.split(); rgb=Image.merge('RGB',(r,g,b)); rgb=ImageEnhance.Brightness(rgb).enhance(dark); rgb=ImageEnhance.Color(rgb).enhance(0.88)
    im=Image.merge('RGBA',(*rgb.split(),a))
    sh=Image.new('RGBA',base.size,(0,0,0,0)); d=ImageDraw.Draw(sh)
    d.polygon([(L[0]-3,L[1]),(T[0],T[1]-2),(Rr[0]+3,Rr[1]),(Bm[0],Bm[1]+3)],fill=(0,0,0,120)); sh=sh.filter(ImageFilter.GaussianBlur(3))
    base.alpha_composite(sh); cx=(L[0]+Rr[0])/2
    base.alpha_composite(im,(round(cx-im.width/2),round(Bm[1]+2-im.height)))
def build(n,spec):
    H=ov.H_of(n); SP=sprites(n)
    base=Image.open(W+'bg%s.jpg'%n).convert('RGBA')
    g=[list(r) for r in json.load(open(W+'map%s.json'%n))['MAP']]
    PR=spec.PR
    for p in sorted(PR,key=lambda p:(p[1]+p[2]+(p[3]+p[4])/2)): place(base,H,SP[p[0]],*p[1:5],**(p[6] if len(p)>6 else {}))
    for p in PR:
        sp,x,y,w,hh,c=p[:6]
        for j in range(hh):
            for i in range(w):
                assert g[y+j][x+i]=='.',(n,sp,x+i,y+j,g[y+j][x+i]); g[y+j][x+i]=c
    MAP=[''.join(r) for r in g]
    base.convert('RGB').save(PUB+'bg_s1_%s.jpg'%n,quality=88)
    base.convert('RGB').save(W+'baked%s.jpg'%n,quality=88)
    for name,spn,wd in getattr(spec,'BARS',[]):
        s=SP[spn]; s.resize((wd,round(s.height*wd/s.width)),Image.LANCZOS).save(PUB+name,optimize=True)
    proj=[round(float(v),9) for v in H.flatten()]
    json.dump({'MAP':MAP,'proj':proj},open(W+'final%s.json'%n,'w'))
    print('\n'.join('%2d %s'%(i,r) for i,r in enumerate(MAP)))
if __name__=='__main__':
    n=sys.argv[1]
    sp=importlib.util.spec_from_file_location('s','/home/claude/maps/s%s.py'%n); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    build(n,m)
