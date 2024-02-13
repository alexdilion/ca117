#!/usr/bin/env python3

import sys

maxCapacity = int(sys.stdin.readline())
totalPeople = 0
deniedEntry = 0

for group in sys.stdin:
    tokens = group.strip().split()
    isLeaving, size = tokens[0] == "leave", int(tokens[1])

    if isLeaving:
        totalPeople -= size
    elif totalPeople + size <= maxCapacity:
        totalPeople += size
    else:
        deniedEntry += 1

print(deniedEntry)
