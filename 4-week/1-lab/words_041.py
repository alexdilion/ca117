#!/usr/bin/env python3

import sys
import string

words = sys.stdin.read().lower().strip().split()
wordCount = {}

for word in words:
    word = word.strip(string.punctuation)

    if word not in wordCount:
        wordCount[word] = 0

    wordCount[word] += 1

for word in sorted(wordCount.keys()):
    print(f"{word} : {wordCount[word]}")
