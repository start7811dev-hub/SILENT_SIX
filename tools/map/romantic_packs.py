# -*- coding: utf-8 -*-
"""로맨틱 맵: 요원별 zip 6개(각 TAKE 1·2·3). 그림을 먼저 받고 충돌은 그림에서 딴다.
사용: python3 tools/map/romantic_packs.py <출력 폴더>
"""
import sys, os, io, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import maps as MP
HERE = os.path.dirname(os.path.abspath(__file__)); PUB = os.path.join(HERE, '..', '..', 'public')
AG = ['raven', 'viper', 'glitch', 'brick', 'mirage', 'doc']
OUTDOOR = {'raven_1', 'raven_3', 'viper_1', 'viper_3', 'glitch_2', 'brick_3', 'doc_2', 'doc_3', 'mirage_1'}
RULES = u'''## INSTRUCTIONS FOR THE IMAGE MODEL

You are painting game-map backgrounds for a real-time stealth tactics game. `ref/look_indoor.jpg` and `ref/look_outdoor.jpg` are finished maps from the same game. Every new map must look like it belongs in the same set: **same canvas, same camera, same scale, same wall construction, same level of detail**. Only the place changes.

This file contains **three maps**. Make them **one at a time: one image per reply**. Write the output file name on its own line before the image. Do not ask questions. After each image, stop and wait for "next". Read only the section of the map you are painting; do not mix details between maps.

### Hard rules for every map
1. Exactly **1536x1024**, landscape. **One plain diamond-shaped plan** filling the frame like the references, 2:1 isometric, same camera angle. No wings or rooms sticking out of the diamond, no notches (one small recessed entrance is fine). Background outside the diamond: flat near-black `#06080b`. No horizon, no sky.
2. **Same scale as the references**: the plan is about 20 x 20 metres. A single bed is about 80 px long, a person would be about 45 px tall. Doorways, corridors and paths at least 2 metres wide and clearly open.
3. **Everything solid runs along the two isometric axes.** No diagonal walls, no chamfered corners, no curves, no octagons.
   - Indoor maps: roof removed, all walls cut at one height (about 46 px), thin, with a flat dark top slab, like `look_indoor.jpg`.
   - Outdoor maps: use fences, building blocks, containers, rock faces, hedges or water edges the same way: straight, axis-aligned, clearly solid, like `look_outdoor.jpg`. Buildings you cannot enter keep their roofs.
4. Lay the plan out on a 4-metre rhythm so walls and paths line up. Six to nine rooms or zones, **at least two different routes** from the entrance to the objective.
5. **Readable floor**: walkable ground is calm and slightly brighter than the objects on it. Cover (waist-high objects) sits clearly on the floor with free floor around it, never blocking a doorway. Water, drops and pits must clearly read as "cannot walk here".
6. One clearly marked **entrance** at the lower corner or lower edge (a doorway or gate with a floor hazard stripe) and the **objective** on the far side from it.
7. **Every doorway that is meant to be used must be visibly open.** Do not paint closed rooms that have no door.
8. No characters, no people, no animals, no text, no numbers, no UI, no grid lines, no watermark.
9. Rendering: detailed hand-painted semi-realistic isometric game art, crisp edges, soft baked lighting, a few practical light sources, gentle ambient occlusion. Night unless the map says otherwise.

---

'''


def sec(m, n):
    leg = m['leg']; kind = 'Outdoor' if m['id'] in OUTDOOR else 'Indoor'
    t = u'## TAKE %d — `%s`\n\n**%s**\n\n- Output file name: `%s`\n- Type: %s map. Follow `ref/look_%s.jpg` for construction.\n\n' % (n, m['file'], m['ko'], m['file'], kind, kind.lower())
    t += u'**Place.** %s\n\n' % m['scene']
    t += u'**Entrance.** %s — at the lower corner of the plan.\n\n**Objective.** %s — on the far side from the entrance. Make it the most eye-catching object on the map.\n\n' % (leg.get('S', 'the way in').capitalize(), leg['X'].capitalize())
    t += u'**What must be on the map**\n'
    names = {'#': 'Walls / structures', 'B': 'Tall solid objects', 'C': 'Waist-high cover', 'W': 'Breakable wall sections (must look cracked and marked with yellow hazard tape)', 'V': 'Impassable flat areas', '=': 'Special walkable floor', '~': 'Wet or frozen walkable floor'}
    for c in '#BWCV=~':
        if c in leg:
            t += u'- %s: %s.\n' % (names[c], leg[c])
    t += u'\nWhen this image is done, stop and wait for "next".\n\n---\n\n'
    return t


def main(out):
    os.makedirs(out, exist_ok=True); pk = os.path.join(HERE, 'packs', 'romantic_by_agent'); os.makedirs(pk, exist_ok=True)
    for a in AG:
        ms = [m for m in MP.MAPS if m['id'].startswith(a + '_')]
        assert len(ms) == 3
        md = u'# SILENT SIX — 로맨틱 맵 · %s (TAKE 1 · 2 · 3)\n\n## 사용법 (사람이 읽는 부분)\n\n1. ChatGPT 새 대화에 이 zip 파일을 올리고 **"압축을 풀고 지시.md 를 읽은 뒤 TAKE 1 부터 한 장씩 진행해 줘."** 라고 보낸다.\n2. 한 번에 한 장만 나온다. 다음 장은 "next".\n3. 파일명 `bgp_%s_1.jpg` · `_2` · `_3` 그대로 저장해 Claude에게 넘긴다. 그림을 분석해 동선 · 충돌 · 경비를 잡는다.\n\n검수: 윤곽이 마름모 하나인지, 대각선 벽이 없는지, 입구와 목표가 반대편에 있는지, 방마다 문이 열려 있는지.\n\n---\n\n' % (a.upper(), a)
        md += RULES
        for n, m in enumerate(ms):
            md += sec(m, n + 1)
        io.open(os.path.join(pk, u'%s_지시.md' % a), 'w', encoding='utf8').write(md)
        zn = 'SILENT6_Map_Romantic_%s' % a.upper()
        z = zipfile.ZipFile(os.path.join(out, zn + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        z.writestr(zn + u'/지시.md', md)
        z.write(os.path.join(PUB, 'bg1.jpg'), zn + '/ref/look_indoor.jpg'); z.write(os.path.join(PUB, 'bg2.jpg'), zn + '/ref/look_outdoor.jpg')
        z.close(); print(zn, os.path.getsize(os.path.join(out, zn + '.zip')) // 1024, 'KB')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'out')
