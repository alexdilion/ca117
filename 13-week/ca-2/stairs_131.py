#!/usr/bin/env python3

import sys

steps = int(sys.stdin.readline().strip())
jump_sizes = [int(k) for k in sys.stdin.readline().split()]

def count_ways(curr_value = 0):
    if curr_value > steps:
        return 0
    elif curr_value == steps:
        return 1
    
    if len(jump_sizes) == 1:
        return count_ways(curr_value + jump_sizes[0])
    else:
        return count_ways(curr_value + jump_sizes[0]) + count_ways(curr_value + jump_sizes[1])

print(count_ways())

# Old method
# Forgot to account for a single jump being supplied (so got index errors there)
# This also used BFS which was really inefficient and caused a timeout on one of the larger tests

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