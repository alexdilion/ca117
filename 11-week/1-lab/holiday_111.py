#!/usr/bin/env python3

import sys

temps = [int(n) for n in sys.stdin.read().split()]
pairs = [max(temps[i], temps[i + 2]) for i in range(len(temps) - 2)]
print(pairs.index(min(pairs)) + 1, min(pairs))
