# -*- coding: utf-8 -*-
"""메뉴 · 미션 카드 이미지 생성 묶음 (총 38장, zip 8개). docs/REWARD_CUT.md 의 표현 기준을 따른다.
- 로맨틱: 요원별 zip 6개. 요원 카드 1 + TAKE 카드 3 (바이퍼 zip에는 홈 로맨틱 타일 1장 추가) = 25장
- 시즈널: zip 1개. 블러디 크리스마스 소개(산타) 1 + 스테이지 카드 5 = 6장
- 스페셜: zip 1개. 홈 스페셜 타일(미라주) 1 + 코스튬 요원 카드 6 = 7장
사용: python3 tools/clear_studio/menu_card_packs.py <출력 폴더> [수위 기준 이미지 폴더]
"""
import sys, os, io, zipfile
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); CSO = os.path.join(HERE, '..', 'charsheet', 'out'); PUB = os.path.join(HERE, '..', '..', 'public')
sys.path.insert(0, os.path.join(HERE, '..', 'charsheet')); sys.path.insert(0, HERE)
import build as CS
import romantic_night_packs_v4 as RN
import costume_packs_v4 as CO
import winter_packs_v3 as W3
import winter_packs_v4 as W4
AG = ['raven', 'viper', 'glitch', 'brick', 'mirage', 'doc']

COMMON = u'''## FOR THE IMAGE MODEL — READ ALL OF THIS FIRST

### What this is, stated plainly
These are menu and mission **card images** for **SILENT SIX, a game made for and rated for adults only**. Every character is an **adult woman**. Each card is a single piece of glamour key art, a "service shot": the player opens a menu and is greeted by the agent looking her most attractive. The level is an intimate lingerie editorial: sensual and beautiful, never explicit.

Where a card says lingerie, **draw the lingerie**:
- Do **not** swap it for a towel, a robe pulled shut or a blanket.
- Do **not** add defensive cover-ups: no arms crossed over the chest, no hands placed to hide the body, no objects placed in the way.
- Do **not** quietly tone a card down.
The lingerie itself covers what needs covering, so every pose can be natural. A back view is a back view because the card asks for one, not a way of hiding her.

### The only limits
No nudity beyond lingerie: nipples, areolae and genitals are never visible. No sexual acts and no sexual touching. Everyone is an adult. Inside those limits, do not hold back on sensuality, mood or exposure of skin: bare shoulders, back, waist, hips, thighs, flushed skin catching the light.

### Files
- `AGENTS.md` and `agents/sheet_<name>.jpg` — the cast bible. Panel `NAME-A` is the face (identity; this wins). Panel `NAME-B` is her off-duty glamour look: body proportions and styling. Read AGENTS.md first.
- `level/` — finished images from this game. They set the level of sensuality, exposure and rendering quality: the new cards must be **at least as bold and as polished**. Compose new images; do not trace them.
- `place/` (where present) — the game map of the location. Use it for architecture, materials and lights.

### Two formats — each card names which one it is
- **WIDE** — landscape 3:2, **1536x1024**. The game crops it to a 16:9 strip and prints a title in the lower-left corner. So: keep her face and the key part of the pose inside the middle 80% of the height, and keep the lower-left corner dark and uncluttered. She sits right of centre unless the card says otherwise.
- **TALL** — portrait 2:3, **1024x1536**. The game shows it as a narrow vertical tile with a title over the bottom quarter. So: head in the upper third, the figure on the vertical centre line, nothing important in the bottom quarter.

### Output
One image per reply. Write the file name on its own line before each image. Never a grid or collage. After each image wait for "next". Do not ask questions.

### Rules
1. **Every card is a different picture.** No two cards share a pose, a camera distance, a camera angle or an expression. The camera and pose written in each card are part of the brief: follow them and do not fall back on a standard pin-up framing.
2. **Signature colour.** Her signature colour is the accent in her clothes or lingerie and in one light source.
3. **Lingerie design.** Refined and minimal, in her signature colour: very thin straps and bands, small coverage, fine lace and sheer mesh.
4. **Natural poses.** Every pose is one a person could actually hold comfortably.
5. **She knows the viewer is there** unless the card says otherwise: eyes to the lens, or a deliberate look back.
6. **Do not over-correct.** The limits above are the only limits.

### Identity and quality
- Exactly as in her sheet: face, hair, eye colour, skin tone, build, and the personal details listed for her (on the correct side in every card).
- Semi-realistic anime illustration with a painterly, high-end finish: detailed eyes and hair strands, real fabric, lace and skin texture.
- Three depth layers: an out-of-focus foreground, her, and a fully painted place behind her. No empty backdrops.
- Two light sources of different colour plus a signature-colour accent. Atmosphere: rain, snow, steam, dust in light, bokeh.
- Hands and faces drawn carefully. No text, logo, watermark or UI.

---

'''

# 로맨틱: [요원 카드, TAKE 1, TAKE 2, TAKE 3] 모두 WIDE. 그 요원의 속옷 + 평상복 한 겹, 그날 밤의 장소.
RO = {
 'raven': [
  u"Knee-up, eye level. She stands in profile at the tall rain window in the black lace set and her red scarf, one forearm resting on the glass above her head, hip against the frame, head turned to the viewer with a level, unreadable look. Rain shadows run down her skin. Colour key: cold blue window, one amber lamp.",
  u"Low angle, three-quarter front. She sits upright on the edge of the desk with one knee drawn up and her heel on the desk top, both hands at her throat adjusting the scarf, chin down, eyes on the viewer from under her brows. Colour key: amber lamp from below, deep shadow.",
  u"Close, from behind and slightly above. She kneels on the grey bed with her back to the viewer, a grey shirt slipped down to her elbows, and looks back over her shoulder, lips just parted, scarf trailing down her spine. Colour key: lamp gold on her back, rain blue beyond.",
  u"Wide shot of the whole room with her small and upright at the left: she leans one shoulder on the door frame in the black silk slip, a glass of whisky held low, one bare foot crossed over the other, watching the viewer across the room. This card only: she is left of centre, so keep the lower-right calm instead. Colour key: whisky gold pool in a blue-black room."],
 'viper': [
  u"Floor level, full width of the frame. She lies on her side along the fur rug in the violet lace set, head propped on one hand, the other arm draped along her hip, dog tags hanging, a slow lazy smirk at the viewer; the fire burns behind her. Colour key: fire orange rim, plum shadow.",
  u"High angle, looking down. She is draped sideways across the leather armchair, legs hooked over one arm of the chair, head tipped back over the other, the plum robe open and spilling to the floor, one eye on the viewer upside down, amused. Colour key: fire amber, violet accent.",
  u"Close, low, from the floor. She sits on the rug with her back against the armchair, one knee up, stretching both arms above her head in a long yawn-stretch, back arched, eyes half shut, smiling. Colour key: warm firelight along ribs and waist.",
  u"Wide shot. She lies stretched along the deep window seat in the violet lace set and an open robe, one arm behind her head, one knee raised, face turned to the viewer; blue snow and pines fill the glass behind her. Colour key: cold snow blue against one warm lamp."],
 'glitch': [
  u"High, wide angle from above the desk. She is curled up in her desk chair in the pale teal lace set with the big black hoodie hanging open off her shoulders, knees pulled up, headphones round her neck, grinning up at the viewer over her glasses; six monitors glow around her. Colour key: teal screen light, magenta window.",
  u"Extreme close, bed level. She lies on her stomach on the unmade bed with her chin on her stacked fists, glasses slipping down her nose, cheeks pink, a cheeky smile; her shoulders, back and raised crossed ankles go soft-focus behind her. Colour key: magenta neon, teal shadow.",
  u"Low angle from the floor. She sits cross-legged on the desk among the keyboards in the lace set, headphones on, one hand throwing a peace sign beside her eye, tongue out, the small drone hovering by her shoulder. Colour key: teal and white monitor glow.",
  u"Back three-quarter, medium. She stands on tiptoe at the window watering a hanging plant from a mug, the hoodie slipped off one shoulder down to her elbow over the lace set, one leg bent, looking back at the viewer over her shoulder with a small shy smile. Colour key: neon signs through leaves."],
 'brick': [
  u"Low angle from the gym floor. She sits on the ring apron in the black lace set with orange edging, both arms draped over the middle rope, legs swinging, goggles pushed up, dog tags on her chest, a wide confident grin down at the viewer. Colour key: one hard lamp from above, orange rim.",
  u"Close, eye level. She hugs the heavy bag with both arms and rests her cheek against it, catching her breath, shoulders shining, eyes sliding sideways to the viewer with a lazy half-smile. Colour key: warm lamp on skin, steel grey.",
  u"Low angle, full figure filling the frame. She stands by the lockers with a towel round her neck, gripping both ends, the charcoal hoodie tied by its sleeves round her hips over the lace set, chin up, laughing. Colour key: locker steel, orange accent, steam.",
  u"Eye level, wide. She lies along the wooden bench on her side, propped on one elbow, tossing a boxing glove up with her free hand and watching the viewer, one knee raised. Colour key: amber lamp pool in a dark gym."],
 'mirage': [
  u"Over her bare shoulder into the lit dressing-table mirror. In the black lace set with fine gold details, the wine silk robe down at her elbows, she touches up her lipstick; her face appears in the reflection, eyes meeting the viewer's with a slow knowing smile. Colour key: mirror bulb gold, wine shadow.",
  u"Eye level, medium. She reclines along the chaise in a long S-curve on her side, propped on one elbow, a champagne coupe held loosely, stockings with lace tops, head tilted, gaze direct. Colour key: city bokeh, warm lamp.",
  u"Back three-quarter, knee-up. She stands at the balcony glass, the robe sliding off her shoulders to the small of her back, looking over her shoulder at the viewer; the city lights and her faint reflection fill the glass. Colour key: midnight blue and gold.",
  u"Close, low, from the carpet. She sits on the edge of the bed drawing a stocking up over her knee with both hands, leaning forward, hair falling to one side, eyes lifted to the viewer, lips curved. Colour key: gold lamp on skin, deep wine."],
 'doc': [
  u"Close, eye level. She sits on the edge of the examination couch in the white lace set with lime ribbon, the white coat open and off both shoulders, stethoscope round her neck, leaning forward on straight arms, a teasing confident smile, tattooed arms framing the shot. Colour key: green-shaded lamp, warm gold.",
  u"Tight side view through blurred leaves. She waters the window plants with a small can, the open white coat hanging from her elbows over the lace set, hair coming loose, glancing sideways at the viewer mid-smile. Colour key: leaf green and lamp amber.",
  u"Eye level, medium. She sits backwards on the rolling stool, arms folded on the backrest and chin on her arms, bare tattooed shoulders, one foot pushing the stool in a slow turn, eyes warm and amused. Colour key: lamp pool, soft lime accent.",
  u"High angle. She lies on her side along the examination couch reading a chart held up in one hand, a pen between her lips, the other hand in her curls, eyes flicking up over the chart to the viewer. Colour key: clinic white, green shadow."],
}
RO_HOME = u"Three-quarter length, straight from behind, eye level. She walks away from the viewer across the lodge toward the fire, barefoot on the fur rug, in the deep violet lace set, the plum silk robe trailing from one hand along the floor, dog tags thrown over her shoulder so they hang down her bare back. Her head is turned just far enough to show her profile and one violet eye looking back, a faint smirk. Firelight wraps one side of her back, waist and hips; the window of blue snow lights the other. Colour key: fire orange against snow blue, violet accent."

# 시즈널: 스테이지 카드(WIDE). 크리스마스 룩 완전 착장.
WS = {
 1: u"Medium two-shot at eye level under the striped awning lights of a market stall. MIRAGE has her arm hooked through RAVEN's and leans in to whisper at her ear, a gloved finger lifting the end of RAVEN's red scarf; RAVEN keeps her eyes on the viewer with one eyebrow raised and the smallest smile, a steaming cup of mulled wine in her hand. Colour key: amber and candy red against blue night.",
 2: u"Low-angle full shot between two freight cars strung with work lights. GLITCH rides piggyback on BRICK, arms round her neck, cheek against her hair, kicking one striped leg and laughing; BRICK holds her thighs, strides toward the camera through the snow and grins straight at the viewer. Colour key: sodium orange and teal signal light.",
 3: u"Close two-shot on the step of the red hut on the frozen lake. They sit hip to hip under one blanket thrown round both their shoulders; VIPER has let her head drop onto DOC's shoulder, eyes half closed, a flask in her hand, while DOC's arm is round her and DOC looks at the viewer with a knowing warm smile. Breath in the cold, the searchlight sweeping far behind. Colour key: violet and lime against ice blue.",
 4: u"Eye-level medium shot in the candlelit aisle between the cathedral pews, tall columns behind. MIRAGE stands close in front of RAVEN retying her red scarf with both hands, forehead almost touching hers, eyes lowered, sincere; RAVEN's hand rests on MIRAGE's waist and her eyes are on MIRAGE, not the viewer. This card only: neither looks at the lens. Colour key: candle gold and stained-glass crimson.",
 5: u"Wide shot inside the hangar, snow blowing past the open doors and runway lights beyond. The three sit in a row on the wing of the small jet: RAVEN in the middle, legs crossed, looking at the viewer; VIPER reclines behind her back to back, one knee up, head tipped onto RAVEN's shoulder; GLITCH hugs RAVEN's arm with both of hers, feet swinging, beaming. Colour key: cold runway blue, warm hangar lamp, crimson, violet and teal accents.",
}
SANTA = u"Three-quarter length, straight from behind, slightly low. SANTA stands in the open doorway of a dark hangar on Christmas Eve, snow blowing in around her, runway lights and the tail of a private jet in the blue night beyond. She is letting her crimson fur-trimmed coat slide off both shoulders; it hangs at her elbows and falls open behind her, and under it she wears a black backless evening gown cut to the small of her back that follows the line of her waist and hips. Long auburn hair blows across her bare shoulder blades. Her head is turned a little to one side: only the line of her jaw and a hint of a smile show, and her eyes are hidden by hair and shadow. **Her face must not be readable.** One gloved hand holds a small red gift box by its ribbon at her side. Mood: a beautiful stranger who knows exactly who is watching her. Colour key: deep blue night, one warm light from inside the hangar on her back, crimson."

# 스페셜: 속옷 차림으로 탈의실에 들어가는 순간. 입을 코스튬이 걸려 있다.
SP = {
 'raven': u"Eye level, knee-up, from inside the wardrobe room. She pushes the heavy crimson drape aside with one raised arm and steps through from the arena, in the black lace set with crimson ties, looking straight at the viewer with a cool half-smile; the matador bolero waits on a hanger beside the bulb-ringed mirror in the foreground. Colour key: crimson drape, warm bulbs.",
 'viper': u"Wide, low shot along the locker-room bench. She leans one shoulder on the door frame in the violet sheer lace set, a pair of white skates slung over her shoulder by their laces, weight on one hip, a lazy smirk; the violet skating dress hangs on the rail beside her, frost on the windows. Colour key: silver frost light, violet accent.",
 'glitch': u"Medium, slightly high. She backs in through the dressing-room door pushing it open with her hip, hugging a garment bag to her side with one arm, the other hand waving, in the pale teal lace set with holographic trim, glasses on, a bright embarrassed grin; fairy lights, the make-up mirror and the holographic jacket on its rail behind her. Colour key: fairy-light gold, teal laser leak from the corridor.",
 'brick': u"Low angle, full figure filling the doorway. She shoulders the locker-room swing door open, a towel over one shoulder, in the black lace set with orange satin edging, goggles pushed up, grinning down at the viewer; the champion's robe hangs on a hook and the title belt lies on the bench in the foreground. Colour key: hard white corridor light behind, warm locker room, orange rim.",
 'mirage': u"Medium, eye level, with a mirror at the edge of frame showing her back. In the VIP salon she folds back one panel of the silk screen with a fingertip and steps round it, in the black lace set with fine gold chains and seamed stockings, chin lifted, a slow knowing smile; the dealer's waistcoat hangs over the top of the screen. Colour key: gold lamp, black marble, green baize glow from the casino beyond.",
 'doc': u"Back three-quarter, medium-wide, down a short corridor of warm wood and drifting steam. She walks toward the relaxation room in the white lace set with lime ribbon, both hands raised to pin up her curls, tattooed arms lifted, and looks back over her shoulder at the viewer with a teasing smile; the white corset dress hangs on the door ahead of her. Colour key: warm wood and steam, lime accent light."}
SP_HOME = u"Three-quarter length from behind and to one side, eye level. MIRAGE walks away down a backstage corridor toward an open dressing-room door ringed with warm bulbs, in the black lace set with fine gold chains, seamed stockings and stilettos, one hand trailing along the wall, the other carrying a costume on a hanger hooked over her shoulder by one finger. She glances back in profile with a slow knowing smile, gold hoop catching the light. Colour key: dark corridor, gold doorway light wrapping her back, waist and hips."


def agent_block(a, lin=None, place=None):
    v = CS.A[a]; t = u'- **%s** (`agents/sheet_%s.jpg`, signature colour %s). %s. Personal details: %s\n' % (v[0], a, v[2], v[5][0].upper() + v[5][1:], u'Her long red scarf is on in every card.' if a == 'raven' else RN.D[a]['det'].replace(u'every cut', u'every card'))
    if lin: t += u'  - Lingerie: %s\n' % lin
    if place: t += u'  - Place: %s\n' % place
    return t


def head(title, rows, note):
    t = u'# SILENT SIX — %s\n\n## 사용법 (사람이 읽는 부분)\n\n1. ChatGPT **새 대화**에 이 zip을 올리고 **"압축을 풀고 지시.md 를 끝까지 읽은 뒤, 첫 장부터 한 장씩 진행해 줘."**\n2. 한 번에 한 장. 다음 장은 "next". **이 묶음은 %d장이다.**\n3. 파일명 그대로 Claude에게 넘긴다.\n4. 수건 · 가운이나 가리는 포즈가 나오면: **"What this is 항목과 level 폴더를 다시 보고, 속옷 차림 그대로 가리는 포즈 없이 다시 그려 줘."**\n\n| 파일 | 쓰이는 곳 | 형식 |\n|---|---|---|\n' % (title, len(rows))
    for r in rows: t += u'| `%s` | %s | %s |\n' % r
    return t + (u'\n' + note + u'\n' if note else u'') + u'\n---\n\n' + COMMON


def build(out, lvdir, zn, text, agents, levels, places=()):
    z = zipfile.ZipFile(os.path.join(out, zn + '.zip'), 'w', zipfile.ZIP_DEFLATED)
    z.writestr(zn + u'/지시.md', text); z.write(os.path.join(CSO, 'AGENTS.md'), zn + '/AGENTS.md')
    for a in agents: z.write(os.path.join(CSO, 'sheet_%s.jpg' % a), '%s/agents/sheet_%s.jpg' % (zn, a))
    k = 0
    for b, m in levels:
        f = os.path.join(lvdir or '', b.capitalize(), 'n_%s_%d.png' % (b, m))
        if lvdir and os.path.exists(f):
            k += 1; tmp = io.BytesIO(); Image.open(f).convert('RGB').resize((768, 1152), Image.LANCZOS).save(tmp, 'JPEG', quality=86); z.writestr('%s/level/level_%s_%d.jpg' % (zn, b, m), tmp.getvalue())
    for p in places: z.write(os.path.join(PUB, p), '%s/place/%s' % (zn, p))
    z.close(); io.open(os.path.join(HERE, 'packs', zn + u'_지시.md'), 'w', encoding='utf8').write(text)
    print(zn, os.path.getsize(os.path.join(out, zn + '.zip')) // 1024, 'KB', 'level', k, 'chars', len(text)); return text.count('\n### ')


def main(out, lvdir=None):
    os.makedirs(out, exist_ok=True); os.makedirs(os.path.join(HERE, 'packs'), exist_ok=True); n = 0
    for a in AG:
        ko = RN.D[a]['ko'].split(u' · ')[0]; rows = []; body = u''
        if a == 'viper':
            rows.append(('kv_romantic', u'홈 화면 로맨틱 미션 타일', u'세로')); body += u'### `kv_romantic` — TALL — home tile: lingerie, seen from behind\n\n%s\n\n' % RO_HOME
        names = [(u'kr_%s_0' % a, u'로맨틱 미션 진입 화면의 %s 카드' % ko, u'AGENT CARD')] + [(u'kr_%s_%d' % (a, k), u'%s TAKE %d 카드' % (ko, k), u'TAKE %d CARD — a variation of the agent card' % k) for k in (1, 2, 3)]
        for (fn, use, lab), c in zip(names, RO[a]):
            rows.append((fn, use, u'가로')); body += u'### `%s` — WIDE — %s\n\n%s\n\n' % (fn, lab, c)
        text = head(u'로맨틱 미션 카드 · %s' % ko, rows, u'네 장의 가로 카드는 같은 요원, 같은 장소, 같은 속옷이고 포즈와 구도만 다르다.') + u'## THIS AGENT\n\n' + agent_block(a, RN.D[a]['lin'], RN.D[a]['place']) + u'\n**Her visual language.** %s\n\n**Wardrobe for every card in this pack.** Her lingerie as written above; where a card names a robe, shirt, hoodie or coat it is worn open or slipping off, never closed. Only she appears.\n\n## THE CARDS\n\n' % RN.VIS[a] + body
        n += build(out, lvdir, 'SILENT6_Card_Romantic_%s' % a.upper(), text, [a], [('brick' if a == 'brick' else a, 5), (a, 4)])
    # 시즈널
    rows = [('kv_winter', u'시즈널 미션 진입 화면의 블러디 크리스마스 소개', u'세로')] + [('kw_%d' % s, u'블러디 크리스마스 스테이지 %d 카드' % s, u'가로') for s in range(1, 6)]
    body = u'## CARD 1 — SANTA\n\nSANTA (`agents/sheet_santa.jpg`) is the antagonist of this event: an adult woman, tall, long auburn hair, a crimson fur-trimmed coat, once one of the agents\' own. The player has not seen her face yet, and this card keeps it that way. Only she appears.\n\n### `kv_winter` — TALL — the coat comes off, the face stays hidden\n\n%s\n\n## CARDS 2–6 — STAGE CARDS\n\nA Christmas service shot of the agents who run that stage. Nobody wears tactical gear: each wears her **Christmas outfit, complete**, styled to flatter (short hems, bare shoulders, thigh-high boots), and they are visibly fond of each other. Every listed agent appears, clearly distinct. The stage map in `place/` is the setting.\n\n' % SANTA
    used = []
    for s in range(1, 6):
        st = W3.ST[s]; body += u'### `kw_%d` — WIDE — STAGE %d · %s\n\n' % (s, s, u' + '.join(CS.A[a][0] for a in st['ag']))
        for a in st['ag']:
            body += (agent_block(a) if a not in used else u'- **%s**: as above.\n' % CS.A[a][0]) + u'  - Christmas outfit: %s\n' % W3.XMAS[a].split(u' Lingerie:')[0]; used.append(a)
        body += u'\n**Place.** %s\n\n**Between them.** %s\n\n**The shot.** %s\n\n' % (st['place'], W4.REL[s], WS[s])
    text = head(u'시즈널 미션 카드 · 블러디 크리스마스', rows, u'홈 화면의 시즈널 타일은 지금 이미지를 유지한다. 스테이지 카드는 속옷이 아니라 크리스마스 룩이다.') + body
    n += build(out, lvdir, 'SILENT6_Card_Seasonal_BloodyChristmas', text, AG + ['santa'], [('raven', 5), ('mirage', 5)], ['bgw1.jpg', 'bgw2_0.jpg', 'bgw3.jpg', 'bgw4_0.jpg', 'bgw5_0.jpg'])
    # 스페셜
    rows = [('kv_special_menu', u'홈 화면 스페셜 미션 타일', u'세로')] + [('kc_%s' % a, u'코스튬 미션의 %s 카드' % RN.D[a]['ko'].split(u' · ')[0], u'가로') for a in AG]
    body = u'## THE IDEA\n\nThe costume mission starts in the dressing room. Each card catches an agent **in her lingerie on her way in to change**, with the costume she is about to put on hanging in the shot. Only that agent appears.\n\n### `kv_special_menu` — TALL — MIRAGE, home tile\n\n' + agent_block('mirage', CO.D['mirage']['lin']) + u'\n%s\n\n' % SP_HOME
    for a in AG:
        d = CO.D[a]; body += u'### `kc_%s` — WIDE — %s\n\n' % (a, CS.A[a][0]) + agent_block(a, d['lin']) + u'  - Her costume (hanging up, not worn): %s\n  - Venue: %s\n\n**The shot.** %s\n\n' % (d['cos'], d['ven'], SP[a])
    text = head(u'스페셜 미션 카드 · 코스튬', rows, u'스페셜 미션 안의 코스튬 미션 카드(닥)는 지금 이미지를 유지한다.') + body
    n += build(out, lvdir, 'SILENT6_Card_Special_Costume', text, AG, [('mirage', 5), ('doc', 5), ('viper', 5)])
    print('cards', n)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'out', sys.argv[2] if len(sys.argv) > 2 else None)
