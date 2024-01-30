#!/usr/bin/env python3

import sys

words = sys.stdin.read().strip().split("\n")

def isAnagram(w, t):
    return w != t and sorted([*w]) == sorted([*t])

length_17 = [w for w in words if len(w) == 17]
length_18_plus = [w for w in words if len(w) >= 18]
contains_4_as = [w for w in words if w.lower().count("a") == 4]
contains_2_plus_qs = [w for w in words if w.lower().count("q") >= 2]
contains_cie = [w for w in words if "cie" in w.lower()]
anagrams_of_angle = [w for w in words if isAnagram(w.lower(), "angle")]

print(f"""Words containing 17 letters: {length_17}
Words containing 18+ letters: {length_18_plus}
Words with 4 a's: {contains_4_as}
Words with 2+ q's: {contains_2_plus_qs}
Words containing cie: {contains_cie}
Anagrams of angle: {anagrams_of_angle}""")