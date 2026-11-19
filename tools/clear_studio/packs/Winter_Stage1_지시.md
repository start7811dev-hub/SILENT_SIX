# SILENT SIX — 블러디 크리스마스 리워드 컷 · STAGE 1 · 첫 번째 상자 — 크리스마스 마켓

## 사용법 (사람이 읽는 부분)

1. ChatGPT 새 대화에 이 zip 파일을 그대로 올린다.
2. 다음 한 줄을 보낸다: **"압축을 풀고 지시.md 를 끝까지 읽은 뒤, 첫 번째 이미지부터 진행해 줘."**
3. 한 번에 한 장씩 나온다. 다음 장은 "next".
4. 파일명 `r_W-1_0` ~ `r_W-1_3` 그대로 저장해 Claude에게 넘긴다.

네 장은 구도 · 얼굴 각도 · 표정 · 색이 서로 다르게 지정돼 있다. 한 장이 다른 장과 비슷하게 나오면 "CUT 번호의 camera 줄을 그대로 다시 지켜서 다시 그려 줘" 라고 돌려보낸다.

---

## FOR THE IMAGE MODEL — READ ALL OF THIS FIRST

You are producing four pieces of premium key art for one stage of a game. They will be shown side by side as a set, so they must look like **four different illustrations by the same artist**, not four takes of one pose.

### Files
- `refs/` — reference images of each character. For every character there are four: `_0` front portrait, `_3` close-up, `_4` dynamic action, `_6` combat. Use them for **identity** (face, hair, build, signature colours) and for **art style**.
- `look/` — four finished images from this game. They set the **quality bar**: level of detail, lighting, rendering finish. Match that finish. Do not copy their poses or compositions.

### Output
- 4 separate images, one per reply. Vertical portrait, 2:3, **1024x1536**. Write the file name on its own line before each image. Never make a grid or collage. After each image wait for "next". Do not ask questions.

### Identity
- Keep each woman exactly as in her references: same face, hair, eye colour, build, signature accent colour. Everyone is an adult woman in her late twenties.
- When a cut lists two or three characters, **all of them appear**, clearly distinct, none merged or dropped.

### Quality — every image must have all of this
- Semi-realistic anime illustration with a painterly, high-end finish like the `look/` images: detailed eyes and hair strands, real fabric and leather texture, stitched seams, metal that reflects its surroundings.
- **Three depth layers**: something in the foreground (out-of-focus snow, a railing, a lantern, a branch), the character(s) in the midground, a fully painted location in the background. No empty or flat backdrops, no plain gradients.
- **Two light sources of different colour** (for example cold blue moonlight against warm string lights) plus a rim light separating the character from the background. Visible atmosphere: falling snow at different depths, breath in the cold, drifting steam or smoke, bokeh.
- The location must be recognisable as the place described for this stage, with at least five specific props from it.
- Hands, weapons and gear drawn carefully and correctly. Faces fully visible and unobstructed unless a cut says otherwise.
- No text, no logo, no watermark, no UI.

### Variety — this is what failed last time, so follow it strictly
The four cuts are specified with a different **shot size, camera angle, head angle, gaze, expression, pose and colour key** each. Follow each cut's camera line literally. Across the four images:
- no two images share the same camera angle or shot size;
- no two images share the same facial expression or head direction;
- the character must not simply stand facing the camera in more than one image;
- the colour key changes from cut to cut as written.

### Limits
Sensual and glamorous is welcome, but everyone stays covered: no nudity, no exposed nipples or genitals, no sexual acts.

---

## THIS STAGE

**Characters**
- RAVEN — short messy black hair, sharp amber eyes, signature long red scarf, black tactical gear with red trim. References: `refs/raven_0.jpg`, `refs/raven_3.jpg`, `refs/raven_4.jpg`, `refs/raven_6.jpg`.

**Place.** 18:40, Christmas Eve. A snowy city-hall square Christmas market: rows of wooden stalls with red-and-white striped awnings and snow on the roofs, a giant decorated tree ringed by a low fence with a pile of wrapped gifts at its foot, a lit carousel, a frozen fountain, a small wooden stage with red curtains, an arched stone gate, iron street lamps, garlands and wreaths on the surrounding arcades.

**What happens.** She goes in alone and lifts Santa's delivery list from the gift pile under the tree. The square is full of civilians, so nobody dies tonight.

**Tone.** Christmas Eve night. Winter mission outfits with fur trim and each agent's accent colour, breath in the cold, snow everywhere.

## THE FOUR CUTS

### CUT 0 — `r_W-1_0` — MISSION CLEAR

Wide establishing shot, full body, low camera about knee height looking up from three-quarters behind her. She walks away through the stone gate arch, body turned away, head turned back over her left shoulder toward the glowing tree. Expression: a small tired half-smile of relief, eyes soft. One hand holds a ribbon-tied envelope against her chest, the red scarf trailing in the wind. Colour key: deep blue dusk with the warm gold of the market behind her; she is rim-lit in gold. Foreground: blurred iron lamp post and falling snow.

### CUT 1 — `r_W-1_1` — COMBAT

Dynamic action shot with a strong diagonal tilt, medium-full, camera high and to the side looking down into a dark service lane behind the stalls. She is mid-motion in a low lunge, locking a choke hold on a fake shopper in a Santa hat whose face is turned away. Her face is in three-quarter profile, jaw set, teeth clenched, eyes narrowed on the target, hair whipping. Red scarf flying across the frame, kicked-up snow, a dropped paper cup spilling. Colour key: cold teal shadow cut by one hard red light from a stall sign. Background: backs of stalls, crates, blurred string lights.

### CUT 2 — `r_W-1_2` — TEASE

Medium close-up from the waist up, camera slightly above eye level, shallow depth of field. She leans back on her elbows against a closed stall counter, head tilted to her right, looking straight into the lens with one eyebrow raised and a slow smirk, pulling the red scarf down off her mouth with two fingers. Winter jacket slipped off one shoulder over a fitted black top, a steaming cup of mulled wine by her hand, a stolen Santa hat hooked on a finger. Colour key: warm amber and candy red, carousel lights spinning into bokeh behind her. Foreground: a blurred garland with baubles.

### CUT 3 — `r_W-1_3` — PRIVATE NIGHT

Intimate interior, full figure, camera low at floor level in three-quarter view from her right side. A small attic room above the square, fairy lights around a frosted window, a tiny tree, a wool blanket. She sits sideways on the window sill, one knee drawn up, in red-and-black lace lingerie with a fur-trimmed robe falling open at the shoulders and the scarf loose round her neck. She does not look at the camera: her head is turned toward the window, eyes half closed, a quiet private smile, the unopened envelope on the sill beside her. Colour key: firelight amber inside against blue snowlight from the window.

