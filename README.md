# SILENT SIX

코만도스풍 실시간 잠입 전술 퍼즐. 폰 브라우저에서 도는 HTML5 게임이다.
빌드 과정이 없다. `public/index.html` 한 파일에 게임 코드가 다 들어 있고, 같은 폴더에 그림 파일이 있다.

## 폴더

| 경로 | 내용 |
|---|---|
| `public/` | 게임 본체. 이 폴더를 그대로 배포한다 |
| `public/index.html` | 게임 코드 전체(스타일, 미션 데이터, 로직) |
| `tools/verify.sh` | 미션 24판이 클리어 가능한지 자동 확인 |
| `tools/solve.js` | 위 확인에 쓰는 탐색기 |
| `tools/studio/` | 요원 풀세트 이미지 생성기(맥용, OpenAI 키 필요) |
| `tools/map/` | 맵 그림에 격자를 맞출 때 쓰는 스크립트 |
| `docs/CHANGELOG.md` | 버전별 변경 기록 |

## 실행

```
cd public && python3 -m http.server 8000
```
브라우저에서 http://localhost:8000 을 연다.

## 패치 순서

1. 브랜치를 만든다: `git checkout -b patch/내용`
2. `public/` 을 고친다.
3. 미션이나 경비병 배치를 건드렸으면 `tools/verify.sh` 를 돌린다(node 필요). 전부 OK 여야 한다.
4. `public/index.html` 의 `VERSION` 과 `docs/CHANGELOG.md` 를 올린다.
5. 커밋하고 main 에 합친 뒤 태그를 단다: `git tag v0.9.1 && git push --tags`

버전 규칙: 버그 수정은 끝자리(0.9.0 → 0.9.1), 미션·기능 추가는 가운데(0.9 → 0.10), 정식 출시가 1.0.0.

## 배포

`vercel.json` 이 `public/` 을 배포 폴더로 지정한다. Vercel 에 이 저장소를 연결하면 main 에 올릴 때마다 배포된다.

## 문서

- 게임 기획서(GDD): https://claude.ai/artifact/1p1cHupV9XCeBuY3JVN3gv
- 요원 포즈 프롬프트: https://claude.ai/artifact/BWeBedPmnBhPX4d9sXVXVk
