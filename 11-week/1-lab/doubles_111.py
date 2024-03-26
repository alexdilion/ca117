#!/usr/bin/env python3

import sys

vowels = "aeiou"

def countDoubleVowels(s):
    i = 0
    count = 0
    while i < len(s) - 1:
        if s[i] in vowels and s[i] == s[i + 1]:
            count += 1
            i += 1

        i += 1
    
    return count

word = ""
maxCount = 0
for line in sys.stdin:
    line = line.strip()
    
    currCount = countDoubleVowels(line)
    if currCount > maxCount:
        word = line
        maxCount = currCount

print(word)
