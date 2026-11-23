// EP2 판 노출 지도: 칸마다 120초 중 앉은 요원이 보이는 비율(0~9), 사용: STAGE=n node ../tools/heat_ep2.js [subsdone]
const fs=require('fs');const html=fs.readFileSync('index.html','utf8');const js=html.match(/<script>([\s\S]*?)<\/script>/)[1];
const noop=new Proxy(function(){},{get:(t,k)=>k==='length'?0:noop,apply:()=>noop,set:()=>true});
const el=()=>({textContent:'',className:'',innerHTML:'',src:'',style:{setProperty(){}},appendChild(){},addEventListener(){},setAttribute(){},getAttribute(){return ''},getContext:()=>noop,getBoundingClientRect:()=>({width:390,height:640,left:0,top:0})});
const els={};global.document={getElementById:id=>els[id]||(els[id]=el()),createElement:el,addEventListener(){},head:{appendChild(){}},body:{appendChild(){}}};global.window={devicePixelRatio:1,addEventListener(){}};global.requestAnimationFrame=()=>{};
(0,eval)(js);setDiff(2);loadMission(E2IDX[(+process.env.STAGE||1)-1]);restart();
if(process.argv[2])M.subs.forEach((sb,si)=>subDone(si));
S.ops.forEach(o=>{o.x=-50;o.y=-50;});
const cnt=new Float32Array(COLS*ROWS);let n=0;
for(let k=0;k<480;k++){for(let y=0;y<ROWS;y++)for(let x=0;x<COLS;x++){if(blocked(x,y))continue;for(const g of S.guards){if(g.down||g.off>0)continue;if(canSee(g,x+.5,y+.5,g.cam?(g.cr||CAMR):(g.tower?CRANGE*1.4:CRANGE))){cnt[y*COLS+x]++;break;}}}n++;for(let i=0;i<8;i++)update(1/32);if(S.over){console.log('over',S.over.why);break;}}
const gp={};S.guards.forEach((g,i)=>{gp[Math.floor(g.y)*COLS+Math.floor(g.x)]=String.fromCharCode(97+i);});
console.log('   '+[...Array(COLS).keys()].map(i=>i%10).join(''));
for(let y=0;y<ROWS;y++){let r='';for(let x=0;x<COLS;x++){const c=y*COLS+x;r+=blocked(x,y)?(MAP[y][x]==='#'?'#':MAP[y][x]):cnt[c]===0?'.':String(Math.min(9,Math.ceil(cnt[c]/n*9)));}console.log(String(y).padStart(2)+' '+r);}
