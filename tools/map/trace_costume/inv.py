import sys,numpy as np,ov
a=sys.argv[1];H=ov.H_of(a);Hi=np.linalg.inv(H)
pts=[tuple(map(float,p.split(','))) for p in sys.argv[2:]]
for x,y in pts:
    p=Hi@np.array([x,y,1.0]);print('(%d,%d) -> %.1f, %.1f'%(x,y,p[0]/p[2],p[1]/p[2]))
