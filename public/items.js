/* SILENT SIX — 스토어 아이템 · 코스튬 진입키 · 구독
   index.html의 전역 함수를 감싸서(patch) 동작을 더한다. index.html 뒤에 로드한다.
   아이템 보유: PROG.it = {ck:{시즌키:true}, bc:수량, bcEnd:종료시각(ms), auto:수량, tb:수량, inv:true, sub:{on,next}} */
(function(){
'use strict';
var W=window;

/* ── 아이콘 (게임 안 표기용, currentColor) ── */
var IC={
  key:'<path d="M7.5 9a5.5 5.5 0 1 1 4.9 5.47L10.8 16H9v2H7v2H3v-3.6l5.1-5.1A5.5 5.5 0 0 1 7.5 9zm5.5-2a2 2 0 1 0 0 4 2 2 0 0 0 0-4z"/>',
  bc:'<path d="M12 4a10 10 0 0 0-10 10h3a7 7 0 0 1 14 0h3A10 10 0 0 0 12 4zm4.6 4.6-5.3 4.1a1.6 1.6 0 1 0 2 2l4.1-5.3z"/><path d="M2 16h20v2H2z"/>',
  auto:'<path d="M12 3a9 9 0 1 0 9 9h-2.2A6.8 6.8 0 1 1 12 5.2V8l4-3.9L12 0z" transform="translate(0 1)"/><path d="M10 9v6l5-3z"/>',
  tb:'<path d="M6 2h12v2h-1.5v3.2L13.3 12l3.2 4.8V20H18v2H6v-2h1.5v-3.2L10.7 12 7.5 7.2V4H6zm3.5 2v2.6L12 10.4l2.5-3.8V4z"/>',
  inv:'<path d="M2.3 3.7 3.7 2.3l18 18-1.4 1.4-3.3-3.3A10.8 10.8 0 0 1 12 20C6.5 20 2.6 15.6 1 12a13 13 0 0 1 4.1-5.3zM12 4c5.5 0 9.4 4.4 11 8a13 13 0 0 1-3.3 4.6l-3.1-3.1A4.5 4.5 0 0 0 10.5 7.4L8.3 5.2A10.6 10.6 0 0 1 12 4z"/>',
  sub:'<path d="M3 7l4.5 4L12 4l4.5 7L21 7l-2 11H5zm2 13h14v2H5z"/>'
};
function ico(k,s){return '<svg class="ic" viewBox="0 0 24 24" width="'+(s||16)+'" height="'+(s||16)+'" fill="currentColor" aria-hidden="true">'+IC[k]+'</svg>';}
IC.ck=IC.key;
W.itIcon=ico;

/* ── 현재 코스튬 미션 (다음 코스튬이 열리면 k를 바꾼다 → 이전 키로는 입장 불가) ── */
var CCUR={k:'C1',id:'doc',t:'왕진',n:'코스튬 미션 #1'};
W.CCUR=CCUR;

/* ── 상품 카탈로그 (인앱결제 대응: 가격 · SKU · 지급 내용을 데이터로 둔다) ──
   type: consumable(수량) / nonconsumable(영구) / season(현재 시즌 한정 영구) / subscription(월 자동결제)
   sku: 스토어 등록 상품 ID. 네이티브 결제가 붙으면 이 값으로 결제를 요청한다.
   grant: 결제 성공 시 지급 내용. price는 표시용 기본값이며 스토어가 내려준 현지 가격(priceText)이 있으면 그 값을 쓴다. */
var BC_MS=30*60*1000,TB_S=180,INV_N=2,INV_K=0.3;
var SUBG={bc:2,auto:5,tb:10}; /* 구독 매월 지급 */
var ITEMS=[
  {k:'ck',id:'s6.costume_key',type:'season',sku:{ios:'s6_costume_key',android:'s6_costume_key'},grant:{ck:1},n:'코스튬 진입키',e:'COSTUME KEY',p:11900,
   d:'진행 중인 코스튬 미션에 입장한다. 언제 사도 지금 열린 코스튬 미션에 쓰이고, 다음 코스튬 미션이 열릴 때까지 무제한으로 플레이한다.'},
  {k:'bc',id:'s6.balance_control',type:'consumable',sku:{ios:'s6_balance_control',android:'s6_balance_control'},grant:{bc:1},n:'밸런스 컨트롤',e:'BALANCE CONTROL',p:12900,
   d:'활성화하면 30분 동안 작동한다. 파워 난이도로 클리어하면 하드 · 헬까지 함께 클리어로 기록된다. 작동 중에는 화면 우측 상단에 남은 시간이 뜬다.'},
  {k:'auto',id:'s6.auto_play',type:'consumable',sku:{ios:'s6_auto_play',android:'s6_auto_play'},grant:{auto:3},n:'오토 플레이 3회',e:'AUTO PLAY ×3',p:9900,
   d:'3회분. 미션 화면 우측 상단 ITEM에서 사용한다. 클리어할 때까지 요원이 스스로 반복 플레이한다. 한 미션에 1회 차감. 다른 아이템과 함께 쓸 수 있다.'},
  {k:'tb',id:'s6.time_breaker',type:'consumable',sku:{ios:'s6_time_breaker',android:'s6_time_breaker'},grant:{tb:1},n:'타임 브레이커',e:'TIME BREAKER',p:3300,
   d:'사용하면 3분 동안 미션 시간이 멈춘다. 1회 차감. 다른 아이템과 함께 쓸 수 있다.'},
  {k:'inv',id:'s6.invisible_agent',type:'nonconsumable',sku:{ios:'s6_invisible_agent',android:'s6_invisible_agent'},grant:{inv:1},n:'인비저블 에이전트',e:'INVISIBLE AGENT',p:29900,
   d:'영구 적용. 미션마다 적 2명을 골라 그 적의 시야를 30%로 줄인다. 미션 화면 우측 상단 ITEM에서 고른다.'},
  {k:'sub',id:'s6.six_pass',type:'subscription',sku:{ios:'s6_six_pass_monthly',android:'s6_six_pass_monthly'},grant:{sub:1},period:30,n:'식스 패스',e:'SIX PASS · 월 구독',p:39900,
   d:'매월 자동 결제. 코스튬 진입키 + 밸런스 컨트롤 2회(30분) + 오토 플레이 5회 + 타임 브레이커 10회 + 포인트 획득 +20%. 설정에서 언제든 해지한다.'}
];
W.ITEMS=ITEMS;

/* ── 결제 어댑터 ──
   admin  : 수퍼관리자 무료 지급(무제한)
   native : 앱 래퍼가 window.S6IAP = {purchase(sku,type)→Promise<{receipt}>, restore()→Promise<[{sku,receipt}]>, products(skus)→Promise<[{sku,priceText}]>} 를 넣으면 자동 사용
   none   : 결제 미연결 → 안내만
   결제 성공 → verify(서버 영수증 검증 훅, 서버 연결 전엔 통과) → grantItem(지급) → 구매 기록 */
var PAY={
  provider:function(){if(W.SUPER())return 'admin';if(W.S6IAP&&W.S6IAP.purchase)return 'native';return 'none';},
  platform:function(){var u=(navigator.userAgent||'');return /iPhone|iPad|iPod/.test(u)?'ios':/Android/.test(u)?'android':'web';},
  purchase:function(x){var pv=PAY.provider();
    if(pv==='admin')return Promise.resolve({src:'admin',receipt:null});
    if(pv==='native'){var sku=x.sku[PAY.platform()]||x.sku.android;return W.S6IAP.purchase(sku,x.type).then(function(r){return {src:'native',sku:sku,receipt:r&&r.receipt};});}
    return Promise.reject(new Error('결제는 준비 중입니다. 곧 열립니다.'));},
  verify:function(x,r){ /* 서버 검증 훅: Supabase RPC s6_iap_verify 가 생기면 여기서 호출 */
    if(r.src!=='native'||!W.sb||!W.rpc)return Promise.resolve(true);
    return W.rpc('s6_iap_verify',{p_product:x.id,p_sku:r.sku,p_receipt:r.receipt}).then(function(v){return v!==false;}).catch(function(){return true;});},
  prices:function(){if(!W.S6IAP||!W.S6IAP.products)return;var pf=PAY.platform();W.S6IAP.products(ITEMS.map(function(x){return x.sku[pf]||x.sku.android;})).then(function(L){(L||[]).forEach(function(q){ITEMS.forEach(function(x){if((x.sku[pf]||x.sku.android)===q.sku)x.priceText=q.priceText;});});}).catch(function(){});},
  restore:function(){if(!W.S6IAP||!W.S6IAP.restore)return Promise.resolve(0);return W.S6IAP.restore().then(function(L){var n=0;(L||[]).forEach(function(q){ITEMS.forEach(function(x){if(x.type!=='consumable'&&(x.sku.ios===q.sku||x.sku.android===q.sku)){grantItem(x,'restore');n++;}});});return n;});}
};
W.S6PAY=PAY;
function it(){var P=W.PROG;if(!P.it)P.it={ck:{},bc:0,bcEnd:0,auto:0,tb:0,inv:false,sub:null};if(!P.it.ck)P.it.ck={};return P.it;}
W.itState=it;
function won(n){return '₩'+n.toLocaleString();}
function now(){return Date.now();}
function bcLeft(){return Math.max(0,(it().bcEnd||0)-now());}
function subOn(){var s=it().sub;return !!(s&&(s.on||now()<s.next));}
function ckHas(){return W.SUPER()||subOn()||!!it().ck[CCUR.k];}
W.ckHas=ckHas;W.subOn=subOn;W.bcLeft=bcLeft;
function hms(ms){var s=Math.ceil(ms/1000),h=Math.floor(s/3600),m=Math.floor(s%3600/60),x=s%60;return h+':'+(m<10?'0':'')+m+':'+(x<10?'0':'')+x;}
function ms2(s){s=Math.ceil(s);return Math.floor(s/60)+':'+(s%60<10?'0':'')+s%60;}
function own(k){var I=it();
  if(k==='ck')return ckHas()?'보유 · '+CCUR.n:'';
  if(k==='bc')return (I.bc?'보유 '+I.bc+'회':'')+(bcLeft()?(I.bc?' · ':'')+'작동 중 '+hms(bcLeft()):'');
  if(k==='auto'||k==='tb')return I[k]?'보유 '+I[k]+'회':'';
  if(k==='inv')return I.inv?'영구 적용 중':'';
  if(k==='sub')return subOn()?(I.sub.on?'구독 중 · 다음 결제 ':'해지됨 · 혜택 종료 ')+new Date(I.sub.next).toLocaleDateString('ko-KR'):'';
  return '';}

/* 구독 갱신: 결제일이 지나면 다음 달 혜택 지급(구독 중일 때만) */
function subGrant(I){I.bc+=SUBG.bc;I.auto+=SUBG.auto;I.tb+=SUBG.tb;}
function subTick(){var I=it(),s=I.sub;if(!s||!s.on)return;var n=0;while(now()>=s.next&&n++<12){s.next+=30*86400000;subGrant(I);}if(n)W.saveProg();}

function grantItem(x,src){
  var I=it(),g=x.grant;
  if(g.ck)I.ck[CCUR.k]=true;
  if(g.inv)I.inv=true;
  if(g.sub){I.sub={on:true,next:now()+(x.period||30)*86400000};subGrant(I);}
  ['bc','auto','tb'].forEach(function(q){if(g[q])I[q]=(I[q]||0)+g[q];});
  (I.log||(I.log=[])).push({id:x.id,at:now(),src:src});if(I.log.length>200)I.log.shift();
  W.saveProg();
}
function buy(k){
  var x=ITEMS.filter(function(q){return q.k===k;})[0],I=it();if(!x)return;
  if(x.type==='subscription'&&subOn()&&I.sub.on){W.toast('이미 구독 중입니다.');return;}
  if(x.type==='nonconsumable'&&I.inv&&k==='inv'){W.toast('이미 보유 중입니다.');return;}
  PAY.purchase(x).then(function(r){return PAY.verify(x,r).then(function(ok){if(!ok)throw new Error('결제를 확인하지 못했습니다.');grantItem(x,r.src);W.toast(x.n+(r.src==='admin'?' 지급 완료 (관리자 무료)':' 구매 완료'));store();});})
   .catch(function(e){W.toast((e&&e.message)||'결제가 취소됐습니다.');});
}
function bcOn(){var I=it();if(bcLeft()){W.toast('이미 작동 중입니다.');return;}if(!I.bc){W.toast('밸런스 컨트롤이 없습니다.');return;}I.bc--;I.bcEnd=now()+BC_MS;W.saveProg();W.toast('밸런스 컨트롤 작동 · 30분');pill();store();}

/* ── 스토어 화면: 2열 카드 ── */
function store(){
  var acts=[],h=W.intro('Silent Six Store','Store','작전을 돕는 장비. 결제는 준비 중이며, 지금은 관리자만 무료로 받을 수 있습니다.')+'<div class="stg">';
  ITEMS.forEach(function(x,i){
    var o=own(x.k),im='st_'+x.k+'.jpg',pr=x.priceText||won(x.p);
    h+='<div class="stc"><div class="sti" style="background-image:url('+im+')"><span>'+ico(x.k,34)+'</span></div><div class="stb"><i>'+x.e+'</i><b>'+x.n+'</b><details class="std"><summary>설명</summary><p>'+x.d+'</p></details>'+(o?'<small>'+o+'</small>':'')+'<strong>'+pr+(x.type==='subscription'?'<em> / 월</em>':'')+'</strong>'+
      '<button class="stbuy" data-k="'+acts.length+'">'+(W.SUPER()?'무료 받기':x.type==='nonconsumable'&&it().inv?'보유 중':'구매')+'</button>'+(x.k==='bc'&&it().bc&&!bcLeft()?'<button class="stbuy alt" data-k="'+(acts.length+1)+'">활성화</button>':'')+'</div></div>';
    acts.push(function(){buy(x.k);});if(x.k==='bc')acts.push(bcOn);
  });
  h+='</div><p class="stn">수량 아이템(밸런스 컨트롤 · 오토 플레이 · 타임 브레이커)은 여러 개 살 수 있고 서로 함께 쓸 수 있습니다.</p>';
  if(W.S6IAP&&W.S6IAP.restore){h+='<button class="stbuy alt" data-k="'+acts.length+'">구매 복원</button>';acts.push(function(){PAY.restore().then(function(n){W.toast(n?'구매 '+n+'건을 복원했습니다.':'복원할 구매가 없습니다.');store();});});}
  W.page('스토어','STORE // SPECIAL OPS SUPPLY',h,W.shop,acts);
}
W.store=store;

/* 기존 SHOP의 스토어 카드 → 스토어 화면 */
W.shop=function(){
  W.page('SHOP','POINT · BADGE · STORE','<p><em class="k">사일런트 식스에 공짜는 없어.</em> 쓰고 싶다면 벌고, 벌고 싶다면 참전하라!</p><div class="cg">'+W.cd(0,'a_viper_0.jpg','스토어','진입키 · 밸런스 컨트롤 · 오토 · 구독',{w:1,eye:'STORE',tag:'OPEN',on:1})+W.cd(1,'a_glitch_0.jpg','포인트샵','100점에 1P · 번 만큼만 쓴다',{eye:'POINT · P '+(W.PROG.pt||0).toLocaleString(),tag:'SOON'})+W.cd(2,'a_mirage_0.jpg','배지샵','증거를 내면 옷이 나온다',{eye:'BADGE · ◆ '+W.badgeTotal(),tag:'SOON'})+'</div>',W.home,[store,function(){},function(){}]);
};

/* ── 코스튬 미션: 진입키 게이트 + 교체 안내 강조 ── */
W.costume=function(){
  var kv=W.KVI.special?'kv_special.jpg':'a_mirage_0.jpg',has=ckHas();
  var cards=Object.keys(W.STORY).map(function(id,k){var cur=id===CCUR.id;return W.cd(k,'kc_'+id+'.jpg',W.OPD[id].n,(W.CSTT[id]||'')+(cur?' · 진행 중':' · 예정'),{kv:1,w:1,eye:cur?'NOW · '+CCUR.n:'DRESS CODE',tag:cur?'NOW':'SOON',on:cur?1:0,lock:!cur});}).join('');
  W.page('코스튬 미션','SPECIAL // COSTUME',
    '<div class="cwarn"><b>'+ico('key',14)+' 한정 운영</b>다음 코스튬 미션이 열리면 이번 코스튬 미션은 더 이상 플레이할 수 없습니다.</div>'+
    '<div class="hero big"><span class="bg" style="'+W.bgs(kv)+'"></span><div><i class="hk">COSTUME · '+CCUR.id.toUpperCase()+'</i><b class="ht2">옷이 바뀌면<br>작전도 바뀌어.</b><small>끝까지 살아 나오면 그 옷은 요원의 옷장에 걸린다</small></div></div>'+
    W.intro('Special · Costume','Costume Mission','코스튬 진입키가 있어야 입장합니다. 언제 사도 지금 열린 코스튬 미션에 쓰이며, 다음 코스튬 미션이 열릴 때까지 무제한으로 플레이합니다.')+
    '<div class="cg">'+cards+'</div>'+
    (has?'<button class="cta off">'+ico('key',16)+' 진입키 보유 · 미션 준비 중</button>':'<button class="cta" data-k="99">'+ico('key',16)+' 코스튬 진입키 구매 · '+(ITEMS[0].priceText||won(ITEMS[0].p))+'</button>'),
    W.special,(function(){var a=[];a[99]=store;return a;})());
};

/* ── 밸런스 컨트롤 타이머: 화면 우측 상단 상시 표시 ── */
var PL=null;
function pill(){
  if(!PL){PL=document.createElement('div');PL.id='bcp';document.body.appendChild(PL);}
  var l=bcLeft(),inGame=W.started&&$('app').className!=='pre';
  document.body.classList.toggle('bcon',!!l&&!inGame);
  if(!l||inGame){PL.className='hide';return;}
  PL.className='';PL.innerHTML=ico('bc',14)+'<b>BALANCE</b>'+hms(l);
}
function $(i){return document.getElementById(i);}
setInterval(function(){try{pill();subTick();}catch(e){}},1000);
try{PAY.prices();}catch(e){}

/* ── 미션 상태 ── */
var AU={on:false,tries:0,mi:-1},INVSEL=false;
W.AU=AU;
var _load=W.loadMission;W.loadMission=function(i){if(AU.mi!==i){AU.on=false;AU.tries=0;}INVSEL=false;POPEN=false;try{panel();}catch(e){}return _load(i);};

/* 인비저블: 시야 0.3 */
var _sr=W.senseRange;W.senseRange=function(g,o){var r=_sr(g,o);return g.iv?r*INV_K:r;};
var _cone=W.cone;W.cone=function(g,r){return _cone(g,g.iv?r*INV_K:r);};
var _cs=W.canSee;
var _tap=W.onTap;W.onTap=function(px,py){
  if(INVSEL&&W.started&&W.S&&!W.S.over){
    var ix=(px-W.W/2)/W.cam.z+W.cam.x,iy=(py-W.H/2)/W.cam.z+W.cam.y,best=46,gh=null;
    W.S.guards.forEach(function(g){if(g.down||g.iv)return;var q=W.gp(g),d=Math.hypot(q[0]-ix,q[1]-(g.cam?22:30)-iy);if(d<best){best=d;gh=g;}});
    if(gh){gh.iv=true;W.S.ivs=(W.S.ivs||0)+1;W.pop(gh.x,gh.y,'시야 30%','#9be8ff');W.snd('ok');if(W.S.ivs>=INV_N)INVSEL=false;}
    else W.say('시야를 줄일 적을 탭하세요.');
    return;
  }
  return _tap(px,py);
};

/* 타임 브레이커: 시간 정지 */
var _upd=W.update;
function upd(dt){
  if(W.S.tb>0){var t0=W.S.t;W.S.tb=Math.max(0,W.S.tb-dt);_upd(dt);W.S.t=t0;}
  else _upd(dt);
}
var AUTO_M=0.04; /* 오토 은신 보정: 발각 게이지 상승 배율 */
W.update=function(dt){
  if(AU.on&&AU.mi===W.MI){var m0=W.DF.m;W.DF.m=m0*AUTO_M*Math.pow(0.6,Math.min(AU.tries,8));try{autoTick(dt);upd(dt);if(!W.S.over){autoTick(dt);upd(dt);}}finally{W.DF.m=m0;}} /* 오토: 2배속 */
  else upd(dt);
};

/* ── 오토 플레이: 은신 우선 자동 조종 ── */
var FP=W.followPath;W.followPath=function(o,sp,dt,tn){if(o.hold)return;return FP(o,sp,dt,tn);};
function danger(o,x,y){var S=W.S;for(var i=0;i<S.guards.length;i++){var g=S.guards[i];if(g.down||g.off>0)continue;if(_cs(g,x,y,W.senseRange(g,o)*1.25))return true;}return false;}
function idle(o){return !o.cur&&!o.queue.length&&!(o.path&&o.path.length);}
function give(o,a){o.queue=[a];o.cur=null;o.path=[];o.aim=0;o.hold=false;o.ht0=0;}
/* 길이 막혔으면 부술 수 있는 벽(W)을 찾는다 */
function breachFor(o,tx,ty){var S=W.S;if(W.findPath(Math.floor(o.x),Math.floor(o.y),tx,ty))return null;var best=null,bd=1e9;
  for(var y=0;y<W.ROWS;y++)for(var x=0;x<W.COLS;x++){if(W.cell(x,y)!=='W')continue;S.open[y*W.COLS+x]=1;var ok=W.findPath(Math.floor(o.x),Math.floor(o.y),tx,ty);delete S.open[y*W.COLS+x];if(ok){var d=Math.hypot(x-o.x,y-o.y);if(d<bd){bd=d;best={type:'breach',x:x,y:y};}}}
  return best;}
function giveTo(o,a,tx,ty){var b=breachFor(o,tx,ty);give(o,b||a);}
function nearOp(x,y,ok){var S=W.S,b=null,bd=1e9;S.ops.forEach(function(o){if(ok&&!ok(o))return;var d=Math.hypot(o.x-x,o.y-y);if(d<bd){bd=d;b=o;}});return b;}
function autoTick(dt){
  var S=W.S,M=W.M,i;if(!S||S.over)return;
  AU.acc=(AU.acc||0)+dt;
  /* 은신 이동: 앞길 2칸이 시야 안이면 최대 3초 멈춰 기다린다 */
  S.ops.forEach(function(o){
    if(o.carry<0&&!o.crouch){o.crouch=true;o.disg=false;}
    if(o.path&&o.path.length&&!danger(o,o.x,o.y)){
      var risk=false,k;for(k=0;k<Math.min(2,o.path.length);k++)if(danger(o,o.path[k].x,o.path[k].y)){risk=true;break;}
      if(risk){if(!o.hold){o.hold=true;o.ht0=0;}o.ht0+=dt;if(o.ht0>(o.hm||(o.hm=2+Math.random()*4))){o.hold=false;o.ht0=-1.5;o.hm=0;}}
      else o.hold=false;
    }else o.hold=false;
    var c=o.cur;if(c&&c.type==='ko'){var g=S.guards[c.id];if(g&&!g.down){var d=Math.hypot(g.x-o.x,g.y-o.y);o.hold=d<2.6&&_cs(g,o.x,o.y,W.RANGE);}}
  });
  if(AU.acc<0.4)return;AU.acc=0;
  var h=S.hostage;
  if(h&&!h.free){var r=S.ops[0];if(idle(r))giveTo(r,{type:'move',x:Math.floor(h.x),y:Math.floor(h.y)},Math.floor(h.x),Math.floor(h.y));return;}
  if(M.subs&&!W.subsDone()){
    for(i=0;i<M.subs.length;i++){if(S.subs[i])continue;var sb=M.subs[i];
      var busy=S.ops.some(function(o){var a=o.cur||o.queue[0];return a&&((a.type==='sub'&&a.i===i)||(a.type==='ko'&&a.id===S.radio&&(sb.k==='radio'||sb.k==='mark')));});if(busy)continue;
      if(sb.k==='radio'||sb.k==='mark'){if(S.radio>=0){var rg=S.guards[S.radio];var ko=nearOp(rg.x,rg.y,idle);if(ko){give(ko,{type:'ko',id:S.radio,kill:true});ko.queue.push({type:'pick',id:S.radio});}}continue;}
      var tx=sb.use?sb.use[0]+0.5:sb.x,ty=sb.use?sb.use[1]+0.5:sb.y,op=sb.by?S.ops.filter(function(o){return o.id===sb.by&&idle(o);})[0]:nearOp(tx,ty,idle);
      if(op)giveTo(op,{type:'sub',i:i},sb.use?sb.use[0]:Math.floor(tx),sb.use?sb.use[1]:Math.floor(ty));
    }
    return;
  }
  if(M.objective&&!S.objDone){
    if(W.objWait()>0)return;
    var doing=S.ops.some(function(o){var a=o.cur||o.queue[0];return a&&a.type==='sab';});
    if(!doing){var u=M.objective.use,ob=nearOp(u[0]+0.5,u[1]+0.5,idle);if(ob)giveTo(ob,{type:'sab'},u[0],u[1]);}
    return;
  }
  if(M.evac&&!S.ev)return;
  var E=W.exits();if(!E.length)return;
  S.ops.forEach(function(o,k){if(!idle(o)||W.inExit(o))return;var e=E[k%E.length];giveTo(o,{type:'move',x:e[0],y:e[1]},e[0],e[1]);});
}
var _end=W.showEnd;W.showEnd=function(){
  if(AU.on&&AU.mi===W.MI&&W.S.over&&!W.S.over.win){AU.tries++;W.toast('오토 플레이 · 재시도 '+AU.tries);setTimeout(function(){if(AU.on&&W.S&&W.S.over&&!W.S.over.win){var iv=W.S.guards.filter(function(g){return g.iv;}).map(function(g){return g.id;}),tb=W.S.tb||0;W.restart();iv.forEach(function(id){W.S.guards[id].iv=true;});W.S.ivs=iv.length;W.S.tb=tb;}},1300);return;}
  if(W.S.over&&W.S.over.win&&AU.on){AU.on=false;}
  return _end();
};

/* ── 밸런스 컨트롤: 파워 클리어 → 하드 · 헬 기록 ── */
var _res=W.result;W.result=function(){
  var ap=bcLeft()>0&&W.DIFF===1&&W.S&&W.S.over&&W.S.over.win;
  if(ap){
    var MI=W.MI,s=Math.floor(W.S.t),sc=W.scoreCalc(),P=W.PROG,pc=P.c[MI]||(P.c[MI]={}),ps=P.s[MI]||(P.s[MI]={}),MU=[0.6,0.8,1,1.5],hn=0;
    W.badgeList().forEach(function(b){if(b[2]())hn++;});
    [2,3].forEach(function(k){var v=Math.round(sc.score/sc.mult*MU[k]);if(!(pc[k]<=s))pc[k]=s;if(!(ps[k]>=v))ps[k]=v;try{W.sbClear(W.M.key,k,s,v,0,null);}catch(e){}});
    if(!P.hb)P.hb={};if(!(P.hb[MI]>=hn))P.hb[MI]=hn;
  }
  var pt0=W.PROG.pt||0;
  _res();
  var add=0;if(subOn()){add=Math.round(((W.PROG.pt||0)-pt0)*0.2);W.PROG.pt+=add;}
  if(ap||add){W.saveProg();var tb=document.querySelector('#ovx table');if(tb){var tr=document.createElement('tr');tr.innerHTML='<td>'+(ap?'밸런스 컨트롤':'식스 패스')+'</td><td><em class="k">'+(ap?'HARD · HELL 클리어로 함께 기록':'')+(ap&&add?' · ':'')+(add?'포인트 +'+add+' P (+20%)':'')+'</em></td>';tb.appendChild(tr);}}
};

/* ── 미션 화면 우측 상단: ITEM 버튼 하나 + 작동 중 상태 한 줄 + 펼침 패널 ── */
var TK='',PK='',POPEN=false;
function tray(){
  var tr=document.querySelector('#top .tr');if(!tr)return;
  var el=$('itm');if(!el){el=document.createElement('button');el.id='itm';tr.appendChild(el);el.addEventListener('click',function(e){e.stopPropagation();POPEN=!POPEN;PK='';panel();});}
  var st=$('its');if(!st){st=document.createElement('div');st.id='its';document.getElementById('top').appendChild(st);}
  var S=W.S,l=bcLeft(),chips=[];
  if(l)chips.push(['bc',hms(l)]);
  if(AU.on&&AU.mi===W.MI)chips.push(['auto','AUTO'+(AU.tries?' '+AU.tries:'')]);
  if(S&&S.tb>0)chips.push(['tb',ms2(S.tb)]);
  if(S&&S.ivs)chips.push(['inv',S.ivs+'/'+INV_N]);
  if(INVSEL)chips.push(['inv','적 선택']);
  var h=chips.map(function(c){return '<span>'+ico(c[0],12)+c[1]+'</span>';}).join('');
  if(h!==TK){TK=h;st.innerHTML=h;}
  var on=chips.length>0,lab=ico('sub',14)+'ITEM';
  if(el.dataset.on!==String(on)||!el.innerHTML){el.innerHTML=lab+(on?'<i></i>':'');el.dataset.on=String(on);}
  el.className=POPEN?'sel':'';
  if(POPEN)panel();
}
function rows(){
  var S=W.S,I=it(),G=W.SUPER(),l=bcLeft(),n=function(v){return G?'∞':v+'회';};
  var R=[];
  R.push(['auto','오토 플레이',AU.on&&AU.mi===W.MI?'자동 진행 중':'보유 '+n(I.auto),AU.on&&AU.mi===W.MI?'정지':'사용',!(G||I.auto>0)&&!AU.on]);
  R.push(['tb','타임 브레이커',S&&S.tb>0?'시간 정지 '+ms2(S.tb):'보유 '+n(I.tb),S&&S.tb>0?'작동 중':'사용',(S&&S.tb>0)||!(G||I.tb>0)]);
  if(I.inv||G){var left=INV_N-((S&&S.ivs)||0);R.push(['inv','인비저블',left>0?'이번 미션 '+left+'명 남음':'이번 미션 모두 사용',INVSEL?'취소':'적 선택',left<=0]);}
  R.push(['bc','밸런스 컨트롤',l?'작동 중 '+hms(l):'보유 '+n(I.bc),l?'작동 중':'활성화',!!l||!(G||I.bc>0)]);
  return R;
}
function panel(){
  var p=$('itp');
  if(!POPEN){if(p)p.className='hide';return;}
  if(!p){p=document.createElement('div');p.id='itp';document.getElementById('top').parentNode.appendChild(p);
    p.addEventListener('click',function(e){e.stopPropagation();var b=e.target.closest('button');if(!b||b.disabled)return;act(b.dataset.it);PK='';panel();});
    document.addEventListener('click',function(e){if(POPEN&&!e.target.closest('#itp')&&!e.target.closest('#itm')){POPEN=false;panel();}},true);}
  var h=rows().map(function(r){return '<div class="itr">'+ico(r[0],18)+'<div><b>'+r[1]+'</b><small>'+r[2]+'</small></div><button data-it="'+r[0]+'"'+(r[4]?' disabled':'')+'>'+r[3]+'</button></div>';}).join('')+'<p>모든 아이템은 함께 쓸 수 있습니다.</p>';
  if(h!==PK){PK=h;p.innerHTML=h;}p.className='';
}
function act(k){
  var S=W.S,I=it(),G=W.SUPER();if(!W.started||!S||S.over)return;
  if(k==='auto'){
    if(AU.on){AU.on=false;S.ops.forEach(function(o){o.hold=false;});W.toast('오토 플레이 정지');return;}
    if(!G){if(I.auto<1){W.toast('오토 플레이가 없습니다.');return;}I.auto--;W.saveProg();}
    AU.on=true;AU.mi=W.MI;AU.tries=0;POPEN=false;W.toast('오토 플레이 시작 · 클리어할 때까지 반복');return;}
  if(k==='tb'){if(S.tb>0)return;if(!G){if(I.tb<1){W.toast('타임 브레이커가 없습니다.');return;}I.tb--;W.saveProg();}S.tb=TB_S;POPEN=false;W.toast('타임 브레이커 · 3분 동안 시간 정지');return;}
  if(k==='inv'){if((S.ivs||0)>=INV_N)return;INVSEL=!INVSEL;POPEN=false;if(INVSEL)W.toast('시야를 줄일 적을 탭하세요 · '+(INV_N-(S.ivs||0))+'명');return;}
  if(k==='bc'){if(bcLeft())return;if(!G){if(I.bc<1)return;I.bc--;}I.bcEnd=now()+BC_MS;W.saveProg();POPEN=false;W.toast('밸런스 컨트롤 작동 · 30분');}
}
var _hud=W.hud;W.hud=function(){_hud();try{tray();}catch(e){}};

/* ── 설정: 구독 해지 ── */
var _set=W.settings;W.settings=function(){
  _set();
  var pb=document.querySelector('#pg .pb');if(!pb)return;var I=it();
  var d=document.createElement('div');d.innerHTML='<label>구독</label><div class="row"><span>식스 패스<small>'+(subOn()?(I.sub.on?'구독 중 · 다음 결제 '+new Date(I.sub.next).toLocaleDateString('ko-KR'):'해지됨 · '+new Date(I.sub.next).toLocaleDateString('ko-KR')+'까지 혜택'):'구독하지 않음 · 월 '+(ITEMS[5].priceText||won(ITEMS[5].p)))+'</small></span><button id="ssubx">'+(subOn()&&I.sub.on?'구독 해지':'스토어')+'</button></div>';
  pb.insertBefore(d,pb.firstChild.nextSibling);
  d.querySelector('#ssubx').onclick=function(e){e.stopPropagation();if(subOn()&&I.sub.on){if(W.confirm&&!W.confirm('식스 패스를 해지할까요? 다음 결제일까지 혜택은 유지됩니다.'))return;I.sub.on=false;W.saveProg();W.toast('구독을 해지했습니다.');W.settings();}else store();};
};

/* ── 스타일 ── */
var css=document.createElement('style');css.textContent=[
'.ic{display:inline-block;vertical-align:-3px;flex:none}',
'.stg{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:6px 0 12px}',
'.stc{background:#11171e;border:1px solid rgba(255,255,255,.07);clip-path:var(--cut);display:flex;flex-direction:column;min-width:0}',
'.sti{aspect-ratio:4/3;background:#0d1218 center/cover no-repeat;position:relative;display:flex;align-items:center;justify-content:center;color:var(--c);background-blend-mode:normal}',
'.sti span{width:58px;height:58px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:radial-gradient(circle,rgba(255,59,82,.22),rgba(255,59,82,0) 70%);box-shadow:0 0 0 1px rgba(255,59,82,.35) inset}',
'.stb{padding:10px 10px 12px;display:flex;flex-direction:column;gap:4px;flex:1}',
'.stb i{font-style:normal;font-size:9px;letter-spacing:.22em;color:var(--c);font-weight:700}',
'.stb b{font-size:15px;color:var(--ink)}',
'.stb p{font-size:11.5px;line-height:1.5;color:#aab4be;margin:6px 0 0}',
'.std{flex:1}.std summary{list-style:none;cursor:pointer;font-size:11.5px;color:var(--dim);display:inline-flex;align-items:center;gap:4px}.std summary::-webkit-details-marker{display:none}.std summary::after{content:"▾";font-size:10px}.std[open] summary::after{content:"▴"}',
'.stb small{font-size:11px;color:#9be8ff}',
'.stb strong{font-size:17px;color:var(--ink);margin-top:4px}.stb strong em{font-style:normal;font-size:11px;color:var(--dim)}',
'.stbuy{margin-top:6px;padding:9px 0;background:var(--c);color:#fff;border:0;font-weight:800;font-size:13px;clip-path:var(--cut)}',
'.stbuy.alt{background:transparent;color:var(--c);box-shadow:0 0 0 1px var(--c) inset;margin-top:4px}',
'.stbuy *,.stc .sti *{pointer-events:none}',
'.stn{font-size:11.5px;color:var(--dim)}',
'.cwarn{margin:0 0 12px;padding:10px 12px;background:rgba(255,59,82,.12);border-left:3px solid var(--c);font-size:13px;line-height:1.5;color:var(--ink)}',
'.cwarn b{display:block;color:var(--c);font-size:11px;letter-spacing:.14em;margin-bottom:2px}',
'.cta .ic{margin-right:6px}',
'body.bcon #pg .ph>span{margin-right:118px}',
'#bcp{position:fixed;right:12px;top:calc(env(safe-area-inset-top) + 12px);z-index:45;display:flex;align-items:center;gap:6px;padding:6px 10px;background:rgba(10,14,19,.9);border:1px solid var(--c);color:var(--c);font-size:12px;font-weight:700;font-variant-numeric:tabular-nums;clip-path:var(--cut);pointer-events:none}',
'#bcp b{font-size:9px;letter-spacing:.2em}#bcp.hide{display:none}',
"#itm{pointer-events:auto;position:relative;display:inline-flex;align-items:center;gap:5px;height:30px;margin-left:8px;padding:0 10px;background:rgba(10,14,19,.72);border:1px solid rgba(255,255,255,.2);color:var(--ink);font-size:11px;font-weight:800;letter-spacing:.14em;clip-path:var(--cut)}",
"#itm.sel{border-color:var(--c);color:var(--c)}#itm i{position:absolute;top:4px;right:4px;width:6px;height:6px;border-radius:50%;background:var(--c)}#itm *{pointer-events:none}",
"#its{position:absolute;right:12px;top:calc(100% - 18px);display:flex;gap:6px;justify-content:flex-end;pointer-events:none}",
"#its span{display:inline-flex;align-items:center;gap:4px;height:20px;padding:0 7px;background:rgba(10,14,19,.75);border:1px solid var(--c);color:var(--c);font-size:11px;font-weight:700;font-variant-numeric:tabular-nums}",
"#itp{position:absolute;right:12px;top:calc(env(safe-area-inset-top) + 58px);z-index:6;width:236px;padding:6px;background:rgba(10,14,19,.96);border:1px solid rgba(255,255,255,.12);clip-path:var(--cut);box-shadow:0 10px 30px rgba(0,0,0,.5)}",
"#app.pre #itp,#itp.hide{display:none}#itp p{margin:4px 6px 2px;font-size:10.5px;color:var(--dim)}",
".itr{display:flex;align-items:center;gap:10px;padding:8px 6px;border-bottom:1px solid rgba(255,255,255,.06);color:var(--c)}",
".itr div{flex:1;min-width:0}.itr b{display:block;font-size:13px;color:var(--ink)}.itr small{display:block;font-size:11px;color:var(--dim);font-variant-numeric:tabular-nums}",
".itr button{min-width:54px;height:28px;padding:0 8px;background:var(--c);color:#fff;border:0;font-size:12px;font-weight:800;clip-path:var(--cut)}",
".itr button:disabled{background:rgba(255,255,255,.08);color:var(--dim)}"
].join('\n');document.head.appendChild(css);
})();
