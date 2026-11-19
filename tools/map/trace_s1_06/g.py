import numpy as np
from PIL import Image,ImageDraw,ImageFont
COLS,ROWS=20,21
T,L,R,B=(780,66),(19,508),(1514,487),(722,950)
def homog(src,dst):
    A=[];b=[]
    for (x,y),(u,v) in zip(src,dst):
        A.append([x,y,1,0,0,0,-u*x,-u*y]);b.append(u);A.append([0,0,0,x,y,1,-v*x,-v*y]);b.append(v)
    h=np.linalg.solve(np.array(A,float),np.array(b,float));return list(h)+[1.0]
H=homog([(0,0),(0,ROWS),(COLS,0),(COLS,ROWS)],[T,L,R,B])
def P(x,y,z=0,S=1):
    w=H[6]*x+H[7]*y+1;return (S*(H[0]*x+H[1]*y+H[2])/w,S*((H[3]*x+H[4]*y+H[5])/w-z))
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',13)
def overlay(out,z=0,S=3,crops=None,MAP=None,lab=True,src='src.png'):
    im=Image.open(src).convert('RGB');im=im.resize((im.width*S,im.height*S),Image.LANCZOS);d=ImageDraw.Draw(im)
    for i in range(COLS+1):d.line([P(i,0,z,S),P(i,ROWS,z,S)],fill=(255,255,0),width=1)
    for j in range(ROWS+1):d.line([P(0,j,z,S),P(COLS,j,z,S)],fill=(255,255,0),width=1)
    for j in range(ROWS):
        for i in range(COLS):
            p=P(i+.5,j+.5,z,S);ch=MAP[j][i] if MAP else '.'
            col={'#':(255,70,70),'C':(255,200,0),'X':(0,255,255)}.get(ch,(255,255,255))
            if lab:d.text((p[0]-14,p[1]-7),'%d,%d'%(i,j),font=F,fill=col,stroke_width=2,stroke_fill=(0,0,0))
    for k,c in enumerate(crops or [(0,0,im.width,im.height)]):im.crop(c).save('%s_%d.jpg'%(out,k),quality=85)
if __name__=='__main__':
    print(H)
    overlay('full',0,S=1,lab=False)
