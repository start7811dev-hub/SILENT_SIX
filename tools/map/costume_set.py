# -*- coding: utf-8 -*-
"""코스튬 미션 원샷 세트: 맵 6 + 대화 일러스트 54 + 리워드 컷 24 를 한 zip 으로 묶는다.
사용: python3 tools/map/costume_set.py <출력 폴더>   (pack.py 를 먼저 돌려 packs/costume 이 있어야 한다)
"""
import sys, os, io, re, zipfile
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..', '..'); PUB = os.path.join(ROOT, 'public')
AG = ['raven', 'viper', 'glitch', 'brick', 'mirage', 'doc']
sys.path.insert(0, os.path.join(HERE, '..', 'charsheet'))
import build as CS
COS = {'raven': 'a red-and-black matador-inspired stage outfit with her signature red scarf', 'viper': 'a violet-and-silver ice-queen figure-skating-inspired outfit', 'glitch': 'a teal-neon cyber-idol stage outfit with a holographic visor pushed up on her head', 'brick': 'an orange-and-black champion-boxer-inspired outfit with an open satin robe', 'mirage': 'a gold-and-black casino-dealer-inspired outfit with a bow tie and waistcoat', 'doc': 'a glossy white-and-lime nurse-inspired corset outfit with a short cropped jacket, long gloves and a medic-cross choker'}
LOOK = {k: (v[0], v[5], COS[k]) for k, v in CS.A.items()}
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

Folders: `guides/` map blueprints, `LEGEND.png` guide colours, `style/` two finished maps as style references for PART A, `AGENTS.md` and `agents/sheet_<name>.jpg` the cast bible for PART B and PART C (three labelled panels per agent: `NAME-A` face, `NAME-B` glam, `NAME-C` tactical; read AGENTS.md before PART B).

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
- Same semi-realistic anime illustration style as the agent sheets in `agents/`. Soft key light from the front, a thin rim light.
- Each character gets **three expressions: #0, #1, #2**. The three images must be the same person, same outfit, same pose and framing; only the face (and at most a small shoulder or hand shift) changes.
- **Other people (n1, n2) face toward the RIGHT of the image** (three-quarter view). **Agents (me) face toward the LEFT of the image** (three-quarter view).
- Agents: keep the woman exactly as on her sheet (panel A: face, hair, skin tone, build), wearing the costume described. Fully clothed, glamorous, no nudity.
- No weapons in any portrait.

Expressions for other people: #0 %s · #1 %s · #2 %s.
Expressions for agents: #0 %s · #1 %s · #2 %s.

Work one character at a time: three images, then wait for "next".

''' % tuple(EXP_N + EXP_A)
PC = u'''
---

# PART C — REWARD CUTS (24 images)

'''


LADDER = u'''### Wardrobe ladder — exposure rises from cut to cut
- **CUT 0**: the full outfit, complete and intact.
- **CUT 1**: the same outfit under stress: jacket open or torn at a shoulder, a zip pulled lower, a glove lost. Still dressed.
- **CUT 2**: clearly more revealing: outer layers off, down to a fitted top or bralette and shorts or stockings, one strap slipping, bare shoulders, midriff and thighs.
- **CUT 3**: the boldest. **No clothing and no underwear visible on her torso.** She is covered only by her own hands and arms, her hair, a turned shoulder or raised knee, or one prop named in the cut (her scarf, a fur blanket, a robe sliding off, a towel, steam). The pose must look natural and unposed, a private moment, not a pin-up presented to the camera. Keep one signature item on her (scarf, dog tags, glasses, goggles, earrings, armband) so she is still recognisably herself.

### Limits (never cross)
Implied only. Nipples, areolae and genitals are never visible in any cut: always fully hidden by hands, arms, hair, pose or the prop. No sexual acts, no touching between characters beyond leaning or an arm around a shoulder. Everyone is an adult woman in her late twenties.
'''

VEN = {'raven': ('a circular show arena on a matador-themed gala night: sand ring under spotlights, red drapes, gold trim, banked seats, stage smoke', 'a wardrobe room with bulb-ringed mirrors, costume trunks and red roses'), 'viper': ('an indoor ice rink during a gala figure-skating show: violet and silver spotlights, frost haze, rink boards, glitter in the air', 'a locker room with frosted windows, skate bags, a bench and a rack of sequinned costumes'), 'glitch': ('backstage of a huge concert dome during an idol show: the back of a giant LED wall, teal lasers, flight cases, cables, magenta light leaking through', 'a small dressing room with a make-up mirror, fairy lights, energy-drink cans and a costume rail'), 'brick': ('a luxury hotel ballroom set up for a title fight: a boxing ring under a hard white light, dinner tables, orange and black bunting, chandeliers', "a fighters' locker room with a massage table, hanging robes, a title belt on a bench and steam from the showers"), 'mirage': ('a private penthouse casino at night: green baize tables, a roulette wheel, a gold-lit bar, black marble, city lights through tall windows', 'a VIP salon with a velvet chaise, a silk screen, scattered chips and a champagne bucket'), 'doc': ('a private cosmetic clinic and spa at night: white marble, lime-green accent light, a turquoise spa pool, orchids, soft steam', 'a sauna-side relaxation room with warm wood, folded white towels, an orchid and drifting steam')}
SIG = {'raven': 'her long red scarf', 'viper': 'her dog tags and violet neck scarf', 'glitch': 'her round glasses and headphones', 'brick': 'her orange goggles and dog tags', 'mirage': 'her gold hoop earrings and a single black glove', 'doc': 'her medic-cross choker and hoop earrings'}
PROP = {'raven': 'the red scarf itself, draped down her front', 'viper': 'a white towel held to her chest with one hand', 'glitch': 'an oversized tour hoodie held against her chest, not worn', 'brick': 'the open satin robe hanging from her elbows, her crossed forearms covering her chest', 'mirage': 'a fan of playing cards in one hand and her long hair over the other shoulder', 'doc': 'a white towel slipping low on her hips, one arm folded across her chest'}
SHOTS = [
 u"Full-body showpiece, camera low at knee height looking up, three-quarter view from her left. She stands mid-stride in the middle of the venue, weight on one hip, chin lifted, looking past the camera with a proud, composed half-smile. The whole costume is visible and intact. Colour key: her signature colour as stage light against deep shadow. Foreground: a blurred prop of the venue.",
 u"Tension shot with a strong diagonal tilt, medium-full, camera high and to the side. No weapons. She walks in plain sight through the venue while a guard's blurred dark silhouette crosses the foreground. Her body faces away; her head is turned back over her shoulder in three-quarter profile, eyes sharp and alert, lips pressed, one hand lifting the hem or collar of the costume as she moves. Colour key: cold shadow cut by one hard warm light.",
 u"Medium close-up from the waist up at eye level, shallow depth of field. Backstage after the job. She leans on a counter with her head tilted, looking straight into the lens with one eyebrow raised and a slow teasing smirk, biting the fingertip of a glove or pulling a strap down with one finger. Colour key: warm amber with her signature colour as a rim light. Foreground: blurred bulbs or bottles.",
 u"Intimate private moment, camera low and slightly behind her in three-quarter back view, soft focus edges. She is not looking at the camera: head turned in profile, eyes half closed, a quiet private smile, caught mid-movement as she undresses. Colour key: candle or lamp gold with deep shadow.",
]
WARD = [
 u"Wardrobe: the complete costume, intact.",
 u"Wardrobe: the same costume in motion, jacket or robe open and slipping from one shoulder, one glove missing. Still dressed.",
 u"Wardrobe: outer pieces off. Down to the costume's corset or bralette and its shorts or stockings, laces half undone, one strap off the shoulder, bare shoulders, midriff and thighs.",
 u"Wardrobe: the costume lies discarded on a chair behind her. No clothing and no underwear visible on her torso. She is covered only by {prop}, plus her own arms, hair and the turn of her body. She still wears {sig}. Natural and unposed.",
]
NAMES_C = ['SHOWPIECE', 'IN PLAIN SIGHT', 'TEASE', 'PRIVATE']


def partc():
    t = u"""Four images per agent. They are shown side by side as a set, so they must look like **four different illustrations by the same artist**: each cut has a different shot size, camera angle, head angle, gaze, expression, pose and colour key. Follow each cut's camera text literally. No two images of one agent may share a camera angle or a facial expression, and she faces the camera directly in at most one of them.

Format: vertical portrait 2:3, 1024x1536, one image per reply, file name on its own line first. After one agent's four images, wait for "next".

Quality for every image: painterly high-end finish like the agent sheets; three depth layers (blurred foreground object, the agent, a fully painted venue with at least five specific props); two light sources of different colour plus a rim light; visible atmosphere (smoke, steam, glitter, bokeh). Hands and costume details drawn carefully. No text, no logo, no watermark.

Identity: the agent exactly as on her sheet (panel A wins). Her signature colour must be present in every image.

""" + LADDER + u"\n"
    for ag in AG:
        nm, look, cos = LOOK[ag]
        t += u"## %s\n\n- Sheet: `agents/sheet_%s.jpg`\n- Costume: %s.\n- Venue: %s.\n- Private room (CUT 3): %s.\n\n" % (nm, ag, cos, VEN[ag][0], VEN[ag][1])
        for k in range(4):
            w = WARD[k].replace('{prop}', PROP[ag]).replace('{sig}', SIG[ag])
            t += u"### CUT %d — `r_C-%s_%d` — %s\n\n%s %s%s\n\n" % (k, ag, k, NAMES_C[k], SHOTS[k], w, (u" Setting for this cut: the private room.") if k == 3 else (u" Setting: backstage of the venue." if k == 2 else u" Setting: the venue."))
    return t


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
        md += u'- **`d_C-%s_me_0.png`, `_1.png`, `_2.png`** — %s in costume. Agent, faces LEFT. Sheet: `agents/sheet_%s.jpg` (%s). Outfit: %s.\n\n' % (ag, nm, ag, look, cos)
        n += 3
    md += PC + partc()
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
        z.write(os.path.join(HERE, '..', 'charsheet', 'out', 'sheet_%s.jpg' % ag), zn + '/agents/sheet_%s.jpg' % ag)
    z.write(os.path.join(HERE, '..', 'charsheet', 'out', 'AGENTS.md'), zn + '/AGENTS.md')
    z.close()
    print(zn, 'dialogue', n, 'reward', 24, os.path.getsize(os.path.join(out, zn + '.zip')) // 1024, 'KB', len(md))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'out')
