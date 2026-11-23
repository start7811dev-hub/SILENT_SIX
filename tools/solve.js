const fs=require('fs');const html=fs.readFileSync('index.html','utf8');const js=html.match(/<script>([\s\S]*?)<\/script>/)[1];
const noop=new Proxy(function(){},{get:(t,k)=>k==='length'?0:noop,apply:()=>noop,set:()=>true});
const el=()=>({textContent:'',className:'',innerHTML:'',src:'',style:{setProperty(){}},appendChild(){},addEventListener(){},getContext:()=>noop,getBoundingClientRect:()=>({width:390,height:640,left:0,top:0})});
const els={};global.document={getElementById:id=>els[id]||(els[id]=el()),createElement:el,addEventListener(){},head:{appendChild(){}},body:{appendChild(){}}};global.window={devicePixelRatio:1,addEventListener(){}};global.requestAnimationFrame=()=>{};
(0,eval)(js);if(process.env.DIFF)setDiff(+process.env.DIFF);
const PAD=+(process.argv[3]||0.5),DT=1/32,T=260,KS=0.125,NK=Math.floor(T/KS);
function solve(mi,plans){ // plans: [{op, obj:bool}]
  const vopen=()=>(M.vopen||[]).forEach(c=>{S.open[c[1]*COLS+c[0]]=1;}); // 돌파 전용 판: 지정한 금 간 벽을 미리 연 상태로 본다
  loadMission(mi);restart();vopen();S.ops.forEach(o=>o.crouch=true);
  const snap=[];for(let k=0;k<NK;k++){const sn=S.guards.map(g=>({x:g.x,y:g.y,ang:g.ang,tower:g.tower,cam:g.cam,cr:g.cr,boss:g.boss}));sn.R=RANGE;sn.C=CRANGE;sn.q=ENV.quiet;snap.push(sn);for(let i=0;i<4;i++)update(DT);if(S.over){console.log('M'+(mi+1),'IDLE FAIL at',S.t.toFixed(1),S.over.why);return false;}}
  const F0=FOV,C0=CAMFOV;if(PAD>0){FOV=F0*1.15;CAMFOV=C0*1.15;}const N=COLS*ROWS,walk=[];for(let c=0;c<N;c++)if(!blocked(c%COLS,Math.floor(c/COLS)))walk.push(c);
  const tabC=new Uint8Array(N*NK),tabS=new Uint8Array(N*NK);
  for(let k=0;k<NK;k++)for(const c of walk){const x=c%COLS+.5,y=Math.floor(c/COLS)+.5;let sc=0,ss=0;
    const z=zk(x,y),sn=snap[k];
    for(const g of sn){const R=(g.cam?(g.cr||CAMR):(g.tower?sn.R*1.4:sn.R)*z)+PAD,CR=(g.cam?(g.cr||CAMR):(g.tower?sn.C*1.4:sn.C)*z)+PAD;if(!ss&&canSee(g,x,y,R))ss=1;if(!sc&&canSee(g,x,y,CR))sc=1;}
    if(cellIn(M,'hot',x,y)){sc=1;ss=1;} // 열 통로는 풀이에서 아예 피한다
    if(!sc&&!sn.q&&wetAt(x,y))for(const g of sn)if(!g.cam&&!g.tower&&Math.hypot(g.x-x,g.y-y)<=WETR+0.6){sc=1;ss=1;break;} // 물 칸: 경비가 물소리를 들을 거리면 못 지나간다
    tabC[c*NK+k]=sc;tabS[c*NK+k]=ss||sc;}
  const safe=(tab,c,k0,k1)=>{if(k1>=NK)return false;for(let k=k0;k<=k1;k++)if(tab[c*NK+k])return false;return true;};
  const mid=(x,y,k0,k1)=>{const z=zk(x,y);for(let k=k0;k<=k1&&k<NK;k++)for(const g of snap[k])if(canSee(g,x,y,(g.cam?(g.cr||CAMR):(g.tower?snap[k].C*1.4:snap[k].C)*z)+PAD))return false;return true;};
  const NL=Math.floor(NK/2),out=[];let Lstart=0,minL=0;
  for(const pl of plans){
    const o=S0=M.ops[pl.op],start=o.y*COLS+o.x;const exits=new Set(M.exit.map(e=>e[1]*COLS+e[0]));
    // 목표 목록: (중간 목표들 →) 본 목표 또는 호위 대상. 단계 p 는 goals[p] 로 가는 중, 마지막 단계는 출구로 가는 중이다.
    const cellOf=u=>u[1]*COLS+u[0],dwell=t=>Math.ceil((t+0.7)/0.25);
    const goals=M.hostage?[{c:M.hostage.y*COLS+M.hostage.x,L:1}]:[...(M.subs||[]).map((sb,i)=>sb.use?{c:cellOf(sb.use),L:dwell(sb.time),sub:i}:null).filter(Boolean),{c:cellOf(M.objective.use),L:dwell(M.objective.time),after:M.objective.after?Math.ceil((M.objective.after+0.5)/0.25):0}];
    const G=goals.length,ph0=pl.obj?0:G,goalC=goals[G-1].c,aft=goals[G-1].after||0;
    // 본 목표에 대기 시간(after)이 있으면: 직전 중간 목표를 끝내는 시각 Lc 를 하나로 정하고 찾는다(이른 것부터 차례로).
    const search=Lc=>{
      const par=[];for(let i=0;i<=G;i++)par.push(new Int32Array(NL*N).fill(-1));
      par[ph0][Lstart*N+start]=-2;let goal=null;const done=new Set();
      for(let L=Lstart;L<NL-12&&!goal;L++)for(let ph=ph0;ph<=G&&!goal;ph++)for(const c of walk){
        if(par[ph][L*N+c]===-1)continue;const id=(ph*NL+L)*N+c,host=M.hostage&&ph===G,tab=tabC;
        if(ph===G&&exits.has(c)&&L>=minL){goal=[ph,L,c];break;}
        if(safe(tab,c,2*L,2*L+2)&&par[ph][(L+1)*N+c]===-1)par[ph][(L+1)*N+c]=id;
        if(ph<G&&c===goals[ph].c){const gl=goals[ph],L2=L+gl.L,last=ph===G-1,pre=aft&&ph===G-2;
          if(L2<NL&&safe(tabC,c,2*L,2*L2)&&(!pre||Lc==null||L2===Lc)&&(!(last&&aft&&G>1)||(Lc!=null&&L>=Lc+aft))){if(pre)done.add(L2);if((!pre||Lc!=null)&&par[ph+1][L2*N+c]===-1)par[ph+1][L2*N+c]=id;}}
        const cx=c%COLS,cy=Math.floor(c/COLS);
        for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){const nx=cx+dx,ny=cy+dy;if(blocked(nx,ny))continue;const n=ny*COLS+nx;
          if(par[ph][(L+3)*N+n]!==-1)continue;
          if(safe(tab,c,2*L,2*L+(host?7:3))&&safe(tab,n,2*L,2*L+6)&&mid(cx+.5+dx/2,cy+.5+dy/2,2*L,2*L+5))par[ph][(L+3)*N+n]=id;}
      }
      return {par,goal,done};
    };
    let R=null;
    if(aft&&G>1&&pl.obj){const first=search(null),cand=[...first.done].sort((x,y)=>x-y);let last=-99,tries=0;R=first;
      for(const Lc of cand){if(Lc-last<4)continue;last=Lc;if(++tries>40)break;const r=search(Lc);R=r;if(r.goal)break;}}
    else R=search(null);
    const par=R.par,goal=R.goal;
    if(!goal){let gotObj=false,objL=-1;for(let L=0;L<NL;L++){if(par[G][L*N+goalC]!==-1){gotObj=true;if(objL<0)objL=L;}}
      if(gotObj)console.log('   objective first done at t='+(objL*0.25).toFixed(1)+'s (horizon '+(NL*0.25).toFixed(0)+'s)');
      console.log('M'+(mi+1),'op',pl.op,'NO GHOST ROUTE; objective reached:',gotObj);for(let ph=0;ph<=G;ph++){const seen=new Set();for(let L=0;L<NL;L++)for(const c of walk)if(par[ph][L*N+c]!==-1)seen.add(c);console.log(' phase',ph);for(let y=0;y<ROWS;y++){let r='';for(let x=0;x<COLS;x++)r+=seen.has(y*COLS+x)?'o':MAP[y][x];console.log('  '+r);}}return false;}
    const steps=[];let [ph,L,c]=goal;while(true){const p=par[ph][L*N+c];if(p===-2)break;const pc=p%N,pL=Math.floor(p/N)%NL,pph=Math.floor(p/N/NL);
      if(pc!==c)steps.unshift({t:pL*0.25,op:pl.op,x:c%COLS,y:Math.floor(c/COLS)});else if(pph!==ph&&!M.hostage){const gl=goals[pph];steps.unshift(gl.sub!=null?{t:pL*0.25,op:pl.op,sub:gl.sub}:{t:pL*0.25,op:pl.op,sab:true});}ph=pph;L=pL;c=pc;}
    out.push(...steps);minL=goal[1]-2;console.log('M'+(mi+1),'op',pl.op,'ghost route found, finish t='+(goal[1]*0.25).toFixed(1)+'s, moves',steps.length);
  }
  out.sort((a,b)=>a.t-b.t);FOV=F0;CAMFOV=C0;
  restart();vopen();S.ops.forEach(o=>o.crouch=true);let i=0;
  for(let n=0;n<T/DT&&!S.over;n++){while(i<out.length&&out[i].t<=S.t+1e-6){const s=out[i++];S.ops[s.op].queue=[s.sab?{type:'sab'}:s.sub!=null?{type:'sub',i:s.sub}:{type:'move',x:s.x,y:s.y}];S.ops[s.op].cur=null;}update(DT);}
  if(S.over&&!S.over.win&&S.hostage)console.log('   hostage',S.hostage.x.toFixed(2),S.hostage.y.toFixed(2),'trail',S.trail.length,'g4',S.guards[4].x.toFixed(1),S.guards[4].y.toFixed(1),S.guards[4].ang.toFixed(2),S.guards[4].state);if(S.over&&!S.over.win)console.log('   ops',S.ops.map(o=>o.x.toFixed(1)+','+o.y.toFixed(1)).join(' '),'guards',S.guards.map(g=>g.meter.toFixed(2)).join(' '));console.log('   REAL RUN:',JSON.stringify(S.over),'t='+S.t.toFixed(1),'objDone',S.objDone,S.hostage?'hostage '+S.hostage.free:'');
  return S.over&&S.over.win;
}
const P={0:[{op:0,obj:true}],1:[{op:0,obj:true},{op:1,obj:false}],2:[{op:0,obj:true}],3:[{op:1,obj:true}],4:[{op:1,obj:true}],5:[{op:1,obj:true},{op:0,obj:false}]};for(let i=6;i<24;i++)P[i]=[{op:0,obj:true}];P[24]=[{op:0,obj:true}];P[25]=[{op:0,obj:true},{op:1,obj:false}];P[26]=[{op:1,obj:true},{op:0,obj:false}];P[27]=[{op:0,obj:true},{op:1,obj:false}];P[28]=[{op:0,obj:true},{op:1,obj:false},{op:2,obj:false}];
const only=process.argv[2];for(const k of Object.keys(P)){if(only!=null&&only!==k)continue;solve(+k,P[k]);}
