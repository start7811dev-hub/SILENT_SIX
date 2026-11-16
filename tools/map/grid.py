import sys,json,numpy as np
from PIL import Image, ImageDraw
k=sys.argv[1]; FLO=json.loads(sys.argv[2]); SRC={'3':'ddd4b084','5':'fe9da4f6'}
im0=Image.open('/mnt/user-data/uploads/%s-image.png'%SRC[k]).convert('RGB'); sc=1024/im0.height; w=int(im0.width*sc)
im=Image.new('RGB',(1536,1024)); im.paste(im0.resize((w,1024),Image.LANCZOS),((1536-w)//2,0)); im.save('map%s.png'%k)
FLO=[[x*sc+(1536-w)/2,y*sc] for x,y in FLO]
def homog(src,dst):
    A=[];b=[]
    for (x,y),(u,v) in zip(src,dst):
        A.append([x,y,1,0,0,0,-u*x,-u*y]);b.append(u);A.append([0,0,0,x,y,1,-v*x,-v*y]);b.append(v)
    return list(np.linalg.solve(np.array(A,float),np.array(b,float)))+[1.0]
HF=homog([(0,0),(16,0),(0,22),(16,22)],FLO); json.dump(HF,open('hf%s.json'%k,'w'))
def P(x,y):
    w_=HF[6]*x+HF[7]*y+1; return ((HF[0]*x+HF[1]*y+HF[2])/w_,(HF[3]*x+HF[4]*y+HF[5])/w_)
d=ImageDraw.Draw(im)
MAP=json.load(open(sys.argv[3]))[k] if len(sys.argv)>3 else None
for i in range(17): d.line([P(i,0),P(i,22)],fill=(0,255,255) if i%4 else (255,255,0),width=1 if i%4 else 2)
for j in range(23): d.line([P(0,j),P(16,j)],fill=(0,255,255) if j%4 else (255,255,0),width=1 if j%4 else 2)
for i in range(16): p=P(i+.5,-0.6); d.text((p[0]-4,p[1]-6),str(i),fill=(255,255,255))
for j in range(22): p=P(-0.7,j+.5); d.text((p[0]-6,p[1]-6),str(j),fill=(255,255,255))
for j in range(22):
    for i in range(16):
        p=P(i+.5,j+.5)
        if MAP:
            ch=MAP[j][i]
            if ch!='.': d.text((p[0]-3,p[1]-5),ch,fill=(255,60,60))
        elif (i+j)%2==0 and i%2==0: d.text((p[0]-8,p[1]-5),'%d,%d'%(i,j),fill=(255,255,120))
im.save('grid%s.png'%k)
