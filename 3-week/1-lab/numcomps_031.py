#!/usr/bin/env python3

import sys

for n in sys.stdin:
    arr = []
    for i in range(int(n)):
        arr.append(i + 1)

    print(f"Multiples of 3: {[v for v in arr if not v % 3]}")
    print(f"Multiples of 3 squared: {[v * v for v in arr if not v % 3]}")
    print(f"Multiples of 4 doubled: {[v * 2 for v in arr if not v % 4]}")
    print(f"Multiples of 3 or 4: {[v for v in arr if not (v % 3 and v % 4)]}")
    print(f"Multiples of 3 and 4: {[v for v in arr if not (v % 3 or v % 4)]}")
