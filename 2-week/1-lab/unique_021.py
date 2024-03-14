#!/usr/bin/env python3

import sys

text = sys.stdin.read().lower()
words = {}
for word in text.split():
    word = "".join([c for c in word if c.isalnum()])
    
    if word:
        words[word] = 1

print(len(words))
