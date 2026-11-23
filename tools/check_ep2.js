// 스토리 EP2(07~12판) 점검. 사용: cd public && STAGE=1..6 DIFF=2 node ../tools/check_ep2.js [static|idle|gen|tree|ko]
const fs=require('fs');const html=fs.readFileSync('index.html','utf8');const js=html.match(/<script>([\s\S]*?)<\/script>/)[1];
const noop=new Proxy(function(){},{get:(t,k)=>k==='length'?0:noop,apply:()=>noop,set:()=>true});
const el=()=>({textContent:'',className:'',innerHTML:'',src:'',style:{setProperty(){}},appendChild(){},addEventListener(){},setAttribute(){},getAttribute(){return ''},getContext:()=>noop,getBoundingClientRect:()=>({width:390,height:640,left:0,top:0})});
const els={};global.document={getElementById:id=>els[id]||(els[id]=el()),createElement:el,addEventListener(){},head:{appendChild(){}},body:{appendChild(){}}};global.window={devicePixelRatio:1,addEventListener(){}};global.requestAnimationFrame=()=>{};
(0,eval)(js);if(process.env.DIFF)setDiff(+process.env.DIFF);
const MI_=E2IDX[(+process.env.STAGE||1)-1],DT=1/32,KS=0.125;let PAD=+(process.env.PAD||0.3),LOUD=false;
function init(){loadMission(MI_);restart();S.ops.forEach(o=>o.crouch=true);}
function snaps(sec){const real=JSON.stringify(S),R0=RANGE,C0=CRANGE,E0=JSON.stringify(ENV);S.ops.forEach(o=>{o.x=-50;o.y=-50;o.path=[];o.queue=[];o.cur=null;});const out=[];const n=Math.round(sec/KS);
  for(let k=0;k<n;k++){out.push({R:RANGE,C:CRANGE,g:S.guards.filter(g=>!g.down&&!(g.off>0)).map(g=>({x:g.x,y:g.y,ang:g.ang,tower:g.tower,cam:g.cam,boss:g.boss}))});for(let i=0;i<4;i++)update(DT);}
  S=JSON.parse(real);RANGE=R0;CRANGE=C0;Object.assign(ENV,JSON.parse(E0));return out;}
function search(snap,sc,goals,dwell,minT){minT=minT||0; // sc: 시작 칸 index, goals:Set, dwell: 머무는 초
  const N=COLS*ROWS,NK=snap.length,NL=Math.floor(NK/2),memo=new Int8Array(N*NK).fill(-1),F0=FOV;
  const see=(x,y,k)=>{const s=snap[k];FOV=F0*1.15;let r=false;for(const g of s.g)if(canSee(g,x,y,(g.cam?CAMR:(LOUD?s.R:s.C)*(g.tower?1.4:1))+PAD)){r=true;break;}FOV=F0;return r;};
  const safe1=(c,k)=>{if(k>=NK)return false;let v=memo[c*NK+k];if(v<0){v=see(c%COLS+.5,Math.floor(c/COLS)+.5,k)?0:1;memo[c*NK+k]=v;}return v===1;};
  const safe=(c,k0,k1)=>{for(let k=k0;k<=k1;k++)if(!safe1(c,k))return false;return true;};
  const mid=(x,y,k0,k1)=>{for(let k=k0;k<=k1;k++){if(k>=NK||see(x,y,k))return false;}return true;};
  const par=new Int32Array(NL*N).fill(-1);par[sc]=-2;const dl=Math.ceil(dwell/0.25);
  for(let L=0;L<NL-4;L++)for(let c=0;c<N;c++){
    if(par[L*N+c]===-1)continue;
    if(goals.has(c)&&L*0.25>=minT&&safe(c,2*L,Math.min(NK-1,2*(L+dl)))&&2*(L+dl)<NK){const st=[];let l=L,cc=c;while(par[l*N+cc]!==-2){const p=par[l*N+cc],pc=p%N,pl=Math.floor(p/N);if(pc!==cc)st.unshift({t:pl*0.25,x:cc%COLS,y:Math.floor(cc/COLS)});l=pl;cc=pc;}return {steps:st,t:L*0.25,c};}
    if(safe(c,2*L,2*L+2)&&par[(L+1)*N+c]===-1)par[(L+1)*N+c]=L*N+c;
    const cx=c%COLS,cy=Math.floor(c/COLS);
    for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){const nx=cx+dx,ny=cy+dy;if(blocked(nx,ny))continue;const n=ny*COLS+nx;if(L+3>=NL||par[(L+3)*N+n]!==-1)continue;
      if(safe(c,2*L,2*L+3)&&safe(n,2*L,2*L+6)&&mid(cx+.5+dx/2,cy+.5+dy/2,2*L,2*L+5))par[(L+3)*N+n]=L*N+c;}
  }
  return null;
}
const ci=(o)=>Math.floor(o.y)*COLS+Math.floor(o.x);
function go(op,goals,dwell,horizon,act){ // 실제 엔진에서 이동
  const snap=snaps(horizon),r=search(snap,ci(S.ops[op]),goals,dwell);if(!r)return false;
  const t0=S.t;let i=0;const end=t0+r.t;
  while(S.t<end+0.01&&!S.over){while(i<r.steps.length&&t0+r.steps[i].t<=S.t+1e-6){const s=r.steps[i++];S.ops[op].queue=[{type:'move',x:s.x,y:s.y}];S.ops[op].cur=null;}update(DT);}
  for(let n=0;n<40&&S.ops[op].path.length&&!S.over;n++)update(DT);
  if(act){S.ops[op].queue=[act];S.ops[op].cur=null;const t1=S.t+dwell+0.5;while(S.t<t1&&!S.over)update(DT);}
  return !S.over;
}
const cellSet=(a)=>new Set(a.map(c=>c[1]*COLS+c[0]));
const mode=process.argv[2]||'all';let okAll=true;const say_=(n,ok,x)=>{console.log((ok?'OK   ':'FAIL ')+n+(x?'  '+x:''));if(!ok)okAll=false;};
if(mode==='static'||mode==='all'){init();
  const ok=(c,n)=>{const b=blocked(c[0],c[1]);say_('칸 '+n+' '+c,!b,b?cell(c[0],c[1]):'');};
  M.ops.forEach((o,k)=>ok([o.x,o.y],'시작'+k));(M.subs||[]).forEach(sb=>{if(sb.use)ok(sb.use,sb.label);});ok(M.objective.use,'본 목표');
  M.evac.gates.forEach(g=>g.cells.forEach(c=>ok(c,'출구 '+g.n)));M.guards.forEach((g,i)=>(g.wps||[]).forEach(w=>ok(w,'경비'+i)));
  const f=flood(M.ops[0].x,M.ops[0].y),reach=c=>f.prev[c[1]*COLS+c[0]]!==-1;
  const need=[].concat((M.subs||[]).filter(x=>x.use).map(x=>[x.use,x.label]),[[M.objective.use,'본 목표']],M.evac.gates.map(g=>[g.cells[0],g.n]),M.guards.filter(g=>!g.cam&&!g.tower).map((g,i)=>[g.wps[0],'경비 경유점']));
  need.forEach(([c,n])=>say_('도달 '+n+' '+c,reach(c)));}
if(mode==='idle'||mode==='all'){init();let t=0;while(S.t<60&&!S.over)update(DT);say_('idle 60s',!S.over,S.over?S.over.why:'');}
if(mode==='gen'||mode==='all'){init();M.subs.forEach((sb,si)=>{if(!sb.use&&!sb.shoot)return;for(let op=0;op<M.ops.length;op++){if(sb.by&&M.ops[op].id!==sb.by)continue;let ok=false;for(const pd of [0.5,0.3,0.15]){if(ok)break;PAD=pd;init();let goals=[sb.use];if(sb.shoot){goals=[];const tx=sb.x+(sb.w||1)/2,ty=sb.y+(sb.h||1)/2;for(let y=0;y<ROWS;y++)for(let x=0;x<COLS;x++)if(!blocked(x,y)&&Math.hypot(x+.5-tx,y+.5-ty)<=SNIPE-0.7&&los(x+.5,y+.5,tx,ty,true))goals.push([x,y]);}ok=go(op,cellSet(goals),(sb.shoot?AIM:sb.time)+0.6,200,{type:'sub',i:si})&&S.subs[si];}say_(sb.label+' op'+op,ok,'t='+S.t.toFixed(1)+(S.over?' '+S.over.why:''));}});}
if(mode==='tree'||mode==='all'){init();const NG=M.evac.gates.length;for(let gate=0;gate<NG;gate++){let won=false,t1=0;for(const pd of [0.5,0.3,0.7,0.15]){if(won)break;PAD=pd;init();M.evac.fix=gate;M.subs.forEach((sb,si)=>subDone(si));S.dq=null;S.msg=null;
  let ok=go(0,cellSet([M.objective.use]),M.objective.time+0.6,200,{type:'sab'});t1=S.t;
  if(ok&&S.objDone){for(let n=0;n<4;n++)update(DT);const E=cellSet(M.evac.gates[gate].cells);const snap=snaps(170);const rs=M.ops.map((o,k)=>{LOUD=k===0&&!!(M.evac.escort&&M.evac.escort.loud);const r=search(snap,ci(S.ops[k]),E,1);LOUD=false;return r;});
    if(rs.every(Boolean)){const tm=Math.max(...rs.map(r=>r.t));rs.forEach((r,k)=>{if(r.t<tm-0.5){LOUD=k===0&&!!(M.evac.escort&&M.evac.escort.loud);rs[k]=search(snap,ci(S.ops[k]),E,1,tm-0.25)||r;LOUD=false;}});
      const st=[].concat(...rs.map((r,k)=>r.steps.map(x=>({...x,op:k})))).sort((a,b)=>a.t-b.t);const t0=S.t;let i=0;const end=t0+Math.max(...rs.map(r=>r.t))+3;
      while(S.t<end&&!S.over){while(i<st.length&&t0+st[i].t<=S.t+1e-6){const q=st[i++];S.ops[q.op].queue=[{type:'move',x:q.x,y:q.y}];S.ops[q.op].cur=null;}update(DT);}}
    else console.log('   경로 없음',rs.map(Boolean).join());}
  won=!!(S.over&&S.over.win);}
  say_('상자 → '+M.evac.gates[gate].n,won,'상자 t='+t1.toFixed(1)+' 끝 t='+S.t.toFixed(1));}M.evac.fix=null;}
if((mode==='ko'||mode==='all')&&(init(),M.subs.some(x=>x.k==='radio'))){init();for(let r=0;r<3;r++){M.rfix=r;init();const gid=S.radio,base=JSON.stringify(S);let found=null;
  for(let T=4;T<180&&!found;T+=1){S=JSON.parse(base);
    // T초 시점 경비 위치 뒤쪽 2~4칸의 안전한 칸으로 가서 덮친다
    const sn=snaps(T+1),gs=sn[sn.length-8];const real=JSON.stringify(S);
    const tmp=JSON.parse(real);S=tmp;while(S.t<T)update(DT);const g=S.guards[gid];const gx=g.x,gy=g.y,ga=g.ang;S=JSON.parse(real);
    const cand=[];for(let d=1.5;d<=3.5;d+=1){const x=Math.floor(gx-Math.cos(ga)*d),y=Math.floor(gy-Math.sin(ga)*d);if(!blocked(x,y))cand.push([x,y]);}
    for(let dy=-3;dy<=3;dy++)for(let dx=-3;dx<=3;dx++){const x=Math.floor(gx)+dx,y=Math.floor(gy)+dy;if(!blocked(x,y)&&Math.hypot(dx,dy)<=3.2&&Math.hypot(dx,dy)>=1.5)cand.push([x,y]);}
    if(!cand.length)continue;const res=search(sn,ci(S.ops[0]),cellSet(cand),0.3);if(!res||res.t>T)continue;
    let i=0;while(S.t<T&&!S.over){while(i<res.steps.length&&res.steps[i].t<=S.t+1e-6){const s=res.steps[i++];S.ops[0].queue=[{type:'move',x:s.x,y:s.y}];S.ops[0].cur=null;}update(DT);}
    if(S.over)continue;S.ops[0].queue=[{type:'ko',id:gid}];S.ops[0].cur=null;const t1=S.t+8;while(S.t<t1&&!S.over&&!S.guards[gid].down)update(DT);
    if(S.guards[gid].down&&!S.over){ // 가까운 빈 자리로 옮겨 숨긴 뒤 20초 무사한지
      S.ops[0].queue=[{type:'pick',id:gid}];S.ops[0].cur=null;for(let n=0;n<96&&!S.over;n++)update(DT);
      for(let n=0;n<640&&!S.over;n++)update(DT);
      if(!S.over)found=T;}
  }
  say_('무전병 후보 '+r+' (경비 '+gid+') 제압',found!=null,found!=null?'T='+found:'');}M.rfix=null;}
process.exit(okAll?0:1);
