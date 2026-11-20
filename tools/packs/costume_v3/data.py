# -*- coding: utf-8 -*-
# 코스튬 미션 맵 제작 데이터 (6판). docs/COSTUME.md v2 를 따른다. 질문 2의 정답이 맵에서 그대로 보여야 한다.
T = {}
T['raven'] = dict(t=u'붉은 막', place_ko=u'원형 공연장 갈라의 밤', light=u"Gala night. A hard pool of warm light on the sand ring, deep red drapery, brass lamps, dark back-of-house rooms.",
 place=u"The interior of an old show arena: a sand ring in the middle, seating on all four sides, an outer concourse, and back rooms in the corners.",
 lay=u'''**Ring.** The exact centre: a **square ring of raked sand, 10 x 10 m**, enclosed by a red timber barrier 1.2 m high. **The barrier has exactly four gates, one in the middle of each side, and all four stand open.**

**Ringside lane.** A lane of red carpet 2.5 m wide all the way around the ring.

**Seating.** On **all four sides** of the ringside lane, a block of stepped seating, each block **12 m long and 3 m deep**, rising away from the ring. **Empty: no spectators.** Solid. The blocks do not meet at the corners: there is a **2.5 m gap at each of the four corners**.

**Organiser's box.** On the top step of the seating block on the **upper-left side** (the far side, opposite the red curtain), in its centre: one canopied box, 4 x 3 m, with a brass rail, reached by a short straight stair from the concourse behind it.

**Red curtain.** In the centre of the seating block on the **lower-right side**: a performers' passage 3 m wide cut through the block, framed by heavy red curtains tied back.

**Concourse.** Behind the seating, a ring corridor 2.5 m wide with a dark stone floor, running all the way around.

**Corner rooms**, each with one doorway onto the concourse:
- LEFT corner: the **wardrobe**, 6 x 6 m, red carpet floor, built-in mirror counter along one wall.
- TOP corner: the **office**, 6 x 6 m, dark timber floor, a built-in desk.
- RIGHT corner: the **prop store**, 6 x 8 m, bare concrete floor, built-in racking along two walls.
- along the upper-right side, between TOP and RIGHT: the **bookmaker's room**, 5 x 5 m, with a counter and a hatch window onto the concourse.

**Way in:** the artists' door in the near wall at the BOTTOM corner, with a floor hazard stripe.''',
 chk=[u'한가운데에 네모난 모래 링이 있고 울타리 문 4개가 전부 열려 있다(질문 정답: 넷)', u'객석이 네 면에 있고 비어 있으며 모서리 4곳이 트여 있다', u'주최자 박스가 붉은 막 맞은편 위쪽 객석(왼쪽 위)에 있다(질문 정답)', u'객석 뒤로 한 바퀴 도는 복도가 있다', u'모서리에 의상실 · 사무실 · 소품 창고가, 오른쪽 위 변에 마권방이 있다'],
 props=[(u'cover', u'엄폐물', [u"A costume rail full of red and black stage outfits, 1 x 2 m, 1.8 m high, orientation 1.", u"The same costume rail, orientation 2.", u"A wardrobe trunk standing open, waist-high, 1 x 1 m.", u"A stack of gilded chairs, waist-high, 1 x 1 m.", u"A prop cart with capes, hoops and wooden swords, waist-high, 1 x 2 m, orientation 1.", u"A tall painted screen with a red rose motif, 1 x 2 m, 2 m high, orientation 1."]),
        (u'show', u'관객 · 쇼', [u"**A block of spectators**: about fifteen gala guests in evening dress seen from behind and above, seated in three rows, applauding, 2 x 4 m, orientation 1. No faces in detail.", u"The same spectator block, orientation 2.", u"A pair of performers in the ring seen from above: a dancer with a red cape and a partner, mid-turn, drawn as one group.", u"A standing brass candelabra lamp, lit, 1 x 1 m, 2 m high.", u"A waiter with a tray of champagne seen from above.", u"A round follow-spot of hard warm light on the flat background, about 3 x 3 m, soft edge."]),
        (u'special', u'목표 · 인물 · 함정', [u"**The objective** (the game places three identical copies): a small steel strongbox with brass corners and a red wax seal, on a velvet cloth, drawn large.", u"**The wardrobe mistress**, as a small figure for the map: a woman in her fifties, silver hair in a tight bun, black smock, a tape measure round her neck, standing, seen from the map camera, full body, drawn large (about 420 px tall), facing lower-left.", u"**The bookmaker**, as a small map figure: a heavyset man in his forties in a red waistcoat with rolled sleeves, a ledger under his arm, standing, drawn large, facing lower-left.", u"A door alarm: a small box with a red lamp and a wire on a door-frame slice, drawn large.", u"A velvet rope barrier between two brass posts, waist-high, 1 x 2 m, orientation 1.", u"The same rope barrier, orientation 2."])],
 info=[u'코스튬이 통하는 곳: 링 둘레 통로(붉은 카펫), 의상실. 복도와 나머지 방은 통하지 않는다.', u'목표 3곳: 주최자 박스 · 사무실 · 소품 창고. 진짜는 소품 창고.', u'대화 1: 의상 담당(의상실) → 사무실 문에 경보. 대화 2: 마권업자(마권방) → 진짜 위치.', u'무대 큐: 26초마다 7초 동안 박수가 터져 소리가 묻히고 경비 시선이 링으로 쏠린다.'])
T['viper'] = dict(t=u'은반', place_ko=u'아이스링크 갈라쇼', light=u"A gala show. **The ice is lit in violet and silver**: violet wash, silver-white moving highlights. Dark stands, cold blue back rooms.",
 place=u"The interior of an ice arena: one rink, a strip of seating with a VIP lounge, a resurfacer garage and a row of back rooms.",
 lay=u'''**Rink.** In the centre: a **rectangular sheet of ice, 12 x 22 m, its long sides parallel to the lower-left side**, enclosed by white boards 1.2 m high. **The ice is washed in violet light with silver highlights.** The boards have **three gates**: two on the long side nearer the lower-left side, and one in the middle of the short end nearer the lower-right side. **The ice is empty.**

**Board lane.** A rubber-matted lane 2.5 m wide all the way around the outside of the boards.

**Seating.** Along the rink's far long side (toward the upper-right side): one block of stepped seating 22 m long and 3 m deep. Empty. Solid.

**VIP lounge.** At the end of the seating nearest the TOP corner, level with its top step: a glass-fronted lounge 6 x 7 m, violet carpet, a built-in bar, one doorway from the lane behind the seating.

**Lane behind the seating.** A corridor 2 m wide along the upper-right side.

**Resurfacer garage.** Beyond the short end of the rink nearer the lower-right side: a garage 5 x 7 m with a wide open doorway facing the rink's end gate. **Empty inside** (the machine is a sprite).

**Back rooms along the upper-left side**, behind a corridor 2 m wide, from the LEFT end to the TOP end: the **locker room**, 6 x 7 m, with built-in benches and lockers; the **coach room**, 4 x 5 m, with a built-in desk; the **referee room**, 4 x 5 m, with a built-in counter. One doorway each onto the corridor.

**Skaters' bench.** One fixed bench with a low backdrop, 1 x 4 m, on the board lane by the near long side.

**Way in:** the skaters' tunnel in the near wall at the BOTTOM corner, with a floor hazard stripe.''',
 chk=[u'빙판이 가운데에 있고 보라색과 은색 조명이다(질문 정답)', u'빙판 위에 아무것도 없고 보드 문이 3곳이다', u'먼 쪽 긴 변에 객석, 그 끝(위쪽)에 유리로 된 VIP 라운지가 있다', u'오른쪽 아래 끝에 정빙기 차고가 있고 안이 비어 있다', u'왼쪽 위 변을 따라 라커룸 · 코치실 · 심판실이 있다'],
 props=[(u'cover', u'엄폐물', [u"**An ice resurfacing machine**, parked, 2 x 4 m, 2 m high, orientation 1.", u"The same resurfacing machine, orientation 2.", u"A skate rack with rows of white skates, waist-high, 1 x 2 m, orientation 1.", u"A stack of rubber floor mats on a trolley, waist-high, 1 x 1 m.", u"A flower-and-gift table for the skaters, waist-high, 1 x 2 m, orientation 1.", u"A wheeled costume rail of violet and silver skating dresses, 1 x 2 m, 1.8 m high, orientation 1."]),
        (u'show', u'관객 · 쇼', [u"**A block of spectators**: about fifteen guests in winter evening wear seen from behind and above, seated in three rows, 2 x 4 m, orientation 1. No faces in detail.", u"The same spectator block, orientation 2.", u"A pair of figure skaters on the ice seen from above, mid-spin, in violet and silver, drawn as one group.", u"A single skater gliding in a long arabesque, seen from above.", u"A round spotlight of violet-white light on the flat background, about 3 x 3 m, soft edge.", u"A TV camera on a wheeled pedestal with an operator seen from above, 1 x 1 m."]),
        (u'special', u'목표 · 인물 · 함정', [u"**The objective** (the game places three identical copies): a slim jewellery case in silver metal with a violet velvet lining, closed, a small lock, drawn large.", u"**The patron's wife**, as a small figure for the map: an elegant woman in her forties, platinum updo, white fur stole over a violet gown, a champagne flute, standing, seen from the map camera, full body, drawn large (about 420 px tall), facing lower-left.", u"**The coach**, as a small map figure: a stern man in his fifties, grey crew cut, dark team jacket, a stopwatch on a lanyard, arms folded, drawn large, facing lower-left.", u"A security guard in a dark suit with an earpiece standing at ease, seen from the map camera, drawn large, facing lower-left.", u"A portable crowd barrier with violet bunting, waist-high, 1 x 2 m, orientation 1.", u"The same barrier, orientation 2."])],
 info=[u'코스튬이 통하는 곳: 빙판, 보드 둘레 통로, 라커룸.', u'목표 3곳: 정빙기 차고 · VIP 라운지 · 심판실. 진짜는 심판실.', u'대화 1: 후원자 부인(VIP 라운지) → 암전 큐 동안 라운지 앞에 감시. 대화 2: 코치(코치실) → 진짜 위치.', u'무대 큐: 30초마다 6초 암전. 그동안 소리가 묻히고 빙판 밖 경비 시야가 줄지만, 라운지 앞에는 경비가 선다.', u'빙판 위에서는 미끄러져 멈추는 데 한 칸이 더 든다(블러디 3판 얼음 처리).'])
T['glitch'] = dict(t=u'앙코르', place_ko=u'콘서트 돔 백스테이지', light=u"A concert in progress. Teal and magenta light spilling from the stage, a huge glowing LED wall seen from behind, dark cable-strewn backstage, blue running lights.",
 place=u"The backstage of a concert dome: the stage with its lift, the back of the LED wall, a backstage floor and a row of rooms.",
 lay=u'''**Stage.** Along the lower-right side: a black stage floor **14 x 8 m**, its long side parallel to the lower-right side. Beyond its front edge there is only darkness with a haze of tiny lights (the crowd), nothing drawn. **In the centre of the stage, a square stage-lift opening, 3 x 3 m: the lift platform is lowered, so the opening is clearly OPEN**, a dark pit with the platform visible 2 m down and a yellow edge line.

**Wings.** On each short side of the stage, a wing 4 m wide and as deep as the stage.

**LED wall.** Behind the stage, running its full width: the **back of a giant LED wall**, a tall steel truss wall hung with cable looms, glowing at the edges. **It has exactly two gaps, each 2 m wide**, one a third of the way along and one two thirds of the way along. No other way through.

**Backstage floor.** Behind the LED wall, a floor 7 m deep across the full width, black with teal tape lines. Empty.

**Cross corridor.** Behind the backstage floor, a corridor 2.5 m wide across the full width, grey concrete.

**Rooms along the upper-left side**, behind the corridor, from the LEFT end to the TOP end: the **dressing room**, 6 x 6 m, with a bulb-ringed mirror counter; the **green room**, 6 x 6 m, with a built-in sofa bench along two walls; the **control room**, 6 x 7 m, with a long built-in console desk facing a window slot; the **equipment store**, 6 x 8 m, with built-in racking. One doorway each onto the corridor.

**Loading dock.** Along the upper-right side: a raised dock 3 m deep with a closed roller door.

**Way in:** the stage door in the near wall at the BOTTOM corner, in the left wing, with a floor hazard stripe.''',
 chk=[u'무대 한가운데 리프트 구멍이 열려 있다(질문 정답: 열려 있다)', u'무대 뒤 LED 벽에 틈이 정확히 2곳이다(질문 정답: 두 군데)', u'LED 벽 뒤에 넓은 바닥, 그 뒤에 긴 복도가 있다', u'왼쪽 위 변을 따라 대기실 · 그린룸 · 통제실 · 장비 창고 순서다', u'무대 앞(오른쪽 아래)은 어둠과 작은 불빛뿐이다'],
 props=[(u'cover', u'엄폐물', [u"A black flight case on wheels with silver edges, waist-high, 1 x 2 m, orientation 1.", u"The same flight case, orientation 2.", u"Two flight cases stacked, 1 x 1 m, 2 m high.", u"A rack of guitars on a stand, waist-high, 1 x 2 m, orientation 1.", u"A monitor-mix desk with a glowing console, waist-high, 1 x 2 m, orientation 1.", u"A wheeled costume rail of neon stage outfits, 1 x 2 m, 1.8 m high, orientation 1."]),
        (u'show', u'쇼 · 스태프', [u"A group of four idol dancers on stage seen from above and behind, mid-pose, teal neon outfits, drawn as one group.", u"A stagehand in black with a headset carrying a cable coil, seen from above.", u"A camera crane base with an operator seen from above, 2 x 2 m.", u"A burst of stage pyro sparks, soft-edged, on the flat background, about 2 x 3 m.", u"A sweep of teal laser light on the flat background, a long soft fan about 5 x 2 m.", u"A drum riser with a drum kit, 2 x 2 m, waist-high plus."]),
        (u'special', u'목표 · 인물 · 함정', [u"**The objective** (the game places three identical copies): a compact show server in a short rolling rack, front panel lit with teal LEDs, one drive bay slightly open, drawn large.", u"**The tour manager**, as a small figure for the map: a sharp woman in her thirties, black bob, headset, black blazer, a tablet held to her chest, standing, seen from the map camera, full body, drawn large (about 420 px tall), facing lower-left.", u"**The sound director**, as a small map figure: a lanky man in his forties, short beard, grey beanie, headphones round his neck, black crew T-shirt, standing, drawn large, facing lower-left.", u"A security guard in a black bomber with a torch, seen from the map camera, drawn large, facing lower-left.", u"**The stage lift platform** seen from above: a 3 x 3 m black platform with a yellow edge and a teal light ring, to cover the lift opening when raised.", u"A door card-reader with a red lamp on a door-frame slice, drawn large."])],
 info=[u'코스튬이 통하는 곳: 무대 뒤 바닥, 대기실.', u'목표 3곳: 그린룸 · 통제실 · 장비 창고. 진짜는 통제실.', u'대화 1: 매니저(대기실) → 통제실 문은 LED 벽이 번쩍일 때만 감시가 빈다. 대화 2: 음향 감독(장비 창고) → 진짜 위치.', u'무대 큐: 22초마다 6초 동안 LED 벽이 번쩍이고 소리가 묻힌다.'])
T['brick'] = dict(t=u'타이틀 매치', place_ko=u'호텔 연회장 특설 링', light=u"A hotel ballroom on fight night. Crystal chandeliers dimmed, one white truss light over the ring, an orange carpet runner, steel-and-tile service rooms.",
 place=u"The interior of a grand hotel ballroom with a boxing ring set up in its centre, ringed by a service corridor and back rooms.",
 lay=u'''**Ballroom.** One large room, 20 x 20 m, in the middle of the map, with a dark patterned carpet. **Four wide doorways, one in the middle of each wall.** **The floor is empty** (tables are sprites).

**Ring.** In the **exact centre of the ballroom**: a raised boxing ring, 6 x 6 m, white canvas, orange and black ropes. Solid.

**Entrance ramp.** From the ballroom's upper-left doorway straight to the ring: a **raised walkway 2 m wide and 0.5 m high covered in bright ORANGE carpet**, with low steps at both ends.

**Service corridor.** Around the outside of the ballroom on all four sides, a corridor 2.5 m wide with a plain tile floor.

**Rooms outside the corridor:**
- along the upper-right side, between TOP and RIGHT: the **kitchen**, 6 x 12 m, steel floor, a fixed line of ranges down its centre and built-in counters, two doorways.
- TOP corner: the **cash office**, 5 x 5 m, with a barred pay window and a built-in counter, one doorway.
- RIGHT corner: the **cloakroom**, 5 x 6 m, with built-in hanging rails along two walls and a counter hatch, one doorway.
- LEFT corner and along the upper-left side: the **fighters' room**, 6 x 8 m, with built-in benches and a massage table platform, one doorway facing the ballroom's upper-left doorway.

**Way in:** the hotel lobby doors in the near wall at the BOTTOM corner, with a floor hazard stripe.''',
 chk=[u'링이 연회장 한가운데에 있다(질문 정답)', u'선수 대기실 쪽 문에서 링까지 주황색 카펫 램프가 이어진다(질문 정답: 주황)', u'연회장 바닥이 비어 있고 네 벽 가운데에 문이 있다', u'연회장 바깥을 한 바퀴 도는 서비스 복도가 있다', u'주방 · 캐시 오피스 · 물품 보관소 · 선수 대기실이 있다'],
 props=[(u'cover', u'엄폐물', [u"A round banquet table with a white cloth, glasses and a centrepiece, waist-high, 2 x 2 m.", u"A round banquet table with eight seated guests in black tie seen from above, drawn as one group, 3 x 3 m.", u"A kitchen service trolley stacked with plates, waist-high, 1 x 2 m, orientation 1.", u"A champagne tower on a small table, 1 x 1 m, 1.8 m high.", u"A stack of banquet chairs on a dolly, 1 x 1 m, 1.8 m high.", u"A press table with cameras and laptops, waist-high, 1 x 2 m, orientation 1."]),
        (u'show', u'경기 · 관객', [u"Two boxers and a referee in the ring seen from above, mid-exchange, drawn as one group.", u"A ring announcer in a tuxedo with a hanging microphone, seen from above.", u"A square lighting truss with four hot white lamps seen from above, to hang over the ring.", u"A row of five standing spectators cheering, seen from behind and above, 1 x 3 m, orientation 1.", u"The same row of spectators, orientation 2.", u"A ring-card stand with a blank card (no text) and a bell on a small table, 1 x 1 m."]),
        (u'special', u'목표 · 인물 · 함정', [u"**The objective** (the game places three identical copies): a worn leather gym holdall, zipped, with an orange stripe and a small brass padlock, drawn large.", u"**The head chef**, as a small figure for the map: a broad man in his fifties in chef whites, a towel over one shoulder, arms folded, standing, seen from the map camera, full body, drawn large (about 420 px tall), facing lower-left.", u"**The cutman**, as a small map figure: a wiry man in his sixties, flat cap, orange-and-black corner jacket, a towel round his neck, standing, drawn large, facing lower-left.", u"A floor pressure-alarm mat: a thin dark rubber mat with a faint red indicator line, 1 x 2 m, flat.", u"A hotel security guard in a dark blazer with an earpiece, seen from the map camera, drawn large, facing lower-left.", u"A brass stanchion rope barrier, waist-high, 1 x 2 m, orientation 1."])],
 info=[u'코스튬이 통하는 곳: 입장 램프, 링 둘레, 선수 대기실.', u'목표 3곳: 물품 보관소 · 캐시 오피스 · 선수 대기실. 진짜는 선수 대기실.', u'대화 1: 주방 책임자(주방) → 캐시 오피스 앞 바닥에 압력 경보. 대화 2: 컷맨(선수 대기실) → 진짜 위치.', u'무대 큐: 28초마다 6초 동안 라운드 공이 울리고 함성이 터져 소리가 묻힌다.'])
T['mirage'] = dict(t=u'하우스 엣지', place_ko=u'펜트하우스 카지노', light=u"A private casino at night. Gold lamps over green baize, black marble, a skyline of city lights beyond the terrace, cold white light in the back rooms.",
 place=u"The interior of a penthouse casino: a gaming floor with a cashier cage in its centre, a bar, a VIP salon, a terrace, and secure rooms behind the far walls.",
 lay=u'''**Gaming floor.** One large room, 20 x 20 m, toward the near half of the map, with a deep green-and-gold carpet. **The floor is empty** (tables are sprites).

**Cage.** In the **exact centre of the gaming floor**: the cashier cage, 5 x 5 m, brass bars on a marble base, one barred gate on its far side. Solid walls of bars; you can see in.

**Slot machines.** **Along both far walls of the gaming floor** (the upper-left wall and the upper-right wall): one continuous built-in row of slot machines against each wall, glowing, each row broken once by a doorway.

**Bar.** Along the gaming floor's lower-left wall: a fixed bar counter 1 x 9 m with a mirrored back shelf, and a 2 m space behind it for the staff.

**Terrace.** Along the lower-right side: an open terrace 3 m deep, full length, behind a glass wall with two doorways, a low glass balustrade and the city far below.

**VIP salon.** At the LEFT corner: a room 6 x 7 m, dark red carpet, one doorway from the gaming floor screened by a fixed carved partition.

**Back corridor.** Behind the two far walls of the gaming floor, an L-shaped staff corridor 2 m wide with a plain grey floor, reached through the doorways in the slot rows.

**Rooms off the back corridor:** the **surveillance room**, 5 x 5 m, along the upper-left side, with a built-in wall of monitors; the **count room**, 5 x 6 m, at the TOP corner, with a steel door and a built-in counting table; a **staff changing room**, 4 x 5 m, along the upper-right side.

**Way in:** the lift lobby in the near wall at the BOTTOM corner, with a floor hazard stripe.''',
 chk=[u'케이지가 게임 플로어 한가운데에 있다(질문 정답)', u'슬롯머신 줄이 먼 쪽 양쪽 벽에 있다(질문 정답: 양쪽 벽)', u'플로어 바닥이 비어 있다', u'왼쪽 아래 벽에 긴 바, 오른쪽 아래 변에 테라스가 있다', u'먼 벽 뒤로 직원 복도와 감시실 · 카운트룸이 있다'],
 props=[(u'cover', u'엄폐물', [u"A roulette table with its wheel and a dealer's stool, waist-high, 2 x 3 m, orientation 1.", u"The same roulette table, orientation 2.", u"A half-moon blackjack table with stools, waist-high, 2 x 2 m.", u"A baccarat table with six players in evening dress seated round it, seen from above, drawn as one group, 3 x 4 m, orientation 1.", u"A tall floral arrangement on a marble plinth, 1 x 1 m, 2.2 m high.", u"A dealer's chip trolley, waist-high, 1 x 1 m."]),
        (u'show', u'손님 · 직원', [u"A group of three guests with cocktails seen from above, chatting, drawn as one group.", u"A dealer in a gold-and-black waistcoat standing behind a table, seen from above.", u"A cocktail waitress with a tray seen from above.", u"A jazz trio on a small riser seen from above: piano, bass, saxophone, 3 x 3 m.", u"A pit boss lectern with a lamp and a phone, 1 x 1 m, waist-high.", u"A burst of gold confetti and light on the flat background, soft-edged, about 3 x 3 m (a jackpot)."]),
        (u'special', u'목표 · 인물 · 함정', [u"**The objective** (the game places three identical copies): a black steel cash box with gold corners and a combination dial, a few chips beside it, drawn large.", u"**The high roller**, as a small figure for the map: a suave man in his fifties, silver hair, white dinner jacket, a stack of chips in his fingers, standing, seen from the map camera, full body, drawn large (about 420 px tall), facing lower-left.", u"**The pit boss**, as a small map figure: a woman in her forties, sleek ponytail, black suit, an earpiece, hands clasped, standing, drawn large, facing lower-left.", u"A cage guard in a dark uniform with a holstered baton, seen from the map camera, drawn large, facing lower-left.", u"A ceiling eye-in-the-sky camera dome seen from above, with a faint red ring.", u"A velvet rope barrier between two gold posts, waist-high, 1 x 2 m, orientation 1."])],
 info=[u'코스튬이 통하는 곳: 테이블 구역(게임 플로어), 바. 케이지 앞 2칸에서는 통하지 않는다(대화 1로 알게 된다).', u'목표 3곳: 케이지 · 감시실 · 카운트룸. 진짜는 카운트룸.', u'대화 1: 하이롤러(VIP 살롱) → 케이지 앞 함정. 대화 2: 피트 보스(바 끝) → 진짜 위치.', u'무대 큐: 25초마다 5초 동안 잭팟이 터져 소리가 묻히고 시선이 슬롯 쪽으로 쏠린다.'])
T['doc'] = dict(t=u'왕진', place_ko=u'프라이빗 클리닉 & 스파', light=u"A luxury clinic at night. Soft white and lime accent lighting, pale stone, warm timber and steam on the spa side, cool steel in the back rooms.",
 place=u"The interior of a private clinic and spa: a reception hall, a clinic wing on one side and a spa wing on the other.",
 lay=u'''**Reception hall.** At the BOTTOM corner: a hall 8 x 8 m, pale stone floor, a fixed straight reception desk (1 x 4 m), the way in through its near wall.

**Pharmacy.** Directly behind the reception hall (on its far side): a room 5 x 5 m with built-in shelving on three walls and a refrigerated cabinet. **Its only doorway opens into the reception hall.**

**Clinic wing (toward the LEFT corner and along the upper-left side).** A corridor 2.5 m wide leaves the reception hall and runs parallel to the lower-left side, then turns once to run parallel to the upper-left side up to the TOP corner. Off it, in order from the reception hall: the **treatment room**, 6 x 6 m, with a fixed treatment chair platform and built-in cabinets; the **records room**, 5 x 5 m, with built-in filing walls; the **director's office**, 6 x 6 m, at the TOP corner, with a built-in desk and a wall cabinet. One doorway each onto the corridor.

**Spa wing (toward the RIGHT corner and along the upper-right side).** A second corridor 2.5 m wide leaves the reception hall and runs parallel to the lower-right side. Off it: a **changing room**, 4 x 5 m, with built-in lockers; then the **spa pool hall**, 10 x 12 m, at the RIGHT corner, with a **rectangular pool 5 x 8 m** (water, not walkable) and warm timber decking around it, **the deck on the pool's long near side left clear for three sunbeds**; then the **sauna**, 4 x 5 m, timber-lined with built-in benches, opening off the pool hall.

**Garden court.** In the middle of the map, enclosed by the two wings: a small stone-and-moss garden 6 x 6 m, open to the sky. Not walkable. A glass-walled passage 2 m wide runs along its far side and joins the director's office end of the clinic corridor to the pool hall.

Rule 3 (a lane around all four sides) does not apply.''',
 chk=[u'맨 아래 모서리에 리셉션, 바로 뒤에 약제실이 있고 약제실 문이 리셉션 쪽으로 나 있다(질문 정답)', u'왼쪽으로 진료 복도와 시술실 · 기록실 · 원장실이 있다', u'오른쪽으로 스파 복도와 탈의실 · 스파 풀 · 사우나가 있다', u'풀 옆 가까운 쪽 데크가 선베드 3개 놓을 만큼 비어 있다(질문 정답: 셋, 선베드는 낱개)', u'가운데에 들어갈 수 없는 정원과 그 뒤 유리 통로가 있다'],
 props=[(u'cover', u'엄폐물', [u"**A spa sunbed** with a rolled white towel, waist-high, 1 x 2 m, orientation 1.", u"The same sunbed, orientation 2.", u"A medical instrument trolley with steel trays, waist-high, 1 x 1 m.", u"A towel cart stacked with white towels, waist-high, 1 x 1 m.", u"A tall potted palm in a stone planter, 1 x 1 m, 2.2 m high.", u"A folding privacy screen with frosted panels, 1 x 2 m, 1.8 m high, orientation 1."]),
        (u'show', u'손님 · 직원', [u"A patient in a white robe with a bandaged face reading in an armchair, seen from above.", u"A nurse in a white tunic with lime piping carrying a tray, seen from above.", u"Two spa guests in robes with cocktails seen from above, drawn as one group.", u"A cloud of sauna steam, soft-edged, on the flat background, about 3 x 3 m.", u"A reception waiting sofa with a low table and orchids, waist-high, 1 x 3 m, orientation 1.", u"An IV stand with a drip bag on wheels, 1 x 1 m, 2 m high."]),
        (u'special', u'목표 · 인물 · 함정', [u"**The objective** (the game places three identical copies): a white medical cool-box with a lime stripe and a steel latch, a faint frost haze round it, drawn large.", u"**The head nurse**, as a small figure for the map: a strict woman in her fifties, white tunic with lime piping, glasses on a chain, a clipboard, standing, seen from the map camera, full body, drawn large (about 420 px tall), facing lower-left.", u"**The VIP patient**, as a small map figure: a man in his sixties in a white spa robe, a small bandage across his nose, a gold watch, a towel round his neck, sitting on a bench, drawn large, facing lower-left.", u"A silent alarm contact: a tiny sensor with a green lamp on a cabinet-door slice, drawn large.", u"A clinic security guard in a pale grey uniform, seen from the map camera, drawn large, facing lower-left.", u"A glass sliding door leaf with a frosted band, 1 x 2 m, 2.2 m high, orientation 1."])],
 info=[u'코스튬이 통하는 곳: 리셉션, 시술실, 스파.', u'목표 3곳: 기록실 · 원장실 · 약제실. 진짜는 약제실.', u'대화 1: 수간호사(시술실) → 원장실 캐비닛에 무음 경보. 대화 2: VIP 환자(사우나) → 진짜 위치.', u'무대 큐: 쇼가 없는 판이다. 대신 24초마다 6초 동안 호출 방송이 울려 직원들이 리셉션 쪽을 본다.', u'선베드는 반드시 3개만 놓는다(질문 정답).'])
