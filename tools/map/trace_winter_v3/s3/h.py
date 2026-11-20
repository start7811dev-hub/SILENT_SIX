import numpy as np
from PIL import Image, ImageDraw
def homog(src,dst):
    A=[];b=[]
    for (x,y),(u,v) in zip(src,dst):
        A.append([x,y,1,0,0,0,-u*x,-u*y]);b.append(u);A.append([0,0,0,x,y,1,-v*x,-v*y]);b.append(v)
    h=np.linalg.solve(np.array(A,float),np.array(b,float));return np.append(h,1).reshape(3,3)
N=28
T,L,R,B=(768,72),(12,492),(1524,490),(770,1003)
# 격자 좌표: 벽 포함 30x30, 안쪽 1..29
H=homog([(1,1),(1,N+1),(N+1,1),(N+1,N+1)],[T,L,R,B])
def P(x,y):
    p=H@np.array([x,y,1.0]);return (p[0]/p[2],p[1]/p[2])
def overlay(out,box=None,s=1,lab=True):
    im=Image.open('/tmp/s3/map.png').convert('RGB')
    if box: im=im.crop(box)
    ox,oy=(box[0],box[1]) if box else (0,0)
    im=im.resize((im.width*s,im.height*s),Image.LANCZOS);d=ImageDraw.Draw(im)
    def Q(x,y):
        a,b=P(x,y);return ((a-ox)*s,(b-oy)*s)
    for i in range(1,N+2):
        c=(255,255,0) if (i-1)%7==0 else (0,255,255)
        d.line([Q(i,1),Q(i,N+1)],fill=c,width=1);d.line([Q(1,i),Q(N+1,i)],fill=c,width=1)
    if lab:
        for x in range(1,N+1):
            for y in range(1,N+1):
                if (x%2==1 and y%2==1) or s>1:
                    a,b=Q(x+.5,y+.5)
                    if 0<=a<im.width and 0<=b<im.height: d.text((a-7,b-5),'%d,%d'%(x,y) if s>1 else '%d'%x if y==1 or True else '',fill=(255,255,255))
    im.save(out)
if __name__=='__main__':
    overlay('/tmp/s3/ov.png',lab=False)
    print(np.round(H,6).tolist())
