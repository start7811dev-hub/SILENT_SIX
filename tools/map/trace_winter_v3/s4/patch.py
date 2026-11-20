# -*- coding: utf-8 -*-
import io,json
p='public/index.html'; s=io.open(p,encoding='utf8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:60],s.count(a)); s=s.replace(a,b)
D=json.load(open('/tmp/s4/map.json')); MP=D['MAP']
G=[{'wps':[[7,22]],'faces':[0,1.57],'ft':6,'mark':True,'tag':u'부제','loud':True},{'wps':[[12,5]],'faces':[0,1.57],'ft':8},{'wps':[[18,5]],'faces':[3.14,1.57],'ft':8},
   {'wps':[[6,8],[6,13]]},{'wps':[[24,10],[24,15]]},{'wps':[[15,8],[15,25]]},{'wps':[[11,25],[23,25]]},{'wps':[[28,6],[28,22]]},{'wps':[[11,7],[20,7]]},{'wps':[[5,23],[5,13]]}]
for g in G:
    for x,y in g['wps']: assert MP[y][x]=='.',(x,y,MP[y][x])
for x,y in [(16,28),(17,28),(16,4),(24,1),(27,28),(28,28),(12,26),(16,26),(21,25)]: assert MP[y][x]=='.',(x,y)
a=s.index(u" {t:'자정 미사'"); b=s.index(u" {t:'산타의 썰매'")
W4=u""" {t:'자정 미사',copy:'헌금은<br>우리가 걷는다.',pre:'자정, 대성당. 세 번째는 상자가 아니라 돈가방이다. 제단 옆 헌금함에 들어 있다. 열쇠는 고해소 앞의 부제가 갖고 있다. 미사 중이라 소리를 낼 수 없다. 종지기 방의 줄을 당기면 종이 울리는 동안은 소리가 묻힌다.',post:['가방을 바꿔 놓았다.', '산타는 헬리오스의 돈도 빼돌리고 있다. 추적기는 사설 비행장에서 멈췄다.'],bc:'ghost2',img:'a_mirage_5.jpg',par:480,tips:["<b>신도석</b>은 넘을 수 없다. 줄 사이로 앉아서 지나가면 멀리서는 안 보인다.", "<b>종 줄</b>을 당기면 15초 동안 종이 울린다. 그동안은 발소리도 제압 소리도 묻힌다. 언제 당길지는 직접 정한다.", "<b>부제</b>는 종이 울리지 않을 때 쓰러뜨리면 주변 경비가 소리를 듣는다.", "가방을 바꾸면 미사가 끝난다. 신도들이 일어나 <b>가운데 통로</b>를 막고, 경비가 정문 셋을 지킨다. <b>납골당 통로</b>로 나간다."],
  m:{bgs:['bgw4_0.jpg','bgw4_1.jpg'],bg:'bgw4_0.jpg',sk:0.3,zm:1.5,wake:120,opaque:'#BJ',hts:{'#': 40, 'B': 34, 'J': 34, 'P': 12, 'C': 12, 'X': 16, 'R': 0},proj:%s,MAP:%s,
  ops:[{id:'mirage',x:16,y:28},{id:'raven',x:17,y:28}],exit:[[16, 28], [17, 28]],objective:{x:16,y:3,use:[16,4],label:'헌금함',verb:'바꿔치기',time:3},
  lock:'헌금함이 잠겨 있다. 종을 울리고 부제의 열쇠부터.',
  subs:[{k:'bell',x:23,y:1,use:[24,1],label:'종 줄',verb:'종 울리기',btn:'종',time:2,quiet:15,done:'자정의 종이 울린다. 15초 동안 소리가 묻힌다.'},{k:'mark',label:'부제',verb:'부제 재우기',done:'열쇠를 챙겼다.'}],
  evac:{note:'미사가 끝났다. 신도들이 일어선다.',sw:{bit:1,clr:[],shut:%s},posts:[{post:[12,26],face:-1.57},{post:[16,26],face:-1.57},{post:[21,25],face:-1.57}],gates:[{n:'납골당 통로',cells:[[27,28],[28,28]],post:[27,26],face:-1.57,bar:['p_w1_bar_x.png',27,28,2,1]}]},
  santa:{img:'p_w_santa.png',x:14.5,y:1.5,up:34,t:20},
  dlg:{cast:{santa:'d_w_santa_4.webp',mirage:'d_w4_mirage.webp'},
   start:[['hq','자정, 대성당이다. 세 번째는 상자가 아니라 돈가방이다. 제단 옆 헌금함에 들어 있다. 추적기가 든 가방으로 바꿔 놓고 나온다.'],['mirage','성가대 옷은 구해 놨어. 흰색이 나한테 이렇게 잘 받는 줄은 몰랐네.'],['raven','헌금함은 잠겨 있을 텐데. 열쇠는 누가 갖고 있지?',0],['mirage','부제. 고해소 앞을 떠나질 않더라. 재우려면 소리가 좀 날 텐데, 미사 중이라 곤란해.'],['raven','종이 울릴 때 하면 되겠군. 종지기 방에 가서 내가 당긴다.',2],['mirage','자정 종을 네 마음대로 치겠다고? 벌받을 거야, 레이븐.']],
   mid:[['santa','미사 중엔 조용히 해야지. 레이븐, 넌 예전에도 발소리가 컸어.'],['raven','…예전? 너, 나를 언제 봤는데.',1],['santa','네가 스카프를 처음 감던 해부터.'],['mirage','레이븐, 얼굴 굳었어. 저 사람 누군지 알겠어?'],['raven','몰라. 근데 저쪽은 날 너무 잘 알아.',1]],
   obj:[['mirage','잠깐, 가방 안에 송금 전표가 있어. 받는 쪽이… 헬리오스가 아니야. 개인 계좌야.'],['santa','쉿. 그건 못 본 걸로 해 줘. 나도 먹고살아야 하잖아?'],['raven','미사가 끝났어! 사람들이 일어난다. 정문은 막혔어. 납골당 쪽으로 돌아!',1]],
   end:[['raven','헬리오스 돈까지 빼돌렸어. 우릴 팔고, 헬리오스도 속이고 있는 거야.',1],['mirage','양쪽을 다 속이는 사람이라… 솔직히 좀 내 취향인데.'],['raven','농담할 기분 아니야.',0],['mirage','알아. 그래서 하는 거야. …추적기가 멈췄어. 사설 비행장이야. 03시 30분에 뜨는 전용기가 한 대 있어.']]},
  guards:%s}},
""" % (json.dumps(D['proj']),json.dumps(MP),json.dumps(D['shut']),json.dumps(G,ensure_ascii=False))
s=s[:a]+W4+s[b:]
rep("cam:!!d.cam,boss:!!d.boss,keen:!!d.keen,","cam:!!d.cam,boss:!!d.boss,tag:d.tag||'',loud:!!d.loud,keen:!!d.keen,")
rep("  if(M.subs){var pl=[];st.guards.forEach(function(g){if(g.plain)pl.push(g.id);});","  M.guards.forEach(function(d,i){if(d.mark)st.radio=i;});\n  if(M.subs&&st.radio<0){var pl=[];st.guards.forEach(function(g){if(g.plain)pl.push(g.id);});")
rep("if(M.subs[i].k==='radio')subDone(i);","if(M.subs[i].k==='radio'||M.subs[i].k==='mark')subDone(i);")
rep("var st={t:0,subs:[],shut:{},clr:{},bgk:0,evT:0,","var st={t:0,subs:[],shut:{},clr:{},bgk:0,evT:0,bellT:0,")
rep("if(sb.freeze!=null){","if(sb.quiet)S.bellT=S.t+sb.quiet;if(sb.freeze!=null){")
rep("  if(S.dark)k*=S.dark;","  if(S.bellT>S.t){q=true;hot=true;t='자정의 종 · 소리가 묻힌다 '+Math.ceil(S.bellT-S.t);}\n  if(S.dark)k*=S.dark;")
rep("pop(g.x,g.y,a.kill?'사살':'제압',OPD[o.id].col);snd('hit');}","pop(g.x,g.y,a.kill?'사살':'제압',OPD[o.id].col);snd('hit');if(g.loud&&!ENV.quiet){S.noise.push({x:g.x,y:g.y,t:0.6,r:9});alertNear(g.x,g.y,9,g.x,g.y,g);say('소리가 성당에 울렸다.');}}")
rep("    if(g.plain&&g.meter<=0.02&&g.state!=='investigate')label(","    if(g.tag&&g.meter<=0.02&&g.state!=='investigate')label(g.tag,o[0],o[1]-up,12,'#ffd27a');\n    if(g.plain&&g.meter<=0.02&&g.state!=='investigate')label(")
rep(" ghost:['유령',"," ghost2:['조용한 미사','부제 말고는 누구의 몸에도 손대지 않는다',function(){return S.kos<=1&&S.kills===0;}],\n ghost:['유령',")
rep("var VERSION='0.29.0';","var VERSION='0.30.0';")
io.open(p,'w',encoding='utf8').write(s); print('ok')
