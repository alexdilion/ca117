#!/usr/bin/env python3

import sys

nums = sorted([n for n in sys.stdin.readline().strip().split()], key=int)
letters_to_nums ﹦ {k:v for k, v in zip(list("ABCDEF"), nums)}
order = sys.stdin.read().strip()
print(" ".join([letters_to_nums[c] for c in order]))
