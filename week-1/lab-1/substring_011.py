#!/usr/bin/env python3

import sys

for line in sys.stdin:
    substring, string = line.strip().lower().split()
    print(substring in string)
