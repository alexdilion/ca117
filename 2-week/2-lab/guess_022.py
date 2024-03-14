#!/usr/bin/env python3

import sys

lines = sys.stdin.read().strip().split("\n")
correctNumber = int(lines[-2])

guessNumbers = [int(v) for v in lines[:-2] if v.isdigit()]
higherOrLower = [v for v in lines[:-2] if not v.isdigit()]

isConsistent = True
for i, guess in enumerate(guessNumbers):
    if guess < correctNumber and higherOrLower[i] != "higher":
        isConsistent = False
    elif guess > correctNumber and higherOrLower[i] != "lower":
        isConsistent = False
    elif guess == correctNumber:
        isConsistent = False

print("Bert can be trusted" if isConsistent else "Bert is not to be trusted")
