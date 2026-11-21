import sys, os, colorsys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib, numpy as np, cv2
from PIL import Image
def cellmap(k, W, pts, lift=0, Hh=None):
    Hh = Hh or W; pr = lib.Proj(W, Hh, *pts); a = np.asarray(Image.open(os.path.join(lib.SRC, 'bgp_%s_%s.jpg' % (k[:-1], k[-1]))).convert('RGB')).astype(np.float32)
    out = []
    for y in range(Hh):
        row = ''
        for x in range(W):
            q = np.array([pr.P(x + .25, y + .25), pr.P(x + .75, y + .25), pr.P(x + .75, y + .75), pr.P(x + .25, y + .75)]); q[:, 1] -= lift; q = q.astype(np.int32)
            x0, y0 = q.min(0); x1, y1 = q.max(0)
            if x0 < 0 or y0 < 0 or x1 >= a.shape[1] or y1 >= a.shape[0]: row += '?'; continue
            m = np.zeros((y1 - y0 + 1, x1 - x0 + 1), np.uint8); cv2.fillPoly(m, [q - [x0, y0]], 1)
            c = a[y0:y1 + 1, x0:x1 + 1][m > 0].mean(0); h, s, v = colorsys.rgb_to_hsv(*(c / 255))
            sd = a[y0:y1 + 1, x0:x1 + 1][m > 0].std(0).mean()
            if v < 0.16: ch = '#'
            elif s > 0.38 and 0.5 < h < 0.72: ch = 'b'
            elif s > 0.42 and (h < 0.12 or h > 0.95): ch = 'o'
            elif v < 0.28: ch = ':'
            else: ch = '.'
            row += ch
        out.append(row)
    return out
if __name__ == '__main__':
    k = sys.argv[1]; W = int(sys.argv[2]); pts = [tuple(float(v) for v in p.split(',')) for p in sys.argv[3:7]]; lift = int(sys.argv[7]) if len(sys.argv) > 7 else 0
    print('    ' + ''.join(str(i % 10) for i in range(W)))
    for i, r in enumerate(cellmap(k, W, pts, lift)): print('%2d  %s' % (i, r))
