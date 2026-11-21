import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
from PIL import Image, ImageDraw
# 사용: zc.py <키> <W> T R L B lift x0,y0,x1,y1 [Hh] → 지정 영역 확대(가로 1536)
k = sys.argv[1]; W = int(sys.argv[2]); pts = [tuple(float(v) for v in a.split(',')) for a in sys.argv[3:7]]; lift = int(sys.argv[7]); box = [int(v) for v in sys.argv[8].split(',')]
Hh = int(sys.argv[9]) if len(sys.argv) > 9 else W
pr = lib.Proj(W, Hh, *pts); im = Image.open(os.path.join(lib.SRC, 'bgp_%s_%s.jpg' % (k[:-1], k[-1]))).convert('RGB').crop(box)
s = min(1536 / im.width, 1536 / im.height); im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS).convert('RGBA')
ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov); f = lib.font(max(9, int(6.5 * s)))
Q = lambda x, y: ((pr.P(x, y)[0] - box[0]) * s, (pr.P(x, y)[1] - lift - box[1]) * s)
for i in range(W + 1): d.line([Q(i, 0), Q(i, Hh)], fill=(255, 255, 0, 150) if i % 5 == 0 else (0, 255, 255, 80), width=1)
for j in range(Hh + 1): d.line([Q(0, j), Q(W, j)], fill=(255, 255, 0, 150) if j % 5 == 0 else (0, 255, 255, 80), width=1)
for y in range(Hh):
    for x in range(W):
        p = Q(x + .5, y + .5)
        if 0 < p[0] < im.width and 0 < p[1] < im.height:
            t = '%d,%d' % (x, y); d.text((p[0] - 3.2 * len(t) * s / 1.5, p[1] - 6), t, fill=(255, 255, 255, 240), font=f, stroke_width=2, stroke_fill=(0, 0, 0, 220))
Image.alpha_composite(im, ov).convert('RGB').save(os.path.join(lib.OUT, 'zc_%s.jpg' % k), quality=85)
