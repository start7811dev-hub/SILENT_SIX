# SILENT SIX — 로맨틱 맵 · BRICK (TAKE 1 · 2 · 3)

## 사용법 (사람이 읽는 부분)

1. ChatGPT 새 대화에 이 zip 파일을 올리고 **"압축을 풀고 지시.md 를 읽은 뒤 TAKE 1 부터 한 장씩 진행해 줘."** 라고 보낸다.
2. 한 번에 한 장만 나온다. 다음 장은 "next".
3. 파일명 `bgp_brick_1.jpg` · `_2` · `_3` 그대로 저장해 Claude에게 넘긴다. 그림을 분석해 동선 · 충돌 · 경비를 잡는다.

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

## TAKE 1 — `bgp_brick_1.jpg`

**BRICK TAKE 1 · 닫힌 문 — 폐쇄된 지하 벙커**

- Output file name: `bgp_brick_1.jpg`
- Type: Indoor map. Follow `ref/look_indoor.jpg` for construction.

**Place.** The interior of a sealed underground military bunker, roof removed. Eight concrete rooms joined by heavy blast doors, cracked wall sections, rusted bunks and lockers, a ventilation fan room. Bare bulbs, damp concrete, stencilled hazard stripes.

**Entrance.** The entry hatch ladder — at the lower corner of the plan.

**Objective.** A locker with four dog tags hanging on it — on the far side from the entrance. Make it the most eye-catching object on the map.

**What must be on the map**
- Walls / structures: thick reinforced-concrete walls (door gaps stay open, with open blast doors).
- Tall solid objects: a big ventilation fan housing and a generator.
- Breakable wall sections (must look cracked and marked with yellow hazard tape): cracked, crumbling wall sections marked with yellow hazard tape (must look breakable).
- Waist-high cover: bunks, lockers, ammunition crates, fallen debris.

When this image is done, stop and wait for "next".

---

## TAKE 2 — `bgp_brick_2.jpg`

**BRICK TAKE 2 · 인식표 — 지하 격투장**

- Output file name: `bgp_brick_2.jpg`
- Type: Indoor map. Follow `ref/look_indoor.jpg` for construction.

**Place.** An illegal underground fight club in a converted warehouse, roof removed. A raised boxing ring under a hard cone of light in the centre, rough bleacher benches on all four sides, a locker room, a bookmaker's office, a holding cell. Smoke haze, everything outside the ring light is dark.

**Entrance.** The side service entrance — at the lower corner of the plan.

**Objective.** The barred holding-cell cot — on the far side from the entrance. Make it the most eye-catching object on the map.

**What must be on the map**
- Walls / structures: brick partition walls of the locker room, office and holding cell (door gaps stay open).
- Tall solid objects: the raised boxing ring with ropes and corner posts.
- Waist-high cover: bleacher benches, a bar counter, beer crates, betting tables.

When this image is done, stop and wait for "next".

---

## TAKE 3 — `bgp_brick_3.jpg`

**BRICK TAKE 3 · 노크 — 채석장 발파 구역**

- Output file name: `bgp_brick_3.jpg`
- Type: Outdoor map. Follow `ref/look_outdoor.jpg` for construction.

**Place.** An open-pit stone quarry at night. Three stepped terraces cut into grey rock, each a level floor separated by low cliff steps with ramps, excavators and a dump truck, an explosives magazine, a site office, a marked blasting zone. Sodium work lights, stone dust.

**Entrance.** The haul road in — at the lower corner of the plan.

**Objective.** The steel door of the inner store — on the far side from the entrance. Make it the most eye-catching object on the map.

**What must be on the map**
- Walls / structures: the explosives magazine and the site office (door gaps stay open).
- Tall solid objects: rock faces: the quarry rim, the cliff steps between terraces, and parked heavy machines (excavator, dump truck, drill rig).
- Waist-high cover: cut stone blocks, rock piles, cable reels, barrels.
- Special walkable floor: the blasting zone (ground marked with red flags and drilled holes).

When this image is done, stop and wait for "next".

---

