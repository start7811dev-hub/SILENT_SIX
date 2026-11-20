# -*- coding: utf-8 -*-
import io,json
p='public/index.html'; s=io.open(p,encoding='utf8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:60],s.count(a)); s=s.replace(a,b)
D=json.load(open('/tmp/s3/map.json'))
a=s.index(" {t:'얼음 위의 선물'"); b=s.index(" {t:'자정 미사'")
W3=u""" {t:'얼음 위의 선물',copy:'숨을 곳이<br>없는 밤.',pre:'22:30, 얼어붙은 호수. 산타의 상자를 본 증인이 건너편 보트하우스에 갇혀 있다. 다쳤고, 오래 못 버틴다. 구급 가방은 얼음 위 붉은 오두막에 있다. 부두의 안테나를 끊으면 탐조등이 멈춘다. 얼음 위는 눈보라가 칠 때 건넌다.',post:['증인은 제 발로 걸어 나왔다.', '산타는 헬리오스 사람이 아니라 제6과 출신이다. 다음은 자정, 대성당.'],bc:'onesnipe',img:'a_viper_5.jpg',par:540,env:{blizzard:[26,9]},tips:["<b>눈보라</b>: 26초마다 9초 동안 모두의 시야가 절반 아래로 줄어든다. 얼음 위는 그때 오두막에서 오두막으로 건넌다.", "<b>탐조등</b>은 얼음 위를 훑는다. 오두막 뒤에만 그늘이 진다. 바이퍼가 <b>안테나</b>를 쏘면 탐조등이 한 방향으로 멈춘다.", "<b>구급 가방</b>은 얼음 한가운데 붉은 오두막에 있다. 닥이 챙겨야 증인을 치료할 수 있다.", "치료한 뒤에는 <b>증인이 닥을 따라온다</b>. 증인은 앉지 못해서 멀리서도 보인다."],
  m:{bg:'bgw3.jpg',sk:0.3,zm:1.5,wake:120,opaque:'#HJX',hts:{'#': 40, 'H': 44, 'J': 34, 'T': 60, 'X': 20, 'C': 12},proj:%s,MAP:%s,
  ops:[{id:'doc',x:21,y:28},{id:'viper',x:22,y:28}],exit:[[21, 28], [22, 28]],objective:{x:4,y:3,use:[4,4],label:'증인',verb:'응급 처치',time:4,by:'doc'},
  lock:'맨손으로는 못 걷게 한다. 구급 가방과 안테나부터.',
  subs:[{k:'ant',x:26,y:2,w:2,h:2,shoot:true,by:'viper',label:'안테나',verb:'안테나 저격',btn:'안테나',freeze:0,done:'무전이 끊겼다. 탐조등이 멈췄다.'},{k:'bag',x:10,y:12,w:2,h:2,use:[10,14],by:'doc',label:'구급 가방',verb:'구급 가방 챙기기',btn:'가방',time:2,done:'구급 가방을 챙겼다.'}],
  evac:{note:'증인이 일어섰다.',escort:{x:4,y:3,img:'p_w3_witness.png',loud:true},posts:[{post:[8,8],face:-2.36}],gates:[{n:'들어온 숲길',cells:[[21,28],[22,28]],post:[21,26],face:-1.57,bar:['p_w1_bar_x.png',21,28,2,1]}]},
  santa:{img:'p_w_santa.png',x:24.5,y:3.5,up:30,t:20},
  dlg:{cast:{santa:'d_w_santa_3.webp',witness:['d_w3_witness_0.webp','d_w3_witness_1.webp']},
   start:[['hq','22시 30분, 호수다. 산타의 상자를 직접 본 사람이 보트하우스에 갇혀 있다. 다쳤고, 오래 못 버틴다.'],['doc','다쳤다고? 그럼 얘기 끝났네. 내가 들어가서 걷게 만들어 올게.',1],['viper','얼음 위는 숨을 데가 없는데. 오두막 몇 채가 전부야. 건너다 걸리면 그대로 표적이지.',0],['doc','그래서 네가 있는 거잖아. 부두 안테나부터 끊어 줘. 무전만 죽이면 탐조등도 멍청해져.',0],['viper','한 발이면 돼. …근데 닥, 구급 가방은?',2],['doc','아, 그게 문제야. 급하게 나오느라 큰 가방을 못 챙겼어. 저 붉은 오두막에 하나 있을 거야.',2]],
   mid:[['santa','그 사람은 왜 살리려고? 내 얘기가 그렇게 듣고 싶어?'],['viper','어머, 목소리 좋네. 직접 와서 들려주지 그래?',2],['santa','바이퍼구나. 넌 여전히 쏘기 전에 말이 많아.'],['viper','…나 알아?',1],['doc','바이퍼, 대꾸하지 마. 저 사람, 우리 의무 기록까지 읽은 말투야.',1]],
   obj:[['witness','그 여자… 헬리오스 사람이 아니야. 걷는 거, 숨는 거, 전부 당신들이랑 똑같았어.',0],['doc','천천히 말해요. 우리랑 똑같다는 게 무슨 뜻이에요?',1],['witness','6과. 그 여자가 자기 입으로 그랬어. "난 거기서 나왔다"고.',1],['santa','입이 가벼운 사람은 오래 못 사는데. 조심히 데려가, 닥.']],
   end:[['viper','6과 출신이라… 그럼 우리 선배네. 인사라도 할 걸 그랬나.',2],['doc','웃을 일이 아니야. 선배가 왜 헬리오스 물건을 나르고 있는 건데.',1],['viper','글쎄. 배신했거나, 배신한 척하거나. 둘 중 하나겠지.',0],['doc','증인이 그러는데, 세 번째 상자는 벌써 떠났대. 자정 미사가 열리는 대성당으로.',0]]},
  guards:[{wps:[[22,4]],tower:true,lamp:true,faces:[1.9,2.5,3.0],ft:5},{wps:[[26,7]],faces:[1.57,2.6],ft:6},{wps:[[6,9],[6,21]]},{wps:[[8,6],[20,6]]},{wps:[[8,8]],faces:[0.78,1.9,-0.3],ft:5},{wps:[[12,21],[20,12]]},{wps:[[1,8],[1,20]]},{wps:[[23,10],[23,20]]}]}},
""" % (json.dumps(D['proj']),json.dumps(D['MAP']))
s=s[:a]+W3+s[b:]
# 저격으로 끝내는 중간 목표
rep("  else if(a.type==='sub'){var sb=M.subs[a.i];if(!sb.use||S.subs[a.i]){o.cur=null;return;}o.path=findPath(fl(o.x),fl(o.y),sb.use[0],sb.use[1])||[];a.t=sb.time;}",
    "  else if(a.type==='sub'){var sb=M.subs[a.i];if(S.subs[a.i]||(sb.by&&sb.by!==o.id)){if(sb.by&&sb.by!==o.id)say(sb.label+'은 '+OPD[sb.by].n+'만 할 수 있다');o.cur=null;return;}if(sb.shoot){o.path=[];a.t=AIM;}else{o.path=findPath(fl(o.x),fl(o.y),sb.use[0],sb.use[1])||[];a.t=sb.time;}}")
rep("  }else if(a&&a.type==='sub'){\n    if(!o.path.length){",
"""  }else if(a&&a.type==='sub'&&M.subs[a.i].shoot){
    var sh=M.subs[a.i];tx=sh.x+(sh.w||1)/2;ty=sh.y+(sh.h||1)/2;
    if(o.ammo<=0){o.cur=null;o.aim=0;say('탄창이 비었다.');}
    else if(hyp(tx-o.x,ty-o.y)>SNIPE||!los(o.x,o.y,tx,ty,true))approach(o,a,tx,ty,SNIPE-0.6,true,true,dt);
    else{o.path=[];o.ang=Math.atan2(ty-o.y,tx-o.x);a.t-=dt;o.fx='plant';o.fxt=0.2;
      if(a.t<=0){o.ammo--;S.shots.push({x0:o.x,y0:o.y,x1:tx,y1:ty,e:true,t:0.3});S.noise.push({x:o.x,y:o.y,t:0.6,r:2});snd('sup');alertNear(o.x,o.y,2,o.x,o.y,null);o.cur=null;subDone(a.i);}}
  }else if(a&&a.type==='sub'){
    if(!o.path.length){""")
rep("  if(sb.dark)S.dark=sb.dark;applySw(sb.sw);snd('ok');","  if(sb.dark)S.dark=sb.dark;applySw(sb.sw);if(sb.freeze!=null){var fg=S.guards[sb.freeze];fg.faces=[fg.faces[fg.faces.length-1]];fg.fi=0;}snd('ok');")
rep("if(sb.use&&!S.subs[si])h+='<button class=\"ab\" data-a=\"sub\"","if((sb.use||sb.shoot)&&!S.subs[si]&&(!sb.by||sb.by===A.id))h+='<button class=\"ab\" data-a=\"sub\"")
rep("if(sb.use&&!S.subs[si]&&cx>=sb.x&&cx<sb.x+(sb.w||1)&&cy>=sb.y&&cy<sb.y+(sb.h||1)){issue(A,{type:'sub',i:si});return true;}","if((sb.use||sb.shoot)&&!S.subs[si]&&cx>=sb.x&&cx<sb.x+(sb.w||1)&&cy>=sb.y&&cy<sb.y+(sb.h||1)){issue(A,{type:'sub',i:si});return true;}")
rep("M.subs.forEach(function(sb,si){if(!sb.use||S.subs[si])return;glow('#ffd27a',10);","M.subs.forEach(function(sb,si){if(!(sb.use||sb.shoot)||S.subs[si])return;glow('#ffd27a',10);")
rep("M.subs.forEach(function(sb,si){if(!sb.use||S.subs[si])return;p=PF(","M.subs.forEach(function(sb,si){if(!(sb.use||sb.shoot)||S.subs[si])return;p=PF(")
rep("else if(a.type==='sub')label(M.subs[a.i].verb+' 중 '+Math.ceil(a.t)","else if(a.type==='sub')label(M.subs[a.i].shoot?'조준':M.subs[a.i].verb+' 중 '+Math.ceil(a.t)")
# 호위 · 추가 출동
rep("  wallCv=null;say((M.evac.note||'대피 방송.')+' 열린 곳은 '+G[S.exitI].n+'.');",
"""  (M.evac.posts||[]).forEach(function(pt){var best=null,bd=1e9;S.guards.forEach(function(g){if(g.down||g.fixed||g.boss||used[g.id])return;var d=hyp(g.x-pt.post[0],g.y-pt.post[1]);if(d<bd){bd=d;best=g;}});
    if(best){used[best.id]=1;best.wps=[pt.post];best.faces=[pt.face,pt.face+0.8,pt.face-0.8];best.fi=0;best.ft=best.fd=2.5;best.state='patrol';best.rush=true;best.off=3;best.meter=0;best.path=findPath(fl(best.x),fl(best.y),pt.post[0],pt.post[1])||[];}});
  if(M.evac.escort){S.hostage={x:M.evac.escort.x+0.5,y:M.evac.escort.y+0.5,free:true};S.trail=[];}
  wallCv=null;say((M.evac.note||'대피 방송.')+(G.length>1?' 열린 곳은 '+G[S.exitI].n+'.':' '+G[S.exitI].n+'로 데리고 나간다.'));""")
rep("      if(inExit(r)&&hyp(h.x-r.x,h.y-r.y)<2.2)S.over={win:true};","      if(inExit(r)&&hyp(h.x-r.x,h.y-r.y)<2.2&&(!M.evac||S.ops.every(inExit)))S.over={win:true};")
rep("  var HR=g.cam?CAMR:CRANGE*(g.tower?1.4:1);","  var HR=g.cam?CAMR:(M.evac&&M.evac.escort&&M.evac.escort.loud?RANGE:CRANGE)*(g.tower?1.4:1);")
rep("if(a===1)shadow(f);var hi=IM['hostage.png'];ctx.globalAlpha=a;","if(a===1)shadow(f);if(M.evac&&M.evac.escort){loadImg(M.evac.escort.img);var wi=IM[M.evac.escort.img];ctx.globalAlpha=a;if(ok(wi))ctx.drawImage(wi,f[0]-12,f[1]-42,24,44);ctx.globalAlpha=1;return;}var hi=IM['hostage.png'];ctx.globalAlpha=a;")
rep("t=(M.evac.limit?'남은 시간 '+mmss(Math.max(0,Math.ceil(M.evac.limit-(S.t-S.evT))))+' · ':'대피 방송 · ')+'열린 곳은 '+M.evac.gates[S.exitI].n;hot=true;","if(M.evac.gates.length>1||M.evac.limit){t=(M.evac.limit?'남은 시간 '+mmss(Math.max(0,Math.ceil(M.evac.limit-(S.t-S.evT))))+' · ':'대피 방송 · ')+'열린 곳은 '+M.evac.gates[S.exitI].n;hot=true;}")
# 대화: 표정별 캐스트
rep("DCAST={hq:{n:'지휘관',c:'#c9d2dc'},santa:{n:'산타',c:'#e0364f',side:'l'}};","DCAST={hq:{n:'지휘관',c:'#c9d2dc'},santa:{n:'산타',c:'#e0364f',side:'l'},witness:{n:'증인',c:'#ff9a3c',side:'l'}};")
rep("img:cast[k]||(DPORT[k]?'d_'+k+'_'+(e||0)+'.webp':''),card:false};}","img:(cast[k]&&cast[k].pop?cast[k][e||0]:cast[k])||(DPORT[k]?'d_'+k+'_'+(e||0)+'.webp':''),card:false};}")
rep("var VERSION='0.28.0';","var VERSION='0.29.0';")
io.open(p,'w',encoding='utf8').write(s); print('ok')
