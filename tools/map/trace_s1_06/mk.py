import numpy as np,g,seg
from PIL import Image,ImageDraw,ImageFont
C,R=21,21
M=[['.']*C for _ in range(R)]
def put(x,y,ch='#'):
    if 0<=x<C and 0<=y<R:M[y][x]=ch
for x in range(C):put(x,0);put(x,20)
for y in range(R):put(0,y);put(20,y)
for x in (6,7,19):put(x,20,'.')
put(20,10,'.')
for k,pts in seg.G.items():
    for (a,b) in zip(pts,pts[1:]):
        n=int(max(abs(b[0]-a[0]),abs(b[1]-a[1]))*8)+1
        for t in range(n+1):
            x=a[0]+(b[0]-a[0])*t/n;y=a[1]+(b[1]-a[1])*t/n
            # snap the minor axis to the segment's mean so a slanted line does not hop cells
            if abs(b[0]-a[0])>abs(b[1]-a[1]):y=(a[1]+b[1])/2
            else:x=(a[0]+b[0])/2
            put(int(np.floor(x)),int(np.floor(y)))
def show():
    for r in M:print(''.join(r))
def render(out,MAP,S=2,crops=None,lab=True):
    im=Image.open('src.png').convert('RGB');im=im.resize((im.width*S,im.height*S),Image.LANCZOS);d=ImageDraw.Draw(im)
    F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',12)
    def P(x,y,top=False):
        p=g.P(x,y);z=seg.hgt(p[0]) if top else 0;return (S*p[0],S*(p[1]-z))
    W=lambda i,j,cs:0<=i<C and 0<=j<R and MAP[j][i] in cs
    for cs,ct,cb,top in (('#',(255,40,90),(255,255,0),True),('C',(255,160,0),(0,255,120),False)):
      for j in range(R):
        for i in range(C):
            if not W(i,j,cs):continue
            for (a,b,ni,nj) in [((i,j),(i+1,j),i,j-1),((i+1,j),(i+1,j+1),i+1,j),((i+1,j+1),(i,j+1),i,j+1),((i,j+1),(i,j),i-1,j)]:
                if not W(ni,nj,cs):
                    if top:d.line([P(*a,True),P(*b,True)],fill=ct,width=2)
                    d.line([P(*a),P(*b)],fill=cb,width=2)
    if lab:
      for j in range(R):
        for i in range(C):
            if MAP[j][i]=='.':
                p=P(i+.5,j+.5);d.text((p[0]-12,p[1]-6),'%d,%d'%(i,j),font=F,fill=(255,255,255),stroke_width=2,stroke_fill=(0,0,0))
    for k,c in enumerate(crops or [(0,0,im.width,im.height)]):im.crop(c).save('%s_%d.jpg'%(out,k),quality=85)
if __name__=='__main__':
    show();render('w',[''.join(r) for r in M],S=1,lab=False)
