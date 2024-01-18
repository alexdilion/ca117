#!/usr/bin/env python3

import sys

waterLeft = int(sys.stdin.readline())
buckets = [int(v) for v in sys.stdin.read().split()]

i = 0
while i < len(buckets) and waterLeft - buckets[i] >= 0:
    waterLeft -= buckets[i]
    i += 1

print(i)