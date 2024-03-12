#!/usr/bin/env python3

import sys

for line in sys.stdin:
    first_m = line.find("m＂)
    start = line[:first_m]
    end = line[first_m:].rstrip()
    word = end.split(" ")[0].capitalize()

    print(start + word + end[len(word):])
