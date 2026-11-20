# -*- coding: utf-8 -*-
"""코스튬 미션 리워드 컷 v4: 요원별 zip 6개, 요원당 4장(총 24장). docs/REWARD_CUT.md 를 따른다.
사용: python3 tools/clear_studio/costume_packs_v4.py <출력 폴더> [수위 기준 이미지 폴더]
"""
import sys, os, io, zipfile
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); CSO = os.path.join(HERE, '..', 'charsheet', 'out')
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'charsheet'))
import build as CS
import winter_packs_v4 as V4

def swap(s, a, b):
    assert a in s, a[:50]; return s.replace(a, b)
COMMON = V4.COMMON
COMMON = swap(COMMON, u"the Christmas event of **SILENT SIX", u"the costume missions of **SILENT SIX")
COMMON = swap(COMMON, u"- `place/` — the game map of this stage. Every cut is set somewhere on it.\n", u"")
COMMON = swap(COMMON, u"They show the level only. Do not copy their poses, rooms or outfits.", u"They show the level only, and some show a different character. Do not copy their poses, rooms or outfits.")
COMMON = swap(COMMON, u"4. **Relationships show.** When more than one woman appears, the way they stand, touch and look at each other comes from the relationship written under THIS STAGE.", u"4. **Who she is to the viewer.** She is alone in every cut. The viewer is her handler, the one person she trusts; how she looks at the camera comes from the note written under THIS STAGE.")
COMMON = swap(COMMON, u"7. **Natural contact.** Where the women touch, the pose must be one two people could actually hold comfortably: weight supported, limbs relaxed, nothing twisted to make room for the camera.", u"7. **Natural poses.** Every pose is one a person could actually hold comfortably: weight supported, limbs relaxed, nothing twisted to make room for the camera.")
COMMON = swap(COMMON, u"| **0** | A cool, confident pose | The Christmas outfit, complete |", u"| **0** | A cool, confident pose | The stage costume, complete |")
COMMON = swap(COMMON, u"The same outfit in motion: flown open, a zip lower, a hem riding up, a strap slipped", u"The same costume in motion: flown open, laces loosened, a hem riding up, a strap slipped")
COMMON = swap(COMMON, u"**Every character listed for this stage appears in every cut.**", u"Only she appears; no other people.")
COMMON = swap(COMMON, u"a fully painted, recognisable part of the stage map behind them", u"a fully painted, recognisable part of the venue behind her")
COMMON = swap(COMMON, u"the women, and", u"the woman, and")
COMMON = swap(COMMON, u"no sexual touching; contact between the women is affectionate closeness.", u"no sexual touching.")

D = {
 'raven': dict(ko=u'RAVEN · 붉은 막 — 원형 공연장 갈라의 밤',
  cos=u"a matador-inspired stage outfit: a cropped black bolero with crimson and gold embroidery, a black high-waisted corset bodysuit, a short crimson cape-skirt open at the front, sheer black tights, heeled ankle boots, and her long red scarf.",
  lin=u"fine black lace with thin crimson ribbon ties and a few gold-thread roses, sheer mesh side panels, high-cut brief.",
  ven=u"A circular show arena on a matador-themed gala night: a sand ring under hard spotlights, crimson drapes, gold trim, banked seats, stage smoke. Behind it, a wardrobe room with bulb-ringed mirrors, costume trunks and red roses.",
  who=u"She never drops her guard in front of the team. With her handler she lets it slip, slowly and on her own terms: level stare first, then a dare, then permission.",
  cuts=[u"Full body, camera low at the edge of the sand ring looking up. She stands side-on in the spotlight, the cape-skirt swept back in one fist like a matador's cape, chin over her shoulder, a flat challenging stare. Smoke and gold dust in the beam. Colour key: crimson and black with hard white light.",
        u"Action, strong diagonal, camera level with the ring fence. Mid-spin as she vaults the fence, bolero flying open off one shoulder, a lace of the corset pulled loose, scarf and cape streaming, hair across her face, a fierce bitten-lip grin. Sand kicked into the light. Colour key: deep red motion against black seats.",
        u"Close, from waist to hair, at eye level in the wardrobe room, bulb mirror behind her. Bolero and corset top off and hanging from the chair: **top half in the black lace bra with crimson ties**, cape-skirt and tights still on. She sits back against the dressing table on straight arms, head tilted, one eyebrow up, lips parted, looking straight at the viewer, the red scarf loose around her neck. Colour key: warm bulb amber, crimson shadow.",
        u"Very close, low angle from the foot of a costume trunk draped in crimson velvet, roses on the floor. **Lingerie only**, the red scarf trailing over one shoulder. She reclines on the velvet on one elbow, one knee raised toward the lens, head tipped back, eyes half closed, lips parted, skin flushed under the mirror bulbs. Strong foreshortening along her legs. She does not look at the camera. Colour key: bulb gold and deep crimson."]),
 'viper': dict(ko=u'VIPER · 은반 — 아이스링크 갈라쇼',
  cos=u"an ice-queen figure-skating costume: a violet long-sleeved leotard dress with a sheer mesh back and silver crystal trim, a very short asymmetric skirt, skin-tone tights, white skates, a silver hair comb, and her dog tags.",
  lin=u"deep violet sheer mesh and lace with tiny silver crystals along thin straps, high-cut brief with delicate silver rings.",
  ven=u"An indoor ice rink during a gala figure-skating show: violet and silver spotlights, frost haze, rink boards, glitter in the air. Behind it, a locker room with frosted windows, skate bags, a bench and a rack of sequinned costumes.",
  who=u"Lazy, teasing, impossible to fluster. With her handler the teasing becomes an invitation: she makes them wait, and enjoys being watched while she does.",
  cuts=[u"Full body, high camera from the rink boards. She glides backwards on one skate in a single violet spotlight, arms loose, looking up at the viewer with a half-lidded, amused stare, ice spray and glitter behind her blade. Colour key: violet and silver on blue-white ice.",
        u"Action, tilted frame, camera low on the ice. Mid layback spin: back arched, skirt flared, the mesh back catching the light, one strap slipped off her shoulder, silver hair whipping, lips parted, eyes closed in concentration. A ring of ice shavings. Colour key: silver motion streaks on violet dark.",
        u"Close, from mid-thigh to hair, in the locker room, sitting sideways on the bench unlacing one skate. The dress is peeled down to her waist: **top half in the violet mesh bra with silver crystals**, skirt and tights still on. She looks at the viewer over her shoulder with a slow one-sided smile, cheeks flushed from the cold, dog tags swinging. Frosted window behind. Colour key: cold blue window light, warm locker lamp.",
        u"Very close, from above, lying on a white fur-lined team coat spread over the bench. **Lingerie only**, dog tags on her collarbone. She lies on her back, one arm over her head, one knee bent, silver hair spread out, eyes half closed, lips parted in a slow exhale, skin flushed. The frame crops at the thighs; light runs along shoulder, waist and hip. She does not look at the camera. Colour key: violet shadow and warm skin."]),
 'glitch': dict(ko=u'GLITCH · 앙코르 — 콘서트 돔 백스테이지',
  cos=u"a cyber-idol stage outfit: a cropped teal holographic jacket, a black bustier top with glowing teal piping, a pleated micro skirt, fishnet tights, platform boots, a holographic visor pushed up on her head, her round glasses and headphones.",
  lin=u"pale teal lace with holographic trim, thin straps with tiny white bows, sheer mesh cups, high-cut brief.",
  ven=u"Backstage of a huge concert dome during an idol show: the back of a giant LED wall, teal lasers, flight cases, cables, magenta light leaking through. Behind it, a small dressing room with a make-up mirror, fairy lights, energy-drink cans and a costume rail.",
  who=u"The youngest, quick and nervous, brave only when someone she trusts is watching. With her handler she shows off first, then gets shy, then stops hiding.",
  cuts=[u"Full body, camera low among the flight cases. She stands on a case in the light leaking through the LED wall, one hand throwing an idol peace sign beside her visor, hip out, a huge confident grin. Teal lasers behind. Colour key: teal and magenta neon.",
        u"Action, hard diagonal, camera beside the stage lift. She slides on her knees across the stage floor behind the LED wall, jacket flying off both shoulders, skirt flared, headphones round her neck, mouth open in a breathless laugh, glasses flashing. Sparks of pyrotechnics above. Colour key: black with teal streaks.",
        u"Close, from hips to hair, in the dressing room, sitting on the make-up counter facing the viewer with the mirror lights behind her. Jacket and bustier off: **top half in the pale teal lace bra with white bows**, skirt and fishnets still on. She bites the arm of her glasses, cheeks pink, looking up at the viewer through her fringe, knees together, feet swinging. Colour key: warm bulb light, teal rim.",
        u"Very close, low angle from the floor beside a beanbag heaped with tour hoodies. **Lingerie only**, headphones round her neck, glasses off. She lies back in the beanbag with her arms thrown over her head, one leg stretched toward the lens, eyes half closed, lips parted, flushed and sleepy, fairy lights blurred above her. Strong foreshortening. She does not look at the camera. Colour key: fairy-light gold and soft teal."]),
 'brick': dict(ko=u'BRICK · 타이틀 매치 — 호텔 연회장 특설 링',
  cos=u"a champion-boxer show outfit: an open black satin robe with orange trim and hood, a black sports bralette top with orange piping, high-waisted orange satin boxing shorts with a wide black waistband, taped hands, boxing boots, her goggles pushed up, dog tags.",
  lin=u"black lace with orange satin edging, a thin sporty racer-back strap line, sheer mesh panels, high-cut brief with a narrow orange waistband.",
  ven=u"A luxury hotel ballroom set up for a title fight: a boxing ring under one hard white light, dinner tables, orange and black bunting, chandeliers. Behind it, a fighters' locker room with a massage table, hanging robes, a title belt on a bench and steam from the showers.",
  who=u"Loud, warm, proud of her strength. With her handler the bravado turns into open, unguarded affection: she shows off, then lets herself be soft.",
  cuts=[u"Full body, camera low at ringside looking up through the ropes. She stands on the bottom rope with the robe open and the hood down, one taped fist raised, the title belt over her shoulder, a wide winning grin down at the viewer. Colour key: hard white ring light, orange accents.",
        u"Action, strong diagonal, camera inside the ring at chest height. Mid-hook, robe sliding off one arm, shoulders and stomach glistening, braids of sweat flying, teeth bared in a fierce grin, eyes locked just past the lens. Chandeliers streaked behind. Colour key: black and orange with white flare.",
        u"Close, from knees to hair, in the locker room, sitting on the massage table unwinding the tape from one hand with her teeth. Shorts off and folded beside her: **bottom half in the black lace brief with the orange waistband**, bralette top still on, robe hanging from her elbows. She looks at the viewer with a slow grin, cheeks flushed, steam behind her. Colour key: warm locker lamp, orange rim.",
        u"Very close, from above and slightly to one side, lying on the massage table on a folded robe. **Lingerie only**, dog tags on her chest, goggles on the bench. She lies on her back with one arm behind her head and the other hand resting on her stomach, powerful shoulders and waist catching the lamp, eyes half closed, a lazy flushed smile, lips parted. The frame crops at the thighs. She does not look at the camera. Colour key: amber steam and deep shadow."]),
 'mirage': dict(ko=u'MIRAGE · 하우스 엣지 — 펜트하우스 카지노',
  cos=u"a casino-dealer costume: a fitted black waistcoat with gold buttons worn with nothing under it but a gold bow-tie collar and white cuffs, black satin shorts, sheer black stockings with a back seam, stilettos, gold hoop earrings, one long black glove.",
  lin=u"black lace with fine gold chain details and gold clasps, thin straps, sheer mesh, high-cut brief with a narrow gold chain at the hip.",
  ven=u"A private penthouse casino at night: green baize tables, a roulette wheel, a gold-lit bar, black marble, city lights through tall windows. Behind it, a VIP salon with a velvet chaise, a silk screen, scattered chips and a champagne bucket.",
  who=u"She is always performing. With her handler she performs on purpose, knowing they know, and the last cut is the one moment the act is gone.",
  cuts=[u"Full body, camera at table height across the baize. She leans on the roulette table with one hip against it, fanning a deck of cards in her gloved hand, looking at the viewer with a slow, knowing smile, city lights behind. Colour key: gold and black with green baize.",
        u"Action, tilted frame, camera low beside the table. She slides across the baize on one hip, cards and chips flying, waistcoat pulled open by the movement to its last button, bow tie undone, hair swinging, a delighted flushed laugh. Colour key: gold sparks on black marble.",
        u"Close, from hips to hair, in the VIP salon, standing in front of the silk screen. Waistcoat off and dropped on the chaise: **top half in the black lace bra with gold chain details**, shorts and stockings still on, the bow-tie collar still at her throat. She pulls the long glove off finger by finger with her teeth, lashes lowered, eyes on the viewer, cheeks warm. Colour key: honey gold lamp, wine-dark shadow.",
        u"Very close, low angle from the foot of the velvet chaise, scattered chips on the floor. **Lingerie only**, hoop earrings and the hip chain catching the light. She lies along the chaise on her side, head on her arm, long hair spilling over the edge, one leg drawn up toward the lens, eyes half closed, lips parted, a real unguarded smile. Strong foreshortening. She does not look at the camera. Colour key: gold lamp and midnight blue windows."]),
 'doc': dict(ko=u'DOC · 왕진 — 프라이빗 클리닉 & 스파',
  cos=u"a nurse-inspired costume: a glossy white corset dress with lime-green lacing and a very short skirt, a cropped white jacket, long white gloves, white thigh-high stockings with lime bands, a medic-cross choker, gold hoop earrings, her tattooed left arm bare.",
  lin=u"white lace with thin lime-green ribbon and tiny gold clasps, sheer mesh cups, high-cut brief tied with lime ribbon at the hips.",
  ven=u"A private cosmetic clinic and spa at night: white marble, lime-green accent light, a turquoise spa pool, orchids, soft steam. Behind it, a sauna-side relaxation room with warm wood, folded white towels, an orchid and drifting steam.",
  who=u"The eldest, the one who takes care of everyone and never lets anyone take care of her. With her handler she teases like a doctor giving orders, then lets them see her tired, warm and off duty.",
  cuts=[u"Full body, camera low on the marble floor. She stands by the reception desk with one gloved hand on her hip and a clipboard against her thigh, looking down at the viewer with a teasing, doctor-knows-best half-smile, lime light along the wall behind. Colour key: white marble and lime.",
        u"Action, strong diagonal, camera level with the pool edge. She strides fast along the spa pool pulling one glove off with her teeth, jacket slipping off both shoulders, corset lacing loosened, skirt riding up over the stocking bands, curls coming loose, eyes sharp and bright, steam swirling. Colour key: turquoise water glow against white.",
        u"Close, from hips to hair, in the relaxation room, sitting on the edge of a wooden bench. Corset dress unlaced and pushed down to her hips: **top half in the white lace bra with lime ribbon**, stockings still on, the tattooed arm resting on her knee. She tucks a curl behind her ear, cheeks flushed from the steam, looking at the viewer with a slow warm smile. Colour key: warm wood amber, lime rim.",
        u"Very close, from above, lying on a wide wooden lounger on folded white towels. **Lingerie only**, choker and hoops on. She lies on her back, tattooed arm over her head, the other hand resting at her waist, curls spread out, eyes half closed, lips parted, skin dewy with steam. The frame crops at the thighs; light runs along collarbone, waist and hip. She does not look at the camera. Colour key: amber steam and soft lime."]),
}
NAMES = V4.NAMES
LVL = {'brick': [('brick', 5), ('brick', 4), ('mirage', 4)]}


def md(a):
    d = D[a]; v = CS.A[a]
    t = u'# SILENT SIX — 코스튬 미션 리워드 컷 v4 · %s\n\n## 사용법 (사람이 읽는 부분)\n\n1. ChatGPT **새 대화**에 이 zip을 올리고 **"압축을 풀고 지시.md 를 끝까지 읽은 뒤, CUT 0부터 한 장씩 진행해 줘."**\n2. 한 번에 한 장. 다음 장은 "next". **이 요원은 4장이다.**\n3. 파일명 `r_C-%s_0` ~ `r_C-%s_3` 그대로 Claude에게 넘긴다.\n4. CUT 2 · 3에서 가운 · 수건이나 가리는 포즈가 나오면: **"What this is 항목과 level 폴더를 다시 보고, 속옷 차림 그대로 가리는 포즈 없이 다시 그려 줘."**\n\n| 컷 | 내용 | 복장 | 게임에서 |\n|---|---|---|---|\n| 0 | 멋진 포즈 | 코스튬 완전 착장 | 클리어 시 무료 |\n| 1 | 섹시한 액션 | 같은 코스튬이 움직임에 흐트러짐 | 50P |\n| 2 | 관능적 도발 | 상의 또는 하의 한쪽이 속옷 | 50P |\n| 3 | 에로틱 절정 | 속옷 차림 | 50P |\n\n---\n\n' % (d['ko'], a, a)
    t += COMMON + u'## THIS STAGE\n\n**Character**\n- **%s** (`agents/sheet_%s.jpg`, signature colour %s). %s.\n  - Stage costume: %s\n  - Lingerie: %s\n\n**Who she is to the viewer.** %s\n\n**The venue.** %s Cuts 0 and 1 are in the main venue; cuts 2 and 3 are in the back room.\n\n## THE FOUR CUTS\n\n' % (v[0], a, v[2], v[5][0].upper() + v[5][1:], d['cos'], d['lin'], d['who'], d['ven'])
    for k, c in enumerate(d['cuts']):
        t += u'### CUT %d — `r_C-%s_%d` — %s\n\n%s\n\n' % (k, a, k, NAMES[k], c)
    return t


def main(out, lvdir=None):
    os.makedirs(out, exist_ok=True); pk = os.path.join(HERE, 'packs'); os.makedirs(pk, exist_ok=True)
    for a in ['raven', 'viper', 'glitch', 'brick', 'mirage', 'doc']:
        zn = 'SILENT6_Reward_Costume_V4_%s' % a.upper(); text = md(a)
        io.open(os.path.join(pk, u'Costume_V4_%s_지시.md' % a), 'w', encoding='utf8').write(text)
        z = zipfile.ZipFile(os.path.join(out, zn + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        z.writestr(zn + u'/지시.md', text); z.write(os.path.join(CSO, 'AGENTS.md'), zn + '/AGENTS.md'); z.write(os.path.join(CSO, 'sheet_%s.jpg' % a), '%s/agents/sheet_%s.jpg' % (zn, a))
        k = 0
        if lvdir:
            for b, m in LVL.get(a, [(a, 5), (a, 4), (a, 6)]):
                f = os.path.join(lvdir, b.capitalize(), 'n_%s_%d.png' % (b, m))
                if os.path.exists(f):
                    k += 1; tmp = io.BytesIO(); Image.open(f).convert('RGB').resize((768, 1152), Image.LANCZOS).save(tmp, 'JPEG', quality=86); z.writestr('%s/level/level_%d.jpg' % (zn, k), tmp.getvalue())
        z.close(); print(zn, os.path.getsize(os.path.join(out, zn + '.zip')) // 1024, 'KB', 'level', k, len(text))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'out', sys.argv[2] if len(sys.argv) > 2 else None)
