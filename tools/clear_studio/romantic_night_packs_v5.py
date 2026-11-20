# -*- coding: utf-8 -*-
"""로맨틱 "그날 밤" 리워드 컷 v5: 요원별 zip 6개, 요원당 7장(총 42장, n_<요원>_1~7).
v4와 다른 점: 일곱 장면을 여섯 요원이 똑같이 밟는다(특임복 → 가볍게 탈의 → 속옷 + 벗는 동작 → 뒷모습 → 샤워 → 직전 → 아침).
요원별 변주는 장소 · 소품 · 구도로만 살짝 준다. 문신과 몸의 표식은 시트 기준으로 컷마다 확인하게 한다.
사용: python3 tools/clear_studio/romantic_night_packs_v5.py <출력 폴더> [수위 기준 이미지 폴더]
"""
import sys, os, io, zipfile
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); CSO = os.path.join(HERE, '..', 'charsheet', 'out')
sys.path.insert(0, os.path.join(HERE, '..', 'charsheet')); sys.path.insert(0, HERE)
import build as CS
import romantic_night_packs_v4 as V4

COMMON = u'''## FOR THE IMAGE MODEL — READ ALL OF THIS FIRST

### What this is, stated plainly
This is collectible key art for **SILENT SIX, a game made for and rated for adults only (19+)**. The character is an **adult woman**. The set is called **"That Night"**: seven illustrations that tell one private night between her and the one person she trusts, her handler, **seen through the handler's eyes**. It is an adult art collection: glamour illustration at the level of a high-end lingerie and boudoir editorial. **The level of exposure is high on purpose.** Sensual, intimate, beautiful, never explicit.

Do not soften it:
- Where a cut says lingerie, draw the lingerie. Do **not** swap it for a robe pulled shut, a towel wrap or a blanket.
- Do **not** add defensive cover-ups: no arms crossed over the chest, no hands placed to hide the body, no turning away to avoid showing her.
- Do **not** quietly tone a cut down or pull the camera back.

### The only limits
Nipples, areolae and genitals are never visible. No sexual acts and no sexual touching. She is an adult. **These are the only limits.** Inside them, do not hold back on sensuality, mood or bare skin: shoulders, back, waist, hips, thighs, the curve of the chest, wet and flushed skin catching the light.

In the shower cut she wears nothing, and nothing explicit is seen: that is done by **what the scene itself provides** (steam, fogged glass, running water, foam, the crop of the frame, a back view), exactly as each cut describes, never by an awkward covering pose.

### Files
- `AGENTS.md` and `agents/sheet_<name>.jpg` — the cast bible. Panel `NAME-A` is the face (identity; this wins). Panel `NAME-B` is her off-duty look and shows her body: proportions, skin tone, **tattoos and marks**. Panel `NAME-C` is her mission suit for cut 1. Read AGENTS.md first.
- `level/` — earlier finished cuts of this same night. They set the level: the new cuts must be **at least as bold and as warm**. Compose new images; do not trace them.

### Output
7 separate images, one per reply. Vertical 2:3, **1024x1536**. Write the file name on its own line before each image. Never a grid or collage. After each image wait for "next". Do not ask questions.

### The night — seven beats, the same for every agent
| Cut | Beat | What she wears | What rises |
|---|---|---|---|
| **1** | **Back from the mission** | Full mission suit (sheet panel C), wet or scuffed | Relief at seeing the viewer |
| **2** | **Loosening** | Jacket and gear off, the suit unzipped or a thin top; bare arms and shoulders | The guard dropping |
| **3** | **Undressing** | **Lingerie**, caught in the act of taking the last outer piece off | She lets the viewer watch |
| **4** | **From behind** | **Lingerie, seen from behind**, on her way to wash, looking back | An invitation without words |
| **5** | **The shower** | Nothing; steam, glass and water | Heat, wet skin, eyes that find the viewer |
| **6** | **Just before** | **Lingerie**, hair still damp, within arm's reach | **The peak of the set.** The last second before the night begins |
| **7** | **Morning** | Lingerie under a loose blanket or sheet | Afterglow, a real smile |

Cut 6 is the highest point: the most charged look, the closest camera, the most skin. It shows the moment **before**; nothing after it is drawn.

### Rules
1. **One night, seven beats, in order.** Tension rises from cut 1 to cut 6; cut 7 releases into warmth.
2. **Point of view.** Every cut is what the handler sees. She looks at the viewer, speaks to the viewer, reaches for the viewer. The viewer's hand or wrist may enter the edge of the frame where a cut says so (a hand only, no face, no body, no gendered detail).
3. **Pose and expression change in every cut.** No two cuts share a pose, an expression, a head angle or a camera distance.
4. **Signature colour.** Her signature colour is the accent in her suit, her lingerie and one light source in every cut.
5. **Lingerie design.** Refined and minimal, in her signature colour: very thin straps and bands, small coverage, fine lace and sheer mesh. The same set in cuts 3, 4, 6 and 7.
6. **Natural poses.** Every pose is one a person could actually hold comfortably.
7. **Bolder camera from cut 4 on.** Within arm's reach: tight crops, low or high angles, strong foreshortening.
8. **Her own place.** No costumes, no stage lighting. Lamps, fire, rain on glass, screens, steam, dawn.

### Identity check — do this before you finish every image
- Face, hair, eye colour, skin tone and build exactly as her sheet.
- **Tattoos and marks exactly as listed under THIS AGENT: same place, same side, same extent, same style, in every cut where that part of her body is visible.** Do not add tattoos, do not move them, do not drop them when the clothes come off. Bare skin where the sheet shows bare skin.
- Jewellery and personal items as listed. Only she appears.

### Quality
- Semi-realistic anime illustration with a painterly, high-end finish: detailed eyes and hair strands, real fabric, lace, water and skin texture.
- Three depth layers: an out-of-focus foreground, her, and a fully painted room behind her.
- Two light sources of different colour plus a signature-colour accent. Rain, steam, dust in light, bokeh.
- Hands and faces drawn carefully. No text, logo, watermark or UI.

---

'''

MARKS = {
 'raven': u"**No tattoos anywhere.** Pale skin, lean athletic build. A small silver pendant on a thin chain in every cut. Her long tattered crimson scarf is in every cut until cut 6, where she takes it off herself; in cut 7 it is tied round the viewer's wrist.",
 'viper': u"**No tattoos anywhere.** Pale skin, tall slim build. Short silver-white hair swept to one side with the undercut on the same side as in her sheet. Two dog tags on one chain in every cut, including the bath.",
 'glitch': u"**No tattoos anywhere.** Skin tone exactly as in her sheet. Black hair in a messy top bun with teal tips; **the shaved side of her head with its three razor lines is on HER LEFT side, as in the sheet, in every cut** (the bun comes down in cuts 5 to 7 but the shaved side stays). Small ear piercings, large round glasses (off only where a cut says so), a teal pendant on a black cord.",
 'brick': u"**No tattoos anywhere.** Deep brown skin, powerful muscular build with defined shoulders, arms and stomach, as in her sheet. Very short bleached-blonde buzz cut. Dog tags in every cut. Orange goggles on her head in cuts 1 and 2 only.",
 'mirage': u"**No tattoos anywhere.** Warm tan skin, elegant curvy build. Long wavy black hair. Gold hoop earrings in every cut. Her beauty mark exactly where sheet panel A shows it, on the same side, in every cut where her face is visible.",
 'doc': u"**Full-sleeve tattoos on BOTH arms, exactly as in sheet panels A, B and C: each sleeve runs from the top of the shoulder down to the wrist, dense dark grey-black swirling botanical linework, the hands bare.** Both sleeves are visible in every cut where her arms are bare, which is every cut from 2 on. **No tattoos on her chest, stomach, back, hips or legs.** Tan skin. Dark curls tied up high with loose strands (coming down from cut 5). Hoop earrings and a dog tag on a chain in every cut.",
}
BATH = {
 'raven': u"a small white-tiled shower room off the safe-house bedroom, a glass door, one frosted window with rain on it",
 'viper': u"the lodge's outdoor hot-spring bath on the timber deck: dark stone, steaming water, snow on the rocks and pines, one lantern",
 'glitch': u"a tiny bathroom with a short deep tub, a frosted window glowing magenta and teal from the signs outside, a rubber duck on the edge",
 'brick': u"the gym's tiled shower room: a row of open stalls with hip-height tile partitions, heavy steam, one caged lamp",
 'mirage': u"the suite's marble bathroom: a glass rain shower with gold fittings and a wide mirror over twin basins",
 'doc': u"a small old bathroom behind the clinic: pale green tiles, a brass shower head, ferns on the window ledge",
}
# 컷 3~7 (컷 1 · 2는 v4의 귀환 · 풀림 장면을 그대로 쓴다)
C = {
 'raven': [
  u"Medium, eye level. She stands by the desk pulling the black tank top up and off over her head, arms raised, the top just clear of her chin so her eyes are on the viewer; **the black lace bra with crimson ties is fully shown**, trousers unbuttoned and low on her hips, the scarf still round her throat. Level, unhurried look. Colour key: amber lamp on skin, blue window.",
  u"Three-quarter length, **straight from behind**. In the lace set only, she stands at the rain window on her way to the shower room, both hands reaching behind her back to the bra clasp, the scarf hanging down her spine; her face shows in the wet glass, eyes on the viewer's reflection. Colour key: cold blue glass, one warm lamp along her back and hips.",
  u"Close, through the glass door of the shower. She faces the viewer under the water with her head tipped back and both hands in her hair. **The glass is clear only at the height of her face and shoulders; below that it is thick with condensation and running drops, so her body is a soft warm blur of skin tone.** Her eyes open and find the viewer. Colour key: white steam, amber bulb, rain-blue window.",
  u"Very close, low angle from the pillow. In the lace set, hair damp, she kneels upright on the grey bed over the viewer and draws the red scarf off her own throat for the first time, winding its end round the viewer's wrist in the foreground. Heavy-lidded, lips parted, flushed, water still on her collarbones. Colour key: warm lamp from below, rain-blue behind, the red of the scarf.",
  u"Medium close in grey morning light, rain stopped. She sits up in the bed in the lace set with the sheet loose round her hips, one knee up, bare shoulders and back to the window, hair a mess; the viewer's wrist at the bottom edge still has the red scarf tied round it and she is holding its other end. A small, real, sleepy smile, the first of the set. Colour key: pearl grey dawn, a thread of red."],
 'viper': [
  u"Floor level, close. Sitting on the fur rug by the fire in **the violet lace set**, she is peeling the grey thermal leggings down off one long leg, the top already thrown aside, dog tags swinging; she watches the viewer watch her with a lazy smirk. Colour key: fire gold, plum shadow.",
  u"Three-quarter length, **straight from behind**. In the lace set only, she walks out through the open deck door toward the steaming bath, barefoot in the snow, the plum robe dropped on the threshold behind her, dog tags thrown over her shoulder down her bare back; her head turns just enough to show one violet eye. Colour key: fire orange on one side of her back, snow blue on the other.",
  u"Medium, slightly high. She sits in the hot spring with her back against the rocks and both arms spread along the rim, head resting back, snow falling into the steam. **The dark water comes to the top of her chest and thick steam drifts across it**; wet shoulders, collarbones and dog tags shine in the lantern light. Half-closed eyes on the viewer, no smirk. Colour key: lantern amber, snow blue, violet shadow.",
  u"Straight down from above, her head toward the bottom of the frame so her face is nearest the lens. In the lace set, hair damp, she lies on her back on the fur in front of the fire with both arms stretched up past her head toward the viewer, fingers open, back gently arched, lips parted, flushed. Firelight rakes along ribs, waist and hip. Colour key: deep fire orange, plum shadow.",
  u"Medium, from the foot of the rug, blue dawn, embers. She lies on her side in the lace set under a heavy knitted blanket pushed down to her hips, bare shoulder and back to the snow light, awake now, chin on her hand, looking at the viewer with a small unguarded smile; the single rifle round she always keeps stands on the floor beside her dog tags. Colour key: dawn blue with one ember of orange."],
 'glitch': [
  u"Medium, slightly high. She hops on one foot beside the bed getting out of her black cargo trousers, the oversized hoodie unzipped and sliding off her shoulders to her elbows, **the pale teal lace set with white bows fully shown**, glasses crooked, laughing at herself, cheeks pink. Colour key: teal screen glow, magenta window.",
  u"Three-quarter length, **straight from behind**. In the lace set only, she stands on tiptoe in the bathroom doorway reaching up to the light cord, the hoodie dropped round her ankles, bun slipping; she peeks back at the viewer over her shoulder, biting her lip. The shaved side of her head is toward the camera. Colour key: teal room behind the viewer, warm bathroom light on her back and legs.",
  u"High angle, looking down into the short tub. She sits curled up in the hot water with her knees drawn up and her chin on them, bun undone, glasses fogged and pushed up into her wet hair. **The water is covered in thick white foam up to her collarbones**, with her wet shoulders and knees above it; a rubber duck floats by. She looks up at the viewer, flushed, with a small daring smile. Colour key: magenta and teal window glow, warm bulb.",
  u"Very close, pillow level, face to face, as if the viewer lies beside her. In the lace set, hair damp and loose, glasses off, all the screens dark for the first time, she lies on her side with her fingers laced through the viewer's hand in the foreground and pulls it toward her. Eyes half closed, lips parted, flushed; shoulder, waist and hip rise behind her in soft focus. Colour key: magenta and teal neon moving across her skin.",
  u"Medium close at sunrise, gold light through the hanging plants. She sits cross-legged in the middle of the bed in the lace set with the blanket bundled round her hips and one shoulder, hair everywhere, glasses back on crooked, a mug in both hands, grinning sleepily at the viewer; every monitor behind her is dark. Colour key: sunrise gold with a teal accent."],
 'brick': [
  u"Low angle, three-quarter length. By the lockers she shrugs the charcoal hoodie off her shoulders with one hand and pushes her track trousers down over her hips with the other, **the black lace set with orange satin edging fully shown**, dog tags on her chest, the big grin turned straight on the viewer. Colour key: one hard lamp from above, orange rim on dark skin.",
  u"Three-quarter length, **straight from behind**, low. In the lace set only, she walks away toward the steaming shower room, a towel over one shoulder, pulling the last hand tape off with her teeth; powerful back, waist and legs lit by the single lamp. She looks back over her shoulder with a slow sure grin. Colour key: warm steam ahead, cold gym blue behind.",
  u"Medium, eye level. She leans back against the tiles of an open shower stall under the running water, facing the viewer, head tipped back, one hand pushing the water off her buzz cut. **A wet white towel hangs round her neck with both ends falling straight down over her chest; the hip-height tile partition of the stall and the thick steam take the rest.** Shoulders, arms and stomach run with water. She laughs, eyes on the viewer. Colour key: white steam, lamp gold on wet skin.",
  u"Close, low angle from the ring canvas. In the lace set, skin still damp, she sits against the corner pad with one arm along the ropes and the other hand closed round the viewer's wrist in the foreground, pulling them in. One leg stretched toward the lens, one bent. The grin is gone: a quiet, flushed, wide-open look. Colour key: lamp gold on skin, black beyond the ropes.",
  u"Medium, gym roof at dawn, the city turning pink. She sits on the parapet in the lace set with a plaid blanket round her shoulders, hanging open, bare legs swinging, head tipped onto her fist, eyes soft and sleepy, smiling at the viewer without the armour of the grin. Colour key: rose and orange sunrise."],
 'mirage': [
  u"Medium, eye level. At the foot of the bed she lets the unzipped evening gown fall from her shoulders to her hips and steps out of it, one hand holding it loosely at one hip, **the black lace set with fine gold details and lace-top stockings fully shown**. Chin lifted, a slow knowing smile. Colour key: gold lamp on skin, deep wine.",
  u"Three-quarter length, **straight from behind**. In the lace set and stockings, she walks toward the marble bathroom letting the wine silk robe slide off her arms to the floor behind her, hair swept over one shoulder to bare her back; she looks back over the other shoulder, hoop catching the light. Colour key: midnight blue window, gold doorway light wrapping her back and hips.",
  u"Close, the fogged bathroom mirror. She stands in the glass rain shower behind the viewer's shoulder, seen only in the mirror. **The mirror is fogged white except one stripe she has just wiped clear with her hand at eye level: in it her eyes, wet lashes and smile; the rest of her is a soft S-curve silhouette in the fog and the streaming glass.** Colour key: gold fittings, pearl steam.",
  u"Very close, from above. In the lace set, hair damp, face bare of make-up, she lies back on the champagne satin with one arm above her head and the other hand reaching up to rest on the viewer's cheek at the top edge of the frame. Eyes direct, lips parted, flushed, not acting. The frame runs from her face to mid-thigh. Colour key: satin gold, midnight blue.",
  u"Medium close, bright morning in the bed. She sits against the pillows in the lace set with the satin sheet across her lap, a coffee cup in both hands, hair loose, face bare, one strap fallen, laughing quietly at the viewer. Colour key: sunrise gold and soft white."],
 'doc': [
  u"Medium, eye level. Leaning on the examination couch, she unbuttons the last button and lets her medic shirt and white coat slide together off both shoulders to her elbows, **the white lace set with lime ribbon fully shown**, stethoscope still round her neck, both tattoo sleeves bare from shoulder to wrist. A teasing, confident smile. Colour key: green-shaded lamp, warm gold.",
  u"Three-quarter length, **straight from behind**. In the lace set only, she walks through the curtain toward the bathroom with both arms raised to unpin her curls, **both tattoo sleeves visible from behind, her back bare of tattoos**; she looks back over her shoulder with one eyebrow raised. Colour key: lamp amber on her back and hips, lime glow ahead.",
  u"Close, framed **from the collarbones up**, fern leaves blurred in the foreground. She stands under the brass shower head facing the viewer, both tattooed arms lifted to wring the water out of her loosened curls, water sheeting over her shoulders and arms, eyes half closed, a slow smile. Steam fills the lower edge of the frame. Colour key: pale green tile, warm bulb, lime accent.",
  u"Close, eye level, from beside her on the bed. In the lace set, curls damp and down, she half-sits against the headboard with one tattooed arm reaching sideways to the lamp chain and the other hand holding the viewer's hand against her collarbone. Face turned to the viewer: half-closed eyes, parted lips, warm flushed skin. Clinic hours are over. Colour key: lamp amber, soft lime in the shadows.",
  u"Medium, bright morning sun among the plants. She sits on the edge of the bed in the lace set with a white blanket round her hips, a clipboard on her knee and a pen in her hand, having just written one word on it (suggested, not readable), smiling at the viewer over her shoulder, soft and rested. Both sleeves in the sun. Colour key: sunlit white and leaf green."],
}
NAMES = [u'BACK FROM THE MISSION', u'LOOSENING', u'UNDRESSING', u'FROM BEHIND', u'THE SHOWER', u'JUST BEFORE', u'MORNING']
KO7 = [(u'특임복', u'임무 복장', u'TAKE 1 · 2 · 3 HARD 이상 시 무료'), (u'가볍게 탈의', u'장비를 벗은 얇은 상의', u'구매'), (u'속옷 + 벗는 동작', u'속옷, 겉옷을 벗는 중', u'구매'), (u'뒷모습', u'속옷, 뒤에서', u'구매'), (u'샤워', u'수증기 · 유리 · 물', u'구매'), (u'직전(최고조)', u'속옷, 젖은 머리', u'구매'), (u'아침', u'속옷 + 이불', u'구매')]


def md(a):
    d = V4.D[a]; v = CS.A[a]
    t = u'# SILENT SIX — 로맨틱 "그날 밤" 리워드 컷 v5 · %s\n\n## 사용법 (사람이 읽는 부분)\n\n1. ChatGPT **새 대화**에 이 zip을 올리고 **"압축을 풀고 지시.md 를 끝까지 읽은 뒤, CUT 1부터 한 장씩 진행해 줘."**\n2. 한 번에 한 장. 다음 장은 "next". **이 요원은 7장이다.**\n3. 파일명 `n_%s_1` ~ `n_%s_7` 그대로 Claude에게 넘긴다.\n4. 수위를 낮춰서 나오면: **"What this is 항목과 level 폴더를 다시 보고, 지시된 복장 그대로 가리는 포즈 없이 다시 그려 줘."**\n5. 문신 · 표식이 틀리면: **"Identity check 항목대로 시트와 맞춰 다시 그려 줘."**\n\n| 컷 | 장면 | 복장 | 게임에서 |\n|---|---|---|---|\n' % (d['ko'], a, a)
    for k, (s, w, g) in enumerate(KO7, 1): t += u'| %d | %s | %s | %s |\n' % (k, s, w, g)
    t += u'\n`level/` 폴더는 이 요원의 기존 확정 컷이다. 수위와 온도의 기준으로만 쓴다.\n\n---\n\n' + COMMON
    t += u'## THIS AGENT\n\n- **%s** (`agents/sheet_%s.jpg`, signature colour %s). %s.\n- **Tattoos, marks and personal items:** %s\n- Lingerie: %s\n\n**Who she is, and what this night is.** %s\n\n**The place.** %s\n\n**Where she washes (cut 5).** %s.\n\n**Her visual language.** %s\n\n## THE SEVEN CUTS\n\n' % (v[0], a, v[2], v[5][0].upper() + v[5][1:], MARKS[a], d['lin'], d['who'], d['place'], BATH[a][0].upper() + BATH[a][1:], V4.VIS[a])
    for k, c in enumerate(d['cuts'][:2] + C[a]):
        t += u'### CUT %d — `n_%s_%d` — %s\n\n%s\n\n' % (k + 1, a, k + 1, NAMES[k], c)
    return t


def main(out, lvdir=None):
    os.makedirs(out, exist_ok=True); pk = os.path.join(HERE, 'packs'); os.makedirs(pk, exist_ok=True)
    for a in ['raven', 'viper', 'glitch', 'brick', 'mirage', 'doc']:
        zn = 'SILENT6_Reward_Romantic_Night_V5_%s' % a.upper(); text = md(a)
        io.open(os.path.join(pk, u'RomanticNight_V5_%s_지시.md' % a), 'w', encoding='utf8').write(text)
        z = zipfile.ZipFile(os.path.join(out, zn + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        z.writestr(zn + u'/지시.md', text); z.write(os.path.join(CSO, 'AGENTS.md'), zn + '/AGENTS.md'); z.write(os.path.join(CSO, 'sheet_%s.jpg' % a), '%s/agents/sheet_%s.jpg' % (zn, a))
        k = 0
        if lvdir:
            for m in (4, 5, 6):
                f = os.path.join(lvdir, a.capitalize(), 'n_%s_%d.png' % (a, m))
                if os.path.exists(f):
                    k += 1; tmp = io.BytesIO(); Image.open(f).convert('RGB').resize((768, 1152), Image.LANCZOS).save(tmp, 'JPEG', quality=86); z.writestr('%s/level/earlier_cut_%d.jpg' % (zn, m), tmp.getvalue())
        z.close(); print(zn, os.path.getsize(os.path.join(out, zn + '.zip')) // 1024, 'KB', 'level', k, 'cuts', text.count('### CUT '))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'out', sys.argv[2] if len(sys.argv) > 2 else None)
