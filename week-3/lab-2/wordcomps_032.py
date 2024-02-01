#!/usr/bin/env python3

import sys

def contains(word, letters):
    for c in letters:
        if c not in word:
            return False

    return True

def getECount(word):
    return word.lower().count("e")

words = sys.stdin.read().strip().split()
has_all_vowels = [w for w in words if contains(w.lower(), "aeiou")]
print(f"Shortest word containing all vowels: {min(has_all_vowels, key=len)}")

words_ending_in_iary = [w for w in words if w.lower().endswith("iary")]
print(f"Words ending in iary: {len(words_ending_in_iary)}")

words_with_es = [w for w in words if "e" in w.lower()]
max_es = max(words_with_es, key=getECount).count("e")
print(f"Words with most e's: {[w for w in words_with_es if w.count('e') == max_es]}")