# SILENT SIX — 로맨틱 맵 · VIPER (TAKE 1 · 2 · 3)

## 사용법 (사람이 읽는 부분)

1. ChatGPT 새 대화에 이 zip 파일을 올리고 **"압축을 풀고 지시.md 를 읽은 뒤 TAKE 1 부터 한 장씩 진행해 줘."** 라고 보낸다.
2. 한 번에 한 장만 나온다. 다음 장은 "next".
3. 파일명 `bgp_viper_1.jpg` · `_2` · `_3` 그대로 저장해 Claude에게 넘긴다. 그림을 분석해 동선 · 충돌 · 경비를 잡는다.

검수: 윤곽이 마름모 하나인지, 대각선 벽이 없는지, 입구와 목표가 반대편에 있는지, 방마다 문이 열려 있는지.

---

## INSTRUCTIONS FOR THE IMAGE MODEL

You are painting game-map backgrounds for a real-time stealth tactics game. `ref/look_indoor.jpg` and `ref/look_outdoor.jpg` are finished maps from the same game. Every new map must look like it belongs in the same set: **same canvas, same camera, same scale, same wall construction, same level of detail**. Only the place changes.

This file contains **three maps**. Make them **one at a time: one image per reply**. Write the output file name on its own line before the image. Do not ask questions. After each image, stop and wait for "next". Read only the section of the map you are painting; do not mix details between maps.

### Hard rules for every map
1. Exactly **1536x1024**, landscape. **One plain diamond-shaped plan** filling the frame like the references, 2:1 isometric, same camera angle. No wings or rooms sticking out of the diamond, no notches (one small recessed entrance is fine). Background outside the diamond: flat near-black `#06080b`. No horizon, no sky.
2. **Same scale as the references**: the plan is about 20 x 20 metres. A single bed is about 80 px long, a person would be about 45 px tall. Doorways, corridors and paths at least 2 metres wide and clearly open.
3. **Everything solid runs along the two isometric axes.** No diagonal walls, no chamfered corners, no curves, no octagons.
   - Indoor maps: roof removed, all walls cut at one height (about 46 px), thin, with a flat dark top slab, like `look_indoor.jpg`.
   - Outdoor maps: use fences, building blocks, containers, rock faces, hedges or water edges the same way: straight, axis-aligned, clearly solid, like `look_outdoor.jpg`. Buildings you cannot enter keep their roofs.
4. Lay the plan out on a 4-metre rhythm so walls and paths line up. Six to nine rooms or zones, **at least two different routes** from the entrance to the objective.
5. **Readable floor**: walkable ground is calm and slightly brighter than the objects on it. Cover (waist-high objects) sits clearly on the floor with free floor around it, never blocking a doorway. Water, drops and pits must clearly read as "cannot walk here".
6. One clearly marked **entrance** at the lower corner or lower edge (a doorway or gate with a floor hazard stripe) and the **objective** on the far side from it.
7. **Every doorway that is meant to be used must be visibly open.** Do not paint closed rooms that have no door.
8. No characters, no people, no animals, no text, no numbers, no UI, no grid lines, no watermark.
9. Rendering: detailed hand-painted semi-realistic isometric game art, crisp edges, soft baked lighting, a few practical light sources, gentle ambient occlusion. Night unless the map says otherwise.

---

## TAKE 1 — `bgp_viper_1.jpg`

**VIPER TAKE 1 · 빗나간 한 발 — 스키 리조트 야간 슬로프**

- Output file name: `bgp_viper_1.jpg`
- Type: Outdoor map. Follow `ref/look_outdoor.jpg` for construction.

**Place.** A ski resort at night. A floodlit piste running up the middle to a lodge with lit windows, a chairlift line with pylons, a lift station, a snow-groomer garage, dark pine forest on both sides. Bright white slope against deep blue shadow.

**Entrance.** The bottom of the slope — at the lower corner of the plan.

**Objective.** A spotting position below the lodge windows (tripod and scope case) — on the far side from the entrance. Make it the most eye-catching object on the map.

**What must be on the map**
- Walls / structures: the lodge front, the lift station and the groomer garage (door gaps stay open).
- Tall solid objects: dark pine trees and chairlift pylons.
- Waist-high cover: snow mounds, padded fences, stacked skis, a snowmobile.
- Special walkable floor: the floodlit groomed slope (bright corduroy snow).

When this image is done, stop and wait for "next".

---

## TAKE 2 — `bgp_viper_2.jpg`

**VIPER TAKE 2 · 거리 — 온천 료칸의 복도**

- Output file name: `bgp_viper_2.jpg`
- Type: Indoor map. Follow `ref/look_indoor.jpg` for construction.

**Place.** The interior of a traditional hot-spring inn at night, roof removed. Long wooden corridors lined with sliding paper doors, tatami guest rooms on both sides, a small inner courtyard pond with snow, a steaming bath room. Warm lantern light, drifting steam.

**Entrance.** The genkan entrance — at the lower corner of the plan.

**Objective.** A low desk with the spotter's notebook — on the far side from the entrance. Make it the most eye-catching object on the map.

**What must be on the map**
- Walls / structures: timber-and-paper walls with sliding doors (door gaps stay open).
- Tall solid objects: stone lanterns and a garden pine at the pond.
- Waist-high cover: low tables, folding screens, luggage, futon stacks.
- Impassable flat areas: the courtyard pond (snow-edged water).
- Wet or frozen walkable floor: the wet stone floor of the bath room, thick steam.

When this image is done, stop and wait for "next".

---

## TAKE 3 — `bgp_viper_3.jpg`

**VIPER TAKE 3 · 숨 — 산정 관측소**

- Output file name: `bgp_viper_3.jpg`
- Type: Outdoor map. Follow `ref/look_outdoor.jpg` for construction.

**Place.** A mountaintop weather station in a blizzard at night. A cable-car terminal on the lower shoulder, a narrow wind-carved ridge crossing to the summit, a small observatory building with antenna masts. Rime ice, snow cornices, sheer drops on all sides.

**Entrance.** Inside the cable-car terminal — at the lower corner of the plan.

**Objective.** The observation desk by the window — on the far side from the entrance. Make it the most eye-catching object on the map.

**What must be on the map**
- Walls / structures: the cable-car terminal and the observatory (door gaps stay open).
- Tall solid objects: rock spires, antenna masts and ice-crusted boulders.
- Waist-high cover: snow cornices, drifted fuel drums, equipment cases.
- Impassable flat areas: sheer drop into cloud and darkness (cliff edge).

When this image is done, stop and wait for "next".

---

