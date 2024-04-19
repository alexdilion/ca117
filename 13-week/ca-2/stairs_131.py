#!/usr/bin/env python3

import sys

steps = int(sys.stdin.readline().strip())
jump_sizes = [int(k) for k in sys.stdin.readline().split()]

def count_ways(curr_value):
    if curr_value > steps:
        return 0
    elif curr_value == steps:
        return 1
    
    if len(jump_sizes) == 1:
        return count_ways(curr_value + jump_sizes[0])
    else:
        return count_ways(curr_value + jump_sizes[0]) + count_ways(curr_value + jump_sizes[1])

print(count_ways(0))

# Old method
# Failed a couple of test -> didn't account for there being only one jump (so got index errors there)
# Also used BFS which is pretty inefficient since we only care about the nodes at the end of the tree

# options = 0
# s = [0]
# while len(s) > 0:
#     n = s.pop(0)
#     x, y = n + jump_sizes[0], n + jump_sizes[1]
    
#     if x < steps:
#         s.append(x)
#     elif x == steps:
#         options += 1
    
#     if y < steps:
#         s.append(y)
#     elif y == steps:
#         options += 1

# print(options)