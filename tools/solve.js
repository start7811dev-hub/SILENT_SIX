const fs=require('fs');const html=fs.readFileSync('index.html','utf8');const js=html.match(/<script>([\s\S]*)<\/script>/)[1];
const noop=new Proxy(function(){},{get:(t,k)=>k==='length'?0:noop,apply:()=>noop,set:()=>true});
const el=()=>({textContent:'',className:'',innerHTML:'',src:'',style:{setProperty(){}},appendChild(){},addEventListener(){},getContext:()=>noop,getBoundingClientRect:()=>({width:390,height:640,left:0,top:0})});
const els={};global.document={getElementById:id=>els[id]||(els[id]=el()),createElement:el};global.window={devicePixelRatio:1,addEventListener(){}};global.requestAnimationFrame=()=>{};
(0,eval)(js);if(process.env.DIFF)setDiff(+process.env.DIFF);
const PAD=+(process.argv[3]||0.5),DT=1/32,T=260,KS=0.125,NK=Math.floor(T/KS);
function solve(mi,plans){ // plans: [{op, obj:bool}]
  loadMission(mi);restart();S.ops.forEach(o=>o.crouch=true);
  const snap=[];for(let k=0;k<NK;k++){snap.push(S.guards.map(g=>({x:g.x,y:g.y,ang:g.ang,tower:g.tower,cam:g.cam,boss:g.boss})));for(let i=0;i<4;i++)update(DT);if(S.over){console.log('M'+(mi+1),'IDLE FAIL at',S.t.toFixed(1),S.over.why);return false;}}
  const F0=FOV,C0=CAMFOV;if(PAD>0){FOV=F0*1.15;CAMFOV=C0*1.15;}const N=COLS*ROWS,walk=[];for(let c=0;c<N;c++)if(!blocked(c%COLS,Math.floor(c/COLS)))walk.push(c);
  const tabC=new Uint8Array(N*NK),tabS=new Uint8Array(N*NK);
  for(let k=0;k<NK;k++)for(const c of walk){const x=c%COLS+.5,y=Math.floor(c/COLS)+.5;let sc=0,ss=0;
    for(const g of snap[k]){const R=(g.cam?CAMR:g.tower?RANGE*1.4:RANGE)+PAD,CR=(g.cam?CAMR:g.tower?CRANGE*1.4:CRANGE)+PAD;if(!ss&&canSee(g,x,y,R))ss=1;if(!sc&&canSee(g,x,y,CR))sc=1;}
    tabC[c*NK+k]=sc;tabS[c*NK+k]=ss||sc;}
  const safe=(tab,c,k0,k1)=>{if(k1>=NK)return false;for(let k=k0;k<=k1;k++)if(tab[c*NK+k])return false;return true;};
  const mid=(x,y,k0,k1)=>{for(let k=k0;k<=k1&&k<NK;k++)for(const g of snap[k])if(canSee(g,x,y,(g.cam?CAMR:g.tower?CRANGE*1.4:CRANGE)+PAD))return false;return true;};
  const NL=Math.floor(NK/2),out=[];let Lstart=0,minL=0;
  for(const pl of plans){
    const o=S0=M.ops[pl.op],start=o.y*COLS+o.x;const exits=new Set(M.exit.map(e=>e[1]*COLS+e[0]));
    const goalC=M.hostage?M.hostage.y*COLS+M.hostage.x:M.objective.use[1]*COLS+M.objective.use[0];
    const sabL=M.hostage?1:Math.ceil((M.objective.time+0.7)/0.25);
    const par=[new Int32Array(NL*N).fill(-1),new Int32Array(NL*N).fill(-1)];
    const ph0=pl.obj?0:1;par[ph0][Lstart*N+start]=-2;let goal=null,far=0;
    for(let L=Lstart;L<NL-12&&!goal;L++)for(let ph=ph0;ph<2&&!goal;ph++)for(const c of walk){
      if(par[ph][L*N+c]===-1)continue;const id=(ph*NL+L)*N+c,host=M.hostage&&ph===1,tab=tabC;
      if(ph===1&&exits.has(c)&&L>=minL){goal=[ph,L,c];break;}
      if(L>far)far=L;
      if(safe(tab,c,2*L,2*L+2)&&par[ph][(L+1)*N+c]===-1)par[ph][(L+1)*N+c]=id;
      if(ph===0&&c===goalC&&L+sabL<NL&&safe(tabC,c,2*L,2*(L+sabL))&&par[1][(L+sabL)*N+c]===-1)par[1][(L+sabL)*N+c]=id;
      const cx=c%COLS,cy=Math.floor(c/COLS);
      for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){const nx=cx+dx,ny=cy+dy;if(blocked(nx,ny))continue;const n=ny*COLS+nx;
        if(par[ph][(L+3)*N+n]!==-1)continue;
        if(safe(tab,c,2*L,2*L+(host?7:3))&&safe(tab,n,2*L,2*L+6)&&mid(cx+.5+dx/2,cy+.5+dy/2,2*L,2*L+5))par[ph][(L+3)*N+n]=id;}
    }
    if(!goal){let reach0=0,gotObj=false;for(let L=0;L<NL;L++){if(par[1][L*N+goalC]!==-1)gotObj=true;}
      console.log('M'+(mi+1),'op',pl.op,'NO GHOST ROUTE; objective reached:',gotObj);for(let ph=0;ph<2;ph++){const seen=new Set();for(let L=0;L<NL;L++)for(const c of walk)if(par[ph][L*N+c]!==-1)seen.add(c);console.log(' phase',ph);for(let y=0;y<ROWS;y++){let r='';for(let x=0;x<COLS;x++)r+=seen.has(y*COLS+x)?'o':MAP[y][x];console.log('  '+r);}}return false;}
    const steps=[];let [ph,L,c]=goal;while(true){const p=par[ph][L*N+c];if(p===-2)break;const pc=p%N,pL=Math.floor(p/N)%NL,pph=Math.floor(p/N/NL);
      if(pc!==c)steps.unshift({t:pL*0.25,op:pl.op,x:c%COLS,y:Math.floor(c/COLS)});else if(pph!==ph&&!M.hostage)steps.unshift({t:pL*0.25,op:pl.op,sab:true});ph=pph;L=pL;c=pc;}
    out.push(...steps);minL=goal[1]-2;console.log('M'+(mi+1),'op',pl.op,'ghost route found, finish t='+(goal[1]*0.25).toFixed(1)+'s, moves',steps.length);
  }
  out.sort((a,b)=>a.t-b.t);FOV=F0;CAMFOV=C0;
  restart();S.ops.forEach(o=>o.crouch=true);let i=0;
  for(let n=0;n<T/DT&&!S.over;n++){while(i<out.length&&out[i].t<=S.t+1e-6){const s=out[i++];S.ops[s.op].queue=[s.sab?{type:'sab'}:{type:'move',x:s.x,y:s.y}];S.ops[s.op].cur=null;}update(DT);}
  if(S.over&&!S.over.win&&S.hostage)console.log('   hostage',S.hostage.x.toFixed(2),S.hostage.y.toFixed(2),'trail',S.trail.length,'g4',S.guards[4].x.toFixed(1),S.guards[4].y.toFixed(1),S.guards[4].ang.toFixed(2),S.guards[4].state);if(S.over&&!S.over.win)console.log('   ops',S.ops.map(o=>o.x.toFixed(1)+','+o.y.toFixed(1)).join(' '),'guards',S.guards.map(g=>g.meter.toFixed(2)).join(' '));console.log('   REAL RUN:',JSON.stringify(S.over),'t='+S.t.toFixed(1),'objDone',S.objDone,S.hostage?'hostage '+S.hostage.free:'');
  return S.over&&S.over.win;
}
const P={0:[{op:0,obj:true}],1:[{op:0,obj:true},{op:1,obj:false}],2:[{op:0,obj:true}],3:[{op:1,obj:true}],4:[{op:1,obj:true}],5:[{op:1,obj:true},{op:0,obj:false}]};for(let i=6;i<24;i++)P[i]=[{op:0,obj:true}];for(let i=0;i<5;i++)P[24+i]=P[i];
const only=process.argv[2];for(const k of Object.keys(P)){if(only!=null&&only!==k)continue;solve(+k,P[k]);}
