#!/usr/bin/env python3

import sys

def decode(s):
    message = ""
    i = 0
    while i < len(s):
        if s[i] in "aeiou":
            message += s[i]
            i += 2
        else:
            message += s[i]

        i += 1

    return message

for line in sys.stdin:
    line = line.strip()
    print(decode(line))
