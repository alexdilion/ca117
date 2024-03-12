#!/usr/bin/env python3

import sys

words = "zero one two three four five six seven eight nine ten"
num_map = {str(i):v for i, v in enumerate(words.split())}
word_map = {}

with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")
    for l in lines:
        k, v = l.split()
        word_map[k] = v
        
for line in sys.stdin:
    line = line.strip()
    print(" ".join([word_map[num_map[n]] for n in line.split()]))
