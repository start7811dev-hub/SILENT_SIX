import sys; sys.path.insert(0,'/home/claude/cw'); from paint import G
g=G()
def inpoly(px,py,P):
    c=False;n=len(P)
    for i in range(n):
        x1,y1=P[i];x2,y2=P[(i+1)%n]
        if (y1>py)!=(y2>py) and px<(x2-x1)*(py-y1)/(y2-y1)+x1: c=not c
    return c
def sd_fill(ch,P):
    for y in range(1,32):
        for x in range(1,32):
            s=x+y+1; d=x-y
            if inpoly(d,s,[(q[1],q[0]) for q in P]): g.c(ch,(x,y))
# 정원(가운데, 못 들어감)
sd_fill('C',[(25,-4.5),(25,4.5),(30.5,6.8),(33.5,3),(33.5,-4.5),(30.5,-8.3)])
# 유리 통로의 정원 쪽 유리벽
for x in range(1,32):
    y=21-x
    if 1<=y<=31 and -2<=x-y<=6: g.c('W',(x,y))
# 약제실: 앞벽(리셉션 쪽) 문 d=-3..-1, 옆벽 d=-9 / d=5, 뒷벽 s=34
for y in range(1,32):
    for x in range(1,32):
        s=x+y+1; d=x-y
        if 34<=s<=45 and d in (-9,5): g.c('#',(x,y))
        if s in (33,34) and -9<=d<=5: g.c('#',(x,y))
        if s in (44,45) and -9<=d<=5 and not (-3<=d<=-1): g.c('#',(x,y))
        if s in (35,36) and -7<=d<=3: g.c('B',(x,y))
# 리셉션 데스크
for x in range(22,28):
    y=50-x
    if -5<=x-y<=3: g.c('B',(x,y))
# 진료동(왼쪽): 시술실 · 기록실 · 원장실
g.vy(9,20,31); g.hx(20,0,9); g.o((9,25),(9,26))
g.vy(8,12,20); g.hx(12,0,8); g.o((8,16),(8,17))
g.vy(10,0,9); g.hx(9,0,10); g.o((8,9),(9,9))
g.r('B',1,22,1,28); g.c('B',(5,26),(6,26),(5,27),(6,27))
g.r('B',1,14,1,18); g.c('B',(5,4),(6,4),(5,5),(6,5)); g.r('B',1,2,1,6)
# 스파동(오른쪽): 사우나 · 풀 · 탈의실
g.hx(5,10,16); g.vy(16,0,5); g.o((16,3),(16,4)); g.r('B',11,1,15,1)
g.r('P',18,2,27,7)
g.hx(12,21,28); g.hx(18,21,28); g.vy(21,12,18); g.vy(28,12,23); g.o((28,15),(28,16),(21,15))
g.r('B',22,13,26,13)
g.save('/home/claude/cw/work/map_doc.json')
