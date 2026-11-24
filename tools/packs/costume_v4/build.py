# -*- coding: utf-8 -*-
"""코스튬 미션 맵 세트 v4: 요원별 zip 6개.
v3(맵 1 + 소품 시트 3) + EP2 정밀 동선 기준(32 m 격자 정렬) + 대화 일러스트 9장(상대 2명 × 3표정 + 요원 3표정).
요원 한 명 = 맵 1 + 소품 시트 3 + 대화 일러스트 9 = 13장. 6명 78장.
사용: python3 tools/packs/costume_v4/build.py <출력 폴더>
"""
import sys, os, io, zipfile, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); TOOLS = os.path.join(HERE, '..', '..'); ROOT = os.path.join(TOOLS, '..')


def load(name, path, extra=()):
    for p in extra: sys.path.insert(0, p)
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for p in extra: sys.path.remove(p)
    return m


V3 = load('costume_v3_build', os.path.join(HERE, '..', 'costume_v3', 'build.py'), [os.path.join(HERE, '..', 'costume_v3')])
sys.modules.pop('build', None)
CSET = load('costume_set', os.path.join(TOOLS, 'map', 'costume_set.py'), [os.path.join(TOOLS, 'charsheet')])
V5 = load('costume_packs_v5', os.path.join(TOOLS, 'clear_studio', 'costume_packs_v5.py'))
RB = V3.RB; KO = V3.KO; AG = V3.AG
E2 = os.path.join(TOOLS, 'packs', 'story_s1e2'); CSO = os.path.join(TOOLS, 'charsheet', 'out')

GRID = u"""
GRID-ALIGNED MAP RULES (very important — the game collides on a 1-metre grid laid over your painting):
- The plan is exactly 32 x 32 metres. Every wall, railing, counter, stage edge and furniture edge lies on a whole-metre line.
- Walls are solid bands exactly 1 metre thick, cut off at waist height (about 1.2 m) so every floor tile stays visible. No roofs, ceilings, upper floors, balconies or overhangs.
- Only straight walls along the two isometric axes. No diagonal or curved walls; round things (a ring, a rink, a pool, a roulette wheel) sit inside square footprints with straight outer edges.
- Every doorway and corridor is exactly 2 metres wide; main aisles 3 metres. Doors are drawn open (an empty gap), never half-open.
- Fixed furniture and machinery have whole-metre footprints (1x1, 1x2, 2x2, 2x3 m) and are clearly darker or taller than the floor.
- Walkable floor is one calm, even, clearly readable material per zone. No floor-coloured low obstacles, no clutter, no loose objects.
- Leave an alley at least 2 m wide along the outer edges, and keep side alleys and gaps between rooms: the game is about hiding and moving between cover, so avoid one big empty hall with everything pushed to one side.
"""

STD = u"""# 0 · 정밀 동선 기준 — 코스튬 맵(32 × 32 m)

사람이 읽는 부분이다. 아래 규칙은 `1_맵_지시.md` 영어 지시에 이미 들어 있으니 따로 보내지 않는다. EP2 기준(30 m)을 코스튬 맵 크기(32 m)로 맞췄다.

| # | 규칙 | 이유 |
|---|---|---|
| 1 | 맵은 32 × 32 m, 2:1 아이소메트릭 마름모가 화면을 채운다. 1칸 = 1 m | 스토리 맵보다 큰 맵, 플레이타임 확보 |
| 2 | 벽 · 난간 · 카운터 · 무대 가장자리는 전부 1 m 단위 선 위 | 격자와 그림이 칸 단위로 일치 |
| 3 | 벽은 두께 1 m의 단단한 띠. 종이처럼 얇은 벽 금지 | 투명 벽 · 벽 통과 방지 |
| 4 | 벽은 두 축 방향 직선만. 링 · 빙판 · 풀 · 룰렛처럼 둥근 것은 네모 바닥 안에 | 칸이 비스듬히 잘리지 않게 |
| 5 | 문 · 통로 2 m, 큰 통로 3 m. 문은 열린 빈칸 | 요원 몸 반경 통과 |
| 6 | 실내는 컷어웨이. 벽은 허리 높이에서 잘림. 지붕 · 2층 · 발코니 없음 | 가려진 바닥 없음 |
| 7 | 가구 · 설비 바닥 크기는 정수 m | 막힌 칸과 그림 일치 |
| 8 | 바닥에 낱개 물건 금지. 낱개는 소품 시트로 | 충돌과 그림 일치 |
| 9 | 걸을 바닥과 막힌 곳의 명암 · 재질 차이가 분명. 코스튬 구역(공개 · 무대 쪽)과 직원 구역(뒷방)은 바닥 재질이 다름 | 길 · 구역을 한눈에 |
| 10 | 바깥 골목 2 m 이상, 방 사이 골목 유지. 한쪽만 휑하거나 한쪽에 몰린 배치 금지 | 은폐 · 엄폐와 동선 다양성 |

## 검수 순서

1. `1_맵_지시.md` 첫머리 검수 항목(특히 "질문 정답" 항목)
2. 위 10가지: 벽 두께 · 직선 · 문 폭 · 지붕 없음 · 바닥 낱개 없음
3. 틀린 부분만 같은 대화에서 다시 요청

## Claude 쪽 처리(그림이 온 뒤)

격자 맞춤 → 막힌 칸 추출 → 소품 · 인물 · 목표(진짜 1 + 가짜 2) 배치 → 코스튬 구역 지정 → 경비 · 카메라 → 대화 지점 2곳 → 자동 점검(시작 30초 안전, 모든 목표 도달, HARD 풀이) → 게임 적용.
"""


def dialogue(a):
    nm, look, cos = CSET.LOOK[a]; cos = V5.D[a]['cos'].rstrip('.')  # 리워드 컷 v5와 같은 코스튬
    t = u'# 3 · 대화 일러스트 — 코스튬 미션 %s\n\n## 사용법 (사람이 읽는 부분)\n\n- 결과: 9장(상대 2명 × 표정 3 + 요원 × 표정 3). 배경 투명 PNG.\n- **새 대화**에서 진행한다. 올릴 것: 이 zip(또는 `agents/sheet_%s.jpg`)과 이 파일.\n- 보낼 글: **"압축을 풀고 3_대화_일러스트_지시.md 만 읽고, 인물 한 명씩 3장 진행해 줘."** 다음 인물은 "next".\n- 검수: 세 장이 같은 사람 · 같은 옷 · 같은 구도이고 표정만 다른지, 상대는 오른쪽을 보고 요원은 왼쪽을 보는지, 무기 없음, 배경 투명(또는 순수 초록).\n- 투명 배경이 안 나오면 초록 배경 그대로 넘겨도 된다. Claude가 누끼를 딴다.\n\n| 파일 | 인물 |\n|---|---|\n' % (KO[a], a)
    for k, (ko, d) in enumerate(CSET.NPC[a]): t += u'| `d_C-%s_n%d_0~2.png` | %s |\n' % (a, k + 1, ko)
    t += u'| `d_C-%s_me_0~2.png` | %s (코스튬) |\n' % (a, KO[a])
    pb = CSET.PB.replace(u'# PART B — DIALOGUE PORTRAITS (54 images)', u'# DIALOGUE PORTRAITS (9 images)').lstrip(u'\n-').lstrip()
    t += u'\n---\n\n' + pb + u'## The three characters\n\n'
    for k, (ko, d) in enumerate(CSET.NPC[a]):
        t += u'- **`d_C-%s_n%d_0.png`, `_1.png`, `_2.png`** — %s. Other person, faces RIGHT. %s.\n' % (a, k + 1, ko, d[0].upper() + d[1:])
    t += u'- **`d_C-%s_me_0.png`, `_1.png`, `_2.png`** — %s in costume. Agent, faces LEFT. Sheet: `agents/sheet_%s.jpg` (%s). Outfit: %s.\n' % (a, nm, a, look, cos)
    return t


def files(a):
    fs = V3.files(a)
    m = fs[u'1_맵_지시.md']
    anchor = u'- The plan is **32 x 32 metres**'
    i = m.index(anchor); j = m.index(u'\n', i)
    fs[u'1_맵_지시.md'] = m[:j + 1] + GRID + m[j + 1:]
    fs[u'1_맵_지시.md'] = fs[u'1_맵_지시.md'].replace(u'## 사용법 (사람이 읽는 부분)\n', u'## 사용법 (사람이 읽는 부분)\n\n- 정밀 동선 기준(`0_정밀_동선_기준.md`, 32 m 격자 정렬)이 영어 지시에 들어 있다.\n', 1)
    fs[u'0_정밀_동선_기준.md'] = STD
    fs[u'3_대화_일러스트_지시.md'] = dialogue(a)
    t = V3.data.T[a]; fn = 'bgc_%s.jpg' % a
    fs[u'읽어주세요.md'] = (u'# SILENT SIX — 코스튬 미션 맵 세트 v4 · %s "%s"\n\n| 순서 | 파일 | 결과물 | 장수 | 대화 |\n|---|---|---|---|---|\n'
        u'| 0 | `0_정밀_동선_기준.md` | 검수 기준(사람용) | - | - |\n'
        u'| 1 | `1_맵_지시.md` | `%s` · %s | 1 | 새 대화 |\n'
        u'| 2 | `2_소품_지시.md` | `p_c_%s_cover.png` · `_show.png` · `_special.png` | 3 (낱개 18개) | 1과 같은 대화 |\n'
        u'| 3 | `3_대화_일러스트_지시.md` | `d_C-%s_n1_0~2` · `_n2_0~2` · `_me_0~2.png` | 9 | 새 대화 |\n'
        u'| - | `4_판_정리.md` | 검토용. GPT에 시키지 않는다 | - | - |\n\n합계 13장.\n\n'
        u'## ChatGPT에 보내는 방법\n\n1. 새 대화에 이 zip을 올리고 **"압축을 풀고 1_맵_지시.md 만 읽고 진행해 줘."**\n2. 맵을 검수한 뒤(첫머리 항목 + `0_정밀_동선_기준.md`) 같은 대화에서 **"이제 2_소품_지시.md 를 읽고 시트 1부터 한 장씩."** 다음 장은 "next".\n3. **새 대화**에 zip을 다시 올리고 **"압축을 풀고 3_대화_일러스트_지시.md 만 읽고, 인물 한 명씩 3장 진행해 줘."**\n\n한 대화에 지시 파일 하나씩만 읽힌다. 여러 개를 한꺼번에 읽히면 섞인다.\n\n'
        u'## v3에서 바뀐 것\n\n- EP2 **정밀 동선 기준**을 32 m 맵에 맞춰 넣었다: 벽 1 m 띠, 1 m 격자 정렬, 문 2 m, 지붕 없음, 둥근 것은 네모 바닥 안, 골목 유지.\n- 코스튬 대화용 **일러스트 9장**을 같은 묶음에 넣었다(대화 화면에 상대와 요원이 함께 뜬다).\n- 리워드 컷은 이미 적용했다(v0.44.0). 이 묶음에는 없다.\n\n'
        u'## 넘기는 방법\n\n맵 · 소품 · 일러스트를 파일 이름 그대로 `Asset/Special Mission/Costume/Map/<요원>/` 같은 폴더에 넣고 연결해 주면, 격자 → 배치 → 대화 → 점검 → 게임 적용까지 진행한다.\n\n'
        u'## 참고 이미지\n\n- `ref/look_indoor.jpg` 실내 맵 화풍(EP1 실내). `ref/look_scale.jpg` 축척 · 격자 정렬 예시(EP2 30 m). 배치는 따라 하지 않는다.\n- `ref/sprite_sheet_example.png` 소품 시트 형식.\n- `agents/sheet_%s.jpg` 요원 시트(대화 일러스트용).\n') % (KO[a], t['t'], fn, t['place_ko'], a, a, a)
    return fs


def build(out):
    os.makedirs(out, exist_ok=True); allz = []
    for a in AG:
        fs = files(a); N = 'SILENT6_Map_Costume_V4_%s' % a.upper()
        z = zipfile.ZipFile(os.path.join(out, N + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        for k, v in fs.items(): z.writestr(N + '/' + k, v)
        z.write(os.path.join(E2, 'ref', 'look_indoor_ep1.jpg'), N + '/ref/look_indoor.jpg')
        z.write(os.path.join(E2, 'ref', 'look_scale_30m.jpg'), N + '/ref/look_scale.jpg')
        z.write(os.path.join(RB.W, 'ref_sprite_sheet_example.png'), N + '/ref/sprite_sheet_example.png')
        z.write(os.path.join(CSO, 'sheet_%s.jpg' % a), N + '/agents/sheet_%s.jpg' % a)
        z.close(); allz.append(N + '.zip'); print(N, os.path.getsize(os.path.join(out, N + '.zip')) // 1024, 'KB')
    z = zipfile.ZipFile(os.path.join(out, 'SILENT6_Map_Costume_V4_ALL.zip'), 'w', zipfile.ZIP_STORED)
    for f in allz: z.write(os.path.join(out, f), f)
    z.close()


if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else 'out')
