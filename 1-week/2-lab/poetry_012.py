#!/usr/bin/env python3

import sys

lines = sys.stdin.read().strip().split("\n")
maxLength = 0

for line in lines:
    if len(line) > maxLength:
        maxLength = len(line)

for line in lines:
    print(f"{line:^{maxLength}}")
