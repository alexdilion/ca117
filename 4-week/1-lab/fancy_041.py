#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    data = f.read().strip().split("\n")
    contacts = {}

    for contact in data:
        name, phone, email = contact.split()
        contacts[name] = [phone, email]

for name in sys.stdin:
    name = name.rstrip()
    print(f"Name: {name}")

    if name in contacts:
        print(f"Phone: {contacts[name][0]}")
        print(f"Email: {contacts[name][1]}")
    else:
        print("No such contact")
