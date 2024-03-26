#!/usr/bin/env python3

import sys

names = sys.stdin.read().strip().split("\n")
sortedNames = names[0::2] + names[1::2][::-1]

print("\n".join(sortedNames))
