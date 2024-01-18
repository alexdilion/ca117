#!/usr/bin/env python3

import sys

def checkPassword(password):
    charTypes = {}

    for char in password:
        if char.isupper():
            charTypes["upper"] = 1
        elif char.islower():
            charTypes["lower"] = 1
        elif char.isdigit():
            charTypes["digit"] = 1
        else:
            charTypes["special"] = 1

    return len(charTypes)

for password in sys.stdin:
    print(checkPassword(password.rstrip()))
