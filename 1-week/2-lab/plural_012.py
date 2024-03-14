#!/usr/bin/env python3

import sys

consonants = "bcdfghjklmnpqrstvwxyz"
endings = ["ch", "sh", "x", "s", "z", "y", "f", "fe", "o"]

def getEnding(word):
    if word[-1] in endings:
        return word[-1]
    elif word[-2:] in endings:
        return word[-2:]

    return ""

for word in sys.stdin:
    word = word.strip()
    ending = getEnding(word)
    
    if ending == "":
        print(word + "s")
    elif ending == "o":
        print(word + "es")
    elif ending == "f" or ending == "fe":
        print(word[:-(len(ending))] + "ves")
    elif ending == "y":
        if word[-2] in consonants:
            print(word[:-1] + "ies")
        else:
            print(word + "s")
    else:
        print(word + "es")
