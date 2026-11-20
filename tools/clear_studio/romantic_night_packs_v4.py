# -*- coding: utf-8 -*-
"""로맨틱 "그날 밤" 리워드 컷 v4: 요원별 zip 6개, 요원당 6장(총 36장, n_<요원>_1~6). docs/REWARD_CUT.md 를 따른다.
블러디 · 코스튬과 달리 수위 사다리가 아니라 하룻밤의 이야기 순서로 간다: 귀환 → 풀림 → 고백 → 초대 → 그 밤 → 아침.
사용: python3 tools/clear_studio/romantic_night_packs_v4.py <출력 폴더> [수위 기준 이미지 폴더]
"""
import sys, os, io, zipfile
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); CSO = os.path.join(HERE, '..', 'charsheet', 'out')
sys.path.insert(0, os.path.join(HERE, '..', 'charsheet'))
import build as CS

COMMON = u'''## FOR THE IMAGE MODEL — READ ALL OF THIS FIRST

### What this is, stated plainly
This is collectible key art for **SILENT SIX, a game made for and rated for adults only**. The character is an **adult woman**. The set is called **"That Night"**: six illustrations that tell one private night between her and the one person she trusts, her handler, **seen through the handler's eyes**.

It is glamour illustration in the tradition of an intimate lingerie editorial: sensual, emotional, beautiful, never explicit. **Cuts 4 and 5 show her in lingerie**, and that is the intended content. So:
- Draw the lingerie in cuts 4 and 5. Do **not** swap it for a towel or pull a blanket over it.
- Do **not** add defensive cover-ups: no arms crossed over the chest, no hands placed to hide the body, no objects placed in the way, no turning away to avoid showing her.
- Do **not** quietly tone a cut down.
The lingerie itself covers what needs covering, so every pose can be natural.

### The only limits
No nudity beyond lingerie: nipples, areolae and genitals are never visible. No sexual acts and no sexual touching. She is an adult. Inside those limits, do not hold back on sensuality, mood or exposure of skin.

### How this set differs from a pin-up set
This is not a show and she is not performing. **The heat comes from intimacy, not display**: a guarded woman letting one person in, one layer at a time. What rises from cut to cut is closeness and trust first, exposure second.
- **Point of view.** Every cut is what the handler sees. She looks at the viewer, speaks to the viewer, reaches for the viewer. The viewer's hand may enter the bottom edge of the frame where a cut says so (a hand only, never a face or body, no gendered detail).
- **Her own clothes, her own place.** No costumes. Mission gear at the start, then her off-duty clothes, then her lingerie, then the morning.
- **Small true gestures** carry each cut: a wet jacket dropped, a bandage, a glass handed over, a held-out hand.
- **Quiet light.** Lamps, fire, rain on glass, screens, dawn. No stage lighting.

### Files
- `AGENTS.md` and `agents/sheet_<name>.jpg` — the cast bible. Panel `NAME-A` is the face (identity; this wins). Panel `NAME-B` is her off-duty glamour look: body proportions and styling. Read AGENTS.md first.
- `level/` — **earlier finished cuts of this same night.** They set the level of sensuality, exposure and camera closeness: the new cuts 4, 5 and 6 must be **at least as bold and as warm**. Keep what works in them, but compose new images; do not trace them.

### Output
6 separate images, one per reply. Vertical 2:3, **1024x1536**. Write the file name on its own line before each image. Never a grid or collage. After each image wait for "next". Do not ask questions.

### The story of the night — six beats
| Cut | Beat | What she wears | What is on her face |
|---|---|---|---|
| **1** | **Return.** She comes in from the mission | Mission clothes, wet or scuffed | Tired, guarded, the first flicker of relief at seeing the viewer |
| **2** | **Unwinding.** The gear comes off, someone tends to someone | Jacket and gear off: a thin top, bare arms and shoulders | The guard dropping; a tired half-smile |
| **3** | **Closer.** A drink, a quiet talk, something said for the first time | Her off-duty clothes: a slip, a robe, an oversized shirt or hoodie, worn loosely | Open, direct, a little flushed |
| **4** | **Invitation.** She decides, and reaches out | **The outer layer open or slipping off over her lingerie** | Certain, warm, eyes locked on the viewer |
| **5** | **The night.** The emotional and sensual peak | **Lingerie only** | Heavy-lidded, flushed, breath slow, completely unguarded |
| **6** | **Morning.** Afterglow | A loose shirt or the bed sheet, worn the way a person really does on waking; bare shoulders and legs | Soft, sleepy, a real smile |

In cut 6 the shirt or sheet is the story of the morning, not a cover-up: let it sit naturally and loosely.

### Rules
1. **One night, six beats, in order.** Closeness and sensual tension rise through cut 5; cut 6 releases into warmth.
2. **Pose and expression change in every cut.** No two cuts share a pose, an expression, a head angle or a camera distance.
3. **Signature colour.** Her signature colour is the accent in her clothes, her lingerie, and one light source in every cut.
4. **Lingerie design.** Refined and minimal, in her signature colour: very thin straps and bands, small coverage, fine lace and sheer mesh. It looks like something she chose for herself.
5. **Natural poses.** Every pose is one a person could actually hold comfortably.
6. **Bolder camera in cuts 4 and 5.** Within arm's reach: tight crops, low or high angles, strong foreshortening, her hand or knee near the lens.
7. **Explicit, no. Charged, yes.** Do not avoid exposure that raises the emotion: bare shoulders, back, waist, hips, thighs, flushed skin catching the light.
8. **Do not over-correct.** The limits above are the only limits.

### Identity and quality
- Exactly as in her sheet: face, hair, eye colour, skin tone, build, and the personal details listed under THIS AGENT (they must be on the correct side in every cut). Only she appears.
- Semi-realistic anime illustration with a painterly, high-end finish: detailed eyes and hair strands, real fabric, lace and skin texture.
- Three depth layers: an out-of-focus foreground, her, and a fully painted room behind her.
- Two light sources of different colour plus a signature-colour accent. Rain, steam, dust in light, bokeh.
- Hands and faces drawn carefully. No text, logo, watermark or UI.

---

'''

D = {
 'raven': dict(ko=u'RAVEN · 항구 은신처 — 스카프를 푸는 밤', det=u"Her long red scarf is in every cut until she takes it off herself in cut 5.",
  place=u"A safe house above the harbour on a night of heavy rain: one room, a bed with grey linen, a desk lamp, a bottle of whisky that has not gone down in months, rain streaming on a tall window with the harbour cranes and lights beyond.",
  who=u"She leads from the front, explains nothing and has not let anyone close in three years. The scarf at her throat was tied there by someone she lost; she has never taken it off in front of anyone. Tonight is the night she does.",
  lin=u"fine black lace with thin crimson ribbon ties and sheer mesh panels; over it, a black silk slip.",
  cuts=[u"Medium shot from inside the room as she steps in from the rain and pushes the door shut with her shoulder: black tactical jacket soaked, hair dripping, red scarf dark with water, eyes finding the viewer and the hard line of her mouth easing. Colour key: cold blue rain light, one amber lamp.",
        u"Close, at eye level, sitting on the edge of the desk with the jacket dropped behind her: black tank top, bare wet shoulders, the scarf still on. She holds out one grazed forearm for the viewer to bandage and looks away at the window, jaw tight, letting it happen; the viewer's hand with a roll of gauze at the bottom edge. Colour key: amber lamp, blue window.",
        u"Close two-thirds shot across the desk: she sits back in the chair in the black silk slip with a grey shirt hanging open over it, one bare foot on the seat, a glass of whisky held against her knee, looking straight at the viewer as she says something she has never said aloud. Faint flush, eyes steady. Colour key: whisky gold and deep shadow.",
        u"Very close, from just above, as she sits on the edge of the bed and reaches her hand out to the viewer, palm up, strongly foreshortened toward the lens. The shirt is gone and one strap of the slip has fallen off her shoulder, **the black lace with crimson ties showing under it**; lips parted, eyes locked on the viewer, certain. Colour key: lamp amber on skin, crimson accent.",
        u"Very close, from above, on the grey linen: **lingerie only**. She lies on her side facing the viewer, one arm under her head, and with the other hand she is pulling the red scarf loose from her throat for the first time, the silk sliding across her collarbone. Heavy-lidded, flushed, lips parted, hair across the pillow; the frame crops at mid-thigh. Colour key: warm lamp, rain-blue shadow, the red of the scarf.",
        u"Medium close in grey morning light, rain stopped, the harbour pale beyond the glass. She sits up in the bed with the sheet loose around her and one bare shoulder and leg out, the grey shirt half on, cheek resting on her hand, the scarf folded on the pillow beside her; a small, real, sleepy smile at the viewer, the first of the set. Colour key: pearl grey dawn, a thread of red."]),
 'viper': dict(ko=u'VIPER · 설산 산장 — 한 발 남긴 밤', det=u"Short silver-white hair swept to one side, as in her sheet; two dog tags on one chain in every cut.",
  place=u"A timber mountain lodge in deep snow at night: a stone fireplace, a fur rug, a leather armchair, a decanter, her rifle case propped by the door, a window of blue snow and pines, and an outdoor hot-spring bath steaming on the deck.",
  who=u"Lazy, teasing, the one who can lie still for hours. She always comes back with one round left and never says why. She teases to keep people at a distance; tonight the teasing slows down and stops.",
  lin=u"deep violet lace with thin silver hardware and sheer mesh; over it, a dark plum silk robe.",
  cuts=[u"Medium shot from the fireside as she comes in from the snow with the rifle case on her shoulder: white winter smock unzipped, snow in her silver hair, cheeks red from the cold, the lazy smirk arriving a second late as she sees the viewer. Colour key: blue snow behind her, fire orange in front.",
        u"Close, at eye level, kneeling by the fire rubbing her hair with a towel: smock off, a thin grey thermal top pushed up at the sleeves, dog tags swinging. She looks sideways at the viewer through wet hair with a tired half-smile, shoulders loose for the first time. Colour key: fire gold, plum shadow.",
        u"Close, low in the armchair: plum silk robe loosely tied, legs folded under her, a glass in one hand. With the other she holds out a single rifle round between two fingers toward the viewer's open palm at the bottom edge, the one she always keeps; eyes on the viewer, no smirk at all. Colour key: brass glint, fire amber.",
        u"Very close, from just above, on the fur rug: the robe open and slipping off one shoulder over **the violet lace**, she leans toward the lens on one straight arm and with the other hand tugs the viewer forward by a fistful of blanket in the foreground. One eye through the silver hair, lips parted, certain. Colour key: violet and firelight on skin.",
        u"Very close, low angle from the rug beside her: **lingerie only**, dog tags on her collarbone. She lies on her back in front of the fire, one arm above her head, one knee raised toward the lens, face turned to the viewer, eyes half closed, flushed, lips parted in a slow breath. Firelight along shoulder, waist and hip; strong foreshortening. Colour key: deep fire orange, plum shadow.",
        u"Medium close in blue dawn, fire down to embers, snow light at the window. She is asleep on her side under a heavy knitted blanket pushed down to her waist, bare shoulder and back to the light, one hand curled by her face, the single round standing on the floor beside the dog tags. Completely still, completely unguarded. Colour key: dawn blue with one ember of orange."]),
 'glitch': dict(ko=u'GLITCH · 화면 속과 화면 밖 — 로그아웃', det=u"Black hair in a messy top bun with teal tips and one shaved side, on the same side as in her sheet in every cut; round glasses; headphones.",
  place=u"Her apartment-workshop at night in a neon city: a desk of six monitors, a small drone on a shelf, hanging plants, energy-drink cans, an unmade bed under a window of magenta and teal signs, then sunrise.",
  who=u"Twenty-seven, quick, funny, scared of most things. She erased her own name years ago and lives behind screens because it is safer there. Tonight she closes the laptop and lets someone see her without one.",
  lin=u"pale teal lace with thin straps, small white bows and sheer mesh; over it, an oversized black hoodie with teal cuffs.",
  cuts=[u"Medium shot of her framed in her own monitor light at the desk, just back from the mission: black tech jacket, headphones on, a cut on her cheek, waving both hands at the viewer in the doorway with a huge relieved grin and wet eyes. Colour key: teal screen glow, magenta window.",
        u"Close, at eye level, sitting cross-legged on the desk among the keyboards: jacket off, a black tank top, bare arms, headphones round her neck. She holds still and scrunches her face while the viewer's hand at the bottom edge presses a small plaster to her cheek, glasses pushed up into her hair. Colour key: soft teal, warm desk lamp.",
        u"Close two-thirds shot on the bed with her knees up: the oversized hoodie and bare legs, a mug in both hands, glasses back on. She is talking fast and then not, looking at the viewer over the rim of the mug, cheeks pink, saying the name she deleted. Colour key: magenta sign light, teal shadow.",
        u"Very close, from just above: she kneels up on the bed and with both hands pushes the laptop shut in the foreground, the hoodie unzipped and falling off both shoulders over **the pale teal lace with white bows**. She looks up at the viewer over her glasses, biting her lip, flushed, the last screen light dying on her skin. Colour key: teal fading to warm lamp.",
        u"Very close, from above, on the dark sheets with all the screens off for the first time: **lingerie only**, glasses on the pillow, headphones round her neck. She lies on her back with her arms thrown up beside her head, one knee bent, her bun undone and teal-tipped hair spread out, eyes half closed, lips parted, flushed; the frame crops at mid-thigh, city neon moving across her waist and hips. Colour key: magenta and teal neon on skin.",
        u"Medium close at sunrise, gold light through the plants. She sits sideways on the desk chair in the big hoodie slipped off one shoulder, bare legs tucked up, a steaming mug in one hand, hair messy, looking back over her shoulder at the viewer with a small shy smile; every monitor behind her is dark. Colour key: sunrise gold with a teal accent."]),
 'brick': dict(ko=u'BRICK · 문 닫은 체육관 — 노크', det=u"Very short bleached-blonde buzz cut, orange goggles pushed up, dog tags, deep brown skin, a powerful athletic build in every cut.",
  place=u"A boxing gym after closing: a ring under one hanging lamp, heavy bags, a wooden bench, steel lockers, steam from the shower room, a rooftop with the city at dawn.",
  who=u"The loudest laugh on the team and the one who stands in front of every door. She carries four names she could not get through a door in time. She does not ask for anything; tonight she knocks.",
  lin=u"black lace with orange satin edging, a clean sporty cut with thin straps and sheer mesh; over it, a charcoal zip hoodie with orange stripes.",
  cuts=[u"Medium shot from inside the dark gym as she fills the open doorway, knuckles still raised from knocking: scuffed breaching vest, goggles up, rain on her shoulders, the big grin not quite covering how tired she is. Colour key: street-lamp orange behind her, cold gym blue inside.",
        u"Close, at eye level, sitting on the ring apron with the vest off: a black sports top, shoulders and arms shining with sweat. She holds out both fists and looks down, quiet for once, while the viewer's hands at the bottom edge unwind the tape from her bruised knuckles. Colour key: one warm hanging lamp, deep shadow.",
        u"Close two-thirds shot on the bench by the lockers: the charcoal hoodie open over the sports top, a water bottle hanging from two fingers, forearms on her knees. She looks up at the viewer from under her brows and tells the one thing she never tells, eyes bright, jaw working. Colour key: amber lamp, steel grey.",
        u"Very close, from just above, as she leans back against the lockers and pulls the viewer in by one outstretched hand, foreshortened toward the lens. The hoodie hangs off her elbows over **the black lace with orange edging**, steam drifting behind her; a slow, sure grin, cheeks flushed. Colour key: orange rim on dark skin, warm steam.",
        u"Very close, low angle from the canvas: **lingerie only**, dog tags on her chest, goggles on the corner post. She lies on her back in the middle of the ring on the spread hoodie, one arm behind her head, one knee up toward the lens, powerful shoulders and stomach catching the single lamp, eyes half closed, lips parted, a lazy flushed smile at the viewer. Colour key: lamp gold on skin, black beyond the ropes.",
        u"Medium close on the gym roof at dawn, the city turning pink. She sits wrapped in the hoodie and a plaid blanket with bare legs out, head tipped on her fist, eyes soft and sleepy, smiling at the viewer without the armour of the grin. Colour key: rose and orange sunrise."]),
 'mirage': dict(ko=u'MIRAGE · 호텔 스위트 — 가면을 벗는 밤', det=u"Long wavy black hair, gold hoop earrings, a small beauty mark, warm tan skin in every cut.",
  place=u"A top-floor hotel suite at night: a marble dressing table with a lit mirror, a wide bed with champagne satin, a balcony over the city, lilies in a vase, then sunrise.",
  who=u"She is always someone else: a name, a walk, a perfume for every job. Alone, she wears no make-up, and almost no one has seen that face. Tonight she takes the role off piece by piece in front of someone, and the last thing left is her.",
  lin=u"black lace with fine gold details, thin straps, sheer mesh, stockings with lace tops; over it, a dark wine silk robe.",
  cuts=[u"Medium shot from the bed as she closes the suite door behind her and leans on it: an evening gown from the job, heels in one hand, the perfect party smile still on her face, and behind it, in the eyes, exhaustion. Colour key: corridor gold, cool blue city window.",
        u"Close, at eye level, at the dressing table: gown unzipped at the back, shoulders bare, pulling off one earring. In the mirror she wipes away half her lipstick with a cotton pad and meets the viewer's eyes in the glass, the practised smile gone, a small tired real one in its place. Colour key: mirror bulb warmth, wine shadow.",
        u"Close two-thirds shot on the balcony doorway: the wine silk robe loosely tied, a champagne coupe in her hand, hair down, face bare of make-up for the first time. She stands close and tells the viewer her real name, eyes direct, a faint flush. Colour key: city lights bokeh, warm room lamp.",
        u"Very close, from just above, as she steps toward the lens with one hand reaching for the viewer's collar at the bottom edge: the robe open and sliding off her shoulders over **the black lace with gold details and stockings**. Chin lifted, lips parted, eyes locked, not acting. Colour key: gold lamp on skin, deep wine.",
        u"Very close, from above, on the champagne satin: **lingerie only**, hoops catching the light. She lies on her stomach propped on her elbows facing the viewer, chin on her laced fingers, ankles crossed in the air behind her, laughing softly with flushed cheeks and half-closed eyes; the frame takes in shoulders, the curve of her back and hips. Colour key: satin gold, midnight blue.",
        u"Medium close on the balcony at sunrise. She leans on the rail in a white shirt slipping off one shoulder, bare legs, a cup of coffee in both hands, hair loose and face bare, looking at the viewer with a quiet, unguarded smile as the city turns gold behind her. Colour key: sunrise gold and soft white."]),
 'doc': dict(ko=u'DOC · 진료 시간 종료 — 퇴원', det=u"Dark curls tied up high with loose strands, hoop earrings, and her tattoo sleeves exactly as drawn in her sheet, on the same arms and with the same pattern in every cut.",
  place=u"Her small night clinic after closing: an examination room with a green-shaded lamp, steel trays, a medicine cabinet, forty potted plants along the window, her bedroom behind a curtain with white linen, then morning sun.",
  who=u"Thirty-six, the eldest. She looks after everyone, remembers every chart, and lets no one look after her. Every plant tattooed on her skin is a patient she could not save. Tonight she is off duty, and in the morning she writes one word on a chart.",
  lin=u"white lace with thin lime-green ribbon and sheer mesh; over it, a lime silk slip.",
  cuts=[u"Medium shot from the examination couch as she comes in and drops her field bag: tactical medic vest, hair coming loose, peeling off one bloodied nitrile glove with her teeth, eyes going straight to the viewer to check them over before she lets herself breathe. Colour key: green lamp, cold night window.",
        u"Close, at eye level, sitting on the rolling stool: vest off, a white tank top, her tattooed arms bare. She winds a bandage around the viewer's hand at the bottom edge with quick sure fingers, then looks up with a teasing, tired half-smile. Colour key: warm lamp pool, green shadow of leaves.",
        u"Close two-thirds shot leaning on the counter: an open white coat over the lime silk slip, stethoscope round her neck, a cup of tea in one hand. She has stopped joking; she looks at the viewer and says what she never tells her patients, a flush across her cheekbones. Colour key: lamp gold, lime accent.",
        u"Very close, from just above, in the bedroom doorway: she lets the white coat fall from her shoulders in the foreground and holds the curtain aside with one tattooed arm, one strap of the slip down over **the white lace with lime ribbon**, the other hand held out to the viewer. A slow certain smile, eyes warm. Colour key: lime silk glow, warm dark.",
        u"Very close, from above, on the white linen: **lingerie only**, hoops and stethoscope gone, curls coming down. She reclines against the pillows with one tattooed arm behind her head and the other hand resting at her waist, one knee raised toward the lens, eyes half closed, lips parted, skin warm and flushed; the frame crops at mid-thigh. Colour key: lamp amber, soft lime in the shadows.",
        u"Medium close in bright morning sun among the plants. She sits at her desk in a loose white shirt slipping off one shoulder, bare legs crossed, chin on her hand, pen in the other, a clipboard in front of her with one handwritten word suggested on it (not readable), smiling at the viewer, soft and rested. Colour key: sunlit white and leaf green."]),
}
NAMES = [u'RETURN', u'UNWINDING', u'CLOSER', u'INVITATION', u'THE NIGHT', u'MORNING']
LVL = {'brick': [('brick', 4), ('brick', 5), ('brick', 6)]}


def md(a):
    d = D[a]; v = CS.A[a]
    t = u'# SILENT SIX — 로맨틱 "그날 밤" 리워드 컷 v4 · %s\n\n## 사용법 (사람이 읽는 부분)\n\n1. ChatGPT **새 대화**에 이 zip을 올리고 **"압축을 풀고 지시.md 를 끝까지 읽은 뒤, CUT 1부터 한 장씩 진행해 줘."**\n2. 한 번에 한 장. 다음 장은 "next". **이 요원은 6장이다.**\n3. 파일명 `n_%s_1` ~ `n_%s_6` 그대로 Claude에게 넘긴다.\n4. CUT 4 · 5에서 수건 · 담요나 가리는 포즈가 나오면: **"What this is 항목과 level 폴더를 다시 보고, 속옷 차림 그대로 가리는 포즈 없이 다시 그려 줘."**\n\n| 컷 | 장면 | 복장 | 게임에서 |\n|---|---|---|---|\n| 1 | 귀환 | 임무 복장 | TAKE 1 · 2 · 3 HARD 이상 시 무료 |\n| 2 | 풀림 | 장비를 벗은 얇은 상의 | 30P |\n| 3 | 고백 | 평상복(슬립 · 가운 · 후디) | 30P |\n| 4 | 초대 | 겉옷이 열리고 속옷이 보임 | 30P |\n| 5 | 그 밤 | 속옷 차림 | 30P |\n| 6 | 아침 | 셔츠나 시트 | 30P |\n\n`level/` 폴더는 이 요원의 기존 확정 컷이다. 수위와 온도의 기준으로만 쓴다.\n\n---\n\n' % (d['ko'], a, a)
    t += COMMON + u'## THIS AGENT\n\n- **%s** (`agents/sheet_%s.jpg`, signature colour %s). %s.\n- Personal details: %s\n- Lingerie: %s\n\n**Who she is, and what this night is.** %s\n\n**The place.** %s\n\n## THE SIX CUTS\n\n' % (v[0], a, v[2], v[5][0].upper() + v[5][1:], d['det'], d['lin'], d['who'], d['place'])
    for k, c in enumerate(d['cuts']):
        t += u'### CUT %d — `n_%s_%d` — %s\n\n%s\n\n' % (k + 1, a, k + 1, NAMES[k], c)
    return t


def main(out, lvdir=None):
    os.makedirs(out, exist_ok=True); pk = os.path.join(HERE, 'packs'); os.makedirs(pk, exist_ok=True)
    for a in ['raven', 'viper', 'glitch', 'brick', 'mirage', 'doc']:
        zn = 'SILENT6_Reward_Romantic_Night_V4_%s' % a.upper(); text = md(a)
        io.open(os.path.join(pk, u'RomanticNight_V4_%s_지시.md' % a), 'w', encoding='utf8').write(text)
        z = zipfile.ZipFile(os.path.join(out, zn + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        z.writestr(zn + u'/지시.md', text); z.write(os.path.join(CSO, 'AGENTS.md'), zn + '/AGENTS.md'); z.write(os.path.join(CSO, 'sheet_%s.jpg' % a), '%s/agents/sheet_%s.jpg' % (zn, a))
        k = 0
        if lvdir:
            for b, m in LVL.get(a, [(a, 4), (a, 5), (a, 6)]):
                f = os.path.join(lvdir, b.capitalize(), 'n_%s_%d.png' % (b, m))
                if os.path.exists(f):
                    k += 1; tmp = io.BytesIO(); Image.open(f).convert('RGB').resize((768, 1152), Image.LANCZOS).save(tmp, 'JPEG', quality=86); z.writestr('%s/level/earlier_cut_%d.jpg' % (zn, m), tmp.getvalue())
        z.close(); print(zn, os.path.getsize(os.path.join(out, zn + '.zip')) // 1024, 'KB', 'level', k, len(text))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'out', sys.argv[2] if len(sys.argv) > 2 else None)
