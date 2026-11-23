import sys,json,numpy as np
from PIL import Image, ImageDraw, ImageFont
N=31
O=0.5
CFG=json.load(open('/home/claude/work/cfg.json'))
def homog(src,dst):
    A=[];b=[]
    for (x,y),(u,v) in zip(src,dst):
        A.append([x,y,1,0,0,0,-u*x,-u*y]);b.append(u);A.append([0,0,0,x,y,1,-v*x,-v*y]);b.append(v)
    h=np.linalg.solve(np.array(A,float),np.array(b,float));return np.append(h,1).reshape(3,3)
def H_of(n,dy=None):
    c=CFG[n]; d=c.get('dy',0) if dy is None else (dy - c.get('h',0))
    return homog([(O,O),(O,N-O),(N-O,O),(N-O,N-O)],[(x,y+d) for x,y in (c['T'],c['L'],c['R'],c['B'])])
def P(H,x,y):
    p=H@np.array([x,y,1.0]);return (p[0]/p[2],p[1]/p[2])
def font(s):
    try: return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',s)
    except: return ImageFont.load_default()
def overlay(n,out,MAP=None,box=None,s=1,top=False):
    im=Image.open('/home/claude/work/bg%s.jpg'%n).convert('RGB')
    H=H_of(n,0) if top else H_of(n); Ht=H_of(n,0)
    ox,oy=(box[0],box[1]) if box else (0,0)
    if box: im=im.crop(box)
    im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS); d=ImageDraw.Draw(im,'RGBA')
    Q=lambda H,x,y:((P(H,x,y)[0]-ox)*s,(P(H,x,y)[1]-oy)*s)
    f=font(int(9*s))
    if MAP:
        for y in range(len(MAP)):
            for x in range(len(MAP[0])):
                ch=MAP[y][x]
                if ch=='.' : continue
                col={'#':(255,40,40,90),'C':(255,220,0,90),'B':(255,120,0,90),'V':(40,80,255,90),'X':(0,255,0,140),'W':(255,0,255,110),'S':(0,255,255,90)}.get(ch,(255,255,255,90))
                HH=Ht if ch in '#W' else H
                d.polygon([Q(HH,x,y),Q(HH,x+1,y),Q(HH,x+1,y+1),Q(HH,x,y+1)],fill=col)
    for i in range(N+1):
        c=(255,255,0,200) if i%5==0 else (0,255,255,110)
        d.line([Q(H,i,0),Q(H,i,N)],fill=c,width=1); d.line([Q(H,0,i),Q(H,N,i)],fill=c,width=1)
    for i in range(0,N,1):
        a=Q(H,i+.5,-.6); d.text((a[0]-5,a[1]-6),str(i),fill=(255,255,255),font=f)
        a=Q(H,-.8,i+.5); d.text((a[0]-6,a[1]-6),str(i),fill=(255,255,255),font=f)
        a=Q(H,i+.5,N+.6); d.text((a[0]-5,a[1]-6),str(i),fill=(255,255,0),font=f)
        a=Q(H,N+.8,i+.5); d.text((a[0]-6,a[1]-6),str(i),fill=(255,255,0),font=f)
    if s>1.4:
        for y in range(N):
            for x in range(N):
                if (x+y)%2==0:
                    a=Q(H,x+.5,y+.5); d.text((a[0]-8,a[1]-5),'%d,%d'%(x,y),fill=(255,255,255,170),font=font(int(6*s)))
    im.save(out)
if __name__=='__main__':
    n=sys.argv[1]; mode=sys.argv[2] if len(sys.argv)>2 else 'full'
    MAP=None
    try: MAP=json.load(open('/home/claude/work/map%s.json'%n))['MAP']
    except Exception: pass
    if mode=='full': overlay(n,'/home/claude/work/ov%s.png'%n,MAP)
    else:
        # quadrants: tl tr bl br
        top=len(sys.argv)>3
        bx={'t':(384,0,1152,512),'l':(0,256,768,768),'r':(768,256,1536,768),'b':(384,512,1152,1024),'c':(384,256,1152,768)}[mode]
        overlay(n,'/home/claude/work/ov%s_%s.png'%(n,mode),MAP,box=bx,s=2,top=top)
