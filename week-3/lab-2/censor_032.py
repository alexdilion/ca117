#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    censored_words = f.read().strip().split()

text = sys.stdin.read()
for word in censored_words:
    text = text.replace(word, len(word) * "@")

print(text.rstrip())