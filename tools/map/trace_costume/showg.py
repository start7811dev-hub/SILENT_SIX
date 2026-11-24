import json,sys
a=sys.argv[1];M=json.load(open('/home/claude/cw/work/map_%s.json'%a))['MAP']
print('   '+''.join(str(i//10) for i in range(len(M[0]))));print('   '+''.join(str(i%10) for i in range(len(M[0]))))
for y,r in enumerate(M): print('%2d %s'%(y,r))
