#!/bin/bash
# 스토리 6판, 로맨틱 18판, 블러디 크리스마스 5판이 클리어 가능한지 자동으로 확인한다.
# 전체로 돌리면 끝에 로맨틱 전용 맵 판의 시작 지점 안전 · 순찰 경로 점검(check_rom.js)도 한다.
# 사용: tools/verify.sh        (전체)
#       tools/verify.sh 0 5    (미션 번호만. 0~5 스토리, 6~23 로맨틱, 24~28 블러디 크리스마스)
cd "$(dirname "$0")/../public" || exit 1
PADS=(0.2 0 0.5 0.5 0.5 0); FAIL=0; ALL=0
LIST=("$@"); [ ${#LIST[@]} -eq 0 ] && { LIST=($(seq 0 28)); ALL=1; }
for i in "${LIST[@]}"; do
  if [ "$i" -ge 24 ] && [ "$i" -le 28 ]; then if STAGE=$((i-23)) node ../tools/check_w1.js >/dev/null 2>&1; then echo "OK   mission $i (check_w1)"; else echo "FAIL mission $i (check_w1)"; FAIL=1; fi; continue; fi
  pad=${PADS[$i]:-0}; [ "$i" -ge 24 ] && pad=${PADS[$((i-24))]}; out=$(node ../tools/solve.js "$i" "$pad" 2>&1 | grep -E "REAL RUN|NO GHOST|IDLE")
  if echo "$out" | grep -q '"win":true'; then echo "OK   mission $i"; else
    out=$(node ../tools/solve.js "$i" 0.3 2>&1 | grep -E "REAL RUN|NO GHOST|IDLE")
    if echo "$out" | grep -q '"win":true'; then echo "OK   mission $i"; else echo "FAIL mission $i  $out"; FAIL=1; fi
  fi
done
if [ $ALL -eq 1 ]; then if node ../tools/check_rom.js >/dev/null 2>&1; then echo "OK   로맨틱 전용 맵 점검 (check_rom)"; else echo "FAIL 로맨틱 전용 맵 점검 (check_rom)"; FAIL=1; fi; fi
exit $FAIL
