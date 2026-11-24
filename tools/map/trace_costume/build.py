# 코스튬 맵: 소품 시트 → 낱개 → 배경에 굽기 + 격자 갱신
import sys, json, importlib.util, numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
sys.path.insert(0, '/home/claude/cw'); import ov
ART = '/home/claude/cart/art/'; W = '/home/claude/cw/work/'; OUT = '/home/claude/cw/out/'
def trim(im):
    a = np.asarray(im)[..., 3]; ys, xs = np.where(a > 20)
    return im.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
def sprites(a):
    SP = {}
    for key, sh in (('c', 'cover'), ('s', 'show'), ('x', 'special')):
        im = Image.open(ART + '%s/p_c_%s_%s.png' % (a, a, sh)).convert('RGBA')
        for i in range(6):
            c = im.crop(((i % 3) * 512, (i // 3) * 512, (i % 3) * 512 + 512, (i // 3) * 512 + 512))
            if np.asarray(c)[..., 3].max() < 30: continue
            SP[key + str(i)] = trim(c)
    return SP
def place(base, H, sp, x, y, w, hh, dark=0.92, sc=1.0, shadow=True, alpha=1.0, lift=0):
    P = lambda a, b: ov.P(H, a, b)
    L = P(x, y + hh); R = P(x + w, y); B = P(x + w, y + hh); T = P(x, y)
    fw = (R[0] - L[0]) * sc; k = fw / sp.width * 1.02
    im = sp.resize((max(1, round(sp.width * k)), max(1, round(sp.height * k))), Image.LANCZOS)
    r, g, b, al = im.split(); rgb = Image.merge('RGB', (r, g, b)); rgb = ImageEnhance.Brightness(rgb).enhance(dark); rgb = ImageEnhance.Color(rgb).enhance(0.92)
    if alpha < 1: al = al.point(lambda v: int(v * alpha))
    im = Image.merge('RGBA', (*rgb.split(), al))
    if shadow:
        sh = Image.new('RGBA', base.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
        d.polygon([(L[0] - 3, L[1]), (T[0], T[1] - 2), (R[0] + 3, R[1]), (B[0], B[1] + 3)], fill=(0, 0, 0, 110)); sh = sh.filter(ImageFilter.GaussianBlur(3))
        base.alpha_composite(sh)
    cx = (L[0] + R[0]) / 2
    base.alpha_composite(im, (round(cx - im.width / 2), round(B[1] + 2 - im.height - lift)))
def person(base, H, sp, x, y, hpx=58, dark=0.95):
    """사람 하나: 칸 중심 발 위치, 키 hpx 픽셀"""
    k = hpx / sp.height; im = sp.resize((max(1, round(sp.width * k)), hpx), Image.LANCZOS)
    r, g, b, al = im.split(); rgb = ImageEnhance.Brightness(Image.merge('RGB', (r, g, b))).enhance(dark); im = Image.merge('RGBA', (*rgb.split(), al))
    fx, fy = ov.P(H, x + 0.5, y + 0.5)
    sh = Image.new('RGBA', base.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh); d.ellipse((fx - 13, fy - 5, fx + 13, fy + 5), fill=(0, 0, 0, 120)); sh = sh.filter(ImageFilter.GaussianBlur(2)); base.alpha_composite(sh)
    base.alpha_composite(im, (round(fx - im.width / 2), round(fy + 3 - im.height)))
def build(a, spec):
    H = ov.H_of(a); SP = sprites(a)
    base = Image.open(W + 'bg_%s.jpg' % a).convert('RGBA')
    g = [list(r) for r in json.load(open(W + 'map_%s.json' % a))['MAP']]
    items = []
    for p in spec.DECO: items.append(('d', p))
    for p in spec.PR: items.append(('p', p))
    for p in spec.NPC: items.append(('n', p))
    for p in spec.TGT: items.append(('t', p))
    def depth(it):
        k, p = it
        if k == 'n': return p[1] + p[2] + 1
        if k == 't': return p[0] + p[1] + 1
        o = p[5] if (k == 'd' and len(p) > 5) else {}
        return p[1] + p[2] + (p[3] + p[4]) / 2 + (-50 if o.get('under') else 0)
    for k, p in sorted(items, key=depth):
        if k == 'd': place(base, H, SP[p[0]], *p[1:5], **{q: v for q, v in (p[5] if len(p) > 5 else {}).items() if q != 'under'})
        elif k == 'p': place(base, H, SP[p[0]], *p[1:5], **(p[6] if len(p) > 6 else {}))
        elif k == 'n': person(base, H, SP[p[0]], p[1], p[2], hpx=p[3] if len(p) > 3 else 58)
        elif k == 't': place(base, H, SP['x0'], p[0], p[1], 1, 1, dark=1.0, sc=0.95)
    def setc(x, y, c, who):
        assert g[y][x] == '.', (a, who, x, y, g[y][x]); g[y][x] = c
    for p in spec.PR:
        for j in range(p[4]):
            for i in range(p[3]): setc(p[1] + i, p[2] + j, p[5], p[0])
    for p in spec.NPC: setc(p[1], p[2], 'N', p[0])
    for p in spec.TGT: setc(p[0], p[1], 'X', 'tgt')
    MAP = [''.join(r) for r in g]
    base.convert('RGB').save(OUT + 'bgc_%s.jpg' % a, quality=86)
    proj = [round(float(v), 9) for v in H.flatten()]
    json.dump({'MAP': MAP, 'proj': proj}, open(W + 'final_%s.json' % a, 'w'))
    # 런타임 그림: 함정 표시
    for name, key, wd in getattr(spec, 'RUNTIME', []):
        s = SP[key]; s.resize((wd, round(s.height * wd / s.width)), Image.LANCZOS).save(OUT + name, optimize=True)
    return MAP
if __name__ == '__main__':
    a = sys.argv[1]
    sp = importlib.util.spec_from_file_location('s', '/home/claude/cw/maps/s_%s.py' % a); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    M = build(a, m)
    print('\n'.join('%2d %s' % (i, r) for i, r in enumerate(M)))
