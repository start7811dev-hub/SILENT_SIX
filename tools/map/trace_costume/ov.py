import sys, json, numpy as np
from PIL import Image, ImageDraw, ImageFont
N = 33
W = '/home/claude/cw/work/'
def cfg(): return json.load(open(W + 'cfg.json'))
def homog(src, dst):
    A = []; b = []
    for (x, y), (u, v) in zip(src, dst):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); b.append(u); A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); b.append(v)
    h = np.linalg.solve(np.array(A, float), np.array(b, float)); return np.append(h, 1).reshape(3, 3)
def H_of(a, plane='floor'):
    c = cfg()[a]; d = c['dy'] if plane == 'floor' else 0
    T, L, R, B = c['T'], c['L'], c['R'], c['B']
    # 꼭짓점은 외곽 벽 윗면의 바깥 모서리. 바닥면은 벽 높이(dy)만큼 아래. B(앞 모서리)는 이미 바닥이라 bdy 만큼만.
    return homog([(0, 0), (0, N), (N, 0), (N, N)], [(T[0], T[1] + d), (L[0], L[1] + d), (R[0], R[1] + d), (B[0], B[1] + c.get('bdy', 0) * (d > 0))])
def P(H, x, y):
    p = H @ np.array([x, y, 1.0]); return (p[0] / p[2], p[1] / p[2])
def font(s):
    try: return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', s)
    except Exception: return ImageFont.load_default()
COL = {'#': (255, 40, 40, 95), 'C': (255, 220, 0, 95), 'B': (255, 120, 0, 95), 'J': (255, 140, 200, 95), 'V': (40, 80, 255, 95), 'X': (0, 255, 0, 140), 'W': (60, 140, 255, 110), 'S': (0, 255, 255, 90), 'T': (255, 0, 255, 120), 'Z': (120, 255, 120, 60)}
def overlay(a, out, MAP=None, box=None, s=1.0, base=None, extra=None):
    im = Image.open(base or (W + 'bg_%s.jpg' % a)).convert('RGB')
    H = H_of(a); ox, oy = (box[0], box[1]) if box else (0, 0)
    if box: im = im.crop(box)
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS); d = ImageDraw.Draw(im, 'RGBA')
    Q = lambda x, y: ((P(H, x, y)[0] - ox) * s, (P(H, x, y)[1] - oy) * s)
    if MAP:
        for y in range(len(MAP)):
            for x in range(len(MAP[0])):
                ch = MAP[y][x]
                if ch == '.': continue
                d.polygon([Q(x, y), Q(x + 1, y), Q(x + 1, y + 1), Q(x, y + 1)], fill=COL.get(ch, (255, 255, 255, 90)))
    if extra:
        for (x, y, col) in extra:
            d.polygon([Q(x, y), Q(x + 1, y), Q(x + 1, y + 1), Q(x, y + 1)], fill=col)
    f = font(int(9 * s))
    for i in range(N + 1):
        c = (255, 255, 0, 210) if i % 5 == 0 else (0, 255, 255, 110)
        d.line([Q(i, 0), Q(i, N)], fill=c, width=1); d.line([Q(0, i), Q(N, i)], fill=c, width=1)
    for i in range(N):
        a1 = Q(i + .5, -.7); d.text((a1[0] - 5, a1[1] - 6), str(i), fill=(255, 255, 255), font=f)
        a1 = Q(-.8, i + .5); d.text((a1[0] - 6, a1[1] - 6), str(i), fill=(255, 255, 255), font=f)
        a1 = Q(i + .5, N + .6); d.text((a1[0] - 5, a1[1] - 6), str(i), fill=(255, 255, 0), font=f)
        a1 = Q(N + .8, i + .5); d.text((a1[0] - 6, a1[1] - 6), str(i), fill=(255, 255, 0), font=f)
    if s > 1.4:
        for y in range(N):
            for x in range(N):
                if (x + y) % 2 == 0:
                    a1 = Q(x + .5, y + .5); d.text((a1[0] - 9, a1[1] - 5), '%d,%d' % (x, y), fill=(255, 255, 255, 190), font=font(int(5.5 * s)))
    im.save(out)
BOX = {'t': (384, 0, 1152, 512), 'l': (0, 256, 768, 768), 'r': (768, 256, 1536, 768), 'b': (384, 512, 1152, 1024), 'c': (384, 256, 1152, 768)}
if __name__ == '__main__':
    a = sys.argv[1]; mode = sys.argv[2] if len(sys.argv) > 2 else 'full'
    MAP = None
    try: MAP = json.load(open(W + 'map_%s.json' % a))['MAP']
    except Exception: pass
    if mode == 'full': overlay(a, W + 'ov_%s.png' % a, MAP)
    else: overlay(a, W + 'ov_%s_%s.png' % (a, mode), MAP, box=BOX[mode], s=2)
