#!/usr/bin/python3
import sys

def gen_dict(a=1,b=100):
        dict = {}
        for i in range(a, b+1):
            dict[str(i)] = 0
        return dict

stable = gen_dict()

for f in sys.argv[1:]:
    with open(f, 'r') as g:
        for l in g:
            l = l.split(' ')
            lv = int((l[1]).strip('\n'))
            stable[l[0]] = stable[l[0]] + lv
    
for key, value in stable.items():
    print(key, value)
