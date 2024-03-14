#!/usr/bin/env python3

import sys

words = "zero one two three four five six seven eight nine ten"
num_map = {str(k):v for k, v in enumerate(words.split())}

def convertToWord(n):
    return n if n in num_map else "unknown"

for line in sys.stdin:
    line = line.strip()
    print(" ".join([convertToWord(n) for n in line.split()]))
