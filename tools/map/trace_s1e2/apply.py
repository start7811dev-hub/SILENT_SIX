import io,json,re
P='/home/claude/repo/public/index.html'; s=io.open(P,encoding='utf8').read()
def rep(a,b,n=1):
    global s
    c=s.count(a); assert c==n,(a[:80],c); s=s.replace(a,b)
W='/home/claude/work/'
data=io.open('/home/claude/patch/ep2_data.js',encoding='utf8').read()
for n in ['07','08','09','10','11','12']:
    F=json.load(open(W+'final%s.json'%n))
    data=data.replace('__P%s__'%n,json.dumps(F['proj'])).replace('__M%s__'%n,json.dumps(F['MAP']))
assert '__' not in re.sub(r'__[a-z]','',data) or True
# 1. 데이터
rep("  WIDX.push(MIS.length);MIS.push(m);\n});\n","  WIDX.push(MIS.length);MIS.push(m);\n});\n"+data)
nov=io.open('/home/claude/patch/novel2.js',encoding='utf8').read()
rep("function novelRead(n){",nov+"function novelRead(n){")
# 2. 시즌 · 리워드
rep("{n:'누가 흘렸나'},{n:'미공개'}","{n:'누가 흘렸나',mis:E2IDX,novel:2},{n:'미공개'}")
rep("var RWX={'S1-01':2,","var RWX={'S1-07':2,'S1-08':2,'S1-09':2,'S1-10':2,'S1-11':2,'S1-12':2,'S1-01':2,")
rep("function rwProbe(){for(var i=0;i<NBASE;i++)rwProbeM(i);}","function rwProbe(){STI.forEach(function(i){rwProbeM(i);});}")
# 3. 엔진: 카메라 끄기 · 닫히는 출구 · 번지는 화재 · 제한 시간 문구 · 대화 왼쪽 자리
rep("if(sb.dark)S.dark=sb.dark;applySw(sb.sw);","if(sb.dark)S.dark=sb.dark;if(sb.camoff)S.guards.forEach(function(g){if(g.cam){g.off=1e6;g.meter=0;}});applySw(sb.sw);")
rep("  G.forEach(function(gt,j){\n    if(j===S.exitI)return;\n",
    "  var occ=function(c){return S.ops.some(function(o){return fl(o.x)===c[0]&&fl(o.y)===c[1];});};\n  (M.evac.close||[]).forEach(function(c){if(!occ(c))S.shut[c[1]*COLS+c[0]]=1;});\n  G.forEach(function(gt,j){\n    if(j===S.exitI)return;\n    (gt.close||[]).forEach(function(c){if(!occ(c))S.shut[c[1]*COLS+c[0]]=1;});\n")
rep("    if(e.limit){var left=e.limit+(S.lim||0)-S.t;if(!S.objDone){t='이륙까지 '+mmss(Math.max(0,Math.ceil(left)));hot=left<60;if(left<=0)fail('전용기가 떴다. 화물은 하늘에 있다.');}else t='';}",
    "    if(e.limit){var left=e.limit+(S.lim||0)-S.t;if(!S.objDone){t=(e.ltxt||'이륙까지')+' '+mmss(Math.max(0,Math.ceil(left)));hot=left<60;if(left<=0)fail(e.lfail||'전용기가 떴다. 화물은 하늘에 있다.');}else t='';}\n"
    "    if(e.spread){var sp=e.spread,sk=fl(S.t/sp.every);if(!S.fire)S.fire={};for(var ri=0;ri<sp.rooms.length&&ri<sk;ri++)if(!S.fire[ri]){S.fire[ri]=1;sp.rooms[ri].cells.forEach(function(c){if(!S.ops.some(function(o){return fl(o.x)===c[0]&&fl(o.y)===c[1];}))S.shut[c[1]*COLS+c[0]]=1;});wallCv=null;say(sp.rooms[ri].n+' 셔터가 내려왔다. 불길이 번진다.');}\n"
    "      if(!t&&sk<sp.rooms.length){var fl2=sp.every*(sk+1)-S.t;t=sp.rooms[sk].n+' 셔터까지 '+Math.ceil(fl2);hot=fl2<=10;}}")
rep("  if(S.ev)M.evac.gates.forEach(function(gt,j){if(j!==S.exitI)propDraw(gt.bar[0],gt.bar[1],gt.bar[2],gt.bar[3],gt.bar[4],0);});",
    "  if(S.ev)M.evac.gates.forEach(function(gt,j){if(j!==S.exitI&&gt.bar)propDraw(gt.bar[0],gt.bar[1],gt.bar[2],gt.bar[3],gt.bar[4],0);});\n"
    "  if(S.ev&&M.evac.bars)M.evac.bars.forEach(function(b){propDraw(b[0],b[1],b[2],b[3],b[4],0);});\n"
    "  if(S.fire&&M.env&&M.env.spread)M.env.spread.rooms.forEach(function(r,ri){if(S.fire[ri])r.bars.forEach(function(b){propDraw(b[0],b[1],b[2],b[3],b[4],0);});});")
rep("return {n:d.n||(o?o.n:k),c:d.c||(o?o.col:'#fff'),side:d.side||(o?'r':''),",
    "return {n:d.n||(o?o.n:k),c:d.c||(o?o.col:'#fff'),side:d.side||(o?(M.dlg&&M.dlg.left===k?'l':'r'):''),")
# 4. 메뉴: 에피소드 2
rep("function mOpen(i){return i===0||!!PROG.c[i-1]||allOn()||GOD();}",
    "function mOpen(i){if(allOn()||GOD())return true;var e=epOf(i);if(e===1){var k=E2IDX.indexOf(i);return k===0?epAll(0):!!PROG.c[E2IDX[k-1]];}return i===0||!!PROG.c[i-1];}\nvar MEP=0; /* 스토리 스테이지 목록이 보여 줄 에피소드 */\nfunction ep2Open(){return GOD()||allOn()||epAll(0);}")
old_s1=s[s.index("function season1(){"):s.index("function mOpen(i)")]
new_s1=u"""function season1(){
  var n=mainDone(),n2=epDone(1),o2=ep2Open(),go=function(){MEP=0;if(PROG.pro)menu();else{PROG.pro=1;saveProg();reader({t:NOVEL.pro.t,sub:'S1 · EPISODE 1 // PROLOGUE',img:NOVEL.pro.img,p:NOVEL.pro.p,btn:'에피소드 1 시작',next:menu,back:menu});}},soon=function(k){return function(){info('EPISODE '+k,'SEASON 1 // COMING',null,'<p>아직 공개되지 않은 에피소드입니다. <em class="k">앞선 에피소드를 모두 클리어하면</em> 차례로 열립니다.</p>',season1);};};
  var go2=function(){if(o2){MEP=1;menu();}else info('누가 흘렸나','S1 · EPISODE 2 // LOCKED','r_S1-07_0.jpg','<p>여섯이 모인 뒤, <em class="k">명단을 판 번호가 지휘관 자리의 번호였다</em>는 사실에서 시작하는 에피소드입니다.</p><p style="color:var(--dim)">에피소드 1의 여섯 스테이지를 모두 클리어하면 열립니다 · '+n+' / '+NBASE+'</p>',season1);};
  page('지워진 이름들','SEASON 1',intro('Season 1 · 지워진 이름들','시즌 1. Episode','6과의 요원들이 다시 모인 이유와<br>그들이 마주할 운명의 이야기가 시작됩니다.','* 시즌 1은 에피소드 5까지 이어지며, 에피소드는 순서대로 열립니다.')+'<div class="cg">'+cd(0,mimg(4),'여섯이 모이기까지',n+' / '+NBASE+' 스테이지 클리어',{kv:1,w:1,eye:'EPISODE 1',tag:n>=NBASE?'CLEAR':'OPEN',on:1})+cd(1,mimg(E2IDX[0]),'누가 흘렸나',o2?n2+' / '+E2IDX.length+' 스테이지 클리어':'에피소드 1을 마치면 이어집니다',{kv:1,w:1,eye:'EPISODE 2',tag:!o2?'LOCKED':n2>=E2IDX.length?'CLEAR':'OPEN',lock:!o2,on:o2?1:0})+[3,4,5].map(function(k){return cd(k-1,null,'미공개','',{w:1,eye:'EPISODE '+k,tag:'COMING',lock:1});}).join('')+'</div>',seasons,[go,go2,soon(3),soon(4),soon(5)]);
}
"""
s=s.replace(old_s1,new_s1)
old_menu=s[s.index("function menu(){"):s.index("function season3(){")]
new_menu=u"""function menu(){
  var e=MEP===1?1:0,LS=epList(e),L=[],A=[];LS.forEach(function(i,k){if(!vis(i))return;var ok=mOpen(i);L.push(cd(A.length,mimg(i),MIS[i].title,ok?MIS[i].code.split(' // ')[1]:'앞 스테이지를 먼저 클리어하세요',{kv:1,no:('0'+(sOrd(i)+1)).slice(-2),x:bm(i,'span'),lock:!ok,tag:PROG.c[i]?'CLEAR':ok?'':'LOCKED',on:1}));A.push(function(){if(ok)brief(i);});});
  var T=e?['Season 1 · Episode 2','누가 흘렸나','명단을 판 번호는 지휘관 자리의 번호였다.<br>여섯은 그 번호가 쓰인 곳을 하나씩 확인한다.']:['Season 1 · Episode 1','여섯이 모이기까지','6과의 각 요원에게 주어진 베일에 싸인 임무.<br>미션을 클리어하며 탐욕의 진실을 파헤쳐 보세요.'];
  page(T[1],'S1 · EPISODE '+(e+1)+' // '+DF.n,intro(T[0],T[1],T[2],'* 스테이지는 이야기 순서대로 오픈되며, 모두 클리어한 경우에는 자유롭게 재도전이 가능합니다.')+rwdBox('스토리 갤러리')+'<div class="cg one">'+L.join('')+'</div>',season1,A);
}
"""
s=s.replace(old_menu,new_menu)
# 5. 브리핑 · 클리어 소설
rep("  if(MI<NBASE){var ch=NOVEL.ch[MI];reader({t:ch.t,sub:'S1 · EPISODE 1 // '+(MI+1)+'장',img:M.img,p:ch.pre,btn:'작전 브리핑',next:missionCard,back:menu});}",
    "  var ep=epOf(MI);if(ep>=0)MEP=ep;\n  if(ep>=0){var ch=epCh(MI);reader({t:ch.t,sub:'S1 · EPISODE '+(ep+1)+' // '+(epList(ep).indexOf(MI)+1)+'장',img:M.img,p:ch.pre,btn:'작전 브리핑',next:missionCard,back:menu});}")
rep("  if(S.over.win&&MI<NBASE){snd('ok');var ch=NOVEL.ch[MI],go=function(){pgHide();result();};reader({t:ch.t,sub:'MISSION CLEAR // '+(MI+1)+'장',img:M.img,p:ch.post,q:ch.q,btn:'결과 보기',next:go,back:go});}",
    "  if(S.over.win&&isStory(MI)){snd('ok');var ch=epCh(MI),go=function(){pgHide();result();};reader({t:ch.t,sub:'MISSION CLEAR // '+(epList(epOf(MI)).indexOf(MI)+1)+'장',img:M.img,p:ch.post,q:ch.q,btn:'결과 보기',next:go,back:go});}")
rep("else if(MI<NBASE-1)b.unshift(['다음 미션',function(){brief(MI+1);},true]);",
    "else if(isStory(MI)){var so=sOrd(MI),nx=STI[so+1];if(nx!=null&&mOpen(nx))b.unshift([epOf(nx)!==epOf(MI)?'다음 에피소드':'다음 미션',function(){brief(nx);},true]);}")
# 6. 소설(블랙박스)
old_nv=s[s.index("function bbNovel(){"):s.index("function bbClear(){")]
new_nv=u"""function epCh(i){var e=epOf(i);return e===1?NOVEL.e2.ch[E2IDX.indexOf(i)]:NOVEL.ch[i];}
function bbNovel(){
  var c=scCur(),h=scNav(),A=[];
  if(c.E&&c.E.novel){var e=c.E.novel-1,LS=epList(e),CH=e?NOVEL.e2.ch:NOVEL.ch,nd=epDone(e),tot=LS.length,row=function(img,eye,t,open,st){var k=A.length;return '<button data-k="'+k+'" class="'+(open?'go':'lock')+'"><span class="th" style="background-image:url('+img+');background-position:'+fp(img)+'"></span><span><i>'+eye+'</i><b>'+t+'</b></span><em>'+st+'</em></button>';};
    h+='<div class="cap"><i>EP '+(SCP.e+1)+'</i>'+c.E.n+'<u>'+nd+' / '+tot+'장 열림</u></div><div class="nl" style="grid-template-rows:repeat('+(tot+(e?1:2))+',1fr)">';
    if(!e){h+=row(NOVEL.pro.img,'PROLOGUE',NOVEL.pro.t,true,'읽기 ›');A.push(function(){novelRead('p');});}
    CH.forEach(function(ch,k){var mi=LS[k],op=!!PROG.c[mi]||GOD();h+=row(mimg(mi),(k+1)+'장',op?ch.t:'미션을 클리어하면 열립니다',op,op?'읽기 ›':'LOCKED');A.push(function(){if(op)novelRead(e+':'+k);});});
    var all=nd>=tot||GOD();h+=row(e?'r_S1-12_0.jpg':'a_raven_7.jpg','FULL','에피소드 '+(SCP.e+1)+' 전체 읽기',all,all?'읽기 ›':nd+' / '+tot);A.push(function(){if(all)novelRead(e?'all2':'all');});
    h+='</div>';
  }else h+=scEmpty(c.E?'EP '+(SCP.e+1)+' · '+c.E.n+'<br>에피소드가 공개되면 이곳에 소설이 쌓입니다.':c.S.k+' · '+c.S.n+'<br>시즌이 공개되면 이곳에 소설이 쌓입니다.');
  page('사일런트 식스 소설','BLACK BOX // NOVEL',h,blackbox,A,function(e){scTap(e,bbNovel);});fit();
}
"""
s=s.replace(old_nv,new_nv)
rep("  var c=NOVEL.ch[+n];reader({t:c.t,sub:'S1 · EPISODE 1 // '+(+n+1)+'장',img:mimg(+n),p:c.pre.concat(c.post),q:c.q,back:bbNovel});",
    "  if(n==='all2'){var h2='';NOVEL.e2.ch.forEach(function(c,i){h2+='<h3>'+(i+1)+'장 — '+c.t+'</h3>'+c.pre.concat(c.post).map(function(x){return '<p>'+nv(x)+'</p>';}).join('')+'<p class=\"q\">남는 의문 — '+c.q+'</p>';});reader({t:NOVEL.e2.t,sub:'SEASON 1 · EPISODE 2 // 전체',img:'r_S1-12_0.jpg',html:h2,back:bbNovel});return;}\n"
    "  var ep=0,k=+n;if(typeof n==='string'&&n.indexOf(':')>0){ep=+n.split(':')[0];k=+n.split(':')[1];}var c=ep?NOVEL.e2.ch[k]:NOVEL.ch[k],mi=epList(ep)[k];reader({t:c.t,sub:'S1 · EPISODE '+(ep+1)+' // '+(k+1)+'장',img:mimg(mi),p:c.pre.concat(c.post),q:c.q,back:bbNovel});")
# 7. 홈 · 시즌 카드 · 블랙박스 · 랭킹
rep("for(var q=0;q<NBASE;q++)if(!PROG.c[q]){nx=q;break;}var kv=mimg(nx);",
    "var he=ep2Open()&&epAll(0)?1:0,hL=epList(he),hn=epDone(he);nx=hL[0];for(var q=0;q<hL.length;q++)if(!PROG.c[hL[q]]){nx=hL[q];break;}var kv=mimg(nx);")
rep("<i>STORY MISSION · S1 · EPISODE 1</i><b>스토리 미션</b><u>'+n+' / '+NBASE+' · 여섯이 모이기까지</u><em>›</em><span class=\"bar\"><s style=\"width:'+(n/NBASE*100)+'%\"></s></span>",
    "<i>STORY MISSION · S1 · EPISODE '+(he+1)+'</i><b>스토리 미션</b><u>'+hn+' / '+hL.length+' · '+(he?'누가 흘렸나':'여섯이 모이기까지')+'</u><em>›</em><span class=\"bar\"><s style=\"width:'+(hn/hL.length*100)+'%\"></s></span>")
rep("cd(0,mimg(4),'지워진 이름들','에피소드 1 진행 중 · '+mainDone()+' / '+NBASE,",
    "cd(0,mimg(4),'지워진 이름들',(ep2Open()&&epAll(0)?'에피소드 2 진행 중 · '+epDone(1)+' / '+E2IDX.length:'에피소드 1 진행 중 · '+mainDone()+' / '+NBASE),")
rep("  var ids=Object.keys(STORY),nd=mainDone(),sl=[],i;for(i=0;i<NBASE;i++)sl.push(i);",
    "  var ids=Object.keys(STORY),nd=mainDone()+epDone(1),sl=STI.slice(),i;")
rep("cd(0,mimg(4),'사일런트 식스 소설','시즌 · 에피소드별 · '+nd+' / '+NBASE+'장',",
    "cd(0,mimg(4),'사일런트 식스 소설','시즌 · 에피소드별 · '+nd+' / '+STI.length+'장',")
rep("if(i<NBASE)all+=b0;else if(MIS[i].winter)","if(isStory(i))all+=b0;else if(MIS[i].winter)")
rep("[['스토리 미션',function(i){return i<NBASE;}]","[['스토리 미션',function(i){return isStory(i);}]")
# 8. 뷰어: 이미지를 바꿀 때 이전 그림이 남지 않게
rep("function vwGo(i){if(i<0||i>=VWL.length)return;VWI=i;VWF=VWL[i];$('vwi').src=VWF;",
    "var VWT=0;\nfunction vwGo(i){if(i<0||i>=VWL.length)return;VWI=i;VWF=VWL[i];var im=$('vwi'),tk=++VWT;if(im.style)im.style.opacity=0;im.onload=im.onerror=function(){if(tk===VWT&&im.style)im.style.opacity=1;};im.src=VWF;if(im.complete&&im.naturalWidth&&im.style)im.style.opacity=1;[i+1,i-1].forEach(function(j){if(VWL[j]&&typeof Image!=='undefined'){var p=new Image();p.src=VWL[j];}});")
rep("#vw img{width:100%;height:100%;object-fit:contain;","#vw img{width:100%;height:100%;object-fit:contain;transition:opacity .14s;")
rep("var VERSION='0.42.4';","var VERSION='0.43.0';")
io.open(P,'w',encoding='utf8').write(s); print('patched')
