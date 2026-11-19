import mk,g,seg,json,math
M=[r[:] for r in mk.M]
def put(x,y,ch):M[y][x]=ch
for x in (1,2,3,4):put(x,10,'#')          # H from the outer wall
put(5,16,'.')                             # room entrance two cells wide
for (x,y) in [(5,1),(6,1),(7,1),(9,1),(5,7),(11,5),(12,5),(15,2),(16,1),(18,1),(2,12),(2,13),(2,15),(2,16),(3,11),(6,13),(6,14),(9,9),(10,9),(16,13),(16,14),(16,10),(16,11),(18,9),(9,19),(11,19),(10,16)]:
    assert M[y][x]=='.',(x,y,M[y][x]);put(x,y,'C')
for y in (11,12,13,14):
    for x in (8,9,10,11):
        if M[y][x]=='.' and not (y>=13 and x==11):put(x,y,'C')
put(16,2,'X');put(13,1,'K')
MAP=[''.join(r) for r in M]
if __name__=='__main__':
    print('\n'.join(MAP));json.dump({'MAP':MAP,'proj':[float(v) for v in g.H]},open('fin.json','w'))
    mk.render('f',MAP,S=1,lab=False)
