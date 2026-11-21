import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib, zoom
SZ = dict(raven1=26, raven2=24, raven3=30, viper1=28, viper2=24, viper3=28, glitch1=24, glitch2=28, glitch3=28, brick1=24, brick2=26, brick3=28, mirage1=30, mirage2=26, mirage3=26, doc1=24, doc2=28, doc3=30)
NC = json.load(open(os.path.join(lib.OUT, 'near_corners.json'))); AC = json.load(open(os.path.join(lib.OUT, 'auto_corners.json'))); TP = json.load(open(os.path.join(lib.OUT, 'top.json')))
def corners(k, h=40):
    T, R, L, B = NC[k]; B = AC[k]['B']
    T = (TP[k][0], TP[k][1] + h)
    return [tuple(round(v) for v in p) for p in (T, R, L, B)]
FIX = {}
if __name__ == '__main__':
    for a in sys.argv[1:]:
        f = a.split(':'); k = f[0]; lift = int(f[1]) if len(f) > 1 and f[1] else 40
        pts = corners(k, lift)
        if len(f) > 2: pts = [tuple(float(v) for v in p.split(',')) for p in f[2].split('/')]
        print(k, SZ[k], pts)
        zoom.run(k, SZ[k], SZ[k], pts, s=1.25, lift=lift, tag='zl')
