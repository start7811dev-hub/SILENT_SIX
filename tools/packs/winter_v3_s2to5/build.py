# -*- coding: utf-8 -*-
"""블러디 크리스마스 v3 · 2~5판 제작 묶음. 사용: python3 tools/packs/winter_v3_s2to5/build.py <출력 폴더>"""
import io, os, sys, zipfile
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..', '..', '..'); PUB = os.path.join(ROOT, 'public'); CS = os.path.join(ROOT, 'tools', 'charsheet', 'out')

MAPRULES = u'''## INSTRUCTIONS FOR THE IMAGE MODEL

You are painting one game-map background for a real-time stealth tactics game. `ref/look_stage1.jpg` is a finished map from the same game. **Copy its look exactly**: canvas, camera angle, scale, painterly finish, snow, warm practical lights against cool night ambience, black surround. **Do not copy its layout.** The layout below is a level design and every placement in it matters for gameplay.

Make **one image**. Output file name: `%(file)s`. Do not ask questions.

### Canvas, camera, scale
- Exactly **1536x1024**, landscape. One plain diamond-shaped plan filling the frame, 2:1 isometric, same camera as the reference. Outside the diamond: flat near-black `#06080b`.
- The plan is **30 x 30 metres**, drawn at the same scale as the reference: a person would be about 30 px tall.
- %(time)s

### Words used below
Corners of the diamond: **TOP** (far), **BOTTOM** (near), **LEFT**, **RIGHT**.
Perimeter sides: **upper-left side** (TOP to LEFT), **upper-right side** (TOP to RIGHT), **lower-left side** (LEFT to BOTTOM), **lower-right side** (RIGHT to BOTTOM).
"Parallel to a side" means running along that side's isometric axis.

### Rules that apply to every map in this set
1. Everything solid is straight and runs along the two isometric axes. No diagonal walls.
2. **The two near sides (lower-left and lower-right) are closed by a thin, low boundary only about 1 m high** (%(nearwall)s), so that the ground just inside them stays fully visible. Only the two far sides may be tall.
3. %(rule3)s
4. Every structure is **single-storey and low**, so the lanes behind it stay visible. Buildings that can be entered have the roof removed and walls cut at one height with a flat dark top.
5. Walkable ground is calm, even and clearly readable, slightly brighter than the structures on it. No lane dead-ends unless stated.
6. **No loose objects anywhere**: no crates, barrels, drums, sacks, pallets, vehicles, carts, benches, small trees, signs, barriers, people or animals. They are added later as separate sprites. Fixed lamps on walls or posts are fine.
7. No text, numbers, logos, UI, grid lines, arrows, labels or watermark.
'''

PROPRULES = u'''## INSTRUCTIONS FOR THE IMAGE MODEL

You are painting **separate object sprites** that will be placed on top of the map `%(map)s` (if that map is not in this conversation, use `ref/look_stage1.jpg`). They must look cut out of that painting: **same 2:1 isometric camera, same painterly finish, same snow, same lighting**. `ref/sprite_sheet_example.png` is a finished sheet from stage 1: follow its format exactly.

Make **%(n)d sheets, one image per reply**. Write the output file name on its own line before the image. After each sheet, stop and wait for "next". Do not ask questions.

### Rules for every sheet
1. Exactly **1536x1024**. An invisible grid of **3 columns x 2 rows**, each cell 512x512. **One object per cell, centred**, with clear margin on all sides. Objects never touch a neighbouring cell.
2. Background: flat pure magenta `#FF00FF` everywhere behind the objects (or true transparency).
3. **No ground, no floor tile, no cast shadow, no glow spilling onto the background.** Only the object.
4. Same camera for every object: 2:1 isometric from above, as on the map. Every object stands on an invisible rectangular footprint aligned to the two isometric axes.
5. "Orientation 1" = long side running toward the lower-right. "Orientation 2" = the same object with its long side running toward the lower-left.
6. Keep relative scale between cells of one sheet honest. A thin cap of snow on top surfaces where it makes sense.
7. No text, digits, logos, labels, cell borders or watermark.%(extra)s
'''

PORTRULES = u'''Format for dialogue portraits: vertical 2:3, **1024x1536**, flat pure green `#00FF00` background (or true transparency) with no shadow on it. One figure framed from mid-thigh up, large in the frame. No background objects, no text. Art style of `ref/style_cast.jpg`: semi-realistic anime illustration, painterly high-end finish. One image per reply, file name on its own line first, then wait for "next".
'''

def lines(tbl):
    return u'| # | 누가 | 대사 |\n|---|---|---|\n' + u'\n'.join(u'| %d | %s | %s |' % (i + 1, a, b) for i, (a, b) in enumerate(tbl)) + u'\n'

S = {}
# ------------------------------------------------------------------ 2판
S[2] = dict(name=u'화차 44호', place=u'화물 조차장', squad=u'브릭 + 글리치', file='bgw2_v3.jpg', time=u'Night, 20:10. Light snow. Sodium yard lamps, long shadows, steam from a distant engine.',
 nearwall=u'a chain-link fence on a low concrete kerb',
 check=[u'선로 5줄이 왼쪽 아래 변과 나란하다.', u'화차는 선로 A · B · D에만 3량씩 있고, C와 E는 **빈 선로**다.', u'화차 사이 틈이 줄마다 2곳, 줄끼리 어긋나 있다.', u'왼쪽 위 변을 따라 작업 구역이 있고 조명탑 · 신호소 · 사무소가 순서대로 있다.', u'선로를 가로지르는 건널목이 작업 구역 바로 옆에 있다.', u'오른쪽 위 변 앞은 낮은 하역 승강장이다.', u'바닥에 낱개 물건이 없다.'],
 layout=u'''### The place
A freight marshalling yard: five parallel sidings, a service strip at their dead end, a loading platform on the far side.

### Layout
**Tracks.** Five straight railway tracks, **all parallel to the lower-left side**, evenly spaced, each on a 2.5 m wide ballast bed with a **2.5 m gravel lane between neighbouring tracks**. Name them from near to far: **track A** (closest to the lower-left side), **B**, **C**, **D**, **E** (closest to the upper-right side). All five run out through openings in the fence on the lower-right side. At the other end they stop at buffer stops, 7 m short of the upper-left side.

**Freight cars painted into the map.** Only on tracks **A, B and D**: on each of these, **three box cars in a row, each about 7 m long, with a clear 2 m gap between cars**. The gaps of track A, track B and track D are **not lined up with each other**. The cars are tall and solid: they block sight and movement.

**Tracks C and E are completely empty rails** from end to end. (Their cars are separate sprites.)

**Level crossing.** Right at the buffer-stop end, one timber plank crossing, 2.5 m wide, runs straight across all five tracks, parallel to the upper-left side.

**Service strip.** The 7 m deep strip between the buffer stops and the upper-left side. Along it, from the TOP end to the LEFT end:
- near TOP: a steel lattice **lighting tower** on a 2 x 2 m concrete base;
- in the middle: the **signal box**, a 4 x 4 m brick cabin, roof removed, with a row of big levers inside and one door facing the tracks;
- near LEFT: the **yard office**, a 4 x 5 m timber hut, roof removed, with a desk and shelves and one door facing the signal box.
There is a 2 m passage between each of these and its neighbour, and a 2.5 m lane behind them along the upper-left side.

**Loading platform.** Between track E and the upper-right side: a low concrete platform, 3 m deep, running the full length, with two short ramps down to the gravel. Behind it the upper-right side is a long warehouse wall with closed roller doors.

**Second lighting tower.** A second lattice tower on a 2 x 2 m base at the RIGHT corner, beside the end of the platform.

**Way in.** A pedestrian gate in the fence on the lower-left side, about a quarter of the way from the LEFT corner, open, with a floor hazard stripe across it.
''',
 props=[('cars', u'화차 · 기관차 (움직이는 줄)', u'''All in **orientation 1**, each about 7 m long, 2.5 m wide and 3 m tall, each filling about 90%% of its cell's width. They must match the box cars painted on the map.
1. A box car, rust red.
2. A box car, dark green.
3. A tank car, dull grey.
4. A flat car carrying a load under a tied tarpaulin.
5. **The target car**: a box car, dark blue, with one broad yellow diagonal band across its side and a red wax seal on the door latch. No digits.
6. A small diesel shunting locomotive, yellow and black, headlamp lit.'''),
  ('low', u'낮은 엄폐 (1×1 m)', u'''Waist-high, footprint 1 x 1 m.
1. Two stacked wooden crates.
2. Two oil drums side by side.
3. A wooden cable reel lying on its side.
4. A pile of sandbags.
5. A wheeled toolbox trolley.
6. A short stack of railway sleepers.'''),
  ('tall', u'높은 엄폐 (시야 차단)', u'''Taller than a person.
1. A grey steel relay cabinet with vents, 1 x 1 m, 2.2 m high.
2. A pallet of sacks under a tied tarpaulin, 2 x 2 m, 2.2 m high.
3. A bank of shovelled snow, 1 x 2 m, 2 m high, orientation 1.
4. A forklift truck, forks down, orientation 1.
5. The same forklift, orientation 2.
6. A cast-iron water crane (the column used to fill steam engines), 1 x 1 m, 3 m high.'''),
  ('special', u'목표 · 전환용', u'''1. A hand-thrown track switch lever on a small base plate, 1 x 1 m.
2. A block of plastic explosive with a blinking red light and a short wire, drawn large.
3. A red railway signal lamp on a short post, lit.
4. A portable steel barrier with red-and-white tape, 1 x 3 m, orientation 1.
5. The same barrier, orientation 2.
6. One gift box, dark green with a silver ribbon, glowing slightly: the mission objective.''')],
 illus=None,
 play=u'''- 중간 목표(순서 자유): ① 신호소에서 선로 전환기를 돌린다. C줄 화차가 한 칸 밀려 틈의 위치가 바뀐다 ② 사무소의 화물 대장을 확인한다. E줄 3량 중 어느 것이 44호인지 드러난다.
- 본 목표: 44호 문에 폭약을 붙여 상자를 꺼낸다.
- 3막: 폭약이 터지면 3분 타이머. 기관차가 E줄을 끌고 나가 왔던 틈이 닫힌다. 브릭이 화차 벽을 뚫어 새 길을 낸다.
- 조명탑 2기는 글리치가 해킹하면 25초 꺼진다.''',
 dlg=[(u'① 시작 전 — 브리핑', [(u'지휘관', u'20시 10분, 화물 조차장이다. 카드에 적힌 그대로야. 화차 44호에 두 번째 상자가 실려 있다.'), (u'브릭', u'화차가 몇 량인데? 하나하나 다 열어 볼 수는 없잖아.'), (u'글리치', u'사무소에 화물 대장이 있을 거야. 그거 보면 44호가 어느 줄인지 바로 나와. 아, 근데 조명탑이 두 개나 있네… 저건 내가 끌게.'), (u'브릭', u'좋아. 그럼 넌 불 끄고, 난 문 딴다. 간단하네!'), (u'글리치', u'언니 "딴다"가 폭약인 거, 나만 불안해?'), (u'브릭', u'걱정 마. 노크는 딱 한 번만 할게.')]),
  (u'② 중간 목표 1개 완료 — 산타의 무전', [(u'산타', u'브릭이 먼저 담을 넘고, 글리치는 신호소부터 찾았겠지? 맞지?'), (u'글리치', u'어… 어떻게 알았어?! 지금 우리 보고 있어?'), (u'산타', u'볼 필요가 없어. 너희는 늘 그 순서로 움직이니까.'), (u'브릭', u'야, 너 누구야. 얼굴 좀 보고 얘기하자.'), (u'산타', u'얼굴은 선물 다 받고 나서. 착하게 굴어야지?')]),
  (u'③ 폭약 설치 직후 — 판이 바뀐다', [(u'산타', u'어머, 정말 터뜨렸네. 그럼 3분 줄게. 기차는 시간 맞춰 떠나거든.'), (u'글리치', u'브릭! 기관차가 움직여! 우리가 들어온 틈이 막히고 있어!'), (u'브릭', u'막히면 뚫으면 되지! 뒤로 붙어!')]),
  (u'④ 클리어', [(u'글리치', u'잠깐만… 마켓에서 나온 종이랑 이 상자 걸 합치니까 풀려. 이거 암호가 아니라 사번이야.'), (u'브릭', u'사번? 누구 건데.'), (u'글리치', u'…우리 거. 6과 사번이야. 언니 것도 있어.'), (u'브릭', u'뭐? 지난번에 팔린 명단은 절반이라며.'), (u'글리치', u'응. 이게 나머지 절반이야. 그리고 대장에 다음 배송지가 적혀 있어. 22시 30분, 호수 보트하우스.')])],
 extra=u'클리어 화면 두 줄: 두 번째 상자를 확보했다. / 상자의 숫자는 제6과 명단의 나머지 절반이다.')
# ------------------------------------------------------------------ 3판
S[3] = dict(name=u'얼음 위의 선물', place=u'얼어붙은 호수', squad=u'바이퍼 + 닥', file='bgw3_v3.jpg', time=u'Night, 22:30. Clear and bitterly cold between snow squalls. Moonlit blue ice, a few warm lamps on the shore buildings.',
 nearwall=u'a low split-rail fence half buried in snow',
 check=[u'가운데가 네모난 얼음판이고 **아무것도 없다**.', u'얼음 둘레로 호숫가 띠가 사방에 있고 한쪽이 비어 있지 않다.', u'TOP에 보트하우스(지붕 없음, 문 2개), RIGHT에 부두 · 무전실 · 안테나.', u'LEFT에 관리인 오두막과 장작 창고.', u'호숫가 띠에 바깥 오솔길과 물가 길이 둘 다 있다.', u'변마다 덩어리 2개씩, 사이에 샛길.', u'바닥에 낱개 물건이 없다.'],
 layout=u'''### The place
A small frozen lake in the woods, ringed by a strip of shore with a few buildings and clumps of trees.

### Layout
**The ice.** The centre of the plan is a **square sheet of ice, about 16 x 16 m**, its edges parallel to the sides of the map. It is flat, pale blue-white, with a few long cracks, and **completely empty**. (Fishing huts are separate sprites.) The ice is walkable.

**The shore band.** All around the ice, between it and the perimeter, a band of snowy ground about 6 m deep. In this band there are two paths that both go all the way around the lake:
- the **outer trail**, 2.5 m wide, along the perimeter;
- the **waterline path**, 2 m wide, right along the edge of the ice.
Between the two paths sit the solid blocks listed below, with **2 m cut-through paths between neighbouring blocks**.

**Corner blocks**
- **TOP corner: the boathouse.** A 6 x 5 m timber boathouse, roof removed, walls cut at one height. Inside: a slipway and one narrow bunk against the back wall. **Two doors**: a wide one facing the ice and a small side door facing the upper-left side.
- **RIGHT corner: the dock.** A timber jetty about 2.5 m wide projecting 5 m out onto the ice; at its landward end a small **radio shack** (3 x 3 m, solid, roofed) with a **tall thin antenna mast** beside it, and a **searchlight on a post** aimed at the ice.
- **LEFT corner: the ranger's cabin.** A solid 5 x 4 m log cabin with lit windows, and next to it a 3 x 2 m open-fronted woodshed.
- **BOTTOM corner: the trailhead.** A cleared patch of packed snow. The way in is a gap in the fence on the lower-left side near the BOTTOM corner, with a floor hazard stripe.

**Side blocks** (two on each of the four sides, each about 4 x 3 m, with a cut-through between them)
- Upper-left side: a dense clump of pines (solid, treated as one block) and a rocky outcrop.
- Upper-right side: a smokehouse hut (solid) and a dense clump of pines.
- Lower-left side: a boat-rack shed (solid, low) and a rocky outcrop.
- Lower-right side: a dense clump of pines and a net-drying shed (solid, low).

The far two sides of the perimeter are a wall of dark forest. Keep every tree clump low and compact so the paths behind stay visible.
''',
 props=[('ice', u'얼음 위 큰 물건', u'''1. An ice-fishing hut, red-painted plywood, door ajar, 2 x 2 m, 2.2 m high.
2. An ice-fishing hut, weathered blue, stovepipe smoking faintly, 2 x 2 m.
3. An ice-fishing hut, bare grey timber, 2 x 2 m.
4. A snowmobile, orientation 1.
5. The same snowmobile, orientation 2.
6. An overturned wooden rowboat, 1 x 3 m, orientation 1.'''),
  ('low', u'낮은 엄폐 (1×1 m)', u'''Waist-high, footprint 1 x 1 m.
1. A fishing hole in a block of ice with a stool and a small canvas windbreak.
2. A hand sled loaded with gear.
3. A neat pile of split logs.
4. A steel drum brazier with a low fire.
5. Stacked wooden fish crates.
6. A broad snow-covered tree stump with an axe in it.'''),
  ('tall', u'높은 엄폐 (시야 차단)', u'''Taller than a person.
1. A compact clump of three young pines, 2 x 2 m, 3 m high.
2. A granite boulder, 2 x 2 m, 2 m high.
3. A wind-packed snow drift, 1 x 2 m, 2 m high, orientation 1.
4. The same drift, orientation 2.
5. A rack of three canoes stored on edge, 1 x 3 m, 2 m high, orientation 1.
6. A stack of lobster-pot style fish traps, 1 x 1 m, 2 m high.'''),
  ('special', u'목표 · 전환용', u'''1. **The witness**, as a small figure for the map: a man in his late forties in an orange work parka, one arm held against his side, standing hunched, seen from the map camera (slightly from above), full body, drawn large (about 420 px tall), facing lower-left.
2. A red first-aid field bag with a white cross patch, drawn large.
3. A thin steel radio antenna mast with guy wires, 1 x 1 m, 5 m high.
4. A searchlight on a short post, lit.
5. A portable barrier of crossed poles and rope, 1 x 3 m, orientation 1.
6. One gift box, pale ice-blue with a white ribbon, glowing slightly: the mission objective.''')],
 illus=(u'증인 대화용 2장', u'''`ref/style_cast.jpg` is only a style reference. Do not draw those women.

**The witness.** A man in his late forties, a delivery driver for a private logistics company: heavy build, tired face, short greying hair and stubble, a scuffed **orange work parka** over a grey company fleece, one side of the parka dark with a field dressing showing underneath. He **faces RIGHT** (toward the agent he is talking to).

- `d_W3_witness_0.png` — slumped, one hand pressed to his bandaged side, eyes wide and frightened, breath visible.
- `d_W3_witness_1.png` — the same man, steadier after treatment, looking straight at the viewer, speaking urgently, one hand half raised.
'''),
 play=u'''- 중간 목표(순서 자유): ① 부두의 안테나를 바이퍼가 쏴서 끊는다. 그때부터 증원이 오지 않는다 ② 얼음 위 오두막 중 한 곳에서 닥이 구급 가방을 챙긴다.
- 본 목표: 보트하우스의 증인을 닥이 치료한다.
- 3막: 증인이 따라온다. 뛰지 못하고 눈에 잘 띈다. 돌아가는 길은 호위다.
- 눈보라: 26초마다 9초 동안 모두의 시야가 줄어든다. 얼음은 그때 건넌다.''',
 dlg=[(u'① 시작 전 — 브리핑', [(u'지휘관', u'22시 30분, 호수다. 산타의 상자를 직접 본 사람이 보트하우스에 갇혀 있다. 다쳤고, 오래 못 버틴다.'), (u'닥', u'다쳤다고? 그럼 얘기 끝났네. 내가 들어가서 걷게 만들어 올게.'), (u'바이퍼', u'얼음 위는 숨을 데가 없는데. 오두막 몇 채가 전부야. 건너다 걸리면 그대로 표적이지.'), (u'닥', u'그래서 네가 있는 거잖아. 부두 안테나부터 끊어 줘. 무전만 죽이면 사람이 더 안 와.'), (u'바이퍼', u'한 발이면 돼. …근데 닥, 구급 가방은?'), (u'닥', u'아, 그게 문제야. 급하게 나오느라 큰 가방을 못 챙겼어. 저 오두막 어딘가에 하나 있을 거야.')]),
  (u'② 중간 목표 1개 완료 — 산타의 무전', [(u'산타', u'그 사람은 왜 살리려고? 내 얘기가 그렇게 듣고 싶어?'), (u'바이퍼', u'어머, 목소리 좋네. 직접 와서 들려주지 그래?'), (u'산타', u'바이퍼구나. 넌 여전히 쏘기 전에 말이 많아.'), (u'바이퍼', u'…나 알아?'), (u'닥', u'바이퍼, 대꾸하지 마. 저 사람, 우리 의무 기록까지 읽은 말투야.')]),
  (u'③ 증인 치료 직후 — 판이 바뀐다', [(u'증인', u'그 여자… 헬리오스 사람이 아니야. 걷는 거, 숨는 거, 전부 당신들이랑 똑같았어.'), (u'닥', u'천천히 말해요. 우리랑 똑같다는 게 무슨 뜻이에요?'), (u'증인', u'6과. 그 여자가 자기 입으로 그랬어. "난 거기서 나왔다"고.'), (u'산타', u'입이 가벼운 사람은 오래 못 사는데. 조심히 데려가, 닥.')]),
  (u'④ 클리어', [(u'바이퍼', u'6과 출신이라… 그럼 우리 선배네. 인사라도 할 걸 그랬나.'), (u'닥', u'웃을 일이 아니야. 선배가 왜 헬리오스 물건을 나르고 있는 건데.'), (u'바이퍼', u'글쎄. 배신했거나, 배신한 척하거나. 둘 중 하나겠지.'), (u'닥', u'증인이 그러는데, 세 번째 상자는 벌써 떠났대. 자정 미사가 열리는 대성당으로.')])],
 extra=u'클리어 화면 두 줄: 증인을 데리고 나왔다. / 산타는 헬리오스 사람이 아니라 제6과 출신이다.')
# ------------------------------------------------------------------ 4판
S[4] = dict(name=u'자정 미사', place=u'대성당', squad=u'미라주 + 레이븐', file='bgw4_v3.jpg', time=u'Interior, midnight. Candlelight and a few hanging lamps, deep shadow in the aisles, cold moonlight through tall windows painted as light on the floor.',
 nearwall=u'the outer wall of the building cut down to a 1 m stub',
 rule3=u'This is an interior: there is no snow and no outdoor lane. **Every aisle, passage and doorway is at least 2.5 m wide and clearly open.**',
 check=[u'실내 맵이고 지붕이 없다. 벽은 한 높이로 잘려 있다.', u'왼쪽 아래 변 한가운데가 정문, 오른쪽 위 끝이 제단이다.', u'가운데 신도석 두 덩어리 사이에 중앙 통로가 있다.', u'신도석 양옆에 기둥 줄과 측랑이 있다.', u'왼쪽 위 변 쪽에 경당 3칸, 오른쪽 아래 변 쪽에 벽으로 막힌 납골당 통로(양 끝 입구).', u'제단 양옆에 제의실과 종지기 방이 있다.', u'바닥에 낱개 물건과 사람이 없다.'],
 layout=u'''### The place
The inside of a stone cathedral, seen with the roof removed. `ref/look_indoor.jpg` shows how interiors are drawn in this game: thin walls cut at one height with a flat dark top, clear floors, open doorways. Use it for wall construction; use `ref/look_stage1.jpg` for finish and scale.

### Layout
The building's long axis runs **from the lower-left side (entrance) to the upper-right side (altar)**. Describe it as five strips running that way, side by side. From the upper-left side to the lower-right side they are:

1. **Chapel strip**, 4 m wide: three side chapels in a row, separated from each other by walls, each fully open toward strip 2.
2. **Left aisle**, 3 m wide, clear floor.
3. **Nave**, 9 m wide: bounded on each side by a **row of five square stone columns** (columns are cut at wall height). Between the columns and the centre: **two blocks of wooden pews**, eight rows each, all facing the altar, with a **3 m centre aisle** between the two blocks. The pews are empty.
4. **Right aisle**, 3 m wide, clear floor.
5. **Crypt passage**, 3 m wide: separated from the right aisle by a **solid wall** for its whole length, darker and lower, lined with stone tomb niches. It has **only two openings**: an arched doorway at each end.

Across those strips, from the entrance to the altar:
- **Narthex** (entrance hall), 4 m deep, across the full width at the lower-left end, divided from the rest by a wall with **three doorways**: a wide one into the centre aisle and one into each side aisle. The main door, in the middle of the lower-left side, is the way in: paint a floor hazard stripe on its threshold.
- **Nave and aisles**, 16 m deep, as described above. In the left aisle, against the chapel strip, one **confessional booth** (a solid wooden box 2 x 1.5 m).
- **Sanctuary**, 6 m deep, at the upper-right end, raised by two steps. In its centre the **altar**. Beside the altar, on the side toward the right aisle, an **ornate offering chest on a stand**: the most eye-catching object on the map. Choir stalls (low wooden benches) on both sides of the sanctuary.
- At the upper-right end of the chapel strip: the **sacristy**, a closed room with one door into the sanctuary.
- At the upper-right end of the crypt passage: the **bell-ringer's room**, a small room with a thick bell rope hanging down in its centre and one door into the sanctuary.

Every doorway mentioned is visibly open. Do not paint any other rooms.
''',
 props=[('low', u'낮은 엄폐 (1×1 m)', u'''Waist-high, footprint 1 x 1 m.
1. A wooden kneeler bench.
2. A cluster of three floor candle stands with lit candles.
3. A stand of red poinsettias in a brass pot.
4. A small draped offering table with a brass plate.
5. A stack of folded wooden chairs.
6. A carved stone font with a wooden cover.'''),
  ('tall', u'높은 엄폐 (시야 차단)', u'''Taller than a person.
1. A stone saint statue on a plinth, 1 x 1 m, 2.5 m high.
2. A decorated Christmas tree with candles, 1 x 1 m, 3 m high.
3. A steel scaffolding tower with planks and a dust sheet, 2 x 2 m, 3 m high.
4. A nativity scene in a wooden stable, 1 x 2 m, 2 m high, orientation 1.
5. A wooden confessional booth, 2 x 1.5 m, 2.3 m high, orientation 1.
6. A pipe-organ console with bench, 2 x 1 m, 2 m high, orientation 2.'''),
  ('people', u'신도 · 성가대 (3막에서 통로를 막는다)', u'''Small figures seen from the map camera (slightly from above), heavy winter coats and scarves, heads bowed or turned away, **no detailed faces**. Each group stands on the footprint given and fills most of its cell.
1. A row of four worshippers **sitting** in a pew, 1 x 3 m, orientation 1 (seen from behind-left).
2. A row of four worshippers sitting, 1 x 3 m, orientation 2.
3. A tight group of five people **standing** and shuffling, 2 x 2 m.
4. A different standing group of five, one carrying a child's coat, 2 x 2 m.
5. A row of four choir singers in white robes holding folders, 1 x 3 m, orientation 1.
6. Two ushers in dark suits standing side by side, 1 x 1 m.'''),
  ('special', u'목표 · 전환용', u'''1. An ornate wooden offering chest with brass bands on a stand, lid closed, 1 x 1 m.
2. A black leather money bag with a brass clasp, drawn large.
3. A second, identical-looking black bag with a small green light blinking at the seam, drawn large.
4. A ring of old iron keys, drawn large.
5. A rope barrier on two brass posts, 1 x 3 m, orientation 1.
6. The same rope barrier, orientation 2.''')],
 illus=(u'성가대 변장 미라주 1장', u'''Use `agents/AGENTS.md` and `agents/sheet_mirage.jpg`. Face and hair from `MIRAGE-A`.

- `d_W4_mirage_choir.png` — MIRAGE disguised as a cathedral choir singer: a long white choir robe over a black cassock with a high collar, a thin gold stole (her signature colour `#E8C46A`), hair pinned up neatly, a closed music folder held against her chest. A serene, perfectly innocent expression with the faintest knowing look in the eyes. She **faces LEFT**. No weapons.
'''),
 play=u'''- 중간 목표(순서 자유): ① 종지기 방에서 종 줄을 당겨 자정 종을 앞당긴다. 종이 울리는 9초 동안은 소리가 묻힌다. 언제 울릴지 플레이어가 정한다 ② 고해소 앞의 부제를 재워 헌금함 열쇠를 얻는다.
- 본 목표: 헌금함의 돈가방을 추적기가 든 가방으로 바꾼다.
- 3막: 미사가 끝나 신도들이 일어선다. 중앙 통로가 막힌다. 미라주는 군중에 섞여 정문으로, 레이븐은 납골당 통로로 나간다. 두 사람의 출구가 갈린다.
- 미라주는 성가대 복장으로 중앙 통로를 걸을 수 있다.''',
 dlg=[(u'① 시작 전 — 브리핑', [(u'지휘관', u'자정, 대성당이다. 세 번째는 상자가 아니라 돈가방이다. 제단 옆 헌금함에 들어 있다. 추적기가 든 가방으로 바꿔 놓고 나온다.'), (u'미라주', u'성가대 옷은 구해 놨어. 흰색이 나한테 이렇게 잘 받는 줄은 몰랐네.'), (u'레이븐', u'헌금함은 잠겨 있을 텐데. 열쇠는 누가 갖고 있지?'), (u'미라주', u'부제. 고해소 앞을 떠나질 않더라. 재우려면 소리가 좀 날 텐데, 미사 중이라 곤란해.'), (u'레이븐', u'종이 울릴 때 하면 되겠군. 종지기 방에 가서 내가 당긴다.'), (u'미라주', u'자정 종을 네 마음대로 치겠다고? 벌받을 거야, 레이븐.')]),
  (u'② 중간 목표 1개 완료 — 산타의 무전', [(u'산타', u'미사 중엔 조용히 해야지. 레이븐, 넌 예전에도 발소리가 컸어.'), (u'레이븐', u'…예전? 너, 나를 언제 봤는데.'), (u'산타', u'네가 스카프를 처음 감던 해부터.'), (u'미라주', u'레이븐, 얼굴 굳었어. 저 사람 누군지 알겠어?'), (u'레이븐', u'몰라. 근데 저쪽은 날 너무 잘 알아.')]),
  (u'③ 가방을 바꾼 직후 — 판이 바뀐다', [(u'미라주', u'잠깐, 가방 안에 송금 전표가 있어. 받는 쪽이… 헬리오스가 아니야. 개인 계좌야.'), (u'산타', u'쉿. 그건 못 본 걸로 해 줘. 나도 먹고살아야 하잖아?'), (u'레이븐', u'미사가 끝났어! 사람들이 일어난다. 미라주, 넌 섞여서 정문으로 나가. 난 아래로 돌게.')]),
  (u'④ 클리어', [(u'레이븐', u'헬리오스 돈까지 빼돌렸어. 우릴 팔고, 헬리오스도 속이고 있는 거야.'), (u'미라주', u'양쪽을 다 속이는 사람이라… 솔직히 좀 내 취향인데.'), (u'레이븐', u'농담할 기분 아니야.'), (u'미라주', u'알아. 그래서 하는 거야. …추적기가 멈췄어. 사설 비행장이야. 03시 30분에 뜨는 전용기가 한 대 있어.')])],
 extra=u'클리어 화면 두 줄: 가방을 바꿔 놓았다. / 산타는 헬리오스의 돈도 빼돌리고 있다.')
# ------------------------------------------------------------------ 5판
S[5] = dict(name=u'산타의 썰매', place=u'사설 비행장', squad=u'레이븐 + 바이퍼 + 글리치', file='bgw5_v3.jpg', time=u'Night, 03:30. Hard cold, blowing snow low over the concrete. Blue taxiway lights, white floodlights on the apron, warm light spilling from the hangar.',
 nearwall=u'a chain-link fence on a low concrete kerb',
 check=[u'왼쪽 아래 변 쪽에 컨테이너 덩어리 5개가 한 줄로 있고 사이에 골목이 있다.', u'가운데 계류장은 넓고 **비어 있다**.', u'오른쪽 위 변 쪽에 격납고(지붕 없음, 큰 문이 계류장 쪽, 안이 비어 있음).', u'LEFT에 관제탑, BOTTOM에 급수탑, RIGHT에 초소와 차량 문.', u'TOP 쪽에 울타리 친 연료 저장소.', u'왼쪽 위 변 한가운데가 유도로 출구로 뚫려 있다.', u'바닥에 낱개 물건과 비행기가 없다.'],
 layout=u'''### The place
A small private airfield: a container yard, an open apron and one hangar.

### Layout
Describe it as three strips, all **parallel to the lower-left side**. From the lower-left side to the upper-right side:

1. **Container yard**, 7 m deep. A single row of **five container blocks**, each about 4 x 3 m (two shipping containers side by side, single height, different faded colours), with a **2 m alley between neighbouring blocks**. A 2.5 m lane runs between the row and the fence on the lower-left side, and the row's other face opens onto the apron.
2. **Apron**, 11 m deep: an open concrete apron across the full width, with yellow painted taxi lines and a few floodlight poles standing only along its edges. **It is completely empty.** (Vehicles, cargo and the aircraft are separate sprites.)
3. **Hangar strip**, 9 m deep, along the upper-right side:
   - in the middle, the **hangar**: 16 m wide and 8 m deep, **roof removed**, walls cut at one height, the whole side facing the apron is one wide open doorway. **The hangar floor is empty**, polished concrete with a painted parking outline. One small side door at each end.
   - between the hangar and the TOP corner: a **fuel depot**, two horizontal tanks inside a chain-link fence, 5 x 5 m, with one gate.
   - between the hangar and the RIGHT corner: a **workshop annex**, a solid roofed block 5 x 5 m with closed shutters.
   A 2.5 m lane runs behind all three along the upper-right side.

Corners
- **LEFT corner: the control tower.** A solid 5 x 5 m base block, cut at the same height as the other buildings, with a flat roof carrying a small glazed cab and antennas, and one door facing the apron.
- **BOTTOM corner: a water tower.** A steel tank on four lattice legs, on a 3 x 3 m base, with a ladder.
- **RIGHT corner: a guard hut** (3 x 3 m, solid) beside a **vehicle gate** in the fence on the lower-right side, gate arm down.

Openings
- **The way in**: a cut in the fence on the lower-left side, a third of the way from the BOTTOM corner, with a floor hazard stripe.
- **The taxiway exit**: the **middle 10 m of the upper-left side is open**, with the taxi lines running out through it into the dark. This is where an aircraft would leave.
''',
 props=[('vehicles', u'차량 (계류장 엄폐)', u'''1. An airport fuel bowser truck, white with a red stripe, orientation 1.
2. The same fuel truck, orientation 2.
3. A snowplough truck with a wide front blade, orange, beacon lit, orientation 1.
4. The same snowplough, orientation 2.
5. A baggage tractor pulling two loaded carts, orientation 1.
6. A set of mobile boarding stairs on wheels, orientation 2.'''),
  ('low', u'낮은 엄폐 (1×1 m)', u'''Waist-high, footprint 1 x 1 m.
1. A cargo pallet of boxes under a net.
2. Two stacked aluminium flight cases.
3. Three fuel drums.
4. A cluster of traffic cones and wheel chocks.
5. A ground power unit cart with a coiled cable.
6. A de-icing fluid cart with a hose reel.'''),
  ('tall', u'높은 엄폐 (시야 차단)', u'''Taller than a person.
1. A single shipping container, dark blue, 2.5 x 6 m, orientation 1.
2. The same container in rust red, orientation 2.
3. A stack of large wooden crates under a tarpaulin, 2 x 2 m, 2.5 m high.
4. A ploughed bank of snow, 1 x 2 m, 2 m high, orientation 1.
5. A mobile floodlight tower on a trailer, mast raised, lit, 1 x 2 m.
6. A cargo belt loader, orientation 1.'''),
  ('special', u'비행기 · 목표 · 전환용', u'''1. **A private business jet**, twin rear engines, white with a single thin crimson line along the fuselage, no markings, seen from the map camera, **nose pointing lower-left**. It fills the whole cell. In game it is about 12 m long.
2. The same jet with the cabin door open and the stairs down, same angle.
3. An open aluminium cargo case; inside, one empty gift box with an untied red ribbon and a single folded card. Drawn large.
4. A red-and-white runway barrier, 1 x 3 m, orientation 1.
5. The same barrier, orientation 2.
6. One gift box, black with a crimson ribbon, glowing slightly: the mission objective.''')],
 illus=(u'엔딩 컷 2장', u'''These two are full illustrations, not portraits: vertical 2:3, **1024x1536**, full painted background, no text. Art style of `ref/style_cast.jpg`. Use `agents/AGENTS.md` with `agents/sheet_raven.jpg` for RAVEN and `agents/sheet_santa.jpg` for SANTA.

- `w5_end_a.jpg` — **The empty box.** Inside the jet's cargo hold, cold blue light. Close on an open aluminium case: an empty gift box with an untied crimson ribbon. RAVEN (tactical outfit, red scarf) is crouched over it, seen from the side, holding a small folded card up to her flashlight; the handwriting on it is only suggested, not readable. Her face, usually unreadable, has just changed: eyes slightly wide, lips parted. Snow blows in through the open hatch behind her.
- `w5_end_b.jpg` — **Hidden ending: the sleigh does not fly.** The snowy runway at night. A white business jet stopped nose to nose with an orange snowplough, its beacon turning. At the top of the jet's open stairs stands SANTA, hood down, long auburn hair blowing, crimson fur-trimmed coat, gloved hands resting on the rail, looking down at the viewer with a small, almost proud smile. In the foreground, out of focus, the back of RAVEN's head and the end of her red scarf. Fully dressed, no weapons raised.
'''),
 play=u'''- 세 명이 세 방향으로 갈라진다.
- 중간 목표(3개 중 2개): ① 글리치가 관제탑에서 이륙 허가를 늦춘다(제한 시간 +2분) ② 바이퍼가 급수탑에 올라 계류장을 내려다본다(탐조등 조작수를 쏠 수 있다) ③ 레이븐이 연료 저장소의 밸브를 잠근다(급유차가 멈춘다).
- 본 목표: 격납고 안 전용기의 화물칸을 연다.
- 3막: 화물칸은 비어 있다. 전용기가 유도로 쪽으로 움직이기 시작한다. 제설차로 유도로를 막으면 히든 엔딩, 그냥 빠져나와도 클리어.
- 제한 시간 5분.''',
 dlg=[(u'① 시작 전 — 브리핑', [(u'지휘관', u'03시 30분, 사설 비행장이다. 추적기가 여기서 멈췄다. 격납고의 전용기가 뜨기 전에 화물을 확보한다. 시간은 5분.'), (u'바이퍼', u'셋이나 보내다니, 오늘은 진심이네. 난 저 급수탑이 마음에 들어. 계류장이 한눈에 보이겠어.'), (u'글리치', u'난 관제탑! 이륙 허가만 꼬아 놓으면 2분은 더 벌 수 있어. …올라가는 길에 사람만 없으면.'), (u'레이븐', u'난 격납고로 간다. 연료 밸브도 가는 길에 잠글 수 있으면 잠그고.'), (u'바이퍼', u'레이븐, 아까 성당에서부터 말이 없네. 그 여자 때문이야?'), (u'레이븐', u'…끝나고 얘기해. 지금은 비행기부터 잡는다.')]),
  (u'② 중간 목표 1개 완료 — 산타의 무전', [(u'산타', u'셋이나 왔네? 이 정도면 영광인데.'), (u'글리치', u'으악, 또 들어왔어! 회선을 세 번이나 바꿨는데 어떻게…!'), (u'산타', u'글리치, 그 암호 체계는 내가 짠 거야. 넌 그 위에 색칠만 했고.'), (u'레이븐', u'그만해. 거기서 기다려. 직접 물어볼 게 있으니까.'), (u'산타', u'기다리는 건 내 일이 아니야, 레이븐. 그건 늘 네 일이었지.')]),
  (u'③ 화물칸을 연 직후 — 판이 바뀐다', [(u'레이븐', u'…비어 있어. 리본 묶은 빈 상자 하나, 카드 한 장. 그게 전부야.'), (u'산타', u'선물은 벌써 받았잖아. 오늘 밤 너희가 턴 다섯 곳. 그게 내 선물이야.'), (u'글리치', u'비행기가 움직여! 유도로로 나가고 있어!'), (u'바이퍼', u'레이븐, 정해. 막을 거야, 보낼 거야?')]),
  (u'④ 클리어', [(u'글리치', u'마켓, 조차장, 호수, 성당, 비행장… 잠깐, 이거 헬리오스 배달망 전부야. 하룻밤에 다 드러났어. 우리가 쫓아다닌 덕분에.'), (u'바이퍼', u'쫓은 게 아니라 끌려다닌 거네. 처음부터 끝까지.'), (u'레이븐', u'카드에 좌표가 있어. 다음에 만날 자리야. …그리고 이 글씨.'), (u'바이퍼', u'아는 글씨야?'), (u'레이븐', u'현장 수칙 초판. 6과에 처음 들어왔을 때 받은 그 수첩이랑 같은 손이야. 1기 리더.'), (u'레이븐', u'…메리 크리스마스, 선배.')])],
 extra=u'클리어 화면 두 줄: 화물칸은 비어 있었다. / 산타는 처음부터 제6과가 자기를 쫓게 만들었다.\n\n히든 엔딩(제설차로 유도로를 막았을 때): `w5_end_b.jpg`를 띄우고 한 줄 추가 — 산타: "잘 컸네. 다음엔 내가 찾아갈게."')

def build(out):
    os.makedirs(out, exist_ok=True)
    for n in (2, 3, 4, 5):
        d = S[n]; N = 'SILENT6_BloodyChristmas_V3_Stage%d' % n; F = {}
        pre = u'p_w%d' % n
        # 1 맵
        m = u'# 1 · 맵 — 블러디 크리스마스 %d판 "%s" (%s)\n\n## 사용법 (사람이 읽는 부분)\n\n- 결과 파일명: `%s` (1장)\n- 구조만 들어간다. 엄폐물 · 차량 · 사람은 `2_소품_지시.md`로 따로 뽑는다.\n- 검수 %d가지 (틀리면 그 부분만 다시 요청):\n' % (n, d['name'], d['place'], d['file'], len(d['check']))
        m += u''.join(u'  %d. %s\n' % (i + 1, c) for i, c in enumerate(d['check']))
        m += u'  %d. 가까운 두 변(왼쪽 아래 · 오른쪽 아래)의 경계가 낮고 얇아서 그 안쪽 바닥이 다 보인다.\n\n---\n\n' % (len(d['check']) + 1)
        d.setdefault('rule3', u'**A clear walkable lane at least 2.5 m wide runs along the inside of all four sides**, all the way around the map.')
        m += MAPRULES % d + u'\n' + d['layout'] + u'\n### Before you finish, check\nRe-read the layout and confirm every strip, block and opening is present, the near boundary is low, the lanes and passages are open, and the ground is clean.\n'
        F[u'1_맵_지시.md'] = m
        # 2 소품
        ps = d['props']
        p = u'# 2 · 소품 낱개 세트 — %d판 %s\n\n## 사용법 (사람이 읽는 부분)\n\n- 결과: 시트 %d장. 한 장에 6개씩 3×2 칸.\n- 맵 그림이 먼저 나온 뒤 **같은 대화에서** 이어서 진행한다.\n- 검수: 칸마다 1개, 배경이 한 가지 색, 물건끼리 닿지 않음, 맵과 같은 각도, 글자 없음.\n\n| 파일 | 내용 |\n|---|---|\n' % (n, d['place'], len(ps))
        p += u''.join(u'| `%s_%s.png` | %s |\n' % (pre, k, ko) for k, ko, _ in ps) + u'\n---\n\n'
        extra = u'\n8. Sheets that contain people: small figures only, adults in winter clothes, no detailed faces.' if any(k == 'people' for k, _, _ in ps) else u''
        p += PROPRULES % dict(map=d['file'], n=len(ps), extra=extra)
        for i, (k, ko, body) in enumerate(ps):
            p += u'\n### Sheet %d — `%s_%s.png`\nLeft to right, top row then bottom row.\n%s\n' % (i + 1, pre, k, body.replace('%%', '%'))
        F[u'2_소품_지시.md'] = p
        # 3 일러스트
        if d['illus']:
            t, body = d['illus']
            head = u'# 3 · 추가 일러스트 — %d판 (%s)\n\n## 사용법 (사람이 읽는 부분)\n\n- **새 대화**에서 진행한다. zip을 다시 올리고 "3_일러스트_지시.md 를 읽고 한 장씩."\n- 산타 대화용 5장과 요원 대화용 18장은 이미 따로 뽑았으므로 여기에는 없다.\n\n---\n\n## INSTRUCTIONS FOR THE IMAGE MODEL\n\n' % (n, t)
            F[u'3_일러스트_지시.md'] = head + (PORTRULES + u'\n' if n != 5 else u'One image per reply, file name on its own line first, then wait for "next". Do not ask questions.\n\n') + body
        # 4 연출
        q = u'# 4 · 연출과 대사 — %d판 "%s"\n\n그림 생성용이 아니다. 검토용이다. 고칠 줄은 "②-3"처럼 알려 주면 된다.\n\n## 판 정보\n\n- %s. %s.\n%s\n\n## 연출 4곳\n\n' % (n, d['name'], d['place'], d['squad'], d['play'])
        for t, tb in d['dlg']:
            q += u'### %s\n\n%s\n' % (t, lines(tb))
        q += d['extra'] + u'\n\n## 맵 안 연출\n\n- 판 시작 20초 동안 산타 실루엣이 갈 수 없는 높은 곳(%s)에 서 있다가 사라진다.\n' % {2: u'화차 지붕', 3: u'무전실 지붕', 4: u'제단 뒤 2층 창가', 5: u'격납고 문 위'}[n]
        F[u'4_연출과_대사.md'] = q
        # 읽어주세요
        r = u'# SILENT SIX — 블러디 크리스마스 v3 · %d판 "%s" 제작 묶음\n\n| 순서 | 파일 | 결과물 | 장수 |\n|---|---|---|---|\n| 1 | `1_맵_지시.md` | `%s` | 1 |\n| 2 | `2_소품_지시.md` | `%s_*.png` | %d (낱개 %d개) |\n' % (n, d['name'], d['file'], pre, len(ps), len(ps) * 6)
        if d['illus']: r += u'| 3 | `3_일러스트_지시.md` | %s | %d |\n' % (d['illus'][0], {3: 2, 4: 1, 5: 2}[n])
        r += u'| - | `4_연출과_대사.md` | 검토용. GPT에 시키지 않는다 | - |\n\n## ChatGPT에 보내는 방법\n\n1. 새 대화에 이 zip을 올리고 **"압축을 풀고 1_맵_지시.md 만 읽고 진행해 줘."**\n2. 맵을 검수한 뒤 같은 대화에서 **"이제 2_소품_지시.md 를 읽고 시트 1부터 한 장씩."** 다음 장은 "next".\n'
        if d['illus']: r += u'3. 일러스트는 **새 대화**에서. zip을 다시 올리고 **"3_일러스트_지시.md 를 읽고 한 장씩."**\n'
        r += u'\n한 대화에 지시 파일 하나씩만 읽힌다.\n\n## 1판에서 고친 점\n\n- 가까운 두 변의 경계를 낮고 얇게 지정했다. 1판은 가까운 벽이 바닥 두 줄을 가렸다.\n- 네 변 안쪽 골목 폭을 2.5 m 이상으로 지정했다. 1판은 먼 쪽 골목이 1칸 폭으로 나왔다.\n- 움직이거나 3막에 나타나는 것(화차 · 차량 · 비행기 · 신도 · 차단물)은 전부 낱개로 뽑는다.\n\n## 참고 이미지\n\n- `ref/look_stage1.jpg` 1판 완성 맵. 화풍 · 축척 기준.\n- `ref/sprite_sheet_example.png` 1판 소품 시트. 형식 기준.\n'
        if n == 4: r += u'- `ref/look_indoor.jpg` 실내 맵의 벽 표현 기준.\n'
        if d['illus']: r += u'- `ref/style_cast.jpg` 인물 화풍 기준.\n'
        F[u'읽어주세요.md'] = r
        z = zipfile.ZipFile(os.path.join(out, N + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        os.makedirs(os.path.join(HERE, 'stage%d' % n), exist_ok=True)
        for k, v in F.items():
            z.writestr(N + '/' + k, v); io.open(os.path.join(HERE, 'stage%d' % n, k), 'w', encoding='utf8').write(v)
        z.write(os.path.join(HERE, 'ref_look_stage1.jpg'), N + '/ref/look_stage1.jpg'); z.write(os.path.join(HERE, 'ref_sprite_sheet_example.png'), N + '/ref/sprite_sheet_example.png')
        if n == 4: z.write(os.path.join(PUB, 'bg5.jpg'), N + '/ref/look_indoor.jpg')
        if d['illus']:
            z.write(os.path.join(CS, 'sheet_all.jpg'), N + '/ref/style_cast.jpg')
            if n in (4, 5):
                z.write(os.path.join(CS, 'AGENTS.md'), N + '/agents/AGENTS.md')
                for a in {4: ['mirage'], 5: ['raven', 'santa']}[n]: z.write(os.path.join(CS, 'sheet_%s.jpg' % a), N + '/agents/sheet_%s.jpg' % a)
        z.close(); print(N, os.path.getsize(os.path.join(out, N + '.zip')) // 1024, 'KB', len(F), 'files')

if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else 'out')
