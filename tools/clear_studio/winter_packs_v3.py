# -*- coding: utf-8 -*-
"""블러디 크리스마스 리워드 컷 v3: 스테이지별 zip 5개.
사용: python3 tools/clear_studio/winter_packs_v3.py <출력 폴더>
기준: 참여 요원 전원 등장 · 크리스마스 섹시 룩(시그니처 색) · 미션 맵이 배경 · 0→3으로 수위와 열기가 올라간다.
"""
import sys, os, io, zipfile
HERE = os.path.dirname(os.path.abspath(__file__)); PUB = os.path.join(HERE, '..', '..', 'public'); CSO = os.path.join(HERE, '..', 'charsheet', 'out')
sys.path.insert(0, os.path.join(HERE, '..', 'charsheet'))
import build as CS

XMAS = {
 'raven': u"a cropped crimson velvet jacket with white fur trim over a black corset bodysuit, a short crimson skirt with a white fur hem, black thigh-high boots, and her long red scarf. Lingerie: fine black lace with crimson ribbon ties.",
 'mirage': u"a champagne-gold sequin mini dress with a white fur stole, long black satin gloves, gold hoop earrings and a gold body chain, black stilettos. Lingerie: champagne-gold satin with black lace edging.",
 'brick': u"a burnt-orange cropped bomber with a white fur collar over a black sports top, black hot pants with orange braces, orange-and-white striped thigh socks, heavy boots, her goggles pushed up with a sprig of holly tucked in. Lingerie: black sporty-cut lace with orange piping.",
 'glitch': u"an oversized teal Santa-cut hooded mini parka dress with white fur trim, zip half down, teal-and-white striped stockings, short boots, her round glasses, and headphones with tiny reindeer antlers. Lingerie: pale teal lace with small white bows.",
 'viper': u"an off-shoulder violet velvet mini dress with silver-grey fur trim, a slim black belt, black thigh-high boots, her dog tags, a violet ribbon choker. Lingerie: deep violet lace with silver hardware.",
 'doc': u"a lime-green velvet wrap mini dress cut like an elf tunic with white fur trim and a wide black belt, the sleeve pushed up to show her tattooed forearm, gold hoop earrings, white fur-topped ankle boots. Lingerie: white lace with lime-green ribbon.",
}

COMMON = u'''## FOR THE IMAGE MODEL — READ ALL OF THIS FIRST

You are producing four pieces of premium key art that players unlock after clearing one stage of a game's Christmas event. They are shown as a set, in order, so they must read as **one evening getting warmer step by step**: four different illustrations by the same artist, never four takes of one pose.

### Files
- `AGENTS.md` and `agents/sheet_<name>.jpg` — the cast bible. Each sheet has three labelled panels: `NAME-A` face (identity, this wins), `NAME-B` glam (body proportions and how she is styled when she is off duty), `NAME-C` tactical outfit, plus her signature colour. Read AGENTS.md first.
- `place/` — the game map of this stage and, where present, a mood image. **Every cut is set somewhere on this map.** Use it for the architecture, materials and lights of the background.
- `look/` — finished images from this game. They set the quality bar for rendering. Do not copy their poses.

### Output
- 4 separate images, one per reply. Vertical 2:3, **1024x1536**. Write the file name on its own line before each image. Never a grid or collage. After each image wait for "next". Do not ask questions.

### Identity
- Each woman exactly as in her sheet: same face, hair, eye colour, skin tone, build. Everyone is an adult woman in her late twenties or older.
- **Every character listed for this stage appears in every cut**, clearly distinct, none merged or dropped.
- Each woman's **signature colour** leads her outfit and lingerie in every cut.

### Christmas wardrobe
This is a holiday special, not a mission photo. Nobody wears tactical gear. Each woman wears the **Christmas outfit** written for her under THIS STAGE, and later the lingerie written there.

### The ladder — heat rises from cut to cut
| Cut | What it is | Wardrobe | Mood on her face |
|---|---|---|---|
| **0** | A cool, confident pose shot | The Christmas outfit, complete | Composed, in control, a challenging look |
| **1** | An action shot, styled sexier | The same outfit in motion: jacket or stole flying open, a zip lower, a hem riding up, a boot top slipping | Adrenaline: flushed, hair loose, a fierce grin or bitten lip |
| **2** | A sensual tease | **Either the top half or the bottom half is down to lingerie**, the other half still dressed. The lingerie is refined and very small: fine lace, thin straps, high-cut | Teasing and warm: flushed cheeks, parted lips, eyes on the viewer |
| **3** | An erotic, private mood | **Lingerie only**, or, where the cut says so, nothing visible at all with a blanket, her hair, her hands or a turned body covering her | Heavy-lidded, flushed, slow breath, lost in the moment |

### When more than one woman appears
They are close teammates who trust each other with their lives, and it shows. Make the affection active and physical in every cut: an arm around a waist, leaning into each other, fingers laced, a head on a shoulder, a cheek kiss, one fixing the other's ribbon or hair, shared laughter with faces close. It grows warmer with the ladder.

### Quality — every image must have all of this
- Semi-realistic anime illustration with a painterly, high-end finish like `look/`: detailed eyes and hair strands, real velvet, fur, lace and leather texture.
- **Three depth layers**: foreground (out-of-focus snow, a garland, a lantern, a rail), the women in the midground, a fully painted, recognisable part of the stage map behind them. No empty backdrops.
- **Two light sources of different colour** plus a rim light in the signature colour. Visible atmosphere: falling snow at several depths, breath in the cold, steam, bokeh.
- Hands, faces and fabric drawn carefully. No text, no logo, no watermark, no UI.

### Variety
Each cut gives its own shot size, camera angle, pose, expression and colour key. Follow the camera line literally. No two images share a camera angle, a shot size or a facial expression.

### Limits (never cross)
Suggestive, never explicit. **Nipples, areolae and genitals are never visible** in any cut: always fully covered by lingerie, a blanket, hair, hands, arms or the pose. **No sexual acts** and no sexual touching; contact between the women is affectionate closeness only. All characters are adult women.

---

'''

ST = {
 1: dict(ko=u'STAGE 1 · 첫 번째 상자 — 성탄 마켓', ag=['raven', 'mirage'], place_img=['bgw1.jpg'],
  place=u"18:40, Christmas Eve. A walled old-town Christmas market: a great decorated tree inside an iron fence at the centre of a lit plaza, blocks of red-and-white striped stalls with dark alleys between them, a carousel, a small wooden stage with red curtains, a frozen stone fountain, stone houses with lit windows, arched gates, garlands and string lights everywhere, crates, barrels, a sleigh and potted firs along the lanes.",
  cuts=[
   u"Full-body two-shot, camera low at knee height looking up. They stand back to back in front of the great tree, the gift box they came for dangling by its ribbon from MIRAGE's gloved finger. RAVEN has her arms crossed, chin slightly down, looking at the viewer from under her brows, unreadable. MIRAGE leans her shoulders against RAVEN's back, head tilted, one hand on her hip, a polished victorious smile. Colour key: tree gold against deep blue night, crimson and gold rim lights. Foreground: blurred iron fence finials and snow.",
   u"Action shot, strong diagonal, camera high looking down a dark alley between two stall blocks. They run toward the camera hand in hand, RAVEN half a step ahead pulling MIRAGE along, scarf and fur stole streaming, RAVEN's jacket flown open, MIRAGE's hem riding up her thigh as she kicks off one stiletto. RAVEN looks back over her shoulder with a fierce grin; MIRAGE laughs out loud, hair loose, cheeks flushed. Scattered gift boxes and snow in the air. Colour key: cold teal alley, one hard red stall sign.",
   u"Medium two-shot at eye level behind a closed stall, lit by its striped awning lights. RAVEN sits on the counter: jacket off, **top half down to the black lace bra with crimson ties**, skirt and boots still on, leaning back on one hand. MIRAGE stands between her knees still in the gold dress, one long glove half pulled off with her teeth, her other arm around RAVEN's waist. RAVEN looks at the viewer with one eyebrow raised and parted lips; MIRAGE looks sideways at RAVEN with a slow, warm smile, cheeks pink. Steam from two cups of mulled wine. Colour key: amber and candy red.",
   u"Intimate, wide and low inside the dark carousel after closing, the painted horses and brass poles around them, fairy lights left on, snow falling outside. A fur blanket is spread on the platform. MIRAGE reclines on it in the champagne lace set only, one arm above her head, eyes half closed, flushed, lips parted. RAVEN lies along her side in the black lace set and her long red scarf, propped on an elbow, her free hand resting on MIRAGE's waist, face close above MIRAGE's shoulder, heavy-lidded, the faintest smile. Neither looks at the camera. Colour key: warm brass and deep crimson shadow.",
  ]),
 2: dict(ko=u'STAGE 2 · 화차 44호 — 화물 조차장', ag=['brick', 'glitch'], place_img=['bgw2.jpg'],
  place=u"20:10. A freight marshalling yard in falling snow: five parallel tracks, lines of rust-red, dark green and grey box cars with gaps between them, a dark blue box car with a yellow diagonal band, a yellow shunting locomotive, a brick signal box full of levers, two lattice lighting towers, a low loading platform with warehouse doors, sodium lamps, steam, sleepers, cable reels and oil drums.",
  cuts=[
   u"Full-body two-shot, camera low on the track looking up, the yellow shunting locomotive's headlamp blazing behind them. BRICK stands feet apart with a sledgehammer across her shoulders, grinning down at the viewer. GLITCH sits on BRICK's raised forearm perch-style on the locomotive's step beside her, one arm hooked around BRICK's neck, legs crossed in striped stockings, peering over her glasses with a cocky smile. Colour key: orange headlamp against blue snow night, teal rim on GLITCH.",
   u"Action shot, hard diagonal, camera level with the car roofs. They leap the gap between two box cars together, hands clasped mid-air. BRICK's bomber is blown wide open, braces straining, face roaring with laughter; GLITCH's parka dress zip has slid low and the hem flies up over her stockings, hood off, antlers askew, mouth open in a delighted scream. A burst of orange sparks from the blown lock of the blue car below. Colour key: near-black sky, orange sparks, teal accents.",
   u"Medium two-shot inside the brick signal box among the tall levers, frost on the windows, one bare bulb. GLITCH sits on the lever frame: parka dress unzipped and pushed off her shoulders to the waist, **top half down to the pale teal lace bra with white bows**, stockings on. BRICK stands close behind her with both arms wrapped around GLITCH's middle, chin on her shoulder, bomber still on, grinning at the viewer. GLITCH looks at the viewer with flushed cheeks, biting the arm of her glasses. Colour key: warm bulb amber, blue yard light through the frost.",
   u"Intimate, camera high looking down into an open box car lined with wool blankets, a lantern, a string of fairy lights along the door, snow drifting past the opening. BRICK lies on her back in the black lace set with orange piping, one arm behind her head, goggles pushed up, eyes closed, a lazy flushed smile. GLITCH lies curled against her side in the pale teal lace set, head on BRICK's shoulder, glasses off, one hand spread on BRICK's stomach, looking up at her face with half-closed eyes and parted lips. A plaid blanket covers them both from the hips down. Colour key: lantern gold and deep rust shadow.",
  ]),
 3: dict(ko=u'STAGE 3 · 얼음 위의 선물 — 얼어붙은 호수', ag=['viper', 'doc'], place_img=['bgw3.jpg'],
  place=u"22:30. A small frozen lake in the woods under a full moon: a wide sheet of cracked blue ice dotted with little ice-fishing huts with lit windows, a timber jetty with lanterns and a searchlight, a radio shack with a tall antenna, a boathouse, a log ranger's cabin with a woodshed, pine clumps, boulders, snow drifts, sleds and a snowmobile.",
  cuts=[
   u"Full-body two-shot, camera very low on the ice looking up, the moon behind them. VIPER stands with one boot on a sled, a hand on her hip, looking down at the viewer with a cool half-lidded stare. DOC stands pressed to her side with an arm around VIPER's waist and her head tipped against VIPER's shoulder, the other hand tossing a snowball, a teasing grin. Fishing huts glowing behind. Colour key: silver-blue moonlight, violet and lime rim lights.",
   u"Action shot, strong diagonal, camera tracking alongside. They ride the snowmobile across the ice at speed: VIPER driving, leaning forward, off-shoulder dress slipped lower on one arm, hair whipping, teeth bared in a rare wide grin. DOC rides behind with both arms locked around VIPER's waist, wrap dress flying open over her thigh, head thrown back laughing, earrings flying. A plume of snow and the searchlight beam sweeping past. Colour key: white spray, deep violet night, one lime streak.",
   u"Medium two-shot at eye level inside a tiny ice-fishing hut, a stove glowing, a lantern, frost on the plank walls. DOC kneels on a fur rug: wrap dress untied and off, **top half down to the white lace bra with lime ribbon**, belt and skirt part still wrapped at her hips. VIPER sits behind her on a crate, still dressed, both hands in DOC's curls pinning them up, lips close to DOC's ear. DOC looks at the viewer with flushed cheeks and a slow smile, a finger hooked in one strap. VIPER's eyes are on the viewer too, sideways, amused. Colour key: stove orange, blue cold in the door crack.",
   u"Intimate, camera low at floor level in the ranger's cabin: a stone fireplace, a white fur rug, a small tree, snow at the window. VIPER lies on her back on the rug in the violet lace set, dog tags on her collarbone, one knee raised, one arm over her eyes, lips parted, skin flushed by the fire. DOC lies on her stomach beside her in the white lace set, propped on her elbows, tattooed arm across VIPER's waist, cheek resting on VIPER's shoulder, eyes half closed, smiling. A fur throw is tangled over their legs. Neither looks at the camera. Colour key: deep fire orange and plum shadow.",
  ]),
 4: dict(ko=u'STAGE 4 · 자정 미사 — 대성당', ag=['mirage', 'raven'], place_img=['bgw4.jpg'],
  place=u"Midnight inside a stone cathedral: a long nave of dark wooden pews, rows of square stone columns, shadowed side aisles and chapels, a carved wooden confessional, a raised sanctuary with an altar and an ornate offering chest, hundreds of candles, a decorated tree, a dark crypt passage of tomb niches, and a small bell-ringer's room with a thick rope hanging from the ceiling. Moonlight falls through tall windows.",
  cuts=[
   u"Full-body two-shot from a high angle looking down the centre aisle. They walk away from the altar side by side, arms linked. MIRAGE carries the swapped black bag over her shoulder and glances back up at the camera with a slow conspiratorial wink. RAVEN walks half turned toward her, one hand over MIRAGE's linked hand, looking at MIRAGE and not the camera, the corner of her mouth just lifted. Candle rows on both sides. Colour key: candle gold floor, cold blue vaults.",
   u"Action shot, tilted frame, camera low between two columns of the side aisle. The bell is tolling and dust falls in the light. RAVEN spins MIRAGE behind a column by the waist, both pressed together chest to chest in the shadow; RAVEN's jacket is half off one shoulder, MIRAGE's stole is falling and her dress strap has slipped. RAVEN looks past the column with narrowed eyes and a bitten lip; MIRAGE looks up at RAVEN's face, breathless, flushed, smiling. Knocked candles spark gold. Colour key: black and wine red with gold sparks.",
   u"Medium close two-shot inside the carved confessional, lattice shadows across their skin. MIRAGE sits forward with her dress zipped down and pooled at her waist, **top half down to the champagne satin bra with black lace**, a finger to her lips, lashes lowered, looking into the lens with a knowing smile. RAVEN leans in from behind in the dark, still dressed, arms around MIRAGE's shoulders, pulling her own scarf loose around both their necks, cheek against MIRAGE's temple, eyes on the viewer. Both faintly flushed. Colour key: honey gold through the lattice, deep red shadow.",
   u"Intimate, camera high and three-quarter in the bell-ringer's room: old beams, the thick bell rope, a small stove, candles on the floor, snow at a round window. A velvet cloak is spread over a pile of cushions. RAVEN reclines against the cushions in the black lace set, the red scarf loose around her shoulders, head tipped back, eyes closed, lips parted. MIRAGE lies against her chest in the champagne lace set, long hair spilling over them both, one hand laced with RAVEN's, face turned up toward RAVEN's jaw, heavy-lidded and flushed. Neither looks at the camera. Colour key: candle amber and midnight blue.",
  ]),
 5: dict(ko=u'STAGE 5 · 산타의 썰매 — 사설 비행장', ag=['raven', 'viper', 'glitch'], place_img=['bgw5.jpg'],
  place=u"03:30. A small private airfield in blowing snow: an alley of faded shipping containers, an open floodlit apron with yellow taxi lines, a fuel truck, an orange snowplough, a water tower, a control tower with a glass cab, and a wide open hangar holding a white business jet with a thin crimson line and its stairs down. Blue taxiway lights, the first rose of dawn.",
  cuts=[
   u"Full-body three-shot, camera low on the apron looking up, the jet in the hangar behind them. RAVEN stands in the centre holding the empty ribboned box on her hip, level stare at the viewer. VIPER leans an elbow on RAVEN's shoulder from the left, hip cocked, half-lidded smirk. GLITCH hangs on RAVEN's other arm with both hands, one foot kicked up, grinning. All three in their Christmas outfits, three rim lights in crimson, violet and teal. Colour key: white floodlight, deep blue snow.",
   u"Action shot, strong diagonal, camera high from the control tower. They sprint across the apron in a line holding hands, RAVEN leading, GLITCH in the middle being pulled almost off her feet, VIPER last and laughing. RAVEN's jacket is torn open, VIPER's dress has slipped off both shoulders, GLITCH's zip is at her waist and her antlers are gone; the snowplough's beacon and a sweeping searchlight cut the frame. Faces flushed, breath streaming. Colour key: hard white beam, black shadow, three colour accents.",
   u"Medium three-shot at eye level on the jet's boarding stairs, each on a different step, pressed close. GLITCH sits lowest between VIPER's knees: parka dress off her shoulders, **top half down to the pale teal lace bra**, looking up at the viewer over her glasses, flushed. VIPER sits above her, **skirt gone, bottom half down to the violet lace brief and thigh boots**, dress top still on, chin resting on GLITCH's head, arms draped around her. RAVEN stands one step up behind them, jacket off, **top half down to the black lace bra**, leaning over with a hand on VIPER's shoulder, dry smile at the viewer. Colour key: warm cabin light from the door, blue dawn.",
   u"Intimate, wide and low inside the jet cabin: cream leather, a small tree on the table, champagne flutes, snow streaking past the oval windows, rose-gold dawn. All three in lingerie only, piled together on the wide rear sofa under one cream cashmere blanket that covers them from the waist down. RAVEN sits in the middle in black lace and her red scarf, head back against the seat, eyes closed, flushed. VIPER lies with her head in RAVEN's lap in violet lace, looking up at her with half-closed eyes, one hand lifted to RAVEN's cheek. GLITCH is curled against RAVEN's other side in teal lace, glasses off, cheek resting on RAVEN's shoulder, fingers laced with VIPER's. Nobody looks at the camera. Colour key: rose-gold dawn and soft amber.",
  ]),
}
NAMES = [u'POSE', u'ACTION', u'TEASE', u'PRIVATE']


def md(n):
    s = ST[n]
    t = u'# SILENT SIX — 블러디 크리스마스 리워드 컷 v3 · %s\n\n## 사용법 (사람이 읽는 부분)\n\n1. ChatGPT 새 대화에 이 zip을 올리고 **"압축을 풀고 지시.md 를 끝까지 읽은 뒤, CUT 0부터 한 장씩 진행해 줘."** 라고 보낸다.\n2. 한 번에 한 장. 다음 장은 "next".\n3. 파일명 `r_W-%d_0` ~ `r_W-%d_3` 그대로 Claude에게 넘긴다.\n4. 이 판의 새 맵이 이미 나왔다면 대화에 같이 올리고 "배경은 이 맵 기준"이라고 한 줄 덧붙인다.\n\n| 컷 | 내용 | 복장 |\n|---|---|---|\n| 0 | 멋진 포즈 | 크리스마스 룩 완전 착장 |\n| 1 | 섹시한 액션 | 같은 옷이 움직임에 흐트러짐 |\n| 2 | 관능적 도발 | 상의 또는 하의 한쪽이 속옷 |\n| 3 | 에로틱 무드 | 속옷 차림. 담요 · 머리카락 · 손으로 가림 |\n\n검수: 참여 요원이 **전원** 나왔는지, 시그니처 색이 살아 있는지, 배경이 이 판의 맵인지, 네 장의 구도와 표정이 서로 다른지.\n\n---\n\n' % (s['ko'], n, n)
    t += COMMON + u'## THIS STAGE\n\n**Characters and their Christmas outfits**\n'
    for a in s['ag']:
        v = CS.A[a]
        t += u'- **%s** (`agents/sheet_%s.jpg`, signature colour %s). %s. Christmas outfit: %s\n' % (v[0], a, v[2], v[5][0].upper() + v[5][1:], XMAS[a])
    t += u'\n**The stage map.** %s\n\n## THE FOUR CUTS\n\n' % s['place']
    for k, c in enumerate(s['cuts']):
        t += u'### CUT %d — `r_W-%d_%d` — %s\n\n%s\n\n' % (k, n, k, NAMES[k], c)
    return t


def main(out):
    os.makedirs(out, exist_ok=True); pk = os.path.join(HERE, 'packs'); os.makedirs(pk, exist_ok=True)
    allag = ['raven', 'viper', 'glitch', 'brick', 'mirage', 'doc']
    for n in ST:
        s = ST[n]; zn = 'SILENT6_Reward_BloodyChristmas_V3_Stage%d' % n; text = md(n)
        io.open(os.path.join(pk, u'Winter_V3_Stage%d_지시.md' % n), 'w', encoding='utf8').write(text)
        z = zipfile.ZipFile(os.path.join(out, zn + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        z.writestr(zn + u'/지시.md', text); z.write(os.path.join(CSO, 'AGENTS.md'), zn + '/AGENTS.md')
        for a in s['ag']: z.write(os.path.join(CSO, 'sheet_%s.jpg' % a), '%s/agents/sheet_%s.jpg' % (zn, a))
        for i, f in enumerate(s['place_img']): z.write(os.path.join(PUB, f), '%s/place/%s' % (zn, 'map.jpg' if n == 1 else 'mood_old_map.jpg'))
        for i, a in enumerate(s['ag']): z.write(os.path.join(PUB, 'a_%s_%d.jpg' % (a, 2)), '%s/look/look_%d.jpg' % (zn, i + 1))
        z.close(); print(zn, os.path.getsize(os.path.join(out, zn + '.zip')) // 1024, 'KB', len(text))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'out')
