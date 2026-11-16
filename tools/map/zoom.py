import sys,json
from PIL import Image, ImageDraw
k=sys.argv[1]; HF=json.load(open('hf%s.json'%k)); im=Image.open('map%s.png'%k).convert('RGB')
MAP=json.load(open(sys.argv[2]))[k] if len(sys.argv)>2 else None
def P(x,y):
    w=HF[6]*x+HF[7]*y+1; return ((HF[0]*x+HF[1]*y+HF[2])/w,(HF[3]*x+HF[4]*y+HF[5])/w)
for name,(x0,y0,x1,y1) in {'a':(560,90,1470,570),'b':(80,380,990,960)}.items():
    s=1.68; c=im.crop((x0,y0,x1,y1)).resize((int((x1-x0)*s),int((y1-y0)*s)),Image.LANCZOS); d=ImageDraw.Draw(c)
    T=lambda p:((p[0]-x0)*s,(p[1]-y0)*s)
    for i in range(17): d.line([T(P(i,0)),T(P(i,22))],fill=(0,255,255),width=1)
    for j in range(23): d.line([T(P(0,j)),T(P(16,j))],fill=(0,255,255),width=1)
    for j in range(22):
        for i in range(16):
            p=T(P(i+.5,j+.5))
            if MAP:
                ch=MAP[j][i]
                if ch!='.': d.polygon([T(P(i+.15,j+.15)),T(P(i+.85,j+.15)),T(P(i+.85,j+.85)),T(P(i+.15,j+.85))],outline=(255,40,40) if ch=='#' else (255,220,0));d.text((p[0]-3,p[1]-5),ch,fill=(255,255,255))
            else: d.text((p[0]-13,p[1]-5),'%d,%d'%(i,j),fill=(255,255,0))
    c.save('z%s%s.png'%(k,name))
