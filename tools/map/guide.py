# -*- coding: utf-8 -*-
"""maps.py 의 타일 설계를 1536x1024 가이드 이미지와 maps.json 으로 만든다.
사용: python3 tools/map/guide.py <출력 폴더>
게임에서 쓰는 투영: iso(84 + rows*36, 200, 72, 36)  (칸 72x36)
"""
import sys, os, json
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import maps as MP

TW, TH, OY = 72, 36, 200
FLAT = {'.': (46, 54, 64), '=': (150, 120, 60), '~': (60, 130, 170), 'S': (40, 190, 100), 'V': (10, 22, 48)}
BLOCK = {'#': ((150, 160, 175), 46), 'B': ((70, 150, 125), 40), 'C': ((190, 145, 80), 22), 'W': ((235, 205, 50), 46), 'X': ((60, 235, 220), 58)}
BG = (6, 8, 11)


def rows_of(m):
    return m['raw'] if 'raw' in m else MP.build(m)


def proj(m):
    cols, rows = m['size']
    return [TW / 2, -TW / 2, 84 + rows * TW / 2, TH / 2, TH / 2, OY, 0, 0, 1]


def shade(c, k):
    return tuple(int(v * k) for v in c)


def render(m, path, scale=1):
    g = rows_of(m); cols, rows = m['size']; H = proj(m)
    S = 2
    im = Image.new('RGB', (1536 * S, 1024 * S), BG); d = ImageDraw.Draw(im)

    def P(x, y, z=0):
        return (S * (H[0] * x + H[1] * y + H[2]), S * (H[3] * x + H[4] * y + H[5] - z))
    for y in range(rows):
        for x in range(cols):
            ch = g[y][x]; base = FLAT.get(ch, FLAT['.'])
            if ch == '.' and (x + y) % 2:
                base = shade(base, 0.9)
            d.polygon([P(x, y), P(x + 1, y), P(x + 1, y + 1), P(x, y + 1)], fill=base, outline=shade(base, 0.8))
    cells = sorted(((x, y) for y in range(rows) for x in range(cols) if g[y][x] in BLOCK), key=lambda c: (c[0] + c[1], c[0]))
    for x, y in cells:
        col, h = BLOCK[g[y][x]]
        d.polygon([P(x, y + 1), P(x + 1, y + 1), P(x + 1, y + 1, h), P(x, y + 1, h)], fill=shade(col, 0.55))
        d.polygon([P(x + 1, y), P(x + 1, y + 1), P(x + 1, y + 1, h), P(x + 1, y, h)], fill=shade(col, 0.72))
        d.polygon([P(x, y, h), P(x + 1, y, h), P(x + 1, y + 1, h), P(x, y + 1, h)], fill=col, outline=shade(col, 0.85))
    im.resize((1536, 1024), Image.LANCZOS).save(path)


def legend(path):
    im = Image.new('RGB', (900, 420), (18, 22, 28)); d = ImageDraw.Draw(im)
    items = [('#', 'tall wall'), ('B', 'tall solid object'), ('C', 'low cover'), ('W', 'breakable wall'), ('X', 'objective'),
             ('.', 'floor (walkable)'), ('=', 'marked floor (walkable)'), ('~', 'wet / ice floor (walkable)'), ('S', 'entry tiles (walkable)'), ('V', 'impassable flat: water / drop')]
    for i, (ch, t) in enumerate(items):
        x = 30 + (i // 5) * 440; y = 30 + (i % 5) * 76
        col = BLOCK[ch][0] if ch in BLOCK else FLAT[ch]
        d.rectangle([x, y, x + 56, y + 56], fill=col, outline=(255, 255, 255))
        d.text((x + 74, y + 20), t, fill=(235, 238, 242))
    im.save(path)


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'out'
    os.makedirs(out, exist_ok=True)
    data = {}
    for m in MP.MAPS:
        g = rows_of(m)
        assert all(len(r) == m['size'][0] for r in g) and len(g) == m['size'][1], m['id']
        ok, seen, total = MP.check(m, g)
        print('%-9s %s reach=%d/%d %s' % (m['id'], 'OK ' if ok and seen == total else 'CHK', seen, total, '' if ok else 'OBJECTIVE UNREACHABLE'))
        d = os.path.join(out, m['pack']); os.makedirs(d, exist_ok=True)
        render(m, os.path.join(d, 'guide_%s.png' % m['id']))
        data[m['id']] = {'pack': m['pack'], 'file': m['file'], 'title': m['ko'], 'size': list(m['size']), 'proj': proj(m), 'MAP': g, 'start': [list(s) for s in m['S']], 'objective': list(m['X'])}
    legend(os.path.join(out, 'LEGEND.png'))
    json.dump(data, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'maps.json'), 'w'), ensure_ascii=False, indent=1)
