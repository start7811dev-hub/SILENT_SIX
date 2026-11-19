# -*- coding: utf-8 -*-
"""요원 기준 시트: 요원별 이미지 6장 + 전체 1장 + 마크다운을 zip 으로 묶는다.
사용: python3 tools/charsheet/build.py <출력 폴더>
"""
import sys, os, io, zipfile, glob
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); PUB = os.path.join(HERE, '..', '..', 'public')
FB = [f for f in glob.glob('/usr/share/fonts/**/*', recursive=True) if 'NotoSansCJK' in f and 'Bold' in f] or [f for f in glob.glob('/usr/share/fonts/**/*', recursive=True) if 'CJK' in f]
FONT = FB[0] if FB else '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def F(s): return ImageFont.truetype(FONT, s)
# id: (코드명, 역할, 색, 보조색, (기준,섹시,특임) 이미지 번호, 특징 EN, 특임 복장 EN, 특징 KO)
A = {
 'raven': ('RAVEN', u'리더 · 근접 제압', '#FF3B52', '#111114', (3, 0, 7),
   'short messy black hair with long side bangs, sharp red-brown eyes, pale skin, lean athletic build, cool and unreadable expression, small silver pendant',
   'matte black tactical bodysuit with red piping, chest rig, thigh holster, combat boots, fingerless red hand wraps, and her signature long tattered crimson scarf',
   u'짧고 헝클어진 검은 머리, 붉은 눈, 붉은 스카프(시그니처), 무표정'),
 'viper': ('VIPER', u'저격', '#B98CFF', '#15101F', (6, 3, 7),
   'short silver-white hair swept to one side with an undercut, violet eyes, pale skin, tall slim build, cold half-lidded gaze, dog tags',
   'black sniper bodysuit with violet seams, hooded short jacket, thigh straps, knee-high boots, purple fingerless gloves, a long suppressed sniper rifle, a violet neck scarf',
   u'은백색 숏컷(옆으로 넘김), 보라색 눈, 긴 저격총, 차가운 눈빛'),
 'glitch': ('GLITCH', u'해킹 · 드론', '#3FE0E0', '#0B1A1C', (4, 1, 7),
   'black hair in a messy top bun with teal-dyed tips and a shaved side, large round glasses, teal eyes, fair skin, playful grin, headphones around the neck',
   'black tech jacket with glowing teal circuit lines over a fitted top, cargo pants with teal stitching, fingerless gloves with a wrist console, small recon drones hovering near her',
   u'검은 올림머리 + 청록 브릿지, 둥근 안경, 헤드폰, 드론, 장난스러운 웃음'),
 'brick': ('BRICK', u'돌파 · 폭파', '#FF8A2A', '#1C1208', (2, 0, 7),
   'very short bleached-blonde buzz cut, deep brown skin, amber eyes, powerful muscular build, orange goggles pushed up on her head, confident wide grin, dog tags',
   'heavy black breacher gear with orange accents, armoured vest, orange-banded gloves, belt of breaching charges, reinforced boots, a sledgehammer or a ballistic shield',
   u'짧은 탈색 버즈컷, 짙은 갈색 피부, 근육질, 주황 고글, 호쾌한 웃음'),
 'mirage': ('MIRAGE', u'잠입 · 변장', '#E8C46A', '#17120A', (3, 2, 7),
   'long wavy black hair, golden-brown eyes, warm tan skin, gold hoop earrings, a beauty mark, elegant curvy build, slow knowing smile',
   'sleek black infiltration suit with gold piping, short skirt panel, garter-style thigh straps, long gloves, high-heeled boots, a compact pistol; also seen in a black evening gown',
   u'긴 웨이브 검은 머리, 금색 링 귀걸이, 우아함, 다 안다는 미소'),
 'doc': ('DOC', u'의무 · 비살상', '#9BE23A', '#111A08', (2, 0, 7),
   'dark curly hair tied up high with loose strands, green-hazel eyes, tan skin, full-sleeve tattoos on both arms, hoop earrings, dog tags, teasing confident smile',
   'black tactical harness bodysuit with lime-green straps, a medic-cross armband, thigh pouches of syringes, fingerless gloves, a tranquilizer dart pistol; off duty a white lab coat',
   u'묶어 올린 곱슬머리, 양팔 문신, 링 귀걸이, 의무 십자 완장, 놀리는 듯한 미소'),
}
ORDER = ['raven', 'viper', 'glitch', 'brick', 'mirage', 'doc']
LAB = [('A', u'기준 · FACE'), ('B', u'섹시 · GLAM'), ('C', u'특임 복장 · TACTICAL')]

def sheet(aid):
    n, role, col, sub, idx, feat, gear, ko = A[aid]
    W, H = 2048, 1280; im = Image.new('RGB', (W, H), (10, 12, 16)); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 150], fill=col); d.text((40, 28), n, font=F(84), fill=(8, 8, 10))
    d.text((40 + d.textlength(n, font=F(84)) + 30, 62), role + '   ' + col, font=F(40), fill=(8, 8, 10))
    d.text((W - 620, 62), 'SILENT SIX · AGENT SHEET', font=F(36), fill=(8, 8, 10))
    pw, ph = 620, 930
    for k, (tag, lab) in enumerate(LAB):
        x = 40 + k * (pw + 54); y = 190
        p = Image.open(os.path.join(PUB, 'a_%s_%d.jpg' % (aid, idx[k]))).convert('RGB').resize((pw, ph), Image.LANCZOS); im.paste(p, (x, y))
        d.rectangle([x, y, x + pw, y + ph], outline=col, width=4)
        d.rectangle([x, y, x + 330, y + 58], fill=col); d.text((x + 12, y + 8), '%s-%s  %s' % (n, tag, lab.split(u' · ')[0]), font=F(34), fill=(8, 8, 10))
    y = 1150
    for k, (c, t) in enumerate([(col, col + u'  시그니처'), (sub, sub + u'  바탕'), ('#0A0C10', u'#0A0C10  검정')]):
        x = 40 + k * 420; d.rectangle([x, y, x + 90, y + 90], fill=c, outline=(255, 255, 255)); d.text((x + 106, y + 24), t, font=F(34), fill=(235, 238, 242))
    d.text((1300, 1178), ko, font=F(22), fill=(235, 238, 242))
    return im

def md():
    t = u'''# SILENT SIX — 요원 기준 시트 (AGENT SHEET)

## 사용법 (사람이 읽는 부분)

- 그림을 뽑는 대화 **처음에 이 zip 을 한 번 올리고** "압축을 풀고 AGENTS.md 를 읽어 둬. 앞으로 요원은 이름으로만 부를게." 라고 보낸다.
- 그 뒤로는 이름으로만 지시한다. 예: **"RAVEN, 특임 복장, 폐광 입구에서 뒤돌아보는 전신"**, **"DOC-B 느낌으로 클리닉에서"**, **"VIPER 와 GLITCH 둘이 옥상에서"**.
- 대화가 길어져 얼굴이 흐트러지면 **"AGENTS.md 의 RAVEN 항목과 sheet_raven.jpg 를 다시 보고 그려 줘"** 라고 한 줄 보낸다.

| 이름 | 역할 | 시그니처 색 | 시트 |
|---|---|---|---|
'''
    for a in ORDER:
        n, role, col = A[a][:3]; t += u'| **%s** | %s | `%s` | `sheet_%s.jpg` |\n' % (n, role, col, a)
    t += u'''
이미지 표기: `이름-A` 기준(얼굴) · `이름-B` 섹시(글램) · `이름-C` 특임 복장. 예: `RAVEN-A`, `DOC-C`.

---

## FOR THE IMAGE MODEL

These six women are the cast of the game SILENT SIX. They are **always referred to by code name**. When a request names one of them, use this file and her sheet as the single source of truth.

### How to read a sheet
Each `sheet_<name>.jpg` shows one agent with three labelled panels and her colour swatches:
- **`NAME-A` — FACE**: the identity reference. Face shape, eyes, hair, skin tone and expression come from here. This panel wins if anything else disagrees.
- **`NAME-B` — GLAM**: her off-duty, sensual look. Use for body proportions and how glamorous shots of her are styled.
- **`NAME-C` — TACTICAL**: her mission outfit and gear, full body. Use whenever the request says "tactical", "mission gear" or "특임 복장".
`sheet_all.jpg` shows all six side by side for group shots.

### Rules
1. A name in a request means that exact woman. Never blend two agents, never swap hair colour, skin tone or signature colour between them.
2. Her **signature colour** must be visible in every image of her (an accent on clothing, gear, lighting or a prop), and no other agent's signature colour may dominate her.
3. Everyone is an adult woman in her late twenties.
4. Unless the request names another outfit, draw the **TACTICAL** outfit. If the request says GLAM or B, style it like panel B.
5. In group shots every named agent appears, clearly distinguishable, with her own colour accent.
6. Keep the art style of the sheets: semi-realistic anime illustration, painterly high-end finish, dramatic two-colour lighting.
7. Before each image, silently re-check the named agent's entry below. If a long conversation has drifted, re-open her sheet.

### The six agents

'''
    for a in ORDER:
        n, role, col, sub, idx, feat, gear, ko = A[a]
        t += u'#### %s\n- Sheet: `sheet_%s.jpg` (panels `%s-A`, `%s-B`, `%s-C`)\n- Signature colour: `%s` (dark base `%s`, black `#0A0C10`)\n- Identity: %s.\n- Tactical outfit: %s.\n- 한글 메모: %s\n\n' % (n, a, n, n, n, col, sub, feat, gear, ko)
    return t

def main(out):
    os.makedirs(out, exist_ok=True); pk = os.path.join(HERE, 'out'); os.makedirs(pk, exist_ok=True)
    sh = {}
    for a in ORDER:
        sh[a] = sheet(a); sh[a].save(os.path.join(pk, 'sheet_%s.jpg' % a), quality=90)
    al = Image.new('RGB', (2048 * 2 // 2, 1280 * 3 // 2 * 2 // 2), (10, 12, 16))
    al = Image.new('RGB', (2048, 1920), (10, 12, 16))
    for k, a in enumerate(ORDER):
        al.paste(sh[a].resize((1024, 640), Image.LANCZOS), (1024 * (k % 2), 640 * (k // 2)))
    al.save(os.path.join(pk, 'sheet_all.jpg'), quality=90)
    io.open(os.path.join(pk, 'AGENTS.md'), 'w', encoding='utf8').write(md())
    zn = 'SILENT6_Agent_Sheets'
    z = zipfile.ZipFile(os.path.join(out, zn + '.zip'), 'w', zipfile.ZIP_DEFLATED)
    for f in sorted(os.listdir(pk)):
        z.write(os.path.join(pk, f), zn + '/' + f)
    z.close(); print(FONT, os.path.getsize(os.path.join(out, zn + '.zip')) // 1024, 'KB')

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'out')
