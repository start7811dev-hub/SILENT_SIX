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
  cuts=[u"Full-length vertical shot from the far side of the room: she stands in the doorway with the door swinging shut behind her, black tactical jacket soaked, hair dripping, red scarf dark with water, one hand still on the frame. Small in the tall dark room; her eyes have found the viewer and the hard line of her mouth is easing. Colour key: cold blue rain light, one amber lamp.",
        u"Waist-up from the side, in profile: she sits on the edge of the desk with the jacket dropped behind her, black tank top, bare wet shoulders, scarf still on. One grazed forearm is held out to the viewer, whose hand with a roll of gauze enters from the frame edge; she looks away at the window, jaw tight, letting it happen. Colour key: amber lamp on one side of her face, blue window on the other.",
        u"Back three-quarter view, knee-up: she stands at the rain window in the black silk slip with a grey shirt hanging open off one shoulder, a glass of whisky held low at her side, head turned to look back at the viewer over her shoulder as she says something she has never said aloud. Her reflection in the wet glass shows the front of her face. Colour key: whisky gold and deep shadow.",
        u"Very close, steep high angle (the viewer standing over her): she sits on the edge of the bed and reaches one hand up toward the lens, palm up, strongly foreshortened. The shirt is gone and one strap of the slip has fallen, **the black lace with crimson ties showing under it**; face tilted up, lips parted, eyes locked on the viewer, certain. Colour key: lamp amber on skin, crimson accent.",
        u"Close, low angle from the pillow: **lingerie only**. She kneels upright on the grey linen facing the viewer, back straight, both hands at her throat drawing the red scarf loose for the first time, the silk sliding down over her collarbone and one hip. Chin slightly lowered, eyes heavy-lidded and fixed on the viewer, lips parted, flushed; the frame runs from her knees to the top of her head. Colour key: warm lamp from below, rain-blue behind, the red of the scarf.",
        u"Wide shot in grey morning light, rain stopped: she sits sideways in the deep window recess with one knee drawn up, the grey shirt half on and open over bare legs, a cup in her hands, the harbour pale beyond the glass, the scarf folded on the sill beside her. Her head is turned to the viewer with a small, real, sleepy smile, the first of the set. Colour key: pearl grey dawn, a thread of red."]),
 'viper': dict(ko=u'VIPER · 설산 산장 — 한 발 남긴 밤', det=u"Short silver-white hair swept to one side, as in her sheet; two dog tags on one chain in every cut.",
  place=u"A timber mountain lodge in deep snow at night: a stone fireplace, a fur rug, a leather armchair, a decanter, her rifle case propped by the door, a window of blue snow and pines, and an outdoor hot-spring bath steaming on the deck.",
  who=u"Lazy, teasing, the one who can lie still for hours. She always comes back with one round left and never says why. She teases to keep people at a distance; tonight the teasing slows down and stops.",
  lin=u"deep violet lace with thin silver hardware and sheer mesh; over it, a dark plum silk robe.",
  cuts=[u"Wide, low shot from the armchair by the fire: she leans one shoulder on the door frame with the rifle case hanging from her hand, kicking snow off one boot against the other, white smock unzipped, snow in her silver hair, cheeks red from the cold. The lazy smirk arrives a second late as she sees the viewer. Colour key: blue snow behind her, fire orange in front.",
        u"Floor-level close-up: smock off, a thin grey thermal top, she is sprawled on her stomach on the fur rug in front of the fire, chin on her folded forearms, a towel draped over her wet head like a hood, dog tags pooled on the fur. One eye looks sideways at the viewer with a tired half-smile. Colour key: fire gold, plum shadow.",
        u"High angle, looking down from standing height: she lies sideways across the leather armchair in the plum silk robe, legs hooked over one arm of the chair, head tipped back over the other, a glass resting on her stomach. With her free hand she holds a single rifle round up toward the lens between two fingers, the one she always keeps; no smirk at all. Colour key: brass glint, fire amber.",
        u"Very close, floor level, the lens almost on the rug: the robe open and slipping off one shoulder over **the violet lace**, she lies stretched out on her side along the bottom of the frame, propped on one elbow, and with the other hand tugs the viewer toward her by a fistful of blanket in the foreground. Lips parted, eyes steady, certain. Colour key: violet and firelight on skin.",
        u"Straight down from above, her head toward the bottom of the frame so her face is nearest the lens: **lingerie only**, dog tags on her collarbone. She lies on her back on the fur with both arms stretched up past her head toward the viewer, fingers open, back gently arched, looking up into the lens with half-closed eyes and parted lips, flushed. Firelight rakes across from one side along ribs, waist and hip. Colour key: deep fire orange, plum shadow.",
        u"Medium shot from the foot of the rug in blue dawn, fire down to embers: she is asleep on her side under a heavy knitted blanket pushed down to her waist, bare shoulder and back to the snow light, one hand curled by her face, the single round standing upright on the floorboards beside the dog tags in the foreground. Completely still, completely unguarded. Colour key: dawn blue with one ember of orange."]),
 'glitch': dict(ko=u'GLITCH · 화면 속과 화면 밖 — 로그아웃', det=u"Black hair in a messy top bun with teal tips and one shaved side, on the same side as in her sheet in every cut; round glasses; headphones.",
  place=u"Her apartment-workshop at night in a neon city: a desk of six monitors, a small drone on a shelf, hanging plants, energy-drink cans, an unmade bed under a window of magenta and teal signs, then sunrise.",
  who=u"Twenty-seven, quick, funny, scared of most things. She erased her own name years ago and lives behind screens because it is safer there. Tonight she closes the laptop and lets someone see her without one.",
  lin=u"pale teal lace with thin straps, small white bows and sheer mesh; over it, an oversized black hoodie with teal cuffs.",
  cuts=[u"Medium shot from the doorway, slightly high: she spins round in her desk chair, feet off the floor, black tech jacket, headphones on, a cut on her cheek, both arms thrown up in a wave at the viewer with a huge relieved grin and wet eyes, six monitors glowing behind her. Colour key: teal screen glow, magenta window.",
        u"Extreme close-up of her face, the lens a hand's width away: jacket off, black tank top strap and bare shoulder at the frame edge, glasses pushed up into her hair. She scrunches one eye shut and holds very still while the viewer's fingers press a small plaster to her cheek; the other eye peeks at the viewer. Colour key: soft teal, warm desk lamp.",
        u"High, wide shot from the ceiling corner: she is a small figure in the middle of the big unmade bed, knees pulled up inside the oversized hoodie, bare legs, a mug in both hands, glasses on, face tipped up toward the viewer, cheeks pink, saying the name she deleted. Neon stripes from the window fall across the sheets. Colour key: magenta sign light, teal shadow.",
        u"Very close, low angle from the mattress with the laptop lid large in the foreground: she kneels up over it and pushes it shut with both hands, the hoodie unzipped and falling off both shoulders over **the pale teal lace with white bows**. Seen from below, she looks down at the viewer over her glasses, biting her lip, flushed, the last screen light dying on her skin. Colour key: teal fading to warm lamp.",
        u"Very close, pillow level, face to face, as if the viewer is lying beside her: **lingerie only**, all the screens off for the first time, glasses folded on the sheet. She lies curled on her side hugging a pillow to her chest with one arm, the other hand reaching across the sheet toward the lens, bun undone and teal-tipped hair across her cheek, eyes half closed, lips parted, flushed; shoulder, waist and the curve of her hip rise behind her in soft focus. Colour key: magenta and teal neon on skin.",
        u"Wide shot at sunrise, gold light through the hanging plants: she sits sideways in the desk chair with her bare legs tucked up, the big hoodie slipped off one shoulder, a steaming mug in one hand, hair messy, looking back over her shoulder at the viewer with a small shy smile; every monitor behind her is dark. Colour key: sunrise gold with a teal accent."]),
 'brick': dict(ko=u'BRICK · 문 닫은 체육관 — 노크', det=u"Very short bleached-blonde buzz cut, orange goggles pushed up, dog tags, deep brown skin, a powerful athletic build in every cut.",
  place=u"A boxing gym after closing: a ring under one hanging lamp, heavy bags, a wooden bench, steel lockers, steam from the shower room, a rooftop with the city at dawn.",
  who=u"The loudest laugh on the team and the one who stands in front of every door. She carries four names she could not get through a door in time. She does not ask for anything; tonight she knocks.",
  lin=u"black lace with orange satin edging, a clean sporty cut with thin straps and sheer mesh; over it, a charcoal zip hoodie with orange stripes.",
  cuts=[u"Low-angle full figure from inside the dark gym: she fills the open doorway, knuckles still raised from knocking, scuffed breaching vest, goggles up, rain on her shoulders, the big grin not quite covering how tired she is. Colour key: street-lamp orange behind her, cold gym blue inside.",
        u"Close, from slightly below, as if the viewer kneels in front of her: she sits on the ring apron with the vest off, black sports top, shoulders shining with sweat, both fists held out toward the lens while the viewer's hands unwind the tape from her bruised knuckles. Her face is above the fists, eyes down, quiet for once. Colour key: one warm hanging lamp, deep shadow.",
        u"Low-angle three-quarter shot from the gym floor outside the ring: she stands inside leaning forward on the ropes, forearms draped over the top rope, the charcoal hoodie open over the sports top, a water bottle hanging from two fingers. She looks down at the viewer and tells the one thing she never tells, eyes bright, jaw working. Colour key: amber lamp, steel grey, ropes as diagonals.",
        u"Close, eye level, face to face: she sits on the corner stool like a fighter between rounds, leaning far forward with one elbow on her knee, the hoodie hanging off her elbows over **the black lace with orange edging**. Her other arm is stretched toward the lens, a fist opening into an open hand for the viewer to take; a slow, sure grin, cheeks flushed, steam drifting from the shower room behind. Colour key: orange rim on dark skin, warm steam.",
        u"Close, low angle from the canvas: **lingerie only**, dog tags on her chest, goggles hung on the corner post. She sits on the canvas leaning back against the corner pad with both arms spread wide along the ropes, one leg stretched toward the lens and the other bent, head tipped back against the pad, looking down her cheekbones at the viewer with half-closed eyes and a lazy flushed smile. The single lamp picks out shoulders, stomach and thighs. Colour key: lamp gold on skin, black beyond the ropes.",
        u"Wide shot on the gym roof at dawn, the city turning pink: she sits on the parapet edge wrapped in the hoodie and a plaid blanket with her bare legs swinging, head tipped onto her fist, eyes soft and sleepy, smiling at the viewer without the armour of the grin. Colour key: rose and orange sunrise."]),
 'mirage': dict(ko=u'MIRAGE · 호텔 스위트 — 가면을 벗는 밤', det=u"Long wavy black hair, gold hoop earrings, a small beauty mark, warm tan skin in every cut.",
  place=u"A top-floor hotel suite at night: a marble dressing table with a lit mirror, a wide bed with champagne satin, a balcony over the city, lilies in a vase, then sunrise.",
  who=u"She is always someone else: a name, a walk, a perfume for every job. Alone, she wears no make-up, and almost no one has seen that face. Tonight she takes the role off piece by piece in front of someone, and the last thing left is her.",
  lin=u"black lace with fine gold details, thin straps, sheer mesh, stockings with lace tops; over it, a dark wine silk robe.",
  cuts=[u"Waist-up, eye level, from just inside the suite: she has closed the door and leans back on it with her head against the wood, an evening gown from the job, heels dangling from one hand, the perfect party smile still on her face and exhaustion behind it in the eyes. Colour key: corridor gold, cool blue city window.",
        u"Over her bare shoulder into the lit dressing-table mirror: gown unzipped down the back, one earring off in her hand, she wipes away half her lipstick with a cotton pad. Her face appears only in the reflection, meeting the viewer's eyes in the glass; the practised smile is gone and a small tired real one is in its place. Colour key: mirror bulb warmth, wine shadow.",
        u"Eye-level medium shot: she reclines along the chaise on her side in the wine silk robe, propped on one elbow in a long S-curve, a champagne coupe in her free hand, hair down, face bare of make-up for the first time. She tells the viewer her real name, eyes direct, a faint flush; the city lights lie behind her in the balcony glass. Colour key: city bokeh, warm room lamp.",
        u"Low angle from the edge of the bed, three-quarter length: she stands over the viewer, weight on one hip, the robe open and sliding off both shoulders over **the black lace with gold details and stockings**, one hand reaching down toward the lens to take the viewer's collar. Chin lifted, lips parted, eyes locked, not acting; the dressing-table mirror behind her shows her bare back. Colour key: gold lamp on skin, deep wine.",
        u"Very close, from above and in front, on the champagne satin: **lingerie only**, hoops catching the light. She lies on her stomach propped on her elbows facing the viewer, chin on her laced fingers, ankles crossed in the air behind her, laughing softly with flushed cheeks and half-closed eyes; the frame takes in her shoulders, the curve of her back and her hips. Colour key: satin gold, midnight blue.",
        u"Wide profile shot on the balcony at sunrise: she leans on the rail on her forearms in a white shirt slipping off one shoulder, bare legs, one foot hooked behind the other ankle, a cup of coffee in both hands, hair loose and face bare. Her head is turned to the viewer with a quiet, unguarded smile as the city turns gold behind her. Colour key: sunrise gold and soft white."]),
 'doc': dict(ko=u'DOC · 진료 시간 종료 — 퇴원', det=u"Dark curls tied up high with loose strands, hoop earrings, and her tattoo sleeves exactly as drawn in her sheet, on the same arms and with the same pattern in every cut.",
  place=u"Her small night clinic after closing: an examination room with a green-shaded lamp, steel trays, a medicine cabinet, forty potted plants along the window, her bedroom behind a curtain with white linen, then morning sun.",
  who=u"Thirty-six, the eldest. She looks after everyone, remembers every chart, and lets no one look after her. Every plant tattooed on her skin is a patient she could not save. Tonight she is off duty, and in the morning she writes one word on a chart.",
  lin=u"white lace with thin lime-green ribbon and sheer mesh; over it, a lime silk slip.",
  cuts=[u"Tight close-up, face and one raised hand: she has just come in, tactical medic vest at the frame edge, hair coming loose, peeling a bloodied nitrile glove off with her teeth, eyes going straight to the viewer to check them over before she lets herself breathe. Leaves blurred in the foreground. Colour key: green lamp, cold night window.",
        u"High angle, over the viewer's bandaged hand in the foreground: she sits low on the rolling stool, vest off, white tank top, tattooed arms bare, winding the bandage with quick sure fingers. Her face is tipped up toward the lens with a teasing, tired half-smile. Colour key: warm lamp pool, green shadow of leaves.",
        u"Close, shoulder level, from the side, as if the viewer sits beside her: she sits on the examination couch with her feet off the floor, an open white coat over the lime silk slip, stethoscope round her neck, a cup of tea held in her lap, body turned toward the viewer. She has stopped joking; she says what she never tells her patients, a flush across her cheekbones. Colour key: lamp gold, lime accent.",
        u"Low angle, three-quarter length, from inside the bedroom: she stands in the doorway holding the curtain aside with one raised tattooed arm, the white coat falling from her shoulders to the floor, one strap of the slip down over **the white lace with lime ribbon**. Her other hand is held out and down to the viewer, large in the foreground; a slow certain smile, eyes warm. Colour key: lime silk glow, warm dark.",
        u"Close, eye level, from beside her on the bed: **lingerie only**, stethoscope gone, curls coming down. She half-sits against the headboard among the pillows, one leg folded and one stretched out, one tattooed arm reaching sideways to the lamp chain to turn the light down, face turned to the viewer with half-closed eyes, parted lips and warm flushed skin. Clinic hours are over. Colour key: lamp amber, soft lime in the shadows.",
        u"Medium-wide shot through the plants in bright morning sun: she sits at her desk in a loose white shirt slipping off one shoulder, bare legs crossed, chin on her hand, pen in the other, a clipboard in front of her with one handwritten word suggested on it (not readable), smiling at the viewer, soft and rested. Colour key: sunlit white and leaf green."]),
}
VIS = {'raven': 'Upright and vertical. She stands, kneels or sits tall; tall window, door frame and rain streaks as vertical lines; profile and back views; cold blue against one warm lamp.', 'viper': 'Horizontal and low. She sprawls, lounges and lies; the camera sits at floor level or looks straight down; long diagonals of limbs across a wide-feeling frame; firelight from the side.', 'glitch': "Small in a big frame, or extremely close. High angles looking down at her curled up, or the lens a hand's width from her face; screens, cables and plants as frames inside the frame.", 'brick': 'Big and low. She fills the frame, seen from below; ring ropes, lockers and door frames as strong diagonals; one hard lamp from above.', 'mirage': 'Curves and reflections. S-curve poses, mirrors and glass giving a second view of her, over-the-shoulder looks; gold light on dark.', 'doc': 'Hands and faces. Tight framing on what her hands are doing and her eyes above them, plant leaves blurred in the foreground, one pool of lamp light.'}
NAMES = [u'RETURN', u'UNWINDING', u'CLOSER', u'INVITATION', u'THE NIGHT', u'MORNING']
LVL = {'brick': [('brick', 4), ('brick', 5), ('brick', 6)]}


def md(a):
    d = D[a]; v = CS.A[a]
    t = u'# SILENT SIX — 로맨틱 "그날 밤" 리워드 컷 v4 · %s\n\n## 사용법 (사람이 읽는 부분)\n\n1. ChatGPT **새 대화**에 이 zip을 올리고 **"압축을 풀고 지시.md 를 끝까지 읽은 뒤, CUT 1부터 한 장씩 진행해 줘."**\n2. 한 번에 한 장. 다음 장은 "next". **이 요원은 6장이다.**\n3. 파일명 `n_%s_1` ~ `n_%s_6` 그대로 Claude에게 넘긴다.\n4. CUT 4 · 5에서 수건 · 담요나 가리는 포즈가 나오면: **"What this is 항목과 level 폴더를 다시 보고, 속옷 차림 그대로 가리는 포즈 없이 다시 그려 줘."**\n\n| 컷 | 장면 | 복장 | 게임에서 |\n|---|---|---|---|\n| 1 | 귀환 | 임무 복장 | TAKE 1 · 2 · 3 HARD 이상 시 무료 |\n| 2 | 풀림 | 장비를 벗은 얇은 상의 | 30P |\n| 3 | 고백 | 평상복(슬립 · 가운 · 후디) | 30P |\n| 4 | 초대 | 겉옷이 열리고 속옷이 보임 | 30P |\n| 5 | 그 밤 | 속옷 차림 | 30P |\n| 6 | 아침 | 셔츠나 시트 | 30P |\n\n`level/` 폴더는 이 요원의 기존 확정 컷이다. 수위와 온도의 기준으로만 쓴다.\n\n---\n\n' % (d['ko'], a, a)
    t += COMMON + u'## THIS AGENT\n\n- **%s** (`agents/sheet_%s.jpg`, signature colour %s). %s.\n- Personal details: %s\n- Lingerie: %s\n\n**Who she is, and what this night is.** %s\n\n**The place.** %s\n\n**Her visual language (this agent only).** %s Every agent in this series has a different one; the camera and pose given in each cut below are part of the brief, so follow them and do not fall back on a standard pin-up framing.\n\n## THE SIX CUTS\n\n' % (v[0], a, v[2], v[5][0].upper() + v[5][1:], d['det'], d['lin'], d['who'], d['place'], VIS[a])
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
