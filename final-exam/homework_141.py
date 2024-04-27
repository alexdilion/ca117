#!/bin/env python3

import sys

homework = sys.stdin.read().strip().split(";")

total = 0
for entry in homework:
    if "-" in entry:
        n, m = [int(x) for x in entry.split("-")]
        total += m - n + 1
    else:
        total += 1

print(total)