#!/usr/bin/env python3

import sys

pieces = [2, 2, 4, 4, 4, 16]

for line in sys.stdin:
    given = [int(n) for n in line.split()]
    output = [str(pieces[i] - given[i]) for i in range(6)]
    print(" ".join(output))