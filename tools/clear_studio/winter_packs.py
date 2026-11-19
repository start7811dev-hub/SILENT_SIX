# -*- coding: utf-8 -*-
"""블러디 크리스마스 리워드 컷: 스테이지별 zip 5개를 만든다.
사용: python3 tools/clear_studio/winter_packs.py <출력 폴더>
zip 하나 = 지시.md + refs/(요원별 참조 4장) + look/(완성도 기준 4장)
"""
import sys, os, io, zipfile
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); PUB = os.path.join(HERE, '..', '..', 'public')
sys.path.insert(0, os.path.join(HERE, '..', 'charsheet'))
import build as CS
LOOK = {k: u'%s — %s. Signature colour %s. Tactical outfit: %s' % (v[0], v[5], v[2], v[6]) for k, v in CS.A.items()}
REFK = [0, 3, 4, 6]   # 정면 초상 / 클로즈업 / 역동 액션 / 전투

COMMON = u'''## FOR THE IMAGE MODEL — READ ALL OF THIS FIRST

You are producing four pieces of premium key art for one stage of a game. They will be shown side by side as a set, so they must look like **four different illustrations by the same artist**, not four takes of one pose.

### Files
- `AGENTS.md` and `agents/sheet_<name>.jpg` — the cast bible. Each sheet has three labelled panels: `NAME-A` face (identity, this wins), `NAME-B` glam, `NAME-C` tactical outfit, plus her signature colour. Characters are referred to by code name. Read AGENTS.md first.
- `look/` — four finished images from this game. They set the **quality bar**: level of detail, lighting, rendering finish. Match that finish. Do not copy their poses or compositions.

### Output
- 4 separate images, one per reply. Vertical portrait, 2:3, **1024x1536**. Write the file name on its own line before each image. Never make a grid or collage. After each image wait for "next". Do not ask questions.

### Identity
- Keep each woman exactly as in her references: same face, hair, eye colour, build, signature accent colour. Everyone is an adult woman in her late twenties.
- When a cut lists two or three characters, **all of them appear**, clearly distinct, none merged or dropped.

### Quality — every image must have all of this
- Semi-realistic anime illustration with a painterly, high-end finish like the `look/` images: detailed eyes and hair strands, real fabric and leather texture, stitched seams, metal that reflects its surroundings.
- **Three depth layers**: something in the foreground (out-of-focus snow, a railing, a lantern, a branch), the character(s) in the midground, a fully painted location in the background. No empty or flat backdrops, no plain gradients.
- **Two light sources of different colour** (for example cold blue moonlight against warm string lights) plus a rim light separating the character from the background. Visible atmosphere: falling snow at different depths, breath in the cold, drifting steam or smoke, bokeh.
- The location must be recognisable as the place described for this stage, with at least five specific props from it.
- Hands, weapons and gear drawn carefully and correctly. Faces fully visible and unobstructed unless a cut says otherwise.
- No text, no logo, no watermark, no UI.

### Variety — this is what failed last time, so follow it strictly
The four cuts are specified with a different **shot size, camera angle, head angle, gaze, expression, pose and colour key** each. Follow each cut's camera line literally. Across the four images:
- no two images share the same camera angle or shot size;
- no two images share the same facial expression or head direction;
- the character must not simply stand facing the camera in more than one image;
- the colour key changes from cut to cut as written.

### Wardrobe ladder — exposure rises from cut to cut
- **CUT 0**: the full outfit, complete and intact.
- **CUT 1**: the same outfit under stress: jacket open or torn at a shoulder, a zip pulled lower, a glove lost. Still dressed.
- **CUT 2**: clearly more revealing: outer layers off, down to a fitted top or bralette and shorts or stockings, one strap slipping, bare shoulders, midriff and thighs.
- **CUT 3**: the boldest. **No clothing and no underwear visible on her torso.** She is covered only by her own hands and arms, her hair, a turned shoulder or raised knee, or one prop named in the cut (her scarf, a fur blanket, a robe sliding off, a towel, steam). The pose must look natural and unposed, a private moment, not a pin-up presented to the camera. Keep one signature item on her (scarf, dog tags, glasses, goggles, earrings, armband) so she is still recognisably herself.

### Limits (never cross)
Implied only. Nipples, areolae and genitals are never visible in any cut: always fully hidden by hands, arms, hair, pose or the prop. No sexual acts, no touching between characters beyond leaning or an arm around a shoulder. Everyone is an adult woman in her late twenties.

---

'''

ST = {
 1: dict(ko=u'STAGE 1 · 첫 번째 상자 — 크리스마스 마켓', ag=['raven'],
  place="18:40, Christmas Eve. A snowy city-hall square Christmas market: rows of wooden stalls with red-and-white striped awnings and snow on the roofs, a giant decorated tree ringed by a low fence with a pile of wrapped gifts at its foot, a lit carousel, a frozen fountain, a small wooden stage with red curtains, an arched stone gate, iron street lamps, garlands and wreaths on the surrounding arcades.",
  story="She goes in alone and lifts Santa's delivery list from the gift pile under the tree. The square is full of civilians, so nobody dies tonight.",
  cuts=[
   ("Wide establishing shot, full body, low camera about knee height looking up from three-quarters behind her. She walks away through the stone gate arch, body turned away, head turned back over her left shoulder toward the glowing tree. Expression: a small tired half-smile of relief, eyes soft. One hand holds a ribbon-tied envelope against her chest, the red scarf trailing in the wind. Colour key: deep blue dusk with the warm gold of the market behind her; she is rim-lit in gold. Foreground: blurred iron lamp post and falling snow."),
   ("Dynamic action shot with a strong diagonal tilt, medium-full, camera high and to the side looking down into a dark service lane behind the stalls. She is mid-motion in a low lunge, locking a choke hold on a fake shopper in a Santa hat whose face is turned away. Her face is in three-quarter profile, jaw set, teeth clenched, eyes narrowed on the target, hair whipping. Red scarf flying across the frame, kicked-up snow, a dropped paper cup spilling. Colour key: cold teal shadow cut by one hard red light from a stall sign. Background: backs of stalls, crates, blurred string lights."),
   ("Medium close-up from the waist up, camera slightly above eye level, shallow depth of field. She leans back on her elbows against a closed stall counter, head tilted to her right, looking straight into the lens with one eyebrow raised and a slow smirk, pulling the red scarf down off her mouth with two fingers. Winter jacket hanging off both elbows over a black bralette, bare shoulders and midriff, a steaming cup of mulled wine by her hand, a stolen Santa hat hooked on a finger. Colour key: warm amber and candy red, carousel lights spinning into bokeh behind her. Foreground: a blurred garland with baubles."),
   ("Intimate interior, full figure, camera low at floor level in three-quarter view from her right side. A small attic room above the square, fairy lights around a frosted window, a tiny tree, a wool blanket. She sits sideways on the window sill, one knee drawn up, wearing nothing but her long red scarf, which drapes down her front, one arm folded across her chest; a fur-trimmed robe has slid off onto the sill behind her. She does not look at the camera: her head is turned toward the window, eyes half closed, a quiet private smile, the unopened envelope on the sill beside her. Colour key: firelight amber inside against blue snowlight from the window."),
  ]),
 2: dict(ko=u'STAGE 2 · 화차 44호 — 화물 조차장', ag=['brick', 'glitch'],
  place="20:10. A freight rail yard at night in falling snow: long lines of red, green and blue boxcars with snow on their roofs, rails and sleepers on gravel, lamp-lit gaps between cars, a brick signal cabin with a chimney, two tall floodlight towers, a chain-link fence, stacked crates and timber, one boxcar glowing teal with gift-wrapped crates inside.",
  story="The breacher and the hacker find the one marked boxcar among dozens, kill the floodlights, and blow Santa's crates.",
  cuts=[
   ("Wide shot from behind at a low angle, both full body, walking away down the track toward the camera's left. Far behind them a boxcar burns orange. BRICK has the sledgehammer across her shoulders, head thrown back mid-laugh, breath steaming. GLITCH walks half a step behind, looking down at a detonator switch she is flipping closed, a small satisfied grin, glasses reflecting the fire. Colour key: orange fire against blue night. Foreground: blurred rail and drifting embers."),
   ("Action shot, hard diagonal, camera low and close beside the boxcar wall looking up. The floodlights have just died: the only light is the teal spark of GLITCH's drone above and a burst of orange from the breach. BRICK is mid-swing, body twisted, face in profile roaring with effort, splinters and snow exploding outward toward the lens. GLITCH crouches in the background by the rail, one hand on her headset, head turned sharply over her shoulder, eyes wide and alert. Colour key: near-black with teal and orange."),
   ("Medium two-shot at eye level, camera straight on. They sit in an open boxcar door, legs dangling, jackets tied round their waists, down to sports bralettes, bare midriffs steaming in the cold. BRICK leans back on one arm, chin up, grinning wide straight at the viewer, a thermos lid in her taped hand. GLITCH leans against her shoulder, head tilted the other way, looking at the viewer over the top of her glasses with a teasing sideways smile, a ribbon from a gift box wound round her fingers, a Santa hat on her knee. Colour key: warm lantern gold inside the car, blue snow outside, sparks drifting past in the foreground."),
   ("Intimate interior, camera high, looking down at an angle into a warm caboose: iron stove, wool blankets, fairy lights along the ceiling, frosted windows. Neither wears a top: each is wrapped only in a loose wool blanket slipping off bare shoulders and back. BRICK sits on the floor against the bench, one knee up, head turned in profile toward the stove, eyes closed, calm, warming her taped hands. GLITCH lies along the bench above her on her stomach, Santa hat tipped over one eye, chin on her folded arms, looking down at BRICK with a soft sleepy smile. Neither looks at the camera. Colour key: stove amber and deep red shadow."),
  ]),
 3: dict(ko=u'STAGE 3 · 얼음 위의 선물 — 얼어붙은 호수', ag=['viper', 'doc'],
  place="22:30. A vast frozen lake under a full moon in a blizzard: cracked blue ice with wind-blown snow streaks, small ice-fishing huts with lit windows, a wooden pier with lanterns, a timber boathouse, a lakeside lodge, sleds and barrels on the shore, bare birch trees and snow-covered rocks.",
  story="The sniper covers the open ice while the medic crosses in the blizzard to reach a wounded witness held in the boathouse.",
  cuts=[
   ("Very wide shot, both small in a huge landscape, camera high above the shore looking down across the lake. They walk toward the birch forest away from the boathouse, whose door stands open and glowing. DOC is in front, half turned back with one arm raised in a wave toward the boathouse, laughing. VIPER walks behind with the long rifle across her shoulders, head down, hair blown across her face, a faint smile only. Colour key: moonlit silver-blue with one warm doorway. Foreground: snow-laden birch branches."),
   ("Extreme action close shot split by depth. Foreground, very close and low: VIPER prone in the snow behind a sled, cheek on the rifle stock, one eye open and cold, face in tight profile, frost on her eyelashes, the muzzle toward the right edge. Deep in the blurred background DOC sprints across the ice bent low, medical bag in hand, snow tearing sideways in the gust. Hard diagonal composition, wind lines across the whole frame. Colour key: white-out greys and violet."),
   ("Medium shot, camera low at knee height looking up, inside the boathouse doorway with the lake behind. DOC kneels facing the viewer, pulling a lime-green glove off with her teeth, eyes up at the lens, a wicked playful grin, parka open over a lime bralette. VIPER stands behind her leaning on the door frame, arms crossed, looking down at the viewer sideways with one eyebrow lifted and a cool smirk, the rifle propped beside her. Colour key: lantern gold inside, blue blizzard outside, steam of breath."),
   ("Intimate interior seen through a foreground of blurred fairy lights, camera at eye level from the side. A lodge room with a stone fireplace, fur rugs, a small tree. VIPER lies on her back on the rug bare under a white fur throw that covers her from the chest down, one arm over her head, the other hand holding the fur to her chest, eyes on the ceiling, lips parted in a slow exhale. DOC sits beside her bare-backed, seen from behind in three-quarter view with her knees drawn up and one arm across her chest, a ribbon choker and her hoop earrings on, leaning on one hand, looking down at VIPER and brushing a strand of silver hair from her face, a tender smile. Neither looks at the camera. Colour key: deep fire orange and plum shadow."),
  ]),
 4: dict(ko=u'STAGE 4 · 자정 미사 — 대성당', ag=['mirage', 'raven'],
  place="00:00. The interior of a grand gothic cathedral at midnight mass: long rows of dark wooden pews, stone pillars with hanging lanterns, stained-glass windows, hundreds of candles, a raised sanctuary with a red carpet, a white-clothed altar and golden candlesticks, carved confessionals, a great bell tolling above.",
  story="Under cover of the midnight bell, the infiltrator in choir robes and the leader in the shadows swap the money bag in the offering chest for one carrying a tracker.",
  cuts=[
   ("Wide shot down the centre aisle from a high balcony angle, both full body and small against the architecture. They walk out side by side toward the great doors, backs to the altar. MIRAGE in a white-and-gold choir robe glances sideways at RAVEN with a pleased, conspiratorial smile. RAVEN, in dark gear with the red scarf, looks straight ahead, expression flat and composed, one hand resting on the strap of the swapped bag. Colour key: candle gold floor, cold blue vaults above. Foreground: a blurred stone balustrade and candle flames."),
   ("Tense action moment, tilted frame, camera very low between two pews looking up. The bell is tolling: dust shakes from the vault. RAVEN drops from a pillar behind a guard, mid-air, face foreshortened from below, eyes locked, mouth a hard line, scarf streaming upward. In the same frame MIRAGE at the altar rail spins in her robe, head whipping round in three-quarter back view, eyes wide, the bag half hidden in her sleeve. Colour key: deep red and black with gold sparks from a knocked-over candlestick."),
   ("Medium close two-shot at eye level inside a carved confessional, lattice shadows across them. MIRAGE sits forward, the choir robe unbuttoned to the waist and off both shoulders over a black lace bralette, chin resting on the back of her hand, looking into the lens with lowered lashes and a slow knowing smile, a finger to her lips. RAVEN leans in from behind in the shadow, head tilted the opposite way, eyes on the viewer over MIRAGE's shoulder, the faintest smirk, the scarf pulled loose. Colour key: honey gold light through the lattice, wine-red shadow."),
   ("Intimate interior, camera high and three-quarter, a bell-ringer's loft room: old timber beams, a small stove, candles, snow at a round window. MIRAGE reclines along a chaise with a sheer black robe fallen open to her waist, her long hair and one forearm covering her chest, head tipped back, eyes closed, a contented smile, a ribbon wound round her wrist. RAVEN sits on the floor leaning back against the chaise bare-shouldered with only the red scarf wound loosely round her chest and held there by one hand, face in profile looking up at the falling snow in the window, calm, a glass in her hand. Neither looks at the camera. Colour key: candle amber and midnight blue."),
  ]),
 5: dict(ko=u'STAGE 5 · 산타의 썰매 — 사설 비행장', ag=['raven', 'viper', 'glitch'],
  place="03:30. A private airfield before dawn in heavy snow: a lit runway with rows of amber edge lights, a control tower with a sweeping searchlight, an open hangar with a silver private jet inside, fuel trucks, a yellow snowplow, stacked cargo cases, snowbanks and a chain-link fence.",
  story="Three agents cross the open apron before take-off and reach the jet's cargo. Inside there is only an empty ribbon-tied box and a card addressed to their own unit.",
  cuts=[
   ("Wide shot from inside the hangar looking out, camera low near the floor. The three stand in a loose triangle by the jet's open cargo door, all full body, each facing a different way. RAVEN in the centre holds the open empty box, head bowed over the card, brow drawn, mouth tight. VIPER stands to the left with her back mostly to the camera, rifle slung, head turned in profile toward the runway, watchful. GLITCH crouches at the right with a tablet, looking up at RAVEN with a worried questioning look. Colour key: cold teal hangar light, amber runway lights beyond. Foreground: a blurred wheel strut and drifting snow."),
   ("Action shot, strong diagonal, camera high from the control tower's point of view with the searchlight beam cutting the frame. RAVEN sprints across the apron in the beam's edge, body low, face turned back over her shoulder, teeth bared. VIPER slides on one knee behind a fuel truck in the foreground, rifle up, face in tight profile, one eye closed. GLITCH in the background reaches up to a junction box on the tower base, head tilted down, tongue between her teeth in concentration, drone sparking teal. Colour key: white searchlight, black shadow, teal and red accents."),
   ("Medium three-shot at eye level on the jet's boarding stairs, each on a different step. GLITCH sits lowest, leaning forward with elbows on knees, grinning straight at the viewer with her glasses pushed up in her hair, a ribbon from the box tied round her neck like a bow. RAVEN sits in the middle, leaning back on her hands, head tilted, looking at the viewer through half-closed eyes with a dry smile, jacket off her shoulders over a bralette. VIPER stands at the top leaning on the rail, looking down and away to the side with a small amused smile, a Santa hat dangling from her fingers. Colour key: warm cabin light from the jet door behind them, blue snow dawn."),
   ("Intimate interior, camera low and wide inside the jet's cabin: cream leather seats, a small decorated tree on the table, champagne flutes, snow streaking past the oval windows, first light of dawn. None of them wears a top; each is covered only by her own arms and hair or a cabin blanket in her signature colour. VIPER lies across a seat with her legs over the armrest, head back, eyes closed, humming. GLITCH sits cross-legged on the carpet wrapped in a blanket, looking up and laughing at something off-frame. RAVEN stands at a window with one hand on the frame, three-quarter back view, face in profile looking out at the dawn, the card in her other hand, thoughtful. Nobody looks at the camera. Colour key: rose-gold dawn and soft cabin amber."),
  ]),
}
TAGS = ['clear', 'combat', 'tease', 'private']


def md(n):
    s = ST[n]
    t = u'# SILENT SIX — 블러디 크리스마스 리워드 컷 · %s\n\n## 사용법 (사람이 읽는 부분)\n\n1. ChatGPT 새 대화에 이 zip 파일을 그대로 올린다.\n2. 다음 한 줄을 보낸다: **"압축을 풀고 지시.md 를 끝까지 읽은 뒤, 첫 번째 이미지부터 진행해 줘."**\n3. 한 번에 한 장씩 나온다. 다음 장은 "next".\n4. 파일명 `r_W-%d_0` ~ `r_W-%d_3` 그대로 저장해 Claude에게 넘긴다.\n\n네 장은 구도 · 얼굴 각도 · 표정 · 색이 서로 다르게 지정돼 있다. 한 장이 다른 장과 비슷하게 나오면 "CUT 번호의 camera 줄을 그대로 다시 지켜서 다시 그려 줘" 라고 돌려보낸다.\n\n---\n\n' % (s['ko'], n, n)
    t += COMMON
    t += u'## THIS STAGE\n\n**Characters**\n'
    for a in s['ag']:
        t += u'- **%s**. Sheet: `agents/sheet_%s.jpg`.\n' % (LOOK[a], a)
    t += u'\n**Place.** %s\n\n**What happens.** %s\n\n**Tone.** Christmas Eve night. Each agent\'s tactical outfit from her sheet, winterised with fur trim, breath in the cold, snow everywhere.\n\n## THE FOUR CUTS\n\n' % (s['place'], s['story'])
    names = ['MISSION CLEAR', 'COMBAT', 'TEASE', 'PRIVATE NIGHT']
    for k, c in enumerate(s['cuts']):
        t += u'### CUT %d — `r_W-%d_%d` — %s\n\n%s\n\n' % (k, n, k, names[k], c)
    return t


def main(out):
    os.makedirs(out, exist_ok=True); pk = os.path.join(HERE, 'packs'); os.makedirs(pk, exist_ok=True)
    for n in ST:
        s = ST[n]; zn = 'SILENT6_Reward_BloodyChristmas_Stage%d' % n; text = md(n)
        io.open(os.path.join(pk, u'Winter_Stage%d_지시.md' % n), 'w', encoding='utf8').write(text)
        z = zipfile.ZipFile(os.path.join(out, zn + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        z.writestr(zn + u'/지시.md', text)
        z.write(os.path.join(HERE, '..', 'charsheet', 'out', 'AGENTS.md'), zn + '/AGENTS.md')
        for a in s['ag']:
            z.write(os.path.join(HERE, '..', 'charsheet', 'out', 'sheet_%s.jpg' % a), '%s/agents/sheet_%s.jpg' % (zn, a))
        other = [x for x in LOOK if x not in s['ag']][:2]
        for i, (a, k) in enumerate([(other[0], 4), (other[0], 6), (other[1], 3), (other[1], 7)]):
            z.write(os.path.join(PUB, 'a_%s_%d.jpg' % (a, k)), '%s/look/look_%d.jpg' % (zn, i + 1))
        z.close(); print(zn, os.path.getsize(os.path.join(out, zn + '.zip')) // 1024, 'KB')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'out')
