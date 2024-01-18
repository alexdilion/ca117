#!/usr/bin/env python3

import sys

numbers = "0123456789"
for email in sys.stdin:
    firstName, surname = email.split("@")[0].split(".")

    i = 0
    while i < len(surname) and surname[i] not in numbers:
        i += 1

    print(f"{firstName.capitalize()} {surname[:i].capitalize()}")
