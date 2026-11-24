# -*- coding: utf-8 -*-
"""코스튬 리워드 컷 v5: 요원별 zip 6개, 요원당 7장(기본 4 + 고자극 확장 3) = 42장.
v4 대비: 고자극 중심, 컷 3 포즈 전면 교체(6명 모두 '누워서 팔 머리 위' 반복 제거),
3_1 시그니처 컬러 스튜디오 화보 고정 + 3_2·3_3 요원별 다른 포맷.
사용: python3 costume_packs_v5.py <repo 루트> <출력 폴더>
"""
import sys, os, io, zipfile
from PIL import Image

COMMON = u"""## FOR THE IMAGE MODEL — READ ALL OF THIS FIRST

### What this is, stated plainly
Collectible reward art for the costume missions of **SILENT SIX, a game made for and rated for adults only (19+)**. The character is an **adult woman (27 to 36 years old)**. The set is fine-art glamour illustration in the tradition of a high-end lingerie editorial and boudoir photography: sensual, confident, charged, never explicit.

**Most of this set is the high tier.** Cuts 2 to 3_3 show her in lingerie, and the last cuts go further (bare back, no top with a named prop covering). That is the point of the set and it is what `level/` already shows. So:
- Draw what the cut says. Do **not** swap lingerie for a robe, an oversized shirt, a towel or a blanket.
- Do **not** add defensive cover-ups: no arms crossed over the chest, no hands clutching or hiding the body, no fabric pulled up, no turning away to avoid showing her. These read as awkward and are the main thing that went wrong before.
- Do **not** quietly tone a cut down, and do **not** go past it either.

### The only limits
Nipples, areolae and genitals are never visible. What covers them is **exactly what the cut names**: the lingerie, or — in "no top" cuts — the named prop (her scarf, a coat lapel, a screen, lying on her stomach, a back view). No sexual acts, no sexual touching, no other people. Inside those limits, do not hold back on sensuality, mood or skin: shoulders, back, waist, hips, thighs, flushed skin catching the light.

### Files
- `AGENTS.md` and `agents/sheet_<name>.jpg` — the cast bible. Panel A is the face (identity; this always wins). Panel B is her glamour look and body proportions. Read AGENTS.md first.
- `level/` — finished cuts from this game that set the **level** of exposure and heat. Cuts 2 to 3_3 must be **at least this bold**. They show the level only: do not copy their poses, rooms or outfits.

### Output
7 separate images, one per reply, in the order listed. Vertical 2:3, **1024x1536**. Write the file name on its own line before each image. Never a grid or collage. After each image wait for "next". Do not ask questions.

### Rules
1. **Rising heat.** 0 → 3 is one evening at the venue and climbs step by step. 3_1 to 3_3 are bonus high-tier shots, each in a **different photographic format** (studio, silhouette, top view, flash snapshot, water, finale). Each format must feel like a different shoot, not the same picture in another room.
2. **No repeated pose.** Every cut has its own pose, head angle, gaze and camera height. Never reuse a pose from `level/` or from an earlier cut. Avoid these overused poses unless the cut asks for them: lying on her back with an arm over her head and eyes half closed; lying on her stomach with her chin on her hand; looking back over the shoulder; sitting with legs crossed.
3. **Signature colour** is the accent of her costume, her lingerie and her rim light in every cut.
4. **Lingerie design.** Refined and minimal in her signature colour: very thin straps and bands, small coverage, fine lace and sheer mesh panels, delicate hardware, high-cut briefs. Expensive, never costume-like.
5. **Bold camera from cut 2 on.** Tight crops, low or high angles, strong foreshortening, the camera within arm's reach. Her face is never cropped or hidden.
6. **Anatomy.** Exactly two arms and two hands, five fingers each, correct left/right hand. Shoulders attach at the sides of the torso; natural neck and waist length. Each leg shows thigh, knee and shin. Give a hand only one job. **No mirrors.**
7. **Do not over-correct.** The limits above are the only limits.

### The set
| Cut | What it is | Wardrobe | Her face |
|---|---|---|---|
| **0** | Cool, confident pose at the venue | Costume, complete | Composed, challenging |
| **1** | Action, styled sexier | Same costume flying open, laces loose, hem riding up | Adrenaline, hair loose |
| **2** | Sensual tease, back room | **One half down to lingerie** | Warm, teasing, eyes on the viewer |
| **3** | Erotic peak, back room | **Lingerie only** | Heated, lost in the moment |
| **3_1** | **STUDIO** — fashion editorial on a seamless backdrop in her signature colour | Lingerie styled with key costume pieces | Model's confidence, direct |
| **3_2** | Bonus format (below) | As written | As written |
| **3_3** | Bonus format, the boldest of the set | As written | As written |

### STUDIO (cut 3_1) — the same rule for every agent
A professional photo studio. Seamless paper backdrop and floor in her signature colour, curving into the floor with no horizon. Big softbox key light, a hard rim light in a lighter tint of her colour, a little haze. The costume becomes fashion styling: lingerie plus two or three signature costume pieces (named below), and one or two props from the venue used as set pieces. A strong, deliberate editorial pose, full body or three-quarter, graphic colour-blocked composition. No text.

### Identity and quality
- Exactly as in her sheet: face, hair, eye colour, skin tone, build, tattoos. Only she appears.
- Semi-realistic anime illustration with a painterly, high-end finish: detailed eyes and hair strands, real satin, lace, sequin and skin texture.
- Cuts 0 to 3 and venue bonus cuts: three depth layers (soft foreground, her, a fully painted part of the venue). Two light sources of different colour plus signature-colour rim light.
- No text, logo, watermark or UI.

---

"""

FMT = {
 'SILHOUETTE': u'SILHOUETTE — hard backlight through a sheer or translucent surface; her shape in rim light, her face in soft front light',
 'TOPVIEW': u'TOP VIEW — camera directly above, her body and the props on the floor make a graphic pattern',
 'FLASH': u'FLASH SNAPSHOT — direct on-camera flash, candid backstage snapshot, hard shadow on the wall behind, film grain',
 'WATER': u'WATER — wet skin and hair, steam, droplets catching the light',
 'FINALE': u'FINALE — the empty venue after the show, one spotlight, dust in the beam',
}

D = {
 'raven': dict(ko=u'RAVEN · 붉은 막 — 원형 공연장 갈라의 밤', col=u'crimson',
  cos=u"a matador-inspired stage outfit: a cropped black bolero with crimson and gold embroidery, a black high-waisted corset bodysuit, a short crimson cape-skirt open at the front, sheer black tights, heeled ankle boots, and her long red scarf.",
  lin=u"fine black lace with thin crimson ribbon ties and a few gold-thread roses, sheer mesh side panels, high-cut brief.",
  ven=u"A circular show arena on a matador-themed gala night: a sand ring under hard spotlights, crimson drapes, gold trim, banked seats, stage smoke. Back room: a wardrobe room with bulb-ringed vanity lights (no mirror glass shown), costume trunks and red roses.",
  who=u"She never drops her guard in front of the team. With her handler she lets it slip, slowly and on her own terms: level stare first, then a dare, then permission.",
  c0=u"Full body, camera low at the edge of the sand ring looking up. She stands side-on in the spotlight, the cape-skirt swept back in one fist like a matador's cape, chin over her shoulder, a flat challenging stare. Smoke and gold dust in the beam. Colour key: crimson and black with hard white light.",
  c1=u"Action, strong diagonal, camera level with the ring fence. Mid-spin as she vaults the fence, bolero flying open off one shoulder, a lace of the corset pulled loose, scarf and cape streaming, a fierce bitten-lip grin. Sand kicked into the light. Colour key: deep red motion against black seats.",
  c2=u"Close, waist to hair, eye level in the wardrobe room. Bolero and corset off and hanging from a chair: **top half in the black lace bra with crimson ties**, cape-skirt and tights still on. She sits back against the dressing table on straight arms, head tilted, one eyebrow up, lips parted, looking straight at the viewer, the red scarf loose around her neck. Colour key: warm bulb amber, crimson shadow.",
  c3=u"Very close, low angle. **Lingerie only**, boots on. She kneels on the closed lid of a crimson velvet costume trunk, sitting back on her heels, back arched, the red scarf hanging over one shoulder and down her stomach, chin lowered, looking down into the lens from under her lashes with a slow, dangerous half-smile. Roses on the floor in the foreground blur. Colour key: bulb gold and deep crimson.",
  st=u"Crimson seamless. Styling: the lingerie, the embroidered bolero worn open on her shoulders, sheer tights and heeled ankle boots. Set piece: the crimson cape held out wide behind her in one hand like a matador's cape filling half the frame, red rose petals falling. Pose: wide planted stance, weight on one leg, hip turned, chin down, a flat stare straight into the lens. Low camera at knee height.",
  x=[('SILHOUETTE', u"Behind a sheer crimson stage curtain, a spotlight blazing behind her. **Lingerie only.** Her full silhouette glows through the curtain in red rim light; she has parted the curtain at her face with her LEFT hand, so her face, throat and one bare shoulder come through into soft front light. Lips parted, eyes on the viewer. Medium shot, camera at chest height."),
     ('TOPVIEW', u"Camera directly above the sand ring. **No top**, black lace brief only, boots on. She lies on her back in the sand, arms flung out to the sides, hair fanned, the long red scarf laid diagonally across her chest so it covers each breast completely like a bandeau, crimson rose petals scattered around her in a ring. She looks straight up into the lens, flushed, a breathless smile. Hard spotlight from one side, long shadows.")]),
 'viper': dict(ko=u'VIPER · 은반 — 아이스링크 갈라쇼', col=u'deep violet',
  cos=u"an ice-queen figure-skating costume: a violet long-sleeved leotard dress with a sheer mesh back and silver crystal trim, a very short asymmetric skirt, skin-tone tights, white skates, a silver hair comb, and her two dog tags.",
  lin=u"deep violet sheer mesh and lace with tiny silver crystals along thin straps, high-cut brief with delicate silver rings.",
  ven=u"An indoor ice rink during a gala figure-skating show: violet and silver spotlights, frost haze, rink boards, glitter in the air. Back room: a locker room with frosted windows, skate bags, a bench and a rack of sequinned costumes.",
  who=u"Lazy, teasing, impossible to fluster. With her handler the teasing becomes an invitation: she makes them wait, and enjoys being watched while she does.",
  c0=u"Full body, high camera from the rink boards. She glides backwards on one skate in a single violet spotlight, arms loose, looking up at the viewer with a half-lidded, amused stare, ice spray and glitter behind her blade. Colour key: violet and silver on blue-white ice.",
  c1=u"Action, tilted frame, camera low on the ice. Mid layback spin: back arched, skirt flared, the mesh back catching the light, one strap slipped off her shoulder, hair whipping, lips parted, eyes closed in concentration. A ring of ice shavings. Colour key: silver streaks on violet dark.",
  c2=u"Close, mid-thigh to hair, in the locker room, sitting sideways on the bench unlacing one skate. The dress is peeled down to her waist: **top half in the violet mesh bra with silver crystals**, skirt and tights still on. She looks at the viewer with a slow one-sided smile, cheeks flushed from the cold, dog tags swinging. Colour key: cold blue window light, warm locker lamp.",
  c3=u"Close, slightly low. **Lingerie only**, dog tags on her collarbone. She leans her back against the frosted window, both forearms resting on the sill behind her, one knee lifted with that foot flat against the wall, head turned to one side, eyes closed, a slow exhale fogging in the cold air. Cold blue light behind, warm lamp across her stomach and thighs. Colour key: violet shadow and warm skin.",
  st=u"Deep violet seamless with silver haze. Styling: the lingerie, white figure skates, the silver crystal comb in her hair, the dog tags, sheer skin-tone tights. Set piece: a white prop cube and scattered ice crystals catching the strobe. Pose: sitting on the cube in a skater's extension — one leg stretched long toward the camera, toe pointed, the other folded under her, leaning back on one straight arm, head tipped, a half-lidded amused stare. Camera low at the blade.",
  x=[('FLASH', u"Locker room after the show, caught by a direct flash. **Lingerie only**, one white skate still on. She sits astride the bench facing the camera, leaning forward on both hands placed on the bench in front of her, shoulders pressed together, dog tags hanging, hair messy, laughing mid-word at whoever took the picture. Hard flash shadow on the lockers behind."),
     ('TOPVIEW', u"Camera directly above the empty rink. **No top**, violet brief only. She lies on her back on a white fur team coat spread open on the ice, the coat's wide fur lapels folded across her chest covering each breast completely, one knee bent, arms loose above her shoulders in the fur, skate-blade scratches circling her on the ice, glitter scattered. She looks straight up into the lens with a lazy, knowing smile. Violet spotlight pooled around her, blue ice beyond.")]),
 'glitch': dict(ko=u'GLITCH · 앙코르 — 콘서트 돔 백스테이지', col=u'teal',
  cos=u"a cyber-idol stage outfit: a cropped teal holographic jacket, a black bustier top with glowing teal piping, a pleated micro skirt, fishnet tights, platform boots, a holographic visor pushed up on her head, her round glasses and headphones.",
  lin=u"pale teal lace with holographic trim, thin straps with tiny white bows, sheer mesh cups, high-cut brief.",
  ven=u"Backstage of a huge concert dome during an idol show: the back of a giant LED wall, teal lasers, flight cases, cables, magenta light leaking through. Back room: a small dressing room with vanity bulbs (no mirror glass shown), fairy lights, energy-drink cans and a costume rail.",
  who=u"The youngest of the team, quick and nervous, brave only when someone she trusts is watching. With her handler she shows off first, then gets shy, then stops hiding.",
  c0=u"Full body, camera low among the flight cases. She stands on a case in the light leaking through the LED wall, one hand throwing a peace sign beside her visor, hip out, a huge confident grin. Teal lasers behind. Colour key: teal and magenta neon.",
  c1=u"Action, hard diagonal, camera beside the stage lift. She slides on her knees across the stage floor behind the LED wall, jacket flying off both shoulders, skirt flared, headphones round her neck, mouth open in a breathless laugh, glasses flashing. Pyro sparks above. Colour key: black with teal streaks.",
  c2=u"Close, hips to hair, in the dressing room, kneeling up on a flight case facing the viewer, fairy lights behind her. Jacket and bustier off: **top half in the pale teal lace bra with white bows**, skirt and fishnets still on. She bites the arm of her glasses, cheeks pink, looking up at the viewer through her fringe. Colour key: warm bulb light, teal rim.",
  c3=u"Close, eye level. **Lingerie only**, glasses on. She kneels upright on a big beanbag heaped with tour hoodies, facing the camera, using her RIGHT hand to pull the headphones off over her head so her hair is pulled up and messy, her left hand resting on her thigh, flushed, a shy-but-daring grin straight at the viewer. Fairy lights blurred behind. Colour key: fairy-light gold and soft teal.",
  st=u"Teal seamless with holographic light flares. Styling: the lingerie, the holographic jacket slipping off both shoulders to her elbows, fishnet tights, platform boots, the visor pushed up, round glasses. Set piece: a chrome stage microphone stand and a coil of glowing cable on the floor. Pose: leaning her weight on the mic stand at an angle, one platform boot hooked around its base, hip out, other hand on her waist, mouth open in a playful laugh at the lens. Three-quarter body, camera slightly low.",
  x=[('SILHOUETTE', u"Behind the stage, facing the back of the giant LED wall, which blazes teal and magenta through a sheer mesh scrim. **Lingerie only**, platform boots. Back view, full body, both hands raised holding her headphones above her head as if about to put them on, back arched, her silhouette rimmed in teal; she turns her face toward the camera in profile, eyes closed, smiling. Lasers cut the haze above."),
     ('FLASH', u"Dressing room floor, caught by a direct flash like a backstage polaroid. **Lingerie only**, fishnets and platform boots on, glasses crooked. She sits on the floor among dropped costumes, leaning back against the costume rail, knees up and apart with her boots planted, one arm resting on a knee, laughing with her eyes squeezed shut and her tongue just showing, energy-drink cans around her. Hard flash shadow on the wall.")]),
 'brick': dict(ko=u'BRICK · 타이틀 매치 — 호텔 연회장 특설 링', col=u'orange',
  cos=u"a champion-boxer show outfit: an open black satin robe with orange trim and hood, a black sports bralette top with orange piping, high-waisted orange satin boxing shorts with a wide black waistband, taped hands, boxing boots, her goggles pushed up, dog tags.",
  lin=u"black lace with orange satin edging, a thin racer-back strap line, sheer mesh panels, high-cut brief with a narrow orange waistband.",
  ven=u"A luxury hotel ballroom set up for a title fight: a boxing ring under one hard white light, dinner tables, orange and black bunting, chandeliers. Back room: a fighters' locker room with a massage table, hanging robes, a title belt on a bench and steam from the showers.",
  who=u"Loud, warm, proud of her strength. With her handler the bravado turns into open, unguarded affection: she shows off, then lets herself be soft.",
  c0=u"Full body, camera low at ringside looking up through the ropes. She stands on the bottom rope with the robe open and the hood down, one taped fist raised, the title belt over her shoulder, a wide winning grin down at the viewer. Colour key: hard white ring light, orange accents.",
  c1=u"Action, strong diagonal, camera inside the ring at chest height. Mid-hook, robe sliding off one arm, shoulders and stomach glistening, sweat flying, teeth bared in a fierce grin, eyes locked just past the lens. Chandeliers streaked behind. Colour key: black and orange with white flare.",
  c2=u"Close, knees to hair, in the locker room, sitting on the massage table unwinding the tape from one hand with her teeth. Shorts off and folded beside her: **bottom half in the black lace brief with the orange waistband**, bralette still on, robe hanging from her elbows. She looks at the viewer with a slow grin, cheeks flushed, steam behind her. Colour key: warm locker lamp, orange rim.",
  c3=u"Medium close, camera slightly low. **Lingerie only**, dog tags on her chest. She stands in the steam at the locker-room doorway, one forearm braced high on the door frame, the other hand hooked on the orange waistband at her hip, powerful shoulders and stomach glistening, head tilted, a lazy, flushed, wordless smile straight at the viewer. Colour key: amber steam and deep shadow.",
  st=u"Orange seamless. Styling: the lingerie, the black satin robe slipped down to her elbows, boxing boots, taped hands, goggles up. Set piece: the gold title belt worn slung low and diagonal across her hips over the lingerie, a pair of boxing gloves hanging from one shoulder by the laces. Pose: power stance, feet wide, taped fists pressed together in front of her stomach, shoulders squared, chin up, a proud grin down into the lens. Very low hero angle.",
  x=[('FINALE', u"The ring after the crowd has gone, chairs empty, one spotlight from directly above. **Lingerie only**, boxing boots. She sits on the canvas leaning back into a corner post, both arms draped along the top rope, one leg stretched out and one knee up, sweat glistening on her shoulders and stomach, head resting back against the post, eyes on the viewer, a tired, satisfied grin. Dust floating in the beam. Camera low on the canvas."),
     ('WATER', u"Locker-room shower, hot water and thick steam. **No top**, wet black lace brief only. Back view from the hips up: one palm flat on the tiles above her head, water running over her bare back and powerful shoulders, her face turned in clean profile toward the camera with eyes closed and lips parted. Her chest faces the tiles and is not shown. Warm light through steam, droplets on her skin.")]),
 'mirage': dict(ko=u'MIRAGE · 하우스 엣지 — 펜트하우스 카지노', col=u'gold',
  cos=u"a casino-dealer costume: a fitted black waistcoat with gold buttons worn with nothing under it but a gold bow-tie collar and white cuffs, black satin shorts, sheer black stockings with a back seam, stilettos, gold hoop earrings, one long black glove.",
  lin=u"black lace with fine gold chain details and gold clasps, thin straps, sheer mesh, high-cut brief with a narrow gold chain at the hip.",
  ven=u"A private penthouse casino at night: green baize tables, a roulette wheel, a gold-lit bar, black marble, city lights through tall windows. Back room: a VIP salon with a velvet chaise, a translucent silk screen, scattered chips and a champagne bucket.",
  who=u"She is always performing. With her handler she performs on purpose, knowing they know; the last cut of the evening is the one moment the act is gone.",
  c0=u"Full body, camera at table height across the baize. She leans one hip against the roulette table, fanning a deck of cards in her gloved hand, a slow knowing smile at the viewer, city lights behind. Colour key: gold and black with green baize.",
  c1=u"Action, tilted frame, camera low beside the table. She slides across the baize on one hip, cards and chips flying, waistcoat pulled open by the movement to its last button, bow tie undone, hair swinging, a delighted flushed laugh. Colour key: gold sparks on black marble.",
  c2=u"Close, hips to hair, in the VIP salon, standing in front of the silk screen. Waistcoat off and dropped on the chaise: **top half in the black lace bra with gold chain details**, shorts and stockings still on, the bow-tie collar still at her throat. She pulls the long glove off with her teeth, lashes lowered, eyes on the viewer, cheeks warm. Colour key: honey gold lamp, wine-dark shadow.",
  c3=u"Close, camera at floor level. **Lingerie only**, stockings and hoop earrings on. She sits on the carpet leaning back against the side of the velvet chaise, head resting on its cushion, one leg stretched toward the lens, the other knee bent, the hip chain catching the lamp, chips scattered around her, looking at the viewer with a real, unguarded smile — the act gone. Colour key: gold lamp and midnight-blue windows.",
  st=u"Gold seamless with a warm metallic sheen. Styling: the lingerie with gold chains, the gold bow-tie collar and white cuffs, sheer black seamed stockings, stilettos, gold hoops, one long black glove. Set piece: a tall black bar stool and oversized playing cards fanned across the floor and falling through the air. Pose: perched on the edge of the stool, one stiletto on the rung, the other leg extended long to the floor, leaning forward with her gloved forearm on her raised knee, a sly sideways look at the lens. Three-quarter body, camera at hip height.",
  x=[('TOPVIEW', u"Camera directly above a baccarat table. **Lingerie only**, stockings and stilettos on. She lies on her back across the green baize, one knee raised, hair spilling over the table edge, arms loose above her head among scattered chips and an exploded fan of cards, the gold hip chain glinting, looking straight up into the lens with a lazy, winning smile. Warm pendant light, the rest in shadow."),
     ('SILHOUETTE', u"A lamp glows behind the translucent silk screen in the VIP salon. **No top.** Her silhouette shows on the screen behind her. She leans out from behind the screen's edge: her face, throat and bare shoulders and one bare arm come into warm front light, while the screen panel itself covers her from the chest down. The bow-tie collar is still at her throat. Head tilted against the screen frame, a slow knowing smile at the viewer. Medium close, eye level.")]),
 'doc': dict(ko=u'DOC · 왕진 — 프라이빗 클리닉 & 스파', col=u'lime green',
  cos=u"a nurse-inspired costume: a glossy white corset dress with lime-green lacing and a very short skirt, a cropped white jacket, long white gloves, white thigh-high stockings with lime bands, a medic-cross choker, gold hoop earrings. Plant tattoos on BOTH arms only (follow her sheet).",
  lin=u"white lace with thin lime-green ribbon and tiny gold clasps, sheer mesh cups, high-cut brief tied with lime ribbon at the hips.",
  ven=u"A private cosmetic clinic and spa at night: white marble, lime-green accent light, a turquoise spa pool, orchids, soft steam. Back room: a sauna-side relaxation room with warm wood benches, folded white towels and drifting steam.",
  who=u"The eldest, the one who takes care of everyone and never lets anyone take care of her. With her handler she teases like a doctor giving orders, then lets them see her tired, warm and off duty.",
  c0=u"Full body, camera low on the marble floor. She stands by the reception desk with one gloved hand on her hip and a clipboard against her thigh, looking down at the viewer with a teasing, doctor-knows-best half-smile, lime light along the wall behind. Colour key: white marble and lime.",
  c1=u"Action, strong diagonal, camera level with the pool edge. She strides fast along the spa pool pulling one glove off with her teeth, jacket slipping off both shoulders, corset lacing loosened, skirt riding up over the stocking bands, curls coming loose, steam swirling. Colour key: turquoise water glow against white.",
  c2=u"Medium close, in the relaxation room. She stands in the doorway of the sauna, one shoulder against the wooden frame. Corset dress unlaced and pushed down to her hips: **top half in the white lace bra with lime ribbon**, stockings still on, both tattooed arms bare. She tucks a curl behind her ear, cheeks flushed from the heat, a slow warm smile at the viewer. Colour key: warm wood amber, lime rim.",
  c3=u"Close, camera low on the lower bench looking up. **Lingerie only**, choker and hoops on. She sits on the upper sauna bench leaning forward, forearms resting on her knees, hands loosely clasped, damp curls falling forward, skin dewy with steam, looking down into the lens with heavy-lidded, tired, unguarded warmth. Colour key: amber steam and soft lime.",
  st=u"Lime-green seamless. Styling: the lingerie, the cropped white jacket worn open, long white gloves, white thigh-highs with lime bands, the medic-cross choker; both tattooed arms visible. Set piece: a white rolling medical stool and a few white orchids on the floor. Pose: sitting on the stool turned three-quarters, one leg stretched toward the camera with the foot pointed, the other bent, leaning back with one gloved hand gripping the stool edge, the other raised to adjust her choker, chin up, a cool doctor's stare. Camera at knee height.",
  x=[('WATER', u"The turquoise spa pool at night. **Lingerie only**, wet white lace. She sits on the marble pool edge with both legs in the glowing water, leaning back on both straight arms, head tipped back, wet curls clinging to her shoulders and tattooed arms, droplets on her collarbone and stomach, eyes half open toward the viewer. Steam drifting, orchids blurred in the foreground. Camera low at water level."),
     ('FLASH', u"After hours at the clinic, caught by a direct flash. **No top**: she wears the cropped white jacket open over nothing, its lapels lying over her chest and covering each breast completely, with the white lace brief, stockings and choker. She sits on the reception desk, one stockinged foot up on the desk edge, the other leg hanging, leaning back on one hand, a pen held between her teeth, raising one eyebrow at the camera. Hard flash shadow on the white wall.")]),
}
ORDER = ['raven', 'viper', 'glitch', 'brick', 'mirage', 'doc']
LV = {'raven': [30, 33, 51], 'viper': [17, 33, 34], 'glitch': [6, 7, 22], 'brick': [4, 9, 21], 'mirage': [4, 21, 23], 'doc': [31, 32, 34]}  # public/gn 로맨틱 확정 컷(고자극)


def md(a, sheets):
    d = D[a]
    rows = [('0', u'멋진 포즈 — 코스튬 완전 착장', u'클리어 시 무료'), ('1', u'섹시한 액션', u'구매'), ('2', u'도발 — 한쪽 속옷', u'구매'), ('3', u'고자극 — 속옷', u'구매'),
            ('3_1', u'STUDIO — 시그니처 컬러 스튜디오 화보', u'고자극 추가'), ('3_2', u'%s' % d['x'][0][0], u'고자극 추가'), ('3_3', u'%s (세트 최고 수위)' % d['x'][1][0], u'고자극 추가')]
    t = u'# SILENT SIX — 코스튬 미션 리워드 컷 v5 · %s\n\n## 사용법 (사람이 읽는 부분)\n\n1. ChatGPT **새 대화**에 이 zip을 올리고: **"압축을 풀고 지시.md 를 끝까지 읽은 뒤, CUT 0부터 한 장씩 진행해 줘."**\n2. 한 번에 한 장, 다음은 "next". **7장.** 대화가 길어져 얼굴이 흔들리면 새 대화에서 남은 컷부터 다시 시작한다(시트 다시 올림).\n3. 파일 이름 그대로 Claude에게 넘긴다.\n4. 가운 · 수건 · 가리는 포즈가 나오면: **"Read the cut text and level/ again. Same pose, no cover-ups, exactly the wardrobe written."**\n5. 포즈가 앞 컷과 비슷하면: **"Do NOT reuse any earlier pose or camera angle. Follow the cut text exactly."**\n\n| 컷 | 파일 | 내용 | 게임 |\n|---|---|---|---|\n' % (d['ko'])
    for k, n, g in rows:
        t += u'| %s | `r_C-%s_%s` | %s | %s |\n' % (k, a, k, n, g)
    t += u'\n---\n\n' + COMMON
    t += u'## THIS AGENT\n\n- **%s** (`agents/sheet_%s.jpg`), signature colour **%s**. Follow her sheet and AGENTS.md exactly.\n- Stage costume: %s\n- Lingerie: %s\n\n**Who she is to the viewer.** %s\n\n**The venue.** %s Cuts 0 and 1 are in the main venue; cuts 2 and 3 in the back room.\n\n## THE SEVEN CUTS\n\n' % (a.upper(), a, d['col'], d['cos'], d['lin'], d['who'], d['ven'])
    cuts = [('0', 'POSE', d['c0']), ('1', 'ACTION', d['c1']), ('2', 'TEASE', d['c2']), ('3', 'PEAK', d['c3']), ('3_1', 'STUDIO', d['st'])]
    for f, txt in d['x']:
        cuts.append(('3_%d' % (len(cuts) - 3), f, u'*Format: %s.*\n\n%s' % (FMT[f], txt)))
    for k, nm, c in cuts:
        t += u'### CUT %s — `r_C-%s_%s` — %s\n\n%s\n\n' % (k, a, k, nm, c)
    return t


def main(repo, out):
    os.makedirs(out, exist_ok=True)
    cso = os.path.join(repo, 'tools', 'charsheet', 'out'); pub = os.path.join(repo, 'public')
    for a in ORDER:
        zn = 'SILENT6_Reward_Costume_V5_%s' % a.upper(); text = md(a, cso)
        io.open(os.path.join(out, u'Costume_V5_%s_지시.md' % a), 'w', encoding='utf8').write(text)
        z = zipfile.ZipFile(os.path.join(out, zn + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        z.writestr(zn + u'/지시.md', text)
        z.write(os.path.join(cso, 'AGENTS.md'), zn + '/AGENTS.md')
        z.write(os.path.join(cso, 'sheet_%s.jpg' % a), '%s/agents/sheet_%s.jpg' % (zn, a))
        k = 0
        for m in LV[a]:
            f = os.path.join(pub, 'gn', '%s_%02d.jpg' % (a, m))
            if os.path.exists(f):
                k += 1; buf = io.BytesIO(); Image.open(f).convert('RGB').resize((768, 1152), Image.LANCZOS).save(buf, 'JPEG', quality=86)
                z.writestr('%s/level/level_%d.jpg' % (zn, k), buf.getvalue())
        z.close(); print(zn, os.path.getsize(os.path.join(out, zn + '.zip')) // 1024, 'KB', 'level', k)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
