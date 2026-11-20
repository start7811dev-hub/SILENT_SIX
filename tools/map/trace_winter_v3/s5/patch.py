# -*- coding: utf-8 -*-
import io,json
p='public/index.html'; s=io.open(p,encoding='utf8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:60],s.count(a)); s=s.replace(a,b)
D=json.load(open('/tmp/s5/map.json')); MP=D['MAP']
G=[{'wps':[[27,7]],'tower':True,'lamp':True,'faces':[2.5,3.14,2.0],'ft':5},{'wps':[[10,8]],'faces':[0,1.57],'ft':8},{'wps':[[18,8]],'faces':[3.14,1.57],'ft':8},
   {'wps':[[9,13],[16,13]]},{'wps':[[3,19],[18,19]]},{'wps':[[3,23],[23,23]]},{'wps':[[24,11],[24,16]]},{'wps':[[8,2],[26,2]]},{'wps':[[7,8],[7,15]]},{'wps':[[28,10],[28,24]]}]
for g in G:
    if g.get('tower'): continue
    for x,y in g['wps']: assert MP[y][x]=='.',(x,y,MP[y][x])
for x,y in [(12,28),(13,28),(14,28),(13,11),(2,23),(24,27),(5,7),(10,23),(14,23)]: assert MP[y][x]=='.',(x,y,MP[y][x])
a=s.index(u" {t:'산타의 썰매'"); b=s.index("var WIDX=[];")
W5=u""" {t:'산타의 썰매',copy:'이륙은<br>없다.',pre:'03:30, 사설 비행장. 추적기가 여기서 멈췄다. 격납고의 전용기가 뜨기 전에 화물을 확보한다. 격납고는 잠겨 있다. 관제탑, 급수탑, 연료 밸브 셋 중 둘을 해야 열린다. 시간은 5분.',post:['화물칸은 비어 있었다.', '산타는 처음부터 제6과가 자기를 쫓게 만들었다. 카드에는 다음에 만날 좌표가 적혀 있다.'],bc:'nogun',img:'a_raven_6.jpg',endImg:'w5_end_a.jpg',par:420,env:{limit:300},tips:["셋이 갈라진다. <b>관제탑</b>은 글리치(시간 +2분), <b>급수탑</b>은 바이퍼(탐조등 정지), <b>연료 밸브</b>는 레이븐(시간 +1분). 셋 중 둘이면 격납고가 열린다.", "<b>탐조등</b>은 계류장을 훑는다. 차량과 컨테이너 뒤에만 그늘이 진다.", "화물칸을 열면 전용기가 움직인다. <b>2분</b> 안에 셋 다 들어온 곳으로 나간다."],
  m:{bgs:['bgw5_0.jpg','bgw5_1.jpg'],bg:'bgw5_0.jpg',sk:0.3,zm:1.5,wake:120,need:2,opaque:'#HJBT',hts:{'#': 40, 'H': 44, 'J': 34, 'B': 30, 'T': 90, 'X': 10, 'C': 12},proj:%s,MAP:%s,
  ops:[{id:'raven',x:12,y:28},{id:'viper',x:13,y:28},{id:'glitch',x:14,y:28}],exit:[[12, 28], [13, 28], [14, 28]],objective:{x:13,y:10,use:[13,11],label:'산타의 화물',verb:'화물칸 열기',time:3},
  lock:'격납고가 잠겨 있다. 셋 중 둘부터.',
  subs:[{k:'twr',x:1,y:23,use:[2,23],by:'glitch',label:'관제탑',verb:'이륙 지연',btn:'관제탑',time:3,bonus:120,done:'이륙 허가가 꼬였다. 2분 벌었다.'},{k:'wt',x:25,y:26,w:2,h:2,use:[24,27],by:'viper',label:'급수탑',verb:'급수탑 점거',btn:'급수탑',time:3,freeze:0,done:'바이퍼가 위에서 본다. 탐조등이 멈췄다.'},{k:'valve',x:4,y:6,use:[5,7],by:'raven',label:'연료 밸브',verb:'밸브 잠그기',btn:'밸브',time:3,bonus:60,done:'급유가 멈췄다. 1분 벌었다.'}],
  evac:{limit:120,late:'전용기가 떴다.',note:'전용기가 움직인다.',sw:{bit:1,clr:%s,shut:%s},posts:[{post:[10,23],face:-1.57},{post:[14,23],face:-1.57}],gates:[{n:'들어온 곳',cells:[[12,28],[13,28],[14,28]],post:[13,26],face:-1.57,bar:['p_w1_bar_x.png',12,28,2,1]}]},
  santa:{img:'p_w_santa.png',x:14.5,y:4.5,up:36,t:20},
  dlg:{cast:{santa:'d_w_santa_5.webp'},
   start:[['hq','03시 30분, 사설 비행장이다. 추적기가 여기서 멈췄다. 격납고의 전용기가 뜨기 전에 화물을 확보한다. 시간은 5분.'],['viper','셋이나 보내다니, 오늘은 진심이네. 난 저 급수탑이 마음에 들어. 계류장이 한눈에 보이겠어.',2],['glitch','난 관제탑! 이륙 허가만 꼬아 놓으면 2분은 더 벌 수 있어. …올라가는 길에 사람만 없으면.',0],['raven','난 격납고로 간다. 연료 밸브도 가는 길에 잠글 수 있으면 잠그고.',0],['viper','레이븐, 아까 성당에서부터 말이 없네. 그 여자 때문이야?',0],['raven','…끝나고 얘기해. 지금은 비행기부터 잡는다.',1]],
   mid:[['santa','셋이나 왔네? 이 정도면 영광인데.'],['glitch','으악, 또 들어왔어! 회선을 세 번이나 바꿨는데 어떻게…!',1],['santa','글리치, 그 암호 체계는 내가 짠 거야. 넌 그 위에 색칠만 했고.'],['raven','그만해. 거기서 기다려. 직접 물어볼 게 있으니까.',1],['santa','기다리는 건 내 일이 아니야, 레이븐. 그건 늘 네 일이었지.']],
   obj:[['raven','…비어 있어. 리본 묶은 빈 상자 하나, 카드 한 장. 그게 전부야.',1],['santa','선물은 벌써 받았잖아. 오늘 밤 너희가 턴 다섯 곳. 그게 내 선물이야.'],['glitch','비행기가 움직여! 유도로로 나가고 있어!',1],['viper','레이븐, 여기 더 있으면 갇혀. 나가자!',1]],
   end:[['glitch','마켓, 조차장, 호수, 성당, 비행장… 잠깐, 이거 헬리오스 배달망 전부야. 하룻밤에 다 드러났어. 우리가 쫓아다닌 덕분에.',2],['viper','쫓은 게 아니라 끌려다닌 거네. 처음부터 끝까지.',0],['raven','카드에 좌표가 있어. 다음에 만날 자리야. …그리고 이 글씨.',0],['viper','아는 글씨야?',1],['raven','현장 수칙 초판. 6과에 처음 들어왔을 때 받은 그 수첩이랑 같은 손이야. 1기 리더.',1],['raven','…메리 크리스마스, 선배.',2]]},
  guards:%s}}];
""" % (json.dumps(D['proj']),json.dumps(MP),json.dumps(D['body']),json.dumps(D['taxi']),json.dumps(G))
s=s[:a]+W5+s[b:]
rep("function subsDone(){if(!M.subs)return true;for(var i=0;i<M.subs.length;i++)if(!S.subs[i])return false;return true;}","function subsDone(){if(!M.subs)return true;var n=0;for(var i=0;i<M.subs.length;i++)if(S.subs[i])n++;return n>=(M.need||M.subs.length);}")
rep("if(sb.quiet)S.bellT=S.t+sb.quiet;","if(sb.quiet)S.bellT=S.t+sb.quiet;if(sb.bonus)S.lim=(S.lim||0)+sb.bonus;")
rep("if(e.limit){var left=e.limit-S.t;","if(e.limit){var left=e.limit+(S.lim||0)-S.t;")
rep("scene([{k:'MISSION CLEAR // '+M.title,h:M.post[0],p:M.post[1],img:M.img,","scene([{k:'MISSION CLEAR // '+M.title,h:M.post[0],p:M.post[1],img:M.endImg||M.img,")
rep("m.bc=c.bc;m.par=c.par;","m.bc=c.bc;m.par=c.par;m.endImg=c.endImg||'';")
rep("var VERSION='0.30.0';","var VERSION='0.31.0';")
io.open(p,'w',encoding='utf8').write(s)
p='tools/check_w1.js'; s=io.open(p,encoding='utf8').read()
rep("for(const op of [0,1]){if(sb.by&&M.ops[op].id!==sb.by)continue;","for(let op=0;op<M.ops.length;op++){if(sb.by&&M.ops[op].id!==sb.by)continue;")
a=s.index("const snap=snaps(170);"); b=s.index("else console.log('   경로 없음'",a)
s=s[:a]+"""const snap=snaps(170);const rs=M.ops.map((o,k)=>{LOUD=k===0&&!!(M.evac.escort&&M.evac.escort.loud);const r=search(snap,ci(S.ops[k]),E,1);LOUD=false;return r;});
    if(rs.every(Boolean)){const tm=Math.max(...rs.map(r=>r.t));if(M.evac.escort)rs.forEach((r,k)=>{if(r.t<tm-0.5){LOUD=k===0&&!!M.evac.escort.loud;rs[k]=search(snap,ci(S.ops[k]),E,1,tm-0.25)||r;LOUD=false;}});
      const st=[].concat(...rs.map((r,k)=>r.steps.map(x=>({...x,op:k})))).sort((a,b)=>a.t-b.t);const t0=S.t;let i=0;const end=t0+Math.max(...rs.map(r=>r.t))+3;
      while(S.t<end&&!S.over){while(i<st.length&&t0+st[i].t<=S.t+1e-6){const q=st[i++];S.ops[q.op].queue=[{type:'move',x:q.x,y:q.y}];S.ops[q.op].cur=null;}update(DT);}}
    """+s[b:].replace("console.log('   경로 없음',!!r0,!!r1);","console.log('   경로 없음',rs.map(Boolean).join());")
io.open(p,'w',encoding='utf8').write(s); print('ok')
