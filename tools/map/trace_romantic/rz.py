import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
from PIL import Image, ImageDraw
# 사용: rz.py <키> x0,y0,x1,y1 [간격]  → 지정 영역 확대 + 원본 좌표 눈금
k = sys.argv[1]; box = [int(v) for v in sys.argv[2].split(',')]; st = int(sys.argv[3]) if len(sys.argv) > 3 else 50
im = Image.open(os.path.join(lib.SRC, 'bgp_%s_%s.jpg' % (k[:-1], k[-1]))).convert('RGB').crop(box)
s = min(1536 / im.width, 1536 / im.height); im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS).convert('RGBA')
ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov); f = lib.font(12)
for x in range((box[0] // st + 1) * st, box[2], st):
    X = (x - box[0]) * s; d.line([(X, 0), (X, im.height)], fill=(255, 255, 255, 90 if x % 100 == 0 else 40))
    for Y in range(4, im.height, 330): d.text((X + 2, Y), str(x), fill=(255, 255, 0, 255), font=f, stroke_width=2, stroke_fill=(0, 0, 0, 255))
for y in range((box[1] // st + 1) * st, box[3], st):
    Y = (y - box[1]) * s; d.line([(0, Y), (im.width, Y)], fill=(255, 255, 255, 90 if y % 100 == 0 else 40))
    for X in range(2, im.width, 420): d.text((X, Y + 2), str(y), fill=(0, 255, 255, 255), font=f, stroke_width=2, stroke_fill=(0, 0, 0, 255))
Image.alpha_composite(im, ov).convert('RGB').save(os.path.join(lib.OUT, 'rz_%s.jpg' % k), quality=86)
