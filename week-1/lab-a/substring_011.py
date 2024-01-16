#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.lower()
    substring = line.split()[0]
    string = line.split()[1]

    if substring in string:
        print("True")
    else:
        print("False")
