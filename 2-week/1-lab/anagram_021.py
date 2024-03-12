#!/usr/bin/env python3

import sys

# short and simple solution
for line in sys.stdin:
    w1, w2 = line.split()
    print(sorted([*w1]) == sorted([*w2]))

# # Solution without sorted function
# for line in sys.stdin:
#     w1, w2 = line.split()
#     charCounts = [{}, {}]

#     for c in w1:
#         if c not in charCounts[0]:
#             charCounts[0][c] = 0
        
#         charCounts[0][c] += 1

#     for c in w2:
#         if c not in charCounts[1]:
#             charCounts[1][c] = 0
        
#         charCounts[1][c] += 1

#     print(charCounts[0] == charCounts[1])
