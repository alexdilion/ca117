#!/usr/bin/env python3

import sys

for n in sys.stdin:
    multiples_of_3 = [0 if (v + 1) % 3 else v + 1 for v in range(int(n))]
    print(f"Non-multiples of 3 replaced: {multiples_of_3}")
