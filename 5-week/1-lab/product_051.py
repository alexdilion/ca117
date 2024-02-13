#!/usr/bin/env python3

import sys

x = int(sys.stdin.read().strip())
y = x
while y >= 10:
    nonZeroDigits = [int(d) for d in str(y) if d != "0"]
    y = 1
    for d in nonZeroDigits:
        y *= d

print(y)
