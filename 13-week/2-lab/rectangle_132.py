#!/usr/bin/env python3

import sys

points = [int(n) for n in sys.stdin.read().split()]
xs, ys = sorted(points[::2]), sorted(points[1::2])
x = xs[0] if xs.count(xs[0]) == 1 else xs[2]
y = ys[0] if ys.count(ys[0]) == 1 else ys[2]

print(x, y)