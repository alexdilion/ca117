#!/usr/bin/env python3

import sys

lines = sys.stdin.read().strip().split("\n")[1:]
country, visitNo = lines[-1].split()
lines = [v.split() for v in lines[:-1]]

visits = [int(v[1]) for v in lines if v[0] == country]
print(sorted(visits)[int(visitNo) - 1])
