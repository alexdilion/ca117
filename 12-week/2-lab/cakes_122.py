#!/usr/bin/env python3

import sys

for line in sys.stdin:
    prices = sorted([int(n) for n in line.split()])[::-1]
    print(sum(prices) - sum(prices[2::3]))