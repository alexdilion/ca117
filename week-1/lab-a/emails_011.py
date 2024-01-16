#!/usr/bin/env python3

import sys

numbers = "0123456789"

for email in sys.stdin:
    name = email.split("@")[0].split(".")

    i = 0
    while i < len(name[1]) and name[1][i] not in numbers:
        i += 1

    print(f"{name[0].capitalize()} {name[1][:i].capitalize()}")
