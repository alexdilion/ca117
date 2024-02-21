#!/usr/bin/env python3

import sys

for line in sys.stdin:
    start, end = line.strip().split("tiger")
    
    if start.count("|") == end.count("|"):
        print("safe")
    else:
        print("unsafe")