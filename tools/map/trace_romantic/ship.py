import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib, numpy as np
from PIL import Image, ImageDraw
SRCP = [(5, 2), (5, 12), (30, 0), (30, 14)]; DSTP = [(480, 85), (215, 215), (1375, 715), (925, 945)]
def proj(): return lib.ProjH(30, 14, SRCP, DSTP)
if __name__ == '__main__':
    pr = proj(); HI = np.linalg.inv(pr.H)
    for n, p in [('A stbd', (1090, 458)), ('A port', (640, 640)), ('bow tip', (240, 60))]:
        v = HI @ np.array([p[0], p[1], 1.0]); print(n, round(v[0] / v[2], 1), round(v[1] / v[2], 1))
    im = Image.open(os.path.join(lib.SRC, 'bgp_mirage_1.jpg')).convert('RGBA'); ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov); f = lib.font(10)
    for i in range(31): d.line([pr.P(i, 0), pr.P(i, 14)], fill=(255, 255, 0, 170) if i % 5 == 0 else (0, 255, 255, 90))
    for j in range(15): d.line([pr.P(0, j), pr.P(30, j)], fill=(255, 255, 0, 170) if j % 5 == 0 else (0, 255, 255, 90))
    for y in range(14):
        for x in range(30):
            p = pr.P(x + .5, y + .5); t = '%d,%d' % (x, y); d.text((p[0] - 2.8 * len(t), p[1] - 5), t, fill=(255, 255, 255, 240), font=f, stroke_width=1, stroke_fill=(0, 0, 0, 255))
    o = Image.alpha_composite(im, ov).convert('RGB').crop((100, 0, 1436, 1000)); o = o.resize((1536, int(1000 * 1536 / 1336)), Image.LANCZOS); o.save(os.path.join(lib.OUT, 'zc_mirage1.jpg'), quality=86)
