# -*- coding: utf-8 -*-
"""받은 로맨틱 자산을 저장소용으로 정리한다(한 번 실행).
- 맵 원본 18장 → src/
- 소품 시트 36장 → 낱개 216개(키 색 정리, 효과 그림 무채색 보정) → sprites/<판>/<c0..s5>.webp
- 대화 인물 8장 → portraits/ (가장자리 녹색 정리, 640x960)
사용: RSRC=<맵 폴더> RPSRC=<props · portraits 폴더> python3 assets.py"""
import os, sys, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
from PIL import Image
import lib
FX = {('viper', 2, 's2'): 'steam', ('doc', 3, 's2'): 'fog', ('viper', 3, 's5'): 'snow', ('brick', 3, 's3'): 'dust', ('doc', 1, 's4'): 'water'}   # 배경색이 묻은 효과 그림
def neutral(im, kind):
    a = np.asarray(im).astype(np.float32); rgb = a[..., :3]; lum = rgb.mean(-1, keepdims=True)
    tint = {'steam': (1.0, 0.99, 0.97), 'fog': (0.93, 0.96, 1.0), 'snow': (0.95, 0.97, 1.0), 'dust': (1.0, 0.95, 0.88), 'water': (0.9, 0.96, 1.0)}[kind]
    out = lum * np.array(tint) * (1.12 if kind != 'water' else 1.0)
    return Image.fromarray(np.dstack([out.clip(0, 255), a[..., 3]]).astype(np.uint8), 'RGBA')
def run():
    os.makedirs(os.path.join(HERE, 'src'), exist_ok=True); n = 0
    for ag in lib.AG:
        for t in (1, 2, 3):
            shutil.copy(os.path.join(lib.SRC, 'bgp_%s_%d.jpg' % (ag, t)), os.path.join(HERE, 'src', 'bgp_%s_%d.jpg' % (ag, t)))
            d = os.path.join(HERE, 'sprites', '%s%d' % (ag, t)); os.makedirs(d, exist_ok=True)
            for kind, pre in (('cover', 'c'), ('special', 's')):
                sheet = lib.despill(Image.open(os.path.join(lib.PSRC, 'props', 'p_r_%s%d_%s.png' % (ag, t, kind))))
                for i in range(6):
                    sp = lib.trim(sheet.crop(((i % 3) * 512, (i // 3) * 512, (i % 3) * 512 + 512, (i // 3) * 512 + 512)))
                    fx = FX.get((ag, t, pre + str(i)))
                    if fx: sp = neutral(sp, fx)
                    sp.thumbnail((380, 380), Image.LANCZOS); sp.save(os.path.join(d, '%s%d.webp' % (pre, i)), quality=92, method=6); n += 1
    pd = os.path.join(HERE, 'portraits'); os.makedirs(pd, exist_ok=True)
    for f in sorted(os.listdir(os.path.join(lib.PSRC, 'portraits'))):
        if not f.endswith('.png'): continue
        im = lib.despill(Image.open(os.path.join(lib.PSRC, 'portraits', f)).convert('RGBA'))
        a = np.asarray(im).astype(np.float32); al = a[..., 3]; edge = (al > 8) & (al < 250)   # 반투명 가장자리는 어둡게 눌러 녹색 테를 없앤다
        g = a[..., 1]; mx = np.maximum(a[..., 0], a[..., 2]); a[..., 1] = np.where(edge & (g > mx), mx, g)
        Image.fromarray(a.astype(np.uint8), 'RGBA').resize((640, 960), Image.LANCZOS).save(os.path.join(pd, f.replace('.png', '.webp')), quality=88, method=6)
    print('낱개', n, '개 · 인물', len(os.listdir(pd)), '장')
if __name__ == '__main__': run()
