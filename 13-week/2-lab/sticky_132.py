#!/usr/bin/env python3

import sys

line1 = "".join(sys.stdin.readline().split())
line2 = "".join(sys.stdin.readline().split())

output = ""
for l in set(line1):
    if line1.count(l) - line2.count(l) != 0:
        output += l

print("".join(sorted(output)))