#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.lower().rstrip().split()
    chars = line[0]
    word = line[1]

    for char in word:
        if char in chars:
            chars = chars.replace(char, "", 1)

    print(chars == "")
