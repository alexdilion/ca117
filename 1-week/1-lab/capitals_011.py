#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.rstrip()
    print(line[:-1].capitalize() + line[-1].upper())
