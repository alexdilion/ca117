#!/usr/bin/env python3

import sys

def sumDigits(num):
    sum = 0
    for c in str(num):
        sum += int(c)

    return sum

n = int(sys.stdin.read())
while True:
    if not n % sumDigits(n):
        break

    n += 1

print(n)