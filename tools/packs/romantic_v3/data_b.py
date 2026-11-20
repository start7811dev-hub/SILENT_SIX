# -*- coding: utf-8 -*-
# 로맨틱 미션 맵 제작 데이터 (브릭 · 미라주 · 닥).
T = {}
T['brick'] = [
 dict(t=u'닫힌 문', place_ko=u'폐쇄된 지하 벙커', m=24, io='in', light=u"Underground. Bare concrete, rust streaks, caged work lamps, dust hanging in the air.",
  place=u"The interior of a sealed military bunker: nine thick-walled chambers in a three-by-three grid.",
  lay=u'''**Nine chambers.** The whole plan is a **3 x 3 grid of square concrete chambers, each about 6.5 x 6.5 m inside, separated by walls 1 m thick**. There is no corridor: you go from chamber to chamber. Rule 3 (a lane around all four sides) does not apply.

Name the chambers by row and position. **Row 1** touches the lower-left side, **Row 2** is the middle, **Row 3** touches the upper-right side. In each row, **L** is the end nearer the upper-left side, **C** the centre, **R** the end nearer the lower-right side. So chamber **1R is at the BOTTOM corner**, **3L is at the TOP corner**, 1L at the LEFT corner, 3R at the RIGHT corner, and **2C is the centre** of the map.

**Blast doorways (clean rectangular openings, 2 m wide, steel frame, door swung fully open):** 1R-1C, 1C-2C, 2C-2R, 2R-3R, 3R-3C, 3C-3L. These six make one long winding route from 1R to 3L.

**Breaches (ragged holes 2 m wide, broken concrete edges, bent reinforcing bars, rubble dust on the floor):** 1R-2R, 1C-1L, 1L-2L, 2L-2C, 2L-3L, 2C-3C. These six are shortcuts.

**No other openings.** Every other wall between chambers is solid.

**Fixed contents.** 2C: a **ventilation fan housing**, 3 x 3 m, in its centre, with a round grille on top. 3L: built-in concrete bunks along two walls. 1L: a built-in water cistern along one wall. 3R: a row of built-in steel lockers along one wall. 1R: the entrance.

**Way in:** a short stair coming down into chamber 1R through its near wall, with a floor hazard stripe.''',
  chk=[u'방이 가로 3 × 세로 3으로 9개다', u'방 사이에 복도가 없고 벽이 두껍다', u'반듯한 철문 자리가 6곳, 깨진 구멍이 6곳이다', u'한가운데 방에 큰 환기 팬이 있다', u'맨 위 모서리 방에 콘크리트 침상이 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"**A cracked concrete wall plug**: a slab of cracked concrete that exactly fills a 2 m wide wall breach, 1 x 2 m, 2.4 m high, with wide cracks and one corner crumbling, orientation 1. It fills about 80% of the cell's height.", u"The same cracked wall plug, orientation 2.", u"A pile of concrete rubble and bent bars, waist-high, 1 x 1 m.", u"A stack of military ammunition crates, waist-high, 1 x 2 m, orientation 1.", u"A rusted steel bunk frame tipped on its side, waist-high, 1 x 2 m, orientation 1.", u"A row of steel fuel drums, 1 x 2 m, waist-high, orientation 1."]),
         (u'special', u'목표 · 환경', u'', [u"**The objective**: four military identity tags on their chains hanging from a nail above a scratched tally of marks on a slab of concrete, drawn large, lit by a caged lamp.", u"A wall switch box for the ventilation fan with a big lever and one green lamp, drawn large.", u"A caged work lamp on a tripod, lit, 1 x 1 m, 2 m high.", u"A guard's camp table with a radio, mess tins and a lantern, waist-high, 1 x 1 m.", u"A steel blast door leaf, closed, 1 x 2 m, 2.4 m high, orientation 1.", u"The same blast door leaf, orientation 2."])],
  info=[u'환경: 돌파. 금 간 벽 6곳을 브릭이 부숴 길을 낸다. 부수는 소리는 8칸까지 들린다. 환기 팬이 도는 동안(18초마다 6초)에만 소리가 묻힌다. 팬 스위치를 켜면 30초 동안 계속 돈다(1회).', u'목표: 맨 위 방에서 인식표 넷을 찾는다.', u'배지: 무살상', u'엔진: 돌파는 기존 기능. 소음 가림(주기)은 종소리 처리. 금 간 벽이 낱개라서 부순 뒤 그림을 바꾸지 않아도 된다.'],
  dlg=[(u'① 시작 전', [(u'브릭', u'야, 지휘관! 나 오늘 어디 가는지 알지? 그 벙커야. 문 못 열고 서 있기만 했던 데.'), (u'지휘관', u'허가는 안 났어. 지원도 없고.'), (u'브릭', u'그때도 허가가 안 나서 못 열었잖아. 오늘은 허가 안 받고 연다. 그게 다야!')]),
       (u'② 인식표 앞', [(u'브릭', u'…넷 다 있어. 못에 걸어 놨네. 누가 일부러 걸어 둔 거야.'), (u'지휘관', u'벽에 뭐가 적혀 있어?'), (u'브릭', u'날짜. 하루에 한 줄씩. 사백 줄이 넘어. 얘들, 문 닫히고도 일 년을 넘게 살아 있었어.')]),
       (u'③ 클리어', [(u'브릭', u'시신은 없어. 끌려 나간 거야. 발자국이 넷이 아니라 다섯이거든.'), (u'브릭', u'괜찮아, 안 울어. …좀 울었어. 다음은 격투장이다.')])]),
 dict(t=u'인식표', place_ko=u'지하 격투장', m=26, io='in', light=u"A converted warehouse at night. One hard pool of white light on the ring, everything around it in smoky darkness, a few red bulbs.",
  place=u"The interior of an illegal fight club in a warehouse: a ring in the middle, bleachers on three sides, back rooms and a row of holding cells.",
  lay=u'''**Ring.** The exact centre: a raised square boxing ring, 6 x 6 m, with corner posts and ropes. Solid, not walkable.

**Ringside lane.** A 2 m clear lane all the way around the ring.

**Bleachers.** On **three sides** of the ring (the two far sides and the lower-left side), a block of stepped timber bleachers, each block **10 m long and 3 m deep**, rising away from the ring. **Empty: no spectators.** Solid. There is a **2 m gap at each end of every block**. The fourth side (toward the lower-right side) has no bleachers: it is an open floor 6 m deep.

**Back lanes.** Behind each of the three bleacher blocks, a dark lane 2.5 m wide.

**Rooms along the upper-left side**, from the LEFT end: the **fighters' room**, 5 x 6 m, with built-in benches; then the **office**, 5 x 5 m, with a built-in counter and a small window slot. One doorway each onto the back lane.

**Rooms along the upper-right side**, from the RIGHT end: a **storage cage** of steel mesh, 4 x 6 m, one gate; then a fixed **bar counter**, 1 x 6 m.

**Holding cells.** At the TOP corner: a short barred passage 2 m wide with **three cells in a row, each 3 x 3 m, barred fronts, cell doors standing open**.

**Way in:** a loading door in the near wall at the BOTTOM corner, with a floor hazard stripe.''',
  chk=[u'한가운데에 링이 있고 둘레에 통로가 있다', u'관중석이 세 면에만 있고 비어 있다', u'관중석 뒤로 어두운 골목이 있다', u'왼쪽 위에 대기실과 사무실, 오른쪽 위에 철망 창고와 바가 있다', u'맨 위 모서리에 감방 3칸이 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"**A block of spectators**: a tight crowd of about fifteen people in dark coats seen from behind and above, standing and shouting, arms raised, to sit on a bleacher, 2 x 4 m, orientation 1. No faces in detail.", u"The same crowd block, orientation 2.", u"A betting table with cash boxes and a lamp, waist-high, 1 x 2 m, orientation 1.", u"Stacked beer crates and kegs, waist-high, 1 x 1 m.", u"A corner stool, bucket and towel set, low, 1 x 1 m.", u"A heavy punch bag hanging in a steel frame, 1 x 1 m, 2.2 m high."]),
         (u'special', u'목표 · 환경 · 인물', u'', [u"**The comrade**, as a small figure for the map: a tall gaunt man in his thirties, shaved head, torn grey vest, bandaged fists, one eye swollen, standing but stooped, seen from the map camera, full body, drawn large (about 420 px tall), facing lower-left.", u"The same man sitting on the floor against a wall, head down.", u"Two fighters in the ring seen from above, mid-clinch, drawn as one group to sit on the ring.", u"A ring bell on a small table with a hammer, drawn large.", u"A hanging ring light: a square steel truss with four hot lamps, seen from above.", u"A cell door key ring on a hook board, drawn large."])],
  info=[u'환경: 관중. 16초마다 5초 동안 함성이 터져 소리가 묻힌다. 링 조명 안(링과 둘레 통로)은 경비 시야 1.3배, 관중석 뒤는 0.7배.', u'목표: 감방의 동료를 데리고 처음 들어온 문으로 나간다(호위). 동료는 뛰지 못한다.', u'배지: 원테이크', u'엔진: 호위는 블러디 3판 증인 처리. 소음 가림(주기)은 종소리 처리.'],
  dlg=[(u'① 시작 전', [(u'브릭', u'여기서 싸움 붙이는 애들 중에 군번 달고 뛰는 놈이 있대. 우리 분대 번호로.'), (u'지휘관', u'데리고 나오면 걷지도 못할 수 있어.'), (u'브릭', u'그럼 업지 뭐! 내가 뭐 하러 이 덩치겠어.')]),
       (u'② 감방 앞', [(u'동료', u'…분대장? 진짜야? 귀신 아니고?'), (u'브릭', u'귀신이 이렇게 시끄럽냐. 일어나, 막내. 집에 가자.'), (u'동료', u'문 밖에서 소리 들었어요. 그날. 분대장이 문 두드리는 소리. 그래서 버텼어요.')]),
       (u'③ 클리어', [(u'브릭', u'하나 찾았다! 하나! 들었지? 내가 뭐랬어, 살아 있다고 했잖아!'), (u'브릭', u'나머지 셋은 채석장이래. 내가 아침마다 돌 깨러 가던 데 바로 밑이야. 하, 진짜.')])],
  npc=(u'동료(분대 막내)', u"**The comrade.** A tall, gaunt man in his early thirties, once a combat engineer: shaved head, hollow cheeks, one eye swollen shut, a split lip, a torn grey vest, **bandaged fists**, an old set of dog tags missing from his neck (only the tan line). He **faces RIGHT** (toward the agent he is talking to).", [u"staring in disbelief, mouth half open, one hand gripping a cell bar.", u"the same man, crying and laughing at once, head ducked, the back of one bandaged hand against his eyes."])),
 dict(t=u'노크', place_ko=u'채석장 발파 구역', m=28, io='out', light=u"Pre-dawn. Grey stone, dust haze, sodium work lamps, a red warning beacon.",
  place=u"A working quarry cut into three terraces that step up from the near side to the far side.",
  lay=u'''**Three terraces.** The floor is cut into **three flat terraces, each a strip about 8 m deep running the full width of the map parallel to the lower-left side**. The **lower terrace** touches the lower-left side, the **middle terrace** is 2 m higher, the **upper terrace** is 2 m higher again and touches the upper-right side. Between terraces is a **vertical cut rock face 2 m high**: solid.

**Ramps (the only ways up).** Lower to middle: **two rock ramps, each 3 m wide**, one near the upper-left side and one in the centre. Middle to upper: **two ramps**, one near the lower-right side and one a third of the way from the upper-left side. The ramps are not lined up.

**Lower terrace.** From the upper-left end: two **site cabins**, each 3 x 6 m, roof removed, one doorway each, with a 2 m gap between them; then a flat steel **weighbridge plate**, 3 x 8 m, set flush in the ground.

**Middle terrace.** A fixed **stone crusher**, 5 x 8 m, tall and solid, with one conveyor arm resting on the upper rock face. Further along, **three concrete-walled stockpile bays**, each 4 x 4 m, open on the near side, walls 2 m high, with a heap of crushed stone inside each.

**Upper terrace.** Toward the RIGHT corner: the **explosives magazine**, a concrete bunker 4 x 5 m, roof on, steel door facing the terrace, surrounded on three sides by an earth bank. Toward the TOP corner: the **blast bench**, a flat area 8 x 6 m marked off by red-and-white stakes, its floor dotted with a neat grid of drill holes.

**Edges.** The two far sides are the high quarry wall. **Way in:** a gate in the low fence on the lower-left side near the BOTTOM corner.''',
  chk=[u'계단식 단이 3개이고 왼쪽 아래 변과 나란하다', u'단 사이가 수직 암벽이고 경사로로만 오른다', u'경사로가 아래-가운데 2개, 가운데-위 2개이고 서로 어긋나 있다', u'가운데 단에 파쇄기와 골재 칸 3개가 있다', u'위 단에 흙둑으로 둘러싼 화약고와 말뚝으로 표시한 발파 구역이 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"A rough-cut granite block, waist-high, 1 x 1 m.", u"Two granite blocks stacked, 1 x 1 m, 2 m high.", u"A wheel loader with its bucket down, 3 x 5 m, orientation 1.", u"The same wheel loader, orientation 2.", u"A rock drill rig on tracks with its mast up, 2 x 3 m, 3 m high, orientation 1.", u"A stack of wooden pallets with coiled detonator cord, waist-high, 1 x 1 m."]),
         (u'special', u'목표 · 환경 · 인물', u'', [u"**Three comrades**, as one small group for the map: three thin men in dust-grey work overalls with ankle chains, sitting close together against a wall, one with a hand raised against the light, seen from the map camera, drawn large.", u"The same three men standing, the middle one supported by the other two.", u"A blast warning siren on a pole with a red rotating beacon, lit, 1 x 1 m, 3 m high.", u"A burst of rock dust and smoke, soft-edged, about 5 x 4 m, on the flat background.", u"A heavy steel door leaf with a wheel lock, open at 90 degrees, 1 x 2 m, orientation 1.", u"A dump truck, empty, 3 x 6 m, orientation 1."])],
  info=[u'환경: 발파. 30초마다 사이렌 3초 뒤 발파. 발파 뒤 8초 동안 먼지로 모두의 시야가 0.4배가 되고 소리가 묻힌다. 발파 순간 발파 구역 안에 있으면 실패.', u'목표: 화약고에 갇힌 셋을 찾고(문을 부수지 않고 연다), 나오면서 문을 닫는다(문 열기 → 문 닫기, 두 단계).', u'배지: 무발포', u'엔진: 발파는 소음 가림 + 시야 감소를 한 주기에 묶는다. 높낮이는 그림으로만 표현하고 판정은 벽(암벽)으로 처리한다.'],
  dlg=[(u'① 시작 전', [(u'브릭', u'사이렌 울리고 셋 세면 터져. 내가 여기서 아침마다 일했잖아. 박자는 몸이 알아.'), (u'지휘관', u'화약고 문은 부수면 안 돼.'), (u'브릭', u'알아. 오늘은 부수는 날이 아니야. 두드리는 날이지.')]),
       (u'② 화약고 문', [(u'브릭', u'(똑, 똑, 똑.) 야. 나야. 늦어서 미안하다.'), (u'동료들', u'…분대장? 분대장 목소리다. 야, 일어나 봐, 분대장이야!'), (u'브릭', u'문 연다. 이번엔 진짜로 연다. 물러서 있어.')]),
       (u'③ 클리어', [(u'브릭', u'넷 다 찾았어. 넷 다 숨 쉬어. 고양이 이름 바꿔야겠다, 헷갈리니까.'), (u'브릭', u'문은 닫고 왔어. 조용히. …지휘관, 나 오늘 밥 8인분 해도 되지?')])]),
]
T['mirage'] = [
 dict(t=u'초대장', place_ko=u'야간 유람선', m=30, io='in', light=u"Night on a river. Warm gold light from the ship's windows and deck lamps, black water with city reflections.",
  place=u"The main deck of a river cruise ship, seen with the upper decks removed, floating in black water.",
  lay=u'''**This map is a ship in water.** The whole diamond is black river water with reflections. In it lies **one ship deck: a rectangle 14 m wide and 30 m long, its long axis parallel to the lower-left side**, centred in the diamond, with a blunt bow toward the upper-left side and a square stern toward the lower-right side. Water is **not walkable**. Rule 3 (a lane around all four sides) does not apply.

**Side decks.** Along **both long sides of the ship**, an open promenade deck **2 m wide** with a low rail, running the full length from stern to bow.

**Inside the ship, between the side decks (10 m wide), from stern to bow:**
1. **Stern deck**, 5 m long: open, full width, with a gangway opening in the stern rail.
2. **Banquet hall**, 9 m long: one room, a built-in bar along its bow-side wall, a doorway to each side deck and a wide doorway to the stern deck.
3. **Cabin block**, 9 m long: a **central corridor 2 m wide** running stern to bow, with **three cabins on each side, each 3 x 4 m, each with one doorway to the corridor**. A doorway joins the corridor to the banquet hall and another to the stair lobby.
4. **Stair lobby**, 3 m long: a full-width space with a closed engine-room hatch in the floor and a doorway to each side deck.
5. **Owner's suite**, 5 m long: one full-width room with a built-in bed platform and a writing desk, one doorway from the stair lobby.
6. **Bow deck**, 4 m long: open, with an anchor winch fixed in the centre.

All interior walls are cut at one height with a flat dark top; the two near walls of the ship are cut low.

**Way in:** the gangway opening at the stern.''',
  chk=[u'검은 물 위에 길쭉한 배 한 척이 있다', u'배 양옆으로 좁은 갑판이 처음부터 끝까지 이어진다', u'안쪽이 선미 갑판 → 연회장 → 선실 구역 → 계단 로비 → 선주 객실 → 선수 갑판 순서다', u'선실 구역 가운데 복도 양쪽에 선실이 3개씩 있다', u'가까운 쪽 벽이 낮아서 안이 보인다'],
  props=[(u'cover', u'엄폐물', u'', [u"A round banquet table with a white cloth and candles, waist-high, 1 x 1 m.", u"A buffet trolley with a silver cloche, waist-high, 1 x 2 m, orientation 1.", u"A grand piano with its lid down, waist-high, 2 x 2 m.", u"A deck life-raft canister in its cradle, waist-high, 1 x 1 m.", u"**A cabin door**, closed, in a slice of wall, 1 x 1 m, 2.2 m high, orientation 1.", u"The same cabin door, orientation 2."]),
         (u'special', u'목표 · 환경', u'', [u"**The objective**: a writing desk with a single cream envelope under a brass lamp and a half-finished glass of red wine, drawn large.", u"A crew uniform on a hanger: white jacket, black trousers, a cap, drawn large.", u"A group of four party guests in evening dress seen from above, chatting with glasses, drawn as one group, 2 x 2 m.", u"A deck lamp on a brass post, lit, 1 x 1 m.", u"A stack of deck chairs, folded, waist-high, 1 x 1 m.", u"A lifebuoy on a stand with a coiled line, 1 x 1 m."])],
  info=[u'환경: 변장과 흔들림. 미라주는 승무원 복장이라 승객 구역에서 의심이 느리게 찬다. 선실 복도에서는 승무원도 의심받는다. 15초마다 배가 흔들려 선실 문 6개가 3초 동안 열린다(문 안에서 밖이 보인다).', u'목표: 선주 객실에서 초대장을 보낸 사람이 누구인지 확인한다.', u'배지: 유령', u'엔진: 변장은 기존 기능. 문이 주기로 열리는 처리는 새로 만든다(바이퍼 2판의 문과 같이).'],
  dlg=[(u'① 시작 전', [(u'미라주', u'초대장에 내 본명이 적혀 있었어. 그 이름 아는 사람, 이제 셋도 안 남았는데.'), (u'지휘관', u'덫일 수 있어.'), (u'미라주', u'그럴지도. 근데 덫을 놓는 사람은 보통 이름에 꽃무늬 봉투를 쓰진 않거든. 가서 볼게.')]),
       (u'② 선주 객실', [(u'미라주', u'봉투가 하나 더 있네. 이번엔 안 부쳤어. "네가 누군지 3년 전에 알았다. 말하지 않았다."'), (u'지휘관', u'누구 글씨인지 알아?'), (u'미라주', u'알지. 내가 속여야 했던 사람이야. 유일하게 미안했던 사람이고.')]),
       (u'③ 클리어', [(u'미라주', u'객실은 비어 있었어. 대신 표가 한 장 있더라. 내일 밤 오페라, 무대 뒤 출입증.'), (u'미라주', u'초대가 계속되네. 이쯤 되면 예의상 가 줘야지.')])]),
 dict(t=u'역할', place_ko=u'오페라 극장 무대 뒤', m=26, io='in', light=u"During a performance. A bright stage seen from behind, dark wings, blue running lights, warm dressing-room bulbs.",
  place=u"The backstage of an opera house: the stage floor, its two wings, a cross-over corridor, dressing rooms and a prop store.",
  lay=u'''**Stage.** A bare timber stage floor, **12 x 9 m**, in the half of the map nearer the lower-right side, its long side parallel to the lower-right side. **Nothing stands on it.** Its edge toward the lower-right side is the front of the stage: beyond a low footlight rail there is only darkness (the auditorium), no seats drawn.

**Wings.** On each short side of the stage, a **wing 4 m wide** and as deep as the stage, with a fixed rope-and-pin rail along its outer wall.

**Back wall and cross-over.** Behind the stage (on its upper-left side) a solid wall with **two doorways**, one near each end. Behind that wall, a **cross-over corridor 2.5 m wide** runs the full width of the map.

**Rooms along the upper-left side**, behind the cross-over, from the LEFT end to the TOP end: the **prop store**, 6 x 6 m, with built-in racking along two walls; **three dressing rooms**, each 4 x 4 m, each with a mirror counter built along one wall; and the **star dressing room**, 5 x 6 m, with a mirror counter and a built-in wardrobe. One doorway each onto the cross-over.

**Gallery.** Along the upper-right side, a raised steel **gallery walkway 2 m wide**, 1 m above the floor, running from the cross-over to the front of the stage, with a straight flight of steps at each end. It overlooks the right wing.

**Stage door.** At the BOTTOM corner, in the left wing's near wall: the way in, with a floor hazard stripe.''',
  chk=[u'무대 바닥이 비어 있고 오른쪽 아래 변 쪽이 객석(어둠)이다', u'무대 양옆에 날개 공간이 있다', u'무대 뒤 벽에 문이 2곳이고 그 뒤에 긴 복도가 있다', u'왼쪽 위 변을 따라 소품 창고, 분장실 3개, 주연 분장실이 있다', u'오른쪽 위 변을 따라 한 단 높은 통로가 있고 양 끝에 계단이 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"**A scenery flat**: a tall painted canvas wall on a wheeled frame, showing a painted stone arch, 1 x 4 m, 3 m high, orientation 1.", u"The same scenery flat, orientation 2.", u"**A stage curtain leg**: a tall narrow hanging of deep red velvet, 1 x 2 m, 3.5 m high, orientation 1.", u"A costume rail full of dresses, 1 x 2 m, 1.8 m high, orientation 1.", u"A prop table with a crown, goblets and a skull, waist-high, 1 x 2 m, orientation 1.", u"A wicker costume hamper, waist-high, 1 x 1 m."]),
         (u'special', u'목표 · 환경', u'', [u"**The objective**: an old photograph in a small silver frame leaning against a dressing-room mirror ringed with bulbs, a single rose beside it, drawn large.", u"A stage manager's prompt desk with a lit console and a headset, waist-high, 1 x 1 m.", u"A singer in a huge period gown seen from above and behind, arms spread, to stand on the stage.", u"A follow-spot circle of hard white light on the flat background, about 3 x 3 m, soft edge.", u"A stagehand's rope lock lever on a base, drawn large.", u"A music stand with a lamp and a stool, 1 x 1 m."])],
  info=[u'환경: 공연. 24초마다 8초 동안 음악이 커져 소리가 묻힌다. 조명 큐가 12초마다 바뀌어 무대 뒤 왼쪽과 오른쪽 가운데 한쪽만 밝다(밝은 쪽 경비 시야 1.2배). 로프 레버(2곳)를 당기면 무대 장치 한 장이 옆으로 2칸 움직인다.', u'목표: 그가 후원자 자격으로 쓰는 주연 분장실에서 옛 사진을 회수한다.', u'배지: 무의심', u'엔진: 무대 장치 이동은 레이븐 2판 서가와 같은 처리. 소음 가림은 종소리 처리.'],
  dlg=[(u'① 시작 전', [(u'미라주', u'무대 뒤는 내 집 같은 데야. 다들 누군가인 척하고 있고, 아무도 서로 안 쳐다보지.'), (u'지휘관', u'오늘은 누구로 들어가?'), (u'미라주', u'그게 문제야. 초대받은 건 본명인데, 그 사람으로 걸어 본 지가 너무 오래됐어.')]),
       (u'② 분장실', [(u'미라주', u'사진이 있어. 나야. 딜러 조끼 입고 있네. 사흘째 날이야. 웃고 있어, 연기 아닌 걸로.'), (u'지휘관', u'그 사람이 갖고 있었던 거야?'), (u'미라주', u'3년을. 거울 옆에 세워 두고. …화장 번지면 안 되는데, 큰일이네.')]),
       (u'③ 클리어', [(u'미라주', u'안내원이 그러는데, 그 사람 오늘 자기 자리에 안 왔대. 어제 회사 사람들이 데려갔다고.'), (u'미라주', u'3년 동안 입 다문 걸 헬리오스한테 들킨 거야. 나 때문에. 가야겠어.')])]),
 dict(t=u'맨얼굴', place_ko=u'문 닫은 백화점', m=26, io='in', light=u"After closing. Most lights off, cold security lighting, lit shop windows, glints on glass and chrome.",
  place=u"One sales floor of a closed department store: an escalator well in the middle, aisles in a cross, show windows, fitting rooms, a security office and a stock room.",
  lay=u'''**Escalator well.** The exact centre: an opening 6 x 6 m with a pair of stopped escalators and a glass balustrade. Solid, not walkable.

**Aisles.** A **ring aisle 2.5 m wide around the escalator well**, a **ring aisle 2.5 m wide around the inside of the four sides**, and **four straight aisles 2.5 m wide joining the two rings**, one toward the middle of each side, making a cross. The floor of the aisles is pale marble; the four department floors between them are dark carpet. **The four departments are empty floor.**

**Columns.** Square mirrored columns, 1 x 1 m, one at each corner of each department (sixteen in all).

**Show windows.** Along the **lower-right side**, a row of five display bays, each 4 m wide and 2 m deep, with a 0.5 m raised floor and glass toward the street. Empty.

**Fitting rooms.** Along the upper-left side, in the department nearest the LEFT corner: a block 4 x 8 m of **four fitting stalls with curtains drawn open** and a 1.5 m passage in front.

**Cosmetics islands.** In the department nearest the BOTTOM corner: two fixed square counter islands, each 3 x 3 m, counters around a hollow centre with one gap.

**Security office.** At the RIGHT corner: 5 x 5 m, a built-in monitor desk, one doorway.

**Stock room.** At the TOP corner: 6 x 8 m, built-in shelving along two walls, one doorway.

**Way in:** a staff door in the near wall at the BOTTOM corner, with a floor hazard stripe.''',
  chk=[u'한가운데에 멈춘 에스컬레이터 구멍이 있다', u'통로가 안쪽 고리, 바깥 고리, 그 둘을 잇는 십자로 나 있다', u'매장 네 구역 바닥이 비어 있다', u'오른쪽 아래 변을 따라 쇼윈도 칸 5개가 있다', u'탈의실 4칸, 화장품 섬 2개, 보안실, 창고가 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"**A mannequin group**: three featureless white mannequins in evening wear standing on a low round plinth, 1 x 1 m, 2 m high.", u"A single white mannequin in a long coat, standing, 1 x 1 m, 2 m high.", u"A single white mannequin, seated on a cube, 1 x 1 m.", u"A circular clothes rack full of dresses, waist-high plus, 1 x 1 m, 1.5 m high.", u"A straight clothes rail of coats, 1 x 2 m, 1.8 m high, orientation 1.", u"A glass jewellery display case, lit, waist-high, 1 x 2 m, orientation 1."]),
         (u'special', u'목표 · 환경 · 인물', u'', [u"**The man**, as a small figure for the map: a slim man in his late thirties in a rumpled white dress shirt and loosened dark tie, wrists tied, sitting on a chair, seen from the map camera, full body, drawn large (about 420 px tall), facing lower-left.", u"The same man standing, rubbing one wrist, facing lower-left.", u"An empty low round mannequin plinth with a small spotlight on it, 1 x 1 m.", u"A security guard's patrol torch beam on the flat background, a long soft cone about 5 x 2 m.", u"A cut rope and an overturned chair, low, 1 x 1 m.", u"A tall perfume advertising stand with an abstract bottle shape (no text), 1 x 1 m, 2 m high."])],
  info=[u'환경: 마네킹. 마네킹 받침(8곳) 옆 칸에서 멈춰 있으면 경비가 지나친다. 움직이는 순간 평소보다 빨리 들킨다(의심 2배). 경비는 손전등을 들어 시야가 좁고 길다.', u'목표: 창고에 묶인 그를 풀어 준다. 그는 혼자 다른 문으로 나가고, 미라주는 돌아보지 않고 들어온 문으로 나간다.', u'배지: 무살상', u'엔진: 정지 은폐는 새로 만든다. 좁고 긴 시야는 경비 속성으로 추가한다.'],
  dlg=[(u'① 시작 전', [(u'미라주', u'오늘은 화장을 안 했어. 가발도, 억양도. 좀 이상하다, 맨얼굴로 일하러 가는 거.'), (u'지휘관', u'마네킹 옆에서 멈추면 지나쳐. 움직이면 끝이고.'), (u'미라주', u'가만히 서 있는 건 자신 있어. 평생 남이 봐 주길 기다리는 역만 했거든.')]),
       (u'② 창고', [(u'그', u'…왔네. 본명으로 부르면 화낼 건가?'), (u'미라주', u'오늘은 괜찮아. 3년이나 입 다물어 줘서 고마워. 그리고 속여서 미안해. 이건 연기 아니야.'), (u'그', u'알아. 넌 거짓말할 때 왼쪽 눈썹이 올라가거든. 지금은 안 올라갔어.')]),
       (u'③ 클리어', [(u'미라주', u'그 사람은 뒷문으로 보냈어. 나는 안 돌아봤고. 돌아보면 따라갈 것 같아서.'), (u'미라주', u'…지휘관. 오늘은 가면 없이 가도 돼? 네 앞에서도.')])],
  npc=(u'그(초대장을 보낸 사람)', u"**The man.** A slim man in his late thirties, a corporate lawyer: neat dark hair now dishevelled, a kind tired face, a day of stubble, a **rumpled white dress shirt with a loosened dark tie**, suit jacket gone, rope marks on his wrists. He **faces RIGHT** (toward the agent he is talking to).", [u"seated, wrists tied in front of him, looking up with a small wry smile of recognition.", u"the same man, hands free, one hand rubbing his wrist, looking straight at the viewer, gentle and steady."])),
]
T['doc'] = [
 dict(t=u'차트', place_ko=u'폐병원 지하 기록실', m=24, io='in', light=u"A flooded basement. Flickering fluorescent tubes, green-tiled walls, black standing water with reflections, a red glow from the boiler.",
  place=u"The basement of an abandoned hospital: two long corridors joined by three passages, with a chart archive, a morgue, a boiler room and a laundry.",
  lay=u'''**Two corridors.** Two straight corridors, each **2.5 m wide, both parallel to the lower-left side**, run the full width of the map. The **near corridor** is 6 m from the lower-left side; the **far corridor** is 6 m from the upper-right side. Rule 3 (a lane around all four sides) does not apply.

**Three cross passages**, each 2.5 m wide, join the two corridors: one near the upper-left side, one in the centre, one near the lower-right side.

**Water.** The **whole near corridor and the centre cross passage are flooded**: ankle-deep black water, clearly wet, with ripples and floating paper. **It is walkable.** The far corridor and the other two cross passages are dry tile.

**Rooms between the lower-left side and the near corridor**, from the LEFT end: the **laundry**, 5 x 6 m, flooded, with two fixed industrial washers; the **stair lobby**, 5 x 6 m, dry, at the BOTTOM corner, with a stair coming down.

**Rooms between the two corridors** (two blocks, split by the centre passage): toward the upper-left side, the **morgue**, 6 x 7 m, with a wall of body lockers and two fixed steel slabs; toward the lower-right side, the **boiler room**, 6 x 7 m, with one big boiler (3 x 4 m, fixed, glowing) and pipes along the walls. One doorway each, onto the far corridor.

**Rooms between the far corridor and the upper-right side:** the **chart archive**, 7 x 12 m, toward the TOP corner, with **four fixed rows of steel shelving parallel to the upper-right side** and a records desk at its far end, two doorways; and a small **pharmacy store**, 4 x 5 m, toward the RIGHT corner.

**Way in:** the stair in the stair lobby.''',
  chk=[u'긴 복도 2개가 왼쪽 아래 변과 나란하고, 가로 통로 3개가 둘을 잇는다', u'가까운 복도와 가운데 통로만 물에 잠겨 있다', u'두 복도 사이에 영안실과 보일러실이 있다', u'먼 쪽에 서가 4줄이 있는 차트 서고가 있다', u'맨 아래 모서리에 계단 로비가 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"A hospital gurney with a stained sheet, waist-high, 1 x 2 m, orientation 1.", u"The same gurney, orientation 2.", u"A tipped filing cabinet with charts spilling out, waist-high, 1 x 1 m.", u"A linen cart piled with grey laundry, waist-high, 1 x 1 m.", u"An oxygen cylinder rack with four cylinders, 1 x 1 m, 1.8 m high.", u"A wheelchair, 1 x 1 m, waist-high."]),
         (u'special', u'목표 · 환경', u'', [u"**The objective**: one open medical chart on a records desk under a green-shaded lamp, a pen across it, drawn large.", u"A boiler pressure valve wheel with a round gauge on a pipe stand, drawn large.", u"A plank walkway: two scaffold boards laid on bricks, low, 1 x 3 m, orientation 1.", u"The same plank walkway, orientation 2.", u"A ring of ripples on black water, soft-edged, about 2 x 2 m, on the flat background.", u"A guard's battery lantern on an upturned bucket, lit, 1 x 1 m."])],
  info=[u'환경: 침수. 물에서는 걸어도 발소리가 5칸까지 들린다. 20초마다 6초 동안 보일러가 울려 소리가 묻힌다. 판자 다리(2곳)를 놓으면 그 칸은 마른 길이 된다.', u'목표: 차트 서고에서 "수술 중 사망"으로 닫힌 선임의 차트를 찾는다.', u'배지: 무의심', u'엔진: 물 칸 소음은 새로 만든다. 소음 가림은 종소리 처리.'],
  dlg=[(u'① 시작 전', [(u'닥', u'가운은 안 벗었어. 근무 끝나고 바로 온 거라. 뭐, 진료 보러 가는 거니까 맞는 옷이지.'), (u'지휘관', u'10년 전에 닫힌 차트야. 남아 있을까?'), (u'닥', u'병원은 사람은 잃어버려도 서류는 안 버려. 내가 장담해. 발만 좀 젖겠네.')]),
       (u'② 차트 앞', [(u'닥', u'찾았어. …"수술 중 사망". 서명란에 내 이름이 있는데, 내 글씨가 아니야.'), (u'지휘관', u'누가 고쳐 쓴 거야?'), (u'닥', u'몰라. 근데 뒷장에 이송 기록이 붙어 있어. 죽은 사람을 왜 헬기로 옮겨?')]),
       (u'③ 클리어', [(u'닥', u'선임은 그날 밤 안 죽었어. 난 10년 동안 그렇게 말했고 아무도 안 믿었지. 이제 종이가 내 편이야.'), (u'닥', u'옥상 헬기장에 운항 일지가 있을 거야. 어디로 데려갔는지 봐야겠어.')])]),
 dict(t=u'이송', place_ko=u'병원 옥상 헬기장', m=28, io='out', light=u"Night, strong wind. A hospital rooftop: green perimeter lights around the pad, steam from vents, the city glow far below.",
  place=u"A hospital rooftop: a plant zone of big air-handling units with lanes between them, and a helipad beyond.",
  lay=u'''**Parapet.** A low parapet around all four sides (1 m on the near sides).

**Plant zone.** The near half of the roof. **Six big air-handling units, each a steel box 3 x 6 m and 2.5 m tall, arranged in two rows of three, all with their long sides parallel to the lower-left side.** **2.5 m lanes between the units and between the rows**, forming a grid of alleys. Thick ducts run **flat along the tops** of the units only, never across the lanes.

**Stair bulkhead.** At the BOTTOM corner: a solid block 4 x 4 m with a door facing the centre. The way in.

**Lift machine room.** At the LEFT corner: a solid block 4 x 5 m.

**Helipad.** The far half: a **square pad 12 x 12 m, raised 0.5 m**, with a painted circle and a painted cross (no letter), green lights along its edge, and **two short ramps** up onto it from the plant zone side. The pad is empty.

**Flight hut.** Beside the pad, toward the TOP corner: a hut 4 x 5 m, roof removed, one doorway facing the pad, a built-in desk and a radio shelf.

**Fuel store.** Beside the pad, toward the RIGHT corner: a fenced cage 3 x 4 m with a fixed fuel tank.

**Vehicle ramp.** Along the upper-right side, a ramp 4 m wide slopes down out of the map toward the RIGHT corner (to the ambulance garage), with a low kerb.

**Windsock.** One mast on a 1 x 1 m base at the edge of the pad.''',
  chk=[u'가까운 절반에 큰 공조기 6대가 2줄로 있고 사이에 골목이 있다', u'먼 절반에 네모난 헬기장이 있고 비어 있다', u'헬기장 표시에 글자가 없다(원과 십자)', u'헬기장 옆에 운항실(위쪽)과 연료 창고(오른쪽)가 있다', u'오른쪽 위 변을 따라 내려가는 차량 경사로가 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"A rooftop exhaust fan cowl on a square base, waist-high, 1 x 1 m.", u"A stack of medical supply cases strapped on a pallet, waist-high, 1 x 1 m.", u"A stretcher trolley, folded, waist-high, 1 x 2 m, orientation 1.", u"A fire-hose reel cabinet, 1 x 1 m, 1.8 m high.", u"A fuel bowser cart with a hose, waist-high, 1 x 2 m, orientation 1.", u"A rooftop water tank on a low frame, 2 x 2 m, 2.2 m high."]),
         (u'special', u'목표 · 환경', u'', [u"**The objective**: a thick flight logbook, open, on a desk with a radio handset and a storm lantern, drawn large.", u"**A medical helicopter**, seen from the map camera, rotors still, doors shut, white with one lime-green stripe (no text), about 5 x 11 m, orientation 1. It fills about 90% of the cell's width.", u"The same helicopter with its rotors drawn as a blurred disc, orientation 1.", u"A search-light circle on the flat background: a hard white oval about 4 x 3 m with a soft edge.", u"A ground crew member in a hi-vis vest holding two light wands, seen from above.", u"A windsock, full and horizontal, on a short piece of mast."])],
  info=[u'환경: 헬기와 강풍. 40초 주기: 헬기가 내려와 12초 머물다 뜬다. 머무는 동안 소리가 묻히고, 내려오고 뜨는 6초씩은 탐조등이 옥상을 훑는다(움직이는 원 안은 엄폐 없으면 들킨다). 헬기가 앉아 있는 동안 헬기장은 지나갈 수 없다.', u'목표: 운항실에서 운항 일지를 가져온다.', u'배지: 유령', u'엔진: 헬기는 이미지 교체(블러디 5판 방식). 탐조등은 움직이는 카메라.'],
  dlg=[(u'① 시작 전', [(u'닥', u'이 병원 옥상, 인턴 때 몰래 올라와서 울던 데야. 헬기 소리가 커서 아무도 못 들었거든.'), (u'지휘관', u'오늘도 그 소리를 쓰면 돼. 내려앉아 있을 때만 움직여.'), (u'닥', u'응. 근데 오늘은 안 울어. 화가 나 있어서.')]),
       (u'② 운항 일지', [(u'닥', u'10년 전 그날 밤. 환자 한 명, 보호자 없음, 행선지… 요양원이야. 산속에 있는.'), (u'지휘관', u'요양원? 환자를 가두기엔 이상한 곳인데.'), (u'닥', u'아니야. 제일 좋은 곳이지. 요양원에서 10년 못 나오는 사람은 아무도 안 이상하게 봐.')]),
       (u'③ 클리어', [(u'닥', u'일지는 챙겼어. 마지막 장에 메모가 있더라. "환자는 매일 같은 이름을 부른다."'), (u'닥', u'…내 이름이래. 지휘관, 나 내일 왕진 좀 다녀올게. 멀리.')])]),
 dict(t=u'퇴원', place_ko=u'산속 요양원', m=30, io='out', light=u"Dawn fog in the mountains. Soft grey light, wet lawns, warm windows in the ward wing, lamps as blurred halos.",
  place=u"The grounds of a mountain sanatorium: a hedge maze garden, a glass greenhouse, a pavilion and a long ward wing.",
  lay=u'''**Ward wing.** Along the **whole upper-right side**, a single-storey building 6 m deep, roof removed. Inside, on its garden side, a **corridor 2 m wide** running the full length; behind the corridor, from the RIGHT end to the TOP end: a **nurses' station**, 4 x 4 m, with a built-in counter; then **four patient rooms**, each 4 x 4 m, each with one doorway to the corridor and one fixed bed platform. The room at the **TOP end** has a window bay. **Three doorways** lead from the corridor out to the garden.

**Terrace.** In front of the ward wing, a paved terrace 3 m deep along its full length.

**Hedge maze.** The middle of the map: a square garden **16 x 16 m**. **Clipped hedges 1 m thick and 2.2 m tall, all straight and axis-aligned, with gravel paths 2 m wide between them.** In the exact centre of the maze, an open square 5 x 5 m with a **dry stone fountain** (2 x 2 m, fixed). The maze has **three entrances on its near sides and three exits on its far sides**, and **at least three different routes through**, all passing near the centre square. Several short dead ends.

**Greenhouse.** At the LEFT corner, outside the maze: a glass house 6 x 10 m, parallel to the upper-left side, glass walls cut at 1.5 m, a doorway at each end, a straight central aisle with fixed planting benches on both sides.

**Pavilion.** At the RIGHT corner: an open timber pavilion 3 x 3 m, four posts, roof removed.

**Lawns and paths.** A gravel path 2.5 m wide runs around the outside of the maze and joins everything.

**Way in:** an iron gate in the low fence at the BOTTOM corner.''',
  chk=[u'가운데에 반듯한 생울타리 미로가 있고 길 폭이 넉넉하다', u'미로 한가운데에 마른 분수가 있는 네모 마당이 있다', u'미로 입구가 가까운 쪽 3곳, 출구가 먼 쪽 3곳이다', u'오른쪽 위 변 전체가 병동이고 복도와 병실 4개가 있다', u'왼쪽 모서리에 유리 온실, 오른쪽 모서리에 정자가 있다'],
  props=[(u'cover', u'엄폐물', u'', [u"A garden bench, waist-high, 1 x 2 m, orientation 1.", u"The same garden bench, orientation 2.", u"A stone urn planter with a clipped shrub, 1 x 1 m, 1.6 m high.", u"A gardener's wheelbarrow with tools, waist-high, 1 x 1 m.", u"A classical stone statue on a plinth, 1 x 1 m, 2.2 m high.", u"A laundry cart with folded white sheets, waist-high, 1 x 1 m."]),
         (u'special', u'목표 · 환경 · 인물', u'', [u"**The senior**, as a small figure for the map: a thin woman in her sixties with short white hair, in pale blue patient pyjamas and a grey cardigan, sitting very upright in a wheelchair, hands folded, seen from the map camera, full body, drawn large (about 420 px tall), facing lower-left.", u"The same woman walking slowly, one hand on a cane, facing lower-left.", u"A bank of thick fog, soft-edged, about 5 x 3 m, on the flat background.", u"A garden lamp on a short post with a blurred halo, lit, 1 x 1 m.", u"An orderly in white pushing an empty wheelchair, seen from above.", u"A bedside table with a water glass, a pill cup and a small framed photo, drawn large."])],
  info=[u'환경: 안개. 모두의 시야가 0.6배로 줄어든다. 생울타리가 시야를 끊어 모퉁이에서 갑자기 마주친다. 가로등(4곳) 아래는 시야가 평소와 같다.', u'목표: 맨 위 병실의 선임을 데리고 정문으로 나온다(호위). 선임은 지팡이를 짚고 걸어서 느리다. 휠체어는 쓰지 않는다.', u'배지: 무살상', u'엔진: 호위는 블러디 3판 처리. 안개는 전체 시야 배율(상시).'],
  dlg=[(u'① 시작 전', [(u'닥', u'왕진 가방 챙겼어. 청진기, 혈압계, 그리고 차트. 10년 묵은 거.'), (u'지휘관', u'휠체어로 나오는 게 빠를 텐데.'), (u'닥', u'안 돼. 제 발로 걸어서 나오게 할 거야. 그래야 퇴원이지. 실려 나오면 그건 이송이야.')]),
       (u'② 병실', [(u'닥', u'선생님. 저예요. 야간 근무 끝나고 왔어요. 좀 늦었죠.'), (u'선임', u'…늦기는. 인턴 때도 넌 꼭 회진 5분 전에 뛰어왔잖니. 차트는 가져왔어?'), (u'닥', u'가져왔어요. 맨 아래 칸이 비어 있어서요. 선생님이 걸어 나가시면 제가 채울게요.')]),
       (u'③ 클리어', [(u'닥', u'썼어. "퇴원." 내 글씨로. 10년 만에 차트 하나 닫았네.'), (u'닥', u'문신은 이제 그만 늘려도 되겠어. …지휘관, 오늘 진료는 끝났어. 나 좀 봐 줄래?')])],
  npc=(u'선임 군의관', u"**The senior.** A thin, upright woman in her mid-sixties, once a senior army doctor: short white hair, sharp clear eyes behind thin glasses, deep laugh lines, **pale blue patient pyjamas under a grey knitted cardigan**, a hospital wristband. She **faces RIGHT** (toward the agent she is talking to).", [u"sitting very straight, hands folded in her lap, looking up over her glasses with dry warmth, one eyebrow raised.", u"the same woman standing with a cane, chin lifted, eyes wet but smiling, proud."])),
]
