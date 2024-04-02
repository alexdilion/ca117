#!/usr/bin/env python3

import sys

for word in sys.stdin:
    word = word.strip()
    letters = set(word)
    simplicity = len(letters)
    
    if simplicity <= 2:
        print(0)
    else:
        letter_counts = sorted([word.count(l) for l in letters])
        deletions = sum(letter_counts[:-2])
        print(deletions)
