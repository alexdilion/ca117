#!/usr/bin/env python3

import sys

text = sys.stdin.read().lower()
vowelCount = {}
for vowel in "aeiou":
    vowelCount[vowel] = text.count(vowel)

maxWidth = len(str(max(vowelCount.values())))
for vowel in sorted(vowelCount, key=lambda k: vowelCount[k], reverse=True):
    print(f"{vowel} : {vowelCount[vowel]:{maxWidth}}")