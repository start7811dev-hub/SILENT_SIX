import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
from PIL import Image, ImageDraw
# 사용: zoom.py <키> <W> <Hh> T R L B  → 왼쪽 · 오른쪽 확대 두 장(칸마다 좌표)
def run(k, W, Hh, pts, s=1.5, halves=(('a', 0, 1024), ('b', 512, 1536)), MAP=None, lift=0, tag='z'):
    pr = lib.Proj(W, Hh, *pts)
    im = Image.open(os.path.join(lib.SRC, 'bgp_%s_%s.jpg' % (k[:-1], k[-1]))).convert('RGB')
    for name, x0, x1 in halves:
        c = im.crop((x0, 0, x1, 1024)); c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS).convert('RGBA')
        ov = Image.new('RGBA', c.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov); f = lib.font(11)
        Q = lambda x, y: ((pr.P(x, y)[0] - x0) * s, (pr.P(x, y)[1] - lift) * s)
        for i in range(W + 1):
            d.line([Q(i, 0), Q(i, Hh)], fill=(255, 255, 0, 150) if i % 5 == 0 else (0, 255, 255, 95), width=2 if i % 5 == 0 else 1)
        for j in range(Hh + 1):
            d.line([Q(0, j), Q(W, j)], fill=(255, 255, 0, 150) if j % 5 == 0 else (0, 255, 255, 95), width=2 if j % 5 == 0 else 1)
        for y in range(Hh):
            for x in range(W):
                p = Q(x + .5, y + .5)
                if -20 < p[0] < c.width + 20 and -20 < p[1] < c.height + 20:
                    if MAP and MAP[y][x] != '.':
                        d.polygon([Q(x + .1, y + .1), Q(x + .9, y + .1), Q(x + .9, y + .9), Q(x + .1, y + .9)], fill=(255, 40, 40, 60), outline=(255, 60, 60, 220))
                    t = '%d,%d' % (x, y); d.text((p[0] - 3 * len(t), p[1] - 6), t, fill=(255, 255, 255, 235), font=f, stroke_width=2, stroke_fill=(0, 0, 0, 200))
        Image.alpha_composite(c, ov).convert('RGB').save(os.path.join(lib.OUT, '%s_%s_%s.jpg' % (tag, k, name)), quality=84)
if __name__ == '__main__':
    k = sys.argv[1]; W = int(sys.argv[2]); Hh = int(sys.argv[3])
    pts = [tuple(float(v) for v in a.split(',')) for a in sys.argv[4:8]]
    lift = int(sys.argv[8]) if len(sys.argv) > 8 else 0
    run(k, W, Hh, pts, lift=lift, tag='zl' if lift else 'z')
