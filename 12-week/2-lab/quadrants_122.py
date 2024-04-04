#!/usr/bin/env python3

import sys

quadrants = {
    (True, True): 1,
    (True, False): 2,
    (False, False): 3,
    (False, True): 4,
}

for line in sys.stdin:
    x, y = [int(n) for n in line.split()]
    quadrant = (x > 0, y > 0)

    print(quadrants[quadrant])
