#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print(f'Use: {sys.argv[0]} FILE')

n = 0
with open(sys.argv[1], 'r') as f:
    for l in f:
        l = l.split(' ')
        n += int(l[1])

print(f'n = {n}')
