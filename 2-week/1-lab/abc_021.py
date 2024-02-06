#!/usr/bin/env python3

import sys

nums = sorted([int(n) for n in sys.stdin.readline().split()])
order = sys.stdin.read().strip()
print(*[nums[ord(c) - ord("A")] for c in order], sep=" ")