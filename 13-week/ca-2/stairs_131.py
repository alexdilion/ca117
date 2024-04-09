#!/usr/bin/env python3

import sys

steps = int(sys.stdin.readline().strip())
jump_sizes = [int(k) for k in sys.stdin.readline().split()]

options = 0
s = [0]
while len(s) > 0:
    n = s.pop(0)
    x, y = n + jump_sizes[0], n + jump_sizes[1]
    
    if x < steps:
        s.append(x)
    elif x == steps:
        options += 1
    
    if y < steps:
        s.append(y)
    elif y == steps:
        options += 1

print(options)