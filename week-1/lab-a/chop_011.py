#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.rstrip()
    if len(line) > 2:
        print(line[1:-1])
