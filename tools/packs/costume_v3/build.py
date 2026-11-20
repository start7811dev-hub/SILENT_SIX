# -*- coding: utf-8 -*-
"""코스튬 미션 맵 제작 묶음 v3: 요원별 zip 6개. 맵 6장 + 소품 시트 18장(낱개 108개). 로맨틱 v3와 같은 방식.
사용: python3 tools/packs/costume_v3/build.py <출력 폴더>
"""
import sys, os, io, zipfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'romantic_v3'))
import data, build as RB
AG = RB.AG; KO = RB.KO; M = 32


def files(a):
    t = data.T[a]; fn = 'bgc_%s.jpg' % a; out = {}
    m = u'# 1 · 맵 — 코스튬 미션 %s "%s" (%s)\n\n## 사용법 (사람이 읽는 부분)\n\n- 결과 파일명: `%s` (1장)\n- 구조만 들어간다. 가구 · 관객 · 인물 · 목표는 `2_소품_지시.md`로 따로 뽑는다.\n- 스토리 맵보다 1.5배 큰 맵이다(가로세로 32 m).\n- 검수 (틀리면 그 부분만 다시 요청). **"질문 정답"이라고 적힌 항목은 대화 퀴즈의 답이라서 반드시 맞아야 한다.**\n' % (KO[a], t['t'], t['place_ko'], fn)
    for i, c in enumerate(t['chk'] + [u'바닥에 낱개 물건이 없다', u'가까운 두 변의 벽이 낮아서 안쪽 바닥이 다 보인다', u'코스튬이 통하는 곳과 아닌 곳의 바닥 재질이 다르다'], 1): m += u'  %d. %s\n' % (i, c)
    extra = u"\n\n**Floors tell the zones apart.** The public, show-side floors and the staff-only back rooms must have clearly different floor materials and colours, as described, so a player can tell at a glance which zone they are standing in."
    m += u'\n---\n\n' + RB.MAPRULES % dict(ref='look_indoor.jpg', file=fn, m=M, px=int(round(900.0 / M)), light=t['light'], near=u'the wall cut down to a 1 m stub', place=t['place'], lay=t['lay'] + extra)
    out[u'1_맵_지시.md'] = m
    p = u'# 2 · 소품 낱개 세트 — 코스튬 미션 %s "%s"\n\n## 사용법 (사람이 읽는 부분)\n\n- 결과: 시트 3장. 한 장에 6개씩 3×2 칸.\n- 맵 그림이 먼저 나온 뒤 **같은 대화에서** 이어서 진행한다.\n- 목표물은 한 번만 그린다. 게임이 똑같은 것을 세 곳에 놓는다.\n- 검수: 칸마다 1개, 배경이 한 가지 색, 물건끼리 닿지 않음, 맵과 같은 각도, 글자 없음.\n\n| 파일 | 내용 |\n|---|---|\n' % (KO[a], t['t'])
    for k, ko, items in t['props']: p += u'| `p_c_%s_%s.png` | %s |\n' % (a, k, ko)
    p += u'\n---\n\n' + (RB.PROPRULES % dict(map=fn, ref='look_indoor.jpg')).replace(u'Make **2 sheets', u'Make **3 sheets')
    for i, (k, ko, items) in enumerate(t['props'], 1):
        p += u'\n### Sheet %d — `p_c_%s_%s.png`\nLeft to right, top row then bottom row.\n' % (i, a, k) + u''.join(u'%d. %s\n' % (j, x) for j, x in enumerate(items, 1))
    out[u'2_소품_지시.md'] = p
    out[u'4_판_정리.md'] = u'# 4 · 판 정리 — 코스튬 미션 %s "%s"\n\n그림 생성용이 아니다. 검토용이다. 대화의 질문과 정답은 `docs/COSTUME.md` 6장 그대로다.\n\n' % (KO[a], t['t']) + u''.join(u'- %s\n' % x for x in t['info']) + u'\n## 맵에서 반드시 맞아야 하는 것\n\n' + u''.join(u'- %s\n' % c for c in t['chk'] if u'질문 정답' in c)
    out[u'읽어주세요.md'] = u'# SILENT SIX — 코스튬 미션 맵 제작 묶음 · %s "%s"\n\n| 순서 | 파일 | 결과물 | 장수 |\n|---|---|---|---|\n| 1 | `1_맵_지시.md` | `%s` · %s | 1 |\n| 2 | `2_소품_지시.md` | `p_c_%s_cover.png` · `_show.png` · `_special.png` | 3 (낱개 18개) |\n| - | `4_판_정리.md` | 검토용. GPT에 시키지 않는다 | - |\n\n합계 4장.\n\n## ChatGPT에 보내는 방법\n\n1. 새 대화에 이 zip을 올리고 **"압축을 풀고 1_맵_지시.md 만 읽고 진행해 줘."**\n2. 맵을 검수한 뒤 같은 대화에서 **"이제 2_소품_지시.md 를 읽고 시트 1부터 한 장씩."** 다음 장은 "next".\n\n## 만드는 방식\n\n- 맵 그림에는 **벽 · 방 · 길 같은 구조만** 넣는다. 가구 · 관객 · 인물 · 목표는 전부 낱개로 뽑아 Claude가 배치한다.\n- 예전 코스튬 원샷 세트의 맵 지시(가이드 블록 방식)는 이 묶음으로 대체한다. 그 세트의 대화 일러스트 54장 지시는 맵과 무관해서 그대로 쓴다. 리워드 컷은 v4 묶음을 쓴다.\n- 그림이 오면 Claude가 격자를 따고 → 소품 · 인물 · 목표 배치 → 코스튬 구역 지정 → 경비 배치 → 풀이 검증 → 게임에 넣는다.\n\n## 참고 이미지\n\n- `ref/look_indoor.jpg` 실내 맵 화풍 기준(지붕 없이 벽을 한 높이로 자른 모습). 배치는 따라 하지 않는다.\n- `ref/sprite_sheet_example.png` 소품 시트 형식 기준.\n' % (KO[a], t['t'], fn, t['place_ko'], a)
    return out


def build(out):
    os.makedirs(out, exist_ok=True)
    for a in AG:
        fs = files(a); N = 'SILENT6_Map_Costume_V3_%s' % a.upper(); d = os.path.join(HERE, a); os.makedirs(d, exist_ok=True)
        z = zipfile.ZipFile(os.path.join(out, N + '.zip'), 'w', zipfile.ZIP_DEFLATED)
        for k, v in fs.items(): z.writestr(N + '/' + k, v); io.open(os.path.join(d, k), 'w', encoding='utf8').write(v)
        z.write(os.path.join(RB.PUB, 'bg5.jpg'), N + '/ref/look_indoor.jpg'); z.write(os.path.join(RB.W, 'ref_sprite_sheet_example.png'), N + '/ref/sprite_sheet_example.png')
        z.close(); print(N, os.path.getsize(os.path.join(out, N + '.zip')) // 1024, 'KB')


if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else 'out')
