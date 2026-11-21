// 로맨틱 전용 맵 판 점검. 사용: cd public && node ../tools/check_rom.js [미션 번호 ...]
// 1) 시작 지점에 서서 가만히 있어도 30초 동안 들키지 않는지(HARD · HELL)  2) 경비 순찰 지점이 전부 길로 이어지는지
const fs=require('fs');const html=fs.readFileSync('index.html','utf8');const js=html.match(/<script>([\s\S]*)<\/script>/)[1];
const noop=new Proxy(function(){},{get:(t,k)=>k==='length'?0:noop,apply:()=>noop,set:()=>true});
const el=()=>({textContent:'',className:'',innerHTML:'',src:'',style:{setProperty(){}},appendChild(){},addEventListener(){},setAttribute(){},getAttribute(){return ''},getContext:()=>noop,getBoundingClientRect:()=>({width:390,height:640,left:0,top:0})});
const els={};global.document={getElementById:id=>els[id]||(els[id]=el()),createElement:el};global.window={devicePixelRatio:1,addEventListener(){}};global.requestAnimationFrame=()=>{};
(0,eval)(js);
let ids=process.argv.slice(2).map(Number);if(!ids.length)ids=MIS.map((m,i)=>m.rom?i:-1).filter(i=>i>=0);let bad=0;
for(const mi of ids){for(const d of [2,3]){setDiff(d);loadMission(mi);restart();let peak=0,who=-1;
  while(S.t<30&&!S.over){update(1/32);S.guards.forEach(g=>{if(g.meter>peak){peak=g.meter;who=g.id;}});}
  const ok=!S.over&&peak<0.5;if(!ok)bad++;console.log((ok?'OK   ':'FAIL ')+'M'+mi+' '+MIS[mi].title+' '+DIFFS[d].n+' 시작 지점 30초'+(S.over?' · '+S.over.why+' t='+S.t.toFixed(1):'')+' · 의심 최고 '+peak.toFixed(2)+(who>=0?' (경비 '+who+')':''));}
  setDiff(2);loadMission(mi);restart();M.guards.forEach((g,gi)=>{const w=g.wps;for(let i=0;i<w.length;i++){const a=w[i],b=w[(i+1)%w.length];if(w.length>1&&!findPath(a[0],a[1],b[0],b[1])){bad++;console.log('FAIL M'+mi+' 경비 '+gi+' 순찰 길 없음',a,b);}}});}
process.exit(bad?1:0);
