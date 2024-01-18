#!/usr/bin/env python3

import sys

for line in sys.stdin:
    chars, word = line.lower().rstrip().split()

    for char in word:
        if char in chars:
            chars = chars.replace(char, "", 1)

    print(chars == "")
