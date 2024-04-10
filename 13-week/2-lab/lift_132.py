#!/usr/bin/env python3

import sys

line = [int(x) for x in sys.stdin.readline().split()]
floors, curr_floor, target, up_amount, down_amount = line

pushes = 0
visited = set([curr_floor])
s = [curr_floor]

while len(s) > 0 and target not in visited:
    curr_level = [n + up_amount for n in s]
    curr_level += [n - down_amount for n in s]

    s = []
    for n in curr_level:
        if n in visited:
            continue
        
        visited.add(n)

        if n >= 0 and n <= floors:
            s.append(n)
    
    pushes += 1

if target in visited:
    print(pushes)
else:
    print("Sorry Sheila!")