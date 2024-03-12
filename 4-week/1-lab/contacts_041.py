#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    data = f.read().strip().split("\n")
    contacts = {}

    for contact in data:
        name, phone = contact.split()
        contacts[name] = phone

for name in sys.stdin:
    name = name.rstrip()
    print(f"Name: {name.rstrip()}")
    print(f"Phone: {contacts[name]}" if name in contacts else "No such contact")
