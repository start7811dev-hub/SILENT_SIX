# -*- coding: utf-8 -*-
import io,json
p='public/index.html'; s=io.open(p,encoding='utf8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:60],s.count(a)); s=s.replace(a,b)
D=json.load(open('/tmp/s2/map.json'))
a=s.index(" {t:'화차 44호'"); b=s.index(" {t:'얼음 위의 선물'")
W2=u""" {t:'화차 44호',copy:'노크는<br>한 번만 한다.',pre:'20:10, 화물 조차장. 카드에 적힌 그대로다. 화차 44호에 두 번째 상자가 실려 있다. 사무소의 화물 대장을 봐야 어느 화차인지 알 수 있고, 신호소에서 선로를 돌려야 화차 줄 사이에 틈이 생긴다. 조명탑 두 기가 선로 위를 훑는다.',post:['두 번째 상자를 들고 조차장을 빠져나왔다.', '상자의 숫자는 제6과 명단의 나머지 절반이다. 다음은 22:30, 호수 보트하우스.'],bc:'noload',img:'a_brick_5.jpg',par:480,tips:["화차 줄은 <b>화차 사이 틈</b>으로만 건넌다. 신호소에서 <b>선로 전환기</b>를 돌리면 가운데 줄이 밀려 새 틈이 생기고 오른쪽 끝은 막힌다.", "<b>조명탑</b>은 화차 너머까지 내려다본다. 글리치가 해킹하면 25초 동안 꺼진다.", "<b>침목 더미</b> 두 곳은 브릭이 부수고 지나갈 수 있다. 시끄럽다.", "폭약이 터지면 <b>3분</b> 안에 나가야 한다. 열린 출구는 그때 알려 준다."],
  m:{bgs:['bgw2_0.jpg','bgw2_1.jpg','bgw2_2.jpg','bgw2_3.jpg'],bg:'bgw2_0.jpg',sk:0.3,zm:1.5,wake:120,opaque:'#BJX',hts:{'#': 38, 'B': 40, 'J': 34, 'T': 90, 'X': 30, 'C': 12, 'W': 16},proj:%s,MAP:%s,
  ops:[{id:'brick',x:12,y:28},{id:'glitch',x:13,y:28}],exit:[[12, 28], [13, 28]],objective:{x:17,y:7,use:[17,6],label:'화차 44호',verb:'폭약 설치',time:4},
  lock:'어느 화차인지 모른다. 화물 대장과 선로 전환기부터.',
  subs:[{k:'sw',x:2,y:10,use:[3,10],label:'선로 전환기',verb:'선로 전환',btn:'전환기',time:3,sw:{bit:1,clr:%s,shut:%s},done:'화차 줄이 밀렸다. 가운데에 틈이 생겼다.'},{k:'ledger',x:2,y:17,use:[3,17],label:'화물 대장',verb:'화물 대장 확인',btn:'대장',time:3,done:'44호는 노란 띠를 두른 파란 화차다.'}],
  evac:{limit:180,late:'증원이 조차장을 에워쌌다.',note:'기관차가 줄을 끌고 나간다.',sw:{bit:2,clr:%s,shut:[]},gates:[{n:'들어온 문',cells:[[12,28],[13,28]],post:[13,26],face:-1.57,bar:['p_w1_bar_x.png',12,28,2,1]},{n:'남쪽 선로 출구',cells:[[28,20],[28,21]],post:[27,20],face:3.14,bar:['p_w1_bar_y.png',28,20,1,2]},{n:'가운데 선로 출구',cells:[[28,15],[28,16]],post:[27,16],face:3.14,bar:['p_w1_bar_y.png',28,15,1,2]}]},
  santa:{img:'p_w_santa.png',x:17.5,y:7.5,up:26,t:20},
  dlg:{cast:{santa:'d_w_santa_2.webp'},
   start:[['hq','20시 10분, 화물 조차장이다. 카드에 적힌 그대로야. 화차 44호에 두 번째 상자가 실려 있다.'],['brick','화차가 몇 량인데? 하나하나 다 열어 볼 수는 없잖아.',1],['glitch','사무소에 화물 대장이 있을 거야. 그거 보면 44호가 어느 줄인지 바로 나와. 아, 근데 조명탑이 두 개나 있네… 저건 내가 끌게.',0],['brick','좋아. 그럼 넌 불 끄고, 난 문 딴다. 간단하네!',0],['glitch','언니 "딴다"가 폭약인 거, 나만 불안해?',1],['brick','걱정 마. 노크는 딱 한 번만 할게.',2]],
   mid:[['santa','브릭이 먼저 담을 넘고, 글리치는 신호소부터 찾았겠지? 맞지?'],['glitch','어… 어떻게 알았어?! 지금 우리 보고 있어?',1],['santa','볼 필요가 없어. 너희는 늘 그 순서로 움직이니까.'],['brick','야, 너 누구야. 얼굴 좀 보고 얘기하자.',1],['santa','얼굴은 선물 다 받고 나서. 착하게 굴어야지?']],
   obj:[['santa','어머, 정말 터뜨렸네. 그럼 3분 줄게. 기차는 시간 맞춰 떠나거든.'],['glitch','브릭! 기관차가 움직여! 출구에 사람이 붙고 있어!',1],['brick','막히면 뚫으면 되지! 뒤로 붙어!',2]],
   end:[['glitch','잠깐만… 마켓에서 나온 종이랑 이 상자 걸 합치니까 풀려. 이거 암호가 아니라 사번이야.',2],['brick','사번? 누구 건데.',0],['glitch','…우리 거. 6과 사번이야. 언니 것도 있어.',1],['brick','뭐? 지난번에 팔린 명단은 절반이라며.',1],['glitch','응. 이게 나머지 절반이야. 그리고 대장에 다음 배송지가 적혀 있어. 22시 30분, 호수 보트하우스.',0]]},
  guards:[{wps:[[3,5]],tower:true,lamp:true,faces:[0.9,1.57],ft:6},{wps:[[27,3]],tower:true,lamp:true,faces:[2.4,1.57],ft:6},{wps:[[5,9],[5,21]]},{wps:[[9,16],[27,16]]},{wps:[[8,22],[27,22]]},{wps:[[27,19],[8,19]]},{wps:[[18,25],[27,25]]},{wps:[[9,3],[24,3]]},{wps:[[9,9],[27,9]]},{wps:[[5,11]],faces:[1.57,-1.57],ft:5}]}},
""" % (json.dumps(D['proj']),json.dumps(D['MAP']),json.dumps(D['sw1']['clr']),json.dumps(D['sw1']['shut']),json.dumps(D['sw2']['clr']))
s=s[:a]+W2+s[b:]
# 배경 상태
rep("function tall(x,y){","function bgName(){return M.bgs?M.bgs[(S&&S.bgk)||0]:M.bg;}\nfunction tall(x,y){")
rep("  var bg=IM[M.bg];if(wallCv||!ok(bg))return;","  var bg=IM[bgName()];if(wallCv||!ok(bg))return;")
rep("now=Date.now(),bg=IM[M.bg],md=A.mode","now=Date.now(),bg=IM[bgName()],md=A.mode")
rep("  loadImg(M.bg);userZoom=false;","  loadImg(M.bg);if(M.bgs)M.bgs.forEach(loadImg);userZoom=false;")
rep("if(S&&S.shut&&S.shut[y*COLS+x])return '#';","if(S&&S.shut&&S.shut[y*COLS+x])return '#';if(S&&S.clr&&S.clr[y*COLS+x])return '.';")
rep("var st={t:0,subs:[],shut:{},","var st={t:0,subs:[],shut:{},clr:{},bgk:0,evT:0,")
rep("function subsDone(){","function applySw(w){if(!w)return;S.bgk|=w.bit;(w.clr||[]).forEach(function(c){S.clr[c[1]*COLS+c[0]]=1;delete S.shut[c[1]*COLS+c[0]];});(w.shut||[]).forEach(function(c){S.shut[c[1]*COLS+c[0]]=1;delete S.clr[c[1]*COLS+c[0]];});wallCv=null;}\nfunction subsDone(){")
rep("  if(sb.dark)S.dark=sb.dark;snd('ok');","  if(sb.dark)S.dark=sb.dark;applySw(sb.sw);snd('ok');")
rep("say(subsDone()?'울타리 문이 열렸다. 상자는 트리 아래.':sb.done||sb.label+' 완료');","say(sb.done||sb.label+' 완료');")
rep("var G=M.evac.gates,i,used={};S.ev=true;","var G=M.evac.gates,i,used={};S.ev=true;S.evT=S.t;applySw(M.evac.sw);")
rep("  wallCv=null;say('대피 방송. 열린 곳은 '+G[S.exitI].n+'.');","  wallCv=null;say((M.evac.note||'대피 방송.')+' 열린 곳은 '+G[S.exitI].n+'.');")
rep("if(S.ev){t='대피 방송 · 열린 곳은 '+M.evac.gates[S.exitI].n;hot=true;}","if(S.ev){t=(M.evac.limit?'남은 시간 '+mmss(Math.max(0,Math.ceil(M.evac.limit-(S.t-S.evT))))+' · ':'대피 방송 · ')+'열린 곳은 '+M.evac.gates[S.exitI].n;hot=true;if(M.evac.limit&&S.t-S.evT>=M.evac.limit)fail(M.evac.late||'너무 늦었다.');}")
rep("subs:[{k:'gen',x:26,y:3,w:2,h:2,use:[25,4],label:'발전기',verb:'발전기 끄기',btn:'발전기',time:3,dark:0.75,done:'조명이 꺼졌다. 경비의 시야가 줄었다.'}","subs:[{k:'gen',x:26,y:3,w:2,h:2,use:[25,4],label:'발전기',verb:'발전기 끄기',btn:'발전기',time:3,dark:0.75,done:'조명이 꺼졌다. 경비의 시야가 줄었다.'}")
rep("var VERSION='0.27.2';","var VERSION='0.28.0';")
io.open(p,'w',encoding='utf8').write(s); print('ok')
