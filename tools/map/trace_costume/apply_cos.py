import io, re
P = '/home/claude/silent_six/public/index.html'; s = io.open(P, encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:90], c); s = s.replace(a, b)
data = io.open('/home/claude/cw/work/cosmap.js', encoding='utf8').read() + io.open('/home/claude/cw/cos_data.js', encoding='utf8').read()
# 1. 데이터
rep("function epAll(e){var L=epList(e);return L.length>0&&epDone(e)===L.length;}",
    "function epAll(e){var L=epList(e);return L.length>0&&epDone(e)===L.length;}\n" + data)
# 2. 중간 목표 수: need 0 허용
rep("return n>=(M.need||M.subs.length);}", "return n>=(M.need!=null?M.need:M.subs.length);}")
# 3. 가짜 목표 · 대화 목표
rep("function subDone(i){\n  if(S.subs[i])return;",
    "function subDone(i){\n  if(S.subs[i])return;var sb0=M.subs[i];if(sb0.fake){fail(sb0.fake);return;}if(sb0.talk&&!(S.tk&&S.tk[i])){S.tq=i;return;}")
# 4. 대화: 선택지 퀴즈 · 실패
rep('<div id="dgb"><b id="dgn"></b><p id="dgt"></p><div id="dgf">', '<div id="dgb"><b id="dgn"></b><p id="dgt"></p><div id="dgc"></div><div id="dgf">')
rep("#dgs{background:none;", "#dgc{display:flex;flex-direction:column;gap:8px;margin-top:10px}#dgc:empty{display:none}#dgc button{background:#10151b;border:1px solid #3a424c;border-left:3px solid var(--c);color:#ece8e1;font-size:15px;text-align:left;padding:11px 14px;border-radius:2px}#dgc button:active{background:#1b232c}#dgc i{font-style:normal;font-size:11px;letter-spacing:.14em;color:var(--c)}\n#dgs{background:none;")
rep("function dlgNext(){\n  var x=DLQ.shift();if(!x){$('dlg').className='hide';DLGON=false;var d=DLD;DLD=null;if(d)d();return;}",
    "var DLCH=null,DLFAIL=null,DLTM=null;\n"
    "function dlgTimer(){if(DLTM)clearInterval(DLTM);DLTM=null;}\n"
    "function dlgPick(ci){if(!DLCH)return;var q=DLCH.q,nw=DLCH.who,me=M.ops[0].id,okk=ci===q.a;dlgTimer();DLCH=null;$('dgc').innerHTML='';\n"
    "  if(okk){DLQ.unshift([me,q.ch[ci],1]);}else{var nm=(dlgWho(nw).n||'');DLQ=[[me,ci<0?'……':q.ch[ci],2],[nw,q.no||'…수상한데.',1]];DLFAIL=nm+'에게 정체가 들통났다. 침입이 발각됐다.';}\n"
    "  dlgNext();}\n"
    "function dlgNext(){\n  if(DLCH)return;var x=DLQ.shift();if(!x){$('dlg').className='hide';DLGON=false;dlgTimer();var d=DLD;DLD=null;if(DLFAIL){var f=DLFAIL;DLFAIL=null;fail(f);if(S&&S.over)showEnd();return;}if(d)d();return;}")
rep("  $('dgn').textContent=w.n;$('dgt').textContent=x[1];\n}",
    "  $('dgn').textContent=w.n;$('dgt').textContent=x[1];\n"
    "  var qz=x[3],dc=$('dgc');dc.innerHTML='';if(qz&&qz.ch){DLCH={q:qz,who:x[0]};var t0=Date.now(),lim=12;\n"
    "    dc.innerHTML='<i>대답 · <span id=\"dgq\">'+lim+'</span>초</i>'+qz.ch.map(function(c,k){return '<button data-ci=\"'+k+'\">'+c+'</button>';}).join('');\n"
    "    dlgTimer();DLTM=setInterval(function(){var l=lim-Math.floor((Date.now()-t0)/1000),e2=$('dgq');if(e2)e2.textContent=Math.max(0,l);if(l<=0)dlgPick(-1);},250);}\n}")
rep("if($('dlg').addEventListener)$('dlg').addEventListener('click',function(e){if(e.target&&e.target.id==='dgs'){DLQ=[];}dlgNext();});",
    "if($('dlg').addEventListener)$('dlg').addEventListener('click',function(e){var t=e.target;if(DLCH){while(t&&t!==this&&!(t.dataset&&t.dataset.ci!=null))t=t.parentNode;if(t&&t.dataset&&t.dataset.ci!=null)dlgPick(+t.dataset.ci);return;}"
    "if(t&&t.id==='dgs'){if(DLQ.some(function(q){return q[3]&&q[3].ch;})){while(DLQ.length&&!(DLQ[0][3]&&DLQ[0][3].ch))DLQ.shift();}else DLQ=[];}dlgNext();});")
# 5. 대화 시작 · 코스튬 판정 · 함정
rep("  if(S&&S.dq&&!DLGON){var dk=S.dq;S.dq=null;if(M.dlg&&M.dlg[dk])dlg(M.dlg[dk]);}",
    "  if(S&&S.dq&&!DLGON){var dk=S.dq;S.dq=null;if(M.dlg&&M.dlg[dk])dlg(M.dlg[dk]);}\n"
    "  if(S&&S.tq!=null&&!DLGON&&!S.over){var ti=S.tq;S.tq=null;cosTalk(ti);}")
rep("function senseRange(g,o){",
    "/* 코스튬: 구역 안에서 걸으면 시야가 짧고 의심이 느리다. 뛰거나 앉으면 3초간 꺼진다. 함정 칸 */\n"
    "function cosZ(Z,x,y){if(!Z)return false;x=fl(x);y=fl(y);for(var i=0;i<Z.length;i++)if(x>=Z[i][0]&&y>=Z[i][1]&&x<=Z[i][2]&&y<=Z[i][3])return true;return false;}\n"
    "function cueOn(){return !!(M.env&&M.env.mask&&envPhase(M.env.mask)>=0);}\n"
    "function cosOn(o){var C=M.cos;if(!C||(o.run&&o.mv)||o.crouch)return false;if(o.cst!=null&&S.t-o.cst<3)return false;if(cosZ(C.deny,o.x,o.y))return false;return cosZ(C.zones,o.x,o.y);}\n"
    "function trapOn(){var T=M.cos&&M.cos.traps;if(!T)return false;return T.when==='cue'?cueOn():T.when==='nocue'?!cueOn():true;}\n"
    "function cosTrap(o){var T=M.cos.traps;if(!T||!trapOn())return;var x=fl(o.x),y=fl(o.y);for(var i=0;i<T.cells.length;i++)if(T.cells[i][0]===x&&T.cells[i][1]===y){fail(T.why);return;}}\n"
    "function cosTalk(ti){var sb=M.subs[ti];DLFAIL=null;dlg(sb.talk,function(){if(S.over)return;(S.tk||(S.tk={}))[ti]=1;subDone(ti);});}\n"
    "function senseRange(g,o){\n  if(M.cos&&!g.cam&&cosOn(o))return RANGE*M.cos.k;")
rep("if(canSee(g,o.x,o.y,rg)){rate=(g.cam?3:1.6)+(1-d/rg)*5;",
    "if(canSee(g,o.x,o.y,rg)){rate=(g.cam?3:1.6)+(1-d/rg)*5;if(M.cos&&!g.cam&&cosOn(o))rate*=M.cos.r;")
rep("  var moving=o.path.length>0;o.mv=moving;\n",
    "  var moving=o.path.length>0;o.mv=moving;\n  if(M.cos){if((o.run&&moving)||o.crouch)o.cst=S.t;cosTrap(o);}\n")
# 6. 행동: 코스튬은 이동 · 달리기 · 앉기만
rep("  D.acts.forEach(function(m){", "  (M.cos?['move','run']:D.acts).forEach(function(m){")
rep("var acts=OPD[A.id].acts,mv=function()", "var acts=M.cos?['move','run']:OPD[A.id].acts,mv=function()")
rep("if(M.subs)M.subs.forEach(function(sb,si){if((sb.use||sb.shoot)&&!S.subs[si]&&(!sb.by||sb.by===A.id))h+=",
    "if(M.subs)M.subs.forEach(function(sb,si){if((sb.use||sb.shoot)&&!S.subs[si]&&!sb.tgt&&(!sb.by||sb.by===A.id))h+=")
rep("if(M.objective&&!S.objDone&&(!M.objective.by||M.objective.by===A.id)&&(!M.rom||subsDone()))h+=",
    "if(M.objective&&!S.objDone&&!M.cos&&(!M.objective.by||M.objective.by===A.id)&&(!M.rom||subsDone()))h+=")
# 7. 그리기
rep("  if(M.objective&&!S.objDone){glow('#5df0e0',10);ring(M.objective.x+0.5,M.objective.y+0.5,0.6);",
    "  if(M.cos)cosDraw();\n  if(M.objective&&!S.objDone&&!M.cos){glow('#5df0e0',10);ring(M.objective.x+0.5,M.objective.y+0.5,0.6);")
rep("  if(M.subs)M.subs.forEach(function(sb,si){if(!(sb.use||sb.shoot)||S.subs[si])return;glow('#ffd27a',10);",
    "  if(M.subs)M.subs.forEach(function(sb,si){if(!(sb.use||sb.shoot)||S.subs[si]||sb.tgt)return;glow('#ffd27a',10);")
rep("  if(M.objective&&!S.objDone&&!oSame){p=PF(", "  if(M.cos)cosLabels();\n  if(M.objective&&!S.objDone&&!oSame&&!M.cos){p=PF(")
rep("  if(M.subs)M.subs.forEach(function(sb,si){if(!(sb.use||sb.shoot)||S.subs[si])return;p=PF(",
    "  if(M.subs)M.subs.forEach(function(sb,si){if(!(sb.use||sb.shoot)||S.subs[si]||sb.tgt)return;p=PF(")
rep("function propDraw(name,x,y,w,h,up){",
    "function cellFill(x,y,col){var a=PF(x,y),b=PF(x+1,y),c=PF(x+1,y+1),d=PF(x,y+1);ctx.beginPath();ctx.moveTo(a[0],a[1]);ctx.lineTo(b[0],b[1]);ctx.lineTo(c[0],c[1]);ctx.lineTo(d[0],d[1]);ctx.closePath();ctx.fillStyle=col;ctx.fill();}\n"
    "function cosTg(){var L=[{x:M.objective.x,y:M.objective.y,real:1,done:S.objDone}];M.subs.forEach(function(sb,si){if(sb.tgt)L.push({x:sb.x,y:sb.y,real:0,done:S.subs[si]});});return L;}\n"
    "function cosDraw(){var C=M.cos,k1=S.tk&&S.tk[0],k2=S.tk&&S.tk[1],pl=0.35+0.2*Math.sin(S.t*5);\n"
    "  if(k1&&C.traps){var on=trapOn();C.traps.cells.forEach(function(c){cellFill(c[0],c[1],on?'rgba(255,59,82,'+pl+')':'rgba(255,59,82,.12)');});}\n"
    "  if(k1&&C.deny)C.deny.forEach(function(z){for(var y=z[1];y<=z[3];y++)for(var x=z[0];x<=z[2];x++)if(!blocked(x,y))cellFill(x,y,'rgba(255,59,82,.16)');});\n"
    "  cosTg().forEach(function(t){if(t.done)return;var c=k2?(t.real?'#5df0e0':'#5a636d'):'#ffd27a';glow(c,10);ring(t.x+0.5,t.y+0.5,0.62);ctx.strokeStyle=c;ctx.lineWidth=2;if(k2&&!t.real)ctx.setLineDash([4,4]);ctx.stroke();ctx.setLineDash([]);noGlow();});\n"
    "  if(k1&&C.traps&&C.traps.img&&(C.traps.when!=='cue'||cueOn())){var at=C.traps.at;propDraw(C.traps.img,at[0],at[1],at[2],at[3]);}\n"
    "}\n"
    "function cosLabels(){var k2=S.tk&&S.tk[1],p;\n"
    "  cosTg().forEach(function(t){if(t.done)return;p=PF(t.x+0.5,t.y+0.5);label(k2?(t.real?'진짜 · '+M.objective.label:'미끼'):M.objective.label+' ?',p[0],p[1]-50,13,k2?(t.real?'#5df0e0':'#8a96a3'):'#ffd27a');});\n"
    "  if(S.tk&&S.tk[0]&&M.cos.deny&&M.cos.denyImg){var z=M.cos.deny[0];p=PF((z[0]+z[2])/2+0.5,(z[1]+z[3])/2+0.5);label('코스튬 안 통함',p[0],p[1]+64,12,'#ff6b7d');}\n"
    "  var o=S.ops[0],q=PF(o.x,o.y),inz=cosZ(M.cos.zones,o.x,o.y)&&!cosZ(M.cos.deny,o.x,o.y);if(inz)label(cosOn(o)?'DRESS CODE':'코스튬 꺼짐',q[0],q[1]-96,11,cosOn(o)?'#5df0e0':'#8a96a3');\n"
    "}\n"
    "function propDraw(name,x,y,w,h,up){")
# 8. HUD 목표 문구
rep("  $('obj').textContent=done?", "  if(M.cos&&!done){var tk=S.tk||{};$('obj').textContent=M.subs.filter(function(x){return x.talk;}).map(function(x,i){return (tk[i]?'✓ ':'')+x.label;}).join(' · ')+' → '+(tk[1]?'진짜 '+M.objective.label:M.objective.label+' ?')+' 확보';}else\n  $('obj').textContent=done?")
# 9. 배지 · 카드 · 뒤로 · 실패 메뉴 · 결과
rep("function badgeList(){\n  var c=BCOND[M.bc]||BCOND.nokill;",
    "function badgeList(){\n  if(M.cos)return [['완벽한 위장','한 번도 의심받지 않는다',function(){return !(S.inv>0);}],['제한 시간',mmss(M.par)+' 안에 빠져나온다',function(){return S.t<=M.par;}],['원테이크','되돌리지 않고 끝까지',function(){return loads===0;}]];\n  var c=BCOND[M.bc]||BCOND.nokill;")
rep("function mBack(){msHide();if(M.story)storyAgent(M.story.id);else if(M.winter)winter();else menu();}",
    "function mBack(){msHide();if(M.story)storyAgent(M.story.id);else if(M.winter)winter();else if(M.cos)costume();else menu();}")
rep("<img src=\"a_'+o.id+'_'+(st?(k+MI)%2:(M.ops.length>1?6+((k+MI)%2):7))+'.jpg\" style=\"object-position:'+fp('a_'+o.id+'_'+(st?(k+MI)%2:(M.ops.length>1?6+((k+MI)%2):7))+'.jpg')+'\" alt=\"\">",
    "<img src=\"'+(M.cos?M.img:'a_'+o.id+'_'+(st?(k+MI)%2:(M.ops.length>1?6+((k+MI)%2):7))+'.jpg')+'\" style=\"object-position:'+(M.cos?'50% 12%':fp('a_'+o.id+'_'+(st?(k+MI)%2:(M.ops.length>1?6+((k+MI)%2):7))+'.jpg'))+'\" alt=\"\">")
rep("[['퀵로드',load,true],['처음부터',restart],['미션 선택',function(){if(M.story)storyMenu();else menu();}]]",
    "[['퀵로드',load,true],['처음부터',restart],['미션 선택',function(){if(M.story)storyMenu();else if(M.cos)costume();else if(M.winter)winter();else menu();}]]")
rep("  }else{if(DIFF>=2){var hn=0;bl.forEach(",
    "  }else if(M.cos){var cid=M.ops[0].id;rwl='코스튬 리워드 컷';rwi='r_'+M.key+'_0.jpg';rwt=fresh?'<em class=\"k\">기본 컷 1장이 블랙박스에 담겼다</em> · 나머지 '+(cN(cid)-1)+'장은 블랙박스에서 포인트로 소장':'<span style=\"color:var(--dim)\">소장 '+cOwn(cid)+' / '+cN(cid)+' · 블랙박스 코스튬 갤러리</span>';\n"
    "  }else{if(DIFF>=2){var hn=0;bl.forEach(")
rep("var b=[['다시 도전',restart,true],['미션 선택',M.story?storyMenu:M.winter?winter:menu]];",
    "var b=[['다시 도전',restart,true],['미션 선택',M.story?storyMenu:M.winter?winter:M.cos?costume:menu]];")
# 10. 서버 상태: 코스튬 컷 소장
rep("else if(a[0]==='n')(PROG.n[a[1]]||(PROG.n[a[1]]=[]))[+a[2]]=true;});",
    "else if(a[0]==='n')(PROG.n[a[1]]||(PROG.n[a[1]]=[]))[+a[2]]=true;else if(a[0]==='c')(PROG.cs[a[1]]||(PROG.cs[a[1]]=[]))[+a[2]]=true;});")
rep("var K=kIdx();PROG.c={};PROG.s={};PROG.b={};PROG.hb={};PROG.g={};PROG.end={};PROG.n={};",
    "var K=kIdx();PROG.c={};PROG.s={};PROG.b={};PROG.hb={};PROG.g={};PROG.end={};PROG.n={};PROG.cs={};")
# 11. 코스튬 갤러리: 클리어 시 0번 무료, 나머지 포인트 구매(컷당 50P, 남은 컷 전부는 컷당 30P)
old = s[s.index("function cAll(){"):s.index("function svcMi(k){")]
new = u"""function cN(id){return 4+CRX[id];}
function cAll(){var a=0;Object.keys(CRX).forEach(function(id){a+=cN(id);});return a;}
function cCleared(id){return CMAP[id]!=null&&!!PROG.c[CMAP[id]];}
function cHas(id,k){return GOD()||(cCleared(id)&&(k===0||!!((PROG.cs&&PROG.cs[id]||[])[k])));}
function cOwn(id){var n=0;for(var k=0;k<cN(id);k++)if(cHas(id,k))n++;return n;}
function cOpen(){var a=0;Object.keys(CRX).forEach(function(id){a+=cOwn(id);});return a;}
var CCOST=50,CBULK=30;
function cLeft(id){return (cN(id)-cOwn(id))*CBULK;}
function cBuy(id,k,re){
  var all=k==='all',cost=all?cLeft(id):CCOST,g,i;k=all?0:+k;if(!cCleared(id)||(!all&&cHas(id,k))||(all&&!cLeft(id)))return;if(!PROG.cs)PROG.cs={};g=PROG.cs[id]||(PROG.cs[id]=[]);
  if((PROG.pt||0)<cost){toast('포인트가 모자란다. '+cost+'P가 필요하고 지금 '+(PROG.pt||0)+'P다.');return;}
  if(sb&&USER){if(SBBUSY||SBQ.length){toast('방금 작전 기록을 올리는 중이다. 잠시 뒤에 다시.');qFlush();return;}
    rpc('s6_buy_cut',{p_kind:'c',p_agent:id,p_k:k}).then(function(st){applyState(st);snd('ok');toast('리워드 컷을 소장했다.');re();}).catch(function(e){toast(/not enough/.test(''+(e&&e.message))?'포인트가 모자란다.':'서버와 닿지 않는다. 잠시 뒤에 다시.');});return;}
  PROG.pt-=cost;if(all)for(i=1;i<cN(id);i++)g[i]=true;else g[k]=true;saveProg();snd('ok');toast('리워드 컷을 소장했다.');re();
}
function cImg(id,k){return k<4?'r_C-'+id+'_'+k+'.jpg':'r_C-'+id+'_3_'+(k-3)+'.jpg';}
function cGrid(id,A,re){var cl=cCleared(id),o='<div class="fill g22 more">',n=cN(id);
  for(var k=0;k<n;k++){var op=cHas(id,k),lb=k<4?CRN[k]:CRN[3]+' '+(k-2);
    if(!op&&cl)A[k]=(function(q){return function(){cBuy(id,q,re);};})(k);
    o+=cd(op?99:k,cImg(id,k),lb,op?'':cl?CCOST+'P로 소장':(k?'클리어 후 포인트로 소장':'코스튬 미션 클리어'),{kv:1,view:op?1:0,lock:!op,tag:op?'':cl?CCOST+'P':'LOCKED'});}
  o+='</div>';
  if(cl&&cLeft(id)&&!GOD()){A[90]=function(){cBuy(id,'all',re);};o+='<button class="cta" data-k="90">남은 '+(n-cOwn(id))+'장 모두 소장 · '+cLeft(id)+'P</button>';}
  return o;}
"""
s = s.replace(old, new)
rep("'+(GOD()?4+CRX[id]:0)+' / '+(4+CRX[id])+' · 전체 '+cOpen()+' / '+cAll()+'</u></div>'+cGrid(id);",
    "'+cOwn(id)+' / '+cN(id)+' · 전체 '+cOpen()+' / '+cAll()+'</u></div>'+cGrid(id,CA,bbKeep(bbSeasonal));")
rep("  var G=[['WINTER','블러디 크리스마스',WIDX],['SPECIAL','코스튬 미션','C']],g=Math.min(SCP.g,G.length-1),X=G[g];\n  var h='<div class=\"chips\">'",
    "  var G=[['WINTER','블러디 크리스마스',WIDX],['SPECIAL','코스튬 미션','C']],g=Math.min(SCP.g,G.length-1),X=G[g],CA=[];\n  var h='<div class=\"chips\">'")
rep("page('시즈널 · 스페셜','BLACK BOX // SEASONAL',h,blackbox,[],function(e){scTap(e,bbSeasonal);});fit();",
    "page('시즈널 · 스페셜','BLACK BOX // SEASONAL',h,blackbox,CA,function(e){scTap(e,bbSeasonal);});fit();")
rep("var VERSION='0.44.0';", "var VERSION='0.45.0';")
io.open(P, 'w', encoding='utf8').write(s); print('index patched')

# items.js: 코스튬 메뉴 → 플레이 가능
Q = '/home/claude/silent_six/public/items.js'; t = io.open(Q, encoding='utf8').read()
a0 = t.index("W.costume=function(){"); a1 = t.index("/* ── 밸런스 컨트롤 타이머")
t = t[:a0] + u"""W.costume=function(){
  var kv=W.KVI.special?'kv_special.jpg':'a_mirage_0.jpg',has=ckHas(),god=W.GOD(),acts=[];
  var cards=Object.keys(W.STORY).map(function(id,k){var cur=id===CCUR.id,mi=W.CMAP[id],can=mi!=null&&(god||(cur&&has)),clr=mi!=null&&!!W.PROG.c[mi];
    acts[k]=function(){if(can)W.brief(mi);else if(cur)W.toast('코스튬 진입키가 있어야 입장합니다.');else W.toast('지금 열린 코스튬 미션이 아닙니다.');};
    return W.cd(k,'kc_'+id+'.jpg',W.OPD[id].n+' · '+(W.CSTT[id]||''),cur?(clr?'클리어 · 다시 도전':has||god?'입장 가능':'진입키 필요'):god?'관리자 · 테스트 입장':'예정',{kv:1,w:1,eye:cur?'NOW · '+CCUR.n:'DRESS CODE',tag:clr?'CLEAR':cur?'NOW':god?'TEST':'SOON',on:cur||god?1:0,lock:!can});}).join('');
  acts[99]=store;
  W.page('코스튬 미션','SPECIAL // COSTUME',
    '<div class="cwarn"><b>'+ico('key',14)+' 한정 운영</b>다음 코스튬 미션이 열리면 이번 코스튬 미션은 더 이상 플레이할 수 없습니다.</div>'+
    '<div class="hero big"><span class="bg" style="'+W.bgs(kv)+'"></span><div><i class="hk">COSTUME · '+CCUR.id.toUpperCase()+'</i><b class="ht2">옷이 바뀌면<br>작전도 바뀌어.</b><small>무기는 없다. 옷 하나와 말 몇 마디로 들어간다</small></div></div>'+
    W.intro('Special · Costume','Costume Mission','무기 없이 코스튬만 입고 들어갑니다. 현장의 두 사람과 대화해 정보를 얻고, 똑같은 셋 중 진짜를 챙겨 나옵니다.<br>코스튬 진입키가 있어야 입장하며, 다음 코스튬 미션이 열릴 때까지 무제한으로 플레이합니다.','* 클리어하면 리워드 컷 1장이 블랙박스에 담기고, 나머지는 포인트로 소장합니다.')+
    '<div class="cg">'+cards+'</div>'+
    (has?'<button class="cta off">'+ico('key',16)+' 진입키 보유 · '+CCUR.n+'</button>':'<button class="cta" data-k="99">'+ico('key',16)+' 코스튬 진입키 구매 · '+(ITEMS[0].priceText||won(ITEMS[0].p))+'</button>'),
    W.special,acts);
};

""" + t[a1:]
io.open(Q, 'w', encoding='utf8').write(t); print('items patched')
