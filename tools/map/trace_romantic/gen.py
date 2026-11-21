# -*- coding: utf-8 -*-
"""로맨틱 미션 적용: 소품을 맵에 올려 굽고(public/bgp_*.jpg), 격자 · 배치 · 대사를 index.html 의 ROM 자리에 넣는다.
사용: python3 gen.py [키 ...]   (키를 주면 그 판의 그림만 다시 굽는다. 데이터는 항상 전부 다시 쓴다)"""
import sys, os, io, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.append(os.path.join(HERE, '..', '..', 'packs', 'romantic_v3'))
import lib, build, missions, data_a, data_b
from PIL import Image, ImageDraw, ImageFilter
PUB = os.path.join(HERE, '..', '..', '..', 'public'); T = dict(data_a.T); T.update(data_b.T)
KO = {u'레이븐': 'raven', u'바이퍼': 'viper', u'글리치': 'glitch', u'브릭': 'brick', u'미라주': 'mirage', u'닥': 'doc', u'지휘관': 'hq'}
WALK = '.'
def grid_of(k):
    r = missions.R[k]; m = build.M[k]; g = [list(x) for x in m['MAP']]; W, Hh = m['W'], m['Hh']
    if not m.get('src'):   # 가까운 두 변의 낮은 경계는 따로 표시(가림 처리에서 낮게 다룬다)
        for i in range(W):
            if g[Hh - 1][i] == '#': g[Hh - 1][i] = 'F'
        for j in range(Hh):
            if g[j][W - 1] == '#': g[j][W - 1] = 'F'
    for c, x0, y0, x1, y1 in r.get('edits', []):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1): g[y][x] = c
    for x, y in r['exit']: g[y][x] = '.'
    for p_ in r['props']:
        sp, x, y, w, h, c = p_[:6]
        for j in range(h):
            for i in range(w):
                cur = g[y + j][x + i]
                if not (cur == '.' or (c == 'X' and cur in 'XC')): ERR.append((k, 'prop', sp, x + i, y + j, cur))
                if c != '-': g[y + j][x + i] = c
    X = r['X']; g[X[1]][X[0]] = 'X'
    return g
def reach(g, s, t, opened=()):
    W, Hh = len(g[0]), len(g); seen = {s}; st = [s]; op = set(map(tuple, opened))
    while st:
        x, y = st.pop()
        if (x, y) == t: return True
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n = (x + dx, y + dy)
            if 0 <= n[0] < W and 0 <= n[1] < Hh and n not in seen and (g[n[1]][n[0]] == '.' or n in op): seen.add(n); st.append(n)
    return False
ERR = []
def validate(k, g):
    r = missions.R[k]; ok = lambda c: g[c[1]][c[0]] == '.'
    if not ok(r['start']): ERR.append((k, 'start'))
    if not ok(r['use']): ERR.append((k, 'use', g[r['use'][1]][r['use'][0]]))
    if not reach(g, tuple(r['start']), tuple(r['use']), r.get('vopen', ())): ERR.append((k, '목표까지 길 없음'))
    if r.get('vopen') and reach(g, tuple(r['start']), tuple(r['use'])): ERR.append((k, '돌파 없이도 길이 있다'))
    SP = lib.sprites(k[:-1], int(k[-1]))
    for p in r['props']:   # 긴 소품은 그림의 방향과 발자국 방향이 같아야 한다
        if p[3] != p[4] and lib.orient(SP[p[0]]) == (-1 if p[3] > p[4] else 1): ERR.append((k, '소품 방향 반대', p[0], p[3], p[4]))
    for gi, gd in enumerate(r['guards']):
        bad = [wp for wp in gd['wps'] if not ok(wp)]
        for wp in bad: ERR.append((k, 'guard', gi, wp, g[wp[1]][wp[0]]))
        if not bad:
            for a, b in zip(gd['wps'], gd['wps'][1:] + gd['wps'][:1]):
                if not reach(g, tuple(a), tuple(b)): ERR.append((k, 'guard path', gi, a, b))
TALL = '#HWKBTM'
def bake(k):
    r = missions.R[k]; m = build.M[k]; pr = build.PR(m); ag, t = k[:-1], int(k[-1]); SP = lib.sprites(ag, t)
    orig = Image.open(os.path.join(lib.SRC, 'bgp_%s_%d.jpg' % (ag, t))).convert('RGBA')
    if r.get('blackout'):   # 맵 밖 하늘(번개 · 달)을 다른 판처럼 검게
        mk = Image.new('L', orig.size, 0); ImageDraw.Draw(mk).polygon(r['blackout'], fill=255); mk = mk.filter(ImageFilter.GaussianBlur(8))
        orig = Image.composite(orig, Image.new('RGBA', orig.size, (6, 8, 11, 255)), mk)
    base = orig.copy(); G0 = m['MAP']; W, Hh = m['W'], m['Hh']; hts = r['hts']
    def sil(cx, cy, hh):
        q = [pr.P(cx, cy), pr.P(cx + 1, cy), pr.P(cx + 1, cy + 1), pr.P(cx, cy + 1)]
        return [(q[0][0], q[0][1] - hh), (q[1][0], q[1][1] - hh), q[1], q[2], q[3], (q[3][0], q[3][1] - hh)]
    for p in sorted(r['props'], key=lambda p: (p[1] + p[2] + (p[3] + p[4]) / 2.0)):
        sp, x, y, w, h, c = p[:6]; sc = p[6] if len(p) > 6 else 1.0
        lib.place(base, pr, SP[sp], x, y, w, h, dark=r.get('dark', 0.92), shadow=0 if c == '-' else 110, scale=sc)
        # 그림 속 벽이 소품보다 앞에 있으면 벽을 다시 덮는다(소품이 벽 위에 올라타 보이지 않게)
        mk = Image.new('L', base.size, 0); d = ImageDraw.Draw(mk); any_ = False
        for cy in range(y, min(Hh, y + h + 5)):
            for cx in range(x, min(W, x + w + 5)):
                if (cx > x + w - 1 or cy > y + h - 1) and G0[cy][cx] in TALL and hts.get(G0[cy][cx], 0) > 16: d.polygon(sil(cx, cy, hts[G0[cy][cx]]), fill=255); any_ = True
        if any_: base.paste(orig, (0, 0), mk)
    base.convert('RGB').save(os.path.join(PUB, 'bgp_%s_%d.jpg' % (ag, t)), quality=88)
    return base
def dialog(k):
    ag, t = k[:-1], int(k[-1]); d = T[ag][t - 1]['dlg']; out = {}
    for name, (sec, lines) in zip(('start', 'obj', 'end'), d):
        L = []
        for i, (who, text) in enumerate(lines):
            w = KO.get(who, 'npc'); row = [w, text]
            if w == ag: row.append(1 if name == 'obj' else 2 if (name == 'end' and i == len(lines) - 1) else 0)
            L.append(row)
        out[name] = L
    return out
def entry(k, g):
    r = missions.R[k]; m = build.M[k]; pr = build.PR(m); ag, t = k[:-1], int(k[-1]); X = r['X']
    wet = [list(c) for c in m.get('wet', []) if tuple(c) not in set(map(tuple, r.get('dry', [])))]
    mm = dict(bg='bgp_%s_%d.jpg' % (ag, t), sk=r['sk'], zm=r['zm'], wake=68, rk=1.1, opaque=r['opaque'], hts=r['hts'], proj=pr.flat(), MAP=[''.join(x) for x in g],
              ops=[dict(id=ag, x=r['start'][0], y=r['start'][1])], exit=[list(e) for e in r['exit']],
              objective=dict(x=X[0], y=X[1], use=list(r['use']), label=r['ol'], verb=r['ov'], time=r['time']), guards=r['guards'], dlg=dialog(k))
    for f in ('env', 'zones', 'vopen', 'maxLoads'):
        if r.get(f) is not None: mm[f] = r[f]
    if wet: mm['wet'] = wet
    return dict(t=r['t'], copy=r['copy'], pre=r['pre'], post=r['post'], tips=r['tips'], bc=r['bc'], par=r['par'], m=mm)
if __name__ == '__main__':
    only = sys.argv[1:]; ROM = {}
    G_ = {k: grid_of(k) for k in missions.R}
    for k in missions.R: validate(k, G_[k])
    if ERR:
        for e in ERR: print('ERR', e)
        if '-f' not in sys.argv: sys.exit(1)
    only = [a for a in only if a != '-f']
    for k in missions.R:
        g = G_[k]
        if not only or k in only: bake(k)
        ROM.setdefault(k[:-1], [None, None, None])[int(k[-1]) - 1] = entry(k, g)
        print('ok', k, len(g[0]), 'x', len(g))
    p = os.path.join(PUB, 'index.html'); s = io.open(p, encoding='utf8').read()
    a = s.index('/*ROM-BEGIN*/'); b = s.index('/*ROM-END*/')
    s = s[:a] + '/*ROM-BEGIN*/\nvar ROM=' + json.dumps(ROM, ensure_ascii=False, separators=(',', ':')) + ';\n' + s[b:]
    io.open(p, 'w', encoding='utf8').write(s); print('index.html', len(s))
