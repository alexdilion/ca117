#!/usr/bin/env python3

import sys

speeds = []
prevTime, prevDistance = 0, 0
for line in sys.stdin.readlines()[1:]:
    newTime, newDistance = [int(v) for v in line.split()]
    speed = (newDistance - prevDistance) / (newTime - prevTime)
    speeds.append(speed)
    prevTime, prevDistance = newTime, newDistance

print(int(max(speeds)))
