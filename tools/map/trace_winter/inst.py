import io,json,maps,t,shutil
G={1:dict(ops=['raven'],guards="[{wps:[[11,4],[11,7]]},{wps:[[4,4],[4,9]]},{wps:[[13,6],[16,6]]},{wps:[[1,16],[6,16]]},{wps:[[10,4]],faces:[1.57,3.14],ft:5}]",par=150,sk=0.44,
     t='첫 번째 상자',copy='선물은<br>명단이었다.',pre='18:40, 시청 앞 크리스마스 마켓. 헬리오스의 배달 책임자, 통칭 산타가 오늘 밤 다섯 곳을 돈다. 첫 명단은 대형 트리 아래 선물 더미에 있다. 민간인이 많다. 아무도 죽이지 않는다.',post=['명단을 들고 광장을 빠져나왔다.','다음 배달지는 화물 조차장, 화차 44호다.'],ol='배달 명단',ov='회수',bc='nokill',img='a_raven_5.jpg',time=3),
   2:dict(ops=['brick','glitch'],guards="[{wps:[[1,6],[24,6]]},{wps:[[0,9],[8,9]]},{wps:[[15,10],[21,10]]},{wps:[[1,15],[16,15]]},{wps:[[24,5]],tower:true,faces:[3.14,2.7],ft:6}]",par=240,sk=0.42,
     t='화차 44호',copy='노크는<br>한 번만 한다.',pre='20:10, 화물 조차장. 화차 수십 량 가운데 한 량에만 산타의 상자가 실려 있다. 화차 사이 틈으로만 건널 수 있다.',post=['화차 44호가 통째로 날아갔다.','남은 상자는 얼어붙은 호수의 보트하우스로 갔다.'],ol='화차 44호',ov='폭약 설치',bc='noload',img='a_brick_5.jpg',time=4),
   3:dict(ops=['viper','doc'],guards="[{wps:[[6,4],[6,13]]},{wps:[[10,6],[16,6]]},{wps:[[12,5]],faces:[1.57,2.4],ft:5},{wps:[[6,14],[10,14]]}]",par=240,sk=0.44,by='doc',
     t='얼음 위의 선물',copy='숨을 곳이<br>없는 밤.',pre='22:30, 얼어붙은 호수. 상자를 본 증인이 건너편 보트하우스에 갇혀 있다. 얼음 위에는 오두막 몇 채뿐이다.',post=['증인은 제 발로 걸어 나왔다.','그가 본 상자는 자정 미사가 열리는 대성당으로 갔다.'],ol='증인',ov='응급 처치',bc='onesnipe',img='a_viper_5.jpg',time=4),
   4:dict(ops=['mirage','raven'],guards="[{wps:[[6,6],[9,13]]},{wps:[[1,8],[2,19]]},{wps:[[13,2],[13,12]]},{wps:[[1,4]],faces:[1.57,2.6],ft:6}]",par=200,sk=0.42,
     t='자정 미사',copy='헌금은<br>우리가 걷는다.',pre='00:00, 대성당. 제단 옆 헌금함에 산타의 돈가방이 들어 있다. 추적기가 든 가방으로 바꿔 놓고 나온다.',post=['가방을 바꿔 놓았다.','추적기는 사설 비행장에서 멈췄다.'],ol='헌금함',ov='바꿔치기',bc='ghost',img='a_mirage_5.jpg',time=3),
   5:dict(ops=['raven','viper'],guards="[{wps:[[4,5],[9,5]]},{wps:[[1,1],[8,1]]},{wps:[[13,4],[13,9]]},{wps:[[18,10],[21,12]]},{wps:[[4,10]],tower:true,faces:[-1.3,-0.4],ft:6}]",par=260,sk=0.44,
     t='산타의 썰매',copy='이륙은<br>없다.',pre='03:30, 사설 비행장. 격납고의 전용기가 산타의 썰매다. 뜨기 전에 화물을 확보한다.',post=['화물칸에는 리본 묶인 빈 상자와 카드 한 장뿐이었다.','받는 사람 칸에 6과의 과 번호가 적혀 있다. 메리 크리스마스.'],ol='산타의 화물',ov='확보',bc='nogun',img='a_raven_6.jpg',time=3)}
def js(n):
    o=maps.OUT[n];g=G[n];M=[''.join(r) for r in o['MAP']];st=o['start']
    ops=','.join("{id:'%s',x:%d,y:%d}"%(g['ops'][i],st[i][0],st[i][1]) for i in range(len(g['ops'])))
    obj="{x:%d,y:%d,use:[%d,%d],label:'%s',verb:'%s',time:%d%s}"%(o['obj'][0],o['obj'][1],o['use'][0],o['use'][1],g['ol'],g['ov'],g['time'],(",by:'%s'"%g['by']) if g.get('by') else '')
    hts=json.dumps(o['hts']).replace('"',"'")
    return (" {t:'%s',copy:'%s',pre:'%s',post:%s,bc:'%s',img:'%s',par:%d,\n  m:{bg:'bgw%d.jpg',sk:%s,wake:90,opaque:'%s',hts:%s,proj:%s,MAP:%s,\n  ops:[%s],exit:%s,objective:%s,\n  guards:%s}}"
      %(g['t'],g['copy'],g['pre'],json.dumps(g['post'],ensure_ascii=False).replace('"',"'"),g['bc'],g['img'],g['par'],n,g['sk'],o['opaque'],hts,json.dumps([round(v,9) for v in t.H(n)]),json.dumps(M),ops,json.dumps([list(e) for e in o['exit']]),obj,g['guards']))
def install():
    p='/home/claude/silent_six/public/index.html';s=io.open(p,encoding='utf8').read()
    a=s.index('var WINTER=[');b=s.index('var SPECIAL=[')
    new='var WINTER=[\n'+',\n'.join(js(n) for n in range(1,6))+'];\nvar WIDX=[];\nWINTER.forEach(function(c,ci){\n  var m={},k;for(k in c.m)m[k]=c.m[k];\n  m.title=c.t;m.code=\'BLOODY CHRISTMAS // \'+(ci+1)+\' / 5\';m.copy=c.copy;m.pre=c.pre;m.post=c.post;m.img=c.img;m.winter=true;m.season=\'w\';m.key=\'W-\'+(ci+1);m.bc=c.bc;m.par=c.par;\n  m.goal0=m.objective.label+\' — \'+m.objective.verb;m.goal1=m.ops.length>1?\'두 명 모두 진입 지점으로 복귀\':\'진입 지점으로 복귀\';m.brief=\'<ul>\'+RULES+\'</ul>\';\n  WIDX.push(MIS.length);MIS.push(m);\n});\n'
    s=s[:a]+new+s[b:];io.open(p,'w',encoding='utf8').write(s)
    for n in range(1,6):shutil.copy('x/bgw%d.jpg'%n,'/home/claude/silent_six/public/bgw%d.jpg'%n)
if __name__=='__main__':install()
