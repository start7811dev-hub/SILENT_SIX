# SILENT SIX — 코스튬 미션 원샷 생성 세트

맵 6장 + 대화 일러스트 54장 + 리워드 컷 24장 = **84장**.

## 사용법 (사람이 읽는 부분)

1. ChatGPT 새 대화에 이 zip 파일을 그대로 올린다.
2. 다음 한 줄을 보낸다: **"압축을 풀고 지시.md 를 끝까지 읽은 뒤, PART A 부터 순서대로 진행해 줘."**
3. 한 번에 한 묶음씩 나온다. 이어서 받을 때는 "next".
4. 대화가 길어져 끊기면 새 대화에 zip 을 다시 올리고 **"지시.md 의 PART B 의 <파일명> 부터 이어서"** 처럼 이어 간다.
5. 파일명은 지시된 그대로 저장한다. 받은 그림을 Claude에게 넘기면 게임에 들어간다.

| PART | 내용 | 장수 | 파일명 | 규격 |
|---|---|---|---|---|
| A | 맵 | 6 | `bgc_<요원>.jpg` | 1536×1024 |
| B | 대화 일러스트 | 54 | `d_C-<요원>_n1_<0..2>.png` · `_n2_` · `_me_` | 1024×1536, 배경 투명 |
| C | 리워드 컷 | 24 | `r_C-<요원>_<0..3>.jpg` | 1024×1536 |

검수: A는 가이드와 겹쳐 블록 위치가 맞는지, B는 표정 3장이 같은 사람 · 같은 옷 · 같은 자세인지, C는 얼굴이 참조와 같은지 본다.

---

## FOR THE IMAGE MODEL — READ ALL OF THIS FIRST

This archive is one production job in three parts. Do PART A, then PART B, then PART C, in the order written. Never skip ahead. Do not ask questions; where something is ambiguous, follow the reference files. Before every image, write its output file name on its own line. After each unit of work (one map in A, one character's three expressions in B, one agent's four images in C) stop and wait for "next".

Folders: `guides/` map blueprints, `LEGEND.png` guide colours, `style/` two finished maps as style references for PART A, `AGENTS.md` and `agents/sheet_<name>.jpg` the cast bible for PART B and PART C (three labelled panels per agent: `NAME-A` face, `NAME-B` glam, `NAME-C` tactical; read AGENTS.md before PART B).

Everyone depicted is an adult. No text, no logos, no watermarks in any image.

---

# PART A — MAPS (6 images)

You are painting final game-map backgrounds for a real-time stealth tactics game (quarter-view, like Commandos or Shadow Tactics). The game's collision data is already fixed. Each map comes with a **guide image** in `guides/`: a flat-coloured block-out rendered with the game's exact camera. Your job is to turn each block-out into finished painted art **without moving anything**.

### Files used in this part
- `guides/guide_<id>.png` — one block-out per map, 1536x1024. **This is the layout blueprint.**
- `LEGEND.png` — what each guide colour means.
- `style/style_ref_1.jpg`, `style/style_ref_2.jpg` — two finished maps from the same game. Match their rendering style, level of detail, camera and lighting quality. Do not copy their content.

### Hard rules (most important first)
1. **Use the guide as an image reference and repaint over it.** Output must be exactly **1536x1024**, landscape, with the map diamond in the same place, same size, same camera angle (2:1 isometric; the floor-cell size is given per map) as the guide. Do not rotate, zoom, crop, re-centre or change perspective.
2. **Every block stays where it is.** Each coloured block in the guide becomes one solid object with the same footprint, the same position and about the same height. Do not add, remove, merge, shift or resize blocks. Do not add any new solid object on plain floor. Small flat decoration (stains, cables, rugs, leaves, floor markings) is welcome on floor tiles as long as it clearly reads as walkable ground.
3. **Gaps stay open.** Every opening between blocks (doorways, alleys, gates) must stay clearly open and walkable, at the same width.
4. **Readable gameplay.** Walkable floor must be clearly distinguishable from solid objects. Tall blocks must look tall, low blocks must look waist-high. Keep floors a little brighter and calmer than the objects standing on them.
5. Interiors are drawn with the roof removed, walls cut at one height with a visible flat top, exactly like the grey blocks.
6. Outside the map diamond keep the flat dark background colour `#06080b` (or fade to it). No horizon, no sky.
7. **No characters, no people, no animals, no text, no numbers, no UI, no grid lines, no watermark.**
8. Style: detailed hand-painted isometric game art, the same style as the two style references. Semi-realistic, crisp edges, soft baked lighting from the upper left, gentle ambient occlusion at the base of walls.

### Guide colours
- **GREY tall blocks** — structural walls.
- **GREEN tall blocks** — tall solid objects (meaning is given per map).
- **TAN low blocks** — low cover, about waist height (meaning per map).
- **YELLOW tall blocks** — breakable wall sections (only on some maps).
- **CYAN block** — the mission objective. Make it the most eye-catching object, but keep its footprint. Most maps have one. Where a map has three cyan blocks, paint all three as **exactly the same object**, indistinguishable from each other.
- **PINK flat tiles** — conversation spots (only on some maps). Walkable floor. Paint a small inviting lit spot there (a rug, a pool of warm light), no person.
- Dark checker tiles — ordinary walkable floor.
- **AMBER flat tiles** — special walkable floor (meaning per map).
- **BLUE flat tiles** — wet or frozen walkable floor (meaning per map).
- **Bright GREEN flat tiles** — the entry point. Paint it as normal floor with a subtle hint of an entrance; no green.
- **Dark NAVY flat tiles** — flat but impassable (water, a drop, a pit). Must clearly read as "you cannot walk here".

### Procedure
- Work through the maps below **in order, one image per reply**. Before each image write its output file name on its own line. Do not combine maps. Do not ask questions; if something is ambiguous, follow the guide image.
- Before painting each map, open its guide and read the text grid given for that map. The grid is the same layout written in characters. If the two ever seem to disagree, the guide image wins.
- After each image, wait for me to say "next".

## Maps

### 1. `bgc_raven.jpg` — RAVEN · 붉은 막 — 원형 공연장

- Guide: `guides/guide_c_raven.png`
- Output file name: `bgc_raven.jpg`
- Grid: 23 columns x 23 rows, floor cell 60x30 px

**Scene.** A circular show arena dressed for a red-and-black matador-themed gala night, roof removed. A sand ring in the centre under spotlights, a low wooden barrier around it with four gates, banked seating blocks on all four sides with the owner's box cut into the top block, and four corner rooms: a wardrobe room, the owner's office, a prop store, a bookmaker's room. Red drapes, gold trim, drifting stage smoke.

**What the blocks are on this map**
- GREY tall blocks → the arena outer wall and the walls of the four corner rooms (door gaps stay open)
- GREEN tall blocks → banked seating blocks
- TAN low blocks → the low red wooden ring barrier (four gate gaps stay open), flower stands, drinks tables, costume trunks
- the CYAN block(s) → three identical black lockboxes with gold trim, one in the owner's box, one in the office, one in the prop store
- AMBER flat tiles → the sand ring under spotlights
- PINK flat tiles → two conversation spots: a mirror-lit corner of the wardrobe room, and the bookmaker's desk front
- bright GREEN flat tiles → the performers' tunnel

**Layout as text** (`.` floor, `D` = same object as `X`, other characters as in the legend; x runs down-right, y runs down-left, first character of the first line is the top corner)

```
#######################
#..C#BBBBBBBBBBBBB#...#
#.N.#BBBBB.D.BBBBB#.D.#
#...#BBBBB...BBBBB#..C#
##.##.............##.##
#....C...C...C...C....#
#BBB...............BBB#
#BBB...CCCC.CCCC...BBB#
#BBB...C=======C...BBB#
#BBBC..C=======C..CBBB#
#BBB...C=======C...BBB#
#BBB....=======....BBB#
#BBB...C=======C...BBB#
#BBBC..C=======C..CBBB#
#BBB...C=======C...BBB#
#BBB...CCCC.CCCC...BBB#
#BBB...............BBB#
#....C...C...C...C....#
####...............####
#..#.BBBBB...BBBBB.#..#
#X...BBBBB...BBBBB..N.#
#..#.BBBBBSSSBBBBB.#..#
#######################
```

### 2. `bgc_viper.jpg` — VIPER · 은반 — 아이스링크 갈라쇼

- Guide: `guides/guide_c_viper.png`
- Output file name: `bgc_viper.jpg`
- Grid: 26 columns x 20 rows, floor cell 60x30 px

**Scene.** An indoor ice rink set up for a gala figure-skating show, roof removed. A large oval of ice under violet and silver spotlights, rink boards all around with four gates, seating blocks, a glass VIP lounge in one corner, an ice-resurfacer garage in another, and along the near side three rooms: a locker room, a coaches' room, a judges' room. Frost haze, glitter on the ice.

**What the blocks are on this map**
- GREY tall blocks → the rink hall walls and the walls of the VIP lounge, the garage and the three rooms (door gaps stay open)
- GREEN tall blocks → seating blocks, the ice-resurfacing machine, a scoreboard tower
- TAN low blocks → the rink boards (four gate gaps stay open), benches, flower-and-plush bins, a kiss-and-cry sofa
- the CYAN block(s) → three identical silver jewel cases on small stands, one in the garage, one in the VIP lounge, one in the judges' room
- BLUE flat tiles → the ice surface under violet spotlights (walkable)
- PINK flat tiles → two conversation spots: a champagne table in the VIP lounge, and the coach's chair in the middle room
- bright GREEN flat tiles → the skaters' entrance

**Layout as text** (`.` floor, `D` = same object as `X`, other characters as in the legend; x runs down-right, y runs down-left, first character of the first line is the top corner)

```
##########################
#..#.BBBBBBB...BBBBBB.#..#
#B.#..................#NC#
#..#.CCCCCCCC.CCCCCCC.#..#
#....C~~~~~~~~~~~~~~C....#
#.D#.C~~~~~~~~~~~~~~C.#.D#
####.C~~~~~~~~~~~~~~C.#..#
#.....~~~~~~~~~~~~~~C.####
#....C~~~~~~~~~~~~~~.....#
#.C..C~~~~~~~~~~~~~~C....#
#.C..C~~~~~~~~~~~~~~C.CC.#
#....C~~~~~~~~~~~~~~C...B#
#....CCCCCCC.CCCCCCCC....#
####.#######.########.####
#.......#.......#........#
#..C....#.C.....#..C.....#
#.......#...N...#.....X..#
#S...C..#.....C.#...C....#
#S......#.......#........#
##########################
```

### 3. `bgc_glitch.jpg` — GLITCH · 앙코르 — 콘서트 돔 백스테이지

- Guide: `guides/guide_c_glitch.png`
- Output file name: `bgc_glitch.jpg`
- Grid: 26 columns x 20 rows, floor cell 60x30 px

**Scene.** Backstage of a huge concert dome during an idol show, roof removed. The stage at the top washed in teal laser light with an open stage-lift pit, a giant LED wall seen from behind, speaker towers, a wide floor crowded with flight cases and cable runs, and along the near side four rooms: a dressing room, a green room, the production control room, an equipment store. Teal and magenta glow leaking round the LED wall.

**What the blocks are on this map**
- GREY tall blocks → the venue walls and the walls of the four rooms (door gaps stay open)
- GREEN tall blocks → the back of the giant LED wall (two gaps stay open), speaker towers, truss legs, equipment racks
- TAN low blocks → flight cases, cable drums, costume racks, monitor desks
- the CYAN block(s) → three identical black rack-mount show servers with teal status lights, one in the green room, one in the control room, one in the equipment store
- dark NAVY flat tiles → the open stage-lift pit
- AMBER flat tiles → the stage floor under teal lasers
- PINK flat tiles → two conversation spots: the make-up mirror in the dressing room, and a mixing desk in the equipment store
- bright GREEN flat tiles → the loading dock door

**Layout as text** (`.` floor, `D` = same object as `X`, other characters as in the legend; x runs down-right, y runs down-left, first character of the first line is the top corner)

```
##########################
#.....==============.....#
#..B..======VV======..B..#
#.....==============.....#
#..B..==============..B..#
#.....BBB.BBBBBB.BBB.....#
#........................#
#...CC..............CC...#
#S........CC..CC.........#
#S.......................#
#......CC........CC....C.#
#.C.........C............#
#.....B............B.....#
###.#####.######.#####.###
#.....#.....#......#.....#
#...C.#...C.#....B.#.C.D.#
#.N...#..D..#..X...#.....#
#.....#.C...#....B.#.N...#
#.....#.....#......#.....#
##########################
```

### 4. `bgc_brick.jpg` — BRICK · 타이틀 매치 — 호텔 특설 링

- Guide: `guides/guide_c_brick.png`
- Output file name: `bgc_brick.jpg`
- Grid: 23 columns x 23 rows, floor cell 60x30 px

**Scene.** A luxury hotel ballroom converted for a championship title fight, roof removed. A boxing ring on a riser in the centre, round dinner tables with white cloths all around, a long walk-in ramp, a long bar, a camera platform, and four side rooms: a kitchen, a cash office, a cloakroom, the fighters' locker room. Orange and black bunting, chandeliers, a hard white ring light.

**What the blocks are on this map**
- GREY tall blocks → ballroom walls and the walls of the four side rooms (door gaps stay open)
- GREEN tall blocks → the boxing ring on its riser and the TV camera platform
- TAN low blocks → round dinner tables with chairs, the long bar, prep counters, benches
- the CYAN block(s) → three identical orange-and-black sports duffel bags on low benches, one in the cloakroom, one in the cash office, one in the locker room
- AMBER flat tiles → the fighters' walk-in ramp with an orange carpet
- PINK flat tiles → two conversation spots: the pass of the kitchen, and the cutman's stool in the locker room
- bright GREEN flat tiles → the ramp entrance

**Layout as text** (`.` floor, `D` = same object as `X`, other characters as in the legend; x runs down-right, y runs down-left, first character of the first line is the top corner)

```
#######################
#.CCCCCC.......BBBBB..#
#.....................#
#.....................#
#....C..C.....C..C....#
#.....................#
#.....................#
#....C..C.....C..C....#
####...............####
#..#......BBB......#N.#
#D........BBB...C..#..#
#..#..C...BBB.........#
#C.#.......=.......#.X#
####.......=.......####
#.......C..=..C.......#
#..........=..........#
#....C..C..=..C..C....#
#..........=..........#
######.....=.....######
#..C.#.....=.....#..C.#
#.N........=..........#
#....#....SSS....#..D.#
#######################
```

### 5. `bgc_mirage.jpg` — MIRAGE · 하우스 엣지 — 펜트하우스 카지노

- Guide: `guides/guide_c_mirage.png`
- Output file name: `bgc_mirage.jpg`
- Grid: 20 columns x 26 rows, floor cell 60x30 px

**Scene.** A private penthouse casino at night, roof removed. Green baize card tables and a roulette wheel, rows of slot machines, a gold-lit bar, a barred cashier's cage in the middle of the floor, a VIP salon in one corner, and by the elevator lobby a count room and a surveillance room. Black marble, gold trim, low amber light, city lights through the windows.

**What the blocks are on this map**
- GREY tall blocks → penthouse walls, the barred cashier's cage, and the walls of the VIP salon, count room and surveillance room (door gaps stay open)
- GREEN tall blocks → rows of slot machines, gilded pillars, a bank of monitors
- TAN low blocks → blackjack, baccarat and roulette tables, the bar counter, lounge sofas
- the CYAN block(s) → three identical steel strongboxes with a gold crest, one in the cage, one in the surveillance room, one in the count room
- PINK flat tiles → two conversation spots: a private card table in the VIP salon, and the end of the bar
- bright GREEN flat tiles → the private elevator

**Layout as text** (`.` floor, `D` = same object as `X`, other characters as in the legend; x runs down-right, y runs down-left, first character of the first line is the top corner)

```
####################
#.............#....#
#.............#.N..#
#..CC...CC.........#
#.............#..C.#
#.....B....C..#....#
#.............######
#..CC....CC........#
#.............CC...#
#.....B......B.....#
#..................#
#.B.....CCCCCN...B.#
#.B..............B.#
#.B..B........B..B.#
#.B....##.###....B.#
#.B....#....#....B.#
#......#..D.#......#
#.C....#....#....C.#
#......######......#
######........######
#....#........#.B..#
#......C...........#
#.X..#......C.#..D.#
#....#........#....#
#....#...SS...#....#
####################
```

### 6. `bgc_doc.jpg` — DOC · 왕진 — 프라이빗 클리닉 & 스파

- Guide: `guides/guide_c_doc.png`
- Output file name: `bgc_doc.jpg`
- Grid: 26 columns x 20 rows, floor cell 60x30 px

**Scene.** A private cosmetic clinic and spa for the very rich at night, roof removed. A marble reception, a treatment room and a records room, a turquoise spa pool with loungers, a small sauna cabin, a locked pharmacy and the director's office. White stone, lime-green accent lighting, orchids, soft steam.

**What the blocks are on this map**
- GREY tall blocks → clinic walls and glass partitions, the sauna cabin (door gaps stay open)
- GREEN tall blocks → pharmacy shelving and large potted palms
- TAN low blocks → the reception desk, treatment beds, loungers, sofas, instrument trolleys
- the CYAN block(s) → three identical white medical cooler cases with a lime stripe, one in the records room, one in the director's office, one in the pharmacy
- dark NAVY flat tiles → the spa pool (glowing turquoise water)
- PINK flat tiles → two conversation spots: beside the treatment bed, and the bench inside the sauna
- bright GREEN flat tiles → the street door

**Layout as text** (`.` floor, `D` = same object as `X`, other characters as in the legend; x runs down-right, y runs down-left, first character of the first line is the top corner)

```
##########################
#.....#.....#............#
#.C...#...D.#..VVVVVVV...#
#.....#.....#..VVVVVVV.C.#
#...C.#.C......VVVVVVV...#
#..N..#.....#..VVVVVVV.C.#
#.....#.....#..VVVVVVV...#
###.#####.###.........####
#.............C..C..C.#..#
#B.....................N.#
#.........C..B........#..#
#..CCC................####
#.......####.#######.#####
#.......#.......#........#
#.......#.BB..X.#...C....#
#.C.....#.......#.....D..#
#....C..........#..C.....#
#S.C....#....BB.#........#
#S......#.......#........#
##########################
```

---

# PART B — DIALOGUE PORTRAITS (54 images)

These are visual-novel style conversation portraits. In the game two portraits face each other: the other person on the LEFT of the screen, the agent on the RIGHT.

Rules for every portrait
- Vertical 2:3, 1024x1536. **Transparent background** (PNG). If you cannot output transparency, use a flat pure green `#00FF00` background with no shadow on it.
- Waist-up, one person, centred, head in the upper third with clear space above the hair. Nothing cropped at the sides.
- Same semi-realistic anime illustration style as the agent sheets in `agents/`. Soft key light from the front, a thin rim light.
- Each character gets **three expressions: #0, #1, #2**. The three images must be the same person, same outfit, same pose and framing; only the face (and at most a small shoulder or hand shift) changes.
- **Other people (n1, n2) face toward the RIGHT of the image** (three-quarter view). **Agents (me) face toward the LEFT of the image** (three-quarter view).
- Agents: keep the woman exactly as on her sheet (panel A: face, hair, skin tone, build), wearing the costume described. Fully clothed, glamorous, no nudity.
- No weapons in any portrait.

Expressions for other people: #0 neutral, polite, unreadable · #1 suspicious: narrowed eyes, head slightly tilted, lips pressed · #2 relaxed: a small satisfied smile, shoulders loosened.
Expressions for agents: #0 neutral, composed, a faint professional smile · #1 confident: a relaxed knowing smile, one eyebrow slightly raised · #2 tense: smile frozen, eyes sharp, jaw set.

Work one character at a time: three images, then wait for "next".

## RAVEN

- **`d_C-raven_n1_0.png`, `_1.png`, `_2.png`** — 의상 담당. Other person, faces RIGHT. The wardrobe mistress: a woman in her fifties, silver hair in a tight bun, black smock, a pin cushion on her wrist, a tape measure round her neck, a red rose pin.
- **`d_C-raven_n2_0.png`, `_1.png`, `_2.png`** — 마권업자. Other person, faces RIGHT. The bookmaker: a heavyset man in his forties, slicked-back hair, red waistcoat with gold trim, rolled sleeves, an unlit cigar, a ledger under his arm.
- **`d_C-raven_me_0.png`, `_1.png`, `_2.png`** — RAVEN in costume. Agent, faces LEFT. Sheet: `agents/sheet_raven.jpg` (short messy black hair with long side bangs, sharp red-brown eyes, pale skin, lean athletic build, cool and unreadable expression, small silver pendant). Outfit: a red-and-black matador-inspired stage outfit with her signature red scarf.

## VIPER

- **`d_C-viper_n1_0.png`, `_1.png`, `_2.png`** — 후원자 부인. Other person, faces RIGHT. The patron's wife: an elegant woman in her forties, platinum updo, white fur stole over a violet gown, a champagne flute.
- **`d_C-viper_n2_0.png`, `_1.png`, `_2.png`** — 코치. Other person, faces RIGHT. The coach: a stern man in his fifties, grey crew cut, dark team jacket, a stopwatch on a lanyard.
- **`d_C-viper_me_0.png`, `_1.png`, `_2.png`** — VIPER in costume. Agent, faces LEFT. Sheet: `agents/sheet_viper.jpg` (short silver-white hair swept to one side with an undercut, violet eyes, pale skin, tall slim build, cold half-lidded gaze, dog tags). Outfit: a violet-and-silver ice-queen figure-skating-inspired outfit.

## GLITCH

- **`d_C-glitch_n1_0.png`, `_1.png`, `_2.png`** — 매니저. Other person, faces RIGHT. The tour manager: a sharp woman in her thirties, black bob, headset, black blazer, a tablet held to her chest, a lanyard pass with no text.
- **`d_C-glitch_n2_0.png`, `_1.png`, `_2.png`** — 음향 감독. Other person, faces RIGHT. The sound director: a lanky man in his forties, short beard, grey beanie, headphones round his neck, black crew T-shirt.
- **`d_C-glitch_me_0.png`, `_1.png`, `_2.png`** — GLITCH in costume. Agent, faces LEFT. Sheet: `agents/sheet_glitch.jpg` (black hair in a messy top bun with teal-dyed tips and a shaved side, large round glasses, teal eyes, fair skin, playful grin, headphones around the neck). Outfit: a teal-neon cyber-idol stage outfit with a holographic visor pushed up on her head.

## BRICK

- **`d_C-brick_n1_0.png`, `_1.png`, `_2.png`** — 주방 책임자. Other person, faces RIGHT. The head chef: a broad man in his fifties, chef whites, a towel over one shoulder, old burn scars on his forearms.
- **`d_C-brick_n2_0.png`, `_1.png`, `_2.png`** — 컷맨. Other person, faces RIGHT. The cutman: a wiry man in his sixties, flat cap, orange-and-black corner jacket, a towel round his neck, cotton swabs tucked behind one ear.
- **`d_C-brick_me_0.png`, `_1.png`, `_2.png`** — BRICK in costume. Agent, faces LEFT. Sheet: `agents/sheet_brick.jpg` (very short bleached-blonde buzz cut, deep brown skin, amber eyes, powerful muscular build, orange goggles pushed up on her head, confident wide grin, dog tags). Outfit: an orange-and-black champion-boxer-inspired outfit with an open satin robe.

## MIRAGE

- **`d_C-mirage_n1_0.png`, `_1.png`, `_2.png`** — 하이롤러. Other person, faces RIGHT. The high roller: a suave man in his fifties, silver hair, white dinner jacket, a signet ring, a stack of chips in his fingers.
- **`d_C-mirage_n2_0.png`, `_1.png`, `_2.png`** — 피트 보스. Other person, faces RIGHT. The pit boss: a woman in her forties, sleek ponytail, black suit, an earpiece, a small gold pin with no text.
- **`d_C-mirage_me_0.png`, `_1.png`, `_2.png`** — MIRAGE in costume. Agent, faces LEFT. Sheet: `agents/sheet_mirage.jpg` (long wavy black hair, golden-brown eyes, warm tan skin, gold hoop earrings, a beauty mark, elegant curvy build, slow knowing smile). Outfit: a gold-and-black casino-dealer-inspired outfit with a bow tie and waistcoat.

## DOC

- **`d_C-doc_n1_0.png`, `_1.png`, `_2.png`** — 수간호사. Other person, faces RIGHT. The head nurse: a strict woman in her fifties, white tunic with lime piping, glasses on a chain, a clipboard.
- **`d_C-doc_n2_0.png`, `_1.png`, `_2.png`** — VIP 환자. Other person, faces RIGHT. The VIP patient: a man in his sixties in a white spa robe, a small bandage across his nose, a gold watch, a towel round his neck.
- **`d_C-doc_me_0.png`, `_1.png`, `_2.png`** — DOC in costume. Agent, faces LEFT. Sheet: `agents/sheet_doc.jpg` (dark curly hair tied up high with loose strands, green-hazel eyes, tan skin, full-sleeve tattoos on both arms, hoop earrings, dog tags, teasing confident smile). Outfit: a glossy white-and-lime nurse-inspired corset outfit with a short cropped jacket, long gloves and a medic-cross choker.


---

# PART C — REWARD CUTS (24 images)

Four images per agent. They are shown side by side as a set, so they must look like **four different illustrations by the same artist**: each cut has a different shot size, camera angle, head angle, gaze, expression, pose and colour key. Follow each cut's camera text literally. No two images of one agent may share a camera angle or a facial expression, and she faces the camera directly in at most one of them.

Format: vertical portrait 2:3, 1024x1536, one image per reply, file name on its own line first. After one agent's four images, wait for "next".

Quality for every image: painterly high-end finish like the agent sheets; three depth layers (blurred foreground object, the agent, a fully painted venue with at least five specific props); two light sources of different colour plus a rim light; visible atmosphere (smoke, steam, glitter, bokeh). Hands and costume details drawn carefully. No text, no logo, no watermark.

Identity: the agent exactly as on her sheet (panel A wins). Her signature colour must be present in every image.

### Wardrobe ladder — exposure rises from cut to cut
- **CUT 0**: the full outfit, complete and intact.
- **CUT 1**: the same outfit under stress: jacket open or torn at a shoulder, a zip pulled lower, a glove lost. Still dressed.
- **CUT 2**: clearly more revealing: outer layers off, down to a fitted top or bralette and shorts or stockings, one strap slipping, bare shoulders, midriff and thighs.
- **CUT 3**: the boldest. **No clothing and no underwear visible on her torso.** She is covered only by her own hands and arms, her hair, a turned shoulder or raised knee, or one prop named in the cut (her scarf, a fur blanket, a robe sliding off, a towel, steam). The pose must look natural and unposed, a private moment, not a pin-up presented to the camera. Keep one signature item on her (scarf, dog tags, glasses, goggles, earrings, armband) so she is still recognisably herself.

### Limits (never cross)
Implied only. Nipples, areolae and genitals are never visible in any cut: always fully hidden by hands, arms, hair, pose or the prop. No sexual acts, no touching between characters beyond leaning or an arm around a shoulder. Everyone is an adult woman in her late twenties.

## RAVEN

- Sheet: `agents/sheet_raven.jpg`
- Costume: a red-and-black matador-inspired stage outfit with her signature red scarf.
- Venue: a circular show arena on a matador-themed gala night: sand ring under spotlights, red drapes, gold trim, banked seats, stage smoke.
- Private room (CUT 3): a wardrobe room with bulb-ringed mirrors, costume trunks and red roses.

### CUT 0 — `r_C-raven_0` — SHOWPIECE

Full-body showpiece, camera low at knee height looking up, three-quarter view from her left. She stands mid-stride in the middle of the venue, weight on one hip, chin lifted, looking past the camera with a proud, composed half-smile. The whole costume is visible and intact. Colour key: her signature colour as stage light against deep shadow. Foreground: a blurred prop of the venue. Wardrobe: the complete costume, intact. Setting: the venue.

### CUT 1 — `r_C-raven_1` — IN PLAIN SIGHT

Tension shot with a strong diagonal tilt, medium-full, camera high and to the side. No weapons. She walks in plain sight through the venue while a guard's blurred dark silhouette crosses the foreground. Her body faces away; her head is turned back over her shoulder in three-quarter profile, eyes sharp and alert, lips pressed, one hand lifting the hem or collar of the costume as she moves. Colour key: cold shadow cut by one hard warm light. Wardrobe: the same costume in motion, jacket or robe open and slipping from one shoulder, one glove missing. Still dressed. Setting: the venue.

### CUT 2 — `r_C-raven_2` — TEASE

Medium close-up from the waist up at eye level, shallow depth of field. Backstage after the job. She leans on a counter with her head tilted, looking straight into the lens with one eyebrow raised and a slow teasing smirk, biting the fingertip of a glove or pulling a strap down with one finger. Colour key: warm amber with her signature colour as a rim light. Foreground: blurred bulbs or bottles. Wardrobe: outer pieces off. Down to the costume's corset or bralette and its shorts or stockings, laces half undone, one strap off the shoulder, bare shoulders, midriff and thighs. Setting: backstage of the venue.

### CUT 3 — `r_C-raven_3` — PRIVATE

Intimate private moment, camera low and slightly behind her in three-quarter back view, soft focus edges. She is not looking at the camera: head turned in profile, eyes half closed, a quiet private smile, caught mid-movement as she undresses. Colour key: candle or lamp gold with deep shadow. Wardrobe: the costume lies discarded on a chair behind her. No clothing and no underwear visible on her torso. She is covered only by the red scarf itself, draped down her front, plus her own arms, hair and the turn of her body. She still wears her long red scarf. Natural and unposed. Setting for this cut: the private room.

## VIPER

- Sheet: `agents/sheet_viper.jpg`
- Costume: a violet-and-silver ice-queen figure-skating-inspired outfit.
- Venue: an indoor ice rink during a gala figure-skating show: violet and silver spotlights, frost haze, rink boards, glitter in the air.
- Private room (CUT 3): a locker room with frosted windows, skate bags, a bench and a rack of sequinned costumes.

### CUT 0 — `r_C-viper_0` — SHOWPIECE

Full-body showpiece, camera low at knee height looking up, three-quarter view from her left. She stands mid-stride in the middle of the venue, weight on one hip, chin lifted, looking past the camera with a proud, composed half-smile. The whole costume is visible and intact. Colour key: her signature colour as stage light against deep shadow. Foreground: a blurred prop of the venue. Wardrobe: the complete costume, intact. Setting: the venue.

### CUT 1 — `r_C-viper_1` — IN PLAIN SIGHT

Tension shot with a strong diagonal tilt, medium-full, camera high and to the side. No weapons. She walks in plain sight through the venue while a guard's blurred dark silhouette crosses the foreground. Her body faces away; her head is turned back over her shoulder in three-quarter profile, eyes sharp and alert, lips pressed, one hand lifting the hem or collar of the costume as she moves. Colour key: cold shadow cut by one hard warm light. Wardrobe: the same costume in motion, jacket or robe open and slipping from one shoulder, one glove missing. Still dressed. Setting: the venue.

### CUT 2 — `r_C-viper_2` — TEASE

Medium close-up from the waist up at eye level, shallow depth of field. Backstage after the job. She leans on a counter with her head tilted, looking straight into the lens with one eyebrow raised and a slow teasing smirk, biting the fingertip of a glove or pulling a strap down with one finger. Colour key: warm amber with her signature colour as a rim light. Foreground: blurred bulbs or bottles. Wardrobe: outer pieces off. Down to the costume's corset or bralette and its shorts or stockings, laces half undone, one strap off the shoulder, bare shoulders, midriff and thighs. Setting: backstage of the venue.

### CUT 3 — `r_C-viper_3` — PRIVATE

Intimate private moment, camera low and slightly behind her in three-quarter back view, soft focus edges. She is not looking at the camera: head turned in profile, eyes half closed, a quiet private smile, caught mid-movement as she undresses. Colour key: candle or lamp gold with deep shadow. Wardrobe: the costume lies discarded on a chair behind her. No clothing and no underwear visible on her torso. She is covered only by a white towel held to her chest with one hand, plus her own arms, hair and the turn of her body. She still wears her dog tags and violet neck scarf. Natural and unposed. Setting for this cut: the private room.

## GLITCH

- Sheet: `agents/sheet_glitch.jpg`
- Costume: a teal-neon cyber-idol stage outfit with a holographic visor pushed up on her head.
- Venue: backstage of a huge concert dome during an idol show: the back of a giant LED wall, teal lasers, flight cases, cables, magenta light leaking through.
- Private room (CUT 3): a small dressing room with a make-up mirror, fairy lights, energy-drink cans and a costume rail.

### CUT 0 — `r_C-glitch_0` — SHOWPIECE

Full-body showpiece, camera low at knee height looking up, three-quarter view from her left. She stands mid-stride in the middle of the venue, weight on one hip, chin lifted, looking past the camera with a proud, composed half-smile. The whole costume is visible and intact. Colour key: her signature colour as stage light against deep shadow. Foreground: a blurred prop of the venue. Wardrobe: the complete costume, intact. Setting: the venue.

### CUT 1 — `r_C-glitch_1` — IN PLAIN SIGHT

Tension shot with a strong diagonal tilt, medium-full, camera high and to the side. No weapons. She walks in plain sight through the venue while a guard's blurred dark silhouette crosses the foreground. Her body faces away; her head is turned back over her shoulder in three-quarter profile, eyes sharp and alert, lips pressed, one hand lifting the hem or collar of the costume as she moves. Colour key: cold shadow cut by one hard warm light. Wardrobe: the same costume in motion, jacket or robe open and slipping from one shoulder, one glove missing. Still dressed. Setting: the venue.

### CUT 2 — `r_C-glitch_2` — TEASE

Medium close-up from the waist up at eye level, shallow depth of field. Backstage after the job. She leans on a counter with her head tilted, looking straight into the lens with one eyebrow raised and a slow teasing smirk, biting the fingertip of a glove or pulling a strap down with one finger. Colour key: warm amber with her signature colour as a rim light. Foreground: blurred bulbs or bottles. Wardrobe: outer pieces off. Down to the costume's corset or bralette and its shorts or stockings, laces half undone, one strap off the shoulder, bare shoulders, midriff and thighs. Setting: backstage of the venue.

### CUT 3 — `r_C-glitch_3` — PRIVATE

Intimate private moment, camera low and slightly behind her in three-quarter back view, soft focus edges. She is not looking at the camera: head turned in profile, eyes half closed, a quiet private smile, caught mid-movement as she undresses. Colour key: candle or lamp gold with deep shadow. Wardrobe: the costume lies discarded on a chair behind her. No clothing and no underwear visible on her torso. She is covered only by an oversized tour hoodie held against her chest, not worn, plus her own arms, hair and the turn of her body. She still wears her round glasses and headphones. Natural and unposed. Setting for this cut: the private room.

## BRICK

- Sheet: `agents/sheet_brick.jpg`
- Costume: an orange-and-black champion-boxer-inspired outfit with an open satin robe.
- Venue: a luxury hotel ballroom set up for a title fight: a boxing ring under a hard white light, dinner tables, orange and black bunting, chandeliers.
- Private room (CUT 3): a fighters' locker room with a massage table, hanging robes, a title belt on a bench and steam from the showers.

### CUT 0 — `r_C-brick_0` — SHOWPIECE

Full-body showpiece, camera low at knee height looking up, three-quarter view from her left. She stands mid-stride in the middle of the venue, weight on one hip, chin lifted, looking past the camera with a proud, composed half-smile. The whole costume is visible and intact. Colour key: her signature colour as stage light against deep shadow. Foreground: a blurred prop of the venue. Wardrobe: the complete costume, intact. Setting: the venue.

### CUT 1 — `r_C-brick_1` — IN PLAIN SIGHT

Tension shot with a strong diagonal tilt, medium-full, camera high and to the side. No weapons. She walks in plain sight through the venue while a guard's blurred dark silhouette crosses the foreground. Her body faces away; her head is turned back over her shoulder in three-quarter profile, eyes sharp and alert, lips pressed, one hand lifting the hem or collar of the costume as she moves. Colour key: cold shadow cut by one hard warm light. Wardrobe: the same costume in motion, jacket or robe open and slipping from one shoulder, one glove missing. Still dressed. Setting: the venue.

### CUT 2 — `r_C-brick_2` — TEASE

Medium close-up from the waist up at eye level, shallow depth of field. Backstage after the job. She leans on a counter with her head tilted, looking straight into the lens with one eyebrow raised and a slow teasing smirk, biting the fingertip of a glove or pulling a strap down with one finger. Colour key: warm amber with her signature colour as a rim light. Foreground: blurred bulbs or bottles. Wardrobe: outer pieces off. Down to the costume's corset or bralette and its shorts or stockings, laces half undone, one strap off the shoulder, bare shoulders, midriff and thighs. Setting: backstage of the venue.

### CUT 3 — `r_C-brick_3` — PRIVATE

Intimate private moment, camera low and slightly behind her in three-quarter back view, soft focus edges. She is not looking at the camera: head turned in profile, eyes half closed, a quiet private smile, caught mid-movement as she undresses. Colour key: candle or lamp gold with deep shadow. Wardrobe: the costume lies discarded on a chair behind her. No clothing and no underwear visible on her torso. She is covered only by the open satin robe hanging from her elbows, her crossed forearms covering her chest, plus her own arms, hair and the turn of her body. She still wears her orange goggles and dog tags. Natural and unposed. Setting for this cut: the private room.

## MIRAGE

- Sheet: `agents/sheet_mirage.jpg`
- Costume: a gold-and-black casino-dealer-inspired outfit with a bow tie and waistcoat.
- Venue: a private penthouse casino at night: green baize tables, a roulette wheel, a gold-lit bar, black marble, city lights through tall windows.
- Private room (CUT 3): a VIP salon with a velvet chaise, a silk screen, scattered chips and a champagne bucket.

### CUT 0 — `r_C-mirage_0` — SHOWPIECE

Full-body showpiece, camera low at knee height looking up, three-quarter view from her left. She stands mid-stride in the middle of the venue, weight on one hip, chin lifted, looking past the camera with a proud, composed half-smile. The whole costume is visible and intact. Colour key: her signature colour as stage light against deep shadow. Foreground: a blurred prop of the venue. Wardrobe: the complete costume, intact. Setting: the venue.

### CUT 1 — `r_C-mirage_1` — IN PLAIN SIGHT

Tension shot with a strong diagonal tilt, medium-full, camera high and to the side. No weapons. She walks in plain sight through the venue while a guard's blurred dark silhouette crosses the foreground. Her body faces away; her head is turned back over her shoulder in three-quarter profile, eyes sharp and alert, lips pressed, one hand lifting the hem or collar of the costume as she moves. Colour key: cold shadow cut by one hard warm light. Wardrobe: the same costume in motion, jacket or robe open and slipping from one shoulder, one glove missing. Still dressed. Setting: the venue.

### CUT 2 — `r_C-mirage_2` — TEASE

Medium close-up from the waist up at eye level, shallow depth of field. Backstage after the job. She leans on a counter with her head tilted, looking straight into the lens with one eyebrow raised and a slow teasing smirk, biting the fingertip of a glove or pulling a strap down with one finger. Colour key: warm amber with her signature colour as a rim light. Foreground: blurred bulbs or bottles. Wardrobe: outer pieces off. Down to the costume's corset or bralette and its shorts or stockings, laces half undone, one strap off the shoulder, bare shoulders, midriff and thighs. Setting: backstage of the venue.

### CUT 3 — `r_C-mirage_3` — PRIVATE

Intimate private moment, camera low and slightly behind her in three-quarter back view, soft focus edges. She is not looking at the camera: head turned in profile, eyes half closed, a quiet private smile, caught mid-movement as she undresses. Colour key: candle or lamp gold with deep shadow. Wardrobe: the costume lies discarded on a chair behind her. No clothing and no underwear visible on her torso. She is covered only by a fan of playing cards in one hand and her long hair over the other shoulder, plus her own arms, hair and the turn of her body. She still wears her gold hoop earrings and a single black glove. Natural and unposed. Setting for this cut: the private room.

## DOC

- Sheet: `agents/sheet_doc.jpg`
- Costume: a glossy white-and-lime nurse-inspired corset outfit with a short cropped jacket, long gloves and a medic-cross choker.
- Venue: a private cosmetic clinic and spa at night: white marble, lime-green accent light, a turquoise spa pool, orchids, soft steam.
- Private room (CUT 3): a sauna-side relaxation room with warm wood, folded white towels, an orchid and drifting steam.

### CUT 0 — `r_C-doc_0` — SHOWPIECE

Full-body showpiece, camera low at knee height looking up, three-quarter view from her left. She stands mid-stride in the middle of the venue, weight on one hip, chin lifted, looking past the camera with a proud, composed half-smile. The whole costume is visible and intact. Colour key: her signature colour as stage light against deep shadow. Foreground: a blurred prop of the venue. Wardrobe: the complete costume, intact. Setting: the venue.

### CUT 1 — `r_C-doc_1` — IN PLAIN SIGHT

Tension shot with a strong diagonal tilt, medium-full, camera high and to the side. No weapons. She walks in plain sight through the venue while a guard's blurred dark silhouette crosses the foreground. Her body faces away; her head is turned back over her shoulder in three-quarter profile, eyes sharp and alert, lips pressed, one hand lifting the hem or collar of the costume as she moves. Colour key: cold shadow cut by one hard warm light. Wardrobe: the same costume in motion, jacket or robe open and slipping from one shoulder, one glove missing. Still dressed. Setting: the venue.

### CUT 2 — `r_C-doc_2` — TEASE

Medium close-up from the waist up at eye level, shallow depth of field. Backstage after the job. She leans on a counter with her head tilted, looking straight into the lens with one eyebrow raised and a slow teasing smirk, biting the fingertip of a glove or pulling a strap down with one finger. Colour key: warm amber with her signature colour as a rim light. Foreground: blurred bulbs or bottles. Wardrobe: outer pieces off. Down to the costume's corset or bralette and its shorts or stockings, laces half undone, one strap off the shoulder, bare shoulders, midriff and thighs. Setting: backstage of the venue.

### CUT 3 — `r_C-doc_3` — PRIVATE

Intimate private moment, camera low and slightly behind her in three-quarter back view, soft focus edges. She is not looking at the camera: head turned in profile, eyes half closed, a quiet private smile, caught mid-movement as she undresses. Colour key: candle or lamp gold with deep shadow. Wardrobe: the costume lies discarded on a chair behind her. No clothing and no underwear visible on her torso. She is covered only by a white towel slipping low on her hips, one arm folded across her chest, plus her own arms, hair and the turn of her body. She still wears her medic-cross choker and hoop earrings. Natural and unposed. Setting for this cut: the private room.

