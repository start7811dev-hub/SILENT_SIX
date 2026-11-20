#!/bin/bash
# 일레븐랩스에서 받은 BGM을 게임용으로 정리해 public/bgm/ 에 넣는다.
#   앞뒤 무음 제거 → 음량 통일(-18 LUFS, 곡 전체를 같은 폭으로 조정) → MP3 128 kbps, 44.1 kHz
# 사용: tools/bgm/prep.sh <받은 파일이 있는 폴더>
#   폴더 안 파일 이름은 base_1 ~ base_5, rom_1 ~ rom_3, cos_1 ~ cos_3, xmas_1 ~ xmas_3 로 시작하면 된다(mp3 · wav · m4a).
#   ffmpeg 필요(맥: brew install ffmpeg). 없는 곡은 건너뛴다.
SRC="${1:?받은 파일이 있는 폴더를 지정한다}"
OUT="$(cd "$(dirname "$0")/../../public" && pwd)/bgm"
command -v ffmpeg >/dev/null || { echo "ffmpeg 가 없다: brew install ffmpeg"; exit 1; }
mkdir -p "$OUT"; N=0
TRIM="silenceremove=start_periods=1:start_threshold=-50dB"
CUT="$TRIM,areverse,$TRIM,areverse"
for id in base_1 base_2 base_3 base_4 base_5 rom_1 rom_2 rom_3 cos_1 cos_2 cos_3 xmas_1 xmas_2 xmas_3; do
  f=$(ls "$SRC"/"$id"*.mp3 "$SRC"/"$id"*.wav "$SRC"/"$id"*.m4a 2>/dev/null | head -1)
  [ -z "$f" ] && { echo "--   $id  (파일 없음)"; continue; }
  # 1) 무음을 자른 상태의 음량(I)과 최대치(Peak)를 잰다  2) 곡 전체를 같은 폭으로 올리거나 내려 -18 LUFS에 맞춘다(곡 안의 강약은 그대로)
  m=$(ffmpeg -nostdin -hide_banner -i "$f" -af "$CUT,ebur128=peak=true:framelog=quiet" -f null - 2>&1 | sed -n '/Summary/,$p')
  i=$(echo "$m" | awk '/ I:/{print $2; exit}'); pk=$(echo "$m" | awk '/Peak:/{print $2; exit}')
  g=$(awk -v i="$i" -v p="$pk" 'BEGIN{g=-18-i; if(p+g>-1.5)g=-1.5-p; printf "%.2f", g}')
  if [ -n "$i" ] && ffmpeg -nostdin -loglevel error -y -i "$f" -af "$CUT,volume=${g}dB" -ar 44100 -ac 2 -b:a 128k "$OUT/$id.mp3"; then
    d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT/$id.mp3" | cut -d. -f1)
    echo "OK   $id  $((d/60)):$(printf %02d $((d%60)))  ${i} LUFS → ${g} dB  $(du -h "$OUT/$id.mp3" | cut -f1)"; N=$((N+1))
  else echo "FAIL $id  $f"; fi
done
echo "$N / 14 곡 → $OUT ($(du -sh "$OUT" | cut -f1))"
