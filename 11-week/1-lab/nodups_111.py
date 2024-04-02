#!/usr/bin/env python3

import sys

def getLetters(s):
    letters = [c for c in s if c.isalpha()]
    return "".join(letters)

seen = set()
for line in sys.stdin:
    words = line.split()
    output = []
    
    for word in words:
        letters = getLetters(word).lower()

        if letters in seen:
            output.append(".")
        else:
            output.append(word)
            seen.add(letters)

    print(" ".join(output))
