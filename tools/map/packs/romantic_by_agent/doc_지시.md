# SILENT SIX — 로맨틱 맵 · DOC (TAKE 1 · 2 · 3)

## 사용법 (사람이 읽는 부분)

1. ChatGPT 새 대화에 이 zip 파일을 올리고 **"압축을 풀고 지시.md 를 읽은 뒤 TAKE 1 부터 한 장씩 진행해 줘."** 라고 보낸다.
2. 한 번에 한 장만 나온다. 다음 장은 "next".
3. 파일명 `bgp_doc_1.jpg` · `_2` · `_3` 그대로 저장해 Claude에게 넘긴다. 그림을 분석해 동선 · 충돌 · 경비를 잡는다.

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

## TAKE 1 — `bgp_doc_1.jpg`

**DOC TAKE 1 · 차트 — 폐병원 지하 기록실**

- Output file name: `bgp_doc_1.jpg`
- Type: Indoor map. Follow `ref/look_indoor.jpg` for construction.

**Place.** The flooded basement of an abandoned hospital, roof removed. A central corridor ankle-deep in dark water, off it a chart archive with rusted shelves, a morgue with steel slabs, a boiler room, a laundry and a dry store. Peeling paint, one working lamp, reflections on the water.

**Entrance.** The stairwell down — at the lower corner of the plan.

**Objective.** The filing cabinet with the altered chart — on the far side from the entrance. Make it the most eye-catching object on the map.

**What must be on the map**
- Walls / structures: basement walls with peeling tiles (door gaps stay open).
- Tall solid objects: tall rusted chart shelves, the boiler, industrial washing machines.
- Waist-high cover: morgue slabs, gurneys, wheelchairs, boxes of files.
- Wet or frozen walkable floor: standing flood water, ankle-deep, reflecting light (walkable).

When this image is done, stop and wait for "next".

---

## TAKE 2 — `bgp_doc_2.jpg`

**DOC TAKE 2 · 이송 — 병원 옥상 헬기장**

- Output file name: `bgp_doc_2.jpg`
- Type: Outdoor map. Follow `ref/look_outdoor.jpg` for construction.

**Place.** A hospital rooftop helipad at night in strong wind. A large painted H pad with edge lights, HVAC plant and ducting around it, a stairwell house, a ramp down toward the ambulance bay, a small flight-ops booth at the far edge. City glow beyond the parapet, a sweeping searchlight.

**Entrance.** Inside the stairwell house — at the lower corner of the plan.

**Objective.** The flight log on the ops-booth counter — on the far side from the entrance. Make it the most eye-catching object on the map.

**What must be on the map**
- Walls / structures: the stairwell house (door gap stays open).
- Tall solid objects: HVAC units, cooling towers, big ducts and the flight-ops booth walls.
- Waist-high cover: medical supply cases, a stretcher trolley, fuel drums, low pipes.
- Impassable flat areas: the roof edge and the drop to the city below.
- Special walkable floor: the painted helipad surface and the striped vehicle ramp.

When this image is done, stop and wait for "next".

---

## TAKE 3 — `bgp_doc_3.jpg`

**DOC TAKE 3 · 퇴원 — 산속 요양원**

- Output file name: `bgp_doc_3.jpg`
- Type: Outdoor map. Follow `ref/look_outdoor.jpg` for construction.

**Place.** A secluded mountain sanatorium at dawn in thick fog. A long ward building at the top, a glass greenhouse, and in front of them a formal garden of tall clipped hedges forming a small maze with gravel paths and benches. Pale grey light, mist pooling between the hedges.

**Entrance.** The garden gate — at the lower corner of the plan.

**Objective.** The patient's bed by the window — on the far side from the entrance. Make it the most eye-catching object on the map.

**What must be on the map**
- Walls / structures: the ward building walls and the glass-and-iron greenhouse (door gaps stay open).
- Tall solid objects: tall clipped hedges (the maze and the boundary).
- Waist-high cover: beds, garden benches, potted plants, a wheelbarrow.

When this image is done, stop and wait for "next".

---

