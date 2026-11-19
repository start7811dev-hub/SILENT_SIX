# -*- coding: utf-8 -*-
"""가이드 이미지 + 지시 MD + 화풍 참조를 묶어 ChatGPT에 통째로 올릴 zip을 만든다.
사용: python3 tools/map/pack.py <출력 폴더>   (zip 과 tools/map/packs/ 를 함께 갱신)
"""
import sys, os, shutil, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import maps as MP, guide as G

HERE = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(HERE, '..', '..', 'public')
PACKS = {
    'story': ('SILENT6_Map_Story_S1-06', '스토리 미션 시즌 1 · 에피소드 1 · 스테이지 6 맵 (1장)'),
    'romantic': ('SILENT6_Map_Romantic', '로맨틱 미션 맵 (요원 6명 × TAKE 3 = 18장)'),
    'winter': ('SILENT6_Map_BloodyChristmas', '블러디 크리스마스 맵 (5장)'),
    'costume': ('SILENT6_Map_Costume_v2', '코스튬 미션 맵 v2 — 큰 맵 (6장)'),
}
NAMES = {'#': 'GREY tall blocks', 'B': 'GREEN tall blocks', 'C': 'TAN low blocks', 'W': 'YELLOW tall blocks', 'X': 'the CYAN block(s)',
         '=': 'AMBER flat tiles', 'N': 'PINK flat tiles', '~': 'BLUE flat tiles', 'S': 'bright GREEN flat tiles', 'V': 'dark NAVY flat tiles'}
ORDER = '#BWCXV=~NS'

HEAD = u'''# SILENT SIX — %(title)s

## 사용법 (사람이 읽는 부분)

1. ChatGPT 새 대화에 이 zip 파일을 그대로 올린다.
2. 다음 한 줄을 보낸다: **"압축을 풀고 지시.md 를 처음부터 끝까지 읽은 뒤, 그대로 진행해 줘."**
3. 한 번에 한 장씩 나온다. 다음 장은 "next" 라고 보내면 이어진다.
4. 받은 그림은 지시된 파일명 그대로(`.jpg` 또는 `.png`) 저장해 Claude에게 넘긴다. 게임에는 가이드와 같은 좌표로 바로 들어간다.

검수 기준: 가이드 이미지와 그림을 겹쳤을 때 **벽 · 엄폐물 · 목표의 위치가 어긋나지 않아야** 한다. 어긋난 장은 "guide 와 블록 위치가 다르다. 위치를 guide 에 정확히 맞춰 다시 그려 줘" 라고 돌려보낸다.

---

## INSTRUCTIONS FOR THE IMAGE MODEL

You are painting final game-map backgrounds for a real-time stealth tactics game (quarter-view, like Commandos or Shadow Tactics). The game's collision data is already fixed. Each map comes with a **guide image** in `guides/`: a flat-coloured block-out rendered with the game's exact camera. Your job is to turn each block-out into finished painted art **without moving anything**.

### Files in this archive
- `지시.md` — this file.
- `guides/guide_<id>.png` — one block-out per map, 1536x1024. **This is the layout blueprint.**
- `LEGEND.png` — what each guide colour means.
- `style/style_ref_1.jpg`, `style/style_ref_2.jpg` — two finished maps from the same game. Match their rendering style, level of detail, camera and lighting quality. Do not copy their content.

### Hard rules (most important first)
1. **Use the guide as an image reference and repaint over it.** Output must be exactly **1536x1024**, landscape, with the map diamond in the same place, same size, same camera angle (2:1 isometric; the floor-cell size is given per map) as the guide. Do not rotate, zoom, crop, re-centre or change perspective.
2. **Every block stays where it is.** Each coloured block in the guide becomes one solid object with the same footprint, the same position and about the same height. Do not add, remove, merge, shift or resize blocks. Do not add any new solid object on plain floor. Small flat decoration (stains, cables, rugs, leaves, floor markings) is welcome on floor tiles as long as it clearly reads as walkable ground.
3. **Gaps stay open.** Every opening between blocks (doorways, alleys, gates) must stay clearly open and walkable, at the same width.
4. **Readable gameplay.** Walkable floor must be clearly distinguishable from solid objects. Tall blocks must look tall, low blocks must look waist-high. Keep floors a little brighter and calmer than the objects standing on them.
5. Interiors are drawn with the roof removed, walls cut at one height with a visible flat top, exactly like the grey blocks.
6. Outside the map diamond keep the flat dark background colour `#06080b` (or fade to it). No horizon, no sky.
7. **No characters, no people, no animals, no text, no numbers, no UI, no grid lines, no watermark.**
8. Style: detailed hand-painted isometric game art, the same style as the two style references. Semi-realistic, crisp edges, soft baked lighting from the upper left, gentle ambient occlusion at the base of walls.

### Guide colours
- **GREY tall blocks** — structural walls.
- **GREEN tall blocks** — tall solid objects (meaning is given per map).
- **TAN low blocks** — low cover, about waist height (meaning per map).
- **YELLOW tall blocks** — breakable wall sections (only on some maps).
- **CYAN block** — the mission objective. Make it the most eye-catching object, but keep its footprint. Most maps have one. Where a map has three cyan blocks, paint all three as **exactly the same object**, indistinguishable from each other.
- **PINK flat tiles** — conversation spots (only on some maps). Walkable floor. Paint a small inviting lit spot there (a rug, a pool of warm light), no person.
- Dark checker tiles — ordinary walkable floor.
- **AMBER flat tiles** — special walkable floor (meaning per map).
- **BLUE flat tiles** — wet or frozen walkable floor (meaning per map).
- **Bright GREEN flat tiles** — the entry point. Paint it as normal floor with a subtle hint of an entrance; no green.
- **Dark NAVY flat tiles** — flat but impassable (water, a drop, a pit). Must clearly read as "you cannot walk here".

### Procedure
- Work through the maps below **in order, one image per reply**. Before each image write its output file name on its own line. Do not combine maps. Do not ask questions; if something is ambiguous, follow the guide image.
- Before painting each map, open its guide and read the text grid given for that map. The grid is the same layout written in characters. If the two ever seem to disagree, the guide image wins.
- After each image, wait for me to say "next".

---

## MAPS

'''


def block(m, n):
    g = G.rows_of(m)
    used = [c for c in ORDER if any(c in r for r in g)]
    t = u'### %d. `%s` — %s\n\n' % (n, m['file'], m['ko'])
    t += u'- Guide: `guides/guide_%s.png`\n- Output file name: `%s`\n- Grid: %d columns x %d rows, floor cell %dx%d px\n\n' % (m['id'], m['file'], m['size'][0], m['size'][1], m.get('tw', 72), m.get('tw', 72) // 2)
    t += u'**Scene.** %s\n\n**What the blocks are on this map**\n' % m['scene']
    for c in used:
        if c in m['leg']:
            t += u'- %s → %s\n' % (NAMES[c], m['leg'][c])
    t = t.replace('`D`', '')
    t += u'\n**Layout as text** (`.` floor, `D` = same object as `X`, other characters as in the legend; x runs down-right, y runs down-left, first character of the first line is the top corner)\n\n```\n' + '\n'.join(g) + '\n```\n\n'
    return t


def main(out):
    os.makedirs(out, exist_ok=True)
    tmp = os.path.join(out, '_g'); G.legend(os.path.join(out, 'LEGEND.png'))
    for key, (zname, title) in PACKS.items():
        ms = [m for m in MP.MAPS if m['pack'] == key]
        d = os.path.join(HERE, 'packs', key)
        shutil.rmtree(d, ignore_errors=True); os.makedirs(os.path.join(d, 'guides'))
        md = HEAD % {'title': title}
        for n, m in enumerate(ms):
            G.render(m, os.path.join(d, 'guides', 'guide_%s.png' % m['id']))
            md += block(m, n + 1)
        open(os.path.join(d, u'지시.md'), 'w', encoding='utf8').write(md)
        shutil.copy(os.path.join(out, 'LEGEND.png'), os.path.join(d, 'LEGEND.png'))
        z = zipfile.ZipFile(os.path.join(out, zname + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        for root, _, fs in os.walk(d):
            for f in fs:
                p = os.path.join(root, f); z.write(p, os.path.join(zname, os.path.relpath(p, d)))
        z.write(os.path.join(PUB, 'bg5.jpg'), zname + '/style/style_ref_1.jpg')
        z.write(os.path.join(PUB, 'bg4.jpg'), zname + '/style/style_ref_2.jpg')
        z.close()
        print(zname, len(ms), os.path.getsize(os.path.join(out, zname + '.zip')) // 1024, 'KB')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'out')
