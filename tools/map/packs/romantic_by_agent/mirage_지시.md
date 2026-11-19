# SILENT SIX — 로맨틱 맵 · MIRAGE (TAKE 1 · 2 · 3)

## 사용법 (사람이 읽는 부분)

1. ChatGPT 새 대화에 이 zip 파일을 올리고 **"압축을 풀고 지시.md 를 읽은 뒤 TAKE 1 부터 한 장씩 진행해 줘."** 라고 보낸다.
2. 한 번에 한 장만 나온다. 다음 장은 "next".
3. 파일명 `bgp_mirage_1.jpg` · `_2` · `_3` 그대로 저장해 Claude에게 넘긴다. 그림을 분석해 동선 · 충돌 · 경비를 잡는다.

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

## TAKE 1 — `bgp_mirage_1.jpg`

**MIRAGE TAKE 1 · 초대장 — 야간 유람선**

- Output file name: `bgp_mirage_1.jpg`
- Type: Outdoor map. Follow `ref/look_outdoor.jpg` for construction.

**Place.** A river cruise ship at night seen from above with the upper deck removed. The hull fills the image lengthwise, dark water all around: a glittering ballroom forward, a block of small cabins on a narrow inner corridor aft, narrow side decks along both rails, a bow deck and a stern deck. String lights, reflections on black water.

**Entrance.** The stern boarding deck — at the lower corner of the plan.

**Objective.** A cabin writing desk with an invitation card — on the far side from the entrance. Make it the most eye-catching object on the map.

**What must be on the map**
- Walls / structures: the ship's interior bulkheads: ballroom walls and cabin walls (door gaps stay open).
- Tall solid objects: the anchor winch on the bow.
- Waist-high cover: banquet tables, deck chairs, luggage, bar carts.
- Impassable flat areas: the river (black water, light reflections, wake).

When this image is done, stop and wait for "next".

---

## TAKE 2 — `bgp_mirage_2.jpg`

**MIRAGE TAKE 2 · 역할 — 오페라 극장 무대 뒤**

- Output file name: `bgp_mirage_2.jpg`
- Type: Indoor map. Follow `ref/look_indoor.jpg` for construction.

**Place.** Backstage of a grand opera house during a performance, roof removed. The lit stage with painted scenery at the top, a heavy main curtain line, dark wings with scenery flats, a cluttered crossover corridor, then a row of four rooms: a stage-door room, a props store, a star dressing room, a wardrobe room. Warm bulb-ringed mirrors, deep shadow elsewhere.

**Entrance.** The stage door — at the lower corner of the plan.

**Objective.** The dressing-room vanity with an old photograph tucked in the mirror — on the far side from the entrance. Make it the most eye-catching object on the map.

**What must be on the map**
- Walls / structures: backstage walls between the corridor and the four rooms (door gaps stay open).
- Tall solid objects: the heavy red main curtain (two wing gaps stay open) and tall scenery flats in the wings.
- Waist-high cover: prop tables, costume racks, trunks, a piano, make-up tables.
- Special walkable floor: the stage floor under bright show lighting.

When this image is done, stop and wait for "next".

---

## TAKE 3 — `bgp_mirage_3.jpg`

**MIRAGE TAKE 3 · 맨얼굴 — 문 닫은 백화점**

- Output file name: `bgp_mirage_3.jpg`
- Type: Indoor map. Follow `ref/look_indoor.jpg` for construction.

**Place.** A department-store fashion floor after closing, roof removed. Dozens of mannequins on low display islands, glass counters, an escalator bank in the centre, show windows either side of the entrance, a small security room in the corner. Only night lighting and the glow of the show windows.

**Entrance.** The main entrance doors — at the lower corner of the plan.

**Objective.** A chair in the security room with cut ropes — on the far side from the entrance. Make it the most eye-catching object on the map.

**What must be on the map**
- Walls / structures: the security-room walls and the show-window backs by the entrance (door gap stays open).
- Tall solid objects: the escalator bank and square mirrored pillars.
- Waist-high cover: low display islands each carrying dressed mannequins, and glass counters (mannequins must be clearly visible).

When this image is done, stop and wait for "next".

---

