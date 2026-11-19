import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageFilter
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',13)
def homog(src,dst):
    A=[];b=[]
    for (x,y),(u,v) in zip(src,dst):
        A.append([x,y,1,0,0,0,-u*x,-u*y]);b.append(u);A.append([0,0,0,x,y,1,-v*x,-v*y]);b.append(v)
    return [float(v) for v in np.linalg.solve(np.array(A,float),np.array(b,float))]+[1.0]
# cols, rows, wall height, wall-top diamond T,L,R,B (outer edge)
CFG={1:(21,21,46,(768,8),(5,482),(1530,482),(768,948)),
     3:(21,21,46,(768,8),(5,490),(1530,490),(768,958)),
     2:(21,21,0,(768,54),(5,528),(1530,528),(768,994)),
     4:(21,21,46,(768,8),(5,482),(1530,482),(768,948)),
     5:(21,21,46,(768,8),(5,482),(1530,482),(768,948))}
def H(n):
    c,r,h,T,L,R,B=CFG[n];s=lambda p:(p[0],p[1]+h);return homog([(0,0),(0,r),(c,0),(c,r)],[s(T),s(L),s(R),s(B)])
def P(h,x,y,z=0,S=1):
    w=h[6]*x+h[7]*y+1;return (S*(h[0]*x+h[1]*y+h[2])/w,S*((h[3]*x+h[4]*y+h[5])/w-z))
def grid(n,out,z=0,S=1,lab=False,MAP=None,quads=False):
    c,r=CFG[n][:2];h=H(n);im=Image.open('x/bg%d.jpg'%n).convert('RGB');im=im.resize((1536*S,1024*S),Image.LANCZOS);d=ImageDraw.Draw(im)
    for i in range(c+1):d.line([P(h,i,0,z,S),P(h,i,r,z,S)],fill=(255,255,0),width=1)
    for j in range(r+1):d.line([P(h,0,j,z,S),P(h,c,j,z,S)],fill=(255,255,0),width=1)
    COL={'#':(255,60,90),'C':(255,190,0),'B':(60,255,140),'X':(0,255,255),'W':(255,255,0)}
    for j in range(r):
        for i in range(c):
            ch=MAP[j][i] if MAP else '.'
            if MAP and ch!='.':
                zz=CFG[n][2] if ch=='#' or ch=='W' else 0
                d.polygon([P(h,i+.12,j+.12,zz,S),P(h,i+.88,j+.12,zz,S),P(h,i+.88,j+.88,zz,S),P(h,i+.12,j+.88,zz,S)],outline=COL.get(ch,(255,255,255)),width=2)
            if lab and (not MAP or ch=='.'):
                p=P(h,i+.5,j+.5,z,S);d.text((p[0]-15,p[1]-7),'%d,%d'%(i,j),font=F,fill=(255,255,255),stroke_width=2,stroke_fill=(0,0,0))
    if quads:
        W,Hh=1536*S,1024*S
        for k,(x0,y0) in enumerate([(W//2-800,0),(0,Hh//2-525),(W-1600,Hh//2-525),(W//2-800,Hh-1050)]):im.crop((x0,y0,x0+1600,y0+1050)).save('%s_%d.jpg'%(out,k),quality=80)
    else:im.save(out+'.jpg',quality=85)

BASE=dict(CFG);OFF={}
_H0=H
def setgrid(n,ox,oy,c,r,h=46):
    h0=_H0(1) if n!=2 else _H0(2)
    OFF[n]=(ox,oy,homog([(0,0),(0,r),(c,0),(c,r)],[P(h0,ox,oy),P(h0,ox,oy+r),P(h0,ox+c,oy),P(h0,ox+c,oy+r)]));CFG[n]=(c,r,h)+CFG[n][3:]
def H(n):
    return OFF[n][2] if n in OFF else _H0(n)
setgrid(4,-2,-5,25,31)
CFG[5]=(21,21,44,(768,6),(5,462),(1530,462),(768,912))
setgrid(2,-2,-3,23,25,h=0)
