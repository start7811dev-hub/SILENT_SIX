import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
from PIL import Image
# 사용: ov.py <키> <W> <Hh> Tx,Ty Rx,Ry Lx,Ly Bx,By [crop x0,y0,x1,y1 scale]
k = sys.argv[1]; W = int(sys.argv[2]); Hh = int(sys.argv[3])
pts = [tuple(float(v) for v in a.split(',')) for a in sys.argv[4:8]]
pr = lib.Proj(W, Hh, *pts)
im = Image.open(os.path.join(lib.SRC, 'bgp_%s_%s.jpg' % (k[:-1], k[-1])))
o = lib.overlay(im, pr)
if len(sys.argv) > 8:
    x0, y0, x1, y1 = [int(v) for v in sys.argv[8].split(',')]; s = float(sys.argv[9]) if len(sys.argv) > 9 else 2
    o = o.crop((x0, y0, x1, y1)); o = o.resize((int(o.width * s), int(o.height * s)), Image.LANCZOS)
o.save(os.path.join(lib.OUT, 'ov_%s.jpg' % k), quality=88)
