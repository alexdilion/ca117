#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = [c for c in line.lower() if c.isalnum()]
    mid = len(line) // 2
    print(line[:mid] == line[::-1][:mid])