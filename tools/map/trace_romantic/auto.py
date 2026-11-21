# -*- coding: utf-8 -*-
"""벽 윗면(어두운 평면)을 찾아 벽 높이만큼 내려서 격자에 얹는 초안 생성기."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib, numpy as np, cv2
from PIL import Image
def top_mask(im, seeds, tol):
    a = np.asarray(im.convert('RGB')).astype(np.float32); m = np.zeros(a.shape[:2], bool)
    lab = cv2.cvtColor(a.astype(np.uint8), cv2.COLOR_RGB2LAB).astype(np.float32)
    for (x, y) in seeds:
        c = np.median(lab[y - 2:y + 3, x - 2:x + 3].reshape(-1, 3), axis=0)
        d = np.sqrt((((lab - c) * np.array([0.7, 1.4, 1.4])) ** 2).sum(-1)); m |= d < tol
    m = cv2.morphologyEx(m.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    return m.astype(bool)
def to_grid(mask, pr, h, thr=0.45, ch='#'):
    W, Hh = pr.W, pr.Hh; sh = np.zeros_like(mask); sh[h:, :] = mask[:-h, :] if h else mask
    g = [['.'] * W for _ in range(Hh)]; cov = np.zeros((Hh, W))
    for y in range(Hh):
        for x in range(W):
            q = np.array([pr.P(x + .15, y + .15), pr.P(x + .85, y + .15), pr.P(x + .85, y + .85), pr.P(x + .15, y + .85)], np.int32)
            x0, y0 = q.min(0); x1, y1 = q.max(0)
            if x1 <= x0 or y1 <= y0 or x0 < 0 or y0 < 0 or x1 >= mask.shape[1] or y1 >= mask.shape[0]: continue
            cm = np.zeros((y1 - y0 + 1, x1 - x0 + 1), np.uint8); cv2.fillPoly(cm, [q - [x0, y0]], 1)
            sub = sh[y0:y1 + 1, x0:x1 + 1]; c = (sub & (cm > 0)).sum() / max(1, cm.sum()); cov[y, x] = c
            if c >= thr: g[y][x] = ch
    return g, cov
if __name__ == '__main__':
    k = sys.argv[1]; W = int(sys.argv[2]); pts = [tuple(float(v) for v in a.split(',')) for a in sys.argv[3:7]]
    seeds = [tuple(int(v) for v in a.split(',')) for a in sys.argv[7].split(';')]; tol = float(sys.argv[8]); h = int(sys.argv[9])
    pr = lib.Proj(W, W, *pts); im = Image.open(os.path.join(lib.SRC, 'bgp_%s_%s.jpg' % (k[:-1], k[-1])))
    m = top_mask(im, seeds, tol); g, cov = to_grid(m, pr, h)
    MAP = [''.join(r) for r in g]; print('\n'.join('%2d %s' % (i, r) for i, r in enumerate(MAP)))
    lib.overlay(im, pr, MAP, labels=True).save(os.path.join(lib.OUT, 'auto_%s.jpg' % k), quality=85)
    Image.fromarray((m * 255).astype(np.uint8)).save(os.path.join(lib.OUT, 'mask_%s.png' % k))
