#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    print(line[0] + line[1:-1] * 2 + line[-1])
