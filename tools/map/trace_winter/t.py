import numpy as np,json
from PIL import Image,ImageDraw,ImageFont
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',13)
def homog(src,dst):
    A=[];b=[]
    for (x,y),(u,v) in zip(src,dst):
        A.append([x,y,1,0,0,0,-u*x,-u*y]);b.append(u);A.append([0,0,0,x,y,1,-v*x,-v*y]);b.append(v)
    return [float(v) for v in np.linalg.solve(np.array(A,float),np.array(b,float))]+[1.0]
CFG={ # cols, rows, T, L, R, B
 1:(19,19,(768,200),(84,542),(1452,542),(768,884)),
 2:(26,17,(610,125),(10,455),(1500,440),(1125,950)),
 3:(21,21,(770,95),(15,500),(1525,470),(755,945)),
 4:(16,22,(870,240),(130,560),(1400,470),(660,880)),
 5:(22,16,(665,185),(95,445),(1450,580),(880,880)),
}
def H(n):
    c,r,T,L,R,B=CFG[n];return homog([(0,0),(0,r),(c,0),(c,r)],[T,L,R,B])
def P(h,x,y,z=0,S=1):
    w=h[6]*x+h[7]*y+1;return (S*(h[0]*x+h[1]*y+h[2])/w,S*((h[3]*x+h[4]*y+h[5])/w-z))
COL={'#':(255,40,90),'B':(60,255,140),'C':(255,190,0),'X':(0,255,255),'V':(90,140,255),'~':(120,200,255),'.':(255,255,255)}
def grid(n,out,S=2,MAP=None,quads=True,lab=True):
    c,r=CFG[n][:2];h=H(n);im=Image.open('x/bgw%d.jpg'%n).convert('RGB');im=im.resize((1536*S,1024*S),Image.LANCZOS);d=ImageDraw.Draw(im)
    for i in range(c+1):d.line([P(h,i,0,0,S),P(h,i,r,0,S)],fill=(255,255,0),width=1)
    for j in range(r+1):d.line([P(h,0,j,0,S),P(h,c,j,0,S)],fill=(255,255,0),width=1)
    for j in range(r):
        for i in range(c):
            ch=MAP[j][i] if MAP else '.';p=P(h,i+.5,j+.5,0,S)
            if MAP and ch!='.':
                d.polygon([P(h,i+.1,j+.1,0,S),P(h,i+.9,j+.1,0,S),P(h,i+.9,j+.9,0,S),P(h,i+.1,j+.9,0,S)],outline=COL[ch],width=3)
            if lab:d.text((p[0]-15,p[1]-7),'%d,%d'%(i,j),font=F,fill=COL.get(ch,(255,255,255)),stroke_width=2,stroke_fill=(0,0,0))
    if quads:
        W,Hh=1536*S,1024*S;k=0
        for (x0,y0) in [(W//2-800,150*S-50),(0+60,Hh//2-560),(W-1660,Hh//2-560),(W//2-800,Hh-1150)]:
            x0=max(0,min(W-1600,x0));y0=max(0,min(Hh-1050,y0));im.crop((x0,y0,x0+1600,y0+1050)).save('%s_%d.jpg'%(out,k),quality=82);k+=1
    else:im.resize((1536,1024),Image.LANCZOS).save(out+'.jpg',quality=85)
if __name__=='__main__':
    import sys
    for n in map(int,sys.argv[1:]):grid(n,'q%d'%n,S=1,quads=False,lab=False)

def H2fix():
    h=_H(2)
    src=[(2,4),(22,4),(2,16),(22,16)];obs=[(2,4.3),(22,4.0),(2,17.0),(22,15.2)]
    return homog(src,[P(h,*o) for o in obs])
_H=H
def H(n):
    return H2fix() if n==2 else _H(n)
