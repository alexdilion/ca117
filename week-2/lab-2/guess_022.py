#!/usr/bin/env python3

import sys

lines = sys.stdin.read().strip().split("\n")
correctNumber = int(lines[-2])

guessLines = lines[:-2]
guesses = []
for i in range(len(guessLines) // 2):
    guesses.append((int(guessLines[i * 2]), guessLines[i * 2 + 1]))

isConsistent = True
for guess in guesses:
    if guess[0] < correctNumber and guess[1] != "higher":
        isConsistent = False
    elif guess[0] > correctNumber and guess[1] != "lower":
        isConsistent = False
    elif guess[0] == correctNumber:
        isConsistent = False

print("Bert can be trusted" if isConsistent else "Bert is not to be trusted")
