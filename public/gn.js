/* 로맨틱 그래픽 노블 엔진 — 스크롤로 넘기는 세로 컷 노블. 데이터는 gn_data.js(GN). */
(function(){
var css=`
#gnv *{box-sizing:border-box}
#gnv{position:fixed;inset:0;z-index:30;background:#050507;overflow-y:auto;overflow-x:hidden;-webkit-overflow-scrolling:touch;overscroll-behavior:contain;color:#f3eee9;font-family:"Apple SD Gothic Neo","Noto Sans KR",system-ui,sans-serif;--gc:#FF3B52}
#gnv.hide{display:none}
#gnv .gs{position:fixed;inset:0;overflow:hidden;background:#000;pointer-events:none}
#gnv .gbd{position:absolute;inset:-40px;background-size:cover;background-position:center;filter:blur(34px) brightness(.38) saturate(1.2)}
#gnv .gfr{position:absolute;top:0;bottom:0;left:50%;width:min(100vw,66.7vh);transform:translateX(-50%);overflow:hidden}
#gnv .gl{position:absolute;inset:0;opacity:0;transition:opacity 1.1s ease}
#gnv .gl.on{opacity:1}
#gnv .gl img{width:100%;height:100%;object-fit:cover;object-position:center 30%;display:block;will-change:transform,filter,opacity}
#gnv .gl.pulse img{animation:gnpulse 2.6s ease-in-out infinite}
@keyframes gnpulse{0%,100%{scale:1}14%{scale:1.012}28%{scale:1}42%{scale:1.008}}
#gnv .gvg{position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 35%,transparent 45%,rgba(0,0,0,.6) 100%),linear-gradient(to bottom,rgba(0,0,0,.4) 0,transparent 18%,transparent 48%,rgba(0,0,0,.93) 100%)}
#gnv .grd{position:absolute;inset:0;background:#c4102a;mix-blend-mode:multiply;opacity:0;transition:opacity 1.2s}
#gnv .gfk{position:absolute;inset:0;background:radial-gradient(70% 50% at 20% 40%,rgba(255,150,60,.35),transparent 70%);mix-blend-mode:screen;opacity:0;transition:opacity 1s}
#gnv .gfk.on{opacity:1;animation:gnflk 3.1s infinite}
@keyframes gnflk{0%,100%{filter:brightness(1)}12%{filter:brightness(.55)}18%{filter:brightness(1.15)}40%{filter:brightness(.8)}55%{filter:brightness(1.05)}70%{filter:brightness(.6)}}
#gnv .gwm{position:absolute;inset:0;opacity:0;transition:opacity 2s;background:radial-gradient(90% 60% at 80% 20%,rgba(255,170,110,.3),transparent 70%)}
#gnv .gwm.on{opacity:1}
#gnv canvas{position:absolute;inset:0;width:100%;height:100%;opacity:0;transition:opacity 1.5s}
#gnv canvas.on{opacity:.55}
#gnv .gbk{position:absolute;inset:0;background:#000;opacity:1;transition:opacity 1.2s}
#gnv .gtt{position:fixed;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;pointer-events:none;opacity:0;transition:opacity .9s;padding:0 24px}
#gnv .gtt.on{opacity:1}
#gnv .gtt i{font-style:normal;font-size:11px;letter-spacing:.55em;color:var(--gc);margin-bottom:20px}
#gnv .gtt b{font-family:"Noto Serif KR","AppleMyungjo",serif;font-weight:800;font-size:clamp(34px,10vw,72px);letter-spacing:.04em;line-height:1.15;text-shadow:0 0 40px rgba(0,0,0,.6);word-break:keep-all}
#gnv .gtt u{text-decoration:none;margin-top:20px;font-family:"Noto Serif KR","AppleMyungjo",serif;font-size:14px;color:#a39a95;letter-spacing:.06em;word-break:keep-all}
#gnv .gtt s{display:block;width:1px;height:60px;background:linear-gradient(var(--gc),transparent);margin-top:28px;text-decoration:none}
#gnv .gbx{position:fixed;left:50%;transform:translateX(-50%);bottom:0;width:min(100vw,620px);padding:0 24px calc(34px + env(safe-area-inset-bottom));pointer-events:none;transition:opacity .5s}
#gnv .gbx.mid{bottom:auto;top:50%;transform:translate(-50%,-50%);padding-bottom:0}
#gnv .gln{opacity:0;transform:translateY(14px);filter:blur(4px);transition:opacity .8s,transform .8s,filter .8s;margin-top:14px;line-height:1.85;font-size:16px;text-shadow:0 1px 14px rgba(0,0,0,.95);word-break:keep-all}
#gnv .gln.on{opacity:1;transform:none;filter:none}
#gnv .gln.n{color:#ddd5cf;font-family:"Noto Serif KR","AppleMyungjo",serif;font-size:15.5px}
#gnv .gbx.mid .gln.n{font-size:16.5px;line-height:2}
#gnv .gln.r b{display:block;font-size:11px;letter-spacing:.34em;color:var(--gc);font-weight:700;margin-bottom:2px}
#gnv .gln.r span{font-family:"Noto Serif KR","AppleMyungjo",serif;font-weight:600;font-size:18px}
#gnv .gln.s{font-size:12px;color:#a39a95;letter-spacing:.18em}
#gnv .gch{display:flex;flex-direction:column;gap:8px;pointer-events:auto}
#gnv .gch button{font:inherit;font-size:15px;text-align:left;color:#f3eee9;background:rgba(10,8,10,.62);border:1px solid color-mix(in srgb,var(--gc) 55%,transparent);border-radius:3px;padding:12px 14px;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
#gnv .gch button::before{content:'▸ ';color:var(--gc)}
#gnv .gch button.pk{background:color-mix(in srgb,var(--gc) 24%,transparent);border-color:var(--gc)}
#gnv .gch button.ot{opacity:.3}
#gnv .ghd{position:fixed;top:0;left:0;right:0;padding:calc(10px + env(safe-area-inset-top)) 14px 10px;display:flex;align-items:center;gap:10px;font-size:11px;letter-spacing:.24em;color:#a39a95;background:linear-gradient(rgba(0,0,0,.65),transparent)}
#gnv .ghd button{background:none;border:0;color:#fff;font-size:24px;line-height:1;padding:2px 6px}
#gnv .ghd span{flex:1;text-align:center}
#gnv .gbar{position:fixed;top:0;left:0;height:2px;background:var(--gc);width:0;box-shadow:0 0 10px var(--gc)}
#gnv .ght{position:fixed;bottom:calc(12px + env(safe-area-inset-bottom));left:50%;transform:translateX(-50%);font-size:11px;letter-spacing:.3em;color:#a39a95;transition:opacity .6s;animation:gnbob 2s ease-in-out infinite}
@keyframes gnbob{50%{margin-bottom:-6px}}
#gnv .gend{position:relative;background:linear-gradient(transparent,#050507 18vh);padding:32vh 18px calc(70px + env(safe-area-inset-bottom));text-align:center}
#gnv .gend h3{font-family:"Noto Serif KR","AppleMyungjo",serif;font-size:30px;letter-spacing:.06em;margin:0}
#gnv .gend p{color:#a39a95;margin-top:10px;font-size:12px;letter-spacing:.16em}
#gnv .gend .gb{display:flex;gap:8px;justify-content:center;margin:26px 0 40px;flex-wrap:wrap}
#gnv .gend .gb button{font:inherit;color:#f3eee9;background:none;border:1px solid color-mix(in srgb,var(--gc) 60%,transparent);padding:11px 16px;font-size:13px;letter-spacing:.1em}
#gnv .ggl{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;max-width:760px;margin:0 auto}
#gnv .ggl img{width:100%;aspect-ratio:2/3;object-fit:cover;display:block;opacity:0;transform:translateY(18px);transition:opacity .6s,transform .6s}
#gnv .ggl img.on{opacity:1;transform:none}
#pg .gnh{position:relative;aspect-ratio:2/3;max-height:62vh;margin:0 auto 14px;border-radius:12px;overflow:hidden;background:#000}
#pg .gnh img{width:100%;height:100%;object-fit:cover;object-position:center 25%;display:block}
#pg .gnh div{position:absolute;left:0;right:0;bottom:0;padding:60px 16px 16px;background:linear-gradient(transparent,rgba(0,0,0,.9))}
#pg .gnh i{font-style:normal;font-size:11px;letter-spacing:.3em}
#pg .gnh b{display:block;font-family:"Noto Serif KR","AppleMyungjo",serif;font-size:28px;margin-top:4px}
#pg .gnh u{display:block;text-decoration:none;color:#cfc7c1;font-size:13px;margin-top:6px}
#pg .gng{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}
#pg .gng button{padding:0;border:0;background:#111;border-radius:8px;overflow:hidden;aspect-ratio:2/3;position:relative}
#pg .gng img{width:100%;height:100%;object-fit:cover;display:block}
#pg .gng button.lk img{filter:blur(14px) brightness(.4)}
#pg .gng button.lk::after{content:'LOCKED';position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:11px;letter-spacing:.3em;color:#fff}
@media (min-width:900px){#gnv .gbx{padding-bottom:46px}#gnv .gln{font-size:17px}#gnv .gln.r span{font-size:19.5px}}
`;
var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
var lk=document.createElement('link');lk.rel='stylesheet';lk.href='https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;600;800&display=swap';document.head.appendChild(lk);

var COVER={raven:13,viper:12,glitch:6,brick:6,mirage:5,doc:3};
/* 로맨틱 갤러리: 노블을 끝까지 읽어야 열린다. 핵심 컷 · 노출 컷만 */
var GAL={raven:[3,7,9,11,13,15,16,17,18,21,24,26],viper:[1,3,4,6,8,12,13,16],glitch:[1,5,6,7,9,10,12],brick:[3,4,6,8,9,10,12],mirage:[1,4,5,6,8,9,10],doc:[1,3,4,5,6,8]};
window.gnRead=function(id){return GOD()||!!(PROG.gnr&&PROG.gnr[id]);};
function markRead(id){if(PROG.gnr&&PROG.gnr[id])return;if(!PROG.gnr)PROG.gnr={};PROG.gnr[id]=true;try{saveProg();}catch(e){}try{toast('로맨틱 갤러리가 열렸다.');}catch(e){}}
function pad(n){return (n<10?'0':'')+n;}
function gimg(id,n){return 'gn/'+id+'_'+pad(n)+'.jpg';}
window.gnHas=function(id){return !!GN[id]&&nRight(id);};
window.gnTitle=function(id){return GN[id]?GN[id].t:'그날 밤';};
window.gnCover=function(id){return GN[id]?gimg(id,COVER[id]||1):'e_'+id+'.jpg';};
window.gnCount=function(){var n=0;Object.keys(GN).forEach(function(id){if(gnHas(id))n++;});return n;};
window.gnLibCover=function(){var ids=Object.keys(GN);for(var i=0;i<ids.length;i++)if(gnHas(ids[i]))return gnCover(ids[i]);return 'kv_romantic.jpg';};

/* 블랙박스 > 로맨틱 그래픽 노블: 시즌 → 요원 → 읽기 · 갤러리 */
window.gnLib=function(){
  var ids=Object.keys(STORY).filter(function(id){return GN[id];}),A=[];
  var h='<div class="chips">'+SEASONS.map(function(x,i){return '<button data-ss="'+i+'" class="'+(i===SCP.s?'sel':'')+(i?' off':'')+'"><i>'+x.k+'</i>'+x.n+'</button>';}).join('')+'</div>';
  if(SCP.s===0){
    h+='<div class="cap"><i>S1</i>로맨틱 그래픽 노블<u>'+gnCount()+' / '+ids.length+'편 열림</u></div><div class="cg one">'+ids.map(function(id,k){var op=gnHas(id),g=GN[id];A.push(function(){gnAgent(id);});
      return cd(k,op?gnCover(id):'e_'+id+'.jpg',g.t,op?g.sub+(gnRead(id)?' · 갤러리 ♥':' · 끝까지 읽으면 갤러리'):'로맨틱 미션 TAKE 1 · 2 · 3을 HARD 이상으로 · '+nHard(id)+' / 3',{kv:1,w:1,eye:OPD[id].n+' · THAT NIGHT',lock:!op,tag:op?'READ':'LOCKED',on:op?1:0});}).join('')+'</div>';
  }else h+=scEmpty(SEASONS[SCP.s].k+' · '+SEASONS[SCP.s].n+'<br>시즌이 공개되면 이곳에 그래픽 노블이 쌓입니다.');
  page('로맨틱 그래픽 노블','BLACK BOX // ROMANTIC',h,blackbox,A,function(e){scTap(e,gnLib);});
};
window.gnAgent=function(id){
  var g=GN[id],op=gnHas(id),n=g.cnt,h='';
  h+='<div class="gnh"><img src="'+(op?gnCover(id):'e_'+id+'.jpg')+'" alt=""><div><i style="color:'+g.col+'">'+OPD[id].n+' · S1 ROMANTIC</i><b>'+g.t+'</b><u>'+g.sub+'</u></div></div>';
  h+=op?'<button class="cta" data-k="0">그래픽 노블 읽기</button>':'<button class="cta off" data-k="0">로맨틱 미션 TAKE 1 · 2 · 3 HARD↑ · '+nHard(id)+' / 3</button>';
  var L=GAL[id]||[],rd=op&&gnRead(id);
  h+='<label>ROMANTIC GALLERY — '+(rd?L.length:0)+' / '+L.length+'</label>'+(rd?'':'<p style="color:var(--dim);font-size:13px">'+(op?'그래픽 노블을 끝까지 읽으면 열립니다.':'그래픽 노블이 열린 뒤, 끝까지 읽으면 열립니다.')+'</p>')+'<div class="gng">';
  L.forEach(function(i){var f=gimg(id,i);h+='<button'+(rd?' data-view="'+f+'"':' class="lk"')+'><img loading="lazy" src="'+f+'" alt=""></button>';});
  h+='</div>';
  page(g.t,'GRAPHIC NOVEL // '+OPD[id].n,h,gnLib,[function(){if(op)ending(id,function(){gnAgent(id);});}]);
};

/* 플레이어 */
var V=null,S={};
function el(t,c,p){var e=document.createElement(t);if(c)e.className=c;if(p)p.appendChild(e);return e;}
window.gnPlay=function(id,back){
  var g=GN[id];if(!g){if(back)back();return;}
  if(!V){V=el('div','hide');V.id='gnv';document.body.appendChild(V);
    V.addEventListener('scroll',function(){if(!S.tk){S.tk=1;requestAnimationFrame(function(){S.tk=0;tick();});}},{passive:true});
    window.addEventListener('resize',function(){if(V.className!=='hide'){rs();tick();}});}
  V.innerHTML='';V.style.setProperty('--gc',g.col);S={id:id,g:g,back:back,cur:-1,front:null,img:null,pick:{}};
  var stg=el('div','gs',V);S.bd=el('div','gbd',stg);var fr=el('div','gfr',stg);
  S.la=el('div','gl',fr);el('img',null,S.la);S.lb=el('div','gl',fr);el('img',null,S.lb);S.front=S.la;
  S.rd=el('div','grd',fr);S.fk=el('div','gfk',fr);S.wm=el('div','gwm',fr);el('div','gvg',fr);
  S.cv=el('canvas',null,stg);S.bk=el('div','gbk',stg);
  S.tt=el('div','gtt',V);S.tt.innerHTML='<i></i><b></b><u></u><s></s>';
  S.bx=el('div','gbx',V);S.bar=el('div','gbar',V);
  var hd=el('div','ghd',V);hd.innerHTML='<button aria-label="닫기">‹</button><span>'+OPD[id].n+'</span><span style="flex:0;width:30px"></span>';hd.firstChild.onclick=close;S.sc=hd.children[1];
  S.ht=el('div','ght',V);S.ht.textContent='SCROLL';
  var tr=el('div',null,V);
  g.b.forEach(function(b){var n=(b.L||[]).length,s=el('section',null,tr);s.style.height=(b.t==='title'?115:Math.max(140,80+n*72))+'vh';b.el=s;});
  var end=el('section','gend',V);end.innerHTML='<h3>— '+g.t+' —</h3><p>'+OPD[id].n.toUpperCase()+' · THAT NIGHT · END</p><div class="gb"><button data-a="top">처음부터</button><button data-a="out">닫기</button></div><p style="margin-bottom:14px">로맨틱 갤러리가 열렸다 · '+(GAL[id]||[]).length+'컷</p><div class="ggl"></div>';
  end.querySelector('[data-a="top"]').onclick=function(){V.scrollTo({top:0,behavior:'smooth'});};
  end.querySelector('[data-a="out"]').onclick=close;
  var gl=end.querySelector('.ggl'),i;(GAL[id]||[]).forEach(function(n){var im=el('img',null,gl),f=gimg(id,n);im.loading='lazy';im.src=f;im.onclick=function(){viewer(f,true);};});
  S.end=end;
  try{S.io&&S.io.disconnect();S.io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)e.target.classList.add('on');});},{root:V,threshold:.15});[].forEach.call(gl.children,function(x){S.io.observe(x);});}catch(e){}
  for(i=1;i<=g.cnt;i++){var pre=new Image();pre.src=gimg(id,i);}
  try{pgHide();}catch(e){}try{hmHide();}catch(e){}
  V.className='';V.scrollTop=0;rs();act(0);tick();loop();
};
function close(){if(!V)return;V.className='hide';V.innerHTML='';S.dead=1;var b=S.back;S={};if(b)b();else storyMenu();try{navSync();}catch(e){}}
function setImg(n){var f=gimg(S.id,n);if(f===S.img)return;S.img=f;var back=S.front===S.la?S.lb:S.la,im=back.firstChild;im.style.transform='';im.style.filter='';im.style.opacity='';
  var done=0,show=function(){if(done||S.img!==f)return;done=1;back.classList.add('on');S.front.classList.remove('on');S.front=back;};im.onload=show;im.src=f;if(im.complete&&im.naturalWidth)show();S.bd.style.backgroundImage='url('+f+')';}
function box(i){var b=S.g.b[i],bx=S.bx;bx.innerHTML='';b.nodes=[];bx.className='gbx'+(b.t==='black'?' mid':'');
  (b.L||[]).forEach(function(l,k){var d=el('div','gln '+l[0],bx);
    if(l[0]==='r'){d.innerHTML='<b></b><span></span>';d.firstChild.textContent=S.g.n;d.lastChild.textContent=l[1];}
    else if(l[0]==='c'){d.innerHTML='<div class="gch"></div><div class="gln r" style="margin-top:12px"><b></b><span></span></div>';var ch=d.firstChild,rp=d.lastChild;rp.firstChild.textContent=S.g.n;
      var ap=function(){var j=S.pick[i+'-'+k];if(j==null)return;[].forEach.call(ch.children,function(x,m){x.className=m===j?'pk':'ot';});rp.lastChild.textContent=l[1][j][1];requestAnimationFrame(function(){rp.classList.add('on');});};
      l[1].forEach(function(o,j){var bt=el('button',null,ch);bt.textContent=o[0];bt.onclick=function(){S.pick[i+'-'+k]=j;ap();};});ap();}
    else d.textContent=l[1];b.nodes.push(d);});}
function act(i){S.cur=i;var b=S.g.b[i],fx=b.fx||[];
  S.tt.classList.toggle('on',b.t==='title');if(b.t==='title'){S.tt.children[0].textContent=b.no;S.tt.children[1].textContent=b.tt;S.tt.children[2].textContent=b.sub||'';}
  if(b.i)setImg(b.i);if(b.ghost)setImg(b.ghost);
  S.bk.style.opacity=b.t==='cg'?0:(b.ghost?.84:1);S.bk.style.background=b.red?'#1a0206':'#000';
  S.rd.style.opacity=fx.indexOf('red')>=0?.38:(b.red?.6:0);
  S.fk.classList.toggle('on',fx.indexOf('flk')>=0);
  [S.la,S.lb].forEach(function(l){l.classList.toggle('pulse',fx.indexOf('pulse')>=0);});
  var warm=!!(b.warm||b.fx==='warm');S.wm.classList.toggle('on',warm);S.cv.classList.toggle('on',S.g.fx!=='none'&&!warm);
  var tb=null;for(var q=i;q>=0;q--)if(S.g.b[q].t==='title'){tb=S.g.b[q];break;}S.sc.textContent=tb&&/^\d/.test(tb.no)?tb.no+' · '+tb.tt:S.g.n+' · '+S.g.t;
  box(i);}
var MV={in:[1.14,1,0,0,0,0],out:[1,1.12,0,0,0,0],up:[1.1,1.1,0,0,3.5,-3.5],down:[1.1,1.1,0,0,-3.5,3.5],left:[1.12,1.12,3,-3,0,0]};
function ease(t){return t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2;}
function tick(){if(!V||V.className==='hide'||!S.g)return;var y=V.scrollTop,H=V.clientHeight,B=S.g.b,i=0;
  for(var k=0;k<B.length;k++)if(B[k].el.offsetTop<=y+H*.5)i=k;if(i!==S.cur)act(i);
  var b=B[i],p=Math.min(1,Math.max(0,(y+H*.5-b.el.offsetTop)/b.el.offsetHeight)),im=S.front.firstChild;
  if(b.t==='cg'){var m=MV[b.mv||'in'],sc=m[0]+(m[1]-m[0])*p,tx=m[2]+(m[3]-m[2])*p,ty=m[4]+(m[5]-m[4])*p,org='50% 30%';
    if(b.det){org=b.det[0]+'% '+b.det[1]+'%';sc=b.det[2]*(1+.06*p);}
    im.style.transformOrigin=org;im.style.transform='translate('+tx+'%,'+ty+'%) scale('+sc+')';
    var fx=b.fx||[],f='',o=1,e=ease(Math.min(1,p/.75));
    if(fx.indexOf('sil')>=0)f+='brightness('+(.06+.94*e)+') contrast('+(1.4-.4*e)+') saturate('+e+') ';
    if(fx.indexOf('half')>=0)f+='brightness('+(.35+.25*p)+') contrast(1.25) ';
    if(fx.indexOf('blur')>=0)f+='blur('+((1-e)*16)+'px) ';
    if(fx.indexOf('dim')>=0)o=.08+.92*e;if(fx.indexOf('out')>=0)o=1-.9*ease(Math.max(0,(p-.3)/.7));
    im.style.filter=f.trim();im.style.opacity=o;}
  if(b.t==='black'&&b.ghost){im.style.transform='scale('+(1.05+.08*p)+')';im.style.filter='grayscale(.6) blur(2px)';im.style.opacity=1;}
  if(b.t==='title'){var t=S.tt.children[1];t.style.transform='translateY('+((.5-p)*70)+'px)';t.style.opacity=1-Math.abs(p-.5)*1.6;}
  var ns=b.nodes||[],n=ns.length;ns.forEach(function(d,k){var on=p>(k+.25)/(n+.5);if(on!==d.classList.contains('on'))d.classList.toggle('on',on);});
  var vis=ns.filter(function(d){return d.classList.contains('on');}),keep=b.t==='black'?5:3;ns.forEach(function(d){d.style.display='';});
  if(vis.length>keep)vis.slice(0,vis.length-keep).forEach(function(d){d.style.display='none';});
  var tot=V.scrollHeight-H;S.bar.style.width=(tot>0?y/tot*100:0)+'%';S.ht.style.opacity=y>H*.3?0:1;
  var past=y+H>S.end.offsetTop+H*.35;if(y+H>=S.end.offsetTop+H*.6)markRead(S.id);S.bx.style.opacity=past?0:1;S.tt.style.visibility=past?'hidden':'';}
/* 입자: rain snow dust code gold */
function rs(){if(!S.cv)return;var d=window.devicePixelRatio||1,c=S.cv;c.width=innerWidth*d;c.height=innerHeight*d;S.ctx=c.getContext('2d');
  var kind=S.g.fx,N=kind==='rain'?Math.min(220,innerWidth/4):kind==='code'?40:70;
  S.pt=[];for(var i=0;i<N;i++)S.pt.push({x:Math.random()*c.width,y:Math.random()*c.height,l:(10+Math.random()*22)*d,v:(kind==='rain'?9+Math.random()*10:kind==='snow'?.6+Math.random()*1.4:kind==='code'?1.5+Math.random()*2.5:.15+Math.random()*.5)*d,a:.12+Math.random()*.35,r:(1+Math.random()*2.2)*d,w:Math.random()*6.28,ch:String.fromCharCode(48+Math.floor(Math.random()*42))});}
function loop(){if(!S.g||S.dead||!V||V.className==='hide')return;var c=S.cv,x=S.ctx,k=S.g.fx,d=window.devicePixelRatio||1;
  if(x&&c.classList.contains('on')){x.clearRect(0,0,c.width,c.height);
    S.pt.forEach(function(p){
      if(k==='rain'){x.strokeStyle='rgba(200,210,230,'+p.a+')';x.lineWidth=d;x.beginPath();x.moveTo(p.x,p.y);x.lineTo(p.x-p.l*.12,p.y+p.l);x.stroke();p.y+=p.v;p.x-=p.v*.12;}
      else if(k==='snow'){p.w+=.02;x.fillStyle='rgba(235,232,255,'+(p.a+.2)+')';x.beginPath();x.arc(p.x,p.y,p.r,0,6.28);x.fill();p.y+=p.v;p.x+=Math.sin(p.w)*.6*d;}
      else if(k==='code'){x.fillStyle='rgba(63,224,224,'+p.a+')';x.font=(11*d)+'px monospace';x.fillText(p.ch,p.x,p.y);p.y+=p.v;if(Math.random()<.02)p.ch=String.fromCharCode(48+Math.floor(Math.random()*42));}
      else{p.w+=.01;x.fillStyle=(k==='gold'?'rgba(232,196,106,':'rgba(255,170,90,')+(p.a*.8)+')';x.beginPath();x.arc(p.x,p.y,p.r*.7,0,6.28);x.fill();p.y-=p.v;p.x+=Math.sin(p.w)*.4*d;}
      if(p.y>c.height+20){p.y=-p.l;p.x=Math.random()*c.width*1.1;}if(p.y<-20){p.y=c.height+10;p.x=Math.random()*c.width;}});}
  requestAnimationFrame(loop);}
})();
