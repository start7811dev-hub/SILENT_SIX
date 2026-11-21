# -*- coding: utf-8 -*-
"""로맨틱 미션 맵 추적 공용 함수: 투영(호모그래피), 격자 덧그림, 소품 낱개 분리 · 배치."""
import os, json, math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont
HERE_ = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get('RSRC', os.path.join(HERE_, 'src'))          # bgp_<요원>_<판>.jpg (assets.py 가 넣는다)
PSRC = os.environ.get('RPSRC', '')      # 받은 원본 폴더(props/, portraits/). assets.py 를 돌릴 때만 필요하다
OUT = os.environ.get('ROUT', '/tmp/trace_romantic')   # 격자 확인용 그림이 나오는 곳
os.makedirs(OUT, exist_ok=True)
AG = ['raven', 'viper', 'glitch', 'brick', 'mirage', 'doc']

def homog(src, dst):
    A = []; b = []
    for (x, y), (u, v) in zip(src, dst):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); b.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); b.append(v)
    h = np.linalg.solve(np.array(A, float), np.array(b, float)); return np.append(h, 1).reshape(3, 3)

class Proj:
    """격자 (0,0)=TOP, (W,0)=RIGHT, (0,W)=LEFT, (W,W)=BOTTOM. 직사각형이면 (W,Hh)."""
    def __init__(self, W, Hh, T, R, L, B):
        self.W, self.Hh = W, Hh
        self.H = homog([(0, 0), (W, 0), (0, Hh), (W, Hh)], [T, R, L, B])
    def P(self, x, y):
        p = self.H @ np.array([x, y, 1.0]); return (p[0] / p[2], p[1] / p[2])
    def flat(self):
        return [round(float(v), 9) for v in self.H.flatten()]

def font(sz):
    for f in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',):
        if os.path.exists(f): return ImageFont.truetype(f, sz)
    return ImageFont.load_default()

def overlay(im, pr, MAP=None, col=None, labels=True, marks=None):
    im = im.convert('RGBA'); ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    W, Hh = pr.W, pr.Hh
    if MAP:
        for y in range(Hh):
            for x in range(W):
                c = MAP[y][x]
                if c != '.':
                    cc = (col or {}).get(c, (255, 60, 60))
                    d.polygon([pr.P(x + .08, y + .08), pr.P(x + .92, y + .08), pr.P(x + .92, y + .92), pr.P(x + .08, y + .92)], fill=cc + (70,), outline=cc + (230,))
    for i in range(W + 1):
        c = (255, 0, 255, 200) if i % 10 == 0 else (255, 255, 0, 170) if i % 5 == 0 else (0, 255, 255, 70)
        d.line([pr.P(i, 0), pr.P(i, Hh)], fill=c, width=2 if i % 5 == 0 else 1)
    for j in range(Hh + 1):
        c = (255, 0, 255, 200) if j % 10 == 0 else (255, 255, 0, 170) if j % 5 == 0 else (0, 255, 255, 70)
        d.line([pr.P(0, j), pr.P(W, j)], fill=c, width=2 if j % 5 == 0 else 1)
    if labels:
        f = font(11)
        for i in range(W):
            p = pr.P(i + .5, Hh + .9); d.text((p[0] - 6, p[1] - 6), str(i), fill=(255, 255, 255, 255) if i % 5 else (255, 255, 0, 255), font=f)
        for j in range(Hh):
            p = pr.P(W + .9, j + .5); d.text((p[0] - 4, p[1] - 6), str(j), fill=(255, 255, 255, 255) if j % 5 else (255, 255, 0, 255), font=f)
        f2 = font(10)
        for i in range(0, W, 5):
            for j in range(0, Hh, 5):
                p = pr.P(i + .5, j + .5); d.text((p[0] - 10, p[1] - 5), '%d,%d' % (i, j), fill=(255, 255, 255, 255), font=f2, stroke_width=2, stroke_fill=(0, 0, 0, 255))
    for m in (marks or []):
        p = pr.P(m[0] + .5, m[1] + .5); d.ellipse([p[0] - 6, p[1] - 6, p[0] + 6, p[1] + 6], outline=m[2] if len(m) > 2 else (0, 255, 0, 255), width=3)
        if len(m) > 3: d.text((p[0] + 7, p[1] - 6), m[3], fill=(255, 255, 255, 255), font=font(11), stroke_width=2, stroke_fill=(0, 0, 0, 255))
    return Image.alpha_composite(im, ov).convert('RGB')

def auto_corners(path):
    """가까운 두 변(낮은 경계)의 바닥 꼭짓점 L, R, B를 잡고 T는 평행사변형으로 둔다."""
    import cv2
    im = np.asarray(Image.open(path).convert('L'))
    m = (cv2.GaussianBlur(im, (5, 5), 0) > 34).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m, 8)
    k = 1 + int(np.argmax(st[1:, 4])); m = (lab == k)
    ys, xs = np.nonzero(m)
    x0, x1, y1 = xs.min(), xs.max(), ys.max()
    L = (float(x0), float(ys[xs <= x0 + 4].max())); R = (float(x1), float(ys[xs >= x1 - 4].max()))
    B = (float(np.median(xs[ys >= y1 - 3])), float(y1))
    T = (L[0] + R[0] - B[0], L[1] + R[1] - B[1])
    return T, R, L, B

# ---------- 소품 ----------
def despill(im):
    """반투명 가장자리에 남은 키 색(자홍 · 녹색)을 덜어 낸다."""
    a = np.asarray(im.convert('RGBA')).astype(np.float32); r, g, b, al = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    edge = al < 250
    mg = np.minimum(r, b) - g; e = edge & (mg > 12)
    lim = g + (np.minimum(r, b) - g) * 0.25
    r = np.where(e, np.minimum(r, lim + (r - np.minimum(r, b))), r); b = np.where(e, np.minimum(b, lim + (b - np.minimum(r, b))), b)
    gk = g - np.maximum(r, b); e2 = edge & (gk > 6)
    g = np.where(e2, np.maximum(r, b) + 2, g)
    return Image.fromarray(np.dstack([r, g, b, al]).clip(0, 255).astype(np.uint8), 'RGBA')

def trim(im, thr=24):
    a = np.asarray(im)[..., 3]; ys, xs = np.where(a > thr)
    return im.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))

_SP = {}
def sprites(ag, take):
    """{'c0'..'c5','s0'..'s5'} 낱개(잘라 낸 RGBA)."""
    key = (ag, take)
    rd = os.path.join(HERE_, 'sprites', '%s%d' % (ag, take))
    if key not in _SP and os.path.isdir(rd) and not os.environ.get('RPSRC'):
        _SP[key] = {f[:-5]: Image.open(os.path.join(rd, f)).convert('RGBA') for f in os.listdir(rd) if f.endswith('.webp')}
    if key not in _SP:
        d = {}
        for kind, pre in (('cover', 'c'), ('special', 's')):
            im = despill(Image.open(os.path.join(PSRC, 'props', 'p_r_%s%d_%s.png' % (ag, take, kind))))
            for i in range(6):
                c = im.crop(((i % 3) * 512, (i // 3) * 512, (i % 3) * 512 + 512, (i // 3) * 512 + 512))
                d[pre + str(i)] = trim(c)
        _SP[key] = d
    return _SP[key]

def place(base, pr, sp, x, y, w, hh, dark=0.9, tint=(1, 1, 1), scale=1.0, up=0, shadow=110):
    """발자국 (x,y,w,hh)에 낱개를 올린다. 발자국의 화면 폭에 그림 폭을 맞춘다."""
    L = pr.P(x, y + hh); Rr = pr.P(x + w, y); Bm = pr.P(x + w, y + hh); T = pr.P(x, y)
    fw = (Rr[0] - L[0]) * scale; k = fw / sp.width * 1.02
    im = sp.resize((max(1, round(sp.width * k)), max(1, round(sp.height * k))), Image.LANCZOS)
    r, g, b, a = im.split(); rgb = Image.merge('RGB', (r, g, b)); rgb = ImageEnhance.Brightness(rgb).enhance(dark)
    arr = np.asarray(rgb).astype(np.float32) * np.array(tint); rgb = Image.fromarray(arr.clip(0, 255).astype(np.uint8))
    im = Image.merge('RGBA', (*rgb.split(), a))
    cx = (L[0] + Rr[0]) / 2
    if shadow:
        sh = Image.new('RGBA', base.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
        d.polygon([(L[0] - 3, L[1]), (T[0], T[1] - 2), (Rr[0] + 3, Rr[1]), (Bm[0], Bm[1] + 3)], fill=(0, 0, 0, shadow)); sh = sh.filter(ImageFilter.GaussianBlur(3))
        base.alpha_composite(sh)
    base.alpha_composite(im, (round(cx - im.width / 2), round(Bm[1] + 2 - up - im.height)))

def near_corners(path, thr=30):
    """가까운 두 변의 아랫선을 직선으로 맞춰 L, R, B(바닥 바깥 꼭짓점)를 구하고 T는 평행사변형으로 둔다."""
    import cv2
    im = np.asarray(Image.open(path).convert('L'))
    m = (cv2.GaussianBlur(im, (5, 5), 0) > thr).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m, 8); k = 1 + int(np.argmax(st[1:, 4])); m = (lab == k)
    ys, xs = np.nonzero(m); x0, x1 = xs.min(), xs.max()
    low = np.full(m.shape[1], -1)
    for x in range(x0, x1 + 1):
        c = np.nonzero(m[:, x])[0]
        if len(c): low[x] = c.max()
    bx = int(np.argmax(low)); by = low[bx]
    def fit(a, b):
        X = np.arange(a, b); Y = low[a:b]; ok = Y > 0; X, Y = X[ok], Y[ok]
        for _ in range(3):
            p = np.polyfit(X, Y, 1); r = np.abs(np.polyval(p, X) - Y); keep = r < max(2.5, np.percentile(r, 70)); X, Y = X[keep], Y[keep]
        return p
    pl = fit(x0 + 50, bx - 60); prr = fit(bx + 60, x1 - 50)
    Bx = (prr[1] - pl[1]) / (pl[0] - prr[0]); By = np.polyval(pl, Bx)
    L = (float(x0), float(np.polyval(pl, x0))); R = (float(x1), float(np.polyval(prr, x1)))
    B = (float(Bx), float(By)); T = (L[0] + R[0] - B[0], L[1] + R[1] - B[1])
    return T, R, L, B

class ProjH(Proj):
    """임의의 네 대응점으로 만든 투영. src: 격자 좌표 4개, dst: 그림 좌표 4개."""
    def __init__(self, W, Hh, src, dst):
        self.W, self.Hh = W, Hh; self.H = homog(src, dst)

def orient(sp):
    """낱개의 긴 변 방향: +1 = 오른쪽 아래(+x), -1 = 왼쪽 아래(+y), 0 = 판단 어려움. 바닥 쪽 절반의 윤곽으로 본다."""
    a = np.asarray(sp)[..., 3] > 60; ys, xs = np.nonzero(a)
    if len(xs) < 50: return 0
    keep = ys > ys.min() + (ys.max() - ys.min()) * 0.45; xs, ys = xs[keep].astype(float), ys[keep].astype(float)
    c = np.cov(np.vstack([xs, ys]))[0, 1]; r = c / (xs.std() * ys.std() + 1e-6)
    return 1 if r > 0.25 else -1 if r < -0.25 else 0
