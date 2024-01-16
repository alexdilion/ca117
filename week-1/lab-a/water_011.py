#!/usr/bin/env python3

import sys

waterAmount = int(sys.stdin.readline().strip())
buckets = [int(x) for x in sys.stdin.read().split()]

i = 0
while i < len(buckets) and waterAmount - buckets[i] >= 0:
    waterAmount -= buckets[i]
    i += 1

print(i)
