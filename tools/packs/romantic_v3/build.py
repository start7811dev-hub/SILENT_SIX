# -*- coding: utf-8 -*-
"""로맨틱 미션 맵 제작 묶음 v3: 요원별 zip 6개. 맵 18장 + 소품 시트 36장(낱개 216개) + 인물 대화용 8장.
블러디 크리스마스 v3와 같은 방식: 맵은 구조만, 엄폐물과 움직이는 것은 낱개, 연출과 대사는 검토용 문서.
사용: python3 tools/packs/romantic_v3/build.py <출력 폴더>
"""
import sys, os, io, zipfile
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..', '..', '..'); PUB = os.path.join(ROOT, 'public'); W = os.path.join(HERE, '..', 'winter_v3_s2to5'); CS = os.path.join(ROOT, 'tools', 'charsheet', 'out')
sys.path.insert(0, HERE)
import data_a, data_b
T = dict(data_a.T); T.update(data_b.T)
AG = ['raven', 'viper', 'glitch', 'brick', 'mirage', 'doc']
KO = {'raven': u'레이븐', 'viper': u'바이퍼', 'glitch': u'글리치', 'brick': u'브릭', 'mirage': u'미라주', 'doc': u'닥'}
DEV = {'raven': u'무단 외출', 'viper': u'휴가계', 'glitch': u'로그아웃', 'brick': u'노크', 'mirage': u'더블 부킹', 'doc': u'야간 진료'}

MAPRULES = u'''## INSTRUCTIONS FOR THE IMAGE MODEL

You are painting one game-map background for a real-time stealth tactics game. `ref/%(ref)s` is a finished map from the same game. **Copy its look exactly**: canvas, camera angle, painterly finish, level of detail, warm practical lights against cool ambience, black surround. **Do not copy its layout, its season or its decorations.** The layout below is a level design and every placement in it matters for gameplay.

Make **one image**. Output file name: `%(file)s`. Do not ask questions.

### Canvas, camera, scale
- Exactly **1536x1024**, landscape. One plain diamond-shaped plan filling the frame, 2:1 isometric, same camera as the reference. Outside the diamond: flat near-black `#06080b`.
- The plan is **%(m)d x %(m)d metres**: a person would be about %(px)d px tall.
- %(light)s

### Words used below
Corners of the diamond: **TOP** (far), **BOTTOM** (near), **LEFT**, **RIGHT**.
Perimeter sides: **upper-left side** (TOP to LEFT), **upper-right side** (TOP to RIGHT), **lower-left side** (LEFT to BOTTOM), **lower-right side** (RIGHT to BOTTOM).
"Parallel to a side" means running along that side's isometric axis.

### Rules that apply to every map in this set
1. Everything solid is straight and runs along the two isometric axes. No diagonal walls, no curves unless the layout names one.
2. **The two near sides (lower-left and lower-right) are closed by a thin, low boundary only about 1 m high** (%(near)s), so that the floor just inside them stays fully visible. Only the two far sides may be tall.
3. **A clear walkable lane at least 2 m wide runs along the inside of all four sides**, unless the layout says this rule does not apply.
4. Everything is **single-storey and low**, so the lanes behind it stay visible. Rooms and buildings that can be entered have the **roof removed and walls cut at one height with a flat dark top**. Every doorway named in the layout is **visibly open, 2 m wide**.
5. Walkable floor is calm, even and clearly readable, slightly brighter than the structures on it. Water, drops and voids clearly read as "cannot walk here" unless the layout says they are walkable.
6. **No loose objects anywhere**: no furniture, crates, barrels, vehicles, carts, plants in pots, signs, barriers, people or animals. They are added later as separate sprites. Only what the layout calls fixed or built-in is painted. Lamps fixed to walls or posts are fine.
7. No text, letters, numbers, logos, UI, grid lines, arrows, labels or watermark.

### The place
%(place)s

### Layout
%(lay)s

### Before you finish, check
Re-read the layout and confirm every room, strip, opening and fixed object is present and in the stated place, the near boundary is low, the lanes and doorways are open, and the floor is clean of loose objects.
'''
PROPRULES = u'''## INSTRUCTIONS FOR THE IMAGE MODEL

You are painting **separate object sprites** that will be placed on top of the map `%(map)s` (if that map is not in this conversation, use `ref/%(ref)s`). They must look cut out of that painting: **same 2:1 isometric camera, same painterly finish, same lighting and weather**. `ref/sprite_sheet_example.png` is a finished sheet from another stage: follow its **format** exactly (not its snow).

Make **2 sheets, one image per reply**. Write the output file name on its own line before the image. After each sheet, stop and wait for "next". Do not ask questions.

### Rules for every sheet
1. Exactly **1536x1024**. An invisible grid of **3 columns x 2 rows**, each cell 512x512. **One object per cell, centred**, with clear margin on all sides. Objects never touch a neighbouring cell.
2. Background: flat pure magenta `#FF00FF` everywhere behind the objects (or true transparency).
3. **No ground, no floor tile, no cast shadow, no glow spilling onto the background.** Only the object.
4. Same camera for every object: 2:1 isometric from above, as on the map. Every object stands on an invisible rectangular footprint aligned to the two isometric axes.
5. "Orientation 1" = long side running toward the lower-right. "Orientation 2" = the same object with its long side running toward the lower-left.
6. Keep relative scale between cells of one sheet honest.
7. No text, letters, digits, logos, labels, cell borders or watermark.
'''
PORTRULES = u'''## INSTRUCTIONS FOR THE IMAGE MODEL

Format for dialogue portraits: vertical 2:3, **1024x1536**, flat pure green `#00FF00` background (or true transparency) with no shadow on it. One figure framed from mid-thigh up, large in the frame. No background objects, no text. Art style of `ref/style_cast.jpg`: semi-realistic anime illustration, painterly high-end finish. One image per reply, file name on its own line first, then wait for "next".

`ref/style_cast.jpg` is only a style reference. Do not draw those women.

'''


def tbl(rows):
    return u'| # | 누가 | 대사 |\n|---|---|---|\n' + u''.join(u'| %d | %s | %s |\n' % (i + 1, w, x) for i, (w, x) in enumerate(rows))


def files(a):
    out = {}; L = T[a]; npcs = []
    for n, t in enumerate(L, 1):
        fn = 'bgp_%s_%d.jpg' % (a, n); ref = 'look_outdoor.jpg' if t['io'] == 'out' else 'look_indoor.jpg'
        near = u'a low fence or kerb' if t['io'] == 'out' else u'the wall cut down to a 1 m stub'
        m = u'# 맵 — %s TAKE %d "%s" (%s)\n\n## 사용법 (사람이 읽는 부분)\n\n- 결과 파일명: `%s` (1장)\n- 구조만 들어간다. 엄폐물 · 움직이는 것 · 사람은 `T%d_2_소품_지시.md`로 따로 뽑는다.\n- 검수 (틀리면 그 부분만 다시 요청):\n' % (KO[a], n, t['t'], t['place_ko'], fn, n)
        for i, c in enumerate(t['chk'] + [u'바닥에 낱개 물건이 없다', u'가까운 두 변의 경계가 낮아서 안쪽 바닥이 다 보인다'], 1): m += u'  %d. %s\n' % (i, c)
        m += u'\n---\n\n' + MAPRULES % dict(ref=ref, file=fn, m=t['m'], px=int(round(900.0 / t['m'])), light=t['light'], near=near, place=t['place'], lay=t['lay'])
        out['T%d_1_맵_지시.md' % n] = m
        p = u'# 소품 낱개 세트 — %s TAKE %d "%s"\n\n## 사용법 (사람이 읽는 부분)\n\n- 결과: 시트 2장. 한 장에 6개씩 3×2 칸.\n- 맵 그림이 먼저 나온 뒤 **같은 대화에서** 이어서 진행한다.\n- 검수: 칸마다 1개, 배경이 한 가지 색, 물건끼리 닿지 않음, 맵과 같은 각도, 글자 없음.\n\n| 파일 | 내용 |\n|---|---|\n' % (KO[a], n, t['t'])
        for k, ko, intro, items in t['props']: p += u'| `p_r_%s%d_%s.png` | %s |\n' % (a, n, k, ko)
        p += u'\n---\n\n' + PROPRULES % dict(map=fn, ref=ref)
        for i, (k, ko, intro, items) in enumerate(t['props'], 1):
            p += u'\n### Sheet %d — `p_r_%s%d_%s.png`\nLeft to right, top row then bottom row.\n' % (i, a, n, k) + u''.join(u'%d. %s\n' % (j, x) for j, x in enumerate(items, 1))
        out['T%d_2_소품_지시.md' % n] = p
        if t.get('npc'): npcs.append((n, t['npc']))
    if npcs:
        r = u'# 인물 — %s (대화용 %d장)\n\n## 사용법 (사람이 읽는 부분)\n\n- **새 대화**에서 진행한다. zip을 다시 올리고 "3_인물_지시.md 를 읽고 한 장씩."\n- 요원 대화용 일러스트는 이미 있어서 여기에 없다. 맵 위에 서는 작은 인물은 소품 시트에 들어 있다.\n\n---\n\n' % (KO[a], 2 * len(npcs)) + PORTRULES
        for n, (ko, desc, ex) in npcs:
            r += desc + u'\n\n' + u''.join(u'- `d_R-%s%d_npc_%d.png` — %s\n' % (a, n, i, e) for i, e in enumerate(ex)) + u'\n'
        out[u'3_인물_지시.md'] = r
    d = u'# 연출과 대사 — %s "%s"\n\n그림 생성용이 아니다. 검토용이다. 고칠 줄은 "TAKE 2 ②-3"처럼 알려 주면 된다. 대사는 지휘관(플레이어)과의 무전이다.\n' % (KO[a], DEV[a])
    for n, t in enumerate(L, 1):
        d += u'\n## TAKE %d · %s — %s\n\n' % (n, t['t'], t['place_ko']) + u''.join(u'- %s\n' % x for x in t['info']) + u''.join(u'\n### %s\n\n%s' % (h, tbl(rows)) for h, rows in t['dlg'])
    out[u'4_연출과_대사.md'] = d
    rd = u'# SILENT SIX — 로맨틱 미션 맵 제작 묶음 · %s "%s"\n\n| 순서 | 파일 | 결과물 | 장수 |\n|---|---|---|---|\n' % (KO[a], DEV[a])
    for n, t in enumerate(L, 1):
        rd += u'| %d | `T%d_1_맵_지시.md` | `bgp_%s_%d.jpg` · %s | 1 |\n| %d | `T%d_2_소품_지시.md` | `p_r_%s%d_cover.png` · `_special.png` | 2 (낱개 12개) |\n' % (2 * n - 1, n, a, n, t['place_ko'], 2 * n, n, a, n)
    if npcs: rd += u'| 7 | `3_인물_지시.md` | `d_R-%s<판>_npc_0~1.png` | %d |\n' % (a, 2 * len(npcs))
    rd += u'| - | `4_연출과_대사.md` | 검토용. GPT에 시키지 않는다 | - |\n\n합계 %d장.\n\n## ChatGPT에 보내는 방법\n\n1. 새 대화에 이 zip을 올리고 **"압축을 풀고 T1_1_맵_지시.md 만 읽고 진행해 줘."**\n2. 맵을 검수한 뒤 같은 대화에서 **"이제 T1_2_소품_지시.md 를 읽고 시트 1부터 한 장씩."** 다음 장은 "next".\n3. TAKE 2와 3은 각각 **새 대화**에서 같은 순서로 한다. 한 대화에 맵 하나와 그 소품만 다룬다.\n\n## 만드는 방식 (블러디 크리스마스 v3와 같다)\n\n- 맵 그림에는 **벽 · 방 · 길 같은 구조만** 넣는다. 엄폐물과 움직이는 것은 전부 낱개로 뽑아 Claude가 배치한다.\n- 가까운 두 변의 경계는 낮게, 길과 문은 2 m 이상으로 지정했다.\n- 그림이 오면 Claude가 격자를 따고 → 엄폐물 배치 → 경비 · 카메라 배치 → 풀이 검증(HARD 기준) → 게임에 넣는다.\n\n## 참고 이미지\n\n- `ref/look_outdoor.jpg` 야외 맵 화풍 · 축척 기준. 눈과 장식은 따라 하지 않는다.\n- `ref/look_indoor.jpg` 실내 맵 화풍 기준(지붕 없이 벽을 한 높이로 자른 모습).\n- `ref/sprite_sheet_example.png` 소품 시트 형식 기준.\n' % (9 + 2 * len(npcs))
    if npcs: rd += u'- `ref/style_cast.jpg` 인물 화풍 기준.\n'
    out[u'읽어주세요.md'] = rd
    return out, len(npcs)


def build(out):
    os.makedirs(out, exist_ok=True); tot = 0
    for a in AG:
        fs, nn = files(a); N = 'SILENT6_Map_Romantic_V3_%s' % a.upper(); d = os.path.join(HERE, a); os.makedirs(d, exist_ok=True)
        z = zipfile.ZipFile(os.path.join(out, N + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        for k, v in fs.items(): z.writestr(N + '/' + k, v); io.open(os.path.join(d, k), 'w', encoding='utf8').write(v)
        z.write(os.path.join(W, 'ref_look_stage1.jpg'), N + '/ref/look_outdoor.jpg'); z.write(os.path.join(PUB, 'bg5.jpg'), N + '/ref/look_indoor.jpg'); z.write(os.path.join(W, 'ref_sprite_sheet_example.png'), N + '/ref/sprite_sheet_example.png')
        if nn: z.write(os.path.join(CS, 'sheet_all.jpg'), N + '/ref/style_cast.jpg')
        z.close(); tot += 9 + 2 * nn; print(N, os.path.getsize(os.path.join(out, N + '.zip')) // 1024, 'KB', 'files', len(fs), 'images', 9 + 2 * nn)
    print('total images', tot)


if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else 'out')
