# -*- coding: utf-8 -*-
"""SILENT SIX — 새 맵 타일 설계 (가이드 이미지와 게임 충돌 맵의 원본).

문자:
  .  바닥(걸을 수 있음)        =  표시된 바닥(걸을 수 있음: 무대·선로·활주로 등)
  ~  젖은/언 바닥(걸을 수 있음)  S  진입·탈출 칸(걸을 수 있음)
  V  지나갈 수 없는 평면(물·낭떠러지·선로 구덩이)
  #  높은 벽                   B  높은 덩어리(차량·서가·바위·나무 등)
  C  낮은 엄폐                 W  부술 수 있는 벽
  X  목표      D  가짜 목표(코스튬 맵, X 와 같은 모양)      N  대화 지점(걸을 수 있음)
크기는 P=16x22, L=22x16, Q=19x19 (가로+세로 = 38 로 같아 화면에 같은 크기로 들어간다).
"""
P, L, Q = (16, 22), (22, 16), (19, 19)


def F(ch, x0, y0, x1, y1):
    return ('F', ch, x0, y0, x1, y1)


def O(ch, x0, y0, x1, y1):
    return ('O', ch, x0, y0, x1, y1)


def Pt(ch, *pts):
    return ('P', ch, pts)


def build(m):
    cols, rows = m['size']
    g = [[m.get('fill', '.')] * cols for _ in range(rows)]
    b = m.get('border', '#')

    def put(ch, x, y):
        if 0 <= x < cols and 0 <= y < rows:
            g[y][x] = ch
    if b:
        for x in range(cols):
            put(b, x, 0); put(b, x, rows - 1)
        for y in range(rows):
            put(b, 0, y); put(b, cols - 1, y)
    for op in m['ops']:
        if op[0] == 'F':
            _, ch, x0, y0, x1, y1 = op
            for y in range(y0, y1 + 1):
                for x in range(x0, x1 + 1):
                    put(ch, x, y)
        elif op[0] == 'O':
            _, ch, x0, y0, x1, y1 = op
            for x in range(x0, x1 + 1):
                put(ch, x, y0); put(ch, x, y1)
            for y in range(y0, y1 + 1):
                put(ch, x0, y); put(ch, x1, y)
        else:
            for (x, y) in op[2]:
                put(op[1], x, y)
    for (x, y) in m['S']:
        put('S', x, y)
    for (x, y) in m.get('N', []):
        put('N', x, y)
    for (x, y) in m.get('D', []):
        put('D', x, y)
    put('X', *m['X'])
    return [''.join(r) for r in g]


WALK = '.=~SN'
WALKW = WALK + 'W'  # 부술 수 있는 벽은 도달 검사에서 길로 본다


def check(m, rows_):
    cols, rows = m['size']
    seen = set(); st = [tuple(m['S'][0])]
    while st:
        x, y = st.pop()
        if (x, y) in seen or not (0 <= x < cols and 0 <= y < rows) or rows_[y][x] not in WALKW:
            continue
        seen.add((x, y))
        st += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    X = m['X']
    for T in [X] + list(m.get('D', [])) + list(m.get('N', [])):
        if not any((T[0] + dx, T[1] + dy) in seen for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (0, 0))):
            return False, len(seen), -1
    near = any((X[0] + dx, X[1] + dy) in seen for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
    total = sum(r.count(c) for r in rows_ for c in WALKW)
    return near, len(seen), total


MAPS = []


def add(**k):
    MAPS.append(k)


# 스토리 S1-06 은 그림을 먼저 받고 그림에서 충돌을 따 넣었다(tools/map/trace_s1_06). 가이드 없음.

# ───────────────────────── 로맨틱 18
add(id='raven_1', pack='romantic', file='bgp_raven_1.jpg', ko='RAVEN TAKE 1 · 빈자리 — 폭우 속 폐광촌', size=Q, border='B',
    ops=[F('#', 2, 2, 4, 4), F('#', 6, 2, 8, 4), F('#', 2, 6, 4, 8), F('#', 6, 6, 8, 8),
         O('#', 11, 2, 16, 6), Pt('.', (13, 6)), Pt('C', (12, 3), (15, 4)),
         O('#', 11, 10, 16, 14), Pt('.', (11, 12)), Pt('C', (13, 13)),
         F('~', 9, 7, 10, 8), F('~', 4, 12, 6, 12), F('~', 9, 15, 10, 16),
         Pt('C', (5, 10), (6, 10), (2, 11), (8, 12), (3, 14), (4, 14), (7, 15), (9, 10), (14, 8)),
         F('B', 13, 16, 14, 16), F('B', 1, 16, 2, 17), Pt('C', (11, 16), (5, 17))],
    S=[(9, 17), (10, 17)], X=(15, 11),
    scene="An abandoned mining village in heavy rain at night. Collapsed company houses forming narrow alleys, an ore-processing shed, a mine office with a safe. Mud, deep puddles, broken fences, sheets of rain, one distant lightning glow.",
    leg={'B': 'rock outcrops and dead pine clumps closing the edge of the map', '#': 'ruined company houses (solid blocks) and the standing walls of the ore shed and the mine office (door gaps stay open)', 'C': 'rubble piles, broken fences, ore carts, crates', '~': 'deep rain puddles (walkable)', 'X': 'the old office safe', 'S': 'the road in (muddy tracks)'})

add(id='raven_2', pack='romantic', file='bgp_raven_2.jpg', ko='RAVEN TAKE 2 · 서명 — 심야의 기록원 분관', size=P,
    ops=[F('B', 2, 2, 2, 8), F('B', 4, 2, 4, 8), F('B', 6, 2, 6, 8), F('B', 8, 2, 8, 8), F('.', 1, 5, 9, 5),
         F('#', 10, 1, 10, 9), Pt('.', (10, 5)), Pt('C', (12, 3), (13, 3), (12, 7), (13, 7)),
         F('#', 1, 10, 14, 10), Pt('.', (3, 10), (12, 10)),
         F('B', 2, 12, 2, 16), F('B', 4, 12, 4, 16), F('B', 6, 12, 6, 16), F('.', 1, 14, 7, 14),
         O('#', 9, 12, 15, 17), Pt('.', (9, 14), (12, 17)), Pt('C', (12, 15), (11, 13)),
         F('#', 1, 17, 8, 17), Pt('.', (5, 17)), F('C', 6, 19, 8, 19), Pt('C', (2, 19), (13, 19))],
    S=[(7, 20), (8, 20)], X=(14, 13),
    scene="The interior of a state archive annex at midnight, roof removed. Long rows of rolling compact shelves forming a maze, a reading room with green banker lamps, a conservation lab, a small lobby. Polished floor, a few motion-sensor light pools, dust in the air.",
    leg={'#': 'archive walls (door gaps stay open)', 'B': 'tall rolling compact shelves full of files', 'C': 'reading tables with green lamps, the lobby desk, trolleys', 'X': 'the lab table holding the original order under a lamp', 'S': 'the lobby entrance'})

add(id='raven_3', pack='romantic', file='bgp_raven_3.jpg', ko='RAVEN TAKE 3 · 대면 — 항구 끝 등대와 방파제', size=P, border='', fill='V',
    ops=[F('.', 6, 1, 9, 20), F('.', 4, 1, 11, 4), F('#', 6, 1, 9, 2),
         F('.', 10, 8, 13, 12), F('#', 11, 9, 12, 10), F('.', 2, 13, 5, 14), Pt('C', (2, 13)),
         Pt('B', (6, 6), (9, 7), (6, 10), (9, 14), (6, 15), (9, 18), (4, 3), (11, 3), (13, 12)),
         Pt('C', (7, 8), (8, 12), (7, 17), (10, 12), (5, 14))],
    S=[(7, 20), (8, 20)], X=(7, 3),
    scene="A long narrow concrete breakwater at night reaching out to a lighthouse, black sea on every side. Stacked tetrapods, a fishing-gear shed on a side platform, a small boat landing. Wet concrete, a sweeping lighthouse beam, sea spray.",
    leg={'V': 'open sea (dark water with foam along the concrete edge)', '#': 'the lighthouse base and the gear shed', 'B': 'tetrapod stacks and mooring bollards', 'C': 'fishing nets, crab pots, coiled rope, a moored dinghy', 'X': 'the lighthouse door with the tape recorder on a ledge', 'S': 'the landward end of the breakwater'})

add(id='viper_1', pack='romantic', file='bgp_viper_1.jpg', ko='VIPER TAKE 1 · 빗나간 한 발 — 스키 리조트 야간 슬로프', size=Q, border='B',
    ops=[F('=', 6, 1, 12, 17), F('#', 6, 1, 12, 2),
         O('#', 2, 13, 5, 16), Pt('.', (5, 14)), O('#', 14, 12, 17, 16), Pt('.', (14, 14)), Pt('C', (16, 13)),
         Pt('B', (2, 3), (3, 6), (4, 9), (2, 10), (15, 5), (16, 8), (14, 9), (3, 2), (16, 2), (9, 7), (9, 12)),
         Pt('C', (7, 5), (11, 9), (7, 13), (12, 5), (6, 10), (11, 15), (4, 5), (14, 6))],
    S=[(8, 17), (9, 17)], X=(9, 3),
    scene="A ski resort at night. A floodlit piste running up the middle to a lodge with lit windows, a chairlift line with pylons, a lift station, a snow-groomer garage, dark pine forest on both sides. Bright white slope against deep blue shadow.",
    leg={'B': 'dark pine trees and chairlift pylons', '#': 'the lodge front, the lift station and the groomer garage (door gaps stay open)', 'C': 'snow mounds, padded fences, stacked skis, a snowmobile', '=': 'the floodlit groomed slope (bright corduroy snow)', 'X': 'a spotting position below the lodge windows (tripod and scope case)', 'S': 'the bottom of the slope'})

add(id='viper_2', pack='romantic', file='bgp_viper_2.jpg', ko='VIPER TAKE 2 · 거리 — 온천 료칸의 복도', size=P,
    ops=[F('#', 5, 1, 5, 20), F('#', 10, 1, 10, 20),
         F('#', 1, 5, 4, 5), F('#', 1, 10, 4, 10), F('#', 1, 15, 4, 15), Pt('.', (5, 3), (5, 8), (5, 13), (5, 18)),
         F('#', 11, 6, 14, 6), F('#', 11, 12, 14, 12), Pt('.', (10, 3), (10, 9), (10, 15)),
         F('~', 11, 1, 14, 5), F('V', 7, 8, 8, 12),
         Pt('C', (2, 2), (3, 12), (12, 8), (13, 17), (6, 5), (6, 16), (2, 17), (12, 14)), Pt('B', (7, 7), (8, 13))],
    S=[(7, 20), (8, 20)], X=(2, 7),
    scene="The interior of a traditional hot-spring inn at night, roof removed. Long wooden corridors lined with sliding paper doors, tatami guest rooms on both sides, a small inner courtyard pond with snow, a steaming bath room. Warm lantern light, drifting steam.",
    leg={'#': 'timber-and-paper walls with sliding doors (door gaps stay open)', 'C': 'low tables, folding screens, luggage, futon stacks', 'B': 'stone lanterns and a garden pine at the pond', 'V': 'the courtyard pond (snow-edged water)', '~': 'the wet stone floor of the bath room, thick steam', 'X': 'a low desk with the spotter\'s notebook', 'S': 'the genkan entrance'})

add(id='viper_3', pack='romantic', file='bgp_viper_3.jpg', ko='VIPER TAKE 3 · 숨 — 산정 관측소', size=Q, border='V',
    ops=[F('V', 1, 7, 7, 9), F('V', 11, 7, 17, 9), Pt('C', (9, 8)),
         O('#', 2, 13, 6, 16), Pt('.', (6, 14)), O('#', 6, 2, 12, 5), Pt('.', (9, 5)),
         Pt('B', (3, 3), (15, 3), (14, 5), (4, 11), (13, 12), (15, 14), (10, 13), (8, 15), (16, 11)),
         Pt('C', (11, 15), (6, 11), (12, 11), (4, 5), (13, 6), (8, 3))],
    S=[(3, 15), (4, 15)], X=(10, 3),
    scene="A mountaintop weather station in a blizzard at night. A cable-car terminal on the lower shoulder, a narrow wind-carved ridge crossing to the summit, a small observatory building with antenna masts. Rime ice, snow cornices, sheer drops on all sides.",
    leg={'V': 'sheer drop into cloud and darkness (cliff edge)', '#': 'the cable-car terminal and the observatory (door gaps stay open)', 'B': 'rock spires, antenna masts and ice-crusted boulders', 'C': 'snow cornices, drifted fuel drums, equipment cases', 'X': 'the observation desk by the window', 'S': 'inside the cable-car terminal'})

add(id='glitch_1', pack='romantic', file='bgp_glitch_1.jpg', ko='GLITCH TAKE 1 · 로그 — 데이터센터 냉각동', size=L,
    ops=[F('=', 4, 2, 4, 6), F('=', 8, 2, 8, 6), F('=', 12, 2, 12, 6), F('=', 4, 9, 4, 13), F('=', 8, 9, 8, 13), F('=', 12, 9, 12, 13)] +
        [F('B', x, 2, x, 6) for x in (3, 5, 7, 9, 11, 13)] + [F('B', x, 9, x, 13) for x in (3, 5, 7, 9, 11, 13)] +
        [F('#', 16, 1, 16, 14), Pt('.', (16, 4), (16, 11)), F('#', 17, 7, 20, 7), Pt('.', (19, 7)),
         Pt('C', (18, 10), (19, 12), (18, 5), (1, 3), (1, 12), (14, 7))],
    S=[(1, 7), (1, 8)], X=(19, 3),
    scene="The interior of a data-center cooling hall, roof removed. Long rows of black server racks with blue and amber status lights, glowing hot aisles between rack pairs, a cross aisle, a power and console room at one end. Raised floor tiles, overhead cable trays, cold blue light.",
    leg={'#': 'hall walls and the power-room partition (door gaps stay open)', 'B': 'rows of server racks', 'C': 'crash carts, spare-part crates, cooling units', '=': 'hot aisles (floor glowing warm orange-red)', 'X': 'the admin console terminal', 'S': 'the loading-door entrance'})

add(id='glitch_2', pack='romantic', file='bgp_glitch_2.jpg', ko='GLITCH TAKE 2 · 사본 — 전자상가 옥상', size=Q, border='', fill='V',
    ops=[F('.', 1, 11, 6, 17), F('.', 1, 2, 7, 7), F('.', 11, 1, 17, 6), F('.', 10, 10, 17, 17),
         F('=', 3, 8, 3, 10), F('=', 8, 4, 10, 4), F('=', 14, 7, 14, 9), F('=', 7, 14, 9, 14),
         F('#', 2, 3, 5, 3), F('#', 12, 2, 12, 4),
         Pt('B', (2, 13), (4, 15), (5, 12), (12, 12), (11, 16), (14, 3), (16, 5), (2, 6), (6, 5)),
         O('#', 13, 12, 16, 16), Pt('.', (13, 14)), Pt('C', (11, 11), (5, 16), (16, 2), (6, 2), (15, 15))],
    S=[(2, 17), (3, 17)], X=(15, 13),
    scene="The rooftops of an electronics-market district at night. Four separate flat roofs joined by narrow steel catwalks over deep alleys, big neon signboards seen from behind, forests of air-conditioner units, a rooftop workshop shack. Pink and cyan neon glow, wet tar roofs.",
    leg={'V': 'the drop between buildings (dark alley far below, faint street lights)', '#': 'the backs of large neon billboards and the walls of the rooftop workshop (door gap stays open)', 'B': 'air-conditioner units, water tanks, antenna masts', 'C': 'cable drums, crates of parts, satellite dishes', '=': 'steel grating catwalks between roofs', 'X': 'the workbench with the hidden copy', 'S': 'the stair hatch'})

add(id='glitch_3', pack='romantic', file='bgp_glitch_3.jpg', ko='GLITCH TAKE 3 · 로그아웃 — 폐쇄된 지하철 역사', size=L,
    ops=[F('V', 1, 6, 20, 7), F('B', 3, 6, 14, 7), F('=', 6, 6, 6, 7), F('=', 11, 6, 11, 7), F('.', 19, 6, 20, 7),
         Pt('B', (4, 3), (8, 3), (12, 3), (16, 3), (4, 9), (9, 9), (14, 9), (18, 9)), Pt('C', (6, 2), (14, 2), (10, 4), (7, 9), (16, 5)),
         F('#', 1, 11, 20, 11), Pt('.', (5, 11), (15, 11)), F('#', 10, 12, 10, 14),
         Pt('C', (3, 13), (7, 13), (13, 13), (16, 12))],
    S=[(1, 1), (1, 2)], X=(19, 13),
    scene="A closed, abandoned subway station, roof removed. Two platforms either side of a track bed, a dead train parked with its doors open, tiled pillars, a transfer corridor and a station office with a vault below. Emergency lights only, some dark, some dim red.",
    leg={'#': 'station walls (door gaps stay open)', 'V': 'the sunken track bed with rails', 'B': 'the parked train cars and the platform pillars', '=': 'open train doorways you can walk through, car floor visible', 'C': 'benches, ticket machines, vending machines, desks', 'X': 'the station vault with the terminal', 'S': 'the stairs down from the street'})

add(id='brick_1', pack='romantic', file='bgp_brick_1.jpg', ko='BRICK TAKE 1 · 닫힌 문 — 폐쇄된 지하 벙커', size=P,
    ops=[F('#', 8, 1, 8, 20), F('#', 1, 5, 14, 5), F('#', 1, 10, 14, 10), F('#', 1, 15, 14, 15),
         Pt('.', (4, 15), (8, 12), (12, 10), (4, 5), (8, 3)), Pt('W', (8, 17), (12, 15), (4, 10), (8, 7), (12, 5)),
         Pt('C', (2, 17), (11, 18), (3, 12), (12, 13), (5, 7), (11, 7), (3, 2), (11, 3), (6, 19), (13, 8)), Pt('B', (6, 13), (14, 1))],
    S=[(2, 19), (3, 19)], X=(13, 2),
    scene="The interior of a sealed underground military bunker, roof removed. Eight concrete rooms joined by heavy blast doors, cracked wall sections, rusted bunks and lockers, a ventilation fan room. Bare bulbs, damp concrete, stencilled hazard stripes.",
    leg={'#': 'thick reinforced-concrete walls (door gaps stay open, with open blast doors)', 'W': 'cracked, crumbling wall sections marked with yellow hazard tape (must look breakable)', 'C': 'bunks, lockers, ammunition crates, fallen debris', 'B': 'a big ventilation fan housing and a generator', 'X': 'a locker with four dog tags hanging on it', 'S': 'the entry hatch ladder'})

add(id='brick_2', pack='romantic', file='bgp_brick_2.jpg', ko='BRICK TAKE 2 · 인식표 — 지하 격투장', size=Q,
    ops=[F('B', 7, 7, 11, 11), F('C', 5, 5, 13, 5), F('C', 5, 13, 13, 13), F('C', 5, 7, 5, 11), F('C', 13, 7, 13, 11),
         Pt('.', (9, 5), (9, 13), (5, 9), (13, 9)),
         O('#', 1, 1, 4, 4), Pt('.', (4, 3)), O('#', 14, 1, 17, 4), Pt('.', (14, 3)), Pt('C', (16, 2), (2, 2)),
         O('#', 13, 14, 17, 17), Pt('.', (13, 16)), Pt('C', (2, 15), (3, 15), (2, 16), (8, 16), (10, 2), (7, 2))],
    S=[(1, 8), (1, 9)], X=(16, 15),
    scene="An illegal underground fight club in a converted warehouse, roof removed. A raised boxing ring under a hard cone of light in the centre, rough bleacher benches on all four sides, a locker room, a bookmaker's office, a holding cell. Smoke haze, everything outside the ring light is dark.",
    leg={'#': 'brick partition walls of the locker room, office and holding cell (door gaps stay open)', 'B': 'the raised boxing ring with ropes and corner posts', 'C': 'bleacher benches, a bar counter, beer crates, betting tables', 'X': 'the barred holding-cell cot', 'S': 'the side service entrance'})

add(id='brick_3', pack='romantic', file='bgp_brick_3.jpg', ko='BRICK TAKE 3 · 노크 — 채석장 발파 구역', size=L, border='B',
    ops=[F('=', 14, 6, 20, 9), F('B', 1, 5, 16, 5), Pt('.', (4, 5), (13, 5)), F('B', 5, 10, 20, 10), Pt('.', (8, 10), (17, 10)),
         O('#', 17, 1, 20, 4), Pt('.', (17, 3)), O('#', 1, 11, 4, 14), Pt('.', (4, 13)),
         F('B', 7, 2, 8, 3), F('B', 11, 7, 12, 8), F('B', 15, 12, 16, 12),
         Pt('C', (3, 2), (11, 2), (15, 3), (3, 7), (7, 8), (16, 7), (19, 8), (7, 12), (11, 13), (19, 12), (13, 12), (2, 9))],
    S=[(9, 14), (10, 14)], X=(19, 2),
    scene="An open-pit stone quarry at night. Three stepped terraces cut into grey rock, each a level floor separated by low cliff steps with ramps, excavators and a dump truck, an explosives magazine, a site office, a marked blasting zone. Sodium work lights, stone dust.",
    leg={'B': 'rock faces: the quarry rim, the cliff steps between terraces, and parked heavy machines (excavator, dump truck, drill rig)', '#': 'the explosives magazine and the site office (door gaps stay open)', 'C': 'cut stone blocks, rock piles, cable reels, barrels', '=': 'the blasting zone (ground marked with red flags and drilled holes)', 'X': 'the steel door of the inner store', 'S': 'the haul road in'})

add(id='mirage_1', pack='romantic', file='bgp_mirage_1.jpg', ko='MIRAGE TAKE 1 · 초대장 — 야간 유람선', size=P, border='', fill='V',
    ops=[F('.', 2, 3, 13, 19), F('.', 5, 1, 10, 2), F('.', 4, 20, 11, 20),
         O('#', 3, 4, 12, 9), Pt('.', (7, 4), (8, 9), (3, 7), (12, 6)), Pt('C', (5, 6), (10, 6), (6, 7), (9, 7)),
         O('#', 3, 11, 12, 17), Pt('.', (7, 11), (8, 17)), F('#', 6, 12, 6, 16), F('#', 9, 12, 9, 16),
         Pt('#', (4, 14), (5, 14), (10, 14), (11, 14)), Pt('.', (6, 12), (6, 16), (9, 13), (9, 15)),
         Pt('C', (6, 2), (9, 18), (4, 19), (11, 19), (4, 16), (11, 16)), Pt('B', (7, 1), (8, 1))],
    S=[(7, 20), (8, 20)], X=(11, 12),
    scene="A river cruise ship at night seen from above with the upper deck removed. The hull fills the image lengthwise, dark water all around: a glittering ballroom forward, a block of small cabins on a narrow inner corridor aft, narrow side decks along both rails, a bow deck and a stern deck. String lights, reflections on black water.",
    leg={'V': 'the river (black water, light reflections, wake)', '#': 'the ship\'s interior bulkheads: ballroom walls and cabin walls (door gaps stay open)', 'C': 'banquet tables, deck chairs, luggage, bar carts', 'B': 'the anchor winch on the bow', 'X': 'a cabin writing desk with an invitation card', 'S': 'the stern boarding deck'})

add(id='mirage_2', pack='romantic', file='bgp_mirage_2.jpg', ko='MIRAGE TAKE 2 · 역할 — 오페라 극장 무대 뒤', size=L,
    ops=[F('=', 6, 1, 15, 5), F('B', 5, 6, 16, 6), Pt('.', (8, 6), (13, 6)), Pt('B', (3, 2), (3, 4), (18, 2), (18, 4)),
         Pt('C', (4, 8), (10, 8), (11, 8), (17, 8), (1, 8), (20, 8)),
         F('#', 1, 10, 20, 10), Pt('.', (3, 10), (9, 10), (14, 10), (19, 10)), F('#', 6, 11, 6, 14), F('#', 11, 11, 11, 14), F('#', 16, 11, 16, 14),
         Pt('C', (4, 13), (8, 12), (8, 13), (18, 12), (13, 11), (19, 14))],
    S=[(1, 12), (1, 13)], X=(14, 13),
    scene="Backstage of a grand opera house during a performance, roof removed. The lit stage with painted scenery at the top, a heavy main curtain line, dark wings with scenery flats, a cluttered crossover corridor, then a row of four rooms: a stage-door room, a props store, a star dressing room, a wardrobe room. Warm bulb-ringed mirrors, deep shadow elsewhere.",
    leg={'#': 'backstage walls between the corridor and the four rooms (door gaps stay open)', 'B': 'the heavy red main curtain (two wing gaps stay open) and tall scenery flats in the wings', 'C': 'prop tables, costume racks, trunks, a piano, make-up tables', '=': 'the stage floor under bright show lighting', 'X': 'the dressing-room vanity with an old photograph tucked in the mirror', 'S': 'the stage door'})

add(id='mirage_3', pack='romantic', file='bgp_mirage_3.jpg', ko='MIRAGE TAKE 3 · 맨얼굴 — 문 닫은 백화점', size=P,
    ops=[F('B', 7, 9, 8, 12), O('#', 0, 0, 4, 4), Pt('.', (4, 2)),
         Pt('C', (6, 2), (7, 3), (11, 3), (12, 3), (3, 6), (6, 5), (9, 5), (12, 6), (8, 7), (2, 12), (13, 12), (5, 14), (10, 14), (3, 16), (12, 16), (7, 15)),
         F('C', 2, 9, 4, 9), F('C', 11, 9, 13, 9), Pt('B', (5, 8), (10, 8), (5, 13), (10, 13)),
         F('#', 1, 18, 5, 18), F('#', 10, 18, 14, 18)],
    S=[(7, 20), (8, 20)], X=(2, 2),
    scene="A department-store fashion floor after closing, roof removed. Dozens of mannequins on low display islands, glass counters, an escalator bank in the centre, show windows either side of the entrance, a small security room in the corner. Only night lighting and the glow of the show windows.",
    leg={'#': 'the security-room walls and the show-window backs by the entrance (door gap stays open)', 'B': 'the escalator bank and square mirrored pillars', 'C': 'low display islands each carrying dressed mannequins, and glass counters (mannequins must be clearly visible)', 'X': 'a chair in the security room with cut ropes', 'S': 'the main entrance doors'})

add(id='doc_1', pack='romantic', file='bgp_doc_1.jpg', ko='DOC TAKE 1 · 차트 — 폐병원 지하 기록실', size=L,
    ops=[F('~', 1, 7, 20, 8), F('#', 1, 6, 20, 6), Pt('.', (3, 6), (9, 6), (15, 6), (19, 6)),
         F('#', 6, 1, 6, 5), F('#', 12, 1, 12, 5), F('#', 17, 1, 17, 5),
         F('#', 1, 9, 20, 9), Pt('.', (5, 9), (13, 9), (18, 9)), F('#', 8, 10, 8, 14), F('#', 15, 10, 15, 14),
         F('B', 13, 2, 13, 4), Pt('B', (14, 4), (19, 2), (10, 12), (11, 12)), F('~', 1, 4, 5, 5), F('~', 9, 13, 14, 14),
         Pt('C', (8, 2), (10, 2), (8, 4), (10, 4), (2, 2), (4, 2), (3, 12), (5, 13), (7, 7), (14, 8), (18, 4))],
    S=[(19, 13), (20, 13)], X=(15, 2),
    scene="The flooded basement of an abandoned hospital, roof removed. A central corridor ankle-deep in dark water, off it a chart archive with rusted shelves, a morgue with steel slabs, a boiler room, a laundry and a dry store. Peeling paint, one working lamp, reflections on the water.",
    leg={'#': 'basement walls with peeling tiles (door gaps stay open)', '~': 'standing flood water, ankle-deep, reflecting light (walkable)', 'B': 'tall rusted chart shelves, the boiler, industrial washing machines', 'C': 'morgue slabs, gurneys, wheelchairs, boxes of files', 'X': 'the filing cabinet with the altered chart', 'S': 'the stairwell down'})

add(id='doc_2', pack='romantic', file='bgp_doc_2.jpg', ko='DOC TAKE 2 · 이송 — 병원 옥상 헬기장', size=Q, border='V',
    ops=[F('=', 6, 3, 12, 9), F('B', 2, 2, 3, 3), F('B', 15, 2, 16, 4),
         Pt('B', (2, 7), (3, 7), (15, 8), (2, 11), (3, 12), (8, 12), (9, 12), (14, 12), (15, 12), (8, 1), (10, 1)),
         Pt('C', (4, 10), (12, 11), (6, 14), (11, 15), (14, 6), (4, 5), (16, 10)),
         O('#', 1, 14, 4, 17), Pt('.', (4, 15)), F('=', 14, 15, 17, 17)],
    S=[(2, 15), (2, 16)], X=(9, 1),
    scene="A hospital rooftop helipad at night in strong wind. A large painted H pad with edge lights, HVAC plant and ducting around it, a stairwell house, a ramp down toward the ambulance bay, a small flight-ops booth at the far edge. City glow beyond the parapet, a sweeping searchlight.",
    leg={'V': 'the roof edge and the drop to the city below', '#': 'the stairwell house (door gap stays open)', 'B': 'HVAC units, cooling towers, big ducts and the flight-ops booth walls', 'C': 'medical supply cases, a stretcher trolley, fuel drums, low pipes', '=': 'the painted helipad surface and the striped vehicle ramp', 'X': 'the flight log on the ops-booth counter', 'S': 'inside the stairwell house'})

add(id='doc_3', pack='romantic', file='bgp_doc_3.jpg', ko='DOC TAKE 3 · 퇴원 — 산속 요양원', size=P, border='B',
    ops=[O('#', 2, 1, 13, 6), Pt('.', (7, 6), (8, 6)), F('#', 7, 2, 7, 3), Pt('C', (4, 2), (4, 4), (10, 4)),
         O('#', 9, 9, 13, 13), Pt('.', (9, 11)), Pt('C', (11, 10), (12, 12)),
         F('B', 2, 8, 6, 8), F('B', 2, 10, 2, 14), F('B', 4, 10, 7, 10), F('B', 4, 12, 4, 15), F('B', 6, 12, 7, 12), F('B', 6, 14, 8, 14),
         F('B', 2, 16, 5, 16), F('B', 10, 15, 13, 15), F('B', 8, 16, 8, 18), F('B', 11, 17, 13, 17),
         Pt('C', (3, 18), (12, 19), (6, 19), (14, 8))],
    S=[(7, 20), (8, 20)], X=(11, 2),
    scene="A secluded mountain sanatorium at dawn in thick fog. A long ward building at the top, a glass greenhouse, and in front of them a formal garden of tall clipped hedges forming a small maze with gravel paths and benches. Pale grey light, mist pooling between the hedges.",
    leg={'B': 'tall clipped hedges (the maze and the boundary)', '#': 'the ward building walls and the glass-and-iron greenhouse (door gaps stay open)', 'C': 'beds, garden benches, potted plants, a wheelbarrow', 'X': 'the patient\'s bed by the window', 'S': 'the garden gate'})

# ───────────────────────── 블러디 크리스마스 5
add(id='w1', pack='winter', file='bgw1.jpg', ko='STAGE 1 · 첫 번째 상자 — 시청 앞 크리스마스 마켓', size=Q, border='B',
    ops=[F('=', 7, 1, 11, 2), F('V', 2, 1, 3, 2), F('B', 14, 1, 16, 2)] +
        [F('C', 3, y, 7, y) for y in (4, 7, 11, 14)] + [F('C', 11, y, 15, y) for y in (4, 7, 11, 14)] +
        [Pt('.', (5, 4), (13, 7), (5, 11), (13, 14), (12, 4), (4, 14)), F('B', 8, 8, 10, 10), Pt('C', (1, 9), (17, 9), (9, 5), (9, 14), (2, 16), (16, 16))],
    S=[(9, 17), (10, 17)], X=(9, 11),
    scene="A snowy city-hall square Christmas market at dusk. Rows of wooden stalls with striped awnings forming alleys, a giant decorated tree in the centre with a pile of gifts beneath it, a carousel, a frozen fountain, a small stage. Warm string lights in the middle, dark blue shadow at the edges.",
    leg={'B': 'the surrounding building fronts, the giant Christmas tree (centre block) and the carousel', 'C': 'market stalls with awnings, barrels, sleigh props, crates', 'V': 'the frozen fountain basin', '=': 'the small wooden stage', 'X': 'the gift pile under the tree', 'S': 'the street entrance arch'})

add(id='w2', pack='winter', file='bgw2.jpg', ko='STAGE 2 · 화차 44호 — 화물 조차장', size=L, border='B',
    ops=[F('=', 1, y, 20, y) for y in (2, 4, 7, 10, 13)] +
        [F('B', 2, 2, 8, 2), F('B', 11, 2, 19, 2), F('B', 1, 4, 5, 4), F('B', 8, 4, 14, 4), F('B', 17, 4, 20, 4),
         F('B', 2, 7, 8, 7), F('B', 15, 7, 20, 7), F('#', 10, 6, 12, 8),
         F('B', 1, 10, 6, 10), F('B', 9, 10, 16, 10), F('B', 19, 10, 20, 10), F('B', 5, 13, 10, 13), F('B', 13, 13, 18, 13),
         Pt('C', (3, 5), (11, 5), (18, 8), (7, 11), (13, 11), (2, 12), (20, 12), (16, 3), (6, 8)), Pt('B', (1, 1), (20, 14))],
    S=[(1, 14), (2, 14)], X=(9, 2),
    scene="A freight rail yard at night in falling snow. Five parallel tracks running the long way with lines of boxcars and gaps between cars, stacked containers, a brick signal cabin in the middle, two tall floodlight towers casting wide circles of light. Snow on the car roofs, steam from a heater.",
    leg={'B': 'the yard fence line, lines of boxcars standing on the tracks, and two floodlight towers at opposite corners', '#': 'the signal cabin', 'C': 'shipping containers, pallet stacks, rail-tie piles', '=': 'empty stretches of rail track (rails and sleepers on gravel, walkable)', 'X': 'the open side door of the marked boxcar, with gift-wrapped crates inside', 'S': 'the gap in the fence'})

add(id='w3', pack='winter', file='bgw3.jpg', ko='STAGE 3 · 얼음 위의 선물 — 얼어붙은 호수와 보트하우스', size=Q, border='B',
    ops=[F('~', 1, 1, 12, 11), F('=', 9, 3, 12, 3), O('#', 13, 1, 16, 4), Pt('.', (13, 3)),
         O('#', 1, 13, 5, 16), Pt('.', (5, 15)), Pt('C', (3, 14)),
         Pt('B', (4, 3), (9, 6), (3, 8), (8, 9), (14, 7), (16, 6), (15, 9), (13, 10), (16, 11), (14, 13), (16, 14), (12, 15), (9, 14), (7, 16), (10, 16), (8, 13)),
         Pt('C', (6, 6), (11, 1), (2, 5), (10, 8), (5, 10), (7, 2))],
    S=[(16, 17), (17, 17)], X=(15, 2),
    scene="A vast frozen lake at night under a full moon. Open ice across most of the image with a few ice-fishing huts and sled piles, a wooden pier leading to a boathouse, a lodge on the near shore, dense birch forest along the shore. Wide and empty, wind-blown snow streaks on blue ice.",
    leg={'B': 'birch trees (forest edge and scattered shore trees) and, on the ice, small ice-fishing huts', '#': 'the boathouse and the lakeside lodge (door gaps stay open)', 'C': 'sled piles, fishing gear crates, snow drifts', '~': 'the frozen lake surface (blue ice with snow streaks, walkable)', '=': 'the wooden pier', 'X': 'a cot in the boathouse where the witness is held', 'S': 'the forest path'})

add(id='w4', pack='winter', file='bgw4.jpg', ko='STAGE 4 · 자정 미사 — 대성당', size=P,
    ops=[F('=', 5, 1, 10, 3)] + [F('C', 4, y, 6, y) for y in range(6, 17, 2)] + [F('C', 9, y, 11, y) for y in range(6, 17, 2)] +
        [Pt('B', (3, 5), (12, 5), (3, 9), (12, 9), (3, 13), (12, 13), (3, 17), (12, 17)),
         F('B', 1, 8, 1, 9), F('B', 14, 8, 14, 9), Pt('B', (1, 13), (14, 13), (14, 19)), Pt('V', (1, 19)),
         Pt('C', (7, 3), (3, 2), (12, 2), (1, 3), (14, 3)), F('#', 1, 18, 5, 18), F('#', 10, 18, 14, 18)],
    S=[(7, 20), (8, 20)], X=(8, 1),
    scene="The interior of a grand cathedral at midnight mass, roof removed. Two long columns of pews down the nave, stone pillars, side aisles with confessional booths, a raised sanctuary with the altar, choir stalls, a narthex at the entrance with a bell-tower stair and a crypt opening. Hundreds of candles, warm near the altar, cold stone elsewhere.",
    leg={'#': 'cathedral walls and the narthex screen (centre opening stays open)', 'B': 'stone pillars, wooden confessional booths, the bell-tower stair turret', 'C': 'rows of wooden pews, the altar table, choir stalls, candle stands', 'V': 'the open crypt stairwell', '=': 'the raised sanctuary floor with a red carpet', 'X': 'the offering box behind the altar', 'S': 'the west door'})

add(id='w5', pack='winter', file='bgw5.jpg', ko='STAGE 5 · 산타의 썰매 — 사설 비행장', size=L, border='B',
    ops=[F('=', 1, 2, 20, 4), F('=', 9, 5, 10, 8), O('#', 12, 7, 20, 13), F('.', 12, 9, 12, 11),
         F('B', 16, 9, 18, 10), Pt('C', (14, 8), (19, 12), (14, 12)),
         F('B', 2, 7, 3, 8), F('B', 6, 7, 7, 7), F('B', 5, 11, 6, 11), F('B', 9, 11, 10, 11),
         Pt('C', (3, 5), (7, 5), (13, 5), (17, 5), (4, 10), (8, 9), (2, 12), (10, 13), (5, 1), (15, 1))],
    S=[(1, 14), (2, 14)], X=(17, 11),
    scene="A private airfield in heavy snow before dawn. A lit runway along the top with rows of edge lights, a taxiway, a large open hangar with a private jet inside, a control tower, fuel trucks and a snowplow on the apron, snowbanks, a perimeter fence. Blue-white light, drifting snow.",
    leg={'B': 'the perimeter fence and snow berm, the control tower, two fuel trucks, a snowplow, and the private jet inside the hangar', '#': 'the hangar walls (the wide front opening stays open)', 'C': 'ploughed snowbanks, tool carts, cargo cases', '=': 'the cleared runway and taxiway tarmac with edge lights', 'X': 'the jet\'s open cargo door with a ribbon-tied box', 'S': 'the cut in the fence'})

# ───────────────────────── 코스튬 6  (큰 맵: 칸 60x30, 가로+세로 = 46)
# N = 대화 지점(걸을 수 있음) 2곳, D = 가짜 목표(X 와 똑같이 그린다) 2곳, X = 진짜 목표
P2, L2, Q2 = (20, 26), (26, 20), (23, 23)

add(id='c_raven', pack='costume', file='bgc_raven.jpg', ko='RAVEN · 붉은 막 — 원형 공연장', size=Q2, tw=60,
    ops=[F('=', 8, 8, 14, 14), O('C', 7, 7, 15, 15), Pt('.', (11, 7), (11, 15), (7, 11), (15, 11)),
         F('B', 5, 1, 17, 3), F('.', 10, 2, 12, 3), F('B', 1, 6, 3, 16), F('B', 19, 6, 21, 16), F('B', 5, 19, 9, 21), F('B', 13, 19, 17, 21),
         O('#', 0, 0, 4, 4), Pt('.', (2, 4)), O('#', 18, 0, 22, 4), Pt('.', (20, 4)),
         O('#', 0, 18, 3, 22), Pt('.', (3, 20)), O('#', 19, 18, 22, 22), Pt('.', (19, 20)),
         Pt('C', (5, 5), (17, 5), (5, 17), (17, 17), (9, 5), (13, 5), (4, 9), (4, 13), (18, 9), (18, 13), (9, 17), (13, 17), (21, 3), (3, 1))],
    S=[(10, 21), (11, 21), (12, 21)], X=(1, 20), D=[(11, 2), (20, 2)], N=[(2, 2), (20, 20)],
    scene="A circular show arena dressed for a red-and-black matador-themed gala night, roof removed. A sand ring in the centre under spotlights, a low wooden barrier around it with four gates, banked seating blocks on all four sides with the owner's box cut into the top block, and four corner rooms: a wardrobe room, the owner's office, a prop store, a bookmaker's room. Red drapes, gold trim, drifting stage smoke.",
    leg={'#': 'the arena outer wall and the walls of the four corner rooms (door gaps stay open)', 'B': 'banked seating blocks', 'C': 'the low red wooden ring barrier (four gate gaps stay open), flower stands, drinks tables, costume trunks', '=': 'the sand ring under spotlights', 'X': 'three identical black lockboxes with gold trim, one in the owner\'s box, one in the office, one in the prop store', 'N': 'two conversation spots: a mirror-lit corner of the wardrobe room, and the bookmaker\'s desk front', 'S': 'the performers\' tunnel'})

add(id='c_viper', pack='costume', file='bgc_viper.jpg', ko='VIPER · 은반 — 아이스링크 갈라쇼', size=L2, tw=60,
    ops=[F('~', 6, 4, 19, 11), O('C', 5, 3, 20, 12), Pt('.', (5, 7), (20, 8), (12, 12), (13, 3)),
         F('B', 5, 1, 11, 1), F('B', 15, 1, 20, 1), O('#', 22, 0, 25, 7), Pt('.', (22, 4)), O('#', 0, 0, 3, 6), Pt('.', (3, 4)), Pt('B', (1, 2), (24, 11)),
         F('#', 1, 13, 24, 13), Pt('.', (4, 13), (12, 13), (21, 13)), F('#', 8, 14, 8, 18), F('#', 16, 14, 16, 18),
         Pt('C', (3, 15), (5, 17), (10, 15), (14, 17), (19, 15), (20, 17), (22, 10), (23, 10), (2, 9), (2, 10), (24, 2))],
    S=[(1, 17), (1, 18)], X=(22, 16), D=[(2, 5), (24, 5)], N=[(23, 2), (12, 16)],
    scene="An indoor ice rink set up for a gala figure-skating show, roof removed. A large oval of ice under violet and silver spotlights, rink boards all around with four gates, seating blocks, a glass VIP lounge in one corner, an ice-resurfacer garage in another, and along the near side three rooms: a locker room, a coaches' room, a judges' room. Frost haze, glitter on the ice.",
    leg={'#': 'the rink hall walls and the walls of the VIP lounge, the garage and the three rooms (door gaps stay open)', 'B': 'seating blocks, the ice-resurfacing machine, a scoreboard tower', 'C': 'the rink boards (four gate gaps stay open), benches, flower-and-plush bins, a kiss-and-cry sofa', '~': 'the ice surface under violet spotlights (walkable)', 'X': 'three identical silver jewel cases on small stands, one in the garage, one in the VIP lounge, one in the judges\' room', 'N': 'two conversation spots: a champagne table in the VIP lounge, and the coach\'s chair in the middle room', 'S': 'the skaters\' entrance'})

add(id='c_glitch', pack='costume', file='bgc_glitch.jpg', ko='GLITCH · 앙코르 — 콘서트 돔 백스테이지', size=L2, tw=60,
    ops=[F('=', 6, 1, 19, 4), Pt('V', (12, 2), (13, 2)), F('B', 6, 5, 19, 5), Pt('.', (9, 5), (16, 5)), Pt('B', (3, 2), (3, 4), (22, 2), (22, 4), (6, 12), (19, 12)),
         Pt('C', (4, 7), (5, 7), (10, 8), (11, 8), (14, 8), (15, 8), (20, 7), (21, 7), (7, 10), (8, 10), (17, 10), (18, 10), (12, 11), (2, 11), (23, 10)),
         F('#', 1, 13, 24, 13), Pt('.', (3, 13), (9, 13), (16, 13), (22, 13)), F('#', 6, 14, 6, 18), F('#', 12, 14, 12, 18), F('#', 19, 14, 19, 18),
         Pt('C', (4, 15), (8, 17), (10, 15), (21, 15)), Pt('B', (17, 15), (17, 17))],
    S=[(1, 8), (1, 9)], X=(15, 16), D=[(9, 16), (23, 15)], N=[(2, 16), (21, 17)],
    scene="Backstage of a huge concert dome during an idol show, roof removed. The stage at the top washed in teal laser light with an open stage-lift pit, a giant LED wall seen from behind, speaker towers, a wide floor crowded with flight cases and cable runs, and along the near side four rooms: a dressing room, a green room, the production control room, an equipment store. Teal and magenta glow leaking round the LED wall.",
    leg={'#': 'the venue walls and the walls of the four rooms (door gaps stay open)', 'B': 'the back of the giant LED wall (two gaps stay open), speaker towers, truss legs, equipment racks', 'C': 'flight cases, cable drums, costume racks, monitor desks', 'V': 'the open stage-lift pit', '=': 'the stage floor under teal lasers', 'X': 'three identical black rack-mount show servers with teal status lights, one in the green room, one in the control room, one in the equipment store', 'N': 'two conversation spots: the make-up mirror in the dressing room, and a mixing desk in the equipment store', 'S': 'the loading dock door'})

add(id='c_brick', pack='costume', file='bgc_brick.jpg', ko='BRICK · 타이틀 매치 — 호텔 특설 링', size=Q2, tw=60,
    ops=[F('=', 11, 12, 11, 20), F('B', 10, 9, 12, 11)] +
        [Pt('C', (x, y)) for x in (5, 8, 14, 17) for y in (4, 7, 14, 16) if not (y == 14 and x in (5, 17))] +
        [F('C', 2, 1, 7, 1), F('B', 15, 1, 19, 1),
         O('#', 0, 18, 5, 22), Pt('.', (5, 20)), O('#', 17, 18, 22, 22), Pt('.', (17, 20)),
         O('#', 0, 8, 3, 13), Pt('.', (3, 10)), O('#', 19, 8, 22, 13), Pt('.', (19, 11)), Pt('C', (3, 19), (20, 19), (1, 12), (6, 11), (16, 10))],
    S=[(10, 21), (11, 21), (12, 21)], X=(21, 12), D=[(1, 10), (20, 21)], N=[(2, 20), (20, 9)],
    scene="A luxury hotel ballroom converted for a championship title fight, roof removed. A boxing ring on a riser in the centre, round dinner tables with white cloths all around, a long walk-in ramp, a long bar, a camera platform, and four side rooms: a kitchen, a cash office, a cloakroom, the fighters' locker room. Orange and black bunting, chandeliers, a hard white ring light.",
    leg={'#': 'ballroom walls and the walls of the four side rooms (door gaps stay open)', 'B': 'the boxing ring on its riser and the TV camera platform', 'C': 'round dinner tables with chairs, the long bar, prep counters, benches', '=': 'the fighters\' walk-in ramp with an orange carpet', 'X': 'three identical orange-and-black sports duffel bags on low benches, one in the cloakroom, one in the cash office, one in the locker room', 'N': 'two conversation spots: the pass of the kitchen, and the cutman\'s stool in the locker room', 'S': 'the ramp entrance'})

add(id='c_mirage', pack='costume', file='bgc_mirage.jpg', ko='MIRAGE · 하우스 엣지 — 펜트하우스 카지노', size=P2, tw=60,
    ops=[Pt('C', (3, 3), (4, 3), (8, 3), (9, 3), (11, 5), (3, 7), (4, 7), (14, 8), (15, 8), (9, 7), (10, 7), (7, 21), (12, 22), (2, 17), (17, 17)),
         F('B', 2, 11, 2, 15), F('B', 17, 11, 17, 15), F('C', 8, 11, 12, 11), Pt('B', (6, 5), (13, 9), (6, 9), (5, 13), (14, 13)),
         O('#', 7, 14, 12, 18), Pt('.', (9, 14)), O('#', 14, 0, 19, 6), Pt('.', (14, 3)), Pt('C', (17, 4)),
         O('#', 0, 19, 5, 25), Pt('.', (5, 21)), O('#', 14, 19, 19, 25), Pt('.', (14, 21)), Pt('B', (16, 20))],
    S=[(9, 24), (10, 24)], X=(2, 22), D=[(10, 16), (17, 22)], N=[(16, 2), (13, 11)],
    scene="A private penthouse casino at night, roof removed. Green baize card tables and a roulette wheel, rows of slot machines, a gold-lit bar, a barred cashier's cage in the middle of the floor, a VIP salon in one corner, and by the elevator lobby a count room and a surveillance room. Black marble, gold trim, low amber light, city lights through the windows.",
    leg={'#': 'penthouse walls, the barred cashier\'s cage, and the walls of the VIP salon, count room and surveillance room (door gaps stay open)', 'B': 'rows of slot machines, gilded pillars, a bank of monitors', 'C': 'blackjack, baccarat and roulette tables, the bar counter, lounge sofas', 'X': 'three identical steel strongboxes with a gold crest, one in the cage, one in the surveillance room, one in the count room', 'N': 'two conversation spots: a private card table in the VIP salon, and the end of the bar', 'S': 'the private elevator'})

add(id='c_doc', pack='costume', file='bgc_doc.jpg', ko='DOC · 왕진 — 프라이빗 클리닉 & 스파', size=L2, tw=60,
    ops=[F('#', 1, 7, 12, 7), Pt('.', (3, 7), (9, 7)), F('#', 6, 1, 6, 6), F('#', 12, 1, 12, 7), Pt('.', (12, 4)),
         F('V', 15, 2, 21, 6), O('#', 22, 7, 25, 11), Pt('.', (22, 9)),
         F('#', 8, 12, 24, 12), Pt('.', (12, 12), (20, 12)), F('#', 16, 13, 16, 18), F('#', 8, 13, 8, 18), Pt('.', (8, 16)),
         Pt('B', (10, 14), (11, 14), (13, 17), (14, 17), (1, 9), (13, 10)), F('C', 3, 11, 5, 11),
         Pt('C', (2, 2), (4, 4), (8, 4), (14, 8), (17, 8), (20, 8), (23, 3), (23, 5), (2, 15), (5, 16), (3, 17), (19, 16), (20, 14), (10, 10))],
    S=[(1, 17), (1, 18)], X=(14, 14), D=[(10, 2), (22, 15)], N=[(3, 5), (23, 9)],
    scene="A private cosmetic clinic and spa for the very rich at night, roof removed. A marble reception, a treatment room and a records room, a turquoise spa pool with loungers, a small sauna cabin, a locked pharmacy and the director's office. White stone, lime-green accent lighting, orchids, soft steam.",
    leg={'#': 'clinic walls and glass partitions, the sauna cabin (door gaps stay open)', 'V': 'the spa pool (glowing turquoise water)', 'B': 'pharmacy shelving and large potted palms', 'C': 'the reception desk, treatment beds, loungers, sofas, instrument trolleys', 'X': 'three identical white medical cooler cases with a lime stripe, one in the records room, one in the director\'s office, one in the pharmacy', 'N': 'two conversation spots: beside the treatment bed, and the bench inside the sauna', 'S': 'the street door'})
