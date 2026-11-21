# -*- coding: utf-8 -*-
"""로맨틱 전용 맵을 받는 엔진 수정(한 번만 적용). 사용: python3 engine_patch.py"""
import io, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'public', 'index.html'); s = io.open(p, encoding='utf8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a)); s = s.replace(a, b)
# 1. 로맨틱 미션 데이터 자리와 조립
rep("var SIDX={};\nObject.keys(STORY).forEach(function(id){", "/*ROM-BEGIN*/\nvar ROM={};\n/*ROM-END*/\nvar SIDX={};\nObject.keys(STORY).forEach(function(id){")
rep("    m.bc=['nokill','noinv','noload'][ci];m.story={id:id,ci:ci};SIDX[id].push(MIS.length);MIS.push(m);",
"""    m.bc=['nokill','noinv','noload'][ci];m.story={id:id,ci:ci};
    var R=(ROM[id]||[])[ci];
    if(R){ /* 전용 맵이 들어온 판: 맵 · 배치 · 대사를 통째로 바꾼다 */
      m={};for(k in R.m)m[k]=R.m[k];
      m.title=R.t;m.code='ROMANTIC // '+OPD[id].n+' TAKE '+(ci+1);m.copy=R.copy;m.pre=R.pre;m.post=R.post;m.img='a_'+id+'_'+(ci%2)+'.jpg';
      m.goal0=m.hostage?R.goal:m.objective.label+' — '+m.objective.verb;m.goal1=m.hostage?'함께 들어온 곳으로':'들어온 곳으로 복귀';
      m.brief='<ul>'+RULES+'<li>혼자 들어간다. 지원은 없다.</li>'+(R.tips||[]).map(function(x){return '<li>'+x+'</li>';}).join('')+'</ul>';
      m.bc=R.bc;m.par=R.par;m.story={id:id,ci:ci};m.rom=true;
    }
    SIDX[id].push(MIS.length);MIS.push(m);""")
# 2. 환경 규칙 일반화: mask(주기 소음 가림) · vis(주기 시야 배율) · fog(상시 시야 배율) · hush(발소리 없음) · rk(판별 시야 배율)
rep("  var e=M.env,b,k=1,q=false,t='',hot=false;\n  if(e){",
"""  var e=M.env,b,k=M.rk||1,q=false,t='',hot=false;
  if(e){
    if(e.fog)k*=e.fog;
    if(e.vis){b=envPhase(e.vis);if(b>=0){k*=e.vis[2];hot=true;t=e.vis[3]+' '+Math.ceil(e.vis[1]-b);}else t=(e.vis[4]||'다음까지')+' '+Math.ceil(envNext(e.vis));}
    if(e.mask){b=envPhase(e.mask);if(b>=0){q=true;hot=true;t=e.mask[2]+' '+Math.ceil(e.mask[1]-b);}else if(!hot)t=(e.mask[3]||'다음까지')+' '+Math.ceil(envNext(e.mask));}""")
rep("    if(e.blizzard){b=envPhase(e.blizzard);if(b>=0){k=0.45;", "    if(e.blizzard){b=envPhase(e.blizzard);if(b>=0){k*=0.45;")
rep("    if(o.nt<=0){o.nt=0.35;S.noise.push({x:o.x,y:o.y,t:0.6,r:NOISE});alertNear(o.x,o.y,NOISE,o.x,o.y,null);}\n  }",
"""    if(o.nt<=0){o.nt=0.35;if(!(M.env&&M.env.hush)){S.noise.push({x:o.x,y:o.y,t:0.6,r:NOISE});alertNear(o.x,o.y,NOISE,o.x,o.y,null);}}
  }else if(moving&&wetAt(o.x,o.y)&&!ENV.quiet){ /* 물 칸: 앉아서 걸어도 물소리가 난다 */
    o.nt-=dt;
    if(o.nt<=0){o.nt=0.5;S.noise.push({x:o.x,y:o.y,t:0.6,r:WETR});alertNear(o.x,o.y,WETR,o.x,o.y,null);}
  }""")
rep("function senseRange(g,o){\n  var low=o.crouch&&o.carry<0;\n  if(g.cam)return CAMR;\n  if(o.disg&&!g.boss)return g.keen?RANGE*0.6:1.5;\n  return (low?CRANGE:RANGE)*(g.tower?1.4:1);\n}",
"""var WETR=3.2;
function wetAt(x,y){var w=M.wet;if(!w)return false;if(!M.wetS){M.wetS={};w.forEach(function(c){M.wetS[c[1]*COLS+c[0]]=1;});}return !!M.wetS[fl(y)*COLS+fl(x)];}
/* 구역별 시야 배율: M.zones=[[x0,y0,x1,y1,k],...] 서 있는 칸이 드는 첫 구역 */
function zk(x,y){var z=M.zones;if(!z)return 1;x=fl(x);y=fl(y);for(var i=0;i<z.length;i++)if(x>=z[i][0]&&y>=z[i][1]&&x<=z[i][2]&&y<=z[i][3])return z[i][4];return 1;}
function senseRange(g,o){
  var low=o.crouch&&o.carry<0;
  if(g.cam)return CAMR;
  if(o.disg&&!g.boss)return g.keen?RANGE*0.6:1.5;
  return (low?CRANGE:RANGE)*(g.tower?1.4:1)*zk(o.x,o.y);
}""")
# 3. 되돌리기 제한(TAKE 2 는 3회, TAKE 3 은 1회)
rep("function load(){if(!saved)return;S=JSON.parse(saved);", "function load(){if(!saved)return;if(M.maxLoads!=null&&loads>=M.maxLoads){S.over={win:false,why:'되돌릴 기회를 다 썼다. 이 TAKE는 '+M.maxLoads+'번까지다.'};overlay('작전 실패','ALERT','<p>'+S.over.why+'</p>',[['처음부터',restart,true],['미션 선택',function(){if(M.story)storyMenu();else menu();}]]);return;}S=JSON.parse(saved);")
# 4. 대화: 판별 인물, 목표 접촉 대화(대피 없는 판)
rep("function dlgWho(k,e){var d=DCAST[k]||{},o=OPD[k]", "function dlgWho(k,e){var d=DCAST[k]||(M.dlg&&M.dlg.who&&M.dlg.who[k])||{},o=OPD[k]")
rep("if(a.t<=0){S.objDone=true;o.cur=null;say(M.objective.label+' '+M.objective.verb+' 완료');snd('ok');}", "if(a.t<=0){S.objDone=true;o.cur=null;say(M.objective.label+' '+M.objective.verb+' 완료');snd('ok');if(!M.evac&&M.dlg&&M.dlg.obj&&!S.dseen.obj){S.dseen.obj=1;S.dq='obj';}}")
rep("if(hyp(h.x-r.x,h.y-r.y)<0.9){h.free=true;S.trail=[];say('데리고 나간다. 출구까지.');snd('ok');}", "if(hyp(h.x-r.x,h.y-r.y)<0.9){h.free=true;S.trail=[];say('데리고 나간다. 출구까지.');snd('ok');if(M.dlg&&M.dlg.obj&&!S.dseen.obj){S.dseen.obj=1;S.dq='obj';}}")
io.open(p, 'w', encoding='utf8').write(s); print('ok', len(s))
