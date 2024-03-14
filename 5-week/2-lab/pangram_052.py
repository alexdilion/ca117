#!/usr/bin/env python3

import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"

for line in sys.stdin:
    missing = [c for c in alphabet if line.lower().count(c) == 0]
    print("pangram" if not missing else f"missing {''.join(missing)}")
