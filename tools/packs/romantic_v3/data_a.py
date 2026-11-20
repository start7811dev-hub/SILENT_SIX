# -*- coding: utf-8 -*-
# 로맨틱 미션 맵 제작 데이터 (레이븐 · 바이퍼 · 글리치). docs/ROMANTIC.md v2 를 따른다.
T = {}
T['raven'] = [
 dict(t=u'빈자리', place_ko=u'폭우 속 폐광촌', m=26, io='out', light=u"Night, heavy rain. Mud, deep puddles, one dim lamp on the office wall, a faint lightning glow in the clouds.",
  place=u"An abandoned mining village: three rows of ruined company houses with alleys between them, an ore shed, the mine office and the mine mouth.",
  lay=u'''**Company houses.** The near half of the map. **Three rows of ruined single-room houses, all rows parallel to the lower-left side.** Each row is four roofless brick shells, each 4 x 4 m, with a **2 m gap between shells**. A **2.5 m muddy alley** separates one row from the next. The gaps of the three rows are **not lined up**. Each shell has one doorway and is empty inside.

**Yard.** Beyond the third row, an open muddy yard 8 m deep running the full width, with one fixed steel **water tank on four legs** (2 x 2 m base) in its centre.

**Ore shed.** On the far side of the yard, toward the RIGHT corner: a long shed 6 x 12 m, parallel to the upper-right side, roof removed, two doorways on its yard side, an empty conveyor trestle fixed along its back wall.

**Mine office.** On the far side of the yard, toward the TOP corner: a 5 x 6 m brick office, roof removed, one doorway facing the yard, a small alcove in its far corner.

**Mine mouth.** In the middle of the upper-left side: a timber-framed tunnel mouth in the rock face, boarded shut, with rails running 6 m out of it and stopping.

**Edges.** The two far sides are a wet rock face. **Way in:** a gap in the fence on the lower-right side, close to the BOTTOM corner, with muddy tyre tracks.''',
  chk=[u'사택이 3줄이고 줄마다 4채, 줄 사이에 골목이 있다', u'사택 사이 틈이 줄끼리 어긋나 있다', u'세 번째 줄 너머에 넓은 마당과 물탱크가 있다', u'마당 건너 오른쪽에 선광장, 위쪽에 관리소가 있다', u'왼쪽 위 변 가운데에 막힌 갱도 입구가 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"A pile of brick rubble, waist-high, 1 x 1 m.", u"A rusted ore cart on a short piece of rail, waist-high, 1 x 2 m, orientation 1.", u"The same ore cart, orientation 2.", u"A section of collapsed timber fence, waist-high, 1 x 3 m, orientation 1.", u"A stack of rotting timber props, 1 x 2 m, 2.2 m high, orientation 1.", u"A dead pine with a broken top, 1 x 1 m base, 4 m high."]),
         (u'special', u'목표 · 환경', u'', [u"**The objective**: an old green steel safe, door ajar, a paper folder visible inside, drawn large, lit by a small lamp.", u"A rusted oil lantern on a post, lit, 1 x 1 m.", u"A tarpaulin shelter on four poles, 2 x 2 m, 2.2 m high (blocks sight).", u"A guard's brazier: an oil drum with a fire in it, 1 x 1 m.", u"A parked off-road pickup truck, lights off, 2 x 5 m, orientation 1.", u"The same pickup, orientation 2."])],
  info=[u'환경: 폭우. 14초마다 4초 동안 번개가 쳐서 전체가 밝아진다(경비 시야 1.3배). 그 밖의 시간에는 달려도 소리가 나지 않는다.', u'목표: 관리소 금고에서 3년 전 철수 기록을 꺼낸다.', u'배지: 무살상', u'엔진: 소음 가림(주기)은 블러디 4판 종소리 처리를 그대로 쓴다. 번개는 새로 만든다.'],
  dlg=[(u'① 시작 전', [(u'레이븐', u'좌표는 너한테만 보냈어. 본부엔 내가 자고 있는 걸로 해 둬.'), (u'지휘관', u'폐광촌은 3년 전에 닫힌 곳이야. 왜 거기에 아직 경비가 있지?'), (u'레이븐', u'그러니까 가 보는 거지. 지킬 게 없으면 사람을 세워 둘 리가 없잖아.')]),
       (u'② 금고 앞', [(u'레이븐', u'…철수 기록이야. 그날 밤 거. 서명란이 비어 있어.'), (u'지휘관', u'비어 있다고? 명령은 분명히 내려왔잖아.'), (u'레이븐', u'그래. 누가 내렸는지만 지워 놨어.')]),
       (u'③ 클리어', [(u'레이븐', u'나왔어. 아무도 안 건드렸으니까 걱정 마.'), (u'레이븐', u'원본은 기록원에 있을 거야. 다음엔 거기야.')])]),
 dict(t=u'서명', place_ko=u'심야의 기록원 분관', m=24, io='in', light=u"Midnight. Dark polished floor, a few pools of light from motion-sensor ceiling lamps, green banker lamps in the reading room.",
  place=u"The interior of a state archive annex: a large stack hall with floor rails for rolling shelves, ringed by a corridor and four rooms.",
  lay=u'''**Ring corridor.** A 2.5 m corridor runs all the way around the inside of the four sides.

**Stack hall.** The centre of the map: one hall 13 x 13 m, enclosed by walls with **four doorways, one in the middle of each wall**. Its floor carries **seven pairs of steel floor rails, all parallel to the upper-left side**, evenly spaced, running wall to wall. **The hall is otherwise empty.** (The rolling shelves are separate sprites.) Along the hall's upper-right wall, one fixed row of built-in filing cabinets.

**Rooms outside the ring corridor, in the four corners:**
- BOTTOM corner: the **lobby**, 6 x 6 m, with a built-in reception counter and the way in.
- RIGHT corner: the **reading room**, 6 x 8 m, with one doorway; no furniture.
- LEFT corner: the **card-catalogue room**, 6 x 6 m, its two far walls lined with built-in catalogue drawers, one doorway.
- TOP corner: the **conservation lab**, 6 x 8 m, with a built-in workbench along its far wall and one doorway.

**Way in:** a glass double door in the lobby's near wall, with a floor hazard stripe.''',
  chk=[u'가운데 서고 홀에 바닥 레일만 있고 서가는 없다', u'서고 홀 네 벽 가운데에 문이 하나씩 있다', u'홀을 한 바퀴 도는 복도가 있다', u'네 모서리에 로비 · 열람실 · 목록실 · 보존 처리실이 있다', u'가까운 두 벽이 낮아서 안쪽 바닥이 보인다'],
  props=[(u'cover', u'엄폐물', u'', [u"**A rolling compact shelf**: a tall steel shelf unit full of grey file boxes with a hand-wheel on its end, 1 x 5 m, 2.4 m high, orientation 1. It fills about 90% of the cell's width.", u"The same rolling shelf, orientation 2.", u"A reading table with a green banker lamp, lit, waist-high, 1 x 2 m, orientation 1.", u"The same reading table, orientation 2.", u"A book trolley loaded with folders, waist-high, 1 x 1 m.", u"A tall glass display case of old documents, 1 x 1 m, 2 m high."]),
         (u'special', u'목표 · 환경', u'', [u"**The objective**: a conservation table with one document under a glass plate and a bright task lamp over it, drawn large.", u"A hand-wheel crank for a rolling shelf on a small floor plinth, 1 x 1 m.", u"A ceiling motion-sensor lamp seen from above with its cone of light, drawn as a round fitting.", u"A security guard's desk with a monitor and a thermos, waist-high, 1 x 2 m, orientation 1.", u"A stack of archive boxes, waist-high, 1 x 1 m.", u"A step ladder on wheels, 1 x 1 m, 2 m high."])],
  info=[u'환경: 이동식 서가. 손잡이(3곳)를 돌리면 서가 한 줄이 옆으로 한 칸 밀려 통로가 열리고 다른 통로가 닫힌다. 동작 감지등 아래에 2초 넘게 서 있으면 불이 켜져 경비가 보러 온다.', u'목표: 보존 처리실에서 원본 명령서의 서명을 확인한다.', u'배지: 무의심', u'엔진: 서가 이동과 감지등은 새로 만든다. 서가는 낱개라서 그림을 다시 뽑지 않고 옮길 수 있다.'],
  dlg=[(u'① 시작 전', [(u'지휘관', u'야간 경비는 둘뿐이야. 대신 천장 등이 움직임을 잡아.'), (u'레이븐', u'알아. 그래서 천천히 갈 거야. 종이 한 장 보러 가는데 뛸 일은 없지.')]),
       (u'② 명령서 앞', [(u'레이븐', u'…서명 있어. 본부 직인이 아니야. 사람 이름이야.'), (u'지휘관', u'누군데?'), (u'레이븐', u'설계자. 그날 철수시킨 게 그 사람이었어. 내가 아니라.')]),
       (u'③ 클리어', [(u'레이븐', u'3년 동안 내가 버리고 온 줄 알았는데.'), (u'레이븐', u'녹음이 남아 있대. 항구 끝 등대에. 그건 내 귀로 들어야겠어.')])]),
 dict(t=u'대면', place_ko=u'항구 끝 등대와 방파제', m=30, io='out', light=u"Night, wind and sea spray. Black water, wet concrete, a few caged bulkhead lamps. (The lighthouse beam is added by the game.)",
  place=u"A concrete breakwater reaching out over black sea to a lighthouse. Most of the plan is water.",
  lay=u'''**This map is mostly sea.** The whole diamond is black water with slow swell and foam. Only the structures below are land. Rule 3 (a lane around all four sides) does not apply.

**Quay.** A concrete quay strip 6 m deep along the **whole lower-right side**. This is the land end.

**Causeway.** From the middle of the quay, a concrete causeway **5 m wide** runs straight out toward the upper-left side for 16 m, then makes one right-angle turn and runs toward the TOP corner for 10 m, ending at the lighthouse platform.

**Service ledge.** Along the **outer side of the whole causeway**, a second, lower walkway: a concrete ledge 2 m wide, 1 m below the causeway deck, reached by **short flights of steps at three points** (near the quay, at the turn, and just before the lighthouse platform).

**Side platforms.** Two square platforms, each 5 x 5 m, attached to the inner side of the first stretch of causeway, one third and two thirds of the way along. The first carries a **gear shed**, 4 x 4 m, roof removed, one doorway. The second is a bare **boat landing** with steps down into the water.

**Lighthouse platform.** A square platform 8 x 8 m at the end. On it the **lighthouse tower** (a round white tower on a square 4 x 4 m base, drawn only up to 4 m and cut off flat) with one door facing the causeway.

**Tetrapods.** Heaps of concrete tetrapods piled in the water against the outer side of the turn and around the lighthouse platform: solid, not walkable.

**Way in:** a gate in the low fence where the quay meets the lower-right side, near the BOTTOM corner.''',
  chk=[u'맵 대부분이 검은 바다다', u'오른쪽 아래 변을 따라 부두가 있고 가운데에서 방파제가 뻗는다', u'방파제가 한 번 직각으로 꺾여 등대 받침으로 이어진다', u'방파제 바깥쪽에 한 단 낮은 통로가 있고 계단이 3곳이다', u'안쪽에 네모난 받침 2개(창고, 선착장)가 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"A cluster of three concrete tetrapods sitting on the deck, 2 x 2 m, 2.2 m high.", u"A stack of crab pots and fishing nets, waist-high, 1 x 1 m.", u"A steel mooring bollard with coiled rope, waist-high, 1 x 1 m.", u"Stacked fish crates, waist-high, 1 x 2 m, orientation 1.", u"An upturned wooden dinghy on trestles, 1 x 3 m, waist-high, orientation 1.", u"The same dinghy, orientation 2."]),
         (u'special', u'목표 · 환경', u'', [u"**The objective**: an old reel-to-reel tape recorder on a stone ledge, reels turning, a small red light, drawn large.", u"The lighthouse lantern room seen from above: a glass cage with a bright lens, to sit on top of the cut-off tower.", u"A caged bulkhead lamp on a short post, lit, 1 x 1 m.", u"A small harbour patrol boat moored side-on, 2 x 6 m, orientation 1.", u"A guard's windbreak: a canvas screen on a steel frame, 1 x 2 m, 2 m high, orientation 1.", u"The same windbreak, orientation 2."])],
  info=[u'환경: 등대 불빛. 10초에 한 바퀴 도는 빛줄기가 방파제를 훑는다. 빛 안에서는 엄폐가 없으면 바로 들킨다. 레이븐은 총을 두고 와서 사격을 쓸 수 없다.', u'목표: 등대 문 옆의 녹음기를 끝까지 듣는다(6초).', u'배지: 무발포(이 판은 항상 달성). 대신 TAKE 3 되돌리기 1회 제한이 붙는다.', u'엔진: 등대 불빛은 회전 카메라로 처리한다(기존 기능).'],
  dlg=[(u'① 시작 전', [(u'지휘관', u'총은?'), (u'레이븐', u'두고 왔어. 오늘은 쏘러 가는 게 아니라 들으러 가는 거라서.'), (u'지휘관', u'…빛이 한 바퀴 도는 데 10초야. 그 사이에만 움직여.')]),
       (u'② 녹음기 앞', [(u'녹음', u'"대장, 문은 내가 닫을게. 셋 다는 못 나가. 그러니까 가. 이건 명령 아니고 부탁이야."'), (u'레이븐', u'………'), (u'레이븐', u'바보 같은 게. 그걸 왜 네가 정해.')]),
       (u'③ 클리어', [(u'레이븐', u'다 들었어. 그 애는 버려진 게 아니었어. 자기가 남은 거였어.'), (u'레이븐', u'…오늘은 본부로 안 가. 문 열어 둬.')])]),
]
T['viper'] = [
 dict(t=u'빗나간 한 발', place_ko=u'스키 리조트 야간 슬로프', m=28, io='out', light=u"Night, clear and cold. A floodlit white piste between dark pine forest; long blue shadows.",
  place=u"A ski resort at night: a base area with a lift station, a floodlit piste crossing the map, and dark forest beyond it.",
  lay=u'''**Piste.** A groomed, floodlit ski piste **10 m wide crosses the whole map, parallel to the upper-left side**, from the lower-left side to the upper-right side. Its centre line is 12 m from the upper-left side. It is bright, flat and **completely empty**.

**Lift line.** Along the near edge of the piste, a straight line of **four steel lift pylons**, each on a 1 x 1 m concrete base, evenly spaced. No chairs. (Chairs are sprites.)

**Underpass.** Near the upper-right side, a **timber skier tunnel 2.5 m wide** passes under the piste from the near side to the far side: a dark opening on each side.

**Base area (near side of the piste).** Three buildings, each roof removed, with **2.5 m alleys between them and behind them**:
- toward the LEFT corner: the **ski rental hut**, 5 x 6 m, one doorway;
- in the middle: the **lift station**, 6 x 7 m, open on its piste side, with the big drive wheel housing inside;
- toward the RIGHT corner: the **snow-groomer garage**, 6 x 8 m, open front facing the piste, empty inside.

**Far side of the piste.** A strip 7 m deep. Along the upper-left side, a belt of **dense snow-laden pines 3 m deep** (solid). In front of it a 2.5 m snow path. Fixed low **snow fences** in three short straight runs along the piste's far edge. At the TOP corner, a square timber **viewing deck**, 4 x 4 m, with a rail on its far edges.

**Way in:** a gap in the low fence on the lower-left side, close to the BOTTOM corner.''',
  chk=[u'환한 슬로프가 왼쪽 위 변과 나란히 맵을 가로지른다', u'슬로프 위에 아무것도 없다', u'슬로프 가까운 쪽 가장자리에 리프트 기둥 4개가 한 줄로 있다', u'오른쪽 위 변 가까이에 슬로프 밑을 지나는 터널이 있다', u'가까운 쪽에 건물 3채와 그 사이 골목이 있다', u'맨 위 모서리에 전망 데크가 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"A snow cannon on a wheeled tripod, 1 x 1 m, 2 m high.", u"A rack of skis and poles, waist-high, 1 x 2 m, orientation 1.", u"A pile of shovelled snow, waist-high, 1 x 1 m.", u"Orange safety netting between two poles, waist-high, 1 x 3 m, orientation 1.", u"The same netting, orientation 2.", u"A stack of padded crash mats, 1 x 2 m, 2 m high, orientation 1."]),
         (u'special', u'목표 · 환경', u'', [u"**The objective**: a low sniper's rest of packed snow with a folded white camouflage sheet and a spotting scope on a small tripod, drawn large.", u"**A ski-lift chair**: an empty two-seat chair hanging from its grip and a short piece of cable, seen from the map camera.", u"A snow-grooming machine with a front blade, lights on, 3 x 5 m, orientation 1.", u"The same grooming machine, orientation 2.", u"A floodlight mast with two lamps, lit, 1 x 1 m base, 4 m high.", u"A snowmobile, parked, 1 x 2 m, orientation 1."])],
  info=[u'환경: 조명 대비. 슬로프 위에서는 경비 시야가 1.4배, 숲과 건물 그늘에서는 0.7배. 리프트 의자가 8초마다 지나가며 그 그림자 안은 3초 동안 어둡다.', u'목표: 전망 데크에서 조준경으로 옛 관측수가 묵는 방을 확인한다(5초). 쏘지 않는다.', u'배지: 무발포', u'엔진: 구역별 시야 배율은 블러디 1판 발전기(어둠) 처리를 구역 단위로 바꿔 쓴다.'],
  dlg=[(u'① 시작 전', [(u'바이퍼', u'휴가계 냈어. 사유는 "스키". 거짓말은 아니잖아?'), (u'지휘관', u'스키장에 조준경을 들고 가는 사람은 없어, 바이퍼.'), (u'바이퍼', u'보기만 할 거야. 진짜로. 손가락은 주머니에 넣고 갈게.')]),
       (u'② 전망 데크', [(u'바이퍼', u'…있네. 3층 끝 방. 불 켜 놓고 책 읽고 있어.'), (u'지휘관', u'네 관측수가 맞아?'), (u'바이퍼', u'맞아. 내 대신 보고서 쓰고 옷 벗은 사람. 늙었네, 저 인간.')]),
       (u'③ 클리어', [(u'바이퍼', u'한 발도 안 쐈어. 칭찬해 줘.'), (u'바이퍼', u'내일은 좀 더 가까이 가 볼래. 저 거리에선 말이 안 들리거든.')])]),
 dict(t=u'거리', place_ko=u'온천 료칸의 복도', m=24, io='in', light=u"Night. Warm paper-lantern light, dark timber, tatami, steam drifting from the bath wing.",
  place=u"The interior of a traditional hot-spring inn: rooms and a bath wing arranged around a courtyard garden.",
  lay=u'''**Courtyard.** The exact centre: a rock garden 8 x 8 m, open to the sky, with a pond, raked gravel and one pine. **Not walkable.**

**Veranda.** A polished timber veranda **2 m wide runs all the way around the courtyard**.

**Guest wing (upper-left side).** Three guest rooms in a row, each 5 x 5 m, tatami floor, each with **one wide sliding-door opening onto the veranda**. The room nearest the TOP corner has a raised alcove on its far wall.

**Bath wing (upper-right side).** From the TOP end to the RIGHT end: a **changing room**, 5 x 5 m, with built-in basket shelves; then the **bath hall**, 5 x 9 m, with a sunken stone pool filling its far half (water, not walkable) and a wet stone walkway along its veranda side. One opening from the veranda into each.

**Service wing (lower-right side).** A straight **service corridor 2 m wide** behind a wall, running the full length of the side, with one doorway to the veranda at each end. Off it, a kitchen 5 x 6 m with a built-in stove range.

**Front wing (lower-left side).** The **entrance hall** at the BOTTOM corner, 6 x 6 m, with a raised timber step; next to it two more guest rooms, 5 x 5 m each, opening onto the veranda.

**Way in:** the front door in the near wall of the entrance hall.''',
  chk=[u'한가운데에 들어갈 수 없는 중정이 있다', u'중정을 한 바퀴 도는 툇마루가 있다', u'왼쪽 위에 객실 3개, 오른쪽 위에 탈의실과 탕이 있다', u'오른쪽 아래 변을 따라 벽 뒤에 좁은 서비스 복도가 있다', u'객실마다 툇마루 쪽 문이 열려 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"**A sliding paper screen door (shoji)**, closed, standing upright in its track, 1 x 2 m, 2 m high, orientation 1.", u"The same sliding screen door, orientation 2.", u"A low lacquer table with a tea set, waist-high, 1 x 1 m.", u"A folding painted screen (byobu), three panels, 1 x 2 m, 1.8 m high, orientation 1.", u"A stack of folded futons, waist-high, 1 x 1 m.", u"A large potted bamboo, 1 x 1 m, 2.2 m high."]),
         (u'special', u'목표 · 환경', u'', [u"**The objective**: a worn pocket field notebook with a pencil on a small writing box, drawn large, lit by a paper lantern.", u"A standing paper floor lantern, lit, 1 x 1 m.", u"A cloud of thick white steam, soft-edged, about 3 x 3 m, on the flat background.", u"A wooden bath bucket and stool set, low, 1 x 1 m.", u"A serving trolley with covered dishes, waist-high, 1 x 2 m, orientation 1.", u"A pair of guest slippers and a folded robe on a tray, drawn large."])],
  info=[u'환경: 수증기. 탕과 그 앞 툇마루는 모두의 시야가 0.5배. 장지문 5곳을 여닫아 시야를 끊는다(닫으면 벽). 저격 사거리가 나오지 않아 가까이 가야 한다.', u'목표: 맨 위 객실(옛 관측수의 방)에서 관측 수첩을 가져온다.', u'배지: 유령', u'엔진: 문 여닫기는 새로 만든다. 수증기는 구역 시야 배율.'],
  dlg=[(u'① 시작 전', [(u'바이퍼', u'여긴 복도가 길어 봐야 열 걸음이야. 내 총이 제일 쓸모없는 곳이지.'), (u'지휘관', u'그럼 문을 써. 닫으면 벽이야.'), (u'바이퍼', u'가까이 가는 거 별로 안 좋아하는데. …뭐, 휴가니까.')]),
       (u'② 수첩 앞', [(u'바이퍼', u'그날 페이지가 있어. 거리, 바람, 습도. 그리고 맨 밑에 한 줄.'), (u'지휘관', u'뭐라고 적혀 있어?'), (u'바이퍼', u'"사수는 쏘지 않았다. 나는 그게 옳았다고 적지 못했다." …글씨 여전히 못 쓰네.')]),
       (u'③ 클리어', [(u'바이퍼', u'방은 비어 있었어. 산 위 관측소로 올라갔대.'), (u'바이퍼', u'나 피해서 올라간 건 아니겠지? 그럼 좀 서운한데.')])]),
 dict(t=u'숨', place_ko=u'산정 관측소', m=28, io='out', light=u"Night on a summit above the clouds. Hard moonlight, blown snow, a few red aviation lamps.",
  place=u"A mountain summit: a cable-car top station, a narrow rock ridge, and a weather observatory at the far end. Everything off the ridge is a drop into cloud.",
  lay=u'''**Most of this map is a drop.** Apart from the land described below, the diamond is dark cloud far below: **not walkable**. Rule 3 (a lane around all four sides) does not apply.

**Top station.** At the BOTTOM corner, a flat rock shelf 10 x 10 m. On it the **cable-car station**, 6 x 8 m, roof removed, with an empty docking bay open toward the BOTTOM corner and one doorway on the far side.

**Ridge.** From the top station a **rock ridge 3 m wide** runs straight toward the TOP corner for 16 m. Bare wind-scoured rock and ice.

**Lee ledge.** Along the lower-left flank of the ridge, **2 m below it**, a sheltered ledge path 2 m wide runs parallel to the ridge for its whole length. **Three short stairways cut in the rock** join ledge and ridge: at both ends and in the middle. A fixed snow cornice overhangs the ledge.

**Saddle.** Halfway along, the ridge widens into a flat 6 x 6 m saddle with a **steel weather mast** on a 2 x 2 m base and one fixed L-shaped dry-stone windbreak wall, 1 m high.

**Observatory compound.** At the TOP corner, a flat shelf 11 x 11 m. On it the **observatory**, 6 x 7 m, roof removed, divided into an instrument room and a bunk room, with one outside doorway each and one doorway between them; and a **generator shed**, 3 x 3 m, roof on.

**Way in:** the cable-car docking bay.''',
  chk=[u'땅은 아래 승강장, 능선, 위 관측소뿐이고 나머지는 구름이다', u'능선이 좁고(3 m) 곧다', u'능선 왼쪽 아래에 한 단 낮은 길이 나란히 있고 계단이 3곳이다', u'능선 중간이 넓어지고 기상 탑과 돌담이 있다', u'관측소가 방 2개로 나뉘어 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"A wind-carved boulder capped with snow, 1 x 1 m, 2 m high.", u"A low snow-block wall, waist-high, 1 x 2 m, orientation 1.", u"The same snow-block wall, orientation 2.", u"A steel instrument crate lashed with straps, waist-high, 1 x 1 m.", u"A stack of fuel jerrycans on a pallet, waist-high, 1 x 1 m.", u"A white radar dome on a square steel frame, 2 x 2 m, 2.5 m high."]),
         (u'special', u'목표 · 환경 · 인물', u'', [u"**The spotter**, as a small figure for the map: a lean man in his fifties in a faded olive parka with the hood down, grey beard, sitting on a camp stool with a tin mug, seen from the map camera, full body, drawn large (about 420 px tall), facing lower-left.", u"The same man standing, hands open at his sides, facing lower-left.", u"**The objective marker**: a small camp stove with a kettle on it, lit, steam rising, drawn large.", u"A red aviation warning lamp on a short pole, lit, 1 x 1 m.", u"A cable-car cabin, empty, doors open, 2 x 3 m, orientation 1.", u"A swirl of blown snow, soft-edged, about 4 x 2 m, on the flat background."])],
  info=[u'환경: 눈보라. 22초마다 8초 동안 돌풍이 불어 모두의 시야가 0.4배가 된다. 능선 위는 그때만 건널 수 있고, 아랫길은 느리지만 가려져 있다.', u'목표: 관측소에서 관측수에게 묻는다(대화). 사격은 한 발만 허용되고, 그 한 발을 쓰지 않으면 배지.', u'배지: 한 발(남긴 채 클리어)', u'엔진: 눈보라는 블러디 3판 처리를 그대로 쓴다.'],
  dlg=[(u'① 시작 전', [(u'바이퍼', u'탄은 한 발 넣었어. 버릇이라서.'), (u'지휘관', u'쓸 일 없길 바랄게.'), (u'바이퍼', u'나도. 오늘은 물어보러 가는 거니까. 대답 듣기 전에 죽으면 곤란하잖아.')]),
       (u'② 관측수 앞', [(u'바이퍼', u'오랜만이네, 영감. 하나만 물을게. 그날 내가 안 쏜 거, 맞았어?'), (u'관측수', u'…네가 안 쐈어도 그 사람은 일주일 뒤에 죽었다. 휴전도 깨졌고.'), (u'관측수', u'그래도 맞았어. 네 손으로 깬 게 아니잖아. 난 그 말을 보고서에 못 썼다. 그게 10년 걸렸구나.')]),
       (u'③ 클리어', [(u'바이퍼', u'들었어? "맞았어"래. 겨우 그 한마디 들으려고 산을 두 개나 탔네.'), (u'바이퍼', u'…한 발은 그대로 가져왔어. 이건 네가 좀 맡아 줘.')])],
  npc=(u'관측수', u"**The spotter.** A lean, weathered man in his fifties, once a military sniper's observer: grey beard, deep lines, calm tired eyes, a faded **olive mountain parka** with the hood down, a wool scarf, fingerless gloves. He **faces RIGHT** (toward the agent he is talking to).", [u"sitting, a tin mug in both hands, looking up without surprise, a faint tired smile.", u"the same man, eyes lowered, speaking quietly, one hand rubbing the back of his neck."])),
]
T['glitch'] = [
 dict(t=u'로그', place_ko=u'데이터센터 냉각동', m=24, io='in', light=u"Night shift. Cold white light, blue and amber floor glow between the racks, status LEDs.",
  place=u"The interior of a data centre: a server hall of rack rows, a cooling plant room, a power room and a security office.",
  lay=u'''**Ring corridor.** A 2.5 m corridor runs all the way around the inside of the four sides.

**Server hall.** The centre: one hall 16 x 14 m with **two doorways on its near (lower-left) wall and one on each of its two end walls**. Inside, **five rows of tall server racks, all parallel to the lower-left side**, each row 13 m long, with **2 m aisles between rows**. **Each row is broken once by a 2 m cross-gap, and the gaps of neighbouring rows are not lined up.** The aisles alternate: a **cold aisle** with a blue-lit perforated floor, then a **hot aisle** with an amber-lit floor, and so on.

**Cooling plant.** Between the server hall and the upper-right side: a room 5 m deep running the hall's full length, holding **three big cooling-fan units** fixed in a row (each 3 x 3 m, with a round grille on top), with a doorway at each end.

**Power room.** At the TOP corner: 5 x 5 m, switchgear cabinets built in along two walls, one doorway.

**Network cage.** At the RIGHT corner: a 4 x 4 m room walled in **steel mesh**, one mesh gate, a built-in terminal desk inside.

**Security office.** At the BOTTOM corner: 4 x 5 m with a built-in monitor desk, next to an **airlock entrance** (two doors in a short passage).

**Staging room.** At the LEFT corner: 5 x 6 m, empty, one doorway.

**Way in:** the airlock at the BOTTOM corner.''',
  chk=[u'서버 랙이 5줄이고 왼쪽 아래 변과 나란하다', u'줄마다 끊긴 틈이 1곳, 줄끼리 어긋나 있다', u'통로 바닥이 파란색과 주황색으로 번갈아 있다', u'홀 뒤(오른쪽 위)에 큰 팬 3대가 있는 방이 있다', u'오른쪽 모서리에 철망으로 된 방이 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"A single server rack with its door open and cables hanging out, 1 x 1 m, 2.2 m high.", u"A crash cart: a wheeled trolley with a monitor and keyboard, waist-high, 1 x 1 m.", u"A stack of server shipping boxes, waist-high, 1 x 1 m.", u"A cable drum on a stand, waist-high, 1 x 1 m.", u"A wheeled tool chest, waist-high, 1 x 2 m, orientation 1.", u"A row of three gas-suppression cylinders in a frame, 1 x 2 m, 2 m high, orientation 1."]),
         (u'special', u'목표 · 환경', u'', [u"**The objective**: a console terminal with one bright screen showing abstract scrolling lines (no readable text) and a small data key plugged into it, drawn large.", u"A ceiling dome camera with a red thermal lens, seen from above.", u"A wall control panel for the cooling fans with a big rotary dial and three lights, drawn large.", u"A floor tile lifted open showing cables, 1 x 1 m, low.", u"A night technician's chair and coffee cup at a small desk, waist-high, 1 x 1 m.", u"A wet-floor style warning tripod with a blank yellow face (no text), 1 x 1 m."])],
  info=[u'환경: 냉각 팬. 20초마다 7초 동안 팬이 최대로 돌아 소리가 묻힌다. 주황색 통로(열 통로)에는 열화상 카메라가 있어 3초 넘게 머물면 들킨다.', u'목표: 철망 방의 단말에서 옛 계정의 접속 기록을 뜬다.', u'배지: 무의심', u'엔진: 소음 가림(주기)은 종소리 처리. 열 통로 체류 제한은 새로 만든다.'],
  dlg=[(u'① 시작 전', [(u'글리치', u'6과 장비는 하나도 안 가져왔어. 이건 내 일이니까. 노트북도 내 거, 드론도… 드론은 집에 뒀어. 걔까지 휘말리면 안 돼.'), (u'지휘관', u'혼자 괜찮겠어?'), (u'글리치', u'안 괜찮지! 근데 누가 내 옛날 이름으로 로그인을 하고 있다니까? 그건 더 안 괜찮아.')]),
       (u'② 단말 앞', [(u'글리치', u'찾았다. 접속 기록… 어, 이거 봐. 타자 습관이 나랑 똑같아. 백스페이스 누르는 자리까지.'), (u'지휘관', u'너를 흉내 내는 거야?'), (u'글리치', u'아니. 나한테 배운 사람이야. …한 명 있어. 내가 두고 온 사람.')]),
       (u'③ 클리어', [(u'글리치', u'하, 살았다. 열 통로에서 진짜 익는 줄 알았어.'), (u'글리치', u'접속지는 전자상가 옥상이야. 우리 옛날 작업실. 아직도 거기 있었구나.')])]),
 dict(t=u'사본', place_ko=u'전자상가 옥상', m=28, io='out', light=u"Night in a dense city. Neon glow from below in magenta and teal, wet rooftops, red beacon lights.",
  place=u"Four neighbouring rooftops of an electronics market, joined by steel footbridges, with the street far below between them.",
  lay=u'''**Four rooftops.** The diamond is divided into **four square rooftops, each about 12 x 12 m, one in each corner of the diamond** (BOTTOM roof, LEFT roof, RIGHT roof, TOP roof), separated by a **cross-shaped gap 3 m wide**. The gap is a dark street far below with tiny neon lights: **not walkable**. Every rooftop has a low parapet 0.5 m high around its edge. Rule 3 (a lane around all four sides) does not apply; instead keep a 2 m clear lane around the edge of each rooftop.

**Footbridges.** Four steel grating footbridges, each 2 m wide with low rails, cross the gaps: **BOTTOM-LEFT, BOTTOM-RIGHT, LEFT-TOP and RIGHT-TOP**. There is no bridge straight from BOTTOM to TOP and none from LEFT to RIGHT.

**BOTTOM roof.** A stair-head bulkhead 3 x 3 m (solid, door facing the centre) and a fixed row of four big ventilation ducts running along its lower-left edge.

**LEFT roof.** The **back of a huge sign**: a steel truss frame 9 m long and 3 m tall standing along the roof's upper-left edge, seen from behind. A solid lift machine room 4 x 4 m.

**RIGHT roof.** A **water tank on steel legs** (3 x 3 m base, solid) and a fixed pigeon loft 2 x 4 m. A second, smaller sign frame along the upper-right edge.

**TOP roof.** The **rooftop workshop**: a shack 5 x 6 m, roof removed, one doorway facing the centre, a built-in workbench along its far wall. Beside it a lattice antenna mast on a 2 x 2 m base.

**Way in:** a fire-escape ladder head at the BOTTOM corner of the BOTTOM roof, marked with a floor hazard stripe.''',
  chk=[u'옥상이 4개이고 십자 모양 틈으로 나뉜다', u'철제 다리가 4개다(아래-왼쪽, 아래-오른쪽, 왼쪽-위, 오른쪽-위)', u'아래에서 위로 바로 가는 다리가 없다', u'왼쪽 옥상에 큰 간판 뒷면 골조가 있다', u'위쪽 옥상에 작업실이 있다', u'틈 아래로 먼 거리의 불빛이 보인다'],
  props=[(u'cover', u'엄폐물', u'', [u"An air-conditioner outdoor unit on a low stand, waist-high, 1 x 1 m.", u"Two air-conditioner units stacked in a frame, 1 x 1 m, 2 m high.", u"A row of three outdoor units, waist-high, 1 x 3 m, orientation 1.", u"The same row of three, orientation 2.", u"A satellite dish on a weighted base, 1 x 1 m, 2 m high.", u"A stack of plastic crates of old circuit boards, waist-high, 1 x 1 m."]),
         (u'special', u'목표 · 환경', u'', [u"**The objective**: an old beige desktop computer tower with a single external drive on top, a green light blinking, drawn large.", u"**A patrol drone**: a small four-rotor security drone with a red sensor eye, seen from the map camera, drawn large.", u"The same drone seen from a second angle, turned 90 degrees.", u"A neon tube sign shaped as abstract zigzags (no letters), lit magenta, on a small frame, 1 x 2 m.", u"The same sign unlit.", u"A folding camp chair, a crate table and instant-noodle cups, low, 1 x 1 m."])],
  info=[u'환경: 네온 간판. 6초 켜지고 4초 꺼진다. 켜진 동안 간판 앞 옥상은 경비 시야 1.3배. 순찰은 사람이 아니라 드론 3대(움직이는 카메라)이고 드론은 기절시킬 수 없다.', u'목표: 위쪽 옥상 작업실에서 사본을 찾는다.', u'배지: 원테이크(되돌리기 0회)', u'엔진: 드론은 움직이는 카메라(기존). 간판 깜빡임은 구역 시야 배율을 주기로 바꾼다.'],
  dlg=[(u'① 시작 전', [(u'글리치', u'여기 3층에서 컵라면 진짜 많이 먹었는데. 옥상은 그때도 무서웠어. 다리가 그물이라 밑이 다 보이거든.'), (u'지휘관', u'드론이 셋이야. 사람은 없어.'), (u'글리치', u'걔가 짠 순찰 경로네. 딱 봐도 알아. 왼쪽으로만 돌아. 맨날 그랬어.')]),
       (u'② 작업실', [(u'글리치', u'사본 찾았어. 내가 지운 거, 걔가 전부 다시 모아 놨어. 내 이름까지.'), (u'지휘관', u'왜 그랬을까.'), (u'글리치', u'쪽지가 있어. "네가 없어진 줄 알았어. 없앤 줄은 몰랐어." …나 진짜 못됐다.')]),
       (u'③ 클리어', [(u'글리치', u'걔는 없었어. 헬리오스가 먼저 데려갔대. 단말은 폐역사에 숨겼다고.'), (u'글리치', u'가서 끝낼래. 이번엔 지우는 게 아니라, 내 손으로 끄는 거야.')])]),
 dict(t=u'로그아웃', place_ko=u'폐쇄된 지하철 역사', m=28, io='in', light=u"Underground, power failing. Pools of weak emergency light, long dark stretches, dusty tile.",
  place=u"A closed underground station: an island platform between two track beds, a stalled train, and a concourse along one side.",
  lay=u'''**Island platform.** In the centre, a platform **8 m wide running the full length of the map, parallel to the lower-left side**. Down its centre line, **a row of square tiled columns, 1 x 1 m, one every 4 m**. One fixed kiosk shell, 3 x 3 m, shutters down, a third of the way along.

**Track beds.** On each long side of the platform, a track bed **4 m wide and 1.2 m lower**, with rails and sleepers. **Both track beds are walkable.** Short steel **service steps at three points on each side** join platform and track bed.

**Stalled train.** On the far track bed (the one toward the upper-right side): **three metro cars in a row, each 7 m long, with 1.5 m gaps between them**, dark, doors shut. Tall and solid. The near track bed is empty.

**Far service walkway.** Beyond the far track bed, along the upper-right side: a 2 m maintenance walkway with a doorway into a **maintenance room**, 4 x 5 m, at the RIGHT corner.

**Concourse.** Beyond the near track bed there is nothing but the low near wall. Instead the concourse lies along the **upper-left side**: a raised strip 6 m deep across the full width, reached from the platform end by **two straight stairways side by side** (drawn as stepped ramps). On it, from the LEFT end to the TOP end: a line of fixed ticket-gate posts with two gaps; a transfer passage mouth (blocked by a shutter); and the **station office**, 5 x 6 m, roof removed, one doorway, a small vault alcove in its far corner.

**Way in:** a stairway coming down onto the platform at its end by the lower-right side, close to the BOTTOM corner.''',
  chk=[u'가운데 승강장이 왼쪽 아래 변과 나란히 길게 있다', u'승강장 가운데에 네모 기둥이 한 줄로 있다', u'양쪽 선로가 한 단 낮고 계단이 3곳씩 있다', u'먼 쪽 선로에만 전동차 3량이 있다', u'왼쪽 위 변을 따라 높은 대합실과 역무실이 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"A platform bench with a broken back, waist-high, 1 x 2 m, orientation 1.", u"The same bench, orientation 2.", u"A vending machine, dark, 1 x 1 m, 2 m high.", u"A stack of sandbags and a folded barrier, waist-high, 1 x 1 m.", u"A maintenance hand trolley on rails loaded with tools, waist-high, 1 x 2 m, orientation 1.", u"A fallen ceiling panel and cable tangle, waist-high, 1 x 1 m."]),
         (u'special', u'목표 · 환경', u'', [u"**The objective**: a small steel wall safe, open, with a rugged handheld terminal inside, its screen glowing teal, drawn large.", u"An emergency light box on a bracket, lit, weak green-white glow.", u"The same emergency light box, dark.", u"A steel drum with a small fire burning in it (for burning the terminal), 1 x 1 m.", u"A portable floodlight on a tripod with a generator, lit, 1 x 1 m, 2 m high.", u"A guard's folding table with a radio and a lantern, waist-high, 1 x 1 m."])],
  info=[u'환경: 정전. 12초 켜지고 6초 꺼진다. 꺼진 동안 경비도 글리치도 서로 2칸 밖은 보지 못한다. 휴대 조명(2곳) 주변은 꺼지지 않는다.', u'목표: 역무실 금고의 단말을 꺼내 드럼통 불에 태운다(금고 → 드럼통, 두 단계).', u'배지: 유령', u'엔진: 주기 정전은 블러디 1판 발전기 어둠을 주기로 바꿔 쓴다. 두 단계 목표는 블러디 중간 목표 처리.'],
  dlg=[(u'① 시작 전', [(u'글리치', u'지우는 건 쉬워. 엔터 한 번이야. 근데 그건 전에도 해 봤잖아. 결국 누가 다시 주워 왔고.'), (u'지휘관', u'그래서 태우려고?'), (u'글리치', u'응. 불 꺼지면 6초야. 그 사이에 뛸 거야. 나 뛰는 거 진짜 싫어하는데.')]),
       (u'② 드럼통 앞', [(u'글리치', u'화면에 내 이름 떠 있어. 진짜 오랜만에 본다. …생각보다 평범하네.'), (u'지휘관', u'아까우면 안 태워도 돼.'), (u'글리치', u'아니야. 이건 걔가 알던 내 이름이고, 지금 나는 네가 부르는 이름으로 살 거야. 잘 가.')]),
       (u'③ 클리어', [(u'글리치', u'로그아웃 완료. 와, 손 떨려. 이거 봐, 아직도 떨려.'), (u'글리치', u'…오늘은 화면 말고 직접 갈게. 문 좀 열어 줘.')])]),
]
