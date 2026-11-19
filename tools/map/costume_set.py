# -*- coding: utf-8 -*-
"""코스튬 미션 원샷 세트: 맵 6 + 대화 일러스트 54 + 리워드 컷 24 를 한 zip 으로 묶는다.
사용: python3 tools/map/costume_set.py <출력 폴더>   (pack.py 를 먼저 돌려 packs/costume 이 있어야 한다)
"""
import sys, os, io, re, zipfile
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..', '..'); PUB = os.path.join(ROOT, 'public')
AG = ['raven', 'viper', 'glitch', 'brick', 'mirage', 'doc']
LOOK = {
 'raven': ('RAVEN', 'short messy black hair, sharp eyes, signature red scarf', 'a red-and-black matador-inspired stage outfit with her signature red scarf'),
 'viper': ('VIPER', 'silver-lavender hair, cool gaze', 'a violet-and-silver ice-queen figure-skating-inspired outfit'),
 'glitch': ('GLITCH', 'dark hair with teal highlights, glasses, headphones around the neck', 'a teal-neon cyber-idol stage outfit with a holographic visor pushed up on her head'),
 'brick': ('BRICK', 'strong athletic build, taped hands', 'an orange-and-black champion-boxer-inspired outfit with an open satin robe'),
 'mirage': ('MIRAGE', 'elegant, poised, knowing smile', 'a gold-and-black casino-dealer-inspired outfit with a bow tie and waistcoat'),
 'doc': ('DOC', 'dark curly hair tied up high, hoop earrings, tattooed forearm', 'a glossy white-and-lime nurse-inspired corset outfit with a short cropped jacket, long gloves and a medic-cross choker'),
}
NPC = {
 'raven': [('의상 담당', 'the wardrobe mistress: a woman in her fifties, silver hair in a tight bun, black smock, a pin cushion on her wrist, a tape measure round her neck, a red rose pin'),
           ('마권업자', 'the bookmaker: a heavyset man in his forties, slicked-back hair, red waistcoat with gold trim, rolled sleeves, an unlit cigar, a ledger under his arm')],
 'viper': [('후원자 부인', 'the patron\'s wife: an elegant woman in her forties, platinum updo, white fur stole over a violet gown, a champagne flute'),
           ('코치', 'the coach: a stern man in his fifties, grey crew cut, dark team jacket, a stopwatch on a lanyard')],
 'glitch': [('매니저', 'the tour manager: a sharp woman in her thirties, black bob, headset, black blazer, a tablet held to her chest, a lanyard pass with no text'),
            ('음향 감독', 'the sound director: a lanky man in his forties, short beard, grey beanie, headphones round his neck, black crew T-shirt')],
 'brick': [('주방 책임자', 'the head chef: a broad man in his fifties, chef whites, a towel over one shoulder, old burn scars on his forearms'),
           ('컷맨', 'the cutman: a wiry man in his sixties, flat cap, orange-and-black corner jacket, a towel round his neck, cotton swabs tucked behind one ear')],
 'mirage': [('하이롤러', 'the high roller: a suave man in his fifties, silver hair, white dinner jacket, a signet ring, a stack of chips in his fingers'),
            ('피트 보스', 'the pit boss: a woman in her forties, sleek ponytail, black suit, an earpiece, a small gold pin with no text')],
 'doc': [('수간호사', 'the head nurse: a strict woman in her fifties, white tunic with lime piping, glasses on a chain, a clipboard'),
         ('VIP 환자', 'the VIP patient: a man in his sixties in a white spa robe, a small bandage across his nose, a gold watch, a towel round his neck')],
}
EXP_N = ['neutral, polite, unreadable', 'suspicious: narrowed eyes, head slightly tilted, lips pressed', 'relaxed: a small satisfied smile, shoulders loosened']
EXP_A = ['neutral, composed, a faint professional smile', 'confident: a relaxed knowing smile, one eyebrow slightly raised', 'tense: smile frozen, eyes sharp, jaw set']

MASTER = u'''# SILENT SIX — 코스튬 미션 원샷 생성 세트

맵 6장 + 대화 일러스트 54장 + 리워드 컷 24장 = **84장**.

## 사용법 (사람이 읽는 부분)

1. ChatGPT 새 대화에 이 zip 파일을 그대로 올린다.
2. 다음 한 줄을 보낸다: **"압축을 풀고 지시.md 를 끝까지 읽은 뒤, PART A 부터 순서대로 진행해 줘."**
3. 한 번에 한 묶음씩 나온다. 이어서 받을 때는 "next".
4. 대화가 길어져 끊기면 새 대화에 zip 을 다시 올리고 **"지시.md 의 PART B 의 <파일명> 부터 이어서"** 처럼 이어 간다.
5. 파일명은 지시된 그대로 저장한다. 받은 그림을 Claude에게 넘기면 게임에 들어간다.

| PART | 내용 | 장수 | 파일명 | 규격 |
|---|---|---|---|---|
| A | 맵 | 6 | `bgc_<요원>.jpg` | 1536×1024 |
| B | 대화 일러스트 | 54 | `d_C-<요원>_n1_<0..2>.png` · `_n2_` · `_me_` | 1024×1536, 배경 투명 |
| C | 리워드 컷 | 24 | `r_C-<요원>_<0..3>.jpg` | 1024×1536 |

검수: A는 가이드와 겹쳐 블록 위치가 맞는지, B는 표정 3장이 같은 사람 · 같은 옷 · 같은 자세인지, C는 얼굴이 참조와 같은지 본다.

---

## FOR THE IMAGE MODEL — READ ALL OF THIS FIRST

This archive is one production job in three parts. Do PART A, then PART B, then PART C, in the order written. Never skip ahead. Do not ask questions; where something is ambiguous, follow the reference files. Before every image, write its output file name on its own line. After each unit of work (one map in A, one character's three expressions in B, one agent's four images in C) stop and wait for "next".

Folders: `guides/` map blueprints, `LEGEND.png` guide colours, `style/` two finished maps as style references for PART A, `refs/` one reference image per agent for PART B and PART C.

Everyone depicted is an adult. No text, no logos, no watermarks in any image.

---

# PART A — MAPS (6 images)

'''
PB = u'''
---

# PART B — DIALOGUE PORTRAITS (54 images)

These are visual-novel style conversation portraits. In the game two portraits face each other: the other person on the LEFT of the screen, the agent on the RIGHT.

Rules for every portrait
- Vertical 2:3, 1024x1536. **Transparent background** (PNG). If you cannot output transparency, use a flat pure green `#00FF00` background with no shadow on it.
- Waist-up, one person, centred, head in the upper third with clear space above the hair. Nothing cropped at the sides.
- Same semi-realistic anime illustration style as the images in `refs/`. Soft key light from the front, a thin rim light.
- Each character gets **three expressions: #0, #1, #2**. The three images must be the same person, same outfit, same pose and framing; only the face (and at most a small shoulder or hand shift) changes.
- **Other people (n1, n2) face toward the RIGHT of the image** (three-quarter view). **Agents (me) face toward the LEFT of the image** (three-quarter view).
- Agents: keep the woman exactly as in her reference image (face, hair, build), wearing the costume described. Fully clothed, glamorous, no nudity.
- No weapons in any portrait.

Expressions for other people: #0 %s · #1 %s · #2 %s.
Expressions for agents: #0 %s · #1 %s · #2 %s.

Work one character at a time: three images, then wait for "next".

''' % tuple(EXP_N + EXP_A)
PC = u'''
---

# PART C — REWARD CUTS (24 images)

'''


def main(out):
    packs = os.path.join(HERE, 'packs', 'costume')
    md_a = io.open(os.path.join(packs, u'지시.md'), encoding='utf8').read()
    a_rules = md_a[md_a.index('You are painting final game-map backgrounds'):md_a.index('## MAPS')].rstrip().rstrip('-').rstrip()
    a_rules = a_rules.replace('### Files in this archive', '### Files used in this part').replace(u'- `지시.md` — this file.\n', '')
    a_maps = md_a[md_a.index('## MAPS') + len('## MAPS'):].strip()
    md = MASTER + a_rules + '\n\n## Maps\n\n' + a_maps + '\n' + PB
    n = 0
    for ag in AG:
        nm, look, cos = LOOK[ag]
        md += u'## %s\n\n' % nm
        for k, (ko, desc) in enumerate(NPC[ag]):
            md += u'- **`d_C-%s_n%d_0.png`, `_1.png`, `_2.png`** — %s. Other person, faces RIGHT. %s.\n' % (ag, k + 1, ko, desc[0].upper() + desc[1:])
            n += 3
        md += u'- **`d_C-%s_me_0.png`, `_1.png`, `_2.png`** — %s in costume. Agent, faces LEFT. Reference: `refs/a_%s_0.jpg` (%s). Outfit: %s.\n\n' % (ag, nm, ag, look, cos)
        n += 3
    pc = io.open(os.path.join(ROOT, 'tools', 'clear_studio', 'PROMPTS_Costume.md'), encoding='utf8').read()
    common = re.search(r'## 공통 지시\s+```\n(.*?)```', pc, re.S).group(1)
    blocks = pc[pc.index(u'## 요원별 블록') + len(u'## 요원별 블록'):].strip()
    blocks = blocks.replace(u'첨부: `a_', u'Reference: `refs/a_')
    md += PC + common.replace('For every mission block I send', 'For every mission block below').replace('I attach one reference image per character.', 'Each block names its reference image in `refs/`.') + '\n' + blocks + '\n'
    os.makedirs(out, exist_ok=True)
    io.open(os.path.join(HERE, 'packs', u'Costume_TotalSet_지시.md'), 'w', encoding='utf8').write(md)
    zn = 'SILENT6_Costume_TotalSet'
    z = zipfile.ZipFile(os.path.join(out, zn + '.zip'), 'w', zipfile.ZIP_DEFLATED)
    z.writestr(zn + u'/지시.md', md)
    for f in sorted(os.listdir(os.path.join(packs, 'guides'))):
        z.write(os.path.join(packs, 'guides', f), zn + '/guides/' + f)
    z.write(os.path.join(packs, 'LEGEND.png'), zn + '/LEGEND.png')
    z.write(os.path.join(PUB, 'bg5.jpg'), zn + '/style/style_ref_1.jpg'); z.write(os.path.join(PUB, 'bg4.jpg'), zn + '/style/style_ref_2.jpg')
    for ag in AG:
        z.write(os.path.join(PUB, 'a_%s_0.jpg' % ag), zn + '/refs/a_%s_0.jpg' % ag)
    z.close()
    print(zn, 'dialogue', n, 'reward', blocks.count('Image #'), os.path.getsize(os.path.join(out, zn + '.zip')) // 1024, 'KB', len(md))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'out')
