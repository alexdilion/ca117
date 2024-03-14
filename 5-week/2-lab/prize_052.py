#!/usr/bin/env python3

import sys

cups = [0, 0, 0]
swaps = {"A": (0, 1), "B": (1, 2), "C": (0, 2)}
cups[int(sys.stdin.readline().strip()) - 1] = 1

for swap in sys.stdin.read().strip():
    c1, c2 = swaps[swap]
    cups[c1], cups[c2] = cups[c2], cups[c1]
    
print(cups.index(1) + 1)
