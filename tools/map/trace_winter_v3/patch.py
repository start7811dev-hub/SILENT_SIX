# -*- coding: utf-8 -*-
import io,json,re
p='public/index.html'; s=io.open(p,encoding='utf8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:60],s.count(a)); s=s.replace(a,b)
D=json.load(open('/tmp/s1/map.json'))
# ---- 1. 데이터 ----
a=s.index(" {t:'첫 번째 상자'"); b=s.index(" {t:'화차 44호'")
W1=u""" {t:'첫 번째 상자',copy:'선물은<br>돈이 아니었다.',pre:'18:40, 구시가 성탄 마켓. 헬리오스의 배달 책임자, 호출명 산타가 오늘 밤 상자 다섯 개를 돌린다. 첫 번째 상자는 광장 한가운데 트리 아래 있다. 울타리는 잠겨 있다. 발전기를 끄고 무전병을 재워야 열린다. 민간인이 많다. 아무도 죽이지 않는다.',post:['상자를 들고 마켓을 빠져나왔다.', '상자에 든 것은 돈이 아니라 암호로 적힌 명단이다. 다음은 20:10, 화차 44호.'],bc:'nokill',img:'a_raven_5.jpg',par:420,tips:["<b>울타리</b>는 발전기를 끄고 무전병을 재워야 열린다. 순서는 상관없다.", "<b>사복 경비</b> 셋 중 한 명이 무전병이다. 3칸 안으로 다가가야 누구인지 보인다. 사복 경비는 변장도 알아본다.", "상자를 집으면 <b>대피 방송</b>이 나오고 문 넷 중 셋이 막힌다. 열린 문은 그때 알려 준다.", "골목 안쪽의 빈 자리는 숨는 자리다. 쓰러뜨린 경비는 거기 숨긴다."],
  m:{bg:'bgw1.jpg',sk:0.3,zm:1.5,wake:120,opaque:'#BHTJX',hts:{'#': 38, 'B': 30, 'H': 44, 'T': 70, 'X': 70, 'J': 32, 'C': 12, 'F': 14, 'G': 22},proj:%s,MAP:%s,
  ops:[{id:'raven',x:13,y:30},{id:'mirage',x:14,y:30}],exit:[[13, 30], [14, 30]],objective:{x:16,y:13,use:[16,12],label:'첫 번째 상자',verb:'회수',time:3},
  lock:'울타리가 잠겨 있다. 발전기와 무전병부터.',
  subs:[{k:'gen',x:26,y:3,w:2,h:2,use:[25,4],label:'발전기',verb:'발전기 끄기',time:3,dark:0.75,done:'조명이 꺼졌다. 경비의 시야가 줄었다.'},{k:'radio',label:'무전병',verb:'무전병 재우기',done:'무전이 끊겼다.'}],
  evac:{gates:[{n:'왼쪽 아래 문',cells:[[13,30],[14,30]],shut:[[13,30],[14,30],[13,29],[14,29]],post:[13,28],face:-1.57,bar:['p_w1_bar_x.png',13,29,2,1]},{n:'왼쪽 위 문',cells:[[0,15],[0,16]],shut:[[0,15],[0,16]],post:[2,15],face:0,bar:['p_w1_bar_y.png',0,15,1,2]},{n:'오른쪽 위 문',cells:[[15,0],[16,0]],shut:[[15,0],[16,0]],post:[15,2],face:1.57,bar:['p_w1_bar_x.png',15,0,2,1]},{n:'오른쪽 아래 문',cells:[[30,14],[30,15]],shut:[[30,14],[30,15]],post:[28,14],face:3.14,bar:['p_w1_bar_y.png',30,14,1,2]}]},
  santa:{img:'p_w_santa.png',x:4.5,y:4.5,up:34,t:20},
  dlg:{cast:{santa:'d_w_santa_1.webp',mirage:'d_w1_mirage.webp'},
   start:[['hq','18시 40분, 구시가 성탄 마켓이다. 헬리오스 배달 책임자, 호출명은 "산타". 오늘 밤 상자 다섯 개를 돌릴 거고, 첫 번째가 저 트리 밑에 있다.'],['raven','트리 둘레에 울타리가 쳐져 있네. 저건 어떻게 열지?'],['mirage','그게 좀 골치 아파. 조명이 저렇게 환하면 넘다가 바로 걸릴 거고, 사복 경비 셋 중에 누군가는 무전기를 쥐고 있거든.'],['raven','그럼 발전기부터 꺼서 불을 죽이고, 무전 쥔 놈을 찾아서 재워야겠군. 어느 쪽이 먼저든 상관없어.'],['mirage','난 점원인 척 들어갈게. 앞치마가 생각보다 잘 어울리더라고, 나.'],['raven','장난은 거기까지. 민간인이 너무 많아. 총은 절대 꺼내지 마.']],
   mid:[['santa','어머, 이 주파수… 아직도 그대로 쓰고 있네?'],['raven','…누구야, 너.'],['santa','선물 나눠 주는 사람이지. 물론 착한 아이들한테만.'],['mirage','잠깐, 지휘관. 이거 우리 비밀 회선인데… 외부에서 어떻게 들어온 거지?'],['santa','글쎄. 꼭 밖에서 들어왔다는 법은 없잖아?']],
   obj:[['santa','집었구나? 그럼 이제 뛰어야지. 리본 풀 시간까지는 안 줄 거야.'],['raven','젠장, 출구가 막히고 있어! 미라주, 열린 곳부터 찾아!']],
   end:[['mirage','어…? 돈이 아니야. 종이 딱 한 장인데, 숫자만 세 줄 적혀 있어.'],['raven','숫자? …받는 사람은 누구로 돼 있어?'],['mirage','시청 도시안전국장. 공무원한테 돈도 아니고 종이 쪼가리를 보낸다고? 이상하잖아.'],['mirage','잠깐만, 바닥에 카드가 한 장 더 있어. "다음 선물은 20시 10분, 화차 44호"…'],['raven','…이건 국장한테 쓴 게 아니야. 우리 보라고 남긴 거지.']]},
  guards:[{wps:[[13,11]],faces:[0,-1.57],ft:6},{wps:[[19,11]],faces:[3.14,1.57],ft:6},{wps:[[23,9],[23,16]]},{wps:[[23,16],[23,9]]},{wps:[[1,2],[1,21]]},{wps:[[9,1],[22,1]]},{wps:[[7,9],[7,21]],plain:true,keen:true},{wps:[[9,9],[12,9],[12,12]],plain:true,keen:true},{wps:[[9,23],[11,23],[11,19]],plain:true,keen:true},{wps:[[29,9]],faces:[1.57,3.14],ft:5},{wps:[[29,13]],faces:[-1.57,3.14],ft:5},{wps:[[22,7],[28,7]]}]}},
""" % (json.dumps(D['proj']),json.dumps(D['MAP'],ensure_ascii=False))
s=s[:a]+W1+s[b:]
rep("m.env=c.env||null;m.brief=","m.env=c.env||null;if(m.subs){m.goal0=m.subs.map(function(x){return x.verb;}).join(' · ')+' → '+m.goal0;m.goal1='열린 문으로 두 명 모두 이탈';}m.brief=")
# ---- 2. 엔진 ----
rep("if(S&&S.open&&S.open[y*COLS+x])return '.';","if(S&&S.shut&&S.shut[y*COLS+x])return '#';if(S&&S.open&&S.open[y*COLS+x])return '.';")
rep("if(o.disg&&!g.boss)return 1.5;","if(o.disg&&!g.boss)return g.keen?RANGE*0.6:1.5;")
rep("if(canSee(g,o.x,o.y,RANGE)&&!(o.disg&&!g.boss))fail(","if(canSee(g,o.x,o.y,RANGE)&&!(o.disg&&!g.boss&&!g.keen))fail(")
rep("function newState(){\n  return {t:0,","function newState(){\n  var st={t:0,subs:[],shut:{},exitI:-1,radio:-1,ev:false,dark:0,dq:null,dseen:{},")
rep("cam:!!d.cam,boss:!!d.boss,fixed:","cam:!!d.cam,boss:!!d.boss,keen:!!d.keen,plain:!!d.plain,rev:false,rush:false,fixed:")
rep("    hostage:M.hostage?{x:M.hostage.x+0.5,y:M.hostage.y+0.5,free:false}:null};\n}",
"""    hostage:M.hostage?{x:M.hostage.x+0.5,y:M.hostage.y+0.5,free:false}:null};
  if(M.subs){var pl=[];st.guards.forEach(function(g){if(g.plain)pl.push(g.id);});if(pl.length)st.radio=pl[M.rfix!=null?M.rfix:fl(Math.random()*pl.length)];}
  return st;
}
/* 중간 목표 · 판 바꾸기 */
function subsDone(){if(!M.subs)return true;for(var i=0;i<M.subs.length;i++)if(!S.subs[i])return false;return true;}
function subDone(i){
  if(S.subs[i])return;S.subs[i]=true;var sb=M.subs[i],n=0,j;for(j=0;j<M.subs.length;j++)if(S.subs[j])n++;
  if(sb.dark)S.dark=sb.dark;snd('ok');say(subsDone()?'울타리 문이 열렸다. 상자는 트리 아래.':sb.done||sb.label+' 완료');
  if(n===1&&M.dlg&&M.dlg.mid&&!S.dseen.mid){S.dseen.mid=1;S.dq='mid';}
}
function exits(){return M.evac?(S.ev?M.evac.gates[S.exitI].cells:[]):M.exit;}
function evacStart(){
  var G=M.evac.gates,i,used={};S.ev=true;S.exitI=M.evac.fix!=null?M.evac.fix:fl(Math.random()*G.length);
  G.forEach(function(gt,j){
    if(j===S.exitI)return;gt.shut.forEach(function(c){S.shut[c[1]*COLS+c[0]]=1;});
    var best=null,bd=1e9;S.guards.forEach(function(g){if(g.down||g.fixed||g.boss||g.faces||used[g.id])return;var d=hyp(g.x-gt.post[0],g.y-gt.post[1]);if(d<bd){bd=d;best=g;}});
    if(best){used[best.id]=1;best.wps=[gt.post];best.faces=[gt.face,gt.face+0.7,gt.face-0.7];best.fi=0;best.ft=best.fd=2.5;best.state='patrol';best.rush=true;best.path=findPath(fl(best.x),fl(best.y),gt.post[0],gt.post[1])||[];}
  });
  wallCv=null;say('대피 방송. 열린 곳은 '+G[S.exitI].n+'.');
  if(M.dlg&&M.dlg.obj&&!S.dseen.obj){S.dseen.obj=1;S.dq='obj';}
}""")
rep("  followPath(g,g.state==='patrol'?1.3:2.2,dt,5);","  if(g.rush&&!g.path.length)g.rush=false;\n  followPath(g,g.rush?2.6:g.state==='patrol'?1.3:2.2,dt,5);")
rep("  else if(a.type==='sab'){var u=M.objective.use;o.path=findPath(fl(o.x),fl(o.y),u[0],u[1])||[];a.t=M.objective.time;}",
    "  else if(a.type==='sab'){if(!subsDone()){say(M.lock||'아직 잠겨 있다.');o.cur=null;return;}var u=M.objective.use;o.path=findPath(fl(o.x),fl(o.y),u[0],u[1])||[];a.t=M.objective.time;}\n  else if(a.type==='sub'){var sb=M.subs[a.i];if(!sb.use||S.subs[a.i]){o.cur=null;return;}o.path=findPath(fl(o.x),fl(o.y),sb.use[0],sb.use[1])||[];a.t=sb.time;}")
rep("  }else if(a&&a.type==='hack'){\n    g=S.guards[a.id];",
"""  }else if(a&&a.type==='sub'){
    if(!o.path.length){
      var sb=M.subs[a.i],su=sb.use;
      if(fl(o.x)!==su[0]||fl(o.y)!==su[1]){o.cur=null;say('거긴 길이 없다.');}
      else{o.ang=Math.atan2(sb.y+(sb.h||1)/2-o.y,sb.x+(sb.w||1)/2-o.x);o.fx='plant';o.fxt=0.2;a.t-=dt;if(a.t<=0){o.cur=null;subDone(a.i);}}
    }
  }else if(a&&a.type==='hack'){
    g=S.guards[a.id];""")
rep("function inExit(o){for(var i=0;i<M.exit.length;i++)if(fl(o.x)===M.exit[i][0]&&fl(o.y)===M.exit[i][1])return true;return false;}",
    "function inExit(o){var E=exits();for(var i=0;i<E.length;i++)if(fl(o.x)===E[i][0]&&fl(o.y)===E[i][1])return true;return false;}")
rep("  if(k!==ENV.k){RANGE=6.5*DF.r*k;CRANGE=3.6*DF.r*k;}",
    "  if(S.dark)k*=S.dark;if(S.ev){t='대피 방송 · 열린 곳은 '+M.evac.gates[S.exitI].n;hot=true;}else if(S.dark&&!t)t='조명 OFF · 경비 시야 감소';\n  if(k!==ENV.k){RANGE=6.5*DF.r*k;CRANGE=3.6*DF.r*k;}")
rep("  }else if(S.objDone){var all=true;","  }else if(S.objDone&&M.evac&&!S.ev){evacStart();\n  }else if(S.objDone){var all=true;")
rep("  for(i=0;i<S.guards.length;i++){var gg=S.guards[i];if(gg.down&&!gg.dead){",
"""  if(M.subs){
    if(S.radio>=0&&S.guards[S.radio].down)for(i=0;i<M.subs.length;i++)if(M.subs[i].k==='radio')subDone(i);
    S.guards.forEach(function(g){if(!g.plain||g.rev)return;for(var j=0;j<S.ops.length;j++){var o=S.ops[j];if(hyp(o.x-g.x,o.y-g.y)<3.2&&los(o.x,o.y,g.x,g.y,false)){g.rev=true;pop(g.x,g.y,g.id===S.radio?'무전병이다':'무전기가 없다',g.id===S.radio?'#ffd27a':'#c9d2dc');}}});
  }
  for(i=0;i<S.guards.length;i++){var gg=S.guards[i];if(gg.down&&!gg.dead){""")
# 그리기
rep("  M.exit.forEach(function(e){ctx.beginPath();poly(ctx,quad(e[0],e[1],0.12));ctx.stroke();});noGlow();","  exits().forEach(function(e){ctx.beginPath();poly(ctx,quad(e[0],e[1],0.12));ctx.stroke();});noGlow();")
rep("  if(wallCv)ctx.drawImage(wallCv,0,0);\n  /* 캐릭터 */",
"""  if(M.subs)M.subs.forEach(function(sb,si){if(!sb.use||S.subs[si])return;glow('#ffd27a',10);ring(sb.x+(sb.w||1)/2,sb.y+(sb.h||1)/2,0.9);ctx.strokeStyle='#ffd27a';ctx.lineWidth=2;ctx.stroke();noGlow();});
  if(wallCv)ctx.drawImage(wallCv,0,0);
  if(S.ev)M.evac.gates.forEach(function(gt,j){if(j!==S.exitI)propDraw(gt.bar[0],gt.bar[1],gt.bar[2],gt.bar[3],gt.bar[4],0);});
  /* 캐릭터 */""")
rep("  S.guards.forEach(function(g){if(!g.tower)return;var f=gp(g);if(g.down)spr('misc.png',0,g.ang,[f[0],f[1]+6],0,1,'#59616b');",
    "  if(M.santa&&S.t<M.santa.t&&!S.objDone){ctx.globalAlpha=Math.min(1,(M.santa.t-S.t)/2);propDraw(M.santa.img,M.santa.x-0.5,M.santa.y-0.5,1,1,M.santa.up);ctx.globalAlpha=1;}\n  S.guards.forEach(function(g){if(!g.tower)return;var f=gp(g);if(g.down)spr('misc.png',0,g.ang,[f[0],f[1]+6],0,1,'#59616b');")
rep("    if(g.boss&&g.meter<=0.02&&g.state!=='investigate')label('WARDEN',o[0],o[1]-up,12,'#ffd27a');",
    "    if(g.boss&&g.meter<=0.02&&g.state!=='investigate')label('WARDEN',o[0],o[1]-up,12,'#ffd27a');\n    if(g.plain&&g.meter<=0.02&&g.state!=='investigate')label(!g.rev?'사복 ?':g.id===S.radio?'무전병':'사복',o[0],o[1]-up,12,!g.rev?'#c9d2dc':g.id===S.radio?'#ffd27a':'#8a96a3');")
rep("  if(M.objective&&!S.objDone){p=PF(M.objective.x+0.5,M.objective.y+0.5);label(M.objective.label,p[0],p[1]-56,14,'#5df0e0');}\n  p=PF(M.exit[0][0]+(M.exit.length>1?(MI===1?1:2):0.5),M.exit[0][1]+(M.exit.length>1&&MI===1?1:0.5));label('탈출',p[0],p[1],14,'#5dff7a');",
"""  if(M.objective&&!S.objDone){p=PF(M.objective.x+0.5,M.objective.y+0.5);label(M.objective.label+(subsDone()?'':' · 잠김'),p[0],p[1]-56,14,subsDone()?'#5df0e0':'#8a96a3');}
  if(M.subs)M.subs.forEach(function(sb,si){if(!sb.use||S.subs[si])return;p=PF(sb.x+(sb.w||1)/2,sb.y+(sb.h||1)/2);label(sb.label,p[0],p[1]-44,13,'#ffd27a');});
  if(M.evac){var EX=exits();if(EX.length){p=PF((EX[0][0]+EX[1][0])/2+0.5,(EX[0][1]+EX[1][1])/2+0.5);label('탈출',p[0],p[1],14,'#5dff7a');}}
  else{p=PF(M.exit[0][0]+(M.exit.length>1?(MI===1?1:2):0.5),M.exit[0][1]+(M.exit.length>1&&MI===1?1:0.5));label('탈출',p[0],p[1],14,'#5dff7a');}""")
rep("    if(a.type==='sab')label(M.objective.verb+' 중 '+Math.ceil(a.t),q[0],q[1]-84,14,'#5df0e0');",
    "    if(a.type==='sab')label(M.objective.verb+' 중 '+Math.ceil(a.t),q[0],q[1]-84,14,'#5df0e0');\n    else if(a.type==='sub')label(M.subs[a.i].verb+' 중 '+Math.ceil(a.t),q[0],q[1]-84,14,'#ffd27a');")
rep("function opCol(o){return OPD[o.id].col;}",
"""function propDraw(name,x,y,w,h,up){
  loadImg(name);var im=IM[name];if(!ok(im))return;
  var L=PF(x,y+h),R=PF(x+w,y),B=PF(x+w,y+h),fw=R[0]-L[0],k=fw/(im.naturalWidth||im.width),ih=(im.naturalHeight||im.height)*k;
  if(up){k=M.sk*0.62;fw=(im.naturalWidth||im.width)*k;ih=(im.naturalHeight||im.height)*k;ctx.drawImage(im,(L[0]+R[0])/2-fw/2,B[1]-up-ih,fw,ih);return;}
  ctx.drawImage(im,(L[0]+R[0])/2-fw/2,B[1]+2-ih,fw,ih);
}
function opCol(o){return OPD[o.id].col;}""")
# UI
rep("plan,S.objDone,started,S.ops.map(","plan,S.objDone,started,S.subs.join(),S.ops.map(")
rep("  if(M.objective&&!S.objDone&&(!M.objective.by||M.objective.by===A.id))h+=ib('sab','sab',M.objective.verb);",
    "  if(M.subs)M.subs.forEach(function(sb,si){if(sb.use&&!S.subs[si])h+='<button class=\"ab\" data-a=\"sub\" data-v=\"'+si+'\">'+num()+ic('sab')+'<span>'+sb.verb+'</span></button>';});\n  if(M.objective&&!S.objDone&&(!M.objective.by||M.objective.by===A.id))h+=ib('sab','sab',M.objective.verb);")
rep("  $('obj').textContent=done?M.goal1:M.goal0;",
    "  $('obj').textContent=done?(S.ev?M.evac.gates[S.exitI].n+'으로 두 명 모두 이탈':M.goal1):M.subs?M.subs.map(function(sb,si){return (S.subs[si]?'✓ ':'')+sb.verb;}).join(' · ')+' → '+M.objective.label+' '+M.objective.verb:M.goal0;")
rep("  else if(a==='sab')issue(A,{type:'sab'});","  else if(a==='sab')issue(A,{type:'sab'});\n  else if(a==='sub')issue(A,{type:'sub',i:+v});")
rep("    else if(M.objective&&!S.objDone&&cx===M.objective.x&&cy===M.objective.y){",
"""    else if(M.subs&&M.subs.some(function(sb,si){if(sb.use&&!S.subs[si]&&cx>=sb.x&&cx<sb.x+(sb.w||1)&&cy>=sb.y&&cy<sb.y+(sb.h||1)){issue(A,{type:'sub',i:si});return true;}return false;})){return;}
    else if(M.objective&&!S.objDone&&cx===M.objective.x&&cy===M.objective.y){""")
# 줌
rep("  if(!userZoom)cam.z=Math.max(Math.min(W,H)/600,Math.min(W/IW,H/IH));","  if(!userZoom)cam.z=Math.max(Math.min(W,H)/600,Math.min(W/IW,H/IH))*((M&&M.zm)||1);")
rep("  loadImg(M.bg);\n}","  loadImg(M.bg);userZoom=false;\n}")
# ---- 3. 대화 화면 ----
rep('<div id="sc" class="hide">','<div id="dlg" class="hide"><img id="dgl" alt=""><img id="dgr" alt=""><div id="dgb"><b id="dgn"></b><p id="dgt"></p><div id="dgf"><button id="dgs">건너뛰기</button><span>화면을 누르면 다음</span></div></div></div>\n<div id="sc" class="hide">')
rep("#sc{position:fixed;",
"""#dlg{position:fixed;inset:0;z-index:12;background:linear-gradient(180deg,rgba(6,8,11,.55) 0%,rgba(6,8,11,.2) 35%,rgba(6,8,11,.9) 78%);overflow:hidden;--c:#ff3b52}
#dlg.hide{display:none}
#dlg img{position:absolute;bottom:17vh;height:66vh;max-width:62vw;object-fit:contain;object-position:bottom;transition:filter .2s,transform .2s,opacity .2s;filter:brightness(.38) saturate(.6);transform:scale(.96);transform-origin:bottom}
#dlg img.card{width:46vw;height:56vh;object-fit:cover;-webkit-mask-image:linear-gradient(180deg,#000 60%,transparent);mask-image:linear-gradient(180deg,#000 60%,transparent)}
#dlg img.on{filter:none;transform:none}
#dlg img.off{opacity:0}
#dgl{left:-3vw}#dgr{right:-3vw}
#dgb{position:absolute;left:0;right:0;bottom:0;padding:16px 18px calc(18px + env(safe-area-inset-bottom));background:rgba(6,8,11,.92);border-top:2px solid var(--c);min-height:19vh}
#dgn{display:block;font-size:13px;letter-spacing:.14em;color:var(--c);margin-bottom:8px}
#dgt{margin:0;font-size:16px;line-height:1.6;color:#ece8e1;word-break:keep-all;min-height:4.8em}
#dgf{display:flex;justify-content:space-between;align-items:center;margin-top:10px;font-size:11px;color:#8a96a3}
#dgs{background:none;border:1px solid #3a424c;color:#c9d2dc;font-size:12px;padding:6px 12px;border-radius:2px}
#sc{position:fixed;""")
rep("function save(){saved=JSON.stringify(S);}",
"""/* 대화 화면: 왼쪽 상대, 오른쪽 요원. lines=[[누구,대사],...] */
var DLGON=false,DLQ=[],DLD=null,DLGM=-1,DCAST={hq:{n:'지휘관',c:'#c9d2dc'},santa:{n:'산타',c:'#e0364f',side:'l'}};
function dlgWho(k){var d=DCAST[k]||{},o=OPD[k],cast=(M.dlg&&M.dlg.cast)||{};return {n:d.n||(o?o.n:k),c:d.c||(o?o.col:'#fff'),side:d.side||(o?'r':''),img:cast[k]||(o?'a_'+k+'_6.jpg':''),card:!cast[k]&&!!o};}
function dlg(lines,done){
  DLQ=lines.slice();DLD=done||null;DLGON=true;var L=$('dgl'),R=$('dgr'),seen={l:'',r:''};
  lines.forEach(function(x){var w=dlgWho(x[0]);if(w.side&&!seen[w.side])seen[w.side]=x[0];});
  [['l',L],['r',R]].forEach(function(a){var w=seen[a[0]]?dlgWho(seen[a[0]]):null;a[1].className=w?(w.card?'card':''):'off';if(w){a[1].src=w.img;if(w.card&&a[1].style)a[1].style.objectPosition=fp(w.img);}a[1].setAttribute&&a[1].setAttribute('data-w',seen[a[0]]||'');});
  $('dlg').className='';dlgNext();
}
function dlgNext(){
  var x=DLQ.shift();if(!x){$('dlg').className='hide';DLGON=false;var d=DLD;DLD=null;if(d)d();return;}
  var w=dlgWho(x[0]),el=$('dlg'),L=$('dgl'),R=$('dgr'),t=w.side==='l'?L:w.side==='r'?R:null;
  if(el.style&&el.style.setProperty)el.style.setProperty('--c',w.c);
  if(t&&t.getAttribute&&t.getAttribute('data-w')!==x[0]){t.src=w.img;t.setAttribute('data-w',x[0]);if(t.style)t.style.objectPosition=w.card?fp(w.img):'bottom';}
  [L,R].forEach(function(e){var c=(e.className||'').replace(/ ?on/,'');if(c==='off')return;if(e===t)c=(w.card?'card':'')+' on';e.className=c;});
  $('dgn').textContent=w.n;$('dgt').textContent=x[1];
}
if($('dlg').addEventListener)$('dlg').addEventListener('click',function(e){if(e.target&&e.target.id==='dgs'){DLQ=[];}dlgNext();});
function save(){saved=JSON.stringify(S);}""")
rep("function restart(){setPre(false);S=newState();plan=false;loads=0;wallCv=null;UIK='';save();hideOv();started=true;freeCam=false;var p=PF(S.ops[0].x,S.ops[0].y);cam.x=p[0];cam.y=p[1];}",
    "function restart(){setPre(false);S=newState();plan=false;loads=0;wallCv=null;UIK='';save();hideOv();started=true;freeCam=false;var p=PF(S.ops[0].x,S.ops[0].y);cam.x=p[0];cam.y=p[1];if(M.dlg&&M.dlg.start&&DLGM!==MI){DLGM=MI;dlg(M.dlg.start);}}")
rep("  setPre(true);hideOv();hmHide();pgHide();loadMission(i);","  setPre(true);hideOv();hmHide();pgHide();DLGM=-1;loadMission(i);")
rep("function showEnd(){\n","function showEnd(){\n  if(S.over.win&&M.dlg&&M.dlg.end&&!S.dseen.end){S.dseen.end=1;snd('ok');dlg(M.dlg.end,showEnd);return;}\n")
rep("  if(started&&!plan&&!S.over&&!TIPON){update(dt);if(S.over)showEnd();}","  if(S&&S.dq&&!DLGON){var dk=S.dq;S.dq=null;if(M.dlg&&M.dlg[dk])dlg(M.dlg[dk]);}\n  if(started&&!plan&&!S.over&&!TIPON&&!DLGON){update(dt);if(S.over)showEnd();}")
rep("var VERSION='0.26.0';","var VERSION='0.27.0';")
io.open(p,'w',encoding='utf8').write(s); print('ok',len(s))
