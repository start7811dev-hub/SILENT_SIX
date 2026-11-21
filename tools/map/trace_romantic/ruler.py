import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
from PIL import Image, ImageDraw
def ruler(k):
    im = Image.open(os.path.join(lib.SRC, 'bgp_%s_%s.jpg' % (k[:-1], k[-1]))).convert('RGBA'); ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov); f = lib.font(11)
    for x in range(0, 1536, 50):
        d.line([(x, 0), (x, 1024)], fill=(255, 255, 255, 80 if x % 100 == 0 else 30))
        if x % 100 == 0:
            for y in (4, 340, 680, 1008): d.text((x + 2, y), str(x), fill=(255, 255, 0, 255), font=f, stroke_width=2, stroke_fill=(0, 0, 0, 255))
    for y in range(0, 1024, 50):
        d.line([(0, y), (1536, y)], fill=(255, 255, 255, 80 if y % 100 == 0 else 30))
        if y % 100 == 0:
            for x in (2, 510, 1020, 1500): d.text((x, y + 2), str(y), fill=(0, 255, 255, 255), font=f, stroke_width=2, stroke_fill=(0, 0, 0, 255))
    Image.alpha_composite(im, ov).convert('RGB').save(os.path.join(lib.OUT, 'ruler_%s.jpg' % k), quality=86)
for k in sys.argv[1:]: ruler(k)
