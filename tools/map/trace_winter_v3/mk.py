import numpy as np, json
from PIL import Image, ImageDraw
import h
W=31
g=[['.']*W for _ in range(W)]
def R(x0,x1,y0,y1,c):
    for y in range(y0,y1+1):
        for x in range(x0,x1+1): g[y][x]=c
for i in range(W): g[0][i]=g[i][0]=g[W-1][i]=g[i][W-1]='#'
for i in range(W):
    g[29][i]='#' if i>14 else '.'
    g[i][29]='#' if i>16 else '.'
g[29][0]=g[0][29]='#'; g[29][29]='#'
for x,y in [(13,30),(14,30),(30,14),(30,15),(0,15),(0,16),(15,0),(16,0)]: g[y][x]='.'
R(2,7,2,7,'F'); R(3,6,3,6,'B')            # 회전목마
R(2,6,10,14,'B'); R(2,6,17,21,'B')        # 가판대 묶음 A, B
R(10,14,2,6,'B')                          # 가판대 묶음 C
R(17,21,2,6,'H')                          # 장난감 가게
R(23,28,2,6,'F'); R(24,27,3,5,'.'); R(26,27,3,4,'G'); g[6][24]='.'   # 발전기 마당
R(24,28,10,13,'H')                        # 무대
R(24,27,16,20,'B')                        # 가판대 묶음 D
R(23,26,23,26,'C')                        # 분수
R(2,6,23,27,'H'); R(9,12,24,27,'H'); R(15,20,24,27,'H')   # 집 셋
R(13,16,13,16,'T')                        # 트리
for x0,y0 in [(9,14),(14,9),(13,20),(20,14)]: R(x0,x0+1,y0,y0+1,'B')
MAP=[''.join(r) for r in g]
if __name__=='__main__':
    import sys
    col={'#':(255,0,0),'B':(255,140,0),'H':(255,0,255),'F':(0,255,0),'C':(0,200,255),'T':(255,255,0),'G':(255,255,255)}
    im=Image.open('map.png').convert('RGBA');ov=Image.new('RGBA',im.size,(0,0,0,0));d=ImageDraw.Draw(ov)
    for y in range(W):
        for x in range(W):
            c=MAP[y][x]
            if c!='.' and not (x in (0,30) or y in (0,30)):
                d.polygon([h.P(x,y),h.P(x+1,y),h.P(x+1,y+1),h.P(x,y+1)],fill=col[c]+(95,),outline=col[c]+(255,))
    for i in range(0,W+1):
        d.line([h.P(i,0),h.P(i,W)],fill=(255,255,255,50));d.line([h.P(0,i),h.P(W,i)],fill=(255,255,255,50))
    im=Image.alpha_composite(im,ov).convert('RGB')
    box=eval(sys.argv[1]) if len(sys.argv)>1 else None
    if box: im=im.crop(box).resize(((box[2]-box[0])*2,(box[3]-box[1])*2),Image.LANCZOS)
    im.save(sys.argv[2] if len(sys.argv)>2 else 'chk.png')
    print('\n'.join(MAP))
