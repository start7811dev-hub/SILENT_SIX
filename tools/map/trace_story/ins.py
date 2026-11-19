import io,json,re,shutil,sm,st
G={1:"[{wps:[[5,5],[5,13]]},{wps:[[7,5],[15,5]]},{wps:[[9,9],[9,15]]},{wps:[[14,6],[14,9]]},{wps:[[13,13]],faces:[3.14,-1.57],ft:5},{wps:[[14,5]],faces:[1.57,3.14],ft:5}]",
   2:"[{wps:[[12,8],[15,8]]},{wps:[[6,9],[6,14]]},{wps:[[10,15],[16,15]]},{wps:[[19,16]],faces:[3.14,-1.57],ft:5},{wps:[[7,3],[7,7]]}]",
   5:"[{wps:[[8,8],[13,11],[10,15]],boss:true},{wps:[[5,7],[5,12]]},{wps:[[17,11]],faces:[1.57,-1.57],ft:6},{wps:[[5,5]],cam:true,faces:[0,1.57],ft:9}]",
   3:"[{wps:[[5,8],[5,15]]},{wps:[[7,10],[7,15]]},{wps:[[14,6],[14,10]]},{wps:[[13,14]],faces:[3.14,-1.57],ft:5},{wps:[[7,2]],cam:true,faces:[-0.9,1.5],ft:12},{wps:[[1,15]],cam:true,faces:[0,-0.9],ft:6}]"}
OPS={1:['raven'],3:['raven','glitch'],2:['raven','viper'],5:['mirage','glitch']}
EXIT={5:'[[19,19],[18,18],[18,19],[19,18]]',2:'[[13,23],[14,23],[15,23],[16,23],[13,22],[14,22],[15,22],[16,22]]'}
HTS={5:"{'#':44,'B':40,'C':22,'X':50}",2:"{'#':40,'B':34,'C':20,'X':40}"}
OPQ={2:'#B',5:'#B'}
TITLE={1:'혼자 남은 사람',3:'눈이 되는 자',2:'원거리 지원',5:'가면 무도회'}
def install(ns):
    p='/home/claude/silent_six/public/index.html';s=io.open(p,encoding='utf8').read()
    for n in ns:
        o=sm.OUT[n];M=[''.join(r) for r in o['MAP']];a=s.index("{title:'%s'"%TITLE[n]);b=s.index("{title:'",a+5)
        blk=s[a:b]
        i=blk.index("bg:'bg%d.jpg'"%n);j=blk.index(" brief:")
        st_=o['start'];ops=','.join("{id:'%s',x:%d,y:%d}"%(OPS[n][k],st_[k][0],st_[k][1]) for k in range(len(OPS[n])))
        ex=EXIT.get(n,"[[18,18],[18,19],[19,18],[19,19]]")
        old=blk[i:j];wake=re.search(r'wake:(\d+)',old).group(1)
        if 'hostage' in o:tgt="hostage:{x:%d,y:%d}"%o['hostage']
        else:
            ob=re.search(r'objective:\{[^}]*\}',old).group(0);ob=re.sub(r'x:\d+,y:\d+,use:\[\d+,\d+\]','x:%d,y:%d,use:[%d,%d]'%(o['obj']+tuple(o['use'])),ob);tgt=ob
        new="bg:'bg%d.jpg',sk:0.44,wake:%s,opaque:'%s',hts:%s,\n proj:%s,\n MAP:%s,\n ops:[%s],exit:%s,%s,\n guards:%s,\n"%(n,wake,OPQ.get(n,'#'),HTS.get(n,"{'#':46,'C':22,'X':40}"),json.dumps([round(v,9) for v in st.H(n)]),json.dumps(M),ops,ex,tgt,G[n])
        s=s[:a]+blk[:i]+new+blk[j:]+s[b:]
        shutil.copy('x/bg%d.jpg'%n,'/home/claude/silent_six/public/bg%d.jpg'%n)
    io.open(p,'w',encoding='utf8').write(s)
if __name__=='__main__':
    import sys;install([int(a) for a in sys.argv[1:]])
