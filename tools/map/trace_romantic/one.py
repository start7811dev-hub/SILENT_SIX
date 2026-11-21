import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
from PIL import Image, ImageDraw
# 사용: one.py <키> <W> T R L B [lift]  → 칸마다 좌표가 적힌 한 장
k = sys.argv[1]; W = int(sys.argv[2]); pts = [tuple(float(v) for v in a.split(',')) for a in sys.argv[3:7]]; lift = int(sys.argv[7]) if len(sys.argv) > 7 else 0
pr = lib.Proj(W, W, *pts); im = Image.open(os.path.join(lib.SRC, 'bgp_%s_%s.jpg' % (k[:-1], k[-1]))).convert('RGBA')
ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov); f = lib.font(9)
Q = lambda x, y: (pr.P(x, y)[0], pr.P(x, y)[1] - lift)
for i in range(W + 1):
    c = (255, 255, 0, 170) if i % 5 == 0 else (0, 255, 255, 80)
    d.line([Q(i, 0), Q(i, W)], fill=c, width=1); d.line([Q(0, i), Q(W, i)], fill=c, width=1)
for y in range(W):
    for x in range(W):
        p = Q(x + .5, y + .5); t = '%d,%d' % (x, y); d.text((p[0] - 2.6 * len(t), p[1] - 5), t, fill=(255, 255, 255, 240), font=f, stroke_width=1, stroke_fill=(0, 0, 0, 255))
Image.alpha_composite(im, ov).convert('RGB').save(os.path.join(lib.OUT, 'one_%s.png' % k))
