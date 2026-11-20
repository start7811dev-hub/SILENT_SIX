# SILENT SIX — BGM 제작 지침 (일레븐랩스 뮤직)

상태: **v0.33.0에 재생 엔진과 음원 14곡을 넣었다.** 원본(192 kbps)은 `Desktop/GAMES/SilentSix/OST`에 있고, 게임에는 무음을 자르고 음량을 맞춘 128 kbps 파일(합계 34 MB)이 들어 있다. 코스튬 3곡은 코스튬 미션 엔진이 들어오면 나온다. 가사가 있는 테마송 2곡(같은 폴더)은 아직 게임에 넣지 않았다.

## 1. 구성

| 풀 | 쓰는 곳 | 곡 수 | 곡당 길이 | 합계 | 파일 |
|---|---|---|---|---|---|
| 공용 | 홈 · 메뉴 · 스토리 미션 | 5 | 2:30 (150초) | 12:30 | `base_1` ~ `base_5` |
| 로맨틱 | 로맨틱 미션(브리핑부터 결과까지) | 3 | 2:40 (160초) | 8:00 | `rom_1` ~ `rom_3` |
| 코스튬 | 코스튬 미션 | 3 | 3:00 (180초) | 9:00 | `cos_1` ~ `cos_3` |
| 블러디 크리스마스 | 시즈널 겨울 5판 | 3 | 2:40 (160초) | 8:00 | `xmas_1` ~ `xmas_3` |

합계 14곡, 37분 30초. MP3 128 kbps 기준 36 MB 안팎이다.

길이 근거:
- 한 판의 플레이 시간은 스토리 3~9분, 블러디 크리스마스 6~9분, 코스튬 8~12분이다. 풀 합계를 한 판 길이에 맞춰 한 판 안에서 같은 곡이 두 번 나오는 일을 줄였다.
- 곡당 2분 30초~3분이면 곡이 바뀌는 간격이 지루하지 않고, 일레븐랩스 한 번 생성 한도(5분) 안에서 구성이 흐트러지지 않는다.
- 게임이 곡 끝 2.5초를 다음 곡과 겹쳐 넘긴다. 그래서 **루프 이음매를 맞출 필요가 없다.** 대신 첫머리 무음과 긴 페이드아웃은 피한다.

## 2. 일레븐랩스 설정

| 항목 | 값 |
|---|---|
| 모델 | Music v2 이상 |
| Duration | 표의 초 값을 직접 입력(자동 길이 쓰지 않음) |
| Instrumental | 토글이 보이면 켠다. 프롬프트에도 `Instrumental only`가 들어 있다 |
| Variants | 곡당 2~4개 뽑아 1개 고른다 |
| Audio Reference | `base_1`을 확정한 뒤, 그 곡의 30초를 나머지 공용 4곡의 레퍼런스로 넣으면 음색이 한 벌로 묶인다 |

고르는 기준:
1. 목소리 · 허밍 · 내레이션이 없다.
2. 첫 1초 안에 소리가 시작된다.
3. 중간에 크게 터지거나 뚝 끊기는 구간이 없다(잠입 중에 음악이 플레이어보다 먼저 흥분하면 안 된다).
4. 작은 음량으로 틀어 놓고 3분 들었을 때 거슬리는 소리(날카로운 고음, 반복되는 효과음)가 없다.

## 3. 프롬프트

모든 프롬프트 끝에 아래 **공통 꼬리**를 붙인다(각 프롬프트에 이미 붙여 두었다).

> Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.

### 3-1. 공용 5곡 — Duration 150초

톤: 네오 누아르 첩보물. 차갑고 세련되고, 여섯 요원의 관능이 깔린 밤. 홈에서도 잠입 중에도 어울리게 중간 이하 강도로 맞췄다. 다섯 곡의 역할을 나눠 랜덤으로 돌아도 분위기가 한쪽으로 쏠리지 않는다.

**`base_1` NO RECORD — 메인 테마**
```
Main theme for a sleek, mature tactical stealth game about six female covert agents. Neo-noir spy downtempo electronica, 92 BPM, D minor. Start with a deep sub-bass pulse and a tight trip-hop drum groove with brushed snare and crisp closed hi-hats, then bring in a muted tremolo electric guitar motif of four notes, cool and memorable, answered by vibraphone. Add a low dark string pad underneath and short brass swells kept far in the background. Mood: confident, seductive, dangerous, midnight city. Clean modern cinematic mix, wide stereo, warm low end. Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.
```

**`base_2` NIGHT WATCH — 숨죽인 잠입**
```
Minimal infiltration underscore for a stealth game, 84 BPM, A minor. A ticking closed hi-hat like a stopwatch, a soft pulsing analog synth bass ostinato, and sparse felt-piano notes with long reverb. Add distant sonar-like pings, a cold airy pad and a subtle heartbeat kick, then bring in a quiet muted string ostinato for a little forward motion. Mood: patient, watchful, holding your breath in the dark. Very restrained dynamics with a lot of space. Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.
```

**`base_3` SIX SHADOWS — 누아르 라운지**
```
Smoky noir lounge trip-hop, 78 BPM, F minor. Dusty slow breakbeat, round upright bass line, warm Rhodes electric piano chords, and a muted trumpet playing short, lazy, sultry phrases with plate reverb. Add soft vibraphone and gentle tape saturation, then a silky string pad in the second half. Mood: femme fatale after hours, sensual, unhurried, a little dangerous. Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.
```

**`base_4` GHOST SIGNAL — 차가운 테크**
```
Cold tech-espionage electronica, 100 BPM, E minor. Glitchy syncopated percussion, a plucked arpeggiated analog synth line, filtered bass pulses, and radio-static and data-blip textures used rhythmically. Bring in a dark pad and a simple two-note synth hook after eight bars, then add a tight sidechained sub bass in the second half. Mood: precise, focused, a surveillance room at 3 a.m. Crisp, clean, modern sound design. Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.
```

**`base_5` EXFIL — 조여 오는 시간**
```
Restrained cinematic tension cue for a stealth game, 108 BPM, C minor. Low staccato cello and viola ostinato, pulsing synth bass, soft taiko-like low drum hits and ticking percussion. Add high string harmonics and a slowly rising low brass pad, then a hybrid electronic drum groove that keeps driving but never explodes into action. Mood: controlled urgency, the clock is running, get out unseen. Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.
```

### 3-2. 로맨틱 미션 3곡 — Duration 160초

톤: 허가 없이 혼자 나간 밤. 은밀하고 가깝고 씁쓸하다. 잠입 미션이라 긴장의 실은 끝까지 남긴다.

**`rom_1` AFTER HOURS — 늦은 밤의 온도**
```
Late-night sensual noir R&B instrumental, 72 BPM, E-flat minor. Warm Rhodes chords, a slow fingered electric bass, brushed drums with a soft rimshot, and a breathy tenor saxophone playing slow intimate phrases far back in the mix. Add a lush analog pad and gentle tremolo electric guitar licks. Mood: a secret night out that nobody ordered, tender but tense, bittersweet. Keep a quiet pulse of suspense underneath so it still works for sneaking past guards. Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.
```

**`rom_2` OFF THE RECORD — 기록에 없는 일**
```
Intimate cinematic downtempo, 80 BPM, B minor. A solo felt piano motif and a warm cello melody over a subtle trip-hop beat and deep sub bass. Add soft pizzicato strings and a distant reverb guitar, then a slow-swelling string section in the second half that stays restrained. Mood: longing, a private mission, old wounds, quiet resolve. Emotional but never sentimental, with a thread of tension throughout. Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.
```

**`rom_3` THAT NIGHT — 그날 밤으로**
```
Sultry slow-burn electronic soul instrumental, 88 BPM, G minor. Deep 808 sub bass, finger snaps and a laid-back half-time beat, nylon-string guitar plucks, and a smooth analog synth lead that bends slowly like a voice. Add silky Rhodes, a soft shaker and warm tape-saturated pads. Mood: charged, alluring, skin-close, the night she lets her guard down, yet still careful and quiet, music for moving unseen. Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.
```

### 3-3. 코스튬 미션 3곡 — Duration 180초

톤: 무기 없이 의상 하나로 들어가는 화려한 현장(갈라, 아이스쇼, 콘서트, 특설 링, 카지노, 스파). 능청스러운 케이퍼물. 대화로 정보를 캐는 구간이 있어 말소리를 덮지 않는 편성으로 잡았다.

**`cos_1` DRESS CODE — 능청스러운 침투**
```
Sly heist-caper funk, 104 BPM, G minor. A slinky syncopated electric bass riff, tight dry funk drums, wah-wah rhythm guitar, bongos and muted brass stabs. Bring in a Hammond organ and a playful flute hook after eight bars, then add handclaps and a baritone sax doubling the bass in the second half. Mood: undercover in costume with no weapons, bluffing through a glamorous venue, cheeky, confident, on tiptoe. Light on its feet, medium-low intensity. Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.
```

**`cos_2` SHOWTIME — 무대 뒤의 화려함**
```
Glamorous backstage electro-swing meets nu-disco, 116 BPM, A minor. Soft four-on-the-floor kick, swung hi-hats, bouncing upright bass, pizzicato strings, and short clarinet and muted trumpet riffs. Add sparkling piano runs and a filtered disco string line. Mood: a gala night of spotlights and sequins, smiling while hiding in plain sight, playful and stylish with a wink of danger. Keep the groove elegant and moderate, not a club banger. Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.
```

**`cos_3` HOUSE EDGE — 판돈과 눈치 싸움**
```
Cool casino lounge spy jazz with a bossa nova groove, 96 BPM, D minor. Vibraphone melody, walking upright bass, brushed drums, bongos and shaker, with a sneaky pizzicato string line. Add a muted trumpet answering the vibraphone and soft Rhodes, with a quiet suspense pad in the sparser passages. Mood: high-stakes small talk, reading a bluff, charming and tense, velvet and smoke. Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.
```

### 3-4. 블러디 크리스마스 3곡 — Duration 160초

톤: 캐럴의 악기(첼레스타, 썰매 방울, 종)를 쓰되 단조로 뒤집는다. 위는 반짝이고 아래는 위험하다. 기존 캐럴 선율은 쓰지 않는다.

**`xmas_1` BLOODY CHRISTMAS — 뒤틀린 캐럴(메인)**
```
Dark Christmas stealth theme, 90 BPM in 6/8 time, D minor. An original carol-like melody, not quoting any existing carol, played on celesta and music box, with sleigh bells, pizzicato strings and a soft tubular bell. After eight bars bring in a deep sub bass and a slow trip-hop beat, then add a cold choir-like synth pad and low strings. Mood: Christmas Eve gone wrong, festive lights over a covert chase, mischievous, ominous, elegant. Twinkling on top, dangerous underneath. Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.
```

**`xmas_2` RED COAT — 산타의 테마**
```
Noir jazz Christmas cue for a mysterious woman in a red hooded coat, 84 BPM, A minor. Muted trumpet and vibraphone trade an original carol-flavored phrase over upright bass and brushed drums, with gentle sleigh bells on the off-beats and celesta twinkles. Add a smoky Rhodes, a cold wind-like pad and a low bass clarinet shadowing the melody. Mood: teasing, seductive, always one step ahead, snow falling on an empty street, a taunt disguised as a lullaby. Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.
```

**`xmas_3` LAST DELIVERY — 마지막 상자**
```
Tense Christmas-night pursuit underscore, 108 BPM, C minor. An original fast repeating four-note bell ostinato on glockenspiel and staccato strings, church bells tolling in the distance, sleigh bells driving steady eighth notes, and a pulsing synth bass. Bring in low brass swells, hybrid cinematic percussion and a cold choir-like synth pad, building pressure in waves but never breaking into full action. Mood: from midnight mass to a snowy airfield, the last box, the clock running out. Instrumental only, no vocals, no spoken words. The music starts immediately with no silent intro. Steady, even energy from start to finish for use as background music in a stealth video game: no big drops, no dramatic climax, no sudden stops. End on a sustained chord.
```

## 4. 받은 뒤 넣는 법

1. 받은 파일 이름을 표의 이름으로 바꾼다(`base_1.mp3` …). 한 폴더에 모은다.
2. `tools/bgm/prep.sh <그 폴더>` 를 돌린다. 앞뒤 무음을 자르고, 곡 전체를 같은 폭으로 올리거나 내려 14곡의 음량을 같은 기준(-18 LUFS)으로 맞춘 뒤 `public/bgm/`에 넣는다. ffmpeg가 필요하다(`brew install ffmpeg`).
3. 커밋해서 올리면 배포된다. 일부만 있어도 된다. 없는 곡은 건너뛰고, 전용 풀이 통째로 없으면 공용 풀이 대신 나온다.

곡 제목(설정 화면 BGM 줄에 나온다)과 풀 구성은 `public/index.html`의 `BGM` 표에서 바꾼다. 곡을 늘리려면 그 표에 줄을 추가하고 같은 이름의 파일을 넣는다.

### 지금 들어 있는 곡 (2026-11-21)

| 게임 파일 | 원본 파일 | 길이 | 원본 음량 → 조정 |
|---|---|---|---|
| `base_1` | `Main_NO_RECORD` | 2:28 | -13.7 LUFS → -4.3 dB |
| `base_2` | `Main_NIGHT_WATCH` | 2:25 | -17.9 → -1.0 |
| `base_3` | `Main_SIX_SHADOWS` | 2:28 | -15.3 → -2.7 |
| `base_4` | `Main_GHOST_SIGNAL` | 2:28 | -14.9 → -3.1 |
| `base_5` | `Main_EXFIL` | 2:26 | -15.1 → -2.9 |
| `rom_1` | `Romantic_AFTER_HOURS` | 2:40 | -14.0 → -4.0 |
| `rom_2` | `Romantic_OFF_THE_RECORD` | 2:38 | -13.0 → -5.0 |
| `rom_3` | `Romantic_THAT_NIGHT` | 2:38 | -14.2 → -3.8 |
| `cos_1` | `Costume_DRESS_CODE` | 2:59 | -14.9 → -3.1 |
| `cos_2` | `Costume_SHOWTIME` | 2:56 | -14.0 → -4.0 |
| `cos_3` | `Costume_HOUSE_EDGE` | 2:59 | -16.2 → -1.8 |
| `xmas_1` | `Seasonal_WINTERBOOLDY_CHRISTMAS` | 2:38 | -12.3 → -5.7 |
| `xmas_2` | `Seasonal_WINTER_RED_COAT` | 2:36 | -14.7 → -3.3 |
| `xmas_3` | `Seasonal_WINTER_LAST_DELIVERY` | 2:36 | -13.4 → -4.6 |

원본끼리는 음량이 최대 5.6 LU 벌어져 있었다. 조정 뒤에는 14곡 중 13곡이 0.1 LU 안에 들어오고, `base_2`만 최대치 보호 때문에 1 LU쯤 작다.

## 5. 게임 동작

| 항목 | 동작 |
|---|---|
| 재생 순서 | 풀 안에서 랜덤. 풀을 한 바퀴 다 돌기 전에는 같은 곡이 다시 나오지 않는다 |
| 곡 넘김 | 곡 끝 2.5초를 다음 곡과 겹친다 |
| 풀 전환 | 로맨틱 · 코스튬 · 블러디 크리스마스는 브리핑에 들어갈 때 전용 풀로, 메뉴로 나오면 공용 풀로 겹쳐 넘어간다 |
| 코스튬 풀 | 미션 데이터에 `costume:true`가 붙은 판에서 나온다. 코스튬 엔진을 넣을 때 붙인다 |
| 시작 | 브라우저 규칙상 첫 터치 뒤에 소리가 난다 |
| 화면을 벗어나면 | 멈췄다가 돌아오면 이어서 나온다 |
| 홈 HUD | `BGM ON/OFF` 토글, 난이도 칩(누르면 4단계 목록) |
| 설정 > 사운드 | BGM 켜기 · BGM 음량 · 미션 전용 BGM 켜기 · 다음 곡 · 효과음 음량 |

설정값은 기기에 저장된다(`s6prog`의 `bgm`, `bvol`, `bth`).

## 6. 출시 전 확인

일레븐랩스 음악의 상업 이용 범위는 요금제에 따라 다르다. 스토어 출시 전에 쓰는 요금제의 음악 이용 약관(https://elevenlabs.io/music-terms)을 확인한다.
