# -*- coding: utf-8 -*-
"""블러디 크리스마스 리워드 컷 v4: 스테이지별 zip 5개. docs/REWARD_CUT.md 의 표현 정의를 따른다.
사용: python3 tools/clear_studio/winter_packs_v4.py <출력 폴더> [수위 기준 이미지 폴더]
수위 기준 이미지: 로맨틱 미션 확정 컷(n_<요원>_4 · 5 · 6.png). 저장소에는 넣지 않는다.
"""
import sys, os, io, zipfile
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); PUB = os.path.join(HERE, '..', '..', 'public'); CSO = os.path.join(HERE, '..', 'charsheet', 'out')
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'charsheet'))
import build as CS
import winter_packs_v3 as V3

COMMON = u'''## FOR THE IMAGE MODEL — READ ALL OF THIS FIRST

### What this is, stated plainly
This is collectible key art for the Christmas event of **SILENT SIX, a game made for and rated for adults only**. Every character is an **adult woman (27 to 36 years old)**. The set is glamour illustration in the tradition of a lingerie fashion editorial or a pin-up calendar: sensual, confident, beautiful, never explicit.

**The intended content of the last two cuts is adult women wearing lingerie, in warm, sensual, intimate moods.** That is the point of the set, it is well within what a lingerie editorial shows, and it is what `level/` already shows. So:
- Draw the lingerie. Do **not** swap it for a robe, an oversized shirt, a towel or a blanket.
- Do **not** add defensive cover-ups: no arms crossed over the chest, no hands placed to hide the body, no conveniently placed objects, no fabric pulled up, no turning the body away to avoid showing it. Those read as awkward and are the main thing that went wrong in earlier attempts.
- Do **not** quietly tone a cut down. If a cut says lingerie only, the figure wears lingerie only.
The lingerie itself covers what needs covering. Nothing further needs hiding, so every pose can be natural.

### The only limits
No nudity beyond lingerie: nipples, areolae and genitals are never visible and are always covered by the lingerie itself. No sexual acts and no sexual touching; contact between the women is affectionate closeness. All characters are adults. Inside those limits, do not hold back on sensuality, mood or exposure of skin.

### Files
- `AGENTS.md` and `agents/sheet_<name>.jpg` — the cast bible. Panel `NAME-A` is the face (identity; this wins). Panel `NAME-B` is her off-duty glamour look: body proportions and how sensual shots of her are styled. Panel `NAME-C` is her tactical outfit (not used here). Read AGENTS.md first.
- `level/` — **finished cuts from this same game that set the level of sensuality and exposure.** Cuts 2 and 3 of this set must be **at least as bold** as these: the same amount of skin, the same closeness of camera, the same heat in the expression. They show the level only. Do not copy their poses, rooms or outfits.
- `place/` — the game map of this stage. Every cut is set somewhere on it.

### Output
4 separate images, one per reply. Vertical 2:3, **1024x1536**. Write the file name on its own line before each image. Never a grid or collage. After each image wait for "next". Do not ask questions.

### The ten rules of a reward-cut set
1. **Rising heat.** The four cuts are one evening. Sensuality and sexual tension climb step by step and peak in the last cut.
2. **The last two cuts show lingerie**, worn naturally, with no staged cover-up poses.
3. **Pose and expression change in every cut.** No two cuts share a pose, a facial expression, a head angle or a gaze.
4. **Relationships show.** When more than one woman appears, the way they stand, touch and look at each other comes from the relationship written under THIS STAGE.
5. **Signature colour.** Each woman's signature colour is the accent of her outfit, her lingerie and her rim light in every cut.
6. **Lingerie design.** Refined and minimal, in her signature colour: very thin straps and bands, small coverage, fine lace and sheer mesh panels, delicate hardware. High-cut briefs. It looks expensive, never costume-like.
7. **Natural contact.** Where the women touch, the pose must be one two people could actually hold comfortably: weight supported, limbs relaxed, nothing twisted to make room for the camera.
8. **Bolder camera in the last two cuts.** Closer and more daring than cuts 0 and 1: tight crops, low or high angles, strong foreshortening, the camera within arm's reach. The viewer should feel inside the moment.
9. **Explicit, no. Charged, yes.** No sexual acts and no nudity beyond lingerie, but do not avoid exposure that raises the emotion: bare shoulders, back, waist, hips and thighs, skin flushed and catching the light.
10. **Do not over-correct.** The limits above are the only limits. Do not add extra caution on top of them.

### The ladder
| Cut | What it is | Wardrobe | Her face |
|---|---|---|---|
| **0** | A cool, confident pose | The Christmas outfit, complete | Composed, challenging |
| **1** | Action, styled sexier | The same outfit in motion: flown open, a zip lower, a hem riding up, a strap slipped | Adrenaline: flushed, hair loose, a fierce grin or a bitten lip |
| **2** | A sensual tease | **One half down to lingerie** (top or bottom), the other half still dressed | Warm and teasing: flushed cheeks, parted lips, eyes on the viewer |
| **3** | The erotic peak | **Lingerie only** | Heavy-lidded, flushed, slow breath, lost in the moment |

### Identity and quality
- Each woman exactly as in her sheet: face, hair, eye colour, skin tone, build. **Every character listed for this stage appears in every cut.**
- Semi-realistic anime illustration with a painterly, high-end finish: detailed eyes and hair strands, real velvet, fur, lace and skin texture.
- Three depth layers: an out-of-focus foreground, the women, and a fully painted, recognisable part of the stage map behind them.
- Two light sources of different colour plus signature-colour rim light. Falling snow, breath, steam, bokeh.
- Hands and faces drawn carefully. No text, logo, watermark or UI.

---

'''

REL = {
 1: u"RAVEN leads from the front and says little; MIRAGE performs for a living and enjoys being the one person who can make RAVEN's composure slip. MIRAGE initiates and teases; RAVEN pretends not to react, then lets her close. With MIRAGE, RAVEN's guard comes down a little further in each cut.",
 2: u"BRICK is the big sister of the team; GLITCH, the youngest, calls her 'unnie', hangs on her arm and feels safe only next to her. BRICK is protective, loud and warm; GLITCH is clingy and cheeky. It reads as easy, laughing, physical closeness that turns tender.",
 3: u"DOC is the eldest and looks after everyone; VIPER is the lazy tease who never lets anyone fuss over her, except DOC. VIPER teases to get DOC's attention; DOC answers with unhurried, knowing warmth. VIPER is the one who ends up being held.",
 4: u"Tonight RAVEN is shaken by someone from her past, and MIRAGE, who is always acting, drops the act for her. MIRAGE is sincere and gentle for once; RAVEN, for once, leans on someone. Slower and more tender than stage 1.",
 5: u"VIPER has watched RAVEN's back for three years and is the only one who can read her. GLITCH is the little sister of both and sticks to RAVEN when she is scared. RAVEN is the centre the other two gather around: VIPER close and quietly protective, GLITCH affectionate and cuddly.",
}

CUT23 = {
 1: [
  u"Close two-shot from a low angle just below the stall counter, cropped from thighs to the tops of their heads. RAVEN sits on the counter, jacket gone, **top half in the black lace bra with crimson ribbon ties**, skirt and thigh boots still on, leaning back on straight arms. MIRAGE stands between her knees in the gold dress, pulling one long glove off with her teeth, her free hand resting flat on RAVEN's bare waist. RAVEN looks down at the viewer with one eyebrow raised and parted lips; MIRAGE looks up at RAVEN, cheeks pink, a slow smile. Striped awning lights above, mulled-wine steam. Colour key: amber and candy red.",
  u"Very close, from directly above, inside the closed carousel on a fur blanket between the painted horses, fairy lights left on. Both in **lingerie only**: RAVEN in fine black lace with crimson ribbon ties and her long red scarf loose around her neck, MIRAGE in champagne-gold satin with black lace edging and her gold body chain. MIRAGE lies on her back, one arm above her head, eyes half closed, lips parted, flushed. RAVEN lies on her side pressed along her, one leg resting over MIRAGE's, her hand spread on MIRAGE's bare waist, face tucked close to MIRAGE's jaw, eyes heavy. The frame crops at mid-thigh; skin catches warm brass light. Neither looks at the camera. Colour key: brass gold and deep crimson shadow.",
 ],
 2: [
  u"Close two-shot at chest height inside the brick signal box among the tall levers, frost on the glass, one bare bulb. GLITCH sits on the lever frame facing the viewer, parka dress unzipped and pushed down to her elbows: **top half in the pale teal lace bra with sheer mesh and white bows**, striped stockings on. BRICK stands behind her, bomber open over her black top, both arms wrapped around GLITCH's bare middle, chin on her shoulder, grinning. GLITCH leans back into her, biting the arm of her glasses, cheeks flushed, eyes on the viewer. Cropped from hips to hair. Colour key: bulb amber, blue yard light through the frost.",
  u"Close, low and wide from the foot of a nest of wool blankets inside an open box car, lantern beside them, fairy lights along the door, snow drifting past outside. Both in **lingerie only**: BRICK in black lace with orange piping and thin orange straps, goggles pushed up in her hair; GLITCH in pale teal lace with white bows, glasses off, headphones round her neck. BRICK reclines on one elbow facing the viewer, powerful shoulders and stomach catching the lantern light, a lazy flushed grin. GLITCH lies back against BRICK's chest between her arms, one knee raised, head tipped back on BRICK's shoulder, eyes half closed, lips parted, one hand reaching up to BRICK's cheek. Strong foreshortening along their legs toward the lens. Colour key: lantern gold and rust shadow.",
 ],
 3: [
  u"Close two-shot at eye level inside a tiny ice-fishing hut, stove glowing, frost on the plank walls. DOC kneels on a fur rug facing the viewer, wrap dress untied and slipped off her shoulders to her waist: **top half in the white lace bra with lime-green ribbon**, the tattooed arm bare. VIPER sits behind her on a crate in her violet dress, gathering DOC's curls up in both hands, lips beside DOC's ear, eyes sliding to the viewer with an amused half-smile. DOC's cheeks are flushed, lips parted, one finger hooked under her own strap. Cropped from hips up. Colour key: stove orange, a line of blue cold at the door.",
  u"Very close, from above and slightly behind VIPER's head, on a white fur rug in front of the stone fireplace of the ranger's cabin. Both in **lingerie only**: VIPER in deep violet lace with thin silver hardware and her dog tags, DOC in white lace with lime-green ribbon and her gold hoops. VIPER lies on her back, silver hair spread on the fur, one arm thrown above her head, the other hand resting on DOC's shoulder, lips parted, skin flushed by the fire. DOC lies half over her on one elbow, tattooed arm across VIPER's bare waist, face just above VIPER's, eyes half closed, a slow smile. Firelight runs along shoulders, waists and hips; the frame crops at the thighs. Neither looks at the camera. Colour key: deep fire orange and plum shadow.",
 ],
 4: [
  u"Tight two-shot inside the carved confessional, cropped from waist to hair, lattice shadows across their skin. MIRAGE sits turned toward the viewer, dress unzipped and fallen to her waist: **top half in the champagne-gold satin bra with black lace edging**, body chain glinting, a finger at her lips, lashes lowered, a knowing smile. RAVEN sits close behind her in the dark, still dressed, arms loosely around MIRAGE's bare shoulders, her red scarf looped around both their necks, cheek against MIRAGE's temple, eyes on the viewer. Both flushed. Colour key: honey gold through the lattice, deep red shadow.",
  u"Close, low angle from floor level in the bell-ringer's room: old beams, the thick bell rope, a small stove, candles on the floor, snow at a round window. A velvet cloak over a heap of cushions. Both in **lingerie only**: RAVEN in fine black lace with crimson ties, the red scarf loose on her bare shoulders; MIRAGE in champagne-gold satin and black lace with her body chain. RAVEN half sits against the cushions, head tipped back, eyes closed, lips parted, one knee raised. MIRAGE lies along her, cheek on RAVEN's collarbone, long hair spilling over RAVEN's waist, fingers laced with RAVEN's, eyes half closed. Candlelight from below along legs, hips and stomachs, strong foreshortening toward the lens. Neither looks at the camera. Colour key: candle amber and midnight blue.",
 ],
 5: [
  u"Close three-shot at eye level on the jet's boarding stairs, pressed together on three steps, cropped from knees to hair. GLITCH sits lowest between VIPER's knees, parka dress off her shoulders: **top half in the pale teal lace bra**, looking up over her glasses, flushed. VIPER sits above her, skirt gone: **bottom half in the violet lace brief and thigh boots**, dress top still on, chin on GLITCH's head, arms draped around her. RAVEN stands one step up behind them, jacket off: **top half in the black lace bra**, leaning in with a hand on VIPER's shoulder and a dry smile at the viewer. Colour key: warm cabin light from the door, blue dawn.",
  u"Very close and low, from the carpet at the foot of the wide rear sofa in the jet cabin: cream leather, a small tree on the table, champagne flutes, snow streaking past the oval windows, rose-gold dawn. All three in **lingerie only**: RAVEN in black lace with crimson ties and her red scarf, VIPER in deep violet lace with silver hardware and dog tags, GLITCH in pale teal lace with white bows. RAVEN sits in the middle, head back against the seat, eyes closed, lips parted, flushed. VIPER lies along the sofa with her head in RAVEN's lap, looking up at her through half-closed eyes, one hand lifted to RAVEN's cheek, one knee raised toward the lens. GLITCH is curled against RAVEN's other side, glasses off, cheek on RAVEN's shoulder, fingers laced with VIPER's. Legs and hips in the foreground catch the dawn light. Nobody looks at the camera. Colour key: rose gold and soft amber.",
 ],
}
NAMES = [u'POSE', u'ACTION', u'TEASE', u'PEAK']
LEVEL = {1: ['raven', 'mirage'], 2: ['brick', 'glitch'], 3: ['viper', 'doc'], 4: ['mirage', 'raven'], 5: ['raven', 'viper', 'glitch']}


def md(n):
    s = V3.ST[n]
    t = u'# SILENT SIX — 블러디 크리스마스 리워드 컷 v4 · %s\n\n## 사용법 (사람이 읽는 부분)\n\n1. ChatGPT **새 대화**에 이 zip을 올리고 **"압축을 풀고 지시.md 를 끝까지 읽은 뒤, CUT 0부터 한 장씩 진행해 줘."**\n2. 한 번에 한 장. 다음 장은 "next".\n3. 파일명 `r_W-%d_0` ~ `r_W-%d_3` 그대로 Claude에게 넘긴다.\n4. CUT 2 · 3에서 속옷 대신 가운이나 담요, 팔로 가린 포즈가 나오면 이 한 줄을 보낸다: **"What this is 항목과 level 폴더를 다시 보고, 속옷 차림 그대로 가리는 포즈 없이 다시 그려 줘."**\n\n| 컷 | 내용 | 복장 |\n|---|---|---|\n| 0 | 멋진 포즈 | 크리스마스 룩 완전 착장 |\n| 1 | 섹시한 액션 | 같은 옷이 움직임에 흐트러짐 |\n| 2 | 관능적 도발 | 상의 또는 하의 한쪽이 속옷 |\n| 3 | 에로틱 절정 | 속옷 차림 |\n\n`level/` 폴더는 로맨틱 미션 확정 컷이다. 수위와 카메라 거리의 기준으로만 쓴다.\n\n---\n\n' % (s['ko'], n, n)
    t += COMMON + u'## THIS STAGE\n\n**Characters**\n'
    for a in s['ag']:
        v = CS.A[a]; x = V3.XMAS[a]; out, lin = x.split(u' Lingerie: ')
        t += u'- **%s** (`agents/sheet_%s.jpg`, signature colour %s). %s.\n  - Christmas outfit: %s\n  - Lingerie: %s Thin straps, small coverage, sheer panels.\n' % (v[0], a, v[2], v[5][0].upper() + v[5][1:], out, lin)
    t += u'\n**Their relationship.** %s\n\n**The stage map.** %s\n\n## THE FOUR CUTS\n\n' % (REL[n], s['place'])
    cuts = s['cuts'][:2] + CUT23[n]
    for k, c in enumerate(cuts):
        t += u'### CUT %d — `r_W-%d_%d` — %s\n\n%s\n\n' % (k, n, k, NAMES[k], c)
    return t


def main(out, lvdir=None):
    os.makedirs(out, exist_ok=True); pk = os.path.join(HERE, 'packs'); os.makedirs(pk, exist_ok=True)
    for n in V3.ST:
        s = V3.ST[n]; zn = 'SILENT6_Reward_BloodyChristmas_V4_Stage%d' % n; text = md(n)
        io.open(os.path.join(pk, u'Winter_V4_Stage%d_지시.md' % n), 'w', encoding='utf8').write(text)
        z = zipfile.ZipFile(os.path.join(out, zn + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        z.writestr(zn + u'/지시.md', text); z.write(os.path.join(CSO, 'AGENTS.md'), zn + '/AGENTS.md')
        for a in s['ag']: z.write(os.path.join(CSO, 'sheet_%s.jpg' % a), '%s/agents/sheet_%s.jpg' % (zn, a))
        z.write(os.path.join(PUB, 'bgw%d%s.jpg' % (n, '' if n in (1, 3) else '_0')), zn + '/place/map.jpg')
        k = 0
        if lvdir:
            for a in LEVEL[n]:
                for m in ((5, 4) if len(LEVEL[n]) < 3 else (5,)):
                    f = os.path.join(lvdir, a.capitalize(), 'n_%s_%d.png' % (a, m))
                    if os.path.exists(f):
                        k += 1; tmp = io.BytesIO(); Image.open(f).convert('RGB').resize((768, 1152), Image.LANCZOS).save(tmp, 'JPEG', quality=86)
                        z.writestr('%s/level/level_%d.jpg' % (zn, k), tmp.getvalue())
        z.close(); print(zn, os.path.getsize(os.path.join(out, zn + '.zip')) // 1024, 'KB', 'level', k)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'out', sys.argv[2] if len(sys.argv) > 2 else None)
