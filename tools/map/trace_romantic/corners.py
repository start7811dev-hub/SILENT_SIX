import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
out = {}
for ag in lib.AG:
    for t in (1, 2, 3):
        k = '%s%d' % (ag, t)
        T, R, L, B = lib.auto_corners(os.path.join(lib.SRC, 'bgp_%s_%d.jpg' % (ag, t)))
        out[k] = dict(T=T, R=R, L=L, B=B)
        print(k, 'T(%.0f,%.0f) R(%.0f,%.0f) L(%.0f,%.0f) B(%.0f,%.0f)' % (T + R + L + B))
json.dump(out, open(os.path.join(lib.OUT, 'auto_corners.json'), 'w'))
