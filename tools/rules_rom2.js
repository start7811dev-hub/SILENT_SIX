// 이번에 넣은 규칙 점검: 열 통로 · 마네킹 은폐 · 드론 · 등대 빛 거리 · 되돌리기 1회 · 호위 이름표 · 초상 파일
const fs=require('fs');const html=fs.readFileSync('index.html','utf8');const js=html.match(/<script>([\s\S]*)<\/script>/)[1];
const noop=new Proxy(function(){},{get:(t,k)=>k==='length'?0:noop,apply:()=>noop,set:()=>true});
const el=()=>({textContent:'',className:'',innerHTML:'',src:'',style:{setProperty(){}},appendChild(){},addEventListener(){},setAttribute(){},getAttribute(){return ''},getContext:()=>noop,getBoundingClientRect:()=>({width:390,height:640,left:0,top:0})});
const els={};global.document={getElementById:id=>els[id]||(els[id]=el()),createElement:el};global.window={devicePixelRatio:1,addEventListener(){}};global.requestAnimationFrame=()=>{};global.localStorage={getItem(){return null},setItem(){}};
(0,eval)(js);setDiff(2);
let ok=0,bad=0;const T=(n,c,x)=>{console.log((c?'OK  ':'FAIL')+' '+n+(x!==undefined?'  '+x:''));c?ok++:bad++;};
const run=s=>{for(let i=0;i<Math.round(s*32);i++){if(S.over)break;update(1/32);}};
// 열 통로(글리치 1)
loadMission(12);restart();T('글리치1 열 통로 칸 있음',M.hot&&M.hot.length>0,M.hot&&M.hot.length+'칸');
if(M.hot&&M.hot.length){const c=M.hot[0];S.guards.forEach(g=>{g.off=999;});S.ops[0].x=c[0]+.5;S.ops[0].y=c[1]+.5;S.ops[0].path=[];run(2.5);T('열 통로 2.5초: 아직 실패 아님',!S.over);run(1);T('열 통로 3초 넘김: 실패',S.over&&!S.over.win,S.over&&S.over.why);}
// 드론(글리치 2)
loadMission(13);restart();const dr=S.guards.filter(g=>g.drone);T('글리치2 드론 있음',dr.length>0,dr.length+'대');
// 등대 빛(레이븐 3)
loadMission(8);restart();T('레이븐3 등대 빛 거리 15칸',S.guards[0].cam&&S.guards[0].cr===15);T('레이븐3 되돌리기 1회',M.maxLoads===1);
// 마네킹(미라주 3)
loadMission(20);restart();const st=M.still[0],o=S.ops[0];o.x=st[0]+1.5;o.y=st[1]+.5;o.path=[];o.mv=false;T('미라주3 마네킹 옆 정지: 숨음',stillHid(o)===true);o.x=st[0]+3.5;T('마네킹에서 두 칸 떨어지면 안 숨음',!stillHid(o));o.x=st[0]+1.5;o.mv=true;T('마네킹 옆이라도 움직이면 안 숨음',!stillHid(o));
// 호위 판 이름 · 초상
for(const [i,n] of [[16,'동료'],[23,'선임']]){loadMission(i);restart();T('M'+i+' 호위 대상 있음 · 이름 '+n,!!S.hostage&&M.dlg.who.npc.n===n);}
for(const i of [16,11,20,23]){loadMission(i);const fs2=(M.dlg.cast||{}).npc||[];T('M'+i+' 대면 초상 2장 파일 있음',fs2.length===2&&fs2.every(f=>fs.existsSync(f)),fs2.join(','));}
for(const [i,n] of [[8,'녹음'],[17,'동료들']]){loadMission(i);T('M'+i+' 이름만 있는 화자 '+n,M.dlg.who&&M.dlg.who.npc.n===n&&!(M.dlg.cast||{}).npc);}
// 환경
loadMission(14);restart();let lo=1e9,hi=0;for(let i=0;i<32*20;i++){update(1/32);lo=Math.min(lo,RANGE);hi=Math.max(hi,RANGE);}T('글리치3 정전 시야 '+hi.toFixed(2)+' → '+lo.toFixed(2),lo<hi*0.4);
loadMission(23);restart();update(1/32);T('닥3 안개 포함 시야 '+RANGE.toFixed(2)+'칸(45칸 격자)',Math.abs(RANGE-6.5*DIFFS[2].r*1.65*0.6)<0.01);
loadMission(17);restart();lo=1e9;hi=0;let q=0;for(let i=0;i<32*31;i++){update(1/32);lo=Math.min(lo,RANGE);hi=Math.max(hi,RANGE);if(ENV.quiet)q++;}T('브릭3 발파 먼지: 시야 '+hi.toFixed(2)+' → '+lo.toFixed(2)+' · 소리 묻힘 '+(q/32).toFixed(1)+'초',lo<hi*0.45&&q>0);
// 두 단계 목표 · 사격 제한 (v0.36.0)
const act=(a,sec)=>{const o=S.ops[0];o.queue=[a];o.cur=null;run(sec);};
const put=u=>{const o=S.ops[0];o.x=u[0]+.5;o.y=u[1]+.5;o.path=[];o.cur=null;o.queue=[];};
loadMission(14);restart();S.guards.forEach(g=>{g.off=999;});
put(M.objective.use);act({type:'sab'},3);T('글리치3 금고 전에는 드럼통이 잠김',!S.objDone);
put(M.subs[0].use);act({type:'sub',i:0},M.subs[0].time+0.5);T('글리치3 금고에서 단말 꺼내기',S.subs[0]===true);
put(M.objective.use);act({type:'sab'},M.objective.time+0.5);T('글리치3 드럼통에 태우기 → 목표 완료 · 목표 대화',S.objDone&&S.dseen.obj===1);
loadMission(17);restart();S.guards.forEach(g=>{g.off=999;});
put(M.subs[0].use);act({type:'sub',i:0},M.subs[0].time+0.3);T('브릭3 문 열기 → 문 열린 그림 · 문 앞 대화',S.subs[0]&&bgName()==='bgp_brick_3b.jpg'&&S.dseen.mid===1,bgName());
S.dq=null;act({type:'sab'},2);T('브릭3 셋이 나오는 동안은 못 닫음',!S.objDone&&objWait()>0,'남은 '+objWait().toFixed(1)+'초');
run(M.objective.after);act({type:'sab'},M.objective.time+0.5);T('브릭3 8초 뒤 문 닫기 → 목표 완료 · 원래 그림',S.objDone&&bgName()==='bgp_brick_3.jpg');
loadMission(8);restart();T('레이븐3 권총 0발',S.ops[0].pistol===0&&S.ops[0].p0===0);
loadMission(11);restart();T('바이퍼3 저격 1발 · 권총 0발',S.ops[0].ammo===1&&S.ops[0].pistol===0);
T('바이퍼3 배지 "한 발": 안 쏘면 달성',BCOND[M.bc][0]==='한 발'&&BCOND[M.bc][2]()===true);S.ops[0].ammo=0;T('바이퍼3 배지: 쏘면 실패',BCOND[M.bc][2]()===false);
loadMission(1);restart();T('스토리 2판 바이퍼 저격 3발 · 권총 6발 그대로',S.ops.some(o=>o.id==='viper'&&o.ammo===3&&o.pistol===6));
console.log(ok+' ok / '+bad+' fail');
