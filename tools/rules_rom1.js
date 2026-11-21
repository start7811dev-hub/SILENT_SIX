const fs=require('fs');const html=fs.readFileSync('index.html','utf8');const js=html.match(/<script>([\s\S]*)<\/script>/)[1];
const noop=new Proxy(function(){},{get:(t,k)=>k==='length'?0:noop,apply:()=>noop,set:()=>true});
const el=()=>({textContent:'',className:'',innerHTML:'',src:'',style:{setProperty(){}},appendChild(){},addEventListener(){},setAttribute(){},getAttribute(){return ''},getContext:()=>noop,getBoundingClientRect:()=>({width:390,height:640,left:0,top:0})});
const els={};global.document={getElementById:id=>els[id]||(els[id]=el()),createElement:el};global.window={devicePixelRatio:1,addEventListener(){}};global.requestAnimationFrame=()=>{};
(0,eval)(js);const DT=1/32;const run=s=>{for(let i=0;i<s/DT;i++)update(DT);};const T=(n,ok,x)=>console.log((ok?'OK   ':'FAIL ')+n+(x?'  '+x:''));
// 1. 목표 접촉 대화 · 클리어
loadMission(6);restart();S.guards.forEach(g=>{g.down=true;g.dead=true;});let o=S.ops[0],u=M.objective.use;o.x=u[0]+.5;o.y=u[1]+.5;o.queue=[{type:'sab'}];run(6);
T('레이븐1 목표 완료 → 목표 대화 예약',S.objDone&&S.dq==='obj'&&M.dlg.obj.length===3,'dq='+S.dq);
o.x=M.exit[0][0]+.5;o.y=M.exit[0][1]+.5;o.queue=[];o.cur=null;o.path=[];run(0.5);T('레이븐1 출구 도착 → 클리어',!!(S.over&&S.over.win));
T('레이븐1 대사: 시작 '+M.dlg.start.length+'줄 · 끝 '+M.dlg.end.length+'줄, 표정 지정',M.dlg.start[0][0]==='raven'&&M.dlg.start[0][2]===0&&M.dlg.end[1][2]===2);
// 2. 폭우: 달려도 소리 없음 / 번개: 시야 1.3배
loadMission(6);restart();o=S.ops[0];o.run=true;o.queue=[{type:'move',x:20,y:19,run:true}];let nz=0,rmin=99,rmax=0;for(let i=0;i<20/DT;i++){update(DT);nz=Math.max(nz,S.noise.length);rmin=Math.min(rmin,RANGE);rmax=Math.max(rmax,RANGE);}
T('폭우: 달려도 소음 0',nz===0);T('번개: 시야 '+rmin.toFixed(2)+' ↔ '+rmax.toFixed(2)+' (1.3배)',Math.abs(rmax/rmin-1.3)<0.01&&Math.abs(rmin-6.5*1.1)<0.01);
// 3. 물 칸 소음과 보일러
loadMission(21);restart();o=S.ops[0];o.crouch=true;o.x=5.5;o.y=18.5;S.guards.forEach(g=>{g.x=-40;g.y=-40;g.wps=[[-40,-40]];g.path=[];});let wn=0,qn=0;
for(let i=0;i<40/DT;i++){if(!o.path.length)o.queue=[{type:'move',x:fl(o.x)<10?14:3,y:18}];update(DT);if(S.noise.length){if(ENV.quiet)qn++;else wn++;}}
T('물 칸: 앉아 걸어도 소음 발생',wn>0,'소음 프레임 '+wn);
loadMission(21);restart();o=S.ops[0];o.crouch=true;o.x=5.5;o.y=8.5;S.guards.forEach(g=>{g.x=-40;g.y=-40;g.wps=[[-40,-40]];g.path=[];});let dn=0;for(let i=0;i<15/DT;i++){if(!o.path.length)o.queue=[{type:'move',x:fl(o.x)<10?14:3,y:8}];update(DT);dn=Math.max(dn,S.noise.length);}
T('마른 칸: 소음 0',dn===0);T('판자 칸은 물 칸에서 빠짐',!wetAt(20.5,16.5)&&!wetAt(11.5,13.5)&&wetAt(11.5,11.5));
// 4. 구역 시야(슬로프 1.4 / 숲 가장자리 0.7)
loadMission(9);restart();T('구역 배율 슬로프 '+zk(8.5,10.5)+' · 숲 가 '+zk(3.5,8.5)+' · 그 밖 '+zk(20.5,20.5),zk(8.5,10.5)===1.4&&zk(3.5,8.5)===0.7&&zk(20.5,20.5)===1);
// 5. 되돌리기 제한(TAKE 2 = 3회)
loadMission(7);restart();save();let n=0;for(let i=0;i<5;i++){load();if(S.over)break;n++;}T('레이븐2 되돌리기 3회 뒤 실패 처리',n===3&&S.over&&!S.over.win,'허용 '+n+'회');
// 6. 돌파(브릭1): 금 간 벽을 부수면 길이 열리고, 환기 팬 중에는 경보 없음
loadMission(15);restart();T('브릭1 돌파 전에는 목표까지 길 없음',!findPath(22,22,6,2));S.open[9*COLS+8]=1;S.open[10*COLS+8]=1;T('브릭1 금 간 벽 열면 길 있음',!!findPath(22,22,6,2));
// 7. 변장을 알아보는 승무원(미라주1)
loadMission(18);restart();T('미라주1 복도 · 로비 승무원 keen',S.guards.filter(g=>g.keen).length===2);
