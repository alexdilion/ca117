#!/usr/bin/env python3

import sys

for line in sys.stdin:
    nums = [int(n) for n in line.strip().split()]
    uniqueNums = [n for n in nums if nums.count(n) == 1]
    print(max(uniqueNums) if uniqueNums else "none")
