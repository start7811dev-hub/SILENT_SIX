#!/bin/bash
cd "$(dirname "$0")"
if ! command -v python3 >/dev/null; then echo "python3가 없습니다. 터미널에서 xcode-select --install 을 실행한 뒤 다시 열어 주세요."; read -n 1; exit 1; fi
python3 silent6_studio.py
