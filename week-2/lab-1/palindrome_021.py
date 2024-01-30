#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = [c for c in line.lower() if c.isalnum()]
    print(line == line[::1])